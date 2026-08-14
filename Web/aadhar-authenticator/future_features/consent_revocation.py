"""Fast consent revocation checks."""
class ConsentRegistry:
    def __init__(self): self._revoked:set[str]=set()
    def revoke(self,consent_id:str)->None:self._revoked.add(consent_id)
    def is_revoked(self,consent_id:str)->bool:return consent_id in self._revoked
    def require_active(self,consent_id:str)->None:
        if self.is_revoked(consent_id): raise PermissionError("consent revoked")
