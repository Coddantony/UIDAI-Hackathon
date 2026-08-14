from datetime import datetime, timezone


def is_consent_active(expires_at: datetime | None, revoked: bool) -> bool:
    if revoked:
        return False
    if expires_at is None:
        return True
    return expires_at > datetime.now(timezone.utc)
