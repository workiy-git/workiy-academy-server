from pydantic import BaseModel
from typing import Any

class CourseDetailsBase(BaseModel):
    path: str
    data: Any

class CourseDetailsCreate(CourseDetailsBase):
    pass

class CourseDetailsOut(CourseDetailsBase):
    id: int
    class Config:
        orm_mode = True
