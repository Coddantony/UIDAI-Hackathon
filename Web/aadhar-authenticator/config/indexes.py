from config.database import db


async def ensure_indexes():
    await db.users.create_index("username", unique=True, name="users_username_unique")
    await db.users.create_index([("vid", 1), ("isActive", 1)], name="users_vid_active")
    await db.verifiers.create_index("username", unique=True, name="verifiers_username_unique")
    await db.verifiers.create_index("api_key", unique=True, name="verifiers_api_key_unique")
    await db.access_logs.create_index("accessedAt", expireAfterSeconds=60 * 60 * 24 * 90, name="access_logs_ttl")
    await db.access_logs.create_index([("api_key", 1), ("accessedAt", -1)], name="access_logs_api_key_time")
