from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.processor import clean_csv

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Data Processing API is running"}

@app.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...)):
    try:
        # Read file content
        content = await file.read()

        # Process file
        df = clean_csv(content)

        # Convert to JSON response
        result = df.to_dict(orient="records")

        return JSONResponse(content={
            "rows": len(result),
            "data": result
        })

    except Exception as e:
        return JSONResponse(content={
            "error": str(e)
        })
