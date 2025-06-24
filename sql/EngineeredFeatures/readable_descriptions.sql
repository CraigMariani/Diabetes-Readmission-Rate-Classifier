
--enrich the UCI dataset with readable descriptions:
SELECT 
  d.patient_nbr,
  d.readmitted,
  t.description AS admission_type,
  s.description AS admission_source,
  dd.description AS discharge_disposition
FROM uci_diabetes_readmissions d
LEFT JOIN admission_type_lookup t ON d.admission_type_id::int = t.admission_type_id
LEFT JOIN admission_source_lookup s ON d.admission_source_id::int = s.admission_source_id
LEFT JOIN discharge_disposition_lookup dd ON d.discharge_disposition_id::int = dd.discharge_disposition_id
LIMIT 20;
