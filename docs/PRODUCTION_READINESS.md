# UVerifier production-readiness plan

## Objective

UVerifier is intended to reduce friction in identity-backed check-in and booking flows. A competition prototype must not be presented as a production UIDAI integration until endpoint authorization, data-retention rules, cryptographic requirements and deployment approvals are independently verified.

## Security baseline

- Use HTTPS for every network request.
- Do not log Aadhaar numbers, OTPs, mobile numbers, VID values, eKYC XML, QR payloads or authentication responses.
- Do not persist raw identity credentials in ordinary SharedPreferences.
- Keep backup/export disabled for sensitive application state.
- Minimize Android permissions; request runtime permissions only when a documented feature requires them.
- Enforce input validation before any network request.
- Apply explicit network timeouts and bounded retries.

## Privacy by design

1. Collect only fields required for the stated purpose.
2. Display masked identifiers by default.
3. Record consent and workflow metadata without storing identity payloads.
4. Define retention and deletion policies before production deployment.
5. Separate demonstration/mock data from real identity data.
6. Provide an explicit failure state rather than silently retrying sensitive operations.

## Threat model

| Threat | Control |
|---|---|
| Cleartext interception | TLS-only network security configuration |
| Sensitive log leakage | Redacted logging policy; never log request/response bodies |
| Device backup leakage | Disable Android backup for the verifier |
| Invalid identity input | Client-side format + checksum validation |
| Replay of stale workflow state | Bind requests to server-issued transaction references and expiry |
| OTP abuse | Server-side rate limits, attempt limits and expiry |
| Malicious APK modification | Release signing, integrity checks and controlled distribution |
| Lost/stolen device | No raw credential persistence; short-lived session state |

## API integration requirements

The current repository contains historical stage endpoints and prototype-only integrations. Before any real deployment:

- confirm current UIDAI-approved APIs and authorization requirements;
- move all environment-specific endpoints into configuration;
- remove hard-coded transaction IDs, share codes, VID values and credentials;
- use structured JSON parsing rather than comma/colon string splitting;
- define typed error codes for timeout, authentication, validation, rate-limit and server failures;
- add contract tests against an approved mock/sandbox service.

## Enterprise readiness

- CI must run unit tests and an APK build for every pull request.
- Add dependency vulnerability scanning and secret scanning.
- Add crash-safe telemetry that contains no identity payloads.
- Maintain an architecture decision record for every security-sensitive integration.
- Produce a deployment runbook and incident-response procedure.

## Competition demo boundary

The demo should clearly label simulated or sandbox behavior. Real Aadhaar data should not be used in screenshots, fixtures, tests, logs, sample payloads or public issue discussions.
