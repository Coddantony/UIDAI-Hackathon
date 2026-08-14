from enum import StrEnum


class VerificationPurpose(StrEnum):
    SERVICE_ACCESS = "service_access"
    ACCOUNT_RECOVERY = "account_recovery"
    BENEFIT_DELIVERY = "benefit_delivery"
    OPERATOR_VERIFICATION = "operator_verification"


ALLOWED_PURPOSES = frozenset(item.value for item in VerificationPurpose)


def validate_purpose(purpose: str) -> str:
    if purpose not in ALLOWED_PURPOSES:
        raise ValueError("Unsupported verification purpose")
    return purpose
