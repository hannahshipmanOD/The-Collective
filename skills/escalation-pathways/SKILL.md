# Escalation Pathways

## Trigger phrases
- "escalation"
- "escalate"
- "escalation path"
- "who handles"
- "routing"

## What this skill does

Provides escalation routing logic for CX, TC, and sales support. Helps answer: who does this go to? What's the right path for this situation?

## Escalation matrix

### CX (Customer Support / XA)

| Situation | First escalation | Second escalation |
|-----------|-----------------|------------------|
| Customer requests manager | Senior XA → Matt | |
| Legal threat | Matt directly | Legal team |
| Wire fraud concern | Matt directly | Security + Legal |
| Pricing dispute (factual error) | Market Ops | Matt if unresolved |
| 3rd repeat contact, no resolution | Senior XA review | Matt |
| Media inquiry | Matt | Comms team |

### TC (Transaction Management)

| Situation | First escalation | Second escalation |
|-----------|-----------------|------------------|
| Title issue | TC lead → Hannah Shipman | Title vendor |
| Customer cancellation threat | TC + Matt | |
| Closing delay (our fault) | TC lead | Matt |
| Closing delay (customer/buyer fault) | TC lead manages | Matt if >5 days |
| Fraud suspicion | Matt directly | Legal + Security |

### Sales Support

| Situation | First escalation |
|-----------|------------------|
| Agent complaint | Matt |
| Commission dispute | Matt + Finance |
| MLS issue | Matt + Market Ops |

## Workflow

1. Identify situation type
2. Look up in escalation matrix above
3. Draft escalation message if needed
4. Log in Linear if it's a systemic issue

## Related
- `skills/cx-knowledge/ACQ_SUPPORT.md` — detailed CX escalation triggers
- `skills/linear-sync/SKILL.md` — logging issues in Linear
