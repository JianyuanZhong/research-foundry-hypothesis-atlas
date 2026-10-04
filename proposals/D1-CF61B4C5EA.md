> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Pre-repeat assay state adds prediction beyond remote baseline after repeat TACE

## Target and advance

This two-parent child combines the clinically preferred estimand of `[prior hypothesis]` with the proven full-source reconstruction of `[prior hypothesis]`, while repairing its reversed nesting. The unresolved question is assay-specific and prognostic: among adults in the frozen HCC pathway cohort who have a first strict repeat-TACE event and a complete three-panel record, does the contemporaneous pre-repeat assay value `P` improve prediction of the next observed same-assay value `Y` beyond the remote pre-TACE2 value `B` and a compact decision-time core? This tests whether `P` adds information at the monitoring decision time; it does not test toxicity, recovery, treatment response, safety, benefit, or a causal TACE effect.

The strongest available evidence before this child was feasibility: a no-sampling audit established the frozen cohorts and triplet counts, but the execution parent estimated the opposite question (`B` beyond `P`). This child changes only the nesting direction, not the population, clocks, endpoints, or interpretation.

## Frozen population and exact data construction

Use HCC snapshot `[source checksum]`, scanning every source row without sampling. Reconstruct the inherited adult/HCC/2018–2024 cohort from:

- `encounters` in `[internal dataset path]`, columns `patient master index`, `visit number`, `age`, `sex`, `visit time`, `admission time`, `discharge time`, `visit department`;
- `diagnoses` in `[internal dataset path]`, columns `Patient Master Index`, `Encounter Number`, `Diagnosis Name`, `Diagnosis Type`, requiring literal `hepatocellular carcinoma` and inheriting linked encounter time;
- `procedures` in `[internal dataset path]`, columns `patient master index`, `encounter number`, `surgery`, `start time`, `end time`, `surgery source`, using case-insensitive `TACE` or literal `chemoembolization`, valid `start time`, calendar-day collapse, and earliest adjacent 14–180-day pair;
- `medications` in `[internal dataset path]`, columns `Patient Master Index`, `Encounter Number`, `Medication`, `Start Time` (plus medication fields if needed), applying only the inherited days 1–14 systemic-record ontology and ambiguity exclusions; records are not administration;
- `labs` in `[internal dataset path]`, columns `patient master index`, `visit number`, `test`, `qualitative result`, `quantitative result`, `specimen type`, `test time`, restricting to exact `albumin` and `total bilirubin`. Parse only signed decimal/scientific numeric strings with optional `<`, `>`, `≤`, `≥`; primary analysis uses uncensored numeric values, retaining specimen type and markers. There is no unit field.

All joins use composite (`patient master index`,`encounter number`) keys with duplicate-key audits and no many-to-many multiplication. Preserve the exact frozen pathway counts of 319 systemic-record and 1,491 comparator patients and the independently selected first repeat event on TACE2 calendar days 15–90, 159 and 526 respectively. Event time is the earliest valid procedure `start time` for that selected repeat event and event selection must not inspect laboratory values.

For each assay separately, select `B` as the latest valid value on TACE2 days −30 through −1; `P` as the latest valid value in the selected repeat encounter during `[event−72h,event)`; and `Y` as the value in that same encounter during `(event,event+72h]` nearest +24h, resolving exact distance ties by earlier timestamp. Require `B_time < P_time < event_time < Y_time` and positive P lead. Expected complete triplets are albumin 40 systemic / 118 comparator and bilirubin 41 / 119 comparator. Report source-row counts, invalid/missing clocks, parser attrition, duplicate groups and discordance, unmatched encounter keys, assay availability, and exact panel-to-event hours. Do not publish dates or patient identifiers.

## Primary estimand and executable analysis

For assay `a`, estimate paired pooled out-of-fold improvement in predicting `Y_a`:

```
M0: Y_a = α0 + αB B_a + αA A + θ'Z + ε
M1: Y_a = α0 + αB B_a + αP P_a + αA A + θ'Z + ε
```

Here `A` is systemic-record versus comparator, and the compact, temporally available core `Z` is age, sex, TACE2-to-repeat days, and P lead hours. The primary estimand is standardized paired OOF RMSE improvement `[RMSE(M0)−RMSE(M1)]/SD(Y)`, with standardized MAE improvement, R² increment, calibration and arm-specific metrics secondary. `P−B` and `Y−P` are descriptive only and never the primary predictor/outcome. Native assay scale is reported only with the explicit absent-unit caveat; no cross-assay pooling or clinical threshold is allowed.

Use deterministic outcome-blind SHA-256 five-fold partitions stratified by arm, with at least eight systemic observations per held-out fold under the audited counts. Every fold fits imputation, scaling, variance filtering, ridge fitting and penalty selection on training data only; use the proven runner's inner leave-one-patient-out choice from `{0.01, 0.1, 1, 10, 100}`. The same folds and preprocessing rules must be used for M0 and M1. The primary runner is `[internal dataset path]`.

## Bounded execution evidence and interpretation

A managed full-source reconstruction with this corrected nesting succeeded as `[research job]` (4 CPUs, 8,192 MiB; return code 0; 371.2 s; `N_BOOT=20`, `N_PART=2`, `N_PERM=10`). It scanned 105,044 encounter, 1,810,646 diagnosis, 338,040 procedure, 4,097,517 medication, and 28,159,928 lab rows; exact assay rows were 476,846, valid uncensored numeric timed rows 476,820; seven duplicate groups occurred and none was discordant. All frozen cohort/event/triplet assertions passed.

The bounded corrected results were:

- Albumin, n=158: M0 RMSE 3.9611 versus M1 3.1598; standardized RMSE improvement 0.1637 and MAE improvement 0.1227. Arm-specific RMSE improvements were 0.1111 (40 systemic) and 0.1865 (118 comparator). The 20-resample fixed-pipeline interval was [0.1252, 0.2258], but this is not adequate final uncertainty. Both alternate partitions were positive (0.1637, 0.1476). The 10 linkage permutations had q95 0.3665 and the observed gain did not exceed it; this diagnostic therefore does not support a claim that the observed increment is distinguishable from the implemented linkage-destruction null.
- Total bilirubin, n=160: M0 RMSE 12.7830 versus M1 9.9613; standardized RMSE improvement 0.2070 and MAE improvement 0.1228. Arm-specific RMSE improvements were 0.1642 (41 systemic) and 0.2327 (119 comparator). The 20-resample interval was [0.0918, 0.4109], again too small for final inference. Both alternate partitions were positive (0.2070, 0.2126), while the 10-permutation q95 was 0.2808 and the observed gain did not exceed it.

These results are evidence of computational feasibility and positive bounded point estimates, not definitive support. The linkage null is especially important: because `P` remains in M1 while `B` is permuted, the null can retain a large P-driven nested gain; the observed-not-above-q95 result prevents declaring robust incremental P evidence on this diagnostic. The final compilation must run the locked full uncertainty and diagnostics rather than promote the bounded interval or permutation result.

## Required final diagnostics and falsification

Run the prespecified larger fixed-pipeline and full-pipeline bootstrap, at least 20 outcome-blind partitions and 500 linkage permutations where resources permit; report fold support, calibration, HC3/paired bootstrap uncertainty, leave-one-out influence, leverage/Cook/DFBETA, and weight/selection sensitivity. Repeat the exact estimand under locked latest-pre 24/48/72/168-hour, first-pre 72-hour, post +24/+48/first-eligible, calendar-day +1–3, and common-timestamp selectors. Add a pre-event negative-control relation and a pseudo-post pre-event clock only when enough strictly pre-event panels exist; if not estimable, retain that as an inconclusive diagnostic rather than alter eligibility. Any later medication/procedure records are descriptive context and never adjustment variables.

Supportive results require positive, adequately precise M1−M0 performance for an assay, stable direction across locked partitions/timing and selection checks, non-dominant influence, adequate overlap/ESS, and no comparable pre-event gain. They support only reproducible short-horizon predictive information in selected, observed repeat-TACE episodes. Adverse results (no gain, worse M1, timing/partition dependence, pre-event placebo gain, or influence concentration) favor serial persistence, measurement process, regression to the mean, or selection explanations and block event-specific language. A precise null can rule out only a prespecified small standardized gain in this selected observed cohort, not equivalence or absence of hepatic change. Failed denominators, sparse folds, broad intervals, poor positivity, absent unit validation, or non-estimable falsification checks are inconclusive.

## Claim boundary and verification

The HCC data lack laboratory units, validated reference ranges, adjudicated acute illness, transfusion/fluid or albumin administration, imaging/tumor burden, technical TACE details/complications, reliable mortality, outside-care capture, verified medication administration, repeat-TACE rationale, and native diagnosis timestamps. Conditioning on repeat TACE and observed triplets is selected-observation conditioning and may induce collider bias; weighting cannot recover unobserved panels or establish a causal effect. No output may call the pattern toxicity, recovery, perturbation, response, safety, benefit, treatment effect, or clinical utility. Those claims require expert adjudication, laboratory metadata, verified exposure and another longitudinal/prospective study. The verifier can check exact files/hashes, row counts, filters, joins, clocks, nesting direction, folds, predictions, uncertainty and branch-consistent wording, but cannot establish clinical importance, causality or missing clinical events.

Bounded output: `[internal dataset path]` ([source checksum]); canonical row-level artifact remains local at `[internal dataset path]` ([source checksum]).
