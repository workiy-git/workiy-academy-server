
from sqlalchemy.orm import Session
from models.course import Course
from schemas.course import CourseCreate

def create_course_crud(course: CourseCreate, db: Session):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_courses_crud(db: Session):
    return db.query(Course).all()

def get_course_crud(course_id: int, db: Session):
    course = db.query(Course).filter(Course.id == course_id).first()
    return course

def update_course_crud(course_id: int, updated_course: CourseCreate, db: Session):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        return None
    for key, value in updated_course.dict().items():
        setattr(course, key, value)
    db.commit()
    db.refresh(course)
    return course

def delete_course_crud(course_id: int, db: Session):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        return False
    db.delete(course)
    db.commit()
    return True
