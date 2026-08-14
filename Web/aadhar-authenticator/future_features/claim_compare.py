"""Constant-time comparison for sensitive claim strings."""
import hmac
def equal(a:str,b:str)->bool:return hmac.compare_digest(a or '',b or '')
