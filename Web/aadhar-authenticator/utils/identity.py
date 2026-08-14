import hashlib
import hmac
from config.variables import JWT_CONFIG


def fingerprint(value: str) -> str:
    """Deterministic, non-reversible lookup fingerprint for sensitive identifiers."""
    return hmac.new(
        JWT_CONFIG["SECRET_KEY"].encode("utf-8"),
        value.strip().encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
