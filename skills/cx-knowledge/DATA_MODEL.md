# CX Data Model

## Key tables

### `opendoor.cx_ops.contacts`
Customer contacts and interaction history.

| Column | Type | Description |
|--------|------|-------------|
| `contact_id` | STRING | Unique contact ID |
| `customer_email` | STRING | Customer email |
| `address_token` | STRING | Property address token |
| `channel` | STRING | phone/email/chat |
| `created_at` | TIMESTAMP | Contact creation time |
| `resolved_at` | TIMESTAMP | Resolution time |
| `xa_email` | STRING | Assigned XA |
| `category` | STRING | Contact category/topic |
| `state` | STRING | Contact state |

### `opendoor.cx_ops.cases`
Zendesk case records.

| Column | Type | Description |
|--------|------|-------------|
| `case_id` | STRING | Zendesk ticket ID |
| `subject` | STRING | Ticket subject |
| `status` | STRING | open/pending/solved/closed |
| `priority` | STRING | low/normal/high/urgent |
| `assignee_email` | STRING | Assigned agent |
| `created_at` | TIMESTAMP | Created time |
| `updated_at` | TIMESTAMP | Last updated |
| `tags` | ARRAY<STRING> | Ticket tags |
| `market` | STRING | Market code |

## Common queries

### Daily contact volume by XA
```sql
SELECT
  xa_email,
  DATE(created_at) AS date,
  COUNT(*) AS contacts
FROM opendoor.cx_ops.contacts
WHERE DATE(created_at) = CURRENT_DATE - 1
GROUP BY 1, 2
ORDER BY 3 DESC
```

### Open cases by priority
```sql
SELECT
  priority,
  COUNT(*) AS count
FROM opendoor.cx_ops.cases
WHERE status IN ('open', 'pending')
GROUP BY 1
ORDER BY 2 DESC
```
