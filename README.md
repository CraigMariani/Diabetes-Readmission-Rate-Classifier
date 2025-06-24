# Hospital Readmission Prediction

This project uses real-world healthcare data to predict hospital readmissions using Logistic Regression and Random Forest models.

## Objectives

- Analyze patient data to identify patterns in readmissions
- Engineer meaningful features with SQL and Python
- Build and evaluate ML models for binary classification
- Compare model performance and trade-offs
- (Optional) Deploy model or dashboard

##  Tools Used

- Python, scikit-learn, pandas, matplotlib, seaborn
- SQL (PostgreSQL)
- Jupyter Notebook
- Git + GitHub

##  Results

- Logistic Regression AUC: 0.68 (higher precision, more interpretable)
- Random Forest AUC: 0.64 (higher recall, better F1 for readmitted patients)
- Full performance metrics in `reports/model_summary.md`

##  Project Structure

/data → Source & processed data
/sql → SQL queries used for analysis & feature engineering
/models → Trained serialized ML models (.pkl)
/notebooks → Jupyter notebook (modeling.ipynb) and graphs
/reports → Model summary & visualizations


## How to Run

1. Clone the repo
2. Install requirements  
   `pip install -r requirements.txt`
3. Open and run `notebooks/modeling.ipynb`

## Key Takeaways

- Random Forest caught more readmissions (69% recall)
- Logistic Regression provided better interpretability
- Dataset features like discharge disposition, lab procedures, and medication count were highly predictive
