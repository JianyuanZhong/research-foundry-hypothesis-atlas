> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Fail-closed operational review-prioritization validation of the frozen eICU respiratory-label trajectory

## Parentage, goal, and substantive change

This proposal is a substantive child of assessed-valid `[prior hypothesis]` and `[prior hypothesis]`. It is a targeted repair for the remaining ambiguity identified by the Lead: whether an exact care-plan label that adds information to a later structured respiratory-chart trajectory is useful for a bounded operational task, rather than merely being a source, site, persistence, or time artifact. It does not alter the frozen scientific schema, cohort, labels, landmarks, decision time, endpoint, estimand, exits, clustering, transport unit, or causal boundary.

The substantive addition is a predeclared **review-prioritization analysis contract**. It defines exactly what can and cannot be called operationally useful, separates all-row workload accounting from decision-curve calculations that require an observed target, compares the label-augmented model only with the inherited no-label model and fixed policy baselines, and fails closed when unresolved states, support, calibration, overlap, or cluster uncertainty make a metric non-computable. It is an allocation exercise for a fixed manual respiratory-chart-review queue. It is not bedside triage, a treatment recommendation, an assessment of SBT/extubation readiness, a measure of patient benefit, or a claim that review changes outcomes.

No empirical result is asserted. The experiment tests the following falsifiable hypothesis:

> **H1 (operational association, not clinical benefit):** after using only information available before the exact decision time `D`, the exact two-level label adds reproducible held-out-hospital information about the inherited later structured trajectory `K` and/or the separately defined summary-vital alert targets, such that a fixed-capacity manual-review queue can be prioritized with better held-out workload and discrimination metrics than the no-label model, without the increment being explained by documentation opportunity, source provenance, pre-D placebo behavior, lagged persistence, exits, repeated landmarks, a single hospital/component/source, or unsupported extrapolation.

The strongest claim supported before this experiment is only that the two literal strings are structured eICU documentation whose association with later chart fields may reflect state, source opportunity, entry timing, site/workflow composition, exits, or repeated documentation. Neither parent supports treating the strings as delivered care, clinician intent, an SBT, extubation evaluation, readiness, treatment, benefit, harm, quality, or causality. A supportive result here would establish at most reproducible incremental prediction and/or review-queue prioritization for named structured eICU constructs. Any bedside or patient-outcome interpretation requires unavailable adjudication and another study.

## Frozen population, exposure, time, endpoint, and estimand

Use the inherited read-only artifacts; do not reconstruct a substitute cohort:

* `eicu_strict_cohort.csv`: exactly 540 person-landmark rows, 443 distinct first qualifying ICU stays/persons, and 74 hospitals; [source checksum].
* The inherited action-row artifact: exactly one row per (`patientunitstayid`, `landmark`) with exact `label`, `D`, and `decision_offset`; [source checksum].

The compiler must record the actual absolute paths supplied for these two artifacts in `source_manifest.json`, verify byte identity, identity fields, uniqueness, all five landmarks, one-to-one joins, exact labels, and `D == decision_offset`, and stop before endpoint extraction if either artifact is absent or divergent. Missing inherited artifacts yield only feasibility/inconclusive status; they are not replaced by a newly filtered source cohort.

Retain the first qualifying ICU stay per `uniquepid`; retain all repeated landmarks within that stay as rows in the frozen all-row estimand and cluster all uncertainty and model grouping by `patientunitstayid`. The landmarks are exactly `L ∈ {1440, 2880, 4320, 5760, 7200}` minutes after ICU admission. Select the first exact target label in `[L,L+360]`. The only exposure arms are the literal values:

* `Ventilated - with daily extubation evaluation`, represented as `evaluation`;
* `Ventilated - with no daily extubation trial`, represented as `no_trial`.

Set `D = cplitemoffset` from the action row. All offsets are ICU-admission-relative minutes. Use clinical time, not documentation-entry time, for every primary endpoint and placebo window:

* `B = (D-720,D]`;
* `E = (D,D+720]`;
* `T = (D+720,D+2160]`.

Assign every row exactly one ordered primary state:

`K ∈ {competing_exit, classifiable-de-escalation, classifiable-escalation, classifiable-stable/mixed, non_exit_unobservable}`.

A finite `patient.unitdischargeoffset <= D+2160` has precedence, including death, discharge, transfer, or inability to complete `T`. Record the exact exit offset, `unitdischargestatus`, `unitdischargelocation`, and `exit_before_washout = 1{unitdischargeoffset <= D+720}`. Invalid or unavailable exit time is a separate `invalid_exit_time` administrative status and never means alive. Do not silently recode an exit or unobservable row as respiratory negative. Assert exactly one `K` state for each of the 540 rows before model fitting or arm contrasts.

Parse only the locked components FiO2, PEEP/PEEP-CPAP, pressure support, and set ventilator rate using the inherited aliases, case rules, finite-number and bound checks, fraction/percentage conversion, duplicate collapse, same-clinical-time conflict rules, and recorded parse reasons. A component requires at least two valid observations at distinct clinical offsets separated by at least 30 minutes; a respiratory state requires at least three of four components. Missing is never zero, unchanged, or carried forward. Keep fixed absolute thresholds: FiO2 `0.10` fraction, PEEP `2 cmH2O`, pressure support `2 cmH2O`, and set rate `2 breaths/min`.

Among rows without a competing exit, use the inherited ordered endpoint rules. Sustained de-escalation requires observed B and T states, at least two component decreases, no increase, and no E escalation. Escalation requires observed B and T states plus at least two increases, or a newly documented invasive airway in E/T after no invasive evidence in B. Stable/mixed is the remaining classifiable state. An indeterminate required E airway check cannot create de-escalation and is non-exit unobservable unless an independent increase/airway rule assigns escalation. `respiratoryCare` corroborates airway status and supplies sensitivity analyses only; it cannot fill numeric settings. An active interval is `ventstartoffset <= time` and missing or `ventendoffset >= time`.

The primary all-row descriptive estimand is unchanged:

`p_k(a) = N_a^{-1} Σ_i 1{A_i=a,K_i=k}` and `Δ_k = p_k(evaluation)-p_k(no_trial)`.

The secondary classifiable display is unchanged:

`q_c(a) = count(A=a,K=classifiable-c)/count(A=a,K is classifiable)` and `δ_c=q_c(evaluation)-q_c(no_trial)`.

Competing exits and `non_exit_unobservable` remain in the all-row denominator. These are descriptive quantities, not treatment effects or causal estimands. No review analysis may replace, censor, or reweight the frozen primary displays.

## Exact current eICU source and schema binding

All source files are read-only. The eICU snapshot is `[source checksum]`. The catalog is `[internal dataset path]`, [source checksum]. The current local guides are:

* `[internal dataset path]`;
* `[internal dataset path]`.

Each listed source is a gzip file with archive member `ordinary file`, under `[internal dataset path]`. Before reading endpoint values, verify current source bytes, gzip/member convention, headers, schema JSONs, schema hashes, catalog hash, snapshot, and relationships. Any mismatch sets `verification.status=invalid` and prevents scientific interpretation.

The exact tables and fields permitted in this experiment are as follows. The compiler must parse the complete schema JSON, not infer columns from this summary.

### `patient`

Source `[internal dataset path]`; [source checksum]. Schema `[internal dataset path]`; schema [source checksum].

The full current columns are `patientunitstayid`, `patienthealthsystemstayid`, `gender`, `age`, `ethnicity`, `hospitalid`, `wardid`, `apacheadmissiondx`, `admissionheight`, `hospitaladmittime24`, `hospitaladmitoffset`, `hospitaladmitsource`, `hospitaldischargeyear`, `hospitaldischargetime24`, `hospitaldischargeoffset`, `hospitaldischargelocation`, `hospitaldischargestatus`, `unittype`, `unitadmittime24`, `unitadmitsource`, `unitvisitnumber`, `unitstaytype`, `admissionweight`, `dischargeweight`, `unitdischargetime24`, `unitdischargeoffset`, `unitdischargelocation`, `unitdischargestatus`, `uniquepid`.

Join the frozen rows to `patient` on `patientunitstayid`. Use `uniquepid`, `patientunitstayid`, `patienthealthsystemstayid`, `hospitalid`, `unitvisitnumber`, `age`, `unitdischargeoffset`, `unitdischargestatus`, and `unitdischargelocation`. `hospitalid` identifies the held-out fold but is never a predictor.

### `carePlanGeneral`

Source `[internal dataset path]`; [source checksum]. Schema `[internal dataset path]`; schema [source checksum].

Full columns are `cplgeneralid`, `patientunitstayid`, `activeupondischarge`, `cplitemoffset`, `cplgroup`, and `cplitemvalue`. Join on `patientunitstayid`. Use `patientunitstayid`, `cplitemoffset`, `cplgroup`, `cplitemvalue`, and `cplgeneralid` only to verify the inherited exact exposure, `D`, action-row identity, and target label. No care-plan count, value, note, or post-D record may enter a baseline, opportunity feature, endpoint, diagnostic target, null, model, fold, cutpoint, review score, or workload calculation. The label belongs to neither state nor opportunity feature block.

### `respiratoryCharting`

Source `[internal dataset path]`; [source checksum]. Schema `[internal dataset path]`; schema [source checksum].

Full columns are `respchartid`, `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respcharttypecat`, `respchartvaluelabel`, and `respchartvalue`. Join on `patientunitstayid`. `respchartoffset` is clinical time and `respchartentryoffset` is documentation-entry time. Use `respchartid`, `respcharttypecat`, `respchartvaluelabel`, and `respchartvalue` for the locked parser, endpoint, source-wide label inventory, value-blind opportunity, entry-lag audit, and pre-D placebo. Entry time is never a substitute for clinical time.

### `respiratoryCare`

Source `[internal dataset path]`; [source checksum]. Schema `[internal dataset path]`; schema [source checksum].

Full columns are `respcareid`, `patientunitstayid`, `respcarestatusoffset`, `currenthistoryseqnum`, `airwaytype`, `airwaysize`, `airwayposition`, `cuffpressure`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`, `apneaparms`, `lowexhmvlimit`, `hiexhmvlimit`, `lowexhtvlimit`, `hipeakpreslimit`, `lowpeakpreslimit`, `hirespratelimit`, `lowrespratelimit`, `sighpreslimit`, `lowironoxlimit`, `highironoxlimit`, `meanairwaypreslimit`, `peeplimit`, `cpaplimit`, `setapneainterval`, `setapneatv`, `setapneaippeephigh`, `setapnearr`, `setapneapeakflow`, `setapneainsptime`, `setapneaie`, and `setapneafio2`.

Join on `patientunitstayid`; `respcarestatusoffset` is the row clinical time and the interval fields define active airway intervals with `ventstartoffset <= time` and missing or `ventendoffset >= time`. Use airway fields for inherited corroboration, value-blind opportunity, endpoint sensitivity, and pre-D state facts only as declared. Do not treat this table as proof of bedside intent or delivered settings and do not use its numeric limit fields to fill respiratoryCharting settings.

### `vitalPeriodic`

Source `[internal dataset path]`; [source checksum]6`. Schema `[internal dataset path]`; schema [source checksum].

Full columns are `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `temperature`, `sao2`, `heartrate`, `respiration`, `cvp`, `etco2`, `systemicsystolic`, `systemicdiastolic`, `systemicmean`, `pasystolic`, `padiastolic`, `pamean`, `st1`, `st2`, `st3`, and `icp`. Join on `patientunitstayid`; clinical time is `observationoffset`. Use only finite `sao2` and `respiration` for declared pre-D state/opportunity and separate post-D summary-vital proxies. These are five-minute summary observations, not raw waveforms; the guide specifies SpO2 percent and respiration breaths/min.

### `treatment`

Source `[internal dataset path]`; [source checksum]. Schema `[internal dataset path]`; schema [source checksum].

Full columns are `treatmentid`, `patientunitstayid`, `treatmentoffset`, `treatmentstring`, and `activeupondischarge`. Join on `patientunitstayid`; use `treatmentoffset`, `treatmentstring`, and `activeupondischarge` only for inherited pre-D row-opportunity, airway-concordance, and negative-control audits. Treatment text is not an endpoint, intervention, semantic label, or patient-benefit outcome.

The catalog relationship for each required table is `patientunitstayid` to `patient`. Duplicate or non-one-to-one joins, wrong headers, or any undeclared field entering a restricted calculation are computational failures.

## Leakage-safe predictors and provenance-held-out models

Before reading any post-D target, emit machine-readable `pre_D_baseline.json`, `post_D_endpoint.json`, and `post_D_diagnostic.json` manifests enumerating every table, column, clinical time field, inequality, and permitted/forbidden use. All primary predictors have clinical time `< D`; the only exception is the exact current label in `M1`, which is intentionally the exposure under test. No entry timestamp substitutes for clinical time.

Assign every predictor exactly one mutually exclusive block:

* `S`, residual pre-D state proxy: finite parsed B-window values and trends for the four locked components; valid pre-D airway facts from `respiratoryCare`; and finite pre-D `vitalPeriodic.sao2` and `respiration` summaries. These are structured measurements, not diagnoses, delivered settings, or readiness.
* `O`, value-blind documentation opportunity: row counts, distinct clinical timestamps, distinct component labels, spacing and window-availability flags, missingness/availability indicators, respiratoryCharting entry-lag summaries, respiratoryCare row/interval counts, vitalPeriodic row/timestamp counts and spacing, and treatment row counts. `O` describes source opportunity, not clinical state.
* `C`, fixed design/structural covariates: landmark, age category, and only inherited explicitly permitted pre-D covariates. `C` is neither `S` nor `O`.

Ambiguous, nonfinite, unvalidated-text, source-presence, and label-derived fields are excluded or assigned to `O` as specified; they are never silently promoted to `S`. The exact label and all care-plan fields belong to no predictor block. Any duplicated block assignment, post-D field, endpoint-derived feature, exit-derived feature, placebo-derived feature, or hidden hospital predictor invalidates interpretation.

Fit deterministic leave-one-hospital-out folds. Every landmark of a `patientunitstayid` remains in one fold. Hospital ID is used only to define the held-out unit and macro summaries, never as a predictor. Within each fold, learn all imputation, finite handling, scaling, regularization choice, calibration, feature maps, weighting, support bins, and cutpoints in training hospitals only, then freeze them before evaluating held-out K, H, exit, or placebo targets.

Use one fixed low-dimensional multinomial logistic family with a declared solver, tolerance, regularization grid, and deterministic tie-break. Fit and cache out-of-fold predictions for:

* `M_C`: `C` only;
* `M_O`/`Mopp`: `C + O`, no respiratory values or label;
* `M_S`: `C + S`, no opportunity features;
* `M_0`: `C + S + O`, no current label;
* `M_1`: exactly `M_0` plus the current exact two-level label.

Report held-out micro and equal-hospital macro multiclass log loss and Brier score, calibration, and nested increments `M_O-M_C`, `M_0-M_S`, `M_1-M_0`, and `M_1-M_O`. These are predictive information increments, not mediation, causality, or identification of a latent clinical state.

## Support, source views, and falsification

Within each fold derive scalar `S` and `O` support maps from training rows only. Use fixed empirical tertiles when all bins have support, otherwise deterministic median split, otherwise a documented fixed feature-order sparse-cell collapse. Cross bins with landmark. Apply frozen cutpoints to held-out rows without clipping. Record training ranges, held-out in-range/out-of-range/missing/invalid counts, and exact arm and stay counts.

A joint held-out S/O/landmark cell is supported only with at least 10 rows in each exact arm and at least 20 total rows, with finite training maps and no unresolved block assignment. Unsupported or out-of-range cells are unavailable, never merged, reweighted, or converted into negative evidence. A residual-state claim requires at least five supported joint cells spanning at least five hospitals and both arms, with no one cell contributing more than 25% of supported rows. The cross-hospital gate requires at least five hospitals with at least 10 supported classifiable non-competing rows per exact arm, representing at least 50% of supported rows, no more than 25% directional reversals, and no hospital above 25% of supported rows. Equal-hospital macro and row-weighted micro summaries are both mandatory.

Fit two predeclared source views with the same folds and training-only transformations:

1. `RC_view`: respiratoryCharting and respiratoryCare state/opportunity fields plus `C`, excluding vitalPeriodic values.
2. `VP_view`: vitalPeriodic state/opportunity fields plus `C`, excluding respiratoryCharting and respiratoryCare value fields; only explicitly declared value-blind counts/timestamps may remain.

Never pool these views as interchangeable measurements. A source-provenance validation claim requires persistence beyond the all-source baseline in at least one predeclared source view, no adverse source-ablation result, and no dependence on one site, landmark, component, source, or repeated landmark. If the independent VP view lacks opportunity or support, the source-triangulation gate is inconclusive, not adverse.

Construct, in a separate diagnostic pipeline, value-blind post-D pseudo-targets `O_E_RC`, `O_T_RC`, `O_E_VP`, and `O_T_VP` from the declared clinical windows. RespiratoryCharting opportunity requires at least two distinct `respchartoffset` values; vitalPeriodic opportunity requires at least two finite rows at distinct `observationoffset` values spanning at least five minutes. Keep unresolved, competing-exit, and invalid-time statuses explicit. These pseudo-targets cannot enter K models or replace K. A label increment that is stronger for documentation opportunity than for K, or a K increment that disappears after O adjustment and is reproduced by an opportunity-preserving null, is adverse to an unqualified residual-state interpretation; it does not prove a workflow mechanism.

Retain the pre-D trajectory placebo, value-blind opportunity placebo, and exact `D_pl = D+720` lagged-label future-anchor placebo from both parents. The pre-D placebo uses the locked parser from `(D-1440,D-720]` to `B`; the opportunity placebo is `O_pre_shift`; the lagged placebo uses newly constructed windows after `D_pl` with the current label historical rather than contemporaneous. Use clinical offsets, preserve exits and unresolved statuses, cluster by stay, record overlaps, and run first-landmark-only sensitivity. A positive pre-D or opportunity placebo is adverse to clean residualization; a positive future-anchor placebo is adverse to a time-specific interpretation and may indicate persistence or evolving state. A null is only reassuring and never validates bedside semantics. Placebo outcomes never modify the frozen K estimand.

Retain broad hospital-by-landmark opportunity-preserving permutation and complete-stay S/O-conditional label-vector permutation. Use deterministic seed `61061`, attempt at least 1,000 valid arrangements where feasible or enumerate all unique arrangements when fewer exist, and assert unchanged stays, signatures, vector lengths, labels, hospital membership, per-landmark/per-cell counts, and no stay splitting. Fewer than 20 valid global arrangements, fewer than five hospitals, lost support, or a failed invariant is inconclusive, not adverse. Preserve component/source ablations, exit decomposition, first-versus-repeated landmark persistence, whole-stay sequence null where exactly feasible, and clinical-time versus as-entered sensitivity.

## Separate summary-vital proxy

Use `vitalPeriodic` only as an independent secondary chart proxy. A window has value-blind opportunity if at least two finite rows occur at distinct `observationoffset` values spanning at least five minutes. In E and T, finite `sao2` is percent and respiration is breaths/min. Define `H_E` and `H_T` independently as `{alert,no_alert,physiologic_unobservable}`, with alert requiring at least two distinct valid observations satisfying `sao2 < 88` or `respiration > 30`. Absence is not `no_alert`. Preserve exits and invalid times. This proxy is not hypoxemia, tachypnea, respiratory failure, harm, or an adjudicated clinical outcome.

## Predeclared review-prioritization utility and workload analysis

### Operational estimand

The action is only `review this row in a fixed manual respiratory-chart queue` versus `do not review now`; it is not a treatment or bedside triage action. For each held-out fold, target, model `m ∈ {M_0,M_1}`, threshold `τ`, review cost `c`, unresolved penalty `u`, unresolved-review cost `c_u`, and capacity `r`, use only predictions generated without training on the held-out hospital or held-out target values. The exact grids are frozen before results are inspected:

* thresholds `τ ∈ {0.10,0.20,...,0.90}`;
* review costs `c ∈ {0.05,0.10,0.20,0.30,0.50}`;
* unresolved penalties `u ∈ {0.25,0.50,1.00}`;
* unresolved-review costs `c_u ∈ {0.00,0.05,0.10}`;
* queue capacities `r ∈ {0.10,0.20,0.30}` of the applicable all-row queue.

The operational targets are evaluated separately:

* `Y_K = 1{K=classifiable-escalation}`;
* `Y_HE = 1{H_E=alert}`;
* `Y_HT = 1{H_T=alert}`.

For `Y_K`, `competing_exit`, `non_exit_unobservable`, and invalid exit time are unresolved, never negative. For `Y_HE` and `Y_HT`, `physiologic_unobservable`, competing exit, and invalid time are unresolved, never negative. The all-row K display remains the primary endpoint; the review target is a named derived operational target only.

A threshold policy reviews rows with held-out predicted probability at least `τ`. A capacity policy reviews the top `r` proportion by held-out predicted probability, with deterministic ties by `patientunitstayid`, landmark, and row identifier. If a capacity cannot be filled without violating an applicable support gate, report it unavailable rather than borrowing rows from unsupported cells. Report review/no-review/abstain explicitly; do not force an unresolved row into a binary outcome.

### Metrics that are computable without pretending to measure benefit

For every target, fold, hospital, arm, landmark, model, threshold, cost, unresolved scenario, and capacity, emit the complete action table in `decision_curve.json` with:

* all-row queue size, review fraction, and no-review fraction;
* number and fraction reviewed with observed positive, observed negative, and unresolved target status;
* unresolved fraction among reviewed and among the full queue;
* observed-positive yield per 100 reviews, observed recall among known positives, and reviews per known positive;
* coverage of known target states and the number of rows/stays contributing;
* equal-hospital macro and row-weighted micro summaries;
* calibration and held-out log loss/Brier score for `M_0` and `M_1`;
* comparison with `M_0`, `M_1`, treat-none/no-review, treat-all-observed-target where defined, and deterministic fixed-capacity policies.

These workload quantities are descriptive and are not patient utility. “Positive” means only the literal observed target state above. Do not call the reviewed positives respiratory deterioration, harm, or patients needing intervention.

A standard decision-curve net-benefit calculation is emitted only on an explicitly labeled **observed-target diagnostic denominator**: rows with a valid non-competing target state and no invalid/unobservable status for that target. On that denominator, for a threshold policy, report `NB_obs = TP/N_obs - c*FP/N_obs` and incremental `NB_obs(M1)-NB_obs(M0)` for every frozen `c` and `τ`; use no imputation of unresolved rows. Because this denominator excludes unresolved cases, it cannot support an all-row clinical utility claim.

In parallel, report bounded operational sensitivity tables on the full applicable queue. For each unresolved assignment scenario (`unresolved=negative`, `unresolved=positive`, and the declared penalty `u`), calculate the predeclared workload score in which a reviewed known positive receives unit review-prioritization benefit, a reviewed known negative incurs `c`, an unresolved reviewed row incurs `c_u`, and unresolved non-review is penalized by `u` only as an explicit sensitivity convention. Label this as an **analytic review-allocation score**, not utility, benefit, or harm. If a target has no observed-target denominator, no decision-curve value is computed; if a full-queue scenario is not defined by the declared statuses, that scenario is unavailable rather than filled by assumptions.

All grids are reported in full, including negative, zero, and unavailable cells. Select no favorable threshold, cost, capacity, hospital, landmark, arm, or unresolved scenario post hoc. A metric is eligible for an operational conclusion only when its denominator, status counts, support, and prediction linkage are present in the artifact.

### Operational relevance gate

Call `M1` operationally decision-relevant for a named target only if all conditions hold:

1. The run is computationally valid and the target's required units, opportunity, status, and held-out predictions are complete.
2. The inherited all-row K accounting is valid, and `M1` improves both held-out micro and equal-hospital macro loss over `M0` for the all-row K target and the applicable supported operational target. This requirement is assessed separately for each target; failure for one target does not transfer to another.
3. At least one prespecified capacity and two adjacent prespecified review costs show positive incremental `NB_obs` over `M0` on the observed-target diagnostic denominator, **and** the same direction is present in the corresponding full-queue analytic workload score under every unresolved scenario that the target's support can identify. If the observed denominator or any required unresolved scenario is unavailable, the gate is inconclusive rather than negative.
4. The improvement survives equal-hospital and row-weighted summaries, the declared transport gate, and supported S/O cells; no one hospital contributes over 25% of supported rows and no more than 25% of supported hospitals reverse the prespecified increment direction.
5. A stay-cluster bootstrap interval for the prespecified incremental workload score and observed-target loss excludes zero, with at least 500 valid replicates (target 1,000), using complete first qualifying stays resampled within hospital and all repeated landmarks carried together.
6. The result is not explained by a pre-D placebo, lagged-label placebo, post-D opportunity pseudo-target, source ablation, exit composition, unobservability, entry lag, out-of-range extrapolation, one component/source, or repeated landmarks.

If only workload yield improves but loss, calibration, transport, or uncertainty does not, report a descriptive workload difference and **do not** call it decision-relevant. If decision-curve values are computable only after excluding unresolved rows, report the observed-target diagnostic and state that operational relevance is inconclusive. No operational gate can establish that review is beneficial, safe, clinically appropriate, or superior bedside triage.

A stronger triangulated structured-chart statement additionally requires directional concordance between `K` and the separately evaluated `H_E/H_T` proxy in at least two supported overlap hospitals. This remains association with structured chart constructs, not clinical validation.

## Uncertainty, clustering, and fail-closed rules

Use fixed-seed `61061` stay-cluster bootstrap with minimum 500 and target 1,000 valid replicates. Resample complete first qualifying stays within hospital, carrying every retained landmark, exposure, pre-D feature, K/H status, diagnostic status, source view, and review-policy row together. Refit the complete held-out pipeline and recompute support, cutpoints, source views, null-compatible summaries, all-row endpoint accounting, decision curves, workload metrics, and transport summaries in each replicate. Never use a row bootstrap and never nest conditional permutations inside bootstrap replicates. Report attempted, valid, failed, effective clusters, fold/site loss, overlap, supported-cell, out-of-range, and unresolved counts.

Set `verification.status=invalid` and stop interpretation on any source/schema/catalog/hash/member mismatch; missing/divergent inherited artifacts; duplicate or non-one-to-one joins; wrong exact labels, landmarks, D, windows, parser aliases, boundaries, thresholds, units, or K/H/exit precedence; post-D leakage; care-plan contamination; duplicated block assignment; fold or stay leakage; source-view contamination; broken placebo anchor; failed permutation invariant; unsupported review table; nonreproducible tie rule; or missing machine-readable linkage from a conclusion to predictions, denominator, support, and uncertainty artifact.

Feasibility is supportive only if at least 40% of the 540 rows are classifiable and at least 10 hospitals have both exact labels among classifiable rows. Below 20% or below five hospitals is adverse feasibility; the intermediate range is inconclusive. Transport and joint-cell gates above are hard gates. Failure of source view, vital opportunity, target observability, overlap, calibration, null exchangeability, or bootstrap is inconclusive, not adverse evidence. Unresolved rows are never silently excluded from all-row workload accounting and never converted to negatives.

## Required compiler artifacts and conclusion linkage

Emit at least:

`source_manifest.json`, `filter_counts.json`, `frozen_population_verified.csv`, `exposure_verified.csv`, `trajectory_rows.csv`, `site_support.csv`, `site_state_opportunity_transport.csv`, `heldout_metrics.json`, `transport_envelope.json`, `state_opportunity_cells.json`, `feature_block_manifest.json`, `interpretability_attribution.json`, `source_view_metrics.json`, `documentation_pseudotargets.json`, `documentation_opportunity.json`, `physiologic_triangulation.csv`, `decision_curve.json`, `bootstrap_summary.json`, `permutation_summary.json`, `conditional_null_summary.json`, `placebo_summary.json`, `as_entered_clock_sensitivity.json`, `landmark_persistence.json`, `component_source_ablation.json`, `exit_decomposition.json`, `pre_D_baseline.json`, `post_D_endpoint.json`, `post_D_diagnostic.json`, `compute_manifest.json`, and `verification.json`.

`source_manifest.json` must contain actual absolute source and inherited-artifact paths, source/schema/catalog hashes, snapshot, headers, ordinary-file member convention, relationships, and byte-verification results. `feature_block_manifest.json` must assign every predictor exactly once. `decision_curve.json` must distinguish all-row workload tables, observed-target decision-curve denominators, unresolved scenarios, support status, model, target, threshold, cost, capacity, hospital, landmark, and arm; it must include all frozen grid cells rather than only favorable ones. `interpretability_attribution.json` must link each nested model increment, source-view result, placebo/null result, and review metric to its out-of-fold predictions, exact target/status definition, denominator, held-out hospitals/cells, and bootstrap interval. Every narrative conclusion must cite the exact artifact, denominator, support gate, and interval, or explicitly say the gate was inconclusive. No empirical estimate is supplied by this proposal.

## Results interpretation and evidence boundary

* **Supportive:** only a valid held-out computation that passes the all-row K, source/opportunity, transport, null, uncertainty, and operational gates may be described as incremental prediction and bounded review-queue prioritization for the named structured eICU target. It does not establish that the label denotes an intervention or that review improves a patient outcome.
* **Adverse:** with adequate support and uncertainty, no robust label increment, reproduction by an S/O-preserving null, disappearance under source ablation, stronger documentation pseudo-target increment, persistence in the lagged placebo, or site/source/exit/repeated-landmark confinement is adverse to the corresponding structured-chart or temporal-specificity claim. It does not prove absence of bedside meaning.
* **Inconclusive:** failed artifacts, insufficient classifiable rows or hospitals, unsupported joint cells, source or vital unavailability, unresolved target denominator, noncomputable decision curve, failed calibration, fewer than 20 valid permutations, fewer than 500 valid bootstrap replicates, or any validity invariant failure is inconclusive (or computationally invalid where specified), never an adverse scientific result.

The configured release contains no raw waveforms, synchronized device logs, complete narrative workflow evidence, local interface/workflow dictionaries, validated bedside labels, adjudicated SBT/extubation/reintubation outcomes, post-ICU follow-up, patient-preference or resource-cost data, or external/prospective replication. `vitalPeriodic` is a five-minute summary rather than a waveform, and exact care-plan strings are not validated bedside actions. Therefore the review-prioritization score is not patient utility, and no result can establish bedside evaluation, extubation readiness, treatment, delivered settings, benefit, harm, quality, safety, or causality. Those claims require expert adjudication, local workflow/interface metadata, synchronized device data, validated clinical outcomes, and another or prospective study.
