---
type: knowledge
name: cx-knowledge
description: >
  Master CX knowledge skill (v2) — THE single entry point for ALL product, process, people, and policy
  questions. Product FAQ, seller personas, objection handling, state regulations, escalation routing,
  training, closing/title, HSA onboarding. Triggers: 'how does X work', 'objection', 'state reg',
  'escalation', 'who handles', 'training', 'closing', 'onboarding', 'new HSA setup', any product/process FAQ.
---

# cx-knowledge v2.0 — Master CX Knowledge Skill

> Everything an HSA, XA, EP, or TC needs to know. Product, process, people, states, escalation, training, onboarding — one skill.

---

## When to Use This Skill

| Input | Action |
|-------|--------|
| "How does Cash Plus work?" | Product FAQ → DATA_MODEL Section 2 |
| "What's the inspection period in Texas?" | State regs → STATES.md |
| "Seller says offer is too low" | Objection handling → DATA_MODEL Section 8 |
| "Should I escalate this?" | Escalation decision tree → DATA_MODEL Section 10 |
| "What's the DV process?" | Process FAQ → DATA_MODEL Section 5 |
| "How do I find X in City?" | Route to **city-nav** skill |
| "What's this seller's persona?" | Persona framework → DATA_MODEL Section 7 |
| State-specific question | STATES.md → state lookup |
| Market-specific question | STATES.md → market nuances |
| HSA training question | Training → `knowledge/training.md` |
| "Who handles X?" / escalation routing | Full routing → `knowledge/escalation.md` |
| Closing / title / escrow question | Closing process → `knowledge/closing.md` |
| New HSA setup / onboarding | Checklist → `knowledge/onboarding.md` |

This skill is a **reference knowledge base**. It synthesizes 20+ source documents into one queryable system. Load the relevant section — don't dump everything.

---

## Decision Tree

```
Level 1: WHAT TYPE OF QUESTION?
├── Product (Cash, Cash Plus, fees, timeline)  → DATA_MODEL Sections 1-3
├── Instant Final Offer (IFO, instant offer)   → DATA_MODEL Section 11
├── Lennar Trade-In (Lennar, trade-in, NHC)    → DATA_MODEL Section 12
├── Process (assessment, FO, DV, closing)      → DATA_MODEL Sections 4-6
├── State/Market regulation                     → STATES.md
├── Seller objection                            → DATA_MODEL Section 8
├── Subsidy question                            → DATA_MODEL Section 9 → subsidy-agent skill
├── Escalation routing                          → DATA_MODEL Section 10 → escalation-pathways skill
├── Persona / seller behavior                   → DATA_MODEL Section 7
├── City platform / navigation                  → city-nav skill
└── Data / metrics question                     → Route to analytics skills

Level 2: WHO IS ASKING?
├── HSA  → Full detail, include talk tracks and coaching angles
├── XA   → Process-focused, include handoff rules
├── TC   → Document/timeline focused
├── Manager → Strategic view, include metrics context
└── External (seller via Mike) → Customer-friendly language only

Level 3: WHAT DEAL STAGE?
├── Pre-offer (address entry, assessment)  → Assessment paths, timeline
├── FO (unreleased, sent, negotiation)     → FO process, objection handling
├── In-contract (signed, DV, CR)           → DV process, cancellation rights
├── Late-stage (checkout, closing)         → TC process, title, escrow
└── Post-close (resale, CP2)               → Post-close escalation
```

---

## Seller Journey Overview

Source: HSA 101 Training (David V, Feb 23, 2026)

### 7 Steps

| Step | What | Timeline | HSA Role |
|------|------|----------|----------|
| 1. **Get Offer** | Seller enters address, gets preliminary offer | Same day | — |
| 2. **Assessment** | ORVA, SSVA, Key App, or IWT | Flexible | — |
| 3. **Final Offer** | UW reviews, FO generated | 24-48 hours | HSA presents via Calendly call |
| 4. **DV** | Inspectify diligence visit | 1-6 days post-sign | HSA sets expectations, follows Day 0-15 timeline |
| 5. **Choose Date** | Seller picks close date | — | HSA confirms preference |
| 6. **Close** | Escrow closes, seller gets paid | 7-60 days from contract | TC manages docs |
| 7. **CP2** (if applicable) | Second payment after OD resells | Up to 1 year | — |

### HSA Daily Priorities (In Order)

1. **Scheduled FO calls** — non-negotiable, these are booked
2. **DV conversations** — Day 0-15 timeline management
3. **High propensity unscheduled** — leads with high propensity score
4. **Proactive outreach** — follow-ups, re-engagements
5. **Admin** — notes, CITY updates, subsidy requests

### HSA Key Metrics

| Metric | Target | Definition |
|--------|--------|------------|
| FO Conversion % | ~7%+ | Contracts Signed / FO Tasks Created |
| Withdrawal Rate | < 20% | Withdrawals / Contracts Signed |
| Net Conversion | ~6%+ | FO Conv × (1 - Withdrawal Rate) |
| Contracts/Month | 40 | Signed contracts |
| Closings/Month | 40 | Completed closings |

---

## Rules of Engagement

### XA vs HSA Scope

| XA Handles | HSA Handles |
|-----------|-------------|
| Inbound support calls | Final Offer calls |
| Basic process questions | Pricing negotiation |
| Assessment scheduling | Complex seller situations |
| General status updates | Subsidy decisions |
| DV scheduling assistance | DV results presentation |
| Routing to Calendly | Post-DV customer conversations |
| Simple FAQ answers | High-value relationship management |

### Handoff Rules

| Scenario | XA Action | HSA Action |
|----------|-----------|------------|
| Seller calls about FO | Route to HSA via Calendly link | Make FO call within 24hrs |
| FO Unreleased visible | **NEVER tell seller FO is ready** | Present when ready |
| Seller wants to negotiate | Create HSA request in Zendesk | Review, potentially request Pricing 2nd look |
| Seller threatening to cancel | Empathize, create HSA request | Assess subsidy opportunity, retention call |
| Urgent (FO expiring today) | Escalate to `#support-hsa-escalations` | Respond immediately |

### FO Unreleased Protocol

**CRITICAL RULE:** When "Final Offer Unreleased" tag is visible in CITY:
1. XA must **NEVER** tell the seller the FO is ready
2. Route seller to HSA via **Calendly link only**
3. As of Jan 23, 2026: Calendly links are for **actual FO calls only**, not 15-minute meetings
4. If FO expires today and HSA unreachable: escalate to `#support-hsa-escalations`

### 90-Minute HSA SLA

- HSA should respond to XA escalations within **90 minutes** during working hours
- If no response: XA provides HSA direct contact info to customer
- If no response in 48 hours: manager escalation

---

## Escalation Quick-Reference

### "Should I Escalate?" — 3-Question Test

1. **Is the customer at risk of leaving?** (expiring FO, competitive offer, frustration)
   - YES → escalate (HSA or manager based on severity)
2. **Is this outside my scope?** (pricing change, subsidy approval, title issue)
   - YES → route to appropriate channel (see routing table)
3. **Has the standard process failed?** (2+ attempts, SLA exceeded)
   - YES → escalate one level up

### Quick Routing

| I need... | Go to... |
|-----------|----------|
| HSA to call seller | HSA Calendly link (XA) or `#support-hsa-escalations` (urgent) |
| Subsidy approval | `#cx-subsidy-ask` (Google Form → David Villasenor) |
| Pricing review | `#pricing-on-call` (Michael Weitz / Yang Guo) |
| Title help | Market-specific title channel → EO chain |
| DV/field issue | `#acq-cx-homes-escalation` |
| Post-close complaint | `#xa-voc-escalation-support` (Katie Wright) |
| Partnership deal | `#partnerships-cs-manager-seam` |
| System bug | `#tech-support` (Linear Asks bot) |

For full escalation routing with contacts, SLAs, and processes → load `knowledge/escalation.md`.

---

## Cross-Skill Map

| Skill | How cx-knowledge Supports It |
|-------|------------------------------|
| **hsa-morning-gameplan** | Loads persona framework (Section 7) + objection handling (Section 8) for battle card |
| **call-coach** | References objection handling for coaching notes; persona detection for call scoring |
| **subsidy-agent** | Section 9 provides subsidy FAQ context; routes detailed analysis to subsidy-agent |
| **cx-support-daily** | Loads rules of engagement for XA ticket triage; escalation quick-ref for routing |
| **tc-pipeline-daily** | References DV timeline (Section 5) and state-specific requirements (STATES.md) |
| **daily-debrief** | Persona distribution informs debrief coaching notes |
| **city-nav** | cx-knowledge handles "what" questions; city-nav handles "where to find it in City" |
| **escalation-pathways** | cx-knowledge Section 10 is the quick-ref; escalation-pathways has full detail |
| **sms-instance** | References talk tracks and objection responses for AI-suggested SMS replies |
| **sales-analytics** | Metric definitions (FO conv, net conv, withdrawal) align to Section 4 authoritative definitions |

---

## Source Document Index

| Section | Primary Source | Last Updated |
|---------|---------------|--------------|
| 1. Cash Offer | Sell Direct Zendesk KB | Feb 3, 2026 |
| 2. Cash Plus | Cash Plus Zendesk KB + Initiative Hub | Feb 12, 2026 |
| 3. Fees | Service Charge Zendesk KB + Cash Plus Charges doc | Feb 19, 2026 |
| 4. Assessment/FO | FO Process Zendesk KB + Conversion Metric Definition | Feb 4, 2026 |
| 5. DV | DV Zendesk KB + DV Credit Addendum doc + New FO Prez DV Process (Tara Jones, #hsa-team-acq Jan 14) + SELL-338/SELL-582 + Appliance Requests KB | Feb 24, 2026 |
| 6. Cancellation | HSA Daily Standup + Seller Experience slides | Feb 23, 2026 |
| 7. Personas | FO Seller Persona Analysis (Ben Booi) | Feb 10, 2026 |
| 8. Objections | HSA Training Top 10 Issues (David V) | Feb 18, 2026 |
| 9. Subsidy | subsidy-agent v6.3 + CX Subsidy Strategy | Feb 13, 2026 |
| 10. Escalation | escalation-pathways SKILL.md | Feb 21, 2026 |
| 11. Instant Final Offer | IFO Experiment (DATA-497), Josh Benard, #tmp-final-offer-prez-updates | Mar 18, 2026 |
| 12. Market Product Availability | HSA Market Nuances Sheet (`1iMdE0Z7Rt2B4lbMqK272ijOFO91LL13RutVyOIng-6I`) | Mar 24, 2026 |
| 13. Addendum V21 | [Template] {{All}} Opendoor Addendum (3-2-26 V21) — new 5-day/10-day DV scheduling window for Cash | Mar 24, 2026 |
| 14. CNML Addendum | Cash Now, More Later Addendum Template (03232026) — two-part fee (program fee + initial cash adjustment) | Mar 24, 2026 |
| 12. Lennar Trade-In | #proj-lennar-trade-in, Kia Nejatian, Lennar Integration 1-Pager | Mar 18, 2026 |
| STATES.md | Real Estate Laws SoT sheet + Market Nuances sheet | Feb 13, 2026 |
