## Logistic Regression Summary

**Top Features (by negative coefficient size)**:
- cat__discharge_disposition_id_11.0 : -5.98 (decreased odds of readmission)
- cat__discharge_disposition_id_14.0 : -2.28 (decreased odds of readmission)
- cat__discharge_disposition_id_13.0 : -1.57 (decreased odds of readmission)

**Top Features (by positive coefficient size)**:
- cat__discharge_disposition_id_28.0 : +1.05 (increased odds of readmission)
- cat__discharge_disposition_id_15.0 : +0.85 (increased odds of readmission)
- cat__admission_source_id_20.0 : +0.78 (increased odds of readmission)

**Performance on Test Set**:
 		precision    recall  f1-score   support

           0       0.63      0.78      0.70     10980
           1       0.64      0.46      0.53      9374

    accuracy                           0.63     20354
   macro avg       0.63      0.62      0.61     20354
weighted avg       0.63      0.63      0.62     20354

- Accuracy: 0.63
- Precision (No Readmission - class 0)**: 0.63
- Recall (No Readmission - class 0)**: 0.78
- F1 Score (No Readmission - class 0)**: 0.70

- Precision (Readmission - class 1)**: 0.64
- Recall (Readmission - class 1)**: 0.46
- F1 Score (Readmission - class 1)**: 0.53

- Macro Avg F1 Score: 0.61
- ROC AUC: 0.68

**Confusion Matrix**:
- True Positives: 4279
- False Positives: 2396
- True Negatives: 8584
- False Negatives: 5095


Note: All top features came from the `discharge_disposition_id` column, which was one-hot encoded. Certain discharge types (e.g., to hospice or another hospital) strongly influenced readmission risk — either positively or negatively.



## Random Forest Model Summary

**Top Features (by importance)**:
- num_lab_procedure : 0.21
- num__num_medications	 : 0.17
- num__time_in_hospital : 0.11
...

**Performance on Test Set**:
- Accuracy: 0.60
- Precision (class 0): 0.62
- Recall (class 0): 0.69
- F1 (class 0): 0.65
- Precision (class 1): 0.58
- Recall (class 1): 0.69
- F1 (class 1): 0.65
- ROC AUC: 0.64





## Interpretation:

- **Logistic Regression** showed stronger overall precision and ROC AUC, making it more conservative in flagging patients as likely to be readmitted (fewer false positives).
- **Random Forest** delivered higher recall and F1 score for readmission cases, making it more effective at identifying true readmissions — though at the cost of more false positives.
- If minimizing missed readmissions is the top priority, **Random Forest** may be more appropriate.
- If interpretability and reducing false positives matter more, **Logistic Regression** is a solid, explainable baseline.

## Clinical Relevance:

In healthcare, the cost of missing a true readmission can be higher than issuing a false alert. Therefore, **Random Forest’s higher recall** may be more valuable in a hospital setting — especially for early intervention or care management programs.


Higher recall means we mighty have more false positives and higher precision means we might have more false negatives. In this scenario we would want higher false positives because the consequences are higher for missing a readmission then flagging someone falsely.