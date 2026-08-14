import re

VID_PATTERN = re.compile(r"^[0-9]{16}$")


def is_valid_vid(value: str) -> bool:
    return bool(VID_PATTERN.fullmatch((value or "").replace(" ", "")))
