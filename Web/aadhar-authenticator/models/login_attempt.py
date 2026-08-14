from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class LoginAttempt:
    username: str
    occurred_at: datetime
    successful: bool
