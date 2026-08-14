"""HMAC request signing primitive for verifier-to-service integrity."""
import hashlib,hmac
def sign(body:bytes,secret:bytes)->str:return hmac.new(secret,body,hashlib.sha256).hexdigest()
def verify(body:bytes,signature:str,secret:bytes)->bool:return hmac.compare_digest(sign(body,secret),signature)
