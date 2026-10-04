# Residual physiologic instability before live ICU discharge

## Scientific question and hypothesis

The unresolved question is whether residual instability immediately before a clinician discharges a patient from the ICU identifies a clinically important risk group that is missed by a single last vital sign or a conventional severity summary.

The testable hypothesis is: among patients discharged alive from an index MIMIC-IV ICU stay, a prespecified trajectory of oxygen/ventilatory support and vital-sign instability during the final 12 hours before ICU outtime predicts 48-hour ICU readmission or in-hospital death more accurately and with better calibration than a baseline using only the last available measurements and fixed admission/stay covariates. The primary estimand is the out-of-sample difference in Brier score and calibration, with AUROC/AUPRC secondary; it is not a causal effect of delaying discharge or changing treatment.

Evidence already supports only the weaker claim that ICU readmission and death can be observed after an ICU transfer and that dated physiologic observations exist before outtime. It does not establish that residual instability causes readmission, that discharge decisions were inappropriate, or that monitoring/intervention would improve outcomes. This experiment tests the unresolved incremental prognostic claim.

This could inform a consequential decision: whether a patient being considered for ICU transfer should receive additional review/monitoring because their recent physiologic trajectory is high risk. A positive result would justify prospective clinical adjudication and implementation evaluation; it would not itself justify a discharge rule.

## Population and temporal design

Use the MIMIC-IV 3.1 core snapshot. The unit is an index ICU stay, linked to its hospital admission.

Eligibility:

- adults with an index row in `icu/icustays` (`subject_id`, `hadm_id`, `stay_id`, `intime`, `outtime`);
- `outtime` is observed and the stay is not an ICU-to-death event: exclude records with `hosp/admissions.deathtime <= icustays.outtime`; require `hosp/admissions.hospital_expire_flag=0` for the live-discharge cohort;
- `outtime < hosp/admissions.dischtime` or a non-death hospital discharge is documented, so the index event is an ICU discharge rather than hospital death;
- retain only the first eligible ICU stay per `hadm_id` for the primary analysis to avoid multiple correlated discharge decisions; a prespecified secondary analysis includes later ICU stays with participant-clustered uncertainty.

Time zero is the recorded `icustays.outtime`. Features may use only events with `charttime <= outtime` and in the interval [outtime - 12 hours, outtime]. No `storetime`, transfer outcome, discharge note, or future event may be used as a feature. The primary forecast horizon is 48 hours after outtime; the secondary horizon is through the end of the same hospital admission (`hosp/admissions.dischtime`), administratively censored there.

Primary composite outcome: first subsequent ICU readmission within 48 hours or in-hospital death before 48 hours. Readmission is a later `icu/icustays.intime > index outtime` for the same `subject_id` and `hadm_id`. Death is `hosp/admissions.deathtime` or `hospital_expire_flag=1), restricted to the horizon. Report the components separately. For the competing-risk analysis, death before a possible readmission is a competing event; do not count a patient who dies first as a readmission.

Secondary outcomes are ICU readmission through hospital discharge, death through hospital discharge, and a mutually exclusive three-state endpoint (no event, readmission, death first). Discharge destination is descriptive adjustment/stratification only; it is not a proxy for patient recovery.

## Exact data bindings

The read-only source for all archive tables is:

`[internal dataset path]`, [source checksum].

Required archive members and columns:

1. `mimic-iv-3.1/icu/icustays.csv.gz`, catalog table `icu/icustays`: `subject_id`, `hadm_id`, `stay_id`, `intime`, `outtime`, `first_careunit`, `last_careunit`, `los`. This defines index stay and time zero.
2. `mimic-iv-3.1/hosp/admissions.csv.gz`, catalog table `hosp/admissions`: `subject_id`, `hadm_id`, `dischtime`, `deathtime`, `hospital_expire_flag`, `admission_type`, `admission_location`, `discharge_location`. Join to `icu/icustays` on `subject_id,hadm_id`; it defines live discharge eligibility and hospital outcomes.
3. `mimic-iv-3.1/hosp/patients.csv.gz`, catalog table `hosp/patients`: `subject_id`, `gender`, `anchor_age`, `anchor_year_group`, `dod`. Join on `subject_id`; use age/sex and the deidentified age convention (age >89 represented as 91) as baseline covariates. Do not use `dod` as a feature.
4. `mimic-iv-3.1/hosp/transfers.csv.gz`, catalog table `hosp/transfers`: `subject_id`, `hadm_id`, `eventtype`, `careunit`, `intime`, `outtime`. Join on `subject_id,hadm_id`; use as a sensitivity check of transfer timing and to characterize destination. The primary readmission definition remains the ICU-stay table.
5. `mimic-iv-3.1/icu/chartevents.csv.gz`, catalog table `icu/chartevents`: `subject_id`, `hadm_id`, `stay_id`, `charttime`, `storetime`, `itemid`, `value`, `valuenum`, `valueuom`, `warning`. Join observations to the index `stay_id`; filter by `charttime), not storetime.
6. `mimic-iv-3.1/icu/d_items.csv.gz`, catalog table `icu/d_items`: `itemid`, `label`, `abbreviation`, `linksto`, `category`, `unitname`, `param_type`. It verifies item meaning/units. The audited items are HR 220045; non-invasive BP systolic/diastolic/mean 220179/220180/220181; respiratory rate 220210; pulse-ox SpO2 220277; temperature C/F 223762/223761; O2 flow 223834; ventilator mode 223849. Text-valued ventilator mode is retained as a categorical support signal only if its event coverage is adequate; otherwise report its missingness and omit it without changing the primary feature specification.
7. `mimic-iv-3.1/icu/procedureevents.csv.gz`, catalog table `icu/procedureevents`: `subject_id`, `hadm_id`, `stay_id`, `starttime`, `endtime`, `itemid`, `value`, `valueuom`, `ordercategoryname`, `statusdescription`. Items 225792 (Invasive Ventilation) and 225794 (Non-invasive Ventilation) define whether either support is active during each two-hour bin, using overlap of [starttime,endtime] with the bin. These are processes, not proof of oxygen dose or clinical indication.
8. `mimic-iv-3.1/icu/outputevents.csv.gz`, catalog table `icu/outputevents`: `subject_id`, `hadm_id`, `stay_id`, `charttime`, `itemid`, `value`, `valueuom`. Use only in a prespecified exploratory sensitivity feature for urine-output coverage; do not let its selective measurement define the primary instability phenotype.

The catalog relationship is `icu/icustays -> hosp/admissions` on `subject_id,hadm_id`, and `hosp/admissions -> hosp/patients` on `subject_id`. Other joins above are explicitly checked by keys. Timestamps are subject-specific shifted timestamps: within-subject intervals are usable, cross-subject calendar comparisons are not.

Construct six consecutive two-hour bins ending at outtime. In each bin calculate, where present, the median and last value for HR, MAP (prefer item 220181; otherwise derive no MAP from systolic/diastolic in the primary analysis), RR, SpO2, temperature, O2 flow, and binary overlap indicators for invasive/non-invasive ventilation. Derive trajectory summaries using only the six bins: last value, within-window minimum/maximum, count of observed bins, linear slope when at least three bins are observed, and number of direction reversals for each continuous signal. Prespecify clinically directional flags (e.g., increasing O2 flow, low SpO2, hypotension, tachypnea) only after units and observed ranges are checked in the readiness job; do not invent cutoffs from the hypothesis. Missingness indicators are included because measurement intensity is informative, and a complete-case analysis is a sensitivity analysis, not the primary analysis.

## Baseline and substantive alternative

The simple baseline is a regularized logistic regression for the primary 48-hour composite, using only: age, sex, index ICU type, ICU length of stay, admission type/location, last value and observation indicator for each signal, and last support indicators. Fit the regularization parameter inside training folds. This baseline represents the practical “last status” discharge screen and makes the incremental question explicit.

The learned alternative is a small temporal model fitted on the same six two-hour bins and the same item-derived variables: a masked GRU (or, if the solver environment lacks a recurrent implementation, a one-layer temporal convolution with the same input/output contract) followed by a logistic head. It must use only pre-outtime bins, explicit missingness masks and support indicators, and no notes or future variables. Its scientific purpose is not a tiny leaderboard gain: it tests whether order, persistence, fluctuation and changing measurement/support patterns carry information that the baseline’s last-value summaries lose. A mechanistic/transparent alternative to record but defer is a prespecified instability state score built from clinically directional threshold crossings and consecutive-bin persistence. It is scientifically useful for interpretability, but exact thresholds and adjudication are not verified in this discovery episode; revisit it if an ICU clinician supplies cutoffs.

Fit baseline and GRU on the same participant-level training partition, with a validation partition for tuning and an untouched discovery test partition. Partition by `subject_id`, keeping all stays from one subject together. The catalog’s reserved 20% participant partition is inaccessible in this episode and is not to be called external validation. Future solver execution may use a deterministic 60/20/20 split within the accessible discovery partition, stratified only after splitting by subject, with a fixed seed and a second seed sensitivity run.

## Evaluation, uncertainty and falsification

The primary comparison is paired held-out Brier score difference (GRU minus baseline; lower is better) with a 95% subject-cluster bootstrap confidence interval, plus calibration intercept/slope and reliability plots. Secondary metrics are AUROC, AUPRC, sensitivity at a prespecified baseline operating point, and decision-curve net benefit over clinically plausible thresholds. Report prevalence, event counts, feature coverage and the number excluded at every filter.

The hypothesis is supported only if the learned trajectory model has a held-out Brier improvement whose 95% interval excludes zero, calibration is not materially worse, and the direction is consistent across at least two prespecified sensitivity analyses: (a) restricting to stays with measurements in at least four of six bins, and (b) excluding patients with an active invasive/non-invasive ventilation procedure at outtime. An improvement only in AUROC with worsened calibration is not sufficient.

The hypothesis is adverse/falsified if the baseline is as good or better on Brier with a confidence interval including zero for the trajectory increment, or if the trajectory model’s apparent gain disappears under participant-level splitting, timestamp leakage audits, or the coverage restriction. If the learned model is worse, that is a scientifically informative result: the last observed status may capture nearly all reproducible signal, or trajectory measurements may be too selective/noisy.

Results are inconclusive if the primary event count is too small for the prespecified uncertainty interval, if item/unit mapping or outcome linkage fails readiness checks, if key features are absent in most eligible stays, or if confidence intervals remain too wide to distinguish a clinically meaningful increment. Do not relabel an inconclusive result as support.

Pre-specified leakage checks include: no feature after outtime; no admissions `deathtime`, `hospital_expire_flag`, discharge destination, transfer-after-outtime, or future ICU-stay data in features; no random row-level split; no cross-subject timestamp alignment; and an audit that each feature’s maximum charttime is <= outtime. Report complete-case and missingness-ablated analyses to determine whether the model learns documentation intensity rather than physiology.

## What the study can and cannot conclude

Computationally checkable outputs are the frozen cohort counts, feature-coverage table, model fit status, held-out predictions, Brier/AUROC/AUPRC/calibration estimates, clustered uncertainty, split reproducibility, and leakage tests. These can establish whether the incremental prognostic claim is supported in this snapshot.

The data cannot adjudicate why the patient was discharged, whether an ICU bed was clinically necessary, whether an intervention would prevent readmission, or whether the measurements reflect true physiologic instability rather than clinician documentation. It lacks a validated discharge-readiness label, prospective clinician adjudication, complete treatment limitation/goals-of-care context, and an external hospital cohort. Radiology text is present but not required; MIMIC-CXR images and raw waveforms are unavailable, so no image/waveform claim is permitted. A causal discharge policy, clinical threshold, or transportability claim requires expert review, prospective validation, and another study.

## Demonstration and seed dispositions

- Delphi/natural-history: structured dated histories make the GRU comparison a bounded adaptation, but the original UKB trajectory cohort and external Danish validation are unavailable; no reproduction claim is made.
- ALADYNOULLI: a latent trajectory model could be revisited if it answers whether physiologic states are more stable/interpretable than the GRU; the original genetic inputs are not required here and are unavailable for a reproduction. It is deferred because the present question needs an auditable prognostic increment first.
- Oncoformer/cancer: the accessible supplement supports multimodal ambition, but the main article/STAR Methods and MIMIC-CXR images are unavailable; an image adaptation is not pursued. Structured EHR signals are sufficient for this narrower test.
- Other imported MIMIC seeds remain unused because they require stronger causal assumptions (diuretic/transfusion/de-escalation), unavailable measured kidney function or ischemia adjudication, or more selective treatment/confounding definitions. They remain repairable alternatives, not rejected scientific questions.
- The expert seed `[starting question]` is the true parent. Its broad “high oxygen/fluctuating vitals before discharge” idea is repaired into a fixed 12-hour window, explicit event definition, baseline-vs-trajectory comparison, and non-causal interpretation.

## Scientific deliverable and resource plan

The future solver must newly construct the cohort and six-bin feature table, fit both the regularized logistic baseline and masked temporal model, produce held-out predictions and uncertainty, and write an interpretation tied to the primary Brier/calibration comparison. Completion requires those outputs plus the cohort/coverage/leakage audit; a readiness pass alone is not a solved research objective.

The future study is planned within the solver envelope in `inputs.json` (up to 16 CPUs, 8 GPUs, 262144 MiB, 28800 seconds). Discovery has verified schemas and item labels, not full event counts or training time. A CPU baseline should fit within minutes to hours after chunked extraction. The GRU is expected to fit on CPU for the compact six-bin tabular sequence, but a single allocated A100 job is a reasonable measured feasibility option if repeated fits or sensitivity analyses are slow; ordinary shell CUDA absence must not be interpreted as hardware absence. No GPU is scientifically required. Full runtime and event-count estimates remain unverified until the declared bounded readiness/coverage job runs. Sources remain read-only and all derived cohorts/features/predictions belong in the workspace.
