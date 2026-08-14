from collections import Counter

_counters = Counter()

def increment(name: str) -> None:
    _counters[name] += 1

def snapshot() -> dict:
    return dict(_counters)
