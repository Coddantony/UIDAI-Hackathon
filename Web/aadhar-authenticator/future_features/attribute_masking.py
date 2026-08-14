"""Display-safe masking for identity attributes."""
def mask(value:str,visible:int=2,fill='*')->str:
    if not value:return value
    n=max(0,min(visible,len(value)));return value[:n]+fill*max(0,len(value)-n)
