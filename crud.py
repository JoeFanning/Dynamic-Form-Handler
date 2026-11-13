import pandas as pd
from sqlalchemy.orm import Session
from models import FormSubmission

def get_all_submissions(db: Session):
    return db.query(FormSubmission).all()

# Fetch data and convert model instances to dictionaries
submissions = get_all_submissions(db)
data = [{
    "id": s.id,
    "name": s.name,
    "email": s.email,
    "message": s.message,
    "submitted_at": s.submitted_at
} for s in submissions]

df = pd.DataFrame(data)
print(df) # Or display(df) in a Jupyter notebook
