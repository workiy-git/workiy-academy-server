
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
