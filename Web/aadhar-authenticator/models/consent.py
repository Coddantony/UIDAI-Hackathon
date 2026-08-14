from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class ConsentRecord:
    """Minimal consent evidence; deliberately excludes raw Aadhaar/PID fields."""

    consent_id: str
    purpose: str
    disclosure_text_version: str
    granted: bool
    captured_at: str
    request_id: str

    @classmethod
    def create(cls, consent_id: str, purpose: str, disclosure_text_version: str, granted: bool, request_id: str):
        return cls(
            consent_id=consent_id,
            purpose=purpose,
            disclosure_text_version=disclosure_text_version,
            granted=granted,
            captured_at=datetime.now(timezone.utc).isoformat(),
            request_id=request_id,
        )
