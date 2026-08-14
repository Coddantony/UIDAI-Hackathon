import os


REQUIRED_PRODUCTION_SECRETS = (
    "AUDIT_PSEUDONYM_KEY",
    "JWT_SECRET",
)


def validate_production_security_config(env: str | None = None) -> None:
    """Fail fast when production is missing cryptographic secrets."""
    if (env or os.getenv("ENV", "development")).lower() != "production":
        return
    missing = [name for name in REQUIRED_PRODUCTION_SECRETS if not os.getenv(name)]
    if missing:
        raise RuntimeError(f"Missing required production secrets: {', '.join(missing)}")
