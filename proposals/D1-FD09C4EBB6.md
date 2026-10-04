# Selection-robust metabolic discordance and competing failure after first ICU discharge

## Scientific deliverable

The future solver must newly construct and fit an auditable, leakage-safe MIMIC-IV 3.1 study asking whether a repeated lactate pattern at the first ICU discharge is a decision-relevant recorded-data marker of *which early failure pathway is likely*, or whether its apparent association is explained by selective lactate measurement and death competing with ICU return.

The deliverable is an estimand, not a bedside rule. It must establish the following outputs on a locked patient-level test set:

1. `run_manifest.json`, containing the dataset-catalog [source checksum], MIMIC snapshot `[source checksum]`, exact source hashes and paths, archive members, schema hashes, direct dictionary-label/unit assertions, locked windows and thresholds, split seeds, software versions, and output hashes.
2. `cohort_audit.parquet`, one earliest valid adult ICU stay per subject, with join success, temporal integrity, alive-at-`outtime` rule, hospital-end fields, lactate observation eligibility, support-state eligibility, and every exclusion.
3. `feature_ledger.parquet`, with every eligible lactate observation and candidate vasoactive interval plus twelve one-hour rows in `[outtime-12h,outtime)`. Each row must retain values, timestamps, masks, duplicate/validity flags, and source provenance; no imputation may create a measurement.
4. `observation_selection_audit.parquet`, documenting the qualifying-pair indicator, assay-specific coverage, measurement intensity, support-documentation coverage, fitted observation propensities, positivity/effective sample size, and the selection-sensitivity parameter results.
5. `phenotype_audit.parquet`, with the observed lactate trajectory class, recorded circulatory state, four-cell discordance class, unclassified/contradictory cells, and all threshold, assay, repeat-window, and boundary recodings.
6. `topology_outcome_audit.parquet`, with every later same-admission ICU stay, every relevant transfer interval, documented/non-documented bridge evidence, return candidate times, death/discharge timing, and lower/upper topology labels.
7. Held-out predictions and estimands from both methods: 6-, 24-, and 48-hour cumulative-incidence functions (CIFs), lower/upper topology intervals, all-cause first-event composition, calibration, IPCW Brier/log loss where defined, bootstrap/split uncertainty, sensitivity matrices, and a conclusion-to-output map in `interpretation.md`.

The primary scientific output is not AUROC. It is the standardized contrast for persistent-high/recorded-off versus low/recorded-off, with death retained as a competing first event, reported for the documented-bridge lower endpoint (L), any-later-ICU-return upper endpoint (U), and death. The study must show whether that contrast remains directionally and materially separated from zero after measurement-process adjustment and under explicit missing-phenotype bounds.

## Evidence-supported claim and unresolved question

The expert seed `[starting question]` proposes that persistent hyperlactatemia can have different meanings when perfusion is improving versus worsening. Its stated caveat is that repeated lactates are selectively obtained and cannot diagnose microcirculatory dysfunction. The available local evidence supports only that this MIMIC snapshot contains dated lactate, vital-sign, vasoactive-input, ICU-stay, transfer, death, discharge, and note tables. It does not support a biological diagnosis, a treatment response, or the clinical intent behind ordering or stopping a vasoactive drug.

The parent design established a useful measured-subset discordance comparison and preserved lower/upper ICU-return topology. This successor advances it in a specific way: the primary target population is **all eligible adults alive at first ICU outtime**, not only those selected for two lactate tests. It explicitly separates:

- the observed complete-pair estimand;
- a selection-standardized estimand that transports the observed phenotype comparison to all eligible discharges under a declared observation assumption; and
- an assumption-light interval that allows the unobserved lactate/support phenotype to vary while keeping recorded event times fixed.

The unresolved clinical question is therefore:

> At a first ICU discharge, does persistent measured lactate after a documented withdrawal of vasoactive support identify a distinct early post-ICU failure composition—especially more return-compatible failure than low lactate after the same recorded withdrawal—or does the apparent contrast disappear when selective lactate measurement and death before return are handled explicitly?

The prespecified primary hypothesis is that, among eligible first ICU discharges, persistent-high/recorded-off has a higher 48-hour L CIF than low/recorded-off and a different return-versus-death composition; the contrast should persist after observation-process standardization and should not be eliminated by the assumption-light interval unless the missing phenotype is assigned adversarially. The concordant persistent-high/active-support cell is a descriptive positive-control severity stratum, not the main clinical comparison.

The null and adverse directions are equally legitimate. A null after selection adjustment, a reversal, or a death-dominant rather than return-dominant pattern falsifies the proposed interpretation. A signal only in U (any ICU return) is not called confirmed ICU escalation. This is prognostic and care-process observational research, not an estimate of delaying discharge, continuing vasopressors, giving fluid, or improving outcome.

This question matters because the clinical decision is not “build another first-ICU-discharge risk score.” It is whether a scarce, selectively ordered serial lactate result carries information about *the mode and timing of early failure* beyond the fact that clinicians chose to measure it. A robust answer could justify prospective evaluation of lactate-informed post-ICU surveillance; a non-robust answer would caution against treating a measured lactate as a portable discharge signal.

## Population, landmark, and temporal boundaries

Use the read-only source ZIP:

`[internal dataset path]`

Source [source checksum].

Select one stay per subject: the earliest `icu/icustays` row by `intime` with non-null `subject_id`, `hadm_id`, `stay_id`, `intime < outtime`, a successful join to `hosp/admissions` on `subject_id,hadm_id`, and an adult `hosp/patients.anchor_age >= 18`. Require that the ICU outtime falls inside the matching admission interval, and that the patient is alive at the ICU landmark: `deathtime` is absent or strictly after `outtime`. Require the recorded ICU stay to end before a recorded hospital death/discharge boundary; retain temporal contradictions as exclusions and audit strata rather than repairing them silently. Do not use `patients.dod` to define an outcome.

The landmark is the recorded `icu/icustays.outtime`. All predictors must be charted or started before `outtime`. The primary pre-landmark window is left-closed/right-open `[outtime-12h,outtime)`; the final measurement subwindow is `[outtime-6h,outtime)`. Follow-up windows are `[outtime,outtime+6h)`, `[outtime,outtime+24h)`, and `[outtime,outtime+48h)`, truncated at the corresponding hospital end. No post-outtime treatment, monitoring, destination, later note, or later measurement is a predictor.

Join age, sex, and `anchor_year_group` from `hosp/patients` by `subject_id`; retain admission type from `hosp/admissions`. Join same-stay observations on `subject_id,hadm_id,stay_id` where the source provides `stay_id`. For outcomes, use same-admission `subject_id,hadm_id` joins and preserve unmatched transfer rows in the audit.

## Recorded metabolic and circulatory phenotype

### Lactate and selective measurement

Use `hosp/labevents` rows with `itemid in {50813,52442}`, positive numeric `valuenum`, parseable `charttime`, and a verified blood unit/value convention. Before analysis, assert against `hosp/d_labitems` that both IDs have label `Lactate`, fluid `Blood`, and category `Blood Gas`; audit `value`, `valuenum`, `valueuom`, duplicate timestamps, and implausible/unit-inconsistent rows. Harmonize only after the unit assertion. The primary lactate measurement time is `charttime`; `storetime` is retained for a timestamp negative control and never substituted in the primary analysis.

Define the observed qualifying-pair indicator R=1 if at least two valid blood-lactate observations occur in the primary 12-hour window, their chart times are at least two hours apart, and the latest member of the selected pair is in `[outtime-6h,outtime)`. Select the latest qualifying pair by chart time, with deterministic tie handling for duplicate timestamps; retain all other eligible observations in the ledger. R=0 includes zero, one, and non-qualifying repeated measurements. R is a measurement-process indicator, not a patient characteristic and not a missing-at-random fact.

For R=1, define the primary recorded lactate classes before test evaluation:

- low: both selected values <2.0 mmol/L;
- persistent-high: both selected values >=2.0 mmol/L;
- resolving-high: earlier value >=2.0 and latest value <2.0;
- indeterminate: all other qualifying pairs.

The cutoff is a recorded measurement convention, not a diagnosis. Locked sensitivity analyses use thresholds 1.5, 2.0, and 2.5 mmol/L; repeat windows of 6, 12, and 24 hours; latest-pair versus all-pair qualifying rules; item 50813 only, item 52442 only, and both verified assays. A sensitivity rule may not create a value where none was recorded.

### Recorded vasoactive state

Derive support only from valid `icu/inputevents` records whose `itemid` is in the verified primary dictionary: norepinephrine 221906, vasopressin 222315, epinephrine 221289, dopamine 221662, or phenylephrine 221749. Admit a concentration/legacy variant only after a local `icu/d_items` audit verifies the same medication label and `linksto=inputevents`; otherwise retain it as an unclassified candidate.

Use `starttime`, `endtime`, `statusdescription`, and `continueinnextdept` to audit interval validity. A valid interval must have parseable times with `starttime < endtime`, matching stay keys, and a non-contradictory status. It is active if it overlaps the final six-hour window `[outtime-6h,outtime)`. Define recorded-off only when a prior valid vasoactive interval is observed, its end precedes the final six-hour window, and no valid interval overlaps the final six-hour window. Absence without prior positive support is unknown, never off. Continue-in-next-department and ambiguous status fields are retained as ambiguous/unknown, not converted to cessation. Recode boundary tolerances at 0, 15, and 30 minutes.

The primary four-cell comparison is low/recorded-off, persistent-high/recorded-off, low/active-support, and persistent-high/active-support. Resolving-high, indeterminate, R=0, ambiguous support, and contradictory cells remain explicit audit strata. They are not silently folded into low or off. The primary contrast is the first two cells; the other cells test whether any signal is simply current support severity.

### Identical feature ledger

Both the transparent baseline and learned alternative receive the same feature ledger:

- every lactate row with item ID, value/unit, chart/store time, pair-selection flags, and measurement mask;
- every candidate vasoactive interval with item ID, label assertion, start/end/store time, status, continuation flag, validity, overlap, and support mask;
- twelve one-hour pre-landmark rows containing final/last-observed and count/time-since-measurement summaries for lactate, support, MAP, HR, RR, SpO2, O2 flow, FiO2, and PEEP, plus separate source-specific observation masks;
- static age, sex, anchor-year group, and admission type.

Vital signs come only from `icu/chartevents` item IDs 220052 (arterial mean), 220181 (non-invasive mean), 220045 (heart rate), 220210 (respiratory rate), 220277 (pulse-oximetry oxygen saturation), 223834 (O2 flow), 223835 (inspired O2 fraction), and 220339 (PEEP set). Before use, assert each label, unit, and `linksto=chartevents` in `icu/d_items`. Use `charttime` in the primary ledger; retain `storetime` only for the negative control. Do not use optional procedure/output records to infer missing support.

The primary analysis uses no discharge-note text, radiology text, waveform, image, or post-landmark data. Those sources remain available but are not required for this estimand.

## Outcomes, competing death, and partial identification

For each horizon, define mutually exclusive first recorded events while preserving two topology versions:

- L (lower, return-compatible): a later same-admission ICU stay begins within the horizon and is preceded by a documented non-ICU transfer interval in `hosp/transfers` after the index `outtime` and before the later ICU `intime`.
- U (upper, any return): any later same-admission `icu/icustays` row begins within the horizon.
- U-only/unknown topology: a U candidate for which the required non-ICU bridge is absent, missing, overlapping, contradictory, or otherwise not verifiable. It is included in U and excluded from L; it is not called confirmed ICU escalation.
- death: the first recorded in-hospital death. Use `hosp/admissions.deathtime` when present. If `hospital_expire_flag=1` but `deathtime` is absent, retain the death classification and mark its exact timing as unavailable; primary CIF timing uses `dischtime` as the recorded administrative time and a sensitivity analysis interval-censors it between the last known alive time and `dischtime`. This does not claim that `dischtime` is physiologic death time.
- alive hospital discharge: `dischtime` with no earlier return or death, treated as a competing event for the horizon-specific first-event analysis.
- administrative censoring: no event by the horizon or loss of the corresponding admission boundary.

Use `hosp/transfers` columns `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime` and all later same-admission ICU rows to build the topology audit. Because transfer topology and careunit semantics can be incomplete, report L as a lower endpoint and U as an upper endpoint. Sensitivities vary bridge duration rules 0/15/30/60 minutes, transfer permutations, a +6-hour shift of transfer times, and return/death tie ordering (death-first primary; return-first sensitivity).

The primary estimands at 6, 24, and 48 hours are:

1. the standardized absolute CIF contrast \\(Delta^L_h = CIF^L_h(persistent-high/off)-CIF^L_h(low/off)\\) with death and alive discharge competing;
2. the analogous \\(Delta^U_h\\) and death CIF contrast;
3. the return-versus-death composition \\(CIF^{return}_h/(CIF^{return}_h+CIF^{death}_h)\\) whenever the denominator is nonzero; and
4. the width and direction of the identification interval after jointly varying topology and unobserved phenotype assignment.

Report the unadjusted observed-pair estimand, then the full-cohort estimand under observation standardization, and finally assumption-light bounds. Standardize to the entire eligible cohort, not to the distribution of people who happened to receive serial lactates.

For the observation-standardized estimand, estimate R from pre-landmark ledger information, static variables, prior measurement masks, and recorded support/physiology; do not use post-outtime outcomes. Under the declared conditional observation assumption, use stabilized inverse-probability-of-observation weights to transport observed phenotype-specific competing-risk hazards to the eligible cohort. Fit the observation model on training data only, cap primary weights at 10, report uncapped diagnostics and effective sample size, and repeat with caps 5 and 20. Vary the unmeasured selection odds for R=1 versus R=0 by a locked Rosenbaum-style multiplier Gamma in {0.5, 1, 2}; Gamma=1 is the declared conditional-observation analysis, not a fact about the data. The selection-adjusted result is not causal.

For assumption-light intervals, keep each subject's recorded event/censoring time and competing-event label fixed. Enumerate or solve the finite assignment problem over subjects with R=0, indeterminate lactate, ambiguous support, or contradictory topology, allowing every assignment compatible with the deterministic observed constraints. Minimize and maximize each phenotype-specific CIF contrast and composition at each horizon, jointly with L/U topology assignment; use a linear-programming or exact finite-assignment implementation and publish the assignment counts. This is an identification interval, not a confidence interval. It may be wide or uninformative. Confidence intervals around weighted estimates and bootstrap intervals around fixed-bound endpoints must remain separate.

Death is never censored as if it were non-informative loss to follow-up. A larger return CIF with a simultaneous larger death CIF is not interpreted as a single “readmission risk” gain; the first-event composition is part of the result.

## Baseline and substantive learned alternative

Use fixed subject-level 70/15/15 train/validation/test splits with seeds 17, 29, and 43. No subject may cross splits. All thresholds, unit rules, scaling, weight caps, observation-model tuning, latent-state initialization, and sensitivity choices are fixed using training/validation only. The test set is used once for locked estimates.

### Transparent baseline: selection-robust competing hazards

Fit pooled one-hour cause-specific logistic hazard models over eight six-hour post-landmark bins for L, U-only, death, and alive discharge; fit the L and U versions separately because they represent different endpoint definitions. Use penalized logistic regression with fixed regularization selected on training/validation. Predictors are the prespecified cell indicator, all identical-ledger physiology values and masks, support evidence, measurement intensity, static covariates, and time-bin indicators. Fit nested models:

A. cell/last-lactate only;
B. physiology and support without lactate values;
C. observation masks/intensity only;
D. lactate values/trajectory with masks;
E. the full ledger.

For each model, standardize held-out CIFs to the full eligible cohort. For the full model, also provide the stabilized observation-weighted version and the assumption-light finite-assignment bounds. Use the Aalen-Johansen recursion from the fitted cause-specific hazards with death and alive discharge competing. Report absolute CIFs, contrasts, risk composition, calibration intercept/slope, IPCW Brier/log loss, and uncertainty; do not report odds ratios as the clinical result.

This baseline is transparent enough to reveal whether the contrast is present in values, in support/physiology, in observation intensity, or only in the composite cell. It provides the primary inferential comparison even if the learned model is better calibrated.

### Learned alternative: observation-aware two-domain hidden semi-Markov model

Fit a small, CPU-suitable observation-aware two-domain hidden semi-Markov model on exactly the same ledger and splits. The metabolic domain has latent states low, persistent-high, resolving, and unknown; the circulatory domain has active, recorded-off, and unknown. State durations span the same twelve one-hour rows and may be parameterized by six-hour blocks. A separate observation model predicts lactate assay occurrence/value availability and support evidence availability from the latent state, prior ledger history, and recorded measurement intensity. The event head predicts the same L, U-only, death, and alive-discharge hazards over the same eight six-hour post-landmark bins. The fitting target is the joint observed ledger plus held-out event labels, with no extra source or post-landmark input.

The alternative must output posterior state probabilities/entropy, observation propensities, state-transition/duration summaries, held-out CIFs and the same L/U/death contrasts, with bootstrap or multi-initialization uncertainty. It can reveal whether ordered persistence and trajectory timing carry stable information that an endpoint cell loses, or whether the apparent phenotype is largely a recording process. It cannot recover unrecorded perfusion, clinician intent, treatment response, or a true latent tissue state.

Compare the two methods on the scientific outputs: direction and interval width of Delta-L/U/death, calibration, IPCW Brier/log loss, stability across seeds, observation-model calibration, latent entropy, and agreement of failure composition. A small predictive score gain alone is not a scientific win. Retain the baseline as the primary result if the latent model is high-entropy, poorly calibrated, seed-unstable, materially changes the target estimand, or narrows uncertainty only through unverifiable latent assumptions.

## Falsification and interpretation gates

The following are prespecified before test evaluation:

- Permute lactate values and their temporal order within subject and support-intensity strata while preserving assay count, masks, timestamps, and R. The primary lactate contrast should attenuate toward the observation-only result.
- Permute the recorded-off/active support timing within support-intensity strata while preserving medication counts and interval lengths.
- Fit observation-only, support/physiology-only, lactate-value-only, and full-ledger models. If observation-only reproduces the full contrast, the proposed metabolic interpretation is weakened.
- Replace lactate `charttime` and support `starttime/endtime` with `storetime` as a timestamp negative control.
- Repeat at pseudo-landmarks 6 and 12 hours before `outtime`, shifting the outcome origin identically. A landmark-specific effect should not appear with arbitrary misaligned windows.
- Remove optional procedure/output markers (they are not primary inputs) and confirm that no unverified support inference was required.
- Repeat each assay separately; vary threshold, pair rule, window, support-boundary tolerance, transfer bridge, death timing, and return/death tie rule.
- Stratify by first/last careunit, admission type, and anchor-year group without treating deidentified cross-subject dates as calendar time.
- Report cell counts, missingness, contradiction rates, observation-model calibration, weight positivity/ESS, latent entropy, and topology-bound width. A confidence interval that ignores selection or topology width cannot be presented as robust evidence.

Supportive evidence requires: adequate counts and positivity in the two primary cells; a full-cohort selection-standardized Delta-L that remains positive with uncertainty excluding zero under the declared Gamma sensitivity; a non-vacuous assumption-light interval or a clearly reported reason it is vacuous; concordant baseline and learned directions; acceptable held-out calibration; attenuation after lactate permutation; and persistence across assay/window/threshold/topology sensitivities. The learned model need not improve a score, but it must either reproduce the contrast with lower unexplained latent uncertainty or show a stable trajectory/observation decomposition.

Adverse evidence includes a null or reversal after selection adjustment, a contrast explained by measurement intensity, persistence under lactate permutation, a signal dependent on one assay or one missingness rule, death dominating the alleged return pathway, poor calibration, or a U-only signal with a wide or null L interval. A death-only contrast rejects the return-dominant hypothesis but can support a separately reported competing-risk description.

Inconclusive evidence includes sparse or non-positive cells, high R=0/unknown/indeterminate prevalence, very wide finite-assignment or topology intervals, unstable selection weights, unresolved death timing, split instability, high latent entropy, model disagreement, or insufficient event support. Inconclusive is a valid result and must not be converted into a null claim.

Computation can establish reproducible recorded-data feature construction, the observed-pair estimand, the selection-standardized recorded-data estimand conditional on its observation assumption, competing-risk CIFs, assumption-light bounds, held-out calibration/prediction, and sensitivity consistency. It cannot establish tissue hypoperfusion, microcirculatory dysfunction, fluid responsiveness, treatment benefit/harm, clinician intent, planned versus unplanned return, preventability, discharge readiness, clinical utility, or patient outcomes after leaving the hospital. Those claims require expert chart adjudication, treatment-limitation and ward-monitoring evidence, external validation, and likely prospective or causal study.

## Exact source bindings and availability

The primary ZIP and archive members are read-only:

- `mimic-iv-3.1/hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`; schema `datasets/mimic/table-e8ec3e6e4c428559.json`, hash `[source checksum]`.
- `mimic-iv-3.1/hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; schema `table-9154f8c46cade9af.json`, hash `[source checksum]`.
- `mimic-iv-3.1/icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; schema `table-7d5c8feb0fb0dbd4.json`, hash `[source checksum]`.
- `mimic-iv-3.1/hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; schema `table-685b6b74d0d7c547.json`, hash `[source checksum]`.
- `mimic-iv-3.1/hosp/labevents.csv.gz`: `labevent_id,subject_id,hadm_id,specimen_id,itemid,order_provider_id,charttime,storetime,value,valuenum,valueuom,ref_range_lower,ref_range_upper,flag,priority,comments`; schema `table-bf701d962c63287c.json`, hash `[source checksum]`.
- `mimic-iv-3.1/hosp/d_labitems.csv.gz`: `itemid,label,fluid,category`; schema `table-57ae65f0eb6cf1a6.json`, hash `[source checksum]`.
- `mimic-iv-3.1/icu/inputevents.csv.gz`: `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,patientweight,totalamount,totalamountuom,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate`; schema `table-d193e854c19eb4ba.json`, hash `[source checksum]`.
- `mimic-iv-3.1/icu/d_items.csv.gz`: `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue`; schema `table-d1023acc404fd1d4.json`, hash `[source checksum]`.
- `mimic-iv-3.1/icu/chartevents.csv.gz`: `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; schema `table-8208609a785ea7e8.json`, hash `[source checksum]`.
- Optional but excluded from the primary ledger: `mimic-iv-3.1/icu/procedureevents.csv.gz` (`table-f6493e8403a0abe7.json`, hash `[source checksum]`) and `mimic-iv-3.1/icu/outputevents.csv.gz` (`table-a7ad1c4cdcdbfe0a.json`, hash `[source checksum]`).

The direct archive audit confirmed the required members exist and exposed the stated headers. It also confirmed `d_labitems` labels `Lactate`/fluid `Blood` for 50813 and 52442, and `d_items` labels/linkage for the primary vital and vasoactive IDs. These checks are readiness facts, not clinical findings.

The note releases `note/discharge.csv.gz`, `note/discharge_detail.csv.gz`, `note/radiology.csv.gz`, and `note/radiology_detail.csv.gz` are available in the configured snapshot but are not used: their lexical extraction is explicitly unvalidated for clinical diagnosis and they cannot recover intent, perfusion, or treatment limitation. MIMIC-CXR images and raw waveforms are unavailable in this snapshot.

The other configured read-only datasets remain accessible through their verified dataset indexes: HCC (12 source files), EICU (31), and UKB (8). They are not pooled with MIMIC because their identifiers, time semantics, transfer topology, and lactate/support dictionaries are not harmonized for this question. Cross-dataset validation is a deferred separate study, not silently claimed here.

## Method alternatives, compute, and revisit record

The transparent baseline and semi-Markov alternative above are the actual scientific comparison. A static first-discharge logistic score was rejected because it cannot distinguish selective lactate measurement from lactate content, competing death from return, or L from U. A causal fluid/pressor target-trial emulation is deferred: treatment indication, response, treatment limitations, and microcirculation are not adequately observed. A GRU/TCN or transformer is deferred because additional capacity would test mainly predictive compression after the two-domain latent model, not the present measurement-versus-trajectory uncertainty. It may be revisited only if the ledger is populated, the learned model is stable, and the remaining disagreement is specifically long-range temporal rather than selection/topology.

The alternative is not excluded for using a latent learned model; its selection is justified by the scientific information it may reveal—trajectory persistence and observation intensity as separate processes. It is kept small and CPU-suitable to make its assumptions inspectable. It must be abandoned or demoted if it is high-entropy, poorly calibrated, unstable across initializations/splits, or changes the estimand.

Measured discovery facts are the configured 7,200-second discovery budget, read-only source/header/schema/item audits, catalog/source hashes, and hardware inventory in `inputs.json` (eight A100-SXM4 80-GB devices, allocated only through managed jobs). No full cohort extraction, bootstrap, weighted fit, or latent fit was run here; those durations and event counts are unverified. The baseline is expected to fit on CPU. The latent model should first be profiled on CPU with approximately 8–16 CPUs and 64–128 GiB; this is a planning estimate, not a measurement. A bounded allocated A100 is optional only if repeated matrix operations prove limiting; within an allocation it must use `cuda:0`, and GPU use does not change the scientific acceptance criteria.

The future solver must newly fit the competing-hazard baseline and observation model, solve the phenotype/topology assignment bounds, fit the two-domain semi-Markov alternative, and emit the listed test-set outputs. Completion is established by reproducible manifests, populated ledgers/audits, locked predictions, estimands with uncertainty/bounds, falsification results, and a conclusion map—not by readiness checks or a claimed clinical result.
