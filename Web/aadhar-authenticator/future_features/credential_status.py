"""Credential lifecycle states for wallet-style identity proofs."""
from enum import Enum
class CredentialStatus(str,Enum): ACTIVE='active'; SUSPENDED='suspended'; REVOKED='revoked'; EXPIRED='expired'
def usable(status:CredentialStatus)->bool:return status is CredentialStatus.ACTIVE
