> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Baseline cystatin-C/creatinine discordance and repeat kidney-function status

## Successor scope and unchanged question

This is a substantive successor to `[prior hypothesis]`. It does not change the estimand, target population, time window, biomarker fields, equations, or claim boundaries. The question remains:

> Among adults with baseline creatinine-equation eGFR at least 60 who have a qualifying first available UK Biobank field-instance-1 repeat observation, does baseline cystatin-C/creatinine discordance improve baseline-only prioritization of the repeat creatinine-equation kidney-function status beyond sex, age, and baseline creatinine-equation eGFR?

The represented action is prioritizing a repeat kidney-function assessment. The outcome is an equation-defined biomarker status observed at the repeat assessment. This is not a study of whether ordering a test improves outcomes, and it does not estimate a treatment, testing, or referral threshold.

The strongest claim supported before this experiment is only that clinical practice and prior evidence motivate confirming abnormal kidney markers and considering creatinine/cystatin-C information when creatinine may be inaccurate and GFR affects a decision. The supplied local package does not certify that fields 30700 and 30720 are the intended analytes, their units, specimen matrices, assay platforms, missing-value codes, or comparable measurements across instances. Thus the current snapshot cannot support a biological discordance result. The unresolved, conditional claim is incremental baseline ranking information for an observed repeat biomarker-derived status in the selected complete-repeat cohort.

A supportive result would support only conditional ranking in that selected cohort. It would not establish CKD, chronicity, measured GFR, kidney failure, assay interchangeability, causal utility, benefit from testing, cost-effectiveness, an actionable threshold, or transportability.

## Immutable data binding and provenance

Use only the frozen UK Biobank rectangular export `ukb672073`, snapshot `[source checksum]`. All source files are read-only and ordinary files, with no archive members. The exact source files required for the scientific branch are:

- `[internal dataset path]`, [source checksum].
- `[internal dataset path]`, [source checksum].
- `[internal dataset path]`, [source checksum].

The exact current schema files, as inspected in this workspace, are:

- `[internal dataset path]`, table `biological_samples`, [source checksum].
- `[internal dataset path]`, table `assessment`, [source checksum].
- `[internal dataset path]`, table `population`, [source checksum].
- `[internal dataset path]`.

The workspace guide is `[internal dataset path]`. Record catalog `[internal dataset path]`, [source checksum], and all source/schema hashes before reading participant rows. The table schemas explicitly bind the required fields as follows:

| Table | Required columns | Use |
|---|---|---|
| `population` (`table-38565c9e35e7cb6c`) | `eid`, `31-0.0` | baseline sex |
| `assessment` (`table-901ef6c7ddce2d51`) | `eid`, `53-0.0`, `53-1.0`, `21003-0.0`, `21003-1.0` | baseline/repeat assessment dates and ages |
| `biological_samples` (`table-c6b666d905f3b02f`) | `eid`, `30700-0.0`, `30700-1.0`, `30720-0.0`, `30720-1.0` | certified baseline/repeat laboratory values |

The only join key is `eid`. Join horizontally, one-to-one, and assert unique non-null `eid` in each required table, declared cardinalities, equal row identity after joining, and agreement for overlapping columns. No vertical union, duplicate resolution, inferred table relationship, or participant-level export is permitted.

## Explicit execution states: metadata-only stop is not scientific output

The implementation must use a state machine and write a machine-readable `run_manifest.json` before any result file. Scientific claims are permitted only in state `CERTIFIED_SCIENTIFIC_OUTPUT`.

### State `METADATA_ONLY_STOP`

This is the mandatory result for the current frozen package. Before any row-level biological processing, read only the catalog, exact schema JSON files, and frozen `metadata.json`; verify their hashes, required column presence, table IDs, source paths, snapshot ID, and ordinary-file/no-archive declarations. Write:

- `provenance_manifest.json`: catalog, source, schema and metadata paths, hashes, snapshot, and code hash;
- `field_certificate.json`: one record for each requested field-instance pair;
- `run_manifest.json`: `state=METADATA_ONLY_STOP`, `SCIENTIFIC_EXECUTION=STOP_ASSAY_METADATA_UNRESOLVED`;
- `gate_status.json`: gate outcomes and blocked descendants;
- `technical_qa.json`: only schema/path/hash/field-presence checks.

In this state, the program must not read participant values, calculate row-level join counts, call anything a biological cohort, recode missing values, convert units, compute eGFR, construct discordance, fit models, report outcome rates, report a baseline anchor, or emit a supportive/adverse/inconclusive biological conclusion. A zero-row technical stop is deliberately different from a failed or negative scientific analysis. The stop is neutral evidence about package certification, not evidence for or against the hypothesis.

### State `TECHNICAL_INTEGRITY_QA` (optional, non-scientific)

A separately invoked integrity job may read the three exact source files to check file readability, header/schema correspondence, unique `eid`, one-to-one join behavior, and overlapping-field agreement. Its output must be labeled `TECHNICAL_INTEGRITY_QA_ONLY`, must not contain participant-level data, and must not compute or publish biological counts, assay distributions, eGFR, discordance, model metrics, or conclusions. If integrity fails, the state is `STOP_SOURCE_OR_JOIN_INTEGRITY`, and no scientific branch can run. Technical integrity passing does not upgrade an assay-unresolved run.

### State `CERTIFIED_SCIENTIFIC_OUTPUT`

This state is reachable only when a versioned, hashed, per-field certificate is supplied as an explicit frozen input and passes every certificate requirement below, and when source/schema/integrity checks pass. The certificate must be an input, not fetched or inferred during execution. Every scientific output file must carry the same `run_id`, certificate hash, source/schema hashes, code hash, and `state=CERTIFIED_SCIENTIFIC_OUTPUT`. A verifier must reject any output claiming scientific results when the run manifest says either stop state.

## Neutral fail-closed assay certificate

The frozen `metadata.json` states that per-field labels, units, and missing-value meanings are absent; supplied field-ID files are not coding dictionaries; negative numeric codes must not be globally interpreted; and the only locally approved examples are field 21022 and field 31/coding 9. It supplies no approved record for 30700 or 30720 and no assay/platform provenance. Schema presence is not semantic certification.

Write exactly one certificate row for each of `30700-0.0`, `30700-1.0`, `30720-0.0`, and `30720-1.0` with these columns:

`field_id`, `column_name`, `table_id`, `source_path`, `schema_path`, `field_label`, `analyte`, `specimen_matrix`, `unit`, `assay_platform`, `measurement_method`, `instance_semantics`, `permitted_range`, `missing_codes`, `metadata_source`, `metadata_source_sha256`, `retrieved_or_frozen_version`, `certification_status`, `reason`.

For this snapshot, all four rows must have `certification_status=UNAVAILABLE_FROZEN_EVIDENCE` and reason exactly equivalent to: `metadata.json explicitly reports that per-field labels, units, and missing-value meanings are absent and supplies no approved metadata record for field 30700 or field 30720`. The artifact may record that field 31 and 21022 are approved local examples, but must not use them to certify laboratory fields. The negative certification source is the exact local metadata file and its hash, not an unverified internet assertion.

No external Showcase/dictionary metadata, URL, paper, or assumed conventional UKB meaning may be fetched, merged, or substituted. A future certificate can unblock the scientific branch only if, for every field-instance pair, it supplies field identity/label, analyte, specimen matrix, unit, assay/platform or measurement method, instance semantics, permitted/range information, field-specific missing codes, and provenance/version/hash; it must establish baseline/instance-1 comparability or give a documented change and predeclared harmonization/stratification. A URL alone fails closed. Missing or contradictory certificate fields produce `STOP_ASSAY_METADATA_UNRESOLVED`.

Even with a valid certificate, do not globally recode negative values. Use only its field-specific missing codes; preserve raw values privately; require finite positive values and certificate-approved plausibility checks; classify other failures as predeclared assay/value QA exclusions.

## Population, repeat timing, and observed-schedule selection

After certification only, construct nested sets in this fixed order and save a private selection-flow table with counts and loss reasons. The order prevents repeat laboratory availability or outcome status from selecting the repeat date.

1. `J`: one-to-one joined rows with `eid` and all required columns in their declared tables. This is a technical joined population, not yet a biological cohort.
2. `B`: require valid baseline `31-0.0`, `21003-0.0`, `53-0.0`, certified positive-finite `30700-0.0`, and certified positive-finite `30720-0.0`, using only certificate missing codes. Define baseline variables before inspecting any repeat value. The inherited integrity anchors `J=502,370` and `B=468,887` are audit expectations only, never forced values; any discrepancy is reported and blocks interpretation pending review.
3. `R_date`: within `B`, inspect only `53-1.0` to select the repeat schedule. Require a valid parseable date, strictly greater than `53-0.0`, and define `delta_years=(date(53-1.0)-date(53-0.0)) / 365.25 days`. Retain `2 <= delta_years <= 8`, inclusively. This is the first available UKB field-instance-1 assessment date represented by the fixed column; it is not an exact blood-draw date, not evidence of clinical attendance outside UKB, and not proof of a participant's first real-world repeat.
4. `R_complete`: within `R_date`, require certified positive-finite `30700-1.0`, certified positive-finite `30720-1.0`, and valid `21003-1.0`. Do not replace a missing instance-1 date or assay with instance 2 or any other field. Record each failure separately: invalid/missing repeat date, date ordering, outside interval, repeat creatinine missing-code/value failure, repeat cystatin-C missing-code/value failure, repeat age failure, and any certificate comparability failure. No repeat laboratory field is allowed to influence `R_date` selection.
5. `S_A`: within `R_complete`, retain `eGFRcr_0 >= 60`, with the eGFR calculated only after certificate validation. Report baseline strata `[60,75)` and `>=75`; the inherited audit anchor is `16,372`, never a forced result.

If multiple representations of a date occur in a cell, reject the row unless the frozen schema/certificate explicitly defines a deterministic representation; do not choose the earliest valid date after inspecting alternatives. If a date parses but has an impossible calendar value, classify it as invalid. The schedule band is assigned once from the unrounded `delta_years`: `[2,3)`, `[3,5)`, or `[5,8]`. It is an observed-schedule descriptor, not a baseline predictor, and must never be pooled into a fixed-horizon claim.

The primary estimand is conditional on `S_A` and the observed complete first available field-instance-1 repeat cohort. It is not a population-screening, all-enrolled, or fixed-time survival estimand. Participation, baseline completeness, repeat attendance, and repeat assay completeness are selection mechanisms. Among `B`, an observation model for `I(R_complete=1)` may be fit using only sex, age, baseline eGFRcr, baseline cystatin C, and baseline missingness indicators defined before the repeat date. Use stabilized inverse-probability weights truncated to `[0.10,10]` only for a missingness-sensitivity descriptive analysis. Weighted and unweighted results must be labeled assumption-indexed and cannot recover unobserved outcomes, nonparticipants, or transportability.

## Exact biomarker calculations

The mandated race-free 2021 CKD-EPI equations use floating-point exponentiation, no race coefficient, no rounding before thresholding, and baseline sex held fixed at repeat. `female=1` means the certified field-31 coding is Female and `female=0` means Male, using only the locally approved field-31/coding-9 record. Let `Scr` be certified serum creatinine in mg/dL and `Scys` certified cystatin C in mg/L.

For sex-specific `k` and `alpha`, use `k=0.7, alpha=-0.302` for female and `k=0.9, alpha=-0.241` for male.

```
eGFRcr = 142 * min(Scr/k, 1)^alpha
             * max(Scr/k, 1)^(-1.200) * (0.9938^A)
             * (1.012 if female else 1.000)

eGFRcys = 133 * min(Scys/0.8, 1)^(-0.499)
              * max(Scys/0.8, 1)^(-1.328) * (0.996^A)
              * (0.932 if female else 1.000)

eGFRcr_cys = 135 * min(Scr/k, 1)^alpha
                 * max(Scr/k, 1)^(-0.544)
                 * min(Scys/0.8, 1)^(-0.323)
                 * max(Scys/0.8, 1)^(-0.778)
                 * (0.9961^A) * (1.012 if female else 1.000)
```

`eGFRcr_0`, `eGFRcys_0`, and `eGFRcr_cys_0` use baseline fields and `21003-0.0`; corresponding `_1` values use instance-1 fields and `21003-1.0`, with baseline sex held fixed. A numerical unit test must run before participant rows in the certified branch. For `female=0`, `A=50`, `Scr=1.0`, `Scys=0.8`, the implementation must reproduce, to `1e-6` when recomputed from the displayed equations, approximately `89.419`, `91.231`, and `91.191` for the three equations. It must also test female `k=0.7`, alpha `-0.302`, and female multipliers, recording exact computed values rather than relying on rounded prose.

Define primary baseline discordance only after certification and valid values: `Z=log(eGFRcys_0/eGFRcr_0)`. The primary outcome is `Ycr=I(eGFRcr_1 < 60)`. Secondary outcomes are `Ycys=I(eGFRcys_1 < 60)`, `Ycomb=I(eGFRcr_cys_1 < 60)`, the four-level pair `(I(eGFRcr_1<60), I(eGFRcys_1<60))`, and continuous repeat eGFR summaries. These are biomarker-derived equation statuses only, not CKD, persistent CKD, chronicity, measured GFR, kidney failure, or adjudicated disease. No albuminuria, clinical adjudication, observed testing action, or measured GFR is available.

## Baseline-only predictive comparison

Freeze the deployment feature manifest before reading any repeat outcome. `M0` contains sex, baseline age, and `eGFRcr_0`, with the inherited fixed natural-cubic-spline basis for age and eGFRcr plus sex. `M1` adds exactly one training-fold-standardized linear `Z` column. Neither model may use repeat date, repeat age, repeat biomarkers, repeat completeness, attendance, interval, or any future-derived quantity. The manifest must be machine-checked against the source column names and derived-variable dependency graph; any forbidden dependency blocks scientific output.

For each primary and secondary outcome, use outcome-stratified-round-robin five-fold cross-fitting over ten fixed repeats, with all preprocessing learned within training folds. Fit fixed L2 logistic regression, no tuning and no class weighting. Produce paired out-of-fold risks for M0 and M1, preserving identical folds and preprocessing within each pair.

The primary fixed-capacity grid is `q=0.01,0.02,...,0.20`; report `q=0.10` for continuity. At each q, select `ceil(q*n)` by out-of-fold risk with a fixed participant-independent tie order. Report event capture, fraction of all events captured, PPV, and `DeltaC(q)=C_M1(q)-C_M0(q)`, with paired simultaneous 98% max-|T| bands. The evidence gate requires a positive uncertainty-supported curve over the contiguous prespecified 5–15% capacity region, stable across ten repeats and prespecified baseline strata. An isolated q, arbitrary event increment, or post hoc capacity is insufficient. This remains a ranking estimand, not a threshold recommendation.

For transparency, report the assumption-indexed threshold grid `p_t={0.001,0.0025,0.005,0.0075,0.010,0.015,0.020,0.030,0.040,0.050,0.075,0.100,0.150,0.200}` using `NB=TP/n - FP/n*p_t/(1-p_t)` and `DeltaNB=NB_M1-NB_M0`, with test-all and test-none. These values index an externally assumed harm-to-benefit exchange rate. The data do not estimate that exchange rate, observe testing actions, or justify a clinically selected net-benefit threshold.

Use 4,000 paired participant-bootstrap draws with seed `520241`, recomputing complete capacity grids and calibration contrasts. Label intervals conditional on cross-fitted predictions. Report between-repeat variation, calibration-in-the-large, calibration slope, Brier score, and stratum/risk-bin calibration. A directional subgroup statement requires at least 1,000 participants and 20 events; otherwise it is unsupported.

## Falsification and executable audit gates

Every gate writes `gate_id`, `status`, `required_for`, `input_hashes`, `output_paths`, `failure_action`, and `claim_ids_unlocked`. No claim may be emitted unless all gates listed for it have status `PASS`.

- **G0 provenance:** exact source, schema, catalog, metadata, snapshot, archive-member and code hashes match the frozen manifest. Failure yields `STOP_PROVENANCE`.
- **G1 schema:** the three exact table IDs and all required columns are present in the exact schemas; only `eid` is used as join key. Failure yields `STOP_SCHEMA`.
- **G2 assay certificate:** all four field-instance certificate rows meet every requirement. Current result is `FAIL_UNAVAILABLE_FROZEN_EVIDENCE`; it unlocks no biological claim and forces `METADATA_ONLY_STOP`. A missing or contradictory future certificate has the same effect.
- **G3 integrity:** source readability, unique `eid`, one-to-one horizontal join, and overlapping-field agreement pass. Failure yields `STOP_SOURCE_OR_JOIN_INTEGRITY`, never an adverse hypothesis result.
- **G4 repeat schedule:** the date is selected from `53-1.0` independently of repeat assay completeness; parsing, strict ordering, `2 <= delta_years <= 8`, and fixed schedule-band assignment pass. Failure blocks all outcome claims.
- **G5 values and formulas:** certificate-specific missing handling, positive-finite checks, unit conversion if and only if certificate specifies it, equations, sex coding, numerical tests, and no-rounding threshold behavior pass. Failure blocks all biomarker-derived claims.
- **G6 population:** the ordered `J -> B -> R_date -> R_complete -> S_A` flow and every loss reason are reproducible; no outcome or repeat value selects eligibility except the predeclared completeness step. Failure blocks interpretation.
- **G7 leakage:** feature dependency manifest, fold-local preprocessing, fixed folds, and private leaked-model sentinel show no repeat/future variables in M0/M1. Failure invalidates predictive outputs.
- **G8 uncertainty/falsification:** bootstrap completion, simultaneous bands, 200 within-baseline-stratum outcome permutations with seed `520242`, predictor permutations within baseline eGFRcr deciles and sex, and reversed-label control complete. The label null reconstructs outcome-stratified folds and both fits for each permutation; randomized-plus-one, statistic-specific tail fractions are reported. Persistent predictor-null gains indicate leakage or implementation error. A discordance-specific conclusion cannot rely on an equally large gain for `1-Ycr`.
- **G9 interpretation:** the conclusion file contains only claim IDs unlocked by passed gates and explicitly carries the observed-repeat selection, schedule, biomarker-status, and noncausal limitations. Any unsupported wording such as CKD, chronicity, measured GFR, benefit, utility, threshold recommendation, or transportability is a verifier failure.

The `[2,3)`, `[3,5)`, and `[5,8]` schedule-band results are timing sensitivity analyses, not alternative primary estimands. A direction confined to one band, one repeat, one stratum, or one unadjudicated equation is not a general kidney-status finding. Complete-case versus observation-weighted descriptive divergence is selection uncertainty, not causal evidence.

## Claim-to-gate linkage and interpretation

Use stable claims in `claims.json`:

- `C0`: the current package has a neutral assay-certification stop. Required gates: G0, G1, and the G2 negative certificate. This is technical package evidence only.
- `C1`: the conditional primary ranking result for repeat creatinine-equation status. Required G0-G9, with G2 PASS and G4-G8 complete.
- `C2`: secondary equation-defined consistency. Required C1 plus prespecified secondary results; it still cannot be called clinical kidney disease.
- `C3`: observed-repeat selection and schedule description. Required G0-G6; it is descriptive and conditional, never population-screening evidence.
- `C4`: any missingness sensitivity. Required G0-G6 plus explicit observation-model diagnostics and assumptions; it cannot be interpreted causally.

Current frozen execution must produce `C0` only and must explicitly mark `C1`-`C4` as `BLOCKED_BY_G2` (C3/C4 are also not to be emitted as biological counts in metadata-only mode). A future certified run may emit C1 only if its evidence gate passes: valid certificate, all integrity/timing/formula/leakage/uncertainty gates, M1 calibration acceptable relative to M0, simultaneous 98% lower band for `DeltaC(q)` positive throughout 5–15%, stability across ten repeats and supported strata, and observed primary curve more favorable than its prespecified 98% label-null envelope. Predictor-null gains must collapse. Concordance in at least one prespecified secondary equation strengthens but is not required for C1.

- **Supportive:** C1 is unlocked under all stated gates. Interpret only as baseline conditional ranking in the selected observed complete-repeat cohort.
- **Adverse:** with certification passed, M1 reproducibly worsens calibration or capacity capture, or its gain is null-compatible, leakage-related, or selection-fragile. This argues against incremental prioritization value within this evidence boundary, not against cystatin C in all clinical uses.
- **Inconclusive:** bands cross zero over 5–15%, results vary materially by repeat or stratum, null refits do not complete, or only isolated threshold points improve. Under the current package this is superseded by the more specific neutral `STOP_ASSAY_METADATA_UNRESOLVED`; it is not a biological inconclusive result.

## Privacy, unavailable evidence, and verification limits

Keep eids, rows, raw values, folds, bootstrap/permutation arrays, weights, and intermediate tables private. Publish no participant-level projection and no aggregate biological count from a metadata-only stop. Technical artifacts must be aggregate and non-identifying.

The verifier can check exact paths, hashes, table columns, join assertions, certificate schema and negative status, state ordering, repeat-date independence, instance selection, equations and numerical tests, feature manifests, fold isolation, grids, seeds, null completion, gate statuses, and whether each conclusion is linked to computed outputs. It cannot decide whether an unavailable field is clinically the intended assay, whether biomarker status represents CKD, whether measured GFR agrees, whether testing benefits patients, whether an intervention is useful, or whether results transport outside this selected UKB repeat-attender cohort. Those require a valid external/frozen assay certificate, clinical adjudication, repeated clinical records, observed testing decisions, utility/cost evidence, and preferably measured GFR.

## What changed and what remains uncertain

The parent already had the correct baseline-only observed-schedule question, exact current UKB bindings, neutral fail-closed assay certificate, race-free 2021 CKD-EPI formulas, and strict no-CKD/no-causal/no-utility boundaries. This successor makes execution auditable at the boundary where a run must stop. It adds a three-state execution contract that forbids row-level biological output in the current metadata-only stop, makes optional technical integrity QA non-scientific, and requires a certified state before any cohort, eGFR, model, or outcome output. It also makes repeat-instance handling deterministic: instance 1 and its date are selected before repeat assay completeness, no instance substitution is allowed, invalid dates and each loss reason are separated, and the variable observed interval is assigned once without entering the baseline model. Finally, every interpretive claim is linked to named gates and output artifacts, so a technically correct stop cannot be presented as a negative finding and a predictive result cannot bypass timing, leakage, null, calibration, or selection checks.

The central uncertainty is unchanged and deliberately preserved: this frozen package does not certify the semantics or comparability of 30700/30720, so no scientific discordance result is currently admissible. Even after certification, selected repeat attendance, variable timing, lack of albuminuria/adjudication/measured GFR, absence of clinical testing actions, and no external utility data limit the claims.
