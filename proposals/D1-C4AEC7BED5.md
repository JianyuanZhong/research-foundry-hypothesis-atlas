# Cumulative procedural perturbation at TACE2 and first strict repeat TACE

## Proposed child of

Parent: `[prior hypothesis]`

This proposal preserves the parent's frozen common-TACE2 cohort, medication ontology, pathway definitions, strict repeat-event definition, and temporal boundaries. It adds an empirical dual-event audit and a paired cumulative-perturbation analysis; it does not reinterpret the pathway as randomized treatment.

## Clinical question and falsifiable hypothesis

In adults with HCC who have a qualifying second TACE (TACE2) in 2018–2024 and then undergo their first strict repeat TACE on TACE2 calendar days 15–90, is the within-patient biochemical perturbation at the repeat procedure larger or smaller than that patient's perturbation at TACE2, and does the repeat-minus-TACE2 contrast differ between the frozen days-1–14 systemic-record pathway and the ambiguity-excluded TACE2-only comparator pathway?

The falsifiable hypothesis is that the pathway-stratified distribution of the paired cumulative contrast differs for at least one prespecified liver-related assay, after accounting for baseline and selection differences. The primary assays are exact labels `白蛋白` and `总胆红素`; `国际标准化比值` is confirmatory/supporting, and `丙氨酸氨基转移酶`, `γ-谷氨酰转移酶`, and `碱性磷酸酶` are contextual enzyme outcomes. The hypothesis is not that systemic medication causes injury or benefit, nor that repeat TACE causes the contrast: the available records do not identify dose, intent, tumor burden, laboratory units, or all clinical indications.

The strongest existing evidence in the parent supports feasibility of an acute exact-clock repeat-TACE comparison, not cumulative injury. The new audit tests the unresolved claim that the same patients have valid, temporally ordered, same-label laboratory pairs at both procedures in sufficient numbers to compare paired perturbations. Recovery is not an outcome: the parent found only 2 systemic and 5 comparator complete albumin/bilirubin recovery triplets.

## Frozen population and pathway

1. Read-only source files are the HCC snapshot documented in `datasets/hcc/README.md`.
2. Procedure source: `[internal dataset path]`, columns `患者主索引`, `就诊号`, `手术`, `开始时间`, `结束时间`, `手术来源`.
3. Encounter source: `[internal dataset path]`, columns `患者主索引`, `就诊号`, `年龄`, `性别`, `就诊时间`, `入院时间`, `出院时间`, `就诊科室`.
4. Diagnosis source: `[internal dataset path]`, columns `患者主索引`, `就诊号`, `诊断名称`, `诊断类型`.
5. Medication source: `[internal dataset path]`, columns `患者主索引`, `就诊号`, `用药`, `单次用药计量`, `单次用药计量单位`, `频次`, `开始时间`, `结束时间`, `用药方式`, `药品类型`.
6. Laboratory source: `[internal dataset path]`, columns `患者主索引`, `就诊号`, `检验`, `定性结果`, `定量结果`, `标本类型`, `检验时间`.
7. Join only on documented keys `患者主索引`, `就诊号`; procedure and laboratory clocks are their own timestamp fields. Diagnoses have no native timestamp, so HCC qualification uses the linked encounter time and requires an HCC diagnosis on an encounter at or before TACE2. Duplicate encounter keys are collapsed as in the parent implementation.
8. A strict procedure row is one whose `手术` contains literal case-insensitive `TACE` or literal `化疗栓塞`. Collapse qualifying rows to the earliest timestamp per patient/calendar day. Select each patient's earliest adjacent qualifying pair separated by 14–180 calendar days, with the second event TACE2. Retain adult HCC pairs with institutional observation through TACE2 day 14 and TACE2 calendar year 2018–2024.
9. Preserve the frozen medication ontology and placebo removal. Exclude prior ontology records through TACE2 day 0. Assign `systemic` when a non-bevacizumab ontology medication begins on days 1–14; assign `bev_only` when only bevacizumab occurs in that window; assign `generic` when an ambiguity-prone generic procedure occurs in days 1–14; retain only `systemic` and ambiguity-excluded `comparator` (TACE2-only) patients.
10. Select the first later strict patient-day TACE with calendar-day difference 15–90 inclusive. This event is the repeat anchor. The audit verified repeat day range 21–90 and `repeat_timestamp > TACE2_timestamp` for every selected repeat.

## Empirical feasibility audit

The complete-source managed job `[research job]` scanned all 28,159,928 laboratory rows and reproduced the parent's flow exactly:

- 78,067 strict textual procedure rows; 72,273 with valid timestamps; 38,742 patient-day episodes; 6,589 earliest adjacent pairs; 6,586 HCC/adult pairs.
- 2,992 era-and-observation-qualified patients; frozen arms 319 systemic and 1,491 comparator.
- First strict repeat TACE days 15–90: 159 systemic and 526 comparator.
- Laboratory labels were audited over the complete source. Exact source-wide labels include 238,293 `白蛋白`, 238,553 `总胆红素`, 297,735 `国际标准化比值`, 308,671 `丙氨酸氨基转移酶`, 308,440 `γ-谷氨酰转移酶`, and 238,372 `碱性磷酸酶`. No exact AST label was found under the complete searched label inventory; no `（急）` label is pooled with a frozen label.
- Exact-clock TACE2 pairs, systemic/comparator respectively, were albumin 125/588, bilirubin 126/591, INR 254/982, ALT 249/928, GGT 250/931, and ALP 125/589.
- Exact-clock repeat pairs were albumin 57/204, bilirubin 58/205, INR 116/331, ALT 109/309, GGT 110/309, and ALP 57/204.
- Dual-event same-assay pairs were albumin 36/109, bilirubin 37/109, INR 30/92, ALT 96/237, GGT 97/237, and ALP 36/109, systemic/comparator respectively. Strict same-specimen and four-value uncensored counts were albumin 35/109, bilirubin 36/109, INR 29/92, ALT 95/237, GGT 96/237, and ALP 35/109.
- Joint dual-event albumin-plus-bilirubin support was 35 strict systemic and 109 strict comparator patients. Adding INR yielded 29 strict systemic and 92 strict comparator patients.
- Exact-clock timing was ordered as designed. Across assays, pre values were selected before the procedure (typical medians approximately -7 to -14 hours) and post values near approximately +32.5 hours. Same-event encounter matching was nearly complete. The one recurring systemic specimen mismatch was `血 -> 血清`; it is excluded by the strict-context analysis.
- Later non-placebo ontology records after day 14 and on/before repeat occurred in 14/159 systemic and 4/526 comparator repeaters. This is retained as a context flag and a prespecified sensitivity restriction; it is not silently treated as absent exposure.

These counts support a repairable, feasibility-limited paired experiment. The primary albumin/bilirubin pathway contrast is estimable descriptively but is too small in the systemic arm for broad claims or unconstrained high-dimensional adjustment. INR is confirmatory only; enzyme results are supporting and may provide more stable context. Any model failing overlap or effective-sample-size gates must report descriptive paired results only or be declared inconclusive.

## Laboratory construction and estimands

For each patient `i`, exact assay label `a`, and anchor `k` in `{TACE2, repeat}`:

- `pre(i,a,k)` is the latest valid numeric result with the identical exact label in `[anchor_timestamp - 7 days, anchor_timestamp)`.
- `post(i,a,k)` is the valid numeric result with the identical exact label in `(anchor_timestamp, anchor_timestamp + 72 hours]` whose timestamp is closest to anchor plus 24 hours; earlier timestamp and encounter string are deterministic tie-breakers.
- Parse numeric values only from optional inequality marker `<`, `>`, `≤`, or `≥` followed by a numeric token. Retain marker metadata; raw-change analyses use only values without inequality markers.
- `Delta(i,a,k) = post - pre`.
- The patient-level cumulative perturbation is `C(i,a) = Delta(i,a,repeat) - Delta(i,a,TACE2)`.

The primary descriptive estimand is the difference in mean (with robust and bootstrap uncertainty) of `C(i,a)` between the systemic and comparator pathways among repeat-event patients with an exact same-label pair at both events. The primary analysis is restricted further to strict context: same specimen at pre/post within each procedure and no inequality markers among all four values. Albumin and bilirubin are reported separately as co-primary outcomes; there is no cross-assay composite and no ALBI score because the laboratory file has no unit column and `标本类型` is a specimen field, not a unit.

A secondary estimand targets the repeat-event population using measured-selection standardization. Fit an event-selection model over all frozen systemic/comparator patients for the indicator of first strict repeat on days 15–90, and assay-specific observation models among repeaters for having both event-level pairs. Use only covariates known before the relevant selection decision, including pathway, TACE2 calendar year, age, sex, department/encounter context, TACE1-to-TACE2 interval, institutional observation indicators, and availability of pre-TACE2 exact-label results where defined. Fit nested cross-fitted models within training folds; do not use post-repeat laboratory values or later medication records as predictors. Combine stabilized inverse event-selection and assay-observation weights only as a sensitivity analysis, not as an automatic correction for unmeasured selection.

For each assay and pathway, report unweighted complete-pair estimates first, then weighted estimates if positivity, calibration, weight truncation stability, and effective sample size pass. Estimate uncertainty with patient-level bootstrap or influence-function methods that resample patients, not individual laboratory rows. Because the systemic strict sample is approximately 35 for albumin/bilirubin, limit adjustment to prespecified low-dimensional terms and do not fit a flexible outcome model that can overfit. Ratio and log-ratio measures are secondary only for positive values, stable specimen context, exact labels, and clinically defensible within-assay scale; raw differences remain primary because laboratory units are unavailable.

## Baselines, controls, and diagnostics

- Baseline perturbation at TACE2 is the within-patient comparator for the repeat perturbation; this controls each patient's measured acute laboratory level and partially separates pre-existing susceptibility from recurrence-specific change.
- Report TACE2 pre values, TACE2 changes, repeat pre values, repeat changes, and the paired difference rather than only the final contrast.
- Compare event-day distributions, TACE2-to-repeat interval, calendar-year composition, age/sex/department, and pre-event observation patterns between pathways. Display standardized differences and overlap before adjustment.
- Fit repeat-event selection separately from laboratory-pair observation. Report complete-case fractions and selection fractions: repeat selection was 159/319 versus 526/1,491.
- Use pre-event same-assay negative controls: apply the same exact-label selector to two non-overlapping pre-anchor windows where available, with no procedure between the windows. A large pathway contrast in a nominally non-procedural pre-period, or a contrast that reverses under modest timing perturbations, argues for differential surveillance or baseline trend rather than cumulative procedural perturbation.
- Timing falsification: shift the post window to a prespecified placebo anchor before the procedure, and perturb the post target within the allowed 0–72-hour window. A purported acute signal that is equally present before the anchor or highly unstable under deterministic tie-preserving timing perturbation fails the temporal test.
- Context sensitivity: repeat analyses excluding the 14 systemic and 4 comparator repeaters with later ontology records before the repeat; separately report them rather than redefining the frozen pathway.
- Specimen sensitivity: compare all pairs with strict same-specimen pairs. The latter is primary for cumulative interpretation. Do not normalize across assays or import external thresholds.
- Selection diagnostics: report propensity overlap, calibration, maximum and percentile weights, truncation thresholds, effective sample size, and the change from unweighted to weighted estimates. If either pathway has inadequate overlap or effective sample size, do not publish a weighted contrast.
- Multiplicity: treat albumin and bilirubin as co-primary descriptive outcomes with joint interpretation; INR and enzymes are supporting, not independent confirmatory claims. Avoid claiming a global liver-injury effect from discordant assays.

## Falsification and interpretation gates

The cumulative-stress proposal is methodologically falsified if the reconstruction no longer reproduces the frozen arms or repeat counts; if any repeat precedes TACE2; if exact-label selectors admit same-timestamp post values; if pair counts change when raw source rows are re-read; if labels are silently pooled; or if assay pairs cannot be linked to the same patient and exact assay at both events.

It is downgraded to descriptive feasibility if strict systemic albumin/bilirubin support remains around 35 patients, overlap or effective sample size fails, or observation models are unstable. In that branch, report paired distributions and uncertainty without pathway-adjusted causal language; retain INR/enzyme results as context only.

- Supportive result: both albumin and bilirubin show a consistent, precisely estimated pathway difference in `C`, timing and negative controls are clean, strict-context and sensitivity estimates agree, and selection diagnostics are acceptable. This supports an association between the frozen pathway/clinical trajectory and differential repeat-versus-TACE2 perturbation among observed repeaters, not medication toxicity, TACE harm, or benefit.
- Adverse result: the repeat-minus-TACE2 contrast is larger in the systemic pathway, particularly consistently across albumin/bilirubin and not explained by later systemic records or selection. This supports a clinically important signal for risk stratification and prospective monitoring, but requires dose, indication, tumor burden, severity, and treatment-timing data before attributing it to systemic therapy or cumulative TACE injury.
- Null result: a precise near-zero contrast with clean controls would weaken the claim of a detectable pathway-stratified cumulative perturbation in this observed population; it would not prove biochemical equivalence or safety because missingness and selection remain.
- Selection-sensitive result: materially different weighted, unweighted, strict-specimen, or later-record-restricted estimates indicate that differential repeat selection or laboratory observation dominates; conclusions should be limited to data-generating-process sensitivity.
- Inconclusive result: wide uncertainty, failed positivity, low effective sample size, or insufficient dual-event completeness means the clinical question remains unresolved and needs a larger or prospectively standardized study.

## Evidence limits requiring another study or adjudication

The available files do not contain reliable laboratory units, TACE dose/territory/technical details, tumor burden or stage, treatment indication, outpatient adherence, transfusion/albumin replacement, intercurrent infection or bleeding, imaging response, or adjudicated hepatic decompensation. Diagnoses lack a native timestamp. A clinical expert must adjudicate whether assay changes represent hepatic injury, synthetic dysfunction, cholestasis, nutrition/inflammation, dilution, or unrelated illness. A prospective study with synchronized specimen collection, units, procedure details, medication exposure and indication, serial labs, and blinded clinical outcome adjudication is required for causal toxicity, safety, benefit, or treatment-strategy claims.

## Provenance and outputs

The complete-source audit was executed with managed resources and declared inputs through `job_submit`. Aggregate output is at:

`[internal dataset path]`

The inspected reconstruction is at:

`[internal dataset path]`

The executable audit is at:

`[internal dataset path]`

No patient identifiers, exact dates, raw laboratory values, or clinical notes are published in this proposal.
