import os
import json
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, Text, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# --- DATABASE SETUP ---
# Render provides DATABASE_URL automatically when you link a database service
DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    # SQLAlchemy requires 'postgresql://' instead of legacy 'postgres://'
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Fallback to local SQLite if no environment variable is found (great for local testing)
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./bouwbuild.db"

# Create database engine
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the database table for incoming form submissions
class FormSubmission(Base):
    __tablename__ = "form_submissions"

    id = Column(Integer, primary_key=True, index=True)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    payload = Column(Text, nullable=False)          # Stores form fields as a JSON string
    saved_files = Column(String, nullable=True)     # Comma-separated list of uploaded file names

# Create tables automatically on startup
Base.metadata.create_all(bind=engine)

# --- FASTAPI APP ---
app = FastAPI(title="Bouwbuild Form Handler & CRM Backend")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production if needed (e.g., ["https://www.bouwbuild.eu"])
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create local folder for uploaded files if it doesn't exist
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Bouwbuild Form Handler API with PostgreSQL is live!"}

@app.post("/submit")
async def handle_form(request: Request):
    db = SessionLocal()
    try:
        content_type = request.headers.get("content-type", "")
        parsed_data = {}
        saved_files = []

        print(f"\n--- INCOMING CONTENT-TYPE: {content_type} ---")

        if "application/json" in content_type:
            json_data = await request.json()
            print(f"[JSON Payload]: {json_data}")
            parsed_data = json_data
        else:
            form_data = await request.form()
            for key, value in form_data.multi_items():
                if hasattr(value, "filename") and value.filename:
                    file_path = os.path.join(UPLOAD_DIR, value.filename)
                    contents = await value.read()
                    with open(file_path, "wb") as f:
                        f.write(contents)
                    saved_files.append(value.filename)
                    print(f"[Saved File]: {key} -> {value.filename}")
                else:
                    print(f"[Field]: {key} -> {value}")
                    parsed_data[key] = value

        # Save submission to PostgreSQL database
        db_submission = FormSubmission(
            payload=json.dumps(parsed_data),
            saved_files=", ".join(saved_files) if saved_files else None
        )
        db.add(db_submission)
        db.commit()
        db.refresh(db_submission)

        print(f"[Database]: Saved submission ID {db_submission.id}")

        return {
            "status": "success",
            "message": "Form data processed and saved to database successfully!",
            "submission_id": db_submission.id,
            "received_fields": parsed_data,
            "saved_files": saved_files,
        }
    except Exception as e:
        db.rollback()
        print(f"[ERROR]: {str(e)}")
        raise HTTPException(status_code=422, detail=str(e))
    finally:
        db.close()
