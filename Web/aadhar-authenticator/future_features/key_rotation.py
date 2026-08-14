"""Key rotation state machine for verifier credentials."""
from dataclasses import dataclass
from datetime import datetime,timezone
@dataclass(frozen=True)
class KeyRecord:
    key_id:str; created_at:datetime; expires_at:datetime; active:bool=True
class KeyRotation:
    def needs_rotation(self,key:KeyRecord,now:datetime|None=None)->bool:
        now=now or datetime.now(timezone.utc); return now>=key.expires_at
    def activate(self,key:KeyRecord)->KeyRecord:return KeyRecord(key.key_id,key.created_at,key.expires_at,True)
