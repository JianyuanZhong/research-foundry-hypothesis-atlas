> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Grip-selected replacement for cystatin-C testing in preserved creatinine eGFR

## What changed from the parent

The parent correctly posed a held-out, equal-budget selective-testing problem, but its outcome estimand compared target-positive and target-negative people in a pooled union selected by either rule. That pool is not the clinical policy contrast: it includes people both policies would test and does not identify whom grip would cause a service to test instead of the baseline rule. This revision makes the symmetric-difference switchers the primary clinical population and corrects the source binding for BMI.

The catalog/source inspection also found that BMI is guaranteed in the catalog’s main table (21001-0.0), whereas it is not listed in the catalog schema for assessment (although the current assessment header contains that field). BMI is therefore bound to main for executable reproducibility; the assessment BMI copy may be used only for an overlap-agreement quality check, never as the canonical input.

## Decision problem and falsifiable hypothesis

The decision is which adults with apparently preserved creatinine-based kidney function should receive a confirmatory cystatin-C assay when only 20% of eligible people can be tested. The baseline policy uses age, sex, BMI and eGFRcr. The candidate policy adds baseline hand-grip strength.

Among UK Biobank adults aged 40–69 with baseline eGFRcr 60–89, no prior recorded inpatient N17* diagnosis, and complete measurements, the grip policy will replace the baseline policy’s selections with people who have:

1. a higher prevalence of the assay-defined target condition (combined eGFRcr-cys <60), by at least 25% per replaced assay; and
2. at least 50% higher standardized 10-year risk of first recorded inpatient N17* hospitalization.

The two clauses are joint. This is a policy-value and prognostic hypothesis, not a claim that cystatin C measures true GFR or that testing prevents AKI.

The strongest claim supported by existing evidence is narrower: creatinine–cystatin discordance and lower cystatin-based eGFR are associated with adverse prognosis, and low muscle mass can make creatinine-based estimates misleading. A full-text study of muscle-mass-based indications for cystatin-C testing (Yim et al., Frontiers in Medicine 2022, DOI 10.3389/fmed.2022.1021936, frozen public source [source checksum]) does not establish measured-GFR accuracy or an implementation benefit. What remains untested is whether grip adds enough information to change a fixed-budget testing policy, and whether the people it newly selects are clinically higher-risk than the people it displaces.

The three supplied demonstrations were inspected for research ambition: the natural-history article demonstrates longitudinal held-out prediction and calibration; the Bayesian article emphasizes temporal structure and selection-bias adjustment; and the cancer supplement demonstrates washout, external validation and clinically anchored evaluation. The cancer main article and full STAR Methods were unavailable and were not treated as inspected evidence. These demonstrations motivate the design discipline but do not supply evidence for this kidney hypothesis.

## Harbor experiment

### Population and time boundary

Use the configured UKB discovery partition only: participant SHA-256 buckets 0–79. Never inspect or tune on buckets 80–99. Within discovery, deterministically assign 70% development and 30% confirmatory test with a second namespace-separated SHA-256 hash of eid; the same participant remains in one partition across all tables.

Index is the baseline assessment date 53-0.0. Include participants with:

- age at recruitment 21022-0.0 40 through 69 years inclusive;
- valid sex 31-0.0 in {0,1};
- non-null index date;
- positive baseline creatinine 30700-0.0, positive cystatin C 30720-0.0;
- BMI 21001-0.0 and at least one positive grip value among 46-0.0, 47-0.0;
- eGFRcr between 60 inclusive and 89 inclusive; and
- no paired inpatient N17* code/date with diagnosis date less than or equal to the index date.

A value is used only if its field-specific meaning and unit are established by the frozen field metadata. Do not globally reinterpret UKB negative codes. Exclude impossible/nonpositive analyte or grip values and report counts at every filter. A code without its paired valid date is not an incident event; report those code/date discordances separately.

Follow each index over (index, index + 10 years]. An AKI event is the earliest paired 41270-0.i code beginning N17 with its same-position 41280-0.i date after index and no later than index plus 10 years. For the competing-risk analysis, death is the earliest valid 40000-0.0 or 40000-1.0 date; a death before or on the same day as a candidate AKI date is treated as the competing event, while an earlier AKI is the event. No undocumented person-level censoring date is invented. Unknown emigration and incomplete capture remain limitations.

### Derived variables

Creatinine is converted from µmol/L to mg/dL by dividing by 88.4. Use the 2021 CKD-EPI race-free creatinine equation:

142 × min(Scr/k,1)^alpha × max(Scr/k,1)^−1.200 × 0.9938^age × 1.012(if female)

where k=0.7, alpha=−0.241 for females and k=0.9, alpha=−0.302 for males.

Use the 2012 CKD-EPI cystatin-C equation:

133 × min(Scys/0.8,1)^−0.499 × max(Scys/0.8,1)^−1.328 × 0.996^age × 0.932(if female).

Use the 2021 CKD-EPI race-free combined equation:

135 × min(Scr/k,1)^alpha × max(Scr/k,1)^−0.544 × min(Scys/0.8,1)^−0.323 × max(Scys/0.8,1)^−0.778 × 0.9961^age × 0.963(if female).

The target is T=1 when combined eGFRcr-cys <60. Define secondary discordance as eGFRcys/eGFRcr ≤0.70. The primary grip value is the maximum of valid left and right baseline grip; if one hand is valid, use it; if neither is valid, exclude. Pre-specify minimum-hand and mean-hand sensitivity analyses.

The primary clinical outcome is first inpatient N17* hospitalization within 10 years. Heart-failure hospitalization (I50*) and all-cause death are secondary descriptive outcomes only.

### Frozen policy rules and equal-budget comparison

In development, fit:

- baseline rule: age, sex, BMI and eGFRcr;
- grip rule: the same predictors plus maximum grip and a sex×grip interaction.

Use restricted cubic splines with knots fixed at development 5th, 35th, 65th and 95th percentiles, and ridge penalty selected by five-fold participant-level cross-validation within development. Freeze coefficients, preprocessing, knots, field exclusions and missing-data rules before reading test outcomes.

In the untouched test cohort, let k=floor(0.20N) and select exactly k people under each rule by descending predicted target risk. Resolve ties by a deterministic SHA-256 eid order. Also report random selection, oldest-first and lowest-eGFRcr-first 20% comparators. Universal testing is a cost upper reference, not an equal-budget comparator.

Let Sg and Sb be the frozen grip and baseline selected sets:

- G = Sg \ Sb is uniquely selected by grip;
- B = Sb \ Sg is uniquely selected by baseline.

Because both policies select exactly k, |G|=|B|; these are the people swapped by the policy. The overlap Sg ∩ Sb is reported but is not used to define the primary clinical contrast.

### Primary estimands

The primary policy-detection estimand is the incremental number of assay targets found per 1,000 replaced assays:

ΔT_1000 = 1000 × [mean(T | G) − mean(T | B)].

Also report the unique-set target prevalence ratio mean(T|G)/mean(T|B), its absolute difference, PPV, sensitivity relative to all test-eligible target cases, and the parent-comparable overall selected-set yield ratio. No ratio is interpreted without its denominator and confidence interval.

The primary clinical estimand is the standardized observational contrast in 10-year AKI risk between G and B:

ΔAKI_10 = CIF_10(AKI | G, common switcher distribution) − CIF_10(AKI | B, common switcher distribution),

with the corresponding cause-specific hazard ratio and risk ratio. It answers whether grip would direct assays toward a clinically higher-risk replacement group. It does not estimate the effect of receiving an assay, dose adjustment, monitoring, or treatment.

### Protection against selection-induced bias

Policy membership is frozen without using test outcomes. The primary AKI analysis is restricted to G versus B, not the pooled union, and does not condition on T (which is only observed because the assay is available retrospectively).

To reduce covariate imbalance created by the two ranking rules, fit in development, without cystatin-derived variables or outcomes, a ridge logistic model for G-versus-B membership using age, sex, BMI, eGFRcr, maximum grip and index calendar year, with the same frozen spline convention. Apply it once to the test switchers. Use bounded overlap weights 1−p for G and p for B, where p is the frozen probability of G membership. Restrict to prespecified common support 0.05 ≤ p ≤ 0.95; report retained fraction, effective sample size and standardized mean differences before/after weighting. A weighted standardized risk contrast and weighted cause-specific Cox model with robust variance are primary; weighted Aalen–Johansen cumulative incidence with death competing is the absolute-risk display. An outcome-regression standardization and unweighted analysis are sensitivity checks.

This is a bias guard, not a causal identification claim. The policy assignment is deterministic from baseline measurements, positivity may be weak, unmeasured confounding and selective UKB participation remain possible, and no analysis here can prove that testing changes AKI.

Use 2,000 participant bootstrap resamples of the untouched test set for target-yield contrasts and robust 95% confidence intervals. For survival estimates, use bootstrap resampling with the entire participant record retained. Do not refit policy or weighting models in the test resamples.

### Additional analyses

Report calibration intercept, slope and Brier score for baseline and grip target-risk models; AUC alone is insufficient. For clinical outcomes, report weighted 10-year AKI cumulative incidence, death cumulative incidence, cause-specific hazards, proportional-hazards diagnostics and absolute risk differences.

Secondary sensitivity analyses are:

- minimum-hand and mean-hand grip;
- eGFRcys/eGFRcr ≤0.70 as the target;
- add systolic BP (4080-0.0, 4080-0.1), HbA1c (30750-0.0), CRP (30710-0.0), and urinary albumin/creatinine from 30500-0.0 and 30510-0.0 as development-frozen adjustment variables;
- exclude AKI in the first 1 and 2 years;
- require paired code/date alignment and repeat with stricter date validation;
- Fine–Gray subdistribution analysis as a descriptive competing-risk sensitivity.

No secondary endpoint or subgroup can rescue a failed primary joint gate.

## Exact data binding

All source rows are read-only. The UKB snapshot is [source checksum]; the full catalog is [internal dataset path] with [source checksum].

Join one-to-one horizontally on eid, check overlapping values for agreement, and never write to any source:

| Catalog table and schema | Exact source path | Required fields |
|---|---|---|
| population / table-38565c9e35e7cb6c.json | [internal dataset path] | eid, 31-0.0, 21022-0.0 |
| assessment / table-901ef6c7ddce2d51.json | [internal dataset path] | eid, 53-0.0, 46-0.0, 47-0.0, 4080-0.0, 4080-0.1 |
| main / table-e4a9e4d8baa71a9d.json | [internal dataset path] | eid, canonical BMI 21001-0.0 |
| biological_samples / table-c6b666d905f3b02f.json | [internal dataset path] | eid, creatinine 30700-0.0, cystatin C 30720-0.0, CRP 30710-0.0, HbA1c 30750-0.0, urine microalbumin 30500-0.0, urine creatinine 30510-0.0 |
| health_outcomes / table-3cfae45e0905b0e3.json | [internal dataset path] | eid, all paired 41270-0.0…41270-0.258 and 41280-0.0…41280-0.258, deaths 40000-0.0, 40000-1.0 |

Every listed table is an ordinary CSV source file; there are no archive members. The catalog describes one-to-one horizontal joins. The current source headers were directly checked for the required fields. The assessment header also contains 21001-0.0, but the catalog schema does not list it; using main as the canonical BMI source resolves that provenance discrepancy.

The parent feasibility scan found 468,880 paired analyte rows, 461,523 with eGFRcr ≥60, 22,079 with ratio ≤0.70 and 16,910 with combined eGFR below 60. Those are feasibility counts from all eligible-looking source rows, not results: they were not partitioned and did not apply the final age, grip, BMI, prior-AKI, equal-budget or switcher definitions. Recompute all counts in the Harbor experiment.

## Interpretation and stop rules

Supportive requires all of the following in the untouched test set:

1. at least 200 participants in each unique group, at least 80% of switchers within frozen common support, and post-weighting absolute standardized mean difference ≤0.10 for every weighting covariate;
2. the G-to-B target prevalence ratio has point estimate ≥1.25 and two-sided 95% CI wholly above 1.00, with ΔT_1000 positive; and
3. the overlap-weighted AKI cause-specific HR has point estimate ≥1.50 and 95% CI wholly above 1.00, while the standardized 10-year AKI CIF difference is positive with 95% CI wholly above 0.

This supports prospective evaluation of grip-triggered selective cystatin testing. It does not support a claim of measured-GFR accuracy, clinical benefit, cost-effectiveness, dose safety, or reduced AKI.

Adverse requires strong contrary evidence: the target-yield ratio’s 95% CI is wholly below 1.00, or the weighted AKI HR’s 95% CI is wholly below 1.00 (with CIF difference wholly below 0). This argues against the proposed replacement policy and should be reported even if a secondary endpoint favors grip.

Inconclusive is the prespecified remaining state: either joint support is not met, the ratio is directionally favorable but below the 25% threshold or its CI crosses 1.00, the AKI estimate is favorable but below the 50% threshold or its CI crosses its null, event counts/overlap are inadequate, calibration is materially poor, or results depend on a hand definition, early-event exclusion or one sensitivity model. It is not acceptable to relabel such a result supportive.

All uncertainty intervals, missingness, source-join discrepancies, event-date quality counts, overlap diagnostics, effective sample sizes and filter counts must accompany the conclusion. Secondary endpoints receive 95% intervals and multiplicity labels; they cannot change the primary classification.

## What remains outside computation

Harbor can check source hashes and column presence, one-to-one joins, equations and units, discovery/test isolation, exact eid partitioning, chronological rules, paired code/date handling, fixed assay budgets, switcher construction, bootstrap uncertainty, weighting diagnostics, and whether the narrative follows the stated three-way decision rule.

It cannot establish that combined eGFR is true measured GFR; that grip diagnoses sarcopenia or low muscle mass; that N17* represents adjudicated AKI in every record; complete hospital or death capture; absence of unrecorded prior disease; medication exposure, dosing appropriateness or treatment response; assay cost or feasibility; transportability beyond UKB; or any causal effect of ordering cystatin C. Those require measured-GFR studies, chart adjudication, prescription/pharmacy data, economic inputs, expert clinical review and a prospective implementation study.
