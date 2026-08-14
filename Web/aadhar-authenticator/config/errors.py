"""Stable application error codes for API clients and observability."""

INVALID_CREDENTIALS = "AUTH_INVALID_CREDENTIALS"
ACCOUNT_INACTIVE = "AUTH_ACCOUNT_INACTIVE"
INVALID_TOKEN = "AUTH_INVALID_TOKEN"
INVALID_API_KEY = "VERIFIER_INVALID_API_KEY"
USER_NOT_FOUND = "USER_NOT_FOUND"
INVALID_EKYC = "EKYC_INVALID_XML"
RATE_LIMITED = "REQUEST_RATE_LIMITED"

ERROR_MESSAGES = {
    INVALID_CREDENTIALS: "Authentication failed",
    ACCOUNT_INACTIVE: "Account is inactive",
    INVALID_TOKEN: "Authentication token is invalid",
    INVALID_API_KEY: "Verifier API key is invalid",
    USER_NOT_FOUND: "User does not exist",
    INVALID_EKYC: "The supplied eKYC document is invalid",
    RATE_LIMITED: "Too many requests",
}
