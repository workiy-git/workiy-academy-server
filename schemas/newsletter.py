
from pydantic import BaseModel, EmailStr

class NewsletterCreate(BaseModel):
	email: EmailStr

class NewsletterUpdate(BaseModel):
	email: EmailStr

class NewsletterOut(BaseModel):
	id: int
	email: EmailStr

	class Config:
		orm_mode = True
