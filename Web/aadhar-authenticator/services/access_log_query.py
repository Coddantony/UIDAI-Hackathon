"""Reusable access-log query constraints."""


def normalize_access_log_window(skip: int = 0, limit: int = 50) -> tuple[int, int]:
    return max(skip, 0), min(max(limit, 1), 100)
