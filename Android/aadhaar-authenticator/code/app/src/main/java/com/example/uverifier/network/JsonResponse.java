package com.example.uverifier.network;

import org.json.JSONException;
import org.json.JSONObject;

/** Safe structured JSON accessor replacing brittle comma/colon string splitting. */
public final class JsonResponse {
    private final JSONObject object;

    private JsonResponse(JSONObject object) {
        this.object = object;
    }

    public static JsonResponse parse(String body) throws JSONException {
        if (body == null || body.trim().isEmpty()) throw new JSONException("Empty response");
        return new JsonResponse(new JSONObject(body));
    }

    public String requireString(String key) throws JSONException {
        String value = object.optString(key, null);
        if (value == null || value.trim().isEmpty()) throw new JSONException("Missing field: " + key);
        return value;
    }

    public String optionalString(String key) {
        return object.optString(key, null);
    }

    public boolean has(String key) {
        return object.has(key) && !object.isNull(key);
    }
}
