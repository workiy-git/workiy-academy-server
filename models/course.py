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
    rating = Column(Integer, nullable=False)
    lessons = Column(String(10), nullable=False)
    path = Column(String(255), nullable=False)


