# Five-year renal-vulnerability interaction from creatinine–cystatin C discordance and grip

## Successor decision and unresolved claim

Parent: `[prior hypothesis]`.

This is a targeted repair, not a new topic. The expert seed and the parent establish the physiological motivation and a falsifiable UK Biobank question, but neither establishes that discordance predicts a community renal outcome, that an N17 code is adjudicated AKI, or that the association is renal-specific. The strongest available evidence is therefore only mechanistic motivation from the inspected critical-illness comparison of creatinine, cystatin C and measured kidney function; it does not establish this population association, code validity, or clinical utility.

The unresolved claim is:

> In UK Biobank participants with valid baseline creatinine, cystatin C and bilateral grip, among those without a previously recorded paired N17/N18 hospital diagnosis, the five-year cumulative incidence of a first subsequently recorded paired N17 diagnosis has a positive interaction between lower cystatin-C-minus-creatinine eGFR discordance and lower grip strength, after conditioning on creatinine eGFR, age, sex and BMI.

This is a prognostic association with a recorded hospital-code endpoint. It is not a claim about true filtration, muscle mass, AKI stage, causality, treatment benefit, or clinical utility.

The clinical importance is bounded but consequential: if the interaction is reproducible, a single creatinine-derived estimate may miss a subgroup whose recorded renal vulnerability is concentrated among people with low functional reserve. If it is absent, clinicians should be less confident that this particular discordance-by-grip pattern adds renal prognostic information in this population. Either result informs whether a prospective biomarker-and-function study is warranted.

## Exact data binding and source restrictions

Use only UKB snapshot `[source checksum]`, with the source catalog SHA-256 recorded in `datasets/README.md`. All four primary tables are ordinary files, not archive members, and are joined horizontally one-to-one by `eid`; no source file is modified.

- `population`: `[internal dataset path]`, catalog table `population`, 34 columns. Required `eid`, `31-0.0` (sex; use the verified coding 0=female, 1=male), and `21022-0.0` (age at recruitment).
- `assessment`: `[internal dataset path]`, catalog table `assessment`, 18,159 columns. Required `eid`, `53-0.0` (index assessment date), `21001-0.0` (BMI), `46-0.0` and `47-0.0` (initial left/right grip). Repeat grip fields `46-1.0`--`47-3.0` are not primary inputs.
- `biological_samples`: `[internal dataset path]`, catalog table `biological_samples`, 1,775 columns. Required `eid`, `30700-0.0` (creatinine) and `30720-0.0` (cystatin C). `30700-1.0` and `30720-1.0` are sensitivity-only and may not enter the primary cohort.
- `health_outcomes`: `[internal dataset path]`, catalog table `health_outcomes`, 4,896 columns. Required all `41270-0.i) and `41280-0.i) for (i=0,ldots,258), plus `40000-0.0` and `40000-1.0` for death dates. Pair only equal suffixes.

Before analysis, report for each of these four files row count, duplicate `eid) count, cross-table unmatched `eid) count, and any overlapping-field disagreement. The 58-GB `main` file is not a primary input; it may be used only for an explicitly reported overlap audit. No raw imaging, narrative clinical notes, laboratory time series, urine output, measured GFR, adjudicated AKI labels, or body-composition reference is available.

The local catalog explicitly says that most field labels, units, code dictionaries and exact date semantics are absent; field-instance suffixes are not elapsed-time guarantees. Thus the exposure is called “initial assessment/biomarker instance,” not a precisely timed blood draw, until compatibility with `53-0.0) is verified.

## Provenance and event-support gates

The experiment has a hard pre-analysis gate. Produce a versioned manifest before fitting any outcome model that records:

1. verified units, valid ranges and missing-value handling for `30700-0.0), `30720-0.0), `21001-0.0), `46-0.0) and `47-0.0);
2. verified sex and age meanings;
3. the exact `41270) code representation and an exact, frozen set for N17 and N18;
4. `41280) as the paired hospital-diagnosis date, its valid date range and linkage meaning;
5. identical/compatible meaning and instance conventions for the two `40000) death fields; and
6. the common administrative end date for the hospital linkage in this snapshot.

The lexical presence of strings beginning with N17 or N18 is not sufficient evidence of endpoint semantics. If any item cannot be verified from an authoritative source, the result is “inconclusive—provenance unavailable”; do not substitute prefix matching, the maximum observed diagnosis date, or an inferred cutoff.

The read-only event audit must tabulate, by suffix and overall: nonempty codes, nonempty dates, valid code-date pairs, code-without-date, date-without-code, malformed dates, unknown codes, repeated code/date pairs, unique eids and first dates for the frozen N17 and N18 sets, and death-date counts/range. The audit may be run before dictionary verification as a lexical diagnostic, but those counts cannot be called N17/N18 events until the manifest passes. The prior cancelled diagnostic `[research job]` supplies no event result and is not evidence.

The inferential support gates are:

- at least 100 verified post-index N17 events and at least 20 in each of the four signs of standardized discordance and grip for the transparent interaction;
- at least 200 N17 events, at least 100 verified competing deaths, and usable support at every prespecified risk grid cell for the nonlinear alternative;
- no material code/date or death-date failure that makes event ordering ambiguous; and
- a verified administrative cutoff that supplies at least five years of observable follow-up for some eligible participants.

These are prerequisites, not expected results. If the baseline gate fails, report the cohort and audit only. If only the nonlinear gate fails, fit and interpret the transparent analysis if its gate passes, and label the learned analysis deferred.

## Population and time zero

Create one row per `eid) after the four horizontal joins. Index is `53-0.0). Require finite, metadata-valid age, sex, BMI, both initial grip fields, creatinine and cystatin C; valid index date; and compatibility of baseline biomarker instance with the index assessment. Use the arithmetic mean of left and right grip in kg. Standardize grip within sex using training-cohort parameters.

Exclude death on or before index, invalid or ambiguous index dates, and any valid paired N17 or N18 diagnosis date on or before index. An event on the index date is excluded as temporally ambiguous. “Without prior disease” means without a paired code/date in these outcome arrays only; it does not establish absence of outpatient, primary-care, unlinked or clinically silent disease.

For each equal-suffix pair, trim whitespace and uppercase only as allowed by the verified dictionary; do not broaden the frozen code set by prefix. A first valid N17 date strictly after index is the primary outcome. N18 is a prespecified secondary recorded hospital-code outcome. A same-day N17 and death is ordered death-first in the primary analysis because ordering is unavailable; a same-day-event sensitivity reverses that convention. Follow each participant to first N17, death, administrative end, or other verified censoring. No analysis infers AKI criteria, stage, chronicity, outpatient events or complete healthcare capture.

## Exposure construction

Convert creatinine from verified micromoles/L to mg/dL only if the manifest confirms that unit; retain cystatin C in verified mg/L. Compute and freeze:

[
eGFR_{cr}=142min(S_{cr}/k,1)^amax(S_{cr}/k,1)^{-1.200}0.9938^{Age}1.012^{Female},
]

where (k=0.7,a=-0.241) for female and (k=0.9,a=-0.302) for male, and

[
eGFR_{cys}=133min(S_{cys}/0.8,1)^{-0.499}max(S_{cys}/0.8,1)^{-1.328}0.996^{Age}0.932^{Female}.
]

Define (D=eGFR_{cys}-eGFR_{cr}). Lower D is the prespecified direction of interest, but it is not interpreted as proof that creatinine overestimates filtration. Standardize (eGFR_{cr}), D and mean grip using training data and freeze transformations in validation, test and all sensitivities. A raw log-biomarker specification is an equation-dependence sensitivity, not a validation of accuracy.

## Primary five-year estimand and transparent baseline

The primary estimand is an additive five-year competing-risk interaction in standardized exposure coordinates:

[
I_5 =
CIF^{N17}_5(D=-1,G=-1)
-CIF^{N17}_5(D=+1,G=-1)
-CIF^{N17}_5(D=-1,G=+1)
+CIF^{N17}_5(D=+1,G=+1),
]

where each CIF is standardized over the observed eligible distribution of (eGFR_{cr}), age, sex and BMI, with death as a competing event. Positive (I_5) means that the low-D/low-grip excess exceeds the sum of the two single-dimension contrasts. Report (I_5), all four risks, absolute component contrasts, 95% confidence intervals, and the direction and magnitude before discussing model comparison. A 1-percentage-point (I_5) is a prespecified descriptive meaningfulness flag, not a validated treatment or screening threshold.

The transparent nested baseline uses cause-specific Cox models for N17 and death:

- B0: standardized (eGFR_{cr}), grip, age, sex and BMI;
- B1: B0 plus standardized D;
- B2 (primary transparent model): B1 plus (D	imes G).

Use the same complete-case population and participant split for all model comparisons. Estimate five-year N17 CIFs with the Aalen–Johansen construction from the fitted N17 and death hazards. The Cox interaction coefficient is a secondary shape estimand; its prespecified direction is positive because low D and low grip are both negative standardized values. Report coefficient, robust eid-level uncertainty, proportional-hazards diagnostics, risk-set support and influence diagnostics. Fine–Gray is an optional sensitivity, never the primary estimand.

Uncertainty for (I_5) is obtained by participant-level bootstrap or a valid influence-function/sandwich procedure that refits the complete estimator, including both cause-specific hazards and standardization. Do not treat death as ordinary noninformative censoring in the primary five-year risk.

## Same-input learned alternative

The learned alternative tests whether a clinically meaningful threshold or curved D-by-grip region is hidden by B2’s single log-linear interaction surface. It uses exactly the same six baseline predictors—(eGFR_{cr}), D, grip, age, sex and BMI—and the same index, eligibility, outcomes, competing death and censoring rules. It may not use repeat biomarkers, post-index diagnoses, future laboratory data, or event-derived predictors.

Randomly assign participants by eid with a frozen seed to 60% train, 20% validation and 20% test. Fit a shallow discrete-time competing-risk model with one-year intervals and mutually exclusive hazards for N17 and death; maximum tree depth 2–3, fixed minimum leaf size and regularization, and iteration count selected only on validation. Administrative censoring weights and all transformations are estimated in training. The model must retain a no-event state and produce five-year CIFs, not a death-censored binary label.

The alternative’s scientific target is the same (I_5), evaluated at the same ((-1,+1)) D/grip grid. On the untouched test set report (I_5), four grid CIFs, competing-risk Brier/integrated Brier score, time-dependent discrimination, N17 and death calibration, and participant-bootstrap intervals. The alternative is informative only if its surface is stable and calibrated and changes the grid-level clinical contrast or reveals a reproducible threshold—not merely because its AUC is slightly larger. If it is unstable, poorly calibrated or materially unsupported, retain B2 as the only fitted scientific analysis.

This is computable within the approved limit using streaming interval construction, at most 4 CPUs, 8 GiB RAM and two hours for fitting/evaluation plus bounded bootstrap. No GPU is needed or rewarded. The actual resource use, split hash, fitted model checksum and output paths must be recorded.

## Falsification, specificity and selection checks

Report a source-to-analysis flow: rows per table, joins, missingness, exclusions, and included-versus-excluded baseline distributions using only pre-outcome variables. This is a selected biomarker/assessment cohort, not a representative UK population.

Prespecify:

- a two-year landmark sensitivity excluding anyone with N17, N18 or death by index plus two years, restarting follow-up then; interpret it as survivor-selected reverse-causation sensitivity;
- strict code/date and same-day death ordering sensitivities;
- N17-only versus N17/N18 baseline exclusion;
- raw-biomarker and, only if timing is verified, repeat-biomarker sensitivities;
- within sex-by-age-stratum permutation of D with a frozen seed, which should erase the D-by-grip surface; persistence indicates leakage or an implementation problem; and
- one nonrenal hospital-code negative control, selected before fitting (K35 appendicitis is the candidate), using the same paired-array and date rules. This negative control is run only after its exact code meaning and support are verified. A similar supported association weakens renal specificity but does not prove confounding. If no valid, supported nonrenal control can be verified, report renal specificity as unresolved rather than claiming a clean result.

Supportive evidence requires the provenance, baseline and event gates to pass; (I_5>0) with a 95% interval excluding zero and preferably exceeding the descriptive 1-point flag; persistence under strict timing and the two-year landmark; no comparable supported negative-control interaction; and, if fitted, a stable calibrated learned surface that changes an interpretable risk region. This supports only a prognostic association with prospectively recorded hospital codes in the selected cohort.

Adverse evidence is a precise null/opposite (I_5), no incremental signal in B1/B2, loss of signal after strict timing or landmarking, a comparable negative-control association, or a nonlinear surface that is unstable or clinically trivial. Inconclusive evidence includes missing code semantics, unknown administrative cutoff, inadequate paired events/quadrants/grid support, materially unpaired dates, failed calibration or inability to establish biomarker/index compatibility. None of these outcomes establishes or refutes true AKI, filtration accuracy or clinical utility.

## New scientific deliverable, limitations and revisit record

The required new deliverable is a reproducible provenance and four-table join audit; eligible-cohort flow and missingness; biomarker, eGFR, D and grip distributions; paired code/date and death audit; exact support counts; the newly estimated (I_5) and its uncertainty; all four CIFs and component contrasts; B0/B1/B2 estimates; N18 secondary; timing, landmark, negative-control and permutation diagnostics; and, only if gated, the held-out learned competing-risk surface and calibration/uncertainty outputs. Completion is established by these computed files, not by a favorable result. Each conclusion must cite a specific output.

Available data cannot establish measured filtration, muscle mass, inflammation, AKI adjudication/KDIGO stage, outpatient disease absence, causal mechanism, treatment effect, decision impact, or transportability. Those require longitudinal creatinine/urine-output adjudication, measured GFR or a valid reference, richer body-composition/inflammatory data, treatment context, expert clinical review, an independent cohort and prospective impact evaluation.

Alternatives not selected are retained explicitly. Repeat-trajectory and latent-sequence models are deferred because specimen/repeat dates and missingness are not verified; inverse-probability weighting is deferred until biomarker-selection variables and censoring assumptions are documented; treatment/causal analyses are outside the recorded-code question. The UKB-06 cardiovascular-risk seed is not a substitute: its exact protein IDs, infection/CVD code lists and temporal/confounding design are not frozen and would change the hypothesis. Revisit these branches only after those dependencies are verified. The nonlinear model should be revisited only if its endpoint gate passes and its held-out surface is stable, calibrated and clinically interpretable.
