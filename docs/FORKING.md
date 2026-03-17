# Personalizing Your Dojo

This guide walks through how to make `macrodata-refinement` fully yours.

## 1. Update your global CLAUDE.md

The template is at `config/claude-md/global-claude.md`. Open it and update:

- Your name and role at the top
- Your team members in the XA and TC roster sections
- Your manager's name
- Any org-specific context that matters

Then install it:
```bash
cp config/claude-md/global-claude.md ~/.claude/CLAUDE.md
```

## 2. Update rosters

- `config/xa-roster.json` — your XA (Customer Support) team
- `config/tc-roster.json` — your TC (Transaction Coordinator) team

Each roster entry has: `name`, `email`, `start_date`, `manager`.

## 3. Customize skills

Skills live in `skills/<name>/`. You can:
- Edit `SKILL.md` to adjust trigger phrases and workflows
- Add new `DATA_MODEL.md` files with your team's specific queries
- Add new skills by creating a new directory with a `SKILL.md`

## 4. Add or edit workloads

Workloads are TOML files in `workloads/`. Each one defines a batch pipeline.
See `skills/define-workload/SKILL.md` for how to create new ones.

## 5. Customize scripts

Data pipeline scripts are in `scripts/`. Update:
- `query-cx-support-data.py` — adjust Zendesk/BQ queries for your team
- `query-tc-pipeline-data.py` — adjust TC data sources

## 6. Run install.sh after changes

After updating skills, re-run:
```bash
bash install.sh
```
