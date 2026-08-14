"""Retention deadline calculation for auditable records."""
from datetime import datetime,timedelta,timezone
def expires_after(days:int,created=None):return (created or datetime.now(timezone.utc))+timedelta(days=max(0,days))
