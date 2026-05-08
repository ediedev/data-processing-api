from fastapi import FastAPI, UploadFile, File, Query
from fastapi.responses import JSONResponse, StreamingResponse
from io import StringIO

from app.processor import clean_csv

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Data Processing API is running"}

@app.post("/upload-csv")
async def upload_csv(
    file: UploadFile = File(...),
    output_format: str = Query("json")
):

    # Read uploaded file
    content = await file.read()

    # Process dataframe
    df = clean_csv(content)

    # JSON response
    if output_format == "json":

        result = df.to_dict(orient="records")

        return JSONResponse(content={
            "rows": len(result),
            "data": result
        })

    # Download CSV
    elif output_format == "csv":

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

    # Invalid format
    return JSONResponse(
        status_code=400,
        content={
            "error":
            "Invalid output_format. Use 'json' or 'csv'"
        }
    )
