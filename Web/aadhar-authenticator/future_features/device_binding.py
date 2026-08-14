"""Bind a verifier session to a stable device fingerprint without storing raw identifiers."""
import hashlib,hmac

def fingerprint(device_id:str,secret:bytes)->str:
    return hmac.new(secret,device_id.encode(),hashlib.sha256).hexdigest()

def matches(expected:str,device_id:str,secret:bytes)->bool:
    return hmac.compare_digest(expected,fingerprint(device_id,secret))
