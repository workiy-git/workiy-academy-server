from sqlalchemy import Column, Integer, String, Text, JSON
from database import Base

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(150), nullable=False)
    description = Column(Text, nullable=False)
    duration = Column(String(50), nullable=False)
    image = Column(String(255), nullable=False)
    level = Column(String(50), nullable=False)
    path = Column(String(255), nullable=False)

class CourseDetails(Base):
    __tablename__ = "course_details"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String(255), unique=True, nullable=False)
    data = Column(JSON, nullable=False)
