# models.py
from sqlalchemy import Column, Integer, String, DateTime
from database import Base

class FormSubmission(Base):
    __tablename__ = "form_submissions"

    id = Column(Integer, primary_key=True, index=True)
    submitted_at = Column(DateTime)
    # ... other columns
