from datetime import datetime
from config.database import db


async def record_audit_event(
    action: str,
    actor: str | None = None,
    subject: str | None = None,
    outcome: str = "success",
    request_id: str | None = None,
    metadata: dict | None = None,
):
    """Persist a minimal audit event without storing credentials or identity payloads."""
    event = {
        "action": action,
        "actor": actor,
        "subject": subject,
        "outcome": outcome,
        "request_id": request_id,
        "metadata": metadata or {},
        "created_at": datetime.utcnow(),
    }
    await db.audit_events.insert_one(event)
