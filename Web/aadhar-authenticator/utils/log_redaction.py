import re


AADHAAR_LIKE = re.compile(r"(?<!\d)\d{12}(?!\d)")
VID_LIKE = re.compile(r"(?<!\d)\d{16}(?!\d)")


def redact_sensitive_text(value: str) -> str:
    """Redact common identity-number shapes before they reach application logs."""
    value = AADHAAR_LIKE.sub("[REDACTED-ID]", value)
    return VID_LIKE.sub("[REDACTED-VID]", value)
