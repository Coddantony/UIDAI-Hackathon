package com.example.uverifier.security;

/** Client-side guard against accidental OTP hammering. Server-side limits remain authoritative. */
public final class OtpAttemptPolicy {
    private final int maxAttempts;
    private final long cooldownMillis;
    private int attempts;
    private long nextAllowedAt;

    public OtpAttemptPolicy(int maxAttempts, long cooldownMillis) {
        if (maxAttempts <= 0 || cooldownMillis < 0) {
            throw new IllegalArgumentException("Invalid OTP policy");
        }
        this.maxAttempts = maxAttempts;
        this.cooldownMillis = cooldownMillis;
    }

    public synchronized boolean canAttempt(long nowMillis) {
        return attempts < maxAttempts && nowMillis >= nextAllowedAt;
    }

    public synchronized boolean recordAttempt(long nowMillis) {
        if (!canAttempt(nowMillis)) return false;
        attempts++;
        nextAllowedAt = nowMillis + cooldownMillis;
        return true;
    }

    public synchronized int getRemainingAttempts() {
        return Math.max(0, maxAttempts - attempts);
    }

    public synchronized void reset() {
        attempts = 0;
        nextAllowedAt = 0L;
    }
}
