#!/usr/bin/env python3
"""
query-tc-pipeline-data.py
Pulls TC pipeline data from BigQuery and caches it.

Outputs JSON to stdout and saves to cache.
"""

import json
import sys
from datetime import date, timedelta
from pathlib import Path

try:
    from shared_cache import get_cache, set_cache, CACHE_DIR
except ImportError:
    CACHE_DIR = Path(__file__).parent.parent / "cache"
    CACHE_DIR.mkdir(exist_ok=True)
    def get_cache(key): return None
    def set_cache(key, value): pass

TODAY = date.today().isoformat()
NEXT_WEEK = (date.today() + timedelta(days=7)).isoformat()
CACHE_KEY = f"tc-pipeline-daily-{TODAY}"

def main():
    cached = get_cache(CACHE_KEY)
    if cached:
        print(json.dumps(cached, indent=2))
        return

    try:
        from google.cloud import bigquery
        client = bigquery.Client()

        query = f"""
        SELECT
          a.tc_email,
          COUNT(*) AS active_transactions,
          COUNTIF(t.scheduled_close_date BETWEEN '{TODAY}' AND '{NEXT_WEEK}') AS closing_this_week,
          COUNTIF(t.is_at_risk = TRUE) AS at_risk
        FROM opendoor.tc_ops.transactions t
        JOIN opendoor.tc_ops.tc_assignments a
          ON t.transaction_id = a.transaction_id
          AND a.is_current = TRUE
        WHERE t.status = 'active'
        GROUP BY a.tc_email
        ORDER BY active_transactions DESC
        """

        rows = list(client.query(query).result())
        data = {
            "date": TODAY,
            "pipeline_by_tc": [
                {
                    "tc": row.tc_email,
                    "active": row.active_transactions,
                    "closing_this_week": row.closing_this_week,
                    "at_risk": row.at_risk
                }
                for row in rows
            ],
            "totals": {
                "active": sum(r.active_transactions for r in rows),
                "closing_this_week": sum(r.closing_this_week for r in rows),
                "at_risk": sum(r.at_risk for r in rows),
            }
        }

    except Exception as e:
        print(f"BigQuery unavailable ({e}), using placeholder data.", file=sys.stderr)
        data = {
            "date": TODAY,
            "pipeline_by_tc": [],
            "totals": {"active": 0, "closing_this_week": 0, "at_risk": 0},
            "note": "BigQuery not available — run from an environment with GCP credentials"
        }

    set_cache(CACHE_KEY, data)
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
