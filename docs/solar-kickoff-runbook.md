# Solar Kickoff Agent — Runbook & Learnings

## Overview
The Solar Kickoff Agent automatically sends a "Solar Documentation Needed" email to sellers when solar is detected on a property. It uses two complementary triggers to ensure the kickoff always sends regardless of whether the Zendesk Acquisition ticket or the Snowflake task is detected first — and guarantees no duplicate emails.

---

## Key IDs (Zendesk)

| Item | ID |
|---|---|
| CEP Email form | `13386574321179` ✅ CORRECT |
| Solar Transaction Coordination form | `14088199798683` ❌ WRONG for kickoff tickets |
| Support group | `1900001769264` ✅ CORRECT |
| Solar group | `32544318853659` ❌ WRONG for kickoff tickets |
| Jessica Young (Jess Young) | `1266768018530` |
| Britt Kato | `1266776989269` |
| Hannah Shipman | `1266801247709` |
| Flip Token ZD field | `9707317021979` (on Acquisition tickets) |

---

## Ticket Status Flow

| Ticket | On Creation | After Cross-Link | When Seller Replies |
|---|---|---|---|
| **Kickoff email ticket** | Solved ✅ | Stays Solved ✅ | Open ✅ (auto via ZD trigger) |
| **Acquisition ticket** | N/A | **On Hold** ✅ | N/A |

Note: The Zendesk trigger "Set: Status to open when ticket replied to" automatically reopens the kickoff ticket when a seller responds. This is intentional and desired behavior.

---

## Gumloop Triggers

### Trigger 1: Solar Kick Off — Acquisition Zendesk Ticketing
**ID:** `dxGwvtcim5nU2xfcnyphD6`  
**Previous IDs (disabled):** `aQtbHQ7WgVagdYCBuXFMi4`, `X3eoPYKc8viWsmYfRMBFn7`  
**Type:** MCP trigger | Polls every 15 min  

**What it does:** Detects new Solar Escalation (Acquisition) tickets in Zendesk, looks up seller info in Snowflake, and either creates a kickoff + cross-links OR just cross-links if Trigger 2 already sent the kickoff.

**Flow:**
1. Poll Zendesk for Acquisition tickets (form `9982607579419`) created in last 48 hours with no kickoff comment
2. Extract flip token from ZD field `9707317021979`
3. Query Snowflake for seller info (`DWH.DW.AX_FLIPS` + `DWH.DW.AX_LEADS`)
4. Check if kickoff already exists (search `solar_kickoff_auto` tickets, match by street address in Python)
   - `action: create_and_link` → create kickoff (Solved) + cross-link + set Acquisition to **On Hold**
   - `action: cross_link_only` → just add cross-link + set Acquisition to **On Hold**, no new email

---

### Trigger 2: Solar Kick Off — Snowflake Safety Net
**ID:** `NRjXsWxp4SuMbt3i4z3BPs`  
**Type:** MCP trigger | Polls every 15 min  

**What it does:** Catches properties where a Snowflake `initiate_solar_escalation` task exists but no Zendesk Acquisition ticket has been created yet. Sends the kickoff email without cross-linking — Trigger 1 adds the link once the Acquisition ticket is eventually created.

**Flow:**
1. Query Snowflake for `initiate_solar_escalation` tasks open for **30+ minutes** (gives Trigger 1 a head start)
2. Check if kickoff already exists (street address match)
3. If no kickoff → create kickoff (Solved, no cross-link)
4. If kickoff exists → skip

**Why 30-minute delay:** Prevents race conditions. If the ZD Acquisition ticket is created within 30 min, Trigger 1 fires first and handles everything cleanly.

---

### Trigger 3: Solar Kickoff — Assignment Safety Net
**ID:** `SgS5cnjircWXYjcTqrFZou`  
**Type:** MCP trigger | Polls every 15 min  

**What it does:** Auto-corrects Solar Kickoff tickets assigned to the wrong person or group.

**Flow:**
1. Find Solar Kickoff tickets NOT assigned to Jess or Britt
2. Update in a single call: correct assignee + set group to Support (`1900001769264`)

---

## Trigger ID History

| ID | Status | Notes |
|---|---|---|
| `dxGwvtcim5nU2xfcnyphD6` | ✅ Active | Trigger 1 (ZD-first + dedup) |
| `NRjXsWxp4SuMbt3i4z3BPs` | ✅ Active | Trigger 2 (Snowflake safety net) |
| `SgS5cnjircWXYjcTqrFZou` | ✅ Active | Trigger 3 (Assignment safety net) |
| `aQtbHQ7WgVagdYCBuXFMi4` | ❌ Disabled | Trigger 1 v2 (ZD-first, no dedup) |
| `X3eoPYKc8viWsmYfRMBFn7` | ❌ Disabled | Trigger 1 v1 (Snowflake-first, wrong form/group) |

---

## Deduplication Logic

Both Trigger 1 and Trigger 2 check for existing kickoffs before creating one:
- Fetch all `solar_kickoff_auto` tagged tickets (limit 100)
- Match by street address in the subject line using Python (Zendesk search filters are unreliable for multi-condition matching)
- Result: a seller **never receives two kickoff emails** regardless of which trigger fires first

---

## Round-Robin Assignment

| Agent | ZD ID | Email |
|---|---|---|
| Jess Young | `1266768018530` | jessica.young@opendoor.com |
| Britt Kato | `1266776989269` | brittney.kato@opendoor.com |

Last assigned: **Britt Kato** (#4209956) | Next: **Jess Young**

---

## Snowflake Reference

**Database:** `DWH`  
**Key tables:**
- `DWH.DW.AX_FLIPS` — property/flip info
- `DWH.DW.AX_LEADS` — seller info
- `DWH.DW.AX_FLIP_PARTICIPANTS` — TC info
- `DWH.CASEY.DWH_TASKS_VIEW` — solar escalation tasks
- `DWH.CASEY.DWH_RELATED_OBJECTS_VIEW` — task-to-flip mapping

**Seller lookup by flip token:**
```sql
SELECT f.TOKEN, f.ADDRESS_FULL, l.FULL_NAME, l.EMAIL, p.ACQ_TC
FROM DWH.DW.AX_FLIPS f
LEFT JOIN DWH.DW.AX_LEADS l ON l.FLIP_TOKEN = f.TOKEN
LEFT JOIN DWH.DW.AX_FLIP_PARTICIPANTS p ON p.TOKEN = f.TOKEN
WHERE f.TOKEN = '{flip_token}'
QUALIFY ROW_NUMBER() OVER (PARTITION BY f.TOKEN ORDER BY l.CREATED_AT DESC) = 1 LIMIT 1
```

**Task query (Trigger 2, 30-min delay):**
```sql
SELECT t.UUID, ro.OBJECT_ID AS flip_token, f.ADDRESS_FULL, l.FULL_NAME, l.EMAIL, p.ACQ_TC
FROM DWH.CASEY.DWH_TASKS_VIEW t
JOIN DWH.CASEY.DWH_RELATED_OBJECTS_VIEW ro ON t.UUID = ro.TASK_UUID AND ro.OBJECT_TYPE = 'flip'
JOIN DWH.DW.AX_FLIPS f ON ro.OBJECT_ID = f.TOKEN
LEFT JOIN DWH.DW.AX_LEADS l ON l.FLIP_TOKEN = f.TOKEN
LEFT JOIN DWH.DW.AX_FLIP_PARTICIPANTS p ON p.TOKEN = f.TOKEN
WHERE t.TASK_TYPE = 'initiate_solar_escalation'
  AND t.STATUS = 'open'
  AND f.FLIP_STATE NOT IN ('acq_withdrawn', 'acq_expired', 'pre_listing')
  AND t.ACTIVE_AT <= DATEADD('minute', -30, CURRENT_TIMESTAMP())
QUALIFY ROW_NUMBER() OVER (PARTITION BY ro.OBJECT_ID ORDER BY l.CREATED_AT DESC) = 1
```

---

## Root Cause History

### Fix 1 (2026-04-28) — Wrong Form & Group
Original automation had wrong values hardcoded:
- `ticket_form_id: 14088199798683` (Solar TC) → fixed to `13386574321179` (CEP Email)
- `group_id: 32544318853659` (Solar) → fixed to `1900001769264` (Support)

This caused kickoff tickets to appear in the Solar team’s Zendesk inbox.

### Fix 2 (2026-04-29) — Timing Gap
Original Snowflake-first trigger fired BEFORE the Zendesk Acquisition ticket existed, causing kickoffs to be sent without cross-links. Redesigned to:
- **Trigger 1:** ZD-first — always creates kickoff AFTER Acquisition ticket exists → guaranteed cross-link
- **Trigger 2:** Snowflake safety net — fires after 30-min delay if no ZD ticket yet, Trigger 1 handles cross-link later

---

## Important Context

- **Kickoff emails send from support@opendoor.com** (not solar@opendoor.com) — intentional, prevents seller replies routing to Solar team inbox
- **Seller replies create new tickets** in the general support queue — expected behavior, Assignment Safety Net auto-corrects within 15 min
- **Solar Transaction Coordination-create_ticket_from_incoming_email** ZD trigger is intentional — handles inbound emails to solar@opendoor.com, do not modify
- **Zendesk search is unreliable for multi-condition tag filtering** — always use Python-side filtering when matching on multiple conditions

---

## Pending Items (Zendesk Admin)

**Recommended but not yet confirmed created:**  
Trigger: `Solar Kickoff - Ensure CEP Email form on create`
- Condition: Ticket created + Subject contains “Solar Documentation Needed” + Form ≠ CEP Email
- Action: Set form → CEP Email (`13386574321179`)

---

*Last updated: 2026-04-29 by Solar Kickoff Agent (Gumloop)*
