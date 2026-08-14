package com.example.uverifier.audit;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/** In-memory audit trail suitable for an adapter to a protected persistence layer. */
public final class ConsentAuditLog {
    private final List<ConsentEvent> events = new ArrayList<>();

    public synchronized void record(ConsentEvent event) {
        if (event == null) throw new IllegalArgumentException("event must not be null");
        events.add(event);
    }

    public synchronized List<ConsentEvent> snapshot() {
        return Collections.unmodifiableList(new ArrayList<>(events));
    }

    public synchronized void clear() {
        events.clear();
    }
}
