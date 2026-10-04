> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# HCC repeat-TACE P-beyond-B validation with an explicit three-layer laboratory interpretation contract

## Successor, unresolved question, and substantive repair

This proposal is a targeted child of `[prior hypothesis]` and `[prior hypothesis]`. It preserves the selected mature design in full: the frozen adult repeat-TACE cohort; systemic-record/comparator arm definition; exact B/P/event/Y clocks; annual forward blocks; locked nested ridge estimand; assay-separated all-BP missing-Y partial-identification bounds; patient-frequency bootstrap; event/source/window-specific observability horizons; and strict noncausal evidence limits.

The unchanged primary question is:

> Among selected adult HCC repeat-TACE episodes with remote baseline assay B and pre-repeat assay P, does P improve held-out prediction of the subsequent same-assay numeric laboratory observation Y beyond B and the locked pre-event core?

The remaining clinically material gap is not another prediction model. A finite number in the laboratory table establishes only that a numeric result was recorded. It does not establish that the specimen was valid, that the result was reported in a comparable unit or reference system, or that a three-value numeric sequence is a clinically interpretable HCC trajectory. This successor adds an executable three-layer laboratory interpretation and adjudication contract around the unchanged estimand:

1. **Recorded assay observation**: an exact-assay row with linked identifiers, valid `assay time`, and finite uncensored `quantitative result` under the inherited parser.
2. **Structured result-quality evidence**: auditable specimen/result metadata and duplicate/conflict checks using only `specimen type`, `qualitative result`, `quantitative result`, keys, and time. This is evidence about data structure, not proof of specimen or assay validity.
3. **Clinical trajectory interpretability**: a separate status. Because the HCC source has no unit, reference-range, specimen-collection/accession, assay-platform, or adjudicated validity fields, clinical interpretability is not establishable from this dataset. A B/P/Y numeric sequence may therefore be reported only as a recorded numeric assay trajectory, never as hepatic improvement, deterioration, treatment response, toxicity, or patient-important HCC change.

The added layer is a repair of interpretation, not a change to cohort, clocks, models, estimand, bounds, horizons, or causal scope. It makes a falsifiable distinction between what the computation can check and what requires clinical adjudication.

## Evidence-supported versus untested claims

The inherited full-source audit supports feasibility of selected short-horizon prognostic computation and outcome-blind observation diagnostics only. It does not establish incremental prediction, missing-at-random outcome observation, specimen validity, unit comparability, assay calibration, clinical severity, tumor response, or benefit. Any inherited counts or parent audit findings remain parent support, not new results from this proposal.

The experiment tests whether the pre-specified recorded numeric Y prediction comparison is reproducible under the frozen design and whether its interpretation is limited by observed laboratory metadata quality and unavailability. It does **not** test whether P changes disease, treatment response, liver function, safety, survival, or clinical decisions.

The strongest conclusion that the available data could support is a selected-calendar, noncausal association between a recorded pre-repeat numeric assay value and a later recorded numeric same-assay value, conditional on the stated observed-case and partial-identification contracts. Even that conclusion must be labeled selection-sensitive if observation or metadata-quality strata differ materially or the all-BP bound crosses zero.

A clinical claim that the trajectory is valid or interpretable requires adjudication against laboratory information-system metadata or chart review, including specimen collection/accession status, assay platform, units, reference ranges, dilution/hemolysis or rejection flags, and clinical context. None of those unavailable facts may be inferred from this source.

## Frozen source and exact data bindings

Use HCC snapshot `[source checksum]`, catalog `[internal dataset path]` ([source checksum]), and the read-only ordinary CSV sources listed in `[internal dataset path]`. Scan every source row; do not sample source data. Verify source and schema hashes and required headers before reconstruction. Before every existence join, report duplicate composite-key counts on (`patient master index`,`visit number`); deduplicate existence joins and never permit many-to-many multiplication.

Required bindings are:

* `encounters`, schema `datasets/hcc/table-b743286cb1249287.json`, source `HCC/data_basic_information_2500296761891079109.csv`, columns `patient master index`, `encounter number`, `age`, `sex`, `encounter time`, `admission time`, `discharge time`, `encounter department`. `Discharge time` is only an encounter-close recording.
* `diagnoses`, schema `datasets/hcc/table-12710723c3df0c99.json`, source `HCC/data_diagnosis_7504718184492840569.csv`, exact `diagnosis name == hepatocellular carcinoma`; it has no native time, so timing is inherited only from the linked encounter.
* `procedures`, schema `datasets/hcc/table-d5eae16f8f8093d9.json`, source `HCC/data_surgery_8024330590283626027.csv`, columns `surgery`, `start time`, `end time`, `surgery source`; case-insensitive `TACE` or literal `chemoembolization`, valid `start time`, same-patient same-calendar-day collapse, inherited first adjacent 14–180-day pair and first strict 15–90-day repeat event.
* `medications`, schema `datasets/hcc/table-4f6ecaeb6e8f69c2.json`, source `HCC/data_Medication_5693407050835159466.csv`; retain the inherited systemic-record ontology and exclusions. Medication times are recorded orders, not administrations.
* `labs`, schema `datasets/hcc/table-38aad8c54471332f.json`, source `HCC/data_Test_609065997844652188.csv`, columns exactly `Patient Master Index`, `Encounter Number`, `Test`, `Qualitative Result`, `Quantitative Result`, `Specimen Type`, `Test Time`. Exact assays are `Test == Albumin` and `Test == Total bilirubin`, analyzed separately. No unit, reference-range, collection/accession, rejection, platform, or validity column exists.
* `examinations`, schema `datasets/hcc/table-fd016d2731b9d6c6.json`, source `HCC/data_examination_4203595081195465282.csv`, valid `Start Time` and linked keys only for observation opportunity/horizon; never read `Examination Findings` or `Examination Diagnosis`.
* `clinical_documents`, schema `datasets/hcc/table-66afca58512c2fca.json`, source `HCC/data_medical_records_8434587325530196878.csv`, duplicate header represented as `Admission Diagnosis__duplicate_2`; use nonempty linked-row presence only, optionally timed by linked encounter `Encounter Time`, never narrative text.
* `orders`, schema `datasets/hcc/table-6b93dcf0ea823702.json`, source `HCC/data_Non-drug order_2062526727266216118.csv`, fixed first-valid precedence over `Order time`, `Start time`, `End time`; recorded order only.
* `transfers`, schema `datasets/hcc/table-320c20f732e71789.json`, source `HCC/data_Transfers_7369490831683459252.csv`, identifier-only (`Patient master index`,`Visit number`), no temporal or destination payload.
* `vitals`, schema `datasets/hcc/table-8436de9cba74b8ca.json`, and `front_page`, schema `datasets/hcc/table-38b3224239acc33f.json`, identifier-only/nominal; neither is a physiologic or outcome source.

Pathology is not required for the frozen design and its narrative fields must not be used to adjudicate laboratory validity. No HCC source supplies the missing laboratory unit/reference/collection/quality fields.

## Frozen cohort, event selection, clocks, and estimand

Assert the inherited reconstruction gates exactly: 319 systemic-record patients, 1,491 comparator patients, 159 selected systemic repeat events, 526 selected comparator repeat events, and assay-specific complete triplets albumin 40/118 and total bilirubin 41/119 by arm. A mismatch is `unsupported`; do not silently repair denominators. Event selection must not inspect labs, examination rows, documents, orders, discharge, transfers, Y, or any downstream record.

For each assay separately:

* B is the latest finite, uncensored exact-assay numeric result in the TACE2 calendar-day window `[day -30, day -1]`.
* P is the latest finite, uncensored exact-assay numeric result in the selected repeat encounter in `[event_time -72 hours, event_time)`.
* Y is the nearest finite, valid same-assay numeric result to `event_time +24 hours` in `(event_time, event_time +72 hours]`, using the inherited deterministic tie rule.
* Create `BP_eligible` after B and P but before attaching Y or any downstream label. Require `B_time < P_time < event_time < Y_time` when Y exists and positive P lead. Missing Y remains missing and is never zero, failed, censored, or clinically negative.
* Use origins 2021-01-01, 2022-01-01, 2023-01-01, and 2024-01-01. Training events have `event_date < origin`; each future block is `[origin, origin+365 days)`.

Fit only on pre-origin observed complete triplets with the locked specifications:

```
M0: Y ~ B + systemic-record indicator + age + sex indicators
       + TACE2-to-repeat days + P-lead hours
M1: M0 + P
```

Preserve training-only age median plus missingness indicator, sex coding, variance filtering, centering/scaling, inner leave-one-patient-out alpha selection over `[0.01, 0.1, 1, 10, 100]`, ridge fitting, fixed pre-origin preprocessing/predictions, observed complete-triplet standardized held-out RMSE gain `(RMSE0-RMSE1)/SD_test(Y)`, and inherited arm-stratified patient-frequency bootstrap. No interpretation-layer variable may enter event selection, M0/M1, the primary endpoint, partial-identification bounds, or the bootstrap denominator.

Preserve the assay-separated training-range affine missing-Y bounds, global all-BP denominator, category-level diagnostic intervals without invalid aggregation, common-displacement stress test, and all inherited support/adverse/selection-sensitive/inconclusive branches. No Y imputation is allowed.

## Three-layer laboratory status contract

### Layer 1: recorded assay observation

For every raw lab row and for selected B, P, and Y candidates, emit a mechanical audit record containing patient and encounter keys, exact assay string, raw `test time`, parsed time validity, raw `quantitative result`, finite numeric parser result, censor/non-numeric status, raw `specimen type` presence, raw `qualitative result` presence, and source-row multiplicity. The only Layer-1 pass used by the frozen clocks is:

`exact_assay = 1 AND valid test time = 1 AND finite_uncensored quantitative result = 1 AND linked composite key = 1`.

This means **recorded_numeric_observation**, not specimen validity and not clinical validity. Preserve the inherited clock parser and tie handling exactly; the new audit must not discard or replace a Layer-1 row in the primary analysis.

A source row with finite `quantitative result` but missing `specimen type` is still a Layer-1 recorded numeric observation under the frozen contract and receives `specimen_metadata_missing=1`. A nonfinite, censored, malformed, wrong-assay, or untimed row is not a Layer-1 candidate, exactly as before.

### Layer 2: structured result-quality evidence

For every selected B/P/Y row and every competing exact-assay row at the same patient/encounter/time, calculate these fields without using narrative text:

* `specimen_type_present`: `1` iff trimmed `specimen type` is nonempty, else `0`.
* `specimen_type_conflict`: `1` iff selected/tied rows for the same patient, exact assay, encounter and timestamp have more than one nonempty specimen-type value; `0` iff all nonempty values agree; `not_evaluable` if no nonempty value exists.
* `numeric_result_conflict`: `1` iff tied duplicate rows for the same patient, exact assay, encounter and timestamp have two or more distinct finite numeric values; `0` iff all finite numeric values agree; `not_evaluable` if no finite duplicate comparison exists.
* `qualitative_present`: `1` iff trimmed `qualitative result` is nonempty. It is descriptive only.
* `qualitative_numeric_consistency`: always `not_evaluable` unless an externally supplied, assay-specific validated mapping is present. No mapping is present in HCC; do not infer that a qualitative label agrees or disagrees with a numeric value.
* `unit_present`, `reference_range_present`, `collection_time_present`, `accession_present`, `rejection/quality_flag_present`, and `assay_platform_present`: `0` globally from the verified HCC schema, not row-level missing values.

Define `structured_quality_review` as `required` if `specimen_type_conflict=1`, `numeric_result_conflict=1`, a required metadata value is missing, or the selected value required a duplicate tie resolution. Define it as `not_required_by_available_fields` only when the row has nonconflicting available metadata; this label still does not mean valid. Define `structured_quality_pass` only as the narrow mechanical statement that key, exact assay, finite numeric/time, and no duplicate numeric/specimen conflict are present. It must not be called `specimen_valid`, `assay_valid`, or `clinically_valid`.

When duplicate rows disagree, retain the inherited deterministic selected value for the frozen clock but mark the episode `adjudication_needed=1`; do not claim that the selected value is true. Report duplicate/conflict counts before any deduplication and preserve the raw multiplicity audit.

### Layer 3: clinical trajectory interpretability

For each assay-specific B/P/Y triplet emit:

* `recorded_numeric_trajectory = 1` iff B, P, and Y all pass Layer 1 and satisfy the frozen temporal clocks.
* `metadata_consistent_candidate = 1` iff all three rows have nonempty, mutually equal `specimen type`, no specimen/numeric duplicate conflict, and no unresolved tie conflict. This is a candidate comparability flag only.
* `clinical_trajectory_interpretable = unavailable` for every episode under this HCC snapshot, because units, reference ranges, collection/accession status, assay platform, rejection/hemolysis/dilution flags, and adjudicated specimen validity are absent. Do not convert this global unavailability into a numerical missingness value.
* `adjudication_needed = 1` whenever `clinical_trajectory_interpretable=unavailable`; additionally flag missing/conflicting specimen metadata, numeric duplicate conflict, or a non-evaluable qualitative/numeric relationship.
* `trajectory_language = recorded_numeric_only` for all computable triplets. Prohibited replacements include improved/worsened liver function, hepatic failure, response, progression, toxicity, safety, or patient benefit.

Report model results separately for the frozen Layer-1 observed-case estimand and the descriptive Layer-2 metadata strata (`metadata_consistent_candidate` versus review). These strata are diagnostics and sensitivity descriptions only. They cannot filter the primary cohort, redefine Y, change bounds, or repair missing outcomes. If the favorable observed-case result occurs only in a metadata-complete subset, label it `selection_sensitive` rather than clinically validated.

## Falsifiable negative-control and adjudication-needed layer

The available source does not contain a validated clinical negative-control endpoint. The design therefore uses a deliberately limited, auditable data-integrity negative-control plus an explicit adjudication gate, without pretending either is clinical validation.

### Temporal integrity negative control

After the frozen primary data are built, construct a pre-P pseudo-target `C` for each assay-specific BP row as the nearest finite exact-assay numeric result in `[event_time-168 hours, event_time-72 hours)`, if one exists. `C` is not an outcome, is never merged into B/P/Y, and cannot enter the primary models or bounds. Fit a separately labeled **negative-control audit** using the same frozen feature preprocessing and locked ridge machinery but with C as the descriptive target and with P excluded from the predictor set because P occurs after C. Compare:

* `C ~ B + core` versus `C ~ B + core + a pre-C covariate-only control`, where the added control is restricted to variables known before C and available in the frozen source; and
* a time-shuffled patient-block permutation of C that preserves assay, calendar block, and observed/missing pattern.

The audit is not expected to prove a null clinical relationship. Its falsifiable purpose is narrower: any claim that the primary P-beyond-B result reflects a properly ordered future numeric observation must not be accompanied by evidence of impossible time reversal, duplicate leakage, or an improvement created solely by rows that are also used after C. A nonzero apparent increment under an impossible-time or duplicated-row construction, leakage of a Y row into C/B/P, or failure of the synthetic boundary tests is a `negative_control_warning` and forces `selection_sensitive` or `unsupported`; it cannot support a clinical trajectory claim. If no eligible C exists, report `negative_control_not_estimable`, not a reassuring null.

Because P may be biologically correlated with earlier measurements, the negative-control audit must never be interpreted as a test that true disease trajectories are independent over time. It is a parser/order/duplication falsification check only.

### Adjudication gate

For every assay, block, arm, and Y-observed state, report N and fractions for: Layer-1 recorded numeric status; specimen metadata present; specimen metadata conflict; numeric duplicate conflict; metadata-consistent candidate; and global clinical interpretability unavailable. A cell with fewer than five episodes is suppressed/marked; formal contrasts require at least ten BP rows. If any required adjudication field is absent (as it is here), emit `adjudication_needed/unavailable` rather than treating absence as a pass.

A future study may adjudicate a sample by linking each result to specimen accession/collection, unit, reference interval, assay platform, rejection/quality flags, and clinical context. Only after such adjudication could a clinically interpretable trajectory estimand be defined. The present experiment must not backfill those facts from `specimen type`, `qualitative result`, encounter type, discharge, examination presence, or document text.

## Outcome-blind opportunity and event/source horizons

Retain the mature outcome-blind and source-horizon contract unchanged. For each BP row define `D_y = event_time +72 hours`; before reading target Y or any source rows after `D_y`, freeze mutually exclusive strata: `exam+followup`, `exam_only`, `followup_only`, `document_only`, `none`, using valid examination `Start Time`, additional encounter `Encounter Time`, and nonempty linked clinical-document presence exactly as in the selected parent. Documents have no native timestamp and may be called encounter-timed only through linked encounter time.

For the selected encounter, classify valid `discharge time` as before: `< event`, `== event`, `(event,D_y]`, `>D_y`, or missing/invalid. It is not disposition, survival, transfer, completed follow-up, or proof of absent Y. Emit `death_status=unavailable` globally. A transfers key match is only `nominal_transfer_key_present`; transfer payload is unavailable.

For every BP event, assay, origin/block, source, and requested window, compute patient-event-specific source horizons from valid independent timestamps. Use encounters `encounter time` (excluding selected event encounter), labs `test time` (excluding Y and all B/P/clock-defining rows as anchors), examinations `start time`, orders under fixed timestamp precedence, medications/procedures valid recorded times, and encounter-timed documents. Transfers, vitals, and front_page have no usable temporal payload. For D1 `(event+72h,event+7d)` require an independent anchor at or beyond day 7; for D2 `[event+7d,event+30d]` require an anchor at or beyond day 30. Never substitute a snapshot-global maximum. Incomplete source horizons are `administratively_incomplete`, not no-care.

These opportunity and horizon variables remain descriptive recording diagnostics. They cannot enter primary models, the three laboratory status layers, bounds, or bootstrap denominators, and they do not establish specimen completion or clinical follow-up.

## Missing-Y bounds, bootstrap, and tipping point

Preserve the mature all-BP partial-identification procedure exactly. Fit M0/M1 only on pre-origin complete triplets; freeze finite predictions for every BP row; define training range `[L_train,U_train]` before inspecting future Y; reject future Y outside that range as temporal-bound `unsupported`; retain every BP row in the fixed global denominator N. For observed rows use `d(y)=2y(p1-p0)+p0^2-p1^2`; for missing rows evaluate exact affine endpoint minima/maxima at L and U. Report global and arm-specific bounds, all-L/all-U and least-favorable scenarios, separately from confidence intervals. Preserve fixed-prediction, arm-stratified, patient-frequency bootstrap with original point-estimate SD denominator and all inherited stop rules. Preserve the continuous piecewise-linear common-displacement tipping calculation. No laboratory metadata status, opportunity state, discharge state, or adjudication flag may be used to impute Y or tighten the primary bounds.

## Interpretation precedence and falsification criteria

Use this precedence:

1. `unsupported` for source/schema/hash/header/clock/join failure, duplicate multiplication, target leakage into horizon or negative-control C, invalid parser semantics, or any inference of death/transfer/disposition/clinical validity from unavailable fields.
2. `inconclusive` for failed cohort/arm gates, sparse cells, nonfinite predictions, empty/degenerate training range, future Y outside range, non-estimable SD/bootstrap, unavailable source horizon, or non-estimable negative-control audit.
3. `adverse_primary` for a nonpositive adequately supported observed-case contrast, repeated M1 degradation, or all-BP global bound wholly nonpositive; downstream recording or metadata patterns cannot rescue it.
4. `selection_sensitive` for favorable observed-case gain with a global bound crossing zero, material Y-observation or metadata-quality gradients, duplicate/specimen conflict, negative-control warning, strong arm/calendar heterogeneity, or source disagreement.
5. `supported_recording_description` only for a finite, reproducible, gate-passing recorded-data result with relevant horizons complete and no unresolved negative-control warning. This means support for a recorded numeric prognostic association/recording description only; it never means specimen validity, clinical trajectory validity, treatment response, benefit, or actionability.

For the primary prognostic claim, supportive language remains allowed only if the inherited observed-case estimand is estimable, gates pass, no material observation or metadata warning exists, and the global all-BP Delta interval is strictly positive over the declared training-range scenario. Even then state `recorded_numeric_association_in_selected_calendar_mixture`; never translate it into HCC laboratory improvement or deterioration.

The synthetic oracle/verifier must test exact Y, D1, D2, discharge, B/P/P-lead boundaries; selected-encounter exclusion; malformed/pre-admission discharge; identifier-only transfers; unavailable death; document text non-use; target-Y and clock-row exclusion from horizons; event-specific horizons; assay separation; all-BP denominator preservation; duplicate-safe joins; specimen-type missing/equal/conflict states; numeric duplicate conflict; non-evaluable qualitative/numeric consistency; global unit/reference/collection unavailability; metadata flags not entering M0/M1/bounds/bootstrap; impossible-time negative-control leakage; negative-control-not-estimable branch; and supportive, adverse, selection-sensitive, and inconclusive branches.

## Computationally checkable limits and required further evidence

The compiler/verifier can check hashes, headers, schemas, duplicate counts, cohort/event reconstruction, exact clocks, finite numeric parsing, source-row multiplicity, specimen-presence/conflict flags, numeric duplicate conflicts, global schema absence of units/reference ranges, negative-control temporal boundaries, frozen predictions, bounds, bootstrap bookkeeping, horizons, and interpretation labels. It cannot establish specimen validity, true assay result validity, unit comparability, reference-range meaning, collection versus report timing, assay calibration, hemolysis/dilution/rejection, clinical severity, imaging response, treatment intent/administration, mortality, external-care capture, causality, utility, actionability, or patient benefit.

Relative to `[prior hypothesis]`, this child keeps the mature event/source horizon and partial-identification safeguards and adds a concrete three-layer laboratory contract, duplicate/specimen metadata auditing, a global unavailable-clinical-interpretability status, and a falsifiable time-order/data-integrity negative-control. Relative to `[prior hypothesis]`, it retains the exact compiler-ready bounds/bootstrap/clock specification while closing the remaining semantic gap between a finite lab number and a clinically meaningful trajectory. No new HCC empirical claim is made, and no frozen scientific schema is changed.
