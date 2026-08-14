import re

OTP_PATTERN = re.compile(r"^[0-9]{6}$")


def is_valid_otp(value: str) -> bool:
    """Validate OTP shape without ever persisting or logging the OTP."""
    return bool(OTP_PATTERN.fullmatch(value or ""))
