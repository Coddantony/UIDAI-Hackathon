import os

os.environ.setdefault("SECRET_KEY", "test-secret")
os.environ.setdefault("ENVIRONMENT", "test")

from utils.identity import fingerprint


def test_fingerprint_is_deterministic():
    assert fingerprint("123456789012") == fingerprint("123456789012")


def test_fingerprint_is_not_plaintext():
    value = "123456789012"
    assert fingerprint(value) != value
    assert len(fingerprint(value)) == 64
