# Operations Data Model

## CX tables
- `opendoor.cx_ops.contacts` — customer contact records
- `opendoor.cx_ops.cases` — Zendesk case records
- `opendoor.zendesk.tickets` — raw Zendesk tickets
- `opendoor.zendesk.ticket_events` — ticket event log
- `opendoor.zendesk.sla_policies` — SLA definitions

## TC tables
- `opendoor.tc_ops.transactions` — transaction pipeline
- `opendoor.tc_ops.milestones` — transaction milestone events
- `opendoor.tc_ops.tc_assignments` — TC-to-transaction assignments

## Key joins

```sql
-- Transactions with assigned TC
SELECT
  t.*,
  a.tc_email,
  a.assigned_at
FROM opendoor.tc_ops.transactions t
JOIN opendoor.tc_ops.tc_assignments a
  ON t.transaction_id = a.transaction_id
  AND a.is_current = TRUE
```
