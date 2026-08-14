package com.example.uverifier.config;

/** Environment configuration boundary. Production endpoints must be supplied by the deployment build. */
public final class VerifierEnvironment {
    public enum Type { SANDBOX, PRODUCTION }

    private final Type type;
    private final String baseUrl;

    private VerifierEnvironment(Type type, String baseUrl) {
        if (type == null || baseUrl == null || !baseUrl.startsWith("https://")) {
            throw new IllegalArgumentException("Environment and HTTPS base URL are required");
        }
        this.type = type;
        this.baseUrl = baseUrl.endsWith("/") ? baseUrl.substring(0, baseUrl.length() - 1) : baseUrl;
    }

    public static VerifierEnvironment sandbox(String baseUrl) {
        return new VerifierEnvironment(Type.SANDBOX, baseUrl);
    }

    public static VerifierEnvironment production(String baseUrl) {
        return new VerifierEnvironment(Type.PRODUCTION, baseUrl);
    }

    public Type getType() { return type; }
    public String getBaseUrl() { return baseUrl; }
}
