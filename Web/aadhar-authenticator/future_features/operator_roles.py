"""Least-privilege roles for verifier operators."""
ROLE_SCOPES={'viewer':{'audit:read'},'agent':{'identity:verify'},'auditor':{'audit:read'},'admin':{'verifier:admin'}}
def scopes(role:str)->set[str]:return set(ROLE_SCOPES.get(role,set()))
