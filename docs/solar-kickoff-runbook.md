# Solar Kickoff Agent — Runbook & Learnings

## Overview
The Solar Kickoff Agent automatically sends a "Solar Documentation Needed" email to sellers when solar is detected on a property. It uses two complementary triggers to ensure the kickoff is always sent, regardless of whether the Zendesk Acquisition ticket or the Snowflake task is detected first — and guarantees no duplicate emails.

---

## Key IDs (Zendesk)

| Item | ID |
|---|---|
| CEP Email form | `13386574321179` |
| Solar Transaction Coordination form | `14088199798683` |
| Support group | `1900001769264` |
| Solar group | `32544318853659` |
| Jessica Young (Jess Young) | `1266768018530` |
| Britt Kato | `1266776989269` |
| Hannah Shipman | `1266801247709` |
| Flip Token ZD field | `9707317021979` |

---

## Gumloop Triggers

### Trigger 1: Solar Kick Off — Acquisition Zendesk Ticketing
**Trigger ID:** `dxGwvtcim5nU2xfcnyphD6`  
**Previous ID (disabled):** `aQtbHQ7WgVagdYCBuXFMi4` — replaced 2026-04-29  
**Type:** MCP trigger (polls Zendesk every 15 min)  

**What it does:** Detects new Solar Escalation (Acquisition) tickets in Zendesk, looks up seller info in Snowflake, and either creates a kickoff + cross-links OR just cross-links if Trigger 2 already sent the kickoff.

**Flow:**
1. Poll Zendesk for Acquisition tickets (form `9982607579419`) created in last 48 hours with no kickoff comment
2. For each, get flip token from ZD field `9707317021979`
3. Query Snowflake for seller info
4. Check if kickoff already exists (search `solar_kickoff_auto` tickets for street address)
   - `action: create_and_link` → create kickoff + cross-link both tickets
   - `action: cross_link_only` → just add cross-link, no new email sent
5. Set Acquisition ticket to Pending + add internal note

---

### Trigger 2: Solar Kick Off — Snowflake Safety Net
**Trigger ID:** `NRjXsWxp4SuMbt3i4z3BPs`  
**Type:** MCP trigger (polls Snowflake every 15 min)  

**What it does:** Catches properties where a Snowflake `initiate_solar_escalation` task exists but no Zendesk Acquisition ticket has been created yet. Sends the kickoff email without cross-linking — Trigger 1 adds the link once the Acquisition ticket is created.

**Flow:**
1. Query Snowflake for `initiate_solar_escalation` tasks open for **30+ minutes** (gives Trigger 1 a head start)
2. Check if kickoff already exists (street address match in `solar_kickoff_auto` tickets)
3. If no kickoff → create kickoff (no cross-link, Acquisition ticket doesn’t exist yet)
4. If kickoff exists → skip

**30-minute delay rationale:** Gives Trigger 1 time to run first. If the ZD Acquisition ticket exists within 30 min, Trigger 1 handles everything. If not, Trigger 2 ensures the seller still gets the email promptly.

---

### Trigger 3: Solar Kickoff — Assignment Safety Net
**Trigger ID:** `SgS5cnjircWXYjcTqrFZou`  
**Type:** MCP trigger (polls every 15 min)  

**What it does:** Auto-corrects Solar Kickoff tickets assigned to the wrong person or group.

**Flow:**
1. Poll Zendesk for Solar Kickoff tickets NOT assigned to Jess or Britt
2. For each, update in a single call: correct assignee + set group to Support (`1900001769264`)

---

## Deduplication Logic

Both Trigger 1 and Trigger 2 check for existing kickoffs before creating one:
- Fetch all `solar_kickoff_auto` tagged tickets (limit 100)
- Match by street address in the subject line (Python-side filter, not Zendesk search)
- If match found → skip (or cross-link only for Trigger 1)

This ensures a seller **never receives two kickoff emails** regardless of which trigger fires first.

---

## Round-Robin Assignment

Both triggers determine the next assignee by:
1. Fetching the 10 most recent `solar_kickoff_auto` tickets
2. Finding the last one assigned to Jess or Britt
3. Alternating: Jess → Britt → Jess → ...

| Agent | ZD ID | Email |
|---|---|---|
| Jess Young | `1266768018530` | jessica.young@opendoor.com |
| Britt Kato | `1266776989269` | brittney.kato@opendoor.com |

---

## Snowflake Reference

**Database:** `DWH`  
**Key tables:** `DWH.DW.AX_FLIPS`, `DWH.DW.AX_LEADS`, `DWH.DW.AX_FLIP_PARTICIPANTS`  
**Seller lookup by flip token:**
```sql
SELECT f.TOKEN, f.ADDRESS_FULL, l.FULL_NAME, l.EMAIL, p.ACQ_TC
FROM DWH.DW.AX_FLIPS f
LEFT JOIN DWH.DW.AX_LEADS l ON l.FLIP_TOKEN = f.TOKEN
LEFT JOIN DWH.DW.AX_FLIP_PARTICIPANTS p ON p.TOKEN = f.TOKEN
WHERE f.TOKEN = '{flip_token}'
QUALIFY ROW_NUMBER() OVER (PARTITION BY f.TOKEN ORDER BY l.CREATED_AT DESC) = 1 LIMIT 1
```

**Snowflake task query (Trigger 2):**
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

## Correct Ticket Values

All kickoff tickets must always have:
- `ticket_form_id`: `13386574321179` (CEP Email) ✅
- `group_id`: `1900001769264` (Support) ✅
- `tags`: `solar_escalation`, `solar_kickoff_auto`
- Assignee: Jess Young or Britt Kato (round-robin)

**Never use:**
- Solar Transaction Coordination form `14088199798683` ❌
- Solar group `32544318853659` ❌

---

## Seller Reply Routing

Kickoff emails send from `support@opendoor.com`. When sellers reply, a new ticket is created in the general support queue. The Assignment Safety Net (Trigger 3) auto-corrects the assignee/group within 15 minutes.

---

## Pending Items (Zendesk Admin)

**Name:** `Solar Kickoff - Ensure CEP Email form on create`  
Condition: Ticket created + Subject contains "Solar Documentation Needed" + Form ≠ CEP Email  
Action: Set form → CEP Email (`13386574321179`)

---

## Trigger ID History

| ID | Status | Notes |
|---|---|---|
| `dxGwvtcim5nU2xfcnyphD6` | ✅ Active | Trigger 1 (ZD-first + dedup), created 2026-04-29 |
| `NRjXsWxp4SuMbt3i4z3BPs` | ✅ Active | Trigger 2 (Snowflake safety net), created 2026-04-29 |
| `SgS5cnjircWXYjcTqrFZou` | ✅ Active | Trigger 3 (Assignment safety net) |
| `aQtbHQ7WgVagdYCBuXFMi4` | ❌ Disabled | Trigger 1 v2 (ZD-first, no dedup), replaced 2026-04-29 |
| `X3eoPYKc8viWsmYfRMBFn7` | ❌ Disabled | Trigger 1 v1 (Snowflake-first), replaced 2026-04-29 |

---

*Last updated: 2026-04-29 by Solar Kickoff Agent (Gumloop)*
