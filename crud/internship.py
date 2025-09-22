from sqlalchemy.orm import Session
from models.internship import Internship
from schemas.internship import InternshipCreate

def create_internship(db: Session, internship: InternshipCreate):
	db_internship = Internship(
		fullName=internship.fullName,
		dob=internship.dob,
		phone=internship.phone,
		email=internship.email,
		areaOfStudy=internship.areaOfStudy,
		institute=internship.institute,
		graduationYear=internship.graduationYear,
		areaOfInterest=internship.areaOfInterest,
		skillRating=internship.skillRating,
		resume=internship.resume,
		description=internship.description,
		skills=','.join(internship.skills) if internship.skills else None
	)
	db.add(db_internship)
	db.commit()
	db.refresh(db_internship)
	# Convert skills string back to list for API response
	result = db_internship.__dict__.copy()
	result['skills'] = db_internship.skills.split(',') if db_internship.skills else []
	result['id'] = db_internship.id
	return type('InternshipOutObj', (), result)()


def get_internships(db: Session, skip: int = 0, limit: int = 100):
	db_objs = db.query(Internship).offset(skip).limit(limit).all()
	result = []
	for obj in db_objs:
		item = obj.__dict__.copy()
		item['skills'] = obj.skills.split(',') if obj.skills else []
		item['id'] = obj.id
		result.append(type('InternshipOutObj', (), item)())
	return result

# Get internship by phone
def get_internship_by_phone(db: Session, phone: str):
	objs = db.query(Internship).filter(Internship.phone == phone).all()
	result = []
	for obj in objs:
		item = obj.__dict__.copy()
		item['skills'] = obj.skills.split(',') if obj.skills else []
		item['id'] = obj.id
		result.append(type('InternshipOutObj', (), item)())
	return result

# Update internship by id
def update_internship(db: Session, internship_id: int, internship: InternshipCreate):
	db_internship = db.query(Internship).filter(Internship.id == internship_id).first()
	if not db_internship:
		return None
	db_internship.fullName = internship.fullName
	db_internship.dob = internship.dob
	db_internship.phone = internship.phone
	db_internship.email = internship.email
	db_internship.areaOfStudy = internship.areaOfStudy
	db_internship.institute = internship.institute
	db_internship.graduationYear = internship.graduationYear
	db_internship.areaOfInterest = internship.areaOfInterest
	db_internship.skillRating = internship.skillRating
	db_internship.resume = internship.resume
	db_internship.description = internship.description
	db_internship.skills = ','.join(internship.skills) if internship.skills else None
	db.commit()
	db.refresh(db_internship)
	# Convert skills string back to list for API response
	result = db_internship.__dict__.copy()
	result['skills'] = db_internship.skills.split(',') if db_internship.skills else []
	result['id'] = db_internship.id
	return type('InternshipOutObj', (), result)()

# Delete internship by id
def delete_internship(db: Session, internship_id: int):
	db_internship = db.query(Internship).filter(Internship.id == internship_id).first()
	if not db_internship:
		return False
	db.delete(db_internship)
	db.commit()
	return True
