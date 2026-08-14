"""Scheme/service-scoped transaction identifiers."""
import secrets
def create(scheme:str,service:str)->str:
    s=''.join(c for c in scheme.upper() if c.isalnum())[:16];v=''.join(c for c in service.upper() if c.isalnum())[:16]
    return f'{s}-{v}-{secrets.token_hex(8)}'
