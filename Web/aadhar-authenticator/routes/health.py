from datetime import datetime
from fastapi import APIRouter
from config.database import db

health = APIRouter(tags=["health"])


@health.get("/health")
async def health_check():
    return {"status": "ok", "timestamp": datetime.utcnow()}


@health.get("/ready")
async def readiness_check():
    await db.command("ping")
    return {"status": "ready", "database": "ok", "timestamp": datetime.utcnow()}
