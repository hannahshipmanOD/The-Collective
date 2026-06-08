# Solar Kickoff Agent — Runbook & Learnings

## Overview
The Solar Kickoff Agent automatically sends a "Solar Documentation Needed" email to sellers when solar is detected on a property via a new Zendesk Solar Escalation (Acquisition) ticket. It assigns kickoff tickets to Jess Young or Britt Kato in round-robin, cross-links both tickets, sets the Acquisition ticket to On Hold (with re-verification), and guarantees no duplicate emails are ever sent.

---

## Key IDs (Zendesk)

| Item | ID |
|---|---|
| **CEP Email form** | `13386574321179` ✅ CORRECT form for all kickoff tickets |
| Solar Transaction Coordination form | `14088199798683` ❌ WRONG — do NOT use for kickoff tickets |
| **Support group** | `1900001769264` ✅ CORRECT group for all kickoff tickets |
| Solar group | `32544318853659` ❌ WRONG — do NOT use for kickoff tickets |
| Jess Young | `1266768018530` (jessica.young@opendoor.com) |
| Britt Kato | `1266776989269` (brittney.kato@opendoor.com) |
| Hannah Shipman | `1266801247709` (Slack: `UPF9A23DF`) |
| Flip Token ZD field | `9707317021979` (on Acquisition tickets) |

---

## Ticket Status Flow

| Ticket | On Creation | After Cross-Link | When Seller Replies |
|---|---|---|---|
| **Kickoff email ticket** | Solved ✅ | Stays Solved ✅ | Open ✅ (auto via ZD trigger) |
| **Acquisition ticket** | N/A | **On Hold** ✅ (re-verified after setting) | N/A |

Note: The Zendesk trigger "Set: Status to open when ticket replied to" automatically reopens the kickoff ticket when a seller responds. This is intentional and desired behavior.

---

## Gumloop Triggers

### Trigger 1: Solar Kick Off — Acquisition Zendesk Ticketing
**ID:** `dxGwvtcim5nU2xfcnyphD6` | Polls every 15 min
**Previous IDs (disabled):** `aQtbHQ7WgVagdYCBuXFMi4` → `X3eoPYKc8viWsmYfRMBFn7`

**What it does:** Detects new Solar Escalation (Acquisition) tickets in Zendesk, looks up seller info in Snowflake, and either creates a kickoff + cross-links, or just cross-links if a kickoff already exists. Always sets the Acquisition ticket to On Hold and re-verifies it stayed there.

**Flow:**
1. Poll Zendesk for new Solar Escalation (Acquisition) tickets (form `9982607579419`) created in last 48 hours
2. For each, look up seller info in Snowflake using the flip token (ZD field `9707317021979`)
3. Check if a kickoff already exists by searching `solar_kickoff_auto` tickets for matching street address (Python-side match, not ZD search filter):
   - **`action: create_and_link`** — no kickoff yet → create kickoff (Solved) + cross-link + set Acquisition to **On Hold**, re-verify On Hold
   - **`action: cross_link_only`** — kickoff already exists → add cross-links, no new email, set Acquisition to **On Hold**, re-verify On Hold
   - **`action: no_seller_found`** — no Snowflake match → tag Acquisition ticket `solar_no_leads_match` for Trigger 4 monitoring

**On Hold Re-Verify (added 2026-05-22):** After setting the Acquisition ticket to On Hold, Trigger 1 re-fetches the ticket and corrects it back to On Hold if Zendesk has flipped it to Open. This is the final step in both `create_and_link` and `cross_link_only` flows.

---

### Trigger 2: Solar Kick Off — Snowflake Safety Net
~~**ID:** `NRjXsWxp4SuMbt3i4z3BPs`~~ **DELETED 2026-05-22**

Previously auto-sent kickoff emails when a Snowflake `initiate_solar_escalation` task existed but no ZD Acquisition ticket had been created yet. Removed because:
- The Solar team always creates a ZD Acquisition ticket before the kickoff is needed
- Trigger 1 is the sole path for kickoff creation
- Trigger 4 (below) provides visibility into any gaps without auto-sending emails

Analysis at deletion: ~3.7% of SF tasks never get a ZD ticket; median lag between SF task and ZD ticket creation is 46.5 hours. The team is comfortable with the delay.

---

### Trigger 3: Solar Kickoff — Assignment Safety Net
**ID:** `SgS5cnjircWXYjcTqrFZou` | Polls every 15 min

**What it does:** Auto-corrects Solar Kickoff tickets assigned to the wrong person or group.

**Flow:**
1. Poll Zendesk for Solar Kickoff tickets NOT assigned to Jess or Britt
2. For each found, update in a single call:
   - Correct assignee → Jess or Britt (per round-robin)
   - Correct group → Support (`1900001769264`)

---

### Trigger 4: Solar Escalation Monitor — 72hr No ZD Ticket Alert
**ID:** `5ULDL9NyE3EnS29REkff3Y` | Polls every 24 hours
**Created:** 2026-05-22 (replaced Trigger 2)

**What it does:** Alerts Hannah Shipman when a Snowflake `initiate_solar_escalation` task has been open 72+ hours with no ZD Solar Escalation (Acquisition) ticket created — provides visibility without auto-sending emails.

**Flow:**
1. Query Snowflake for `initiate_solar_escalation` tasks open 72+ hours
2. For each, check if a ZD Acquisition ticket exists (flip token match against form `9982607579419`)
3. If no ZD ticket found → send Slack DM to Hannah (`UPF9A23DF`) with flip token + full property address (`AX_FLIPS.ADDRESS_FULL`)
4. Dedup: alerts once per day per flip token (tracks `last_alerted_utc` in state)
5. Stops alerting once a ZD ticket appears or the SF task closes

**DM format:**
```
☀️ Solar Escalation Alert - No ZD Ticket Created
Flip Token: `{token}` | Property: {address}
Task Opened: {date} UTC | Hours Open: {n} hrs
```

---

## Trigger ID History

| ID | Status | Notes |
|---|---|---|
| `dxGwvtcim5nU2xfcnyphD6` | ✅ Active | Trigger 1 (ZD-first, dedup, On Hold re-verify) |
| `SgS5cnjircWXYjcTqrFZou` | ✅ Active | Trigger 3 (Assignment safety net) |
| `5ULDL9NyE3EnS29REkff3Y` | ✅ Active | Trigger 4 (72hr no-ZD-ticket alert) |
| `NRjXsWxp4SuMbt3i4z3BPs` | ❌ Deleted 2026-05-22 | Trigger 2 (Snowflake safety net — replaced by Trigger 4) |
| `aQtbHQ7WgVagdYCBuXFMi4` | ❌ Disabled | Trigger 1 v2 (ZD-first, no dedup) |
| `X3eoPYKc8viWsmYfRMBFn7` | ❌ Disabled | Trigger 1 v1 (Snowflake-first, wrong form/group) |

---

## Deduplication Logic

Trigger 1 checks for existing kickoffs before creating one:
- Fetch all `solar_kickoff_auto` tagged tickets (limit 100)
- Match by street address in the subject line using Python (not Zendesk search, which is unreliable for multi-condition filtering)
- If match found → cross-link only (no new email)
- This guarantees a seller **never receives two kickoff emails**

---

## Round-Robin Assignment

| Name | Zendesk ID | Email |
|---|---|---|
| Jess Young | `1266768018530` | jessica.young@opendoor.com |
| Britt Kato | `1266776989269` | brittney.kato@opendoor.com |

Last assigned: **Britt Kato** (1266776989269) — ticket #4255226
Next assignment: **Jess Young** (1266768018530)

---

## Snowflake Reference

**Database:** `DWH`
**Key tables:**
- `DWH.DW.AX_FLIPS` — property/flip info (includes `ADDRESS_FULL`)
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

---

## Root Cause History

### Fix 1 (2026-04-28) — Wrong Form & Group
Original automation had wrong values hardcoded:
- `ticket_form_id: 14088199798683` (Solar TC) → fixed to `13386574321179` (CEP Email)
- `group_id: 32544318853659` (Solar) → fixed to `1900001769264` (Support)

This caused kickoff tickets to appear in the Solar team's Zendesk inbox.

### Fix 2 (2026-04-29) — Timing Gap
Original Snowflake-first trigger fired BEFORE the Zendesk Acquisition ticket existed, causing kickoffs to be sent without cross-links. Redesigned to Zendesk-first (Trigger 1) with Snowflake safety net (Trigger 2, later deleted).

### Fix 3 (2026-05-22) — On Hold Re-Verify
Zendesk was occasionally flipping Acquisition tickets back to Open immediately after Trigger 1 set them to On Hold. Added a re-fetch and re-correction step as the final action in both `create_and_link` and `cross_link_only` flows.

### Trigger 2 Deletion (2026-05-22)
Analysis showed the Snowflake safety net was unnecessary — the Solar team reliably creates ZD Acquisition tickets. Replaced by Trigger 4 (passive alert to Hannah vs. auto-sending emails).

---

## Important Context

- **Kickoff tickets belong to Jess/Britt, NOT the Solar team.** The Solar team has their own inbox and should never see kickoff tickets.
- **The correct form is CEP Email** (`13386574321179`). Solar Transaction Coordination (`14088199798683`) is the wrong form and causes tickets to appear in the Solar team's inbox.
- **The correct group is Support** (`1900001769264`). Never use the Solar group (`32544318853659`) for kickoff tickets.
- **Kickoff emails send from support@opendoor.com** (not solar@opendoor.com) — intentional, prevents seller replies routing to Solar team inbox.
- **Seller replies create new tickets** in the general support queue — expected behavior, Assignment Safety Net auto-corrects within 15 min.
- **Solar Transaction Coordination-create_ticket_from_incoming_email** ZD trigger is intentional — handles inbound emails to solar@opendoor.com, do not modify.
- **Zendesk search is unreliable for multi-condition tag filtering** — always use Python-side filtering when matching on multiple conditions.
- **Inbound Solar TC tickets** (e.g., title companies emailing solar@opendoor.com) will NOT match as ZD Acquisition tickets — they use the wrong form, wrong group, and have no flip token populated. This is expected and correct behavior.

---

## Pending Item (Zendesk Admin)

Recommended but not yet confirmed created:
- **Trigger:** `Solar Kickoff - Ensure CEP Email form on create`
- **Condition:** Ticket created + Subject contains "Solar Documentation Needed" + Form ≠ CEP Email
- **Action:** Set form → CEP Email (`13386574321179`)

---

*Last updated: 2026-06-08 by Solar Kickoff Agent (Gumloop)*
