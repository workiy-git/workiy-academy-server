from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas.newsletter import NewsletterCreate, NewsletterUpdate, NewsletterOut
from crud.newsletter import create_newsletter, get_newsletters, update_newsletter, delete_newsletter
from utils.email_utils import send_email, send_email_admin
from datetime import datetime

router = APIRouter()

@router.post("", response_model=NewsletterOut)
def create_newsletter_route(newsletter: NewsletterCreate, db: Session = Depends(get_db)):
    db_newsletter = create_newsletter(db, newsletter)
    adminsubject = "New Newsletter Subscriber Alert - Workiy Academy"
    adminmessage = (
        "Hello Admin,\n\n"
        "A new user has subscribed to the Workiy Academy newsletter.\n\n"
        f"Subscriber Email: {newsletter.email}\n"
        f"Subscription Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        "Thank you for helping our community grow!\n\n"
        "– Workiy Academy System"
    )

    send_email_admin(adminsubject, adminmessage)
    
    usersubject = "Workiy Academy - Important Notification"
    usermessage = (
            "Hello,\n\n"
            "We’re excited to bring you the latest news from Workiy Academy.\n"
            "Discover new resources, tips, and updates designed to support your growth and learning journey.\n\n"
            "Thank you for staying connected with our community!\n\n"
            "– The Workiy Academy Team"
        )
    send_email(newsletter.email, usersubject, usermessage)
    
    if not db_newsletter:
        raise HTTPException(status_code=400, detail="Email already exists.")
    return db_newsletter

@router.get("", response_model=list[NewsletterOut])
def get_newsletters_route(db: Session = Depends(get_db)):
    return get_newsletters(db)

@router.put("/{newsletter_id}", response_model=NewsletterOut)
def update_newsletter_route(newsletter_id: int, newsletter: NewsletterUpdate, db: Session = Depends(get_db)):
    db_newsletter = update_newsletter(db, newsletter_id, newsletter)
    if not db_newsletter:
        raise HTTPException(status_code=404, detail="Newsletter not found")
    return db_newsletter

@router.delete("/{newsletter_id}")
def delete_newsletter_route(newsletter_id: int, db: Session = Depends(get_db)):
    success = delete_newsletter(db, newsletter_id)
    if not success:
        raise HTTPException(status_code=404, detail="Newsletter not found")
    return {"detail": "Deleted"}
