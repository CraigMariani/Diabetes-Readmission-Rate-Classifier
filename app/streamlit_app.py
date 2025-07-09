import streamlit as st
import joblib
import numpy as np

# Load model and any encoders if needed
model = joblib.load("models/logistic_model.pkl")

# App title
st.title("Hospital Readmission Risk Predictor")
st.write("Enter patient info below to predict likelihood of readmission.")

# Input fields — adjust based on your final model features
age = st.selectbox("Age", ["[0-10)", "[10-20)", "[20-30)", "[30-40)", "[40-50)", "[50-60)", "[60-70)", "[70-80)", "[80-90)", "[90-100)"])
gender = st.selectbox("Gender", ["Male", "Female"])
time_in_hospital = st.slider("Time in hospital (days)", 1, 14, 5)
num_lab_procedures = st.slider("Number of lab procedures", 1, 132, 40)
num_medications = st.slider("Number of medications", 1, 81, 20)
number_diagnoses = st.slider("Number of diagnoses", 1, 16, 5)

# Create input array — match your model’s preprocessing format!
# You'll likely need to one-hot encode or match column order if using full pipeline
user_input = np.array([[time_in_hospital, num_lab_procedures, num_medications, number_diagnoses]])

# Predict button
if st.button("Predict Readmission"):
    prediction_proba = model.predict_proba(user_input)[0][1]
    st.success(f"Predicted Readmission Probability: {prediction_proba:.2%}")
