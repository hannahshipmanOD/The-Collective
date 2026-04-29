# Solar Kickoff Agent — Runbook & Learnings

## Overview
The Solar Kickoff Agent automatically sends a "Solar Documentation Needed" email to sellers when a Solar Escalation (Acquisition) ticket is detected. The kickoff email is created as a Zendesk ticket assigned to either **Jessica Young** or **Britt Kato** in the **Support group**.

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

### 1. Solar Kick Off — Acquisition Zendesk Ticketing
**Trigger ID:** `aQtbHQ7WgVagdYCBuXFMi4`  
**Previous ID (disabled):** `X3eoPYKc8viWsmYfRMBFn7` — replaced 2026-04-29  
**Type:** MCP trigger (polls Zendesk every 15 min)  
**What it does:** Detects new Solar Escalation (Acquisition) tickets in Zendesk, looks up seller info in Snowflake, and creates a Solar Kickoff email ticket linked to the Acquisition ticket.

**How it works:**
1. Poll Zendesk for Solar Escalation (Acquisition) tickets (form `9982607579419`) without a kickoff sent
2. Extract flip token from ZD custom field `9707317021979`
3. Query Snowflake (`DWH.DW.AX_FLIPS` + `DWH.DW.AX_LEADS`) for seller name/email
4. Create kickoff ticket with correct form/group/assignee
5. Cross-link both tickets + set Acquisition ticket to Pending

**Correct values:**
- `ticket_form_id`: `13386574321179` (CEP Email)
- `group_id`: `1900001769264` (Support)
- Assignee: round-robin between Jess Young and Britt Kato

**Why redesigned (2026-04-29):** The original trigger fired based on Snowflake task data, which was available hours before the Zendesk Acquisition ticket was created. This caused kickoffs to be sent without being linked to the Acquisition ticket. The new trigger fires based on Zendesk Acquisition ticket creation, eliminating the timing gap.

---

### 2. Solar Kickoff — Assignment Safety Net
**Trigger ID:** `SgS5cnjircWXYjcTqrFZou`  
**Type:** MCP trigger (polls every 15 min)  
**What it does:** Detects Solar Kickoff tickets NOT assigned to Jess or Britt and auto-corrects both the **assignee** and the **group** (sets to Support: `1900001769264`) in a single update.

---

## Root Cause Investigation (April 2026)

### Problem
Solar Team was seeing Solar Kickoff email tickets in their Zendesk inbox even though they should only appear for Jessica Young and Britt Kato.

### Investigation Path
1. Initially suspected wrong **group assignment**.
2. Zendesk admin clarified the real issue was the **ticket form** — tickets were using "Solar Transaction Coordination" instead of "CEP Email."
3. Traced to the **Gumloop automation prompt** which had both `ticket_form_id` and `group_id` hardcoded with wrong values from the original build.

### Fix Applied (2026-04-28)
- `ticket_form_id`: `14088199798683` → `13386574321179` (CEP Email) ✅
- `group_id`: `32544318853659` → `1900001769264` (Support) ✅

### Timing Gap Fix (2026-04-29)
The original Snowflake-based trigger fired BEFORE the Zendesk Acquisition ticket existed, causing kickoffs to be sent without cross-links. Redesigned to be Zendesk-first: trigger now polls ZD Acquisition tickets and looks up seller info in Snowflake using the flip token from ZD field `9707317021979`.

---

## Snowflake Query Reference

**Database:** `DWH`  
**Key tables:** `DWH.DW.AX_FLIPS`, `DWH.DW.AX_LEADS`, `DWH.DW.AX_FLIP_PARTICIPANTS`

```sql
SELECT
    f.TOKEN AS flip_token,
    f.ADDRESS_FULL AS property_address,
    CASE
        WHEN l.FULL_NAME LIKE '%@%' OR l.FULL_NAME IS NULL THEN 'Seller'
        ELSE SPLIT_PART(TRIM(l.FULL_NAME), ' ', 1)
    END AS seller_first_name,
    l.FULL_NAME AS seller_full_name,
    l.EMAIL AS seller_email,
    p.ACQ_TC AS tc_name
FROM DWH.DW.AX_FLIPS f
LEFT JOIN DWH.DW.AX_LEADS l ON l.FLIP_TOKEN = f.TOKEN
LEFT JOIN DWH.DW.AX_FLIP_PARTICIPANTS p ON p.TOKEN = f.TOKEN
WHERE f.TOKEN = '{flip_token}'
QUALIFY ROW_NUMBER() OVER (PARTITION BY f.TOKEN ORDER BY l.CREATED_AT DESC) = 1
LIMIT 1
```

---

## Seller Reply Routing

When sellers reply to kickoff emails, the reply creates a **new ticket** in Zendesk routed to `support@opendoor.com`. This is expected behavior. The Safety Net trigger will auto-correct assignee/group within 15 minutes.

---

## Protections In Place (as of 2026-04-29)

| Layer | What it does |
|---|---|
| **Acquisition trigger** (every 15 min) | Detects new ZD Acquisition tickets, looks up seller in Snowflake, creates kickoff + cross-links |
| **Safety Net trigger** (every 15 min) | Auto-corrects wrong assignee AND wrong group |
| **Zendesk admin trigger** (pending) | Safety net for wrong form — recommended but not yet confirmed created |

---

## Pending Items (Zendesk Admin)

**Name:** `Solar Kickoff - Ensure CEP Email form on create`

| Field | Value |
|---|---|
| Condition | Update type = Created |
| Condition | Subject contains "Solar Documentation Needed" |
| Condition | Ticket form is NOT CEP Email |
| Action | Set form → CEP Email (`13386574321179`) |

---

## Relevant Zendesk Triggers (Existing)

| Trigger | Condition | Purpose |
|---|---|---|
| Solar Transaction Coordination - create_ticket_from_incoming_email | via email to solar@opendoor.com | Sets form to Solar TC for inbound emails to solar team — intentional, do not change |
| Solar Escalation (Acquisition) - reopen_unassigned | form `9982607579419` | Reopens unassigned pending/hold tickets |

---

*Last updated: 2026-04-29 by Solar Kickoff Agent (Gumloop)*
