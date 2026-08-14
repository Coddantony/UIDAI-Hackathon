from pydantic import BaseModel, Field
from datetime import datetime
from typing import Any, Optional

class IdempotencyRecord(BaseModel):
    key: str = Field(min_length=8, max_length=128)
    created_at: datetime
    response: Optional[Any] = None
