"""Single-use nonce registry for replay-resistant verification requests."""
class NonceRegistry:
    def __init__(self): self._seen:set[str]=set()
    def consume(self,nonce:str)->bool:
        if not nonce or nonce in self._seen:return False
        self._seen.add(nonce);return True
