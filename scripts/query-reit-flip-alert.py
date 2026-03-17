#!/usr/bin/env python3
"""
query-reit-flip-alert.py

Daily alert: properties in pre-reno flip states with an active REIT resale contract.
Runs via GitHub Actions each weekday morning and sends a Slack DM to Matt.
"""

import os
import sys
from datetime import date

import snowflake.connector
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# --- Config ---
SLACK_USER_ID = "U45HRF2QL"  # Matt McCollum

QUERY = """
SELECT
    f.ADDRESS_FULL,
    f.MARKET_NAME,
    f.FLIP_STATE,
    p.HPM,
    lo.CLOSE_OF_ESCROW,
    lo.CONTRACT_EXECUTION_DATE,
    lo.BUYER_NAME
FROM DWH.DW.ax_flips f
JOIN DWH.WEB.LISTINGS l
    ON l.FLIP_ID = f.ID
JOIN DWH.WEB.LISTING_OFFERS lo
    ON lo.ID = l.ACCEPTED_OFFER_ID
LEFT JOIN DWH.DW.ax_flip_participants p
    ON p.TOKEN = f.TOKEN
WHERE f.FLIP_STATE IN (
    'contingencies_released',
    'late_checkout',
    'pre_renovation',
    'in_renovation'
)
AND lo.STATE = 'in_contract'
AND lo.CHANNEL = 'reit'
ORDER BY lo.CONTRACT_EXECUTION_DATE DESC
"""

FLIP_STATE_LABELS = {
    "contingencies_released": "Contingencies Released",
    "late_checkout": "Late Checkout",
    "pre_renovation": "Pre-Renovation",
    "in_renovation": "In Renovation",
}


def run_query():
    conn = snowflake.connector.connect(connection_name="default")
    cursor = conn.cursor(snowflake.connector.DictCursor)
    cursor.execute(QUERY)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def format_message(rows):
    today = date.today().strftime("%B %-d, %Y")
    count = len(rows)

    if count == 0:
        return (
            f":white_check_mark: *REIT Flip Alert \u2014 {today}*\n\n"
            f"No properties currently in a pre-reno state with an active REIT contract."
        )

    lines = [
        f":rotating_light: *REIT Flip Alert \u2014 {today}*",
        f"{count} {'property' if count == 1 else 'properties'} in a pre-reno state with an active REIT contract:\n",
    ]

    for row in rows:
        state_label = FLIP_STATE_LABELS.get(row["FLIP_STATE"], row["FLIP_STATE"])
        hpm = row["HPM"] or "_HPM not assigned_"
        coe = str(row["CLOSE_OF_ESCROW"]) if row["CLOSE_OF_ESCROW"] else "TBD"
        contract_date = str(row["CONTRACT_EXECUTION_DATE"])[:10] if row["CONTRACT_EXECUTION_DATE"] else "Unknown"
        buyer = row["BUYER_NAME"] or "Unknown"

        lines.append(
            f"*{row['ADDRESS_FULL']}* \u2014 {row['MARKET_NAME']}\n"
            f"  State: {state_label} | HPM: {hpm}\n"
            f"  Contract executed: {contract_date} | COE: {coe}\n"
            f"  Buyer: {buyer}\n"
        )

    lines.append("_These properties have active REIT contracts \u2014 reno may not be needed. Notify the HPM._")
    return "\n".join(lines)


def send_slack_dm(message):
    client = WebClient(token=os.environ["SLACK_BOT_TOKEN"])
    response = client.conversations_open(users=[SLACK_USER_ID])
    channel_id = response["channel"]["id"]
    client.chat_postMessage(
        channel=channel_id,
        text=message,
        unfurl_links=False,
    )


def main():
    print("Running REIT flip alert query...")
    try:
        rows = run_query()
    except Exception as e:
        print(f"Snowflake query failed: {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(rows)} properties.")
    message = format_message(rows)
    print("\n--- Slack message preview ---")
    print(message)
    print("---")

    try:
        send_slack_dm(message)
        print("Slack DM sent successfully.")
    except SlackApiError as e:
        print(f"Slack error: {e.response['error']}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
