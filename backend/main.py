
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from utils import analyze_with_gpt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    df = pd.read_excel(file.file) if file.filename.endswith(".xlsx") else pd.read_csv(file.file)
    result = analyze_with_gpt(df)
    return {"analysis": result}
