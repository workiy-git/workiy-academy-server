from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import date


class InternshipApplicationBase(BaseModel):
	fullName: str
	dob: date
	phone: str
	email: EmailStr
	areaOfStudy: str
	institute: str
	graduationYear: int
	areaOfInterest: str
	skillRating: int
	resume: Optional[str] = None
	description: Optional[str] = None
	skills: List[str] = []


class InternshipApplicationCreate(InternshipApplicationBase):
	pass


class InternshipApplicationOut(BaseModel):
	id: int
	fullName: str
	dob: date
	phone: str
	email: EmailStr
	areaOfStudy: str
	institute: str
	graduationYear: int
	areaOfInterest: str
	skillRating: int
	resume: Optional[str] = None
	description: Optional[str] = None
	skills: List[str] = []

	class Config:
		from_attributes = True

