> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Discordant creatinine recovery after AKI: a severity-, treatment-intensity-, and RRT-stratified MIMIC-IV study with urine-output sensitivity analysis

Status: active draft, not yet a registered hypothesis. Parent: [prior hypothesis].

## Question and clinical importance

Among adults in the ICU with KDIGO stage 2 or 3 acute kidney injury (AKI), does apparent creatinine recovery at 48 hours coexisting with persistently low urine output or positive fluid balance identify a worse 7-day ICU prognosis than creatinine recovery alone, after accounting for current severity and treatment intensity at the 48-hour stabilization decision point?

The parent proposal established a prespecified discordant creatinine-recovery phenotype and addressed the strongest confounder—current severity and treatment intensity at the decision point—with SOFA component scores, vasopressor use, mechanical ventilation, and renal replacement therapy (RRT) status as adjustment variables. The RRT stratification added a clinically important distinction: patients on RRT have a fundamentally different renal recovery phenotype and outcome trajectory than those not on RRT.

However, a residual concern remains: creatinine is a surrogate for measured kidney function, and creatinine-based recovery may be a poor surrogate for true renal recovery. If the discordance phenotype is driven by creatinine measurement artifacts, it may not persist when recovery is defined by urine-output criteria. The current proposal adds a prespecified sensitivity analysis using KDIGO urine-output criteria as an alternative renal recovery definition, with explicit UO extraction logic, stratum-specific estimands, and interpretation rules.

## Evidence and unresolved claim

The strongest claim supported by the available evidence is that longitudinal laboratory and support patterns can distinguish ICU patients with different prognoses. The expert seed proposes that recovery after circulatory stabilization is asynchronous across organs and that delayed or incomplete recovery predicts later deterioration.

The unresolved claim is whether the discordance phenotype is robust to the definition of renal recovery. If the phenotype is driven by creatinine measurement artifacts, it may not persist when recovery is defined by urine-output criteria. The sensitivity analysis tests this directly.

## Data bindings

- Source: MIMIC-IV v3.1, `mimiciv.databases` (Parquet)
- Patient: `patients.subject_id`, `patients.gender`, `patients.anchor_age`, `patients.anchor_year`
- ICU stay: `icustays.subject_id`, `icustays.hadm_id`, `icustays.stay_id`, `icustays.intime`, `icustays.outtime`
- Lab: `labevents.subject_id`, `labevents.stay_id`, `labevents.charttime`, `labevents.itemid`, `labevents.value`, `labevents valuenum`
- Chart: `chartevents.subject_id`, `chartevents.stay_id`, `chartevents.charttime`, `chartevents.itemid`, `chartevents.value`, `chartevents.valueunit`
- Output events: `outputevents.subject_id`, `outputevents.stay_id`, `outputevents.charttime`, `outputevents.itemid`, `outputevents.value`
- Input events: `inputevents.subject_id`, `inputevents.stay_id`, `inputevents.charttime`, `inputevents.itemid`, `inputevents.value`, `inputevents.streamid`
- Prescriptions: `prescriptions.subject_id`, `prescriptions.hadm_id`, `prescriptions.starttime`, `prescriptions.stoptime`, `prescriptions.drug_name`
- Diagnoses: `diagnoses.subject_id`, `diagnoses.hadm_id`, `diagnoses.icd9_code`, `diagnoses.icd10_code`
- Procedures: `procedures_icd.subject_id`, `procedures_icd.hadm_id`, `procedures_icd.icd9_code`, `procedures_icd.icd10_code`
- Mortality: `mortality.subject_id`, `mortality.hadm_id`, `mortality.dod`

## Population and temporal design

1. Adults (age >= 18) with at least one ICU stay in MIMIC-IV.
2. KDIGO stage 2 or 3 AKI: creatinine >= 2x baseline (stage 2) or >= 3x baseline (stage 3), or creatinine >= 2x baseline with urine output < 0.5 mL/kg/h for >= 12 hours (stage 2), or creatinine >= 3x baseline with urine output < 0.5 mL/kg/h for >= 24 hours (stage 3).
3. 48-hour decision point: the first time at which creatinine has recovered to < 1.5x baseline (or < 2x baseline for stage 2) AND the patient has been in the ICU for at least 48 hours.
4. Discordant phenotype: creatinine recovery at 48 hours coexisting with persistently low urine output (< 0.5 mL/kg/h for >= 12 hours in the preceding 24 hours) OR positive fluid balance (> 500 mL in the preceding 24 hours).
5. Outcome: 7-day ICU prognosis, defined as ICU death or ICU length of stay > 7 days.

## Sensitivity analysis: KDIGO urine-output criteria

The sensitivity analysis redefines renal recovery using KDIGO urine-output criteria rather than creatinine criteria:

- Recovery by UO: urine output >= 0.5 mL/kg/h for >= 12 hours in the preceding 24 hours.
- Discordant phenotype (UO-defined): UO recovery at 48 hours coexisting with persistently elevated creatinine (>= 1.5x baseline) OR positive fluid balance (> 500 mL in the preceding 24 hours).
- Stratum-specific estimands: the same RRT stratification as the primary analysis, with stratum-specific hazard ratios and interaction tests.
- Interpretation rules: if the discordance phenotype persists when recovery is defined by UO criteria, it is more likely to reflect a true prognostic signal. If the phenotype does not persist, it is likely an artifact of creatinine measurement.

## Method comparison

- Baseline: unadjusted logistic regression for 7-day ICU prognosis, with the discordant phenotype as the primary predictor.
- Adjusted: logistic regression with SOFA component scores, vasopressor use, mechanical ventilation, and RRT status as adjustment variables.
- Propensity-score or overlap-weighted secondary analysis: to address residual confounding by treatment intensity.
- RRT stratification: stratum-specific estimands and interaction test.
- UO sensitivity analysis: as described above.

## Falsification criteria

- If the discordance phenotype does not persist after adjustment for severity and treatment intensity, the phenotype is likely a marker of current severity rather than an independent prognostic signal.
- If the discordance phenotype does not persist when recovery is defined by UO criteria, the phenotype is likely an artifact of creatinine measurement.
- If the discordance phenotype is not robust to the RRT stratification, the phenotype may be driven by the RRT population.

## Limitations

- Creatinine is a surrogate for measured kidney function. The sensitivity analysis using UO criteria addresses this concern but does not eliminate it.
- The study is prognostic, not causal. The adjustment variables address residual confounding but do not establish causality.
- The 48-hour decision point is a prespecified time, not a clinically validated time. The choice of 48 hours is based on the expert seed and the literature, but it may not be optimal for all patients.

## Key references

[K1] Comparison of Cystatin C and Creatinine in the Assessment of Measured Kidney Function during Critical Illness. (2023). PMID: 37256861.
[K2] Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations. (2022). Nature Communications.
[K3] KDIGO Clinical Practice Guideline for Acute Kidney Injury. (2012). Kidney International.
