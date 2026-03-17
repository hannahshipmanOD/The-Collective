# Rosters Schema

Roster files define the team members for each function. They're used by batch workloads and skills to know who's on the team.

## Schema

```json
{
  "team": "string — team display name",
  "manager": "string — direct manager name",
  "senior_manager": "string — senior manager name",
  "members": [
    {
      "name": "string — full name",
      "email": "string — work email",
      "role": "string — XA / TC / etc.",
      "manager": "string — direct manager name",
      "start_date": "string (optional) — YYYY-MM-DD"
    }
  ]
}
```

## Files
- `config/xa-roster.json` — Customer Support (XA) team
- `config/tc-roster.json` — Transaction Management (TC) team

## Updating rosters

Edit the JSON directly and commit. The workloads will pick up changes on next run.
