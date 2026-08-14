from config.database import db


async def ensure_indexes():
    """Create indexes used by authentication and identity lookup paths."""
    await db.users.create_index("username", unique=True, name="users_username_unique")
    await db.users.create_index("vid", unique=True, sparse=True, name="users_vid_unique")
    await db.verifiers.create_index("username", unique=True, name="verifiers_username_unique")
    await db.verifiers.create_index("api_key", unique=True, sparse=True, name="verifiers_api_key_unique")
    await db.access_logs.create_index(
        [("vid", 1), ("accessedAt", -1)],
        name="access_logs_vid_time",
    )
