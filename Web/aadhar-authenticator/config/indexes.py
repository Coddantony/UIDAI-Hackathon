from config.database import db


async def ensure_indexes():
    """Create safe lookup indexes used by authentication workflows."""
    await db.users.create_index("email", unique=True, sparse=True, name="uniq_user_email")
    await db.users.create_index("phone", sparse=True, name="idx_user_phone")
    await db.verifiers.create_index("email", unique=True, sparse=True, name="uniq_verifier_email")
