# Architecture Decisions

- FastAPI provides the HTTP API layer.
- MongoDB is accessed asynchronously through Motor.
- JWT access and refresh tokens separate short-lived API access from renewal.
- Verifier API keys identify external verification clients.
- Access logs provide an audit trail for identity lookups.
- eKYC XML is parsed into a limited set of supported identity attributes.
