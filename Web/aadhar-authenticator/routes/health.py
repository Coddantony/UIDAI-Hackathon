from datetime import datetime, timezone

from fastapi import APIRouter

health = APIRouter(tags=["health"])


@health.get("/health", summary="Liveness probe")
async def healthcheck():
    return {
        "status": "ok",
        "service": "uVerifier-authenticator",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@health.get("/ready", summary="Readiness probe")
async def readiness():
    # Keep the probe dependency-light; database readiness is exposed separately
    # once a real deployment supplies the datastore connection.
    return {"status": "ready"}
