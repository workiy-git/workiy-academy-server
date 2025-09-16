
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.course import CourseCreate, CourseOut
from database import get_db
from crud.course import (
    create_course_crud,
    get_courses_crud,
    get_course_crud,
    update_course_crud,
    delete_course_crud
)

router = APIRouter(tags=["courses"])

@router.post("", response_model=CourseOut)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = create_course_crud(course, db)
    return db_course

@router.get("", response_model=list[CourseOut])
def get_courses(db: Session = Depends(get_db)):
    return get_courses_crud(db)

@router.get("/{course_id}", response_model=CourseOut)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = get_course_crud(course_id, db)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=CourseOut)
def update_course(course_id: int, updated_course: CourseCreate, db: Session = Depends(get_db)):
    course = update_course_crud(course_id, updated_course, db)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    success = delete_course_crud(course_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Course not found")
    return {"message": "Course deleted successfully"}
