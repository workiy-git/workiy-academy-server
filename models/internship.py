from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, SmallInteger
from sqlalchemy.orm import relationship
from database import Base


class InternshipApplication(Base):
	__tablename__ = "internship_applications"

	id = Column(Integer, primary_key=True, index=True)
	full_name = Column(String(100), nullable=False)
	dob = Column(Date, nullable=False)
	phone = Column(String(20), nullable=False, index=True)
	email = Column(String(255), nullable=False, index=True)
	area_of_study = Column(String(100), nullable=False)
	institute = Column(String(150), nullable=False)
	graduation_year = Column(SmallInteger, nullable=False)
	area_of_interest = Column(String(100), nullable=False)
	skill_rating = Column(SmallInteger, nullable=False)
	resume = Column(String(255), nullable=True)
	description = Column(Text, nullable=True)

	skills = relationship("InternshipApplicationSkill", back_populates="application", cascade="all, delete-orphan")


class InternshipApplicationSkill(Base):
	__tablename__ = "internship_application_skills"

	id = Column(Integer, primary_key=True, index=True)
	application_id = Column(Integer, ForeignKey("internship_applications.id", ondelete="CASCADE"), nullable=False)
	skill = Column(String(100), nullable=False)

	application = relationship("InternshipApplication", back_populates="skills")

