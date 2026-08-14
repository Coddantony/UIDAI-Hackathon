"""Fine-grained permissions for verifier applications."""
class VerifierScopes:
    READ_IDENTITY="identity:read"; VERIFY="identity:verify"; AUDIT="audit:read"; ADMIN="verifier:admin"
    @classmethod
    def allowed(cls,granted:set[str],required:str)->bool:return required in granted or cls.ADMIN in granted
