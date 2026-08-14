package com.example.uverifier.network;

/** Immutable result for verifier API calls. Response bodies are never logged by this type. */
public final class ApiResult {
    private final int statusCode;
    private final String body;
    private final String error;

    private ApiResult(int statusCode, String body, String error) {
        this.statusCode = statusCode;
        this.body = body;
        this.error = error;
    }

    public static ApiResult success(int statusCode, String body) {
        return new ApiResult(statusCode, body, null);
    }

    public static ApiResult failure(int statusCode, String error) {
        return new ApiResult(statusCode, null, error);
    }

    public int getStatusCode() { return statusCode; }
    public String getBody() { return body; }
    public String getError() { return error; }
    public boolean isSuccessful() { return statusCode >= 200 && statusCode < 300; }
}
