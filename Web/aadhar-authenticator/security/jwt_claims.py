"""Validation rules for security-critical JWT claims."""

import time


def validate_claims(claims: dict, issuer: str, audience: str, now: int | None = None) -> dict:
    current = int(time.time()) if now is None else now
    for key in ("sub", "iss", "aud", "exp", "iat", "jti"):
        if key not in claims:
            raise ValueError(f"missing JWT claim: {key}")
    if claims["iss"] != issuer or claims["aud"] != audience:
        raise ValueError("JWT issuer or audience mismatch")
    if claims["exp"] <= current or claims["iat"] > current + 30:
        raise ValueError("invalid JWT lifetime")
    return claims
