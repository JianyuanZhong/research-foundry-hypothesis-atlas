> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 9: observed renal-recovery discordance with a source-prioritized exact census

## Decision and unresolved clinical claim

This is a substantive successor to `[prior hypothesis]`. It keeps the parent’s clinically important, noncausal question but repairs the most consequential remaining execution risk: primary phenotype construction must be finishable without silently broadening the scan or changing the phenotype after seeing support.

The falsifiable hypothesis is:

> Among adults in the earliest valid ICU stay of a hospitalization who are alive and still in that ICU at a fixed 72-hour landmark, have an observed early creatinine rise, documented early Foley oliguria, apparent creatinine recovery by 72 hours, adequate pre-specified Foley observation in both the first and last 24-hour windows, and a baseline weight, patients whose observed Foley-recorded output remains below the recovery threshold have a higher probability of death before hospital discharge than patients whose output recovers.

This tests whether apparent biochemical recovery can be discordant with a second, clinically used recovery signal and identify residual risk. It does not test whether low recorded output is true oliguria, whether creatinine recovery reflects measured GFR, or whether changing treatment improves outcomes. A positive result could motivate prospective validation using complete urine capture, cystatin C, measured GFR, volume assessment and adjudicated catheter status before any bedside alert or treatment change.

The strongest available evidence is the local Haines et al. critical-illness study (CJASN 2023, DOI 10.2215/CJN.0000000000000203; `references/expert-seeds/papers/kidney-function/article.readable.txt` and PDF), which measured cystatin C, iohexol clearance and muscle in 38 ventilated patients and supports concern that creatinine-based estimates may overestimate kidney function during critical illness. It does not establish the MIMIC prevalence, prognosis, completeness of Foley capture, mechanism or causal meaning of this phenotype. The expert card `references/expert-seeds/cards/mimic-03.md` explicitly identifies measured kidney function as unavailable. The present estimand is therefore a conditional observed association.

## Actual scientific deliverable

The computation must newly produce, from the read-only snapshot:

1. `provenance.json`, `cohort_flow.csv`, `item_support.csv`, `phenotype_outcomes.csv`, a frozen one-row-per-hospitalization analytic table, and a machine-readable gate log;
2. exact support, duplicate, unit, chart-time/store-time and missingness counts for every retained item and flow gate;
3. the primary unadjusted and pre-48-hour covariate-standardized mortality risk difference and risk ratio for discordant versus concordant recovery, with subject-clustered bootstrap 95% intervals;
4. descriptive first post-landmark RRT, later same-admission ICU readmission, death-or-RRT and time-to-event summaries;
5. two newly fitted models on the same support-defined rows, target and subject-held-out split: a transparent ridge-logistic baseline and a six-hour binned nonlinear gradient-boosted-tree alternative, plus a urine/output ablation;
6. locked-test AUROC, AUPRC, Brier score, calibration intercept/slope and subject-cluster bootstrap uncertainty, with grouped feature-family ablations;
7. output-linked supportive, adverse or inconclusive classification.

No result, count or effect is claimed by this proposal.

## Read-only data bindings

The source is the exact archive in `datasets/mimic/README.md`:

- path `[internal dataset path]`;
- snapshot `[source checksum]`;
- archive [source checksum];
- catalog [source checksum].

(The snapshot identifier above is copied from the catalog and must be checked against the catalog at execution; a mismatch is a preflight failure.)

Primary and secondary archive members, table IDs, schema files and required columns are:

- `mimic-iv-3.1/icu/icustays.csv.gz`, `icu/icustays`, `datasets/mimic/table-7d5c8feb0fb0dbd4.json`: `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`.
- `mimic-iv-3.1/hosp/admissions.csv.gz`, `hosp/admissions`, `table-e8ec3e6e4c428559.json`: `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admission_location, discharge_location, insurance, language, marital_status, race, hospital_expire_flag`.
- `mimic-iv-3.1/hosp/patients.csv.gz`, `hosp/patients`, `table-9154f8c46cade9af.json`: `subject_id, gender, anchor_age`.
- `mimic-iv-3.1/icu/d_items.csv.gz`, `icu/d_items`, `table-d1023acc404fd1d4.json`: `itemid, label, linksto, category, unitname, param_type`.
- `mimic-iv-3.1/hosp/d_labitems.csv.gz`, `hosp/d_labitems`, `table-57ae65f0eb6cf1a6.json`: `itemid, label, fluid, category`.
- `mimic-iv-3.1/hosp/labevents.csv.gz`, `hosp/labevents`, `table-bf701d962c63287c.json`: `labevent_id, subject_id, hadm_id, specimen_id, itemid, charttime, storetime, value, valuenum, valueuom`; creatinine item IDs `50912, 52546`.
- `mimic-iv-3.1/icu/chartevents.csv.gz`, `icu/chartevents`, `table-8208609a785ea7e8.json`: `subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valuenum, valueuom`; creatinine `220615`, weight `226512, 224639`, and physiology `220181, 220045, 220210, 220277, 50813, 52442, 53154`.
- `mimic-iv-3.1/icu/outputevents.csv.gz`, `icu/outputevents`, `table-a7ad1c4cdcdbfe0a.json`: `subject_id, hadm_id, stay_id, caregiver_id, charttime, storetime, itemid, value, valueuom`; Foley `226559`.
- `mimic-iv-3.1/icu/procedureevents.csv.gz`, `icu/procedureevents`, `table-f6493e8403a0abe7.json`: `subject_id, hadm_id, stay_id, caregiver_id, starttime, endtime, storetime, itemid, value, valueuom`; RRT `225441,225802,225803,225805,225809,225955`, ventilation `225792,225794`.

The executable must first read all corresponding schema JSON and verify columns, member names, schema hashes and the archive hash. The dictionary pass must verify labels/linkage/units, including serum creatinine `220615` linked to chartevents, laboratory creatinine `50912/52546`, Foley `226559` linked to outputevents with mL, and weights `226512/224639` with kg. It must stop on a mismatch rather than remap items.

Join `icustays` to `admissions` on `(subject_id,hadm_id)`, to `patients` on `subject_id`, and measurement rows to the ICU stay on `stay_id`, checking the redundant subject/admission keys. Hospital labs join on `(subject_id,hadm_id)` and are retained only inside the selected ICU interval. No note text, radiology text, images or waveform data are needed; the catalog states images and raw waveforms are unavailable. Diagnoses are not required because a discharge-coded CKD/ESRD proxy would not be onset-timed.

## Feasible exact census and source-priority repair

Stage 1 streams only the three small tables, selects the earliest valid ICU stay per hospitalization ordered by `intime, stay_id`, and creates an eligible-key file with the exact interval `[intime,outtime)`, 72-hour eligibility and discharge fields.

Stage 2 performs one buffered sequential pass over each needed archive member. It tests key and item membership before timestamp/value conversion and writes only whitelisted fields for eligible keys to compact workspace files. It never materializes a multi-gigabyte member. The primary path is `chartevents + outputevents` for ICU creatinine, weight, physiology and Foley; `labevents` is scanned once for the two hospital-creatinine IDs and is a required source-specific sensitivity, not a reason to change the primary phenotype. A completed-member checkpoint contains the archive/member hash, row count, retained count and code hash. A member timeout yields an incomplete audit and no scientific fit; it cannot trigger sampling, a creatinine-only fallback or relaxed phenotype rules.

Stage 3 deterministically reduces retained rows. Clinical `charttime` defines windows and relative time; procedure `starttime) defines post-landmark procedures; a value is primary as-observed only when nonmissing `storetime <= t0`. Late/missing storage rows are retained in diagnostics and excluded from the primary support. Exact duplicate signatures are removed before aggregation, excluding caregiver/provenance identifiers; same-time valid creatinine values are combined by median and source/disagreement flags are retained. Units are not silently converted.

## Population and phenotype

The unit is one hospitalization’s earliest valid ICU stay. Require adult `anchor_age >= 18`, valid `intime < outtime`, `intime + 72h < outtime`, discharge after the landmark, and no `deathtime <= t0`. The analysis is conditional on surviving and remaining in the ICU through t0. Multiple hospitalizations may contribute, but splits and bootstrap resampling cluster by `subject_id`.

Use half-open windows W0=[0,24h), W1=[24,48h), W2=[48,72h). Require at least one storage-available creatinine in each window. Let C0=min(W0), C1=max(W1), Cpeak=max(W0∪W1), Clate=min(W2). An observed early rise is C1 >= C0+0.3 mg/dL OR C1/C0 >= 1.5; apparent recovery is Clate <= Cpeak-0.3 mg/dL OR Clate/Cpeak <= 0.75. Preserve continuous values and each component; these are not KDIGO labels.

For Foley item 226559, retain nonnegative mL values, remove exact duplicates, bin by relative chart hour and sum per hour. In both W0 and W2 require at least 18 distinct observed hours, first-last span at least 20 hours and maximum gap at most 4 hours. Divide recorded output by the full 24-hour window and positive W0 weight, not observed hours. Require W0 output <0.5 mL/kg/hour. W2 recovery is >=0.5 and non-recovery <0.5. Zero is observed zero; absence is missing. This is dense chart support, not proof of complete Foley capture.

Weight is the first positive W0 value from 226512, otherwise 224639, with charttime in W0 and storage available by t0; if both occur at the same time, 226512 wins. Record source and timing. The primary groups are:

- discordant: early rise + apparent creatinine recovery + early observed oliguria + dense Foley/weight support, with W2 Foley non-recovery;
- concordant: the same eligibility criteria with W2 Foley recovery.

Report all four creatinine rise/recovery cells, low-density and charttime-only versions, and missing/late-weight exclusions. Do not replace the paired question with a creatinine-only analysis if primary support fails.

## Outcomes, analysis and uncertainty

Primary death is `t0 < deathtime <= dischtime`; `hospital_expire_flag` is a consistency check. Reconcile impossible/missing dates and flag/date discrepancies before interpretation. The primary estimand is the observed probability difference and ratio before discharge between discordant and concordant groups. Report risks and subject-clustered percentile-bootstrap 95% intervals, then a standardized associational contrast from ridge logistic adjustment using only information through 48 hours: age, sex, careunit/admission context, W0 weight, C0/C1/rise severity, W0 Foley amount/coverage and pre-48 MAP, HR, RR, SpO2 and lactate summaries/counts/missingness. Never adjust for W2 Foley, W2 density, Clate, post-t0 treatments or outcome-derived variables.

Secondary outcomes are first qualifying RRT procedure after t0 and before dischtime, later ICU readmission within the same admission using a later `icustays.intime > index.outtime`, and death-or-RRT. They remain descriptive and do not replace mortality.

The model target is post-t0 in-hospital death. The prediction population is frozen before final group labeling: all primary-support stays with observable outcome, including both groups. Split by SHA-256 of `subject_id || "renal-discordance-episode9"` into 60% train, 20% validation, 20% locked test, keeping subjects together. The baseline is ridge logistic with one-hot categorical and standardized continuous predictors: demographics/context, W0 weight, creatinine trajectory through t0, physiology summaries, counts and missingness; it excludes every Foley amount, normalized-output and output-density feature. Select a small lambda grid by validation Brier score only.

The substantive alternative is CPU histogram gradient-boosted trees on six-hour bins over [0,72h), using last/mean/min/max, slope when defined, count and missingness for creatinine, Foley mL/hour and normalized Foley output, MAP, HR, RR, SpO2, lactate, ventilation flags and pre-landmark RRT. The ablation removes amount, normalized-output and output-density features. It can reveal persistence, timing, threshold nonlinearity and interactions lost by terminal summaries. It is selected over a transformer or latent GP because this question needs inspectable temporal ablations under the exact-census budget; a mechanistic fluid model is deferred because complete intake/output, volume status, catheter intent and treatment indication are unavailable.

Require at least 20 deaths and 20 non-deaths in each train and locked test and estimable calibration. Report held-out AUROC, AUPRC, Brier, calibration intercept/slope, subject-cluster bootstrap intervals and feature-family ablation. A small metric gain is not a clinical success.

## Falsification and interpretation

Run dense versus 18-hour coverage, maximum-gap strata, storage-available versus charttime-only, ICU-chart-only versus hospital-lab-only versus combined creatinine, absolute-only versus relative-only recovery rules, 0.5-threshold and unweighted mL/hour sensitivity, alternate eligible weight, exclusion of pre-t0 RRT, full versus urine/output-ablated versus density-only models, within-stay Foley timestamp permutation preserving values/counts/windows, and label permutation within support/creatinine strata.

Supportive requires both cells >=50 stays and >=10 deaths each, adjusted and unadjusted contrasts above the null with a 95% interval excluding it, direction retained across source/coverage/threshold checks, process and timestamp permutations not explaining it, and reproducible calibrated urine/output information beyond baseline. This supports only a conditional observed prognostic signal.

Adverse is a precise null/reversal under adequate support, especially under dense storage-available data, or attenuation attributable to source/coverage/process controls. A temporal model gain without the primary phenotype contrast is adverse for the discordance claim, not a rescue.

Inconclusive applies to inadequate paired support/events, irreconcilable outcome dates, differential observability inseparable from phenotype, failed permutation, unstable calibration/bootstrap, schema/item mismatch, incomplete member checkpoint or resource watchdog failure. Thresholds cannot be relaxed after inspection. The verifier can check computation, output linkage and uncertainty; it cannot establish complete Foley capture, true GFR, mechanism, causality, treatment benefit, utility or external validity. Those require adjudication, additional measurements or another cohort.

## Demonstration and seed dispositions

Delphi demonstrates that dated structured trajectories can add information beyond snapshots; its UK Biobank/Danish validation setting is absent, so only the inspectable temporal comparison is adapted. ALADYNOULLI demonstrates longitudinal latent modeling, but the genetic inputs and exact reproduction dependencies are unavailable; an EHR-only latent model is deferred because it would not resolve the present measurement-process uncertainty. Oncoformer demonstrates multimodal longitudinal learning, but the main text/STAR Methods and chest-X-ray images are unavailable; no reproduction is claimed and the lab-only precedent does not supersede this design.

The MIMIC seeds were retrieved and assessed: mimic-03 is the direct parent idea; mimic-01 overlaps asynchronous organ recovery but lacks a more specific adjudicable recovery signal; mimic-02 has strong indication/confounding problems for causal diuretic timing; mimic-04 lacks microcirculatory and selective-lactate evidence; mimic-05 has selective HbA1c and anemia/transfusion limitations; mimic-06 lacks indication-resolved sedation depth; mimic-07 lacks source-control and result-availability timing; mimic-08 lacks validated congestion and causal decongestion data; mimic-09 lacks reliable ischemia/bleeding ascertainment and causal identification; mimic-10 lacks fully specified discharge selection, destination and competing-risk definitions. These are retained as repairable provenance, not discarded as false.
