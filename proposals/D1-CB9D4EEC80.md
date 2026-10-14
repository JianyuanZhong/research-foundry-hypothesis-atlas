> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Time-weighted hypotension burden and subsequent acute kidney injury in eICU

## Scientific question

Among adult ICU patients with periodic or aperiodic systolic blood pressure measurements, does a prespecified early-ICU hypotension burden measure predict subsequent acute kidney injury (AKI) better than the minimum systolic blood pressure alone?

The unresolved claim is that duration and time-weighting of hypotension add prognostic information beyond the nadir, after accounting for baseline illness severity, vasopressor exposure, kidney function at baseline, and hospital. A null result would weaken the claim that duration is clinically useful; a positive result would support further validation and prospective study.

## Why it matters

Minimum systolic blood pressure is a common bedside summary, but it can understate sustained hypoperfusion. If time-weighted burden improves early AKI risk stratification, it may inform monitoring and resuscitation decisions. If it does not, clinicians and researchers should not add a more complex measure without evidence.

## Population and temporal design

Use eICU 2.0 adult ICU admissions with at least one systolic blood pressure measurement in the first 24 hours after ICU admission and at least one creatinine measurement before or within the early window. Exclude patients whose ICU admission is not the first admission in the dataset when a repeat-admission rule is needed; document the exact rule in the solver.

Define the exposure window as the first 24 hours after ICU admission. Define subsequent AKI using a prespecified creatinine-based rule over the next 72 hours, for example KDIGO-style creatinine increase from the lowest pre-window or early baseline value, with the exact threshold fixed before fitting. If creatinine measurements are sparse, report sensitivity analyses using available measurements and label the result inconclusive rather than imputing a continuous renal trajectory.

## Variables and exact bindings

- `patient.csv.gz`: adult age and sex; patient identifier and ICU admission linkage.
- `hospital.csv.gz`: hospital identifier for within-hospital and held-out-hospital analysis.
- `admissionDx.csv.gz` and `diagnosis.csv.gz`: admission diagnoses and ICU diagnoses for baseline illness context.
- `vitalPeriodic.csv.gz` and `vitalAperiodic.csv.gz`: systolic blood pressure, measurement timestamp, and patient/admission keys.
- `infusionDrug.csv.gz`: vasopressor exposure during the exposure window.
- `lab.csv.gz`: creatinine and other renal function measurements with timestamps.
- `apachePatientResult.csv.gz` and `apacheApsVar.csv.gz`: baseline severity variables if available for the admission.

Join on the documented patient/admission identifiers only within eICU. Preserve source-specific identifiers; do not join across HCC or MIMIC.

## Estimand and analysis

Primary estimand: the association between time-weighted hypotension burden during the first 24 hours and the probability of subsequent AKI, adjusted for baseline age, sex, admission severity, baseline creatinine, vasopressor exposure, and hospital.

Define hypotension burden as the fraction of the exposure window with systolic BP below a prespecified threshold, using interpolation or a prespecified last-observation-carried-forward rule only after checking measurement density. Also report the duration below threshold and the minimum BP. Compare:

1. Baseline: adjusted logistic regression using minimum systolic BP and standard covariates.
2. Time-aware alternative: a gradient-boosted or sequence-aware model using timestamped BP values and covariates, or a mechanistic time-weighted summary if sequence modeling is not feasible.

Use hospital-held-out validation where feasible, with calibration, Brier score, and AUROC. A simple adjusted model is the baseline; the learned alternative is justified only if it reveals timing or nonlinear patterns that summaries lose.

## Falsification and interpretation

Supportive: the burden measure has a positive adjusted association, improves held-out calibration or AUROC, and is consistent across multiple hospitals.

Adverse: burden adds no predictive value, worsens calibration, or is confined to a small number of hospitals.

Inconclusive: sparse BP or creatinine measurements, large missingness, or unstable hospital-held-out estimates. These findings would require denser data or a prospective study.

## Limitations

eICU records may have heterogeneous measurement density and artifact. Vasopressor exposure is an adjustment, not proof of adequate resuscitation. The analysis is observational and cannot establish that changing BP targets causes AKI.
