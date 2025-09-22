# Import necessary modules

from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date

class InternshipCreate(BaseModel):
	fullName: str
	dob: date
	phone: str
	email: EmailStr
	areaOfStudy: str
	institute: str
	graduationYear: int
	areaOfInterest: str
	skillRating: int
	resume: str
	description: Optional[str] = None
	skills: List[str] = []

class InternshipOut(InternshipCreate):
	id: int

	class Config:
		from_attributes = True
