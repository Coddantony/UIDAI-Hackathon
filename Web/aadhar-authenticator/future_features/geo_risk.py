"""Simple travel-speed anomaly detector for risk engines."""
from math import radians,sin,cos,asin,sqrt
def km(a:tuple[float,float],b:tuple[float,float])->float:
    lat1,lon1,lat2,lon2=map(radians,(*a,*b));dlat=lat2-lat1;dlon=lon2-lon1
    x=sin(dlat/2)**2+cos(lat1)*cos(lat2)*sin(dlon/2)**2
    return 6371*2*asin(sqrt(x))
def impossible(a,b,hours,max_kmh=900)->bool:return km(a,b)/max(hours,0.01)>max_kmh
