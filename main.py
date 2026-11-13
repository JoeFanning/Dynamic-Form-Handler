# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud

app = FastAPI()

@app.get("/api/submissions")
def read_submissions(db: Session = Depends(get_db)):
    try:
        submissions = crud.get_all_submissions(db)
        
        results = []
        for sub in submissions:
            results.append({
                "id": sub.id,
                "submitted_at": str(sub.submitted_at),
                # ... parse remaining fields
            })
        return results
        
    except Exception as e:
        print(f"[ERROR]: {str(e)}")
        raise HTTPException(status_code=422, detail=str(e))
