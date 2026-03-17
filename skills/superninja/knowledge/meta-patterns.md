# Meta Patterns

Patterns for effective Claude Code use in CX/TC/Sales Support operations.

## Pattern: Skill stacking
Combine multiple skills in one session. Example:
```
@analytics pull yesterday's CX volume, then @meeting-capture format it for standup
```

## Pattern: Workload-first
For recurring tasks, define a workload TOML first, then run it. Don't re-describe the same pipeline in chat each time.

## Pattern: Roster awareness
When asking about team performance, Claude knows your roster from `config/xa-roster.json` and `config/tc-roster.json`. Reference team members by name.

## Pattern: Escalation clarity
When something goes wrong, use `@escalation-pathways` first to confirm the right path before acting. Don't escalate ad-hoc.

## Pattern: Log everything systemic
If you see a pattern (same issue 3+ times), use `@linear-sync` to file it. One-offs stay in chat; patterns go to Linear.

## Pattern: Meeting → Action → Linear
Capture meeting with `@meeting-capture`, then pipe action items directly to `@linear-sync`. Close the loop.
