from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.internship import InternshipCreate, InternshipOut
from crud import internship as crud_internship
from typing import List
from utils.email_utils import send_email, send_email_admin
from datetime import datetime

router = APIRouter()

# POST: Create internship
@router.post("/", response_model=InternshipOut)
def create_internship(internship: InternshipCreate, db: Session = Depends(get_db)):
    adminsubject = "New Internship Submission - Workiy Academy"
    adminmessage = (
        "Hello Admin,\n\n"
        "A new internship application has been submitted at Workiy Academy.\n\n"
        f"Applicant Email: {internship.email}\n"
        f"Applicant Name: {internship.fullName}\n"
        f"Submission Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        "Thank you for reviewing and supporting our internship program!\n\n"
        "– Workiy Academy System"
    )

    send_email_admin(adminsubject, adminmessage)
    
    usersubject = "Workiy Academy - Internship Application Received"
    usermessage = (
        f"Hello {internship.fullName},\n\n"
        "Thank you for submitting your internship application to Workiy Academy! "
        "Our team will review your details and get back to you shortly with the next steps.\n\n"
        "Best regards,\n"
        "The Workiy Academy Team"
    )
    send_email(internship.email, usersubject, usermessage)
    
    return crud_internship.create_internship(db, internship)


# GET: List internships
@router.get("/", response_model=List[InternshipOut])
def read_internships(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	return crud_internship.get_internships(db, skip=skip, limit=limit)


# GET: Get internships by phone (returns a list)
from typing import List
@router.get("/{phone}", response_model=List[InternshipOut])
def read_internship_by_phone(phone: str, db: Session = Depends(get_db)):
	db_internships = crud_internship.get_internship_by_phone(db, phone)
	if not db_internships:
		raise HTTPException(status_code=404, detail="No internships found for this phone")
	return db_internships

# PUT: Update internship by ID
@router.put("/{internship_id}", response_model=InternshipOut)
def update_internship(internship_id: int, internship: InternshipCreate, db: Session = Depends(get_db)):
	db_internship = crud_internship.update_internship(db, internship_id, internship)
	if db_internship is None:
		raise HTTPException(status_code=404, detail="Internship not found")
	return db_internship

# DELETE: Delete internship by ID
@router.delete("/{internship_id}", response_model=dict)
def delete_internship(internship_id: int, db: Session = Depends(get_db)):
	result = crud_internship.delete_internship(db, internship_id)
	if not result:
		raise HTTPException(status_code=404, detail="Internship not found")
	return {"ok": True}
