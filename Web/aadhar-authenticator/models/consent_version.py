from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ConsentVersion:
    consent_id: str
    version: int
    recorded_at: datetime
