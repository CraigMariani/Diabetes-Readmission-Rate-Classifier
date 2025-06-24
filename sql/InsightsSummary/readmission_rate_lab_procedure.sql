SELECT 
  CASE 
    WHEN num_lab_procedures < 20 THEN '0–19'
    WHEN num_lab_procedures BETWEEN 20 AND 39 THEN '20–39'
    WHEN num_lab_procedures BETWEEN 40 AND 59 THEN '40–59'
    WHEN num_lab_procedures BETWEEN 60 AND 79 THEN '60–79'
    ELSE '80+' 
  END AS lab_procedure_range,
  COUNT(*) AS total_patients,
  SUM(CASE WHEN readmitted = 'NO' THEN 0 ELSE 1 END) AS readmitted_count,
  ROUND(100.0 * SUM(CASE WHEN readmitted = 'NO' THEN 0 ELSE 1 END) / COUNT(*), 2) AS readmission_rate
FROM uci_diabetes_readmissions
GROUP BY lab_procedure_range
ORDER BY lab_procedure_range;
