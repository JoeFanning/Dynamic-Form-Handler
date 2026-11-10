import os
from typing import List, Optional
from fastapi import FastAPI, File, Form, Request, UploadFile, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()

# Create a folder for temporary file storage before database/cloud upload
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/submit-form")
async def handle_form(request: Request):
    try:
        # 1. Capture all dynamic text/input fields from the incoming form submission
        form_data = await request.form()
        form_dict = {key: value for key, value in form_data.items() if not isinstance(value, UploadFile)}
        
        # 2. Capture any uploaded files
        saved_file_paths = []
        for key, value in form_data.items():
            if isinstance(value, UploadFile):
                file: UploadFile = value
                if file.filename:
                    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                    contents = await file.read()
                    with open(file_path, "wb") as f:
                        f.write(contents)
                    saved_file_paths.append(file_path)

        # TODO: Save `form_dict` and `saved_file_paths` into your PostgreSQL database here!

        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": "Form data and files processed successfully!",
                "data_received": form_dict,
                "files_saved": saved_file_paths
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
