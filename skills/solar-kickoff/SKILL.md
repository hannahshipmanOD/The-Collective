---
name: solar-kickoff
description: >
  Automated Solar Kick Off email to sellers when an "Initiate Solar Escalation Process"
  task is created in City. Queries Snowflake for task, deal, and contact info, then
  creates a Zendesk ticket via create_ticket that sends the email to the seller.
  Run as a recurring cron every 15 minutes.
---

# Solar Kick Off — Automation

Trigger: `task_type = 'initiate_solar_escalation'` open in City (Casey)
Action: Send Solar Kick Off email to seller via Zendesk (`solar_tc` form, `solar` group)
Dedup: Skip if a ZD ticket already exists for this flip with tag `solar_kickoff_auto`

---

## Cron Setup (run in Claude Code session after restart)

Paste this to start the automation:

```
Set up a recurring cron every 15 minutes to run the Solar Kick Off automation.
Use the solar-kickoff skill in The Collective for full instructions.
```

Or paste the full prompt below directly into a new session.

---

## Full Automation Prompt

```
Run the Solar Kick Off automation:

1. QUERY SNOWFLAKE for open solar escalation tasks:

SELECT
    t.UUID                      AS task_id,
    t.ACTIVE_AT                 AS task_created_at,
    ro.OBJECT_ID                AS flip_token,
    f.ADDRESS_FULL              AS property_address,
    h_tc.FULL_NAME              AS tc_name,
    l.EMAIL                     AS seller_email
FROM DWH.CASEY.DWH_TASKS_VIEW t
JOIN DWH.CASEY.DWH_RELATED_OBJECTS_VIEW ro
    ON t.UUID = ro.TASK_UUID AND ro.OBJECT_TYPE = 'flip'
JOIN DWH.DW.AX_FLIPS f
    ON ro.OBJECT_ID = f.TOKEN
LEFT JOIN DWH.DW.AX_FLIP_PARTICIPANTS p
    ON ro.OBJECT_ID = p.TOKEN
LEFT JOIN DWH.WEB.HUMANS h_tc
    ON p.ACQ_TC = h_tc.TOKEN
LEFT JOIN DWH.DW.AX_LEADS l
    ON f.ID = l.FLIP_ID
WHERE t.TASK_TYPE = 'initiate_solar_escalation'
  AND t.STATUS = 'open'
ORDER BY t.ACTIVE_AT DESC

2. FOR EACH TASK returned:

   a. DEDUP CHECK — search Zendesk for existing ticket:
      mcp__zendesk-mcp__search_tickets(
        query="flip_token:<flip_token> tags:solar_kickoff_auto"
      )
      → If any results found, SKIP this task (already sent).

   b. GET SELLER NAME — Snowflake does not store customer name reliably.
      Use City MCP: mcp__city-mcp__list_todos(query=<flip_token>) to get task,
      then get customer_id and call mcp__city-mcp__get_customer(customer_id)
      to retrieve seller's first name.

   c. POPULATE TEMPLATE — substitute into email body:
      - [Seller_Name] → seller first name from City
      - [Property_Address] → ADDRESS_FULL from Snowflake
      - [Assigned_Transaction_Coordinator's_Name] → tc_name from Snowflake

   d. CREATE ZENDESK TICKET:
      mcp__zendesk-mcp__create_ticket(
        requester_email  = seller_email,
        requester_name   = seller full name,
        subject          = "Action Required: Solar Documentation Needed for Your Opendoor Sale",
        body             = <populated template below>,
        form             = "solar_tc",
        group            = "solar",
        flip_token       = flip_token,
        property_address = property_address,
        tags             = ["solar_escalation", "solar_kickoff_auto"]
      )

3. LOG each ticket created (ticket_id, flip_token, seller_email, timestamp).
```

---

## Email Template

```
Hello [Seller_Name],

Our records indicate that solar is present on [Property_Address]. In an effort to ensure that closing stays on track, Opendoor will need the following documentation and information as soon as possible:

- Solar Company Name and any contact information
- Solar Agreement/Contract for the system
- Warranty Paperwork (usually included in Agreement/Contract)
- Payoff Documentation to pay at or before closing
- Account Transfer (if applicable)

Context
Opendoor requires that a solar system is owned. If purchasing the system is an option within a lease, then the seller is required to purchase the system. The seller is responsible for the full cost of any payoff. Opendoor is not able to proceed with closing without the balance being paid in full at close, or proof of a zero dollar balance.

Next Steps
The Payoff Documentation will need to be requested directly from the solar company, or loan provider, by the current owner. Opendoor cannot request this on the Seller's behalf and cannot close on the sale of the home without it. If electronic copies of the Solar Agreement and Warranty Paperwork are not available, it may be possible to request these along with the payoff. Once the documentation is obtained, please forward it here.

Please be aware that Opendoor will not be able to close on the sale of the home without the above documentation and information. Delays in receiving any of the above could also result in a delay in closing. Let us know if you have any questions!

Best,
[Assigned_Transaction_Coordinator's_Name]
```

---

## Zendesk Constants (from constants.py)

| Key | Value |
|-----|-------|
| Form: `solar_tc` | `14088199798683` |
| Group: `solar` | `32544318853659` |
| Dedup tag | `solar_kickoff_auto` |

---

## Notes

- `create_ticket` lives in `superdojo/services/zendesk-mcp/opendoor_zendesk_mcp/server.py` line 400
- Seller name is NOT in Snowflake — always fetch from City MCP `get_customer`
- TC name comes from `AX_FLIP_PARTICIPANTS.ACQ_TC` → join `HUMANS.TOKEN` → `FULL_NAME`
- Snowflake schema reference: `~/.claude/skills/opendoor-data/DATA_MODEL.md` (validated 2026-03-27)
- Cron is session-only — re-run setup prompt after each Claude Code restart
