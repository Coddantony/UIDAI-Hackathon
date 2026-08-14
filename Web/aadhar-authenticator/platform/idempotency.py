"""Idempotency-key validation for safe retryable verification requests."""

import re

_KEY = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{15,127}$")


def validate_idempotency_key(value: str) -> str:
    key = (value or "").strip()
    if not _KEY.fullmatch(key):
        raise ValueError("invalid idempotency key")
    return key
