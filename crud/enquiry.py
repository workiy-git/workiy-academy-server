
from models.enquiry import Enquiry  # Assuming you have an Enquiry SQLAlchemy model
from schemas.enquiry import EnquiryCreate
from sqlalchemy.orm import Session

def create_enquiry(db: Session, enquiry: EnquiryCreate):
	db_enquiry = Enquiry(
		firstName=enquiry.firstName,
		lastName=enquiry.lastName,
		email=enquiry.email,
		phone=enquiry.phone,
		message=enquiry.message
	)
	db.add(db_enquiry)
	db.commit()
	db.refresh(db_enquiry)
	return db_enquiry

def get_enquiry(db: Session, phone: str):
	return db.query(Enquiry).filter(Enquiry.phone == phone).all()

def get_enquiries(db: Session, skip: int = 0, limit: int = 100):
	return db.query(Enquiry).offset(skip).limit(limit).all()

def update_enquiry(db: Session, enquiry_id: int, enquiry_data: EnquiryCreate):
	enquiry = db.query(Enquiry).filter(Enquiry.id == enquiry_id).first()
	if enquiry:
		enquiry.firstName = enquiry_data.firstName
		enquiry.lastName = enquiry_data.lastName
		enquiry.email = enquiry_data.email
		enquiry.phone = enquiry_data.phone
		enquiry.message = enquiry_data.message
		db.commit()
		db.refresh(enquiry)
	return enquiry

def delete_enquiry(db: Session, enquiry_id: int):
	enquiry = db.query(Enquiry).filter(Enquiry.id == enquiry_id).first()
	if enquiry:
		db.delete(enquiry)
		db.commit()
	return enquiry
