from collections import defaultdict, deque
from datetime import datetime, timedelta
from threading import Lock


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
