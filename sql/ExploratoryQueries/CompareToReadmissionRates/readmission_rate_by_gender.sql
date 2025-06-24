---readmission rate by gender
SELECT 
  d.gender AS gender,
  COUNT(*) AS total_patients,
  SUM(CASE WHEN d.readmitted <> 'NO' THEN 0 ELSE 1 END) AS readmitted_count,
  ROUND(100.0 * SUM(CASE WHEN d.readmitted <> 'NO' THEN 0 ELSE 1 END) / COUNT(*), 2) AS readmission_rate
FROM uci_diabetes_readmissions d
--JOIN discharge_disposition_lookup dd ON d.admission_source_id::int = dd.discharge_disposition_id
GROUP BY d.gender
ORDER BY readmission_rate DESC;