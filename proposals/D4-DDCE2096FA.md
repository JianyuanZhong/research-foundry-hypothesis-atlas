> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

TITLE
Cross-marker persistence test of baseline cystatin-C/creatinine discordance and protocol-measured renal biomarker deterioration at UK Biobank repeat assessment

SCIENTIFIC QUESTION AND CLINICAL IMPORTANCE
When cystatin-C is unexpectedly high relative to creatinine at one protocol visit, does it identify a reproducible renal signal that is subsequently expressed in creatinine, or does the discrepancy mainly regress toward the mean or track non-GFR determinants? The distinction matters because cystatin-C/creatinine discordance is common and may alter CKD staging, drug dosing, testing, and referral, yet a single discrepant pair can be driven by muscle mass, diet, adiposity, thyroid disease, smoking, steroids, tubular-secretion inhibitors, assay error, or acute biological variation. An observational UK Biobank result cannot establish benefit from ordering cystatin-C or changing care. It can determine whether discordance merits external prospective validation as a monitoring signal among repeat attenders.

EVIDENCE-SUPPORTED CLAIM VERSUS UNTESTED CLAIM
Supported before this experiment: Chen et al. studied 468,969 UK Biobank participants with baseline serum cystatin-C and creatinine, found large eGFR discrepancies to be common, and identified numerous demographic, lifestyle, disease, medication, and body-composition correlates. The paper reports Siemens latex-enhanced immunoturbidimetric cystatin-C (interassay CV 1.1%) and Beckman Coulter enzyme-based creatinine (CV 2.0%). It explicitly describes muscle mass, activity, meat intake, chronic illness, and tubular-secretion inhibitors as non-GFR determinants of creatinine, and obesity, hypothyroidism, smoking, and steroid use as non-GFR determinants of cystatin-C. This supports biological ambiguity of discordance, not longitudinal renal decline (Chen DC et al., Kidney Medicine 2024; PMCID PMC10986041; DOI 10.1016/j.xkme.2024.100796; inspected full-text XML source-id [source checksum]).

Untested hypothesis: among UK Biobank participants with protocol measurements at baseline and repeat assessment, a higher baseline cystatin-C residual conditional on creatinine, age, and sex predicts a higher repeat creatinine conditional on baseline creatinine and elapsed time. This cross-marker prediction will remain after measured confounder adjustment, repeat-attendance weighting, and a calibrated no-decline measurement-error simulation, and will be stronger than associations with prespecified nonrenal negative-control biomarkers. The symmetric result—creatinine unexpectedly high conditional on cystatin-C predicting repeat cystatin-C—is secondary and must agree in direction for a claim about a shared renal signal.

The strongest possible conclusion is deliberately narrower than “true GFR decline”: baseline cross-marker discordance contains a longitudinally persistent component associated with later protocol-measured renal biomarkers in eligible repeat attenders. Measured GFR, clinical adjudication, external cohorts, and an intervention study would be required to claim kidney-function decline, transportability, decision benefit, or causality.

EXACT DATA BINDINGS AND PROVENANCE
Dataset snapshot: UKB rectangular phenotype export ukb672073, catalog snapshot [source checksum]. All sources are ordinary CSV files, not archive members. Horizontal one-to-one joins use eid; duplicate eid or disagreement in overlapping fields is a fatal integrity error.

1. Table biological_samples, schema datasets/ukb/table-c6b666d905f3b02f.json, source [internal dataset path], [source checksum]:
- eid: join key.
- 30700-0.0 and 30700-1.0: serum creatinine at instances 0 and 1.
- 30720-0.0 and 30720-1.0: serum cystatin-C at instances 0 and 1.
- 30670-0.0 and 30670-1.0: urea, a renal-related secondary outcome only, not an independent validation of GFR.
- 30780-0.0 and 30780-1.0: LDL direct, negative-control biomarker.
- 30890-0.0 and 30890-1.0: vitamin D, negative-control biomarker.
- Optional baseline confounder biomarkers only after field/unit certificate: 30600-0.0 albumin, 30710-0.0 CRP, 30750-0.0 HbA1c, 30880-0.0 urate; corresponding instance-1 columns are available for secondary descriptive analyses.
The exact headers for all primary renal and negative-control instance pairs were inspected. A frozen authoritative field/unit certificate is a pre-execution gate because the local catalog states that per-field units are absent. No eGFR equation may be run until creatinine and cystatin-C identity and units are certified. Raw log-analyte models remain computable after identity/range validation and are primary so equation choice cannot create the main result.

2. Table assessment, schema datasets/ukb/table-901ef6c7ddce2d51.json, source [internal dataset path], [source checksum]:
- eid: join key.
- 53-0.0 and 53-1.0: assessment dates; elapsed years = (date1-date0)/365.25. Instance number is never treated as elapsed time.
- 54-0.0 and 54-1.0: assessment centers.
- 21003-0.0 and 21003-1.0: age at assessment.
- 21001-0.0 and 21001-1.0: BMI.
The exact source header was inspected for these fields. Baseline covariates available in this table and to be used only with field-specific coding certificates include smoking 20116-0.0, alcohol frequency 1558-0.0, diabetes proxy 2443-0.0, blood-pressure fields 93/94/4079/4080 at instance 0, waist/body-size fields 48/49/50 at instance 0, medication category arrays 6177-0.* and 6179-0.*, and treatment/medication code array 20003-0.*. The compiler must enumerate every array column from the schema rather than assume a single array element.

3. Table population, schema datasets/ukb/table-38565c9e35e7cb6c.json, source [internal dataset path], [source checksum]:
- eid: join key.
- 31-0.0: sex, locally approved coding 0 female, 1 male.
- 21022-0.0: age at recruitment in years, used only as an integrity check against 21003-0.0.

No negative numeric value is globally recoded. The UKB metadata explicitly says negative-code meanings are field-specific and instance is not elapsed time. Each categorical variable requires a frozen coding map; uncoded values remain explicit unknown categories. Nonpositive creatinine/cystatin-C, impossible dates, nonpositive intervals, duplicate eid, or out-of-certified-range analytes trigger exclusion with an audited reason, never silent winsorization.

POPULATION AND TEMPORAL BOUNDARIES
Source population: all rows in biological_samples, left-joined one-to-one to assessment and population by eid; report source rows, duplicates, unmatched keys, and overlapping-field agreement before filtering.

Baseline pool for selection modeling: participants with valid baseline date, sex, age, creatinine, and cystatin-C at instance 0.

Primary analysis population: baseline-pool participants with valid instance-1 date, creatinine, and cystatin-C; elapsed time strictly positive and prespecified as 2.0 through 8.0 years inclusive. The 2–8-year restriction prevents near-contemporaneous repeats and very long extrapolation; report all interval quantiles and rerun with every positive interval as sensitivity. Require both repeat renal markers even though each cross-marker model uses one outcome, so the two co-analysis samples are identical and cannot differ through assay-specific selection. Do not exclude CKD, diabetes, medication use, extreme discordance, or changes in center unless a value fails a certified validity rule.

The target population is this eligible repeat-attender population. No estimate is called population-representative for UK Biobank or the United Kingdom.

EXPOSURE, OUTCOMES, AND ESTIMANDS
Use natural logs after certified positivity/range checks. All transformations, splines, residualization, standardization, imputation, and attendance models are fitted within training folds only.

Primary discordance exposure R_cys|cr: fold-specific residual from a restricted cubic spline regression of baseline log(cystatin-C) on baseline log(creatinine), baseline age, sex, age-by-sex, and baseline center. Standardize residual by the training-fold SD. Positive values mean cystatin-C is higher than expected for creatinine/demographics; this operationalizes the clinically concerning lower-cystatin-eGFR direction without introducing an eGFR formula into the primary test.

Symmetric exposure R_cr|cys: residual from the analogous fold-specific regression of baseline log(creatinine) on log(cystatin-C), age, sex, interaction, and center; positive means creatinine is higher than expected.

Primary cross-marker outcome model P1: repeat log(creatinine). Baseline comparator contains baseline log(creatinine), age, sex, baseline center, repeat center/change indicator, elapsed years (restricted cubic spline), and the prespecified measured-confounder set. The tested term is R_cys|cr. Report adjusted coefficient per 1-SD residual, robust 95% CI, partial R-squared, and nested out-of-fold change in RMSE and log predictive density.

Symmetric model P2: repeat log(cystatin-C), conditioned on baseline log(cystatin-C) and the same covariates, testing R_cr|cys. P2 is secondary but directional agreement is necessary to interpret P1 as evidence of a shared renal signal.

Shared-signal secondary model: define fold-standardized baseline log markers, M0=(zlogCr0+zlogCys0)/2 and D0=(zlogCys0-zlogCr0)/2. Predict identically standardized M1 from M0, D0, D0 squared, interval, demographics, centers, and confounders. This is supportive only because algebraic transformation cannot add information beyond both component markers.

Secondary outcomes: annualized changes in each raw log marker and urea, and equation-based eGFRcr/eGFRcys/combined eGFR only after certified units and equation implementation tests. Change scores can illustrate regression to the mean but can never establish the primary result.

Primary estimand: adjusted within-repeat-attender association between one training-fold SD higher R_cys|cr and repeat log(creatinine), conditional on baseline creatinine. This is associational, not causal. Incremental-prediction estimands compare preregistered marker-alone models with the residual-added model in held-out folds. “Beyond either marker alone” means improvement versus the corresponding single-marker baseline model; it does not mean discordance contains information beyond a model already given both exact marker values.

CONFOUNDING AND MISSINGNESS
Minimal adjustment fixed before outcomes: baseline age, sex, baseline log outcome marker, date/season, baseline center, repeat center/change, elapsed time, BMI, waist circumference, smoking, diabetes proxy, systolic BP, albumin, CRP, HbA1c, and urate. Add medication indicators for systemic steroids and creatinine tubular-secretion inhibitors (at minimum trimethoprim where identifiable), and antihypertensive/diabetes drugs only if exact UKB coding maps are frozen before analysis. If medication code identities cannot be certified, execute the minimal model without them, label medication confounding unresolved, and prohibit a “clinically actionable” conclusion. Never infer absence from one empty array element; scan all enumerated 20003/6177/6179 instance-0 array columns.

For covariates, report missingness separately for baseline assays, repeat attendance/date, repeat assay, and each covariate. Main inference uses multiple imputation within analysis folds (including exposure components, outcome-free at prediction time, attendance predictors, and missingness indicators where appropriate), with at least 20 imputations; complete-case is sensitivity. Outcomes and primary exposure markers are not imputed.

Repeat-attendance selection: among the baseline pool, fit a fold-specific logistic model for membership in the primary analysis population using all certified baseline variables above plus date and center. Use stabilized inverse-odds/attendance weights in a sensitivity analysis, truncated at prespecified 1st/99th percentiles; report positivity, effective sample size, standardized differences before/after weighting, and compare weighted/unweighted coefficients. This can address selection on measured variables only. If nonattendance outcome data are absent, MNAR sensitivity uses delta shifts in unobserved repeat outcomes over a clinically interpretable grid; no transportability claim follows.

ANALYSIS
1. Produce a cohort-flow certificate with actual full-row counts and reason-specific exclusions. No sampling is allowed for feasibility counts.
2. Describe baseline distributions and compare baseline pool, eligible repeat attenders, repeat attendees missing either renal assay, and nonattenders.
3. Use participant-level 10-fold cross-fitting, stratified by sex, baseline center, and discordance decile where feasible. All residualization and preprocessing are training-fold operations. Cluster-robust sensitivity by baseline center; bootstrap participants (at least 1,000 replicates) for prediction metric CIs.
4. Fit P1 and P2 using flexible but preregistered restricted cubic splines for baseline marker, age, interval, BMI, waist, BP, and laboratory covariates. Do not select covariates by p-values.
5. Compare single-marker baseline versus residual-added models only out of fold. Report absolute metrics and CIs, not merely p-values. A tiny statistically significant gain is not clinically actionable.
6. Assess nonlinearity and both tails with D0 spline/categorical sensitivity, but continuous P1 is primary. Report effect modification by sex, baseline combined-eGFR category, diabetes, BMI, smoking, and steroid use as exploratory interactions with multiplicity control and no subgroup implementation claim.

REGRESSION-TO-MEAN AND MATHEMATICAL-COUPLING STRESS TESTS
A naive regression of marker change on baseline eGFR difference is prohibited because the same noisy baseline observations occur on both sides. P1 instead tests the other marker at follow-up while conditioning directly on its own baseline value; fold-residualization reduces deterministic collinearity. This does not eliminate correlated assay/biological errors.

Calibrated null simulation: estimate the four-marker baseline/repeat covariance and same-marker repeat reliabilities in the eligible cohort, then simulate at least 10,000 datasets under a no-person-specific-decline null that preserves baseline levels, marginal variances, cross-marker covariance, follow-up interval structure, center effects, and estimated assay/within-person error. Run the entire fold-residualization and P1/P2 pipeline in each simulation. The observed coefficient and incremental prediction gain must exceed the 97.5th percentile of this coupling/measurement-error null. Because two visits cannot identify true trajectory separately from all error components, repeat simulation across a grid of plausible correlated-error fractions; failure anywhere in the prespecified plausible grid makes the result inconclusive rather than supportive.

Directional decomposition: for positive R_cys|cr, report repeat cystatin-C normalization and cross-marker creatinine movement separately. A result driven only by cystatin-C moving toward its mean, without cross-marker worsening in creatinine, falsifies the persistent shared-renal-signal interpretation. Likewise P2 must not be explained solely by creatinine normalization.

NEGATIVE CONTROLS AND PLACEBOS
1. Negative-control outcomes: repeat LDL direct (30780-1.0) conditioned on 30780-0.0, and repeat vitamin D (30890-1.0) conditioned on 30890-0.0, using the same eligibility, folds, time/center adjustment, and residual exposures. These are not guaranteed null biologically; associations diagnose broad health/selection/non-GFR pathways. If either standardized residual association is as large as or larger than P1 after accounting for uncertainty, specificity is adverse and renal interpretation is prohibited.
2. Permutation placebo: permute residual exposure within training-fold strata of sex, age decile, baseline center, baseline outcome-marker decile, and interval decile; refit at least 1,000 times. Nominal significance without separation from this null is falsification.
3. Date placebo: after conditioning on baseline date and center, residual discordance should not predict elapsed follow-up interval. A material association flags invitation/selection structure and requires weighted results to agree.
4. Same-marker change placebo: demonstrate how much naive change-score associations attenuate or reverse under cross-marker ANCOVA and the calibrated null; do not treat the naive estimate as evidence.
5. Center/batch sensitivity: repeat among participants with the same assessment center and after excluding one baseline center at a time. Strong center dependence is adverse.

FALSIFICATION AND INTERPRETATION RULES
Supportive for a longitudinally persistent cross-marker signal only if all are true: (a) P1 has the hypothesized positive direction with a robust CI excluding zero; (b) its coefficient and prediction gain exceed the calibrated coupling null; (c) P2 agrees directionally and is not materially inconsistent with P1 on standardized scales; (d) findings are stable to flexible adjustment, complete-case/imputation, interval windows, and attendance weighting; (e) positivity/effective sample size remain acceptable; (f) negative controls are materially weaker; and (g) no result is driven only by own-marker normalization or a center.

Adverse/falsifying: P1 is null or negative with a CI excluding the smallest scientifically relevant effect; P1 lies within the coupling null; only the same marker normalizes; P2 conflicts; negative controls equal/exceed the renal signal; permutation/placebo is not passed; or the estimate is center-specific. Conclude that baseline discordance did not provide specific evidence of later cross-marker renal biomarker deterioration in eligible repeat attenders. This negative result is scientifically useful.

Inconclusive: too few eligible pairs, wide intervals spanning meaningful benefit/harm, nonpositivity or severe weight instability, uncertified field units/codes, implausible ranges, simulation conclusions dependent on unidentified error assumptions, or materially different imputation/selection results. Do not collapse inconclusive into no association.

Predeclare the smallest scientifically relevant standardized effect before outcome modeling (provisional 0.05 SD in repeat log marker per 1-SD discordance residual) and require its CI to exclude both zero and clinically trivial values for any importance claim. Statistical support without meaningful magnitude is described as detectable but clinically small.

COMPUTATIONALLY CHECKABLE VERSUS NOT CHECKABLE
Automatically checkable: source hashes and headers; eid uniqueness/join counts; date arithmetic; cohort flow; exact column use; fold isolation; residual definitions; model formulas; missingness; weights; simulations/permutations; estimates/CIs; prediction metrics; negative controls; and whether the submitted conclusion follows the above result branches.

Not automatically establishable: that analyte change equals measured GFR decline; whether an observed magnitude changes CKD staging or drug dosing appropriately; diagnostic coding validity; completeness of medication exposure; biological meaning of non-GFR determinants; clinical actionability; generalizability beyond repeat attenders; or benefit from testing/intervention. These require authoritative metadata, nephrology/clinical pathology review, measured-GFR or externally adjudicated outcomes, external validation, and potentially a prospective impact study.

FEASIBILITY GATE
The schema and exact headers establish availability of baseline/repeat creatinine, cystatin-C, dates, centers, demographics, and repeated negative-control biomarkers. Before model execution, a resource-managed full-row pass must record exact eligible counts, interval distribution, analyte ranges, nonpositive/uninterpreted values, duplicates, and join failures. If fewer than 1,000 valid paired participants remain, if either primary repeat assay is structurally absent, or if field identity/units cannot be authoritatively certified, stop and report infeasibility rather than changing endpoints. A pivot to another protocol-measured longitudinal biomarker requires a new Lead proposal.
