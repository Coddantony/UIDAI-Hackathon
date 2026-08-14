"""Minimal circuit breaker for unreliable verification dependencies."""
class Circuit:
    def __init__(self,threshold=5):self.threshold=threshold;self.failures=0;self.open=False
    def failure(self):self.failures+=1;self.open=self.failures>=self.threshold
    def success(self):self.failures=0;self.open=False
