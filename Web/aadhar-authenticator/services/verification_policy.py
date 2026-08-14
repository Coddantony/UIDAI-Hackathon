ALLOWED_PURPOSES = {"identity_verification", "kyc", "account_recovery"}


def purpose_allowed(purpose: str) -> bool:
    return purpose in ALLOWED_PURPOSES
