"""Expiry wrapper for disclosed claims."""
from dataclasses import dataclass
from datetime import datetime,timezone
@dataclass(frozen=True)
class Claim: value:object; expires_at:datetime

def valid(claim:Claim,now=None)->bool:return (now or datetime.now(timezone.utc))<claim.expires_at
