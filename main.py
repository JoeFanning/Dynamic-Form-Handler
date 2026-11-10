import os
from fastapi import FastAPI, File, Form, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

app = FastAPI(title="Dynamic Form Handler")

# Add CORS middleware right after initializing 'app'
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specifically ["https://joefanning.github.io", "https://www.bouwbuild.eu"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a folder to store uploaded files if it doesn't already exist
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def read_root():
    return {"message": "Dynamic Form Handler is live and ready!"}


@app.post("/submit")
async def handle_form(
    request: Request,
    files: Optional[List[UploadFile]] = File(None),
):
    # 1. Capture all form fields / text data dynamically
    form_data = await request.form()
    parsed_data = {}

    print("\n--- INCOMING FORM SUBMISSION ---")

    for key, value in form_data.multi_items():
        # If the item is an uploaded file sent via standard form data, handle its metadata
        if hasattr(value, "filename") and value.filename:
            print(f"[Field - File]: {key} -> filename: {value.filename}")
        else:
            print(f"[Field - Text]: {key} -> {value}")
            parsed_data[key] = value

    # 2. Save any explicitly uploaded files
    saved_files = []
    if files:
        for file in files:
            if file.filename:
                file_path = os.path.join(UPLOAD_DIR, file.filename)
                contents = await file.read()
                with open(file_path, "wb") as f:
                    f.write(contents)
                saved_files.append(file.filename)
                print(f"[Saved File Successfully]: {file.filename} -> to {file_path}")

    print("---------------------------------\n")

    return {
        "status": "success",
        "message": "Form data processed and logged successfully!",
        "received_fields": parsed_data,
        "saved_files": saved_files,
    }
