
from sqlalchemy import Column, Integer, String, Date
from database import Base

class Internship(Base):
	__tablename__ = "internship"

	id = Column(Integer, primary_key=True, index=True)
	fullName = Column(String(255), nullable=False)
	dob = Column(Date, nullable=False)
	phone = Column(String(255), nullable=False)
	email = Column(String(255), nullable=False)
	areaOfStudy = Column(String(255), nullable=False)
	institute = Column(String(255), nullable=False)
	graduationYear = Column(Integer, nullable=False)
	areaOfInterest = Column(String(255), nullable=False)
	skillRating = Column(Integer, nullable=False)
	resume = Column(String(255), nullable=False)
	description = Column(String(255), nullable=True)
	skills = Column(String(255), nullable=True)  # Comma-separated string
