> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Baseline-only action estimand for repeat kidney testing: assumption-indexed threshold curves and fixed-capacity ranking

## Proposal status and lineage

This proposal is a meaningful child of assessed-valid `[prior hypothesis]`. It preserves that candidate's UK Biobank snapshot, one-to-one `eid` joins, first qualifying repeat-attender evidence boundary, baseline/repeat field definitions, and repeat creatinine-defined outcome. It changes the estimand in a substantive and clinically necessary way: the deployed policy is restricted to variables available at baseline, and the primary output is an assumption-indexed threshold curve plus fixed-capacity action-ranking contrasts, not a claimed clinical-utility threshold.

## Clinical question and advance

When an adult has a baseline creatinine-based eGFR in or near the normal-to-mildly-reduced range, does baseline cystatin-C/creatinine discordance identify people for whom a repeat kidney-function assessment should be prioritized, beyond a creatinine-only baseline rule?

The clinically consequential action is a repeat kidney-function assessment, potentially including cystatin C when the result could change a GFR-dependent decision. The available evidence supports repeat confirmation after an incidental low eGFR or other kidney abnormality and supports combined creatinine/cystatin-C estimation when creatinine-based GFR may be inaccurate and GFR affects a decision. It does not provide a validated, universal probability threshold or harm-to-benefit ratio for ordering a repeat test in this UK Biobank population. UK Biobank also lacks observed testing harms, costs, downstream treatment changes, measured GFR, adjudicated CKD, and patient-important outcomes.

Accordingly, the experiment will answer a narrower falsifiable question: across prespecified assumed action thresholds and prespecified testing capacities, does a baseline-only model containing cystatin-C/creatinine discordance rank future repeat creatinine-eGFR threshold crossings better than a baseline creatinine-only comparator? It will not infer that testing improves outcomes, that a particular threshold should be used clinically, or that a repeat eGFR threshold crossing is CKD.

The substantive advance over the parent is an explicitly deployable baseline information set and an action estimand that separates two questions that were previously conflated:

1. predictive ranking: who would be prioritized for a repeat assessment under a stated capacity or assumed exchange rate; and
2. clinical utility: whether ordering that assessment produces more benefit than harm.

Only the first is identifiable here.

## Evidence boundary and exact population

Use UK Biobank rectangular phenotype export `ukb672073`, snapshot `[source checksum]`.

Join each table horizontally one-to-one on `eid`, checking that overlapping fields agree, as required by `datasets/ukb/metadata.json`. Read only these ordinary source files and fields.

- `biological_samples`, source `[internal dataset path]`, catalog schema `datasets/ukb/table-c6b666d905f3b02f.json`: `eid`, baseline creatinine `30700-0.0`, repeat creatinine `30700-1.0`, baseline cystatin C `30720-0.0`, repeat cystatin C `30720-1.0`.
- `assessment`, source `[internal dataset path]`, catalog schema `datasets/ukb/table-901ef6c7ddce2d51.json`: `eid`, baseline date `53-0.0`, first-repeat date `53-1.0`, baseline age `21003-0.0`, first-repeat age `21003-1.0`.
- `population`, source `[internal dataset path]`, catalog schema `datasets/ukb/table-38565c9e35e7cb6c.json`: `eid`, baseline sex `31-0.0`.

The retrospective validation population is the inherited selected first-repeat-attender cohort, constructed in this order:

1. `B`: valid baseline sex, baseline age, baseline date, baseline creatinine, and baseline cystatin C, with positive finite laboratory/age values; retain the parent anchor `B=468,887` after the joined population anchor `502,370`.
2. `R`: within `B`, require a first-repeat date and positive finite repeat age, repeat creatinine, and repeat cystatin C, and require elapsed time `(53-1.0 - 53-0.0)/(365.25 days)` inclusively between 2 and 8 years. Retain `R=16,546`.
3. `S_A`: within `R`, require baseline `eGFRcr_0 >= 60` using the race-free 2021 CKD-EPI creatinine equation. Retain `S_A=16,372`, with 309 repeat outcomes.

The parent anchors must be reproduced exactly, including elapsed range `2.1081451061` to `6.1136208077` years, baseline minimum eGFRcr `60.0659423121`, borderline stratum `[60,75)` with 1,038 participants and 140 events, and far stratum `>=75` with 15,334 participants and 169 events. This is an evidence-availability boundary, not a claim that all people in the source population would attend a repeat visit.

Creatinine is converted from micromoles/L to mg/dL by division by 88.4. Define

- `eGFRcr_0` and `eGFRcr_1` by race-free 2021 CKD-EPI creatinine equations;
- `eGFRcys_0` by the inherited cystatin-C-only equation;
- `Z = log(eGFRcys_0 / eGFRcr_0)`;
- primary outcome `Y = I(eGFRcr_1 < 60)`.

`Y` is a repeat creatinine-equation threshold crossing over a variable 2–8-year assessment interval. It is not measured GFR, adjudicated CKD, persistent CKD, or a patient-important renal outcome. Repeat cystatin C is required only to preserve the inherited complete-repeat evidence boundary; it is not a baseline predictor and is not used to define the primary outcome.

## Baseline-only policies and estimands

No predictor may use `53-1.0`, repeat age, repeat creatinine, repeat cystatin C, elapsed repeat time, visit attendance, or any other future-known variable. The model's baseline deployment feature set is fixed before outcome analysis.

### Comparator and augmented policy scores

Fit two prespecified, fold-aware models using only `S_A` baseline variables.

- `M0` (creatinine-only comparator): sex, baseline age, and baseline eGFRcr, represented by the inherited fixed four-column natural cubic spline basis for age and eGFRcr plus sex. No time-to-repeat variable is included.
- `M1` (discordance-augmented): `M0` plus one training-fold-standardized linear column `Z`.

Use the inherited fixed L2 logistic-regression configuration, no tuning, no class weighting, and the ten inherited outcome-stratified round-robin five-fold repeats. All knots, spline boundaries, centering/scaling, and model fitting are learned within training folds. Produce out-of-fold baseline risk estimates `p0_i` and `p1_i` for the same participant in each repeat.

For interpretability, also predefine two non-model rules, evaluated without tuning:

- `Rule-Cr75`: prioritize if baseline `eGFRcr_0 < 75`.
- `Rule-Discordant`: prioritize if `eGFRcr_0 >= 75` and `eGFRcys_0 < 60`, or if `eGFRcr_0 < 75` and `eGFRcys_0 < eGFRcr_0`; the exact Boolean expression must be frozen before outcomes are inspected and reported separately from model-based results.

The rules are descriptive baseline prioritization rules, not recommendations.

### Primary action estimand: fixed-capacity prioritization

For each model `m` and capacity `q`, let `T_m(q)` be the top `ceil(q * n)` participants by out-of-fold risk, with ties resolved by participant-independent stable ordering fixed before analysis. Use the prespecified capacity grid `q = 0.01, 0.02, ..., 0.20`, plus the inherited 10% capacity point.

Report:

- event capture `C_m(q) = sum(Y_i * I(i in T_m(q)))`;
- event fraction captured `C_m(q)/sum(Y_i)`;
- positive predictive value among prioritized participants;
- incremental captured events `DeltaC(q) = C_M1(q) - C_M0(q)`;
- incremental capture curve across the complete capacity grid.

The primary contrast is the full `DeltaC(q)` curve, not a single capacity chosen after seeing outcomes. A clinically interpretable favorable result would require a prespecified practically meaningful positive region, uncertainty excluding zero across that region, and replication across fold seeds; no single isolated capacity point is sufficient. The inherited `q=0.10` point is reported for continuity, but the old `+5` event gate is not silently relabeled as clinical utility.

### Secondary action estimand: assumption-indexed threshold curve

For a threshold probability `p_t`, define the action `A_m(p_t)=I(p_m >= p_t)`. Report the standard decision-curve quantity

`NB_m(p_t) = TP_m(p_t)/n - FP_m(p_t)/n * p_t/(1-p_t)`

and the incremental curve `DeltaNB(p_t) = NB_M1(p_t)-NB_M0(p_t)`. Also report test-all and test-none reference curves. Use the fixed grid

`p_t in {0.001, 0.0025, 0.005, 0.0075, 0.010, 0.015, 0.020, 0.030, 0.040, 0.050, 0.075, 0.100, 0.150, 0.200}`.

The ratio `p_t/(1-p_t)` is an assumed relative harm-to-benefit exchange rate. It is not estimated from UK Biobank, and no threshold is selected as clinically preferred. The curve is therefore called an **assumption-indexed threshold curve** in the primary interpretation. It may be displayed as a mathematical decision-curve analysis, but it must not be described as demonstrated net clinical benefit. Thresholds above the observed event prevalence are retained to show where any testing policy becomes dominated under the assumed exchange rate; they are not discarded post hoc.

As a robustness check, calculate standardized net benefit after restricting to the borderline baseline eGFRcr stratum `[60,75)` and the far stratum `>=75`, with the same frozen grid and simultaneous uncertainty. These are subgroup descriptions, not evidence that clinicians should use different thresholds.

## Uncertainty and calibration

The primary uncertainty procedure is a paired participant bootstrap applied to the ten-repeat out-of-fold prediction arrays, preserving the paired M0/M1 predictions, outcome, and baseline stratum. Use seed `520241`, 4,000 draws for continuity with the parent, and no outcome-informed threshold or capacity selection. For every draw, recompute the entire prespecified capacity and threshold grids. Construct two-sided simultaneous 98% max-|T| bands separately for:

1. the complete `DeltaC(q)` capacity curve;
2. the complete `DeltaNB(p_t)` threshold curve; and
3. calibration contrasts and the two baseline strata.

Because this conditional bootstrap does not refit models, label its bands conditional on the fitted cross-fitting mechanism. Also report between-repeat variation and the minimum/maximum number of selected participants at every capacity. A sensitivity execution may refit within bootstrap samples if resources permit, but it cannot replace the prespecified conditional analysis or change the interpretation.

Report calibration-in-the-large, calibration slope, Brier score, and observed-versus-predicted risk by prespecified baseline eGFRcr strata and risk bins. Calibration is a prerequisite for interpreting probability-indexed curves but cannot establish action benefit. Require at least 1,000 participants and 20 events in each primary stratum before making a stratum-level directional statement; otherwise report it as unsupported.

## Exact falsification and negative controls

The following falsification criteria are frozen before inspecting action curves.

1. **Label-null refit:** independently permute `Y` within the frozen borderline/far strata for 200 permutations, reconstruct outcome-stratified folds under each permuted label vector, and refit both models with training-only preprocessing. Recompute every capacity and threshold contrast. The observed `DeltaC(q)` and `DeltaNB(p_t)` curves must be compared with simultaneous empirical null envelopes. A claimed incremental signal is falsified if the observed curve is compatible with the null envelope throughout the prespecified practically relevant region, or if its apparent advantage occurs only at an isolated grid point without repeat consistency.
2. **Predictor-null permutation:** within baseline eGFRcr deciles and sex, permute `Z` while preserving its marginal distribution and the outcome. Refit M1. Incremental curves should collapse toward zero; a persistent large advantage indicates leakage, implementation error, or residual dependence created by the permutation scheme and blocks interpretation.
3. **Outcome-direction check:** reverse the event label to `1-Y` and rerun the frozen pipeline as a negative-control target. A clinically specific discordance action claim cannot rely on a selective gain that appears equally or more strongly for the reversed artificial label.
4. **Threshold-selection check:** publish all prespecified grid points, not the best point. A result is inconclusive if its direction changes materially across adjacent thresholds, capacities, fold seeds, or baseline strata, or if the claimed conclusion requires a post hoc threshold/capacity.
5. **Time-leakage sentinel:** verify by code and audit that no column derived from `53-1.0`, repeat age, repeat biomarkers, attendance, or elapsed time enters either baseline model. A deliberately leaked model may be run only as a debugging sentinel and must never be compared as an action policy or used in conclusions.
6. **Outcome-definition sensitivity:** repeat the descriptive curves for a prespecified repeat cystatin-C-derived eGFR threshold outcome, clearly labeled secondary and assay-dependent. Discordance-specific claims are weakened if they disappear or reverse under this sensitivity, but this sensitivity cannot establish measured GFR or CKD.

A computational falsification failure is a blocking result, not evidence for clinical utility. Permutation compatibility is evidence against a predictive incremental signal under that null, not proof that the null is biologically true.

## Supportive, adverse, and inconclusive outcomes

- **Supportive for baseline predictive prioritization:** M1 has better calibration and a positive `DeltaC(q)` over a prespecified contiguous capacity region, with the simultaneous 98% lower band above zero there, the result survives both label-null and predictor-null checks, and the direction is stable across repeats and strata. The threshold curve may show positive `DeltaNB` for some assumed `p_t`, but this remains assumption-indexed and is not a clinical-utility claim.
- **Adverse to the incremental discordance hypothesis:** M1 has a reproducibly negative capacity contrast or calibration deterioration with simultaneous uncertainty, or the predictor-null/label-null checks reveal that the apparent gain is compatible with artifact. A negative result would be scientifically useful and would argue against prioritizing repeat testing using this discordance in this evidence boundary.
- **Inconclusive:** curves are wide, cross zero over the clinically relevant capacity range, differ by repeat or stratum, fail support gates, or show only isolated threshold/capacity improvements. Inconclusive results do not justify a threshold recommendation.

Even a supportive computational result would establish only conditional baseline risk ranking for the selected repeat-attender cohort and the repeat eGFRcr threshold outcome. It would not establish benefit from testing, cost-effectiveness, patient acceptability, downstream treatment benefit, CKD diagnosis, measured GFR accuracy, assay interchangeability, causality, or transportability.

## Why no clinically justified net-benefit threshold is claimed

The public guidance consulted for this proposal supports repeating an abnormal kidney marker to establish chronicity and using combined creatinine/cystatin C when creatinine-based GFR is inaccurate and GFR affects a decision. It does not identify a universal probability at which repeat testing should be ordered, nor an empirically validated harm-to-benefit ratio applicable to this cohort. The decision-curve literature defines how to translate an externally justified threshold probability into a net-benefit curve; it does not supply the threshold for this action.

The UK Biobank sources contain laboratory measurements, assessment dates/ages, sex, and the inherited repeat outcome, but no testing cost, adverse-event burden, false-positive consequence, patient utility, clinician action, treatment effect, or adjudicated CKD/GFR endpoint. In addition, the selected outcome is observed after a variable future interval and the cohort is selected on complete first-repeat attendance. Consequently, numerical threshold curves are identifiable as sensitivity analyses indexed by assumptions, whereas a clinically justified net-benefit threshold is not identifiable from these data. Any future clinical-utility claim requires external preference/cost information, clinical adjudication, and prospective validation in a population in which baseline deployment and the testing decision are observed.

## Computation, provenance, and privacy

All source files remain read-only. Derived projections, participant-level predictions, fold assignments, bootstrap indices, and permutation arrays must remain private workspace/job artifacts and must not be published. Published support should contain only aggregate curves, uncertainty bands, anchors, hashes, model specifications, and audit outputs. No `eid`, clinical note, participant row, or private source projection may be sent to public literature or web-search services.

A verifier can check source snapshot/hash bindings, exact join and cohort anchors, baseline-only feature inclusion, formulae, fold isolation, policy definitions, threshold/capacity grids, null completion, bootstrap arithmetic, and whether textual conclusions match the reported curves and gates. It cannot establish clinical benefit, acceptable testing harms, CKD adjudication, measured GFR accuracy, or transportability; those require expert review or another study.

## Public evidence provenance

Relevant frozen public-search evidence is represented by source-cache records from Europe PMC/OpenAlex/web search, including the KDIGO 2024 themes of repeat confirmation/chronicity and combined eGFRcr-cys when GFR affects a decision, and Vickers, Van Calster, and Steyerberg, “Net benefit approaches to the evaluation of prediction models, molecular markers, and diagnostic tests” (BMJ 2016; DOI `10.1136/bmj.i6`, OpenAlex work `W2226880313`). Search snippets and metadata are not treated as substitutes for unavailable full guideline text. No private dataset content was included in any public query.
