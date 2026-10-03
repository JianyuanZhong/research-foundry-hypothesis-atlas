# UKB-07 repaired: CRP-discordant GlycA, persistent inflammation and future infection

## Scientific deliverable

The experiment must newly estimate, from held-out UKB participants, (1) the adjusted contrast in 3-year and 10-year risk of first hospital-recorded infection for CRP-low/GlycA-high versus CRP-low/GlycA-low, with death as a competing event; (2) whether that contrast is present after a 180-day delayed entry and separately in the 0--179-day occult-illness window; (3) whether the contrast survives BMI/ALT adjustment and is specific to infection rather than generic mortality; and (4) whether a cross-fitted CRP/metabolic-adjusted GlycA residual gives the same direction. A locked output package must contain participant counts, missingness/timing checks, event counts, effect estimates with uncertainty, cumulative-incidence curves, held-out calibration/discrimination, repeat-state stability, and a conclusion classified as supportive, adverse or inconclusive. No fitted hypothesis result is claimed in this proposal.

## Opening and unresolved claim

GlycA is an NMR measure of glycoprotein acetylation, while CRP is an acute-phase protein. The seed's clinically important opening is whether a high GlycA value when CRP is low identifies a longer-lived inflammatory state that matters for later infection risk, rather than merely reflecting a transient illness or metabolic context.

The strongest inspected evidence supports three bounded claims. First, large-scale NMR metabolomic profiles predict incident disease and changes between two time points can track changed disease risk, but this is not infection-specific or a CRP/GlycA comparison [K1]. Second, prospective UK Biobank inflammatory/metabolic composite indices associate with later sepsis, including after a 3-year left-truncation sensitivity analysis, but the composite does not identify GlycA or persistence [K2]. Third, a UK Biobank NMR signature that included GlycA was associated with hospital-recorded acute respiratory infection, LRTI and pneumonia, but GlycA was one component among many and was not compared with CRP or repeated [K3].

Untested hypothesis: among adults with paired baseline CRP and GlycA, the CRP-low/GlycA-high state has a higher cause-specific hazard and higher Aalen-Johansen cumulative incidence of a first hospital-recorded infection after a 180-day washout than the CRP-low/GlycA-low state, and the direction remains when GlycA is represented as excess above that predicted by CRP, BMI, ALT, age, sex and calendar year. The claim is about prospective association and risk stratification, not a causal mechanism or clinical utility.

The strongest rival explanations make different predictions:

- Occult illness: the contrast is concentrated in 0--179 days and attenuates toward the null after delayed entry.
- Obesity/metabolic or liver confounding: the contrast is largely removed by BMI and ALT, or is similar for CRP-high/GlycA-high and other metabolically burdened states rather than specific to CRP-low/GlycA-high.
- Measurement timing: the state is not reproducible between instances, or the association depends on the baseline instance without a compatible repeat-state signal. The repeat date is only a timing proxy.
- Generic frailty: GlycA predicts all-cause death to the same extent without a distinctive infection gradient, or the infection signal disappears under death competition.

The advance over [K1]--[K3] is a falsifiable boundary test of a named biomarker contrast, delayed entry, competing outcomes and sparse repeat evidence. It can determine whether a low-CRP patient with high GlycA warrants a distinct infection-risk hypothesis for external validation, or whether this apparent discordance is transient or metabolic. It cannot establish a treatment threshold.

## Population and time

The source population is participants in the four ukb672073 Parquet tables listed in source-schema-audit.json, joined one-to-one on string eid. Include age 40--69 years at recruitment (21022-0.0), either recorded sex (31-0.0), a valid baseline assessment date (53-0.0), and valid positive baseline CRP (30710-0.0) and GlycA (23480-0.0). Do not use ukb671626, Olink/dta, or any cross-namespace identifier. BMI and ALT are adjustment variables; retain missingness indicators rather than silently treating missing as zero.

Index time is 53-0.0. The primary risk set enters at index +180 days (left truncation) and ends at the first infection event, death, administrative censoring at 2022-10-31, index +10 years, or loss of usable follow-up. Report a prespecified 3-year horizon as the clinically nearer-term long-term check and a 10-year horizon as the principal long-term check. Separately tabulate events and deaths in index day 0--179. A sensitivity analysis repeats the primary analysis with entry at index +365 days; it is not a replacement for the 180-day estimand.

Prior infection is not used as an exclusion that could select survivors. Derive an indicator for any A00--B99 or J00--J22 diagnosis dated in the five years before index and include it as a baseline covariate; report a sensitivity analysis excluding any prior code. Events dated before index are never counted as future events.

## Exposure

Normalize biomarker strings explicitly and preserve missingness. Use CRP <2 mg/L versus >=2 mg/L. Estimate the GlycA low/high cut point as the median among complete baseline exposure values in the development split only; lock it before calibration/test evaluation. The primary four-level exposure is:

1. CRP-low/GlycA-low (reference);
2. CRP-low/GlycA-high (the prespecified discordant contrast);
3. CRP-high/GlycA-low;
4. CRP-high/GlycA-high.

Do not claim that the observed diagnostic median (approximately 0.783 mmol/l) is a fitted threshold. Use log1p(CRP), GlycA, BMI, ALT, age, sex and calendar year as continuous/specified covariates in sensitivity models. No post-index variables are allowed.

Repeat evidence uses 23480-1.0 and 30710-1.0 with 53-2.0 as the repeat-assessment timing proxy. Instance-1 is treated as a repeat measurement, but the proposal does not call 53-2.0 the exact blood-draw date. The complete baseline-plus-repeat overlap is only 589 in the bounded audit. Therefore repeated state is a prespecified temporal check, not a powered independent validation cohort. Report its state-transition table and residual correlation; if the repeat subset has fewer than 100 participants or fewer than 10 primary events, label that check inconclusive regardless of direction.

## Outcomes and competing events

The primary endpoint is the first hospital inpatient diagnosis whose normalized ICD-10 code is either:

- A00--B99: infectious and parasitic diseases; or
- J00--J22: acute respiratory infections.

Use the paired fields 41270-0.k and 41280-0.k, k=0,...,258, and count an event only when the paired date is valid and lies in the risk interval. Pre-specify secondary subsets A40--A41 (sepsis) and J12--J18 (pneumonia), plus the A00--B99-only endpoint. An infection-coded underlying cause of death uses 40001-0.0/40001-1.0 and its 40000 date as a secondary outcome, not a substitute for hospital infection.

For the primary cause-specific model, death from any cause before infection is a competing event; infection is the event of interest. Aalen-Johansen cumulative incidence and a Fine-Gray subdistribution analysis are required secondary summaries. Same-day infection and death are assigned infection first in the primary analysis because a dated inpatient diagnosis is directly observed; rerun with death-first ties as a sensitivity. Death after infection is not allowed to erase the infection event. Generic all-cause mortality from 40000 is reported separately and as the competing event.

The audit confirms endpoint support before fitting: the health-outcome table has 502,370 rows, 119,550 A00--B99 code cells and 67,692 J00--J22 code cells; 40,017 baseline-complete participants had a first A00--B99 event 180 days to 10 years in the bounded diagnostic. These are availability diagnostics, not hypothesis results. Diagnosis records do not establish symptoms, organism, microbiology, outpatient infection, antibiotic treatment, vaccination, severity or adjudicated infection.

## Analysis

Use a deterministic participant-level split based on SHA-256(eid) modulo 100: 60% development, 20% calibration, 20% held-out test. All imputation, GlycA thresholding, residual fitting, spline knots, calibration and model choices that depend on outcomes are learned only in development/calibration as specified below. Never peek at test outcomes to change endpoints, subgroups, washout or thresholds.

The transparent baseline is a delayed-entry cause-specific Cox model with the four-level exposure and baseline age, sex, BMI, ALT, calendar year and five-year prior-infection indicator. Impute BMI/ALT within development with a missingness flag; use robust standard errors. Report the CRP-low/GlycA-high versus low/low hazard ratio, 95% interval, event counts, and 3- and 10-year Aalen-Johansen risk differences. Fine-Gray estimates, a 365-day washout, and exclusion of prior infection are sensitivity analyses.

The mechanistic alternative uses the identical baseline population, outcome, split and clinical inputs. In each development fold, fit:
standardized GlycA ~ log1p(CRP) + BMI + ALT + age + sex + calendar year
with development-fold imputation and missingness flags. The cross-fitted residual is excess GlycA beyond acute CRP and metabolic/liver context. Fit the same delayed-entry outcome model using the residual (a restricted cubic spline with knots locked from development), log1p(CRP), and the same covariates. Compare the held-out residual surface with the four-level baseline. This can reveal a graded CRP-discordant signal that a median category loses, and whether it survives explicit metabolic/liver adjustment. It is not evidence of a biological mechanism by itself.

For both representations, output held-out time-dependent C-index, integrated Brier score, calibration slope/intercept, and observed-versus-predicted cumulative incidence by exposure group at 3 and 10 years. Use at least 2,000 stratified participant bootstrap replicates for 95% intervals when feasible and report the actual count if lower. Predictive improvement alone cannot establish persistence; the scientific comparison is whether the exposure direction and long-term infection contrast replicate under the alternative representation.

The two-time-point check compares baseline and repeat four-level states and the residual's test-retest correlation. It reports missingness and time-lag distributions before any outcome model. Do not use repeat values for baseline prediction or impute them into the main cohort.

## Falsification and interpretation rules

Supportive evidence requires, on held-out data, a CRP-low/GlycA-high versus low/low adjusted infection HR above 1 with a 95% interval excluding 1 at the primary 180-day-to-10-year analysis, a same-direction 3-year cumulative-incidence contrast, and materially preserved direction after BMI/ALT adjustment and in the residual representation. A larger near-term association may coexist, but support for persistence requires that the long-term estimate is not confined to day 0--179 and that the repeat check is at least directionally compatible when it has sufficient events.

Adverse evidence is a long-term HR at or below 1, or a positive association confined to day 0--179 with the delayed-entry estimate near null; attenuation by at least half after BMI/ALT adjustment with the interval including no effect; loss of direction in the residual representation; or a stronger indistinguishable generic-mortality association without infection specificity. These outcomes redirect the question toward occult illness, metabolic confounding, measurement timing or frailty rather than confirming the hypothesis.

Results are inconclusive—not refuting—when intervals remain compatible with both clinically meaningful benefit and harm, when repeat support has fewer than 100 participants or 10 events, when missingness/selection materially differs across exposure states, or when the endpoint parser cannot verify code-date pairing. No favorable subgroup or horizon may be substituted after inspecting results.

Computationally checkable claims are field availability, joins, row/participant counts, code-date parsing, timing boundaries, model fits, uncertainty, calibration and whether conclusions match the locked outputs. Clinical adjudication, causal interpretation, biological persistence, clinical utility, treatment benefit, and generalization beyond this UKB subset require expert review, exact specimen dates, richer clinical records or an external prospective study.

## Alternatives not chosen

The transparent category Cox and CRP/metabolic-adjusted residual were matched on inputs and selected because they directly discriminate the rival explanations. A neural sequence model or high-dimensional NMR model was deferred: the bound contains only two sparse GlycA/CRP instances (589 complete pairs), lacks exact assay dates and microbiologic adjudication, and extra capacity would not identify persistence. Revisit a learned longitudinal model only if denser repeated biomarker data and adjudicated infection outcomes become available. This is a scientific deferral, not a restriction against GPU or structured-data models.

The method comparison, measured/estimated resource budget and selection record are in method-alternatives.md. The source audit, exact hashes, and inspected evidence receipts are in source-schema-audit.json and key-references.json.

## Three key references

[K1] Nightingale Health Biobank Collaborative Group; Barrett JC; Esko T; Fischer K; et al. Metabolomic and genomic prediction of common diseases in 700,217 participants in three national biobanks. Nature Communications, 2024. DOI: 10.1038/s41467-024-54357-0. Inspected abstract, study-population methods and repeat-measurement results; excerpt attached.

[K2] Liu X; Zhou D; Liao D; Chen Q. Evidence of immune-metabolic imbalance prior to sepsis: a prospective study in the UK Biobank. Frontiers in Nutrition, 2026. DOI: 10.3389/fnut.2026.1836381. Abstract-focused inspection; excerpt attached.

[K3] Fu X; Li X; Ma X; Wu N; Ni W; Li H. A lifestyle-driven inflammatory load index and its circulating metabolomic signature identify susceptibility to hospital-recorded acute respiratory infections: a population-based cohort study of 295,679 adults. Frontiers in Endocrinology, 2026. DOI: 10.3389/fendo.2026.1878728. Inspected title, abstract and relevant introduction/methods passages; excerpt attached.

All three attached excerpts are UTF-8 and each is below 1 MiB. Their exact byte hashes and retrieval receipts are in key-references.json.
