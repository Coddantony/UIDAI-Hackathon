"""Return only attributes explicitly requested by a verifier policy."""
def disclose(identity: dict, requested: set[str], allowed: set[str]) -> dict:
    fields = requested & allowed
    return {key: identity[key] for key in fields if key in identity}
