"""Portable consent receipt generation."""
from datetime import datetime,timezone
from .transaction_hash import transaction_hash

def receipt(subject:str,verifier:str,purpose:str,attributes:list[str])->dict:
    body={'subject':subject,'verifier':verifier,'purpose':purpose,'attributes':sorted(attributes),'issued_at':datetime.now(timezone.utc).isoformat()}
    return {**body,'receipt_id':transaction_hash(body)}
