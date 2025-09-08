from pydantic import BaseModel
from typing import Any

class CourseBase(BaseModel):
    title: str
    description: str
    duration: str
    image: str
    level: str
    path: str

class CourseCreate(CourseBase):
    pass

class CourseOut(CourseBase):
    id: int
    class Config:
        from_attributes = True

class CourseDetailsBase(BaseModel):
    path: str
    data: Any

class CourseDetailsCreate(CourseDetailsBase):
    pass

class CourseDetailsOut(CourseDetailsBase):
    id: int
    class Config:
        orm_mode = True
