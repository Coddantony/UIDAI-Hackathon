from uuid import uuid4

from starlette.middleware.base import BaseHTTPMiddleware


class RequestIdMiddleware(BaseHTTPMiddleware):
    """Propagate a bounded request correlation ID for support and audit tracing."""

    async def dispatch(self, request, call_next):
        request_id = request.headers.get("X-Request-ID") or uuid4().hex
        request_id = request_id[:128]
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers["X-Request-ID"] = request_id
        return response
