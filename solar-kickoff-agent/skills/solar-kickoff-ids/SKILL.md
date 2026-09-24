---
name: solar-kickoff-ids
description: Source-of-truth reference for all Solar Kickoff Zendesk IDs, Snowflake tables, assignee IDs, and trigger IDs. Activate whenever creating or updating Zendesk tickets, querying Snowflake for seller/flip data, or managing Solar Kickoff triggers.
icon: database
color: Blue
related_server_ids:
- zendesk
- snowflake
---

# Solar Kickoff — IDs & Reference

## Zendesk Form & Group IDs

| Item | ID | Notes |
|---|---|---|
| **CEP Email form** | `13386574321179` | ✅ CORRECT — use for ALL kickoff tickets |
| Solar TC form | `14088199798683` | ❌ WRONG — routes to Solar team inbox |
| **Support group** | `1900001769264` | ✅ CORRECT — use for ALL kickoff tickets |
| Solar group | `32544318853659` | ❌ WRONG — do not use for kickoff tickets |
| Flip Token ZD field | `9707317021979` | Custom field on Acquisition tickets |
| Acquisition ticket form | `9982607579419` | Used only for polling, not for creating |

## Assignees

| Name | Zendesk ID | Email |
|---|---|---|
| Britt Kato | `1266776989269` | brittney.kato@opendoor.com |
| Sarah Dumke | `51437835705499` | s.dumke@opendoor.com |
| Claire Buser | `1266761670590` | claire.buser@opendoor.com |
| Katie Villasenor | `8951685716379` | katie.villasenor@opendoor.com |

**Round-robin rotation:** Britt Kato → Sarah Dumke → Claire Buser → Katie Villasenor → (repeat)
**Current state:** Last assigned = Britt Kato → Next = Sarah Dumke

## Slack

| Person | Slack User ID |
|---|---|
| Russell White | `U02A82RHUBB` |

## Trigger IDs

| Trigger | ID | Frequency |
|---|---|---|
| Trigger 1 — Acquisition ZD Ticketing | `bCMpEUsesa3Eq5JKqGsxbM` | Every 15 min |
| Trigger 3 — Assignment Safety Net | `YFFXs6fBtYjat8f3JaMiZb` | Mon–Fri 14:30 MST (schedule) |
| Trigger 4 — 72hr No-ZD-Ticket Alert | `AvaYawaaSovuqn7gu7yX8G` | Every 24 hrs |

## Snowflake Tables

| Purpose | Table / View |
|---|---|
| Database | `DWH` |
| Flip data + address | `DWH.DW.AX_FLIPS` (field: `ADDRESS_FULL`) |
| Seller (lead) info | `DWH.DW.AX_LEADS` (field: `FIRST_NAME`) |
| Participants (assignee lookup) | `DWH.WEB.PARTICIPANTS` + `DWH.WEB.HUMANS` |
| Escalation tasks | `DWH.CASEY.DWH_TASKS_VIEW` + `DWH.CASEY.DWH_RELATED_OBJECTS_VIEW` |

## Acq Sales Support Query

```sql
SELECT h.FULL_NAME AS support_owner, h.EMAIL AS support_email
FROM DWH.WEB.PARTICIPANTS p
JOIN DWH.WEB.HUMANS h ON h.ID = p.PARTICIPATING_HUMAN_ID
JOIN DWH.DW.AX_FLIPS f ON f.ID = p.FLIP_ID
WHERE f.TOKEN = '{flip_token}'
  AND BITAND(p.ROLES_MASK, 17179869184) > 0   -- 2^34 = Acq Sales Support
LIMIT 1
```
If the email matches Britt/Sarah/Claire → assign to them. Otherwise → round-robin fallback.
