# API Security Notes

## Authentication

User sessions use short-lived JWT access tokens and longer-lived refresh tokens. Access tokens should be sent using the `Authorization: Bearer <token>` header.

## Verification API

Verifier access requires an active API key. Verification responses expose only the supported identity attributes.

## Operational guidance

- Keep JWT signing secrets outside source control.
- Restrict CORS origins in deployed environments.
- Use HTTPS for all API traffic.
- Rotate verifier API keys when compromise is suspected.
- Review access logs for unexpected verification activity.
