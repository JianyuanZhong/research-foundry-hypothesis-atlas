# Residual instability before ICU-to-ward transfer: sealed opening and informative order-null contract

Status: proposed substantive child of `[prior hypothesis]`. No post-transfer association, outcome model result, order-null contrast, or clinical effect is claimed. This child preserves the frozen 49,157-transfer population, landmark, outcomes, C/G/G-perp/G-pre estimands, temporal roles, thresholds, and clinical question. It closes two execution gaps: the uninstantiated pooled split and the lack of a nonadaptive criterion for whether endpoint-fixed shams actually perturb direction enough to support attribution.

## Question, evidence boundary, and strongest rival

The strongest currently supported claim is feasibility. An outcome-blind audit exactly reproduced 49,157 first eligible ICU-to-general-ward transfers among 40,014 subjects, found 2,607 raw 48-hour ICU-return/death events in inherited endpoint work, and found raw-G coverage of 88.70%. G-pre coverage was 83.83% overall, 78.71% in locked 2017–2019, and 75.08% in 2020–2022. The audit did not fit an outcome model or establish that direction predicts deterioration.

Inspected work shows that longitudinal ICU-discharge models can outperform snapshot scores while remaining vulnerable to operational and composite-endpoint interpretation [K1], that longitudinal prediction results vary substantially by population, outcome, and window [K2], and that observation timing and frequency can carry healthcare-process signal independent of measured values [K3]. These works motivate but do not establish the hypothesis.

The unresolved hypothesis is unchanged: among otherwise similar ICU-to-ward transfers with the same measured endpoint state at `t0`, unusually worsening rather than improving recent measured-value history changes calibrated 48-hour ICU-return/death risk and fixed-capacity ranking, especially when current state and recent direction disagree.

The strongest rival is not a single mechanism. It is the combination of:

1. mathematical coupling and regression to the mean because raw G and endpoint state share late measurements;
2. response to treatment, where measured improvement or worsening is caused or anticipated by recorded or unrecorded care;
3. observation process, where chart timing, frequency, store lag, and caregiver activity encode concern;
4. transfer process, where destination, service, goals of care, bed pressure, staffing, and return opportunity affect both measurement and outcome.

Endpoint-fixed shams preserve the endpoint value and unordered within-patient values while destroying their pre-final order. G-pre removes shared chart rows from its matched endpoint window. Neither control proves latent physiology. Shams also break value–treatment and value–observation alignment; G-pre remains vulnerable to serial measurement error, treatment response, and transfer selection. Therefore a supportive result can establish only residual temporally ordered measured-value information beyond the tested endpoint/coupling and recorded-process controls. It cannot establish mechanism, preventability, clinician intent, or benefit from monitoring or delayed transfer.

The clinical decision remains whether a ward or rapid-response service with a fixed 2%, 5%, or 10% review capacity should prioritize different patients when recent measured-value direction is added to endpoint state. The result can justify or stop a later external/prospective evaluation; it cannot demonstrate that acting on a worklist benefits patients.

## Frozen design

Retain without modification:

- first eligible adult transfer per hospitalization from ICU to one of the 17 frozen general-ward destinations after ICU LOS at least 24 hours;
- `t0=icu/icustays.outtime` with exact successor `hosp/transfers.intime=t0`;
- predictors in `[t0-24h,t0)`; chart rows require both `charttime<t0` and `storetime<t0`; interval events require overlap and `storetime<t0`;
- raw three-state 48-hour outcome, with same-admission later ICU return or `admissions.deathtime` in `(t0,t0+48h]`, plus the frozen adjudicated first-transition R/D/valid-live-discharge extension and endpoint sensitivities;
- pooled seed-20260923 60/20/20 subject split, approximate-era development/validation/locked-2017–2019/separately-opened-2020–2022 roles, and 2,000 subject-cluster bootstrap replicates;
- endpoint state `C=logit(p_E0(R+D))`;
- raw G from six two-hour bins in `[t0-12h,t0)`, comparing the first and last six hours, requiring at least two observed bins per half in at least four of HR, BP, RR, SpO2, temperature, and oxygen support;
- G-perp as outcome-blind residual direction conditional on endpoint, observation, context, and recorded treatment variables;
- G-pre from `[t0-12,-8)` versus `[t0-8,-4)`, matched to E0-4 using only `[t0-4,t0)`, with the half-open boundary proving that no chart row contributes to both;
- 200 within-patient/domain endpoint-fixed order permutations plus exact reversal;
- E0, raw D1, D1-perp, D1-pre, first-transition counterparts, and the two-stream causal TCN L2-D;
- the inherited Brier, continuous C×direction interaction, calibration, component, quota-capture, endpoint-agreement, and temporal-transport estimands and materiality thresholds.

This child specifies underdetermined implementation details; it does not resplit in response to a result, alter an outcome, exclude a subgroup, or change an estimand.

## Nonadaptive label and opening protocol

The inherited phrase “outcome-stratified subject split before opening outcomes” is logically impossible if interpreted as zero outcome access: creating that split requires the outcome. The repair is a one-purpose label custodian followed by sealed staged opening. The custodian may compute labels and the split, but may not inspect features, fit a model, tune a threshold, or return row-level labels to modeling code.

### Stage 0: materialize before any outcome is constructed

Write and hash all of the following:

1. `source_manifest.json`: archive/note hashes, member names, physical headers, schema hashes, item IDs, plausibility rules, ward dictionary, oxygen ordinal specification, and code commit/environment;
2. `cohort.parquet`: exactly one frozen row per eligible hospitalization with `subject_id,hadm_id,stay_id,t0,destination`, eligibility flags, and approximate-era role, but no post-t0 outcome;
3. `cohort_manifest.json`: 49,157 rows, 40,014 subjects, ordered row-key hash, cohort-flow counts, and duplicate/non-null assertions;
4. `features_prelabel.parquet`: E0 inputs, all 12 two-hour value bins, masks, gaps, store-lag/caregiver summaries, treatment/support transition flags, raw G, G-pre, and Z excluding the later-fitted C term;
5. `feature_dictionary.json`: transformations, normal bounds, bin boundaries, missingness rules, exact oxygen dictionary, and development-fitted objects that do not require knowing which subjects are development;
6. `temporal_roles.parquet` and its subject-isolation assertions;
7. `splitter.py`, `split_spec.json`, `metric_spec.json`, `bootstrap_spec.json`, `conclusion_rules.json`, and an immutable opening ledger;
8. `order_permutation_indices.parquet`: all 200 value-to-position maps and the reversal map, generated without outcomes as specified below.

No direction threshold, process stratum, permutation seed, model grid, metric, materiality bound, subgroup, or conclusion rule may change after Stage 0.

### Stage 1: deterministic split creation under label isolation

The custodian constructs the frozen raw outcome only from the frozen endpoint tables. For each subject, define `subject_event=1` if any of that subject’s cohort rows has frozen 48-hour R+D, otherwise 0. Define dominant destination as the most frequent frozen destination across that subject’s cohort rows; ties use ascending UTF-8 destination text. The subject stratum is `(subject_event, dominant_destination)`.

Within each stratum, sort subjects by the unsigned byte value of
`SHA256("pooled-split-v1|seed-20260923|" + decimal_subject_id)`.
For stratum size `n`, assign the first `floor(0.60n)` subjects to train, the next `floor(0.20n)` to validation, and the remainder to test. All rows for a subject inherit the role. This is the sole admissible instantiation if no authoritative byte-identical parent split artifact exists. If such an artifact is found, use it only if its code/specification, subject coverage, seed, and hash are supplied; disagreement stops execution rather than choosing the more favorable split.

The custodian writes:

- `pooled_split.parquet` containing only `subject_id,role`;
- `split_manifest.json` with code/spec/source/cohort hashes, stratum sizes, role counts, and assignment hash;
- `labels.sealed.parquet` containing row keys and frozen labels in evaluator-only storage.

Only aggregate split-balance counts may leave the custodian. Model-facing code receives no validation/test label. This is outcome use for deterministic partitioning, not an outcome analysis, and the ledger must state it explicitly.

### Stage 2: training-label opening

Join and open training labels only after the split hash is frozen. Using training subjects:

- fit all E0 and outcome models with subject-grouped folds;
- generate out-of-fold C for training and frozen E0 predictions for validation/test and temporal roles;
- fit the G nuisance regression using G as its target, never R+D, with cross-fitted training C and frozen later-set C;
- materialize raw G, G-perp, G-pre, all model-ready tensors, and all 200 sham versions for every role;
- fit training models for every prespecified hyperparameter and seed and emit label-free predictions for unopened roles.

### Stage 3: validation opening and final freeze

Open validation labels only to choose among the prespecified grids, calibrate, verify nuisance balance, and freeze thresholds. Before any pooled test or late-era evaluation label is opened, materialize and hash:

- `pooled_split.parquet`, temporal roles, all row keys, and no-overlap assertions;
- fitted preprocessors, E0/C predictions, nuisance model, G-perp scale, G/G-perp/G-pre knots and q30/q70 cut points;
- 200 permutation maps, complete sham feature matrices, null-informativeness report, and reversal features;
- selected D1-perp and L2-D configurations, all five L2-D checkpoints, calibration objects, and unopened-set predictions;
- 2,000 subject bootstrap ID lists, metric code, materiality bounds, quota denominators, and conclusion templates;
- a `preopening_manifest.json` with hashes for every item above and a signed ledger state.

If any required file is missing, any invariant fails, or a later-set prediction is regenerated after labels are opened, the affected confirmatory result is invalid rather than repairable by refitting.

### Stage 4: locked outcome opening

Open pooled test labels once. Freeze all outputs and the conclusion status. Open 2017–2019 labels next and freeze outputs/status. Only then open 2020–2022 as a separately labeled stress test. No recalibration, seed replacement, subgroup change, threshold change, or feature reconstruction follows an opening. Any post-opening exploratory analysis is labeled exploratory and cannot satisfy the confirmatory rule.

## Endpoint-fixed order null and its informativeness

For each row and each of the six domains, aggregate abnormality margins in the same six occupied two-hour bins used by raw G. Freeze the position and value of the final observed bin. For permutation `k=1,...,200`, shuffle the other observed bin summaries only among that row/domain’s other occupied positions with deterministic Fisher–Yates draws from
`SHA256("order-null-v2|seed-20260923|" + k + "|" + stay_id + "|" + domain)`.
Values never cross rows or domains. Missing positions, chart/store schedule, caregiver/process tensors, treatment sequence, endpoint C, split, role, outcome, value multiset, and final observed value remain fixed. Recompute G with unchanged eligibility. For L2-D, change only the corresponding value-stream positions in the final six bins; the first six bins, static stream, and process stream remain fixed. The reversal map reverses nonfinal occupied values within domain and also leaves the final occupied value fixed.

Every sham must pass exact machine-checkable invariants for row/domain membership, occupied positions, value multiset, final value, masks, process/treatment rows, eligibility, split, and era. A failed invariant stops the order analysis.

The parent’s prior “three movable bins in four domains” gate is not informative because raw-G eligibility entails it. The following fixed, outcome-free contract replaces it. Let `sG` be the training-subject SD of observed raw G. For row i, let `Gik` be its 200 sham values, `di=SDk(Gik)/sG`, and `qi` the fraction of shams with `|Gik-Gi| >= 0.10*sG`. An informative row has `di>=0.05` and `qi>=0.20`. Values are compared after rounding only for distinct-count reporting at `1e-6*sG`; all calculations use full precision.

Before validation labels open, report by pooled role and approximate-era role:

- fraction of raw-G rows with at least four domains whose exact admissible permutation set can change the domain G contribution;
- median/IQR of di and qi and fraction of informative rows;
- per-seed RMS `(Gik-Gi)/sG`, correlation with observed G, and 200 column hashes;
- fraction unchanged in all 200 shams and under reversal;
- G/G-perm support, range, and eligibility equality.

The structural gate passes in a role only if at least 70% of raw-G-eligible rows are informative, at least 190 of 200 sham columns have distinct hashes, every sham has positive cohort-level variance, and all invariants pass. These thresholds are design-adequacy thresholds, not evidence for the hypothesis. They may not be relaxed and seeds may not be regenerated. Failure makes order attribution in that role inconclusive; raw D1 and G-perp may still be described, but neither L2-D nor G-pre can “rescue” a failed null.

After labels open, null precision is additionally judged from the prespecified paired subject-bootstrap intervals for observed-minus-median-null interaction, Brier gain, and quota capture. An interval spanning both the inherited material benefit and corresponding harm is inconclusive. Permutation tail areas use `(1+# null at least as extreme)/201` and are secondary; they cannot replace effect size and uncertainty.

This null is informative about order only under its preserved-information set. Independent within-domain shuffling can disrupt autocorrelation, cross-domain synchrony, and alignment with treatment/observation events. Therefore observed superiority over shams may represent ordered patient values, coordinated multichannel change, or value–care-process response. It is not a mechanism test.

## Transparent residual-direction baseline

The transparent primary baseline remains E0, raw D1, and D1-perp.

For each raw-G row, Z contains the six endpoint abnormality margins, freshness/missing flags, cross-fitted/frozen C, destination, latest service, ICU source, transfer clock, ICU LOS, per-half bin counts, distinct observed hours, median/max store lag, caregiver count, and frozen ventilation, vasopressor, oxygen-device/FiO2/flow start/stop/escalation/de-escalation flags in `[t0-12h,t0)`.

Fit the primary additive ridge nuisance regression `m(Z)=E(G|Z)` with five subject-grouped training folds. A depth-3 histogram gradient-boosted nuisance model is a prespecified sensitivity and may replace ridge only if it lowers subject-grouped validation RMSE by at least 5% and passes the same balance gates; this choice never uses R+D association. Define `G_perp=(G-mhat(Z))/SD_train(G-mhat(Z))`. Require in validation and each evaluation era an absolute standardized slope on nuisance prediction below 0.05, absolute Spearman correlation with C below 0.05, and no endpoint/process block explaining more than 1% additional residual variance.

Fit ridge multinomial `D1-perp = E0 + restricted-cubic-spline(G_perp) + C×G_perp` to the frozen raw three-state target, with training preprocessing/penalty fitting and validation-only selection/calibration. Repeat the matched frozen first-transition model. Raw D1 and D1-pre are fit identically using G and G-pre/E0-4. Inputs, target, split, knots, calibration, metrics, and uncertainty are therefore fixed and directly auditable.

D1-perp reveals the sign and magnitude of unusually worsening history at matched recorded endpoint/process context and exposes the continuous C×direction contrast. It loses within-half order, nonlinear relapse, cross-domain lag, and opposing-domain patterns. Residualization is a prediction control, not causal adjustment: it may remove real treatment response, retain unmeasured care, or induce conditioning artifacts.

## Matched two-stream learned alternative

L2-D uses the same subjects, raw three-state target, 12 fixed two-hour bins in `[t0-24h,t0)`, static E0 context, opening order, and calibration protocol:

- value stream: training-standardized observed/forward-filled physiologic values, without masks/gaps;
- process stream: masks, time since measurement, counts, decision-time store lag, caregiver counts, and recorded treatment/support transitions, without measured values;
- static stream: exactly E0 context;
- separate two-layer causal convolutions, kernel 3, dilations 1/2, 32 or 64 channels, dropout 0 or 0.2; Adam at 1e-3 or 3e-4;
- five fixed seeds, validation-log-loss early stopping, validation-only temperature scaling;
- mandatory full, value+static, process+static, and static-only heads, plus all endpoint-fixed value-order shams.

It can reveal nonlinear relapse, cross-domain lag, synchrony, and opposing-organ patterns that scalar G-perp loses. It is preferred over D1-perp only if calibrated and seed-stable, improves Brier and supported fixed-quota capture in both locked late eras, and its full/value contribution exceeds process-only and its own endpoint-fixed order null. Otherwise prefer D1-perp. A small predictive gain alone does not justify the learned model.

Approximate solver budget: extraction and prelabel materialization 8 CPUs/64 GiB for 2–4 hours; nuisance/ridge/200 sham refits and 2,000 bootstraps 8–16 CPUs/64–128 GiB for 4–6 hours; five-seed L2-D one allocated A100 plus 8 CPUs/64 GiB for 3–6 hours, partly parallel after extraction. These are planning estimates within 16 CPUs, 262,144 MiB, and 28,800 seconds. The inherited exact audit took 1,817 seconds on 8 CPUs/64 GiB; only that audit is measured.

## Results and falsification

A **supportive ordered-information result** requires all inherited parent conditions plus:

1. raw D1 is supportive and calibrated under pooled and temporal rules;
2. D1-perp has the prespecified interaction sign with 95% intervals excluding zero in pooled test and both late eras, with concordant adjudicated R+D;
3. the structural permutation gate passes; observed-minus-median-null interaction and Brier-gain intervals are positive; observed quota capture exceeds the null by at least 2 R+D events per 1,000 reviewed at at least one parent-supported quota without worse overall capture; reversal attenuates or opposes the interaction;
4. either G-pre is concordant with an interval excluding zero in pooled test, or raw/G-perp persist in both no-recorded-support-change and observation-stable sensitivities;
5. any claimed L2-D contribution is not reproduced by process-only or permuted-value heads.

This supports consequential re-ranking by residual ordered measured-value history conditional on tested controls. It does not establish latent physiological deterioration, treatment causality, preventability, safe transfer, or intervention benefit.

A **coupling/mean-reversion adverse result** occurs when raw D1 appears supportive but endpoint-fixed shams reproduce it: observed-minus-null interaction includes or favors zero, the 95% upper bound of observed-minus-null Brier gain is below 0.002, reversal does not attenuate, and the quota-capture upper bound is below 2 events per 1,000 at every quota. If D1-perp is also materially null, the specified evidence is adequately explained by unordered repeated values plus endpoint coupling/regression-to-mean under this null. Do not rescue the claim with L2-D.

A **process-adverse result** occurs when the signal is absent or reversed in both no-recorded-support-change and observation-stable rows, while active-treatment/observation-change strata or the process+static head reproduce the re-ranking, or when full L2-D has no positive value contribution beyond process+static in both late eras. The allowable conclusion is a treatment/documentation/transfer-process-associated predictor. This rejects residual-instability attribution but does not prove that physiology is irrelevant.

An **endpoint-sufficiency result** retains the inherited rule: pooled and both late-era upper bounds exclude 0.002 Brier improvement and 2 additional captures per 1,000 at every quota. Prefer E0/S0.

The result is **inconclusive** if the deterministic split cannot be instantiated, a preopening artifact or invariant is missing, the structural null gate fails, G-perp balance fails, G-pre coverage is below 70% in an evaluation era, intervals include material benefit and harm, raw and residual direction disagree without a valid null explanation, endpoint sensitivities disagree, temporal support/calibration fails, or learned seeds are unstable. A G-pre null alone is inconclusive because relevant change may occur in the final four hours.

These categories are mutually prioritized: packaging/opening or null-informativeness failure yields inconclusive before scientific interpretation; coupling-adverse is evaluated next; process-adverse next; only then may supportive wording be used.

## Exact source bindings

Read-only archive: `[internal dataset path]`, [source checksum].

- `icu/icustays` / `mimic-iv-3.1/icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; `outtime=t0`, later same-admission `intime` defines R.
- `hosp/transfers` / `mimic-iv-3.1/hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; exact successor and destination.
- `hosp/admissions` / `mimic-iv-3.1/hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`; alive-at-t0 gate, raw D, valid L, and endpoint adjudication.
- `hosp/patients` / `mimic-iv-3.1/hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; age and approximate-era interval.
- `hosp/services` / `mimic-iv-3.1/hosp/services.csv.gz`: `subject_id,hadm_id,transfertime,prev_service,curr_service`; latest `transfertime<=t0`.
- `icu/chartevents` / `mimic-iv-3.1/icu/chartevents.csv.gz`: `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; joins on stay/item; bins use charttime and require storetime availability.
- `icu/d_items` / `mimic-iv-3.1/icu/d_items.csv.gz`: `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue`; fail on mapping mismatch.
- `icu/inputevents` / `mimic-iv-3.1/icu/inputevents.csv.gz`: identifiers plus `starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,statusdescription`; interval overlap and `storetime<t0`.
- `icu/procedureevents` / `mimic-iv-3.1/icu/procedureevents.csv.gz`: identifiers plus `starttime,endtime,storetime,itemid,statusdescription`.
- Endpoint adjudication only: `[internal dataset path]`, [source checksum], columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`. Notes never enter predictors, splitting, or automatic labels.

Frozen item IDs: HR 220045; SBP 220050/220179; MAP 220052/220181; RR 220210; SpO2 220277; temperature 223761/223762; oxygen flow 223834; FiO2 223835; device 226732; GCS 220739/223900/223901; code status 223758; ventilation 225792; vasopressors 221289/229617, 221662, 221749/229630/229631/229632, 221906, 222315.

## Scientific deliverable and verification boundary

Completion requires newly fitted E0/raw-D1/D1-perp/D1-pre and first-transition counterparts, five-seed L2-D heads, 200 refitted null pipelines, held-out predictions, and paired uncertainty. Required outputs include the staged manifests above plus `direction_features.parquet`, `null_informativeness.json`, `orthogonalization_balance.json`, `model_predictions.parquet`, `order_null_metrics.parquet`, `coupling_contrasts.json`, `process_sensitivities.json`, `quota_metrics.json`, `interpretation_axes.json`, and result-linked `conclusion.md`.

An automatic verifier can check source/cohort/split hashes, strict times and joins, row nonoverlap, subject isolation, feature/permutation invariants, staged label access, model inputs/fits, unopened-set prediction hashes, bootstraps, metrics, and whether the conclusion obeys the appropriate supportive, adverse, or inconclusive rule. It must reject unsupported supportive wording even when computation is correct, and accept an adverse or inconclusive conclusion when outputs warrant it.

Automatic computation cannot establish device/treatment semantics, latent physiology, clinician intent, goals of care, bed pressure, staffing, ward monitoring, preventability, actionability, harms, or intervention benefit. Those require clinical adjudication, operational data, an external site, or a prospective/quasi-experimental study.

## Exactly three inspected key references

[K1] Heo Y, Kim M, Han SS, et al. *AI-Driven Predictions of Readmission and Mortality for Improved Discharge Decisions in Critical Care: A Retrospective Study.* Diagnostics. 2026;16(6):874. doi:10.3390/diagnostics16060874.

[K2] Ruppert MM, Loftus TJ, Small C, et al. *Predictive Modeling for Readmission to Intensive Care: A Systematic Review.* Crit Care Explor. 2023;5(1):e0848. doi:10.1097/CCE.0000000000000848.

[K3] Agniel D, Kohane IS, Weber GM. *Biases in electronic health record data due to processes within the healthcare system: retrospective observational study.* BMJ. 2018;361:k1479. doi:10.1136/bmj.k1479.

The attached full-text excerpts and receipts were re-inspected. K1 supports the clinical relevance of longitudinal discharge prediction while bounding operational, DNR, and composite interpretation; K2 bounds generalization from prior longitudinal models; K3 directly supports the healthcare-process rival. None establishes this hypothesis, the validity of the order-null assumptions, physiology, external transport, or intervention benefit.
