> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Proposal: Repeat-assessment weight loss as a near-term occult-cancer signal in UK Biobank

## Clinically important unresolved question

In an older adult whose measured body weight has fallen substantially between two encounters, clinicians must distinguish a potentially beneficial long-term change from a marker of occult disease. Existing observational associations between weight loss and cancer are difficult to interpret because intentionality, reverse causation, and the timing of diagnosis are often unresolved. The UK Biobank snapshot can test a narrower, clinically useful and falsifiable claim: **among cancer-free participants with two dated, measured weights, is at least 5% weight loss associated specifically with cancer diagnosed soon after the second measurement, rather than with a persistent elevation across later follow-up?** A near-term-only excess would support use of weight loss as a warning signal, not the claim that weight loss causes cancer.

## Evidence boundary

### Strongest claim already supported by inspected evidence

The configured rectangular export contains participant-level, horizontally joinable, repeated measured-weight values and explicit assessment dates, as well as cancer registry diagnosis-date/code arrays and death dates. In a deterministic prefix audit of the first 20,000 assessment rows, baseline weight was present for 19,896 and repeat values were present at later instances; `53-*` values were ISO dates. In the first 50,000 health-outcome rows, cancer date/code arrays and death dates were populated. This establishes data presence and computational feasibility only.

### Unresolved claim tested

Relative to weight stability (change between -2% and +2%), at least 5% measured weight loss from baseline assessment to the first eligible repeat assessment is associated with a larger adjusted cumulative incidence of first invasive cancer during days 91–730 after the repeat assessment, with attenuation during days 731–1,825. The primary estimand is an observational standardized risk difference, not a causal treatment effect.

### Claims this study cannot establish

The export cannot establish whether weight loss was intentional, whether it was caused by an occult cancer, whether diagnostic work-up improves outcomes, or whether weight loss itself causes or prevents cancer. Those claims require intent/intervention data, clinical adjudication, and a separate prospective or randomized study. Registry codes cannot by themselves adjudicate symptoms, stage, recurrence, or diagnostic pathway.

## Exact Harbor experiment

### Source snapshot and tables

Snapshot: `[source checksum]`. All files are ordinary CSV files and are read-only.

Join one-to-one on `eid` (and assert equality for overlapping fields):

1. `assessment`, source `[internal dataset path]`, schema `datasets/ukb/table-901ef6c7ddce2d51.json`:
   - assessment date: `53-0.0`, `53-1.0`, `53-2.0`, `53-3.0`
   - measured weight: `21002-0.0`, `21002-1.0`, `21002-2.0`, `21002-3.0`
   - BMI for baseline adjustment/sensitivity: `21001-0.0` through `21001-3.0`
   - age at assessment: `21003-0.0` through `21003-3.0`
   - smoking-status field for prespecified adjustment only after its authoritative coding is frozen: `20116-0.0` through `20116-3.0`
2. `health_outcomes`, source `[internal dataset path]`, schema `datasets/ukb/table-3cfae45e0905b0e3.json`:
   - cancer diagnosis dates: `40005-0.0` through `40005-21.0`
   - corresponding cancer type codes: `40006-0.0` through `40006-21.0`
   - death dates: `40000-0.0`, `40000-1.0`
3. `population`, source `[internal dataset path]`, schema `datasets/ukb/table-38565c9e35e7cb6c.json`:
   - sex: `31-0.0` (frozen local coding: 0 female, 1 male)
   - age at recruitment: `21022-0.0` (years)

Before execution, freeze authoritative UK Biobank Showcase definitions for fields 53, 21002, 21001, 21003, 20116, 40005, 40006, and 40000, including units, coding, array semantics, and registry coverage. If authoritative metadata does not establish that `40005-0.k` and `40006-0.k` are corresponding date/code elements, the primary outcome is not computable and the experiment must stop rather than infer pairing from values. No global interpretation of negative codes is permitted.

### Population and temporal boundaries

- Start with all `eid` rows having baseline `53-0.0` and `21002-0.0`.
- Select the chronologically earliest later instance j in {1,2,3} with nonmissing `53-j.0` and `21002-j.0`, a date strictly after baseline, and an interval of 365–3,650 days. Instance number alone never defines elapsed time.
- Index date = `53-j.0` (second eligible dated weight).
- Require age 40–79 years at index, computed from `21003-j.0` after metadata validation (sensitivity: baseline `21022-0.0` plus exact elapsed time).
- Exclude nonpositive or physiologically impossible weights according to a prespecified, metadata-supported range; report every exclusion threshold and count.
- Exclude any cancer registry diagnosis with `40005-0.k < index date`, after pairing to `40006-0.k`; exclude same-day diagnoses. Exclude participants with insufficient outcome coverage through day 90.
- The primary analysis begins on index day 91 to reduce diagnoses already under evaluation. Follow through day 1,825, earliest cancer diagnosis, death, or a country-specific administrative censoring date derived from frozen registry coverage metadata. Do not use the maximum observed event date as if it were complete coverage.

### Exposure and comparator

Percent weight change = 100 × (`21002-j.0` − `21002-0.0`) / `21002-0.0`.

- Primary exposure: loss <= -5%.
- Primary comparator: stable change from -2% through +2% inclusive.
- Secondary mutually exclusive categories: moderate loss (-5% < change < -2%), moderate gain (+2% < change < +5%), and gain >= +5%.
- Secondary continuous analysis uses a restricted cubic spline in percent change. Report baseline and repeat weights, elapsed years, and change distributions; do not call the exposure intentional weight loss.

### Outcomes

Primary: first registry-recorded invasive malignant cancer in days 91–730 after index, defined using `40005-0.k`/`40006-0.k` and a versioned prespecified ICD-10 malignant-neoplasm code list. Non-melanoma skin cancer is excluded in the primary outcome and included in sensitivity analysis. The first qualifying post-index date across paired arrays is the event date.

Temporal specificity outcome: first qualifying cancer in days 731–1,825 among those alive and cancer-free at day 731; this is a secondary landmark estimand, not directly comparable without acknowledging conditioning.

Competing event: death before cancer from `40000-*`. Report cause-specific Cox estimates and Aalen–Johansen cumulative incidence with death as a competing event. All-cause death is also a safety/adverse-pattern outcome because severe weight loss may mark non-cancer illness.

Exploratory cancer-site estimates may be reported only when event counts are adequate and with multiplicity control; they are not primary claims.

### Covariates and selection adjustment

Prespecified index-time model: age, sex, baseline weight/BMI, elapsed time between weights, baseline calendar year, and smoking status at baseline and repeat only if coding metadata is successfully frozen. Add no covariate whose coding is guessed. Missing categorical covariates receive an explicit missing category only when allowed by field metadata; otherwise use multiple imputation and report missingness.

Because repeat assessment is selected, estimate a repeat-participation model in the baseline cohort using only validated baseline fields available both for attendees and non-attendees (age, sex, baseline BMI/weight, baseline smoking if validated, and pre-index cancer-free status). Apply stabilized inverse-probability-of-observation weights, truncate at the 1st/99th percentiles, and report positivity diagnostics and standardized differences. The unweighted analysis is a required sensitivity analysis. This adjustment cannot remove unmeasured selection.

### Analysis

1. Publish a cohort flow with counts for every filter, missingness, date-order violations, and unmatched cancer date/code elements.
2. Estimate standardized 730-day cancer cumulative incidence and risk differences using weighted pooled logistic regression with flexible time and exposure-by-time terms; bootstrap `eid` 1,000 times for 95% CIs.
3. Estimate competing-risk cumulative incidence and cause-specific hazard ratios as complementary measures.
4. For temporal specificity, estimate the day-731 landmark 3-year risk difference separately. Also plot hazard ratios in 0–90, 91–365, 366–730, 731–1,825 day intervals; the excluded 0–90 interval is a diagnostic analysis, never part of the primary estimand.
5. Sensitivities: loss thresholds 3%, 5%, and 10%; intervals restricted to 2–6 years; adjustment for starting BMI spline; exclude cancer in first 365 days; complete-case versus imputed; weighted versus unweighted; non-melanoma skin cancer included/excluded; analyses stratified by sex and smoking only if coding/event support is adequate.
6. Quantify an E-value for the primary risk ratio solely as an unmeasured-confounding sensitivity metric, not evidence of causality.

### Falsification and bias checks

- **Temporal-gradient check:** occult-disease signaling predicts the strongest association in days 0–90 and 91–730 with attenuation thereafter. A constant or increasing association after day 730 contradicts the proposed near-term-warning interpretation.
- **Future-exposure negative control:** among participants with a third dated weight, test whether weight change occurring only after the index predicts cancer before that later measurement. Any association flags selection, coding, or time-order bias; future data must not enter the primary model.
- **Date-pair integrity:** require equal missingness status for each cancer date/code pair where metadata says they correspond; report discordances and stop if pairing integrity is materially violated.
- **Positive-pattern check, not proof:** all-cause mortality should generally rise with large loss if it is a marker of illness. Absence does not invalidate the cancer result, and presence does not prove occult cancer.

## Interpretation rules

### Supportive

The adjusted 730-day risk difference for >=5% loss versus stable weight is positive with a 95% CI excluding zero, the estimate is materially larger in the early window than at the day-731 landmark, results retain direction under the 365-day washout and selection weighting, and the future-exposure negative control is near null. The justified conclusion is: substantial measured weight loss identifies a subgroup with elevated near-term registry-recorded cancer incidence in this selected repeat-assessment cohort. It does not justify causal language or universal diagnostic screening.

### Adverse/contradictory

The 730-day estimate is null or negative with an interval excluding the prespecified minimum clinically important risk difference of +0.5 percentage points, or the association is stronger after day 730 than before it, or negative-control timing is similarly associated. This contradicts the proposed near-term occult-cancer-warning pattern and argues against using this UKB association to motivate near-term work-up.

### Inconclusive

The 95% CI includes both zero and +0.5 percentage points; effective sample size after weighting is inadequate; positivity is poor; date/code pairing or censoring coverage cannot be verified; results are highly sensitive to washout/selection adjustment; or the future-exposure control is non-null. The conclusion must then be that this snapshot does not resolve the hypothesis.

The +0.5 percentage-point margin is a prespecified decision-scale benchmark for interpretability, not a universal clinical threshold; clinical experts and health-economic evidence would be needed before any diagnostic policy.

## Computation versus adjudication

Automatically checkable: source hashes/headers, one-to-one `eid` joins, chosen repeat instance, date ordering, weight-change calculation, cohort counts, paired-array implementation, event windows, censoring code, effect estimates, confidence intervals, diagnostics, and whether narrative conclusions match supportive/adverse/inconclusive rules.

Not automatically establishable: cancer validity beyond the registry definition, weight-loss intentionality, occult symptoms, stage, causal mechanism, appropriateness or benefit of diagnostic testing, transportability outside UKB repeat attendees, and clinical importance of a particular risk difference. These require field-definition review, oncology/primary-care adjudication, external validation, and possibly a prospective study.

## Provenance

Local evidence files: `derived/header_audit.json`, `derived/known_field_presence.json`, and `derived/light_field_sample.json`. The latter used deterministic prefix samples (50,000 health rows and 20,000 assessment rows) and records selected columns, nonmissing counts, and examples; it is a feasibility audit, not a prevalence estimate. Public Showcase fetches attempted during design returned an internal listing error and therefore are not treated as field-definition evidence. The compiler must acquire/freeze usable authoritative definitions before executing coded clinical variables.
