"""Small registry for discoverable verifier metadata."""
class VerifierDirectory:
    def __init__(self):self._items={}
    def register(self,verifier_id,metadata):self._items[verifier_id]=dict(metadata)
    def get(self,verifier_id):return dict(self._items[verifier_id])
