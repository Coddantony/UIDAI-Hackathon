import os


def allowed_origins() -> list[str]:
    raw = os.getenv("CORS_ORIGINS", "")
    if not raw.strip():
        return []
    origins = [item.strip().rstrip("/") for item in raw.split(",") if item.strip()]
    if "*" in origins and len(origins) > 1:
        raise RuntimeError("CORS_ORIGINS cannot mix wildcard and explicit origins")
    return origins
