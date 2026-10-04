# HCC repeat-TACE P-beyond-B: executable fixed-prediction missing-Y bound pass

## Targeted successor and preserved design

This targeted successor of `[prior hypothesis]` preserves the frozen adult HCC repeat-TACE prognostic question, cohort, clocks, annual forward blocks, outcome-blind support/ascertainment audit, locked nested-ridge estimand, and noncausal evidence limits. The question remains whether pre-repeat assay `P` adds short-horizon prognostic information for subsequent assay `Y` beyond remote assay `B` and the locked pre-event core. It is not a treatment-effect, response, safety, utility, action-rule, transport, or clinical-benefit analysis.

The substantive repair is an executable, fail-closed missing-`Y` partial-identification pass. The parent had an algebraic contract and formula oracle but left the clinically decisive pass downstream. This child supplies a runnable JSON interface and managed execution on a fixture that exercises overall and arm-specific all-`BP_eligible` denominators, missing outcomes, predictions outside the training range, model-specific SSE endpoints, sharp affine contrast endpoints, conservative RMSE enclosures, common-displacement clipping/tipping behavior, zero/undefined SD handling, and training-derived reference labeling. The fixture is deliberately synthetic and is not HCC evidence; no HCC outcome is imputed or recovered.

## Evidence boundary and exact frozen inputs

The retained parent evidence remains the only empirical HCC support: a no-sampling full-source audit of the frozen snapshot reconstructed 319 systemic-record and 1,491 comparator patients, 159 and 526 selected repeat events, 242 `BP_eligible` episodes per assay, and complete triplets of albumin 40/118 and total bilirubin 41/119 by arm. The audit found 2022 locally supported by its pre-specified gates, while later blocks had severe observation loss (including 29/43 observed in 2023 and 14/70 in 2024 overall, with 1/9 systemic in 2024). These facts motivate the bound pass but do not establish robustness or benefit.

Use snapshot `[source checksum]` and catalog `[internal dataset path]` (catalog [source checksum]). The frozen reconstruction must scan every row, without sampling, from these ordinary read-only CSVs and schemas:

* `encounters`, `table-b743286cb1249287.json`, `[internal dataset path]`, columns `患者主索引`, `就诊号`, `年龄`, `性别`, `就诊时间`, `入院时间`, `出院时间`, `就诊科室`.
* `diagnoses`, `table-12710723c3df0c99.json`, `[internal dataset path]`, exact `诊断名称 == 肝细胞癌`; time inherited from encounter.
* `procedures`, `table-d5eae16f8f8093d9.json`, `[internal dataset path]`, `患者主索引`, `就诊号`, `手术`, `开始时间`, `结束时间`, `手术来源`; identify case-insensitive `TACE` or literal `化疗栓塞`, deduplicate same patient/calendar date, choose the first adjacent 14–180-day pair and first strict 15–90-day event.
* `medications`, `table-4f6ecaeb6e8f69c2.json`, `[internal dataset path]`, apply the inherited days 1–14 systemic-record ontology and exclusions; recorded orders are not verified administrations.
* `labs`, `table-38aad8c54471332f.json`, `[internal dataset path]`, columns `患者主索引`, `就诊号`, `检验`, `定性结果`, `定量结果`, `标本类型`, `检验时间`; use exact `白蛋白` and `总胆红素`, finite uncensored numeric `定量结果`, and never pool assays.
* Outcome-blind `examinations`, `table-fd016d2731b9d6c6.json`, `[internal dataset path]`; use only valid `开始时间` and row presence, never text-mine `检查所见` or `检查诊断`.
* Outcome-blind `clinical_documents`, `table-66afca58512c2fca.json`, `[internal dataset path]`; use nonempty linked-row presence only. `入院诊断__duplicate_2` is the duplicate header; this table has no time and cannot supply a `Y` timestamp.

All encounter joins are deduplicated existence joins on (`患者主索引`,`就诊号`), with composite-key duplicate counts audited before joining. Patient-level sequencing uses `患者主索引` only where frozen. Define `B` as latest finite assay in TACE2 [day -30, day -1], `P` as latest assay in the selected repeat encounter [event -72 h, event), and `Y` as nearest valid assay to event +24 h in (event, event +72 h], using the inherited deterministic tie rule. Build `BP_eligible` before inspecting `Y`; missing `Y` stays missing. Origins are 2021-01-01 through 2024-01-01, with training event date < origin and future block `[origin, origin+365 days)`.

## Fixed-prediction bound contract

The upstream frozen runner fits exactly the locked models only on observed complete training triplets:

`M0: Y ~ B + systemic indicator + age + sex indicators + TACE2-to-repeat days + P-lead hours`; `M1: M0 + P`.

It performs training-only age median imputation plus missingness indicator, sex coding, variance filtering, centering/scaling, inner leave-one-patient-out alpha selection over `[0.01,0.1,1,10,100]`, and ridge fitting. It then freezes finite held-out `p0_i,p1_i` for **every** future `BP_eligible` row, including rows with missing `Y`. A nonfinite prediction fails closed; no row is dropped.

For every assay, origin, future block, and arm, the runner consumes `training_y`, `assay`, `origin`, and rows containing `arm`, `y` (null only for missing), `p0`, and `p1`. It sets `L=min(Y_train)` and `U=max(Y_train)` from the exact finite training parser before future outcomes are used. Empty/degenerate training range or any observed future `Y` outside `[L,U]` yields `unsupported`, without widening the range. Overall bounds use `N=all BP_eligible rows`; arm bounds use that arm's `N_a`; complete-triplet counts are never denominators.

For observed rows, `d_i(y)=(y-p0_i)^2-(y-p1_i)^2`. For missing rows, calculate model-specific SSE endpoint sums using `(clip(p_j,L,U)-p_j)^2` and `max((L-p_j)^2,(U-p_j)^2)`. Use the exact affine identity `d_i(y)=2y(p1_i-p0_i)+p0_i^2-p1_i^2`; missing contrast endpoints are the min/max of `d_i(L),d_i(U)`. Report `Delta_lower`, `Delta_upper`, observed/missing counts and fractions, observed and missing endpoint components, all-missing-`L`, all-missing-`U`, and per-row least-favorable lower-contrast assignments. Report the conservative, explicitly non-sharp unstandardized RMSE-difference enclosure `[sqrt(MSE0_lower)-sqrt(MSE1_upper), sqrt(MSE0_upper)-sqrt(MSE1_lower)]`. It is never a confidence interval and is never standardized by unidentified test SD.

For common displacement, use `y_i(delta)=clip(m_ref+delta,L,U)` for all missing rows, with `m_ref` the future observed-Y mean when available, otherwise the training observed-Y mean explicitly labeled training-derived. Evaluate the continuous piecewise-linear `Delta(delta)` over `[L-m_ref,U-m_ref]`, solve its affine segment analytically, verify roots by direct evaluation, choose smallest absolute root (ties by smallest delta), and report endpoint sign crossing. No root is a sign-robust common-displacement result; a zero-crossing bound is selection-sensitive rather than supportive.

The primary standardized held-out RMSE gain and optional fixed-fit paired patient bootstrap remain unchanged and separate. A missing-Y bound cannot alter model fitting, held-out predictions, endpoint, bootstrap denominator, or complete-triplet estimand. If observed test-Y SD is undefined/zero, `G` is non-estimable, while unstandardized bounds may remain valid. Bootstrap with fewer than two observed patient clusters is non-estimable, not zero, and its CI cannot repair selection bias.

## Executed artifact and interpretation

Draft runner: `[internal dataset path]`, [source checksum]. Managed fixture input: `[internal dataset path]`, [source checksum]. Managed output: `[internal dataset path]`, [source checksum], from successful job `[research job]` (return code 0, 0.54 s, 1 CPU, 2 GiB). The output is a fixture computation only and carries the explicit nonclaim that it is not an HCC result.

The managed fixture demonstrates the required branches without being evidence: its albumin all-row bound is `[-5.5625,18.4375]` and crosses zero, its arm-level common-displacement example has a verified root, its bilirubin example has a positive deterministic interval but non-estimable SD. These outputs show that the interface preserves missing rows and denominators and does not silently convert non-estimability into zero. The compiler must run the same runner on actual frozen model predictions and emit per-assay/per-origin/per-arm records; this child does not claim that downstream HCC execution has occurred.

Supportive empirical interpretation requires all source/hash/reconstruction/clock assertions, outcome-blind and complete-triplet gates, an estimable primary result in a supported block, no material ascertainment warning, and a deterministic `Delta` interval strictly above zero under the declared training-range scenario. A favorable complete-case result with a bound crossing zero is selection-sensitive. Adverse evidence includes nonpositive primary contrast, repeated M1 degradation, or a bound containing a sign reversal in an adequately supported block. Unsupported/degenerate range, future out-of-range Y, nonfinite predictions, failed support, low ESS, influential clusters, or non-estimable SD/cluster bootstrap are inconclusive, not null findings.

Computational execution cannot establish assay units/reference ranges, disease severity, tumor burden, imaging response, TACE intent/administration, external-care capture, mortality, hepatic failure, completed follow-up, causality, utility, actionability, or patient benefit. Those require clinical adjudication and independent temporal, external, or prospective data. The decisive remaining uncertainty is the actual HCC bound pass on frozen predictions and whether its identification region remains favorable; no missing assay is imputed here.
