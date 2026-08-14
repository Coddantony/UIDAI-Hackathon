from datetime import datetime, timezone


def utc_now() -> datetime:
    """Return a timezone-aware UTC timestamp for persisted audit data."""
    return datetime.now(timezone.utc)
