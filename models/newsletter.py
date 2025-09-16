
from sqlalchemy import Column, Integer, String
from database import Base

class Newsletter(Base):
	__tablename__ = "newsletter"
	id = Column(Integer, primary_key=True, index=True)
	email = Column(String(255), unique=True, index=True, nullable=False)
