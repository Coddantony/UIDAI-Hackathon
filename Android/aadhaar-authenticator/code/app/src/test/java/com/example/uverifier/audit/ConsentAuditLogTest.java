package com.example.uverifier.audit;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotSame;

public class ConsentAuditLogTest {
    @Test
    public void snapshotIsDefensive() {
        ConsentAuditLog log = new ConsentAuditLog();
        log.record(new ConsentEvent(1L, ConsentEvent.Type.CONSENT_GRANTED, "ticketing", "txn-1"));
        assertEquals(1, log.snapshot().size());
        assertNotSame(log.snapshot(), log.snapshot());
    }

    @Test
    public void clearRemovesEvents() {
        ConsentAuditLog log = new ConsentAuditLog();
        log.record(new ConsentEvent(1L, ConsentEvent.Type.VERIFICATION_STARTED, "ticketing", "txn-2"));
        log.clear();
        assertEquals(0, log.snapshot().size());
    }
}
