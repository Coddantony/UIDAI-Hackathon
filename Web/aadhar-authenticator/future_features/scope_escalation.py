"""Detect requests that exceed an application's previously approved scopes."""
def escalation(granted:set[str],requested:set[str])->set[str]:return requested-granted
