# Threat Model

## Assets

- User identity attributes returned by verification.
- Device and virtual identifiers.
- Verifier API keys.
- Authentication and access-log data.

## Primary threats

- Credential theft and token replay.
- Unauthorized verifier access.
- Transport interception.
- Malformed identity XML.
- Excessive exposure of identity attributes.

## Mitigations

Use short-lived access tokens, HTTPS, active-account checks, defensive XML parsing, restricted response fields, API-key controls, and audit logging.
