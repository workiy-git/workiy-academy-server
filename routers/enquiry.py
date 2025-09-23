from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.enquiry import EnquiryCreate, EnquiryOut
from crud.enquiry import create_enquiry
from database import get_db
from models.enquiry import Enquiry
from typing import List
from utils.email_utils import send_email, send_email_admin
from datetime import datetime

router = APIRouter()

# Create enquiry
@router.post("", response_model=EnquiryOut)
def submit_enquiry(enquiry: EnquiryCreate, db: Session = Depends(get_db)):
    db_enquiry = create_enquiry(db, enquiry)
    adminsubject = "New Student Enrolled in a Course - Workiy Academy"
    adminmessage = (
                "Hello Admin,\n\n"
                "A new student has joined a course at Workiy Academy.\n\n"
                f"Student Email: {enquiry.email}\n"
                f"Student Name: {enquiry.firstName} {enquiry.lastName}\n"
                f"Enrollment Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                "Thank you for supporting our learning community!\n\n"
                "– Workiy Academy System"
            )

    send_email_admin(adminsubject, adminmessage)
    
    usersubject = "Workiy Academy - Enquiry Received"
    usermessage = (
                f"Hello {enquiry.firstName},\n\n"
                "Thank you for reaching out to Workiy Academy! We have received your enquiry and will get back to you shortly.\n\n"
                "Best regards,\n"
                "The Workiy Academy Team"
            )
    send_email(enquiry.email, usersubject, usermessage)
    
    return db_enquiry


# Get all enquiries
@router.get("", response_model=List[EnquiryOut])
def get_enquiries(db: Session = Depends(get_db)):
    from crud.enquiry import get_enquiries
    return get_enquiries(db)


# Get all enquiries by phone
@router.get("/{phone}", response_model=List[EnquiryOut])
def get_enquiry(phone: str, db: Session = Depends(get_db)):
    from crud.enquiry import get_enquiry
    db_enquiries = get_enquiry(db, phone)
    if not db_enquiries:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    return [EnquiryOut.from_orm(e) for e in db_enquiries]


# Update enquiry by id 
@router.put("/{enquiry_id}", response_model=EnquiryOut)
def update_enquiry(enquiry_id: int, enquiry: EnquiryCreate, db: Session = Depends(get_db)):
    from crud.enquiry import update_enquiry
    db_enquiry = update_enquiry(db, enquiry_id, enquiry)
    if not db_enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    return db_enquiry


# Delete enquiry by id
@router.delete("/{enquiry_id}", response_model=dict)
def delete_enquiry(enquiry_id: int, db: Session = Depends(get_db)):
    from crud.enquiry import delete_enquiry
    db_enquiry = delete_enquiry(db, enquiry_id)
    if not db_enquiry:
        raise HTTPException(status_code=404, detail="Enquiry not found")
    return {"detail": "Enquiry deleted"}