# CX Support Daily

## Trigger phrases
- "cx daily"
- "cx standup"
- "cx support daily"
- "morning cx"
- "daily cx pipeline"

## What this skill does

Runs the daily CX support standup pipeline. Pulls yesterday's contact volume, open case counts, SLA metrics, and flags any anomalies for the team standup.

## Workflow

1. Run `scripts/query-cx-support-data.py` to pull fresh data
2. Load XA roster from `config/xa-roster.json`
3. Summarize: contact volume per XA, open cases, SLA hits/misses
4. Flag anything that needs attention
5. Format as standup-ready summary

## Output format

```
CX Support Daily — [DATE]

Yesterday's volume:
  [XA name]: [N] contacts
  ...

Open cases: [N] (High: [N], Urgent: [N])

SLA performance:
  First response: [X]% on time
  Resolution: [X]% on time

Flags:
  - [anything needing attention]
```

## Related
- `workloads/cx-support-daily.toml` — batch version
- `skills/zendesk-ops/SKILL.md` — deeper Zendesk ops
- `skills/cx-knowledge/SKILL.md` — domain context
