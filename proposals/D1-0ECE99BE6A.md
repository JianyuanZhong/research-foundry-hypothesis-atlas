> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Repaired timing-anchored eICU hypotension-duration hypothesis

## Provisional hypothesis
Among adults in a qualifying eICU ICU admission with at least one valid systolic blood-pressure measurement below 65 mmHg during ICU time 0–24 hours, greater cumulative time below 65 mmHg is associated with higher risk of a new or worsening creatinine-defined AKI event during the subsequent 24–72 hours, after accounting for baseline illness severity, prior vasopressor exposure, and hospital. Cumulative duration is expected to add reproducible information beyond the admission nadir alone.

This is an association hypothesis, not a causal claim that lowering blood pressure causes AKI or that 65 mmHg is a treatment target.

## Evidence and unresolved question
The parent evidence supports the relevance of hypotension burden, the dynamic and heterogeneous nature of ICU AKI, and the importance of EHR observation processes, but does not establish this eICU association. [K1] inspected a perioperative cohort using time-weighted MAP <65 mmHg and found that waveform morphology did not improve AKI prediction beyond hypotension burden; it does not answer the eICU duration-versus-nadir question. [K2] describes ICU AKI as dynamic and heterogeneous, with creatinine-centered diagnosis necessary but insufficient and urine-output context important. [K3] addresses EHR missingness and observation-process effects on dynamic prediction. These works motivate the test but do not validate the local eICU fields or establish the proposed effect.

The most consequential uncertainty is endpoint timing and ascertainment. The primary outcome must be anchored to a pre-exposure creatinine baseline and measured after the exposure window, rather than allowing a post-exposure creatinine to define baseline. Urine output is a secondary endpoint only if its row semantics, timing, and availability are validated; otherwise it is unavailable rather than substituted for creatinine. No computed eICU effect estimate is claimed.

## Exact eICU bindings
Use only eICU rows and documented eICU identifiers; no cross-dataset identity matching is permitted. Source files are read-only and the exact archive members are the CSV.gz files named in the eICU README.

- `patient` (`patient.csv.gz`): `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `hospitalid`, `age`, `gender`, `unitadmittime24`, `unitdischargeoffset`, `unitdischargestatus`.
- `vitalPeriodic` (`vitalPeriodic.csv.gz`): `patientunitstayid`, `observationoffset`, `systemicsystolic`.
- `vitalAperiodic` (`vitalAperiodic.csv.gz`): `patientunitstayid`, `observationoffset`, `noninvasivesystolic`.
- `lab` (`lab.csv.gz`): `patientunitstayid`, `labresultoffset`, `labresultrevisedoffset`, `labname`, `labresult`, `labmeasurenamesystem`; select the verified creatinine item.
- `infusionDrug` (`infusionDrug.csv.gz`): `patientunitstayid`, `infusionoffset`, `drugname`, `drugrate`, `infusionrate`, `drugamount`; verify vasopressor labels before use.
- `intakeOutput` (`intakeOutput.csv.gz`): `patientunitstayid`, `intakeoutputoffset`, `intakeoutputentryoffset`, `outputtotal`, `celllabel`, `cellvaluenumeric`, `cellvaluetext`; use urine-output AKI only after semantic and timing validation.
- `hospital` (`hospital.csv.gz`): `hospitalid`, `numbedscategory`, `teachingstatus`, `region`; use for hospital-held-out evaluation.

Join longitudinal tables by `patientunitstayid`; join hospital context by `hospitalid`. Derived cohort, exposure, outcome, and analysis files belong in the branch workspace.

## Population, exposure, outcome, and analysis
Qualifying population: adults (`age >=18` at admission) in a single qualifying ICU admission with valid ICU start time and at least one valid systolic BP <65 mmHg in ICU time 0–24 hours. Exclude records lacking the required admission identifier or with impossible/ambiguous timestamps.

Exposure: derive valid systolic BP from both vital tables, cumulative minutes below 65 mmHg, nadir, and measurement counts in 0–24 hours. Use piecewise-linear interpolation between valid measurements, no extrapolation beyond first/last observed measurement, and prespecified physiologic-range filtering. Sensitivity analyses use no interpolation, shorter interpolation gaps, and measurement-count/observation-intensity adjustment.

Primary outcome: a creatinine-defined event in 24–72 hours. Define baseline as the last valid creatinine at or before ICU time 0 when available; if unavailable, use the first valid creatinine in a prespecified pre-exposure window and report missingness rather than imputing normal. Define the event as the earliest creatinine increase >=0.3 mg/dL from that baseline within 48 hours, or >=1.5 times baseline if the rise is documented within the outcome window, retaining time to event. Do not use a post-exposure creatinine as baseline. If the required pre-exposure baseline or outcome-window measurements are absent, classify the endpoint as unavailable/indeterminate rather than silently treating it as negative.

Secondary urine-output endpoint: retain only after a bounded semantic check of `intakeOutput` labels, numeric/text values, entry versus event offset, duplicate/cumulative behavior, and weight/availability. If semantics cannot be established, report urine-output AKI as unavailable rather than substitute a proxy.

The simple baseline is a prespecified hospital-stratified logistic model using nadir systolic BP in 0–24 hours, age, sex, baseline creatinine, and available baseline severity/vasopressor context. The substantive time-aware alternative adds cumulative hypotension minutes, time below threshold in prespecified intervals, last BP before window end, and a simple recovery/trajectory feature while retaining nadir. Evaluate both models on the same rows with a hospital-held-out split and the same outcome definition and uncertainty procedure. Report duration effect estimates and confidence intervals, calibration, and hospital-held-out discrimination as secondary descriptive outputs. A complex sequence model is deferred because the available data cannot distinguish hypotension-mediated kidney injury from severity, treatment, and observation artifacts; revisit only if a bounded diagnostic shows trajectory information is materially unavailable to the simpler representation.

## Falsification and interpretation
Supportive: duration adds reproducible information beyond nadir with a prespecified direction and uncertainty, and the result is not explained solely by observation density or a single hospital. Adverse: duration adds no information, reverses after prespecified adjustment, or is confined to artifact-prone measurements. Inconclusive: creatinine ascertainment, timestamp validity, or sampling is too sparse to estimate the comparison reliably; an imprecise null is not decisive refutation. Any causal interpretation, treatment threshold, or mechanism requires additional clinical adjudication, richer treatment/etiology data, and prospective or quasi-experimental evidence.

## Deliverable and limitations
The deliverable is a newly fitted baseline and time-aware analysis with a frozen cohort, explicit pre-exposure baseline and post-exposure event timing, uncertainty, hospital-held-out evaluation, and interpretation tied to computed outputs. No full study result has been computed in discovery. Clinical adjudication of AKI, reasons for missing measurements, interface interruptions, discharge/transfer, and end-of-life treatment limitations are not assumed available. The three attached works are inspected full-text sources with frozen receipts; no unavailable full text is claimed.
