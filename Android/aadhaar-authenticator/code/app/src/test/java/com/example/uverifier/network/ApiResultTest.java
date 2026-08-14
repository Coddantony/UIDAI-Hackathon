package com.example.uverifier.network;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

public class ApiResultTest {
    @Test
    public void successResultContainsBodyAndStatus() {
        ApiResult result = ApiResult.success(200, "{\"ok\":true}");
        assertTrue(result.isSuccessful());
        assertEquals(200, result.getStatusCode());
        assertEquals("{\"ok\":true}", result.getBody());
    }

    @Test
    public void failureResultDoesNotExposeAResponseBody() {
        ApiResult result = ApiResult.failure(401, "Remote API returned HTTP 401");
        assertFalse(result.isSuccessful());
        assertEquals(401, result.getStatusCode());
        assertEquals("Remote API returned HTTP 401", result.getError());
    }
}
