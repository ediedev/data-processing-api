from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from io import StringIO

from app.processor import clean_csv

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Data Processing API is running"}

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):

    # Read uploaded file
    content = await file.read()

    # Process dataframe
    df = clean_csv(content)

    # Convert cleaned dataframe back to CSV
    output = StringIO()
    df.to_csv(output, index=False)

    output.seek(0)

    return StreamingResponse(
        output,
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=cleaned_data.csv"
        }
    )
