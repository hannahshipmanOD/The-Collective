# Zendesk Triage Playbook

## Triage priority order

1. **Urgent** tickets — respond within 1 hour
2. **High** tickets with due_at within 2 hours
3. **Escalated** tickets (tagged `escalated` or `manager_requested`)
4. **High** tickets — respond within 4 hours
5. **Normal** tickets — respond within 24 hours
6. **Low** tickets — respond within 48 hours

## Auto-routing rules

| Tag | Route to |
|-----|----------|
| `legal_threat` | Senior Manager (Matt) |
| `wire_fraud` | Senior Manager (Matt) + Security |
| `manager_requested` | Senior Manager (Matt) |
| `tc_issue` | TC team |
| `inspection` | Inspection coordination group |
| `closing` | TC team |
| `offer_dispute` | Senior XA review |

## Common ticket dispositions

### Offer questions
- Acknowledge within 1 hour
- Pull offer details from platform
- Explain comps methodology if disputed
- Escalate pricing errors to market ops

### Inspection disputes
- Pull inspection report
- Review repair credit calculation
- Escalate if customer has evidence of incorrect findings

### Closing issues
- Route to TC team for anything title/escrow related
- XAs handle: scheduling questions, general doc questions
- TCs handle: wire instructions, title issues, closing disclosure

### Cancellations
- Attempt de-escalation first
- Understand root cause
- If salvageable: offer resolution path
- If not: process cancellation per SOP
