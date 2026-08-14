"""Cryptographically secure opaque token generation."""

import secrets


def new_token(bytes_length: int = 32) -> str:
    if bytes_length < 16:
        raise ValueError("token entropy must be at least 128 bits")
    return secrets.token_urlsafe(bytes_length)
