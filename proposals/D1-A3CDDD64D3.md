> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Does laboratory surveillance dependence reach a downstream renal-escalation signal?

## Scientific deliverable and substantive advance

The future solver must newly construct one leakage-safe eICU six-hour stay ledger and estimate whether laboratory-observation behavior changes a downstream, clinically more consequential recorded renal-escalation process after general vital-surveillance intensity is represented. The primary deliverable is:

1. the standardized hospital 90th-minus-10th percentile spread in the 48-hour cumulative incidence of a strict renal-escalation composite after a first qualifying recorded creatinine rise;
2. its decomposition into a distinct later recorded creatinine confirmation and a newly documented high-specificity renal-support record;
3. the fraction of that spread explained by repeat-test opportunity, early laboratory process, vital-monitoring process and competing ICU exits; and
4. a matched ordered multi-state estimate showing whether hospital variation occurs in testing opportunity, confirmation, support documentation or exit.

The composite is intentionally a downstream endpoint for the incumbent's surveillance question. It is closer to a consequential renal-care decision than the incumbent's expired-unit-exit threshold crossing, while remaining observable and falsifiable in this database. The incumbent's B0/BV/BL/BLV 10% decision contrasts remain required secondary outputs, so the child does not discard the laboratory-versus-vital comparison.

Completion requires a frozen ledger, two fitted model families, hospital-standardized CIFs and uncertainty intervals for the composite and both components, held-out-hospital transport, and falsification outputs. No result is claimed here.

## Evidence-supported claim, unresolved hypothesis and importance

The inspected evidence supports only data availability and feasibility. The frozen eICU 2.0 snapshot has ICU-relative laboratory, periodic-vital, treatment and intake/output records; unit disposition and hospital identifiers; and admission severity fields. Direct schemas expose the exact keys and times below. A read-only scan of the configured treatment.csv.gz found 3,688,745 rows, 1,107,493 rows at offsets 360–2880, and 10,561 rows whose strings contained a dialysis/CRRT/hemofiltration/renal-replacement term. This is a source feasibility count, not a cohort event rate and not evidence of treatment initiation. The intake/output schema exposes dialysis totals and cell labels, but no uniformly valid collection interval or treatment-intent field.

The unresolved claim is:

> Among adult ICU stays with a valid six-hour pre-rise risk set, does hospital variation in laboratory surveillance predict a materially different 48-hour probability of a downstream recorded renal-escalation event after measured case mix, early physiologic state, vital-surveillance intensity, repeat-test opportunity and competing ICU exits are represented, and does that variation transport to held-out hospitals?

Primary hypothesis: the supported-hospital standardized renal-escalation CIF has an H90–10 spread of at least 5 percentage points, with a two-sided hospital-cluster interval excluding zero, and at least half of the unadjusted spread remains after repeat-test opportunity and exit processes are included. This is a prespecified scale for portability of a recorded clinical process, not a treatment threshold or patient benefit.

A supportive result would mean that laboratory surveillance dependence reaches an endpoint more consequential than repeated measurement alone. It could justify site-specific calibration or a warning that a renal-risk model is partly a local documentation policy. It would not establish AKI, dialysis initiation, treatment response, hospital quality, or a causal effect of testing.

## Population, index rise and temporal boundary

Use each patientunitstayid as one ICU-stay observation; never concatenate later stays. Include adults with patient.age >= 18, parsing age > 89 as 90 and retaining an age-censored flag. Require patient.unitdischargeoffset > 360. The landmark is ICU minute 360. Every predictor and exposure must use a source time <=360 and also strictly before unit discharge.

Require at least two valid vitalPeriodic.systemicmean observations in 0–360, each restricted to 20–200 mmHg; a numeric baseline creatinine in 0–60 with the development-frozen accepted measurement-system/interface pair; an index recorded rise by minute 360, defined as the first same-pair creatinine after baseline at least 0.3 mg/dL above baseline; no qualifying strict renal-support record at or before minute 360; and no qualifying baseline-plus-0.3 rise before the index rise.

If the development-only audit cannot verify an adequately supported mg/dL pair, the biological-threshold index-rise branch is infeasible and must not be silently replaced. Preserve the incumbent's documented-exit secondary. A broad numerical-unit branch is a labelled sensitivity only and cannot support the primary clinical interpretation.

For each stay let U = unitdischargeoffset and E = min(2880,U). Source events are eligible only at times t < U; if U >2880, an event at exactly 2880 is eligible, and if U <=2880 an exit at U precedes an event at that same minute. unitdischargestatus=Expired is a documented expired ICU-unit exit and Alive is an alive unit exit. NULL or another status is unknown-status censoring, never alive. hospitaldischargeoffset is never used for the ICU endpoint.

## Outcome and renal-support definition

The risk clock starts at the first qualifying recorded rise, but the primary outcome window begins at minute 360 and ends at E. The strict composite is the first of:

1. Recorded confirmation: a distinct later labid, at least 360 minutes after the index-rise offset, with the same development-frozen measurement pair and numeric creatinine at least baseline+0.3 mg/dL. A duplicate labid, same-minute row, or revised version of that labid cannot confirm. The primary time is labresultoffset; labresultrevisedoffset is a sensitivity.
2. Newly documented renal support: the first post-360, pre-exit, high-specificity renal-support record from treatment or intakeOutput. Strict treatment matches are case-folded modality strings containing renal dialysis/hemodialysis, CRRT/CVVH/CVVHD/CVVHDF, hemofiltration, peritoneal dialysis or SLED. Exclude catheter insertion, access surgery, hyperkalemia-treatment text without a modality, and fluid-removal-only ultrafiltration. Strict intake/output matches are modality-specific dialysis/CRRT/hemofiltration labels or nonblank numeric dialysistotal, with exact label rules frozen before outcome analysis. A row is called newly documented, not initiated or administered.

Deduplicate exact labid, treatmentid and intakeoutputid. If both components occur at one minute, retain both indicators and count one composite event. Retain an ordered ledger for no rise, index rise, repeat-test opportunity, confirmation, renal-support documentation, expired exit, alive exit and unknown-status censoring.

The renal-support component is not a validated dialysis-initiation endpoint. Treatment rows lack administration, dose, indication and intent. Intake/output labels lack uniformly reliable interval, denominator and collection semantics. Urine-labelled rows are observation-process audit only; no oliguria or KDIGO claim is permitted. Broad support, treatment-only and intake/output-only definitions are sensitivities. If strict support is too sparse, the composite cannot be promoted to a clinically consequential conclusion; report confirmation and the incumbent secondary instead.

## Predictors and process exposure

Construct the incumbent's exact clinical block C from patient demographics/admission fields, admission severity and 0–360 lab/vital values: case-folded exact analytes creatinine, BUN, sodium, potassium, chloride, glucose, lactate, WBC, hemoglobin, hematocrit, bilirubin and albumin; six summaries (median, minimum, maximum, IQR, last and slope) for accepted lab values and the five incumbent periodic vital channels temperature, sao2, heartrate, respiration and systemicmean. Keep actual* fields and all discharge fields out of predictors. Development medians, scaling and accepted pairs are frozen within development only.

The laboratory-process block L uses no lab values: total/numeric rows, distinct analytes, panel presence, counts in [0,120] and (120,360], first/last offset, median gap over distinct offsets, explicit measurement-pair fraction, and revised-row count. The vital-process block V uses deduplicated valid vitalPeriodic metadata: row and distinct-offset counts, occupied half-hour bins, first/last offset, median gap, bin coverage and per-channel observation indicators. L and V are process proxies, not interventions or negative controls.

Add post-rise opportunity variables only for renal-outcome analysis: time to first post-360 creatinine opportunity, repeat-test indicator within six hours, number of eligible pre-rise creatinine rows, and urine-observability counts/coverage as audit or adjustment variables. No post-rise lab value or post-landmark treatment record may become a predictor.

## Primary estimand and retained parent estimand

For every supported development hospital h, estimate the cause-specific competing-risk CIF q_h_RE for the strict composite from the first qualifying rise through E, with expired and alive unit exits as competing events and unknown-status stays censored. Standardize each hospital to the development risk-set distribution of case mix, first-rise characteristics, early MAP history, L/V process, repeat-test opportunity and hospital context (numbedscategory, teachingstatus, region), without making hospital identity an individual predictor. Use only hospitals with at least 50 first-rise stays and 10 strict composite events for a hospital-specific estimand. Define H90-10_RE = Q90(q_h_RE)-Q10(q_h_RE) and report the same quantity for confirmation, renal-support documentation, repeat-test opportunity and each exit.

The process decomposition compares raw H90–10; after B0 state standardization; after adding L and V; after adding repeat-test opportunity and urine-observability audit terms; and the residual spread in the ordered multi-state model.

The parent’s exact secondary estimands are mandatory: B0/BV/BL/BLV decision curves at q=0.10, with 0.05 and 0.20 sensitivities; NB(BLV)-NB(BV) conditional on V; development-to-held-out transport penalty; threshold crossing-in/out composition; and expired-versus-alive endpoint-specificity comparison.

## Matched transparent baseline

Fit regularized additive cause-specific pooled-logistic models on identical stays, splits and feature preprocessing, using 30-minute intervals and transition-specific elapsed-time terms. Fit nested versions:

- B0: measured state, first-rise characteristics and elapsed time;
- B1: B0 plus transition-specific hospital random intercepts;
- B2: B1 plus hospital context;
- B3: B1 plus L, V and repeat-test opportunity;
- B4: B3 plus urine-observability audit terms; and
- B5: B3 without hospital-by-time slopes as a stability/null-heterogeneity reference.

Use the same models to obtain standardized composite and component CIFs, calibration, Brier/log loss, observed/predicted events and the incumbent's threshold decisions. Patient post-rise results are outcomes, never predictors.

## Substantive temporal/mechanistic alternative

Fit an ordered piecewise-exponential multi-state model on the same 30-minute ledger, risk sets, covariates, split, standardization distribution and bootstrap procedure. States are first rise, repeat-test opportunity, confirmation, renal-support documentation, composite renal escalation, expired exit, alive exit and unknown-status censoring. Keep confirmation and support transitions separate, enforce the six-hour confirmation delay structurally, and use shrunk transition-specific hospital effects. Its key output is whether H90–10 is carried by repeat-test opportunity, confirmation after opportunity, independent support documentation or exit.

The additive baseline is selected for auditability and algebraic decision decomposition; it loses event ordering and cannot distinguish opportunity from confirmation from support. The multi-state model is required because an apparent downstream renal endpoint could arise from surveillance, a state trajectory or local support documentation. Agreement across models is robustness, not proof of biology. A learned temporal model is deferred unless both models show reproducible held-out shape-specific miscalibration and a learned representation can preserve component transitions and hospital-held-out estimation. This is a scientific deferral, not a neural-network or GPU prohibition.

## Split, transport and uncertainty

Construct hospital connected components from any shared uniquepid in patient; assign each component by SHA-256 of eicu-renal-escalation-v1 + NUL + sorted hospital IDs, modulo 100, with buckets 0–79 development and 80–99 held out. Perform this before accepted-pair selection, process quantiles, imputation, fitting or standardization. No patient, hospital component or uniquepid crosses the outer split. Use five deterministic development hospital folds for out-of-fold predictions and a second namespace as a stability sensitivity. Do not tune or recalibrate held-out hospitals.

Use 500 whole-hospital bootstrap replicates for H90–10, component spreads, model differences and the incumbent decision contrasts; add a uniquepid cluster sensitivity. Report supported hospitals, event counts, overlap, effective sample size, convergence, calibration and random-effect shrinkage. Transport is inconclusive with fewer than 10 held-out hospitals, fewer than 25 strict composite events or inadequate timing/support overlap.

## Falsification and result interpretation

Run outcome permutations within hospital, ordinary within-hospital process permutations, and a stratified L swap within development-frozen B0-risk and V-intensity strata. The conditional laboratory decision contribution should collapse under the swap; persistence indicates leakage, join error or unrecognised state in L. Reverse 12 half-hour process-bin order in the temporal model while holding values and outcomes fixed; a large unchanged process gain suggests a static data-density/site proxy. Repeat with revision-conservative versus revision-ignored lab clocks, exact ID deduplication, vitalAperiodic MAP, strict versus broad support, treatment-only versus intake/output-only support, prior-support exclusion, and unit-boundary/unknown-status rules. Report raw event and action rates, crossings, calibration and hospital concentration.

Label results supportive only if H90–10_RE >=0.05 with a two-sided hospital-cluster interval excluding zero, at least half the raw spread remains after opportunity/exit adjustment, the strict support component has adequate support, both matched models agree qualitatively, the finding transports to held-out hospitals, and channel/split/clock sensitivities are stable. These are deployment-portability criteria, not clinical-effect thresholds.

Label the new hypothesis adverse if the composite spread is null or reversed, disappears after opportunity/exit adjustment, exists only under broad unvalidated labels, or fails transport while falsifications behave as expected. A large confirmation spread with no support spread means the recorded signal is not shown to reach documented renal care. A large support-only spread means support documentation is site-dependent, not that renal therapy differs in initiation or benefit.

Label inconclusive for sparse support, fewer than 10 supported hospitals, weak overlap, interval crossing both zero and the margin, model nonconvergence, poor held-out calibration, treatment/flowsheet disagreement, material clock sensitivity or endpoint dependence on unknown-status handling. Inconclusive is not evidence for or against intervention.

Computationally checkable claims include source/header/schema hashes, joins, offsets, deduplication, no-leakage ledger, split integrity, endpoint construction, model fits, CIFs, standardization, uncertainty and sensitivity outputs. Clinical adjudication or another study is required for biological AKI, chronic-versus-new dialysis, actual initiation/administration, clinician intent, assay comparability, urine-output meaning, treatment harm/benefit or policy change. No causal MAP/pressor, mortality, quality-ranking or treatment claim is licensed.

## Exact read-only data bindings and provenance

Catalog: [internal dataset path], [source checksum]. eICU snapshot: [source checksum]. All listed members are ordinary read-only .csv.gz files; there is no nested archive member.

- patient: [internal dataset path] 2.0 data/patient.csv.gz; SHA [source checksum]; table patient; schema datasets/eicu/table-ab037c09d7df9a3c.json, SHA [source checksum]. Join patientunitstayid; use age, gender, ethnicity, hospitalid, hospitaladmitsource, admissionweight, unittype, unitvisitnumber, unitdischargeoffset, unitdischargestatus, unitdischargelocation, uniquepid.
- lab: [internal dataset path] 2.0 data/lab.csv.gz; SHA [source checksum]; table lab; schema datasets/eicu/table-79bdb33275339b1a.json, SHA [source checksum]. Join patientunitstayid; use labid, labresultoffset, labtypeid, labname, labresult, labresulttext only for audit, labmeasurenamesystem, labmeasurenameinterface, labresultrevisedoffset.
- vitalPeriodic: [internal dataset path] 2.0 data/vitalPeriodic.csv.gz; SHA [source checksum]; table vitalPeriodic; schema datasets/eicu/table-a22c6d6981a32279.json, SHA [source checksum]. Join patientunitstayid; use vitalperiodicid, observationoffset, temperature, sao2, heartrate, respiration, systemicmean.
- vitalAperiodic sensitivity: [internal dataset path] 2.0 data/vitalAperiodic.csv.gz; SHA [source checksum]; table vitalAperiodic; schema datasets/eicu/table-72ace5b89971196b.json, SHA [source checksum]. Use vitalaperiodicid, observationoffset, noninvasivemean.
- apachePatientResult: [internal dataset path] 2.0 data/apachePatientResult.csv.gz; SHA [source checksum]; table apachePatientResult; schema datasets/eicu/table-754bebf64d3d9909.json, SHA [source checksum]. Join patientunitstayid; use acutephysiologyscore, apachescore, predictedicumortality, predictediculos; reject every actual* field.
- hospital: [internal dataset path] 2.0data/hospital.csv.gz; SHA [source checksum]; table hospital; schema datasets/eicu/table-811df7b2ef435e12.json, SHA [source checksum]. Join hospitalid; use numbedscategory, teachingstatus, region only for context/splits.
- treatment: [internal dataset path] 2.0 data/treatment.csv.gz; SHA [source checksum]; table treatment; schema datasets/eicu/table-5461361964176606.json, SHA [source checksum]. Join patientunitstayid; use treatmentid, treatmentoffset, treatmentstring, activeupondischarge; source timing only.
- intakeOutput: [internal dataset path] 2.0 data/intakeOutput.csv.gz; SHA [source checksum]; table intakeOutput; schema datasets/eicu/table-ebba5dc91b1d37e7.json, SHA [source checksum]. Join patientunitstayid; use intakeoutputid, intakeoutputoffset, intakeoutputentryoffset, dialysistotal, cellpath, celllabel, cellvaluenumeric, cellvaluetext only under strict label rules.

The full catalog contains 31 eICU tables. Notes, diagnoses, medications, nurse charting and other tables are not silently used as substitutes for renal adjudication. Sources remain read-only; ledgers, fits and derived reports belong in the workspace.

## Compute and retained alternatives

Discovery compute is limited to 7,200 science seconds and two concurrent jobs. The future solver envelope in inputs.json is 16 CPUs, 262,144 MiB RAM, up to eight A100-SXM4 80-GB GPUs and 28,800 seconds. The treatment scan was measured at 11.8 seconds on four CPUs; full ledger construction, hierarchical fits, temporal fits and 500 refits are unmeasured. CPU-first is appropriate for these tabular/multi-state fits; GPU is optional after allocated profiling and must use cuda:0. Long runs checkpoint the ledger, splits and predictions.

The learned sequence branch is deferred pending reproducible held-out shape-specific miscalibration and preservation of the same transition decomposition. Urine/KDIGO is deferred for missing interval and denominator semantics. Causal pressor analysis is deferred because infusionDrug lacks validated administration, dose, indication and intent. These are revisit conditions, not blanket method exclusions.
