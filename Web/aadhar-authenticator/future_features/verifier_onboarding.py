"""Enterprise verifier onboarding validation."""
REQUIRED={'organization','contact','purpose','scopes'}
def validate(profile:dict)->tuple[bool,list[str]]:
    missing=sorted(REQUIRED-profile.keys());return not missing,missing
