import time
import uuid
from collections import defaultdict, deque
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["Cache-Control"] = "no-store" if request.url.path.startswith("/api/") else "no-cache"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
        return response


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.limit = requests_per_minute
        self.buckets = defaultdict(deque)

    async def dispatch(self, request: Request, call_next):
        now = time.monotonic()
        key = request.client.host if request.client else "unknown"
        bucket = self.buckets[key]
        while bucket and bucket[0] <= now - 60:
            bucket.popleft()
        if len(bucket) >= self.limit:
            return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"}, headers={"Retry-After": "60"})
        bucket.append(now)
        return await call_next(request)
