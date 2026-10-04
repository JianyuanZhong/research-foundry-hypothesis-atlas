# Independent first-day Apache triangulation and state/opportunity-preserving null for the frozen eICU respiratory-label experiment

## Purpose and bounded advance

This proposal is a substantive child of assessed-valid `[prior hypothesis]` and `[prior hypothesis]`. It follows the Lead goal exactly. The frozen scientific schema is unchanged: 540 person-landmark rows, 443 distinct first qualifying ICU stays/persons, 74 hospitals; first qualifying stay per `uniquepid`; landmarks `L ∈ {1440, 2880, 4320, 5760, 7200}` minutes after ICU admission; first exact target label in `[L,L+360]`; `D = cplitemoffset`; inherited pre-landmark exclusions; exact literal arms; fixed B/E/T windows and parser; five mutually exclusive all-row states; repeated landmarks clustered by `patientunitstayid`; and a descriptive, noncausal evidence boundary.

The strongest evidence available supports only that the two literal care-plan values are sparse, hospital-heterogeneous structured documentation and that an apparent association can arise from patient-state mix, documentation opportunity, source density, exits, or repeated-stay documentation. It does not establish SBT or extubation semantics, clinician intent, readiness, delivered settings, treatment, benefit, harm, quality, or causality. The unresolved claim remains narrower and falsifiable: after pre-`D` state and documentation opportunity are controlled, does the exact label add reproducible information about a later independently constructed respiratory chart trajectory, including an independent physiologic proxy, when tested on hospitals not used for fitting?

The substantive repair is an **outcome-blind first-day Apache physiologic triangulation** and a stricter **state/opportunity-preserving label null**. The new Apache block is used only as an admission/first-day physiologic severity sensitivity and residual state adjustment. It is never treated as an endpoint, never used to define the cohort or exposure, and never interpreted as bedside readiness. The current vitalPeriodic triangulation is retained as a separate secondary target. The new experiment asks whether a label increment survives when independent first-day physiologic measurements are added to the respiratory-chart state, and whether it exceeds a null that preserves the joint patient-state/documentation opportunity structure. If Apache timing cannot be verified as first-day or its fields cannot be shown outcome-blind, that triangulation is unavailable and the result is explicitly inconclusive; the primary frozen analysis still proceeds.

## Frozen reconstruction and fail-closed stop

Before reading any respiratory endpoint or value, byte-verify the inherited artifacts:

* `eicu_strict_cohort.csv`, exactly 540 rows, 443 unique first qualifying stays/persons, 74 hospitals, [source checksum].
* The action-row artifact, exactly one row per (`patientunitstayid`, landmark), with exact `label`, `D`, and `decision_offset`, [source checksum].

Verify byte identity, required identity columns, uniqueness of (`patientunitstayid`,`landmark`), one-to-one action joins, all five landmarks, exact labels, and `D == decision_offset`. If either artifact is absent or differs, stop before outcome extraction and emit only a feasibility/inconclusive result naming the failed check; never reconstruct a substitute cohort. Arms remain exactly `Ventilated - with daily extubation evaluation` (`evaluation`) and `Ventilated - with no daily extubation trial` (`no_trial`). `carePlanGeneral` is exposure/D verification only. No care-plan field, count, note, value, or post-D record may enter baseline, opportunity, endpoint, diagnostic, null, or model calculations.

## Primary endpoint and unchanged five-state all-row accounting

Use clinical offsets, never entry offsets, relative to each row's `D`:

* `B = (D-720,D]`
* `E = (D,D+720]`
* `T = (D+720,D+2160]`

Enumerate all source-wide `respchartvaluelabel` and `respcharttypecat` values with matched/unmatched counts before arm-stratified results. Apply the inherited locked parser to FiO2, PEEP/PEEP-CPAP, pressure support, and set ventilator rate: aliases, finite-number and bounds checks, fraction/percentage conversion, duplicate collapse, same-clinical-time conflict rules, and recorded reasons. A component requires at least two valid observations at distinct clinical offsets separated by at least 30 minutes; a respiratory state requires at least three of four observed components. Missing is never zero, unchanged, or carried forward. Fixed absolute thresholds are FiO2 `0.10` fraction, PEEP `2 cmH2O`, pressure support `2 cmH2O`, and set rate `2 breaths/min`.

For rows without a competing exit, sustained de-escalation requires observed B/T states, at least two component decreases, no increase, and no E escalation. Escalation requires observed B/T states plus at least two increases, or a newly documented invasive airway in E/T after no invasive evidence in B. Stable/mixed is the remaining classifiable state. An indeterminate required E airway check cannot create de-escalation and is non-exit unobservable unless an independent increase/airway rule assigns escalation. `respiratoryCare` is airway corroboration/sensitivity only and cannot fill numeric settings; active interval is `ventstartoffset <= time` and missing or `ventendoffset >= time`.

Every row receives exactly one ordered state:

`K ∈ {competing_exit, classifiable-de-escalation, classifiable-escalation, classifiable-stable/mixed, non_exit_unobservable}`.

A finite `patient.unitdischargeoffset <= D+2160` has precedence, including death, discharge, transfer, or inability to complete T. Record exact exit offset, `unitdischargestatus`, `unitdischargelocation`, and `exit_before_washout = 1{unitdischargeoffset <= D+720}`. Invalid or unavailable exit timing is a separate `invalid_exit_time` administrative reason and is never treated as alive. Do not assign exits to respiratory classes. Assert exactly one K state for all 540 rows.

The unchanged primary estimand is

`p_k(a) = N_a^{-1} Σ_i 1{A_i=a,K_i=k}` and `Δ_k = p_k(evaluation)-p_k(no_trial)`.

The unchanged conditional display is `q_c(a) = count(A=a,K=classifiable-c)/count(A=a,K is classifiable)` and `δ_c=q_c(evaluation)-q_c(no_trial)`, only after support checks and always beside all-row denominators, exits, and unobservability. Neither estimand is causal.

## Exact source bindings and read-only provenance

All sources are the eICU 2.0 snapshot `[source checksum]`; catalog `[internal dataset path]`, [source checksum]; and local guide `[internal dataset path]`, snapshot [source checksum]. The gzip sources are ordinary files (archive member `ordinary file`) under `[internal dataset path]`. The compiler must recheck current paths, headers, hashes, schema hashes, snapshot, and ordinary-file convention and fail closed on divergence. Every table joins `patient` on `patientunitstayid` according to `metadata.json`.

* `patient`: source `[internal dataset path]`, source [source checksum]; schema `[internal dataset path]`, schema [source checksum]; join `patientunitstayid`; use `uniquepid`, `hospitalid`, `unitvisitnumber`, `age`, `unitdischargeoffset`, `unitdischargestatus`, `unitdischargelocation`.
* `carePlanGeneral`: source `[internal dataset path]`, source [source checksum]; schema `[internal dataset path]`, schema [source checksum]; use `patientunitstayid`, `cplitemoffset`, `cplgroup`, `cplitemvalue`, `cplgeneralid` for exposure/D verification only.
* `respiratoryCharting`: source `[internal dataset path]`, source [source checksum]; schema `[internal dataset path]`, schema [source checksum]; join `patientunitstayid`; clinical time `respchartoffset`, entry time `respchartentryoffset`; use `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`, `respchartid` for parser, endpoint, opportunity, and entry-clock audit.
* `respiratoryCare`: source `[internal dataset path]`, source [source checksum]; schema `[internal dataset path]`, schema [source checksum]; join `patientunitstayid`; use `respcarestatusoffset`, `airwaytype`, `airwaysize`, `airwayposition`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset` for airway, interval, and opportunity fields.
* `vitalPeriodic`: source `[internal dataset path]`, source [source checksum]; schema `[internal dataset path]`, schema [source checksum]; join `patientunitstayid`; clinical time `observationoffset`; use `sao2`, `respiration` for pre-D state/opportunity and independent post-D sensitivity. The metadata identifies these as five-minute summary observations, not waveforms.
* `treatment`: source `[internal dataset path]`, source [source checksum]; schema `[internal dataset path]`, schema [source checksum]; join `patientunitstayid`; use `treatmentoffset`, `treatmentstring`, `activeupondischarge` only for inherited airway concordance/negative-control and pre-D opportunity, never semantic treatment claims.
* `apacheApsVar`: source `[internal dataset path]`, source [source checksum]; schema `[internal dataset path]`, schema [source checksum]; join `patientunitstayid`; use only the outcome-blind physiologic columns `intubated`, `vent`, `respiratoryrate`, `pao2`, `pco2`, `fio2`, `ph`, `heartrate`, `meanbp`, `temperature`, `wbc`, `sodium`, `hematocrit`, `creatinine`, `albumin`, `bun`, `glucose`, and `bilirubin`, with finite-value and source-unit audit. Do not use any outcome or discharge field from another Apache table as a predictor.
* `apachePredVar`: source `[internal dataset path]`, source [source checksum]; schema `[internal dataset path]`, schema [source checksum]; join `patientunitstayid`. Use only the explicitly outcome-blind admission/first-day physiologic/context fields `saps3day1`, `saps3today`, `saps3yesterday`, `age`, `gender`, `admitdiagnosis`, `pao2`, `fio2`, `creatinine`, `day1pao2`, and `day1fio2` if the source audit confirms their first-day timing and no outcome derivation. Exclude `diedinhospital`, `dischargelocation`, all mortality/length-of-stay fields, and other fields whose timing or outcome dependence cannot be established. Because this table has no temporal column, it is a first-day/admission block only, never a time-varying pre-D observation.

`apachePatientResult` is inspected only for schema audit and is excluded from all predictors because it contains actual and predicted mortality, length of stay, and actual ventilation outcomes (`actualicumortality`, `actualhospitalmortality`, `actualiculos`, `actualhospitallos`, `actualventdays`, and related fields). It cannot be used to claim outcome-blindness. The catalog and `metadata.json` are the authority for relationships and conventions.

## Predictor clocks, state, and documentation opportunity

All ordinary baseline predictors must have clinical time `< D`, except the current exact label in M1. The inherited pre-D state includes B summaries and missingness for four respiratory components, pre-D airway evidence, finite pre-D `vitalPeriodic.sao2` and `vitalPeriodic.respiration`, age category, landmark, and inherited covariates. Pre-D opportunity is value-blind: respiratoryCharting row counts, distinct clinical timestamps, distinct component labels, spacing and entry-lag summaries; respiratoryCare row/airway counts; vitalPeriodic row/timestamp counts and spacing; and treatment row counts. No post-D value/count, endpoint flag, future exit, treatment meaning, or care-plan field may enter a predictor.

Add an `apache_first_day` manifest with source row counts, one-to-one stay join counts, missingness, finite-value and unit audits, and the exact accepted/rejected column list. Since all landmarks are at least 1440 minutes, an audited first-day/admission Apache block is temporally prior to every `D` in the frozen cohort; nevertheless the compiler must not infer a finer timestamp than the source provides. If the source guide or headers cannot verify first-day semantics, omit the block and mark Apache triangulation inconclusive rather than treating it as pre-D.

Define an outcome-blind scalar `Aphys` from the accepted Apache physiologic fields using training-fold-only preprocessing: fixed finite-value checks, prespecified physiologic ranges from the source dictionary, missingness indicators, and regularized standardization. Do not hand-label illness or interpret any score clinically. Use `Aphys` only as a covariate block and stratification variable. Do not include any Apache actual/predicted outcome, discharge, LOS, mortality, or post-D field.

Emit separate manifests `pre_D_baseline`, `apache_first_day`, `post_D_endpoint`, and `post_D_diagnostic`. Any post-D leakage, care-plan contamination, unverified Apache timing, or outcome-dependent Apache field invalidates the corresponding triangulation and is reported in `verification.json`; it does not silently downgrade to a claim.

## Cross-fitted models and independent triangulation

Retain the parent models:

* `M0`: pre-D respiratory state plus pre-D opportunity, no current label;
* `M1`: identical predictors plus exact current two-level label;
* `Mopp`: pre-D opportunity only, no respiratory values and no label.

Add:

* `MA`: M0 plus the accepted outcome-blind `Aphys` Apache block, no label;
* `M1A`: MA plus the exact current label.

All imputation, scaling, regularization, probability estimation, calibration, observation weighting, Aphys construction, and cutpoints are fit within training hospitals of each held-out-hospital fold. No hospital predictor, held-out target-rate calibration, or held-out intercept is used. Every `patientunitstayid` stays in one fold; repeated landmarks never split across training and test. The primary comparison remains M1 versus M0. `M1A` versus `MA` is a prespecified residual-state sensitivity, not a replacement primary estimand. Report both micro row-weighted and equal-hospital macro held-out log loss and Brier scores for all-row K and classifiable displays, with confidence intervals from stay-cluster resampling.

A label increment is compatible with residual patient-state information only if it is present in M1-M0 and remains directionally and computationally supported in M1A-MA, with Apache availability and support explicitly reported. Failure of Apache support, timing, or outcome-blindness is inconclusive for the triangulated claim, not evidence against the label. A gain only before Apache adjustment is a state-confounding warning, not evidence of bedside meaning.

Retain the independent `vitalPeriodic` secondary target exactly as in the parents. In E and T, define separate `H_E` and `H_T` states `{alert,no_alert,physiologic_unobservable}`: opportunity requires at least two finite rows at distinct `observationoffset` values spanning at least 5 minutes; an alert requires at least two distinct valid observations with `sao2 < 88` or `respiration > 30`. Verify units and convention (`sao2` percent, respiration breaths/min) from the guide. This is a five-minute summary chart proxy, not hypoxemia, tachypnea, respiratory failure, harm, or an adjudicated outcome. Preserve exits and invalid exit time separately; never code absent observations as no-alert.

## Joint state/opportunity partition and conditional null

Within each training fold only, form a scalar state score from permitted pre-D respiratory component summaries/missingness, pre-D airway evidence, vital summaries, and accepted `Aphys`; form an opportunity score from permitted value-blind counts, distinct timestamps, spacing, and entry-lag summaries. Fixed empirical tertiles are used when all bins have support, otherwise a deterministic median split; sparse cells are collapsed deterministically without using label, K, H, effect direction, or endpoint. Cross each frozen training-derived state and opportunity bin with landmark. For transport summaries, the held-out hospital is never used to fit cutpoints. Apply training cutpoints to held-out rows and record cutpoints, all cell counts, Apache availability, and support.

The primary conditional null is an exact-label permutation within held-out-evaluation hospital-by-landmark strata and the joint training-derived state/opportunity cells. Preserve the exact arm counts, all five-landmark composition, and stay-cluster structure. A stay is permutable only under the predeclared cluster-preserving implementation; if row-level membership would break a stay cluster, leave the affected stratum unavailable rather than silently splitting or merging it. No null cell is merged using observed effect direction. Use at least 1,000 valid permutations where feasible and record attempted/valid permutations, valid strata, cluster-preservation checks, and nonempty cells. Fewer than 20 valid strata, inability to preserve stay clusters, or unsupported held-out cells is inconclusive, not a negative result.

For supported cells with at least 10 rows per exact arm and at least 20 total rows, report held-out M1-M0 and M1A-MA loss increments, plus descriptive arm contrasts for every K state. Summarize equal-cell and row-weighted aggregates; no unsupported cell contributes. Require residual patient-state evidence to appear in at least five supported state/opportunity/Apache cells spanning at least five hospitals, with no cell contributing more than 25% of supported rows. If the observed increment is typical under the joint state/opportunity-preserving null, the result is adverse to incremental patient-state information even if a broad hospital-by-landmark null is unfavorable. If Apache is unavailable, the original state/opportunity null remains interpretable but the independent Apache triangulation is inconclusive.

Retain the parent broad hospital-by-landmark null, site-balanced envelope, leave-one-site-out influence, first-versus-repeated landmark/persistence audit, whole-stay sequence null when exactly feasible, placebo/exposure-shift tests, component/source ablations, exit decomposition, and clinical-time versus as-entered sensitivity. Any increment confined to exits, unobservability, source density, entry lag, one site/component/source, repeated landmarks without first-landmark support, or unsupported Apache cells is not patient-state evidence.

## Transport, all-row metrics, and operational target

Use leave-one-hospital-out folds with no hospital predictor. Report all-row five-state K probabilities and held-out M0/M1/MA/M1A log loss, Brier score, calibration where finite, classifiable-only metrics, exits, and non-exit unobservability. Retain parent site support: for each hospital report rows, stays, arms, each K state, classifiable non-competing counts, opportunity distributions, Apache availability/support, vital availability, entry-clock counts, and exit timing. Keep one-arm sites descriptively and do not create a contrast for them.

The transport gate remains predeclared: at least five hospitals with at least 10 classifiable non-competing rows per exact arm, representing at least 50% of supported rows, both micro and equal-site held-out loss increments favorable, and no more than 25% directional reversals. The Apache residual-state gate additionally requires at least five hospitals and five supported joint state/opportunity/Apache cells spanning both arms, no cell above 25% of supported rows, valid Apache audits, and no adverse joint null. Otherwise report adverse or inconclusive according to the specified support and uncertainty, never a bedside interpretation.

Retain the secondary fixed manual respiratory-review prioritization task only as an operational chart-review analysis. For `Y_K=1{K=classifiable-escalation}` and separate `Y_HE`/`Y_HT`, compare held-out M0 versus M1 (and label-free MA where applicable), treat-none, treat-all-observed-target, and fixed-capacity review policies under the inherited prespecified threshold/cost/capacity grids. Review/no-review/abstain and unresolved states remain explicit. This score is not patient utility, mortality cost, treatment, or clinical benefit. It cannot rescue a failed state/opportunity or Apache triangulation.

## Uncertainty, falsification, and interpretation

Use fixed-seed `61061` stay-cluster bootstrap, minimum 500 and target 1,000 valid replicates, refitting the full held-out pipeline and recomputing folds, Aphys, partitions, nulls, transport summaries, and review metrics. Report attempted, valid, failed, effective-cluster, site-support-loss, Apache-support-loss, and supported-cell counts. Do not use a row bootstrap or replace unsupported replicates with a row bootstrap.

Computational invalidity includes artifact/hash/schema/source mismatch; duplicate or non-one-to-one joins; wrong labels/landmarks/D; parser or boundary errors; unit/timing audit failure; post-D leakage; care-plan contamination; outcome-dependent Apache field use; failure of exactly one K state; exit precedence failure; fold/stay leakage; null cluster failure; nonreproducible threshold/action tables; or missing machine-readable linkage from conclusions to outputs. Stop interpretation on invalidity.

A computationally supportive incremental label-information result requires M1 to improve both micro and equal-hospital macro held-out K loss over M0 in the unbounded primary and at least two frozen endpoint/observation sensitivities, favorable stay-cluster uncertainty, transport support, no adverse broad or joint state/opportunity null, and no gain confined to exits, unobservability, opportunity, entry lag, persistence, or one source. The stronger triangulated result additionally requires M1A versus MA to remain supported, an audited outcome-blind first-day Apache block, at least five supported joint cells across at least five hospitals, and directional concordance in at least two supported overlap hospitals with the separately evaluated vitalPeriodic target. A gain that disappears after Aphys is added is adverse to a residual-label interpretation. Failure of Apache timing, support, or outcome-blindness is inconclusive for that stronger claim.

Supportive output establishes only incremental prediction or operational prioritization of named structured eICU chart constructs. Adverse output says the label is not robust for those constructs or is explainable by state, opportunity, site, persistence, or exits. Inconclusive output identifies sparse cells, missing Apache timing/units, unavailable vital opportunity, invalid null, failed calibration, support loss, or uncertainty. None establishes bedside evaluation, SBT/extubation semantics, treatment effect, patient benefit, harm, quality, or causality. Those conclusions require local interface/workflow dictionaries, synchronized device logs, expert adjudication, validated SBT/extubation/reintubation outcomes, follow-up, and external or prospective replication.

## Required compiler outputs

Emit at least `source_manifest.json`, `filter_counts.json`, `frozen_population_verified.csv`, `exposure_verified.csv`, `trajectory_rows.csv`, `site_support.csv`, `heldout_metrics.json`, `transport_envelope.json`, `state_opportunity_cells.json`, `apache_first_day.json`, `apache_support.csv`, `conditional_null_summary.json`, `documentation_opportunity.json`, `physiologic_triangulation.csv`, `decision_curve.json`, `bootstrap_summary.json`, `permutation_summary.json`, `placebo_summary.json`, `as_entered_clock_sensitivity.json`, `landmark_persistence.json`, and `verification.json`.

Every artifact must record source/schema/catalog hashes, exact source paths, headers, ordinary-file convention, table and join keys, filter/status attrition, clinical and entry inequalities, parser and unit/opportunity manifests, Apache accepted/rejected field list and timing audit, K/H precedence, fold and stay grouping, partition cutpoints/support, null counts, threshold/cost grids, uncertainty, and mechanically derived gates. Every conclusion must cite a machine-readable artifact and interval. No estimates are supplied in this proposal.

## Reference and availability boundary

The local research-ambition demonstrations were inspected only at the level permitted by `[internal dataset path]`. The README states that the natural-history and Bayesian papers have downloaded full articles/supplements but that mechanical extraction can lose figure, table, and equation formatting; it also states that the cancer main article and full STAR Methods remain unavailable and only its supplement is available. No unavailable cancer article or methods are used here. These references motivate longitudinal leakage control and evidence boundaries only; they are not evidence that the eICU labels have bedside semantics.
