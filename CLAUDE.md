# Macrodata Refinement — Repo Navigation

This is Matt McCollum's Claude Code dojo repo. Use this file to understand what's here and how to use it.

## Repo layout

```
macrodata-refinement/
├── skills/          # Domain knowledge modules (install with install.sh)
├── workloads/       # TOML batch pipeline definitions
├── scripts/         # superdojo-run orchestrator + data pipelines
├── config/          # Rosters, CLAUDE.md templates
└── docs/            # Personalization guides
```

## How skills work

Each skill lives at `skills/<name>/SKILL.md`. Run `install.sh` to symlink them into `~/.claude/skills/`. Reference them in conversation with `@<skill-name>`.

## How workloads work

Workloads are TOML files in `workloads/`. Run them with:
```bash
./scripts/superdojo-run workloads/<name>.toml
```

## Key files

- `config/xa-roster.json` — XA team roster
- `config/tc-roster.json` — TC team roster
- `config/claude-md/global-claude.md` — template for `~/.claude/CLAUDE.md`
- `config/claude-md/project-claude.md` — template for project-level `CLAUDE.md`

## Personalization

See `docs/FORKING.md` for how to customize this repo for your team.
