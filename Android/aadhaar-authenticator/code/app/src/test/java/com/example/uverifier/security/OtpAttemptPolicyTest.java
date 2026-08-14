package com.example.uverifier.security;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class OtpAttemptPolicyTest {
    @Test
    public void enforcesCooldownAndAttemptLimit() {
        OtpAttemptPolicy policy = new OtpAttemptPolicy(2, 1000L);
        assertTrue(policy.recordAttempt(1000L));
        assertFalse(policy.recordAttempt(1000L));
        assertTrue(policy.recordAttempt(2000L));
        assertFalse(policy.recordAttempt(3000L));
    }

    @Test
    public void resetRestoresPolicy() {
        OtpAttemptPolicy policy = new OtpAttemptPolicy(1, 0L);
        assertTrue(policy.recordAttempt(1L));
        assertFalse(policy.recordAttempt(2L));
        policy.reset();
        assertTrue(policy.recordAttempt(3L));
    }
}
