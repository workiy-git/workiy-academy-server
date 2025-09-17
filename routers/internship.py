
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from database import get_db
from models import internship as internship_model
from schemas import internship as internship_schema
from crud import internship as internship_crud
from utils.email_utils import send_email, send_email_admin
from datetime import datetime

router = APIRouter()
@router.put("/by-phone/{phone}", response_model=internship_schema.InternshipApplicationOut)
def update_internship_by_phone(phone: str, internship: internship_schema.InternshipApplicationCreate, db: Session = Depends(get_db)):
    db_app = internship_crud.get_internship_application_by_phone(db, phone)
    if db_app is None:
        raise HTTPException(status_code=404, detail="Internship application not found")
    updated = internship_crud.update_internship_application(db, db_app.id, internship)
    if updated is None:
        raise HTTPException(status_code=404, detail="Internship application not found")
    return updated

@router.delete("/by-phone/{phone}")
def delete_internship_by_phone(phone: str, db: Session = Depends(get_db)):
    db_app = internship_crud.get_internship_application_by_phone(db, phone)
    if db_app is None:
        raise HTTPException(status_code=404, detail="Internship application not found")
    result = internship_crud.delete_internship_application(db, db_app.id)
    if not result:
        raise HTTPException(status_code=404, detail="Internship application not found")
    return {"ok": True}

@router.post("", response_model=internship_schema.InternshipApplicationOut)
def create_internship_application(internship: internship_schema.InternshipApplicationCreate, db: Session = Depends(get_db)):
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
    return internship_crud.create_internship_application(db, internship)

from typing import Optional

@router.get("", response_model=List[internship_schema.InternshipApplicationOut])
def read_internship_applications(
    skip: int = 0,
    limit: int = 100,
    phone: Optional[str] = None,
    db: Session = Depends(get_db)
):
    if phone:
        app = internship_crud.get_internship_application_by_phone(db, phone)
        if app is None:
            raise HTTPException(status_code=404, detail="Internship application not found")
        return [app]
    return internship_crud.get_internship_applications(db, skip=skip, limit=limit)

@router.get("/{application_id}", response_model=internship_schema.InternshipApplicationOut)
def read_internship_application(application_id: int, db: Session = Depends(get_db)):
    db_app = internship_crud.get_internship_application(db, application_id=application_id)
    if db_app is None:
        raise HTTPException(status_code=404, detail="Internship application not found")
    return db_app

@router.put("/{application_id}", response_model=internship_schema.InternshipApplicationOut)
def update_internship_application(application_id: int, internship: internship_schema.InternshipApplicationCreate, db: Session = Depends(get_db)):
    db_app = internship_crud.update_internship_application(db, application_id, internship)
    if db_app is None:
        raise HTTPException(status_code=404, detail="Internship application not found")
    return db_app

@router.delete("/{application_id}")
def delete_internship_application(application_id: int, db: Session = Depends(get_db)):
    result = internship_crud.delete_internship_application(db, application_id)
    if not result:
        raise HTTPException(status_code=404, detail="Internship application not found")
    return {"ok": True}
