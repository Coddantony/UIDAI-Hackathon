package com.example.uverifier.network;

import org.json.JSONException;
import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class JsonResponseTest {
    @Test
    public void readsStructuredFields() throws Exception {
        JsonResponse response = JsonResponse.parse("{\"txnId\":\"abc\",\"status\":\"Success\"}");
        assertEquals("abc", response.requireString("txnId"));
        assertEquals("Success", response.optionalString("status"));
        assertTrue(response.has("txnId"));
    }

    @Test(expected = JSONException.class)
    public void rejectsMissingRequiredField() throws Exception {
        JsonResponse.parse("{\"status\":\"Success\"}").requireString("txnId");
    }
}
