from pydantic import BaseModel, EmailStr

class EnquiryCreate(BaseModel):
	firstName: str
	lastName: str
	email: EmailStr
	phone: str
	message: str

class EnquiryOut(EnquiryCreate):
	id: int

	class Config:
		orm_mode = True