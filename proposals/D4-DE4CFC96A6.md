> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Renal-marker specificity of the continuous cystatin-C rescue

## Lineage and scientific question

This proposal is a substantive prospective child of the assessed, valid candidate `[prior hypothesis]`. It preserves that candidate's UK Biobank snapshot, selected population, temporal boundary, creatinine outcome, comparator, repeated cross-fitting framework, aggregate-only publication boundary, and prior binary/continuous evidence. The parent found that `Zrenal = log(eGFRcys_0/eGFRcr_0)` improved held-out log loss beyond a flexible creatinine comparator in all ten repeats, but the fixed 10% capacity result was only +1 outcome (conditional 98% interval -6.401 to 8.5), so the joint rescue was inconclusive.

The unresolved, falsifiable question is whether the reproducible probabilistic gain is specific to renal-marker discordance, rather than a generic consequence of adding any baseline biomarker that carries participant-level persistence or assay information. This matters because a renal-specific signal would motivate external replication of cystatin-C discordance as a kidney-focused measurement hypothesis; a comparable gain for nonrenal biomarkers would materially weaken that interpretation and redirect the explanation toward generic biomarker augmentation. Neither result would establish clinical utility or causality.

The strongest claim already supported is narrow: under the parent protocol, one continuous baseline cystatin-C/creatinine-derived feature contains reproducible held-out information about a later repeat creatinine-equation threshold in selected qualifying repeat attenders. The experiment below tests the stronger, currently unsupported claim that this gain exceeds matched nonrenal biomarker gains on the same people, folds, horizon, and comparator.

## Exact data binding and population

Use UKB snapshot `[source checksum]`, with read-only ordinary-file archive members and horizontal one-to-one joins on `eid`:

1. `[internal dataset path]`, catalog table `biological_samples`, schema `datasets/ukb/table-c6b666d905f3b02f.json`, [source checksum]. Required columns are `eid`, `30700-0.0`, `30700-1.0` (creatinine), `30720-0.0`, `30720-1.0` (cystatin C), `30790-0.0` and `30790-1.0` (direct LDL cholesterol), and `30870-0.0` and `30870-1.0` (vitamin D).
2. `[internal dataset path]`, catalog table `assessment`, schema `datasets/ukb/table-901ef6c7ddce2d51.json`, [source checksum]. Required columns are `eid`, `53-0.0`, `53-1.0` (assessment dates), and `21003-0.0`, `21003-1.0` (age at assessment).
3. `[internal dataset path]`, catalog table `population`, schema `datasets/ukb/table-38565c9e35e7cb6c.json`, [source checksum]. Required columns are `eid` and `31-0.0` (sex).

The field IDs and instances must be verified against the complete schema and source headers before execution. The local catalog describes availability and one-to-one `eid` relationships; it does not supply reliable field units for these biomarker columns. No unit conversion may be invented. The implementation must record the raw-column values, finite/positive checks, and any locally verified unit metadata in its aggregate provenance. If `30790` or `30870` is absent or not interpretable as the named field in the frozen schema/header, the candidate is repairable only by replacing it with an explicitly verified direct-LDL/vitamin-D field before any outcome is inspected; no silent substitution is allowed.

Construct the parent projection by the same one-to-one joins and the same row order. Reproduce the parent masks exactly:

- `B`: valid sex, nonmissing baseline date, positive finite baseline age, creatinine, and cystatin C.
- `R`: `B`, nonmissing repeat date, elapsed time `(53-1.0 - 53-0.0)/(365.25 days)` finite and inclusively between 2 and 8 years, and positive finite repeat age, creatinine, and cystatin C.
- `S_A`: `R` and baseline race-free 2021 CKD-EPI creatinine eGFR at least 60.

The parent anchor expectations are `joined_n=502370`, `B_n=468887`, `R_n=16546`, `S_A_n=16372`, 309 outcomes, and `(E0Y0,E0Y1,E1Y0,E1Y1)=(15769,255,294,54)`. Execution must fail rather than proceed if these inherited anchors do not match. Repeat cystatin C remains a selection variable only, not a predictor.

After `S_A` is formed, define the **single common-complete analysis population `S_C`** as `S_A` plus finite valid baseline values for both direct LDL `30790-0.0` and vitamin D `30870-0.0`, with no imputation and no arm-specific exclusions. The exact `S_C` count, event count, and renal discordance contingency table are frozen only after applying this mask and must be reported as aggregate anchors. The analysis must not use the repeat values of LDL or vitamin D, because their repeat availability is not needed for the scientific contrast and using them would alter the parent temporal/selection protocol. Repeat columns `30790-1.0` and `30870-1.0` may be read only for an availability audit, not for prediction or eligibility.

## Derived variables and models

Use the parent equations exactly: race-free 2021 CKD-EPI creatinine eGFR for baseline and repeat creatinine, and the 2012 cystatin-C-only equation for baseline cystatin C. Define `Y=I(eGFRcr_1 < 60)`, retaining the parent's repeat creatinine-equation threshold and its limitations. Define

`Zrenal = log(eGFRcys_0 / eGFRcr_0)`.

For matched nonrenal additions, use exactly one baseline scalar per arm, with transformations frozen before fitting:

- `ZLDL = log(LDL_0)` for `30790-0.0`, only if the verified unit and positive range make this transformation valid.
- `ZvitD = log(vitaminD_0)` for `30870-0.0`, only if the verified unit and positive range make this transformation valid.

If a verified field permits zero values, the transformation rule must instead be frozen as `log1p(x)` before execution; it must not be selected after viewing outcomes. The final rule and valid-value counts are part of the aggregate audit. Each added feature is standardized using the training-fold mean and population SD only. These are matched one-degree-of-freedom biomarker additions, not claims that LDL or vitamin D are biologically equivalent to cystatin C.

For every arm, M0 is unchanged and contains a fitted intercept, sex, and separate four-column natural cubic spline bases for baseline eGFRcr, baseline age, and observed elapsed repeat time. Knots are the training-fold 25th, 50th, and 75th percentiles, boundaries are training minimum/maximum, constraints are centered, and all spline columns are scaled using training data only. The three extensions are:

- `Mrenal = M0 + Zrenal`;
- `MLDL = M0 + ZLDL`;
- `MvitD = M0 + ZvitD`.

All four models use `sklearn.linear_model.LogisticRegression(solver='lbfgs', penalty='l2', C=1, fit_intercept=True, tol=1e-10, max_iter=2000, class_weight=None, n_jobs=1)`, with no tuning or class weighting. A single set of ten outcome-stratified round-robin five-fold partitions is generated on `S_C` using the inherited seeds `[104729,104759,104773,104779,104789,104801,104827,104831,104849,104851]`. The same folds, row ordering, preprocessing rules, and held-out participants are used for all four arms. Every fold fits each model independently on its training data; no test outcome or test feature is used in fitting or preprocessing. Every participant must receive one finite held-out probability per arm per repeat, yielding 40,000 predictions in total (`|S_C| x 10 x 4`). No model or split is refit in the bootstrap.

## Estimands and multiplicity

The primary estimand is the paired difference in mean held-out log loss on `S_C`, averaged over participants and the ten repeats:

`Delta_LL,k = mean[LL(Mk)-LL(M0)]`, for `k in {renal, LDL, vitD}`.

Negative values favor the extension. The primary specificity contrasts are

`G_LDL = Delta_LL,renal - Delta_LL,LDL` and
`G_vitD = Delta_LL,renal - Delta_LL,vitD`.

A negative `G` means the renal addition improves log loss more than that comparator. The pre-specified renal-specificity claim requires both contrasts to have 98% simultaneous paired intervals wholly below zero, with family-wise error controlled at 2% by a max-absolute-bootstrap procedure over the two contrasts. The absolute `Delta_LL,renal` interval and ten-repeat direction count remain descriptive evidence of replication, not a substitute for the specificity contrasts. LDL and vitamin D are negative-control comparators for generic biomarker augmentation, not negative controls for every possible biological pathway.

Secondary estimands are paired Brier differences, AUC differences from mean repeated held-out predictions, and fixed 10% capacity outcome differences for each extension versus M0 and for renal versus each nonrenal extension. Capacity ranking is within held-out fold, with the inherited stable-tie and floor-plus-largest-remainder allocation, selecting exactly `floor(0.10*|S_C|)` positions (with deterministic remainder allocation) per repeat. Capacity is not permitted to upgrade a specificity claim unless its pre-specified gate passes.

Use 4,000 participant bootstrap resamples with seed `520241`. Each resample carries all four predictions, selection indicators, outcomes, and the two specificity contrasts together. Use simultaneous percentile intervals for the two primary contrasts, formed from the maximum absolute studentized-free paired contrast deviation around the point estimate; report the unadjusted component intervals as diagnostics. No split regeneration, model refitting, or feature selection occurs inside the bootstrap. The primary two-contrast multiplicity rule is frozen before execution; all other measures are clearly labeled descriptive.

## Decision gates and falsification

A **supportive renal-specificity** result requires: (1) both simultaneous 98% specificity intervals are wholly below zero; (2) at least 8 of 10 repeat-specific renal-versus-M0 log-loss differences are negative; (3) Mrenal has no calibration degradation beyond inherited margins of 0.10 for absolute intercept/slope degradation and 0.002 for absolute CITL degradation; (4) all anchor, convergence, finite-prediction, exact-capacity, and bootstrap checks pass; and (5) no prespecified adverse criterion is met. This supports only renal-marker-specific incremental predictive information within `S_C` under the horizon-conditioned internal protocol.

An **adverse renal-specificity** result is declared if either simultaneous specificity interval is wholly above zero, or renal log loss is adverse versus M0 in at least 8 repeats, or renal calibration degradation is wholly beyond a margin, with computation valid. This would falsify the proposed renal-specificity advantage under this operationalization; it would not prove that cystatin C has no kidney value in another population or outcome.

Otherwise the result is **inconclusive**. In particular, a renal gain with both specificity intervals crossing zero is not sufficient to claim renal specificity; a nonrenal gain does not prove generic persistence; and a capacity interval crossing zero cannot be presented as clinical benefit. Capacity may be reported using the inherited parent +5 outcome floor as a descriptive operational benchmark, but failure of that floor must not be relabeled as adverse specificity unless its dedicated adverse gate is met.

Falsification and robustness checks are frozen as follows. First, rerun the identical pipeline after permuting each added feature within training folds and independently permuting the corresponding held-out feature values using a deterministic seed; these null runs must destroy feature-outcome alignment while preserving marginal distributions and must not be used as the primary estimate. Second, repeat the primary contrasts with the feature labels exchanged among the three one-feature arms to detect implementation asymmetry. Third, verify that no arm-specific missingness or row filtering changes `S_C`, fold assignments, or M0 predictions. A failure of these checks invalidates computation and yields repairable/rejected validity rather than a scientific adverse finding.

## Interpretation and evidence limits

Supportive results would narrow the unresolved explanation toward renal-marker-specific information and justify a separately designed external replication using baseline-available predictors and clinically adjudicated kidney outcomes. They would not establish measured GFR, CKD chronicity, causality, benefit from ordering cystatin C, clinically useful thresholds, deployment, transportability to nonattenders, or benefit-risk superiority.

Adverse results would weaken the renal-specificity hypothesis and favor the interpretation that the parent's log-loss rescue may be a generic one-feature biomarker augmentation or selected-cohort artifact. Inconclusive results preserve the parent’s narrow log-loss evidence but leave specificity unresolved; they should not be upgraded by the parent result or by descriptive AUC/Brier movement.

The observed repeat interval is included in M0 as in the parent, so this remains horizon-conditioned rather than a baseline-deployable forecast. Complete-case selection, repeat attendance, and the inherited requirement for repeat cystatin C can induce selection bias. No measured filtration rate, adjudicated CKD timeline, assay traceability, ordering records, costs, competing-risk structure, external cohort, or clinical notes sufficient for adjudication is available in the bound evidence. Stronger claims require clinical expert review and an external, deployable-horizon decision study.

Only source bindings, code, aggregate anchors/results, and aggregate audit output may support or publish the candidate. Do not publish `eid`, participant rows, fold membership, individual predictions, bootstrap draws/weights, or private notes. Source files remain read-only; all projections and derived participant-level artifacts remain private and are not candidate support.

## What changed from the parent

The parent tested one continuous renal feature against M0 and found reproducible log-loss improvement but inconclusive fixed-capacity concentration. This child adds a pre-specified common-complete population and two matched one-feature nonrenal biomarker arms, direct LDL and vitamin D, while holding the parent comparator, outcome, horizon, folds, model family, capacity procedure, uncertainty size, and evidence boundaries fixed. The new primary estimands are paired renal-versus-negative-control log-loss contrasts with simultaneous multiplicity control. The central unresolved issue is therefore testable without attributing a generic biomarker gain to renal biology. Exact `S_C` anchors and final field-unit transformation rules remain to be established by the declared schema/header verification and execution; no result is claimed in advance.
