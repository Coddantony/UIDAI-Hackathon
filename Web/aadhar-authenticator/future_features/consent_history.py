"""Bounded consent history container."""
class ConsentHistory:
    def __init__(self,limit=100):self.limit=limit;self.items=[]
    def add(self,event):self.items.append(event);self.items=self.items[-self.limit:]
