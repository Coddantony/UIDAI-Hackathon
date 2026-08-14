# Testing Strategy

## API tests

Cover registration, login, refresh, current-user access, verifier authentication, invalid API keys, inactive accounts, missing users, and access-log summaries.

## Parser tests

Cover valid eKYC XML, missing `Poi`, missing attributes, malformed XML, and empty input.

## Security tests

Verify protected routes reject missing or invalid bearer tokens and that identity responses expose only approved fields.
