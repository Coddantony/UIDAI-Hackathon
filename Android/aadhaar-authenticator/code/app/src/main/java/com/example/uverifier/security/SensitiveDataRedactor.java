package com.example.uverifier.security;

/** Defensive redaction utilities for diagnostics. Prefer not logging sensitive payloads at all. */
public final class SensitiveDataRedactor {
    private SensitiveDataRedactor() { }

    public static String redact(String value) {
        return value == null ? "<null>" : "<redacted>";
    }

    public static String describeHttpFailure(int statusCode, String operation) {
        String safeOperation = operation == null || operation.trim().isEmpty()
                ? "unknown-operation" : operation.replaceAll("[^A-Za-z0-9._-]", "_");
        return safeOperation + " failed with HTTP " + statusCode;
    }
}
