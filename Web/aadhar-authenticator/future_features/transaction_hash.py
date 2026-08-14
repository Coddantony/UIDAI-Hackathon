"""Canonical transaction hashing for tamper-evident references."""
import hashlib,json
def transaction_hash(payload:dict)->str:
    canonical=json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    return hashlib.sha256(canonical.encode()).hexdigest()
