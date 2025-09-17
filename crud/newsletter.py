
from sqlalchemy.orm import Session
from models.newsletter import Newsletter
from schemas.newsletter import NewsletterCreate, NewsletterUpdate

def create_newsletter(db: Session, newsletter: NewsletterCreate):
	db_newsletter = Newsletter(email=newsletter.email)
	db.add(db_newsletter)
	try:
		db.commit()
		db.refresh(db_newsletter)
	except Exception:
		db.rollback()
		return None
	return db_newsletter

def get_newsletters(db: Session):
	return db.query(Newsletter).all()

def update_newsletter(db: Session, newsletter_id: int, newsletter: NewsletterUpdate):
	db_newsletter = db.query(Newsletter).filter(Newsletter.id == newsletter_id).first()
	if not db_newsletter:
		return None
	db_newsletter.email = newsletter.email
	db.commit()
	db.refresh(db_newsletter)
	return db_newsletter

def delete_newsletter(db: Session, newsletter_id: int):
	db_newsletter = db.query(Newsletter).filter(Newsletter.id == newsletter_id).first()
	if not db_newsletter:
		return False
	db.delete(db_newsletter)
	db.commit()
	return True
