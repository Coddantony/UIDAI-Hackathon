from config.database import db

async def database_ready() -> bool:
    try:
        await db.command("ping")
        return True
    except Exception:
        return False
