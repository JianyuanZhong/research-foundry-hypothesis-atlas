# Residual instability before ICU-to-ward transfer: adjudicated first-transition prioritization

Status: proposed substantive child of `[prior hypothesis]`. No outcome model has been fit, no prediction result is claimed, and the fixed scientific question is unchanged. This child repairs the meaning of live discharge, selects a first-transition landmark estimand over recurrent-state alternatives, and defines the exact monitoring-prioritization claim the event-time extension can and cannot support.

## Substantive advance and endpoint finding

The parent established that exact event timing matters but treated every `admissions.dischtime` before a later event as a live discharge. A new bounded exact-cohort audit shows that this interpretation is wrong for the 22 highlighted conflicts: all 22 have `hospital_expire_flag=1` and `discharge_location='DIED'`; 20 have a later `deathtime` within 48 hours and two have a later ICU return before death. They are administrative timestamp discordances, not observed live discharge followed by readmission or death. The median `deathtime-dischtime` gap among these 22 is 19.72 hours (range 2.0–23.25 hours). The fixed raw adverse label remains correct and unchanged.

The audit also found 33 additional first-dischtime records within 48 hours with `discharge_location='DIED'` but no structured ICU return or death within the horizon. These cannot be called live discharge or confidently called alive/in hospital. They require an explicit unresolved endpoint category or clinical adjudication. Under the frozen parent's literal-dischtime rule, first states were 1,999 ICU returns, 586 deaths, 9,950 apparent live discharges, and 36,622 without a first event. Under the structured valid-live-discharge rule defined below, before excluding unresolved records, the corresponding states are 2,001 ICU returns, 606 deaths, 9,895 valid live discharges, and 36,655 without a resolved transition. These are endpoint-feasibility counts, not fitted outcome results.

The same audit found only 18 patients with two ICU returns in 48 hours and 55 deaths after an ICU return. A recurrent/nonabsorbing model would therefore estimate sparse post-return transitions and answer a new question about care after the first failure. For the frozen decision at `t0`, the scientifically adequate alternative is a first-transition competing-risk landmark model with an endpoint-adjudication gate, not a recurrent model or a rolling landmark.

## Evidence boundary, question, and decision

The strongest inspected evidence supports three bounded claims. A longitudinal MIMIC-IV/external-hospital model predicted seven-day ICU readmission/death better than SWIFT, while explicitly noting unresolved operational factors, treatment limitation, and distinct composite-component trajectories [K1]. A systematic review found that longitudinal predictors can improve ICU-readmission prediction but windows and composite definitions vary substantially [K2]. Measurement timing and frequency in EHR data encode healthcare processes as well as patient state [K3].

The strongest evidence available here now additionally supports only an endpoint statement: live discharge is common and time-dependent, and some MIMIC `dischtime` values are administrative hospitalization-close times rather than evidence of live discharge. Neither the literature nor the endpoint audit establishes that T1 improves prediction, that trajectory signal is physiologic, or that monitoring changes outcomes.

**Frozen primary hypothesis.** In the fixed adult first ICU-to-general-ward cohort and decision-time information set, T1's prespecified final-24-hour value-trajectory features improve held-out 48-hour raw three-state prediction over S0. The primary estimand remains paired test-set `Brier(S0)-Brier(T1)`.

**Revised event-time hypothesis.** Relative to a matched S0 first-transition model, the T1 first-transition model improves calibrated cumulative-incidence prediction of ICU return or in-hospital death through 48 hours, and its gain is not confined to valid live-discharge prediction.

**Consequential decision being evaluated.** At `t0`, a ward/rapid-response service with a fixed review capacity must rank newly transferred patients for enhanced clinical review or monitoring eligibility during the next 24 or 48 hours. The computable decision estimand is whether a T1-based worklist captures more observed first ICU-return/death transitions than its matched S0 worklist at identical frozen quotas. This is prioritization performance, not proof that monitoring, delaying transfer, or retaining an ICU bed benefits anyone. Establishing benefit requires an intervention, uptake, harms/costs, true capacity, and prospective or quasi-experimental outcome data not present in MIMIC.

The leading rival remains operational selection: transfer pathway, destination, treatment limitation, charting, and hospital discharge processes may explain prediction or remove opportunities for an in-hospital return. The selected analysis distinguishes that rival by modeling valid live discharge as a competing transition and reporting destination/service/treatment-limit sensitivity. Adjustment cannot prove physiology or eliminate unmeasured operations.

## Frozen population, landmark, information set, and raw target

Retain the parent verbatim:

- one row per hospitalization's first eligible adult ICU-to-frozen-general-ward transfer after ICU LOS at least 24 hours;
- `t0 = icu/icustays.outtime`, with exact successor `hosp/transfers.intime=t0` on nonmissing `subject_id,hadm_id`;
- the 17-value primary destination set: Medicine, Neurology, Med/Surg, Medicine/Cardiology, Transplant, Vascular, Med/Surg/GYN, Surgery/Trauma, Med/Surg/Trauma, Surgery, Cardiac Surgery, Medical/Surgical (Gynecology), Surgery/Pancreatic/Biliary/Bariatric, Cardiology, Thoracic Surgery, Oncology, and Hematology/Oncology; preserve the parent's step-down sensitivity;
- final-24-hour exposure exactly `[t0-24h,t0)`;
- chart predictors require both `charttime<t0` and `storetime<t0`, with `charttime` used for biological bins;
- input/procedure predictors require exposure-window interval overlap and `storetime<t0`;
- subject split seed 20260923, 60/20/20 train/validation/test, all admissions of a subject kept together, validation-only model selection/calibration, and one test opening;
- all S0 features, T1 formulas, item mappings, plausibility limits, O1 observation-process comparator, L1/L2 value/process/order analyses, and 2,000 subject-cluster bootstrap rules.

No post-`t0` measurement, treatment, destination change, service, or note enters a predictor.

The raw 48-hour primary target is also frozen: adverse if any same-admission later ICU `intime` or `admissions.deathtime` occurs in `(t0,t0+48h]`; live-discharge class if discharged by 48 hours without the raw adverse label; otherwise no raw adverse event/live discharge by 48 hours. The frozen raw target uses the parent's implementation and is not relabeled after this audit. It contains 2,607 adverse composites. S0 versus T1 on this raw target remains the primary test.

## Endpoint-adjudicated first-transition estimand

### Candidate timestamps and valid states

Create eight six-hour intervals over `(t0,t0+48h]`. Every patient starts at landmark state W: transferred to a qualifying ward with no post-`t0` return or death yet.

- W→R: first later same-admission `icu/icustays.intime`.
- W→D: `hosp/admissions.deathtime`.
- W→L: `hosp/admissions.dischtime` only when `hospital_expire_flag=0` and `discharge_location!='DIED'`.
- W→W: no observed valid transition by the interval end; for flagged administrative-discordance records this is not verified ward occupancy.

R, D, and L are absorbing only for this first-transition analysis. Earliest valid exact timestamp wins. For exact ties, freeze precedence D, then R, then L, and report tie counts before fitting. A death after an earlier ICU return contributes W→R; the later R→D path is descriptive. Live discharge ends observable same-admission ward risk and is not proof of safety after discharge.

### Administrative endpoint gate

Flag `endpoint_admin_discordance=1` whenever a `dischtime` in the horizon is accompanied by `hospital_expire_flag=1`, `discharge_location='DIED'`, or contradictory death fields. Preserve every raw timestamp; never delete a dischtime merely because a later death exists.

Primary M0/M1 fitting retains all 49,157 transfers. A dischtime that fails the valid-L rule does not generate a transition; a later R or D may still become the first valid transition. If neither occurs by 48 hours, the record remains in computational state W but is flagged as endpoint-unresolved, and W must be described as **no observed valid transition**, not verified alive-on-ward occupancy. This currently concerns 33 apparent first discharges with `discharge_location='DIED'` and no R/D in the horizon. Report their exact count and characteristics without using outcomes as predictors. Mandatory sensitivities are:

1. administrative-terminal sensitivity: model their invalid dischtime as a separate competing state A;
2. unresolved-exclusion sensitivity: exclude the 33 endpoint-unresolved records but no others;
3. literal-dischtime sensitivity: reproduce the parent's old rule, under which all dischtimes preceding later events are L;
4. complete exclusion of every administrative-discordance record, including the 22 with later R/D.

The frozen raw S0/T1 target is unchanged in every sensitivity. Divergence between the raw target and adjudicated first-transition target is an endpoint-validity finding, not evidence for or against T1.

A blinded dual-clinician review of all discordant hospitalizations using the configured discharge note and complete transfer path is the evidence needed to call any record live discharge, expected death, or documentation error. Notes are post-decision and outcome-contaminated; they are prohibited as predictors. Automatic verification can check structured rules and counts but cannot perform this clinical adjudication.

## Baseline and substantive alternative at matched specificity

### Simple direct-horizon baseline

Retain ridge multinomial S0 and nested T1 on the frozen raw 48-hour target. For a fair 24-hour prioritization comparison, fit secondary direct-horizon S0-24/T1-24 ridge multinomial models using the identical predictors, split, preprocessing, penalty search, and structured valid first-state classes at 24 hours. Penalties are selected on validation multinomial log loss and probabilities recalibrated on validation only.

At 24 and 48 hours, rank patients by predicted R+D risk. For each model and frozen quotas q=2%, 5%, and 10%, report the number reviewed, observed first R/D transitions captured per 1,000 transfers, sensitivity, PPV, and number needed to review. The 48-hour T1 raw score remains the primary fixed-horizon result; S0-24/T1-24 are secondary matched decision baselines.

This baseline directly answers whether a simple horizon-specific score can prioritize patients. It loses the shape of risk accumulation, coherent probabilities at intermediate horizons, and whether discharge removes a patient from in-hospital risk.

### M0/M1 first-transition alternative

Reshape each patient into up to eight at-risk six-hour rows. Fit a ridge-penalized pooled multinomial logistic hazard with interval indicators and transitions R, D, L, or remain W:

- M0 uses exactly S0 decision-time inputs;
- M1 uses exactly T1 decision-time inputs;
- no post-`t0` time-varying predictor is permitted;
- select ridge penalty on validation person-period multinomial log loss;
- recalibrate cause-specific cumulative incidences on validation only;
- open the same untouched subject-level test set once.

From hazards, compute coherent individual CIFs for R, D, L, R+D, and W occupancy at 6, 12, 24, 36, and 48 hours. For prioritization, rank by the M0/M1 R+D CIF at the matching 24- or 48-hour horizon and evaluate exactly the same quotas and outcomes as the direct-horizon baseline.

The alternative reveals information the baseline loses: when risk accrues, which component carries a gain, whether valid discharge prediction dominates, and whether a patient's priority depends on a near-term rather than cumulative 48-hour hazard. It earns retention only if that additional information improves calibrated R+D prediction or materially changes same-quota event capture; complexity alone is not an advance.

### Alternatives not selected

A cause-specific Cox/Fine–Gray sensitivity is permissible if pooled multinomial calibration fails, but separate hazard scales are less direct for coherent multiclass state probabilities. A recurrent/nonabsorbing model is deferred: only 18 people have two returns and 55 have death after return within 48 hours, and post-return management is outside the frozen `t0` decision. A rolling 6/12-hour landmark is deferred because it requires post-`t0` information and defines a new sequential decision. GRU-D and the two-stream TCN remain the parent's secondary value/process/order analyses; they do not resolve endpoint chronology. Revisit recurrent or dynamic models only with a separately approved post-return or sequential-monitoring question and adequate transition support.

## Estimands, evaluation, and uncertainty

Report all absolute model scores and these paired contrasts:

1. frozen primary `Δfixed = Brier(S0)-Brier(T1)` for the raw 48-hour three-state target;
2. `ΔIBS_RD = IBS_RD(M0)-IBS_RD(M1)`, averaged over the eight intervals;
3. component `ΔIBS_R`, `ΔIBS_D`, and `ΔIBS_L`;
4. calibration-in-the-large, calibration slope, and time-dependent Brier/log loss for each cause at 6, 12, 24, 36, and 48 hours;
5. direct-horizon versus event-time differences in captured R+D transitions per 1,000 at identical q and h;
6. M0-versus-M1 and S0-versus-T1 capture differences at identical q and h;
7. worklist overlap/Jaccard and movement across <2%, 2–<5%, 5–<10%, and ≥10% risk categories;
8. observed/predicted CIFs and paired contrasts by exact destination, frozen destination family, source ICU, latest service, transfer night/day, admission type, code-status class, PACU-return proxy, and the parent's dense-observation, full-code, no-documented-limitation, and step-down sensitivities.

Use 2,000 subject-cluster bootstrap replicates, preserving all admissions and person-period rows for a resampled subject. Report percentile 95% intervals and event counts. If death-specific support is insufficient, report wide uncertainty rather than pooling it away. No p-value alone establishes materiality.

## Falsification and result meanings

**Primary trajectory information supported:** `Δfixed>0` with paired 95% interval above zero and acceptable held-out calibration. This supports incremental prognosis only.

**Event-time/prioritization extension supported:** M1 has acceptable 24/48-hour R+D calibration; `ΔIBS_RD>0` with interval above zero; the gain is not confined to L; and M1 captures more R+D events than the matched direct T1 worklist at at least two frozen quota/horizon combinations with the paired interval above zero. Report whether the gain is early/late, R/D, and how much worklist membership changes. This supports a better risk-ranking input for external workflow evaluation, not monitoring benefit.

**Operational-selection dominant:** M1's improvement is confined to L, disappears for R+D IBS, or materially reverses by destination/service/treatment-limit strata. This weakens a monitoring interpretation but does not prove absence of physiology.

**Fixed-horizon adequate:** M1 is calibrated but adds no decision-relevant distinction, the 95% upper bound for `ΔIBS_RD` is below 0.002, and the upper interval for extra capture is below 2 R+D transitions per 1,000 at every frozen quota. Retain simple S0/T1; report chronology descriptively.

**Adverse:** T1 or M1 worsens calibrated R+D prediction with an interval excluding zero, or endpoint sensitivities reverse the conclusion. Do not call patients stable or the hypothesis biologically false.

**Inconclusive:** intervals span benefit and harm/materiality bounds, calibration fails, endpoint-adjudication sensitivities disagree, or component/stratum support is sparse. An imprecise null is not falsification.

The event-time model must not rescue an adverse frozen S0/T1 result by changing outcome, subgroup, or horizon after test opening.

## Exact MIMIC-IV 3.1 bindings

Read-only source archive:
`[internal dataset path]`
([source checksum]).

Required catalog tables/archive members, columns, keys, and time roles:

- `icu/icustays` / `mimic-iv-3.1/icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; keys `stay_id` and `subject_id,hadm_id`; `outtime=t0`, later `intime` defines R.
- `hosp/transfers` / `mimic-iv-3.1/hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; exact successor on nonmissing `subject_id,hadm_id` and post-`t0` path. The 408,977 rows with missing `hadm_id` cannot join to the frozen admission key and are excluded before exact matching.
- `hosp/admissions` / `mimic-iv-3.1/hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`; D, valid L, and administrative-discordance gate.
- `hosp/patients` / `mimic-iv-3.1/hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; age by `subject_id`; `dod` is not substituted for in-hospital `deathtime`.
- `hosp/services` / `mimic-iv-3.1/hosp/services.csv.gz`: `subject_id,hadm_id,transfertime,prev_service,curr_service`; latest `transfertime<=t0`.
- `icu/chartevents` / `mimic-iv-3.1/icu/chartevents.csv.gz`: `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; join `stay_id`; primary window `charttime in [t0-24h,t0)` and `storetime<t0`.
- `icu/d_items` / `mimic-iv-3.1/icu/d_items.csv.gz`: `itemid,label,abbreviation,linksto,category,unitname,param_type`; fail on mapping mismatch.
- `icu/inputevents` / `mimic-iv-3.1/icu/inputevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,statusdescription`.
- `icu/procedureevents` / `mimic-iv-3.1/icu/procedureevents.csv.gz`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,statusdescription`.

Retain exact item mappings: HR 220045; invasive/noninvasive SBP 220050/220179; invasive/noninvasive MAP 220052/220181; RR 220210; SpO2 220277; temperature F/C 223761/223762; O2 flow 223834; FiO2 223835; O2 device 226732; GCS 220739/223900/223901; code status 223758; invasive ventilation 225792; vasopressors 221289/229617, 221662, 221749/229630/229631/229632, 221906, and 222315.

For adjudication only, configured `note/discharge` is the ordinary read-only file
`[internal dataset path]`
with `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`, joined on `subject_id,hadm_id`. Notes never enter predictors or automatic truth labels. All derived files remain in the workspace.

## Deliverables and computational/clinical verification

The future solver must newly fit S0/T1, S0-24/T1-24, O1, and M0/M1 and produce:

- `cohort_flow.csv`;
- `endpoint_chronology.parquet` with all raw timestamps, valid-state flags, tie flags, and administrative discordance;
- `endpoint_reconciliation.json` reproducing raw and adjudicated counts and all four sensitivities;
- `fixed_horizon_predictions.parquet` and `transition_predictions.parquet`;
- `fixed_metrics.json`, `cif_metrics.json`, and `component_metrics.json`;
- `quota_worklists.parquet` and `quota_metrics.json` at q=2%, 5%, 10% and h=24,48;
- `stratified_transition_report.json`;
- `interpretation_axes.json` linking every status to estimates, intervals, and file paths;
- `conclusion.md` consistent with computed outputs.

Computationally checkable claims are cohort construction, timestamps, structured endpoint rules, split integrity, predictor availability, model fitting, probability coherence, calibration, scores, quotas, bootstrap intervals, and whether conclusions follow the prespecified rules. Clinical plannedness, whether a DIED/dischtime discordance is a documentation error, expected death, treatment intent, preventability, safe discharge, monitoring adequacy, intervention benefit, real capacity utility, and transportability require adjudication, operational data, external validation, or another study.

Measured discovery diagnostics: approximately 20–25 seconds per bounded read of the small structured endpoint tables in ordinary CPU shell; 49,157 transfers reproduced; 55 apparent live-discharge records were reclassified/flagged by structured status, including the 22 parent conflicts; 18 second returns and 55 R→D paths were observed. These are not prediction results.

Estimated future solver budget: 8 CPUs/64 GiB for extraction (2–4 hours) and 8 CPUs/64 GiB for ridge models, person-period fitting, quota evaluation, and 2,000 clustered bootstraps (2–5 hours). No GPU is required for the endpoint extension. The parent's optional L1/L2 source/order models may use one allocated A100 plus 8 CPUs/64 GiB for 3–6 hours. These estimates are unverified but fit the configured 16-CPU, 262,144-MiB, 8-GPU, 28,800-second solver envelope.

## Exactly three rechecked key references

[K1] Heo Y, Kim M, Han SS, et al. *AI-Driven Predictions of Readmission and Mortality for Improved Discharge Decisions in Critical Care: A Retrospective Study.* Diagnostics. 2026;16(6):874. doi:10.3390/diagnostics16060874.

[K2] Ruppert MM, Loftus TJ, Small C, et al. *Predictive Modeling for Readmission to Intensive Care: A Systematic Review.* Crit Care Explor. 2023;5(1):e0848. doi:10.1097/CCE.0000000000000848.

[K3] Agniel D, Kohane IS, Weber GM. *Biases in electronic health record data due to processes within the healthcare system: retrospective observational study.* BMJ. 2018;361:k1479. doi:10.1136/bmj.k1479.

The K1 mapping bounds operational, treatment-limit, and component interpretation; K2 bounds window/composite heterogeneity; K3 supports the observation-process rival. None establishes this hypothesis, endpoint repair, or intervention benefit. The same inspected excerpts and original receipt timestamps/hashes are reused byte-for-byte; no new paper inspection is claimed.
