from pydantic import BaseModel, Field
from datetime import datetime

class Revocation(BaseModel):
    token_id: str = Field(min_length=1, max_length=128)
    revoked_at: datetime
    reason: str = Field(default="manual", max_length=255)
