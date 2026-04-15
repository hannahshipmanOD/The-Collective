#!/usr/bin/env python3
"""
sync-superdojo.py
Fetches tracked skill files from opendoor-labs/superdojo and overwrites
the local copies in The-Collective if they differ.
Designed to run inside a GitHub Actions checkout of The-Collective.

Required env var:
  SUPERDOJO_TOKEN — PAT with read access to opendoor-labs/superdojo
                    and write access to hannahshipmanOD/The-Collective
"""

import os
import sys
import base64
import requests

SUPERDOJO_REPO = "opendoor-labs/superdojo"
TOKEN = os.environ.get("SUPERDOJO_TOKEN")

if not TOKEN:
    print("ERROR: SUPERDOJO_TOKEN not set.", file=sys.stderr)
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}

# ── Skills to track ──────────────────────────────────────────────────────────
# Maps: superdojo path → The-Collective local path (relative to repo root)
# Add or remove entries here to control what gets synced.
SKILL_MAP = {
    # cx-knowledge
    "skills/cx-knowledge/SKILL.md":       "skills/cx-knowledge/SKILL.md",
    "skills/cx-knowledge/DATA_MODEL.md":   "skills/cx-knowledge/DATA_MODEL.md",
    "skills/cx-knowledge/STATES.md":       "skills/cx-knowledge/STATES.md",
    "skills/cx-knowledge/ACQ_SUPPORT.md":  "skills/cx-knowledge/ACQ_SUPPORT.md",
    # escalation-pathways
    "skills/escalation-pathways/SKILL.md": "skills/escalation-pathways/SKILL.md",
    # city-nav (add local file if you want to track this)
    # "skills/city-nav/SKILL.md":          "skills/city-nav/SKILL.md",
    # "skills/city-nav/DATA_MODEL.md":     "skills/city-nav/DATA_MODEL.md",
    # "skills/city-nav/UI_GUIDE.md":       "skills/city-nav/UI_GUIDE.md",
    # city-task-sweeper
    # "skills/city-task-sweeper/SKILL.md": "skills/city-task-sweeper/SKILL.md",
}


def fetch_file(repo: str, path: str) -> str | None:
    """Fetch raw file content from a GitHub repo."""
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    resp = requests.get(url, headers=HEADERS, timeout=30)
    if resp.status_code == 404:
        print(f"  [SKIP] Not found in superdojo: {path}")
        return None
    resp.raise_for_status()
    data = resp.json()
    return base64.b64decode(data["content"]).decode("utf-8")


def main():
    changed = []

    for superdojo_path, local_path in SKILL_MAP.items():
        print(f"Checking: {superdojo_path}")
        remote_content = fetch_file(SUPERDOJO_REPO, superdojo_path)
        if remote_content is None:
            continue

        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        # Read existing local file (if any)
        local_content = None
        if os.path.exists(local_path):
            with open(local_path, "r", encoding="utf-8") as f:
                local_content = f.read()

        if remote_content != local_content:
            print(f"  [CHANGED] Writing update → {local_path}")
            with open(local_path, "w", encoding="utf-8") as f:
                f.write(remote_content)
            changed.append(local_path)
        else:
            print(f"  [OK] No change.")

    if changed:
        print(f"\nUpdated {len(changed)} file(s):")
        for p in changed:
            print(f"  • {p}")
    else:
        print("\nAll tracked files are up to date.")


if __name__ == "__main__":
    main()
