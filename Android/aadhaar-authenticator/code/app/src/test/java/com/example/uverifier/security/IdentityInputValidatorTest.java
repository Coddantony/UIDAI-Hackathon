package com.example.uverifier.security;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class IdentityInputValidatorTest {
    @Test
    public void validatesKnownVerhoeffExamples() {
        assertTrue(IdentityInputValidator.isValidAadhaar("236919785312"));
        assertFalse(IdentityInputValidator.isValidAadhaar("236919785313"));
        assertFalse(IdentityInputValidator.isValidAadhaar("123456789012"));
    }

    @Test
    public void validatesOtp() {
        assertTrue(IdentityInputValidator.isValidOtp("123456"));
        assertFalse(IdentityInputValidator.isValidOtp("12345"));
        assertFalse(IdentityInputValidator.isValidOtp("12345a"));
    }

    @Test
    public void validatesMobile() {
        assertTrue(IdentityInputValidator.isValidIndianMobile("9876543210"));
        assertFalse(IdentityInputValidator.isValidIndianMobile("5876543210"));
        assertFalse(IdentityInputValidator.isValidIndianMobile("987654321"));
    }

    @Test
    public void masksSensitiveIdentifiers() {
        assertEquals("••••••••5312", IdentityInputValidator.maskAadhaar("236919785312"));
        assertEquals("••••••3210", IdentityInputValidator.maskMobile("9876543210"));
    }
}
