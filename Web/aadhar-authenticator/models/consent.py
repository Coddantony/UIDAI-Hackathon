from datetime import datetime
from pydantic import BaseModel, Field


class ConsentRecord(BaseModel):
    subject: str = Field(min_length=1, max_length=128)
    verifier: str = Field(min_length=1, max_length=128)
    purpose: str = Field(min_length=1, max_length=255)
    granted_at: datetime
    expires_at: datetime | None = None
    revoked: bool = False
