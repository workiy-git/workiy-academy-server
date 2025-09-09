from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.enquiry import EnquiryCreate
from crud.enquiry import create_enquiry
from database import get_db
from models.enquiry import Enquiry
from typing import List

router = APIRouter()
@router.post("/enquiry", response_model=EnquiryCreate)
def submit_enquiry(enquiry: EnquiryCreate, db: Session = Depends(get_db)):
    db_enquiry = create_enquiry(db, enquiry)
    return db_enquiry
# GET method to retrieve all enquiries
@router.get("/enquiry", response_model=List[EnquiryCreate])
def get_enquiries(db: Session = Depends(get_db)):
    return db.query(Enquiry).all()
# GET method to retrieve enquiry by phone number
@router.get("/enquiry/by-phone/{phone}", response_model=EnquiryCreate)
def get_enquiry_by_phone(phone: str, db: Session = Depends(get_db)):
    db_enquiry = db.query(Enquiry).filter(Enquiry.phone == phone).first()
    if not db_enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    return db_enquiry
# Update enquiry by phone number
@router.put("/enquiry/by-phone/{phone}", response_model=EnquiryCreate)
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
@router.delete("/enquiry/by-phone/{phone}", response_model=dict)
def delete_enquiry_by_phone(phone: str, db: Session = Depends(get_db)):
    db_enquiry = db.query(Enquiry).filter(Enquiry.phone == phone).first()
    if not db_enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    db.delete(db_enquiry)
    db.commit()
    return {"detail": "Enquiry deleted"}