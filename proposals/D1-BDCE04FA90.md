# Support- and observation-robust forecast relevance for the frozen HCC repeat-TACE P-beyond-B experiment

## Purpose and scope

This is a substantive child of `[prior hypothesis]`, whose adult HCC repeat-TACE population, recorded systemic-record/comparator ontology, event reconstruction, assay-specific clocks, annual forward blocks, nested prognostic estimand, training-range missing-Y contract, and strict noncausal boundary are frozen. Nothing below changes the population, event clocks, model formula, primary endpoint, denominator of the primary endpoint, training folds, bootstrap target, or the claim boundary.

The unresolved evidence-to-decision problem is not merely whether P changes a prediction in an aggregate. A forecast movement could be an artifact of calendar extrapolation, a sparse arm, or differential recording of Y. Conversely, a forecast change that survives those threats is still not a clinical action rule because the records contain no validated assay units/reference ranges, patient-important endpoint, treatment intent, utility, or expert-defined threshold. The falsifiable successor question is:

> Within the frozen risk set, does P produce reproducible pre-event forecast movement and prognostic heterogeneity that remain interpretable after (i) restricting secondary outputs to prespecified training-supported calendar common support and (ii) conditioning on outcome-blind recording-opportunity strata, while the all-BP missing-Y identification envelope remains sign-resolving rather than selection-dependent?

The advance is a **support- and observation-robustness envelope**. It makes the evidence-to-decision bridge fail closed: a favorable complete-case movement is not called reproducible unless it survives an explicitly predeclared support mask, opportunity-stratum comparison, and the existing missing-Y bounds. The envelope is a surrogate forecast-relevance result only. It cannot establish that a clinician should order an assay, repeat TACE, alter medication, or accept a benefit-risk trade-off.

No new HCC empirical result is claimed. The retained executed audit supports at most a local 2022 association; later calendar blocks remain sparse and observation-selected. All support-envelope analyses in this proposal are unexecuted downstream compiler work.

## Exact dataset and source bindings

Use HCC snapshot `[source checksum]` and catalog `[internal dataset path]` with [source checksum]. Every source is an ordinary file, not an archive member. Read all source files read-only. Every linkage uses a deduplicated existence join on (`患者主索引`,`就诊号`); audit duplicate composite keys first, retain one Boolean/payload record per key as appropriate, and prohibit many-to-many multiplication. Emit only aggregate/de-identified output; never emit identifiers, names, identity numbers, phone/card numbers, raw text, or clinical notes.

The exact files and fields are:

* `encounters`, table `table-b743286cb1249287.json`, schema [source checksum], source `[internal dataset path]`, source [source checksum]; use `患者主索引`,`就诊号`,`年龄`,`性别`,`就诊时间`,`入院时间`,`出院时间`,`就诊科室`.
* `diagnoses`, table `table-12710723c3df0c99.json`, schema [source checksum], source `[internal dataset path]`, source [source checksum]; use `患者主索引`,`就诊号`,`诊断名称`, requiring exact `诊断名称 == 肝细胞癌`. This table has no time; inherit linked encounter time.
* `procedures`, table `table-d5eae16f8f8093d9.json`, schema [source checksum], source `[internal dataset path]`, source [source checksum]; use `患者主索引`,`就诊号`,`手术`,`开始时间`,`结束时间`,`手术来源`, the inherited case-insensitive `TACE` or literal `化疗栓塞` rule, valid `开始时间`, same-calendar-day collapse, first adjacent 14–180-day TACE1/TACE2 pair, and first strict 15–90-day repeat event.
* `medications`, table `table-4f6ecaeb6e8f69c2.json`, schema [source checksum], source `[internal dataset path]`, source [source checksum]; use `患者主索引`,`就诊号`,`用药`,`开始时间`,`结束时间`,`药品类型` for the inherited days-1–14 recorded systemic-record ontology and its placebo/prior-exposure/bevacizumab-only/generic-procedure exclusions. These are recorded orders, not verified administration or intent.
* `labs`, table `table-38aad8c54471332f.json`, schema [source checksum], source `[internal dataset path]`, source [source checksum]; use `患者主索引`,`就诊号`,`检验`,`定性结果`,`定量结果`,`标本类型`,`检验时间`. Analyze exact assays `白蛋白` and `总胆红素` separately, with finite uncensored numeric `定量结果`; there is no unit or reference-range field.
* `examinations`, table `table-fd016d2731b9d6c6.json`, schema [source checksum], source `[internal dataset path]`, source [source checksum]; use same-patient/same-encounter row presence and valid `开始时间` in the outcome-blind opportunity window only. Do not text-mine `检查所见` or `检查诊断`.
* `clinical_documents`, table `table-66afca58512c2fca.json`, schema [source checksum], source `[internal dataset path]`, source [source checksum]; use linked composite-key nonempty-row presence only, with duplicate header represented as `入院诊断__duplicate_2`. It has no native time and cannot be assigned to a Y window.
* `orders`, table `table-6b93dcf0ea823702.json`, schema [source checksum], source `[internal dataset path]`, source [source checksum]; if retained in the inherited opportunity audit, use only recorded presence/timing from `患者主索引`,`就诊号`,`医嘱(非药品)`,`开立时间`,`开始时间`,`结束时间`,`医嘱期限`,`医嘱状态`,`频次`, never as proof an intervention occurred.

`vitals` (`table-8436de9cba74b8ca.json`, source `[internal dataset path]`) and `transfers` (`table-320c20f732e71789.json`, source `[internal dataset path]`) are identifier-only and supply no covariates. They may be used only for duplicate-key audit. `front_page` is likewise nominal/identifier-only. No images or validated clinical reference ranges are available.

## Frozen reconstruction, clocks, and primary analysis

Reconstruct the parent exactly and assert the inherited denominators: 319 systemic-record patients and 1,491 comparator patients; 159 and 526 selected repeat events; observed complete triplets albumin 40/118 and total bilirubin 41/119 (systemic/comparator). Event selection must inspect only diagnoses, procedures, and encounter timing, not labs, examinations, documents, orders, medications, or future outcomes. Any mismatch stops interpretation and cannot trigger a silent redefinition.

For each assay separately:

* `B` is the latest finite uncensored assay in the TACE2 encounter calendar-day window [day -30, day -1].
* `P` is the latest finite uncensored assay in the selected repeat encounter in [event time -72 hours, event time).
* `Y` is the assay in that encounter in (event time, event time +72 hours], nearest +24 hours under the inherited deterministic tie rule.
* Require `B_time < P_time < event_time < Y_time`, positive P lead, and one patient-assay row after duplicate/tie handling. Construct `BP_eligible` before reading Y; absent Y is missing, never a negative.

Use origins 2021-01-01, 2022-01-01, 2023-01-01, and 2024-01-01, with training event date strictly before origin and future block [origin, origin+365 days), disjoint by construction. Preserve the locked training-only models:

```
M0: Y ~ B + systemic-record indicator + age + sex indicators
       + TACE2-to-repeat days + P-lead hours
M1: M0 + P
```

Preserve age median imputation plus missingness indicator, sex coding, variance filtering, centering/scaling, inner leave-one-patient-out alpha selection from [0.01, 0.1, 1, 10, 100], ridge fitting, and fixed pre-origin held-out predictions. The primary endpoint remains assay-specific observed complete-triplet standardized held-out RMSE gain `G=(RMSE_0-RMSE_1)/SD_test(Y)`. Preserve the inherited paired arm-stratified patient-frequency bootstrap with 2,000 replicates when feasible, fixed predictions, the original point-estimate `SD_test(Y)` denominator, declared seed, failure count, and the existing nonfinite/zero-denominator/two-cluster stops. No secondary support mask or opportunity result can alter any primary fit or endpoint.

Preserve the parent's deterministic training-range missing-Y contract. Compute `L_train=min(Y_train)` and `U_train=max(Y_train)` before inspecting future Y. If the range is empty/degenerate, any observed future Y lies outside it, or any required prediction is nonfinite, mark that block/stratum unsupported or computationally invalid rather than widening the range or dropping rows. For observed rows use `d_i=(Y_i-p0_i)^2-(Y_i-p1_i)^2`; for missing rows use

```
d_i(y)=2*y*(p1_i-p0_i)+p0_i^2-p1_i^2
lower_i=min(d_i(L_train),d_i(U_train))
upper_i=max(d_i(L_train),d_i(U_train)).
```

Sum over all BP-eligible rows and divide by the fixed BP denominator. Report all-missing-at-L, all-missing-at-U, and least-favorable-row endpoints as deterministic conditional identification regions, never confidence intervals. Preserve the parent piecewise-linear common-displacement tipping coordinate and its segment/root checks. No inverse-observation weighting, MAR assumption, imputation, or full-source range substitution is allowed.

## New support-robustness envelope (secondary, frozen-prediction only)

### 1. Pre-register the support mask before any future Y is read

The mask is defined separately for each assay and origin using training rows only, and uses only fields available by the selected event plus the locked model's pre-event prediction. It is not a replacement population and cannot change the primary estimand. Define continuous support variables as `age`, `B`, `P_lead_hours`, and `TACE2_to_repeat_days`; define categorical support variables as recorded arm and recorded sex category. For missing age, preserve the explicit missing-age category for descriptive strata but do not call the row in continuous common support. For missing B/P or invalid timing, the row is already outside `BP_eligible`.

The primary **training common-support mask** is:

* each continuous variable lies inclusively between its finite training 1st and 99th percentiles, computed separately within the corresponding assay/origin training risk set using the exact parser and no future rows;
* recorded arm and recorded sex category are levels observed in the corresponding training risk set; missing/other sex is one retained category if present in training;
* the row has a finite frozen `p0` and `p1`.

A quantile with fewer than 20 finite training values, a nonfinite/degenerate interval, or no retained row makes the mask unsupported for that assay/origin; do not silently substitute min/max. The 0th–100th-percentile (full observed training range) and 2.5th–97.5th-percentile masks are fixed sensitivity coordinates, not selected after seeing results. All boundaries are inclusive and ties are retained. Report the number and proportion excluded by each mask overall, by arm, calendar block, and prespecified heterogeneity stratum, without releasing row identifiers.

The support mask is an extrapolation diagnostic, not a claim that the future block is transportable. It must not use Y, Y-observation status, examinations, documents, post-event fields, or outcome-derived cutpoints. It also must not use an estimated propensity or an inverse weight to redefine the estimand.

### 2. Recompute only secondary forecast and identification outputs under support masks

For every assay, origin, future block, arm, and inherited one-dimensional stratum, report the parent all-BP outputs and, separately, the same outputs among rows in each support mask:

* median/IQR and mean signed `q=(p1-p0)/SD_train(Y)`;
* proportions with `|q| >= .10`, `.25`, `.50`;
* training-derived forecast-tercile crossings, rank displacement, and fixed decile-boundary crossing as exploratory summaries;
* observed-case `G_s` and `Delta_s` when their original gates pass;
* deterministic all-BP and support-masked `Delta_lower`/`Delta_upper`, with the same training `L_train/U_train`, fixed denominator equal to that mask's BP count, and all three missing-row endpoint scenarios;
* the conservative RMSE-difference enclosure only as a secondary descriptive quantity, never as the primary standardized estimand.

The masked analysis is a secondary conditional question, not an inverse-weighted estimate of the full future population. A mask with fewer than 20 BP rows overall, fewer than 10 in either arm when an arm comparison is claimed, fewer than 10 observed complete triplets, fewer than two observed patient clusters, or fewer than five rows for a crossing proportion is labelled sparse/non-estimable under the inherited rules. Never pool or replace sparse categories after seeing outcomes.

Define a **support-robust forecast-relevance status** only when the all-BP result and the primary 1st–99th support result both have finite predictions, valid training range, and the same qualitative direction/status for `q` movement and the bounded M0-versus-M1 contrast; the 0–100% and 2.5–97.5% masks must be reported as sensitivity, not cherry-picked. If the all-BP favorable result disappears, reverses, or becomes unsupported under the primary mask, label it extrapolation-sensitive, not supportive. If all masks are sparse, label support-inconclusive. A stable sign does not establish transport or clinical benefit.

### 3. Opportunity-conditioned observation robustness

Before reading Y, carry forward the mutually exclusive outcome-blind recording-opportunity categories from the parent:

* `exam+follow-up`: an examination with valid `开始时间` in (event_time,event_time+72h] and an additional distinct encounter with valid `就诊时间` in that interval;
* `exam only`;
* `follow-up only`;
* `document-only` when neither timed indicator is present but the selected encounter has a nonempty linked clinical-document row;
* `none`.

A clinical-document row has no native time and is never put in the Y window. Examinations, encounters, documents, orders, medications, and procedures are recording/opportunity proxies only; none proves completed follow-up, assay review, administration, intent, or need.

For each assay/origin/block/arm and each inherited stratum, report by opportunity class before inspecting Y: BP count, support-mask count, observed-Y count/fraction with Wilson interval, missing fraction, and exclusion fraction. Then, after fixing predictions, report q movement and all-BP Delta endpoints separately by opportunity class. Apply the inherited sparse rules, with a minimum of 10 BP rows and 5 observed complete triplets for a class to receive a directional observed-case label; otherwise show counts and `inconclusive` only.

Define an **observation-robust status** only if every opportunity class with at least 10 BP rows has the same directional q summary and no class with at least 10 BP rows has a bounded Delta interval of opposite strict sign; if fewer than two classes meet this support, status is observation-inconclusive rather than homogeneous. A favorable result confined to a class with a materially higher Y-observation fraction, or with an observed-versus-missing pre-Y SMD >=0.5 for B, age, P lead, interval, arm, or baseline forecast tier, is selection-sensitive even when the global all-BP endpoint is positive. Report the exact SMD and observation fraction; do not call this missing-at-random evidence.

This is a robustness label, not a reweighted estimand. Opportunity classes are not used as post-outcome covariates, treatment proxies, or clinical quality metrics. A shifted-window recording control (event+7 through event+10 days), source-family leave-one-out opportunity recomputation, and the parent's P-only restricted-linkage placebo remain required diagnostics. Similar forecast-movement magnitude in the shifted window, a P-placebo pattern as favorable as the real P pattern, or instability when one opportunity source family is omitted is adverse/selection-sensitive according to the inherited precedence.

### 4. Calendar-support interpretation matrix

For each future block, emit one deterministic status row crossing: (a) primary all-BP versus 1st–99% support mask, (b) observed-case versus all-BP bounded sign, and (c) observation-robust versus observation-sensitive status. The precedence is:

1. reconstruction/clock or computation invalid;
2. training range unsupported or observed future Y outside range;
3. sparse/non-estimable or failed arm/patient-cluster gate;
4. adverse (M1 no better, placebo reproduces the signal, or stable nonpositive contrast);
5. extrapolation-sensitive or observation-selection-sensitive;
6. support- and observation-robust surrogate forecast relevance.

A block may be called **support- and observation-robust surrogate-supportive** only if all of the following hold: inherited reconstruction and primary gates pass; the primary forecast movement and bounded contrast are finite; all-BP and 1st–99% mask status agree; no stricter declared mask creates a contradictory supported direction; at least two adequately supported opportunity classes agree; observed/missing pre-Y SMD flags are absent or explicitly judged non-material under the inherited threshold; the real P-only placebo attenuates as expected; the no-increment control is exact; and no calendar/arm support failure is present. The permitted statement remains only that P adds selected short-horizon prognostic information and reproducible record-level forecast movement in the supported calendar mixture. It is not a treatment or monitoring policy.

If the observed-case gain is favorable but the all-BP bound crosses zero, label selection-sensitive. If the all-BP gain is favorable but the support mask reverses or becomes unsupported, label extrapolation-sensitive. If the forecast movement persists but the opportunity classes disagree or observation gradients are material, label observation-selection-sensitive. If all statuses are finite but the full and masked results agree only in one sparse calendar block or arm, label calendar/arm-inconclusive. Never call a nonsignificant heterogeneity contrast proof of homogeneity.

## Falsification and implementation controls

The compiler and verifier must execute or fixture-test the following without changing the primary fit.

1. **Exact no-increment control.** Set frozen M1 predictions equal to frozen M0 predictions. Require q=0, no tier crossings, Delta endpoints=0, and zero support differences up to declared floating-point tolerance. Failure is a computational invalidity.
2. **Restricted P-linkage placebo.** Within each training/future partition, permute raw P only within inherited arm and broad calendar block, keeping B, core, Y, row membership, patient folds, event dates, and observation pattern fixed. Recompute the nested pipeline and all secondary outputs. A placebo as favorable as the real signal is adverse to P attribution; this is not exact conditional randomization.
3. **Timing placebo.** Use the prior eligible assay or explicit missing P, never a post-event value, for descriptive movement only. Failure to define a valid prior assay is inconclusive.
4. **Support-mask fixture.** Synthetic rows exactly at 1st/99th boundaries must be retained; rows just outside excluded; future Y must never alter the mask. Missing age and an unseen sex category must be status-labelled, not median-reassigned into continuous support.
5. **Opportunity fixture.** Synthetic timestamps exactly at event, +72 hours, +7 days, and +10 days must follow open/closed boundaries. Untimed documents cannot enter a timed window. An additional encounter must have a distinct `就诊号`; duplicate source rows must not inflate opportunity counts.
6. **Bound arithmetic fixture.** Test positive and negative affine slopes, endpoint reversal, all-observed, all-missing, and outside-training-range cases. Verify support-mask denominators are fixed within their declared conditional analysis and never substituted into the primary endpoint. Verify common-displacement tipping remains piecewise linear.
7. **Calendar and arm leave-outs.** Remove each calendar block or arm only as a descriptive sensitivity. A result found only in one unsupported/sparse arm or one block cannot receive a robust label.
8. **Assay separation.** Albumin and total bilirubin have independent parsers, model fits, `SD_train`, quantiles, masks, bounds, and outputs. Any pooling or shared cutpoint is a hard failure.
9. **Observation negative controls.** Shift the recording window to [event+7 days,event+10 days] and omit examinations, encounters, and documents one source family at a time. Similar movement or large dependence on one source family is a selection warning, not evidence of actionability.
10. **Unsupported-conclusion fixtures.** The verifier must reject calling empirical forecast tiers clinical thresholds, q movement benefit, subgroup differences causal effect modification, recorded orders/medications/procedures completed care, deterministic bounds confidence intervals, or a robust label when the all-BP envelope crosses zero or the support/opportunity gate fails. It must also reject claiming homogeneity from a nonsignificant contrast.

## Stop rules and evidence limits

Stop the affected block or secondary cell rather than repairing silently for: denominator mismatch; duplicate-join multiplication; invalid clock or tie rule; nonfinite prediction; empty/degenerate training range; observed future Y outside training range; zero/nonfinite `SD_train` for q; fewer than two observed patient clusters; insufficient BP/arm/opportunity/support counts; unsupported quantile mask; unseen categorical support; assay pooling; any post-event or Y-derived stratum/cutpoint; or a prediction/threshold derived from future rows. Preserve the primary result only if the primary pipeline itself remains valid; a failed secondary layer is not allowed to rewrite it.

Computationally checkable outputs are source and schema hashes, duplicate-safe joins, inherited denominators/events/clocks, pre-event mask membership, frozen predictions, q and tier movement, observed-case contrasts, all-BP and support-masked deterministic bounds, opportunity fractions/SMDs, calendar/arm support diagnostics, placebo bookkeeping, and precedence status. These records cannot identify laboratory units, reference ranges, severity, imaging response, tumor burden, hepatic decompensation, mortality, toxicity, patient-reported outcomes, verified administration, treatment intent, external-care capture, clinician review, utility, acceptable trade-offs, treatment effects, safety, benefit, or transport.

Even a support- and observation-robust surrogate result would establish only a selected, short-horizon prognostic association and reproducible record-level forecast movement. It would not show that measuring P changes care or outcomes. A consequential decision claim requires unit-validated assays, expert adjudication of clinically meaningful thresholds and decisions, patient-important outcomes and adverse events, treatment intent/exposure, and an independent temporal/external or prospective cohort. The experiment therefore repairs interpretability and falsifiability at the evidence-to-decision boundary without pretending that a record-defined forecast category is a clinical action rule.

## Provenance retained from the parent

Retain the parent audit artifact `[internal dataset path]`, [source checksum], as historical evidence only. Do not claim that the new support masks, opportunity-conditioned envelopes, or robustness statuses have been executed.
