import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path


EVENTS = {
    "issues", "issue_comment", "discussion", "discussion_comment",
    "pull_request_target", "pull_request_review", "pull_request_review_comment",
    "workflow_dispatch"
}


class FeedbackError(Exception):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        return None


def request_json(url, payload=None, token=None):
    headers = {"Accept": "application/json", "User-Agent": "wordpress-content-skills"}
    if token:
        headers["Authorization"] = "Bearer " + token
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"
    for attempt in range(3):
        request = urllib.request.Request(url, data=data, headers=headers)
        try:
            with urllib.request.build_opener(NoRedirect).open(request, timeout=20) as response:
                return json.load(response)
        except urllib.error.HTTPError as error:
            if error.code == 429 and attempt < 2:
                try:
                    delay = int(error.headers.get("Retry-After", "5"))
                except ValueError:
                    delay = 5
                time.sleep(min(max(delay, 1), 15))
                continue
            raise FeedbackError("Service rejected request (HTTP " + str(error.code) + ").") from None
        except (urllib.error.URLError, OSError, ValueError):
            raise FeedbackError("Network or response failure; delivery may be uncertain. Inspect the chat before rerunning.") from None
    raise FeedbackError("Request attempt limit reached.")


def trusted_url(value, repository):
    if not isinstance(value, str) or len(value) > 1200 or not value.startswith("https://github.com/" + repository + "/"):
        raise FeedbackError("Feedback URL does not belong to this repository.")
    return value


def capture(payload, event_name, repository, run_id):
    if event_name not in EVENTS or payload.get("repository", {}).get("full_name") != repository:
        raise FeedbackError("Unexpected feedback event or repository.")
    sender = payload.get("sender", {})
    if sender.get("type") == "Bot":
        raise FeedbackError("Bot-generated feedback is excluded.")
    actor = sender.get("login", os.environ.get("GITHUB_ACTOR", ""))
    if not re.fullmatch(r"[A-Za-z0-9-]{1,100}", actor):
        raise FeedbackError("Invalid actor identity.")
    item = payload.get("issue") or payload.get("pull_request") or payload.get("discussion") or {}
    detail = payload.get("comment") or payload.get("review") or item
    if event_name == "workflow_dispatch":
        title = "Manual Telegram delivery test"
        body = "This is a connection test, not a user feedback report."
        url = "https://github.com/" + repository + "/actions/runs/" + str(run_id)
        number = None
    else:
        title = str(item.get("title", ""))[:240]
        body = str(detail.get("body") or "")[:1000]
        url = trusted_url(detail.get("html_url") or item.get("html_url"), repository)
        number = item.get("number")
        if type(number) is not int or number <= 0:
            raise FeedbackError("Missing feedback item number.")
    material = {
        "repository": repository, "event": event_name,
        "action": payload.get("action", "manual"),
        "native_id": detail.get("id", run_id),
        "updated_at": detail.get("updated_at") or detail.get("submitted_at"),
        "title": title, "body": body
    }
    event_key = hashlib.sha256(json.dumps(material, sort_keys=True).encode()).hexdigest()[:20]
    return {
        "schema_version": 1, "source_run_id": str(run_id),
        "repository": repository, "event": event_name,
        "action": material["action"], "event_key": event_key,
        "native_id": detail.get("id"),
        "node_id": detail.get("node_id"),
        "actor": actor, "number": number, "title": title,
        "body": body, "url": trusted_url(url, repository)
    }


def validate_record(record, trigger, repository):
    source = trigger.get("workflow_run", {})
    if trigger.get("repository", {}).get("full_name") != repository:
        raise FeedbackError("Unexpected notification repository.")
    if source.get("name") != "Feedback intake" or source.get("conclusion") != "success":
        raise FeedbackError("A successful feedback intake run is required.")
    if record.get("schema_version") != 1 or record.get("repository") != repository:
        raise FeedbackError("Unexpected feedback record schema or repository.")
    if record.get("source_run_id") != str(source.get("id")):
        raise FeedbackError("Feedback record does not match its source run.")
    if record.get("event") not in EVENTS or record["event"] != source.get("event"):
        raise FeedbackError("Feedback event does not match its source run.")
    if record["event"] in {"pull_request_review", "pull_request_review_comment"}:
        source_prs = source.get("pull_requests") or []
        if not any(item.get("number") == record.get("number") for item in source_prs):
            raise FeedbackError("Review does not match the PR associated with the source run.")
    for key, limit in [("title", 240), ("body", 1000), ("actor", 100), ("action", 40)]:
        if not isinstance(record.get(key), str) or len(record[key]) > limit:
            raise FeedbackError("Invalid bounded feedback field: " + key)
    if not re.fullmatch(r"[a-f0-9]{20}", record.get("event_key", "")):
        raise FeedbackError("Invalid feedback event key.")
    if record["event"] != "workflow_dispatch":
        if type(record.get("number")) is not int or record["number"] <= 0:
            raise FeedbackError("Invalid feedback item number.")
        if type(record.get("native_id")) is not int or record["native_id"] <= 0:
            raise FeedbackError("Invalid native feedback ID.")
    trusted_url(record.get("url"), repository)


def refresh_source(record, trigger, github_token):
    if record["event"] == "workflow_dispatch":
        return record
    if not github_token:
        raise FeedbackError("GitHub token unavailable for source verification.")
    repository = record["repository"]
    number = str(record["number"])
    native_id = str(record["native_id"])
    endpoint = "https://api.github.com/repos/" + repository
    event = record["event"]
    if event.startswith("discussion"):
        node_id = record.get("node_id")
        if not isinstance(node_id, str) or not 1 <= len(node_id) <= 200:
            raise FeedbackError("Discussion node ID is unavailable.")
        query = (
            "query($id:ID!){node(id:$id){__typename id "
            "... on Discussion{number title body url author{login} repository{nameWithOwner}}"
            "... on DiscussionComment{body url author{login} discussion{number title repository{nameWithOwner}}}"
            "}}"
        )
        result = request_json("https://api.github.com/graphql", {"query": query, "variables": {"id": node_id}}, token=github_token)
        item = (result.get("data") or {}).get("node") or {}
        expected_type = "Discussion" if event == "discussion" else "DiscussionComment"
        if item.get("id") != node_id or item.get("__typename") != expected_type:
            raise FeedbackError("Discussion node identity or event type does not match.")
        parent = item.get("discussion", item)
        if parent.get("repository", {}).get("nameWithOwner") != repository or parent.get("number") != record["number"]:
            raise FeedbackError("Discussion source does not match the repository and item.")
        title, body, url = parent.get("title", ""), item.get("body", ""), item.get("url")
    else:
        if event == "issues":
            route = "/issues/" + number
        elif event == "issue_comment":
            route = "/issues/comments/" + native_id
        elif event == "pull_request_target":
            route = "/pulls/" + number
        elif event == "pull_request_review":
            route = "/pulls/" + number + "/reviews/" + native_id
        else:
            route = "/pulls/comments/" + native_id
        item = request_json(endpoint + route, token=github_token)
        if item.get("id") != record["native_id"]:
            raise FeedbackError("Native feedback ID does not match GitHub.")
        if event == "issue_comment" and item.get("issue_url") != endpoint + "/issues/" + number:
            raise FeedbackError("Comment does not belong to the expected issue.")
        if event == "pull_request_review_comment" and item.get("pull_request_url") != endpoint + "/pulls/" + number:
            raise FeedbackError("Review comment does not belong to the expected PR.")
        parent = item
        if event in {"issue_comment", "pull_request_review", "pull_request_review_comment"}:
            parent = request_json(endpoint + "/issues/" + number, token=github_token)
        title, body, url = parent.get("title", ""), item.get("body", ""), item.get("html_url")
    actor = trigger["workflow_run"].get("actor", {}).get("login")
    if not isinstance(actor, str) or not re.fullmatch(r"[A-Za-z0-9-]{1,100}", actor):
        raise FeedbackError("Verified workflow actor is unavailable.")
    return dict(
        record, actor=actor, title=str(title)[:240], body=str(body or "")[:1000],
        url=trusted_url(url, repository)
    )


def acknowledge(record, github_token):
    if record["event"] != "issues" or record["action"] != "opened":
        return "not_applicable"
    if not github_token:
        raise FeedbackError("GitHub token unavailable for issue acknowledgment.")
    endpoint = "https://api.github.com/repos/" + record["repository"] + "/issues/" + str(record["number"]) + "/comments"
    marker = "<!-- feedback-received:" + str(record["number"]) + " -->"
    for page in range(1, 21):
        comments = request_json(endpoint + "?per_page=100&page=" + str(page), token=github_token)
        if any(
            marker in comment.get("body", "") and comment.get("user", {}).get("type") == "Bot"
            for comment in comments
        ):
            return "already_acknowledged"
        if len(comments) < 100:
            break
    else:
        raise FeedbackError("Acknowledgment history exceeded its bounded page limit.")
    body = (
        marker + "\nThanks for the feedback. The maintainer has been notified "
        "and this report is awaiting review.\n\n"
        "For a bug, please include the Skill version, the request you used, "
        "expected behavior, and a redacted example. For an idea, describe "
        "the workflow and intended result. Do not include credentials or private customer data.\n\n"
        "This is an automated receipt, not a diagnosis or a promise that a fix has shipped."
    )
    response = request_json(endpoint, {"body": body}, token=github_token)
    if not response.get("id"):
        raise FeedbackError("Issue acknowledgment was not confirmed.")
    return "acknowledged"


def notify(record, trigger, repository, environment):
    validate_record(record, trigger, repository)
    token = environment.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = environment.get("TELEGRAM_CHAT_ID", "")
    if not token or not re.fullmatch(r"-?[0-9]+", chat_id):
        raise FeedbackError("Required Telegram repository secrets are missing.")
    record = refresh_source(record, trigger, environment.get("GITHUB_TOKEN", ""))
    text = (
        "\u6536\u5230 GitHub \u53cd\u9988\n"
        + repository + "\n"
        + record["event"] + " / " + record["action"] + "\n"
        + record["title"] + "\n"
        + "\u63d0\u4ea4\u8005: @" + record["actor"] + "\n\n"
        + record["body"] + "\n\n"
        + record["url"] + "\n"
        + "\u72b6\u6001: \u5f85\u5ba1\u6838\uff0c\u5c1a\u672a\u81ea\u52a8\u4fee\u590d\n"
        + "Event: " + record["event_key"]
    )
    text = text.replace(token, "[redacted]")
    response = request_json(
        "https://api.telegram.org/bot" + token + "/sendMessage",
        {"chat_id": chat_id, "text": text, "link_preview_options": {"is_disabled": True}}
    )
    message = response.get("result", {})
    if not response.get("ok") or str(message.get("chat", {}).get("id")) != chat_id or not message.get("message_id"):
        raise FeedbackError("Telegram delivery was not confirmed.")
    print("Telegram accepted message ID " + str(message["message_id"]) + " for event " + record["event_key"] + ".")
    ack_status = acknowledge(record, environment.get("GITHUB_TOKEN", ""))
    print("Issue receipt: " + ack_status + ". No code repair, merge or release performed.")
    return message["message_id"], ack_status


def main():
    parser = argparse.ArgumentParser(description="Event-driven repository feedback routing.")
    parser.add_argument("mode", choices=["capture", "notify"])
    parser.add_argument("--record", required=True, type=Path)
    arguments = parser.parse_args()
    try:
        trigger = json.loads(Path(os.environ["GITHUB_EVENT_PATH"]).read_text())
        repository = os.environ["GITHUB_REPOSITORY"]
        if arguments.mode == "capture":
            record = capture(trigger, os.environ["GITHUB_EVENT_NAME"], repository, os.environ["GITHUB_RUN_ID"])
            arguments.record.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
            print("Captured one feedback event. No secrets, code execution, cache or repair state used.")
        else:
            if arguments.record.is_symlink() or arguments.record.stat().st_size > 16000:
                raise FeedbackError("Invalid feedback artifact size or link.")
            record = json.loads(arguments.record.read_text())
            notify(record, trigger, repository, os.environ)
        return 0
    except (FeedbackError, OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        message = str(error) if isinstance(error, FeedbackError) else "Invalid event data or unavailable runtime input."
        print("Feedback routing failed: " + message, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
