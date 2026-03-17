# Meeting Capture

## Trigger phrases
- "meeting capture"
- "capture this meeting"
- "meeting notes"
- "action items"
- "follow-up from"

## What this skill does

Captures meeting content, extracts action items, and produces clean follow-up summaries. Works from transcripts, notes, or live dictation.

## Workflow

1. Receive meeting content (transcript, notes, or description)
2. Load `DATA_MODEL.md` for context on participants/projects if needed
3. Extract:
   - Key decisions made
   - Action items (with owner and due date if mentioned)
   - Open questions / parking lot
4. Format as clean meeting summary
5. Optionally: draft follow-up Slack message or email

## Output format

```
## Meeting: [Title] — [Date]
Attendees: [names]

### Decisions
- [decision 1]
- [decision 2]

### Action Items
- [ ] [owner]: [action] by [date]
- [ ] [owner]: [action]

### Open Questions
- [question]

### Follow-up message
[optional draft]
```

## Related
- `skills/linear-sync/SKILL.md` — log action items as Linear issues
