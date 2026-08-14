"""Policy-first consent evaluation for future identity flows."""
from dataclasses import dataclass
from typing import FrozenSet

@dataclass(frozen=True)
class ConsentRequest:
    purpose: str
    attributes: FrozenSet[str]
    ttl_seconds: int
    explicit: bool

class ConsentPolicy:
    MAX_TTL = 3600
    def evaluate(self, request: ConsentRequest) -> tuple[bool, str]:
        if not request.explicit: return False, "explicit consent required"
        if not request.purpose.strip(): return False, "purpose required"
        if not request.attributes: return False, "at least one attribute required"
        if request.ttl_seconds <= 0 or request.ttl_seconds > self.MAX_TTL: return False, "consent TTL outside policy"
        return True, "approved"
