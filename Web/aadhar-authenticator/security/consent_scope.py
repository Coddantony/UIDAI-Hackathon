"""Least-privilege consent scope validation."""

from dataclasses import dataclass


@dataclass(frozen=True)
class ConsentScope:
    purpose: str
    attributes: frozenset[str]


def validate_scope(requested: ConsentScope, granted: ConsentScope) -> None:
    """Raise ValueError when a request exceeds the user's granted scope."""
    if requested.purpose != granted.purpose:
        raise ValueError("consent purpose does not match")
    extra = requested.attributes - granted.attributes
    if extra:
        raise ValueError(f"attributes outside consent scope: {sorted(extra)}")
