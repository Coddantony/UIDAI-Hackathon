"""Small health service abstraction for application and dependency probes."""

from datetime import datetime, timezone


def process_health() -> dict:
    return {
        "status": "ok",
        "service": "uVerifier",
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }
