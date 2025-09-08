from sqlalchemy.orm import Session
from models.courseDetails import CourseDetails
from schemas.courseDetails import CourseDetailsCreate
import json

# CRUD Operations for CourseDetails
def create_course_details(db: Session, course: CourseDetailsCreate):
    db_course = CourseDetails(path=course.path, data=course.data)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_all_course_details(db: Session):
    courses = db.query(CourseDetails).all()
    return [
        {
            "id": course.id,
            "path": course.path,
            "data": course.data
        }
        for course in courses
    ]

def get_course_details(db: Session, path: str):
    course = db.query(CourseDetails).filter(CourseDetails.path == path).first()
    if not course:
        return None
    return {
        "id": course.id,
        "path": course.path,
        "data": course.data
    }

def update_course_details(db: Session, path: str, updated_details: CourseDetailsCreate):
    course = db.query(CourseDetails).filter(CourseDetails.path == path).first()
    if not course:
        return None
    course.data = updated_details.data
    db.commit()
    db.refresh(course)
    return {
        "id": course.id,
        "path": course.path,
        "data": json.loads(course.data)
    }

def delete_course_details(db: Session, path: str):
    course = db.query(CourseDetails).filter(CourseDetails.path == path).first()
    if not course:
        return False
    db.delete(course)
    db.commit()
    return True
