---
name: solar-kickoff-email-template
description: The Solar Documentation Needed email template sent to sellers during kickoff. Activate when creating or reviewing the kickoff email sent via Zendesk.
icon: mail
color: Orange
related_server_ids:
- zendesk
---

# Solar Kickoff — Seller Email Template

## Subject
```
Solar Documentation Needed for Your Opendoor Sale - [Street Address Only]
```
_Street address = everything before the first comma in the full property address._

## Body

> Hi [Seller First Name],
>
> Thank you for choosing Opendoor to sell your home at [Full Property Address] — we're excited to work with you! As part of our standard process, we've noted that your property has a solar system and need to gather a few details to keep your closing on track. To avoid any delays, please share the following documents, for us to review, at your earliest convenience. You can simply respond to this e-mail.
>
> **Step 1: Provide Documentation**
>
> Please provide:
> - Name of the Solar Provider or Installer
> - A copy of your solar lease agreement or contract
> - Warranty paperwork (typically included in your original agreement or contract) and/or Payoff documentation
> - Account transfer information (if applicable)
>
> **Important to know**
> Opendoor requires that the solar system be owned — not leased — at the time of closing. If there is an outstanding loan balance on the system, it will need to be paid, in full, at or before closing.
>
> **Step 2 - Follow Up**
> Please reach out to us as soon as possible. You can respond to this e-mail.

## Field Notes

| Field | Source |
|---|---|
| `[Seller First Name]` | `DWH.DW.AX_LEADS.FIRST_NAME` via flip token. Falls back to "Hi there," if null. |
| `[Seller Email]` | `DWH.DW.AX_LEADS.EMAIL` via flip token. Set as `requester_email` on the kickoff ticket so the email goes to the seller. |
| `[Full Property Address]` | `DWH.DW.AX_FLIPS.ADDRESS_FULL` |
| `[Street Address Only]` | Everything before the first comma in `ADDRESS_FULL` |

## Sending Rules
- Sends **from support@opendoor.com** — intentional, prevents replies hitting Solar team inbox
- Ticket created with `status: solved`
- Zendesk auto-reopens if seller replies
- Dedup: check for existing `solar_kickoff_auto` tagged tickets matching street address before sending
