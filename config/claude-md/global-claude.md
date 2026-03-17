# Global Claude Context — Matt McCollum

<!-- 
This is your global CLAUDE.md. It loads automatically in every Claude Code session.
Install: cp config/claude-md/global-claude.md ~/.claude/CLAUDE.md
Personalize: update the sections below with your team details.
-->

## Who I am

I'm **Matt McCollum**, Senior Manager at Opendoor responsible for:
- Customer Support (CX / XA team)
- Transaction Management (TC team)
- Sales Support

My manager is **Brad Bonney**.

## My teams

### Customer Support (XA team)
Managed by Alixandra Miller.
- Ingrid Pinheiro
- Christopher Lewis
- Davie Gabayan
- Celeste Blea
- Cameron Cruz

### Transaction Management (TC team)
Managed by Hannah Shipman.
- Sarah Scotia
- Daniel Beaudette
- Kiara Tellez
- Melina Encinas
- Lou Martinez
- Kylie Ottney

## My priorities

1. Team performance — metrics, coaching, removing blockers
2. Escalation management — routing, resolution, follow-up
3. Operational excellence — process quality, SLA adherence
4. Cross-functional alignment — TC/CX coordination, Sales Support

## How I like to work

- Give me summaries first, details on request
- Flag anomalies proactively — don't bury them
- Be direct. I don't need hedging.
- For data questions, write the query and explain it briefly
- Action items should have owners and due dates

## Skills available

These skills are installed in `~/.claude/skills/` via `macrodata-refinement`:

| Skill | Use it for |
|-------|------------|
| `@cx-knowledge` | CX domain questions, states, acquisition support |
| `@cx-support-daily` | Daily CX standup pipeline |
| `@zendesk-ops` | Zendesk triage and ticket analysis |
| `@tc-pipeline-daily` | Daily TC pipeline standup |
| `@escalation-pathways` | Escalation routing decisions |
| `@wavelength` | Team updates, async comms, 1:1 prep |
| `@meeting-capture` | Meeting notes and action items |
| `@analytics` | Data queries and metrics |
| `@define-workload` | Create new batch pipelines |
| `@linear-sync` | Linear issue creation and triage |
| `@training` | Onboarding and training content |
| `@superninja` | Meta-patterns, systems map |

## Dojo repo

My Claude Code dojo: `~/macrodata-refinement`.

Run workloads:
```bash
./scripts/superdojo-run workloads/cx-support-daily.toml
./scripts/superdojo-run workloads/tc-pipeline-daily.toml
```

## Key systems

| System | I use it for |
|--------|--------------|
| Zendesk | CX ticket management |
| BigQuery | Data and metrics |
| Linear | Issue tracking |
| Slack | Team comms |
| Confluence | Documentation |

## Escalation defaults

When something escalates to me:
1. Legal threats — I own it immediately
2. Wire fraud — I own it + loop in Security
3. Manager requests — I take the call/contact
4. Pattern issues (3+ same problem) — I file a Linear ticket

See `@escalation-pathways` for full routing matrix.
