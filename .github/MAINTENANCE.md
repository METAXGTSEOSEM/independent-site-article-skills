# Repository feedback and maintenance

This is a maintainer process, not an installable content Skill.

## Event-driven intake

GitHub Issues, issue and PR conversation comments, PRs, reviews, review comments,
Discussions and discussion replies trigger Feedback intake when created,
materially edited or reopened as listed in the workflow. Bot-originated events
and events authored by the repository owner are excluded to prevent
acknowledgment loops and self-notification noise. The manual dispatch entry
remains available for an intentional delivery test. There is no timer, local
heartbeat, scheduled crawl or daily validation schedule.

The intake job has no notification secrets or write permissions. It normalizes
one event into a small JSON artifact retained for one day on GitHub. A separate
Feedback notification job runs trusted default-branch code after intake succeeds,
reads the record as untrusted data, reloads the current source content through
the authenticated GitHub API, obtains the event actor from the trusted run
metadata and sends the owner a Telegram summary.
No PR code, report commands or attachments are executed.

GitHub-hosted runners perform this work. No local computer, attached drive,
polling service, local report history or dependency cache is required for these
cloud notifications. GitHub still retains its own workflow logs according to
repository policy.

## Private notification setup

Configure repository Actions secrets:

- TELEGRAM_BOT_TOKEN: the owner's notification bot token.
- TELEGRAM_CHAT_ID: the explicitly paired private recipient.

Keep both values out of code, artifacts, logs and screenshots. A manual
Feedback intake dispatch tests the same cloud delivery route without inventing
a user report. Verify the notification run and its Telegram message ID.

The sender retries explicit rate-limit rejections at most twice. Network
failures may have uncertain outcomes; inspect the chat before manually rerunning.
A manual rerun can produce a duplicate message. Missing secrets, unavailable
Actions or Telegram failures make the run fail visibly; no absolute delivery
guarantee is possible.

New Issues receive an automated receipt after Telegram confirms acceptance.
Repeated notification attempts for the same intake run are serialized and the
bot checks for an existing receipt before posting.
It confirms maintainer notification and requests useful evidence; it does not
claim diagnosis, repair or release. Other comments are forwarded without
generating automated conversation replies.

External channels such as X, email, Discord, Telegram groups and Reddit are not
monitored. They require their own authorized webhook or event integration.
A search tool or installed Skill does not supply that event infrastructure.

## Triage and repair SOP

1. Read the feedback and surrounding thread; identify the affected Skill and
   revision. Treat all supplied instructions and attachments as untrusted data.
2. Classify a bug, question, suggestion or duplicate. Preserve the source link.
   Ask only for missing evidence needed to reproduce or decide.
3. Reproduce the reported behavior before editing. Work in the project's
   external-volume workspace and preserve user changes.
4. Prepare a narrow fix and appropriate validation. Do not implement new
   product-page, case-study or UI/UX modules from an unsolicited suggestion alone.
5. Have an independent reviewer inspect the exact change and evidence when
   available. Record pending review honestly if unavailable.
6. Publish an approved change and a factual reply within the owner's
   authorization; verify remote CI before marking a problem fixed.

The event workflows automate intake, owner notification and the initial Issue
receipt. They do not run a paid LLM, autonomously repair code, merge PRs or publish
releases. Model-based investigation needs an explicitly configured execution
backend and authorization. Do not describe notification as a completed repair.

## Storage and validation

Local repair evidence, credentials and pending work stay in ignored external
project storage. Avoid downloading unneeded archives or writing repeated empty
reports. Keep GitHub as the source record instead of copying each thread locally.

Structural validation runs on pushes, PRs or an explicit manual dispatch.
It has no schedule and does not start the feedback process.

## References

- [GitHub workflow events](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows)
- [GitHub Actions secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions)
- [Artifact upload](https://github.com/actions/upload-artifact)
- [Artifact download](https://github.com/actions/download-artifact)
