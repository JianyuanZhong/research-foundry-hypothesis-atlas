> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Dynamic fitness-for-use of carePlanGeneral Ventilation states

## Scientific question and clinical importance

Does a newly documented or changed structured Ventilation care-plan state identify a reproducible, hospital-transportable subsequent respiratory-support trajectory beyond the patient's prior respiratory state, prior care-plan history, hospital, and generic documentation opportunity? A positive answer would justify using longitudinal care-plan state as a cohorting or monitoring feature in multicenter retrospective research. A negative answer would prevent researchers from mistaking local documentation workflow for a common respiratory phenotype.

This is a fitness-for-use question about exported structured documentation. It is not a test of whether a bedside spontaneous breathing trial occurred, whether extubation was appropriate or successful, quality of care, clinical benefit or harm, or a causal effect of a care-plan label.

## What is already supported and what remains untested

The two authorized parents support the following bounded claims. The target-independent denominator can be frozen reproducibly; the full source contains eight normalized Ventilation values, including the two exact labels and three additional values beginning with `Ventilated -`. Static exact and broader receipt is sparse, broader receipt adds only a very small number of rows in bounded airway analyses, and hospital-held-out analyses do not establish a transportable improvement over generic documentation-process controls. The other parent shows substantial between-hospital heterogeneity in exact-label assignment and adverse/common-phenotype transportability diagnostics.

Those findings do not establish that a *new* state, a state transition, or persistence is uninformative. The falsifiable unresolved hypothesis is that temporally new receipt or a change among Ventilation states, assessed after a finite pre-landmark history and before an independently defined outcome window, carries incremental and transportable information about the next respiratory-support trajectory.

## Population and denominator freezing

Use the frozen, target-independent rows from the authorized vocabulary parent:

- input: `[internal dataset path]`
- [source checksum]
- inherited key: `sid`/`patientunitstayid`, `landmark`, and `hospitalid`
- inherited target-independent denominator: 4,798 unique stay-landmark keys, with four airway definitions (`exact_unbounded`, `exact_airway_24h`, `exact_airway_12h`, `exact_airway_6h`)

The denominator is frozen before dynamic state classification and before reading the outcome. A stay can contribute multiple fixed landmarks; no row-level random split is permitted. Analysis is restricted to rows with `complete_outcome_window == True` and nonmissing `robust_reduction`. This complete-follow-up restriction is applied after the denominator is frozen and does not use Ventilation receipt.

## Exact source bindings and extraction

Read the source read-only:

- `[internal dataset path]`
- [source checksum]
- ordinary unarchived CSV member
- table: `carePlanGeneral`
- columns used: `patientunitstayid`, `cplitemoffset`, `cplgroup`, `cplitemvalue`
- join key: `patientunitstayid` to frozen `sid`
- time field: `cplitemoffset`, in minutes from ICU admission

Normalize values by trimming/collapsing whitespace and case-folding. Restrict state classification to rows with normalized `cplgroup == ventilation`. The outcome-blind broad vocabulary is the literal set of all normalized full-source values beginning `ventilated -`, namely:

- `ventilated - with daily extubation evaluation`
- `ventilated - with no daily extubation trial`
- `ventilated - rapid wean/extubation`
- `ventilated - chronic dependency`

No value synonym or site-local token is added after examining outcomes.

For each frozen `(sid, landmark)`:

1. Prior history is the strict half-open interval `[max(0, landmark - 1440), landmark)`.
2. Current classification is the inclusive interval `[landmark, landmark + 360]`.
3. The prior state is the latest broad Ventilation value in the prior interval, ordered by `(cplitemoffset, normalized value)`.
4. The current state is the first broad Ventilation value in the current interval, ordered by `(cplitemoffset, normalized value)`.
5. If no current broad value exists, classify `no_current_broad`.
6. If a current broad value exists but no prior broad value exists in the finite history window, classify `incident_no_prior_broad`.
7. If both exist and the values match, classify `persistent_same`.
8. If both exist and differ, classify `transition_different`.

The deterministic ordering makes same-offset and multiple-row conflicts reproducible. These are documentation states, not physiologic states. The primary dynamic contrast is the four-level dynamic category; transition-flow counts are descriptive sensitivities, not separate confirmatory hypotheses.

The exact receipt indicator is presence of either exact value in `[landmark, landmark+360]`. The broader current indicator is presence of any broad value. The inherited exact receipt is reconstructed and checked against the parent `receipt` field before analysis; a mismatch is a validation failure.

## Outcome and temporal separation

The primary outcome is the inherited `robust_reduction` in the strict post-classification window:

`(landmark + 360, landmark + 1080]`.

It is one if any documented reduction occurs in a non-peak respiratory setting of at least 0.05 FiO2, 2 cm H2O PEEP, 2 cm H2O pressure support, or 2 breaths/min set ventilator rate, and zero otherwise. Peak inspiratory pressure is excluded. The outcome is retained only when the inherited outcome-window completeness indicator is true and the outcome is nonmissing. No outcome timestamp or variable is used to define the dynamic exposure window.

## Baselines and proposed estimand

The estimand is incremental out-of-hospital prediction, not a causal effect. For each eligible held-out hospital, estimate the change in held-out log loss (and secondarily Brier score, AUROC, and calibration) when adding dynamic state/history to:

1. the inherited patient-state baseline: `landmark`, `pre_chart_n`, `pre_distinct_labels`, `pre_robust_n`, `pre_fio2`, `pre_peep`, `pre_pressure_support`, and `pre_vent_rate`;
2. baseline plus generic care-plan opportunity controls: `cp_any`, `cp_log_rows`, `cp_distinct_groups`, `vent_any`, `vent_log_rows`, and `vent_distinct_values`;
3. process controls plus inherited exact receipt (`label3`/`receipt`, with the parent encoding); and
4. process controls plus dynamic category and prior/current broad state indicators.

Prior patient state and generic process controls are included so a dynamic label cannot win merely by marking a chart-rich landmark. The primary comparison is model 4 versus model 2, with model 3 as the static-label comparator. Hospital-held-out folds are fixed by hospital and selected using outcome availability and class support only, never dynamic receipt. Report row-weighted micro and equal-hospital macro metrics. Resampling, if the feasibility gate passes, samples stays within each hospital so all landmarks from one stay move together; every preprocessing step and model is refit within each resample and fold.

## Feasibility-first stopping rule

Before fitting the models, report rows, unique stays, hospitals, events, event rates, hospital counts, largest-hospital share, and the number of hospitals containing each state and both comparator states. Treat the finite 24-hour-history analysis as primary, with unbounded-history, 12-hour-history, and 6-hour-history variants as bounded sensitivity analyses.

Dynamic predictive modeling is permitted only if the primary incident and transition categories each have at least 20 rows, at least five hospitals, at least three hospitals with both outcome classes where applicable, and no single hospital contributes more than 75% of that category. At least five hospitals must remain eligible for hospital-held-out evaluation with both outcome classes. If the gate fails, do not fit an elaborate model; report the failure as a measurement/transportability result and retain the unbounded and airway-window counts as sensitivities.

## Observed feasibility result

The corrected strict 24-hour-history run scanned all 3,115,018 source rows, found 138,620 rows belonging to frozen stays, and classified 4,798 frozen keys. Among complete nonmissing-outcome rows:

- `exact_airway_24h`: 2,273 rows across 66 hospitals; incident 38 rows/38 stays/6 hospitals (7 events), persistent 23 rows/21 stays/3 hospitals (8 events), and transition 24 rows/24 stays/6 hospitals (10 events). Hospital 420 supplied 30/38 incident rows, 20/23 persistent rows, and 17/24 transition rows.
- `exact_airway_12h`: incident 28 rows/5 hospitals, persistent 21 rows/3 hospitals, and transition 18 rows/5 hospitals; hospital 420 supplied 22/28, 18/21, and 14/18 respectively.
- `exact_airway_6h`: incident 16 rows/4 hospitals, persistent 10 rows/3 hospitals, and transition 13 rows/5 hospitals; hospital 420 supplied 11/16, 7/10, and 9/13 respectively.
- The unbounded sensitivity had more apparent support but remained sparse: incident 52 rows/13 hospitals, persistent 23 rows/3 hospitals, and transition 26 rows/7 hospitals; hospital 420 supplied 35/52, 20/23, and 17/26 respectively.

Thus the primary bounded incident and transition states fail the required multisite support and concentration criteria; persistence is even more concentrated. The dominant transition in the bounded analyses is `ventilated - with no daily extubation trial` to `ventilated - with daily extubation evaluation`, but it has only 14 rows in the 24-hour variant and 8 rows in the 6-hour variant. These data do not support a defensible hospital-held-out dynamic model without high-variance or overfit estimates.

## Decision rules

Supportive evidence would require the feasibility gate to pass and, in the prespecified held-out analysis, dynamic state/history to improve both micro and macro log loss over process controls, with consistent improvement over static exact receipt in the primary and at least two airway sensitivities; stay-clustered uncertainty must exclude zero for both micro and macro comparisons. This would support a transportable documentation-feature claim only.

Adverse evidence is the observed branch when bounded incident/transition/persistence states fail the multisite support gate, especially when one hospital dominates the few dynamic observations. It means the exported dynamic feature is not fit for the proposed multicenter predictive use in this snapshot because support and workflow portability are inadequate; it does not mean that bedside respiratory trajectories lack transitions.

Inconclusive evidence would apply if support is borderline or outcome availability prevents a stable held-out comparison without clear adverse concentration, or if point estimates and uncertainty disagree. It would motivate a larger or differently sourced study rather than a positive clinical interpretation.

## Conclusions and limitations

The executable feasibility experiment yields an adverse dynamic fitness-for-use result for the proposed multicenter use: with a strict 24-hour pre-landmark history and bounded airway denominators, incident and transition states are too sparse and too concentrated to identify a reproducible hospital-transportable signal, and persistence is more concentrated still. The result is falsifiable: a new snapshot, a broader validated interface, or independently adjudicated respiratory-support data could supply adequate multisite dynamic events and permit the prespecified held-out test.

Computationally checkable claims include source counts, vocabulary membership, interval membership, deterministic state classification, denominator joins, outcome-window filtering, category support, concentration, and any future held-out metrics. Clinical claims about actual ventilation, daily extubation evaluation, SBT delivery, extubation readiness, appropriateness, benefit, harm, or causality require bedside/source validation, expert adjudication, or another study. Missing local interface metadata and sparse structured documentation remain important limitations.

## Reproducibility artifacts

- feasibility code: `[internal dataset path]`
- feasibility result: `[internal dataset path]`
- stdout capture: `[internal dataset path]`
- source catalog: `[internal dataset path]`
- eICU guide: `[internal dataset path]`
