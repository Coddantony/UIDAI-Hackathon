"""API version deprecation metadata."""
from dataclasses import dataclass
@dataclass(frozen=True)
class Deprecation: version:str; sunset:str; replacement:str
