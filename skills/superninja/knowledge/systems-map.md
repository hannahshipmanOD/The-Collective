# Systems Map

How the systems connect for CX, TC, and Sales Support operations.

## Customer journey data flow

```
Customer contact
  → Zendesk (ticket created)
  → BigQuery sync (nightly)
  → cx_ops.cases (queryable)
  → superdojo-run (daily pipeline)
  → Standup summary (Slack)
```

## Transaction data flow

```
Contract signed
  → Transaction system (internal)
  → BigQuery sync
  → tc_ops.transactions (queryable)
  → superdojo-run (daily pipeline)
  → TC standup summary (Slack)
```

## Issue tracking flow

```
Problem identified (chat, meeting, data)
  → @linear-sync (create issue)
  → Linear (tracked)
  → Weekly review
  → Resolution logged
```

## Skill dependencies

```
superninja
  ← knows about all other skills

cx-support-daily
  ← cx-knowledge
  ← zendesk-ops
  ← analytics

tc-pipeline-daily
  ← analytics

meeting-capture
  ← linear-sync (for action items)

escalation-pathways
  ← cx-knowledge
  ← linear-sync
```
