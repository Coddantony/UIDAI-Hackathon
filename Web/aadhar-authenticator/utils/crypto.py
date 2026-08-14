import secrets


def secure_nonce(length: int = 32) -> str:
    """Generate a cryptographically secure, URL-safe nonce."""
    if length < 16 or length > 256:
        raise ValueError("nonce length must be between 16 and 256 bytes")
    return secrets.token_urlsafe(length)
