from enum import Enum


class VerificationPurpose(str, Enum):
    BENEFIT = "benefit"
    SERVICE = "service"
    ACCOUNT = "account"
    KYC = "kyc"
