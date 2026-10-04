# Continuous baseline cystatin-C rescue test after the adverse binary result

## Lineage, unresolved question, and substantive advance

This is a post-parent follow-up child of assessed-valid `[prior hypothesis]`. It does **not** reinterpret, overwrite, or pool with the parent result. The parent tested only the binary baseline cystatin-C discordance indicator `D = I(eGFRcys_0 < 60)` and found an adverse result under its frozen protocol: small repeat-stable loss reductions failed the multiplicity-controlled two-loss gate, while the added binary feature worsened fixed 10% selected-risk and event concentration. The parent therefore leaves open one narrow mechanistic explanation: dichotomization may have discarded information present in the measured continuous baseline cystatin-C value.

The unresolved, falsifiable question is:

> In the exact parent-selected UK Biobank first-repeat-attender cohort, does one prespecified continuous representation of baseline cystatin-C add reproducible held-out information for repeat creatinine-derived eGFR below 60 beyond the identical strong flexible creatinine comparator used by the parent?

The rescue hypothesis is that the continuous measurement will improve paired held-out prediction and fixed-capacity risk concentration without materially worsening calibration. The null/adverse alternative is that the parent’s failure reflects little reproducible incremental information in the assay value itself, rather than only threshold loss. This is an incremental prediction experiment among observed qualifying repeat attenders, not a test of measured GFR, CKD chronicity, causal testing benefit, or clinical utility.

The substantive advance is a single, fixed, threshold-free assay-value test. It removes the parent’s binary threshold but adds no alternative thresholds, knots, interactions, transformations selected from the outcome, competing model families, or post hoc capacity. Thus a positive result would rescue only continuous incremental information under this protocol; it would not rescue the falsified binary claim or establish that cystatin-C testing improves care.

## Evidence already supported versus claim being tested

The strongest parent-supported claim is narrow: in the exact selected complete-biomarker repeat-attender cohort, adding `D` to the parent’s ridge-spline creatinine model produced small repeat-stable held-out loss reductions, but neither Brier nor log-loss passed the Holm-adjusted two-loss gate, and 10% fixed-capacity selected risk and event capture were lower with `D`. The parent’s model was independently aggregate-audited. That evidence does not determine whether continuous cystatin-C has incremental information.

This proposal tests only the following stronger residual claim: adding a **single continuous baseline cystatin-C feature**, fixed before inspecting child outcomes, improves out-of-sample prediction and prespecified 10% risk concentration beyond the parent comparator. Any result remains conditional on the selected repeat-attender population, observed repeat timing, complete biomarker ascertainment, and the frozen UKB snapshot.

## Frozen data, source paths, tables, archive members, and joins

Use UKB snapshot `[source checksum]`, source catalog [source checksum], and read-only ordinary-file archive members only.

1. Biological samples: `[internal dataset path]`, catalog table `biological_samples`, schema `[internal dataset path]`, ordinary file member. Required columns are `eid`, `30700-0.0`, `30700-1.0`, `30720-0.0`, and `30720-1.0`.
2. Assessment center: `[internal dataset path]`, catalog table `assessment`, schema `[internal dataset path]`, ordinary file member. Required columns are `eid`, `53-0.0`, `53-1.0`, `21003-0.0`, and `21003-1.0`.
3. Population characteristics: `[internal dataset path]`, catalog table `population`, schema `[internal dataset path]`, ordinary file member. Required columns are `eid` and `31-0.0`.

Project only these columns and inner-join `biological_samples`, `assessment`, and `population` one-to-one on `eid`. Assert 502,370 projected rows, 502,370 unique `eid`, and no silent duplicate expansion. Preserve source files read-only; derived projections, predictions, and aggregate results remain private workspace artifacts. Do not publish IDs, rows, fold memberships, individual predictions, model weights, or notes.

The metadata explicitly records UKB field-instance-array encoding and that local per-field labels, units, and missing-value meanings are incomplete. Numeric eligibility rules below are therefore part of the frozen computational protocol, not a claim of independently adjudicated assay units. Field identity, assay provenance, and clinical unit interpretation require external UKB/assay documentation or expert review.

## Exact population and temporal boundary

Reconstruct the cohort sequentially from the joined projection; do not filter a parent result or use parent predictions.

- Let `sex` be numeric `31-0.0`; retain only values exactly 0 or 1.
- Parse `53-0.0` and `53-1.0` as dates; parse `21003-0.0` and `21003-1.0` as positive finite ages.
- Parse all four biomarker fields as finite positive numbers. Creatinine values are converted by `Scr_umol_per_L / 88.4` for the eGFR equation. Baseline and repeat cystatin-C fields are retained as numeric measurements; no cystatin-C threshold is used anywhere in the child predictor.
- Baseline complete-case mask `B` requires valid sex, baseline date, positive baseline age, baseline creatinine `30700-0.0`, and baseline cystatin C `30720-0.0`.
- Qualifying first-repeat-attender mask `R` is `B` plus valid repeat date, positive repeat age, repeat creatinine `30700-1.0`, repeat cystatin C `30720-1.0`, and inclusive elapsed time `(date1-date0)/365.25` in `[2, 8]` years.
- Direction-A selected cohort `S_A` is `R` and baseline unrounded creatinine eGFR at least 60. No other exclusions, trimming, winsorization, imputation, center restriction, or complete-case change is allowed.

The expected integrity anchors, inherited and recomputed before modeling, are `B=468,887`, `R=16,546`, `S_A=16,372`, observed elapsed interval 2.1081451061–6.1136208077 years, and baseline eGFRcr minimum 60.0659423121. The expected 2x2 cells using parent binary `D` only for an audit—not as a child predictor—are `(E0Y0,E0Y1,E1Y0,E1Y1)=(15,769,255,294,54)`, with 309 events and 348 `D=1` participants. If any anchor differs, stop as a source/projection failure; do not repair by changing filters.

The outcome is fixed as `Y = I(eGFRcr_1 < 60)` from repeat creatinine and repeat age. No repeat cystatin-C value, repeat-derived feature, future diagnosis, or post-baseline field may enter a predictor.

## Exact equations and feature definitions

Use the unrounded race-free 2021 CKD-EPI creatinine equation, with creatinine converted from micromoles/L by division by 88.4. For sex code 0 (female), `k=0.7`, `a=-0.241`, and sex multiplier `1.012`; for sex code 1 (male), `k=0.9`, `a=-0.302`, and multiplier `1.0`:

`eGFRcr = 142 * min(Scr/k,1)^a * max(Scr/k,1)^(-1.2) * 0.9938^age * female_multiplier`.

The parent’s 2012 cystatin-C-only equation and binary threshold are not used to construct the child feature. In particular, there is no `eGFRcys <60` term, no alternative eGFRcys threshold, and no cystatin-C threshold search.

The sole continuous child feature is fixed as follows:

`C0 = log(cys0)` where `cys0` is the positive raw baseline value in `30720-0.0`.

Within each training fold only, calculate `mu_C` and population standard deviation `sd_C` (`ddof=0`) over `C0`; define `ZC=(C0-mu_C)/sd_C` for training and held-out rows. Require finite `mu_C`, finite positive `sd_C`, and finite held-out `ZC`. The logarithm is fixed in advance to limit skew and is not selected after looking at outcomes. Because the feature is standardized, any common positive unit multiplier changes only the training mean and not the standardized values; this mathematical invariance does not establish clinical assay units. No cys transform alternatives (raw, reciprocal, square root, polynomial, spline, rank, cut point, quantile, winsorization, or interaction) may be tried for the primary claim.

## Nested models and fixed algorithms

Use the exact parent comparator as `M0`, with no refitting convention changes:

- intercept;
- separate four-column natural-cubic spline bases for baseline unrounded `eGFRcr_0`, baseline age `age0`, and observed elapsed years;
- binary sex.

For each fold, each spline uses training-fold empirical 25th, 50th, and 75th percentiles as interior knots, training-fold minimum and maximum as boundaries, Patsy `cr(..., constraints="center")`, exactly four columns, and training-fold mean/population-SD standardization. Held-out values never determine knots, boundaries, centering, or scaling.

`M1C` is exactly `M0` plus the one standardized continuous feature `ZC`. There are exactly 13 M0 columns and 14 M1C columns before the fitted intercept. No binary `D` enters M1C, and no feature is selected by validation performance. Fit both with `sklearn.linear_model.LogisticRegression`, `solver='lbfgs'`, `penalty='l2'`, `C=1.0`, unpenalized fitted intercept, `tol=1e-10`, `max_iter=2000`, `class_weight=None`, and no tuning. Require convergence before using predictions. A fixed unpenalized-coefficient sensitivity may be executed only as a labeled robustness check using the same folds and feature schema; it cannot alter the primary classification.

Use the parent’s ten exact seeds `[104729,104759,104773,104779,104789,104801,104827,104831,104849,104851]`. For each seed, make participant-level outcome-stratified five-fold assignments by seeded within-outcome permutation followed by deterministic round-robin assignment. Fit on four folds and predict the held-out fold, producing exactly one paired held-out prediction per participant per repeat and 50 paired test folds overall. Do not treat repeated predictions as independent participants.

## Estimands, uncertainty, and fixed decision sequence

The primary estimands are paired participant-averaged differences, `M1C - M0`, over the ten repeated held-out predictions:

1. Brier loss difference, with lower values better.
2. Log loss difference, with lower values better.

Use the same fixed primary two-component Holm adjustment at familywise alpha 0.05. The primary loss gate requires both point estimates below zero and both Holm-adjusted p-values below 0.05. The point estimates and conditional 95% intervals are obtained from a paired participant-level bootstrap with all ten repeated predictions carried together, 2,000 successful replicates, and no model refitting; label intervals explicitly conditional on the frozen splits and fits.

The fixed secondary decision estimand is 10% capacity concentration. In each held-out fold, rank M0 and M1C predictions separately, allocate the exact total `round(0.10*16,372)=1,637` slots across folds by floor plus largest fractional remainder, and select without using outcomes. Report selected risk (event proportion among selected participants) and event capture (selected events divided by all 309 events), and their M1C-minus-M0 differences. Use the fixed 10% capacity as primary concentration; do not choose 5% after seeing results. The 5% capacity (`819` slots) may be reported only as a predeclared descriptive transport-of-capacity diagnostic and cannot rescue or overturn the 10% gate.

For the 10% family, use the same paired participant bootstrap with 1,000 successful replicates and Holm adjustment across selected risk and event capture. The positive concentration gate requires the 95% interval for M1C-minus-M0 selected risk to be wholly above zero. Event capture is reported jointly and is not selectively substituted for selected risk. The fixed concentration rule is deliberately unchanged from the parent so the child cannot move the decision boundary after the adverse result.

Assess calibration on each participant’s mean prediction over ten repeats using joint logistic calibration intercept and slope and observed-minus-mean-predicted risk. Predeclare material deterioration as an increase in absolute intercept error greater than 0.10, absolute slope-from-one error greater than 0.10, or absolute observed-minus-predicted risk greater than 0.002, with the corresponding conditional degradation interval above zero. These are computational margins, not validated clinical utility thresholds.

## Classification and interpretation gates

Classify the continuous rescue test before inspecting its results as follows:

- **Supportive rescue:** both primary loss differences are negative and pass the Holm 0.05 gate; no material calibration deterioration; the 10% selected-risk difference interval is wholly positive; and each primary loss is negative in at least 8 of 10 repeats. This supports reproducible continuous incremental information under the exact protocol, not clinical benefit.
- **Adverse/no rescue:** either primary loss is worse (positive point estimate), material calibration deterioration occurs, the 10% selected-risk difference is nonpositive, or either primary loss is negative in fewer than 8 of 10 repeats. A nonpositive capacity result is adverse under this protocol even if average loss improves, because the prespecified concentration objective was not rescued. If losses improve but fail Holm while concentration is positive, classify adverse/no rescue rather than call it supportive.
- **Inconclusive:** all adverse triggers are absent, but the full supportive gate is not met—for example, mixed loss evidence, a confidence interval crossing zero, or an execution/support failure that prevents a valid comparison. Do not convert non-rejection into equivalence.

The child’s conclusion must be tied to computed aggregate outputs. The parent’s adverse binary result remains a separate prior branch and is not counted as a replicate or combined p-value. No post hoc threshold, model, horizon, capacity, subgroup, calibration margin, or endpoint may be selected to change classification.

## Falsification, leakage, and integrity checks

The implementation must fail closed if any of the following occur: source files or snapshot differ; projected `eid` rows are nonunique; any cohort anchor differs; dates or biomarker values are parsed with undocumented coercion; repeat values enter predictors; a held-out value determines spline knots/scaling or `ZC` scaling; M1C has any feature other than M0 plus `ZC`; a fold lacks exactly one held-out prediction per participant; predictions are nonfinite; logistic fits do not converge; capacity allocation is not exactly 1,637 at 10%; or bootstrap clustering omits the repeated prediction vector for a participant.

As a noninferential leakage falsification, repeat the same fold-local pipeline with `ZC` independently permuted within each training fold before fitting and with the corresponding held-out permutation fixed by a deterministic seed. The placebo feature retains its marginal distribution but has no participant’s actual baseline cystatin-C correspondence. The placebo must not show a systematic primary or 10% advantage; a substantial placebo advantage triggers an implementation audit and suppresses the continuous rescue conclusion. This diagnostic is not an additional opportunity to select a model or threshold and does not generate a second confirmatory p-value.

Also run the exact parent aggregate comparator checks: recompute the inherited `D` cells only as a cohort audit; independently recalculate the M0/M1C point estimates from the private prediction payload using a separately written aggregate script; verify training-only preprocessing, paired rows, fold-local ranking, and feature counts; and confirm that no private IDs, rows, predictions, weights, or notes are published. If these checks fail, report computational inconclusive rather than adverse scientific evidence.

## Meaning of results and evidence limits

A supportive result would mean that a fixed continuous baseline cystatin-C representation contains reproducible held-out information that the parent’s binary discordance threshold failed to retain, within the exact selected first-repeat-attender cohort and the fixed ridge-spline comparator. It would justify external validation of continuous assay-value modeling, not changing a CKD threshold or ordering cystatin C in care.

An adverse result would mean that replacing the binary indicator with this prespecified continuous measurement does not rescue the incremental-information claim under the same strong comparator and fixed capacity objective. It would strengthen the conclusion that no reproducible value was demonstrated under this protocol, while not proving cystatin C biologically irrelevant or useless for other outcomes, equations, populations, or clinical workflows.

An inconclusive result would mean that the data/protocol cannot distinguish these explanations; it is not evidence of no effect or equivalence. In particular, an execution failure, unsupported field interpretation, inadequate event information, or intervals crossing zero must remain uncertainty rather than being narrated as a negative biological finding.

Computationally checkable claims include snapshot/source hashes, exact joins and anchor counts, cohort/outcome construction, equations, feature schema, fold assignments, training-only transformations, convergence, held-out coverage, paired losses, fixed-capacity arithmetic, calibration calculations, bootstrap scope, placebo leakage checks, aggregate reproducibility, and conclusion-to-gate consistency. Expert review or another study is required for assay identity and units, biological interpretation, measured GFR, CKD diagnosis/chronicity, missingness and repeat-attendance mechanisms, treatment decisions, patient benefit or harm, causal effects, clinical utility, and transport to people who did not attend a qualifying repeat visit.

The outcome is repeat creatinine-derived eGFR threshold crossing, not a gold-standard GFR measurement. Because elapsed repeat time is an observed predictor and cohort membership conditions on future attendance, this is not a baseline-deployable risk model. Complete-case selection, low event count (309/16,372), measurement error, assay calibration, selection/collider bias, and external transport remain material limitations.
