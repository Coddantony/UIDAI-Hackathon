from dataclasses import dataclass


@dataclass(frozen=True)
class SessionPolicy:
    access_minutes: int = 30
    refresh_days: int = 7

    def access_seconds(self) -> int:
        return self.access_minutes * 60
