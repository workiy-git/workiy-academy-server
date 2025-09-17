from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from crud.courseDetails import (
    create_course_details as crud_create,
    get_all_course_details as crud_get_all,
    get_course_details as crud_get_one,
    update_course_details as crud_update,
    delete_course_details as crud_delete
)
from schemas.courseDetails import CourseDetailsCreate, CourseDetailsOut
from database import get_db

router = APIRouter()

@router.post("", response_model=CourseDetailsOut)
def create(course: CourseDetailsCreate, db: Session = Depends(get_db)):
    return crud_create(db, course)

@router.get("", response_model=List[CourseDetailsOut])
def get_all(db: Session = Depends(get_db)):
    return crud_get_all(db)

@router.get("/{path}", response_model=CourseDetailsOut)
def get_one(path: str, db: Session = Depends(get_db)):
    course = crud_get_one(db, path)
    if not course:
        raise HTTPException(status_code=404, detail="Course details not found")
    return course

@router.put("/{path}", response_model=CourseDetailsOut)
def update(path: str, updated_details: CourseDetailsCreate, db: Session = Depends(get_db)):
    course = crud_update(db, path, updated_details)
    if not course:
        raise HTTPException(status_code=404, detail="Course details not found")
    return course

@router.delete("/{path}")
def delete(path: str, db: Session = Depends(get_db)):
    success = crud_delete(db, path)
    if not success:
        raise HTTPException(status_code=404, detail="Course details not found")
    return {"detail": "Deleted successfully"}
