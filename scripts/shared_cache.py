#!/usr/bin/env python3
"""
shared_cache.py
Simple file-based cache for superdojo data scripts.
"""

import json
import time
from pathlib import Path

CACHE_DIR = Path(__file__).parent.parent / "cache"
CACHE_TTL = 3600  # 1 hour default


def _cache_path(key: str) -> Path:
    safe_key = key.replace("/", "_").replace(" ", "_")
    return CACHE_DIR / f"{safe_key}.json"


def get_cache(key: str, ttl: int = CACHE_TTL):
    """Return cached value if it exists and is not expired, else None."""
    path = _cache_path(key)
    if not path.exists():
        return None
    try:
        with open(path) as f:
            entry = json.load(f)
        if time.time() - entry["ts"] > ttl:
            return None
        return entry["data"]
    except Exception:
        return None


def set_cache(key: str, value):
    """Write value to cache."""
    CACHE_DIR.mkdir(exist_ok=True)
    path = _cache_path(key)
    with open(path, "w") as f:
        json.dump({"ts": time.time(), "data": value}, f)


def clear_cache(key: str = None):
    """Clear a specific cache key or all cache."""
    if key:
        path = _cache_path(key)
        if path.exists():
            path.unlink()
    else:
        for f in CACHE_DIR.glob("*.json"):
            f.unlink()
