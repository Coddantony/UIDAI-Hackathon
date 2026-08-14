"""Human-readable consent text generation from structured requests."""
def explain(purpose:str,attributes:list[str],ttl_minutes:int)->str:
    fields=', '.join(sorted(attributes));return f"Share {fields} with the verifier for {purpose} for up to {ttl_minutes} minutes."
