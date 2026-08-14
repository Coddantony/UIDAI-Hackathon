from fastapi import APIRouter
from config.database import db

health = APIRouter()


@health.get("/health", tags=["health"])
async def health_check():
    try:
        await db.command("ping")
        return {"status": "ok", "dependencies": {"mongodb": "ok"}}
    except Exception:
        return {"status": "degraded", "dependencies": {"mongodb": "unavailable"}}


@health.get("/ready", tags=["health"])
async def readiness_check():
    try:
        await db.command("ping")
        return {"ready": True}
    except Exception:
        return {"ready": False}
