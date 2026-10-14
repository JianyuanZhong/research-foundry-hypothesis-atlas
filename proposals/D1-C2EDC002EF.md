> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Robustness of time-weighted hypotension burden for early AKI: severity conditioning and solver deliverable

## Scientific question

Among adult ICU patients with adequate systolic and diastolic blood-pressure measurements in the first 24 hours of ICU care, does a prespecified time-weighted hypotension burden measure improve prediction of acute kidney injury (AKI) within 48 hours beyond the 24-hour mean arterial pressure (MAP), after controlling for baseline severity, vasopressor exposure, baseline kidney function, hospital, and measurement density, and after showing that the signal is robust to the choice of blood-pressure summary (MAP, systolic, diastolic)?

The unresolved claim is that duration and time-weighting of hypotension add clinically meaningful prognostic information beyond MAP, after accounting for baseline illness severity, vasopressor exposure, baseline kidney function, hospital, and measurement density. The strongest rival is that the apparent burden signal is an artifact of recording density, measurement timing, or baseline illness severity, or that it is specific to one arbitrary choice of blood-pressure summary. A null result would weaken the claim that a more complex burden measure is useful; a positive result would support further validation and prospective study.

## Why it matters

MAP is the common bedside summary and a natural baseline for hemodynamic risk. Minimum systolic blood pressure alone can overstate a single low reading, while MAP may understate sustained hypoperfusion. If time-weighted burden improves early AKI risk stratification, it may inform monitoring and resuscitation decisions. If it does not, clinicians and researchers should not add a more complex measure without evidence.

## Prior evidence

- [K1] The eICU 2.0 data dictionary provides the source files and table metadata for the study population, vital signs, laboratory values, and infusions. It supports the feasibility of the exact data bindings but does not establish the prognostic value of burden.
- [K2] Kellum et al. (2016) describe the eICU-CRD dataset and its multi-center ICU population, supporting the use of eICU for a transportable prognostic analysis but not the specific burden question.
- [K3] Wu et al. (2015) provide a clinical context for AKI as a consequential ICU outcome and the need for early risk stratification, but do not test time-weighted hypotension burden.

## Population and temporal design

Use eICU 2.0 adult ICU admissions with at least one systolic and one diastolic blood-pressure measurement in the first 24 hours after ICU admission. Exclude patients with missing ICU admission time, missing AKI outcome, or fewer than 5 blood-pressure measurements in the first 24 hours. Define the exposure window as 0–24 hours after ICU admission and the outcome window as 24–72 hours after ICU admission (AKI within 48 hours after the exposure window).

## Variables and definitions

- Blood pressure: systolic and diastolic measurements from the vital table, with timestamps. Compute MAP = (systolic + 2*diastolic)/3 for each measurement.
- Hypotension burden: prespecified time-weighted fraction of the first 24 hours during which MAP < 65 mmHg, using linear interpolation between measurements and censored at the last measurement.
- Baseline severity: APACHE IV score from the patient table, with SOFA score as a fallback if APACHE IV is missing.
- Vasopressors: presence and duration of norepinephrine infusion from the infusion table in the first 24 hours.
- Baseline kidney function: first creatinine measurement in the first 24 hours.
- AKI outcome: KDIGO stage 1–3 AKI defined by creatinine and urine output criteria in the 24–72 hour window.
- Hospital: hospital identifier from the patient table.
- Measurement density: number of blood-pressure measurements per hour in the first 24 hours.

## Analysis

1. Fit a logistic regression baseline with MAP (24-hour mean) and covariates (severity, vasopressors, baseline creatinine, hospital, measurement density).
2. Fit a logistic regression alternative with time-weighted hypotension burden and the same covariates.
3. Compare AUC, calibration (Brier score, calibration-in-the-large, calibration-slope), and likelihood ratio test.
4. Repeat the analysis using systolic and diastolic summaries and a combined summary to test robustness to blood-pressure summary choice.
5. Stratify by severity (APACHE IV quartiles) and test for interaction.
6. Perform a missing-severity sensitivity analysis using SOFA fallback.
7. Report hospital-level analysis and measurement-density sensitivity analysis.

## Falsification criteria

- The burden signal is falsified if the burden coefficient is null or negative after adjustment for severity, vasopressors, baseline creatinine, hospital, and measurement density.
- The burden signal is falsified if it is not robust to the choice of blood-pressure summary (MAP, systolic, diastolic, combined).
- The burden signal is falsified if it is driven by a single hospital or by measurement density.
- The burden signal is inconclusive if the confidence interval for the burden coefficient includes both null and clinically meaningful effects, or if the number of AKI events is insufficient for stable estimation.

## Solver deliverable

The solver must fit both the MAP baseline and the burden alternative, report the model coefficients with 95% confidence intervals, AUC, Brier score, calibration-in-the-large, calibration-slope, and hospital-level analysis. The solver must also report the severity stratum analysis and the missing-severity sensitivity analysis. The solver must not claim clinical causality from the observational analysis.

## Limitations

- eICU is a retrospective, multi-center dataset with irregular blood-pressure recording.
- AKI is defined by creatinine and urine output, which may be affected by fluid balance and diuretic use.
- The analysis is prognostic, not causal. A positive result would support further validation and prospective study, not immediate clinical adoption.
