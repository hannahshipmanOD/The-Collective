#!/usr/bin/env bash
# auto-commit.sh — Auto-commit any changes in the repo
# Usage: ./scripts/auto-commit.sh [message]

set -euo pipefail

MESSAGE="${1:-Auto-commit: $(date '+%Y-%m-%d %H:%M')}"

cd "$(dirname "${BASH_SOURCE[0]}")/.."

if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -m "$MESSAGE"
  echo "Committed: $MESSAGE"
else
  echo "Nothing to commit."
fi
