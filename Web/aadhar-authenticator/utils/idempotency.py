from hashlib import sha256


def request_fingerprint(method: str, path: str, body: bytes, actor: str = "") -> str:
    """Build a deterministic fingerprint for safe duplicate-request detection."""
    payload = b"\x00".join((method.upper().encode(), path.encode(), actor.encode(), body))
    return sha256(payload).hexdigest()
