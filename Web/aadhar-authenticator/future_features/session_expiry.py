"""Bounded verification session expiry."""
from datetime import datetime,timedelta,timezone
def deadline(minutes:int,now=None):return (now or datetime.now(timezone.utc))+timedelta(minutes=max(1,min(minutes,30)))
def expired(deadline,now=None):return (now or datetime.now(timezone.utc))>=deadline
