"""Credential strength policy for verifier accounts."""

import re


def validate_password(password: str) -> None:
    if len(password or "") < 12:
        raise ValueError("password must contain at least 12 characters")
    checks = [r"[A-Z]", r"[a-z]", r"\d", r"[^A-Za-z0-9]"]
    if any(re.search(pattern, password) is None for pattern in checks):
        raise ValueError("password must contain upper, lower, digit and symbol")
