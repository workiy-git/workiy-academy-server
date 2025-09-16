
from sqlalchemy import Column, Integer, String
from database import Base

class Enquiry(Base):
	__tablename__ = "enquiries"

	id = Column(Integer, primary_key=True, index=True)
	firstName = Column(String(255), nullable=False)
	lastName = Column(String(255), nullable=False)
	email = Column(String(255), nullable=False, index=True)
	phone = Column(String(20), nullable=False)
	message = Column(String(1000), nullable=False)
