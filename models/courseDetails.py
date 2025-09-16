from sqlalchemy import Column, Integer, String, Text, JSON
from database import Base


class CourseDetails(Base):
    __tablename__ = "course_details"
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String(255), unique=True, nullable=False)
    data = Column(JSON, nullable=False)
