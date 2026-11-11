import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException

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
async def handle_form(request: Request):
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

        return {
            "status": "success",
            "message": "Form data processed successfully!",
            "received_fields": parsed_data,
            "saved_files": saved_files,
        }
    except Exception as e:
        print(f"[ERROR]: {str(e)}")
        # This will return the exact Python exception back to your browser console
        raise HTTPException(status_code=422, detail=str(e))
