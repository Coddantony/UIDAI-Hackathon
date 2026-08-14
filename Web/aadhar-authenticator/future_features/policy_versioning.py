"""Versioned policy selection for backward-compatible verifier rules."""
class PolicyRegistry:
    def __init__(self):self._policies={}
    def register(self,name,version,policy):self._policies[(name,version)]=policy
    def get(self,name,version):return self._policies[(name,version)]
