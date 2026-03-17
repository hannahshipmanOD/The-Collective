#!/usr/bin/env python3
"""
query-cx-support-data.py
Pulls daily CX support metrics from BigQuery and caches them.

Outputs JSON to stdout and saves to cache.
"""

import json
import sys
from datetime import date, timedelta
from pathlib import Path

# Try to import shared cache
try:
    from shared_cache import get_cache, set_cache, CACHE_DIR
except ImportError:
    # Fallback if running standalone
    CACHE_DIR = Path(__file__).parent.parent / "cache"
    CACHE_DIR.mkdir(exist_ok=True)
    def get_cache(key): return None
    def set_cache(key, value): pass

YESTERDAY = (date.today() - timedelta(days=1)).isoformat()
CACHE_KEY = f"cx-support-daily-{YESTERDAY}"

def main():
    # Check cache first
    cached = get_cache(CACHE_KEY)
    if cached:
        print(json.dumps(cached, indent=2))
        return

    # Try BigQuery
    try:
        from google.cloud import bigquery
        client = bigquery.Client()

        query = f"""
        SELECT
          xa_email,
          COUNT(*) AS contacts,
          COUNTIF(DATE(resolved_at) = '{YESTERDAY}') AS resolved
        FROM opendoor.cx_ops.contacts
        WHERE DATE(created_at) = '{YESTERDAY}'
        GROUP BY xa_email
        ORDER BY contacts DESC
        """

        rows = list(client.query(query).result())
        data = {
            "date": YESTERDAY,
            "contacts_by_xa": [
                {"xa": row.xa_email, "contacts": row.contacts, "resolved": row.resolved}
                for row in rows
            ],
            "total_contacts": sum(r.contacts for r in rows),
        }

    except Exception as e:
        print(f"BigQuery unavailable ({e}), using placeholder data.", file=sys.stderr)
        data = {
            "date": YESTERDAY,
            "contacts_by_xa": [],
            "total_contacts": 0,
            "note": "BigQuery not available — run from an environment with GCP credentials"
        }

    set_cache(CACHE_KEY, data)
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
