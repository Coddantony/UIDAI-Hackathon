from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class AuditEvent:
    event_type: str
    outcome: str
    request_id: str | None = None
    actor_id: str | None = None
    purpose: str | None = None
    timestamp: str | None = None

    def to_record(self) -> dict:
        record = asdict(self)
        record["timestamp"] = self.timestamp or datetime.now(timezone.utc).isoformat()
        return {key: value for key, value in record.items() if value is not None}
