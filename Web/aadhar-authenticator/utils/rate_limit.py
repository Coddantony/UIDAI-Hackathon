from __future__ import annotations

from collections import defaultdict, deque
from datetime import datetime, timedelta
from threading import Lock
from dataclasses import dataclass
from time import monotonic


class LoginRateLimiter:
    def __init__(self, max_attempts=5, window_seconds=60):
        self.max_attempts = max_attempts
        self.window = timedelta(seconds=window_seconds)
        self._attempts = defaultdict(deque)
        self._lock = Lock()

    def check(self, key: str) -> bool:
        now = datetime.utcnow()
        with self._lock:
            attempts = self._attempts[key]
            while attempts and now - attempts[0] > self.window:
                attempts.popleft()
            if len(attempts) >= self.max_attempts:
                return False
            attempts.append(now)
            return True


login_rate_limiter = LoginRateLimiter()


@dataclass(frozen=True)
class RateLimitDecision:
    allowed: bool
    remaining: int
    retry_after_seconds: int


class FixedWindowRateLimiter:
    def __init__(self, limit: int, window_seconds: int) -> None:
        if limit <= 0 or window_seconds <= 0:
            raise ValueError("limit and window_seconds must be positive")
        self.limit = limit
        self.window_seconds = window_seconds
        self._state: dict[str, tuple[float, int]] = {}
        self._lock = Lock()

    def check(self, key: str, now: float | None = None) -> RateLimitDecision:
        if not key:
            raise ValueError("rate-limit key must not be empty")
        current = monotonic() if now is None else now
        with self._lock:
            started, count = self._state.get(key, (current, 0))
            if current - started >= self.window_seconds:
                started, count = current, 0
            if count >= self.limit:
                retry = max(1, int(self.window_seconds - (current - started) + 0.999))
                self._state[key] = (started, count)
                return RateLimitDecision(False, 0, retry)
            count += 1
            self._state[key] = (started, count)
            return RateLimitDecision(True, self.limit - count, 0)

    def clear(self, key: str) -> None:
        with self._lock:
            self._state.pop(key, None)
