---readmission rate by discharge disposition
SELECT 
  t.description AS admission_type,
  COUNT(*) AS total_patients,
  SUM(CASE WHEN d.readmitted <> 'NO' THEN 0 ELSE 1 END) AS readmitted_count,
  ROUND(100.0 * SUM(CASE WHEN d.readmitted <> 'NO' THEN 0 ELSE 1 END) / COUNT(*), 2) AS readmission_rate
FROM uci_diabetes_readmissions d
JOIN admission_type_lookup t ON d.admission_type_id::int = t.admission_type_id
GROUP BY t.description
ORDER BY readmission_rate DESC;