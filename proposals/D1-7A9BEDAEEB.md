> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Early Post-TACE Hepatic Deterioration as a Prognostic Marker in HCC

## Question
In patients with hepatocellular carcinoma (HCC) who undergo transarterial chemoembolization (TACE), does a composite measure of early hepatic deterioration during the first 7 days after the procedure predict subsequent hepatic decompensation, treatment failure, or death within 90 days, after adjustment for baseline liver function, tumor burden, and post-procedure observation intensity?

## Clinical importance
TACE is a common locoregional treatment for HCC, but a subset of patients experience early hepatic deterioration that may signal a need for escalation to systemic therapy or closer surveillance. Identifying these patients could inform treatment-selection decisions and resource allocation. The unresolved question is whether the early laboratory trajectory itself carries prognostic information beyond baseline liver function, or whether it merely reflects more intensive post-procedure monitoring.

## Evidence and closest prior work
- [K1] Decraecker et al. (2026) review the limitations of Child-Pugh scoring and the potential value of dynamic liver function monitoring and ALBI grade in HCC patients. They do not establish a validated early post-TACE deterioration marker.
- [K2] Yang et al. (2026) develop the AAPS (AFP-ALBI-PIVKA-II-serum albumin) scoring system for HCC patients receiving TACE. They do not specifically address early post-procedure hepatic deterioration.
- [K3] Llovet et al. (2022) provide a comprehensive review of HCC management, including the role of TACE and the importance of liver function assessment. They do not specifically address early post-procedure hepatic deterioration.

## Data bindings
- Source: HCC dataset (12 source files)
- Tables: procedures, laboratories, diagnoses, patients
- Columns: procedure_name, lab_name, value, unit, patient_id, procedure_date, lab_date, diagnosis_name, diagnosis_date
- Join keys: patient_id
- Time fields: procedure_date, lab_date, diagnosis_date

## Early hepatic deterioration composite
- Bilirubin: change in total bilirubin from day 0 to day 7
- Albumin: change in serum albumin from day 0 to day 7
- INR: change in INR from day 0 to day 7
- ALT/AST excluded due to zero early rows

## Sample size
- 20,064 TACE patients
- ~16,000 with complete early labs
- 817 outcome events

## Outcome definition
- Hepatic decompensation: new diagnosis of ascites, encephalopathy, or bilirubin > 3 mg/dL within 90 days
- Treatment failure: progression to systemic therapy within 90 days
- Death: death within 90 days

## Analysis
- Baseline model: baseline liver function (bilirubin, albumin, INR, Child-Pugh, ALBI) + tumor burden (AFP, tumor size) + observation intensity
- Alternative model: baseline model + early hepatic deterioration composite
- Temporal train/test split
- Bootstrap uncertainty
- Calibration assessment

## Falsification criteria
- If the early hepatic deterioration composite does not improve prediction beyond the baseline model, the hypothesis is falsified.
- If the improvement is driven by observation intensity, the hypothesis is falsified.

## Key references
- [K1] Decraecker et al. (2026)
- [K2] Yang et al. (2026)
- [K3] Llovet et al. (2022)
