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

---

## Gumloop Triggers

### 1. Solar Kick Off — Acquisition Zendesk Ticketing
**Trigger ID:** `X3eoPYKc8viWsmYfRMBFn7`  
**Type:** MCP trigger (polls Snowflake every 15 min)  
**What it does:** Detects new Solar Escalation (Acquisition) tickets and creates a Solar Kickoff email ticket in Zendesk.

**Correct values (as of 2026-04-28):**
- `ticket_form_id`: `13386574321179` (CEP Email)
- `group_id`: `1900001769264` (Support)
- Assignee: round-robin between Jess Young and Britt Kato

**Previous incorrect values (caused the issue):**
- `ticket_form_id`: `14088199798683` (Solar Transaction Coordination) ❌
- `group_id`: `32544318853659` (Solar group) ❌

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
1. Initially suspected wrong **group assignment** — tickets appeared to be routing to the Solar group.
2. Zendesk admin clarified the real issue was the **ticket form** — tickets were using "Solar Transaction Coordination" instead of "CEP Email."
3. Traced to the **Gumloop automation prompt** which had both `ticket_form_id` and `group_id` hardcoded with wrong values from the original build.

### Why It Was Wrong Originally
When the automation was first built, the Solar Transaction Coordination form and Solar group were used because it seemed logically correct for solar-related tickets. The business requirement — that kickoff emails belong to Jess/Britt under CEP Email form in Support group — wasn't reflected in the original build.

### Fix Applied (2026-04-28)
Updated the Gumloop automation prompt:
- `ticket_form_id`: `14088199798683` → `13386574321179` (CEP Email) ✅
- `group_id`: `32544318853659` → `1900001769264` (Support) ✅

Also updated the Safety Net trigger prompt to auto-correct **both** assignee and group when wrong.

---

## Seller Reply Routing

When sellers reply to kickoff emails, the reply creates a **new ticket** in Zendesk (not threaded to the original) routed to `support@opendoor.com`. This is expected behavior.

- Kickoff emails are sent **from** `support@opendoor.com` (not solar@opendoor.com) — intentional to avoid the Solar team trigger
- The Solar trigger `Solar Transaction Coordination-create_ticket_from_incoming_email` fires for emails TO `solar@opendoor.com` or `solarteam@opendoor.com` — this is correct and unrelated to kickoff tickets
- Seller replies may land with wrong assignee — the Safety Net trigger will auto-correct within 15 minutes

---

## Protections In Place (as of 2026-04-28)

| Layer | What it does |
|---|---|
| **Automation prompt** (primary) | Always creates tickets with CEP Email form + Support group + Jess/Britt |
| **Safety Net trigger** (every 15 min) | Auto-corrects wrong assignee AND wrong group immediately |
| **Zendesk admin trigger** (pending) | Safety net for wrong form — recommended but not yet confirmed created |

---

## Pending Items (Zendesk Admin)

A Zendesk trigger has been recommended as a safety net but not yet confirmed created:

**Name:** `Solar Kickoff - Ensure CEP Email form on create`

| Field | Value |
|---|---|
| Condition | Update type = Created |
| Condition | Subject contains "Solar Documentation Needed" |
| Condition | Ticket form is NOT CEP Email |
| Action | Set form → CEP Email (`13386574321179`) |

---

## Relevant Zendesk Triggers (Existing)

| Trigger | Form Condition | Purpose |
|---|---|---|
| Solar Transaction Coordination - set_recipient_on_create | `14088199798683` | Sets recipient to solar@opendoor.com on creation (not applicable to kickoff tickets anymore) |
| Solar Transaction Coordination - create_ticket_from_incoming_email | via email to solar@opendoor.com | Sets form to Solar TC for inbound emails to solar team — intentional |
| Solar Escalation (Acquisition) - reopen_unassigned | `9982607579419` | Reopens unassigned pending/hold tickets |
| Solar Escalation (Resale) - reopen_unassigned | `10068343231131` | Same for resale |

---

## Tickets Identified But Left As-Is
The following tickets from the week of April 21–23, 2026 had the wrong form but were left unchanged (solved + older than current week per team decision):

`#4159609`, `#4159606`, `#4159362`, `#4157499`, `#4155776`, `#4152579`, `#4152525`, `#4150161`, `#4149144`, `#4147680`, `#4136985`, `#4136960`

The following tickets from April 21–23 were identified for form correction but also left as-is (team decided not to retroactively update):

`#4175633`, `#4174947`, `#4174264`, `#4172497`, `#4166694`, `#4165353`

---

*Last updated: 2026-04-29 by Solar Kickoff Agent (Gumloop)*
