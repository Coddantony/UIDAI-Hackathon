from config.database import db


async def ensure_indexes():
    await db.users.create_index("username", unique=True)
    await db.users.create_index("vid", unique=True)
    await db.verifiers.create_index("username", unique=True)
    await db.verifiers.create_index("api_key", unique=True)
    await db.access_logs.create_index([("vid", 1), ("accessedAt", -1)])
