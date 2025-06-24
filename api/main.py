from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("../models/logistic_model.pkl")

@app.get("/")
def read_root():
    return {"message": "Diabetes readmission model API"}

@app.post("/predict")
def predict(features: dict):
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return {"readmission_prediction": prediction}



'''
Run with bash command
uvicorn api.main:app --reload

'''
