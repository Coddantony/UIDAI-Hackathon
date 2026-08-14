"""Privacy-conscious audit event contract."""

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class AuditEvent:
    action: str
    actor: str
    outcome: str
    request_id: str
    occurred_at: datetime

    @classmethod
    def now(cls, action: str, actor: str, outcome: str, request_id: str):
        return cls(action, actor, outcome, request_id, datetime.now(timezone.utc))
