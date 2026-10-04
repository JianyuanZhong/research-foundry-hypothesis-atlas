# Compiler-ready eICU test of exact ventilation care-plan labels against a persistent respiratory-state endpoint

## Scope, evidence boundary, and substantive advance

This is a substantive child of the two assigned assessed-valid candidates `[prior hypothesis]` and `[prior hypothesis]`. It preserves their frozen scientific question rather than reopening the already completed vocabulary and transportability findings.

The strongest claim supported by the existing lineage is limited to exported structured documentation: the exact care-plan strings are sparse and hospital-concentrated; their prior chart associations are not a stable unqualified multicenter phenotype; peak-pressure charting dominated the earlier proxy; and available fields do not validly ascertain durable liberation. Those findings do not establish what clinicians intended or did at the bedside.

The unresolved claim is narrower and falsifiable: **within the frozen labelled person-landmarks, does receipt of `Ventilated - with daily extubation evaluation` rather than `Ventilated - with no daily extubation trial` contain reproducible information about a subsequent persistent, safety-preserving, independently charted respiratory-state trajectory, beyond respiratory state and documentation opportunity observed strictly before the decision time?**

The estimand is descriptive conditional association and held-out predictive increment, not a treatment effect. A positive result would mean only that the exact label adds information for this structured chart construct in this eICU snapshot. It would not establish a daily extubation evaluation, spontaneous breathing trial, delivered ventilator setting, readiness, liberation, quality, benefit, harm, or causality. A negative result would be useful evidence against fitness of the label for this proxy endpoint, not proof that bedside evaluation did not occur.

The advance over both parents is a fail-closed execution contract. It makes deterministic reconstruction auditable before any outcome read, freezes endpoint labels and parser behavior before arm-specific summaries, separates endpoint observability from the value of the label, handles early exits as competing states rather than silently deleting them, and makes leakage, hospital holdout, repeated-landmark clustering, uncertainty, and interpretation gates mechanically testable. No results are claimed here.

## Frozen population, exposure, and time axis

The population is exactly the inherited eICU cohort: **540 person-landmarks, 443 ICU stays, and 74 hospitals**. Use the first qualifying ICU stay per `uniquepid`; retain all eligible landmarks within that retained first stay. The only allowed landmarks are:

`L ∈ {1440, 2880, 4320, 5760, 7200}` minutes after ICU admission.

The exact exposure strings are case-sensitive after the parent’s prescribed trimming rule:

- `evaluation`: `Ventilated - with daily extubation evaluation`
- `no_trial`: `Ventilated - with no daily extubation trial`

For each eligible landmark, use the first exact target label in `[L, L+360]` under the parent tie and contradiction rule. Define `D` as that selected row’s `cplitemoffset`, not as `L`. Require `L <= D <= L+360` and verify `D` equals the selected source row offset. Contradictory first target labels at the same decision time remain excluded exactly as in the parent recipe. No post-D information may change eligibility, label choice, or the frozen denominator.

All inherited exclusions remain unchanged and must be reproduced, not approximated: adult eligibility; first qualifying stay per `uniquepid`; ICU continuation through the required landmark; pre-L invasive-airway evidence exclusion; the strict pre-L physiologic screen; prior end-of-life discussion exclusion; prior 24-hour `Spontaneous - adequate` exclusion; and every other parent filter and tie rule. The compiler must import or reconstruct the parent recipe version and record each filter, rather than infer eligibility from the 540 count alone.

## Source snapshot and exact read-only bindings

Use only the eICU 2.0 snapshot identified in the dataset guide.

- Snapshot: `[source checksum]`
- Catalog: `[internal dataset path]`
- Catalog [source checksum]
- Read-only source root: `[internal dataset path]`
- Every `.csv.gz` below is an ordinary file archive member, not a nested archive member.

All longitudinal tables join to `patient` only through `patientunitstayid`. Never join measurements on `uniquepid` or `patienthealthsystemstayid`. Source files and schema JSONs are read-only; derived artifacts are written only in the workspace.

### Required source bindings

1. **`patient`**
   - Source: `[internal dataset path]`
   - Source [source checksum]
   - Archive member: ordinary file
   - Schema: `[internal dataset path]`
   - Schema [source checksum]
   - Required columns: `patientunitstayid`, `uniquepid`, `hospitalid`, `unitvisitnumber`, `age`, `unitdischargeoffset`, `unitdischargestatus`, `unitdischargelocation`.
   - Use: stay/person identity, first-stay selection, adult and landmark continuation checks, hospital grouping, and exit classification.

2. **`carePlanGeneral`**
   - Source: `[internal dataset path]`
   - Source [source checksum]
   - Archive member: ordinary file
   - Schema: `[internal dataset path]`
   - Schema [source checksum]
   - Required columns: `cplgeneralid`, `patientunitstayid`, `cplitemoffset`, `cplgroup`, `cplitemvalue`, `activeupondischarge`.
   - Use: exact exposure reconstruction/verification, `D`, contradictory-label handling, and the inherited `Spontaneous - adequate` rule only. Care-plan values and counts are prohibited from the primary endpoint and from post-D baseline predictors.

3. **`carePlanEOL`**
   - Source: `[internal dataset path]`
   - Source [source checksum]
   - Archive member: ordinary file
   - Schema: `[internal dataset path]`
   - Schema [source checksum]
   - Required columns: `cpleolid`, `patientunitstayid`, `cpleolsaveoffset`, `cpleoldiscussionoffset`, `activeupondischarge`.
   - Use: reproduce the inherited prior end-of-life exclusion with the parent’s exact offset semantics; do not reinterpret it.

4. **`apacheApsVar`**
   - Source: `[internal dataset path]`
   - Source [source checksum]
   - Archive member: ordinary file
   - Schema: `[internal dataset path]`
   - Schema [source checksum]
   - Required columns: `apacheapsvarid`, `patientunitstayid`, and the parent-specified inherited-screen fields including `intubated`, `vent`, `respiratoryrate`, and other fields in the schema.
   - Use: reproduce the frozen pre-L physiologic screen only; it may not be redesigned after inspecting outcomes.

5. **`respiratoryCharting`**
   - Source: `[internal dataset path]`
   - Source [source checksum]
   - Archive member: ordinary file
   - Schema: `[internal dataset path]`
   - Schema [source checksum]
   - Required columns: `respchartid`, `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`.
   - Use: numeric respiratory settings and pre/post opportunity. `respchartoffset` is clinical time; `respchartentryoffset` is documentation time and may not place a measurement in a window.

6. **`respiratoryCare`**
   - Source: `[internal dataset path]`
   - Source [source checksum]
   - Archive member: ordinary file
   - Schema: `[internal dataset path]`
   - Schema [source checksum]
   - Required columns: `respcareid`, `patientunitstayid`, `respcarestatusoffset`, `airwaytype`, `airwaysize`, `airwayposition`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`.
   - Use: inherited pre-L invasive screen and post-window corroboration/recency sensitivities. Record time is `respcarestatusoffset`; interval endpoints are not substituted for record time.

7. **`vitalPeriodic`**
   - Source: `[internal dataset path]`
   - Source [source checksum]
   - Archive member: ordinary file
   - Schema: `[internal dataset path]`
   - Schema [source checksum]
   - Required columns: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `sao2`, `respiration`.
   - Use: safety domain. These are five-minute summary observations, not raw waveforms.

8. **`vitalAperiodic`**
   - Source: `[internal dataset path]`
   - Source [source checksum]
   - Archive member: ordinary file
   - Schema: `[internal dataset path]`
   - Schema [source checksum]
   - Required columns: `vitalaperiodicid`, `patientunitstayid`, `observationoffset`, `noninvasivemean`.
   - Use: optional pre-D hemodynamic sensitivity only; never a primary endpoint or exposure feature.

9. **`treatment`**
   - Source: `[internal dataset path]`
   - Source [source checksum]
   - Archive member: ordinary file
   - Schema: `[internal dataset path]`
   - Schema [source checksum]
   - Required columns: `treatmentid`, `patientunitstayid`, `treatmentoffset`, `treatmentstring`, `activeupondischarge`.
   - Use: airway-transition validation sensitivity only. Structured treatment strings are not adjudicated procedure truth.

The full eICU catalog additionally lists the other source tables, but they are not needed for this frozen endpoint. If any required source is absent, has a changed hash/header/schema, or is not an ordinary file member, stop and report feasibility failure rather than substitute another table.

## Deterministic lineage reconstruction before outcome access

The compiler must resolve parent support by content hash, never by stale absolute paths embedded in an earlier workspace. Expected parent artifacts are:

- `eicu_strict_cohort.csv`, [source checksum];
- the parent action-row artifact containing one selected target label and `D` per person-landmark, [source checksum].

The compiler first searches declared candidate support and workspace inputs for these exact hashes. If either artifact is unavailable, it may reconstruct it from the raw snapshot using the frozen parent recipe, but must write a canonical byte-stable replacement and validate it independently. A reconstruction is not accepted merely because it has 540 rows.

Before opening or aggregating any `respiratoryCharting`, `respiratoryCare`, or `vitalPeriodic` outcome values, perform all of the following checks and write their results:

1. Exact expected headers, column names, and schema hashes.
2. One row per `(patientunitstayid, landmark)` in the population and one matching action row.
3. Exactly 540 person-landmark rows, 443 distinct `patientunitstayid` values, 74 distinct `hospitalid` values, and exactly the five allowed landmarks.
4. First qualifying stay per `uniquepid`, with no duplicate retained stay/person identity violating the parent rule.
5. Exact arm strings only; `D` equals the selected `cplitemoffset`; and `L <= D <= L+360` for every row.
6. No contradictory target rows under the inherited same-time rule.
7. Every inherited exclusion flag and source-row identity/digest agrees with the parent artifact or independently reproduced parent recipe.
8. Recompute a deterministic row digest after sorting by `(patientunitstayid, landmark, D, cplgeneralid)` and a deterministic artifact hash. Compare both to the expected lineage where supplied.

Any mismatch in recipe version, row count, identity, hospital, landmark, arm, `D`, exclusion, tie rule, digest, or hash is a **fatal lineage stop**. At that stop, produce only a feasibility/inconclusive artifact and no outcome summary, endpoint estimate, model, or clinical interpretation. This prevents an approximate cohort from being presented as a replication.

The manifest must record snapshot and catalog identifiers, all source and schema hashes, parent artifact hashes, actual absolute source paths, archive-member convention, parser and endpoint version, random seed, deterministic sort order, row counts before and after every filter, and the reason for any stop.

## Outcome-blind parser and endpoint freeze

Freeze parser version, exact labels, bounds, windows, and thresholds in a configuration artifact before arm-specific endpoint counts or outcome summaries. Full-source scans must enumerate every encountered `respchartvaluelabel`, its frequency, matched family, and unmatched status. No substring expansion, post hoc synonym addition, or outcome-guided label mapping is allowed.

Use `respchartoffset` as clinical time. `respchartentryoffset` is retained only for documentation lag/opportunity diagnostics and never rescues a measurement whose clinical time is after `D`.

### Numeric component dictionary

Primary non-peak support families use only these exact trimmed labels:

- PEEP: `PEEP`, `PEEP/CPAP`
- pressure support: `Pressure Support`, `PS above PEEP`
- set rate: `Vent Rate`, `VS RESP RATE`

FiO2 labels are retained as a prespecified sensitivity, not silently combined with pressure settings, because the available export does not supply local unit/interface metadata and fraction-like versus percent-like values cannot be safely normalized without an unsupported conversion:

- FiO2 sensitivity: `FiO2`, `FIO2 (%)`, `Set Fraction of Inspired Oxygen (FIO2)`

The following are excluded from the primary support dictionary: `Peak Insp. Pressure`, `Peak Pressure`, `Plateau Pressure`, `Peak Flow`, `Mean Airway Pressure`, `Pressure Control`, spontaneous/total rate labels, and oxygen-flow labels. They can appear in a label-audit or explicitly named ablation only. Matching is exact and case-sensitive after trimming outer whitespace; no synonym normalization is permitted.

For every candidate value, trim outer whitespace and parse only a complete signed decimal/scientific token matching:

`^[+-]?(?:\\d+(?:\\.\\d*)?|\\.\\d+)(?:[eE][+-]?\\d+)?$`

Reject blanks, embedded units, ranges, inequalities, nonnumeric strings, nonfinite values, and values outside fixed bounds. Bounds are PEEP and pressure support `[0,60]`, set rate `[0,100]`, FiO2 `[0,100]` as recorded (without conversion), `sao2` `[0,100]`, and respiration `[0,200]`. Record raw value, parsed value, rejection reason, matched label, component, and parser version. Do not impute, interpolate, carry forward, or substitute a different component.

For each component and each window, require at least two valid observations at distinct clinical offsets separated by at least 30 minutes. Use the median of all valid values in that interval. Record valid count, unique-time count, first and last offset, maximum and median gap, raw/rejected counts, and missingness reason. Equal-time duplicate rows do not satisfy the spacing rule; deterministic row IDs are retained for tie diagnostics.

### Fixed windows and persistent endpoint

For every frozen row:

- prior trajectory window `P = (D-1440, D-720]`;
- immediate pre-D state window `B = (D-720, D]`;
- primary post-label window `O = (D+360, D+1800]`;
- horizon sensitivity `O12 = (D+360, D+1080]`.

The six-hour washout is fixed. Boundary equality follows these half-open definitions exactly.

For a support component observed with the required observations in both `B` and `O`, define a reduction as post median minus B median below or equal to the negative threshold: at least 2 cm H2O for PEEP or pressure support and at least 2 breaths/min for set rate. The primary support domain is positive if at least one of these three non-peak components qualifies. The FiO2 sensitivity uses a reduction of at least 0.05 in the recorded scale but must be reported separately with all unit-ambiguity diagnostics; it cannot be used to rescue the primary endpoint when all pressure/rate components are unavailable.

The safety domain uses only `vitalPeriodic.sao2` and `vitalPeriodic.respiration`, each parsed from its numeric column and summarized with the same two-observation/30-minute-spacing/median rule in `B` and `O`. Safety passes only if both are observed in both windows, post `sao2` is not more than 2 percentage points below B, and post respiration is not more than 4 breaths/min above B. If either required safety signal lacks the minimum observations, the primary endpoint is missing rather than safe by absence of evidence.

The primary endpoint is therefore **persistent safety-preserving non-peak support reduction**: support domain positive and safety domain passing. The primary endpoint deliberately does not require `respiratoryCare` corroboration, because corroboration is a documentation-source availability property and its sparsity could turn the endpoint into a selective observation rule. Airway corroboration is a separately reported sensitivity, not proof of delivered settings.

Define mutually exclusive row states:

1. `persistent_improvement`: primary support reduction and safety pass, with no competing exit before completion of `O`;
2. `observed_non_improvement`: complete support/safety observation through `O`, no primary improvement, and no competing exit;
3. `endpoint_missing`: no competing exit, but required pre/post support or safety observations are insufficient or rejected;
4. `competing_exit`: death, discharge/transfer, or unclassifiable truncation occurs before the end of `O`, including an exit on or before `D+1800` under the primary horizon.

An exit at or before `D+360` is also flagged `no_post_washout_opportunity`; it remains a competing exit, not missingness or non-improvement. Use the first nonmissing `patient.unitdischargeoffset` relevant to the row. Classify `unitdischargestatus` equal to trimmed case-insensitive `Expired` as death; otherwise classify a known status/location as discharge/transfer; if offset exists but status/location cannot be classified, use truncation. Preserve separate exit and ascertainment reasons.

Report, by arm, hospital, and landmark, counts and denominators for all four states, no pre-D support, no post-D support, no pre/post safety, parser rejection, source absence, no corroboration in the corroboration sensitivity, and each competing exit type. No complete-case analysis may be shown without the full 540-row state distribution and the arm-specific observation/exit denominators.

Prespecified sensitivities are: a setting-only endpoint removing the safety requirement; a stricter both-safety/at-least-one-safety rule; FiO2-inclusive endpoint with the recorded-scale limitation; `O12`; airway corroboration requiring a post-window `respiratoryCare` row with nonempty `airwaytype` or at least one nonmissing ventilator interval field; and pre-L invasive-airway recency variants of 360, 1,440, and 4,320 minutes only when the parent artifact/recipe defines them. No sensitivity may replace the primary endpoint, and denominator changes must be displayed.

## Pre-D predictors and leakage contract

All baseline predictors must have clinical time `<= D`. This includes all state values, opportunity counts, source presence, measurement-time counts, medians, gaps, and entry-lag summaries. A row with `respchartentryoffset > D` cannot be used as a pre-D observation even when its entry timestamp is retained diagnostically.

The baseline state-plus-opportunity model may use only pre-D respiratory charting state/opportunity, pre-D vital safety state/opportunity, pre-D respiratory-care and treatment counts/presence, and inherited pre-D covariates. It must not use care-plan values, care-plan counts, post-D source rows, post-D treatments, post-D respiratory-care rows, post-D opportunity, endpoint availability, or any outcome-derived field.

Define three prespecified models:

- `opportunity_only`: pre-D row counts, distinct clinical times, distinct labels by frozen family, source presence, gaps, and entry-lag summaries, without respiratory values or label semantics;
- `state_only`: pre-D numeric state and fixed pre-D trends plus the same nonsemantic opportunity variables, without the exact target label;
- `state_plus_label`: the identical `state_only` feature contract plus the binary exact arm.

The primary predictive increment is `state_plus_label` versus identical `state_only` (with opportunity variables included in both). The secondary comparison is versus `opportunity_only`. A model cannot receive credit for predicting missingness alone: report four-state discrimination/calibration and the value-based persistent-improvement component separately.

Before fitting, write a leakage audit containing maximum clinical time for every predictor family, maximum entry time used, count of violations, offending table/column/row identifier, and a fail-closed stop if any violation is nonzero. Post-D opportunity may be reported as an ascertainment diagnostic only and cannot enter the primary model or primary estimand.

## Hospital-held-out evaluation and repeated-landmark uncertainty

The primary transport estimand is leave-one-hospital-out prediction. For every held-out hospital, fit imputation, standardization, feature selection, regularization, observation weights, calibration, and any hyperparameters on training hospitals only. No held-out outcome, label rate, target rate, or calibration intercept may be used in training. Hospital ID may define the split and training stratum but may not encode held-out outcome rates.

Report fold-specific and aggregate:

- row-weighted micro and equal-hospital macro log loss and Brier score;
- calibration slope/intercept where estimable;
- AUROC only when both relevant classes occur, with availability counts;
- observed and predicted evaluation-minus-no-trial risk differences where both arms and endpoint states are supported;
- test row/stay counts, four-state counts, label counts, missingness, exits, and hospital-specific directions.

The label-contrast gate requires at least five hospitals with at least 10 complete endpoint-observed rows under each arm, at least 50% of analyzed complete rows arising in those hospitals, and no arm contributing over 40% from one hospital. If this support does not exist, label-contrast transport is inconclusive; do not pool sparse rows and call the result multicenter evidence. Folds with one label only may contribute to broad four-state prediction when the metric is mathematically defined, but cannot contribute a within-hospital arm contrast.

Repeated landmarks are not independent. The primary uncertainty unit is `patientunitstayid`, resampling all retained landmarks of a stay together within hospital strata. A sensitivity resamples by `uniquepid`. Use fixed seed `61061`, target 1,000 complete-pipeline stay-cluster bootstrap replicates, and report attempted, successful, failed, and failure reasons before interpreting intervals. If fewer than 500 valid refits are possible, mark uncertainty and the corresponding gate inconclusive rather than silently using a row bootstrap. A fixed 1st/99th percentile truncation is used only for the inverse-observation-weight sensitivity; weights use pre-D variables, hospital, and landmark only.

For label permutations, permute labels within hospital-by-landmark strata only where both arms are present, preserving arm counts and all other rows. Run 1,000 permutations when at least 20 valid strata exist; otherwise report the exact valid-stratum count and mark the permutation gate unavailable/inconclusive. Never relabel single-arm strata artificially.

## Falsification and robustness tests

Run the same frozen parser and thresholds without outcome-guided changes for:

1. **Pre-D placebo:** compare `P` versus `B` using the same separated observations, medians, safety rule, and airway-corroboration sensitivity. A comparable label contrast before D is adverse to a newly emerging post-label interpretation.
2. **Lead-time placebo:** shift the exposure reference to `D-720` while retaining the fixed D-relative post window. Similar held-out gains indicate pre-existing trajectory or timing leakage.
3. **Component ablations:** remove PEEP, pressure support, set rate, safety SpO2, and safety respiration individually; report FiO2 separately. A result dependent on one ambiguous component is not supportive.
4. **Source ablations:** remove respiratoryCare corroboration, then restrict to respiratoryCharting plus vitalPeriodic; compare primary and sensitivity estimands without changing the primary definition.
5. **Documentation negative control:** predict post-window row density, unique times, and entry lag from pre-D opportunity and label. A label effect on documentation without a corresponding value-based trajectory gain supports ascertainment rather than respiratory-state information.
6. **Copy-persistence check:** repeat with a 60-minute minimum separation and a prespecified first/last summary sensitivity. Large instability is evidence of chart persistence or measurement artifact.
7. **Airway recency:** repeat only the inherited 6-, 12-, and 24-hour pre-L invasive-evidence variants, reporting attrition and support; do not tune the variant after outcome inspection.
8. **Permutation null:** compare the observed held-out increment to the valid within-hospital-by-landmark null, with unavailable status when strata are insufficient.

## Mechanical interpretation gates

These gates describe computational evidence, not clinical truth.

### Supportive

The result may be called computationally supportive of incremental label information only if the primary endpoint and at least two prespecified airway-recency variants have adequate support; at least five hospitals satisfy the complete endpoint/arm rule; the evaluation-minus-no-trial risk difference is positive with at least four of five estimable hospital directions positive; `state_plus_label` improves both micro and equal-hospital macro held-out log loss over identical `state_only` by at least 0.01 with a stay-cluster 95% interval excluding zero in the favorable direction; the increment survives component/source ablations, pre-D and lead-time placebos, and the valid permutation null; missingness/competing-exit differences do not account for the value-based gain; and airway corroboration is present in at least 10% of rows in each arm for the corroboration sensitivity. Failure of corroboration coverage prevents a fully supportive conclusion, even if the chart-only endpoint appears positive.

Even all supportive gates establish only reproducible incremental predictive information in this structured eICU chart construct. They do not establish bedside intent, delivered settings, SBT, extubation, readiness, benefit, harm, quality, or causality.

### Adverse

With adequate endpoint support, evidence is adverse to label fitness for this endpoint if the label increment is no better than opportunity/state alone; the risk difference or held-out increment reverses across hospitals; the observed increment is comparable to the pre-D or lead-time placebo or lies within the valid permutation null; it disappears after a component/source ablation; or the label predicts documentation density without improving the value-based trajectory. This means the exact labels are not validated as incremental features for this endpoint in this snapshot. It does not prove absent bedside evaluation or a documentation artifact.

### Inconclusive

The result is inconclusive if parent artifacts or source hashes cannot be verified; fewer than five hospitals have the required endpoint support; no held-out arm contrast is defined; endpoint support, corroboration, or valid permutation strata are too sparse; missingness/competing exits differ so strongly that state and ascertainment cannot be separated; uncertainty spans both a meaningful increment and zero; or bounded endpoint definitions disagree materially. Do not relax thresholds, select a new endpoint after seeing counts, collapse competing exits into missingness, use a row bootstrap, or expand labels post hoc.

## Required machine-readable outputs

Compilation must produce, in the writable workspace:

- `source_manifest.json`: snapshot, catalog hash, all source paths/hashes, archive-member convention, schema paths/hashes, headers, and read-only checks;
- `lineage_manifest.json`: parent artifact resolution, expected/actual hashes, recipe version, row digests, identity checks, exact counts, and fatal-stop status;
- `filter_counts.json`: full-source counts, required-column counts, every inherited filter count, unique stays/persons/hospitals, landmark and arm counts, contradiction counts, and all endpoint attrition reasons;
- `frozen_population_verified.csv` and `exposure_verified.csv`: canonical copied/reconstructed rows with identity, `D`, label, digest, and validation flags;
- `parser_dictionary.json` and `respchart_label_audit.csv`: parser version, exact matched sets, every encountered label, parse/rejection counts, bounds, and unit-ambiguity flags;
- `trajectory_rows.parquet` or CSV: one row per frozen person-landmark with identity, L, D, arm, hospital, component medians/counts/times, pre-D opportunity, endpoint state, exit type, and missingness reasons;
- `site_support.csv`: hospital/landmark arm counts, complete endpoint counts, four-state counts, concentration, and fold estimability;
- `leakage_audit.json`: predictor timestamp maxima, entry-time checks, violations, and stop status;
- `heldout_metrics.json`: fold metrics, aggregate micro/macro metrics, risk differences, calibration, train/test row and stay counts, and unavailable reasons;
- `bootstrap_summary.json` and `permutation_summary.json`: seed, cluster unit, attempted/successful replicates, valid strata, fitting procedure, intervals, failures, and artifact hashes;
- `gate_decision.json`: numeric inputs and mechanically derived supportive/adverse/inconclusive decisions, including every unmet condition;
- `verification.json`: hashes of every derived artifact, one-to-one joins, duplicate checks, exact boundary arithmetic, parser decisions, endpoint-state arithmetic, no-post-D baseline proof, split isolation, cluster unit, and gate-to-output linkage.

The verifier can check source and parent hashes, schema and column availability, exact joins, row counts, labels, D, exclusion flags, parser bounds, interval boundaries, observation spacing, medians, endpoint states, competing exits, missingness, leakage, held-out splits, clustering, permutation strata, and whether written conclusions follow the gate outputs. It cannot determine whether a charted value was delivered at the bedside, whether a label expressed SBT intent, whether extubation occurred, or whether a patient benefited. Those claims require device-linked measurements, local interface/workflow metadata, complete notes, blinded clinician adjudication, validated extubation/reintubation outcomes, and external or prospective validation.

No cohort result, endpoint estimate, model result, or clinical conclusion is fabricated by this proposal. If deterministic lineage reconstruction fails, the executable must publish the failure as feasibility/inconclusive and stop before outcome reads.
