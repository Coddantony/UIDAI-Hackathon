package com.example.uverifier.config;

/** Makes it explicit when a competition/demo build must not contact production identity services. */
public final class DemoModePolicy {
    private final boolean enabled;

    public DemoModePolicy(boolean enabled) {
        this.enabled = enabled;
    }

    public boolean isEnabled() { return enabled; }

    public void requireSandbox(boolean productionEnvironment) {
        if (enabled && productionEnvironment) {
            throw new IllegalStateException("Demo mode cannot use production identity services");
        }
    }
}
