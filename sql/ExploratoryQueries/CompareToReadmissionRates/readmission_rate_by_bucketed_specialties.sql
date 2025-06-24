---see medical specialties 
SELECT DISTINCT medical_specialty
FROM uci_diabetes_readmissions
ORDER BY medical_specialty;

--bucket specialties for readmission rate
SELECT 
  CASE 
    WHEN medical_specialty ILIKE '%cardio%' THEN 'Cardiology'
    WHEN medical_specialty ILIKE '%internal%' THEN 'Internal Medicine'
    WHEN medical_specialty ILIKE '%family%' OR medical_specialty ILIKE '%general%' THEN 'Primary Care'
    WHEN medical_specialty ILIKE '%surg%' THEN 'Surgery'
    WHEN medical_specialty = 'Emergency/Trauma' THEN 'Emergency'
    WHEN medical_specialty IS NULL OR medical_specialty = '?' THEN 'Unknown'
    ELSE 'Other'
  END AS specialty_group,
  COUNT(*) AS total_patients,
  SUM(CASE WHEN readmitted = 'NO' THEN 0 ELSE 1 END) AS readmitted_count,
  ROUND(100.0 * SUM(CASE WHEN readmitted = 'NO' THEN 0 ELSE 1 END) / COUNT(*), 2) AS readmission_rate
FROM uci_diabetes_readmissions
GROUP BY specialty_group
ORDER BY readmission_rate DESC;
