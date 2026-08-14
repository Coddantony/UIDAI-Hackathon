"""Data classification labels for privacy-aware processing pipelines."""
from enum import Enum
class Classification(str,Enum): PUBLIC='public'; INTERNAL='internal'; SENSITIVE='sensitive'; RESTRICTED='restricted'
def stricter(a:Classification,b:Classification)->Classification:return max(a,b,key=lambda x:list(Classification).index(x))
