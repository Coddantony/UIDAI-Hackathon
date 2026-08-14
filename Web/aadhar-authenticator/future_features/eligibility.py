"""Privacy-preserving eligibility predicates over a birth date."""
from datetime import date

def age_on(dob:date,at:date|None=None)->int:
    at=at or date.today();return at.year-dob.year-((at.month,at.day)<(dob.month,dob.day))

def eligible(dob:date,min_age:int,max_age:int|None=None,at:date|None=None)->bool:
    age=age_on(dob,at);return age>=min_age and (max_age is None or age<=max_age)
