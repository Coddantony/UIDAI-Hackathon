"""Stable, machine-readable API error contract."""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class ApiError:
    code: str
    message: str
    request_id: str | None = None
    retryable: bool = False
    details: dict[str, Any] | None = None

    def to_response(self) -> dict[str, Any]:
        payload = asdict(self)
        if payload["details"] is None:
            payload.pop("details")
        return {"success": False, "error": payload}


def client_error(code: str, message: str, request_id: str | None = None) -> dict[str, Any]:
    return ApiError(code, message, request_id=request_id).to_response()


def dependency_error(code: str, message: str, request_id: str | None = None) -> dict[str, Any]:
    return ApiError(code, message, request_id=request_id, retryable=True).to_response()
