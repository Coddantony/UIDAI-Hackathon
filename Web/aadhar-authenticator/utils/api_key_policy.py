MIN_API_KEY_LENGTH = 32


def valid_api_key_format(value: str) -> bool:
    return isinstance(value, str) and len(value) >= MIN_API_KEY_LENGTH
