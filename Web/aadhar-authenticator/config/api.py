"""API-level metadata and compatibility settings."""

API_PREFIX = "/api/v1"
API_NAME = "uVerifier"
API_VERSION = "1"


def api_metadata() -> dict:
    return {"name": API_NAME, "version": API_VERSION, "prefix": API_PREFIX}
