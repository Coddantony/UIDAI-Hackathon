package com.example.uverifier.security;

/** Short-lived verification state. Never stores Aadhaar, OTP or eKYC payloads. */
public final class VerificationSession {
    private final String transactionReference;
    private final long expiresAtMillis;

    public VerificationSession(String transactionReference, long issuedAtMillis, long lifetimeMillis) {
        if (transactionReference == null || transactionReference.trim().isEmpty() || lifetimeMillis <= 0) {
            throw new IllegalArgumentException("Invalid verification session");
        }
        this.transactionReference = transactionReference;
        this.expiresAtMillis = issuedAtMillis + lifetimeMillis;
    }

    public String getTransactionReference() { return transactionReference; }

    public boolean isExpired(long nowMillis) {
        return nowMillis >= expiresAtMillis;
    }
}
