> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional checkpoint: timing-anchored eICU hypotension duration

## Proposed relationship
Among adults in qualifying eICU ICU admissions with at least one valid systolic BP below 65 mmHg during ICU time 0–24 hours, greater cumulative time below 65 mmHg is associated with higher risk of a new or worsening creatinine-defined AKI event during the subsequent 24–72 hours, after accounting for baseline illness severity, prior vasopressor exposure, and hospital. Cumulative duration is expected to add reproducible information beyond the admission nadir alone. This is an association hypothesis, not a causal claim that lowering BP causes AKI or that 65 mmHg is a treatment target.

## Concrete supporting observations and exact source locations
The inherited parent identifies three inspected works that motivate, but do not establish, this question:
- [K1] inspected a perioperative cohort using time-weighted MAP <65 mmHg and found waveform morphology did not improve AKI prediction beyond hypotension burden; it does not answer the eICU duration-versus-nadir question.
- [K2] describes ICU AKI as dynamic and heterogeneous, with creatinine-centered diagnosis necessary but insufficient and urine-output context important.
- [K3] addresses EHR missingness and observation-process effects on dynamic prediction.
The parent explicitly states that these works do not validate the local eICU fields or establish the proposed effect. The exact source IDs for the required frozen evidence are [source checksum], [source checksum], and [source checksum]; their exact passages and receipts still require inspection before the final bundle.

## Uncertainties and missing evidence
No computed eICU effect estimate is claimed. The main uncertainty is endpoint timing and ascertainment: baseline creatinine must be pre-exposure, the event must be post-exposure in 24–72 hours, and unavailable measurements must remain indeterminate. Urine-output AKI is secondary and unavailable unless row semantics, timing, duplicates, and availability are validated. Clinical adjudication of AKI, missing measurements, interface interruptions, discharge/transfer, and end-of-life treatment limitations is not assumed available.

## Falsifiable test
Compare a prespecified hospital-stratified logistic baseline using nadir systolic BP, age, sex, baseline creatinine, and baseline severity/vasopressor context with a time-aware model adding cumulative hypotension minutes, interval-specific burden, last BP, and recovery/trajectory features. Use the same rows, pre-exposure baseline, post-exposure outcome, hospital-held-out split, uncertainty procedure, and prespecified falsification checks. Support requires reproducible duration information beyond nadir with uncertainty and not solely observation density or one hospital; adverse results include no added information, reversal, or artifact confinement; sparse or invalid ascertainment is inconclusive rather than decisive refutation.

## Exact data bindings
Use only eICU rows and documented eICU identifiers, with read-only source files: patient.csv.gz (patientunitstayid, patienthealthsystemstayid, uniquepid, hospitalid, age, gender, unitadmittime24, unitdischargeoffset, unitdischargestatus), vitalPeriodic.csv.gz (patientunitstayid, observationoffset, systemicsystolic), vitalAperiodic.csv.gz (patientunitstayid, observationoffset, noninvasivesystolic), lab.csv.gz (patientunitstayid, labresultoffset, labresultrevisedoffset, labname, labresult, labmeasurenamesystem), infusionDrug.csv.gz (patientunitstayid, infusionoffset, drugname, drugrate, infusionrate, drugamount), intakeOutput.csv.gz (patientunitstayid, intakeoutputoffset, intakeoutputentryoffset, outputtotal, celllabel, cellvaluenumeric, cellvaluetext), and hospital.csv.gz (hospitalid, numbedscategory, teachingstatus, region). Join longitudinal tables by patientunitstayid and hospital context by hospitalid; derived files belong in this branch.
