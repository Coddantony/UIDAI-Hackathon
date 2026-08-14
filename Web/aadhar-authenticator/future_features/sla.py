"""Verification SLA classification."""
def breach(elapsed_ms:int,target_ms:int)->bool:return elapsed_ms>target_ms
def percentile_bucket(elapsed_ms:int)->str:return 'fast' if elapsed_ms<250 else 'normal' if elapsed_ms<1000 else 'slow'
