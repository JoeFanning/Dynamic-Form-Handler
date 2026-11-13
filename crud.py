from sqlalchemy.orm import Session
from models import FormSubmission

def get_all_submissions(db: Session):
    return db.query(FormSubmission).all()
