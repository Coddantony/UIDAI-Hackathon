package com.example.uverifier.config;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertThrows;

public class VerifierEnvironmentTest {
    @Test
    public void normalizesTrailingSlash() {
        VerifierEnvironment environment = VerifierEnvironment.sandbox("https://sandbox.example/");
        assertEquals("https://sandbox.example", environment.getBaseUrl());
        assertEquals(VerifierEnvironment.Type.SANDBOX, environment.getType());
    }

    @Test
    public void rejectsCleartextEndpoints() {
        assertThrows(IllegalArgumentException.class,
                () -> VerifierEnvironment.sandbox("http://sandbox.example"));
    }
}
