> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Outcome-blind HCC repeat-TACE P-beyond-B validation with compiler-proof missing-Y identification and ascertainment stress contract

## Two-parent successor and substantive repair

This is a two-parent successor of `[prior hypothesis]` and `[prior hypothesis]`. It preserves the assessed leader's frozen adult HCC repeat-TACE prognostic estimand and the second parent's executed outcome-blind support/observation audit. The scientific question is unchanged: among selected adult HCC repeat-TACE episodes with a valid remote baseline assay `B` and contemporaneous pre-repeat assay `P`, does `P` add short-horizon prognostic information for the subsequent same-encounter assay `Y` beyond `B` and the locked pre-event core? This remains a noncausal prognostic comparison, not a treatment effect, treatment response, safety, utility, action rule, transport guarantee, or clinical-benefit claim.

The clinically important unresolved limitation is differential post-event assay observation. The retained audit found 2022 to be the only arm-supported block; 2023 had 29/43 observed outcomes and an observed-versus-missing standardized mean difference of 0.672 for `B` and 0.582 for timing; 2024 had only 14/70 observed outcomes, including 1/9 systemic. A favorable complete-triplet RMSE can therefore be selection-sensitive. The first parent supplied a precise but previously unexecuted partial-identification contract. This successor makes that layer compiler/verifier-proof by adding a runnable algebraic oracle and explicit edge-case tests, while retaining the executed audit as the only empirical support artifact. The oracle tests formulas and failure behavior; it does not fabricate HCC outcomes or claim that missing Y has been recovered.

## Evidence boundary

The strongest available evidence remains the executed full-source audit from the second parent: exact reconstruction passed, with 319 systemic-record and 1,491 comparator patients, 159 and 526 selected repeat events, 242 outcome-blind BP-eligible episodes per assay, 158 complete albumin triplets and 160 complete bilirubin triplets overall. The 2022 future block had 29 BP-eligible episodes per assay and 28 observed outcomes, with both outcome-blind and complete-triplet support gates passing. This can support at most a local short-horizon prognostic association in that selected 2022 calendar mixture. It cannot establish reproducible multi-era transport. The missing-Y bounds below are a sensitivity/identification analysis, not an executed empirical finding in this proposal.

## Exact source and table bindings

Use HCC snapshot `[source checksum]` and source catalog `[internal dataset path]` (catalog [source checksum]). Scan all rows, with no sampling, from the following read-only ordinary CSV files. Archive member for each is `ordinary file`.

* `encounters`, schema `table-b743286cb1249287.json`, source `[internal dataset path]`, [source checksum]. Required columns are `Patient Master Index`, `Encounter Number`, `Age`, `Sex`, `Encounter Time`, `Admission Time`, `Discharge Time`, `Encounter Department`.
* `diagnoses`, schema `table-12710723c3df0c99.json`, source `[internal dataset path]`, [source checksum]. Require `Diagnosis Name == Hepatocellular Carcinoma`; timing is inherited from linked encounter because this table has no native time.
* `procedures`, schema `table-d5eae16f8f8093d9.json`, source `[internal dataset path]`, [source checksum]. Required fields include `patient master index`, `visit number`, `surgery`, `start time`, `end time`, `surgery source`; identify case-insensitive `TACE` or literal `chemoembolization`, require valid `start time`, collapse same-patient same-calendar-day duplicates, select the first adjacent 14–180-day TACE1/TACE2 pair and first strict event 15–90 days after TACE2.
* `medications`, schema `table-4f6ecaeb6e8f69c2.json`, source `[internal dataset path]`, [source checksum]. Apply the inherited days 1–14 systemic-record ontology and placebo, prior-exposure, bevacizumab-only, and generic-procedure ambiguity exclusions. These are recorded orders, not verified administrations.
* `labs`, schema `table-38aad8c54471332f.json`, source `[internal dataset path]`, [source checksum]. Required fields are `patient master index`, `visit number`, `test`, `qualitative result`, `quantitative result`, `specimen type`, `test time`; use exact assays `albumin` and `total bilirubin`, finite uncensored numeric `quantitative result`, and `test time`. No units or reference range are available; never pool the assays.
* Outcome-blind ascertainment uses `examinations`, schema `table-fd016d2731b9d6c6.json`, source `[internal dataset path]`, [source checksum]; use only valid `Start Time` and row presence, never text-mine `Examination Findings` or `Examination Diagnosis`.
* Outcome-blind document presence uses `clinical_documents`, schema `table-66afca58512c2fca.json`, source `[internal dataset path]`, [source checksum]; use nonempty linked-row presence only. The duplicate `Admission Diagnosis` header is `Admission Diagnosis__duplicate_2`; this table has no time and must never supply a Y-window timestamp.

Every encounter join is a deduplicated existence join on (`Patient Master Index`,`Visit Number`), with duplicate composite-key counts audited before joining and no many-to-many multiplication. Patient-level event sequencing uses `Patient Master Index` only where explicitly specified.

## Frozen population, clocks, and forward estimand

Reconstruct and assert exactly 319 systemic-record patients, 1,491 comparator patients, 159 and 526 selected repeat events, and assay-specific complete triplets of albumin 40/118 and total bilirubin 41/119 by arm. Event selection must not inspect labs, examinations, documents, or future outcomes.

For each assay and selected event, define:

* `B`: latest finite uncensored assay in the TACE2 calendar-day window [day -30, day -1].
* `P`: latest finite assay in the selected repeat encounter in [event time -72 hours, event time).
* `Y`: nearest valid assay to event time +24 hours in (event time, event time +72 hours], with the inherited deterministic tie rule.

Require `B_time < P_time < event_time < Y_time` when Y exists and positive P lead. Construct `BP_eligible` after B and P, before reading Y; attach `Y_observed` afterward. Missing Y is missing, never a negative assay. Use origins 2021-01-01, 2022-01-01, 2023-01-01, and 2024-01-01; training events satisfy `event_date < origin`, and each future block is `[origin, origin + 365 days)`.

Fit only in pre-origin training using the locked specifications.

```
M0: Y ~ B + systemic-record indicator + age + sex indicators
       + TACE2-to-repeat days + P-lead hours
M1: M0 + P
```

Use training-only age median imputation plus age-missingness indicator, sex coding, variance filtering, centering/scaling, inner leave-one-patient-out alpha selection over `[0.01, 0.1, 1, 10, 100]`, and ridge fitting. The primary estimand remains observed complete-triplet standardized held-out RMSE gain
`G = (RMSE_0 - RMSE_1) / SD_test(Y)` with predictions from fixed pre-origin fits. Missing-Y diagnostics cannot change fitted rows, model, endpoint, or bootstrap denominator.

## Outcome-blind support and ascertainment layer

For every assay, origin, block, and arm, report the exact funnel `selected event -> has_B -> has_P -> BP_eligible -> Y_observed -> complete triplet`. Require at least 20 BP-eligible episodes overall and at least 10 in each arm in both training and future for an outcome-blind support gate; report the analogous complete-triplet gate separately. Failed gates remain descriptive and do not silently remove rows.

Among BP-eligible rows, before reading Y, define `exam_opportunity` as an examination row with valid `Start Time` in (event time, event time +72 hours], `followup_encounter` as an additional distinct encounter with valid `Visit Time` in that interval, and `document_presence` as a nonempty linked document row for the selected encounter. Report mutually exclusive precedence categories: exam+follow-up, exam only, follow-up only, document-only when neither timed indicator is present, and none. These are recording/opportunity proxies, not proof of completed care. Report counts, assay-specific fractions, Wilson 95% intervals, and a separate document cross-tab; suppress or mark cells under five episodes.

Fit the training-only pre-Y calendar-membership diagnostic using B, P, age, sex, P-lead hours, TACE2-to-repeat days, and arm. Report future propensity range, fraction outside training range, normalized training transport ESS overall/by arm, maximum normalized weight, and same-arm nearest-neighbor distance against the training 95th percentile. Weights are diagnostic only. Fit the training-only observation diagnostic for Y-observed using the same pre-Y variables and ascertainment indicators plus calendar block; report future observed fraction/Wilson interval, predicted probability range, Brier score, inverse-observation-probability ESS among observed rows, and pre-Y observed-versus-missing SMDs. Do not call this MAR evidence, imputation, or a primary-analysis weight.

## Compiler-proof partial-identification and missing-Y stress tests

Run this section for every assay, origin, and future block over **all** BP-eligible rows, including missing Y.

1. Fit M0/M1 only on observed, finite, complete pre-origin triplets. Freeze finite held-out predictions `p0_i` and `p1_i` for every future BP row. If any required prediction is nonfinite, stop the block's bound and label it computationally invalid; never drop that row to rescue the calculation.
2. Let `N` be the total number of BP-eligible rows in the block, `n_mis` the number with missing Y, and define the denominator as exactly `N` for overall bounds and exactly `N_a` for arm `a`, where `N_a` is that arm's BP-eligible count. Never use the complete-triplet denominator for a bound.
3. Set `L_train = min(Y_train)` and `U_train = max(Y_train)` over the exact finite training parser, before inspecting future Y. If the training range is empty or degenerate, or any observed future Y lies outside `[L_train,U_train]`, mark the temporal bound `unsupported` and do not widen the range. A full-source range may be reported only as a separately labeled descriptive check. If no future Y is observed, the training observed-Y mean may be used only as a training-derived tipping coordinate, not as a future outcome.
4. For observed rows, calculate `e0_i=(Y_i-p0_i)^2`, `e1_i=(Y_i-p1_i)^2`, and `d_i=e0_i-e1_i`. For missing row `i`, calculate model-specific squared-error endpoints

```
e_j,min = (clip(p_j,L_train,U_train)-p_j)^2
e_j,max = max((L_train-p_j)^2,(U_train-p_j)^2).
```

5. Calculate the M0-minus-M1 contrast through its affine identity, not by a quadratic optimization:

```
d_i(y) = (y-p0_i)^2-(y-p1_i)^2
       = 2*y*(p1_i-p0_i) + p0_i^2-p1_i^2.
```

Therefore missing-row contrast extrema are `min(d_i(L_train), d_i(U_train))` and `max(d_i(L_train), d_i(U_train))`. The sharp conditional fixed-prediction MSE contrast bounds are

```
Delta_lower = [sum_observed d_i + sum_missing min{d_i(L), d_i(U)}] / N
Delta_upper = [sum_observed d_i + sum_missing max{d_i(L), d_i(U)}] / N.
```

For arm-specific results replace both sums' denominator with `N_a` and use only rows in arm `a`. Report N, observed count, missing count, missing fraction, endpoint components, and three stress scenarios: all missing Y set to L; all set to U; and each missing row set to its least-favorable endpoint for the lower M0-minus-M1 contrast (`L` when `2(p1_i-p0_i) >= 0`, otherwise `U`). For each model separately, divide its SSE endpoints by N (or N_a) to obtain MSE endpoints. The conservative, non-primary RMSE-difference enclosure is

```
[sqrt(MSE0_lower)-sqrt(MSE1_upper),
 sqrt(MSE0_upper)-sqrt(MSE1_lower)].
```

Never call this enclosure sharp and never standardize it by an unidentified test SD. If the observed test-Y SD is nonfinite or zero, G and its CI are non-estimable while valid unstandardized bounds may still be emitted.

6. The deterministic common-displacement stress test sets all missing outcomes simultaneously to
`y_i(delta)=clip(m_ref+delta,L_train,U_train)`, where `m_ref` is the observed future-Y mean if any future Y is observed, otherwise the training observed-Y mean clearly labeled training-derived. Evaluate

```
Delta(delta) = [sum_observed d_i + sum_missing d_i(y_i(delta))] / N.
```

Because each contrast is affine and clipping changes only slopes, this function is continuous piecewise linear, with shared breakpoints `L_train-m_ref` and `U_train-m_ref`; there is no quadratic segment. On each segment, use slope
`sum_{missing,unclipped} 2(p1_i-p0_i)/N`, solve the linear equation analytically, retain roots only inside the segment, and verify each root by deterministic endpoint evaluation. Report all roots in `[L_train-m_ref,U_train-m_ref]`, then select the smallest absolute displacement, ties by smallest delta. If `Delta(0)==0`, report zero; if no root exists, report sign-robust for this common-displacement scenario. Also report whether the endpoint interval crosses zero. This is a sensitivity coordinate, not an imputation, estimate, or clinical plausibility assertion.

7. Optional uncertainty for bounded quantities must remain separate from deterministic identification regions. If run, use a declared-seed paired arm-stratified patient-frequency bootstrap with B=2000 (or record a smaller number only with resource-failure reason), resampling patients with replacement within arm and retaining all selected events. Keep pre-origin fits and all predictions fixed; do not refit or impute missing Y. For each replicate calculate the observed complete-triplet RMSE difference and divide by the original point-estimate `SD_test(Y)`, not a replicate SD. Report percentile 95% interval, replicate failures, and effective observed-patient clusters. Zero/undefined SD, no observed triplets, or fewer than two observed patient clusters means non-estimable, not zero. This CI does not repair outcome-selection bias and never merges with Delta bounds.

The submitted formula test artifact is `[internal dataset path]`; its managed execution output is `[internal dataset path]`, [source checksum], from job `[research job]` (return code 0). It tests the affine identity, per-row squared-error endpoints including predictions outside the training range, sharp fixed-denominator contrast endpoints by direct enumeration, and piecewise-linear common-displacement root/clipping behavior. Scope is explicitly formula/edge-case testing only: no HCC rows, outcomes, reconstruction, or clinical conclusion are read by this artifact. The earlier failed run due to a test harness bug was repaired before the successful run; it is retained only as compute provenance, not evidence.

## Interpretation and falsification contract

Supportive evidence requires successful source/hash/reconstruction/clock assertions, both outcome-blind and complete-triplet gates, an estimable prespecified primary result in an adequately supported block, no material ascertainment warning, and a deterministic Delta interval strictly above zero throughout the declared training-range scenario. This supports only selected short-horizon prognostic association in that calendar mixture. It does not establish transport, causality, treatment effect, response, safety, utility, or benefit.

Adverse evidence is a nonpositive primary contrast in an adequately supported block, repeated M1 degradation, or a Delta bound that includes a sign reversal under the declared training-range scenario. This challenges incremental prediction in the tested selected population; it does not prove B alone is sufficient or identify mechanism. Selection-sensitive evidence is favorable observed-case performance with Delta crossing zero, a near-boundary tipping point, strong observation gradient, or discrepant ascertainment patterns. Inconclusive evidence includes failed gates, unsupported/degenerate training range, future Y outside range, nonestimable SD or bootstrap, nonfinite predictions, low ESS, influential clusters, nonestimable small cells, or dependence on a full-source range. Under the retained audit, 2022 may remain locally supportive while 2023/2024 remain transport-inconclusive; no new HCC bound result is claimed.

The compiler/verifier must explicitly test that: missing Y is never treated as zero or a negative result; bound denominators are all BP rows and arm-specific BP rows; endpoint bounds do not alter model fitting or the fixed-SD bootstrap; affine contrast arithmetic is piecewise linear; out-of-range future Y invalidates the temporal bound; documents without native time cannot enter the Y window; examination/encounter/document presence is not completed follow-up; deterministic bounds are not confidence intervals; the RMSE enclosure is not called sharp; and a favorable observed estimate with a zero-crossing bound is selection-sensitive rather than supportive. Unsupported, adverse, and inconclusive branches must remain available.

Computational outputs can verify source hashes and headers, full scans, duplicate-safe joins, denominator reconstruction, exact clocks, outcome-blind funnels, diagnostic calculations, prediction finiteness, endpoint arithmetic, roots, and bootstrap bookkeeping. They cannot establish assay units/reference ranges, disease severity, tumor burden, imaging response, TACE intent or administration, transfusion/fluid exposure, external-care capture, mortality, hepatic failure, completed follow-up, causal effects, utility, actionability, or patient benefit. Those claims require clinical adjudication and independent temporal, external, or prospective data.

## What changed and what remains uncertain

Relative to `[prior hypothesis]`, this child adds an actually executed, managed formula/edge-case test harness, records its successful output hash and scope, makes the all-BP and arm-specific denominators explicit in every equation, and specifies testable stop conditions and interpretation branches for missing Y, nonfinite predictions, degenerate ranges, out-of-range observations, zero SD, and insufficient patient clusters. Relative to `[prior hypothesis]`, it retains the executed funnel, calendar-support, and observation-selection diagnostics while adding a mathematically sharp missing-Y layer that can be run on the frozen reconstruction without changing its population or estimand. It does not claim that missing Y has been observed, imputed, bounded empirically, or clinically adjudicated; execution of the full HCC bound pass remains a required downstream compiler job.


## Targeted compiler repair: executable bound-pass interface and audit ledger

The remaining gap is not the identification algebra; it is the lack of a fully specified hand-off from the frozen reconstruction/model predictions to a bound result that a compiler can execute and a verifier can audit. This child repairs that gap without changing the cohort, any clock, the annual forward blocks, the nested ridge estimand, or the noncausal interpretation.

### Frozen input contract (one row per assay-by-BP-eligible event)

The compiler shall materialize a UTF-8/Parquet or CSV artifact named `hcc_frozen_bp_predictions` in the writable workspace, with one and only one row per (`assay`, `event_id`, `origin`). `event_id` is a deterministic hash of (`Patient Master Index`,`TACE2 encounter key`,`repeat encounter key`,`event start`) created after the parent reconstruction; it is not a new patient identifier. Required columns are:

* `assay` (exactly `albumin` or `bilirubin`), `patient_id` (the source `patient master index`), `arm` (systemic-record or comparator), `origin` (one of 2021-01-01, 2022-01-01, 2023-01-01, 2024-01-01), `event_time`, `event_date`, and `block_role` (training or future);
* `B_time`, `P_time`, `y_time` and `y_observed`, where `y_observed` is true only when the deterministic nearest-Y rule selected a finite lab row in `(event_time,event_time+72 hours]`; missing Y is null and is never encoded as zero;
* `p0`, `p1`, and the exact integer/boolean fields `bp_eligible`, `selected_event`, `has_B`, `has_P`.

The compiler must assert uniqueness, `bp_eligible == true`, valid event and origin membership, `B_time < P_time < event_time`, and (when observed) `event_time < y_time <= event_time+72h` plus finite `y_observed`, `p0`, and `p1`. It must assert that each training/future row belongs to the inherited temporal rule (`event_date < origin` versus `[origin,origin+365 days)`) and that all required prediction values are finite before computing any bound. A failed assertion produces a block-level `computationally_invalid` record rather than row deletion.

The prediction artifact is a derived input, not a source replacement. Its provenance manifest must list the exact HCC source paths, table IDs, schema hashes, source SHA-256 values, no-sampling/full-scan declaration, duplicate-key audit, and the parent reconstruction version. The manifest must also record that `examinations` contributed only valid `Start Time` row presence, while `clinical_documents` contributed only nonempty linked-row presence and never a timestamp or Y value. The two assays are processed in separate partitions; no unit or scale conversion is allowed.

### Deterministic bound-pass algorithm and output schema

For each assay × origin × future block, first derive `L_train` and `U_train` from finite training `y_observed` only. Before inspecting future Y for the bound, freeze those two scalars and record `training_y_n`, `L_train`, and `U_train`. Then validate all finite observed future Y against the frozen range. If training Y is empty, nonfinite, or degenerate, or any observed future Y is out of range, emit status `unsupported_temporal_range` with the offending count and no widened bound. This status is not a failed cohort gate and must not be converted into an estimate.

For a valid block, the output `hcc_missing_y_bounds_long` has one row for each `assay, origin, block, arm_or_all, model_or_contrast, quantity, scenario`. It must contain `N_bp`, `n_observed_y`, `n_missing_y`, `missing_fraction`, denominator, observed contribution, missing contribution, lower, upper, and status. `arm_or_all` is `all`, `systemic-record`, or `comparator`; the denominator is `N_bp` for `all` and the corresponding arm-specific `N_bp` for an arm. The pass must assert `N_bp == n_observed_y+n_missing_y` separately for all and each arm and must fail loudly on a denominator mismatch.

For each model `j`, compute observed SSE and missing-row endpoint SSE, then report `mse_lower_j` and `mse_upper_j`. For the M0-minus-M1 contrast, compute observed `d_i` and the missing endpoints from the affine expression

`d_i(y)=2*y*(p1_i-p0_i)+p0_i^2-p1_i^2`,

using the minimum and maximum of `d_i(L_train)` and `d_i(U_train)` per missing row. Also emit the three explicit scenarios (`all_missing_L`, `all_missing_U`, and `least_favorable_lower`) as distinct rows, not merely as prose. The pass must compare its endpoint result against direct enumeration of both endpoints for each missing row in a small internal test fixture and fail package validation if they differ beyond a declared floating-point tolerance.

A second output, `hcc_missing_y_bounds_summary.json`, records exactly one machine-readable object per block with: input row hash; counts; frozen range; observed-Y range check; M0/M1 SSE and conservative RMSE enclosure; sharp fixed-prediction contrast bounds; endpoint scenario values; common-displacement breakpoints, all in-range roots, selected smallest-absolute root and tie rule; `endpoint_interval_crosses_zero`; and statuses. It must explicitly include `sd_test_y`, `primary_gain_estimable`, and `bootstrap_estimable` as separate fields. A nonfinite/zero observed test SD prevents standardized gain and its CI, but does not suppress valid unstandardized bounds. No field called `imputed_y`, `filled_y`, `completed_y`, or `causal_effect` may be created.

### Common-displacement and uncertainty safeguards

Implement the common-displacement pass by enumerating the two finite clipping breakpoints, evaluating the affine slope on each resulting segment, solving only roots inside `[L_train-m_ref,U_train-m_ref]`, and re-evaluating every retained root from the original row values. If `Delta(0)==0`, select zero; if no root exists, emit `no_in_range_root` and the sign-robust flag. The reference `m_ref` is the observed future-Y mean when available, otherwise the training observed-Y mean marked `training_derived`; it is a sensitivity coordinate and never a replacement value. `Delta` must be calculated with the same all-BP denominator as the endpoint bound (and repeated with each arm denominator), never the complete-triplet denominator.

If the optional paired patient-frequency bootstrap is requested, its manifest must carry the declared seed and replicate count, resample patients within arm while retaining all their selected events, freeze the original fits/predictions and original `SD_test(Y)`, and calculate only the complete-triplet observed-case gain. Replicate failures and effective observed patient-cluster counts are output explicitly. This CI is a sampling-uncertainty object for the observed-case quantity, not a confidence interval for the deterministic identification region; the two are printed in separate sections and are never intersected or merged.

### Verifier assertions and interpretation matrix

Package validation shall use synthetic fixtures to assert: (1) one missing Y changes neither ridge rows nor predictions; (2) all-BP and arm denominators differ from complete-triplet denominators when missingness exists; (3) an out-of-range observed future Y yields `unsupported_temporal_range` rather than range widening; (4) a document-only row cannot create a timed opportunity; (5) a favorable complete-triplet gain with a zero-crossing Delta interval is labeled `selection_sensitive`; and (6) a finite unstandardized bound with zero/undefined test SD leaves standardized gain `non_estimable`.

The interpretation dispatcher is deterministic: `supportive` requires an adequately supported block, estimable pre-specified observed-case gain, no material ascertainment warning, and a Delta interval strictly above zero; `adverse` includes a nonpositive gain or repeated M1 degradation in an adequately supported block; `selection_sensitive` takes precedence whenever the observed gain is favorable but the Delta interval crosses zero or observation/transport diagnostics are materially divergent; `unsupported` applies to invalid/degenerate/out-of-range temporal bounds or failed computational assertions; otherwise use `inconclusive`. These labels describe prognostic evidence only. In particular, no label implies TACE benefit, response, safety, utility, causal effect, or transport beyond the selected calendar mixture.

This repair makes the missing-Y layer directly executable and mechanically checkable from the frozen parent reconstruction while preserving the parent’s exact HCC bindings and already executed outcome-blind audit. It still cannot recover absent assays, establish assay units, verify TACE administration or intent, measure tumor response, mortality, hepatic failure, external-care capture, or prove clinical benefit; those require adjudicated or independent data.
