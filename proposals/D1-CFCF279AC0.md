# Suspected discordant renal recovery after early ICU AKI: episode 2 repair

## Scientific deliverable

Newly derive a frozen, one-row-per-eligible-first-ICU-stay MIMIC-IV v3.1 cohort and estimate whether a prespecified creatinine-recovered/Foley-output-not-recovered phenotype is associated with post-landmark in-hospital death. Completion requires:

1. a provenance manifest, cohort counts, item-level support counts, measurement-density and missingness table, and phenotype prevalence;
2. adjusted phenotype contrasts with 95% confidence intervals and event timing;
3. a fitted transparent baseline and a substantive temporal alternative using the same subject-level held-out split;
4. held-out AUROC, AUPRC, Brier score, calibration intercept/slope, uncertainty intervals and urine/fluid ablations;
5. threshold, coverage, early-RRT and source-sensitivity analyses, plus prespecified falsification and adverse/inconclusive reporting.

No fitted clinical result is asserted here. The managed archive-wide support scan was attempted for 223 seconds and cancelled before counts were produced; compilation must perform the audit and stop or classify the result inconclusive if support is inadequate.

## Unresolved question and hypothesis

The strongest available evidence supports a measurement concern, not this hypothesis. Haines et al. (CJASN 2023, DOI 10.2215/CJN.0000000000000203; inspected local readable text at `references/expert-seeds/papers/kidney-function/article.readable.txt`) studied 38 selected mechanically ventilated patients with paired creatinine, cystatin C, iohexol clearance and muscle measurements. They found creatinine-based kidney function increasingly overestimated measured function during prolonged critical illness. This does not establish the prevalence, prognostic value, or mechanism of a urine-output discordance phenotype in MIMIC-IV.

The falsifiable unresolved claim is:

> Among adults alive and still in their first ICU stay at 72 hours who meet an observed early-creatinine-AKI criterion and have adequate paired measurements, patients whose creatinine improves while Foley urine output does not recover have higher subsequent in-hospital mortality than patients with concordant creatinine and urine-output recovery.

This is a prognostic association about an observed phenotype. A positive result would motivate validation with cystatin C/measured GFR and prospective renal-monitoring studies; it would not show that creatinine recovery is harmful, that oliguria is the mechanism, or that any treatment should be started, stopped, delayed or continued.

## Population and temporal boundaries

Use MIMIC-IV v3.1. The primary unit is the first ICU stay within each `hadm_id`; adults have `hosp/patients.anchor_age >= 18`. Join:

- `icu/icustays` on `subject_id,hadm_id`, with `stay_id,intime,outtime,first_careunit,last_careunit,los`;
- `hosp/admissions` on `subject_id,hadm_id`, with `admittime,dischtime,deathtime,hospital_expire_flag`;
- `hosp/patients` on `subject_id`, with `anchor_age,gender`.

Exclude invalid ICU intervals, missing time-zero fields, and later ICU stays as primary index stays. Time zero is `t0 = icustays.intime + 72 hours`. Require `t0 < outtime` and no `admissions.deathtime <= t0`. All predictors end strictly before `t0`; follow-up begins at `t0`. Timestamps are MIMIC subject-shifted timestamps and are not compared across subjects.

Use the early window `[intime,intime+24h)`, rise window `[intime+24h,intime+48h)`, and recovery window `[intime+48h,intime+72h)`. A patient must have a valid creatinine in the early and recovery windows and a later rise candidate in the rise window. This later-window requirement repairs the previous wording that could mistake an early-only maximum for AKI.

## Observed AKI and discordant phenotype

Creatinine comes from:

- `icu/chartevents` itemid 220615 (“Creatinine (serum)”), using `stay_id,hadm_id,charttime,valuenum,valueuom`;
- `hosp/labevents` itemid 50912 (“Creatinine”, blood chemistry), using `subject_id,hadm_id,itemid,charttime,valuenum,valueuom`, joined to the index ICU by `hadm_id` and timestamp containment.

Join item labels through `icu/d_items` and `hosp/d_labitems`; retain only positive plausible mg/dL numeric values, record source and duplicate-resolution rules, and exclude or flag non-mg/dL values. Define `C_early` as the minimum early creatinine and `C_rise` as the maximum creatinine in the later rise window. Eligibility requires `C_rise >= C_early+0.3` mg/dL or `C_rise/C_early >= 1.5`; record continuous changes. Define `C_peak` as the maximum valid value in `[intime,intime+48h)` and `C_late` as the minimum valid value in the recovery window. Require `C_late <= C_peak-0.3` mg/dL or `C_late/C_peak <= 0.75` for creatinine recovery; preserve continuous versions for sensitivity analyses.

Foley output comes from `icu/outputevents` itemid 226559 (“Foley”), using `stay_id,charttime,value,valueuom`. Retain nonnegative mL values and aggregate to hourly bins. Do not treat missing charting as zero. For the primary weight-standardized phenotype require at least 12 observed hourly bins in each 24-hour urine window; repeat with >=18 bins as measurement-dense sensitivity. Weight comes from `icu/chartevents` itemids 226512 (“Admission Weight (Kg)”) or 224639 (“Daily Weight”), using `stay_id,charttime,valuenum,valueuom`; use the latest valid positive kg measurement available before the relevant window. If weight is unavailable, report an unweighted mL/hour analysis separately rather than silently mixing scales.

Define late urine recovery as late Foley volume per observed hour per latest weight >=0.5 mL/kg/hour, with the same coverage rule in the early window for the trajectory comparison. The primary contrast is:

- discordant: creatinine recovery + late urine-output non-recovery;
- reference: creatinine recovery + late urine-output recovery.

Retain the other two combinations descriptively and in secondary models. The primary phenotype is suspected discordance, not persistent renal dysfunction or a KDIGO adjudication.

## Outcomes

The primary outcome is in-hospital death after `t0`, using `admissions.deathtime` with the event required to be after `t0` and before `dischtime`; `hospital_expire_flag` is a consistency field, not a substitute event time. Report risks, risk differences or ratios with 95% intervals and a cause-specific time-to-event analysis as secondary.

Secondary outcomes are:

- later ICU readmission after the index `outtime` and before the same admission `dischtime`, from a later `icu/icustays` row with the same `hadm_id`; analyze only among patients discharged alive from the index ICU and treat death before readmission as competing;
- new charted renal replacement after `t0` from `icu/procedureevents` itemids 225441 (Hemodialysis), 225802 (Dialysis-CRRT), 225803 (CVVHD), 225805 (Peritoneal Dialysis), 225809 (CVVHDF), and 225955 (SCUF), using `starttime,endtime,stay_id,itemid`;
- death or new RRT as a descriptive composite, not a replacement for the primary outcome;
- ICU/hospital length of stay descriptively because discharge and death create selection and competing-risk concerns.

## Covariates and leakage controls

All predictors are measured at or before `t0). Use demographics and context from `patients`, `admissions`, and `icustays); creatinine levels, slopes, peaks, measurement counts and missingness; vital signs from `icu/chartevents`: 220181 NBP mean, 220045 Heart Rate, 220210 Respiratory Rate, and 220277 SpO2; lactate from `hosp/labevents` itemids 50813, 52442 or 53154; vasoactive exposure from `icu/inputevents` itemids 221906, 221662, 221749, 229630, 229631, 229632, 221289, 229617; ventilation from `icu/procedureevents` 225792 and 225794; pre-`t0` RRT using the listed RRT itemids; and a measured input-minus-output mL proxy from `icu/inputevents` and `icu/outputevents`.

Use `hosp/diagnoses_icd` joined to `hosp/d_icd_diagnoses` on `icd_code,icd_version` for an admission-coded CKD/ESRD proxy only. Do not use `deathtime`, `hospital_expire_flag`, later ICU stays, post-`t0` treatments, or post-landmark events as predictors. Every split is by `subject_id`, even if the primary row is a stay.

## Baseline and substantive alternative

The simple baseline is penalized logistic regression for post-`t0` death using age, sex, first care unit, observed-AKI/creatinine summaries, pre-landmark vital/lactate/vasopressor/ventilation/RRT indicators and missingness indicators, excluding Foley-output and fluid-trajectory features. It tests whether the renal phenotype adds information beyond a transparent creatinine-centered risk model.

The learned alternative is a CPU `HistGradientBoostingClassifier` or equivalent Harbor-available tree booster fit to the same outcome, eligibility, predictor boundary and subject-level held-out 20% test set. Create 6-hour bins from 0–72 hours for creatinine, Foley output, weight-standardized output, input-minus-output proxy, MAP, HR, respiratory rate, SpO2, lactate, vasoactive exposure, ventilation and RRT. Retain last, mean, minimum, maximum, slope, variability, measurement count and missingness per bin. Use grouped/nested cross-validation on the training subjects and one predeclared held-out test set. Fit a full model and a urine/fluid ablation on identical splits. Report AUROC, AUPRC, Brier score, calibration intercept/slope and bootstrap intervals. The learned model can reveal nonlinear timing, interactions and whether output trajectories add information that a snapshot loses; it is not used to rescue a failed primary phenotype contrast.

Budget is CPU-only, approximately two CPUs/4 GiB for bounded preprocessing and fitting, with no GPU requirement. If event support or coverage makes the model uncertainty uninterpretable, defer the alternative and preserve the primary phenotype estimate; do not replace the question with an easier model.

## Analysis, falsification and interpretation

First report cohort flow, item/stay support, phenotype counts, outcome counts, coverage and missingness by phenotype. Estimate the primary contrast with an adjusted robust logistic/binomial model and subject-clustered bootstrap or sandwich uncertainty; use a cause-specific Cox model only as a secondary check. Prespecify threshold sensitivity (absolute/relative creatinine), coverage thresholds, unweighted output, source-specific creatinine, and early-RRT exclusions.

Supportive evidence requires a directionally higher discordant risk with uncertainty excluding the null, persistence in measurement-dense and threshold analyses, and reproducible calibration/risk information from urine/fluid features beyond the baseline. Adverse evidence is a precisely near-null or reversed primary contrast, especially under dense coverage; an improved learned score alone cannot rescue this. Inconclusive evidence includes sparse events, phenotype-dependent missingness, failed calibration, unstable thresholds, or no support after the required compiled audit.

The verifier can check joins, temporal boundaries, reproducibility, estimates, uncertainty, leakage controls, and whether conclusions match computed outputs. It cannot establish measured renal function, mechanism, bedside utility, causal treatment effects, clinical adjudication, or external validity. Those require cystatin C/measured GFR, muscle/volume-status assessment, treatment indications, clinician review and an external or prospective study.

## Exact source and archive provenance

Dataset guide: `datasets/README.md`; MIMIC guide: `datasets/mimic/README.md`; snapshot `[source checksum]`. Full catalog: `[internal dataset path]`, [source checksum].

The read-only primary archive is `[internal dataset path]`, [source checksum]. Members and schemas:

- `mimic-iv-3.1/icu/icustays.csv.gz`, schema `datasets/mimic/table-7d5c8feb0fb0dbd4.json`;
- `mimic-iv-3.1/hosp/admissions.csv.gz`, schema `table-e8ec3e6e4c428559.json`;
- `mimic-iv-3.1/hosp/patients.csv.gz`, schema `table-9154f8c46cade9af.json`;
- `mimic-iv-3.1/icu/chartevents.csv.gz`, schema `table-8208609a785ea7e8.json`;
- `mimic-iv-3.1/icu/outputevents.csv.gz`, schema `table-a7ad1c4cdcdbfe0a.json`;
- `mimic-iv-3.1/icu/d_items.csv.gz`, schema `table-d1023acc404fd1d4.json`;
- `mimic-iv-3.1/hosp/labevents.csv.gz`, schema `table-bf701d962c63287c.json`;
- `mimic-iv-3.1/hosp/d_labitems.csv.gz`, schema `table-57ae65f0eb6cf1a6.json`;
- `mimic-iv-3.1/icu/inputevents.csv.gz`, schema `table-d193e854c19eb4ba.json`;
- `mimic-iv-3.1/icu/procedureevents.csv.gz`, schema `table-f6493e8403a0abe7.json`;
- `mimic-iv-3.1/hosp/diagnoses_icd.csv.gz`, schema `table-b12f3369d4b2601b.json`;
- `mimic-iv-3.1/hosp/d_icd_diagnoses.csv.gz`, schema `table-b0aa21973044b4bd.json`.

Required keys are `subject_id,hadm_id` for admissions/patients/diagnoses joins, `stay_id` for ICU events, `itemid` to dictionaries, and timestamp containment for hospital labs to ICU stays. All source files are read-only; derived cohort, audit and model outputs belong in workspace.

## Disposition of demonstrations and unused seeds

Delphi is adapted only as dated structured trajectory-vs-snapshot inspiration; its UKB cohort and Danish external validation are unavailable. ALADYNOULLI is not reproduced because genetics/full inputs are unavailable; an EHR-only latent alternative changes the question and is deferred. Oncoformer is not reproduced because images, full main text and complete STAR Methods are unavailable, and its lab-only cancer question is out of scope. The unused MIMIC seeds remain provenance/alternatives: diuretic timing and transfusion need treatment indications and time-varying confounding; sedation needs reliable depth and indication; hyperlactatemia and asynchronous organ recovery need stronger fixed phenotypes/outcome support; ICU-discharge residual instability remains a valid fallback if renal support fails. These are not conclusions or ranking claims.

Supporting method/reference notes: `work/episode2_method_and_reference_notes.md`.
