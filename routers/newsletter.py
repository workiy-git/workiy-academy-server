from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.newsletter import Newsletter
from schemas.newsletter import NewsletterCreate, NewsletterUpdate, NewsletterOut

router = APIRouter(tags=["Newsletter"])

@router.post("", response_model=NewsletterOut)
def create_newsletter(newsletter: NewsletterCreate, db: Session = Depends(get_db)):
    db_newsletter = Newsletter(email=newsletter.email)
    db.add(db_newsletter)
    try:
        db.commit()
        db.refresh(db_newsletter)
    except Exception:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists.")
    return db_newsletter

@router.get("", response_model=list[NewsletterOut])
def get_newsletters(db: Session = Depends(get_db)):
    return db.query(Newsletter).all()

@router.put("/{newsletter_id}", response_model=NewsletterOut)
def update_newsletter(newsletter_id: int, newsletter: NewsletterUpdate, db: Session = Depends(get_db)):
    db_newsletter = db.query(Newsletter).filter(Newsletter.id == newsletter_id).first()
    if not db_newsletter:
        raise HTTPException(status_code=404, detail="Newsletter not found")
    db_newsletter.email = newsletter.email
    db.commit()
    db.refresh(db_newsletter)
    return db_newsletter

@router.delete("/{newsletter_id}")
def delete_newsletter(newsletter_id: int, db: Session = Depends(get_db)):
    db_newsletter = db.query(Newsletter).filter(Newsletter.id == newsletter_id).first()
    if not db_newsletter:
        raise HTTPException(status_code=404, detail="Newsletter not found")
    db.delete(db_newsletter)
    db.commit()
    return {"detail": "Deleted"}
