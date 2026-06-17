# cx-knowledge -- Acquisition Support Reference

> Distilled from Acquisition Training / Transaction Management deck. Covers transaction lifecycle, HSA task types, settlement statements, LCO rules, solar process, HOA demand review, state nuances, entity/legal, and seller-facing scripts.

**Source:** Google Slides `1BXrnrP9rOYiSeRTyTja4c5QvNDT62RjzjppcgXXtKRs`
**Last Updated:** March 3, 2026

---

## 1. Transaction Lifecycle

### Pre-Closing

| Team | Responsibility |
|------|---------------|
| **TM (Transaction Management)** | Send earnest money 3 days after contract. Check if home has solar. |
| **TM Support (Chennai)** | Assist TM with documentation, validations, post-close tasks. |
| **HOA Ops** | Review HOA demand. Verify no litigations, violations, or special assessments. |
| **OSN TCs** | Send Outside Title intro emails. Request and review Phase 1 docs. |
| **HSA** | One required task: Confirm seller is a U.S. citizen (FIRPTA) for tax purposes. Contact title to confirm if closing is being delayed. |

**Pre-closing navigation:** CITY To-dos > Transaction Tasks > Due Date Past

### Closing

**Signing:**
- TCs sign on behalf of Opendoor for real estate transactions (corporate purchases -- no single buyer, designated authorized signers act on behalf of entity).
- Docs requiring notary block, shipping label/mailing, or wet-sign per lender request are submitted via Slack `#notary-signing-channel` > "Resale Signing Request."
- After signing: docs received (in progress) > signed, scanned, uploaded > TC uploads to TOWN, sends to title, marks complete.

**Settlement Statement Review:** See Section 3.

**Sending Signed Docs:**
1. Upload signed documents into Admin.
2. Verify Digital Checkout / Late Checkout status.
3. Use correct macro when sending back.

**Send Wire:**
- Verify amount on Settlement Statement before sending (listed under "amount due from borrower").
- Input the amount and hit "Initiate Wire."

### Post-Closing

**Final Documents:**
- After closing, final documents are received. If not received, request from title.
- Use macro "Assign to TC Transaction Support (Chennai) - Acquisition" to forward emails to TM Support Team.
- TM Support Team closes and validates the home in TOWN.

**First Day Walk:**
- After close, HPMs do their first day walk to assess the home.
- Post-closing escalations handled by HSAs, T&E, and Voice of the Customer Team (VOC).

**Validations:**
- Final step after title confirms closing (Phase 2 for OSN).
- **Required docs:** Final Settlement Statement (must be stamped FINAL or have 3 signatures: buyer, seller, escrow) + Deed (only Warranty Deed or Grant Deed accepted).
- Upload both to Admin > Documents tab under "Final Settlement Statement" and "Deed."

**Steps to Close & Validate:**
1. Verify COE is within 24 business hours (if not, submit Validation Workflow in `#tm-questions`).
2. In Admin > Closing + Validation > Start Closing Process.
3. Confirm FSS details match > input Closing & Disbursement date > select Close Transaction + Validate.
4. Add note in Listing Offer Notes: "Closed + Validated per FSS/Deed COE [date]"
5. If pending docs: "Closed, but not validated per [reason]."

**If Docs Missing:**
- Close in Admin > select Skip Validation & Close.
- Add note and follow up with title for FSS/Deed.
- Do NOT reopen SOLD properties. Use Closing Validation Update Requests Sheet or file a bug.

---

## 2. HSA Task Reference

### How to Find and Claim Tasks

**Navigation:** CITY > To-dos > left sidebar > Under "Assigned To" select the HSA name > Search through and claim tasks.

**Viewing Claimed Tasks:** In To-dos, under "Assigned To" uncheck EPs and select "Me" (or another individual's name for coverage). Complete tasks via ellipsis > "Complete Task."

**Tasks to Claim:**
- Assessment Failure
- Acquire Septic Inspection
- Get Corrected Land Survey
- Confirm Utilities & Disclosure Info
- Alert: Tenant-Occupied Home
- Set up Late Checkout for Homebuilder Customer
- Confirm Closing is on Track
- Review Digital Checkout Results (COE in Future)
- Review Digital Checkout Results (COE Same Day)
- Follow up on Overdue Digital Checkout
- Follow up on Overdue Digital Checkout from Late Checkout
- Initiate the Solar Escalation Process
- HOA Violations

---

### Assessment Failure

**Description:** In-Person Walkthrough (IWT) was unable to be completed by the HPM and needs to be rescheduled.

**Action:**
1. Contact the customer and reschedule the IWT through CITY.
2. Navigate to Assessments tab > Click "+ Add" > Select "In-person walkthrough" > Select available time slot > Click "Schedule."
3. Leave notes regarding any specific instructions from the customer.

**IWT Expectations to Set:**
- Interior and exterior walkthrough.
- Assessment windows: 8-12 or 12-4 (local time).
- SMS + Email reminder sent prior.
- HPM visit ~30 minutes.
- Someone 18+ must be at property to provide access.
- All utilities must be on.
- If vacant, seller may provide access instructions.
- Gates must be unlocked. Pets must be inside.

**Script:**
> Hi [CX Name], I'm reaching out because our team member was unable to complete the in-person walkthrough at your home today. In order for Opendoor to make an offer on your home, we will need to reschedule the visit. Please let us know if there is another day that would work for you between either 8-12 or 12-4. Thank you!

---

### Acquire Septic Inspection

**Description:** Customer has a septic tank -- must confirm it is in working condition to proceed with acquisition.

**Action:**
1. Reach out to customer via email/phone asking for septic certification/inspection documents.
2. Use macro in saved replies: "Request for Septic Inspection Docs."
3. Upon receiving documentation: File "Septic Inspection Review" Zendesk ticket in CITY. Attach the seller's documentation.
4. HOC team reviews the documentation. If HOC is not auto-assigned, change "Assignee" to HOC.

**Key Details:**
- Septic certification/inspection should typically be less than 12 months old.
- Document must show system is in working order.

**Outcomes:**
| Result | Action |
|--------|--------|
| **Septic PASSED review** | Clear to move forward. No further action needed. |
| **Septic FAILED review** (+ reason) | Seller must supply updated documentation with required tests AND/OR failing tests must now show "passed." System must be proven fully functional. Must be completed by COE or Opendoor may cancel. Contact seller via phone and email with results. |

**Script:**
> Use macro "Request for Septic Inspection Docs" in saved replies.

---

### Corrected Land Survey

**Description:** A land survey was provided to title but is either too old or has information missing. A new one is needed before closing.

**Action:**
1. Reach out to customer via email/text asking for a new land survey with item/info noted in the task description.
2. New survey must be submitted to title team for review and approval before closing.
3. Close task manually.

**Script:**
> Hi [CX Name], I'm reaching out on behalf of our title team. They let us know the land survey provided is missing [fill in from task details]. In order for them to move forward with closing, you will need to provide a new survey with that information included. Please feel free to reach out to them directly at [insert email address from CITY] if you have any additional questions. Thank you!

---

### Confirm Utilities & Disclosure Info

**Description:** Customer has not filled out utility and disclosure information on their dashboard before COE.

**Action:**
1. Text and email the customer to remind them to fill out info before closing.
2. Copy & paste the dashboard link for easy access.
3. Task should auto-close once customer completes all information. Double-check task completion.

**How to Get Dashboard Link:**
CITY > Property Transaction page > vertical ellipsis "..." > Select "Copy Dashboard."

**Script:**
> Hi [CX Name], it looks like we're missing some details on your dashboard about the home's utilities and some information for the next buyer of the home. Please use the link below to provide this information as soon as possible before closing. Thank you! [PASTE LINK]

**Utilities Support:**
- The Utilities Team (Divya, Chennai) uses `#utilities-support` to request info on incomplete utility service (sewer, water, gas, trash).
- They tag `@hsa-tc-task-force` when they need HSA help.
- HSA calls/texts/emails the seller to gather required info, then follows up with Utilities Team by threading on their original request.
- Note: Divya also uses this channel to inform if utilities were not switched over to the buyer on Resale.

---

### Tenant-Occupied Home

**Description:** Customer has indicated on their dashboard that the home is occupied by a tenant.

**Action:**
1. Cancel LCO (if applicable).
2. Notify customer that LCO is cancelled due to tenant occupancy policy.
3. If no LCO previously set up: leave note in CITY indicating customer disclosed tenant-occupied home, close task.

**How to Cancel LCO:**
CITY > Property Transaction Page > Checkout Tab > Scroll to "Late Checkout" section > Click "Cancel LCO" > Note LCO cancelled due to tenant > Slack title to inform them.

**Key Rule:** Tenant-occupied properties are NOT eligible for LCO.

**Script:**
> Hi [CX Name], you recently disclosed the home you're selling to Opendoor is being occupied by a tenant. Given Opendoor is not the tenant's legal landlord, our late checkout option is not available for homes that have tenants in place. We have cancelled the late checkout stay and your tenant will need to move out of the home before our scheduled closing date. If the tenant needs more time, we do give the option to extend closing up to 60 days. Please let us know if you need to make any changes.

---

### Confirm Closing

**Description:** Populates 3 days before COE to confirm property is on track for closing.

**Action:**
1. Go to proper title channel in Slack.
2. Cmd+F search for the property address.
3. If thread exists: continue in that thread. If not: start a new one.
4. Ping the escrow officer noted in Participants in CITY.
5. Include property address. Ask if clear to close/on track for COE date.
6. Leave note in CITY: "Reached out to title to confirm closing on track [INSERT SLACK LINK TO MESSAGE]"

---

### Digital Checkout (DCO)

**Description:** Review the Digital Checkout photos provided by the customer.

**Action:**
1. Review photos for debris, furniture, or personal items left in home.
2. Extra paint and flooring tiles in garage are OK. No large furniture or excessive cleaning supplies.
3. If photos look good: Approve DCO.
4. If photos show issues: text customer requesting photos showing items removed, or request additional/missing photos.
5. If customer is leaving items behind: create manual task for EP to escalate to Homes.

**DCO Approval Steps in CITY:**
1. Click on task (opens transaction page, Checkout tab).
2. Scroll down to photo reel, click first photo.
3. Arrow through all photos to ensure no personal items.
4. If clear: click "Approve Digital Checkout" button.
5. Pop-up confirms -- click "Approve."
6. Leave note in CITY: "Approved DCO."
7. Auto-email goes to title company approving DCO and they release funds.

**Scoping Review:**
- If large items appear in DCO photos, check CITY > Assessments tab to see if items were scoped during assessment.
- If unsure, reach out to HPM in `#acq-homes-escalations`.

**Scripts:**
> Hi [CX Name], thank you for submitting your digital checkout photos. It looks like there are [name items remaining in home] in some of the pictures provided. Can you text over a photo showing they've been removed so there's no delay in closing today? Thank you!

> Hi [CX Name], thank you for submitting your digital checkout photos. It looks like the living room photo was provided twice and we don't have a photo of your primary bedroom. Can you send that over as soon as possible so we don't have any delays in closing? Thank you!

---

### Overdue Digital Checkout

**Description:** Customer has not submitted DCO by midnight (12 AM) on COE date.

**Action:**
1. Open task.
2. Text customer to follow up on ETA of move-out photos.
3. Provide dashboard link for easy access.
4. Once DCO submitted, approve per usual process.
5. If photos not received before wire cutoff with title/escrow, COE moves to following day.
6. If customer can't get dashboard to work, they can text photos in alternatively.

**Script:**
> Hi [CX Name], I'm following up on your move out photos. We will need them this morning to ensure there are no delays in your closing. If we do not receive them ASAP we will not be able to fund. Please let me know if you need any help, here's the link to your dashboard to submit them. [PASTE DASHBOARD LINK FROM CITY]

---

### Debris Left in DCO

**When items are questionable:**
1. Confirm with seller if they are removing items. If not:
2. CITY > "Contract Change" dropdown > "Request Approval - Other" > submit for HSA Manager approval.
3. For customers not yet closed: send addendum for seller credit to buyer.
4. For customers in LCO: "Update Withholding" amount.

**Posting an Addendum:**
1. Click Contract Change dropdown.
2. Select "Create generic addendum."
3. Enter addendum title and verbiage.
4. Click "Save and send addendum."
5. Slack title to inform them of credit to buyer so they update Settlement Statement.

---

### Approving DCO Without Photos

**Rare situations** where DCO may need to be "turned off":
- Seller texts/emails photos directly.
- In-person walk of the home is performed.

**Steps:**
1. Go to DCO tab and turn off DCO.
2. Go to closing dashboard (no impersonation needed) and fill out: lockbox location (check photos if sent), phone number (match to profile), check declaration, click submit.
3. Go back to DCO tab and click "Approve" if photos look good or HPM approval received.

---

### Late Checkout (LCO)

See Section 4 for full LCO rules and rates.

**Approving LCO in CITY:**
1. Click on task (opens Checkout tab).
2. Scroll to photo reel, click first photo.
3. Arrow through all photos for personal items.
4. If clear: click "Approve Digital Checkout."
5. Pop-up confirms -- check box "Complete LCO."
6. Click "Approve."
7. Leave note in CITY: "Approved LCO."

**Overdue Late Checkout:**
- Populates if customer has not submitted DCO by 5pm on their final LCO day.
- Text customer to follow up. Provide dashboard link.
- If customer will be delayed: charge overstay rate of $750/day (see Overstay section).

**Overdue LCO Script:**
> Hi [CX Name], I'm following up on your move out photos, they were due at 5pm yesterday upon moving out. We will need them ASAP this morning to ensure there are no delays in your closing. Please let me know if you need any help, here's the link to your dashboard to submit them. [PASTE DASHBOARD LINK FROM CITY]

---

### Homebuilder LCO

See Section 4 for Homebuilder LCO rates.

**Description:** Most homebuilder customers need to close on existing home to finance new build. Opendoor offers 2 free days of LCO.

**Action:**
1. Text customer to find out if they want to use LCO days.
2. If yes: set up LCO and close task manually.
3. If no: note in CITY and close task manually.

**Script:**
> Hi [CX Name], I just wanted to check in as we get closer to your closing date to confirm if you want to set up late checkout (post-possession) to help smoothly transition into your new home. As a reminder if you utilize this program, we provide 2 free days after closing and hold back a refundable deposit of $2k in escrow. The $2k is refunded once you've provided your move out photos of the home confirming it's vacated. If you need additional time, we can also do up to 17 days for an additional daily cost. Let me know if you'd like me to get that set up for you.

---

### Solar Escalation

See Section 5 for full solar process.

---

### HOA Violations

See Section 6 for full HOA demand review and violation handling.

**When you receive an HOA Violation Ticket:**
1. Review ticket for all necessary details.
2. Understand the violation and customer options:
   - 30+ days from COE: customer must resolve themselves.
   - <30 days from COE: customer can resolve, or OD can resolve for a cost.
   - Already in scope and confirmed covered by OD.
3. If unclear, ask the HOA Violations team before reaching out.
4. Call customer within 24 hours of receiving the HOA Violation To-Do.

**Creating an HOA Ticket (if none exists):**
- First check CITY Property Page (not transaction page) for existing tickets.
- If related ticket exists: leave internal note with additional info.
- If no related ticket: CITY > Overview Page > "+To-Do" > Create Ticket > HOA Violations > Describe the violation > Click "Create."

**Parent/Child Ticket Structure:**
- Parent ticket: assigned to HOA Violation Team, has multiple branches.
- Child ticket: what HSAs are tagged in. Not created until HOA Violation team has heard back from side conversations with HOA Ops and budget review.

**Closing HOA Tickets:**
HSAs cannot solve HOA tickets directly (required fields: HOA Disposition, Priority, On-Hold Action). Leave internal note:
> Hi @operator! Looks like we've got this ticket resolved, however, I am unable to close the ticket due to these required fields (HOA Disposition, Priority, and On-Hold Action). I am re-assigning this child ticket back to you, can you please update the required fields and close out the ticket for the both of us? Thanks!

**HOA Violation Call Script:**
> Hi [Customer Name], I was just reaching out because our team has informed us that your HOA has reported a violation for "XXX." Are you aware? OK, good / Sorry to be the one to inform you. We would need this to be resolved before you close on the home on [COE DATE].
>
> We have two options for addressing this:
> 1. Opendoor can resolve the violation once we own the home, but we would request a $$$$ credit to cover the cost of remediation.
> 2. You can address the violation yourself, provided that the HOA provides documentation confirming the violation has been cleared at least three days before the close of escrow date.
>
> Which option do you prefer?

**"That's not in the contract" Objection Response:**
> I can appreciate you bringing this up. There are a few reasons the HOA and Opendoor require the violation(s) to be cleared before closing on the home. In a normal real estate transaction on the open market, buyers typically expect a smooth transition, including the resolution of any issues related to the property. Opendoor follows this same norm and requests that the HOA provides a clearance letter or similar documentation, confirming that all issues have been addressed, as homes with unresolved issues tend to lead to additional costs and complications. Without resolution, the sale could be delayed or even blocked.

---

## 3. Settlement Statement Review

### What is a Settlement Statement?

- Lists all charges and credits to buyer and seller.
- Breaks down closing costs, dues, and concessions.
- Includes HOA fees, tax bills, prorations, etc.

### Information Data to Verify

- Property Address
- Opendoor Purchasing Entity
- Settlement & Disbursement Dates

### Financial Data to Verify

| Category | What to Check |
|----------|---------------|
| **Deposits, Credits, Debits** | Headline Price (Debit), Earnest Money (Credit), Fees, Repair Credits, Other Credits |
| **Prorations** | HOA prorations: start date should match COE (check HOA recap in Address Notes). Tax prorations: check Tax Certificate for what's been paid for the year. Utilities (sewer/water): may appear but do NOT need to verify. |
| **Commission** | Compare instructions to SS. Include Retail Partnerships (Redfin, Zillow, etc.). Solar payoffs if applicable. Ignore OD Brokerage Payment 0.25%. Verify using Commission document. |

### Revised Docs

Title may send revised closing docs before or after closing. Always review and verify before signing.

**Common reasons for revised docs:**
- New COE / Disbursement date
- Corrected line item (seller credit, title fee, commission, HOA fee)
- Fee on seller's side updated
- Title forgot to add a document to the original package

**Always** leave a note in Admin (e.g., "Sent revised lender doc w/ link" or "Sent revised docs to Title").

---

## 4. Late Checkout (LCO) Rules

### Rate Summary

| Product | Free Days | Daily Rate | Deposit | Max Timeline |
|---------|-----------|------------|---------|-------------|
| **Core** | 1 | Varies by property | $4,000 | 17 days |
| **Agent Acq / ORE** | 1 | Varies by property | $4,000 | 17 days |
| **Homebuilder** | 2 | Varies by property | $2,000 | 17 days |

### Key Rules

- **Tenant-occupied properties are NOT eligible for LCO.**
- LCO/DCO is due by 5pm on last day of occupancy.
- Opendoor will NOT issue a refund for any unused LCO days.
- Maximum LCO period: 17 days. No extensions beyond this timeframe.

### Changing LCO Date After COE

If a seller already enrolled in LCO wants to use more days:
1. In CITY Checkout tab: select "Update move-out date."
2. Select the new expected move-out date and enter the overstay amount.
3. This automatically updates the withheld deposit amount.
4. Customers are charged **$750 per day** past the original LCO date.
5. Note in CITY how many extra days used and how much withheld from deposit.

### Overstay Rules

**Pre-COE (customer requests longer LCO before closing):**
- DO NOT escalate to Resolutions.
- Work with customer to extend their Late Checkout Agreement within 17-day max.
- Ensure customer signs updated agreement.

**Post-COE (customer cannot leave by end of LCO period):**
- You may grant extension without Manager Approval for up to as many days as the security deposit accommodates.
- Each day is charged the **Overstay Rate ($750/day)**, NOT the normal daily rate.
  - Core ($4K deposit) = up to 5 extra days at $750/day
  - Homebuilder ($2K deposit) = up to 2 extra days at $750/day
- Inform customer and adjust LCO date in Admin. Record notes.
- Withhold total overstay charge from security deposit and complete DCO steps.

**Overstay Rate Reduction:**
- In extenuating circumstances (weather, illness, moving issues), HSA can escalate for EP Manager approval to charge daily rate instead of $750.
- CITY > "Request approval - other" under Contract Change dropdown. Include context.
- Use sparingly.

### Maxed-Out Security Deposit

If customer still has not vacated after entire deposit is consumed:
1. File a Jira ticket with the **Resolutions Team** (Consumer Resolution - Core).
2. Resolutions will send a "Fact Log" -- fill it out ASAP.
3. Email customer using "LCO Overstay - Resolutions Handoff" macro in Zendesk.
4. Resolutions Team takes over all communication with the seller.
5. No further action needed unless Resolutions contacts you.

**Set expectations clearly:**
> If you have not vacated the home by [Date], our Resolutions Team will step in and pursue further actions.

### Overstay Flow Summary

```
Customer needs more time
  |
  v
Grant extension (up to deposit limit at $750/day)
  |
  +-- Customer vacates --> Withhold $ from deposit, complete DCO
  |
  +-- Customer does NOT vacate --> Escalate to Consumer Resolutions
       Resolutions takes over communication until further notice
```

---

## 5. Solar Process

### Overview

When a property is identified as having solar panels, a Solar Escalation ticket must be created for tracking. The process involves both the HSA/EP and the Solar Team.

### Solar Escalation Workflow

**Step 1: Create Solar Escalation Ticket**
1. CITY > Overview tab > Click "+ Add" on right side.
2. Select "Solar Escalation Acquisition" from dropdown.
3. Complete information based on what was collected from the seller.
4. If any info is unknown, input "unknown" (Solar Team will follow up with EP).
5. Click "Create" -- redirects to the created ticket in Zendesk.

**Step 2: Send Solar Kickoff Email**
1. CITY Participants section > click envelope icon next to customer name > "Confirm" to open email in Zendesk.
2. Under "Apply Macro" dropdown (bottom left), select "Solar Kickoff Email" from Saved Replies.
3. Ensure it is a **Public Reply** (so it reaches the customer).
4. Select "Pending" when sending (enables proactive follow-up).

**Step 3: Notes Process (as of 1/26/26)**
1. When you receive the Solar ticket prompting kickoff, open the CITY page and send the kickoff email.
2. Copy the kickoff link back into the Solar ticket and send/update to the team.
3. Leave an **internal note on the customer message page** including kickoff link and cross-references (Solar ticket + customer kickoff ticket).
4. Key: Internal notes on customer message page auto-post to CITY/property page. Notes on the Solar team ticket alone do NOT.
5. Mark solved and refresh CITY page to confirm note is showing on the property.

### Solar Team Roles

| Solar Team DOES | Solar Team Does NOT |
|-----------------|---------------------|
| Log all solar workflows in channels | Interact with the customer |
| Call solar companies | Initiate payoffs or transfers with solar company (seller's responsibility) |
| Work with title on solar payoff | |
| Approve solar to title in emails/Slack | |

### Solar Follow-Up Best Practices

- Follow up **WEEKLY** with customers on solar items (create custom to-dos).
- Make clear each time: we cannot close without all required documents.
- Submit ZD Solar Escalation Ticket and send Kickoff Email immediately after contract.
- Provide update on every follow-up within the ZD Solar Ticket (even "no update received").
- Do NOT tag Russell directly.
- Keep all updates within the ZD Solar Escalation Ticket (not Slack).
- If assisting on someone else's ticket, complete the entire task or leave detailed internal ZD notes.

### Required Solar Documents

**No exceptions.** If customer cannot provide all required docs, they must:
1. Remove solar (themselves) and have OD assess the roof condition prior to COE, OR
2. Cancel the contract, OR
3. Delay COE and try to obtain documentation.

### Provider-Specific Nuances

#### Sunnova (formerly Sunstreet)
- Opendoor **cannot** purchase unless customer has completed a full **buyout** of the solar system.
- Buyout process: minimum 30 days.
- **Buyout is NOT the same as pre-paying** or paying remaining lease balance. Pre-paying does not absolve lease terms. Sunnova lease terms do not allow transfer to an entity (Opendoor).
- Buyout absolves lease terms and allows warranty transfer to Opendoor.
- **Required to close:**
  - Documentation showing balance paid + date
  - UCC3 Termination of the lien
  - Bill of Sale

#### Tesla / Sunrun
- Two of the top three providers.
- Process usually takes less than 30 days.
- Seller must request the purchase payoff while providing the buyer's (Opendoor's) contact information.

#### Out of Business Solar (OOB)
- **Required:**
  - Statement showing panels have $0 owed and customer owns rights.
  - Proof of function: recent electric bill (entire bill, no screenshots, not cropped) showing solar generation, OR 3rd-party inspection report from licensed electrician/solar tech.
- **Nice to have:** Agreement/Warranty.
- If customer cannot provide everything: must remove panels prior to COE or cancel contract.

#### New Builds (Solar Included at Purchase)
- **Agreement/Warranty:** If no agreement, manufacturer warranty may suffice. Sometimes neither available.
- **Payoff:** Most likely included in mortgage. Seller can provide new build contract showing solar was included.
- **Proof of function** required.

#### Previous Owner Purchased
- **Agreement:** Difficult to obtain. At minimum, need name of the system. If installed by builder/subcontractors with no Solar Agreement signed, require proof of function.
- **Warranty:** Difficult to obtain for same reasons.
- **Payoff:** Official zero-balance doc, OR final settlement statement listing solar provider/lender, OR email from provider stating account paid in full. Do NOT rely on Title Commitment or clean lien search (providers/lenders not obligated to report active liens, especially under previous owner's name).

#### Pool / Water Heater / Condenser Unit / Attic Fan / DIY Solar
- Payoff documentation
- Picture of panel system
- Any other information/documentation concerning the system

### Market-Specific Solar Nuances

| Market | Nuance |
|--------|--------|
| **Dallas (DFW)** | Opendoor will charge ALL DFW customers for removal of solar panels from the roof. |
| **Las Vegas (LAS)** | Solar documentation must include kWh (power generated/capacity) AND installation date of panels. |
| **All Markets** | If customer opts to remove panels: must provide letter from solar company authorizing removal. Panels removed prior to COE. Homes must inspect roof for damage prior to COE. |

### Cash Plus Solar

If the property is Cash Plus, ping **Jacob Griffith** and leave him the ticket to complete.

---

## 6. HOA Demand Review

### 8-Point Self-Checklist

When reviewing an HOA demand, verify all of the following:

| # | Item | Details |
|---|------|---------|
| 1 | **HOA Name** | Identify the HOA. |
| 2 | **Management Company** | Is there one? What is their name? Self-managed? (May not be obvious -- read through demand carefully.) |
| 3 | **HOA Dues** | How much? What frequency? (Formats vary across demands.) |
| 4 | **Account Balance** | Is there a balance? Balances must be paid off on or before COE. ACQ side = seller responsible. RSL side = OD responsible. Credits shown in parentheses, e.g., ($145.00). |
| 5 | **Violations or Litigations?** | See violation/litigation ticket process below. If demand does not specify, reach out to title for confirmation. |
| 6 | **Demand Freshness** | Is it outdated? Most good for 30 days from COE unless stated otherwise (some 90 days). If outdated, need updated demand before COE. |
| 7 | **Special Assessments** | Flag to TC. Leave note in Admin with demand review note and ZD ticket for assigned TC (found in Admin under "ACQ Fulfillment"). |
| 8 | **Other Fees** | Disclosure fee, transfer fee, new account fee, working capital, reserve contribution, initiation, etc. |

### HOA Demand Review Note Template

Leave this in Admin when completing the demand review:

```
HOA REVIEW
Data Input Complete: YES
Frequency: [quarterly/monthly/annual]
Seller Balance/Credit: [amount or none]
Litigation: [yes/no + details]
Violation: [yes/no + details]
```

### TOWN Data Entry Steps

1. Locate property in TOWN with flip token or address.
2. Click property address (opens property details page). Note: clicking flip token opens Admin.
3. Scroll down and click "Add another HOA." Type HOA name and save.
4. Select three dots in upper right > Edit Details.
5. Verify Association Type = "Home Owner Assoc."
6. Verify "Association Mandatory" = "Yes."
7. Add HOA dues by selecting "Add a Standard Fee."
8. Read demand for other fees. Fees without specified frequency: label as "One-Off."
9. Note: Seller balances/credits are NOT inputted into TOWN (not recurring, vary by owner).
10. Add Management Agency: click "Add Agency" > search name > verify correct state.
11. Verify all contact information. Confirm "Association Type" = "Management Agency."
12. Validate by selecting "Validate HOA" in top right corner (for both HOA and Management).

**Reminders:**
- HOA section: ONLY fees.
- Management section: ONLY contact info.

### Violation Ticket Process (TOWN)

1. Pull up property in TOWN using flip token or address.
2. Select three dots to the right of notes section.
3. Select "Create a ticket."
4. Select "HOA Violation" from the ticket form dropdown.
5. Address auto-populates. Leave description of violation.
6. Submit. Ticket populates in ZD.
7. Include ZD link in your demand review note.

**If demand does not specify violations:**
- Reach out to title via ZD ticket for confirmation: "Can you please confirm there are no violations on the property as the demand provided does not specify. Thank you."
- Use **Public Reply** in ZD (internal note will NOT reach title).

### Litigation Ticket Process

1. Select three dots > "Create a Ticket."
2. Select "HOA Litigation" from dropdown.
3. Copy/paste litigation description from demand. (Some companies send litigation reports separately.)
4. Ticket goes back to TC to determine if deal can proceed.

---

## 7. State-Specific Nuances

### State-Specific Required Documents

In addition to standard 3 documents (Final Settlement Statement, Deed, and standard package), some states require extra:

| State | Additional Required Docs |
|-------|-------------------------|
| **Florida** | Lien Search |
| **Texas** | Land Surveys |
| **California** | NHD Reports |
| **Colorado** | HOA Insurance |

### Florida

**Open Permits:**
- TC ensures lien search is on file and completes TOWN task.
- Title works with seller to resolve liens/permits.
- No purchases with open permits. No Hold Harmless agreements allowed.

**HOA Buyer Applications:**
- OD = corporation (not individual) -- issues with HOA approval process.
- Handled by HOA Squad (Phoenix).

**Surveys:**
- Standard FL buyers obtain surveys; Opendoor opts out.
- If title asks: decline survey.
- May be required to sign Hold Harmless for no survey.

### New York & New Jersey

**General:**
- Contract attorney states. All docs must be drafted by attorneys. Buyer and seller each have their own.
- Attorneys handle inspections. 30-day COE rarely possible (delays common).

**NY Contacts:**
- Attorney: Ansell, Grimm & Aaron, PC (Jon Sherman -- Attorney, Meylin Zaks -- Paralegal).
- Title/Escrow: Fidelity (holds funds, main point of contact).

**NY Process:**
- EMD, Phase 1 docs, and HOA handled via Fidelity.
- 3+ days before COE: request and review Preliminary Statement.
- Attorney fees are normal on settlement statement.

**NJ Process:**
- Buyer must order HOA. Coordinated so Title orders and adds to statement.
- TC: make receipt once Title orders HOA docs.
- 3 days before COE: FSS must be approved by Ansell Grimm, OSN, and TC (via Fidelity).

---

## 8. Entity & Legal

### Entity / Financier Issues

**How to Identify Missing Entity/Financier:**
- Slack ping from Escrow Officer.
- Missing in Financial Details during EMD tasks.
- "Wire Transfers" shows Freeform Template Form.

**Fix:**
1. Notify **Michaela Fried** in `#tm-capm-comms` (include address + Admin Closing Tab URL).
2. Wait for update. Inform title once fixed.
3. Leave note in TOWN with comms links.

**Incorrect Entity:**
- Entities can change mid-transaction.
- If closing docs show wrong entity: title checks daily report.
- No addendum needed if docs match Admin.

### Opendoor Property Trust I

- Delaware statutory trust used to buy/sell property.
- Widely vetted and accepted by underwriters.
- Typically no need for extra docs (certificate of trust, resolution, etc.).

### LegalOps Escalation

- LegalOps = branch of Opendoor Legal Team.
- Common role: responding to Property Trust I inquiries.
- "Underwriting requirement" = document or title condition.
- Escalate to Team Lead/Manager if pushback continues. They determine if Legal Ops is needed.

### Entity Documents

- Sent to Outside Title at transaction start.
- If re-requested: check Entity Corporate Documentation Drive.

### Underwriter Inquiries

- When underwriter pushes back on entity documentation, escalate to Team Lead/Manager first.
- They assess whether LegalOps involvement is warranted.

---

## 9. Key Contacts & Channels

| Channel / Team | Purpose |
|----------------|---------|
| `#notary-signing-channel` | Submit docs requiring notary/wet-sign via "Resale Signing Request" |
| `#tm-capm-comms` | Entity/financier issues (Michaela Fried) |
| `#utilities-support` | Utility info requests (Divya, Chennai). Uses `@hsa-tc-task-force` tag. |
| `#acq-homes-escalations` | HPM/homes-related questions (DCO scoping, first-day walk issues) |
| `#tm-questions` | Validation workflow issues (COE outside 24 business hours) |
| Title channels (market-specific) | Confirm closing, title issues. Ping EO from CITY Participants. |
| **Solar Team** | Logs workflows, calls solar companies, works with title on payoffs. Do NOT tag Russell directly. |
| **HOA Ops** | Reviews HOA demands, verifies no litigations/violations/special assessments. |
| **HOA Violations Team** | Works parent/child ticket structure for violations. |
| **Resolutions Team** | Handles overstay escalations after security deposit is exhausted. Consumer Resolution - Core. |
| **TM Support (Chennai)** | Closes and validates homes in TOWN post-closing. |
| **LegalOps** | Property Trust I inquiries, underwriter pushback escalation. |
| **Michaela Fried** | `#tm-capm-comms` for entity/financier issues. |
| **Jacob Griffith** | Cash Plus solar tickets. |
| **Ansell, Grimm & Aaron, PC** | NY/NJ attorney (Jon Sherman, Meylin Zaks). |
| **Fidelity** | NY/NJ title/escrow -- holds funds, main contact. |

---

## 10. Message Templates

### Assessment Failure -- IWT Reschedule
> Hi [CX Name], I'm reaching out because our team member was unable to complete the in-person walkthrough at your home today. In order for Opendoor to make an offer on your home, we will need to reschedule the visit. Please let us know if there is another day that would work for you between either 8-12 or 12-4. Thank you!

### Septic Inspection Request
> Use macro in saved replies: "Request for Septic Inspection Docs"

### Corrected Land Survey
> Hi [CX Name], I'm reaching out on behalf of our title team. They let us know the land survey provided is missing [fill in from task details]. In order for them to move forward with closing, you will need to provide a new survey with that information included. Please feel free to reach out to them directly at [insert email address from CITY] if you have any additional questions. Thank you!

### Utilities & Disclosure Reminder
> Hi [CX Name], it looks like we're missing some details on your dashboard about the home's utilities and some information for the next buyer of the home. Please use the link below to provide this information as soon as possible before closing. Thank you! [PASTE LINK]

### Tenant-Occupied -- LCO Cancelled
> Hi [CX Name], you recently disclosed the home you're selling to Opendoor is being occupied by a tenant. Given Opendoor is not the tenant's legal landlord, our late checkout option is not available for homes that have tenants in place. We have cancelled the late checkout stay and your tenant will need to move out of the home before our scheduled closing date. If the tenant needs more time, we do give the option to extend closing up to 60 days. Please let us know if you need to make any changes.

### DCO Follow-Up -- Items Remaining
> Hi [CX Name], thank you for submitting your digital checkout photos. It looks like there are [name items remaining in home] in some of the pictures provided. Can you text over a photo showing they've been removed so there's no delay in closing today? Thank you!

### DCO Follow-Up -- Missing Photo
> Hi [CX Name], thank you for submitting your digital checkout photos. It looks like the living room photo was provided twice and we don't have a photo of your primary bedroom. Can you send that over as soon as possible so we don't have any delays in closing? Thank you!

### Overdue DCO
> Hi [CX Name], I'm following up on your move out photos. We will need them this morning to ensure there are no delays in your closing. If we do not receive them ASAP we will not be able to fund. Please let me know if you need any help, here's the link to your dashboard to submit them. [PASTE DASHBOARD LINK FROM CITY]

### Homebuilder LCO Setup
> Hi [CX Name], I just wanted to check in as we get closer to your closing date to confirm if you want to set up late checkout (post-possession) to help smoothly transition into your new home. As a reminder if you utilize this program, we provide 2 free days after closing and hold back a refundable deposit of $2k in escrow. The $2k is refunded once you've provided your move out photos of the home confirming it's vacated. If you need additional time, we can also do up to 17 days for an additional daily cost. Let me know if you'd like me to get that set up for you.

### Overdue Late Checkout
> Hi [CX Name], I'm following up on your move out photos, they were due at 5pm yesterday upon moving out. We will need them ASAP this morning to ensure there are no delays in your closing. Please let me know if you need any help, here's the link to your dashboard to submit them. [PASTE DASHBOARD LINK FROM CITY]

### HOA Violation -- Customer Call
> Hi [Customer Name], I was just reaching out because our team has informed us that your HOA has reported a violation for "XXX." Are you aware? OK, good / Sorry to be the one to inform you. We would need this to be resolved before you close on the home on [COE DATE].
>
> We have two options for addressing this:
> 1. Opendoor can resolve the violation once we own the home, but we would request a $$$$ credit to cover the cost of remediation.
> 2. You can address the violation yourself, provided that the HOA provides documentation confirming the violation has been cleared at least three days before the close of escrow date.
>
> Which option do you prefer?

### HOA Violation -- "That's Not in the Contract"
> I can appreciate you bringing this up. There are a few reasons the HOA and Opendoor require the violation(s) to be cleared before closing on the home. In a normal real estate transaction on the open market, buyers typically expect a smooth transition, including the resolution of any issues related to the property. Opendoor follows this same norm and requests that the HOA provides a clearance letter or similar documentation, confirming that all issues have been addressed, as homes with unresolved issues tend to lead to additional costs and complications. Without resolution, the sale could be delayed or even blocked.

### Overstay -- Resolutions Warning
> If you have not vacated the home by [Date], our Resolutions Team will step in and pursue further actions.

### HOA Ticket -- Close Request (Internal Note)
> Hi @operator! Looks like we've got this ticket resolved, however, I am unable to close the ticket due to these required fields (HOA Disposition, Priority, and On-Hold Action). I am re-assigning this child ticket back to you, can you please update the required fields and close out the ticket for the both of us? Thanks!

### HOA Violation Confirmation Request to Title
> Can you please confirm there are no violations on the property as the demand provided does not specify. Thank you.

---

## Cross-Reference Map

| Topic | Also See |
|-------|---------|
| City navigation, task types, entity schemas | `city-nav/SKILL.md`, `city-nav/DATA_MODEL.md`, `city-nav/UI_GUIDE.md` |
| Product FAQ, seller personas, objection handling | `cx-knowledge/DATA_MODEL.md` |
| State regulations, market nuances | `cx-knowledge/STATES.md` |
| Escalation routing, contacts, SLAs | `escalation-pathways/SKILL.md` |
| DV process, credit addendum, post-inspection | `cx-knowledge/DATA_MODEL.md` Section 5 |
| Subsidy requests | `subsidy-agent/SKILL.md` |
| Task sweeping, batch close | `city-task-sweeper/SKILL.md` |
