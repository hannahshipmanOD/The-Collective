# cx-knowledge — CX Knowledge Base Data Model

> Centralized knowledge base for ANY question an HSA/XA might encounter — product, process, state regs, objections, escalation. The first single source of truth for Opendoor CX operations.

---

## 1. Cash Offer (Sell Direct) FAQ

Source: Sell Direct Zendesk KB (Feb 3, 2026), Seller Experience slides (Feb 13, 2026), Business Model Training (Feb 23, 2026)

### How It Works

1. **Seller enters address** on opendoor.com → same-day preliminary offer
2. **Completes assessment** (ORVA, SSVA, Key App, or IWT) — flexible scheduling
3. **Final Offer** generated in 24-48 hours after underwriting
4. **HSA presents** net-cash-focused offer via Calendly-scheduled call
5. **Seller signs** → 15-day diligence period begins
6. **DV (Diligence Visit)** within 1-6 days, via Inspectify
7. **Close** in 7-60 days — flexible date, seller chooses

### Key Selling Points

- **Speed:** Close in as few as 14 days
- **Certainty:** Cash offer, no financing contingency
- **Simplicity:** No showings, no staging, no open houses
- **Flexibility:** Seller picks close date (7-60 day window)
- **No risk:** Cancel anytime at no cost per Opendoor Addendum
- **Opendoor pays closing costs** — typical seller closing costs covered

### Service Fee

- **Variable fee** presented as a **dollar amount** (NOT a percentage)
- XAs/HSAs should NEVER quote a specific percentage
- **Verbiage:** "Our service fee covers the transaction cost, operational costs while we own the home, and the market risk we take on."
- Three components: (1) transaction cost, (2) operational costs during ownership, (3) market risk
- Fee differs between Cash and Cash Plus products
- Seller sees fee as part of net proceeds calculation

### Timeline

| Step | Timeframe |
|------|-----------|
| Preliminary offer | Same day |
| Assessment | Flexible (seller schedules) |
| Final Offer | 24-48 hours post-UW |
| Contract signing | After FO call |
| DV | 1-6 days post-sign |
| Choose close date | 7-60 days from contract |

---

## 2. Cash Plus (Cash Now More Later) FAQ

Source: Cash Plus Zendesk KB (Dec 20, 2025), Cash Plus Initiative Hub (Feb 12, 2026), Cash Plus Cheat Sheet (Dec 17, 2025), Acquisition Cash Plus Charges doc (Feb 19, 2026)

### How It Works

1. **CP1 (First Payment):** Seller sells to Opendoor for cash upfront — ~75% of estimated sale price
2. **Opendoor renovates** and lists the home on the open market
3. **CP2 (Second Payment):** After home resells, seller receives additional proceeds (upside)
4. **CP2 window:** Up to 1 year from acquisition close (extended from 120 days)

### Key Terms

| Term | Detail |
|------|--------|
| **Earnest money** | $1,250 deposited with escrow agent |
| **Upfront cash (CP1)** | ~75% of estimated sale price |
| **Service fee** | "Opendoor Service Fee" — 0.1% to 3.1% variable |
| **CP2 timeline** | Up to 1 year after acquisition close |
| **Close timeline** | As early as 14 days |
| **Inspection period** | 15 days |
| **Cancel policy** | Cancel anytime before CP1 closes at no cost |

### Seller Guarantee

- Seller can **cancel anytime** before CP1 closes — no cost, no penalty
- If seller changes mind after CP1 closes: can **buy back** property for upfront cash amount + 3% processing fee
- EMD refunded 3-5 business days after cancellation

### Cash vs Cash Plus Comparison

| Feature | Cash Offer | Cash Plus |
|---------|-----------|-----------|
| Payment timing | 100% at close | ~75% at close + CP2 after resale |
| Upside potential | None | Yes — share in resale proceeds |
| Service fee | Variable (dollar amount) | 0.1-3.1% |
| Close timeline | 7-60 days | As early as 14 days |
| Cancel policy | Anytime, no cost | Anytime before CP1, no cost |
| EMD | Varies | $1,250 |
| Best for | Quick Closers, certainty-focused | Equity Optimizers, price-sensitive |

### How to Identify Cash Plus in CITY

- Both eligible: Shows "Cash & Cash+" options
- CP only: Shows only "Cash Plus" option
- Ineligible: Red "Denied" bar on Cash Plus line
- Pricing escalations: `#cash-plus-pricing-escalations`

---

## 3. Fees & Net Proceeds

Source: Service Charge Zendesk KB (Feb 3, 2026), Acquisition Cash Plus Charges doc (Feb 19, 2026)

### Service Fee Structure

The service fee is a **VARIABLE FEE** presented as a **dollar amount**. It covers:

1. **Transaction cost** — Title, escrow, closing, recording
2. **Operational costs** — Holding costs while Opendoor owns the home (taxes, insurance, maintenance)
3. **Market risk** — Risk of price decline between acquisition and resale

### How to Talk About Fees

**DO say:**
- "Our service fee is shown as a dollar amount in your net proceeds"
- "It covers transaction costs, operational costs, and market risk"
- "Many sellers find our fee competitive when you factor in no agent commission, no showings, and certainty"

**DON'T say:**
- Never quote a specific percentage (old 5% is deprecated)
- Never compare to "traditional 6% commission" directly
- Never say "service charge" — it's "service fee"

### True Cash Net Formula

```
Seller Net = Offer Price - Service Fee - Outstanding Mortgage - Liens/Judgments
```

For Cash Plus:
```
CP1 Net = Upfront Cash Amount - Outstanding Mortgage - Liens
CP2 Net = Resale Price - Opendoor Costs - Service Fee - CP1 Amount
Total Seller Net = CP1 Net + CP2 Net
```

---

## 4. Assessment & Final Offer Process

Source: FO Process Zendesk KB (Feb 3, 2026), Seller Assessment Journey doc (Oct 2025), EP Process Guide

### Assessment Paths

| Path | Method | When Used |
|------|--------|-----------|
| **ORVA** | Online Remote Video Assessment | Standard DTC path |
| **SSVA** | Self-Service Video Assessment | Self-guided option |
| **IWT** | Interior Walkthrough (HPM in-person) | Higher-value or complex |
| **Key App** | Opendoor Key App photo tour | App-guided self-assessment |
| **Exterior Only** | Drive-by exterior inspection | Special cases |
| **Offer Review Only** | No physical assessment needed | Low-risk properties |

### FO Generation

- **Timeline:** FO generated 24-48 hours after UW completes assessment review
- **FO held for HSA:** Shows as `final_offer_unreleased` in CITY
  - DTC: 48-hour hold for HSA outreach
  - Agent channel: FO released immediately, but HSA task still created
- **180-day reuse window:** If seller returns within 180 days, prior assessment can be reused

### FO Communication Rules

| Rule | Detail |
|------|--------|
| **XA must NEVER tell seller FO is ready** | When "Final Offer Unreleased" tag visible — route to HSA via Calendly |
| **HSA makes FO call within 24 hours** | Scheduled via Calendly link |
| **Follow-up every 48 hours** | Until contact or expiration |
| **As of Jan 23, 2026** | XAs should ONLY use HSA Calendly for actual FO calls, NOT 15-minute meetings |
| **FO is non-negotiable** | If seller believes something was missed, HSA can request Pricing Team second look |
| **4-hour contact rule** | Contacting within 4 hours = 2x conversion rate |

### FO Conversion Definition (Authoritative)

Source: Sales Conversion Metric Definition doc (Feb 4, 2026)

```
Conversion = Contracts Signed / FO Tasks Created (in period)
- Denominator: FO tasks created in the measurement period
- Numerator: Contracts signed from those FO tasks
- Cohorting: Numerator cohorted on FO task creation date
- Exclusions: Unique flip tokens per month only
- Settlement lag: 5 days after period end
- Filters: Channel, True Seller, Serious Seller
```

**Net Conversion** = FO Conv % × (1 - Withdrawal Rate)

---

## 5. DV & Post-Contract Process

Source: DV Zendesk KB (Feb 3, 2026), DV Credit Addendum doc (Feb 10, 2026), HSA Follow Up ALO & DV Training

### DV Overview

- **All DVs via Inspectify** as of January 6, 2026 (third-party inspectors)
- **Diligence timeline differs by product:**
  - **Cash (V21 Addendum, Mar 2 2026):** Seller has **5 days** from contract to schedule DV, visit must occur within **10-day window**. Seller can reschedule once within the window with 1 day's notice. If DV doesn't occur within 10 days, contract auto-cancels.
  - **Cash Plus / CNML:** Standard **15-day diligence period** from contract signing.
- **Scheduling:** Seller prompted on dashboard. If not scheduled within 6 days → reminder
- **Availability:** Inspectify available weekends, typically scheduled within 24-48 hours
- **HSA can schedule through CITY** if seller needs help
- **Buyer representation:** V21 base addendum no longer explicitly states "Buyer is unrepresented" in §3. CNML addendum still does. Both state Buyer has NO BROKERAGE RELATIONSHIP with Seller.

### DV Timeline

| Day | Action |
|-----|--------|
| Day 0 | Contract signed. DV Expectations SMS sent. |
| Day 1 | DV Expectations Call by HSA |
| Day 5 | Friendly reminder SMS (if reached on Day 1) |
| Day 7 | Halfway reminder SMS |
| Day 10 | Warning SMS |
| Day 13 | **URGENT** escalation call + warning SMS/email at 10 AM |
| Day 15 | **Auto-cancel** if DV not complete. Cancellation SMS + email. EMD refund 3-5 days. |

### DV Outcomes

| Outcome | Frequency | What Happens |
|---------|-----------|--------------|
| **Clear-to-close** | Most common | Contingencies released, move to close |
| **Offer adjustment** | Low | Credit addendum generated, seller reviews |
| **Walk** | Very low | Opendoor exercises walk right, deal cancelled |

### DV Credit Process — By Deal Type

The post-DV credit process differs based on whether the deal is New FO Prez Cash Plus vs. other deal types:

**New FO Prez + Cash Plus (DTC):**
Since all fees/charges come out of CP2, the DV credit also comes out of CP2. Cash Plus amounts are estimates, so **no addendum is required** — just notify the customer their estimates are changing.

1. Have the DV conversation with the seller — explain repair findings and additional cost
2. Send the customer an **email via Zendesk saved reply** (NOT an addendum)
3. Leave a note in City with the ZD ticket number
4. Done — no addendum, no diligence period pressure

The "Send Addendum" button in the Post-Inspection Call modal is **intentionally disabled** for New FO Prez deals (SELL-338). This is by design, not a bug.

**How to identify:** Check for the **"New Final Offer Prez"** tag on the transaction in City.

Step-by-step doc: [DV Process for New CP Experience](https://docs.google.com/document/d/1UL-PZLWeiTYQNubx7zrFUqm_XIYDVfnhkDEbozfMBr0/edit)

Source: Tara Jones, #hsa-team-acq (Jan 14, 2026)

**Old Cash Plus / Agent Acq Cash Plus:**
Standard DV credit addendum process still applies — use Contract Change → Create Generic Addendum from the transaction page.

**Cash (non-Plus):**
Standard DV credit addendum process — Contract Change → Create Generic Addendum.

**Known bug (SELL-582, Feb 18 2026):** For New FO Prez Cash Plus, the "Combined Purchase Agreement and Repair Addendum" still registers as addendum #1 even though the repair addendum was removed, causing subsequent addenda to start at #2. Workaround from Tara: if title asks for an addendum to address the missing #1, send verbiage: *"The parties acknowledge that no Addendum 1 has been executed in connection with this Agreement."*

### DV Talk Track (HSA)

> "The next part of the process is scheduling a quick visit with one of our project managers to confirm everything matches what was shared during the assessment. It's typically about 30-45 minutes, and they'll schedule at a time that works for you."

### Appliance Addendum (Seller Keeps Appliances)

Source: Appliance Requests Zendesk KB (Nov 2025)

Sellers often ask to keep appliances after receiving their final offer. Opendoor requires appliances to stay, but washer/dryer are negotiable.

**Negotiable vs Non-Negotiable:**

| Category | Appliances | Can Seller Keep? |
|----------|-----------|-----------------|
| **Negotiable** | Washer, dryer | Yes — offered "as a show of good faith" |
| **Non-negotiable** | Refrigerator, oven/range, dishwasher | No — must stay with property |

**Creating the Addendum in City:**

1. Pull up the acquisition transaction page
2. Click **Contract Change** dropdown → **Create Generic Addendum**
3. **Addendum Title:** `Appliance Addendum`
4. **Standard Verbiage:** *"The seller agrees that the [insert appliance] does not convey with the property."*
   - Example: *"The seller agrees that the washer and dryer does not convey with the property."*
5. Double-check spelling, grammar, and accuracy — this is a binding document
6. Submit — sent to customer for signature

**XA Talk Track:** *"While I am unable to let you take the refrigerator, you can take the washer/dryer as a show of good faith. This will have to be outlined in an addendum."*

**Escalation:** If the seller pushes back to take a non-negotiable appliance, the XA submits an escalation to the HSA for follow-up. If the HSA determines it would significantly degrade the customer experience or risk the deal, they may negotiate further.

### Re-engagement After Auto-Cancel

Three paths offered to seller:
1. **Website** — start a new offer request
2. **Call HSA** — direct number provided
3. **Reply RESTART** — re-initiates via SMS

---

## 5b. Market Product Availability

Source: HSA Market Nuances Sheet (Mar 24, 2026) — `1iMdE0Z7Rt2B4lbMqK272ijOFO91LL13RutVyOIng-6I`

**Not all products are available in all markets.** Before discussing products with a seller, verify availability for their market.

Key variations by market:
- **Cash Plus:** Available in most markets but NOT all (e.g., Asheville, Boise, Reno — Cash offer only)
- **Homebuilder partnerships:** Only in markets with HBD flag = TRUE (DFW, Houston, Phoenix, Nashville, etc.)
- **City inspections:** Required in some markets (Boston, Cleveland, Detroit, Indianapolis, LA, Miami, Minneapolis, NJ/NY, SF). HSA must set expectations about inspection timeline.
- **Age-restricted communities:** Accepted in most markets but excluded in Asheville, Boise, Reno
- **Gated communities:** NOT accepted in Asheville, Boise, Reno, Portland
- **Appliances convey:** TRUE in all active markets. Washer/dryer can be left by seller in markets where `Leave Washer/Dryer` = TRUE.
- **Title companies:** Vary by market. See sheet for specific title company per market.

**When in doubt:** Query the sheet directly via Google Sheets MCP or reference `cx-knowledge/STATES.md` for state-level legal requirements.

---

## 6. Cancellation & Withdrawal

Source: HSA Daily Standup (Feb 23, 2026), Seller Experience slides

### Seller Cancellation Rights

- **Opendoor Addendum** allows cancellation at **any time** at **no cost/penalty**
- For Cash Plus: cancel anytime **before CP1 closes**
- EMD refunded 3-5 business days
- **Notice of Cancellation** auto-generates in CITY when contract is withdrawn
- Seller withdrawal automatically cancels scheduled Inspectify inspections (shipped Jan 2026)

### Walk Process (Opendoor Walks)

| Walk Reason | EMD Goes To |
|-------------|-------------|
| Primary: `opendoor_walk`, Secondary: `opendoor_addendum` | **BUYER** (Opendoor) |
| Primary: `opendoor_walk`, Other secondary reasons | **SELLER** |
| Seller-initiated withdrawal | **SELLER** (refund) |

### Withdrawal Tracking

- **Key metric:** Withdrawal Rate = Withdrawals / Contracts Signed
- **Target:** < 20% withdrawal rate
- **Net Conversion** = FO Conv % × (1 - Withdrawal Rate) — "contracts that stick"
- High withdrawal rate is as damaging as low conversion

---

## 7. Seller Personas

Source: FO Seller Persona Analysis (Ben Booi, Feb 2026), 5,109 FO calls analyzed (Jan 2026 data)

### 5 Personas

| Persona | % of FO Calls | Conversion Rate | Handling Approach |
|---------|---------------|-----------------|-------------------|
| **Quick Closer** | 17% (expected 14%) | 23% | HIGH priority. Life-event driven. Speed + certainty messaging. Close fast. |
| **Pragmatic Planner** | 31% (expected 46%) | 15% | HIGH priority. Sell+Buy, timeline focused. Net proceeds framing. Build trust. |
| **Agent-Guided** | 7% (expected 20%) | 9% | MEDIUM priority. Has agent, comparing options. Data-driven, comp-focused. |
| **Equity Optimizer** | 31% (expected 8%) | 6% | LOW time investment. Price-first, hard to close on Cash. Lead with Cash Plus. |
| **Digital Dreamer** | 11% (expected 12%) | ~0% | MINIMAL time. Not a seller, just gathering info. Quick qualification, move on. |

### Key Insight: Equity Optimizers are 4x Overrepresented

- 8% expected at FO stage, 31% actual — "the funnel leak"
- 40% of HSA call time goes to two lowest-converting segments (Equity Optimizer + Digital Dreamer)
- **Recommendation:** Earlier qualification via 5 discovery questions → redirect low-intent leads

### Discovery Questions (Early Persona Detection)

1. "What's driving your timeline to sell?" → Quick Closer signals urgency, Digital Dreamer has none
2. "Have you been working with a real estate agent?" → Agent-Guided = yes
3. "What would the ideal outcome look like for you?" → Equity Optimizer focuses on price, Pragmatic Planner on logistics
4. "When would you ideally like to close?" → Quick Closer = ASAP, Planner = specific date
5. "Have you looked at what comparable homes are selling for?" → Equity Optimizer = yes and higher, Dreamer = vaguely

### Time Allocation Matrix

| Persona | Time Investment | Why |
|---------|----------------|-----|
| Quick Closer | **HIGH** — Full discovery, negotiation, close | Highest conversion, lowest time-to-close |
| Pragmatic Planner | **HIGH** — Relationship building, timeline planning | Largest market segment, solid conversion |
| Agent-Guided | **MEDIUM** — Data-driven, comp-focused | Moderate conversion, needs differentiation |
| Equity Optimizer | **LOW** — Quick qualification, Cash Plus pivot | Low conversion, high opportunity cost |
| Digital Dreamer | **MINIMAL** — Qualify out, offer self-service | Near-zero conversion, preserve capacity |

---

## 7b. Persona Talk Tracks (FO Calls)

Scripted openers and key phrases for each persona. Use after discovery questions confirm persona type.

### Quick Closer (23% conversion — highest)

**Opener:** "I know you've got a lot going on with [life event]. The good news is we can make this really simple — I've got your final offer ready, and we can have you closed in as few as 14 days."

**Key phrases:**
- "We handle everything — no showings, no repairs, no staging"
- "You pick the close date that works for your timeline"
- "Cash offer means no financing contingency — no deal falling through"

**Close:** "Based on what you've told me, this sounds like a great fit. Would you like to go ahead and accept today?"

**If hesitant:** "What would need to be true for you to feel comfortable moving forward today?"

### Pragmatic Planner (15% conversion — largest segment)

**Opener:** "I can see you've been thoughtful about this process. Let me walk you through your offer and then we can talk through timing — I want to make sure this fits your plan."

**Key phrases:**
- "Let me show you the net proceeds — what actually hits your account"
- "You choose your close date — 14 to 60 days — so this works with your move"
- "If you're buying, we can coordinate timing so you're not carrying two mortgages"

**Close:** "It sounds like [date] would work well for your timeline. Shall we set that as your close date?"

**If hesitant:** "What's the one thing that would make this decision easier?"

### Equity Optimizer (6% conversion — overrepresented)

**Opener:** "I want to make sure you have the full picture. Let me walk you through both options — Cash and Cash Plus — because the Cash Plus program might be a really good fit based on what you're looking for."

**Key phrases:**
- "Cash Plus lets you participate in the upside when we resell"
- "Your upfront payment is about 75% of estimated sale price, then you get a second check"
- "Let me show you what the total net could look like compared to listing traditionally"

**Pivot:** Lead with Cash Plus. If they're anchored on a Zillow estimate, reframe around net proceeds after agent commissions, repairs, holding costs.

**If firm no:** "I understand this isn't the right fit right now. Your offer stays valid for [X] days if anything changes." Minimize time investment.

### Agent-Guided (9% conversion)

**Opener:** "I know you've been working with your agent on this. Let me share the numbers so you and your agent can make an informed comparison."

**Key phrases:**
- "We're happy to coordinate directly with your agent — they can stay involved"
- "The key difference: our offer is all-cash, no contingency, and you're not paying buyer agent commission"
- "Here's the comparison: traditional sale after commissions vs. our net to you"

**Close:** "Would it help if I sent a comparison summary you can review with your agent?"

### Digital Dreamer (~0% conversion)

**Quick qualification:** "Can I ask — what's your timeline for selling? Are you actively looking to sell, or more in the information-gathering stage?"

**If gathering info:** "Totally understand. Here's what I'd recommend — check your offer anytime on your dashboard. When you're ready to move forward, we're here. Your offer is valid for [X] days."

**Time cap:** 5 minutes max. Do not invest in discovery or objection handling.

---

## 8. Objection Handling

Source: HSA Training Top 10 Issues (David V, Feb 2026), S.I.M.P.L.E. Framework training (Feb 2026)

### A.C.E. Response Framework

For every objection:
1. **A — Acknowledge** — Validate the concern ("I hear you, that's a fair concern")
2. **C — Clarify** — Understand the real issue ("Help me understand what's most important to you")
3. **E — Engage** — Offer solution or reframe ("Here's how our offer addresses that...")

### Top 6 Objections + Responses

#### Objection 1: "Your offer is too low"

**Acknowledge:** "I understand — getting the right value for your home is important."
**Clarify:** "Can I ask what number you had in mind? And what's that based on — a Zillow estimate, an agent's CMA, or something else?"
**Engage:**
- Explain net proceeds (after agent commission, closing costs, repairs, showings, holding costs)
- "When you factor in zero agent commission, no repair costs, and our speed to close, your true net is often comparable"
- If still far apart: request Pricing Team second look (not a negotiation — a review)
- If Equity Optimizer: pivot to Cash Plus for upside potential

#### Objection 2: "I should just list traditionally"

**Acknowledge:** "That's a perfectly valid option, and many sellers do compare."
**Clarify:** "What's most important to you — maximizing price, speed, certainty, or convenience?"
**Engage:**
- Quick Closer: "Listing typically takes 30-90 days with showings, staging, and uncertainty. We can close in 14 days."
- Pragmatic Planner: "With a traditional sale, your timeline depends on the market. With us, you choose your close date."
- Equity Optimizer: "Cash Plus gives you upside participation while still getting cash certainty today."

#### Objection 3: "Your service fee is too high"

**Acknowledge:** "I appreciate you looking at the details — let's walk through what that number actually includes."
**Clarify:** "Are you comparing to a traditional agent commission?"
**Engage:**
- "Our fee covers transaction costs, holding costs, and market risk — things you'd normally pay separately"
- "In a traditional sale, you're paying 5-6% in agent commissions PLUS closing costs PLUS repair concessions. Our number wraps everything into one transparent fee."
- Never quote a percentage — always reference the dollar amount in their net proceeds

#### Objection 4: "I need more time to decide"

**Acknowledge:** "Absolutely, this is a big decision and I want you to feel confident."
**Clarify:** "Is there specific information that would help you decide? Or is it more about timing?"
**Engage:**
- Set specific follow-up: "I'll call you Wednesday at 2pm — would that work?"
- Remind of offer window: "Your offer is good for [X] days, so no rush, but I want to make sure we don't lose it"
- Follow-up every 48 hours per protocol

#### Objection 5: "I'm worried about the inspection / DV adjusting my offer"

**Acknowledge:** "That's a common concern — let me explain exactly how it works."
**Clarify:** "Is there anything about your home's condition you're concerned about?"
**Engage:**
- "The DV is a quick 30-45 minute walkthrough to confirm what was shared during assessment. Most homes clear with no changes."
- "If there IS an adjustment, you'll see it before deciding — and you can cancel anytime at no cost."
- "The vast majority of our DVs result in clear-to-close."

#### Objection 6: "I'm anxious about the closing process"

**Acknowledge:** "Moving is stressful — we designed this process to make it as smooth as possible."
**Clarify:** "What part of closing feels uncertain?"
**Engage:**
- "You choose your close date — anywhere from 14 to 60 days out."
- "Our title team handles all the paperwork. You'll have a dedicated transaction coordinator."
- "And remember — you can cancel anytime before closing at no cost."

#### Objection 7: "I got a higher Zillow/Redfin estimate"

**Acknowledge:** "I totally get that — online estimates are a natural starting point."
**Clarify:** "Have you compared that to what homes in your neighborhood have actually sold for recently — not listed, but sold?"
**Engage:**
- "Online estimates don't account for condition, repairs needed, or current market conditions"
- "Our offer is based on actual comparable sales, a physical assessment, and real-time market data"
- "And remember — our number is your NET. A Zillow estimate doesn't subtract agent commissions, closing costs, or repairs"

#### Objection 8: "I want to wait for the market to improve"

**Acknowledge:** "That's a fair thought — timing the market is something every seller considers."
**Clarify:** "What signals would tell you it's the right time?"
**Engage:**
- "The challenge is that holding costs add up — mortgage, taxes, insurance, maintenance every month you wait"
- "Your offer is valid for [X] days, so you don't have to decide today"
- "If the market does shift, you can always request a new offer — we reassess based on current conditions"
- If Quick Closer: "Every month you wait is another month of carrying costs before your next chapter starts"

#### Objection 9: "My neighbor sold for more"

**Acknowledge:** "Comps are definitely important — let me pull up what we're seeing in your area."
**Clarify:** "Do you know if that was their list price or their actual net after commissions and concessions?"
**Engage:**
- "List price and net proceeds are very different numbers — most sellers net 8-10% less than list after agent commissions, closing costs, and buyer concessions"
- "Our offer already factors in zero commissions and we cover closing costs"
- If they have specific comps: "I can request a second look from our pricing team to make sure we haven't missed anything"

#### Objection 10: "I need to talk to my spouse/family first"

**Acknowledge:** "Absolutely — this is a family decision and I want everyone to feel good about it."
**Clarify:** "Is there specific information that would help that conversation? I'm happy to send a summary."
**Engage:**
- "I can send you a one-page breakdown — offer price, net proceeds, timeline, and cancellation policy — so you have everything in one place"
- Set specific follow-up: "How about I call you Thursday at 3pm — would that give you enough time?"
- "And just a reminder — accepting doesn't lock you in. You can cancel at any time at no cost per our addendum."

---

## 8b. State-Specific Objection Patterns

Objections that arise from state-specific regulations or market conditions:

| State | Common Objection | Response |
|-------|-----------------|----------|
| **Texas** | "What's this option period fee?" | "The option fee is separate from earnest money — it gives you the right to walk for any reason during the 7-10 day option period. It's a standard Texas contract feature." |
| **Florida** | "Why is the HOA taking so long?" | "Florida requires HOA estoppel letters, which can take 10-15 business days. We've already started the process — this is normal for FL transactions." |
| **Georgia** | "Why is my closing taking longer?" | "Georgia requires an attorney to oversee all closings. This adds a few days but ensures everything is legally sound." |
| **North Carolina** | "What happens to my due diligence fee?" | "The DD fee is non-refundable to the seller — it's your consideration for taking the home off the market during due diligence." |
| **Arizona** | "What's the BINSR?" | "The Buyer Inspection Notice and Seller's Response — it's how inspection findings are communicated in AZ. It's part of the standard 10-day inspection period." |
| **Florida (Miami)** | "Why are my taxes higher?" | "Miami-Dade County has an additional documentary surtax on top of the state documentary tax. We factor this into your net proceeds calculation." |

---

## 8c. Post-Rejection & Re-Engagement Framework

When a seller says no or a deal falls through, the response depends on WHY:

| Rejection Reason | Re-Engagement Strategy | Timeline |
|-----------------|----------------------|----------|
| **"Offer too low"** | Note deal. If market shifts OR subsidy becomes available, proactive outreach. "Market conditions have changed — would you like an updated offer?" | 30-60 days |
| **"Going with agent"** | Respectful close. "Your offer stays valid for [X] days. If anything changes with your listing, we're here." Check back after 60 days on market | 60-90 days |
| **"Not ready yet"** | Set specific follow-up. "I'll check in [timeframe]. In the meantime, your dashboard is always available." | Per seller's timeline |
| **"Found a better deal"** | "Congratulations — I hope it works out. If anything changes, don't hesitate to reach out." No pressure. | Only if they re-engage |
| **Withdrawal (post-contract)** | Review withdrawal reason. If seller-initiated: wait 30 days, then offer refresh. If OD walk: move on. | 30 days (seller) / never (OD walk) |
| **Expired offer** | Contract Change → Refresh Offer. Assessment reusable if < 180 days. "We'd love to take another look — a lot can change in the market." | Anytime |

**Decision rule:** Re-engage if (1) seller was close to signing, (2) reason was price/timing not fundamental, (3) conditions have changed. Do NOT re-engage if seller was hostile, threatened legal, or explicitly requested no contact.

---

## 9. Subsidy FAQ

Source: subsidy-agent SKILL.md (v6.3), CX Subsidy Strategy doc (Brad Bonney, Feb 2026)

### What Is a Subsidy?

A financial concession offered to a seller to close the gap between their expectations and the offer. Typically $2,000-$6,000, applied as a credit at closing.

### When to Use Subsidy

| Scenario | Subsidy Appropriate? |
|----------|---------------------|
| Seller close to signing but needs small nudge | YES — conversion subsidy |
| Seller signed but considering withdrawal | YES — retention subsidy |
| Seller wants $50K more than offer | NO — too far from offer |
| Deal is `acq_expired` or `acq_withdrawn` | CAUTION — deal may be dead |
| Seller has competitive offer from agent | MAYBE — depends on gap size |
| Partnership/homebuilder deal | Route to `#partnerships-cs-manager-seam` |

### Request Process

1. HSA submits Google Form → posts to `#cx-subsidy-ask`
2. Include: CITY link, flip token, headline price, amount requested, context
3. **David Villasenor** reviews and responds
4. Approval thresholds: < $3K manager discretion, > $5K requires conversation
5. HSA applies in CITY (CR state) or via Zendesk ticket (pre-contract)

### Net Conversion Formula

```
Net Conversion = FO Conv % × (1 - Withdrawal Rate)
```

"Contracts that stick" — the north star metric. Subsidy is an **investment** that should improve net conversion by either:
1. **Boosting conversion** — turning a "no" into a signed contract
2. **Reducing withdrawal** — keeping a signed contract from falling out

### SubsidyAgent Reference

For detailed subsidy analysis on a specific deal, provide the flip token → `subsidy-agent` skill runs the full 8-Layer Deal Health Assessment automatically.

---

## 10. Escalation Decision Tree

Source: escalation-pathways SKILL.md (Feb 21, 2026)

### "Should I Escalate?" Matrix

```
Step 1: CATEGORIZE the issue
  ├── Pricing / offer amount    → Step 2A
  ├── Process / timeline        → Step 2B
  ├── Title / escrow            → Step 2C
  ├── DV / inspection           → Step 2D
  ├── Post-close / property     → Step 2E
  └── Emergency / legal         → Step 2F

Step 2A: PRICING
  ├── Seller unhappy with offer → HSA handles (non-negotiable, request 2nd look from Pricing)
  ├── Pricing error suspected   → #pricing-on-call
  └── Walk decision needed      → #pricing-on-call → Michael Weitz / Yang Guo

Step 2B: PROCESS / TIMELINE
  ├── FO delay                  → Check CITY state, route to UW if stuck
  ├── Close date change         → TC handles, #acq-contract-change-review if complex
  ├── DV not scheduled          → HSA follows Day 0-15 timeline (see Section 5)
  └── Closing docs missing      → TC handles

Step 2C: TITLE / ESCROW
  ├── Known EO                  → Contact directly
  ├── EO unresponsive          → EO's Associate Manager → Senior Manager → #title-escalations
  └── Market-specific           → #[market]-title-[company] channel

Step 2D: DV / INSPECTION
  ├── DV results review         → HSA presents to seller (task: post_diligence_decision_review)
  ├── HPM no-show               → #acq-cx-homes-escalation
  ├── DV credit needed          → Credit addendum process
  └── Walk after DV             → #pricing-on-call + HSA informs seller

Step 2E: POST-CLOSE
  ├── Property defect           → #xa-voc-escalation-support → Katie Wright
  ├── Community complaint       → Same as above
  └── Legal threat              → Step 2F

Step 2F: EMERGENCY / LEGAL
  └── ALWAYS escalate to manager immediately
      Mike Billett (PHX/MIA) | Eric Wyrowski (Core/SD) | Ben Braksick (Agent Acq)
```

### Quick Routing Table

| Issue | Channel | Primary Contact |
|-------|---------|-----------------|
| Subsidy request | `#cx-subsidy-ask` | David Villasenor |
| HSA escalation | `#support-hsa-escalations` | @acq-hsa-managers |
| Pricing question | `#pricing-on-call` | Michael Weitz |
| Partnership subsidy | `#partnerships-cs-manager-seam` | Spencer Jenkins |
| Title issue | `#[market]-title-[company]` | EO on file → manager chain |
| DV/field issue | `#acq-cx-homes-escalation` | Market-specific Homes team |
| Post-close complaint | `#xa-voc-escalation-support` | Katie Wright |
| System bug | `#tech-support` | Linear Asks bot |
| Fallthrough (resale) | `#[market]-fallthrough-panel` | Regional approver |
| LP escalation | `#support-listing-partner-escalations` | LP manager |

### Escalation Rules

1. **Always allow HSA a chance to connect first** — don't skip to manager
2. **XAs should NOT proactively offer a manager** — only if customer specifically requests one
3. **90-minute SLA** for HSA responses to XA escalations
4. **2+ repeat escalations** or **time-sensitive** (< 24hrs) → manager escalation
5. **HSA OOO 3+ days** → assigned pod backup; **48hrs no response** → manager

---

## 11. Instant Final Offer (IFO)

Source: IFO Experiment Design (DATA-497, Diksha Radhakrishnan), #tmp-final-offer-prez-updates, #sales-acq-collaboration, Josh Benard (Growth EPDD). Last updated: March 18, 2026.

### What Changed

The old flow was linear: **Assessment → Underwriting → Offer**. ~90% of sellers dropped off at assessment. IFO decouples underwriting from offer generation, enabling **contract first, underwriting later**.

### Customer Flow (IFO)

| # | Stage | What Happens | Trigger |
|---|-------|-------------|---------|
| 1 | **Onboarding** | Seller enters address on opendoor.com, answers condition questions (timeline, mortgage balance, buying interest). Timeline question is required — drives "Serious Seller" flag. | Seller visits site |
| 2 | **Instant Offer** | System generates offer using Relist pricing + condition scores. No assessment, no photos. Offer goes straight to "accepted" state. | Onboarding completion |
| 3 | **Contract Signing** | Seller signs immediately — no UW wait. This is the key difference from old flow. | Seller accepts |
| 4 | **Post-Contract DV** | Inspectify diligence visit scheduled. Physical inspection happens AFTER contract. | Contract signed |
| 5 | **Post-Contract UW** | Full underwriting (PA valuation) happens after contract with DV data. | DV data available |
| 6 | **Reassessment** | If UW reveals material pricing gap (condition worse than stated), credit addendum issued. | UW complete |
| 7 | **Contingencies Released** | Flip transitions from "In Contract" to "contingencies_released" after UW approved. | UW approved |
| 8 | **Close** | Standard closing flow. | TC process |

### Key Technical Details

- **Launched:** ~March 15-16, 2026. Capped at 200 contracts initially.
- **Offer state:** Goes straight to "accepted" (bypasses `final_offer_unreleased` hold).
- **Pricing model:** Relist (NOT LightningOVM — bug fixed Mar 14).
- **Flip state:** Stays in "In Contract" until UW completes, then → "Contingencies Released."
- **City tags:** "Instant Offer" and/or "Instant Final Offer"
- **Experiment scope:** DTC only. Not including refreshed offers or ORE.
- **HSA involvement:** FO tasks still created — HSA presents offer and handles seller relationship. Aligned Mar 18.

### vs Standard Flow

| Dimension | Standard Flow | IFO |
|-----------|--------------|-----|
| Assessment | Required before offer | Not required |
| Underwriting | Before offer | After contract |
| Offer timing | 24-48hr after assessment | Instant at onboarding |
| Contract | After FO presentation | Can sign immediately |
| DV | After contract | Same (after contract) |
| Offer state | `final_offer_unreleased` → `accepted` | Straight to `accepted` |

### Known Issues (as of Mar 18)

- **Reassessment tension:** Large post-DV adjustments undermine "instant" promise. Under active debate.
- **Condition score accuracy:** Without full assessment, relies on seller-reported answers. "Hot or not" comp comparison tool being explored.
- **Seller timeline question:** Was accidentally made optional (bug), fixed Mar 16 (PR #97593). Drives Serious Seller flag and Google conversion goals.

### Key People

| Person | Role |
|--------|------|
| Josh Benard | Product lead (Growth EPDD) |
| Diksha Radhakrishnan | Experiment design (Data Science) |
| Fanxing Yu / Esther Yu | Engineering |
| Matthew Smith | Pricing, condition scoring |
| Bastian Wieck / Rob Clemons | Architecture |

---

## 12. Lennar Trade-In Program

Source: #proj-lennar-trade-in (C0AC6DK4XLY), Lennar Integration 1-Pager, Kia Nejatian, Brad Bonney. Last updated: March 18, 2026.

### What It Is

Partnership with Lennar (America's largest homebuilder). Customers buying a new Lennar home get an instant trade-in offer for their existing home, directly in the Lennar sales office. Uses the same IFO pricing engine.

### Customer Flow (Lennar Trade-In)

| # | Stage | What Happens | Trigger |
|---|-------|-------------|---------|
| 1 | **Lennar Community Visit** | Customer walks into Lennar sales office to buy a new home. | Customer visits |
| 2 | **NHC Introduction** | Lennar New Home Consultant introduces trade-in on their iPad (DSP — Digital Sales Platform). Required for ALL customers. | NHC identifies seller |
| 3 | **Onboarding via DSP** | NHC walks customer through condition questionnaire using embedded Opendoor components on iPad. | NHC initiates |
| 4 | **Instant Offer** | Opendoor generates instant trade-in offer (same IFO pricing: Relist + condition scores). Goes to "accepted." | Questionnaire submitted |
| 5 | **Trade-In Summary** | Customer sees offer value and trade-in details. | Offer generated |
| 6 | **Contract Signing** | Customer signs. Contract first, DV later (same as IFO). | Customer accepts |
| 7 | **Post-Contract DV** | Inspectify inspection. | Contract signed |
| 8 | **Post-Contract UW** | Full underwriting. Flip → Contingencies Released after UW. ~4 days for first property. | DV + PA complete |
| 9 | **Reassessment** | Credit addendum if condition gap found. Policy: reassess every home, subsidize strategically. | UW reveals gap |
| 10 | **Close** | Home traded in; customer completes Lennar new home purchase. | TC process |

### How Lennar Differs from Standard IFO

| Dimension | Standard IFO | Lennar Trade-In |
|-----------|-------------|-----------------|
| Entry point | opendoor.com | Lennar sales office (NHC iPad/DSP) |
| Lead source | DTC | Partner (`partner_identifier: "lennar_trade_in"`) |
| City tags | "Instant Offer" / "Instant Final Offer" | "Lennar Trade In lead", "Lennar Trade In" |
| Experiment | In IFO experiment bucket | Uses IFO flow but NOT in experiment |
| Pricing | Standard IFO | ~93% of expected resale (tighter spreads) |
| Reassessment | Normal | Reassess but willing to subsidize early in pilot |
| Budget | N/A | Up to $1M in pilot losses approved |

### Pilot Markets

Riverside (Inland Empire), Los Angeles, Sacramento, Myrtle Beach SC, Indianapolis, Nashville.

### Flip State Bug (Active)

`has_workflow?` guard in `offer.rb` line 246 skips `Flips::Api.on_offer_contingencies_released` for workflow-based offers (like Lennar). Causes flip to stay stuck at "In Contract" even after UW completes. **Workaround:** manual admin release. Fix needed from Transaction Tooling / Seller eng.

### Known Issues (as of Mar 18)

- **Low NHC adoption:** 0 DSP usage in some markets since training. Kia escalated to Lennar leadership.
- **25% denial rate** on Coastal requests — flagged as too high for partner relationship.
- **Trade-in summary gap:** Mortgage payoff not reflected for one customer. NHC had to manually follow up.
- **NHC dashboard visibility:** Trade-ins not showing in NHC dashboards.
- **First pricing hit:** Mission Viejo CA, $50K condition gap. Decision: eat it to build momentum. Brad: "giving on homes, not just walking."

### Key People

| Person | Role |
|--------|------|
| Kia Nejatian | Partnership lead |
| Alexis Schlattman | Operational coordination, NHC training |
| Josh Benard | Product (DSP SDK, Amplitude) |
| Brad Bonney | Strategic direction, subsidy decisions |
| Michael Weitz / Yang Guo | Pricing, LGM review |
| David Thornton | Engineering (flip state issues) |

### Slack Channels

| Channel | Purpose |
|---------|---------|
| #proj-lennar-trade-in (C0AC6DK4XLY) | Main coordination channel |
| #lennar-pilot | Market-specific pilot discussions |
| #pricing-questions | Pricing/reassessment decisions |
