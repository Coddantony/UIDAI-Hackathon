"""Minimal verification receipt that avoids identity payloads."""
from datetime import datetime,timezone
import uuid
def create(status:str,purpose:str,transaction_id:str)->dict:
    return {'receipt_id':str(uuid.uuid4()),'status':status,'purpose':purpose,'transaction_id':transaction_id,'issued_at':datetime.now(timezone.utc).isoformat()}
