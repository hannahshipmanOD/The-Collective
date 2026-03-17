#!/usr/bin/env bash
set -euo pipefail

SKILLS=(
  cx-knowledge
  cx-support-daily
  zendesk-ops
  tc-pipeline-daily
  escalation-pathways
  wavelength
  meeting-capture
  analytics
  define-workload
  linear-sync
  training
  superninja
)

SCRIPTS=(
  superdojo-run
  auto-commit.sh
  query-cx-support-data.py
  query-tc-pipeline-data.py
  shared_cache.py
)

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$HOME/.claude/skills"

mkdir -p "$SKILLS_DIR"

echo "Installing skills..."
for skill in "${SKILLS[@]}"; do
  src="$REPO_DIR/skills/$skill"
  dst="$SKILLS_DIR/$skill"
  if [ -d "$src" ]; then
    ln -sfn "$src" "$dst"
    echo "  ✓ $skill"
  else
    echo "  ✗ $skill (not found at $src)"
  fi
done

echo ""
echo "Making scripts executable..."
for script in "${SCRIPTS[@]}"; do
  path="$REPO_DIR/scripts/$script"
  if [ -f "$path" ]; then
    chmod +x "$path"
    echo "  ✓ $script"
  fi
done

echo ""
echo "Done! Skills installed to $SKILLS_DIR"
echo ""
echo "Next steps:"
echo "  1. Edit config/claude-md/global-claude.md with your details"
echo "  2. cp config/claude-md/global-claude.md ~/.claude/CLAUDE.md"
echo "  3. Open claude in any project and reference skills with @<skill-name>"
