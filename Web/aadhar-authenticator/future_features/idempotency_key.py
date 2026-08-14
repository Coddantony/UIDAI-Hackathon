"""Canonical idempotency-key validation."""
import re
PATTERN=re.compile(r'^[A-Za-z0-9._:-]{8,128}$')
def valid(key:str)->bool:return bool(PATTERN.fullmatch(key or ''))
