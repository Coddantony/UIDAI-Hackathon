"""Structured dependency health results for readiness endpoints."""

from dataclasses import dataclass


@dataclass(frozen=True)
class HealthProbe:
    name: str
    healthy: bool
    latency_ms: float | None = None
    detail: str | None = None

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "healthy": self.healthy,
            "latency_ms": self.latency_ms,
            "detail": self.detail,
        }
