# Competition readiness

## Security
- Sensitive virtual identifiers are stored as keyed SHA-256 fingerprints rather than plaintext.
- Production startup rejects an unspecified JWT secret.
- Production CORS requires an explicit allow-list.
- API responses include request IDs and defensive security headers.
- API traffic is rate-limited per client address to reduce brute-force and abuse risk.
- Access logs have a 90-day TTL and indexed lookup paths.
- Authentication failures use generic messages to reduce account enumeration.

## Reliability
- Liveness and readiness endpoints verify MongoDB connectivity.
- MongoDB uniqueness and query indexes are created during startup.
- Backend regression tests run in GitHub Actions for pushes and pull requests.

## Demo strategy
- Keep the existing Android, verifier, and POC application flows intact while routing production traffic through `/api/v1`.
- Configure `SECRET_KEY`, `MONGO_HOST`, `MONGO_DBNAME`, `CORS_ORIGINS`, `ENVIRONMENT`, and rate-limit settings through deployment secrets/environment variables.
- Do not put Aadhaar/VID values, API keys, JWT secrets, or real eKYC payloads in source control, screenshots, logs, or issue comments.

## Migration note
Existing databases that contain the legacy plaintext `vid` field need a controlled migration to `vid_fingerprint` before switching traffic to this branch. The migration should run against an approved backup and must not print identifier values.
