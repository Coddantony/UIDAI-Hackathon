"""Declarative attribute minimization policies."""
class AttributePolicy:
    def __init__(self,rules:dict[str,set[str]]):self.rules=rules
    def allowed(self,purpose:str)->set[str]:return set(self.rules.get(purpose,set()))
    def filter(self,purpose:str,claims:dict)->dict:
        allowed=self.allowed(purpose);return {k:v for k,v in claims.items() if k in allowed}
