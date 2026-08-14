package com.example.uverifier.security;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SensitiveDataRedactorTest {
    @Test
    public void payloadIsAlwaysRedacted() {
        assertEquals("<redacted>", SensitiveDataRedactor.redact("123456789012"));
        assertEquals("<null>", SensitiveDataRedactor.redact(null));
    }

    @Test
    public void operationNameIsSafeForDiagnostics() {
        assertEquals("otp_generate failed with HTTP 429",
                SensitiveDataRedactor.describeHttpFailure(429, "otp/generate"));
    }
}
