"""Portable consent receipt generation."""
from datetime import datetime,timezone
import hashlib,json

def receipt(subject:str,verifier:str,purpose:str,attributes:list[str])->dict:
    body={'subject':subject,'verifier':verifier,'purpose':purpose,'attributes':sorted(attributes),'issued_at':datetime.now(timezone.utc).isoformat()}
    raw=json.dumps(body,sort_keys=True,separators=(',',':')).encode()
    return {**body,'receipt_id':hashlib.sha256(raw).hexdigest()}
