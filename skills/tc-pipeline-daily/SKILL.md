# TC Pipeline Daily

## Trigger phrases
- "tc daily"
- "tc pipeline"
- "tc standup"
- "transaction coordinator daily"
- "tc pipeline daily"

## What this skill does

Runs the daily TC pipeline standup. Shows pipeline counts by stage, flags transactions approaching close, and surfaces any stuck/at-risk deals.

## Workflow

1. Run `scripts/query-tc-pipeline-data.py` to pull fresh data
2. Load TC roster from `config/tc-roster.json`
3. Summarize pipeline by TC: count by stage, approaching close, at-risk
4. Flag anything needing attention
5. Format as standup-ready summary

## Output format

```
TC Pipeline Daily — [DATE]

Pipeline by TC:
  [TC name]: [N] active | [N] closing this week | [N] at-risk
  ...

Closing this week: [N]
At-risk: [N]

Flags:
  - [anything needing attention]
```

## Related
- `workloads/tc-pipeline-daily.toml` — batch version
- `config/tc-roster.json` — TC roster
