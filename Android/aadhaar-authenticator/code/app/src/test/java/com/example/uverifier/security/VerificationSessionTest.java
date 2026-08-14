package com.example.uverifier.security;

import org.junit.Test;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class VerificationSessionTest {
    @Test
    public void expiresAtConfiguredBoundary() {
        VerificationSession session = new VerificationSession("txn-demo", 1000L, 5000L);
        assertFalse(session.isExpired(5999L));
        assertTrue(session.isExpired(6000L));
    }
}
