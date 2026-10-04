# HCC repeat-TACE P-beyond-B: observation-robustness and decision-resolution successor

## Targeted successor and unchanged scientific claim

This is a targeted successor of `[prior hypothesis]`. It preserves the parent's frozen adult HCC repeat-TACE population, selected event algorithm, calendar origins and forward blocks, B/P/Y clocks, outcome-blind cohort construction, locked ridge models M0 and M1, complete-triplet held-out standardized RMSE gain estimand, and noncausal claim boundary. No population, clock, estimand, model specification, endpoint, or primary denominator is changed.

The unresolved question remains whether the contemporaneous pre-repeat assay P adds short-horizon prognostic information for the subsequent same-encounter assay Y beyond remote baseline B and the locked pre-event core, among the selected adult repeat-TACE episodes. The parent correctly showed why favorable complete-triplet performance may be observation-selected and supplied all-BP missing-Y bounds. This child adds a clinically substantive, computable resolution layer: can the sign of the incremental prediction claim be made robust across the observed opportunity/recording regimes, and what minimum additional outcome adjudication would be needed to resolve an otherwise selection-sensitive result? This is decision relevance for prioritizing prospective data completion and assay follow-up, not a patient treatment rule, clinical utility estimate, treatment effect, or benefit claim.

The strongest available evidence remains the parent's executed outcome-blind audit: exact reconstruction, supported 2022, and severe later observation loss (including 29/43 observed in 2023 and 14/70 in 2024). The supplied formula oracle validates missing-Y arithmetic only; it is not HCC evidence. No new HCC result is claimed here.

## Exact frozen source bindings and metadata

Use HCC snapshot `[source checksum]`, catalog `[internal dataset path]` ([source checksum]), and scan all rows of the ordinary, read-only CSV files named below. Archive member for every source is `ordinary file`.

* `encounters`, table schema `table-b743286cb1249287.json`, source `[internal dataset path]`, [source checksum]; use `患者主索引`, `就诊号`, `年龄`, `性别`, `就诊时间`, `入院时间`, `出院时间`, `就诊科室`.
* `diagnoses`, `table-12710723c3df0c99.json`, source `[internal dataset path]`, [source checksum]; use `患者主索引`, `就诊号`, `诊断名称`, `诊断类型`; select `诊断名称 == 肝细胞癌`, inheriting linked encounter timing because diagnoses has no native timestamp.
* `procedures`, `table-d5eae16f8f8093d9.json`, source `[internal dataset path]`, [source checksum]; use `患者主索引`, `就诊号`, `手术`, `开始时间`, `结束时间`, `手术来源`; identify case-insensitive `TACE` or literal `化疗栓塞`, require valid `开始时间`, collapse same-patient same-calendar-day duplicates, and retain the parent's first adjacent 14–180-day TACE1/TACE2 pair and first strict event 15–90 days after TACE2.
* `medications`, `table-4f6ecaeb6e8f69c2.json`, source `[internal dataset path]`, [source checksum]; apply the inherited days 1–14 systemic-record ontology and all placebo, prior-exposure, bevacizumab-only, and generic-procedure ambiguity exclusions. These are recorded orders, not verified administration.
* `labs`, `table-38aad8c54471332f.json`, source `[internal dataset path]`, [source checksum]; use `患者主索引`, `就诊号`, `检验`, `定性结果`, `定量结果`, `标本类型`, `检验时间`; exact assays `白蛋白` and `总胆红素`, finite uncensored `定量结果`, and native `检验时间`. There is no unit or reference-range column, so never pool assays and do not infer clinical thresholds.
* `examinations`, `table-fd016d2731b9d6c6.json`, source `[internal dataset path]`, [source checksum]; use only valid `开始时间` and linked-row presence; never text-mine `检查所见` or `检查诊断`.
* `clinical_documents`, `table-66afca58512c2fca.json`, source `[internal dataset path]`, [source checksum]; use nonempty linked-row presence only. The duplicate header is `入院诊断__duplicate_2`; this table has no time and cannot supply a Y-window timestamp.

All linked tables use a deduplicated existence join on (`患者主索引`,`就诊号`), with duplicate composite-key counts reported before joining and no many-to-many multiplication. Patient-level sequencing uses `患者主索引` only under the inherited rules.

## Frozen population, clocks, models, and primary analysis

Reconstruct and assert the parent's exact counts: 319 systemic-record patients, 1,491 comparator patients, 159 and 526 selected repeat events, and albumin/bilirubin complete-triplet counts of 40/118 and 41/119 by arm. Event selection must not inspect labs, examinations, documents, or future outcomes.

For each assay and event retain:

* B = latest finite assay in the TACE2 calendar-day window [day -30, day -1].
* P = latest finite assay in the selected repeat encounter in [event time -72 hours, event time).
* Y = nearest valid assay to event time +24 hours in (event time, event time +72 hours], using the parent's deterministic tie rule.

Assert `B_time < P_time < event_time < Y_time` when Y exists and positive P lead. Form `BP_eligible` after B/P and attach `Y_observed` only afterward; missing Y is missing, not a negative result. Origins remain 2021-01-01, 2022-01-01, 2023-01-01, and 2024-01-01; training is `event_date < origin`, future is `[origin, origin+365 days)`.

Fit only in pre-origin training:

```
M0: Y ~ B + systemic-record indicator + age + sex indicators
       + TACE2-to-repeat days + P-lead hours
M1: M0 + P
```

Retain training-only age median plus missingness indicator, sex coding, variance filtering, scaling, inner leave-one-patient-out alpha selection over `[0.01,0.1,1,10,100]`, and ridge fitting. The primary outcome remains observed complete-triplet held-out standardized RMSE gain `G=(RMSE0-RMSE1)/SD_test(Y)`, with fixed pre-origin predictions. Neither the new layer nor missing-Y bounds changes fitted rows, endpoint, model, or bootstrap denominator.

## New repair A: ascertainment-regime robustness decomposition

The parent's opportunity categories are retained and made analytically consequential without treating them as completed care. For every assay, origin, arm, and future block, assign every BP-eligible row exactly one pre-Y category using valid examination `开始时间` in (event,event+72h], an additional distinct encounter with valid `就诊时间` in that interval, and nonempty linked clinical-document row for the selected encounter, with the inherited precedence: `exam+follow-up`, `exam only`, `follow-up only`, `document-only` when neither timed indicator is present, and `none`. A document has no timestamp and never enters the Y window. Cells under five are descriptive/suppressed, not pooled silently.

Before reading Y, create an immutable row ledger containing category, assay, arm, calendar block, B/P covariates, prediction inputs, and category membership. For each category with at least 10 BP-eligible rows overall and at least 5 in each relevant arm when arm-specific reporting is requested, report N, Y-observed fraction, Wilson interval, observed-versus-missing SMDs, complete-triplet RMSE gain, and the parent's fixed-prediction missing-Y contrast interval with the category's BP-eligible denominator. Fit models only once under the frozen primary design; these are fixed-prediction diagnostic strata, not refitted subgroup estimands.

Report the decomposition identity for each estimable block:

```
Delta_global = sum_s (N_s/N) * Delta_s
```

where each `Delta_s` is the M0-minus-M1 MSE contrast bound using the same training-range endpoints and fixed predictions. Assert that the weighted lower and upper sums equal the global all-BP bounds within declared floating-point tolerance. Do not average standardized gains across strata and do not combine incompatible assay intervals. Also report the range of category-specific observed complete-case gains and the maximum absolute contribution `(N_s/N)*Delta_s`.

Predeclare an observation-robust sign label. `robust-positive` requires every non-suppressed category interval and the global interval to be strictly above zero; `robust-nonpositive` requires every non-suppressed category upper endpoint to be <=0; `observation-sensitive` applies when the global interval crosses zero, category intervals disagree in sign, or the only positive result is a category with a materially higher observation fraction and the contrast cannot be evaluated in the lower-observation categories; `inconclusive` applies to failed/degenerate training range, out-of-range future Y, nonfinite predictions, inadequate cells, or nonestimable SD. This label is not a causal interaction or transport guarantee. It asks whether the prognostic comparison survives recorded-care opportunity regimes.

Repeat the same decomposition by calendar block and systemic-record/comparator arm, with the parent's minimum gates. Calendar/arm strata are descriptive robustness diagnostics; no reweighting changes the primary estimand. Report normalized training transport ESS, future propensity range, outside-range fraction, nearest-neighbor distance, and observation-model diagnostics exactly as in the parent. If a favorable block is not supported in both ascertainment regimes, label the result selection-sensitive even if the pooled observed estimate is favorable.

## New repair B: decision-resolution frontier for prospective outcome completion

Because no HCC unit, reference range, validated clinical threshold, mortality, liver failure, tumor burden, imaging response, or treatment-benefit endpoint is available, do not claim patient-level clinical utility or construct a treatment alert. Instead, make the consequential next-study decision computable: whether additional timed Y ascertainment/adjudication could resolve the sign of the prognostic comparison.

For each future assay/origin/block and each BP-eligible missing-Y row, retain the fixed predictions `p0_i,p1_i`, the training-range endpoint `[L_train,U_train]`, and contrast endpoints `l_i=min(d_i(L),d_i(U))`, `u_i=max(d_i(L),d_i(U))`. Keep the parent's global and arm-specific all-BP bounds as primary. Add the following deterministic, non-empirical outputs.

1. **Resolution gap.** Report global lower/upper contrast, zero-crossing status, number and fraction missing, and the sum of interval widths `W=sum_missing(u_i-l_i)/N`. Report the analogous values by ascertainment category and arm, but do not pool strata with different unsupported statuses.
2. **Adjudication priority curve.** Rank missing rows only by their current uncertainty width `(u_i-l_i)` with deterministic ties by patient identifier, selected event time, and assay. For k = 0,1,...,n_missing, calculate the *oracle resolution envelope* after revealing the exact Y for the first k rows: the remaining unresolved rows retain `[l_i,u_i]`, while revealed rows are represented by a required input slot and not assigned a guessed value. The output must distinguish (a) computable current interval, (b) interval conditional on supplied adjudicated values, and (c) a hypothetical best-case envelope in which each selected row resolves at its favorable endpoint. Never present the best-case curve as an expected benefit or as an observed result.
3. **Minimum sufficient adjudication under observed values.** When a downstream compiler supplies actual, valid Y for a missing row, replace only that row's endpoint by its observed `d_i(Y_i)` and recompute fixed-denominator bounds. Find the smallest k for which the resulting interval is strictly positive, strictly nonpositive, or remains crossing zero. If no supplied adjudications resolve the sign, report unresolved rather than zero. This is a deterministic stopping rule for data completion, not an assumption about unobserved outcomes.
4. **Worst-case and favorable-case study planning limits.** Calculate the smallest k at which even the favorable endpoint envelope becomes strictly positive, and the smallest k at which even the adverse endpoint envelope becomes nonpositive, when such k exists. If neither exists, report “no deterministic resolution with endpoint-only planning.” These are feasibility bounds on information collection and must not be called sample-size calculations, power, or clinical utility.
5. **Decision relevance statement.** For an interval that crosses zero, the correct operational decision is “do not treat P as decision-ready; prioritize timed outcome completion/clinical adjudication.” For a sign-robust interval with adequate opportunity strata, the operational decision is “the prognostic comparison is observation-robust under the recorded-data stress contract,” still not “use P clinically.” For a robust adverse interval, deprioritize P as an incremental prognostic candidate in this selected population, without concluding B is clinically sufficient. For a nonestimable or transport-failed block, retain “evidence insufficient; do not extrapolate.”

The frontier must preserve the original observed-test SD distinction: deterministic unstandardized MSE intervals are not confidence intervals; G and its bootstrap CI remain complete-triplet quantities. If SD is zero/nonfinite, report G nonestimable while still reporting valid unstandardized fixed-denominator bounds when their range conditions pass. Bootstrap, if run, remains the parent's declared-seed patient-frequency bootstrap with fixed fits/predictions and B=2000 (or explicit resource-failure reason), never refitted for the frontier.

## Falsification and verifier contract

The compiler/verifier must test both favorable and unfavorable fixtures and assert that:

* all exact source hashes, headers, duplicate-safe joins, inherited counts, clocks, and frozen model specifications remain unchanged;
* the row ledger assigns each BP row to one and only one precedence category, uses no Y to define category, and never gives a document a timestamp;
* weighted category bounds reproduce the global all-BP bound, with denominators N and N_a, not complete-triplet counts;
* missing Y is never recoded as zero, negative, or a fabricated lab value;
* category sign disagreement produces observation-sensitive, not supportive, status;
* a favorable complete-case result with zero-crossing global or category bounds is selection-sensitive;
* out-of-range future Y, empty/degenerate training range, nonfinite predictions, inadequate strata, and nonfinite/zero SD fail closed with explicit statuses;
* oracle resolution curves are labeled hypothetical and cannot be emitted as empirical HCC results;
* actual supplied adjudications alter only the corresponding fixed-prediction endpoint component and cannot refit models or change the primary denominator;
* deterministic intervals are not confidence intervals and the frontier is not power, sample-size, utility, or a treatment threshold;
* supportive, adverse, observation-sensitive, and inconclusive branches are all reachable and correctly interpreted.

Computationally checkable claims include source integrity, cohort reconstruction, row-level category membership, funnel counts, fixed-prediction arithmetic, decomposition identities, interval signs, resolution-frontier bookkeeping, and bootstrap bookkeeping. Clinical adjudication remains essential for whether a recorded row reflects a collected specimen, whether assay values are comparable in units/reference ranges, whether TACE was administered/intended, whether follow-up was completed, and whether any prognostic association is clinically useful. External validation, timed prospective capture, and a clinically defined outcome would be required before any patient-care action or benefit claim.

## Interpretation and changed evidence boundary

Supportive evidence now requires the parent's reconstruction and support gates, an estimable primary result, and either a global deterministic interval strictly above zero with no category sign conflict and adequate ascertainment strata, or a transparently labeled local result when only a supported block qualifies. This supports only an observation-robust, selected, recorded-scale prognostic association under the declared training-range scenario; it does not establish transport, causality, treatment response, safety, utility, or benefit.

Adverse evidence is a robustly nonpositive primary/bounded contrast across adequate strata or repeated M1 degradation. Observation-sensitive evidence is favorable observed-case performance whose global or category interval crosses zero, a category sign reversal, a strong observation gradient, or favorable performance confined to opportunity-rich rows. Inconclusive evidence includes all inherited gate failures plus nonestimable strata, out-of-range future values, low transport/observation ESS, influential patients, or inability to distinguish category-specific resolution. A 2022 local signal may remain locally supportive only if it passes this new decomposition; no new HCC result is asserted.

Relative to `[prior hypothesis]`, this child does not alter the frozen scientific design. It converts the parent's descriptive ascertainment categories into a prespecified observation-robustness decomposition and adds a decision-resolution frontier that tells a next-study team whether additional timed Y adjudication could, in principle, resolve a sign-sensitive result. The repair is substantive because it prevents a pooled favorable bound from concealing ascertainment-regime reversal and links unresolved evidence to a concrete, computable data-collection decision. The remaining uncertainty is fundamental: endpoint ranges cannot recover unobserved HCC outcomes, validate assay units or specimen provenance, establish completed follow-up, or demonstrate that any statistically robust association would improve patient care.
