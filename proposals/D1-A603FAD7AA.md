> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Compiler-ready repair: deterministic eICU respiratory trajectory experiment

## Scope and preserved estimand

This targeted child preserves the assigned endpoint-validity estimand and does not reopen the settled vocabulary or transportability findings. The frozen target population remains 540 person-landmarks, 443 ICU stays, 74 hospitals; the first qualifying stay per `uniquepid`, the five landmarks `L ∈ {1440,2880,4320,5760,7200}`, exact labels, label timing, and all inherited exclusions remain fixed. The exposure is still the first exact target label in `[L,L+360]`, with `D = cplitemoffset`; the comparison is:

- `evaluation`: `Ventilated - with daily extubation evaluation`
- `no_trial`: `Ventilated - with no daily extubation trial`

The estimand remains the descriptive, hospital-held-out association and predictive increment of label receipt for a later persistent, independently charted respiratory-state improvement, conditional on strictly pre-D patient state and documentation opportunity. It is not a treatment effect and does not claim SBT, extubation readiness, liberation, benefit, harm, or causality.

The substantive repair is execution-level but scientifically important: it removes ambiguous endpoint/parser and stale-artifact failure modes, retains competing exits instead of silently excluding them, and makes every lineage and leakage decision fail closed.

## Source snapshot, exact bindings, and archive convention

All raw files are read-only, from eICU 2.0 snapshot `[source checksum]`, catalog [source checksum]. Every listed `.csv.gz` is an ordinary file archive member (not a nested member). The source root is `[internal dataset path]`.

Required raw bindings are:

| table | exact source and SHA-256 | schema JSON | required columns and use |
|---|---|---|---|
| `patient` | `patient.csv.gz`, `[source checksum]` | `[internal dataset path]` | `patientunitstayid`, `uniquepid`, `hospitalid`, `unitvisitnumber`, `age`, `unitdischargeoffset`, `unitdischargestatus`, `unitdischargelocation`; identity, first-stay, age, hospital and exit checks |
| `carePlanGeneral` | `carePlanGeneral.csv.gz`, `[source checksum]` | `[internal dataset path]` | `cplgeneralid`, `patientunitstayid`, `cplitemoffset`, `cplgroup`, `cplitemvalue`, `activeupondischarge`; exact exposure, D, contradictory-label and inherited `Spontaneous - adequate` predicates |
| `carePlanEOL` | `carePlanEOL.csv.gz`, `[source checksum]` | `[internal dataset path]` | `cpleolid`, `patientunitstayid`, `cpleolsaveoffset`, `cpleoldiscussionoffset`, `activeupondischarge`; exact inherited prior-end-of-life exclusion, with offset semantics frozen by parent recipe |
| `respiratoryCare` | `respiratoryCare.csv.gz`, `[source checksum]` | `[internal dataset path]` | `respcareid`, `patientunitstayid`, `respcarestatusoffset`, `airwaytype`, `airwaysize`, `airwayposition`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`; pre-L invasive screen and post-window corroboration/continuity |
| `respiratoryCharting` | `respiratoryCharting.csv.gz`, `[source checksum]` | `[internal dataset path]` | `respchartid`, `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`; numeric state values, clinical time, and documentation lag |
| `vitalPeriodic` | `vitalPeriodic.csv.gz`, `[source checksum]` | `[internal dataset path]` | `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `sao2`, `respiration`; safety domain (catalog says five-minute summary, not raw waveform) |
| `vitalAperiodic` | `vitalAperiodic.csv.gz`, `[source checksum]` | `[internal dataset path]` | `vitalaperiodicid`, `patientunitstayid`, `observationoffset`, `noninvasivemean`; optional pre-D hemodynamic sensitivity only |
| `treatment` | `treatment.csv.gz`, `[source checksum]` | `[internal dataset path]` | `treatmentid`, `patientunitstayid`, `treatmentoffset`, `treatmentstring`, `activeupondischarge`; secondary airway-transition sensitivity only, never primary exposure/outcome |
| `apacheApsVar` | `apacheApsVar.csv.gz`, `[source checksum]` | `[internal dataset path]` | `apacheapsvarid`, `patientunitstayid`, and the parent-specified physiologic-screen fields; only to reproduce the frozen inherited screen, not to redefine it |

Schema JSONs confirm table names, columns, identity keys and temporal fields. Metadata relationships join each longitudinal table to `patient` on `patientunitstayid`; do not join on `uniquepid` or `patienthealthsystemstayid` for measurements. IDs such as `cplgeneralid`, `respchartid`, `respcareid`, `vitalperiodicid`, `vitalaperiodicid`, and `treatmentid` are retained for deterministic tie handling and row digests, but the catalog identifies `patientunitstayid` as the table identity rather than promising a composite clinical key.

## Lineage reconstruction and hard stops

The compiler must first verify the parent artifacts by content hash, not by the stale absolute workspace paths recorded by the parent. The expected frozen artifacts are `eicu_strict_cohort.csv` [source checksum] and the action-row artifact [source checksum]. If either is unavailable, reconstruct from the raw snapshot using the parent recipe and independently write a byte-stable replacement; do not estimate from an approximate reconstruction.

Accept a frozen artifact only if all checks pass: exact header and column types; one row per `(patientunitstayid, landmark)`; 540 rows; 443 distinct stays; 74 distinct hospitals; five allowed landmarks only; one first qualifying stay per `uniquepid`; exact arm strings; `D` equals the selected `cplitemoffset`; `L <= D <= L+360`; no duplicate or contradictory target rows under the parent rule; and every inherited exclusion flag and source-row digest agrees with the parent. Recompute a deterministic row digest after sorting by `(patientunitstayid, landmark, D, cplgeneralid)` and a deterministic artifact hash. Any mismatch in recipe version, counts, identities, labels, D, flags, or digest is a fatal lineage stop with no association estimate.

The compiler must retain a machine-readable manifest containing snapshot ID, catalog hash, all eight source hashes above plus the parent artifact hashes, schema JSON hashes, parser version, random seed, sort order, and actual row counts at every filter. Filtering is full-source and unsampled; only the final frozen cohort limits downstream joins.

## Parser and endpoint freeze before outcome inspection

Freeze a versioned parser and label dictionary before reading outcome summaries or fitting models. For `respiratoryCharting`, use `respchartoffset` as clinical time; `respchartentryoffset` is never used to place a measurement. Exact component label sets are:

- FiO2: `FiO2`, `FIO2 (%)`, `Set Fraction of Inspired Oxygen (FIO2)`
- PEEP: `PEEP`, `PEEP/CPAP`
- pressure support: `Pressure Support`, `PS above PEEP`
- set rate: `Vent Rate`, `VS RESP RATE`
- safety SpO2: only the `vitalPeriodic.sao2` numeric column
- safety respiration: only the `vitalPeriodic.respiration` numeric column

`Peak Insp. Pressure`, `Peak Pressure`, `Plateau Pressure`, `Peak Flow`, `Mean Airway Pressure`, `Pressure Control`, spontaneous/total rate labels, and oxygen-flow labels are excluded from the primary support component dictionary. They may be retained as diagnostics or prespecified ablations, but cannot enter the primary endpoint by substring matching. Matching is case-sensitive after trimming whitespace and does not normalize synonyms beyond this frozen list.

Numeric parsing is deterministic: trim outer whitespace; parse a signed decimal or scientific-notation token only if the entire value matches `^[+-]?(?:\\d+(?:\\.\\d*)?|\\.\\d+)(?:[eE][+-]?\\d+)?$`; reject blanks, embedded units, ranges, inequalities, and nonnumeric strings. Apply field bounds before aggregation: FiO2 in `[0,100]` when represented as percent, PEEP and pressure support in `[0,60]`, set rate in `[0,100]`, `sao2` in `[0,100]`, respiration in `[0,200]`. No fraction-to-percent conversion, unit conversion, interpolation, carry-forward, or device-semantic inference is permitted. The parser records label, raw value, parsed value, rejection reason, and parser version.

For each component and each interval, require at least two valid observations at distinct `respchartoffset` values separated by at least 30 minutes. Use the median of all valid observations in the interval, not first/last value. Pre-D state is built only from `(D-1440,D-720]` and `(D-720,D]`; the primary post period is `(D+360,D+1800]`. Values at a boundary follow these half-open intervals exactly. The six-hour gap is fixed. A persistent component reduction is a post median at least 0.05 lower for FiO2, 2 lower for PEEP or pressure support, or 2 lower for set rate than the corresponding pre-D median, and is supported only when the component has the required observations in both periods. No component is silently substituted for another.

The primary composite is a persistent support reduction in at least one non-peak component plus no adverse change in both available safety signals: post `sao2` is not more than 2 percentage points below pre-D median and post respiration is not more than 4 breaths/min above pre-D median. If either safety signal lacks the required observations in either period, the composite is endpoint-missing, not a non-event. `respiratoryCare` corroboration requires at least one post-window row with nonempty `airwaytype` or at least one nonmissing ventilator interval field; this is a chart corroboration flag, not proof of delivered support.

## Competing exits, truncation, and missingness

Do not impose `unitdischargeoffset > D+1800` as an eligibility exclusion. Retain every frozen cohort row. Define an administrative exit at the first `unitdischargeoffset` on or before `D+1800`; classify it using `unitdischargestatus` and `unitdischargelocation` as death when status is `Expired` (case-insensitive exact value after trimming), otherwise discharge/transfer, and call it truncation when the offset is nonmissing but the status/location cannot classify it. A row exiting before the end of the primary window is a competing exit and cannot be labeled improvement or ordinary observed non-event.

If no early exit occurs but the required measurements are absent, classify the primary endpoint as missing due to ascertainment. Report separate missingness reasons: no pre-D support, no post-D support, no pre/post safety, no respiratory-care corroboration, parser rejection, and any source absent. A setting-only secondary endpoint may omit corroboration but retains the same observation rules. Report counts and denominators for event, observed non-event, death, discharge/transfer, truncation, and missingness by arm, hospital, and landmark. Primary risk differences are estimated on the prespecified observed-endpoint estimand with competing exits displayed separately; a competing-risk sensitivity treats death and non-death exit as distinct events. No complete-case restriction may be introduced after seeing arm-specific outcomes.

## Leakage audit and analysis

Before fitting, assert that every predictor row has clinical timestamp `<= D`; `respchartentryoffset > D` is never allowed to rescue a pre-D measurement. Exclude care-plan values, care-plan counts, post-D observations, post-D treatment, post-D respiratory-care rows, and outcome-derived availability from baseline predictors. Produce a leakage audit with maximum predictor time, number of violations, offending table/column, and a fail-closed stop if any violation is nonzero. Post-D opportunity is an outcome/ascertainment diagnostic only.

The baseline model uses the same pre-D variables and pre-D opportunity counts; the label model adds only the binary exact arm. The opportunity-only model uses pre-D row counts, distinct labels, distinct measurement times, source presence, and pre-D entry-lag summaries, but no respiratory values or label semantics. Evaluate leave-one-hospital-out with row-weighted micro and equal-hospital macro log loss, Brier score, calibration slope/intercept, and risk difference; AUROC is reported only when defined. Repeated landmarks are clustered by `patientunitstayid` (and sensitivity-clustered by `uniquepid`); uncertainty uses stay-cluster bootstrap with a fixed seed, never row bootstrap. Inverse-observation weighting is a sensitivity, with weights estimated from pre-D variables, hospital and landmark only and truncated at the fixed 1st/99th percentiles.

## Falsification and interpretation gates

Run the same frozen parser and endpoint on the pre-D placebo `(D-1440,D-720]` versus `(D-720,D]`, and a lead-time placebo shifting exposure time to `D-720` while preserving the primary D-relative outcome window. Run leave-one-component-out ablations, source-family ablations, the documentation-density negative control, and 1,000 within hospital-by-landmark label permutations with fixed seed and preserved arm counts. No threshold or label map may be tuned using outcomes.

A result is **supportive** only if the primary unbounded endpoint and at least two airway-recency sensitivities meet the parent overlap requirement (at least five hospitals with at least ten endpoint-observed rows per arm and at least 50% of analyzed rows in those hospitals, with no hospital over 40% of either arm), evaluation-minus-no-trial risk difference is positive, at least four of five estimable hospital directions agree, equal-hospital held-out label-model log loss improves over baseline-plus-opportunity by at least 0.01 for both micro and macro measures with a favorable 95% stay-cluster interval excluding zero, and the increment survives component/source ablations, placebo checks, and the permutation null. Independent corroboration in fewer than 10% of rows in either arm makes the overall result not fully supportive.

It is **adverse** if the label increment is no better than opportunity-only, is comparable to the pre-D placebo or permutation null, reverses across hospitals/held-out folds, depends on one component/source/hospital, or predicts documentation density without improving the value-based endpoint. It is **inconclusive** if endpoint support or hospital overlap is too sparse, uncertainty spans both a clinically meaningful increment and zero, competing exits/missingness differ so strongly that the prespecified analyses cannot separate state from ascertainment, or bounded airway definitions disagree. These gates do not produce a clinical benefit claim.

A verifier can check hashes, lineage, exact joins, columns, offsets, parser decisions, windows, endpoint arithmetic, competing exits, leakage, held-out splits, clustering, permutation and gate logic. It cannot establish bedside intent, delivered ventilator settings, SBT performance, extubation or reintubation, or causal/clinical benefit. Those claims require clinician adjudication, local interface and workflow metadata, device-linked measurements, and external/prospective validation. No outcome result is claimed by this proposal.
