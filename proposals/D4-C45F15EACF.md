# Dynamic cystatin-C/creatinine discordance after repeat assessment and future inpatient AKI

## Unresolved clinical question and hypothesis

The prior candidate established a clinically important one-time question: among people whose creatinine-based eGFR is preserved, does a lower cystatin-C-based eGFR identify excess subsequent inpatient-coded AKI, especially in people with low grip strength? The next unresolved decision question is whether a repeat measurement changes that risk assessment. A repeat cystatin-C test is only clinically useful if a newly discordant result identifies risk that was not already apparent from the baseline phenotype and ordinary covariates.

The prespecified hypothesis is:

> Among UK Biobank participants with initially concordant-preserved kidney estimates (baseline eGFRcr >=60 and eGFRcys >=60), who are alive, free of coded AKI/CKD, and have valid repeat creatinine and cystatin-C measurements, a new repeat discordance (repeat eGFRcr >=60 but repeat eGFRcys <60) is associated with a higher 5-year cumulative incidence of a first inpatient-coded AKI than repeat concordant preservation (both repeat estimates >=60). The association will be larger among participants with low baseline grip strength and will add calibrated prognostic information beyond baseline estimates and routine clinical covariates.

This is a prognostic/measurement-value hypothesis. It does not claim that cystatin C causes AKI, that a repeat test improves outcomes, or that the repeat result is a treatment target.

## What is established, what is unresolved, and the advance

The strongest directly relevant evidence I inspected is Haines et al., “Comparison of Cystatin C and Creatinine in the Assessment of Measured Kidney Function during Critical Illness” (CJASN 2023), frozen at `references/expert-seeds/papers/kidney-function/article.readable.txt` and its PDF. It studied 38 mechanically ventilated ICU patients with serial creatinine, cystatin C, iohexol clearance, and rectus-femoris ultrasound. It supports the narrower claim that, during prolonged critical illness and muscle loss, creatinine-based eGFR can overestimate measured kidney function and diverge from cystatin-C-based estimates. It does not establish a community-cohort association with future AKI, the value of a repeat test, or effect modification by grip strength.

A current Europe PMC search was also frozen during this episode (source ID `[source checksum]`). Its model-mediated excerpt included a 2026 prospective stroke-registry report associating eGFR discordance and one-year change with later outcomes, but that is a different population/outcome and was not treated as full-text evidence. The proposed advance is therefore a data-bound landmark test of whether *new* discordance after an initially reassuring result identifies subsequent coded AKI risk in a general UKB cohort, with explicit comparison against a baseline-only assessment.

## Population, time zero, and temporal boundaries

Use only the initial UKB assessment (instance `0.0`) to define baseline. Baseline time zero is the participant's date in `53-0.0`, not file order. Require nonmissing baseline age, sex, assessment date, creatinine, cystatin C, left/right grip, and the covariates used in the primary complete-case analysis. Use the initial assessment window represented by the snapshot (approximately 2006–2010), but use the recorded date rather than an assumed calendar date.

The dynamic landmark cohort is restricted to participants who:

1. have baseline eGFRcr >=60 and eGFRcys >=60;
2. have no aligned inpatient `N17.x`, `N18.x`, or `N19.x` diagnosis on or before baseline time zero;
3. have a valid repeat assessment date `53-1.0` strictly after `53-0.0`, valid repeat creatinine `30700-1.0`, cystatin C `30720-1.0`, and repeat grip if used in the secondary reserve analysis; and
4. are alive and have no qualifying AKI/CKD diagnosis on or before the repeat date.

The landmark time zero is the repeat assessment date `53-1.0`. Events between baseline and the repeat date are not counted in the landmark outcome analysis; they are used only for the eligibility flow table and a prespecified selection-bias comparison. This prevents immortal time from being assigned to the repeat-exposed group. The estimand is explicitly conditional on reaching the repeat assessment with valid paired biomarkers, not a claim about all UKB participants.

Follow from the repeat date until the first qualifying outcome, death, the last available outcome date, or 2023-03-31, whichever occurs first; the primary horizon is 5 years. Require qualifying diagnosis dates to be strictly after landmark time zero. Repeat dates outside the recorded baseline-to-repeat ordering are invalid and are reported, not silently repaired.

For the reverse-causation sensitivity, exclude AKI/CKD outcomes in the first 365 days after the repeat date. This is a sensitivity estimand, not the primary outcome definition.

## Exact data bindings and read-only sources

All UKB joins are one-to-one horizontal joins on `eid`. The authoritative snapshot is `[source checksum]`. Every listed archive member is an ordinary read-only file; there is no archive extraction step.

| Role | Catalog table and schema | Required columns | Exact read-only source and archive member |
|---|---|---|---|
| Demography | `population`, `datasets/ukb/table-38565c9e35e7cb6c.json`, schema [source checksum] | `eid`, `31-0.0` sex, `21022-0.0` age at recruitment | `[internal dataset path]`; ordinary file |
| Assessment and time | `assessment`, `datasets/ukb/table-901ef6c7ddce2d51.json`, schema [source checksum] | `eid`, `53-0.0`, `53-1.0`, `46-0.0`, `47-0.0`, optional `46-1.0`, `47-1.0`, `21001-0.0`, `4079-0.0`, `4080-0.0`, `2443-0.0` | `[internal dataset path]`; ordinary file |
| Kidney/metabolic biomarkers | `biological_samples`, `datasets/ukb/table-c6b666d905f3b02f.json`, schema [source checksum] | `eid`, `30700-0.0`, `30720-0.0`, `30750-0.0`, and repeat `30700-1.0`, `30720-1.0`, `30750-1.0` | `[internal dataset path]`; ordinary file |
| Outcomes and censoring | `health_outcomes`, `datasets/ukb/table-3cfae45e0905b0e3.json`, schema [source checksum] | `eid`; aligned indexed arrays `41270-0.0` through `41270-0.258` for ICD-10 codes and matching `41280-0.0` through `41280-0.258` for first inpatient diagnosis dates; `40000-0.0`, `40000-1.0` death dates | `[internal dataset path]`; ordinary file |

The same fields are duplicated in `main`, `datasets/ukb/table-e4a9e4d8baa71a9d.json`, schema [source checksum], source `[internal dataset path]`. Read `main` only for cross-table agreement/QC; do not append it as a second sample. The local source-header audit confirmed the required baseline/repeat columns, numeric biomarker cells, ISO assessment dates, and paired indexed diagnosis/date fields. Repeat cells are allowed to be empty and are part of the feasibility report.

The catalog also exposes `additional_exposures`, `online_followup`, and `genomics`, but they are not required for this experiment. The catalog explicitly states that no raw imaging, verified narrative extraction, raw waveform, or sequence/variant bundle is available; `genomics` is derived metadata, not a validated PRS or CHIP source.

## Exposure construction

Convert creatinine `30700` from umol/L to mg/dL and calculate 2021 CKD-EPI eGFRcr and eGFRcys in ml/min/1.73 m2 using age and sex-specific constants. Preserve the exact formula, units, field-level missing-code decision, and any invalid-value counts in the run manifest. Do not globally recode negative values until field-specific metadata are verified.

The primary exposure is defined only among baseline-concordant-preserved participants:

- repeat concordant-preserved: repeat eGFRcr >=60 and repeat eGFRcys >=60 (reference);
- new discordant-low: repeat eGFRcr >=60 and repeat eGFRcys <60 (primary contrast);
- repeat creatinine-low: repeat eGFRcr <60, described as a secondary category and not pooled into the primary contrast.

The continuous secondary exposure is the change in eGFRcys minus eGFRcr from baseline to repeat, with a prespecified spline and a descriptive threshold analysis. HbA1c change (`30750-1.0 - 30750-0.0`) is a secondary covariate/heterogeneity analysis, not a replacement hypothesis. Low grip is the sex-specific baseline 20th percentile of the maximum valid `46-0.0`/`47-0.0), standardized once in the eligible baseline-concordant cohort. Grip is not treated as a direct muscle-mass measurement.

## Outcomes and estimands

The primary outcome is first inpatient-coded AKI: the earliest indexed `41280-i` date strictly after landmark time zero whose aligned `41270-i` code begins with `N17`. The primary estimand is the adjusted 5-year cumulative-incidence difference between new discordant-low and repeat concordant-preserved participants, reported overall and by baseline grip stratum, with the interaction contrast and 95% confidence intervals. Report risk difference, risk ratio, cause-specific hazard ratio, and cumulative-incidence curves. Death before AKI is a competing event, not ordinary noninformative censoring.

Secondary outcomes are first inpatient-coded CKD `N18.x`, all-cause death using the earliest eligible `40000-0.0`/`40000-1.0`, and the composite of AKI or CKD. They cannot substitute for an infeasible primary AKI analysis.

## Baselines and analysis

First report the participant flow from baseline to repeat landmark, baseline-versus-repeat availability, missingness, biomarker validity, exposure-cell counts, follow-up, outcomes, and deaths. Report the distribution of baseline-to-repeat interval and compare repeat-observed versus eligible-but-not-observed participants on baseline variables.

The primary model is a cause-specific Cox model for first N17.x AKI with death as a competing event. Include repeat exposure, baseline age (restricted cubic spline), sex, baseline BMI, systolic/diastolic BP, HbA1c, self-reported diabetes, baseline eGFRcr, baseline eGFRcys, and baseline low-grip status; include exposure-by-grip interaction. Derive standardized 5-year cumulative-incidence contrasts from the fitted model. Fine-Gray is a sensitivity analysis, not the primary estimand. Use participant-level bootstrap for cumulative-incidence uncertainty and robust checks for proportional-hazards violations.

The clinically relevant baseline-only comparator is fitted in exactly the same landmark cohort using only information available at baseline: baseline eGFRcr/eGFRcys, grip, age, sex, BMI, BP, HbA1c, and diabetes. The dynamic model adds repeat eGFRcr/eGFRcys (and the prespecified change terms). Compare calibration at 5 years, Brier score, optimism-corrected discrimination, and decision-curve net benefit only as secondary evidence. A bounded elastic-net Cox model may be fit with the same baseline versus dynamic feature sets, using a fixed eid-hash 70/15/15 train/tune/test split and all preprocessing inside training folds. It is optional, CPU-feasible, and cannot turn a small predictive improvement into clinical utility.

Address informative repeat assessment by (a) making the primary estimand conditional on the repeat-observed landmark cohort, (b) reporting the selection flow, and (c) repeating the dynamic analysis with inverse-probability-of-repeat weights estimated from baseline variables, with weight truncation prespecified. Do not interpret weighting as removal of unmeasured selection bias. Complete-case and multiple-imputation analyses must keep imputation and model tuning within training folds. No GPU or foundation-model training is needed.

Prespecified sensitivities are: 365-day post-repeat washout; continuous discordance change; baseline and repeat sex/age strata; a restricted baseline-to-repeat interval (1–6 years); repeat grip as an effect modifier where available; complete-case versus imputed analysis; and the negative-control inpatient outcome of traumatic injury (ICD-10 S00–T14), whose code list and date pairing are fixed before results are viewed. Never change N17/N18/N19 or the negative-control code list after inspecting results.

## Falsification and interpretation

Support requires: (1) a positive, clinically nontrivial adjusted 5-year AKI contrast for new discordant-low versus repeat concordant-preserved in the prespecified direction; (2) uncertainty that does not include clinically trivial and harmful values simultaneously, with the event-count gate met; (3) broadly consistent direction after the 365-day washout, interval restriction, and repeat-observation weighting; and (4) no equal-or-larger association for the unrelated traumatic-injury negative control. A calibration or AUC improvement alone is not supportive.

An adverse result is a clearly opposite AKI association, a null contrast with adequate event support, loss of the association under the reverse-causation washout/interval restriction, or an association that is as large or larger for traumatic injury. It would argue against interpreting new discordance as kidney-specific hidden vulnerability. If the parent baseline phenotype is absent in the same landmark cohort, the repeat result cannot rescue that failed premise.

The result is inconclusive if field units or missing-code meanings cannot be verified; repeat and diagnosis dates cannot be aligned; fewer than 100 primary AKI events occur overall or fewer than 10 in either primary exposure cell; weighting is unstable; or confidence intervals remain too wide to distinguish clinically relevant benefit from harm. Do not replace an underpowered AKI analysis with CKD, death, or a predictive-only endpoint.

Computation can establish field availability, filtering counts, temporal ordering, code-based inpatient associations, competing-risk estimates, incremental calibration, and whether the prespecified falsification gates are met. It cannot establish AKI stage, outpatient AKI, measured GFR, cystatin-C specificity, causal effects, representativeness, or that repeat cystatin-C testing improves medication safety or patient outcomes. Those claims require linked outpatient laboratory trajectories, adjudicated AKI and CKD, measured GFR, inflammation and muscle-mass measures, treatment/medication data, expert review, external validation, and ideally a prospective testing/management study.

## Demonstration dispositions

- The natural-history transformer demonstration (`references/research-ambition/natural-history/article.readable.txt`, with XML/PDF available) motivates explicit longitudinal ordering and competing morbidity. A concrete local adaptation is this landmark/update analysis; reproducing its generative model is not justified by UKB's structured fields.
- The cancer demonstration's main article and full STAR Methods remain unavailable. I inspected only its supplement (`references/research-ambition/cancer/supplement.readable.txt`) and metadata; its multimodal imaging/treatment-response setting is not pursued because this UKB snapshot has no raw images, verified narrative extraction, staging, or treatment records.
- The Bayesian longitudinal EHR/genetic demonstration (`references/research-ambition/bayesian/article.readable.txt`, supplement and reporting summary available) motivates explicit time-updated likelihoods, leakage control, and calibration. I adapt those principles with transparent cause-specific models and a bounded elastic-net sensitivity; I do not import its genetic claims because UKB `genomics` here is derived metadata rather than a sequence/PRS bundle.

## Provenance and audit requirements

Keep every source read-only. Record snapshot and schema hashes, source paths, exact rows at each filter, invalid and missing-value counts, baseline-to-repeat interval distribution, exposure-cell/event feasibility, code-list version, weight diagnostics, bootstrap seed, eid split rule, and every supportive/adverse/inconclusive branch. No participant rows or clinical notes are sent to public search. The parent is `[prior hypothesis]`, with seed provenance `[prior hypothesis]` and `references/expert-seeds/manifest.json`.
