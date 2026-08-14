"""Recursive redaction for sensitive fields in logs and diagnostics."""

SENSITIVE_KEYS = frozenset({"aadhaar", "aadhaar_number", "password", "token", "api_key", "ekycxml"})


def redact(value):
    if isinstance(value, dict):
        return {k: "[REDACTED]" if k.lower() in SENSITIVE_KEYS else redact(v) for k, v in value.items()}
    if isinstance(value, list):
        return [redact(v) for v in value]
    return value
