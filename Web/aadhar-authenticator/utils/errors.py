from typing import Optional


def public_error(code: str, message: str, request_id: Optional[str] = None) -> dict:
    """Build a stable public error contract without leaking internal exceptions."""
    payload = {"error": {"code": code, "message": message}}
    if request_id:
        payload["error"]["request_id"] = request_id
    return payload
