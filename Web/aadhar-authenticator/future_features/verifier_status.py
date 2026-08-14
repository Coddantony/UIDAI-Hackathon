"""Verifier operational status states."""
from enum import Enum
class Status(str,Enum): PENDING='pending'; ACTIVE='active'; SUSPENDED='suspended'; REVOKED='revoked'
def can_verify(status:Status)->bool:return status is Status.ACTIVE
