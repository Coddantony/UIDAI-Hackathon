# Incident Response

1. Disable compromised verifier accounts or rotate affected API keys.
2. Rotate JWT signing secrets if token compromise is suspected.
3. Review access logs for affected verification identifiers.
4. Preserve correlation IDs and timestamps for investigation.
5. Avoid recording raw identity XML or credentials in incident artifacts.
6. Restore service only after configuration and access controls are verified.
