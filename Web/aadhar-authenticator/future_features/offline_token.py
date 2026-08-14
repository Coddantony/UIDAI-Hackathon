"""Short-lived signed token payload for offline verifier handoff."""
import base64,json,hmac,hashlib

def issue(payload:dict,secret:bytes)->str:
    body=base64.urlsafe_b64encode(json.dumps(payload,separators=(',',':')).encode()).decode().rstrip('=')
    sig=hmac.new(secret,body.encode(),hashlib.sha256).hexdigest()
    return body+'.'+sig

def verify(token:str,secret:bytes)->dict:
    body,sig=token.split('.',1)
    expected=hmac.new(secret,body.encode(),hashlib.sha256).hexdigest()
    if not hmac.compare_digest(sig,expected): raise ValueError('invalid token')
    return json.loads(base64.urlsafe_b64decode(body+'='*((4-len(body)%4)%4)))
