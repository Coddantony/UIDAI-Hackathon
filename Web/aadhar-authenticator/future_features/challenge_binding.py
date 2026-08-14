"""Challenge generation for transaction-bound user approval."""
import secrets
def new_challenge()->str:return secrets.token_urlsafe(32)
def matches(expected:str,provided:str)->bool:return bool(expected) and secrets.compare_digest(expected,provided)
