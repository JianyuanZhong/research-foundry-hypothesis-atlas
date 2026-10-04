# Availability-matched UACR test of grip-triggered cystatin-C allocation

## Decision, evidence boundary, and unresolved hypothesis

The inherited question is whether a fixed cystatin-C budget should be allocated using raw maximum grip strength, and the selected parent added a clinically necessary comparison with urine albumin-to-creatinine ratio (UACR). The remaining decision-validity problem is semantic: the parent’s all-`O` A policy imputes unavailable UACR, so the all-`O` `G:A` contrast cannot by itself establish that grip can substitute for a UACR policy when a usable urine result is actually present. Conversely, restricting every primary result to complete UACR would change the inherited operational population and answer a different question.

The strongest evidence already supported is narrower. Chen et al., *Kidney Medicine* 2024, DOI 10.1016/j.xkme.2024.100796 (PMID 38567244; PMCID PMC10986041), studied 468,969 UK Biobank participants with paired creatinine and cystatin C and reported that predictors including grip strength were associated with the direction of eGFRcys–eGFRcr differences. The public full-text record/search evidence describes association and internal prediction, not a fixed-budget testing policy, superiority to UACR, measured GFR, persistence, or patient benefit. The parent’s read-only audit supports feasibility: its unchanged pre-assay population (O) has 134,118 participants and UACR is constructible for approximately 97% in each locked partition using the numeric albumin value or the documented low-result flag. These facts do not show that either policy is clinically superior.

The unresolved claim is:

> Among participants in the inherited (O) who have a UACR result usable under a prespecified censor-aware rule, a grip-only policy (G_U), trained without cystatin-C or outcomes, is noninferior to a UACR-informed policy (A_U) for fixed-budget detection of combined-equation eGFR<60, and is noninferior for the same target followed by first inpatient N18 when event sufficiency holds. Separately, adding grip to UACR ((AG) versus (A)) must retain the parent’s incremental biochemical claim in the all-(O) analysis. If the availability-matched (G_U:A_U) test fails, grip-only substitution must not be claimed even if the imputed all-(O) contrast appears favorable.

This is a substantive repair, not a change in the parent’s primary population or a claim that UACR collection is free. It distinguishes (i) incremental value of grip after UACR in the inherited all-(O) experiment from (ii) substitution value when UACR is actually observed. The clinical advance is a directly interpretable choice between two plausible confirmatory-testing strategies under the same assay capacity.

## Frozen inheritance and population

Retain every inherited and parent-c1643d6f0c0d098cc6023b5b rule unchanged for the global analysis:

- time zero is the initial assessment date 53-0.0;
- (O) is defined before any cystatin-C value, UACR value, future biomarker, outcome, or policy membership is opened;
- eligibility, prior inpatient N17/N18 exclusion, 2021 race-free eGFR equations, development/test/replication SHA-256 v3 locks, tie hash, exact floor(0.20 times the partition size) budgets, H/D/N18 outcomes, death ordering, missing-label bounds, bootstrap, calibration, sex-stability, placebo and event-sufficiency gates remain inherited;
- the global parent policies (B,G,A,AG,W,Q,F,T) and all parent UACR censoring variants remain frozen.

The inherited audit is feasibility only, not a result: (O=134,118) (development 80,516; test 26,977; replication 26,625), with approximately 97.09%, 97.18%, and 97.14% usable UACR in the three partitions. No locked H, D, K18, or policy yield is opened during population construction.

Define an availability-matched nested set (O_U=Ocap U), where (U=1) only if baseline UACR is available by the exact construction below. This nested analysis does not replace or alter (O), global policy membership, or global assay denominators. A participant with missing UACR is retained in all inherited global analyses and is excluded only from the explicitly labeled (O_U) secondary decision analysis. Report counts and fractions excluded from (O_U) by lock before outcomes are opened.

## UACR availability and censoring

Use only instance-0 values:

- urine albumin 30500-0.0, mg/L;
- albumin result flag 30505-0.0;
- urine creatinine 30510-0.0, micromol/L;
- urine-creatinine result flag 30515-0.0.

For finite albumin (a\ge0) and finite creatinine (c>0), define (uACR=1000a/c) in mg/mmol. If albumin is blank and the trimmed 30505-0.0 value is exactly `<6.7`, define the primary interval-censored substitute (a=3.35) mg/L solely for policy construction. A missing/nonpositive creatinine, missing albumin without that exact flag, any other flag, nonfinite ratio, or contradictory numeric-plus-flag record makes (U=0) and is reported as an integrity condition. Never parse 30515-0.0 as the albumin flag, and never treat 6.7 as a measured albumin value.

The primary (Z_U) is log1p(uACR), winsorized at the development-(O_U) 1st and 99th percentiles and standardized by the development-(O_U) mean and standard deviation. No UACR transform is fit in test or replication. Freeze before opening locks the six prespecified variants formed by albumin substitution 0, 3.35, or 6.7 mg/L crossed with unavailable-value handling at the development 1st or 99th percentile. The 3.35/development-median version is descriptive only for the all-(O) imputed parent A/AG models and primary for (O_U), while the extreme variants are robustness analyses. A contradictory field record is an integrity failure, not an opportunity to choose the favorable value.

For the actual-availability analysis, no missing-UACR imputation is allowed because (O_U) contains only (U=1). If UACR availability is below 95% in either lock, the availability-matched result is reported but its substitution conclusion is inconclusive; the inherited all-(O) result is not relabeled as substitution.

## Availability-matched policies and estimands

Within development (O_U) only, fit and freeze:

- (B_U): the parent baseline B design plus exactly (Z_U);
- (G_U): the parent B design plus exactly the inherited one globally development-winsorized/standardized raw maximum-grip scalar (Z_R), with no UACR term;
- (A_U): (B_U), equivalently B plus exactly (Z_U);
- (AG_U): (B_U) plus exactly (Z_R), as a descriptive incremental check.

No future field, cystatin label, locked outcome, center, era, repeat result, or UACR-derived threshold is used in fitting. The nested policies rank every member of each locked (O_U) partition and select exactly (n_U=mathrm{floor}(0.20|O_{U,p}|)), using the inherited deterministic tie hash. Thus (G_U) and (A_U) have identical denominators, the same eligible participants, and no artificial advantage from different UACR missingness.

The primary availability-matched contrast is (G_U-A_U), expressed as:

1. (Y_H): combined creatinine-cystatin eGFR below 60 per 1,000 selected cystatin assays, with participant-level unknown-label bounds exactly as inherited;
2. (Y_{H18}): selected participants with observed H and first post-baseline inpatient N18 in (53-0.0, 53-0.0 plus 10 years], per 1,000 selected assays, with death before same-day N18 competing as inherited.

The clinically conservative noninferiority margins are -1 H reclassification per 1,000 assays and -1 H×K18 event per 1,000 assays. In each test and replication lock, the one-sided simultaneous 95% lower bound for (G_U-A_U) must exceed -1/1,000 for the substitution claim. Claim (G_U) superiority only if the two-sided interval is above zero in both locks. Require the pooled lock-stratified interval to meet the same noninferiority margin and require positive or noninferior paired swap-set behavior in both directions; report (G_U-A_U) and (A_U-G_U) selection swaps rather than only pooled rates.

For the grip-increment question, (AG_U-A_U) is secondary and cannot rescue substitution. The parent’s global (AG:A) and (G:A) results remain primary for their stated all-(O) estimands. A global imputed-policy contrast may be reported as “all-(O) predictive allocation” but may not be called “substitution for available UACR” unless the matched (G_U:A_U) gate passes.

If H×K18 observed-label swap sets have fewer than 20 events in either direction in either lock, do not call the clinical noninferiority result adverse; mark it inconclusive and report the biochemical result separately. Positive N17 or Kany diagnostics cannot rescue N18. Retain all parent missing-H bounds, >1% missing-cystatin adverse rule, competing-death rule, multiplicity and calibration gates.

## Repeat biochemical confirmation stress test

A single baseline eGFR estimate is not persistent CKD. As a prespecified, non-rescuing validity stress test, use later UKB instance-1 fields only in participants with:

- assessment date 53-1.0 strictly after 53-0.0;
- repeat creatinine 30700-1.0 and cystatin C 30720-1.0 both finite and positive.

Compute repeat combined eGFR using the same race-free 2021 equation, with age advanced from baseline age 21022-0.0 by the exact day difference between 53-1.0 and 53-0.0 divided by 365.2425. Define (H_1) as repeat combined eGFR<60. The primary inherited H remains the baseline label; (H_1) is a later biochemical confirmation outcome, not a replacement label and not an adjudicated CKD diagnosis. Do not use repeat data in any policy score or threshold.

For each global and (O_U) policy, report selected-set (H_1) yield and paired policy contrasts using the same selected-assay denominator, with participant-level missing-(H_1) bounds. Require at least 100 observed H1 values in each selected-set union and at least 20 observed H1 swap-set events in each lock before interpreting the persistence stress test. If those gates fail, it is inconclusive. Full source scanning found only about 17,800 people with both repeat creatinine and cystatin values in the full biological-samples table, so this gate is plausibly limiting and must not be quietly relaxed. Repeat dates are assessment dates, not assay dates; their absence or implausible chronology is an integrity failure.

Repeat UACR (30500-1.0, 30505-1.0, 30510-1.0) is not a primary gate because only about 6,500 full-table rows have both repeat albumin and repeat urine creatinine, and instance assignment does not provide a clinical three-month persistence interval. If reported, it is an exploratory agreement diagnostic only. No conclusion may call one baseline UACR “persistent albuminuria.”

## Inference, robustness and falsification

Use paired participant-level bootstrap and inherited joint unknown-label bounds, with a 2,000-resample max-|t| family extended only to the prespecified (O_U) contrasts and repeat-H1 diagnostics. Never refit on locks. Freeze all UACR variants and (O_U) membership before reading H, K18, death or H1. Report exact denominators, selected counts, missing-label counts, swap-set counts, intervals and both lock-specific and pooled estimates.

Support for the parent’s full claim requires all inherited global gates plus the parent (AG:A) and (G:A) UACR gates. Support for the stronger statement that grip can substitute for available UACR additionally requires, in both locks, UACR availability at least 95%, exact equal (O_U) budgets, (G_U:A_U) biochemical noninferiority, no sign reversal over the frozen UACR censoring variants, and—only if event sufficiency passes—N18 noninferiority. The repeat-H1 result strengthens interpretation but cannot rescue a failed primary policy gate.

- Supportive: global AG adds the prespecified material H yield beyond A; global G is noninferior to A; and matched (G_U) is noninferior to (A_U), with adequate N18/H1 precision. This supports only a prospective comparison of grip-only versus UACR-informed allocation in an observed UKB-like frame, not clinical benefit or guideline adoption.
- Adverse: the matched (G_U) lower bound is below -1/1,000, or the two-sided interval favors (A_U), in either lock with adequate precision; or a global inherited gate fails. Then grip-only substitution is rejected for this decision even if an imputed all-(O) result is favorable. If repeat H1 similarly favors A, the biochemical claim is less likely to reflect durable low filtration, but this remains observational.
- Inconclusive: UACR availability below 95%, sparse swap/event/H1 counts, lock disagreement, crossed margins, censoring-variant sign reversal, join/flag/date integrity failure, or missing-label bounds crossing the margin. Do not turn a wide interval into evidence of equivalence.

Falsification fixtures must include: 30505/30515 swap; incorrect UACR units; treating <6.7 as 6.7 measured; imputation or complete-case changes to global O; unequal (O_U) budgets; fitting UACR transforms or model coefficients on locks; letting UACR, repeat values or outcomes enter G; calling global imputed G:A substitution without the matched gate; using repeat H1 as baseline H; using repeat instance membership as proof of three-month CKD persistence; and interpreting supportive arithmetic as measured-GFR validity, muscle mechanism, treatment benefit, cost-effectiveness, fairness, or guideline endorsement.

The verifier can check source hashes, schema identity, one-to-one eid joins, O and (O_U), field-instance rules, UACR formula/flags/units, exact budgets and policy membership, development-only fitting, leakage, chronology, missing-label bounds, uncertainty, gates and output-linked conclusions. It cannot establish that a single UACR is persistent albuminuria, that combined eGFR equals measured GFR, that N18 is adjudicated CKD, that grip measures muscle mass, that UACR is available at the intended clinical decision time, or that testing changes treatment or patient outcomes. Those require repeat clinically timed urine testing, measured GFR/body-composition data, outpatient and medication/action records, nephrology review, cost and workflow data, external validation, and prospective implementation or randomized testing-strategy evidence.

## Exact source bindings and provenance

All sources are read-only ordinary CSV files in UKB snapshot [source checksum], joined one-to-one on `eid`. Archive member is null for each.

- Population and baseline covariates: `[internal dataset path]`, table `population`, schema `datasets/ukb/table-38565c9e35e7cb6c.json`; inherited columns include `eid`, `31-0.0`, `21022-0.0`.
- Assessment: `[internal dataset path]`, table `assessment`, schema `datasets/ukb/table-901ef6c7ddce2d51.json`; inherited columns include `eid`, `53-0.0`, `54-0.0`, `46-0.0`, `47-0.0`, `21001-0.0`, and repeat date `53-1.0`.
- Baseline/repeat biomarkers and urine fields: `[internal dataset path]`, table `biological_samples`, schema `datasets/ukb/table-c6b666d905f3b02f.json`; required `eid`, `30700-0.0`, `30720-0.0`, `30500-0.0`, `30505-0.0`, `30510-0.0`, `30515-0.0`, `30700-1.0`, `30720-1.0`, `30500-1.0`, `30505-1.0`, and `30510-1.0`.
- Main UKB table: `[internal dataset path]`, table `main`, schema `datasets/ukb/table-e4a9e4d8baa71a9d.json`; inherited `eid`, `200-0.0`, `1647-0.0`, `20115-0.0` and audit fields as applicable.
- Outcomes: `[internal dataset path]`, table `health_outcomes`, schema `datasets/ukb/table-3cfae45e0905b0e3.json`; paired `41270-0.0` through `41270-0.258` and `41280-0.0` through `41280-0.258`, plus death `40000-0.0` and `40000-1.0`. N18 chronology and all inherited diagnosis-code/date parsing remain unchanged.

The exact source hashes are recorded in datasets/ukb/README.md and the full catalog `[internal dataset path]` (catalog [source checksum]). The available UKB rows do not include measured GFR, assay timestamps, validated outpatient CKD history, adjudicated N18/AKI, individual censor dates, treatment response, UACR cost/availability workflow, or external cohort data.

## Substantive advance

This child fixes an interpretive overreach without weakening the inherited scientific question. It retains the all-(O) fixed-budget test of whether grip adds value after UACR, but requires an availability-matched, no-imputation (G_U:A_U) comparison before calling grip a substitute for an actually observed UACR. The repeat-H1 analysis asks whether selected low combined eGFR is reproducible at a later assessment, while explicitly treating its sparse coverage and absent clinical persistence interval as limitations. A supportive result would justify prospective strategy comparison; an adverse result would prevent a misleading substitution claim; an inconclusive result would identify the exact additional data needed.
