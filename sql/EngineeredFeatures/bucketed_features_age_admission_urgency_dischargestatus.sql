

---age_bucket, admission_urgency, discharge_status buckets
SELECT 
  *,
  CASE 
    WHEN age IN ('[0-10)', '[10-20)', '[20-30)') THEN 'Under 30'
    WHEN age IN ('[30-40)', '[40-50)', '[50-60)') THEN '30–60'
    WHEN age IN ('[60-70)', '[70-80)', '[80-90)', '[90-100)') THEN 'Over 60'
    ELSE 'Unknown'
  END AS age_bucket,

  CASE 
    WHEN admission_type_id::int = 1 THEN 'Emergency'
    WHEN admission_type_id::int = 2 THEN 'Urgent'
    WHEN admission_type_id::int = 3 THEN 'Elective'
    ELSE 'Other'
  END AS admission_urgency,

  CASE 
    WHEN discharge_disposition_id::int IN (11, 19, 20, 21) THEN 'Expired'
    WHEN discharge_disposition_id::int IN (3, 4, 5, 6, 22, 23, 24, 30) THEN 'Transferred'
    WHEN discharge_disposition_id::int = 1 THEN 'Discharged Home'
    ELSE 'Other'
  END AS discharge_status,

  CASE 
    WHEN readmitted = 'NO' THEN 0
    ELSE 1
  END AS readmitted_flag

FROM uci_diabetes_readmissions;

/*
---length of stay buckets (los_bucket)
SELECT 
  patient_nbr,
  time_in_hospital,
  CASE 
    WHEN time_in_hospital::int <= 3 THEN 'Short'
    WHEN time_in_hospital::int BETWEEN 4 AND 7 THEN 'Medium'
    ELSE 'Long'
  END AS los_bucket
FROM uci_diabetes_readmissions
LIMIT 10;
*/

-- number of diagnosis volumes (diagnosis_volume)
SELECT 
  patient_nbr,
  d.number_diagnoses,
  CASE 
    WHEN d.number_diagnoses::int < 5 THEN 'Few'
    WHEN d.number_diagnoses::int BETWEEN 5 AND 8 THEN 'Moderate'
    ELSE 'Many'
  END AS diagnosis_volume
FROM uci_diabetes_readmissions d
LIMIT 10;



/*
--- Age Group Refinement (age_group)
SELECT 
  patient_nbr,
  age,
  CASE 
    WHEN age IN ('[0-10)', '[10-20)', '[20-30)') THEN '<30'
    WHEN age IN ('[30-40)', '[40-50)', '[50-60)') THEN '30-60'
    ELSE '60+'
  END AS age_group
FROM uci_diabetes_readmissions
LIMIT 10;
*/
