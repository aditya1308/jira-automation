from fastapi import FastAPI, UploadFile, File
import pandas as pd
import openai
import io

app = FastAPI()


@app.post("/process-files")
async def process_files(
    md_file: UploadFile = File(...),
    excel_file: UploadFile = File(...)
):

    # Read markdown prompt
    md_content = await md_file.read()
    prompt = md_content.decode("utf-8").replace("\r\n", "\n")

    # Read excel file
    excel_bytes = await excel_file.read()
    df = pd.read_excel(io.BytesIO(excel_bytes))

    # Convert excel to text
    excel_data =excel_data = df.to_json(orient="records")

    final_prompt = f"""
{prompt}

Here is the data from the excel file:

{excel_data}
"""

    return {
        "md_file": prompt,
        "excel_file": excel_data
    }