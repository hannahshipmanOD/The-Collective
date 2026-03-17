# Setting Up GitHub Secrets for Automated Alerts

The REIT flip alert runs as a GitHub Action and needs credentials stored as secrets.
Secrets are encrypted and never visible after you save them.

## Required secrets

Go to: https://github.com/Matt-McCollum/macrodata-refinement/settings/secrets/actions

Add each of these:

| Secret name | What to put in it |
|-------------|------------------|
| `SNOWFLAKE_ACCOUNT` | Your Snowflake account identifier (e.g. `opendoor.us-east-1`) |
| `SNOWFLAKE_USER` | Your Snowflake username (usually your Opendoor email) |
| `SNOWFLAKE_PASSWORD` | Your Snowflake password |
| `SNOWFLAKE_WAREHOUSE` | The warehouse to use (e.g. `ANALYST_WH`) |
| `SNOWFLAKE_ROLE` | Your Snowflake role (e.g. `ANALYST`) — optional |
| `SLACK_BOT_TOKEN` | A Slack bot token with `chat:write` and `im:write` scope |

## Getting your Snowflake details

In Snowflake, run:
```sql
SELECT CURRENT_ACCOUNT(), CURRENT_USER(), CURRENT_ROLE(), CURRENT_WAREHOUSE();
```

For the account identifier: it's the part of your Snowflake URL before `.snowflakecomputing.com`.

## Getting a Slack bot token

You need a Slack app with a bot token. Ask someone on the Opendoor eng/tools team
if there's an existing internal app you can use, or:

1. Go to https://api.slack.com/apps
2. Create a new app → "From scratch"
3. Add OAuth scopes: `chat:write`, `im:write`, `conversations.open`  
4. Install to your Opendoor workspace
5. Copy the "Bot User OAuth Token" (starts with `xoxb-`)

## Testing the action manually

Once secrets are set, go to:
https://github.com/Matt-McCollum/macrodata-refinement/actions/workflows/reit-flip-alert.yml

Click **Run workflow** to trigger it immediately without waiting for 8am.
