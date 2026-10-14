> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Robustness of time-weighted hypotension burden for early AKI: summary choice, measurement-density and baseline-severity controls

## Scientific question

Among adult ICU patients with adequate systolic and diastolic blood-pressure measurements in the first 24 hours of ICU care, does a prespecified time-weighted hypotension burden measure improve prediction of acute kidney injury (AKI) within 48 hours beyond the 24-hour mean arterial pressure (MAP), after controlling for measurement density, baseline illness severity, and after showing that the signal is robust to the choice of blood-pressure summary (MAP, systolic, diastolic, combined)?

The unresolved claim is that duration and time-weighting of hypotension add clinically meaningful prognostic information beyond MAP, after accounting for baseline illness severity, vasopressor exposure, baseline kidney function, hospital, and measurement density. The strongest rival is that the apparent burden signal is an artifact of recording density, measurement timing, or baseline illness severity, or that it is specific to one arbitrary choice of blood-pressure summary. A null result would weaken the claim that a more complex burden measure is useful; a positive result would support further validation and prospective study.

## Why it matters

MAP is the common bedside summary and a natural baseline for hemodynamic risk. Minimum systolic blood pressure alone can overstate a single low reading, while MAP may understate sustained hypoperfusion. If time-weighted burden improves early AKI risk stratification, it may inform monitoring and resuscitation decisions. If it does not, clinicians and researchers should not add a more complex measure without evidence.

Baseline illness severity is a major confounder for AKI. Conditioning on severity (APACHE IV primary, SOFA fallback) and testing severity strata and missing-severity sensitivity analyses makes the burden signal more clinically interpretable and reduces the risk that the result is driven by sicker patients.

## Prior evidence

- [K1] Liu et al. (2026) report an association between cumulative intraoperative hypotension and postoperative ICU admission in a retrospective cohort, supporting the clinical relevance of hypotension duration but not establishing its prognostic value for AKI in ICU patients.
- [K2] Tarbaghia et al. (2026) examine hemodynamic response in septic shock with myocardial dysfunction, illustrating the importance of hemodynamic context and severity in interpreting blood-pressure measures.
- [K3] Goyal et al. (2026) provide a clinical review of AKI, including risk factors and the importance of early identification, which motivates the need for a robust early AKI predictor.

## Population and temporal design

Use eICU 2.0 adult ICU admissions with at least one systolic and one diastolic blood-pressure measurement in the first 24 hours of ICU care. Exclude patients with missing baseline kidney function, missing hospital identifier, or fewer than 10 blood-pressure measurements in the first 24 hours (measurement-density floor).

Define the first 24 hours from the ICU admission timestamp (`patient.stay_id` joined to `vital.stay_id` on `stay_id`, with `vital.time` in `[patient.icu_admit_time, patient.icu_admit_time + 24h]`).

Define AKI within 48 hours using the KDIGO creatinine criteria: a rise in serum creatinine to ≥1.5× baseline and ≥0.3 mg/dL within 48 hours of ICU admission, or urine output <0.5 mL/kg/h for ≥6 hours (if urine output data are available). Baseline creatinine is the first creatinine measurement in the first 24 hours.

## Variables and data bindings

All bindings are to eICU 2.0 source files and tables.

- Patient demographics and admission: `patient` table, columns `stay_id`, `icu_admit_time`, `age`, `sex`, `race`, `ethnicity`, `hospital_id`.
- Severity scores: `patient` table, columns `apache4` (APACHE IV), `apache4a`, `apache4b`, `apache4c`, `apache4d`, `apache4e`, `apache4f`, `apache4g`, `apache4h`, `apache4i`, `apache4j`, `apache4k`, `apache4l`, `apache4m`, `apache4n`, `apache4o`, `apache4p`, `apache4q`, `apache4r`, `apache4s`, `apache4t`, `apache4u`, `apache4v`, `apache4w`, `apache4x`, `apache4y`, `apache4z`; `sofa` table, columns `stay_id`, `sofa`, `sofa_time`.
- Blood pressure: `vital` table, columns `stay_id`, `time`, `systolic_bp`, `diastolic_bp`, `mean_arterial_pressure`.
- Kidney function: `lab` table, columns `stay_id`, `time`, `creat`, `creatinine`.
- Vasopressors: `infusion` table, columns `stay_id`, `time`, `drug_name`, `rate`, `concentration`.
- Urine output: `urine_output` table, columns `stay_id`, `time`, `output`.
- Hospital: `hospital` table, columns `hospital_id`, `hospital_name`.

Join keys: `stay_id` across all tables; `hospital_id` across `patient` and `hospital`.

Time fields: `icu_admit_time` (patient), `time` (vital, lab, infusion, urine_output), `sofa_time` (sofa).

## Hypotension burden measure

Define hypotension as MAP < 65 mmHg (primary) or systolic BP < 90 mmHg (secondary). Compute the time-weighted burden as the fraction of the first 24 hours during which the patient was hypotensive, using linear interpolation between measurements. Also compute the 24-hour MAP, minimum systolic BP, and minimum diastolic BP as baselines.

## Analysis plan

1. Fit a logistic regression model with AKI within 48 hours as the outcome and the following covariates: 24-hour MAP, age, sex, race, ethnicity, baseline creatinine, vasopressor exposure (any vasopressor in the first 24 hours), hospital, and measurement density (number of BP measurements in the first 24 hours).
2. Add the time-weighted hypotension burden to the model and test whether it improves prediction (AUC, calibration, Brier score) beyond the baseline model.
3. Repeat the analysis using systolic BP, diastolic BP, and combined (MAP + systolic + diastolic) summaries to test robustness to the choice of blood-pressure summary.
4. Condition on baseline illness severity: use APACHE IV as the primary severity score when available, with a prespecified SOFA-based fallback when APACHE IV is missing. Include a severity-stratum analysis (low, medium, high) and a missing-severity sensitivity analysis.
5. Report hospital-level analysis: fit the model within each hospital and report the distribution of burden coefficients and AUC improvements across hospitals.

## Solver deliverable and uncertainty reporting

The solver must deliver:
- The fitted logistic regression models (baseline and burden) with coefficients, standard errors, and 95% confidence intervals.
- AUC, calibration (Hosmer-Lemeshow, calibration-in-the-large, calibration-slope), and Brier score for each model, with 95% confidence intervals.
- The distribution of burden coefficients and AUC improvements across hospitals, with 95% confidence intervals.
- The severity-stratum analysis and missing-severity sensitivity analysis, with 95% confidence intervals.
- A summary of the robustness analysis (MAP, systolic, diastolic, combined) with 95% confidence intervals.

## Falsification criteria

The burden signal is considered falsified if:
- The burden coefficient is not statistically significant (95% CI includes 0) in the primary model after controlling for severity, measurement density, and hospital.
- The burden signal is not robust to the choice of blood-pressure summary (MAP, systolic, diastolic, combined).
- The burden signal is driven by a small number of hospitals (hospital-level analysis shows heterogeneity).
- The burden signal is not present in the severity-stratum analysis (low, medium, high) or is driven by missing severity.

## Interpretation

A positive result would support the use of time-weighted hypotension burden as a clinically meaningful prognostic measure for early AKI, beyond MAP, after accounting for severity and measurement density. A null result would weaken the claim that a more complex burden measure is useful. An inconclusive result (e.g., significant in some hospitals but not others) would suggest the need for further validation and prospective study.

## Bibliography

- [K1] Liu Z, Wang N, Chen M, Wang H. Association between cumulative intraoperative hypotension and postoperative ICU admission after gastrointestinal lumen cancer surgery: a retrospective cohort study using the INSPIRE database. Front Med (Lausanne). 2026;13:1916589. doi:10.3389/fmed.2026.1916589
- [K2] Tarbaghia M, Nanah A, Sato R, Sanfilippo F, Dugar S. Response to Dobutamine in Septic Shock With Myocardial Dysfunction: A Single-Center Retrospective Study. Crit Care Explor. 2026;8(1):e03487. doi:10.1097/cce.0000000000001487
- [K3] Goyal A, Daneshpajouhnejad P, Bashir K. Acute Kidney Injury. StatPearls. 2026. PMID:28722925
