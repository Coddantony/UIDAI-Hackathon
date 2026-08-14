from datetime import datetime
from pydantic import BaseModel

class PasswordHistory(BaseModel):
    username: str
    password_hash: str
    changed_at: datetime
