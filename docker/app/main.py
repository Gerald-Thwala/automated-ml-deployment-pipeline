# docker/app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .utils import predict_sequence

app = FastAPI(title="DNA Sequence Classifier")

class SequenceInput(BaseModel):
    sequence: str

@app.get("/")
def root():
    return {"message": "DNA Classifier API is running"}

@app.post("/predict")
def predict(input_data: SequenceInput):
    sequence = input_data.sequence.upper()
    if not all(c in "ACGT" for c in sequence):
        raise HTTPException(status_code=400, detail="Invalid characters in DNA sequence. Only A, C, G, T allowed.")
    
    try:
        result = predict_sequence(sequence)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
