# Compiler-ready negative-control and cross-hospital residualization child for the frozen eICU respiratory-label trajectory

## Status, inherited decisions, and substantive advance

This is a substantive child of the two assigned assessed-valid parents `[prior hypothesis]` and `[prior hypothesis]`. It is a targeted compiler-readiness repair for Episode 87. It does not restart, redefine, or estimate a different scientific schema.

The Lead-frozen population and estimand are retained exactly. The analysis uses 540 person-landmark rows, 443 distinct first qualifying ICU stays/persons, and 74 hospitals; retains the first qualifying stay per `uniquepid`; uses landmarks `L ∈ {1440, 2880, 4320, 5760, 7200}` minutes after ICU admission; selects the first exact target label in `[L,L+360]`; uses `D = cplitemoffset`; and retains all inherited pre-landmark exclusions, action-row construction, exact label strings, repeated-landmark rows, and stay clustering by `patientunitstayid`. The two arms remain exactly `Ventilated - with daily extubation evaluation` (`evaluation`) and `Ventilated - with no daily extubation trial` (`no_trial`). The primary all-row outcome is the inherited five-state respiratory-chart accounting with competing exits:

`K ∈ {competing_exit, classifiable-de-escalation, classifiable-escalation, classifiable-stable/mixed, non_exit_unobservable}`.

The primary contrasts remain fixed-arm-denominator all-row probabilities `p_k(a)` and `Δ_k = p_k(evaluation) - p_k(no_trial)`, with the inherited secondary classifiable display `q_c(a)` and `δ_c`. They are descriptive, noncausal quantities. Death, discharge, transfer, inability to complete the T window, invalid exit timing, and unobservable non-exit rows remain visible and are never silently recoded as respiratory negatives or dropped into a complete-case estimand.

The strongest evidence available before execution supports only that these are literal, sparse, heterogeneous structured-chart values and that associations may reflect pre-D patient state, source opportunity, hospital/workflow composition, exits, entry-clock behavior, or repeated documentation. It does not support that either value denotes an SBT, extubation evaluation, readiness, clinician intent, delivered setting, treatment, benefit, harm, quality, or causality.

The unresolved claim is narrow and falsifiable: after conditioning on pre-D respiratory state proxies and value-blind documentation opportunity, does the exact current label add reproducible information about the later independently parsed respiratory-chart trajectory in hospitals held out from fitting, rather than merely marking a site/opportunity/documentation process? A secondary bounded question is whether that incremental structured-chart information can prioritize a fixed manual chart-review queue. The queue is an operational review-allocation exercise, not a patient-benefit or treatment decision.

The substantive advance in this child is an explicit, fail-closed falsification and transport contract that makes the interpretation auditable in three ways:

1. It separates label information from residual state and documentation opportunity with mutually exclusive `S/O/C` feature blocks, nested cross-fitted models, training-only joint support maps, and site-balanced held-out summaries.
2. It adds two prespecified negative-control/placebo families: an outcome-blind pre-D placebo target and a future-anchor lagged-label placebo. These cannot replace the primary endpoint. A positive label increment on the pre-D placebo is adverse to the claim that the primary increment is a clean post-D residual-state signal; a positive future-anchor placebo is adverse to a time-specific interpretation and is reported as persistence/documentation evidence, not as validation.
3. It requires cross-hospital opportunity/state residualization: every label increment is reported by held-out hospital and by training-derived state/opportunity cells, with both equal-hospital and row-weighted aggregation, site reversal counts, range/overlap audits, and explicit support gates. Hospital identity is never a predictor and no result is generalized beyond supported held-out sites.

No estimates or empirical conclusions are asserted here. Every interpretation is conditional on source, inherited-artifact, support, null, calibration, uncertainty, and verification gates.

## Exact source and artifact binding

All source data are read-only. The eICU snapshot is `[source checksum]`. The current dataset catalog is `[internal dataset path]` with [source checksum]. The current local guides are:

* `[internal dataset path]`;
* `[internal dataset path]`.

Every listed source is a gzip file whose archive member is `ordinary file` under `[internal dataset path]`. The compiler must recheck source bytes, gzip/member convention, headers, schema JSONs, catalog hash, snapshot, joins, and relationships before reading any endpoint value. Any mismatch is computationally invalid and stops interpretation.

Required sources and exact current schema bindings are:

* `patient`: source `[internal dataset path]`, [source checksum]; schema `[internal dataset path]`, schema [source checksum]. Join on `patientunitstayid`; use `uniquepid`, `hospitalid`, `unitvisitnumber`, `age`, `unitdischargeoffset`, `unitdischargestatus`, and `unitdischargelocation`.
* `carePlanGeneral`: source `[internal dataset path]`, [source checksum]; schema `[internal dataset path]`, schema [source checksum]. Use `patientunitstayid`, `cplitemoffset`, `cplgroup`, `cplitemvalue`, and `cplgeneralid` only to verify the frozen exposure, D, action-row identity, and exact label; no care-plan count, value, note, or post-D record may enter baseline, opportunity, endpoint, diagnostic, null, model, cutpoint, fold, placebo, or review calculations.
* `respiratoryCharting`: source `[internal dataset path]`, [source checksum]; schema `[internal dataset path]`, schema [source checksum]. Join on `patientunitstayid`; clinical time is `respchartoffset`; entry time is `respchartentryoffset`; use `respchartid`, `respcharttypecat`, `respchartvaluelabel`, and `respchartvalue` for the frozen parser, endpoint, opportunity, entry-clock audit, and pre-D placebo construction.
* `respiratoryCare`: source `[internal dataset path]`, [source checksum]; schema `[internal dataset path]`, schema [source checksum]. Join on `patientunitstayid`; use `respcarestatusoffset`, `airwaytype`, `airwaysize`, `airwayposition`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, and `priorventendoffset` for airway corroboration, active intervals, opportunity, and the inherited endpoint/sensitivity rules.
* `vitalPeriodic`: source `[internal dataset path]`, [source checksum]; schema `[internal dataset path]`, schema [source checksum]. Join on `patientunitstayid`; clinical time is `observationoffset`; use finite `sao2` and `respiration` for pre-D state/opportunity and the separate secondary physiologic alert proxy only. It is a five-minute summary source, not a waveform.
* `treatment`: source `[internal dataset path]`, [source checksum]; schema `[internal dataset path]`, schema [source checksum]. Join on `patientunitstayid`; use `treatmentoffset`, `treatmentstring`, and `activeupondischarge` only for inherited airway concordance/negative-control and pre-D row-opportunity audit, never as a treatment endpoint or semantic label.

* The compiler receives `HARBOR_WORKSPACE` (the current invocation workspace) and resolves every guide, schema, source, inherited artifact, script, and output relative to that binding or to the explicitly verified shared source root; it must not contain copied ancestor-attempt paths. Before any table scan, it writes `source_manifest.json` containing the resolved absolute path, logical table, archive member, SHA-256, schema path and SHA-256, catalog path and SHA-256, snapshot, and ordinary-file/member check for each source. The manifest also records the resolved paths and SHA-256 values of both mandatory inherited artifacts and the compiler version/configuration hash. A path outside the current workspace is permitted only for the six immutable source files, their schema/catalog metadata, or an explicitly supplied inherited artifact whose bytes pass the declared hash check; all generated outputs must be under the current workspace.
* Artifact resolution is explicit and fail-closed: accept a mandatory inherited artifact only from a configured path or an exact filename supplied by the invocation, then verify its declared SHA-256, required columns, row count, uniqueness, first-stay identity, five landmarks, exact labels, and `D == decision_offset`. Do not search arbitrarily, reconstruct the cohort, select a same-named artifact from another attempt, or substitute a derived support file. If either artifact cannot be resolved unambiguously or any check fails, write `verification.json` and `compute_manifest.json` with `status=invalid` or `feasibility=inconclusive` and the failed check, and stop before endpoint, placebo, model, or contrast extraction.

Every required path is therefore bound at runtime and recorded, making the proposal executable in a fresh workspace rather than dependent on an ancestor attempt directory.

The current dataset catalog is

* `eicu_strict_cohort.csv`, exactly 540 rows, 443 distinct first qualifying stays/persons, 74 hospitals, [source checksum];
* the action-row artifact, exactly one row per (`patientunitstayid`, `landmark`), containing exact `label`, `D`, and `decision_offset`, [source checksum].

Record their actual current absolute paths in `source_manifest.json`. Verify byte identity, identity columns, uniqueness, all five landmarks, one-to-one joins, exact labels, and `D == decision_offset`. If either artifact is absent or differs, stop before endpoint or placebo extraction and emit only feasibility/inconclusive status naming the failed check.

## Frozen endpoint, parser, times, and all-row accounting

All offsets are ICU-admission-relative minutes. Use clinical offsets, never entry offsets, for every primary endpoint and placebo window. The inherited windows relative to each row's `D` remain:

* `B = (D-720,D]`;
* `E = (D,D+720]`;
* `T = (D+720,D+2160]`.

Before arm-stratified output, enumerate every source-wide `respchartvaluelabel` and `respcharttypecat` with matched and unmatched counts. Parse only the locked components FiO2, PEEP/PEEP-CPAP, pressure support, and set ventilator rate using the inherited exact aliases, case rules, finite-number and bound checks, fraction/percentage conversion, duplicate collapse, same-clinical-time conflict rules, and parse-reason recording. A component requires at least two valid observations at distinct clinical offsets separated by at least 30 minutes; a state requires at least three of four observed components. Missing is never zero, unchanged, or carried forward. Fixed absolute thresholds remain FiO2 `0.10` fraction, PEEP `2 cmH2O`, pressure support `2 cmH2O`, and set rate `2 breaths/min`.

For rows without a competing exit, preserve the inherited ordered rules. Sustained de-escalation requires observed B/T states, at least two component decreases, no increase, and no E escalation. Escalation requires observed B/T states plus at least two increases, or a newly documented invasive airway in E/T after no invasive evidence in B. Stable/mixed is the remaining classifiable state. An indeterminate required E airway check cannot create de-escalation and is non-exit unobservable unless an independent increase/airway rule assigns escalation. `respiratoryCare` is airway corroboration/sensitivity only and cannot fill numeric settings. An active interval is `ventstartoffset <= time` and missing or `ventendoffset >= time`.

A finite `patient.unitdischargeoffset <= D+2160` has precedence, including death, discharge, transfer, and inability to complete T. Record exact exit offset, `unitdischargestatus`, `unitdischargelocation`, and `exit_before_washout = 1{unitdischargeoffset <= D+720}`. Invalid/unavailable exit time is a separate `invalid_exit_time` administrative reason and never means alive. Assert exactly one K state for all 540 rows before any model or contrast.

The primary arm-specific all-row probabilities retain fixed denominators:

`p_k(a) = N_a^{-1} Σ_i 1{A_i=a,K_i=k}` and `Δ_k = p_k(evaluation)-p_k(no_trial)`.

The conditional classifiable display remains:

`q_c(a) = count(A=a,K=classifiable-c)/count(A=a,K is classifiable)` and `δ_c=q_c(evaluation)-q_c(no_trial)`.

No placebo or model result may replace these frozen displays.

## Pre-D state/opportunity contract and leakage barriers

Construct predictors only from source fields with clinical time `< D`, except for the deliberately added current exact label in M1. Emit separate machine-readable `pre_D_baseline`, `post_D_endpoint`, and `post_D_diagnostic` manifests listing every table, column, time field, inequality, and permitted/forbidden use. Any post-D leakage, care-plan contamination, endpoint-derived predictor, or placebo-derived predictor entering the primary model invalidates interpretation.

Define mutually exclusive blocks before fitting:

* `S` (residual state proxy): finite parsed pre-D respiratory values and value-derived summaries, including the locked B-window four-component summaries/trends, permitted first/last/dispersion summaries, valid pre-D airway facts from `respiratoryCare`, and finite pre-D `vitalPeriodic.sao2` and `respiration` summaries. These are structured measurements, not bedside diagnoses or delivered settings.
* `O` (documentation opportunity): value-blind counts, distinct clinical timestamps, distinct component labels, minimum-spacing and window-availability flags, missingness/availability indicators, respiratoryCharting entry-lag summaries, respiratoryCare row/interval counts, vitalPeriodic row/timestamp counts and spacing, and treatment row counts. `O` describes source-population opportunity and is not a clinical state.
* `C` (fixed design/structural covariates): landmark, age category, and only the inherited explicitly permitted pre-D covariates. `C` is neither S nor O.

A feature has exactly one block in `feature_block_manifest.json`. Ambiguous, nonfinite, source-presence, or unvalidated text fields are O or excluded; they are never silently promoted to S. The current label and all care-plan fields are exposure-only and belong to no block. A feature cannot occur in both S and O.

Fit deterministic leave-one-hospital-out models with complete-stay fold assignment and no hospital predictor:

* `M_C`: C only;
* `M_O`/`Mopp`: C + O, no respiratory values and no label;
* `M_S`: C + S, no opportunity features;
* `M_0`: C + S + O, no current label;
* `M_1`: exactly M0 plus the exact current two-level label.

Use a fixed low-dimensional multinomial logistic family, fixed regularization grid, solver, tolerance, and deterministic tie-break. All imputation, finite-value handling, scaling, feature selection, calibration, weighting, state/opportunity cutpoints, and support decisions are learned in training hospitals only. Cache one observed out-of-fold prediction and fold manifest per row. Repeated landmarks from a stay never split across folds.

## Cross-hospital opportunity/state residualization

The held-out unit is a whole hospital for model fitting. Within each fold, fit all maps on training hospitals and freeze them before reading held-out K, H, exit, or placebo target values. Hospital ID and site intercepts are forbidden predictors.

From training rows only, construct deterministic bins for a scalar S score and scalar O score using fixed empirical tertiles when all bins have support, otherwise a deterministic median split, otherwise a documented feature-order-based sparse-cell collapse. No label, K, hospital, effect direction, exit, post-D endpoint, or placebo target may influence bins. Cross bins with landmark. Apply frozen cutpoints to held-out rows without clipping. Record training range, held-out in-range, out-of-range, missing, and invalid counts for every continuous feature and cell.

A held-out state/opportunity cell is supported only with at least 10 rows in each exact arm and at least 20 total rows, with finite training maps and no unresolved block assignment. Report exact arm counts, distinct stays, held-out hospital, landmark, S/O bin, out-of-range counts, and both row- and stay-level support. Unsupported cells are unavailable and are never merged, reweighted, or converted to negative evidence.

For each supported cell and hospital, report:

* observed M1-minus-M0 multiclass log-loss and Brier increments;
* M_O-minus-M_C, M_0-minus-M_S, and M1-minus-M0 nested increments;
* exact-arm K contrasts with fixed denominators and explicit status counts;
* number and proportion of rows/stays contributed;
* direction relative to the pooled increment and whether the site is a directional reversal;
* the same summaries for the prespecified placebo targets.

Aggregate supported-cell results two ways: equal-cell mean and row-weighted mean. Aggregate hospital results two ways: equal-hospital macro and row-weighted micro. The primary unbounded all-row metrics remain reported separately. A single site may not contribute more than 25% of supported rows to a state/opportunity claim. The residual-state interpretation requires at least five supported joint cells spanning at least five hospitals, both exact label arms, and no more than 25% contribution from one cell; otherwise it is inconclusive even if the pooled M1 metric improves.

The cross-hospital transport gate requires at least five hospitals with at least 10 supported classifiable non-competing rows per exact arm, representing at least 50% of supported rows, no more than 25% directional reversals for the prespecified increment, and no site above 25% of supported rows. A fold without a supported cell remains in all-row micro accounting but cannot support equal-site or cell-level interpretation. A positive result confined to one hospital, a label-prevalence extreme, an out-of-training-range group, one component/source, exits/unobservability, entry lag, or repeated landmarks is not residual patient-state evidence.

The compiler must emit `site_state_opportunity_transport.csv`, `state_opportunity_cells.json`, and `transport_envelope.json` with fold-local maps, exact support, site direction, range status, and all denominators. These outputs supplement rather than replace the inherited primary artifacts.

## Prespecified negative controls and placebo tests

These tests are falsification diagnostics, not additional endpoints and not license to search for a favorable result. They are frozen before any arm-stratified result is viewed. Each has its own support denominator, status, and gate. A failed opportunity or support requirement is inconclusive, not a negative result.

### A. Pre-D measurement/opportunity placebo outcome

Construct an outcome entirely before the true decision time D, so it cannot be a later consequence of the current label. The preferred placebo is a locked-parser pre-D trajectory from an earlier window `P=(D-1440,D-720]` to the inherited B window `(D-720,D]`, using only respiratoryCharting clinical offsets, respiratoryCare airway corroboration, and the same finite-value and spacing rules. Define `K_pre` with the same ordered classifiable directional labels where the required pre-D states exist, plus `pre_unobservable`; no post-D source field, exit, future status, current label, or care-plan field enters its construction. If the earlier window cannot support the required two states, assign `pre_unobservable`, never a classifiable negative.

For this placebo only, fit the same fixed cross-fitted M0/M1 definitions using predictors available strictly before D and the exact current label in M1. Do not add P-derived values to the primary feature blocks unless they were already explicitly declared in S before fitting; if a P-derived field is not in the frozen S dictionary, it is excluded from the primary model and is used only to construct `K_pre`. Report M1-minus-M0 loss and Brier increments for `K_pre`, and the same state/opportunity-cell and held-out-hospital summaries.

A label increment on `K_pre` is adverse to the interpretation that the primary post-D increment is a clean residual-state signal, because it demonstrates that the label carries information about an earlier chart process not accounted for by the declared S/O/C blocks. It may reflect residual state, opportunity, selection, persistence, or leakage; it does not prove any one explanation. A null pre-D increment is supportive only of temporal specificity of the structured association, never of bedside semantics. If the pre-D placebo target is too sparse, its result is unavailable/inconclusive and cannot be counted as a successful falsification.

### B. Value-blind opportunity placebo outcome

Construct a nonclinical documentation-process target from pre-D source timing, without using measurement values, label semantics, or care-plan rows. Define `O_pre_shift` as whether respiratoryCharting has at least two distinct clinical timestamps spanning at least 30 minutes in `(D-1440,D-720]`, with a separate `unobservable` state when the source lacks the required opportunity. This target is deliberately an opportunity construct, not a patient outcome. Fit the same held-out M0/M1 comparison with the declared pre-D O features and exact current label. A reproducible M1 gain after O adjustment is adverse to the claim that the exact label increment is not documentation-process residual; it may indicate incomplete opportunity adjustment or label persistence. A null is not proof of clinical validity.

Report `O_pre_shift` in a separate `placebo_summary.json` section. Do not combine it with K, do not call it physiologic, and do not include it in the frozen estimand.

### C. Lagged-label future-anchor placebo

Retain the exact current label attached to each valid primary row, but move the analysis anchor forward by exactly 720 minutes to `D_pl = D+720` and evaluate a newly constructed future chart trajectory in `(D_pl,D_pl+720]` and `(D_pl+720,D_pl+2160]`, using only rows for which the anchor and windows are administratively available. The label therefore predates the placebo anchor; it is not a contemporaneous exposure. Use the same parser, thresholds, state requirements, competing-exit precedence relative to the placebo anchor, and all-row unresolved accounting. The primary frozen row, D, K, and contrasts remain untouched.

Fit a diagnostic label-versus-no-label comparison using only pre-`D_pl` source features that are explicitly eligible for this placebo, while marking the original-label history as a historical exposure and excluding any current care-plan field from predictors. Do not use this test to infer a treatment effect or to validate label semantics. A positive lagged-label increment is a negative control for a time-specific interpretation: it indicates persistence, repeated documentation, site process, or an unmeasured evolving state and is adverse to claiming that the current label uniquely captures the immediately subsequent trajectory. It can be compatible with a useful documentation marker, but not with a contemporaneous bedside meaning. A null lagged increment is merely reassuring and does not establish specificity. Rows with overlapping original and placebo endpoint windows, a competing exit before the placebo endpoint, or invalid placebo anchor time remain explicit unresolved statuses; they are not silently removed from the primary analysis.

Because repeated landmarks and windows can overlap, cluster every placebo analysis by `patientunitstayid`, record overlap flags, and run a first-landmark-only sensitivity. A placebo result supported only by repeated landmarks or by overlap is adverse to temporal specificity and cannot support a state claim.

### D. Conditional label nulls and exact permutation invariants

Retain both parent nulls and strengthen their audit. First, within held-out hospital-by-landmark strata, permute the exact label only among rows/stays sharing the training-derived S/O cell, preserving arm counts and stay structure. Second, partition complete stays within held-out hospital by the ordered, label-independent complete vector over all retained landmarks of `(landmark, frozen S bin, frozen O bin, pre-D availability/status)`, and permute entire exact-label vectors only among identical signatures. The signature contains no K, H, exit, post-D observability, endpoint flag, placebo target, or care-plan field beyond the exact label being permuted.

For every arrangement assert unchanged stay IDs/signatures, vector lengths, exact arm membership, per-landmark/per-cell arm counts, hospital membership, and no stay splitting. Use deterministic seed `61061`; attempt at least 1,000 valid arrangements where feasible or enumerate all unique arrangements when fewer exist. Report attempted, valid, unique, failed, block, and hospital counts. Fewer than 20 valid global arrangements, fewer than five hospitals, no exchangeable block, lost supported cells, or any failed invariant is inconclusive, never adverse. If the observed M1-minus-M0 increment is typical of either opportunity/state-preserving null, it is adverse to incremental patient-state information even if a broad unstratified permutation differs.

The null envelope is a conditional diagnostic, not a confidence interval. Do not nest permutations inside bootstrap replicates.

### E. Additional inherited falsification suite

Retain without substitution the broad hospital-by-landmark opportunity-preserving permutation, site-balanced envelope, leave-one-hospital-out influence, first-versus-repeated landmark and persistence audit, whole-stay sequence null when exactly feasible, component/source ablations, exit decomposition, and clinical-time versus as-entered sensitivity. The inherited placebo/exposure-shift tests must be implemented with explicit source/time manifests and are not satisfied merely by naming them. Any increment confined to exit composition, unobservability, source density, entry lag, one site/component/source, a repeated-landmark sequence, unsupported/out-of-range cells, or either placebo process is not patient-state evidence.

## Secondary independent vital proxy and review allocation task

Retain `vitalPeriodic` as a separate secondary chart proxy, never as a replacement or pooled endpoint. A value-blind window has opportunity when at least two finite rows occur at distinct `observationoffset` values spanning at least five minutes. In E and T, accept finite `sao2` percent and respiration breaths/min; an alert requires at least two distinct valid observations satisfying `sao2 < 88` or `respiration > 30`. Define separate `H_E` and `H_T` states `{alert,no_alert,physiologic_unobservable}`. Preserve exits and invalid exit time separately; absent observations are not no-alert. Verify units/conventions from the current guide. This is not hypoxemia, tachypnea, respiratory failure, harm, or an adjudicated outcome.

Use held-out M0/M1 probabilities for separate operational targets `Y_K=1{K=classifiable-escalation}`, `Y_HE=1{H_E=alert}`, and `Y_HT=1{H_T=alert}` on applicable opportunity-supported denominators. The action is manual respiratory chart review. At fixed thresholds `τ ∈ {0.10,0.20,...,0.90}`, costs `c ∈ {0.05,0.10,0.20,0.30,0.50}`, unresolved penalties `u ∈ {0.25,0.50,1.00}`, unresolved-review costs `c_u ∈ {0.00,0.05,0.10}`, and capacities 10%, 20%, 30%, emit complete action-by-state tables. Keep review/no-review/abstain explicit. Competing exits, invalid exits, and applicable unobservable states remain unresolved, never negatives. Compare M1 with M0, treat-none, treat-all-observed-target, and deterministic fixed-capacity policies.

Call a named target decision-relevant only as an operational chart-review result if valid held-out computation improves both micro and equal-hospital macro log loss for all-row accounting and the applicable supported target view, has positive incremental net benefit over M0 at two adjacent prespecified costs and at least one fixed capacity, and has a stay-cluster bootstrap interval excluding zero. A stronger state-triangulated structured-chart interpretation additionally requires directional concordance in at least two supported overlap hospitals between K and the separately evaluated physiologic proxy. This does not establish bedside semantics or patient utility.

## Uncertainty and fail-closed gates

Use fixed-seed `61061` stay-cluster bootstrap, minimum 500 and target 1,000 valid replicates. Resample complete first qualifying stays within hospital with all repeated landmarks, labels, predictors, K/H states, and placebo statuses together. Refit full held-out pipelines and recompute support, cells, transport, null-compatible summaries, and review metrics. Never use row bootstrap or replace unsupported cells. Report attempted, valid, failed, effective-cluster, site/fold loss, overlap loss, supported-cell, and out-of-range counts. If at least 500 valid replicates cannot be obtained, uncertainty-dependent claims are inconclusive. Conditional permutations are not nested in bootstrap replicates.

A computationally invalid run includes source/schema/catalog/hash/member mismatch; missing or divergent inherited artifacts; duplicate/non-one-to-one joins; wrong exact labels, landmarks, D, parser boundaries, inequalities, thresholds, or units; post-D leakage; care-plan contamination; feature in multiple blocks; wrong K/H/exit precedence; fold or stay leakage; placebo anchor leakage; failed permutation invariant; unsupported action tables; or missing machine-readable linkage from a conclusion to its artifact and interval. Stop interpretation and mark `verification.status=invalid`.

Feasibility is supportive only if at least 40% of the 540 rows are classifiable and at least 10 hospitals have both exact labels among classifiable rows. Below 20% or below five hospitals is adverse feasibility; intermediate support is inconclusive. Transport requires at least five hospitals with at least 10 classifiable non-competing rows per exact arm representing at least 50% of supported rows, no more than 25% directional reversals, and no single site above 25% of supported rows. Residual S/O interpretation additionally requires at least five supported S×O×landmark cells spanning at least five hospitals and both arms, with no cell above 25% of supported rows. For the pre-D and lagged-label placebo, report their own opportunity/support denominators; unavailable placebo support is inconclusive and cannot be counted as a reassuring null.

A computationally supportive exact-label information result requires M1 to improve both micro and equal-hospital held-out K loss over M0 in the unbounded primary and at least two prespecified endpoint/observation sensitivities, with favorable stay-cluster uncertainty, transport support, no adverse broad or conditional null, no meaningful pre-D placebo gain, and no gain confined to exit, unobservability, opportunity, entry lag, out-of-range extrapolation, one site/component/source, persistence, or repeated landmarks. A residual patient-state interpretation additionally requires a valid S/O/C dictionary, supported joint cells and site transport, M1 improvement beyond M0 rather than only M_O, and an observed increment not typical of the complete-stay S/O conditional null. A lagged-label placebo gain blocks temporal-specificity interpretation even if the primary K result is positive. A positive opportunity placebo blocks a clean documentation-residualization claim. Failure of support, overlap, vital opportunity, clock availability, null exchangeability, or bootstrap is inconclusive rather than adverse evidence.

Supportive results establish only incremental prediction and/or operational prioritization of named structured eICU chart constructs. Adverse results mean that the label is not robust for those constructs or is compatible with state, opportunity, site, exit, persistence, or repeated-documentation composition. Inconclusive results identify failed source, artifact, support, timing, null, compute, calibration, or uncertainty gates. No result establishes presence or absence of bedside evaluation, treatment, benefit, harm, quality, or causality.

## Required compiler outputs and conclusion linkage

Emit at least:

`source_manifest.json`, `filter_counts.json`, `frozen_population_verified.csv`, `exposure_verified.csv`, `trajectory_rows.csv`, `site_support.csv`, `site_state_opportunity_transport.csv`, `heldout_metrics.json`, `transport_envelope.json`, `state_opportunity_cells.json`, `feature_block_manifest.json`, `interpretability_attribution.json`, `documentation_opportunity.json`, `physiologic_triangulation.csv`, `decision_curve.json`, `bootstrap_summary.json`, `permutation_summary.json`, `conditional_null_summary.json`, `placebo_summary.json`, `as_entered_clock_sensitivity.json`, `landmark_persistence.json`, `exit_decomposition.json`, `pre_D_baseline.json`, `post_D_endpoint.json`, `post_D_diagnostic.json`, `compute_manifest.json`, and `verification.json`.

`placebo_summary.json` must distinguish the pre-D parser placebo, value-blind opportunity placebo, lagged-label future-anchor placebo, and all support/overlap/cluster statuses. `site_state_opportunity_transport.csv` must provide fold-local cutpoints, exact hospital and cell denominators, out-of-range counts, direction/reversal flags, and both aggregation schemes. `interpretability_attribution.json` must link each nested increment and negative-control result to its out-of-fold predictions, target definition, support gate, and uncertainty artifact. Every output records source/schema/catalog/artifact hashes, headers, ordinary-file convention, snapshot, relationships, exact inequalities, parser/unit/opportunity manifests, K/H/exit precedence, fold/stay grouping, feature-block membership, cutpoints, null invariants, attempted/valid arrangements, threshold/cost/capacity grids, bootstrap status, and mechanically derived gates.

Each narrative conclusion must cite the exact computed artifact, denominator, held-out hospital/cell support, and interval or explicitly say the corresponding gate was inconclusive. No empirical estimate is supplied by this proposal.

## Evidence boundary and unavailable bedside adjudication

The configured release contains no raw waveforms, synchronized device logs, complete narrative workflow evidence, local interface/workflow dictionaries, adjudicated SBT/extubation/reintubation outcomes, post-ICU follow-up, or validated bedside labels. `vitalPeriodic` is a five-minute summary rather than a waveform. The exact care-plan strings are not validated bedside actions. The review score is not patient utility. Expert adjudication, local dictionary review, synchronized device data, adjudicated outcomes, and external/prospective replication would be required for bedside semantic claims or clinical recommendations.

This child can test whether the exact labels carry transportable, opportunity-residualized information about the named structured respiratory-chart constructs and whether that information survives explicit pre-D and persistence negative controls. It cannot establish SBT/extubation intent, readiness, delivered ventilator settings, treatment effects, benefit, harm, quality, clinical truth, or causality.
