from datetime import datetime, timezone
from fastapi import APIRouter
from config.database import db

health = APIRouter(tags=["system"])


@health.get('/health')
async def health_check():
    return {
        "status": "ok",
        "service": "uVerifier",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@health.get('/ready')
async def readiness_check():
    await db.command("ping")
    return {"status": "ready"}
