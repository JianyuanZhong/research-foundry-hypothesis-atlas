# Residual instability before ICU-to-ward transfer: explicit observability and all-transfer deployment value

Status: proposed substantive child of `[prior hypothesis]`. The frozen cohort, t0, predictor windows, raw/adjudicated outcomes, split, endpoint/process/value definitions, endpoint-fixed nulls, materiality thresholds, temporal transport roles, and exactly three inspected references are preserved. No E0/P1/J1 outcome result, order-null outcome contrast, worklist result, or learned outcome model has been computed.

## Why this child is warranted

The parent asks a clinically broad question—whether recent ordered measured values improve 48-hour ICU-return/death prioritization among eligible ICU-to-ward transfers—but fits every confirmatory and learned comparison only on rows where scalar raw G is defined. That is 43,507 of 49,157 transfers (88.51%), with coverage falling to 84.51% in 2017–2019 and 81.53% in 2020–2022. The parent therefore has a valid complete-case estimand, but its nominal all-transfer fixed-capacity queue and applicability claim are not yet identified.

A corrected bounded audit reusing the byte-identified frozen pre-outcome tensor ([source checksum]) exactly reproduced 49,157 transfers, 40,014 subjects, and 43,507 S=1 rows. Coverage was 88.50% in development, 88.43% in pooled test, and 88.60% in validation, but varied materially by workflow: 78.65% for Neurology destination versus 96.17% for Cardiac Surgery, and 45.86% for Neuro Intermediate source versus 96.06% for CVICU. In development only, without opening validation or pooled-test outcome contrasts, R+D occurred in 300/3,389 S=0 transfers (8.85%) versus 1,252/26,082 S=1 transfers (4.80%): risk difference S=1 minus S=0 -4.05 percentage points (subject-cluster bootstrap 95% interval -5.02 to -3.06). A five-fold subject-grouped logistic selection model reached AUROC 0.731 from static context and 0.953 after adding frozen measurement-density summaries. These are selection diagnostics, not a J1/P1 result: they show that completeness marks a clinically and operationally different subpopulation and that P cannot recover unobserved G.

Including measurement counts, store lag, caregivers, and treatment transitions in P does not by itself repair this boundary. P can control recorded process when comparing J1 and P1 among S=1 transfers; it cannot reveal the unobserved G or its outcome relation when S=0. Conversely, excluding S=0 is not automatically bias in the conditional S=1 estimand. The required repair is to name that scientific target and separately test a deployable all-transfer strategy whose predictions are defined for everyone.

The strongest evidence supports feasibility and clinical relevance only. A longitudinal ICU-discharge model can outperform a snapshot score while missingness, operational factors, DNR status, and composite components complicate interpretation [K1]. A systematic review finds potential advantages from longitudinal modeling but heterogeneous populations, outcomes, and bias [K2]. Observation timing and frequency can themselves carry outcome information because EHR trajectories encode healthcare processes [K3]. None establishes ordered-value information, transport from S=1 to S=0, or benefit from intervention.

## Frozen question and two explicit estimands

Let S=1 when raw G is computable exactly as frozen: in six left-closed two-hour bins over `[t0-12h,t0)`, at least four of HR, BP, RR, SpO2, temperature, and oxygen have at least two observed bins in each six-hour half; exact oxygen-device value `Other` remains unknown. S is determined before outcomes and is preserved by every null.

The unresolved scientific hypothesis is unchanged: among S=1 eligible transfers at the same endpoint state and recorded process, unusually worsening rather than improving recent measured-value order adds calibrated 48-hour ICU-return/death information and changes ranking. The confirmatory scientific estimand remains J1 versus P1 among S=1.

The new consequential hypothesis is operational: across all 49,157 eligible transfers, a routed policy that uses J1 only when S=1 and the same process baseline otherwise improves Brier score and the fixed 5% review queue over an otherwise identical policy that uses P1 when S=1. This estimand requires no imputed G and makes the 11.49% without raw G part of the decision population rather than silently excluding them.

A coarse measured-case-mix sensitivity asks whether the S=1 contrast changes after standardizing complete rows toward the full cohort on static context W. W excludes every observation-count, missing-position, store-lag, caregiver, treatment-transition, freshness, or other feature that directly or deterministically defines S. This is not an effect estimate for S=0 and cannot establish missing-at-random; it only tests dependence on overlapping static case mix.

## Frozen population, time, outcome, and roles

The population remains the first eligible adult transfer per hospitalization after ICU LOS at least 24 hours, with exact `t0=icu/icustays.outtime=hosp/transfers.intime`, to the inherited 17-value general-ward dictionary. Predictors use only `[t0-24h,t0)`; chart rows require `charttime<t0` and `storetime<t0`; treatment intervals overlap the window and have `storetime<t0`.

The raw three-state 48-hour target remains R+D (same-admission later ICU return or admission death in `(t0,t0+48h]`), valid live discharge when R+D is absent, or neither. The adjudicated first-transition R/D/valid-live-discharge endpoint and return/death components remain mandatory sensitivities. Notes remain prediction-forbidden and available only to blinded endpoint adjudicators.

The deterministic subject split remains development 23,987 subjects/29,471 transfers, validation 7,983/9,815, and pooled test 8,044/9,871. Pooled test alone determines support. The isolated 2017–2019 and 2020–2022 roles remain transport modifiers. All uncertainty uses 2,000 paired subject-cluster bootstrap replicates.

## Transparent baseline, value model, and routed all-transfer policy

The frozen E0, process block P, nuisance Z, raw G, G-perp, ridge/HGB nuisance selection, balance gates, P1, J1, raw D1 coupling diagnostic, reversal, G-pre, spline knots, outcome-model tuning, and calibration rules are unchanged.

Fit on S=1:

- `P_C=P1=E0+P`;
- `J_C=J1=P1+RCS(G_perp)+C×G_perp`.

Fit `P_A=E0+P+S` on all development transfers, using the same multinomial target, transformations, category levels, ridge grid, validation selection, and calibration algorithm. P_A supplies only S=0 predictions in the routed estimands. P_C and J_C retain their S=1 validation calibration. Require calibration gates separately within S=1, within S=0 for P_A, and in the mixed pooled-test predictions; do not fit a second global calibrator that would change S=0 predictions between policies.

Define, for every transfer i:

`Q0_i = P_C_i if S_i=1, otherwise P_A_i`;

`Q1_i = J_C_i if S_i=1, otherwise P_A_i`.

Thus Q0 and Q1 are byte-identical for S=0; every observed difference is inherited from value-over-process prediction among S=1, while all-transfer worklist ranking allows measured and unmeasured-history patients to compete for the same fixed capacity.

Report paired `Brier(Q0)-Brier(Q1)`, additional R+D events captured per 1,000 reviewed in the 5% all-transfer queue, entrant/exits by S, and subgroup calibration. The 2%/10% queues, components, destinations, coverage strata, and temporal roles remain secondary. The frozen complete-case J1-versus-P1 state cannot be rescued by the routed analysis.

## Selection diagnostics and sensitivity

Before validation or pooled-test outcomes open, run two outcome-blind diagnostics on development with the frozen five subject-grouped folds.

First, describe S prevalence by role, destination, service, ICU source, admission type, clock, and every P component. Fit selection models from (a) static W—age, sex, admission type, destination, service, ICU source, transfer clock, LOS and prior ICU count—and (b) W plus P. Compare ridge and depth-3 histogram-gradient boosting by log loss, with one-standard-error preference for ridge. Report cross-fitted calibration, AUC and overlap. Because S is a deterministic function of per-domain/per-half observed-bin counts already contained in P, the W+P model is descriptive only: it documents structural selection and cannot supply propensity weights or positivity.

Second, using only W, form stabilized selection weights `Pr(S=1)/pi(W)` for S=1 rows, with 1st/99th-percentile truncation sensitivity and weighted effective sample size. Recompute complete-case J1-versus-P1 Brier and queue contrasts with paired subject bootstrap weights. A clinically important reversal worse than -0.002 Brier or -2 events/1,000 makes static-case-mix sensitivity adverse; poor W overlap, weight ESS below 70% of S=1, or 99th-percentile weight above 10 makes it inconclusive. This is deliberately not standardization over endpoint/process measurement features. Neither weighting nor a high selection AUC identifies the missing ordered values or their outcome relation in S=0.

The bounded audit attached to this child used development outcomes only; it did not compute S-by-outcome contrasts in validation or pooled test. It is a design diagnostic, not a J1/P1 result.

## Matched endpoint-fixed null

The parent's 200 PCG64 endpoint-fixed permutations and complete nuisance/outcome refits are unchanged. S, missing positions, chart/store schedules, caregivers, treatment sequence, final observed bin, complete value multiset, split, and role are invariant.

For every seed, refit the nuisance target and residual scale on S=1 development, refit raw D1 and J_C, select/calibrate only with validation, and form Q1_k by replacing J_C with J_C,k while leaving P_A and all S=0 predictions fixed. Evaluate complete-case J1-minus-P1 and all-transfer Q1-minus-Q0 metrics under the same paired subject draws. This tests whether both subset information and all-transfer queue movement exceed endpoint/process-preserved unordered histories; it does not identify physiology.

## Scientifically substantive learned alternative

The transparent routed model intentionally discards partial value histories when S=0 and compresses complete histories to one scalar. The smallest useful alternative is therefore the parent's fixed two-layer causal TCN moved to the full 49,157-transfer population, not a broader architecture search.

Inputs remain exact: 12 two-hour value bins over `[t0-24h,t0)` for six signed margins; a separate process stream of masks, time since observation, counts, store lag, caregiver counts, and ventilation/vasopressor/oxygen transitions; and E0 static context. Leading value missingness uses pooled-development medians and later values are causally forward-filled only after first observation. No measured value enters the process stream.

Freeze the parent's architecture (kernel 3, dilations 1/2, 32 channels, dropout 0.2, Adam 1e-3, batch 256, at most 100 epochs, validation log-loss early stopping patience 10). Fit observed full and process+static models for seeds 20260923–20260927 (10 fits), plus full models for the first 20 frozen 12-bin order-null mappings with seed 20260923 (20 fits). Training is development only and each model is temperature-calibrated on validation.

Primary learned comparisons are full versus process+static over all transfers, full versus process+static within S=0, and full versus Q1 over all transfers. The null preserves masks and value multisets but destroys movable nonfinal order. Report effective null movement separately in S=1 and S=0. A value gain in S=0 without an effective/order-surviving null is partial-history prediction, not ordered-history evidence. Learned evidence cannot rescue failed transparent attribution.

This alternative can reveal clinically material nonlinear lag, cross-domain cancellation, or usable partial histories that scalar G and complete-case routing lose. A multiple-imputation alternative is rejected because the absent bins are structurally process-linked and imputed G would substitute model assumptions for observed order. Relaxing the four-domain rule is also rejected because it changes the frozen exposure. Inverse-observation weighting is retained only as a sensitivity because it cannot recover S=0 trajectories. Revisit richer latent models only if the fixed TCN shows stable, material, null-surviving all-transfer gain.

## Result contract

Apply structural, leakage, prediction-coverage, calibration, nuisance-balance, endpoint, and null-informativeness gates first.

**Broadly applicable ordered-value support.** The parent's complete-case supportive state passes; Q1 versus Q0 has a pooled-test 95% lower bound above zero for Brier gain and at least 2 additional R+D events/1,000 at the 5% all-transfer queue; complete-case and all-transfer null contrasts pass; subgroup/overall calibration passes; and the static-case-mix weighted sensitivity has no clinically important reversal. Conclude that ordered values add predictive information where measurable and materially improve the all-transfer prioritization rule. Do not claim information for S=0, mechanism, or intervention benefit.

**Selection-limited support.** The complete-case state is supportive, but with adequate precision the all-transfer Q1-versus-Q0 95% upper bound is <0.002 Brier or <2 events/1,000 reviewed, while no opposite effect occurs. Conclude that ordered-value information is supported in S=1 but does not meet the frozen materiality criterion for the full eligible queue. Do not describe this as endpoint/process sufficiency within S=1.

**Selection-adverse.** Complete-case support is accompanied by a precise all-transfer queue harm, or the adequately overlapping static-case-mix sensitivity reverses beyond -0.002 Brier or -2 events/1,000. Conclude that the complete-case claim is selection-dependent for the tested deployment/case mix. This does not prove harm from measuring more often.

**Parent adverse states.** Coupling-consistent, endpoint/process-sufficient, and precise opposite J1 effects retain the parent's exact meanings. Neither routing nor the learned model can rescue them.

**Inconclusive.** Any mandatory gate fails; complete-case and routed conclusions conflict without adequate precision; subgroup or mixed calibration fails; selection overlap is inadequate; all-transfer intervals span material benefit and harm/absence; raw/adjudicated or oxygen sensitivities materially disagree; or learned seeds/nulls are unstable. An imprecise null or incomplete-case learned null does not refute the complete-case hypothesis.

The learned axis remains separate: `learned_partial_history_additional`, `learned_no_material_increment`, or `learned_inconclusive`. Transport remains a modifier and cannot upgrade pooled evidence.

## Exact data bindings

Read-only core archive:
`[internal dataset path]`,
[source checksum].

- `hosp/admissions` / `mimic-iv-3.1/hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`.
- `hosp/patients` / `mimic-iv-3.1/hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`.
- `hosp/transfers` / `mimic-iv-3.1/hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`.
- `hosp/services` / `mimic-iv-3.1/hosp/services.csv.gz`: `subject_id,hadm_id,transfertime,prev_service,curr_service`; latest `transfertime<=t0`.
- `icu/icustays` / `mimic-iv-3.1/icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`.
- `icu/chartevents` / `mimic-iv-3.1/icu/chartevents.csv.gz`: stay keys plus `caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`.
- `icu/d_items` / `mimic-iv-3.1/icu/d_items.csv.gz`: `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue`.
- `icu/inputevents` / `mimic-iv-3.1/icu/inputevents.csv.gz`: stay keys plus `starttime,endtime,storetime,itemid,amount,rate,statusdescription`.
- `icu/procedureevents` / `mimic-iv-3.1/icu/procedureevents.csv.gz`: stay keys plus `starttime,endtime,storetime,itemid,statusdescription`.

Join patients to admissions by `subject_id`; stays to admissions by `subject_id+hadm_id`; index transfer by `subject_id+hadm_id` and exact transfer `intime=icustays.outtime=t0`; chart/input/procedure by `stay_id` with subject/hadm checks; d_items by `itemid`. A later same-admission ICU `intime` defines return.

Endpoint adjudication only may use
`[internal dataset path]`,
[source checksum],
columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; join by `subject_id+hadm_id`. Notes never enter predictors.

Frozen item IDs remain HR 220045; SBP 220050/220179; MAP 220052/220181; RR 220210; SpO2 220277; temperature 223761/223762; oxygen flow 223834; FiO2 223835; oxygen device 226732; GCS 220739/223900/223901; code status 223758; ventilation 225792; and vasopressors 221289/229617, 221662, 221749/229630/229631/229632, 221906, 222315.

## Completion artifacts and resources

In addition to every parent artifact, completion requires:

- `observability/eligibility.parquet`, `coverage_by_role.parquet`, `selection_model.json`, `selection_predictions.parquet`, `selection_overlap.json`, and `selection_weighted_metrics.parquet`;
- `predictions/P_A.parquet`, `predictions/Q0.parquet`, `predictions/Q1.parquet`, and all 200 null Q1 predictions;
- `all_transfer_metrics.parquet`, `all_transfer_worklist_5pct.parquet`, branch/overall calibration, queue entrants/exits by S, and 2,000 paired bootstrap contrasts;
- full-population learned tensors, fit summaries and predictions for exactly 10 observed and 20 null fits, with null movement by S;
- `result_state.json` containing one parent pooled state, one applicability state, one learned state, one transport modifier, and every claim linked to computed fields.

The verifier can check S, joins, timing, branch identity for S=0, calibration, all metrics, null preservation/refits, fit inventory, uncertainty, state rules, and conclusion linkage. It cannot establish missing-at-random, clinician intent, staffing/bed pressure, device semantics, physiology, preventability, actionability, external transport, or intervention benefit.

The corrected audit took 44.7 seconds on ordinary CPU using the frozen tensor and split. An earlier 754-second independent reconstruction was superseded after it exposed a 14-row cohort mismatch caused by omitting the parent's alive-at-t0 and exact unit/range rules; none of its counts is used here. Future estimates are unverified: extraction plus E0/P_C/J_C/P_A, selection diagnostics, 200 transparent refits, routing, and bootstraps use one 8-CPU/128-GiB job for at most 6.5 hours; the 30 full-population TCN fits use one allocated A100 plus 8 CPUs/64 GiB for at most 4.5 hours; aggregation uses up to 16 CPUs/64 GiB for one hour. The roughly 13% training-row increase over the parent fits within the configured 16-CPU, 262,144-MiB, 8-GPU, 28,800-second planning envelope.

## Exactly three inspected key references

[K1] Heo Y, Kim M, Han SS, et al. *AI-Driven Predictions of Readmission and Mortality for Improved Discharge Decisions in Critical Care: A Retrospective Study.* Diagnostics. 2026;16(6):874. doi:10.3390/diagnostics16060874.

[K2] Ruppert MM, Loftus TJ, Small C, et al. *Predictive Modeling for Readmission to Intensive Care: A Systematic Review.* Crit Care Explor. 2023;5(1):e0848. doi:10.1097/CCE.0000000000000848.

[K3] Agniel D, Kohane IS, Weber GM. *Biases in electronic health record data due to processes within the healthcare system: retrospective observational study.* BMJ. 2018;361:k1479. doi:10.1136/bmj.k1479.

The attached frozen excerpts were inspected and their receipts reused byte-identically. Claim mappings were rechecked for this coverage/estimand repair. None establishes ordered-value information, transport to missing histories, causality, or intervention benefit.
