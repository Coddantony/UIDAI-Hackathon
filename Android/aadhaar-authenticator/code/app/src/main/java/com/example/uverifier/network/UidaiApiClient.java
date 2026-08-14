package com.example.uverifier.network;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.Map;

/** Small blocking HTTP adapter. Call from a worker thread; UI code should not perform network I/O. */
public final class UidaiApiClient {
    private static final int CONNECT_TIMEOUT_MS = 10_000;
    private static final int READ_TIMEOUT_MS = 20_000;
    private final String baseUrl;

    public UidaiApiClient(String baseUrl) {
        if (baseUrl == null || !baseUrl.startsWith("https://")) {
            throw new IllegalArgumentException("UIDAI API base URL must use HTTPS");
        }
        this.baseUrl = trimTrailingSlash(baseUrl);
    }

    public ApiResult postJson(String path, String json, Map<String, String> headers) {
        HttpURLConnection connection = null;
        try {
            URL url = new URL(baseUrl + "/" + trimLeadingSlash(path));
            connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("POST");
            connection.setConnectTimeout(CONNECT_TIMEOUT_MS);
            connection.setReadTimeout(READ_TIMEOUT_MS);
            connection.setDoOutput(true);
            connection.setRequestProperty("Accept", "application/json");
            connection.setRequestProperty("Content-Type", "application/json; charset=utf-8");
            if (headers != null) {
                for (Map.Entry<String, String> entry : headers.entrySet()) {
                    if (entry.getKey() != null && entry.getValue() != null) {
                        connection.setRequestProperty(entry.getKey(), entry.getValue());
                    }
                }
            }

            byte[] payload = json == null ? new byte[0] : json.getBytes(StandardCharsets.UTF_8);
            try (OutputStream output = connection.getOutputStream()) {
                output.write(payload);
            }

            int status = connection.getResponseCode();
            InputStream stream = status >= 400 ? connection.getErrorStream() : connection.getInputStream();
            String body = readBody(stream);
            if (status >= 200 && status < 300) {
                return ApiResult.success(status, body);
            }
            return ApiResult.failure(status, "Remote API returned HTTP " + status);
        } catch (IOException e) {
            return ApiResult.failure(-1, "Network request failed");
        } finally {
            if (connection != null) connection.disconnect();
        }
    }

    private static String readBody(InputStream stream) throws IOException {
        if (stream == null) return "";
        StringBuilder body = new StringBuilder();
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(stream, StandardCharsets.UTF_8))) {
            String line;
            while ((line = reader.readLine()) != null) body.append(line);
        }
        return body.toString();
    }

    private static String trimTrailingSlash(String value) {
        return value.endsWith("/") ? value.substring(0, value.length() - 1) : value;
    }

    private static String trimLeadingSlash(String value) {
        return value.startsWith("/") ? value.substring(1) : value;
    }
}
