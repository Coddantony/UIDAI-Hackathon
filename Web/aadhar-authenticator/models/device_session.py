from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class DeviceSession:
    session_id: str
    user_id: str
    created_at: datetime
    device_id: str
