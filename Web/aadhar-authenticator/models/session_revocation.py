from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SessionRevocation:
    session_id: str
    revoked_at: datetime
    reason: str
