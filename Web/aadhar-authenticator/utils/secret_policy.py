"""Fail-closed checks for security-sensitive application secrets."""

from __future__ import annotations


class WeakSecretError(ValueError):
    """Raised when a configured secret is unsafe for a deployment."""


def validate_secret(name: str, value: str | None, *, minimum_length: int = 32) -> str:
    if not value:
        raise WeakSecretError(f"{name} is not configured")
    if len(value) < minimum_length:
        raise WeakSecretError(f"{name} must contain at least {minimum_length} characters")
    lowered = value.lower()
    if lowered in {"secret", "password", "changeme", "change-me", "default", "test"}:
        raise WeakSecretError(f"{name} uses a known default value")
    return value


def validate_required_secrets(values: dict[str, str | None]) -> None:
    for name, value in values.items():
        validate_secret(name, value)
