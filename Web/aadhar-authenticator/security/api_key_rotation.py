"""Verifier API-key rotation policy."""

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass(frozen=True)
class ApiKeyPolicy:
    lifetime_days: int = 90
    overlap_minutes: int = 15

    def expires_at(self, issued_at: datetime) -> datetime:
        if issued_at.tzinfo is None:
            issued_at = issued_at.replace(tzinfo=timezone.utc)
        return issued_at + timedelta(days=self.lifetime_days)

    def is_expired(self, issued_at: datetime, now: datetime | None = None) -> bool:
        return (now or datetime.now(timezone.utc)) >= self.expires_at(issued_at)
