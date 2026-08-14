"""Canonical JSON encoding for signatures, hashes and audit fingerprints."""

from __future__ import annotations

import json
from typing import Any


def canonical_json(value: Any) -> str:
    """Serialize JSON deterministically without leaking implementation ordering."""
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def canonical_bytes(value: Any) -> bytes:
    return canonical_json(value).encode("utf-8")
