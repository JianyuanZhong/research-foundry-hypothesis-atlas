# Fixed-combined-eGFR profiles: separating stable first-recording propensity, discovery-day frequency, and same-day coding density

Status: prospective substantive child of [prior hypothesis]. No creatinine/cystatin profile–outcome association has been inspected or fitted. This child preserves the parent's renal population, P−/P0 profiles, day-30 origin, common N17/N18-free risk set, 10-year marginal estimand, competing-death analysis, support/matching/censoring gates, and clinical limits. It revises the observation-process test because UKB supplies first-appearance dates, not encounters.

## Scientific opening and bounded advance

The strongest inspected evidence supports three limited claims. Large eGFRcys-minus-eGFRcr differences are common in UK Biobank and have kidney and non-GFR predictors [K1]. In SPRINT, the difference was associated with frailty and broad adverse outcomes, so a combined equation can lose prognostic information [K2]. Administrative AKI coding can be insensitive and subgroup-dependent relative to creatinine-defined AKI [K3]. None establishes that equal-combined-eGFR negative discordance selectively predicts biological AKI, that first-appearance dates measure contact, or that a K-th broad code is exchangeable with N17.

The unresolved hypothesis is: among supported P− and P0 profiles at equal combined eGFR, P− has a larger 10-year contrast for first recorded N17 than for first recorded N18 and than for three profile-blinded summaries of nonrenal first appearances—total accumulation, distinct discovery-day frequency, and high-density same-day bundles—after measured pre-index first-appearance propensity is balanced.

The strongest rival has two observable parts and one unobservable part:

1. A stable first-recording propensity should persist from pre-index to post-index, raise the number of distinct discovery dates and B_K passage, and produce broadly similar P−/P0 contrasts across renal and nonrenal first appearances.
2. High-density coding should raise same-day bundle size and concentrate any N17 contrast on dates carrying many other newly appearing codes, even without more distinct discovery dates.
3. Actual healthcare contact, admission severity, testing, and disease onset are absent. They cannot be separated from morbidity or coding using these summaries.

The advance is therefore a bounded discrimination among *measured first-appearance patterns*, not proof of renal biology. A supportive result means “recorded N17 selectivity beyond measured pre-index propensity and broad date/bundle density”; it still requires encounter- and laboratory-adjudicated validation.

## Existing marker-blind feasibility evidence

The inherited full-file audit used age, sex, baseline date, all-position first-appearance pairs, and death only; it did not read creatinine, cystatin C, G, delta, P−/P0, or any profile association. Among 498,473 provisional common-history-free participants with a marker-blind 10-year eligibility proxy, training selected K=30 from {1,3,5,10,15,20,30}; held-out B30/mean-renal crude-risk ratios were 0.831 and 0.861. Test counts were approximately 1,962 N17, 1,857 N18, and 1,644 B30. This establishes broad pooled feasibility only. It does not establish final profile-window support, valid administrative completeness, or feasibility of the discovery-day and high-bundle comparators.

The global 1,938-code unseen universe is retained only as QA. Almost everyone had at least 1,852 globally unseen groups, so it is not a credible participant-specific trial denominator.

## Exact read-only bindings

Use UKB snapshot `[source checksum]`. These are ordinary CSVs, joined one-to-one on `eid`; verify hashes and headers before execution.

- `population`, `[internal dataset path]` ([source checksum]): `eid`, sex `31-0.0`, age `21022-0.0`.
- `assessment`, `[internal dataset path]` ([source checksum]): index `53-0.0`, centre `54-0.0`, grips `46-0.0`/`47-0.0`, waist `48-0.0`, BMI `21001-0.0`, ethnicity `21000-0.0`, smoking `20116-0.0`, diabetes `2443-0.0`, SBP `4080-0.0/.1`, DBP `4079-0.0/.1`.
- `biological_samples`, `[internal dataset path]` ([source checksum]): creatinine `30700-0.0`, cystatin C `30720-0.0`, CRP `30710-0.0`, urine albumin `30500-0.0`, urine creatinine `30510-0.0`, glucose `30740-0.0`, HbA1c `30750-0.0`.
- `health_outcomes`, `[internal dataset path]` ([source checksum]): 259 all-position code/date pairs `41270-0.[0..258]`/`41280-0.[0..258]`; 80 principal pairs `41202-0.[0..79]`/`41262-0.[0..79]`; death `40000-0.0`/`40000-1.0`; `41259-0.0` HESIN row-count summary for QA only.

Direct header checks confirmed every named field and all pair endpoints. Pair only equal array indices. Normalize uppercase alphanumeric codes and retain three-character groups matching `^[A-Z][0-9]{2}`. Exclude and count code-without-parseable-date and date-without-code. The inherited audit found 84 all-position and 35 principal code values without paired dates, but its earlier empty-string ancillary counter was invalid and removed without changing endpoints.

These files contain summary first appearances, not admission IDs, repeated diagnosis rows, provider/nation, tests, or outpatient renal measurements. A date with one or more first appearances is called a *discovery date*, never an encounter.

## Preserved renal population and estimand

Use baseline instance 0; age 40–69; valid sex/index; positive creatinine and cystatin C after unit verification; at least one grip; race-free 2021 eGFRcr >=60. Risk starts `S=index+30 days`. Exclude N17 on/before S and pre-S N18.5/N18.6/Z49/Z94.0/Z99.2/T86.1; the common state also excludes all N18 on/before S. A renal clinician must approve the failure/replacement set.

Compute race-free 2021 CKD-EPI eGFRcr, 2012 CKD-EPI eGFRcys, race-free 2021 combined eGFR `G`, and `delta=eGFRcys−eGFRcr`. Preserve P−: 85<=G<=95 and −18<=delta<=−12; P0: 85<=G<=95 and −3<=delta<=3. Generate age/sex-specific raw profiles by inversion. Require >=100/window in every sex×five-year-age stratum, both targets inside each observed-stratum convex hull, and the inherited raw-assay nearest-neighbour gate, repeated after diagnosis and calendar restrictions.

Preserve 1:1 matching without replacement: exact sex, five-year-age, assessment year; |G difference|<=1.5; 0.2 pooled-SD propensity-logit caliper. Use continuous age, G, centre, listed clinical covariates, and the transparent pre-index recording block below. Reject if either group loses >50%, fewer than 1,000 pairs remain, or any prespecified covariate/G/recording feature has |SMD|>0.10. Repeat matching in participant bootstraps.

Through S+10 calendar years classify N17-first, N18-first, same-day N17/N18 tie, death-first, death/renal tie, or event-free/censored. Preserve tie assignment/exclusion and principal-position sensitivities. Eligibility requires S+10 years<=verified participant-applicable administrative end C. An observed maximum date is not C; absent provider/export provenance, every clinical conclusion is inconclusive.

Primary estimands remain `theta17=log RR10(N17-first;P−/P0)`, `theta18`, and `D=theta17−theta18`, standardized over the same eligible cohort. Fit cause-specific Cox models and standardized CIFs for N17, N18, death, and ties, with splined G/delta, prespecified interaction, clinical covariates, and pre-index recording block. Report CIF, RD, RR, joint covariance, >=500 participant bootstraps, and matched Aalen–Johansen estimates. Fewer than 90% successful replicates is inconclusive. No post-index process is a renal adjustment variable.

## Transparent matched-specificity observation-process baseline

Freeze one participant-level 70/15/15 train/validation/test split before profile associations, seed 20260924, stratified only by sex and aggregate renal transition class. All threshold choices use training pooled outcomes without marker values or profile labels; freeze them before validation/test and before any profile association.

Define `V` as valid non-N17/N18 three-character groups from paired all-position fields. For each person, a post-S discovery is a V group whose first date is after S; groups sharing a date form one discovery-date bundle.

Pre-index recording block, all in [index−5 years,index), with [−2,0) and [−10,−5) sensitivities:

- distinct discovery dates, distinct groups, and groups per observed history-year;
- counts in [−5,−2) and [−2,0), their log ratio with pseudocount, and recency/none;
- median, 90th percentile, and maximum same-day bundle size;
- proportion of discovery dates with bundle >=2 and >=5;
- represented ICD-10 chapters;
- exact principal-pair confirmation proportion/none;
- assessment year and beginning of observed history.

Use prespecified restricted splines; missing history is not health. Report early-to-late rank correlation and late-window prediction from early-window features as a *persistence diagnostic*, not contact validation.

Freeze three commensurate broad outcomes:

1. **Accumulation `B_K`**: first passage to the K-th new nonrenal group. Choose K from {1,3,5,10,15,20,30} minimizing absolute difference between training 10-year CIF and pooled mean N17/N18 CIF; tie to smaller K. The audit predicts K=30 but final selection is rerun.
2. **Discovery frequency `F_L`**: first passage to the L-th distinct post-S discovery date. Choose L from {1,2,3,5,8,10,15,20} by the identical blinded incidence rule.
3. **Coding density `H_b`**: first post-S discovery date carrying at least b newly appearing nonrenal groups. Choose b from {2,3,4,5,8,10} by the identical rule; tie to larger b, which is more specific to density.

Death before each threshold competes; C censors. Fit each with the identical cohort, clock, covariates, standardization, matching, bootstrap, and effect scale as N17. Define `thetaK`, `thetaF`, `thetaH` and `Qx=theta17−thetax`.

Each comparator independently requires: >=200 events in each profile window; held-out pooled CIF between 0.5 and 2 times pooled mean renal CIF; both profile windows >=95% structurally able to reach K or L given exported dates; and no validation/test reselection. Failure makes that pathway inconclusive. Failure of F or H prevents a claim that the corresponding rival was excluded. Do not replace grids, populations, clocks, or horizons.

For N17 event context, count nonrenal groups first appearing on the N17 date using only paired all-position data. With frozen b, split N17 into low-density (`<b`) and high-density (`>=b`) first transitions, with death/N18 competing. Estimate `theta17-low`, `theta17-high`, and `Cbundle=theta17-high−theta17-low`. Require >=150 N17 events in each context overall and >=50/window; otherwise concentration is inconclusive. This is not conditioning the primary N17 result; it is a secondary competing-outcome decomposition.

Retain first discoveries in acute respiratory (J09–J18), injury/poisoning (S00–T14), ear/mastoid (H60–H95), and skin (L00–L99) as contextual comparison outcomes over the full cohort. Family-free subsets are sensitivities only. Non-significance never proves specificity.

## Substantive learned/mechanistic alternative

The transparent summaries discard code composition and assume a few scalar history features adequately represent persistence. Fit one matched-specificity, two-factor marked first-appearance model:

- From [index−10,index), form participant × (three-character group × recency bin [10,5), [5,2), [2,0.5), [0.5,0) × all-position/principal channel) sparse matrices. Apply a training-frequency threshold of 50. Fit nonnegative latent composition ranks 8/16/32 and seeds 20260924–20260926; choose by validation Poisson deviance and matched-component cosine stability >=0.80. Freeze loadings and top codes before naming components.
- Fit correlated participant latent factors `a_i` (persistent discovery-date intensity) and `b_i` (conditional bundle density). Infer/calibrate persistence using only early pre-index history to predict later pre-index history. At S, posterior factors may use all pre-index history but no post-index value.
- Post-S, model recurrent discovery-date intensity with a yearly piecewise-exponential frailty process driven by `a_i`; conditional bundle size with a zero-truncated negative-binomial mark model driven by `b_i`; and death as absorbing. Add N17 and N18 competing first-transition hazards with freely estimated loadings on the *pre-index-inferred* factors plus a direct G/delta surface. Do not update participant factors from post-S outcomes for estimand calculation.
- Jointly simulate 10-year standardized trajectories under P− and P0 while preserving baseline histories. Emit discovery days, bundle distribution, total groups, B_K/F_L/H_b probabilities, N17/N18/death CIFs, direct profile contrasts, factor loadings, and residual N17 selectivity after the two measured factors.

Compare scalar-only, scalar+latent composition, and full two-factor models on untouched test data: yearly discovery-day calibration, zero-count calibration, bundle quantiles/tails, B_K/F_L/H_b Brier score and calibration, N17/N18/death calibration, joint deviance, seed stability, and pre-index temporal transport. Retain the learned result only if calibration intercept absolute value <=0.10 and slope 0.8–1.2 for each sufficiently supported binary endpoint, observed/expected yearly counts 0.8–1.25 in at least 8/10 years, 90th bundle quantile error <=1 group or <=20%, cosine stability passes, and no Brier score is worse than the transparent model by >0.01. Otherwise it is diagnostic failure, not evidence for renal selectivity.

The model can reveal whether two stable measured first-appearance factors explain multiple endpoints and whether N17 retains a residual profile contrast. It cannot label `a_i` as healthcare contact, `b_i` as admission intensity, or the residual as biological AKI.

A transformer is deferred: only first dates are available, and the scientific uncertainty is day frequency versus bundle density rather than next-code prediction. Revisit only if the two-factor model fails held-out process targets and a preregistered sequence model materially improves those same targets. A latent true-GFR model is deferred without measured GFR or repeated-marker error data.

## Observable predictions and interpretation rules

All rules require verified field semantics and C, support/matching, comparator event/commensurability, calibration/convergence, >=90% bootstrap success, joint 95% intervals, and no material principal/tie or cause-specific/CIF reversal.

**Supportive for bounded recorded-N17 selectivity** requires:

- lower bounds of theta17 and D >0;
- matched/principal direction agrees;
- lower bounds of QK, QF, and QH >0;
- lower bound of `theta17-low−thetaH` >0 and upper bound of Cbundle < log(1.25), so an N17 excess is neither explained by broad density nor concentrated materially on high-bundle dates;
- the calibrated two-factor model retains a positive residual N17 profile contrast and no equally large N18 or broad-process contrast.

This supports external adjudication only. It does not exclude unmeasured contact or differential renal-code salience.

**Adverse / stable recording-propensity pattern** is supported when pre-index propensity transports adequately and one of these precise patterns occurs: thetaF and thetaK are positive with upper bounds of QF and QK <=0; or the two-factor persistent-intensity loading explains N17, N18, B_K, F_L, and multiple families with the residual N17 profile contrast interval including no clinically material advantage (upper bound <=log(1.25)). This is compatible with stable morbidity, contact, or capture; the data cannot choose among them.

**Adverse / high-density coding pattern** is supported when thetaH is positive with QH upper bound <=0 and Cbundle lower bound >log(1.25), especially if thetaF is near null with an interval excluding RR 1.25. This is compatible with admission/coding intensity or clustered disease presentation, not proof of either.

**Adverse to acute-versus-chronic renal selectivity**: D upper bound <=0, or precise similar theta17/theta18. Both renal theta upper bounds <=0 are adverse to both profile claims. A death-driven reversal is inconclusive for selectivity.

**Inconclusive** includes unverified C; support/matching failure; no admissible K/L/b; sparse context cells; Q intervals spanning clinically material alternatives; inability to validate pre-index persistence; learned-model instability/miscalibration; method disagreement without a calibrated pathway; or principal/tie reversal. An imprecise null does not refute a rival. Do not rescue findings by changing thresholds, profiles, windows, families, ranks, or exclusions.

## Scientific deliverable, compute, and solver outputs

The deliverable is newly estimated—not assumed—joint evidence comprising the renal N17/N18 contrasts, three commensurate broad contrasts, N17 bundle-context decomposition, pre-index persistence diagnostics, and calibrated two-factor process results, ending in one rule-linked conclusion.

Required outputs:

- `run-manifest.json`, `censoring-provenance.json`, `field-audit.json`, `cohort-flow.csv`
- `profile-support.json`, `matched-balance.csv`, `events-by-definition.json`
- `code-universe.csv`, `baseline-recording-features.csv`, `persistence-diagnostic.json`
- `threshold-selection.json` with all K/L/b training risks and frozen choices
- `commensurability-audit.json`, `cox-results.json`, `broad-process-results.json`
- `n17-bundle-context.json`, `family-results.json`, `latent-history-results.json`
- `marked-process-results.json`, `transition-contrasts.json`, `bootstrap-summary.json`
- `conclusion.json`, `report.md`

The verifier can check hashes/headers/joins/pairing, split and marker blinding, pre-index-only adjustment, threshold freezing, identical population/clock/death handling, event gates, calibration, bootstrap intervals, and conclusion-rule consistency. It must accept supportive, adverse, and inconclusive results when computed rules warrant them, and reject biological/contact claims. It cannot establish C, clinical AKI/CKD, contact/testing, coding intent, mechanism, transportability, benefit, or true filtration.

Estimated solver envelope: vectorized parse/checkpoint 0.5–1 hour (parent audit measured 410 seconds on 8 CPUs); cohort/matching/Cox/bootstrap 2–4 hours; threshold/context analyses 1–2 hours; latent marked-process fit and bootstrap 2–4 hours. Use <=16 CPUs, <=262,144 MiB, <=8 hours. CPU-first is adequate; one allocated A100 is optional only after profiling. No discovery execution of the scientific associations is authorized.

## Exactly three inspected works

[K1] Chen DC et al. *Cystatin C- and Creatinine-based Estimated GFR Differences: Prevalence and Predictors in the UK Biobank.* Kidney Medicine. 2024;6:100796. doi:10.1016/j.xkme.2024.100796. Relevant full-text XML excerpt inspected.

[K2] Potok OA et al. *The Difference Between Cystatin C- and Creatinine-Based Estimated GFR and Associations With Frailty and Adverse Outcomes: A Cohort Analysis of SPRINT.* American Journal of Kidney Diseases. 2020;76:765–774. doi:10.1053/j.ajkd.2020.05.017. Relevant PMC full-text excerpt inspected.

[K3] Zhang J et al. *Validation of Administrative Coding and Clinical Notes for Hospital-Acquired Acute Kidney Injury in Adults.* AMIA Annual Symposium Proceedings. 2021:1234–1243. PMID:35308921; PMCID:PMC8861756. Relevant full-text sections inspected; its US single-system performance is not transported to UKB.
