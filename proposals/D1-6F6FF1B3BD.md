> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Early Post-TACE Hepatic Deterioration: Trajectory Shape vs. Endpoint Composite

## Question
In patients with hepatocellular carcinoma (HCC) who undergo transarterial chemoembolization (TACE), does the temporal pattern of hepatic deterioration (trajectory shape: AUC and slope of bilirubin, albumin, and INR over days 1-7) add prognostic information beyond the fixed 7-day endpoint composite, after adjustment for baseline liver function, tumor burden, and post-procedure observation intensity?

## Clinical importance
TACE is a common locoregional treatment for HCC, but a subset of patients experience early hepatic deterioration that may signal a need for escalation to systemic therapy or closer surveillance. The fixed 7-day endpoint composite captures the magnitude of deterioration at day 7, but not the temporal pattern. Two patients with the same day-7 bilirubin level may have very different trajectories: one with a rapid early spike followed by partial recovery, and another with a slow, progressive rise. The trajectory shape may carry prognostic information beyond the endpoint composite, and this distinction could inform early intervention decisions (e.g., whether to escalate to systemic therapy or intensify surveillance).

## Evidence and closest prior work
- [K1] Decraecker et al. (2026) review the limitations of Child-Pugh scoring and the potential value of dynamic liver function monitoring and ALBI grade in HCC patients.
- [K2] Yang et al. (2026) demonstrate that the AAPS scoring system, integrating dynamic biomarkers (AFP, PIVKA-II) with liver function (ALBI grade, serum albumin), refines prognostic stratification in HCC.
- [K3] Singalagada et al. (2025) show that early post-procedure laboratory changes are associated with 90-day outcomes in HCC patients undergoing TACE.

## Data bindings
- Source: HCC dataset (exact paths in datasets/README.md)
- Procedure: TACE (procedure name in the procedures table)
- Laboratories: bilirubin, albumin, INR (laboratory names in the labs table)
- Tables: patients, procedures, labs, outcomes
- Join keys: patient_id
- Time fields: procedure_date, lab_date, outcome_date
- Sample size: 20,064 TACE patients, ~16,000 with complete early labs, 817 outcome events

## Design
- Baseline: fixed 7-day endpoint composite (bilirubin, albumin, INR at day 7)
- Alternative: trajectory shape (AUC and slope of bilirubin, albumin, INR over days 1-7)
- Models: nested Cox models comparing baseline vs. alternative
- Metrics: NRI, IDI, C-index
- Interaction term: trajectory shape × endpoint composite
- Falsification: non-significant interaction or negligible incremental C-index

## Prognostic vs. causal
This is a prognostic study, not a causal study. The trajectory shape is a prognostic marker, not a causal intervention. The design does not establish causality.

## Sensitivity analysis
- 3-day window
- 5-day window
- 10-day window

## Decision-curve analysis
- Thresholds for treatment escalation
- Net benefit at each threshold

## Key references
- [K1] Decraecker et al. (2026)
- [K2] Yang et al. (2026)
- [K3] Singalagada et al. (2025)
