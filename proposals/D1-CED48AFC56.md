> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional episode-13 hypothesis: timing-anchored hypotension duration and subsequent AKI

## Proposed relationship

Among adults in a qualifying eICU ICU admission with at least one valid systolic blood-pressure measurement below 65 mmHg during ICU time 0–24 hours, greater cumulative time below 65 mmHg is associated with higher risk of a new or worsening creatinine-defined AKI event during the subsequent 24–72 hours, after accounting for baseline illness severity, prior vasopressor exposure, and hospital. Cumulative duration is expected to add reproducible information beyond the admission nadir alone.

This is an association hypothesis, not a causal claim that lowering blood pressure causes AKI or that 65 mmHg is a treatment target.

## Opening and unresolved question

A single nadir may be transient or artifact-prone, while sustained hypotension may represent a different exposure burden. The unresolved claim is whether duration adds reproducible information beyond nadir after explicit pre-exposure baseline anchoring and post-exposure outcome timing, rather than merely reflecting illness severity, treatment response, or measurement intensity. Resolving this could inform whether early AKI risk assessment should use duration/trajectory rather than a single minimum.

The inherited evidence motivates but does not establish this eICU association. It supports the relevance of time-weighted hypotension, the dynamic and heterogeneous nature of ICU AKI, and the importance of observation processes; it does not answer the local duration-versus-nadir question or validate local field semantics.

## Exact data binding (read-only)

Use the eICU snapshot and ordinary gzip CSV members listed in `datasets/eicu/README.md`. The primary joins are by documented eICU identifiers, without joining incompatible patient namespaces.

- `patient.csv.gz` / table `patient`: `patientunitstayid`, `patienthealthsystemstayid`, `gender`, `age`, `ethnicity`, `admissiontype`, `hospitalarrivaloffset`, `hospitaldischargestatus`, `intime`, `outtime`, and `hospitalid`.
- `vitalPeriodic.csv.gz` / table `vitalPeriodic` and `vitalAperiodic.csv.gz` / table `vitalAperiodic`: `patientunitstayid`, `charttime`, `systolicbp`, `diastolicbp`, `meanbp`, and `map` (use the documented columns after header inspection).
- `lab.csv.gz` / table `lab`: `patientunitstayid`, `charttime`, `testname`, `value`, `valueuom`, and `interpretation`; use creatinine rows after verifying the local test-name/unit semantics.
- `infusionDrug.csv.gz` / table `infusionDrug`: `patientunitstayid`, `charttime`, `medication`, `dosevalue`, `doseunit`, and documented start/stop fields; use only verified vasopressor rows for prior-exposure adjustment.
- `intakeOutput.csv.gz` / table `intakeOutput`: `patientunitstayid`, `charttime`, `intakeoutputname`, `intakeoutputvalue`, and `intakeoutputcategory`; treat urine-output ascertainment as secondary and gate it on semantic/timing validation.
- `hospital.csv.gz` / table `hospital`: `hospitalid` for hospital-held-out grouping.

All source files are read-only. Derived cohort and analysis files belong in the workspace.

## Population, time, variables, and outcome

Restrict to adults with a valid qualifying ICU stay and at least one valid systolic BP <65 mmHg in ICU time 0–24 hours. Define exposure as cumulative time below 65 mmHg in that window, with a prespecified interpolation/observation-density rule and sensitivity analysis for missingness and artifact-prone measurements. Define nadir as the minimum valid systolic BP in the same window.

Use a pre-exposure creatinine baseline when available, anchored before the exposure window or before the first qualifying hypotension measurement, and define the primary outcome as a new or worsening creatinine-defined AKI event during ICU time 24–72 hours. Preserve indeterminate/missing endpoint status rather than silently coding it as no event. Urine-output-based AKI is secondary and only used if local units, categories, and timing are verified.

Adjust for baseline severity, prior vasopressor exposure, and hospital; compare against a simple nadir-only baseline and a substantive time-aware alternative that can capture duration, trajectory, and observation intensity. Use hospital-held-out evaluation, uncertainty intervals, and prespecified artifact/observation-density sensitivities.

## Falsification and interpretation

Supportive results require a reproducible duration increment beyond nadir, with uncertainty and hospital-held-out consistency, and no explanation by measurement density or baseline severity alone. Adverse results include no increment, a reversed association, or failure under held-out hospitals/semantic checks. Inconclusive results include sparse BP/creatinine observations, unresolved urine semantics, unstable endpoint ascertainment, or wide intervals. None establishes causality, a treatment threshold, or clinical utility without adjudication and prospective validation.

## Missing evidence and limits

The local urine-output semantics and creatinine sampling adequacy remain to be confirmed by a bounded source-row/dictionary check. No computed effect is claimed in this provisional draft. The three inspected key works and frozen receipts are inherited from the parent branch and must be rechecked for claim mapping before final selection.
