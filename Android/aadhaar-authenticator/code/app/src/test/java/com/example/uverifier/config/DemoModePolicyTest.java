package com.example.uverifier.config;

import org.junit.Test;

import static org.junit.Assert.assertThrows;
import static org.junit.Assert.assertTrue;

public class DemoModePolicyTest {
    @Test
    public void demoBuildAllowsSandbox() {
        DemoModePolicy policy = new DemoModePolicy(true);
        policy.requireSandbox(false);
        assertTrue(policy.isEnabled());
    }

    @Test
    public void demoBuildRejectsProduction() {
        DemoModePolicy policy = new DemoModePolicy(true);
        assertThrows(IllegalStateException.class, () -> policy.requireSandbox(true));
    }
}
