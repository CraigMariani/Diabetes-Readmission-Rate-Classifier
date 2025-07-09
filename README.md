# Hospital Readmission Prediction

This project analyzes real-world hospital data to predict readmissions in diabetic patients using machine learning — and presents the findings through a **Power BI dashboard** and a **Streamlit app**.

It demonstrates full-stack data skills across SQL, ML, visualization, and deployment.

---

## Objectives

- Analyze patient data to identify patterns in readmissions
- Engineer meaningful features with SQL and Python
- Build and evaluate ML models for binary classification
- Compare model performance and trade-offs
- Visualize trends and insights with Power BI
- Deploy interactive app with Streamlit and backend model

##  Tools Used

- Python, scikit-learn, pandas, matplotlib, seaborn
- SQL (PostgreSQL)
- Jupyter Notebook
- Git + GitHub
- Power BI
- Streamlit

##  Results

- Logistic Regression AUC: 0.68 (higher precision, more interpretable)
- Random Forest AUC: 0.64 (higher recall, better F1 for readmitted patients)
- Full performance metrics in `reports/model_summary.md`

---

## Power BI Dashboard

This dashboard summarizes readmission patterns by race, gender, age, admission type, discharge disposition, time in hospital, and medical specialty.

**Layout**: 2-column structure with 7 clean visualizations  
**KPI**: Overall Readmission Rate = **0.47**

### Visuals Included:

| Metric/Dimension            | Chart Type      |
|-----------------------------|------------------|
| Readmission Rate (overall)  | KPI Card         |
| By Race                     | Donut Chart      |
| By Gender                   | Bar Chart        |
| By Age                      | Column Chart     |
| By Admission Type           | Bar Chart        |
| By Discharge Disposition    | Bar Chart        |
| By Time in Hospital         | Column Chart     |
| By Medical Specialty        | Bar Chart        |

*Insight:* Emergency admissions and certain specialties (e.g. cardiology) were associated with higher readmission risk.

---


##  Project Structure

/data → Source & processed data
/sql → SQL queries used for analysis & feature engineering
/models → Trained serialized ML models (.pkl)
/notebooks → Jupyter notebook (modeling.ipynb) and graphs
/reports → Model summary & visualizations
/app → Streamlit app scripts 


## How to Run

1. Clone the repo
2. Install requirements  
   `pip install -r requirements.txt`
3. Open and run `notebooks/modeling.ipynb`

## Key Takeaways

- Random Forest caught more readmissions (69% recall)
- Logistic Regression provided better interpretability
- Dataset features like discharge disposition, lab procedures, and medication count were highly predictive
-Features like discharge disposition, medication count, and lab procedures were strong predictors

-Power BI dashboard effectively communicates risk patterns to stakeholders


Discharge disposition is a strong driver of readmission — where a patient is sent after care can indicate their risk of returning.

Treatment complexity (lab tests, medications, diagnoses) consistently ranked high across models.

Simple correlations don’t reveal much — predictive modeling captured more nuance than raw feature relationships.

