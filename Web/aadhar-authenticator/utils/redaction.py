SENSITIVE_FIELDS = {"password", "api_key", "eKYCXML", "vid"}


def redact(data: dict) -> dict:
    return {k: ("[REDACTED]" if k in SENSITIVE_FIELDS else v) for k, v in data.items()}
