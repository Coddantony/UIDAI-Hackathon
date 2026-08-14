from pydantic import BaseModel
from typing import Literal


class HealthResponse(BaseModel):
    status: Literal["ok", "degraded", "down"]
    service: str
    version: str
