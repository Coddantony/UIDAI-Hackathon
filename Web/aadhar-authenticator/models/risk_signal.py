from dataclasses import dataclass


@dataclass(frozen=True)
class RiskSignal:
    code: str
    score: int
    description: str

    def bounded_score(self) -> int:
        return max(0, min(100, self.score))
