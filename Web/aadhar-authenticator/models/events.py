from pydantic import BaseModel
from datetime import datetime

class AuditEvent(BaseModel):
    action: str
    actor: str
    subject: str | None = None
    outcome: str
    occurred_at: datetime
    request_id: str | None = None
