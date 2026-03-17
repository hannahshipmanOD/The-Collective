# Zendesk Data Model

## Zendesk objects

### Tickets
Core unit — a customer support request.

| Field | Description |
|-------|-------------|
| `id` | Ticket ID |
| `subject` | Ticket subject |
| `status` | new / open / pending / hold / solved / closed |
| `priority` | low / normal / high / urgent |
| `type` | question / incident / problem / task |
| `assignee_id` | Assigned agent |
| `group_id` | Assigned group |
| `tags` | Array of tags |
| `created_at` | Creation timestamp |
| `updated_at` | Last update timestamp |
| `due_at` | SLA due timestamp |

### Users (agents)
| Field | Description |
|-------|-------------|
| `id` | User ID |
| `email` | Agent email |
| `name` | Agent name |
| `role` | agent / admin / end-user |

### Groups
Team groupings for routing.

## BigQuery sync tables

### `opendoor.zendesk.tickets`
Daily snapshot of all tickets.

### `opendoor.zendesk.ticket_events`
Event log for all ticket state changes.

### `opendoor.zendesk.sla_policies`
SLA policy definitions and breach events.

## Common queries

### Tickets breaching SLA today
```sql
SELECT
  t.id,
  t.subject,
  t.priority,
  t.assignee_email,
  t.due_at
FROM opendoor.zendesk.tickets t
WHERE t.status IN ('new', 'open', 'pending')
  AND t.due_at < CURRENT_TIMESTAMP
ORDER BY t.due_at ASC
```

### Volume by group last 7 days
```sql
SELECT
  group_name,
  DATE(created_at) AS date,
  COUNT(*) AS tickets
FROM opendoor.zendesk.tickets
WHERE created_at >= CURRENT_TIMESTAMP - INTERVAL 7 DAY
GROUP BY 1, 2
ORDER BY 2 DESC, 3 DESC
```
