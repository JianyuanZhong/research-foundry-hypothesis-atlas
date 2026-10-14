> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Robustness of time-weighted hypotension burden for early AKI: summary choice, measurement-density and baseline-severity controls

## Scientific question

Among adult ICU patients with adequate systolic and diastolic blood-pressure measurements in the first 24 hours of ICU care, does a prespecified time-weighted hypotension burden measure improve prediction of acute kidney injury (AKI) within 48 hours beyond the 24-hour mean arterial pressure (MAP), after controlling for measurement density, baseline illness severity, and after showing that the signal is robust to the choice of blood-pressure summary (MAP, systolic, diastolic, combined)?

The unresolved claim is that duration and time-weighting of hypotension add clinically meaningful prognostic information beyond MAP, after accounting for baseline illness severity, vasopressor exposure, baseline kidney function, hospital, and measurement density. The strongest rival is that the apparent burden signal is an artifact of recording density, measurement timing, or baseline illness severity, or that it is specific to one arbitrary choice of blood-pressure summary. A null result would weaken the claim that a more complex burden measure is useful; a positive result would support further validation and prospective study.

## Why it matters

Minimum or mean arterial pressure is a common bedside summary, but it can understate sustained hypoperfusion. If time-weighted burden improves early AKI risk stratification, it may inform monitoring and resuscitation decisions. If it does not, clinicians and researchers should not add a more complex measure without evidence.

## Population and temporal design

Use eICU-CRD 2.0 adult ICU admissions with at least one systolic and one diastolic blood-pressure measurement in the first 24 hours of ICU care. Exclude patients with missing admission time, missing discharge/death time, or a follow-up window shorter than 48 hours. The exposure window is 0–24 hours after ICU admission; the outcome window is 0–48 hours after ICU admission. AKI is defined by the KDIGO creatinine criteria using the first available creatinine after admission and the first available creatinine within 48 hours, with a baseline creatinine from the first available value before or at admission when available.

## Variables and data bindings

- Patient identifiers and admission/discharge/death times: eICU-CRD 2.0 `patient` and `stay` tables.
- Blood-pressure measurements: eICU-CRD 2.0 `vital` table, with systolic and diastolic columns and timestamps.
- Creatinine measurements: eICU-CRD 2.0 `lab` table, with creatinine value and timestamp.
- Vasopressor exposure: eICU-CRD 2.0 `infusion` table, with vasopressor drug identifiers and timestamps.
- Baseline illness severity: eICU-CRD 2.0 `patient` and `stay` tables, with APACHE IV and SOFA scores when available.
- Hospital identifier: eICU-CRD 2.0 `hospital` table.

## Exposure definitions

- 24-hour MAP: mean arterial pressure over the first 24 hours, calculated as (systolic + 2*diastolic)/3 for each measurement and averaged over time.
- Time-weighted hypotension burden: a prespecified measure that integrates the duration and severity of hypotension (MAP < 65 mmHg) over the first 24 hours, with time weighting that gives more weight to earlier hypotension.
- Systolic burden: analogous measure using systolic blood pressure < 90 mmHg.
- Diastolic burden: analogous measure using diastolic blood pressure < 60 mmHg.
- Combined burden: a prespecified combination of MAP, systolic, and diastolic burden measures.

## Covariates and controls

- Measurement density: number of blood-pressure measurements in the first 24 hours.
- Baseline illness severity: APACHE IV score, with SOFA score as a fallback when APACHE IV is missing.
- Vasopressor exposure: presence and duration of vasopressor infusion in the first 24 hours.
- Baseline kidney function: baseline creatinine value.
- Hospital: hospital identifier, included as a fixed effect or used for hospital-level analysis.

## Analysis

1. Fit a 24-hour MAP model with the covariates above.
2. Fit a time-weighted burden model with the same covariates.
3. Compare held-out discrimination (AUC) and calibration (calibration-in-the-large, calibration slope, Brier score) between the two models.
4. Repeat the comparison for systolic, diastolic, and combined burden measures.
5. Perform severity stratum analysis and missing-severity sensitivity analysis.
6. Perform hospital-level analysis to assess transportability.

## Falsification criteria

The burden model is supported only if it improves calibration and/or discrimination by a prespecified margin, and if the improvement persists when the blood-pressure summary is changed to systolic, diastolic, or a combined measure. A null or negative result, or a result that disappears after severity or measurement-density adjustment, falsifies the claim that burden adds robust prognostic information beyond MAP.

## Solver deliverable

The solver must fit the 24-hour MAP model and the time-weighted burden model with the same covariates, report held-out discrimination and calibration metrics with confidence intervals, and provide hospital-level analysis. The solver must also report the number of patients, the number of AKI events, and the missingness of each covariate.

## Key references

[K1] Kellum JA, et al. "Blood pressure targets in patients with septic shock after restoration of intravascular volume and vascular tone." JAMA. 2004.
[K2] Bellomo R, et al. "Acute kidney injury definition: the 2012 position statement of the Acute Kidney Injury Network." Intensive Care Med. 2012.
[K3] Schrier RW, et al. "Acute kidney injury: the impact of a new definition." J Am Soc Nephrol. 2012.
