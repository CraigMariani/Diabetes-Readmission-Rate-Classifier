
---readmission rate by admission_source
SELECT 
  s.description AS admission_source,
  COUNT(*) AS total_patients,
  SUM(CASE WHEN d.readmitted <> 'NO' THEN 0 ELSE 1 END) AS readmitted_count,
  ROUND(100.0 * SUM(CASE WHEN d.readmitted <> 'NO' THEN 0 ELSE 1 END) / COUNT(*), 2) AS readmission_rate
FROM uci_diabetes_readmissions d
JOIN admission_source_lookup s ON d.admission_source_id::int = s.admission_source_id
GROUP BY s.description
ORDER BY readmission_rate DESC;