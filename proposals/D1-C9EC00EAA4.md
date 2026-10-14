> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Discordant Organ Recovery Predicts ICU Deterioration

## Hypothesis

In critically ill ICU patients, the presence of discordant organ recovery (one organ function improving while another continues to decline) after initial circulatory stabilization predicts subsequent deterioration more strongly than either organ's recovery alone.

## Scientific Rationale

Current ICU practice relies on aggregate severity scores (SOFA, qSOFA) that measure organ dysfunction at discrete time points. These aggregate measures may mask discordant organ trajectories. Patients whose kidney and respiratory functions diverge in their recovery patterns may require fundamentally different management strategies than those with uniform recovery or no recovery. Understanding these discordant patterns could improve risk stratification and guide targeted organ support.

This hypothesis builds on insights from recent literature:
- **ALADYNOULLI (Nature 2026)** demonstrates that latent disease signatures can be identified from longitudinal EHR data, revealing biological subtypes within diagnostic categories
- **Chen et al. (Front Cell Infect Microbiol 2026)** shows that longitudinal SOFA score trajectories can be modeled using group-based trajectory modeling in ICU patients
- **Abdel-Nabey et al. (Crit Care Med 2021)** examines acute kidney injury recovery patterns in critically ill patients, establishing baseline organ recovery assessment methods

The key gap this addresses is that existing methods focus on either:
1. Single-organ recovery assessment (e.g., kidney recovery alone)
2. Aggregate severity scores (e.g., SOFA) that mask discordant trajectories

This hypothesis tests whether discordance between organ systems provides additional prognostic information beyond what is captured by single-organ or aggregate measures.

## Study Population and Main Data

- **Population**: ICU patients in MIMIC-IV with documented infection or shock
- **Inclusion criteria**:
  - ICU admission with diagnosis of infection or shock
  - ≥2 organ support measurements (SOFA scores)
  - Age ≥18 years
- **Exclusion criteria**:
  - Patients discharged within 24 hours of admission
  - Missing key variables (SOFA respiratory, SOFA renal, SOFA cardiovascular)

## Main Data Tables

- `icustay`: ICU admission records with organ support measurements
  - Key columns: `stuy_id`, `admit_id`, `admit_time`, `sofa_score`, `sofa_respiratory`, `sofa_cardiovascular`, `sofa_hepatic`, `sofa_renal`, `sofa_coagulation`, `sofa_cns`

- `admission`: Patient demographics and comorbidities
  - Key columns: `admit_id`, `age`, `sex`, `charlson_index`

- `diagnoses_icu`: ICU admission diagnoses
  - Key columns: `stuy_id`, `admit_id`, `admit_time`, `diagnosis`

## Temporal Boundaries

- **Start**: Time of ICU admission (`admit_time`)
- **End**: ICU discharge or death (whichever occurs first)
- **Follow-up window**: 28 days from ICU discharge for readmission/death outcomes
- **Discordance assessment window**: 72 hours after initial circulatory stabilization

## Discordance Index Definition

The discordance index will be defined as the **slope of the difference between two organ support scores** over time, after initial circulatory stabilization:

```
Discordance Index = slope of (Organ A SOFA - Organ B SOFA) over time
```

Where:
- **Organ A**: Respiratory (sofa_respiratory)
- **Organ B**: Renal (sofa_renal)
- **Positive discordance**: Respiratory function improving faster than renal function
- **Negative discordance**: Renal function improving faster than respiratory function
- **Zero discordance**: Both organs recovering at similar rates

**Circulatory stabilization definition**: SOFA score reaching threshold of 8 or less for ≥2 consecutive measurements over 24 hours.

## Primary Outcome

- **Primary endpoint**: ICU mortality within 28 days from admission
- **Secondary endpoint**: ICU readmission within 30 days from discharge

## Baseline Model

**Single-organ recovery models**:
1. **Renal recovery model**: Time to renal recovery (sofa_renal ≤ 2)
2. **Respiratory recovery model**: Time to respiratory recovery (sofa_respiratory ≤ 2)
3. **Aggregate recovery model**: Time to aggregate SOFA recovery (sofa_score ≤ 8)

These baseline models represent the current standard of care, which focuses on either single-organ recovery or aggregate severity scores.

## Alternative Model

**Discordance index model**:
- **Model**: Cox proportional hazards regression with discordance index as time-varying covariate
- **Features**:
  - Discordance index (continuous)
  - Baseline SOFA score (continuous)
  - Age (continuous)
  - Sex (binary)
  - Charlson index (continuous)
  - Admission diagnosis (categorical)

## Analysis Plan

### Primary Analysis
- **Method**: Cox proportional hazards regression with discordance index as time-varying covariate
- **Model**: Hazard ratio for ICU mortality associated with discordance index
- **Adjustment**: For baseline SOFA score, age, sex, Charlson index, admission diagnosis

### Secondary Analysis
- **Method**: Machine learning models (random forests, gradient boosting) with discordance index as feature
- **Validation**: Internal validation (bootstrapping, 10-fold cross-validation)
- **External validation**: If other MIMIC cohorts available

### Temporal Analysis
- **Method**: Group-based trajectory modeling of discordance index over time
- **Goal**: Identify distinct discordance trajectory patterns

## Falsification Criteria

- **Hypothesis falsified**: Discordance index shows no association with ICU mortality after adjusting for baseline SOFA score, age, sex, Charlson index, and admission diagnosis (p > 0.05)
- **Hypothesis supported**: Discordance index shows significant association with ICU mortality after adjusting for covariates (p < 0.05)
- **Hypothesis partially supported**: Discordance index shows association with one outcome but not the other (e.g., mortality but not readmission)

## Supportive, Adverse, and Inconclusive Results

### Supportive Results
- Discordance index predicts ICU mortality better than single-organ or aggregate recovery models
- Discordance index identifies distinct patient subgroups with different outcomes
- Discordance index patterns correlate with specific organ system interventions

### Adverse Results
- Discordance index predicts outcomes worse than single-organ or aggregate recovery models
- Discordance index adds no value beyond existing risk stratification methods
- Discordance index patterns are unstable across different patient cohorts

### Inconclusive Results
- Discordance index shows no association with outcomes after adjusting for baseline SOFA score and other covariates
- Discordance index requires additional data (e.g., more granular organ measurements) for meaningful interpretation
- Discordance index patterns are too rare to draw meaningful conclusions

## Data Bindings

### MIMIC-IV Tables
- `datasets/mimic/icustay.csv`: ICU admission records with organ support measurements
- `datasets/mimic/admission.csv`: Patient demographics and comorbidities
- `datasets/mimic/diagnoses_icu.csv`: ICU admission diagnoses

### Required Columns
- `icustay`: `stuy_id`, `admit_id`, `admit_time`, `sofa_score`, `sofa_respiratory`, `sofa_cardiovascular`, `sofa_hepatic`, `sofa_renal`, `sofa_coagulation`, `sofa_cns`
- `admission`: `admit_id`, `age`, `sex`, `charlson_index`
- `diagnoses_icu`: `stuy_id`, `admit_id`, `admit_time`, `diagnosis`

### Join Keys
- `stuy_id` to join `icustay` and `diagnoses_icu`
- `admit_id` to join `icustay`, `admission`, and `diagnoses_icu`
- `admit_time` to join `icustay` and `diagnoses_icu`

### Time Fields
- `admit_time`: ICU admission time (Unix timestamp)
- `sofa_time`: Time of SOFA measurement (implied by `icustay` structure)

## Method Comparison

### Baseline Model
- **Model**: Single-organ recovery models (e.g., renal recovery alone, respiratory recovery alone)
- **Information**: Single-organ recovery patterns
- **Limitations**: Does not capture discordant organ trajectories; may miss patients with mixed recovery patterns

### Learned/Mechanical Alternative
- **Model**: Discordance index model (e.g., gradient boosting with discordance index as feature)
- **Information**: Discordant organ trajectories
- **Advantages**: Captures discordant organ trajectories that may require different management strategies; potentially more informative than single-organ recovery models

### Selection Reason
- The discordance index model is scientifically more informative than single-organ recovery models, as it captures discordant organ trajectories that may require fundamentally different management strategies
- The baseline model is necessary to establish the incremental value of the discordance index model
- This comparison tests a substantive scientific uncertainty: whether discordant organ trajectories provide prognostic information beyond what is captured by single-organ or aggregate measures

## Resource/Time Budget

- **CPU**: 4 cores, 16GB memory
- **GPU**: 0 (not required for this analysis)
- **Time**: 3600 seconds (1 hour)
- **Memory**: 16GB

## Key References

Three key references have been identified and will be attached in key-references.json:

1. **Urbut et al. (2026)** - ALADYNOULLI framework for longitudinal EHR analysis
   - DOI: 10.1038/s41586-026-10780-5
   - Contribution: Demonstrates that latent disease signatures can be identified from longitudinal EHR data, revealing biological subtypes within diagnostic categories

2. **Chen et al. (2026)** - Longitudinal SOFA score trajectories in ICU patients
   - DOI: 10.3389/fcimb.2026.1756348
   - Contribution: Shows that longitudinal SOFA score trajectories can be modeled using group-based trajectory modeling in ICU patients

3. **Abdel-Nabey et al. (2021)** - Acute kidney injury recovery patterns in critically ill patients
   - DOI: 10.1097/CCM.0000000000005008
   - Contribution: Examines acute kidney injury recovery patterns in critically ill patients, establishing baseline organ recovery assessment methods

## Limitations

1. **Data availability**: Requires SOFA respiratory and SOFA renal measurements at sufficient temporal resolution to calculate discordance index
2. **Temporal resolution**: SOFA measurements may not be frequent enough to capture rapid discordance patterns
3. **Causal inference**: Observational design cannot establish causality; discordance may be a marker of underlying pathophysiology rather than a modifiable factor
4. **Clinical applicability**: Discordance index may not be actionable in routine ICU practice without additional validation
5. **Missing data**: Patients with incomplete SOFA measurements may be excluded, introducing selection bias

## Next Steps

1. **Verify data availability**: Confirm that required columns (sofa_respiratory, sofa_renal) are available in MIMIC-IV with sufficient temporal resolution
2. **Define temporal windows**: Specify exact temporal windows for discordance index calculation
3. **Baseline model development**: Develop single-organ recovery models
4. **Alternative model development**: Develop discordance index model
5. **Analysis**: Perform Cox proportional hazards regression and machine learning models
6. **Validation**: Internal validation (bootstrapping), external validation (if other MIMIC cohorts available)
7. **Reference delivery**: Attach key-references.json with three inspected key works

## Scientific Significance

This hypothesis addresses a gap in current ICU monitoring that treats all organ dysfunction equally. By quantifying discordant organ trajectories, this research could:
- Improve risk stratification for ICU patients
- Guide targeted organ support strategies
- Inform development of more granular monitoring systems
- Identify patients who may benefit from specific interventions based on their discordance patterns

## Unresolved Questions

1. **Temporal resolution**: What temporal resolution of SOFA measurements is required to capture meaningful discordance patterns?
2. **Organ pairs**: Which organ pairs show the most clinically relevant discordance patterns?
3. **Actionability**: What clinical interventions are associated with specific discordance patterns?
4. **External validation**: Does discordance index predict outcomes consistently across different ICU populations?
5. **Mechanistic understanding**: What underlying pathophysiological mechanisms drive discordant organ recovery patterns?
