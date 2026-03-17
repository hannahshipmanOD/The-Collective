# Define Workload

## Trigger phrases
- "define workload"
- "new workload"
- "create pipeline"
- "new toml"
- "automate this"

## What this skill does

Helps you define a new TOML workload for the `superdojo-run` batch orchestrator. Asks the right questions and produces a ready-to-use `.toml` file.

## Workflow

1. Ask: what does this workload do? (daily standup, weekly report, ad-hoc analysis, etc.)
2. Ask: what data does it need? (which scripts to run)
3. Ask: what's the output? (Slack message, saved file, Linear update, etc.)
4. Ask: when should it run? (schedule or on-demand)
5. Generate the TOML file
6. Save to `workloads/<name>.toml`

## TOML format

```toml
[workload]
name = "my-workload"
description = "What this does"
schedule = "daily" # or "weekly", "on-demand"

[data]
scripts = ["scripts/my-query.py"]
cache_ttl = 3600 # seconds

[output]
format = "slack" # or "file", "linear", "email"
channel = "#my-channel" # for slack

[steps]
# Define steps inline or reference a skill
skill = "my-skill"
prompt = "Run the daily summary"
```

## Related
- `scripts/superdojo-run` — the orchestrator that runs these
- `workloads/` — existing workload examples
