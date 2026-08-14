def normalize_identifier(value: str) -> str:
    return value.strip() if isinstance(value, str) else value
