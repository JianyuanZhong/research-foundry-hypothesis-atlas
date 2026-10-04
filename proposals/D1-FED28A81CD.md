> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Compiler-ready source reconstruction and endpoint computation for the frozen eICU respiratory-label experiment

## Status and substantive change

This is a targeted successor of assessed-valid `[prior hypothesis]` and `[prior hypothesis]`. It preserves the Lead-frozen scientific schema exactly:

- 540 person-landmark rows, 443 distinct first qualifying ICU stays/persons, and 74 hospitals;
- the first qualifying ICU stay per `uniquepid`, with all eligible landmarks retained within that stay;
- landmarks `L ∈ {1440, 2880, 4320, 5760, 7200}` minutes after unit admission;
- the two literal labels, first-label rule, and decision time `D`;
- every inherited pre-landmark invasive, physiologic, end-of-life, spontaneous-marker, adult, discharge, and other exclusion;
- the fixed post-D endpoint windows, raw thresholds, observation rules, competing-exit precedence, descriptive noncausal estimand, and hospital-held-out analysis;
- the distinction between computable structured-chart information and unavailable bedside intent, delivered settings, SBT/extubation, benefit, harm, quality, or causality.

The substantive repair is executable lineage reconstruction rather than another endpoint redesign. Earlier branches repeatedly lacked byte-identical parent row artifacts and therefore could not complete endpoint computation. This version requires a deterministic reconstruction from the current read-only eICU files, an outcome-blind source-wide label/parser freeze, a canonical row-by-row digest, and a hard pre-outcome gate. If the reconstruction does not exactly reproduce the frozen 540-row population and action rows, the run stops before any post-D endpoint extraction and reports feasibility/inconclusive; it must not silently substitute a near-match cohort. If reconstruction passes, the same executable continues through endpoint computation, observation/exit accounting, hospital-held-out analysis, and mechanically derived gates.

No computed result is claimed in this proposal. The current invocation workspace contains the source catalog and schemas but not the byte-identical frozen row artifacts; the executable must either materialize them from the supplied parent support or prove exact source reconstruction before reporting any endpoint association.

## Clinical question and evidence boundary

The clinically consequential question is whether the exact eICU care-plan labels

- `Ventilated - with daily extubation evaluation`, and
- `Ventilated - with no daily extubation trial`

contain reproducible information about a later persistent respiratory patient-state trajectory beyond structured patient state and documentation opportunity already visible before the label. Such information could determine whether these fields are defensible as a multicenter cohort feature or exploratory decision-support signal, rather than being pooled as if they had common meaning.

The strongest claim already supported by the parent lineage is limited to this snapshot's exported structured documentation: label use is sparse and hospital-concentrated; earlier label-to-setting mappings are peak-pressure dominated and unstable when peak pressure is removed; sedation mappings and some landmark/leave-one-hospital-out directions reverse; and independent durable-liberation ascertainment is too sparse to validate the construct. Those findings do not establish what clinicians intended or did at the bedside.

The untested claim is narrower: conditional on the frozen labelled person-landmarks, the `evaluation` label has a reproducible positive association with a persistent, safety-preserving, non-peak respiratory support de-escalation endpoint, and adding the label improves prediction in hospitals held out from model fitting relative to the identical pre-D state/opportunity model without the label.

This is a descriptive conditional association and predictive-increment estimand. It is not a treatment effect. No exchangeability, positivity, consistency, bedside semantic, or causal assumption is asserted. A positive result supports only incremental information in this structured-chart construct. It cannot establish daily evaluation, SBT delivery, extubation readiness, delivered ventilator settings, liberation, benefit, harm, quality, appropriateness, or general transportability.

## Read-only data and exact bindings

Dataset guide: `[internal dataset path]`.

EICU guide: `[internal dataset path]`.

Snapshot is `[source checksum]`; catalog SHA-256 is `[source checksum]`. All source files are gzip CSVs with archive member convention `ordinary file` and must be opened read-only. Source paths and hashes used by reconstruction are:

1. `[internal dataset path]`, [source checksum], table `patient`, schema `[internal dataset path]`, schema [source checksum]. Required columns include `patientunitstayid`, `uniquepid`, `hospitalid`, `unitvisitnumber`, `age`, `unitadmit...`, `unitdischargeoffset`, `unitdischargestatus`, and `unitdischargelocation`.
2. `[internal dataset path]`, [source checksum], table `carePlanGeneral`, schema `[internal dataset path]`, schema [source checksum]. Required columns `cplgeneralid`, `patientunitstayid`, `activeupondischarge`, `cplitemoffset`, `cplgroup`, `cplitemvalue`.
3. `[internal dataset path]`, [source checksum], table `carePlanEOL`, schema `[internal dataset path]`, schema must expose `patientunitstayid`, `cpleolsaveoffset`, `cpleoldiscussionoffset`, and `activeupondischarge`.
4. `[internal dataset path]`, [source checksum], table `respiratoryCare`, schema `[internal dataset path]`, schema [source checksum]. Required fields include `respcarestatusoffset`, `airwaytype`, `airwayposition`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, and `priorventendoffset`.
5. `[internal dataset path]`, [source checksum], table `respiratoryCharting`, schema `[internal dataset path]`, schema [source checksum]. Required fields `respchartid`, `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`.
6. `[internal dataset path]`, [source checksum], table `vitalPeriodic`, schema `[internal dataset path]`, schema [source checksum]. Required fields `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `sao2`, `respiration`.
7. `[internal dataset path]`, [source checksum], table `treatment`, schema `[internal dataset path]`, schema [source checksum]. Required fields `treatmentid`, `patientunitstayid`, `treatmentoffset`, `treatmentstring`, `activeupondischarge`.

The source guide states offsets are minutes from ICU admission; `vitalPeriodic` is a five-minute summary of monitor observations; narrative note sections are removed; no device logs, raw waveforms, local interface dictionaries, SBT checklists, adjudicated extubation/reintubation outcomes, or post-ICU follow-up are available. `respchartentryoffset` is a documentation-entry lag and never replaces clinical `respchartoffset`.

## Frozen reconstruction contract

### Parent artifact contract

The frozen cohort artifact must be obtained from the assigned parent support if available:

- `eicu_strict_cohort.csv`, expected [source checksum];
- frozen action rows, expected [source checksum].

The action artifact must contain one row per `sid,landmark`, exact `strategy` (`evaluation` or `no_trial`), and `D`/`decision_offset` with equality. If either artifact can be copied into the workspace, copy bytes without normalization, verify the expected hash, and use it only as a positive-control identity target. Never edit it.

### Source reconstruction

The executable must independently scan current read-only source files and reconstruct candidate rows before reading any post-D respiratory endpoint values. It must use a streaming CSV parser, preserve source strings for audit, and write only derived files in the workspace. The reconstruction stages are:

1. Read `patient` and form the stay table keyed uniquely by `patientunitstayid`. Fail if the stay key is duplicated, required offsets cannot be parsed as finite numbers, or a stay has conflicting `uniquepid`, `hospitalid`, `unitvisitnumber`, or discharge fields. Apply the inherited adult and first-qualifying-stay-per-`uniquepid` rules exactly as represented in the parent algorithm; do not infer a new clinical eligibility rule.
2. Full-scan `carePlanGeneral` and retain every row whose exact, case-sensitive `cplitemvalue` equals one of the two literal labels. Do not trim, broaden, stem, regex-match, or case-fold these exposure strings. For each retained stay and each fixed landmark, identify the first qualifying target row in the closed interval `[L,L+360]`. Preserve all candidate times and IDs in the audit. Exclude a landmark if the first qualifying target labels are contradictory at the same `cplitemoffset`, as in the frozen parent algorithm; do not resolve a tie by source order.
3. Reapply every inherited target-independent eligibility filter using data no later than `L`: first qualifying stay, adult criterion, landmark continuation/discharge criterion, pre-L invasive-airway evidence, strict pre-L physiology screen, absence of prior end-of-life discussion, absence of a prior 24-hour `Spontaneous - adequate` marker, and all other parent exclusions. The exact filter implementation must be imported from or byte-compared against the parent support before execution. If its source is unavailable, fail closed rather than reinterpreting a filter.
4. Classify the retained target row after eligibility. Set `D = cplitemoffset`, `strategy = evaluation` only for the daily-evaluation literal and `strategy = no_trial` only for the no-trial literal. No post-D row may affect eligibility, label classification, or the frozen population.
5. Enforce the exact expected identity: 540 rows; 443 distinct `sid`/`patientunitstayid` values and first qualifying stays/persons as defined by the parent; 74 distinct hospitals; landmark counts and arm totals equal the parent artifact; unique `(sid, landmark)`; no duplicate source IDs; exact `D` equality; and one-to-one merge with the action artifact on `sid, uniquepid, hospitalid, landmark, strategy`.

If source reconstruction differs in any row, field, label, D, filter status, or ordering after canonical sorting, do not repair it by dropping rows, changing parsing, or selecting a more convenient parent. Emit mismatch diagnostics and stop before outcome reads.

### Canonical row-level digest

The compiler must make identity auditable at row level, not only by a final file hash. For every reconstructed and parent row, create a canonical record with ordered fields:

`sid, patientunitstayid, uniquepid, hospitalid, unitvisitnumber, landmark, strategy, label, decision_offset, D`.

Canonicalization is fixed before comparison: UTF-8; LF line endings; column order exactly as above; integer-valued finite offsets rendered as base-10 integers; non-integer finite offsets rendered with 17 significant decimal digits; strings preserved exactly; missing values represented by `\\N`; no surrounding whitespace normalization; each row terminated by one LF. Sort by `(sid, landmark)` and compute:

- `row_sha256 = SHA256(canonical_row_bytes)` for each row;
- `cohort_rows_sha256 = SHA256(concatenation of sorted canonical row bytes)`;
- `cohort_file_sha256 = SHA256(exact copied parent bytes)` when the parent artifact exists;
- a mismatch list keyed by `(sid, landmark)` reporting missing, extra, and field-level differences.

Write `reconstruction_digest.json` with source hashes, parent hashes, canonicalization version, row count, unique-key count, sorted row hashes, aggregate row digest, and pass/fail. The expected parent file hash is not treated as a substitute for row-level comparison. A source reconstruction is accepted only when the canonical reconstructed rows equal the canonical parent rows exactly and the raw parent bytes separately match their expected SHA-256. If the parent artifact cannot be acquired, the run may write a source-derived digest for diagnosis but must classify lineage as `inconclusive_artifact_unavailable` and must not compute or report an endpoint association.

## Outcome-blind parser and endpoint freeze

The parser manifest must be created from a full source-wide scan before joining labels or calculating arm-specific counts. It must enumerate every distinct `respchartvaluelabel` exactly as observed, its normalized form, matched family, unmatched status, parseable-value count, malformed/sentinel count, and value examples represented only as bounded audit categories where needed. The manifest is immutable once any arm-specific endpoint extraction begins.

Normalize labels for family matching only by Unicode-safe whitespace collapse and case folding; preserve raw labels and never apply this normalization to the two exposure strings. The family map must be explicit and versioned for:

- FiO2;
- PEEP and PEEP-CPAP;
- pressure support;
- set respiratory rate;
- peak inspiratory pressure (secondary ablation only).

For numeric fields, trim the value representation only for parsing, accept finite full-token numeric values, reject trailing nonnumeric text, empty values, sentinels, and out-of-bound values, and record each reason. Use fixed physiologic bounds from the parent/parser manifest, written before looking at arm contrasts; do not invent unit conversion. FiO2 unit ambiguity is retained as missing unless the frozen manifest establishes an unambiguous eICU representation. The parser must fail if a claimed family has no reproducible source-wide mapping or if a later code path changes the manifest.

Repeated observations within a component-window require at least two valid records at distinct `respchartoffset` values separated by at least 30 minutes. The window statistic is the median of all valid observations. Record count, distinct times, first/last time, median, maximum gap, and parse/missing reasons. Same-time conflicts are retained in a conflict count and resolved only by the pre-frozen deterministic rule; never use file order. Clinical time is `respchartoffset`, not `respchartentryoffset`.

## Primary endpoint and competing exits

For every frozen person-landmark row define:

- `B = (D-720, D]` baseline state window;
- `P = (D-1440, D-720]` versus `B` pre-D placebo trajectory;
- `O = (D+360, D+1800]` primary post-label endpoint window;
- `O12 = (D+360, D+1080]` declared horizon sensitivity.

Support de-escalation is at least one baseline-to-O median reduction of FiO2 by `0.05`, PEEP/PEEP-CPAP by `2 cm H2O`, pressure support by `2 cm H2O`, or set respiratory rate by `2 breaths/min`. Peak inspiratory pressure is excluded from the primary and used only in an ablation.

Safety uses `vitalPeriodic.sao2` and `vitalPeriodic.respiration`, with the same two-observation and 30-minute separation rule and medians. Among signals observed in both B and O, safety passes if median SaO2 does not fall by more than 2 percentage points and median respiration does not rise by more than 4 breaths/min. If a signal is absent from both windows, it is unavailable rather than safe. Prespecified sensitivities require both safety signals, or require at least one.

Airway corroboration requires at least one O-time `respiratoryCare` row with a nonmissing `airwaytype` or a nonmissing ventilator interval among `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, and `priorventendoffset`. It is a source-availability criterion, not proof of delivered device state.

Assign mutually exclusive statuses in this precedence order:

1. `competing_exit` if death, discharge/transfer, or truncation occurs before the end of O; report exit type from `unitdischargestatus` and `unitdischargelocation`. Also flag no post-washout opportunity when `unitdischargeoffset <= D+360`.
2. `endpoint_missing` if no competing exit occurs but minimum repeated observations, safety availability, or required source evidence fails.
3. `persistent_improvement` if complete support, safety, and airway criteria pass.
4. `observed_non_improvement` if complete criteria are available but persistent improvement is false, including support reduction with safety failure.

The primary arm contrast is evaluation minus no-trial risk difference for persistent improvement among complete, non-competing endpoint observations. It must always be accompanied by the all-row four-state distribution, observation/exit rates, and arm-specific denominators. A secondary all-row multinomial model treats the states explicitly; no endpoint is imputed from discharge, missingness, or a care-plan string. A fixed pre-D-only inverse-observation-weighted binary sensitivity may be reported, but cannot replace the complete-observation primary or conceal positivity failure.

RespiratoryCare and treatment airway transitions are validation sensitivities only. The latter uses a frozen exact normalized ETT-removal candidate followed by no invasive-airway respiratoryCare record for 48 hours, or an exact time-ordered `airwaytype` change to `No Artificial Airway`; it is unavailable/inconclusive if fewer than 10% of rows in either arm support it. No durable-liberation association is authorized because the inherited independent-marker audit failed its ascertainment gate.

## Pre-D predictors, documentation opportunity, and leakage controls

The baseline feature table uses only data available at or before D, excluding care-plan values beyond exposure time and all post-D values. Features include fixed summaries of pre-D respiratory state and trend, pre-D `respiratoryCharting` source presence/counts/distinct clinical times/component-label counts, `respiratoryCare` source presence/counts/distinct airway types, pre-D vital observations, treatment source counts, and entry-minus-clinical lag summaries. The label is added only in the state-plus-label model.

The opportunity-only model uses pre-D counts, timestamp density, source presence, and entry lag without respiratory values, labels, or care-plan variables. The state-plus-opportunity model includes pre-D respiratory values and opportunity. The state-only model omits the label and may be reported as a secondary baseline. A post-D opportunity model is diagnostic only and cannot be interpreted as the primary information estimand.

A machine-checkable leakage audit must prove that no post-D respiratory value, post-D source count, endpoint status, treatment string, label count, or outcome-derived quantity occurs in baseline columns. Hospital and landmark may be strata or ordinary covariates in training, but held-out hospital outcomes and target rates cannot enter preprocessing, imputation, calibration, or weights.

## Hospital-held-out analysis and uncertainty

The primary transport estimand is leave-one-hospital-out prediction of the endpoint states. For each held-out hospital, fit preprocessing, imputation, standardization, regularization, calibration, and any observation weights using training hospitals only. Report fold-level and aggregate row-weighted micro log loss, Brier score, calibration slope/intercept, equal-hospital macro log loss/Brier, AUROC only when both classes occur, four-state metrics, observed and predicted evaluation-minus-no-trial contrasts, and support/exit/missingness counts.

The label-added comparison is state-plus-label versus the identical state-plus-opportunity model without label. A gain caused only by predicting documentation or missingness is not a value-based gain. A within-hospital arm contrast is not estimated for a fold lacking both arms with adequate complete endpoints; no artificial relabeling or pooled-row rescue is allowed.

Before fitting, publish per-hospital support with label counts, complete endpoint counts, four-state counts, competing exits, missingness, and arm concentration. The primary label-contrast transport gate requires at least five hospitals with at least 10 complete endpoint-observed rows under each label and at least 50% of complete rows in those hospitals. If fewer than five meet it, label-contrast transport is inconclusive even if broad prediction metrics are computable.

Use stay-cluster bootstrap, not row bootstrap, preserving all landmarks of resampled `sid` clusters within hospital strata. Use fixed seed `61061`, 1,000 refitted replicates if feasible or at least 500 with the shortfall declared before result inspection. A sensitivity permutes labels within hospital-by-landmark strata only where both arms occur, preserving counts and all outcome/opportunity rows. Run 1,000 permutations if at least 20 valid strata exist; otherwise report the exact valid count and mark permutation unavailable/inconclusive.

## Falsification and sensitivity tests

1. Recompute the pre-D placebo trajectory using the same thresholds and repeated-observation rules. A comparable pre-D contrast is adverse to a newly emerging post-label interpretation.
2. Shift the exposure reference to `D-720` while retaining the O window relative to D. Similar held-out gain indicates timing leakage or pre-existing trajectory.
3. Ablate each support and safety component, and separately airway corroboration. Survival only through peak pressure, one field, one source family, or one hospital is not supportive.
4. Predict post-window source density, unique times, and entry lag from the label and pre-D features. Opportunity gain without value trajectory gain supports documentation opportunity rather than patient-state information.
5. Use the valid within-hospital-by-landmark permutation distribution when enough strata exist; do not interpret its absence as support.
6. Repeat fixed pre-L invasive-airway recency variants of 24, 12, and 6 hours only if their parent algorithms/artifacts are available, reporting all attrition. A changed denominator is a declared sensitivity, not tuning.
7. Compare complete-window and fixed, pre-D-only observation-weighted results. Extreme weights, positivity failure, or arm-specific competing exits make the result inconclusive.
8. Repeat with 60-minute observation separation and first/last summaries as declared artifact-sensitivity diagnostics. A large change indicates copied-chart or persistence sensitivity.
9. Audit disjoint windows and boundary inclusion mechanically, including equality at every open/closed endpoint.

## Prespecified interpretation gates

These are semantic-transportability and computational-feasibility gates, not significance tests.

### Supportive

A result is computationally supportive of incremental label information only if the source and parent lineage gates pass; at least five hospitals meet complete-endpoint support with at least 50% of complete rows there and no arm is over 40% concentrated in one hospital; at least four of five estimable hospital contrasts are positive; state-plus-label improves both micro and equal-hospital macro held-out log loss over state-plus-opportunity by at least 0.01 with a stay-cluster interval excluding zero; the gain survives pre-D and lead-time placebos, component/source ablations, valid permutation, and leave-one-hospital-out reversal checks; missingness/competing exits do not explain it; and airway corroboration is present in at least 10% of both arms. Even this supports only structured-chart predictive information, never bedside or causal claims.

### Adverse

With adequate endpoint support, the patient-state-information claim is computationally adverse if the label increment is no better than the identical state/opportunity baseline, reverses across hospitals, is no larger than a placebo or permutation null, disappears after a component/source ablation, or predicts documentation density without a value-based trajectory gain. Adverse means not validated as an incremental feature for this endpoint in this snapshot. It does not prove absence of evaluation or prove a local documentation convention.

### Inconclusive / fail-closed

The result is inconclusive if either parent artifact cannot be verified, source hashes or schemas fail, canonical row identity differs, inherited filters cannot be reproduced, fewer than five hospitals support complete contrasts, no held-out arm contrast exists, endpoint or airway evidence is sparse, competing exits/observation positivity fail, parser mapping is ambiguous, sensitivities disagree materially, or execution cannot complete. No relaxed threshold, outcome-guided endpoint, post-hoc label expansion, endpoint imputation, pooled row bootstrap, or reconstructed near-match cohort is allowed.

## Required machine-readable outputs

The executable must write these derived workspace artifacts:

- `source_manifest.json`: all seven source paths, expected and observed hashes, schema paths/hashes, headers, snapshot/catalog IDs, archive member convention, and read-only checks;
- `filter_counts.json`: full source row counts, required-column checks, counts after every inherited filter, candidate labels, contradiction exclusions, each landmark/arm/stay/person/hospital count, and endpoint attrition reasons;
- `reconstruction_digest.json`: canonicalization version, row-level hashes, aggregate row digest, parent file digest, mismatch diagnostics, and lineage gate;
- `frozen_population_verified.csv` and `exposure_verified.csv`: source-reconstructed rows and byte-copied parent rows with identity checks, never mutating source files;
- `parser_manifest.json`: full source-wide respiratory label inventory, exact family map, numeric bounds, sentinel/malformed counts, and immutable parser hash;
- `trajectory_rows.parquet` or CSV: one row per frozen person-landmark with D, arm, hospital, landmark, all component medians/counts/times, opportunity fields, endpoint status, competing exit, and missingness reason;
- `site_support.csv`: per-hospital/per-landmark label, complete-endpoint, four-state, exit, missingness, concentration, and held-out estimability counts;
- `heldout_metrics.json`: fold-specific and aggregate metrics, contrasts, calibration, support, training/test row and stay counts, and unavailable metrics with reasons;
- `bootstrap_summary.json` and `permutation_summary.json`: seed, cluster unit, replicate count, valid/failure counts, intervals, valid strata, and artifact hashes;
- `verification.json`: source/schema/parent hashes, row identity, duplicate checks, parser/window/boundary audit, no-leakage audit, fitting isolation, bootstrap/permutation checks, and gate decisions computed from numeric outputs.

The compiler should execute a lightweight preflight first that verifies all seven source hashes, schema columns, parent artifact availability, and source-wide label inventory. It should not extract post-D endpoint rows until `reconstruction_digest.json` has a passing lineage status. A failed preflight is useful evidence about feasibility and must be published as such, without fabricated scientific results.

## What is and is not computably verifiable

The verifier can check source and schema hashes, ordinary gzip access, required headers, parent bytes, canonical row identity, 540/443/74 counts, exact labels and D, all window arithmetic, parser immutability, numeric bounds, repeated-observation separation, medians, endpoint-state precedence, exit accounting, absence of post-D baseline features, hospital-held-out fit isolation, cluster resampling, permutation strata, and whether the reported conclusion follows the numeric gates.

It cannot establish that a care-plan label expresses clinician intent, that respiratoryCharting values were delivered settings rather than charted observations, that `airwaytype` proves a device state, that an SBT or extubation occurred, that liberation was durable, that care was appropriate, that a label improves outcomes, or that the result transports outside this selected snapshot. Those claims require device-linked data, local workflow/interface dictionaries, complete narrative/context, blinded clinician adjudication, validated extubation/reintubation outcomes, follow-up, and another study.

## Current feasibility status and unresolved uncertainties

I inspected the current dataset guide, complete eICU metadata, exact source headers and relevant schemas, the research-ambition availability limitations, and both assigned assessed-valid parent proposals. The present workspace does not contain `eicu_strict_cohort.csv` or the frozen action-row artifact, so I did not fabricate a 540-row reconstruction, endpoint computation, or association estimate. The proposed executable must obtain the parent bytes through candidate support or reconstruct and compare them exactly from the current read-only source files using the parent filter implementation. If the byte identity or inherited algorithm cannot be established, the correct result is `inconclusive_artifact_unavailable` before outcome extraction.

The key remaining uncertainty is not a new scientific schema: it is whether the frozen lineage can be recovered byte-identically and whether the persistent, independently charted endpoint has enough noncompeting, repeatedly observed support to permit the predeclared held-out estimand. Even a successful computation remains bounded to structured documentation and cannot resolve bedside semantics, intent, benefit, harm, quality, or causality.
