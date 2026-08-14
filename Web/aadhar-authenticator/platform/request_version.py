"""Versioned request envelope metadata for backward-compatible API evolution."""

from dataclasses import dataclass

SUPPORTED_VERSIONS = frozenset({"1.0", "1.1", "2.0"})


@dataclass(frozen=True)
class RequestVersion:
    value: str

    def validate(self) -> str:
        if self.value not in SUPPORTED_VERSIONS:
            raise ValueError(f"unsupported request version: {self.value}")
        return self.value
