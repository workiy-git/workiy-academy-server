from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.enquiry import EnquiryCreate, EnquiryOut
from crud.enquiry import create_enquiry
from database import get_db
from models.enquiry import Enquiry
from typing import List

router = APIRouter(
    prefix="/api/enquiry",
    tags=["enquiry"]
)

# Create enquiry
@router.post("", response_model=EnquiryOut)
def submit_enquiry(enquiry: EnquiryCreate, db: Session = Depends(get_db)):
    db_enquiry = create_enquiry(db, enquiry)
    return db_enquiry

# Get all enquiries
@router.get("", response_model=List[EnquiryOut])
def get_enquiries(db: Session = Depends(get_db)):
    return db.query(Enquiry).all()

# Get enquiry by phone number
@router.get("/by-phone/{phone}", response_model=EnquiryOut)
def get_enquiry_by_phone(phone: str, db: Session = Depends(get_db)):
    db_enquiry = db.query(Enquiry).filter(Enquiry.phone == phone).first()
    if not db_enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    return db_enquiry

# Update enquiry by phone number
@router.put("/by-phone/{phone}", response_model=EnquiryOut)
def update_enquiry_by_phone(phone: str, enquiry: EnquiryCreate, db: Session = Depends(get_db)):
    db_enquiry = db.query(Enquiry).filter(Enquiry.phone == phone).first()
    if not db_enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    db_enquiry.firstName = enquiry.firstName
    db_enquiry.lastName = enquiry.lastName
    db_enquiry.email = enquiry.email
    db_enquiry.phone = enquiry.phone
    db_enquiry.message = enquiry.message
    db.commit()
    db.refresh(db_enquiry)
    return db_enquiry

# Delete enquiry by phone number
@router.delete("/by-phone/{phone}", response_model=dict)
def delete_enquiry_by_phone(phone: str, db: Session = Depends(get_db)):
    db_enquiry = db.query(Enquiry).filter(Enquiry.phone == phone).first()
    if not db_enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    db.delete(db_enquiry)
    db.commit()
    return {"detail": "Enquiry deleted"}