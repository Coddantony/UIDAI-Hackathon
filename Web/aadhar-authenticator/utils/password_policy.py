import re


def validate_password(password: str) -> None:
    """Enforce a minimum password policy for account credentials."""
    if not password or len(password) < 8:
        raise ValueError("Password must contain at least 8 characters")
    if len(password) > 128:
        raise ValueError("Password must not exceed 128 characters")
    if not re.search(r"[A-Za-z]", password):
        raise ValueError("Password must contain a letter")
    if not re.search(r"\d", password):
        raise ValueError("Password must contain a number")
