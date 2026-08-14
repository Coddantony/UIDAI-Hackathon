from pydantic import BaseModel, Field
from models.verification import VerificationStatus

class VerificationResult(BaseModel):
    status: VerificationStatus
    subject: str = Field(min_length=1, max_length=128)
    reason: str | None = Field(default=None, max_length=255)
