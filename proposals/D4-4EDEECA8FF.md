> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB-36: Pre-cancer Physical Reserve (Grip Strength + Renal Function) and Post-colorectal-cancer Non-cancer Mortality — A Competing Risk Analysis

## Unresolved Question

Colorectal cancer (CRC) survivors face two distinct mortality risks: death from the cancer itself and death from non-cancer causes (cardiovascular disease, other malignancies, infections, metabolic complications). Current prognostic models for CRC focus almost exclusively on cancer-specific survival, treating non-cancer death as a competing event or censoring it. However, it remains unclear whether **pre-diagnosis physical reserve** — measured by grip strength (a proxy for skeletal muscle function and overall physiological capacity) and renal function (creatinine, a marker of metabolic and vascular health) — independently predicts **non-cancer mortality** after CRC diagnosis, beyond its well-established association with overall survival.

This question is clinically important because:
1. If pre-cancer physical reserve independently predicts non-cancer death, it identifies a modifiable risk factor (exercise, renal protection) that could be targeted in survivorship care.
2. If the association is confined to cancer death (i.e., low grip reflects advanced tumor burden rather than host frailty), then the clinical implication is staging/treatment optimization rather than survivorship intervention.
3. The distinction between these two mechanisms requires a competing risk framework that separates the hazard of non-cancer death from the hazard of cancer death, rather than treating them as a single "all-cause mortality" endpoint.

## Hypothesis

In UK Biobank participants with incident CRC (ICD10 C18-C20) and pre-cancer measurements of grip strength and creatinine, **lower pre-diagnosis grip strength** (tertile 1 vs tertile 3) is associated with a significantly higher **subdistribution hazard ratio (sHR) for non-cancer death** after CRC diagnosis, independent of age, sex, BMI, and time from assessment to diagnosis, after accounting for cancer death as a competing event. Specifically:

- **Primary hypothesis**: The sHR for non-cancer death per 5-kg decrease in grip strength (or tertile 1 vs tertile 3) is >1.1 after full adjustment.
- **Secondary hypothesis**: The sHR for non-cancer death is attenuated (closer to 1.0) when restricting to participants with >2 years between assessment and cancer diagnosis (reducing the likelihood that low grip reflects occult tumor burden).
- **Tertiary hypothesis**: Renal function (creatinine) modifies the grip strength–non-cancer mortality association, such that the combined low-grip + high-creatinine group has a higher sHR than either factor alone.

## Clinical Importance

CRC is the third most common cancer globally, with ~5-year overall survival of ~60% in high-income countries. A substantial fraction of CRC deaths, particularly in early-stage disease, are attributable to non-cancer causes. Current clinical guidelines for CRC survivorship focus on surveillance for recurrence and general cardiovascular risk management, but do not incorporate pre-diagnosis functional biomarkers. If pre-cancer grip strength and renal function independently predict non-cancer mortality, this would:

1. Support the use of simple, inexpensive bedside measurements (handgrip dynamometer, serum creatinine) as part of CRC survivorship risk stratification.
2. Identify a window for intervention: prehabilitation (exercise, nutritional optimization) before or after CRC treatment to improve non-cancer survival.
3. Distinguish "host reserve" effects from "tumor burden" effects, informing whether frail CRC patients should receive modified treatment or enhanced supportive care.

## Population Definition

**Source**: [UKB data file] (ukb671626)

**Inclusion criteria**:
1. CRC diagnosis: ICD10 code C18, C19, or C20 in field 40006 (Type of cancer: ICD10)
2. Pre-cancer grip strength: non-null value in field 46 (Hand grip strength left, kg) or 47 (Hand grip strength right, kg), with assessment date (field 53) **before** cancer diagnosis date (field 40005)
3. Pre-cancer creatinine: non-null value in field 30700 (Creatinine, µmol/L), with assessment date before cancer diagnosis date
4. Death or censoring: field 40000 (Date of death) non-null OR alive at data snapshot
5. Cause of death: field 40001 (Underlying cause of death: ICD10) for death classification

**Exclusion criteria**:
- Assessment date after cancer diagnosis date (reverse temporality)
- Missing sex (field 31)
- Age < 40 or > 90 at cancer diagnosis (computed from field 21003 date of birth and field 40005)
- More than 10 years between assessment and cancer diagnosis (to limit reverse causation from long-standing comorbidity)

**Verified feasibility**: 6,884 CRC cases with pre-cancer grip and creatinine; 2,206 deaths (including both cancer and non-cancer deaths).

## Temporal Boundaries

| Event | Field | Role |
|-------|-------|------|
| Assessment centre visit | 53 (Date of attending AC) | Baseline measurement date |
| Cancer diagnosis | 40005 (Date of cancer diagnosis) | Index event / start of follow-up |
| Death | 40000 (Date of death) | Terminal event |
| Cause of death | 40001 (ICD10) | Event classification |

**Follow-up window**: From cancer diagnosis date (40005) to death date (40000) or data snapshot (latest available date in dataset).

**Pre-cancer measurement window**: Assessment date (53) must be before cancer diagnosis date (40005). Sensitivity analysis stratifies by time interval: <1 year, 1-2 years, 2-5 years, >5 years.

## Variables

### Exposure variables (measured pre-cancer)
| Variable | Field | Unit | Transformation |
|----------|-------|------|----------------|
| Grip strength (left) | 46-0.0 | kg | Continuous; tertiles by sex |
| Grip strength (right) | 47-0.0 | kg | Continuous; tertiles by sex |
| Grip strength (max) | max(46, 47) | kg | Primary exposure |
| Creatinine | 30700-0.0 | µmol/L | Continuous; eGFR if possible |

### Covariates (measured pre-cancer)
| Variable | Field | Role |
|----------|-------|------|
| Sex | 31-0.0 | Stratification + adjustment |
| Age at diagnosis | 21003 (DOB) → 40005 | Adjustment (continuous, per 10 years) |
| BMI | 21001-0.0 | Adjustment (continuous, per 5 kg/m²) |
| Time from AC to diagnosis | 40005 - 53 | Stratification (sensitivity) |

### Outcome variables
| Outcome | Definition | ICD10 codes |
|---------|-----------|-------------|
| Cancer death | Death with underlying cause C18-C20 | 40001 ∈ {C18, C19, C20} |
| Non-cancer death | Death with underlying cause not C18-C20 | 40001 ∉ {C18, C19, C20} |
| Censored | Alive at data snapshot | 40000 null |

## Analysis Plan

### Primary analysis: Fine-Gray competing risk model

**Model**: Fine-Gray subdistribution hazard model for **non-cancer death** with **cancer death** as the competing event.

- **Dependent variable**: Time from cancer diagnosis to non-cancer death (event=1), cancer death (competing event=2), or censoring (event=0)
- **Exposure**: Grip strength (continuous per 5-kg decrease; and tertile 1 vs 3)
- **Covariates**: Age at diagnosis (per 10 years), sex, BMI (per 5 kg/m²), time from AC to diagnosis (category)
- **Estimate**: Subdistribution hazard ratio (sHR) with 95% confidence interval

**Software**: R `cmprisk::crr()` or Python `lifelines` / custom implementation. The Fine-Gray model estimates the effect of covariates on the subdistribution of the event of interest, accounting for the fact that individuals who experience the competing event (cancer death) are no longer at risk of the event of interest (non-cancer death) but are not simply censored — they are permanently removed from the risk set.

### Baseline analysis: Cox PH for cancer death

**Model**: Standard Cox proportional hazards model for **cancer death** (cancer-specific hazard), with non-cancer death and censoring treated as censored observations.

- This serves as a reference to compare the magnitude and direction of the grip strength effect on cancer death vs non-cancer death.
- If grip strength predicts cancer death but not non-cancer death, this supports the "tumor burden" interpretation.
- If grip strength predicts non-cancer death but not cancer death, this supports the "host reserve" interpretation.

### Sensitivity analyses

1. **Time-stratified analysis**: Repeat Fine-Gray model in strata of time from AC visit to cancer diagnosis (<1 year, 1-2 years, 2-5 years, >5 years). If the association is confined to <1 year, this supports the "occult tumor" explanation (low grip reflects pre-existing cancer).

2. **Renal function interaction**: Add creatinine (or eGFR) as a covariate and test grip × creatinine interaction. The combined low-grip + high-creatinine group should have a higher sHR if the two markers capture complementary aspects of physiological reserve.

3. **Sex-stratified analysis**: Repeat primary analysis separately in men and women, as grip strength distributions differ substantially by sex.

4. **Exclusion of early deaths**: Exclude deaths within 1 year of diagnosis to reduce the impact of treatment-related mortality and acute complications.

### What the competing risk approach reveals that Cox PH loses

A standard Cox PH model for all-cause mortality (or cancer-specific mortality with non-cancer death censored) treats non-cancer deaths as if they were "lost to follow-up." This is problematic because:
- Non-cancer death is **informative**: individuals who die of cardiovascular disease are no longer at risk of dying of cancer, but their removal from the risk set changes the composition of the remaining cohort.
- The Fine-Gray sHR directly estimates the effect of grip strength on the **cumulative incidence** of non-cancer death in the presence of the competing risk of cancer death. This is the clinically relevant quantity: "What is the probability that a CRC patient with low grip strength will die of a non-cancer cause within 5 years?"
- The cause-specific hazard (Cox PH) estimates the instantaneous rate of non-cancer death among those still alive, which is a different (and less clinically intuitive) quantity.

## Falsification Criteria

| Outcome | sHR for non-cancer death (low grip vs high grip) | Interpretation |
|---------|--------------------------------------------------|----------------|
| **Supportive** | sHR > 1.1 (95% CI excluding 1.0) after full adjustment | Pre-cancer grip strength independently predicts non-cancer mortality; supports host reserve hypothesis |
| **Adverse** | sHR 0.9-1.1 (95% CI including 1.0) after full adjustment | No independent effect of grip strength on non-cancer mortality; the association with overall survival is driven by cancer death |
| **Inconclusive** | Wide CIs (e.g., 0.7-1.5) or <50 non-cancer deaths in a stratum | Insufficient power; cannot distinguish supportive from adverse |

**Additional falsification**: If the sHR is significant in the full cohort but attenuated to null when restricting to >2 years from assessment to diagnosis, this supports the "occult tumor" rival explanation and weakens the host reserve interpretation.

## Alternative Explanations (Rival Hypotheses)

1. **Late-stage occult tumor**: Low grip strength measured close to diagnosis may reflect the catabolic effects of an undiagnosed or early-stage tumor rather than pre-existing frailty. **Test**: Time-stratified sensitivity analysis. If the association disappears when restricting to >2 years, the occult tumor explanation is favored.

2. **Treatment differences**: Frailer patients may receive less aggressive treatment (e.g., surgery vs watch-and-wait, full-dose vs reduced-dose chemotherapy), which could increase both cancer and non-cancer mortality. **Limitation**: UK Biobank does not have detailed treatment data. This cannot be directly tested but is acknowledged as a residual confounder.

3. **Selection bias / healthy volunteer effect**: UK Biobank participants are healthier than the general population. However, this affects the absolute risk, not the relative association between grip strength and mortality within the cohort.

4. **Reverse causation from comorbidity**: Low grip strength and elevated creatinine may both be consequences of shared comorbidities (e.g., heart failure, chronic kidney disease) rather than independent markers of physiological reserve. **Test**: The grip × creatinine interaction analysis can partially address this.

5. **Measurement artifact**: Grip strength is measured once at the AC visit. A single measurement may not capture habitual muscle function. **Limitation**: Only one visit is available in this dataset; repeat measurements are not feasible.

## Method Comparison: Fine-Gray vs Cox PH

| Feature | Fine-Gray (primary) | Cox PH (baseline) |
|---------|---------------------|-------------------|
| Estimand | Subdistribution hazard: effect on cumulative incidence of non-cancer death | Cause-specific hazard: instantaneous rate of non-cancer death among survivors |
| Competing events | Explicitly modeled (cancer death) | Treated as censored (non-cancer death for cancer model, or vice versa) |
| Clinical interpretation | "What is the probability of dying of non-cancer causes?" | "What is the instantaneous rate of non-cancer death among those still alive?" |
| When they differ | When competing events are common and informative | When competing events are rare or non-informative |
| What Cox PH loses | The effect of the competing event on the risk set composition | — |

In this cohort, ~32% of deaths (2,206/6,884) are from any cause, and a substantial fraction are non-cancer deaths. The competing risk is therefore non-negligible, and the Fine-Gray approach is appropriate.

## Data Bindings (Verified)

| Field | Column | Non-null count | Role |
|-------|--------|----------------|------|
| 46-0.0 | Grip left (kg) | 498,958 | Exposure |
| 47-0.0 | Grip right (kg) | 499,025 | Exposure |
| 30700-0.0 | Creatinine (µmol/L) | 469,235 | Exposure/covariate |
| 40005-0.0 | Cancer date | 123,681 | Index event |
| 40006-0.0 | Cancer ICD10 | 7,393 (CRC C18-C20) | Case definition |
| 40000-0.0 | Death date | 44,499 | Terminal event |
| 40001-0.0 | Cause of death ICD10 | 44,197 | Event classification |
| 31-0.0 | Sex | 502,371 | Covariate |
| 53-0.0 | AC date | 502,371 | Baseline date |
| 21001-0.0 | BMI | ~500,000 | Covariate |
| 21003-0.0 | DOB | ~500,000 | Age calculation |

**CRC + grip + creatinine overlap**: 6,884
**CRC + grip + creatinine + death**: 2,206

**Source file**: `[internal dataset path]`

## Key References

### [K1] Dai X, Zhang X, Wang H, et al. "Multidimensional physiological impairments are associated with frailty and survival in older patients with cancer." J Transl Int Med. 2026;14(4):589-598. DOI: 10.1515/jtim-2026-0057. PMC13509152.

- **Claim supported**: Frailty (including multidimensional physiological impairments such as malnutrition, metabolic disturbance, and inflammation) is associated with significantly worse survival in older cancer patients (adjusted HR = 1.67, 95% CI 1.45-1.92 for frail vs pre-frail) [K1].
- **Contribution of this proposal**: Extends the frailty-survival association to a specific, measurable pre-cancer biomarker (grip strength) in a specific cancer type (CRC), and uses a competing risk framework to separate cancer from non-cancer mortality.
- **Limitation**: Uses overall survival (not cause-specific), Fried frailty criteria (not grip strength alone), and a single-center Chinese cohort (not population-based).

### [K2] Ichimasa K, Kudo SE, Kouyama Y, et al. "Competing Mortality Redefines the Net Benefit of Additional Surgery After Endoscopic Resection for T1 Colorectal Cancer in Older Adults." Dig Endosc. 2026;38(7):e70222. DOI: 10.1111/den.70222. PMC13332411.

- **Claim supported**: Competing mortality (non-cancer death) is a major determinant of outcomes in CRC, particularly in older adults [K2]. Most deaths in the nonsurgical group for T1 CRC were attributable to causes other than cancer. The survival advantage of surgery becomes evident only after 10 years, while perioperative risks are immediate.
- **Contribution of this proposal**: Provides a population-based, quantitative test of whether pre-cancer physical reserve predicts the non-cancer mortality component, rather than a review of treatment decision-making.
- **Limitation**: Review article, not original data. Focuses on T1 CRC and surgical decision-making, not on pre-cancer biomarkers.

### [K3] Zhang N, Chen S, Ai J, et al. "Follow-up–dependent calendar-period associations with cardiac mortality after lung cancer radiotherapy: a competing-risks SEER analysis." Open Med. 2026;21(1):20261509. DOI: 10.1515/med-2026-1509. PMC13576467.

- **Claim supported**: Competing risk analysis (Fine-Gray model) is essential for correctly estimating cause-specific mortality in cancer survivors, as calendar-period comparisons can be distorted by competing cancer death and unequal follow-up [K3]. The subdistribution hazard ratio (sHR) is the appropriate estimand for cumulative incidence of non-cancer death.
- **Contribution of this proposal**: Applies the same competing risk methodology to a different cancer type (CRC vs lung) and a different exposure (pre-cancer grip strength vs treatment era), testing whether pre-cancer physical reserve predicts non-cancer mortality.
- **Limitation**: Different cancer type (lung), different exposure (treatment era, not physical reserve), and registry-based (SEER) rather than biobank-based (no grip strength measurement).

## Scientific Deliverable

The scientific deliverable is a **newly fitted Fine-Gray competing risk model** estimating the subdistribution hazard ratio for non-cancer death in CRC patients, stratified by pre-cancer grip strength, with cancer death as the competing event. The outputs that establish completion are:

1. Fine-Gray sHR (95% CI) for non-cancer death per 5-kg decrease in grip strength, adjusted for age, sex, BMI, and time from AC to diagnosis.
2. Fine-Gray sHR (95% CI) for non-cancer death in grip tertile 1 vs tertile 3.
3. Cox PH HR (95% CI) for cancer death (baseline comparison).
4. Time-stratified sHRs (sensitivity analysis).
5. Grip × creatinine interaction sHR (sensitivity analysis).
6. Sex-stratified sHRs (sensitivity analysis).

## Compute Resources

- **CPU**: 4-8 cores (Fine-Gray model fitting is computationally light for n=6,884)
- **Memory**: 16 GB (sufficient for parquet loading and model fitting)
- **GPU**: Not required
- **Time**: <1 hour for all analyses (data loading + model fitting + sensitivity analyses)
- **Software**: Python (pandas, numpy, lifelines or custom Fine-Gray implementation), or R (cmprisk, survival)

## Limitations

1. **No staging or treatment data**: UK Biobank does not provide tumor stage, grade, or treatment details. This limits the ability to adjust for treatment intensity or distinguish early from late-stage disease.
2. **Single measurement**: Grip strength and creatinine are measured once at the AC visit. Repeat measurements are not available.
3. **ICD10 cause of death**: The underlying cause of death is coded by ICD10, which may misclassify some deaths (e.g., a patient with CRC who dies of sepsis secondary to chemotherapy may be coded as infection rather than cancer).
4. **No genetic or molecular data**: Cannot adjust for germline risk factors (e.g., Lynch syndrome) or tumor molecular features (e.g., MSI status).
5. **UK Biobank selection bias**: Participants are healthier than the general population, limiting generalizability to absolute risk estimates (though relative associations are less affected).
