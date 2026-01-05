from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import Query
from pydantic import BaseModel
import pickle
import numpy as np
import joblib
import pandas as pd
'''
To start app 
uvicorn api:app --reload  # run this inside of backend folder
uvicorn backend.api:app --reload # run this outside of backend folder
Test endpoints with this url http://localhost:8000/docs

age needs to be one of the following values for testing, have them in quotes
[10-20)
[20-30)
[30-40)
[40-50)
[50-60)
[70-80)
[80-90)



input example 

{
  "model": "logistic"
  "age": "[30-40)",
  "gender": "male",
  "admission_type_id": 0,
  "discharge_disposition_id": 0,
  "admission_source_id": 0,
  "num_procedures": 0,
  "num_medications": 0,
  "time_in_hospital": "0",
  "num_lab_procedures": 0,
  "number_inpatient": 0,
  "number_emergency": 0,
  "number_outpatient": 0,
  "number_diagnoses": 0
}

'''
app = FastAPI()


# Be sure the following features are all fed into model with appropiate choices
# show featues
# [('num', StandardScaler(), ['time_in_hospital', 'num_lab_procedures', 'num_procedures', 
# 'num_medications', 'number_inpatient', 'number_emergency', 'number_outpatient', 'number_diagnoses']), ('cat', OneHotEncoder(handle_unknown='ignore'), ['age', 'gender', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id'])]
# INFO:     Started server process [6240]

#model = joblib.load("backend/models/logistic_model.pkl")  # run this outside of backend folder
log_model = joblib.load("models/logistic_model.pkl") # run this inside of backend folder
rf_model = joblib.load("models/random_forest_model.pkl") 

# print('SHOWING TYPE MODEL')
# print(type(model))
# print('show featues')
# print(model.named_steps['preprocessor'].transformers)


df = joblib.load("data/predicted_prob_distribution.pkl")

class InputData(BaseModel):
    model: str
    # age: str
    age : int
    gender : str
    admission_type_id : int 
    discharge_disposition_id : int 
    admission_source_id : int
    num_procedures: int
    num_medications: int
    time_in_hospital: str
    num_lab_procedures : int 
    number_inpatient : int
    number_emergency : int 
    number_outpatient : int
    number_diagnoses : int 

def age_to_bucket(age: int) -> str:
    if age < 10:
        return "[0-10)"
    elif age < 20:
        return "[10-20)"
    elif age < 30:
        return "[20-30)"
    elif age < 40:
        return "[30-40)"
    elif age < 50:
        return "[40-50)"
    elif age < 60:
        return "[50-60)"
    elif age < 70:
        return "[60-70)"
    elif age < 80:
        return "[70-80)"
    elif age < 90:
        return "[80-90)"
    else:
        return "[90-100)"

@app.post("/predict")
def predict(data: InputData):
    print('in predict')
    print('incoming payload')
    print("As dict:", data.dict())
    input_dict = data.dict()
    input_dict['age'] = age_to_bucket(data.age)
    input_df = pd.DataFrame([input_dict])[[
        'model',
        'time_in_hospital',
        'num_lab_procedures',
        'num_procedures',
        'num_medications',
        'number_inpatient',
        'number_emergency',
        'number_outpatient',
        'number_diagnoses',
        'age',
        'gender',
        'admission_type_id',
        'discharge_disposition_id',
        'admission_source_id'
    ]]
    print('got features')
    #prob = model.predict_proba(features)[0][1]  # Assuming binary classifier

    if data.model == "random_forest":
        model = rf_model
    else:
        model = log_model

    prob = model.predict_proba(input_df)[0][1]  # Assuming binary classifier
    print('new')
    return {"readmission_probability": prob}

@app.get("/distribution")
def get_distribution(model_type: str = Query("logistic_regression", enum=["logistic_regression", "random_forest"])):
    try:
        # df = joblib.load("data/predicted_prob_distribution.pkl")

        if model_type == "logistic_regression":
            # probs = df["logistic_prob"].dropna().tolist()
            selected_df = df[["logistic_prob", "actual_readmitted"]]
        else:
            # probs = df["rf_prob"].dropna().tolist()
            selected_df = df[["rf_prob", "actual_readmitted"]]

        return JSONResponse(content=selected_df.sample(min(1000, len(selected_df))).to_dict(orient="records"))
        # df.sample(1000).to_dict(orient="records")
        # return JSONResponse(content={"probabilities": probs})
        # df = joblib.load("data/predicted_prob_distribution.pkl")
        # # If you want to send only a sample to keep it light
        # return df.sample(1000).to_dict(orient="records")


    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})



# Debugging get request
# @app.get("/ping")
# def ping():
#     return {"message": "pong"}