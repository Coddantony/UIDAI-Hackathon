"""Signature policy constants for modern Aadhaar integrations."""
DIGEST='SHA-256'; SIGNATURE='RSA-SHA256'
def require_modern_algorithms(digest:str,signature:str)->None:
    if digest.upper()!=DIGEST or signature.upper()!=SIGNATURE:raise ValueError('SHA-256/RSA-SHA256 required')
