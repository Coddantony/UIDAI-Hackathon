from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class AuditEvent(BaseModel):
    event_type: str = Field(min_length=1, max_length=80)
    actor: Optional[str] = Field(default=None, max_length=128)
    subject: Optional[str] = Field(default=None, max_length=128)
    timestamp: datetime
    success: bool = True
    request_id: Optional[str] = Field(default=None, max_length=128)
