"""Aggregate counters without identity subjects."""
class AnonymizedCounter:
    def __init__(self):self.counts={}
    def inc(self,event:str,n:int=1):self.counts[event]=self.counts.get(event,0)+max(0,n)
    def snapshot(self):return dict(self.counts)
