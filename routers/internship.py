# Update by phone
@router.put("/{phone}", response_model=internship_schema.InternshipApplicationOut)
def update_internship_by_phone(phone: str, internship: internship_schema.InternshipApplicationCreate, db: Session = Depends(get_db)):
    db_app = internship_crud.get_internship_application_by_phone(db, phone)
    if db_app is None:
        raise HTTPException(status_code=404, detail="Internship application not found")
    updated = internship_crud.update_internship_application(db, db_app.id, internship)
    if updated is None:
        raise HTTPException(status_code=404, detail="Internship application not found")
    return updated

# Delete by phone
@router.delete("/{phone}")
def delete_internship_by_phone(phone: str, db: Session = Depends(get_db)):
    db_app = internship_crud.get_internship_application_by_phone(db, phone)
    if db_app is None:
        raise HTTPException(status_code=404, detail="Internship application not found")
    result = internship_crud.delete_internship_application(db, db_app.id)
    if not result:
        raise HTTPException(status_code=404, detail="Internship application not found")
    return {"ok": True}
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import internship as internship_model
from schemas import internship as internship_schema
from crud import internship as internship_crud

router = APIRouter(
    prefix="/internship",
    tags=["internship"]
)

@router.post("/", response_model=internship_schema.InternshipApplicationOut)
def create_internship_application(internship: internship_schema.InternshipApplicationCreate, db: Session = Depends(get_db)):
    return internship_crud.create_internship_application(db, internship)

from typing import Optional

@router.get("/", response_model=List[internship_schema.InternshipApplicationOut])
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
