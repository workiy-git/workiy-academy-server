from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import LONGTEXT
from pydantic import BaseModel
from typing import Any
import json

# ==================== CONFIGURATION ====================

# MySQL Database Connection
DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/academydb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI App
app = FastAPI()

# Allow React frontend (Vite default port: 5173)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==================== DATABASE MODELS ====================

# Courses Table (For Course Listings)
class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    duration = Column(String(50), nullable=False)
    image = Column(String(255), nullable=False)
    level = Column(String(50), nullable=False)
    path = Column(String(255), nullable=False, unique=True)

# Course Details Table (For Full Course Data)
class CourseDetails(Base):
    __tablename__ = "course_details"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String(255), unique=True, nullable=False)
    data = Column(LONGTEXT, nullable=False)  # Store JSON data

# Create database tables
Base.metadata.create_all(bind=engine)

# ==================== SCHEMAS ====================

# --- Course CRUD Schemas ---
class CourseBase(BaseModel):
    title: str
    description: str
    duration: str
    image: str
    level: str
    path: str

class CourseCreate(CourseBase):
    pass

class CourseUpdate(CourseBase):
    pass

class CourseOut(CourseBase):
    id: int
    class Config:
        from_attributes = True

# --- Course Details Schemas ---
class CourseDetailsBase(BaseModel):
    path: str
    data: Any  # Store full JSON here

class CourseDetailsCreate(CourseDetailsBase):
    pass

class CourseDetailsOut(CourseDetailsBase):
    id: int
    class Config:
        from_attributes = True

# ==================== ROUTES ====================

@app.get("/api/hello")
def hello():
    return {"message": "Welcome to Workiy Academy API! Use /docs for API documentation."}

# ----------- COURSE CRUD -----------

# CREATE a course
@app.post("/api/courses", response_model=CourseOut)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# GET all courses
@app.get("/api/courses", response_model=list[CourseOut])
def get_courses(db: Session = Depends(get_db)):
    return db.query(Course).all()

# GET single course by ID
@app.get("/api/courses/{course_id}", response_model=CourseOut)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

# UPDATE a course
@app.put("/api/courses/{course_id}", response_model=CourseOut)
def update_course(course_id: int, updated_course: CourseUpdate, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    for key, value in updated_course.dict().items():
        setattr(course, key, value)
    db.commit()
    db.refresh(course)
    return course

# DELETE a course
@app.delete("/api/courses/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    db.delete(course)
    db.commit()
    return {"message": "Course deleted successfully"}

# ----------- COURSE DETAILS -----------

# CREATE full course details
@app.post("/api/course-details", response_model=CourseDetailsOut)
def create_course_details(course: CourseDetailsCreate, db: Session = Depends(get_db)):
    db_course = CourseDetails(path=course.path, data=json.dumps(course.data))
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# GET all course details
@app.get("/api/course-details", response_model=list[CourseDetailsOut])
def get_all_course_details(db: Session = Depends(get_db)):
    courses = db.query(CourseDetails).all()
    return [
        {
            "id": course.id,
            "path": course.path,
            "data": json.loads(course.data)  # Convert JSON string back to dict
        }
        for course in courses
    ]


# GET full course details by path
@app.get("/api/course-details/{path}", response_model=CourseDetailsOut)
def get_course_details(path: str, db: Session = Depends(get_db)):
    course = db.query(CourseDetails).filter(CourseDetails.path == path).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course details not found")
    return {
        "id": course.id,
        "path": course.path,
        "data": json.loads(course.data)
    }
# UPDATE course details by path
@app.put("/api/course-details/{path}", response_model=CourseDetailsOut)
def update_course_details(path: str, updated_details: CourseDetailsCreate, db: Session = Depends(get_db)):
    course = db.query(CourseDetails).filter(CourseDetails.path == path).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course details not found")
    course.data = json.dumps(updated_details.data)
    db.commit()
    db.refresh(course)
    return {
        "id": course.id,
        "path": course.path,
        "data": json.loads(course.data)
    }

@app.get("/")
def root():
    return {"message": "Welcome to Workiy Academy API! Use /docs for API documentation."}
