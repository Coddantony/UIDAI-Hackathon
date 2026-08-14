import hmac


def secrets_equal(left: str, right: str) -> bool:
    """Compare secrets without ordinary early-exit string comparison."""
    return hmac.compare_digest((left or "").encode(), (right or "").encode())
