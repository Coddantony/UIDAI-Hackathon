"""Bounded exponential retry schedule for transient verification failures."""
def delays(attempts:int,base:float=0.25,cap:float=8.0)->list[float]:return [min(cap,base*(2**i)) for i in range(max(0,attempts))]
