CREATE TABLE readmission_dashboard_data AS
SELECT
    r.encounter_id,
    r.patient_nbr,
    r.race,
    r.gender,
    r.age,
    r.weight,

    -- JOINED Descriptions
    atl.description AS admission_type_desc,
    ddl.description AS  discharge_disposition_desc,
    asl.description AS  admission_source_desc,

    r.time_in_hospital,
    r.payer_code,
    r.medical_specialty,
    r.num_lab_procedures,
    r.num_procedures,
    r.num_medications,
    r.number_outpatient,
    r.number_emergency,
    r.number_inpatient,
    r.diag_1,
    r.diag_2,
    r.diag_3,
    r.number_diagnoses,
    r.max_glu_serum,
    --r.A1Cresult,
    r.metformin,
    r.repaglinide,
    r.nateglinide,
    r.chlorpropamide,
    r.glimepiride,
    r.acetohexamide,
    r.glipizide,
    r.glyburide,
    r.tolbutamide,
    r.pioglitazone,
    r.rosiglitazone,
    r.acarbose,
    r.miglitol,
    r.troglitazone,
    r.tolazamide,
    r.examide,
    r.citoglipton,
    r.insulin,
    --r.glyburide_metformin,
    --r.glipizide_metformin,
    --r.glimepiride_pioglitazone,
    --r.metformin_rosiglitazone,
    --r.metformin_pioglitazone,
    r.change,
    --r.diabetesMed,
    r.readmitted,

    -- Binary column for modeling and dashboard
    CASE 
        WHEN readmitted = 'NO' THEN 0
        ELSE 1
    END AS readmitted_binary

FROM
    uci_diabetes_readmissions r

-- Join lookup tables
LEFT JOIN admission_source_lookup asl
	ON r.admission_source_id::int = asl.admission_source_id::int

LEFT JOIN admission_type_lookup atl
	ON r.admission_type_id::int = atl.admission_type_id::int

LEFT JOIN discharge_disposition_lookup ddl
	ON r.discharge_disposition_id::int = ddl.discharge_disposition_id::int


WHERE
    r.discharge_disposition_id::int NOT IN (11, 13, 14, 19, 20, 21);  -- Optional: filters you used in modeling

