from pydantic import BaseModel
from typing import Any

class CourseBase(BaseModel):
    title: str
    description: str
    duration: str
    image: str
    level: str
    rating: int
    lessons: str
    path: str

class CourseCreate(CourseBase):
    pass

class CourseOut(CourseBase):
    id: int
    class Config:
        from_attributes = True

