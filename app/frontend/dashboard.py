import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hospital Readmission Predictor", layout="wide")
st.title("Hospital Readmission Risk Predictor")

# --- Sidebar Inputs ---
st.sidebar.title("Enter Patient Information")

age = st.sidebar.selectbox("Age", ["[30-40)", "[40-50)", "[50-60)", "[60-70)", "[70-80)", "[80-90)"])
gender = st.sidebar.radio("Gender", ["Male", "Female"])
time_in_hospital = st.sidebar.slider("Time in hospital (days)", 1, 14, 5)
num_lab_procedures = st.sidebar.slider("Number of lab procedures (tests)", 1, 132, 40)
num_medications = st.sidebar.slider("Number of medications (total)", 1, 81, 20)
number_diagnoses = st.sidebar.slider("Number of diagnoses", 1, 16, 5)
number_inpatient = st.sidebar.slider("Number of inpatient visits (count)", 0, 20, 1)
number_outpatient = st.sidebar.slider("Number of outpatient visits (count)", 0, 20, 1)
number_emergency = st.sidebar.slider("Number of emergency visits (count)", 0, 10, 0)
num_procedures = st.sidebar.slider("Number of procedures (operations)", 0, 6, 1)

# dictionaries for id selection
admission_type_dict = {
    1: "Emergency", 2: "Urgent", 3: "Elective", 4: "Newborn",
    5: "Not Available", 6: "NULL", 7: "Trauma Center", 8: "Not Mapped"
}

discharge_disposition_dict = {
    1: "Discharged to home", 2: "Discharged/transferred to another short term hospital", 3: "Discharged/transferred to SNF",
    4: "ICF", 5: "Another type of facility", 6: "Home with home health service", 7: "Left against medical advice",
    8: "Discharged/transferred to home under care of home IV provider", 11: "Expired", 13: "Expired at home", 14: "Expired at hospital",
    28: "Expired somewhere else"
}

admission_source_dict = {
    1: "Physician Referral", 2: "Clinic Referral", 3: "HMO Referral", 4: "Transfer from hospital",
    5: "Transfer from SNF", 6: "Transfer from other facility", 7: "Emergency Room", 9: "Information Not Available",
    10: "Transfer from Critical Access Hospital", 20: "NULL"
}

# --- Admission Type ---
admission_type_label = st.sidebar.selectbox(
    "Admission Type",
    options=list(admission_type_dict.values()),
    help="Reason for hospital admission"
)
admission_type_id = next(k for k, v in admission_type_dict.items() if v == admission_type_label)

# --- Discharge Disposition ---
discharge_label = st.sidebar.selectbox(
    "Discharge Disposition",
    options=list(discharge_disposition_dict.values()),
    help="Where the patient was discharged to"
)
discharge_disposition_id = next(k for k, v in discharge_disposition_dict.items() if v == discharge_label)

# --- Admission Source ---
admission_source_label = st.sidebar.selectbox(
    "Admission Source",
    options=list(admission_source_dict.values()),
    help="Where the patient came from before this admission"
)
admission_source_id = next(k for k, v in admission_source_dict.items() if v == admission_source_label)

# --- Send POST request to predict ---

model_choice = st.radio("Model", ["Logistic Regression", "Random Forest"])
model_key = "logistic_regression" if model_choice == "Logistic Regression" else "random_forest"

if st.button("Predict Readmission Probability"):
    with st.spinner("Making prediction..."):
        payload = {
            "model": model_key,
            "age": age,
            "gender": gender,
            "admission_type_id": admission_type_id,
            "discharge_disposition_id": discharge_disposition_id,
            "admission_source_id": admission_source_id,
            "num_procedures": num_procedures,
            "num_medications": num_medications,
            "time_in_hospital": str(time_in_hospital),  # ensure it's a string if model expects it
            #"time_in_hospital": time_in_hospital, # should be fixed
            "num_lab_procedures": num_lab_procedures,
            "number_inpatient": number_inpatient,
            "number_emergency": number_emergency,
            "number_outpatient": number_outpatient,
            "number_diagnoses": number_diagnoses
        }

        try:
            # ---- POST to model ----
            # response = requests.post("http://localhost:8000/predict", json=payload) # for local
            response = requests.post("http://backend:8000/predict", json=payload) # for docker
            response.raise_for_status()
            prediction = response.json()["readmission_probability"]

            st.success(f"Predicted Readmission Probability: **{prediction:.2%}**")

            # ---- GET distribution data ----
            # dist_response = requests.get("http://localhost:8000/distribution", params={"model_type": model_key}) # for local
            dist_response = requests.get("http://backend:8000/distribution", params={"model_type": model_key}) # for docker
            dist_response.raise_for_status()
            dist_data = pd.DataFrame(dist_response.json())

            # ---- Plot ----
            st.subheader("Compare with Population Predictions")

            fig, ax = plt.subplots()
            if model_key == "logistic_regression":
                chosen_prob = "logistic_prob"

            else:
                chosen_prob = "rf_prob"

            ax.hist(dist_data[chosen_prob], bins=30, alpha=0.6, label="Population", color='skyblue')
            ax.axvline(prediction, color='blue', linestyle='--', linewidth=2, label="Your Prediction")

            ax.set_xlabel("Predicted Probability of Readmission")
            ax.set_ylabel("Number of Patients")
            ax.legend()

            st.pyplot(fig)

        except Exception as e:
            st.error(f"Error: {e}")
