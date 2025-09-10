from sqlalchemy.orm import Session
from typing import List, Optional
from models.internship import InternshipApplication, InternshipApplicationSkill
from schemas.internship import (
	InternshipApplicationCreate,
	InternshipApplicationOut,
)

def get_internship_application_by_phone(db: Session, phone: str):
	db_app = db.query(InternshipApplication).filter(InternshipApplication.phone == phone).first()
	if not db_app:
		return None
	skills = [skill.skill for skill in getattr(db_app, 'skills', [])]
	return InternshipApplicationOut(
		id=db_app.id,
		fullName=db_app.full_name,
		dob=db_app.dob,
		phone=db_app.phone,
		email=db_app.email,
		areaOfStudy=db_app.area_of_study,
		institute=db_app.institute,
		graduationYear=db_app.graduation_year,
		areaOfInterest=db_app.area_of_interest,
		skillRating=db_app.skill_rating,
		resume=db_app.resume,
		description=db_app.description,
		skills=skills
	)
from sqlalchemy.orm import Session
from typing import List, Optional
from models.internship import InternshipApplication, InternshipApplicationSkill
from schemas.internship import (
	InternshipApplicationCreate,
	InternshipApplicationOut,
)


def create_internship_application(db: Session, application: InternshipApplicationCreate) -> InternshipApplication:
	# Create main application
	db_app = InternshipApplication(
		full_name=application.fullName,
		dob=application.dob,
		phone=application.phone,
		email=application.email,
		area_of_study=application.areaOfStudy,
		institute=application.institute,
		graduation_year=application.graduationYear,
		area_of_interest=application.areaOfInterest,
		skill_rating=application.skillRating,
		resume=application.resume,
		description=application.description,
	)
	db.add(db_app)
	db.commit()
	db.refresh(db_app)

	# Attach skills
	if application.skills:
		for skill_name in application.skills:
			if not skill_name:
				continue
			db_skill = InternshipApplicationSkill(application_id=db_app.id, skill=skill_name)
			db.add(db_skill)
		db.commit()

	# Eager load skills for return
	db.refresh(db_app)
	# Prepare skills as list of strings
	skills = [skill.skill for skill in getattr(db_app, 'skills', [])]
	# Return as Pydantic schema
	return InternshipApplicationOut(
		id=db_app.id,
		fullName=db_app.full_name,
		dob=db_app.dob,
		phone=db_app.phone,
		email=db_app.email,
		areaOfStudy=db_app.area_of_study,
		institute=db_app.institute,
		graduationYear=db_app.graduation_year,
		areaOfInterest=db_app.area_of_interest,
		skillRating=db_app.skill_rating,
		resume=db_app.resume,
		description=db_app.description,
		skills=skills
	)


def get_internship_application(db: Session, application_id: int) -> Optional[InternshipApplication]:
	db_app = db.query(InternshipApplication).filter(InternshipApplication.id == application_id).first()
	if not db_app:
		return None
	skills = [skill.skill for skill in getattr(db_app, 'skills', [])]
	from schemas.internship import InternshipApplicationOut
	return InternshipApplicationOut(
		id=db_app.id,
		fullName=db_app.full_name,
		dob=db_app.dob,
		phone=db_app.phone,
		email=db_app.email,
		areaOfStudy=db_app.area_of_study,
		institute=db_app.institute,
		graduationYear=db_app.graduation_year,
		areaOfInterest=db_app.area_of_interest,
		skillRating=db_app.skill_rating,
		resume=db_app.resume,
		description=db_app.description,
		skills=skills
	)


def get_internship_applications(db: Session, skip: int = 0, limit: int = 100) -> List[InternshipApplication]:
	db_apps = db.query(InternshipApplication).offset(skip).limit(limit).all()
	from schemas.internship import InternshipApplicationOut
	result = []
	for db_app in db_apps:
		skills = [skill.skill for skill in getattr(db_app, 'skills', [])]
		result.append(InternshipApplicationOut(
			id=db_app.id,
			fullName=db_app.full_name,
			dob=db_app.dob,
			phone=db_app.phone,
			email=db_app.email,
			areaOfStudy=db_app.area_of_study,
			institute=db_app.institute,
			graduationYear=db_app.graduation_year,
			areaOfInterest=db_app.area_of_interest,
			skillRating=db_app.skill_rating,
			resume=db_app.resume,
			description=db_app.description,
			skills=skills
		))
	return result


def update_internship_application(db: Session, application_id: int, data: InternshipApplicationCreate) -> Optional[InternshipApplication]:
	app = db.query(InternshipApplication).filter(InternshipApplication.id == application_id).first()
	if not app:
		return None

	# Update scalar fields
	app.full_name = data.fullName
	app.dob = data.dob
	app.phone = data.phone
	app.email = data.email
	app.area_of_study = data.areaOfStudy
	app.institute = data.institute
	app.graduation_year = data.graduationYear
	app.area_of_interest = data.areaOfInterest
	app.skill_rating = data.skillRating
	app.resume = data.resume
	app.description = data.description

	# Replace skills
	if data.skills is not None:
		# Clear existing
		for existing in list(app.skills):
			db.delete(existing)
		# Add new
		for skill_name in data.skills:
			if not skill_name:
				continue
			db_skill = InternshipApplicationSkill(application_id=app.id, skill=skill_name)
			db.add(db_skill)
	db.commit()
	db.refresh(app)
	skills = [skill.skill for skill in getattr(app, 'skills', [])]
	from schemas.internship import InternshipApplicationOut
	return InternshipApplicationOut(
		id=app.id,
		fullName=app.full_name,
		dob=app.dob,
		phone=app.phone,
		email=app.email,
		areaOfStudy=app.area_of_study,
		institute=app.institute,
		graduationYear=app.graduation_year,
		areaOfInterest=app.area_of_interest,
		skillRating=app.skill_rating,
		resume=app.resume,
		description=app.description,
		skills=skills
	)


def delete_internship_application(db: Session, application_id: int) -> bool:
	app = db.query(InternshipApplication).filter(InternshipApplication.id == application_id).first()
	if not app:
		return False
	db.delete(app)
	db.commit()
	return True

