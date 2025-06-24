
-- Readmission Rate by number_inpatient
SELECT 
  number_inpatient,
  COUNT(*) AS total_patients,
  SUM(CASE WHEN readmitted = 'NO' THEN 0 ELSE 1 END) AS readmitted_count,
  ROUND(100.0 * SUM(CASE WHEN readmitted = 'NO' THEN 0 ELSE 1 END) / COUNT(*), 2) AS readmission_rate
FROM uci_diabetes_readmissions
GROUP BY number_inpatient
ORDER BY number_inpatient;
