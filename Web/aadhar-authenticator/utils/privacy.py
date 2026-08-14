import hashlib
import hmac
import os


def mask_identifier(value: str, visible_prefix: int = 2, visible_suffix: int = 2) -> str:
    """Return a display-safe identifier without exposing the full value."""
    if not value:
        return ""
    if len(value) <= visible_prefix + visible_suffix:
        return "*" * len(value)
    return f"{value[:visible_prefix]}{'*' * (len(value) - visible_prefix - visible_suffix)}{value[-visible_suffix:]}"


def pseudonymize_identifier(value: str, secret: str | None = None) -> str:
    """Create a stable, non-reversible audit pseudonym using HMAC-SHA256."""
    key = (secret or os.getenv("AUDIT_PSEUDONYM_KEY", "")).encode()
    if not key:
        raise RuntimeError("AUDIT_PSEUDONYM_KEY must be configured")
    return hmac.new(key, value.encode(), hashlib.sha256).hexdigest()
