package com.example.uverifier.audit;

/** Privacy-safe consent/audit event. Contains metadata only; never store Aadhaar, OTP or eKYC XML. */
public final class ConsentEvent {
    public enum Type { CONSENT_SHOWN, CONSENT_GRANTED, CONSENT_DENIED, VERIFICATION_STARTED, VERIFICATION_COMPLETED, VERIFICATION_FAILED }

    private final long timestampMillis;
    private final Type type;
    private final String purpose;
    private final String transactionReference;

    public ConsentEvent(long timestampMillis, Type type, String purpose, String transactionReference) {
        this.timestampMillis = timestampMillis;
        this.type = type;
        this.purpose = purpose;
        this.transactionReference = transactionReference;
    }

    public long getTimestampMillis() { return timestampMillis; }
    public Type getType() { return type; }
    public String getPurpose() { return purpose; }
    public String getTransactionReference() { return transactionReference; }
}
