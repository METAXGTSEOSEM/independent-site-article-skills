import argparse
import json
import os
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path


def acquire(state_dir):
    state_dir.mkdir(parents=True, exist_ok=True)
    lock_dir = state_dir / "run.lock"
    try:
        lock_dir.mkdir()
    except FileExistsError:
        return {"status": "busy", "message": "A guard already exists. Do not remove it automatically."}, 2
    owner = {
        "token": str(uuid.uuid4()),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "creator_pid": os.getpid(),
        "note": "The creator is a short-lived helper; PID exit does not mean the maintenance run ended."
    }
    try:
        (lock_dir / "owner.json").write_text(json.dumps(owner, indent=2) + "\n", encoding="utf-8")
    except OSError as write_error:
        try:
            (lock_dir / "owner.json").unlink(missing_ok=True)
            lock_dir.rmdir()
        except OSError as cleanup_error:
            raise OSError(
                f"Guard owner write failed: {write_error}. "
                f"Guard cleanup failed: {cleanup_error}. Inspect {lock_dir} manually."
            ) from write_error
        raise
    return {"status": "acquired", **owner}, 0


def release(state_dir, token):
    lock_dir = state_dir / "run.lock"
    owner_file = lock_dir / "owner.json"
    try:
        owner = json.loads(owner_file.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"status": "blocked", "message": "The guard is missing or unreadable. Inspect it manually."}, 2
    if not token or owner.get("token") != token:
        return {"status": "blocked", "message": "Guard token does not match; no files changed."}, 2
    owner_file.unlink()
    lock_dir.rmdir()
    return {"status": "released"}, 0


def main():
    parser = argparse.ArgumentParser(description="An explicit run guard; no expiry or automatic lock stealing.")
    parser.add_argument("action", choices=["acquire", "release"])
    parser.add_argument("--state-dir", required=True, type=Path)
    parser.add_argument("--token")
    arguments = parser.parse_args()
    try:
        if arguments.action == "acquire":
            result, status = acquire(arguments.state_dir.resolve())
        else:
            result, status = release(arguments.state_dir.resolve(), arguments.token)
    except OSError as error:
        result, status = {"status": "error", "message": str(error)}, 1
    print(json.dumps(result))
    return status


if __name__ == "__main__":
    sys.exit(main())
