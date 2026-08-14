"""Explicit fallback decisions when online verification is unavailable."""
from enum import Enum
class Fallback(str,Enum): DENY='deny'; OFFLINE_PROOF='offline_proof'; RETRY='retry'
def choose(online:bool,offline_available:bool)->Fallback:return Fallback.RETRY if online else (Fallback.OFFLINE_PROOF if offline_available else Fallback.DENY)
