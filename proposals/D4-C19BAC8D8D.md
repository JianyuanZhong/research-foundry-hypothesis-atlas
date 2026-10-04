# Baseline cystatin-C/creatinine discordance and repeat kidney status: certified, fail-closed UKB experiment

## Lineage and preserved question

This is a targeted repair of `[prior hypothesis]`. It preserves the parent’s baseline-only, schedule-marginal question:

> Among adults with baseline creatinine-equation eGFR at least 60 and a qualifying first available repeat observation, does baseline cystatin-C/creatinine discordance improve prioritization of the subsequent repeat biomarker-derived kidney-status state beyond age, sex, and baseline creatinine-equation eGFR?

The action represented is prioritizing a repeat kidney-function assessment. This experiment does not estimate whether ordering a test improves outcomes. It does not claim CKD, chronicity, measured GFR, kidney failure, causality, clinical utility, benefit, or transportability.

The strongest evidence available before this experiment is only that a baseline discordance score can be defined conditionally on certified field semantics and may be tested as an incremental predictor. The unresolved claim is the prespecified out-of-fold incremental prioritization contrast in the selected complete-repeat cohort. The experiment is not permitted to turn biomarker threshold status into a diagnosis or a fixed-horizon risk claim.

## Immutable current-workspace data binding

The UKB source is the rectangular export `ukb672073`, snapshot `[source checksum]`. All source files are read-only ordinary files; there are no archive members. The catalog is `[internal dataset path]`, [source checksum].

Use these exact source and schema paths in the current workspace, not paths from a prior attempt.

| table | source path | source SHA-256 | exact schema path | schema SHA-256 | required columns |
|---|---|---|---|---|---|
| `biological_samples` | `[internal dataset path]` | `[source checksum]` | `[internal dataset path]` | `[source checksum]` | `eid`, `30700-0.0`, `30700-1.0`, `30720-0.0`, `30720-1.0` |
| `assessment` | `[internal dataset path]` | `[source checksum]` | `[internal dataset path]` | `[source checksum]` | `eid`, `53-0.0`, `53-1.0`, `21003-0.0`, `21003-1.0` |
| `population` | `[internal dataset path]` | `[source checksum]` | `[internal dataset path]` | `[source checksum]` | `eid`, `31-0.0` |

Each source is an ordinary file. Join the three tables horizontally by `eid`, assert one row per `eid` in every input, assert no unexpected duplicate key, and assert agreement for overlapping columns. Do not use a vertical union, a participant-specific source lookup, or any source not listed above. Before reading values, verify the snapshot, source hashes, schema hashes, table IDs, and required-column sets against this binding.

## Executable certificate gate and neutral stop

The local UKB metadata explicitly says that field labels, units, field-specific missing-value meanings, assay/platform provenance, and exact date semantics are not supplied; instance index is not elapsed time. Therefore the analysis has an explicit pre-analysis certificate input rather than an assumption hidden in code.

The compiler must require a UTF-8 JSON certificate at the declared job input path `workspace/ukb_renal_field_equation_certificate.json`. The certificate is valid only if it contains all of the following, with no extra interpretation inferred from numeric ranges:

1. `dataset_snapshot` exactly `[source checksum]` and `export_id` exactly `ukb672073`.
2. For each field `30700-0.0`, `30700-1.0`, `30720-0.0`, and `30720-1.0`: authoritative field ID and label, analyte identity, specimen/matrix, unit, assay/platform or measurement method, instance semantics, permitted value/range information, every field-specific missing code and its meaning, and authoritative retrieval URL, retrieval timestamp, source version, and SHA-256 of the retrieved evidence. The certificate must establish whether baseline and instance 1 are comparable; a platform/unit change must include an explicit, versioned harmonization rule or cause a stop.
3. The certificate must state the meaning of `53-0.0` and `53-1.0` as assessment dates (or state that the meaning is unresolved), and the meaning/unit of `21003-0.0`, `21003-1.0`, and `31-0.0`. The locally approved evidence for age `21022` is not a substitute for certifying the requested repeat-age fields.
4. `field_missing_policy` must be a mapping by exact field name. No global negative-code recoding is allowed. Values not identified as field-specific missing codes remain values and must fail the positive-finite assay check if invalid.
5. `equation_certificate` must contain the exact equations in the next section, unit prerequisites, version identifier, source URL and SHA-256, and an implementation hash. The implementation must be independently rerunnable from the certificate and must not silently substitute another eGFR equation.
6. A canonical certificate digest is computed over canonical JSON with the `certificate_digest` member removed; the digest is SHA-256 of UTF-8 RFC-8785-style sorted, compact JSON. The supplied digest must match. This avoids an impossible self-referential hash.

No certificate is currently present in the local dataset catalog. This is deliberate and is not filled by a public web search, a column name, expected counts, or numerical plausibility. If the certificate is absent, has a mismatched snapshot/source, lacks any required field, has contradictory evidence, or has a digest/hash mismatch, the only permitted output is `STOP_FIELD_EQUATION_UNCERTIFIED`: a structural audit containing the failed gate, exact missing/contradictory certificate keys, and no biomarker-derived values, cohort counts, participant models, event counts, curves, p-values, bootstrap results, or biological conclusion. This neutral technical stop is distinct from an adverse or inconclusive predictive result. Compilation is still executable because the certificate check and terminal state are explicit; no unsupported certificate is invented.

## Exact 2021 CKD-EPI equations

After and only after the certificate passes, use certified creatinine in mg/dL, certified cystatin C in mg/L, age in years at the corresponding assessment, and baseline sex coding (`31-0.0`: 0 female, 1 male) held fixed at both assessments. These are race-free 2021 CKD-EPI equations; no race coefficient is permitted.

Let `Scr` be creatinine (mg/dL), `Scys` be cystatin C (mg/L), `A` be age (years), and `s=1` for female and `s=0` for male. Let `k=0.7` and `alpha=-0.241` for female; `k=0.9` and `alpha=-0.302` for male.

* Creatinine-only: `eGFRcr = 142 * min(Scr/k, 1)^alpha * max(Scr/k, 1)^(-1.200) * (0.9938^A) * (1.012^s)`.
* Cystatin-C-only: `eGFRcys = 133 * min(Scys/0.8, 1)^(-0.499) * max(Scys/0.8, 1)^(-1.328) * (0.996^A) * (0.932^s)`.
* Combined: `eGFRcr_cys = 135 * min(Scr/k, 1)^alpha * max(Scr/k, 1)^(-0.544) * min(Scys/0.8, 1)^(-0.323) * max(Scys/0.8, 1)^(-0.778) * (0.9961^A) * (1.012^s)`.

The certificate must bind these constants exactly, including decimal precision and sex-specific `k`/`alpha`. A unit conversion such as `Scr_mg_dL = Scr_umol_L / 88.4` is permitted only when the certificate proves the source unit is micromol/L; cystatin conversion is likewise allowed only when certified. Retain raw and converted aggregate audits. A second independent implementation must reproduce aggregate raw, certified-missing, nonpositive/nonfinite, and plausible counts by field and instance.

## Population, temporal boundary, and estimand

Construct nested populations in this order without using outcomes to define eligibility.

* `J`: one-to-one joined rows with required `eid` and required source columns.
* `B`: valid certified baseline sex, age, assessment date, creatinine, and cystatin C, with field-specific missing handling and positive finite assays. The inherited `J=502,370` and `B=468,887` are integrity anchors only. If certified rules produce a different count, report the discrepancy and stop for data-integrity review; never force the anchor.
* `R_date`: within `B`, require `53-1.0` and `53-1.0 > 53-0.0`, with `delta_years=(date1-date0)/365.25`. Retain inclusive `2 <= delta_years <= 8`. The inherited elapsed range `2.1081451061–6.1136208077` and repeat count are audit anchors, not forced outcomes.
* `R_complete`: within `R_date`, require positive finite certified repeat creatinine, cystatin C, and repeat age. Report every field-specific loss reason separately. Do not silently force the inherited `16,546` count if certified semantics alter it.
* `S_A`: within `R_complete`, require `eGFRcr_0 >= 60`. Report the inherited `16,372` and baseline strata `[60,75)` and `>=75` as comparison anchors only.

The primary estimand is conditional on `S_A` and observed complete first-available repeat attendance. It is schedule-marginal over the observed interval, not a fixed-horizon risk estimand. `53-1.0` is the date of the UKB field-instance-1 assessment, not necessarily the blood-draw date and not proof of the participant’s first clinical repeat. The interval is not a feature. Report `[2,3)`, `[3,5)`, and `[5,8]` interval bands as sensitivity descriptions; do not claim a four-year or other fixed-horizon risk.

Define baseline discordance only after certification as `Z=log(eGFRcys_0/eGFRcr_0)`. The primary repeat outcome is `Ycr=I(eGFRcr_1<60)`. Prespecified secondary outcomes are `Ycys=I(eGFRcys_1<60)`, `Ycomb=I(eGFRcr_cys_1<60)`, the four-level pair `(I(eGFRcr_1<60), I(eGFRcys_1<60))`, and aggregate continuous repeat summaries. These are biomarker-derived statuses, not CKD or chronicity. No persistent/chronic label is allowed.

As a descriptive missingness sensitivity, among `B` fit a predeclared baseline-only logistic model for observed `R_complete`, using sex, age, baseline eGFRcr, baseline cystatin C, and baseline missingness indicators available before repeat. Use stabilized inverse-probability weights truncated to `[0.10,10]`; compare weighted and unweighted descriptive risks among observed repeaters. This does not identify unobserved outcomes, nonparticipant outcomes, or transportability and cannot be interpreted causally. Primary analyses do not impute biomarkers or outcomes.

## Baseline-only model and outputs

No deployable feature may use repeat date, repeat age, repeat assays, interval, repeat completeness, attendance, or any other future variable. Use paired outcome-stratified round-robin five-fold cross-fitting over ten fixed repeats, with all preprocessing learned within training folds, fixed L2 logistic regression, no tuning, and no class weighting.

* `M0`: sex, baseline age, and `eGFRcr_0`, represented by the frozen natural-cubic-spline basis for age and eGFRcr plus sex.
* `M1`: `M0` plus one training-fold-standardized linear `Z` column.

Generate paired out-of-fold risks for `Ycr`, then repeat the frozen pipeline for `Ycys` and `Ycomb` as secondary outcomes. Do not use repeat cystatin C as a predictor.

For capacity `q=0.01,0.02,...,0.20`, with `q=0.10` highlighted for continuity, select `ceil(q*n)` by out-of-fold risk using a fixed participant-independent tie order. Report event capture, event fraction captured, PPV, and `DeltaC(q)=C_M1(q)-C_M0(q)` with paired simultaneous 98% max-|T| bands. The primary predictive gate requires a positive uncertainty-supported curve over the contiguous prespecified 5–15% region, repeat-stable and not driven by one baseline stratum. This is protocol-ranking information, not a threshold recommendation.

Also report the assumption-indexed threshold grid `p_t={0.001,0.0025,0.005,0.0075,0.010,0.015,0.020,0.030,0.040,0.050,0.075,0.100,0.150,0.200}` using `NB=TP/n - FP/n * p_t/(1-p_t)`, test-all, test-none, and `DeltaNB`. These curves do not identify clinical utility because relative harms, benefits, costs, preferences, and observed testing actions are unavailable.

Use 4,000 paired participant-bootstrap draws, seed `520241`, recomputing the complete capacity and threshold grids and calibration contrasts. Report between-repeat variation, calibration-in-the-large, calibration slope, Brier score, and risk-bin/stratum calibration. Do not make a directional subgroup statement with fewer than 1,000 participants and 20 events.

## Falsification, audit, and fail-closed rules

1. Verify all source/schema hashes, table IDs, required columns, one-to-one joins, and overlap agreement before values are used.
2. Verify the certificate and exact equation constants before any named biomarker value, eGFR, cohort, event, model, or bootstrap output. Failure is `STOP_FIELD_EQUATION_UNCERTIFIED`.
3. Independently reproduce conversion, missingness, positive-finite checks, equation outputs, and aggregate field-instance counts.
4. Audit code to prove M0/M1 excludes repeat date, repeat age, repeat assays, attendance, interval, and future-derived fields. A deliberately leaked model may be run only as a debugging sentinel and may not support a claim.
5. For 200 within-baseline-stratum outcome permutations (seed `520242`), reconstruct outcome-stratified folds under each label, refit both models, and recompute all capacity and threshold statistics. Compare the observed statistic to the statistic-specific empirical null with randomized-plus-one tails; do not compare only to zero. If the observed primary curve is not more favorable than the prespecified 98% favorable-tail null envelope, incremental evidence is uncertified.
6. Permute `Z` within baseline eGFRcr deciles and sex under identical folds and preprocessing. Persistent gains indicate leakage or implementation error.
7. Rerun the frozen pipeline for `1-Ycr`; a discordance conclusion cannot depend on an equally large artificial reversed-label gain.
8. Report interval-band, secondary-equation, selection-weight, and baseline-stratum sensitivities. A finding restricted to one interval or one unadjudicated equation is not a general kidney-status conclusion.

## Interpretation gates

**Supportive for conditional predictive prioritization only** requires a passed certificate and source audit, acceptable M1 calibration relative to M0, a simultaneous 98% lower band for `DeltaC(q)` positive across contiguous 5–15%, repeat stability, no material baseline-stratum contradiction, and successful empirical label-null and predictor-null checks. Concordance in a prespecified secondary status strengthens but is not required for the primary creatinine-status claim.

**Adverse** means reproducible worsening of calibration or capacity capture, or a gain that is null-compatible, leakage-related, assay-unresolved, or selection-fragile. It argues against incremental prioritization in this selected schedule-marginal evidence boundary, not against cystatin C in every clinical use.

**Inconclusive** means uncertainty bands cross zero across the capacity region, results vary materially by repeat or stratum, null refits do not complete, or only isolated capacity/threshold points improve. No threshold recommendation follows.

A certificate failure is a **neutral technical stop**, not adverse or inconclusive biological evidence. Even a supportive result cannot establish testing benefit, false-positive acceptability, cost-effectiveness, treatment benefit, causal utility, CKD, chronicity, measured GFR accuracy, assay interchangeability, or transportability. Those require authoritative expert assay adjudication, external utility/cost data, prospective testing-decision data, clinical records, and preferably measured GFR or repeated clinical measurements.

## Privacy and verification boundary

Keep participant-level projections, eids, folds, bootstrap/permutation arrays, weights, and audit extracts private in workspace/job artifacts. Publish only aggregate counts, curves, uncertainty bands, certificate provenance and hashes, source/schema hashes, and code/audit checks. No public search receives clinical records or private data.

A verifier can check exact source bindings, joins, certificate presence and digest logic, equation constants, baseline-only features, folds, grids, null completion, and conclusion-to-output consistency. It cannot establish the truth of assay identity beyond the supplied authoritative certificate, adjudicate CKD or measured GFR, establish causal utility or benefit, or establish transportability. The proposal makes no execution claim; with the currently absent certificate, the executable result is the declared neutral stop.
