# Macrodata Refinement

> Claude Code operating system for CX, TC, and Sales Support leadership.

This repo is the personal Claude Code dojo for **Matt McCollum**, Senior Manager for Customer Support, Transaction Management, and Sales Support at Opendoor.

Modeled after [opendoor-labs/superdojo](https://github.com/opendoor-labs/superdojo).

## What lives here

| Directory | Purpose |
|-----------|--------|
| `skills/` | Domain knowledge + workflows Claude loads on-demand |
| `workloads/` | TOML pipeline definitions for batch runs |
| `scripts/` | Data pipelines, automation, and the `superdojo-run` orchestrator |
| `config/` | Rosters, CLAUDE.md templates |
| `docs/` | Guides for personalization and onboarding |

## Skills

| Skill | What it does |
|-------|-------------|
| `cx-knowledge` | CX domain knowledge, states, acquisition support |
| `cx-support-daily` | Daily CX support standup pipeline |
| `zendesk-ops` | Zendesk triage, ops, data model |
| `tc-pipeline-daily` | Daily TC pipeline standup |
| `escalation-pathways` | Escalation routing and decision trees |
| `wavelength` | Team pulse / async communication patterns |
| `meeting-capture` | Meeting notes, action items, follow-ups |
| `analytics` | Data queries, dashboards, ops analytics |
| `define-workload` | Define new TOML workload pipelines |
| `linear-sync` | Linear issue triage and syncing |
| `training` | Onboarding and training content |
| `superninja` | Meta-patterns, systems map, source of truth |

## Quick Start

```bash
# 1. Clone
git clone https://github.com/Matt-McCollum/macrodata-refinement
cd macrodata-refinement

# 2. Install skills into Claude Code
bash install.sh

# 3. Personalize your global CLAUDE.md
# Edit config/claude-md/global-claude.md with your team details
# Then copy to ~/.claude/CLAUDE.md
cp config/claude-md/global-claude.md ~/.claude/CLAUDE.md

# 4. Open Claude Code in any project
claude
```

## Running a workload

```bash
# Daily CX support pipeline
./scripts/superdojo-run workloads/cx-support-daily.toml

# Daily TC pipeline
./scripts/superdojo-run workloads/tc-pipeline-daily.toml
```
