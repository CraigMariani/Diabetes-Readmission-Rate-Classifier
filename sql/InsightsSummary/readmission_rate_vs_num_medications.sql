SELECT 
  CASE 
    WHEN num_medications < 10 THEN '0–9'
    WHEN num_medications BETWEEN 10 AND 19 THEN '10–19'
    WHEN num_medications BETWEEN 20 AND 29 THEN '20–29'
    WHEN num_medications BETWEEN 30 AND 39 THEN '30–39'
    ELSE '40+' 
  END AS medication_range,
  COUNT(*) AS total_patients,
  SUM(CASE WHEN readmitted = 'NO' THEN 0 ELSE 1 END) AS readmitted_count,
  ROUND(100.0 * SUM(CASE WHEN readmitted = 'NO' THEN 0 ELSE 1 END) / COUNT(*), 2) AS readmission_rate
FROM uci_diabetes_readmissions
GROUP BY medication_range
ORDER BY medication_range;
