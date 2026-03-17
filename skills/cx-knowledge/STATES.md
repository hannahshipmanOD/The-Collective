# Property States Reference

Properties move through states during the Opendoor transaction lifecycle. XAs need to understand these states to support customers correctly.

## Pre-offer states
- `lead` — Customer has expressed interest, no offer yet
- `assessment_scheduled` — Home assessment scheduled
- `assessment_complete` — Assessment done, pricing in progress
- `offer_extended` — Offer sent to customer

## Under contract states
- `contract_signed` — Customer accepted offer, contract executed
- `inspection_scheduled` — Inspection scheduled
- `inspection_complete` — Inspection done
- `repair_negotiation` — Repair credits/concessions being negotiated
- `clear_to_close` — All contingencies cleared

## Closing states
- `closing_scheduled` — Closing date set
- `closed` — Transaction complete, title transferred

## Cancelled/declined states
- `offer_declined` — Customer declined our offer
- `cancelled` — Contract cancelled (various reasons)
- `expired` — Offer expired without response

## Post-close states
- `owned` — Opendoor owns property, in renovation/listing
- `listed` — Property listed for resale
- `sold` — Property sold to new buyer

## XA involvement by state

| State | XA role |
|-------|----------|
| lead → offer | Answering questions, setting expectations |
| contract_signed → clear_to_close | Active support, inspection coordination |
| closing | Final logistics, document questions |
| cancelled | De-escalation, next steps guidance |
