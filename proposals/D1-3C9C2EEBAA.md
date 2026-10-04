# Outcome-blind overlap transport sensitivity for sparse-calendar HCC validation

## Targeted evolution and unresolved question

This is a substantive child of `[prior hypothesis]`. The parent established a valid frozen prognostic experiment, but its later calendar arms are sparse and its unweighted estimates cannot distinguish transport failure from a change in the decision-time covariate mix. The unresolved question is narrower than clinical benefit: **among the frozen adult HCC repeat-TACE complete-triplet events, does the incremental prognostic information in contemporaneous pre-repeat assay value `P` remain when the historical training distribution is transported toward the observed covariate distribution of each future calendar block, without extrapolating beyond common support?**

The available evidence already supports only that `P` improved held-out prediction at the adequately supported 2022 cutoff under the parent’s unweighted analysis. This child tests whether that conclusion is sensitive to outcome-blind calendar composition and whether later-era apparent gains are merely extrapolation. It does not test treatment efficacy, safety, clinical benefit, utility, actionability, or causality.

## Frozen population, clocks, estimand, and source bindings

All inherited rules remain immutable. Use HCC snapshot `[source checksum]`, with no sampling and all rows scanned in the inherited reconstruction. Preserve the complete-source repeat-TACE reconstruction, the systemic-record/comparator ontology, and the frozen denominators: 319 systemic and 1,491 comparator patients; 159 and 526 repeat events; albumin triplets 40/118 and bilirubin triplets 41/119 (systemic/comparator), total 318 patient-assay rows.

Required read-only source files and exact schema bindings are:

- `encounters`, `[internal dataset path]`, schema `[internal dataset path]`; keys `患者主索引`,`就诊号`; time fields `就诊时间`,`入院时间`,`出院时间`; covariates `年龄`,`性别`.
- `diagnoses`, `[internal dataset path]`, schema `...[internal dataset path]sets/hcc/table-12710723c3df0c99.json`; keys `患者主索引`,`就诊号`; require literal `肝细胞癌` in `诊断名称`, with timing inherited from the linked encounter because the table has no native time.
- `procedures`, `[internal dataset path]`, schema `...[internal dataset path]sets/hcc/table-d5eae16f8f8093d9.json`; keys `患者主索引`,`就诊号`; procedure `手术`, clocks `开始时间`,`结束时间`; identify TACE/化疗栓塞 and apply the inherited duplicate-day collapse and adjacent-pair/strict-repeat rules.
- `medications`, `[internal dataset path]`, schema `...[internal dataset path]sets/hcc/table-4f6ecaeb6e8f69c2.json`; keys `患者主索引`,`就诊号`; clocks `开始时间`,`结束时间`; apply the inherited days 1–14 systemic-record ontology and exclusions. Medication records are not verified administrations.
- `labs`, `[internal dataset path]`, schema `...[internal dataset path]sets/hcc/table-38aad8c54471332f.json`; keys `患者主索引`,`就诊号`; assay `检验`, numeric value `定量结果`, qualitative/censoring field `定性结果`, specimen `标本类型`, assay clock `检验时间`. Require exact `白蛋白` or `总胆红素`, valid uncensored numeric values, and retain the frozen assay selection.

Composite joins use (`患者主索引`,`就诊号`) and patient sequencing uses `患者主索引` only where inherited. Preserve the exact clocks: `B` is the latest valid assay in TACE2 day −30 through −1; `P` is the latest valid assay in the selected repeat encounter in `[event_time−72 hours,event_time)`; `Y` is the selected assay in `(event_time,event_time+72 hours]`, nearest +24 hours. Require `B_time < P_time < event_time < Y_time`, positive P lead, one patient-assay row, and no outcome-informed event selection.

The primary estimand remains the parent’s **unweighted, assay-specific held-out standardized RMSE gain**, `RMSE(M0)−RMSE(M1)` divided by test `SD(Y)`, with nested models:

- `M0`: `Y ~ B + systemic-record indicator + age + sex indicators + TACE2-to-repeat days + P-lead hours`
- `M1`: `M0 + P`

Assays are never numerically pooled. Calendar test blocks remain fixed and disjoint: origins 2021-01-01, 2022-01-01, 2023-01-01, 2024-01-01; training is all selected complete-triplet events strictly before an origin and testing is `[origin, origin+365 days)`. No test `Y` enters preprocessing, tuning, support estimation, or fitting.

## New support/transport strategy

The parent’s unweighted results remain primary. The new analysis is a prespecified sensitivity analysis for transport, not a replacement estimand and not a row-deletion procedure.

For each assay and origin, pool the pre-origin training rows and that origin’s future test rows and fit a regularized logistic calendar-membership model (train versus future test) using only decision-time, outcome-blind variables available in the canonical output: `B`, `P_lead_hours`, `days`, age (training median imputation), and sex indicators. Do not use `P`, `Y`, residuals, predictions, arm labels, or any post-event information in this membership model. Standardize using training moments. Estimate each training row’s odds of belonging to the future test distribution, stabilize to mean one, and cap weights at 4 before fitting weighted M0 and M1. The weighted result is reported alongside, never instead of, the parent’s unweighted result.

Apply a fixed support diagnostic before interpreting the sensitivity analysis:

1. calendar-membership AUC ≤ 0.75;
2. at least 80% of future test rows have estimated membership propensity in [0.10, 0.90];
3. transport-weight effective sample size (ESS) is at least 50% of the unweighted training n.

These are overlap diagnostics, not evidence that eras are exchangeable. A failed gate does not remove observations; it blocks any transport interpretation and leaves the unweighted block descriptive. Report arm counts unchanged and retain arm-specific results as descriptive, never as treatment effects.

Fit weighted nested ridge models using the same alpha grid `[0.01, 0.1, 1, 10, 100]`, training-only scaling/imputation, and inner leave-one-patient-out tuning. Evaluate the fixed future test rows with ordinary unweighted RMSE so the outcome metric remains interpretable for the observed future block; also report the sensitivity gain and M0/M1 RMSE. The sensitivity model changes how historical training is learned, not the target test population or the frozen `Y` clock.

As a falsification/stability diagnostic, refit the outcome-blind transport weights and weighted models after omitting each available historical calendar year in turn, where at least 20 training rows remain. Large sign reversals, failure of the overlap gate, or dependence on one historical year undermine transportability. This is not a claim of independent replication.

## Executed auditable repair

Runner: `[internal dataset path]` ([source checksum]).

Input canonical file: `[internal dataset path]` ([source checksum]).

Managed execution was job `[research job]`, return code 0, 31.64 seconds, 4 CPUs and 8,192 MiB. Output: `[internal dataset path]` ([source checksum]). The inherited canonical file contains all 318 reconstructed patient-assay rows; no additional sampling was performed.

The executed support diagnostics pass for both assays in 2021–2023. They also pass for albumin 2024 but fail for bilirubin 2024 because only 71.4% of test rows lie in the [0.10,0.90] propensity interval, despite low AUC; therefore bilirubin 2024 remains non-transportable. The weighted sensitivity gains are:

- Albumin: 2021 0.1363, 2022 0.1822, 2023 0.0956, 2024 0.2206 (2024 support gate false).
- Bilirubin: 2021 0.2593, 2022 0.2718, 2023 0.0558, 2024 0.2206 (2024 support gate false).

The 2022 supported parent estimates were albumin 0.1781 and bilirubin 0.3342; the transport-weighted sensitivities are directionally consistent (0.1822 and 0.2718). The 2023 weighted gains remain small (0.0956 and 0.0558), and the systemic arm has only five test observations, so no arm-specific transport conclusion is allowed. Leave-one-historical-year weighted gains remain positive in the executed diagnostics, but this does not create additional independent evidence. Complete values, propensity ranges, ESS, arm counts, and omitted-year results are in the output JSON.

## Falsification and interpretation branches

**Supportive for transport sensitivity, not clinical benefit:** a block passes the gate; weighted gain remains positive and close in direction to the unweighted gain; M1 improves over M0; and leave-one-historical-year analyses do not reverse sign or collapse ESS. This would strengthen the claim that the incremental prognostic signal is not an artifact of measured calendar composition, while still supporting only prognostic prediction in the frozen selected population.

**Adverse:** a gated block’s weighted gain is ≤0, M1 worsens RMSE, or omitting a historical year reverses the result; repeated adverse results would challenge stable incremental prediction across measured support. It would not prove B alone is sufficient, remove the possibility of measurement error, or establish treatment harm.

**Inconclusive/non-transportable:** support gate failure, very low ESS, extreme weights, sparse systemic arm, influential episodes, wide or sign-crossing uncertainty, clock/denominator mismatch, or missing laboratory units/reference ranges. This branch is mandatory for bilirubin 2024 and for every parent block that fails the parent arm-count gate; favorable point estimates must not be promoted to transport evidence.

The computation can verify exact source paths/hashes, complete reconstruction counts, clocks, disjoint calendar blocks, outcome-blind support construction, weights, ESS, model nesting, predictions, and sensitivity metrics. It cannot validate laboratory units/reference ranges, adjudicate disease severity or imaging response, verify medication administration, overcome selection/collider bias from repeat TACE and complete triplets, establish causality or clinical utility, or show benefit. Those claims require expert adjudication and independent temporal, external, or prospective data with validated assay metadata, imaging/tumor burden, reliable outcomes, and verified exposure.

## What changed and what remains uncertain

Changed substantively: the successor adds an outcome-blind, overlap-gated calendar transport sensitivity with capped stabilized odds weights, explicit ESS/propensity diagnostics, and historical-year leave-out falsification. It converts the vague warning “later eras are sparse” into a reproducible rule that can either support measured-composition robustness or formally block transport interpretation. It does not pool eras silently, delete sparse rows, alter clocks, or change the nested RMSE estimand.

Unchanged: population, source snapshot and bindings, reconstruction, B/P/event/Y clocks, non-overlapping forward validation, nested M0/M1 models, noncausal claim limits, and the requirement that only adequately supported results can be interpreted as evidence of incremental prognostic prediction. The remaining uncertainty is fundamental: sparse later systemic arms and unavailable clinical metadata still prevent a claim of multi-era clinical transport or patient benefit.
