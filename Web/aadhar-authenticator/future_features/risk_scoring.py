"""Deterministic verification risk scoring primitive."""
from dataclasses import dataclass
@dataclass(frozen=True)
class RiskSignals:
    failed_attempts:int=0
    velocity:int=0
    new_device:bool=False
    impossible_travel:bool=False
class RiskScorer:
    def score(self,s:RiskSignals)->int:
        return min(100, s.failed_attempts*10+s.velocity*5+(20 if s.new_device else 0)+(40 if s.impossible_travel else 0))
    def band(self,score:int)->str:
        return "low" if score<30 else "medium" if score<70 else "high"
