"""Readiness checklist fields for future face-authentication onboarding."""
REQUIRED={'device_attestation','operator_auth','consent','liveness','audit'}
def missing(checklist:set[str])->set[str]:return REQUIRED-checklist
