> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional repaired hypothesis: hypotension duration and subsequent AKI in eICU

## Proposed relationship

Among adults in eICU who have at least one valid systolic blood-pressure measurement below 65 mmHg during the first 24 hours of a qualifying ICU stay, greater cumulative time below 65 mmHg is associated with a higher risk of new or worsening acute kidney injury during the next 48 hours, after accounting for baseline illness severity, prior vasopressor exposure, and hospital. The duration signal is expected to add reproducible information beyond the admission nadir alone. This is an association hypothesis, not a causal claim that lowering blood pressure causes AKI or that 65 mmHg is a treatment target.

## Clinical importance and unresolved question

A single nadir can be a transient or artifact-prone measurement, whereas sustained hypotension may represent a different exposure burden. The unresolved question is whether duration and trajectory add clinically meaningful information about subsequent AKI beyond the nadir, rather than merely reflecting severity, measurement frequency, or treatment response. Resolving this could inform whether early AKI risk assessment should use time-integrated blood pressure and whether prospective monitoring or resuscitation studies should target duration rather than a single minimum.

## Evidence status and opening

The inherited provisional candidate and expert seed identify a plausible duration-versus-nadir question, but neither supplies an effect estimate or verified eICU bindings. The dataset README confirms that eICU 2.0 includes patient, hospital, vitalPeriodic, vitalAperiodic, lab, infusionDrug, intakeOutput, and other longitudinal files, with source paths and hashes recorded in datasets/eicu/README.md. Direct inspection before the checkpoint confirmed the catalog schemas for patient, hospital, vitalPeriodic, and vitalAperiodic. The exact source headers and schemas for lab, infusionDrug, and intakeOutput remain to be verified; no claim is made that duration already predicts AKI.

## Prespecified data binding

Use only eICU rows and documented eICU identifiers. Candidate source tables are:

- patient (table-ab037c09d7df9a3c.json): patientunitstayid, patienthealthsystemstayid, age, gender, ethnicity, hospitalid, unittype, unitadmittime24, unitadmitoffset, unitvisitnumber, unitstaytype, admissionweight, unitdischargeoffset, unitdischargestatus, and uniquepid. The catalog schema was directly inspected.
- hospital (table-811df7b2ef435e12.json): hospitalid, numbedscategory, teachingstatus, and region. The catalog schema was directly inspected; hospitalid is the documented join key to patient.
- vitalPeriodic (table-a22c6d6981a32279.json): vitalperiodicid, patientunitstayid, observationoffset, systemicsystolic, systemicdiastolic, systemicmean, and other periodic vital fields. The catalog schema was directly inspected; patientunitstayid is the join key and observationoffset is the time field.
- vitalAperiodic (table-72ace5b89971196b.json): vitalaperiodicid, patientunitstayid, observationoffset, noninvasivesystolic, noninvasivediastolic, noninvasivemean, and other aperiodic vital fields. The catalog schema was directly inspected; patientunitstayid is the join key and observationoffset is the time field.
- lab (table-79bdb33275339b1a.json): timestamped creatinine values and identifiers needed to define baseline and post-exposure AKI. The exact header must be verified before execution.
- infusionDrug (table-18e1a8caaa91eb44.json): vasopressor/infusion timing and exposure context, subject to verified drug labels and timestamps. The exact header must be verified before execution.
- intakeOutput (table-ebba5dc91b1d37e7.json): urine-output records for a secondary KDIGO-compatible outcome, if its item labels and timestamps are verified. The exact header must be verified before execution.

The join key must be the documented eICU patient/admission identifier common to these tables; no cross-dataset identity matching is permitted. The source files are read-only and all derived cohort/exposure/outcome tables are written under the branch workspace.

## Population and temporal design

Qualifying population: adults (age >=18 at admission) in a single qualifying ICU admission with a valid documented ICU start time and at least one valid systolic BP <65 mmHg in the first 24 hours. Exclude records lacking the required admission identifier or with impossible/ambiguous timestamps. The primary exposure window is ICU time 0–24 hours; the primary outcome window is the subsequent 24–72 hours (48 hours after exposure-window end), avoiding outcome measurement before the exposure window is complete. A secondary analysis may use 0–48 hours for exposure and 48–96 hours for outcome if creatinine timing supports it, but this is not a post hoc replacement.

Define baseline as the last valid creatinine before or at ICU time 0 when available; otherwise use the first creatinine in a prespecified pre-exposure window, with missingness reported rather than silently imputed as normal. Define hypotension burden as cumulative minutes with systolic BP <65 mmHg in 0–24 hours using a prespecified interpolation rule: piecewise-linear interpolation between valid measurements, with no extrapolation beyond the first/last observed measurement. Report sensitivity analyses using no interpolation, a shorter interpolation gap, and a measurement-count/observation-intensity adjustment. Exclude or flag physiologically implausible values using a prespecified range and do not let a single artifact dominate the exposure.

Primary outcome: new or worsening AKI by KDIGO-compatible creatinine criteria, assessed from timestamped creatinine in 24–72 hours relative to ICU start: creatinine increase >=0.3 mg/dL within 48 hours from the prespecified baseline, or >=1.5 times baseline if the rise is documented within the outcome window. Use the earliest qualifying event and retain the time to event. A secondary outcome is urine-output AKI (urine output <0.5 mL/kg/h for >=6 hours or <0.3 mL/kg/h for >=12 hours) only if intakeOutput item semantics, weight, and timing are verified; otherwise report it as unavailable rather than substitute a proxy.

## Baseline versus time-aware alternative

Baseline model: a prespecified hospital-stratified logistic model (or cause-specific model if competing events are present) using nadir systolic BP in 0–24 hours, age, sex, baseline creatinine, and available baseline severity/vasopressor context. The same hospital-held-out split, outcome definition, and uncertainty procedure are used for both models.

Time-aware alternative: add cumulative hypotension minutes, time below threshold in prespecified intervals, last BP before window end, and a simple recovery/trajectory feature, while retaining the nadir. The alternative can reveal whether sustained exposure, recovery after the nadir, or observation density carries information that a single minimum discards. It is scientifically useful only if those features are stable and not merely proxies for measurement intensity or treatment; otherwise the baseline remains preferred.

Evaluate incremental association and uncertainty (confidence intervals), calibration, and hospital-held-out discrimination/calibration. Compare the two models on the same rows and report whether the duration coefficient and incremental predictive performance are directionally consistent across hospitals. A positive result supports incremental prognostic information, not causality. A null or reversed association is adverse to the duration hypothesis. Sparse creatinine, unstable BP interpolation, or non-reproducible hospital patterns make the result inconclusive.

## Falsification and interpretation

The hypothesis is supported if duration adds reproducible information beyond nadir with a prespecified direction and uncertainty, and the result is not explained solely by observation density or a single hospital. It is adverse if duration adds no information, reverses after prespecified adjustment, or is confined to artifact-prone measurements. It is inconclusive if AKI ascertainment, timestamp validity, or sampling is too sparse to estimate the comparison reliably. Any causal interpretation, treatment threshold, or mechanism requires additional clinical adjudication, richer treatment/etiology data, and prospective or quasi-experimental evidence.

## Scientific deliverable and alternatives not chosen

The actual deliverable is a newly fitted baseline and time-aware analysis with a frozen cohort, exposure/outcome timing, uncertainty, hospital-held-out evaluation, and an interpretation tied to computed outputs. A mechanistic model is deferred because the available data cannot distinguish hypotension-mediated kidney injury from severity, treatment, and observation artifacts. A complex sequence model is not selected over the simple time-aware feature model unless a bounded diagnostic shows that trajectory information is materially unavailable to the simpler representation; complexity alone is not a scientific criterion.
