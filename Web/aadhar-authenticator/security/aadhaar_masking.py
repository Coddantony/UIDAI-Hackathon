"""Privacy-safe helpers for displaying Aadhaar identifiers."""

import re

_AADHAAR_DIGITS = re.compile(r"\D")


def normalize_aadhaar(value: str) -> str:
    """Return the 12-digit Aadhaar representation or raise ValueError."""
    digits = _AADHAAR_DIGITS.sub("", value or "")
    if len(digits) != 12:
        raise ValueError("Aadhaar identifier must contain exactly 12 digits")
    return digits


def mask_aadhaar(value: str, visible_suffix: int = 4) -> str:
    """Mask all but the requested suffix, e.g. ``XXXX-XXXX-1234``."""
    if visible_suffix < 0 or visible_suffix > 8:
        raise ValueError("visible_suffix must be between 0 and 8")
    digits = normalize_aadhaar(value)
    hidden = "X" * (12 - visible_suffix)
    masked = hidden + digits[-visible_suffix:] if visible_suffix else hidden
    return "-".join(masked[i : i + 4] for i in range(0, 12, 4))


def redact_aadhaar(value: str) -> str:
    """Return a non-sensitive audit label without exposing the identifier."""
    digits = normalize_aadhaar(value)
    return f"Aadhaar(last4={digits[-4:]})"
