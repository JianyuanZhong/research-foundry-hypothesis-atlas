# Fixed-capacity monitoring value of lactate-by-perfusion at the first eligible live ICU exit

## Status, parent and scientific deliverable

This is a substantive successor to the assigned valid parent `[prior hypothesis]`. It preserves that branch's exact MIMIC-IV 3.1 source bindings, first-eligible-live-exit selection, one-hour availability buffer, 12-hour dual clinical/recording-time window, lactate-by-measured-perfusion phenotype, endpoint-independent coverage gate, R/D/S/N/U first-transition endpoint, separate event-support gate, selection-overlap audit, uncertainty, falsifications and noncausal limits.

The new clinical deliverable is an explicit fixed-capacity monitoring/transition estimand:

> At the first eligible live ICU exit, does adding the prespecified persistent-lactate-by-measured-perfusion phenotype to an order-blind history model increase capture of the first 48-hour ICU readmission or timed in-hospital death in a fixed 10% review queue, with alive hospital discharge treated as a competing transition?

The future Harbor solver must newly fit the prespecified transparent models and the learned trajectory alternative, then report held-out cumulative-incidence contrasts and fixed-capacity queue capture. It must produce either a gate-passing result package or a complete, row-level gate-failure audit. Readiness, a successful fit, or a favorable result is not completion and no fitted result is claimed here.

Completion requires:

1. an all-candidate flow and deterministic first eligible adult live ICU exit per admission, selected before coverage, labels, model fitting or outcomes;
2. row-level provenance for every retained/rejected lactate, MAP, vasoactive, Foley and organ-laboratory record, including clinical time, recording time, unit/value checks and duplicate/interval handling;
3. the strict dual-time coverage manifest and its endpoint-independent pass/fail result;
4. mutually exclusive first-transition labels through 48 hours: ICU readmission (R), timed in-hospital death (D), alive hospital discharge (S), known event-free follow-up (N), and unresolved ascertainment (U);
5. the primary 48-hour R/D cumulative-incidence interaction and its R- and D-specific decompositions, with 24-hour summaries and S competing;
6. the new fixed-capacity estimand: incremental capture, PPV, and false-negative reduction for R/D at exactly the top 10% of the held-out review queue when Bdisc is compared with B1; 5% and 20% are fixed workload sensitivities;
7. the matched B0/B1/Bmask/Bdisc transparent analyses and a training-only learned M2 trajectory sensitivity using the same source whitelist, population, endpoint, subject split and held-out test set;
8. selection-overlap, measurement-process, timing, label, order, process-only and outcome-permutation falsifications; subject-clustered uncertainty; and a conclusion ledger mapping every claim to computed outputs.

If a coverage, event-support, ascertainment, queue-size or overlap gate fails, the relevant estimand is inconclusive. The solver may not choose another exit, inspect outcomes to loosen the coverage gate, recode absent pressors as zero, merge phenotype cells, redefine the queue fraction, or select the favorable sensitivity.

## Unresolved question and evidence boundary

The expert seed proposes that persistently elevated lactate has different meanings when perfusion is improving versus worsening, and cautions that selective repeated measurement and these proxies cannot diagnose microcirculatory dysfunction. The available evidence establishes only that the configured MIMIC snapshot contains the relevant structured tables, repeated measurements, time fields and dictionary rows. It does not establish proxy validity, prevalence, event support, the interaction, incremental queue capture, or any clinical benefit.

The strongest claim supported before the experiment is therefore only:

- MIMIC-IV records can support a bounded retrospective association study of repeated lactate, MAP and recorded vasoactive intervals around an observed live ICU exit, subject to measurement and selection audits.

The untested scientific claim is:

- among adults at their first eligible live ICU exit with adequate repeated measurement coverage, persistent hyperlactatemia is associated with a different short-term first R/D transition risk under improving than under worsening measured perfusion.

The untested clinical-operational claim is narrower and distinct:

- at the same fixed review capacity, adding that prespecified phenotype to a generic order-blind history representation captures more first R/D transitions than the generic representation alone.

The first claim is tested by a standardized difference-in-differences in cumulative incidence. The second is tested by an incremental fixed-queue capture contrast. Neither is a treatment effect.

This advances the parent by connecting the physiologic-heterogeneity question to a consequential but bounded transition-review decision. A positive interaction without incremental queue capture would mean a retrospective subgroup association exists but does not improve prioritization at the fixed workload. Incremental queue capture without a stable interaction would support only an operational risk-ranking signal, not the proposed interpretation of lactate under perfusion. A robust positive result could justify prospective evaluation of context-aware transition review; it cannot justify an alert, discharge decision, escalation protocol, or treatment.

## Population, time zero and temporal boundary

Only MIMIC-IV is used for this experiment. HCC, eICU and UK Biobank remain directly available through the configured read-only dataset areas; their rows and notes are not mixed into this population.

Use the exact archive source:

- read-only source: `[internal dataset path]`;
- archive size: 10,551,747,784 bytes;
- source [source checksum];
- MIMIC snapshot: `[source checksum]`;
- full catalog: `[internal dataset path]`;
- catalog [source checksum].

Join `mimic-iv-3.1/icu/icustays.csv.gz` to `mimic-iv-3.1/hosp/admissions.csv.gz` on `(subject_id, hadm_id)`, and join `mimic-iv-3.1/hosp/patients.csv.gz` on `subject_id`. An adult requires `anchor_age >= 18`; preserve MIMIC's documented age value 91 rather than recoding it. Missing patient/admission joins are counted as linkage failures in the flow.

For each `hadm_id`, sort ICU rows by `(outtime, intime, stay_id)) and select the first row meeting all rules:

- finite `intime` and `outtime), with `intime < outtime`;
- valid adult patient and admission joins;
- known live ICU exit at `t0 = outtime): `deathtime` is null and `hospital_expire_flag = 0`, or nonmissing `deathtime > t0`;
- `t0 - intime >= 13) hours.

Selection occurs before any feature, coverage flag, phenotype, endpoint, model, queue, or support calculation. A later ICU stay is never substituted after a selected row fails coverage or support. Keep explicit exclusion reasons for missing/reversed times, known death by `t0`, `hospital_expire_flag=1) with missing `deathtime`, missing life status, and insufficient history. Do not treat a missing flag as survival.

Set `tL = t0 - 1) hour. The primary feature window is `[t0-13h, t0-1h] = [tL-12h,tL]). Early is `[tL-12h,tL-6h]); late is `(tL-6h,tL]). Apply these boundaries exactly. The one-hour buffer is fixed to prevent records charted near the exit from entering the primary feature set. `outtime) defines time zero and the boundary only; it is not a feature. Exclude `los`, `last_careunit`, future transfers, discharge fields, `dod`, notes and all post-`tL) records from primary features.

## First-transition competing endpoint

Set `H=t0+48h). Construct candidates only in `(t0,H]):

- R: minimum `intime) of a different `stay_id) in the same `(subject_id,hadm_id));
- D: nonmissing `deathtime) in `(t0,H]);
- S: nonmissing `dischtime) in `(t0,H]) with `hospital_expire_flag=0).

A different admission is not an ICU readmission. A row with `intime <= t0) is not a readmission. If multiple candidates have the same timestamp, use the fixed tie order D before R before S and record all tied candidates and the decision. The first candidate wins; later candidates do not overwrite it.

N means no R, D or S candidate through H with known event-free ascertainment. It is not a clinical event. It is allowed when `deathtime>H), or when `dischtime>H) with `hospital_expire_flag=0), or another available admission fact establishes follow-up beyond H. If neither a timed event nor adequate follow-up is available, do not call the case N.

U means unresolved first-transition ascertainment. Assign U to `hospital_expire_flag=1) with missing `deathtime), to missing-flag cases where survival/event-free status cannot be established, and to incomplete follow-up where ordering through H is unknown. If U could precede a known R/S, retain U rather than claiming a known first transition. Report R, D, S, N and U counts, times, tie decisions and flag/death disagreement.

Primary analyses use known R/D/S/N labels; U is never imputed into N. Prespecified bounds assign every U either to N at H (favorable-for-null) or to D at `t0+1 second` (adverse); report both. The primary adverse transition is A=first R or D, with S a competing event. The R/D composite is not described as “failure” without stating its components.

## Exact source bindings and feature construction

All primary records require both clinical availability and recording availability: valid clinical time `<=tL) and valid recording time `<=tL). A valid chart time with late store time is excluded from primary features and counted as delayed storage. A chart-time-only matrix is a fixed non-operational sensitivity and may not replace the dual-time matrix.

The exact source/member, key, time fields and required columns are:

| role | table and archive member | key and time fields | required columns |
|---|---|---|---|
| index/readmission | `icu/icustays`, `mimic-iv-3.1/icu/icustays.csv.gz` | `stay_id); `intime,outtime` | `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los` |
| admission/death/discharge | `hosp/admissions`, `mimic-iv-3.1/hosp/admissions.csv.gz` | `(subject_id,hadm_id)`; `admittime,dischtime,deathtime,edregtime,edouttime` | `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag` |
| demographic | `hosp/patients`, `mimic-iv-3.1/hosp/patients.csv.gz` | `subject_id`; `anchor_year,dod` | `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod` |
| MAP | `icu/chartevents`, `mimic-iv-3.1/icu/chartevents.csv.gz` | `stay_id`; `charttime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning` |
| vasoactive intervals | `icu/inputevents`, `mimic-iv-3.1/icu/inputevents.csv.gz` | `stay_id); `starttime,endtime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,patientweight,totalamount,totalamountuom,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate` |
| urine corroboration | `icu/outputevents`, `mimic-iv-3.1/icu/outputevents.csv.gz` | `stay_id`; `charttime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valueuom` |
| lactate/organs | `hosp/labevents`, `mimic-iv-3.1/hosp/labevents.csv.gz` | `(subject_id,hadm_id)`; `charttime,storetime` | `labevent_id,subject_id,hadm_id,specimen_id,itemid,order_provider_id,charttime,storetime,value,valuenum,valueuom,ref_range_lower,ref_range_upper,flag,priority,comments` |
| selection-care-unit audit | `hosp/transfers`, `mimic-iv-3.1/hosp/transfers.csv.gz` | `(subject_id,hadm_id)`; `intime,outtime` | `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime` |
| ICU dictionary | `icu/d_items`, `mimic-iv-3.1/icu/d_items.csv.gz` | `itemid) | `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue` |
| laboratory dictionary | `hosp/d_labitems`, `mimic-iv-3.1/hosp/d_labitems.csv.gz` | `itemid) | `itemid,label,fluid,category` |

The catalog JSON records the corresponding table schema hashes and all ten members as usable payload. The archive probe verified member existence and verified these dictionary rows: 220052 arterial BP mean, 220181 non-invasive BP mean and 225312 ART BP mean, all linked to chartevents and mmHg; 226559 Foley, linked to outputevents and mL; 221906 norepinephrine, 222315 vasopressin, 221289/229617 epinephrine, 221749/229630/229631/229632 phenylephrine, 221662 dopamine, 221653 dobutamine and 221986 milrinone, linked to inputevents; and 50813 lactate plus organ rows 50861, 50878, 50885, 50912, 50882, 51222, 51265 and 51300.

Use lactate item 50813 in `hosp/labevents`; require finite `valuenum), normalized `valueuom=mmol/L), valid dual times and both times `<=tL). In each half, lactate is the median accepted value. Persistent P means both half medians are at least 2.0 mmol/L. Nonpersistent NL means both medians are defined and at least one is below 2.0. A 4.0 mmol/L threshold is a fixed sensitivity.

Use MAP items 220052, 220181 and 225312 in `icu/chartevents); require finite `valuenum), normalized `valueuom=mmHg), valid dual times and both times `<=tL). Within `(stay_id,charttime)`, collapse duplicate selected items by median, then calculate half medians and distinct clinical timestamp counts. Record item-presence bits and item-level accepted, invalid, unit-rejected and delayed counts.

Use target vasoactive item IDs 221906, 222315, 221289, 229617, 221749, 229630, 229631, 229632, 221662, 221653 and 221986 in `icu/inputevents`. Retain finite `starttime<endtime), nonmissing `storetime<=tL), and intervals overlapping a half. Clip to the half, collapse exact repeats on `(stay_id,itemid,starttime,endtime,orderid,linkorderid)`, and union overlaps. Use positive unioned duration in minutes; do not pool rates, amounts, concentrations or units and never call absent target rows zero pressor. Record item-presence bits and invalid, rejected, delayed, duplicate and overlap counts. A separate `input_any_valid_n` is process intensity only.

Use item 226559 in `icu/outputevents` as secondary Foley corroboration, requiring finite `value), normalized `valueuom=mL), valid dual time and `charttime,storetime<=tL`. It cannot repair a failed primary MAP/pressor gate.

Use organ audit items 50861 ALT, 50878 AST, 50885 total bilirubin, 50912 creatinine, 50882 bicarbonate, 51222 hemoglobin, 51265 platelets and 51300 WBC in `hosp/labevents), with the same dual-time, numeric-value and unit rules. Keep test presence/process counts separate from physiologic values. For every domain and half, retain before/after counts, distinct clinical timestamps, availability fraction, median chart-to-store lag, unit rejections, invalid values, duplicates and interval diagnostics.

Join ICU measurements by `stay_id`, labs by `(subject_id,hadm_id)), and demographics by `subject_id`. The primary feature whitelist contains no endpoint, discharge, death, stay-end or post-landmark field.

## Measured-perfusion phenotype and endpoint-independent gates

Define measured perfusion using the early/late MAP medians and unioned target-pressor minutes:

- I (improving): late MAP minus early MAP >=5 mmHg and late target-pressor minutes <= early minutes;
- W (worsening): late MAP minus early MAP <=-5 mmHg and late target-pressor minutes >= early minutes;
- indeterminate: all other cases, retained for flow and sensitivities but never forced into I or W.

The strict cells are P/NL × I/W. Cell membership is frozen before endpoint labels, event counts, model fits, estimates, calibration or queue predictions.

The endpoint-independent coverage gate G_cov is frozen before endpoint construction and requires, in each early and late half:

1. at least one valid lactate row;
2. at least two valid MAP observations at two distinct clinical timestamps;
3. at least one positive-duration unioned target-pressor interval.

G_cov passes only if all six half-level requirements pass. All selected eligible exits remain in the denominator and flow when G_cov fails. Report domain-level reasons, not only a total pass count.

The separate support gate G_sup is evaluated after fixed labels but before any fit, effect estimate, held-out prediction, calibration or queue ranking. In each P/NL × I/W cell require n>=40, at least 10 known R/D events in the complete gated cohort, at least 8 subjects and at least 3 known R/D events in the held-out test cell, and U<=10% overall and <=20% in the cell. Fewer than five R or five D events in a cell disallows a component-specific interpretation. No cell is dropped or merged.

The deterministic subject split is 70/15/15 train/validation/test, with no subject in more than one partition. Stratify only on frozen primary cell, fixed endpoint label and anchor-year group; if an integer allocation cannot meet support, G_sup fails. All preprocessing, clipping, imputation, scaling, calibration and model selection use training/validation data only.

Add a decision-support gate G_dec, also fixed before performance inspection: the held-out test set must have at least 90 subjects, at least 10 known A=R/D transitions, a top-10% queue of at least 10 subjects, and U<=10% overall in the test set. The queue is exactly m10=ceil(0.10 N_test) subjects, with deterministic ties by descending predicted risk then `subject_id,hadm_id,stay_id`. If G_dec fails, report the queue arithmetic but call the incremental monitoring estimand inconclusive. The 5% and 20% queues are sensitivity workloads, not opportunities to replace a failed 10% primary queue.

## Primary interaction estimand and fixed-capacity monitoring estimand

For each known-label subject, estimate Aalen-Johansen CIFs for R, D and S at 24 and 48 hours; S is a competing transition. At 48 hours, define:

```
theta_RD =
 [CIF_RD(P,I) - CIF_RD(NL,I)]
 -[CIF_RD(P,W) - CIF_RD(NL,W)]

theta_R =
 [CIF_R(P,I) - CIF_R(NL,I)]
 -[CIF_R(P,W) - CIF_R(NL,W)]

theta_D =
 [CIF_D(P,I) - CIF_D(NL,I)]
 -[CIF_D(P,W) - CIF_D(NL,W)]
```

The directional interaction hypothesis is theta_RD<0: persistent lactate carries less excess first-R/D risk when measured perfusion is improving. The clinically meaningful null region is [-0.02,+0.02] absolute risk difference. A negative estimate inside that region is not clinically meaningful support. Component conclusions require their event-support rule and consistent component direction.

The new primary decision estimand is evaluated on the untouched held-out test set. Let `s_B1` and `s_Bdisc` be each model's predicted 48-hour CIF for A=R/D with S competing. Let `Q10(M)` be exactly the top `ceil(0.10 N_test)` subjects by score from model M. Define:

```
Cap10(M) = P(A=1 | subject in Q10(M))
DeltaCap10 = Cap10(Bdisc) - Cap10(B1)
DeltaFN10 = [# A events outside Q10(B1)] - [# A events outside Q10(Bdisc)]
DeltaPPV10 = Cap10(Bdisc) - Cap10(B1)   (same as DeltaCap10 at fixed queue size)
```

The report must also give event capture `#(A=1 in Q10)/#(A=1 in test)`, absolute queue PPV, number needed to review for one A event, and the number of R and D events captured separately. Because the queue size is identical, `DeltaCap10` is the incremental event proportion in the reviewed slots; report both the proportion among reviewed slots and the fraction of all events captured to avoid confusing PPV with sensitivity. Use 5% and 20% analogues as fixed sensitivities.

Bdisc's new phenotype terms are frozen before fitting: P/NL, I/W/indeterminate, early/late lactate, early/late MAP, early/late pressor minutes, MAP and pressor changes, their interaction, organ values and availability indicators. B1 is the order-blind generic-history comparator. The queue comparison is therefore an incremental decision benchmark at fixed workload, not a claim that Bdisc is an implemented clinical policy.

Pre-specify a clinically meaningful operational threshold `DeltaCap10 >= 0.05) absolute event proportion with a 95% interval wholly above 0.05 for “meaningful incremental capture.” If the interval includes 0.05, the queue result is inconclusive for that threshold even if the point estimate is positive. The 5%/20% workload pattern must be reported without selecting the most favorable capacity. A model improvement alone does not support a physiology interpretation; a theta interaction alone does not establish monitoring benefit.

## Matched baseline, transparent alternative and learned alternative

The scientific comparison is not a complexity contest. It asks whether the phenotype's auditable cross-domain information improves the fixed-capacity transition-review benchmark, and whether a learned temporal representation discovers additional coupled chronology beyond the prespecified summaries.

All models use the same strict gated population, exact source whitelist, endpoint, subject-level 70/15/15 split, held-out test set, censoring/competing-risk convention, queue sizes, calibration procedure and subject bootstrap. The learned model receives the same underlying input records and context fields as the transparent models; only representation and fitting differ.

- B0 is a transparent latest-state/context cause-specific complementary-log-log discrete-time model for R, D and S. It uses admission/demographic context (gender, anchor_age, anchor_year_group, admission_type, admission_location, insurance, first_careunit), late-half physiology, late-half missingness and process variables. It excludes `outtime`, `los`, `last_careunit`, discharge/death fields, `dod` and future rows.
- B1 is the primary transparent order-blind history baseline. It adds early/late and 12 one-hour-bin summaries of the same lactate, MAP, pressor, Foley, organ and observation-process fields, but no chronological order or phenotype interaction. Its 48-hour A CIF and queue define the reference.
- Bmask removes physiologic values but retains context, masks, counts, test presence, Foley charting, pressor presence and observation intensity. It tests whether documentation/measurement process can explain apparent performance.
- Bdisc is the transparent phenotype-augmented model described above. The scientific incremental comparison is Bdisc versus B1 at the fixed queue workload, with Bmask as a process-only negative control.
- M2 is a small masked chronological GRU (hidden dimension and regularization fixed before test inspection) receiving the same 12 one-hour-bin raw summaries, missingness masks, process indicators, admission context and frozen phenotype flags available to Bdisc. Training-only imputation/scaling and validation-only early stopping are used. M2 predicts the same competing R/D/S discrete-time hazards and is evaluated on the same test subjects and queue capacities. It can reveal nonlinear or order-dependent coupled trajectories that B1's order-blind summaries and Bdisc's fixed interactions lose, but it cannot validate that lactate/MAP/pressor changes represent microcirculation.
- A two-component diagonal-covariance Gaussian-mixture trajectory model on the same training-only change vector is a deferred sensitivity, not a substitute for M2. It is revisited only if the GRU cannot be implemented within the solver envelope or if a pre-fit data audit shows insufficient per-bin density; such a change must be documented before test outcomes are inspected.

Before narrowing to Bdisc/M2, the alternatives were matched on exact source variables, 12-hour landmark, target, split, uncertainty and fixed workloads. B1 is retained because its order-blind summaries isolate the phenotype increment. Bdisc is selected as the transparent scientific model because its coefficients and cell contrasts can be audited. M2 is selected because the unresolved alternative information is temporal coupling/nonlinearity, not merely another linear predictor. The deferred GMM is simpler but less able to represent ordered trajectories; a full transformer is deferred because its added capacity is not itself a clinical advance and its stability/compute have not been measured. A fluid-response or treatment-effect model is deferred because `inputevents` do not supply clinician intent, fluid responsiveness, valid counterfactual treatment assignment or adequate time-varying confounding control; it would answer a different causal question.

## Analysis, uncertainty and falsification

Fit cause-specific discrete-time hazards for R, D and S and compute Aalen-Johansen CIFs at 24/48 hours. Standardize theta contrasts to the held-out cell distribution, with the exact fixed cells and competing S. For predictions, report calibration intercept/slope, transition-aware Brier score, AUROC/AUPRC for R and D as secondary metrics, 24/48-hour CIF calibration, fixed 5/10/20% queue tables, B1-to-Bdisc paired differences, and Bdisc-to-M2 differences. Estimate 95% intervals with a subject bootstrap preserving the split and admission clustering; use the identical resamples for paired models. Do not use validation or test outcomes to select preprocessing, hyperparameters, thresholds or queue fractions.

Required falsifications and audits are fixed before fitting:

- source/member/schema, dictionary link/unit, join-key and item-ID checks;
- first-exit selection audit and no-future clinical/recording-time audit;
- duplicate MAP handling, exact-repeat pressor collapse and interval-union audit;
- early/late permutation preserving counts and availability;
- outcome permutation within partitions;
- Bmask process-only comparison and a process-intensity negative-control model;
- MAP-only, pressor-only, arterial-MAP-only, Foley and lactate-4.0 sensitivities;
- chart-time-only versus dual-time matrices;
- 24-hour versus 48-hour horizons;
- complete-ascertainment and U favorable/adverse bounds;
- 4/6/8-bin aggregation sensitivities;
- primary-cell, care-unit, anchor-year and measurement-intensity strata;
- q selection-overlap common-support and ESS diagnostics;
- queue capture for R and D separately, not only A;
- deterministic queue tie and exact queue-size audit.

For selection overlap, build an outcome-free q using subject-blocked cross-fitting. Positives are selected eligible exits at t0. Controls are one-hour records h from any valid ICU stay with `intime+13h <= h < outtime) that are not selected exits. q may use only information available by h under the dual-time rule: baseline demographics/admission context, time-local care unit from `hosp/transfers`, 12-hour measurement counts/masks, MAP/lactate/pressor summaries and input/process intensity. It must not use R/D/S/U, discharge fields, `outtime`, future rows or endpoint labels. Report q common support [0.05,0.95], control decile support (at least 20 controls per occupied exit-q decile), and stabilized inverse-odds ESS >=50 in each primary cell. Report unweighted estimates first and q-weighted estimates only as a descriptive selection-stress sensitivity. q is not causal inverse-selection correction; failure makes selection-robust interpretation inconclusive but does not authorize cohort repair.

## Interpretation ledger

Support for the primary interaction requires G_cov and G_sup, U limits, adequate component events, theta_RD< -0.02 with a 95% interval wholly below -0.02, and the prespecified lower-risk pattern in I. Component support additionally requires its component event count and theta_R or theta_D. Support for incremental monitoring value requires G_dec, Bdisc versus B1 `DeltaCap10 >=0.05) with a 95% interval wholly above 0.05, no material calibration degradation, and a directionally coherent fixed-workload result across the prespecified 5%/20% sensitivities. This supports only “the phenotype-augmented score captured more observed first R/D transitions in a held-out fixed-capacity benchmark.”

Adverse evidence includes theta_RD>=0 or reversed component patterns; DeltaCap10<=0 or degradation versus B1; Bdisc no better calibrated than B1; Bdisc no better than Bmask; queue gain confined to S; outcome-permutation resistance; or instability under fixed timing, coverage, endpoint and U sensitivities. A gain from M2 alone is evidence about representation, not about lactate physiology. A Bdisc gain without theta support is operational association without the proposed effect-modification interpretation.

Inconclusive evidence includes any G_cov, G_sup or G_dec failure; U above thresholds; too few R or D events; unresolved joins or units; high indeterminate phenotype fraction; poor calibration; q overlap/ESS failure for selection-robust claims; or an interaction/queue interval too wide to distinguish the prespecified threshold. All failures are reported rather than repaired by post hoc selection.

Computationally checkable claims include source hashes and archive members, schemas and columns, dictionary link/unit rows, joins, temporal filters, selection order, label/tie logic, coverage/support/queue flags, split integrity, fitted predictions, CIFs, queue counts, uncertainty, calibration, q diagnostics and falsification outputs. Clinical adjudication or another study is required for microcirculatory dysfunction, lactate etiology, clinician intent, treatment response, discharge appropriateness, preventability, monitoring benefit, utility, net benefit, harms, ward surveillance and transportability. This experiment cannot establish a causal treatment or discharge effect, nor that any ICU return was preventable.

## Compute, method choice and limits

The measured facts are archive/catalog/member/schema/dictionary availability and source hashes. Full event-scan time, strict-gate prevalence, cell/event support, U rate, q overlap/ESS, model stability, bootstrap runtime and GPU necessity are unverified.

The future solver envelope is 16 CPUs, 262,144 MiB memory, up to 8 GPUs and 28,800 seconds, with concurrency 2. A full source scan and tabular B0/B1/Bmask/Bdisc fit are expected to be CPU-feasible, but this is an estimate, not a result. M2 is a bounded small sequence model; one allocated A100 may reduce repeated fitting/bootstrap time, but CPU execution remains a valid fallback if measured within the envelope. If a GPU is used, request it explicitly through the managed job, use `cuda:0) inside the allocation, and report image/import/infrastructure dependencies separately. Do not infer GPU absence from an ordinary shell. No task-specific fit or model result has been run or claimed in this proposal.

The actual scientific outputs that establish completion are newly fitted held-out competing-risk predictions and calibrated CIF estimates for B0/B1/Bmask/Bdisc/M2; theta_RD, theta_R and theta_D with uncertainty; exact 5/10/20% queue capture/PPV/false-negative tables; coverage/support/selection manifests; falsification outputs; and the conclusion ledger—or a complete prespecified audit showing why one or more outputs are not estimable.

## Provenance and unavailable evidence

I inspected `datasets/README.md`, `datasets/mimic/README.md`, the full configured catalog, all relevant MIMIC table metadata JSONs, `references/research-ambition/methods-and-compute.md`, `references/research-ambition/README.md`, `references/expert-seeds/README.md`, and `references/expert-seeds/cards/mimic-04.md`. The expert seed remains an untested hypothesis. The demonstration method summaries support considering longitudinal learned alternatives but do not establish this MIMIC phenotype or its clinical value. No demonstration is reproduced. The cancer demonstration's main article and complete STAR Methods were unavailable and are not claimed to have been read.

The note files are available separately as read-only `note/discharge.csv.gz`, `note/discharge_detail.csv.gz`, `note/radiology.csv.gz` and `note/radiology_detail.csv.gz`, but they are excluded from this structured experiment. The catalog warns that note links can be unmatched and radiology `hadm_id) may be absent. Raw waveforms and MIMIC-CXR images are unavailable. Therefore no conclusion uses notes, images, waveforms, adjudicated microcirculation, clinician intent, measured GFR, fluid responsiveness, rescue completeness or external validation.

All derived tables, manifests, model artifacts and reports must be written in the workspace and source archives remain read-only.
