# Transportability of recorded support patterns after the first ICU outtime

## Scientific deliverable

The solver must newly fit an auditable MIMIC-IV 3.1 study and produce:

1. `cohort_audit.parquet`, one row per candidate first ICU stay, with first-stay selection, adult eligibility, temporal ordering, complete 12-hour window, domain coverage, and exclusions;
2. `hourly_features.parquet`, twelve one-hour rows in the locked pre-outtime window, support-evidence ledger, physiology, masks, and no post-outtime predictors;
3. `selection_audit.parquet`, the full target population of eligible first ICU outtimes, coverage-eligibility indicator, landmark covariates, fitted inclusion probabilities, weights, overlap, and leave-one-group-out checks;
4. `support_observation_audit.parquet`, distinguishing positive recorded evidence, observed non-positive values, uninformative absence, contradiction, and invalid timing;
5. locked patient-level train/validation/test predictions and standardized 6-, 24-, and 48-hour CIFs for first ICU return, in-hospital death, and alive hospital discharge;
6. marginal, observation/process-adjusted, and target-standardized contrasts under the selection weights and missing-support sensitivity grid;
7. a transparent cause-specific discrete-time hazard baseline and a same-input two-domain observation-aware hidden semi-Markov alternative, with calibration, IPCW Brier score, bootstrap uncertainty, overlap, state and transport diagnostics; and
8. `interpretation.md` plus a machine-readable table mapping every conclusion to a computed output, estimate, interval, event count, effective sample size, weight range, and sensitivity result.

Completion means these quantities, uncertainty intervals, selection diagnostics, falsifications, and interpretation links have been newly fitted or estimated on the locked test set. It does not mean that a discharge policy, causal effect, or clinical readiness label has been established. This proposal asserts no fitted result.

## Unresolved question and falsifiable hypothesis

The parent repairs the immediate observation-identifiability error: no chart row is not treated as proof that support was absent, and unrecorded support is varied on a locked sensitivity grid. A separate clinically important problem remains. The primary contrast is estimated only among first ICU outtimes with adequate respiratory and MAP observation coverage. Coverage is plausibly related to care unit, admission pathway, ICU intensity, and discharge workflow. A useful contrast in well-documented stays may not describe the broader set of patients for whom an ICU-to-ward transition is considered. Stratifying after the fact is not a transportability analysis, and the local tables do not reveal the counterfactual outcome or support state for sparse records.

The strongest claim supported before fitting is only that MIMIC contains linked, dated ICU observations, support intervals, admissions, transfers, and outcomes from which a *recorded-support evidence* competing-event estimand can be constructed. The source catalog, schema JSONs, and header/dictionary checks establish field and key availability, not an association, clinical truth, or transportability. The local demonstrations motivate sequence ordering and observation-process modeling; they are not reproduction targets, and the unavailable main article/full STAR Methods of the cancer demonstration are not used as evidence.

The unresolved claim is:

> Among adults at an observed first ICU outtime, does recent recorded respiratory or vasoactive withdrawal, versus durable recorded-off evidence, predict the mutually exclusive first ICU return, in-hospital death, or alive hospital discharge within 48 hours, and is that recorded-evidence CIF contrast materially preserved when the coverage-eligible analysis is standardized to all otherwise eligible first ICU outtimes?

The primary claim remains prognostic and record-based. The transport claim is conditional on measured selection assumptions: inclusion in the coverage-eligible subset is exchangeable given prespecified landmark covariates and has positivity. Those assumptions are not identified by MIMIC. A contrast that survives observation adjustment but fails transport overlap is not a broadly applicable bedside signal.

## Clinical importance and substantive advance

ICU return and death soon after an ICU outtime are consequential outcomes, while alive hospital discharge is a competing event that changes the opportunity for ICU return. If the signal is stable after standardization, it could justify prospective evaluation of a record-based reassessment trigger across units and admission pathways. If it is restricted to highly documented patients, the clinically important result is that apparent support-transition risk cannot be assumed to generalize to ordinary documentation conditions.

The advance over the parent is a distinct selection/transportability estimand, not a small predictive gain. It separates: (i) the recorded evidence contrast, (ii) observation-process robustness, and (iii) the population to which the contrast can defensibly be applied.

The analysis will not call a patient safe or unsafe for discharge. MIMIC does not contain a randomized or well-defined alternative of continued ICU care, so this is not an estimate of the effect of discharge, stopping support, ward monitoring, or a clinical policy. Decision relevance is limited to whether the prognostic contrast is calibrated and transportable enough to motivate external/prospective testing; clinical utility and action thresholds require expert review and another study.

## Population, landmark, target, and temporal boundaries

Use the read-only ZIP `[internal dataset path]`, catalogued as MIMIC snapshot `[source checksum]` with ZIP [source checksum]. Archive members are under `mimic-iv-3.1/`. Preserve the complete catalog at `[internal dataset path]` (catalog [source checksum]). Workspace copies of exact metadata are under `datasets/mimic/`.

Select exactly one index stay per subject: the earliest valid `icu/icustays.intime` across all admissions, tied by smallest `stay_id`. Require `patients.anchor_age >= 18`, valid `subject_id,hadm_id`, `intime < outtime < dischtime`, non-null `dischtime`, no `deathtime <= outtime`, and a complete `[outtime-12 hours,outtime)` window. Retain MIMIC anchor-age 91 as top-coded. The target population T is every candidate first stay satisfying these rules, regardless of respiratory/MAP coverage. The primary observed-data population A is T with at least two respiratory observation bins per six-hour half and at least two MAP bins per half. Do not impute the exposure for T minus A.

The landmark is `icustays.outtime`. Predictors use only the left-closed/right-open window `[outtime-12h,outtime)`, split into twelve one-hour bins and preceding/final six-hour halves. Use `charttime` for charted observations and valid `starttime,endtime` overlap for intervals. `storetime` is never clinical time and is used only in a negative timing control. No post-outtime note, transfer, discharge field, or outcome enters predictors. MIMIC times are subject-shifted; only within-subject intervals are compared.

Follow-up is `[outtime,min(outtime+48h,dischtime))`. Mutually exclusive first events are unchanged from the parent:

- first later `icustays.intime > outtime`, same `hadm_id), within 48 hours: ICU return;
- `admissions.deathtime` before a counted return: in-hospital death;
- `admissions.dischtime` before either event: alive hospital discharge.

Use event times, not row order. If death and ICU return are equal within one minute, death is first; if alive discharge ties another event, the non-discharge event is first. Repeat with 0- and 5-minute tie tolerances. Aggregate ICU return is primary; transfer-topology confirmation is secondary and never relabelled planned, unplanned, or deterioration.

## Exact MIMIC bindings, joins, and source members

All source paths below are read-only. Every table is bound to its local schema JSON, source ZIP, and archive member.

- `hosp/admissions`: `datasets/mimic/table-e8ec3e6e4c428559.json`, member `mimic-iv-3.1/hosp/admissions.csv.gz`; columns `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`. Join to ICU by `subject_id,hadm_id`. Use `dischtime,deathtime` only for outcomes and context fields only when known before outtime; `discharge_location` is post-landmark audit only.
- `hosp/patients`: `datasets/mimic/table-9154f8c46cade9af.json`, member `mimic-iv-3.1/hosp/patients.csv.gz`; columns `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`. Join by `subject_id); do not use `dod`.
- `icu/icustays`: `datasets/mimic/table-7d5c8feb0fb0dbd4.json`, member `mimic-iv-3.1/icu/icustays.csv.gz`; columns `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`. Use for first-stay selection, landmark, ICU-return linkage, and care-unit strata.
- `hosp/transfers`: `datasets/mimic/table-685b6b74d0d7c547.json`, member `mimic-iv-3.1/hosp/transfers.csv.gz`; columns `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`. Join by `subject_id,hadm_id`; count only transfers ending no later than index outtime for selection/process covariates. Post-landmark rows are secondary topology only.
- `icu/chartevents`: `datasets/mimic/table-8208609a785ea7e8.json`, member `mimic-iv-3.1/icu/chartevents.csv.gz`; columns `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`. Join events by `subject_id,hadm_id,stay_id`; use item IDs 220045 HR, 220052 arterial MAP, 220181 NIBP MAP, 220210 RR, 220277 SpO2, 223834 O2 flow, 223835 FiO2, 220339 PEEP, and 223761/223762 temperature.
- `icu/d_items`: `datasets/mimic/table-d1023acc404fd1d4.json`, member `mimic-iv-3.1/icu/d_items.csv.gz`; columns `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue`. Join by `itemid` to verify labels, source table, and units before fitting.
- `icu/inputevents`: `datasets/mimic/table-d193e854c19eb4ba.json`, member `mimic-iv-3.1/icu/inputevents.csv.gz`; columns `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,patientweight,totalamount,totalamountuom,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate`. Use only valid interval overlap. Vasoactive IDs are 221906 norepinephrine, 221289/229617 epinephrine, 221662 dopamine, 221749/229630/229631/229632 phenylephrine, and 222315 vasopressin. Never use `storetime` as support time.
- `icu/procedureevents`: `datasets/mimic/table-f6493e8403a0abe7.json`, member `mimic-iv-3.1/icu/procedureevents.csv.gz`; columns `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,value,valueuom,location,locationcategory,orderid,linkorderid,ordercategoryname,ordercategorydescription,patientweight,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate`. Use IDs 224385 intubation, 227194 extubation, and 225794 non-invasive ventilation only to corroborate transitions, never to assert continuous ventilation.
- `icu/outputevents`: `datasets/mimic/table-a7ad1c4cdcdbfe0a.json`, member `mimic-iv-3.1/icu/outputevents.csv.gz`; columns `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valueuom`. Optional observation-coverage descriptor only; not a kidney endpoint.
- `hosp/d_labitems`: `datasets/mimic/table-57ae65f0eb6cf1a6.json`, member `mimic-iv-3.1/hosp/d_labitems.csv.gz`; columns `itemid,label,fluid,category`. Join to `hosp/labevents` by `itemid` only to verify labels for optional pre-landmark lab covariates.
- `hosp/labevents`: `datasets/mimic/table-bf701d962c63287c.json`, member `mimic-iv-3.1/hosp/labevents.csv.gz`; columns `labevent_id,subject_id,hadm_id,specimen_id,itemid,order_provider_id,charttime,storetime,value,valuenum,valueuom,ref_range_lower,ref_range_upper,flag,priority,comments`. Optional descriptive pre-landmark covariates after d_labitems label verification; never use post-outtime labs.
- `note/discharge`: `datasets/mimic/table-69be322e2b58015b.json`, ordinary file `[internal dataset path]`; columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`. Documentation audit only; exclude text.
- `note/discharge_detail`: `datasets/mimic/table-18d43f38e33d1fd2.json`, ordinary file `[internal dataset path]`; columns `note_id,subject_id,field_name,field_value,field_ordinal`. Availability/exclusion audit only.

All joins are patient-to-admission `subject_id,hadm_id`, ICU event linkage `subject_id,hadm_id,stay_id`, and patient-level split key `subject_id`. Any source row failing these keys or the time window is audited and excluded from that feature, never silently reassigned.

## Exposure and observation ledger

Summarize each physiology channel per hour by median, last value, range, slope, and final-minus-preceding-half change when present. Keep arterial and NIBP MAP separate and convert Fahrenheit only by an auditable rule. Positive respiratory evidence is a valid charted O2 flow >2 L/min, FiO2 >0.21, PEEP >0, or procedure corroboration of intubation/NIV. Positive vasoactive evidence requires valid overlap of a listed inputevents interval. For each domain and half-hour, classify positive evidence, observed non-positive value, no qualifying row, contradiction, or invalid timing.

The primary four-category recorded exposure is defined only in A: durable recorded-off (no positive evidence in either half, with at least two respiratory bins and two MAP bins per half); recent respiratory withdrawal (positive respiratory evidence in the preceding half, none in final half, with the same coverage); recent vasoactive cessation (valid vasoactive interval in preceding half, none in final half, with MAP coverage); and both recent withdrawal evidence. “None” means no positive recorded evidence, not continuous absence. Retain active, residual, uninformative, discordant, and inadequate-coverage strata in counts and secondary outputs.

Define q_dh as the probability that an uninformative no-row hour was actually positive support. Evaluate the locked grid q_dh in {0, .10, .25, .50, .75, 1.00}, including shared-q, domain/half-specific, and higher-q vasoactive scenarios. Do not randomize observed non-positive respiratory values. Report label changes, effective sample size, overlap, and the smallest maximum q at which sign, interval compatibility with zero, or clinical interpretation changes. This is sensitivity analysis, not an identified correction.

## Selection/transport estimand and analysis

The primary estimand is unchanged: the standardized absolute CIF contrast between each recorded exposure category and durable recorded-off in A at 6, 24, and 48 hours for each competing event. The primary contrast is not replaced or diluted.

The new secondary estimand is the same contrast for target distribution T, transported from A using only landmark-available variables Z:

`Z = anchor_age, gender, anchor_year_group, admission_type, admission_location, insurance, language, marital_status, race, first_careunit, ICU LOS, pre-index transfer count/last careunit`.

Fit P(S=1|Z), where S=1(A), on training subjects only; select model complexity and weight truncation on validation only; lock on test subjects. Use stabilized generalizability weights proportional to P(S=1)/P(S=1|Z), with prespecified 1st/99th percentile truncation selected on validation. Report truncated and untruncated analyses, target/analysis sizes, standardized mean differences before/after weighting, and exposure-specific positivity/effective sample size. Standardize model-predicted cause-specific hazards/CIFs over T; do not invent exposures or outcomes for S=0. A transport result is reportable only with adequate overlap and without weight domination.

A subtle but important boundary is that selection covariates must be defined for every T row. Twelve-hour observation-bin counts and channel counts are outcomes of the coverage rule and are not used in P(S|Z) when undefined for T. Physiologic exposure features remain restricted to A. This makes the secondary estimate a generalizability analysis under explicit assumptions, not an imputation of missing support.

As transport falsifications, repeat with each first careunit, admission type, and anchor-year group as a pseudo-target, and perform leave-one-group-out transport from the remaining groups. A large failure, extreme weights, or materially different weighted and unweighted contrasts is evidence against generalizability. Include complete-case versus coverage-restricted comparisons and the full q grid. Do not condition on discharge_location, post-outtime transfers, discharge documentation, or any outcome in Z.

## Baseline and substantive alternative

Both methods use exactly the same A cohort, static covariates, twelve-hour channel matrix, support flags, masks, selection covariates, and locked splits. Neither uses narrative text, discharge_location, post-outtime records, or dod.

The simple transparent baseline is pooled cause-specific discrete-time hazards at 1, 6, 24, and 48 hours for ICU return, death, and alive discharge. Fit nested models for recorded physiology/support evidence, observation masks only, process/context only, and the full observed-data model. Predictors include the four exposure categories, final/preceding physiology summaries, source-specific masks, and Z covariates. Standardize predictions first to A for primary CIFs and then to T with locked selection weights. Refit the full model under each q recoding. Use absolute competing-event CIF as the clinical estimand; hazard ratios are secondary.

The substantive alternative is a two-domain factorized hidden semi-Markov model over the twelve hourly bins. Respiratory and hemodynamic latent chains have duration distributions and constrained transitions for persistence and withdrawal ordering. Emissions use the same physiologic values, support evidence, and masks. An explicit observation model uses the same channel masks, row counts, and history; the event head estimates post-outtime cause-specific hazards conditional on posterior state uncertainty and Z. Fit emissions, transitions, observation model, event head, and selection weighting on training data; choose state number, duration restrictions, regularization, and q implementation on validation; lock test posteriors and CIFs.

The baseline preserves transparent absolute contrasts and reveals whether observation and selection fields carry most association. The HSMM can reveal whether ordering and duration of respiratory/hemodynamic recovery add reproducible information that fixed summaries lose, and whether that information remains transportable after selection weighting. It is not justified by complexity alone. Report it only if latent states have reproducible domain/order meaning, entropy is acceptable, split stability holds, and transport is not a calibration-only artifact. If state meaning or transport fails, the baseline and uncertainty are the reportable result. A GRU/TCN is deferred because it adds capacity without resolving exposure missingness or coverage selection. Causal discharge-policy, validated readiness-text, adjudicated renal-recovery, raw waveform, and MIMIC-CXR image branches are deferred because intent, validated labels, adjudicated endpoints, raw waveforms, and images are unavailable.

## Splits, uncertainty, and evaluation

Use subject-level 70/15/15 train/validation/test splits with seeds 17, 29, and 43; no subject crosses partitions. Item mapping, thresholding, imputation, exposure recoding, selection model, weight truncation, HSMM state choice, and q implementation are learned or selected without test outcomes. The final test report must include patient-bootstrap 95% intervals, event counts, positivity, effective sample size, weight range, calibration intercept/slope, IPCW Brier score, calibration plots, and secondary AUROC. Bootstrap subjects, not rows or random seeds, using paired resamples for baseline/HSMM contrasts when possible.

Required falsifications are: shuffle hourly time labels while preserving values, masks, and support totals; remove masks, use masks only, remove support evidence, and use physiology/support only; replace charttime with storetime as a negative timing control; replace interval-overlap coding with last-value coding and remove procedure corroboration; separate arterial from NIBP MAP and FiO2/O2-flow/PEEP channels; vary window length, support thresholds, coverage thresholds, and 0/1/5-minute tie tolerance; use a pseudo-landmark six hours before outtime with a leakage-safe outcome window; perform first-careunit, admission-type, and anchor-year subgroup and leave-one-group-out transport checks; compare aggregate return with transfer-topology-confirmed/unconfirmed return; compare competing-discharge analysis with discharge-as-censoring; report complete-case, coverage-restricted, weighted, unweighted, and q-grid results; and audit excluded/contradictory intervals and post-outtime leakage.

## Supportive, adverse, and inconclusive gates

Supportive evidence requires a prespecified recorded-evidence CIF contrast with adequate event support and overlap; calibrated baseline and, if claimed, reproducible HSMM states; stable bootstrap intervals; persistence across source/time falsifications and the q range; and a weighted target contrast directionally and clinically materially compatible with A without weight domination. This supports a retrospective, transport-conditional association with recorded evidence only. It does not support continuous support cessation, discharge safety, or a treatment effect.

Adverse evidence includes reversal or collapse under observation adjustment or q sensitivity; dependence on storetime, one channel, last-value coding, or procedure corroboration; non-positivity; extreme or unstable selection weights; large leave-one-group-out failures; or HSMM states without reproducible meaning. These argue against the relevant physiology or transport interpretation, not against discharge itself.

Inconclusive evidence includes sparse strata/events, wide intervals, high state entropy, unstable splits, contradictory timing, q frontier inside the locked plausible range, target regions with no support, or a weighted estimate driven by few subjects. Inconclusive does not mean safe or unsafe.

Even supportive results cannot establish causal effects of stopping support, appropriateness or preventability of ICU discharge, clinician intent, goals of care, treatment limitation, ward surveillance, planned versus unplanned return, or transportability to another hospital. Expert chart/device adjudication, ward monitoring, external validation, and a prospective or causal study are required. discharge_location and discharge-note text can be audited after the landmark but cannot supply missing counterfactual or intent labels; full text is not silently treated as adjudication.

## Compute, provenance, and measured versus unverified facts

The configured discovery allowance is 7,200 science seconds with concurrency 2. The solver planning envelope is up to 16 CPUs, 262,144 MiB RAM, 8 allocated GPUs, and 28,800 seconds, while execution must request resources explicitly. This discovery episode performed no cohort extraction, model fit, CIF calculation, or GPU probe, so there are no measured scientific runtimes or results. The inherited parent recorded that source archive/member/header and d_items availability probes completed in under one second; that is a measured access probe, not a model-runtime estimate.

Unverified planning estimates are 10–30 minutes for streaming extraction/materialization, under 30 minutes for the CPU baseline plus selection-weighted bootstrap if derived tables are cached, and 1–4 hours for repeated HSMM optimization, q-grid evaluation, and transport bootstrap. These are estimates, not measurements. Start with CPU for extraction, selection modeling, and baseline. Request an allocated A100 only if a bounded HSMM profile shows material matrix-operation benefit; inside an allocation use cuda:0 and explicitly move model/tensors to it. Ordinary shells intentionally expose no CUDA, so a shell probe cannot establish GPU absence. Use cached ehr-campaign-cpu:20260908 or ehr-campaign-gpu:20260908 as appropriate, declare imports, checkpoint long fits, and report wall time, CPUs, RAM, GPU allocation, retries, and output hashes.

All source archives and table members remain read-only. Derived tables, logs, checkpoints, split manifests, selection models, and interpretation files belong in the workspace. Preserve exact ZIP/catalog/schema provenance and identify which claims are computationally checked versus those requiring clinical adjudication, missing evidence, external validation, or another study.
