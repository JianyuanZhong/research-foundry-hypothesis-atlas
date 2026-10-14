> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Scientific Proposal: Multi-Organ Impairment Duration After Circulatory Stabilization Predicts Post-Stabilization Deterioration

## Unresolved Question

Current critical care practice assesses recovery after circulatory stabilization using either:
1. Single-organ metrics (e.g., creatinine for kidney, WBC for inflammation)
2. Aggregate scores (e.g., SOFA) at fixed time points

However, these approaches fail to capture the **temporal dynamics** of multi-organ impairment. Specifically, we propose that:

**The duration of multi-organ impairment (≥2 organ systems impaired) after circulatory stabilization is an independent predictor of subsequent deterioration, with a critical threshold effect beyond which risk increases exponentially.**

This is distinct from existing work that:
- Focuses on single-organ discordance (kidney vs inflammatory recovery)
- Uses static SOFA scores rather than temporal duration metrics
- Does not explicitly test threshold effects on multi-organ impairment

## Clinical Importance

1. **Current practice limitation**: Single-organ or aggregate SOFA assessments at fixed time points do not capture the temporal dynamics of multi-organ recovery
2. **Patient safety**: Patients who remain multi-organ impaired for extended periods may be at exponentially higher risk of deterioration, yet this is not captured by current monitoring
3. **Resource allocation**: Identifying patients with prolonged multi-organ impairment could inform extended monitoring and escalation strategies
4. **Mechanistic insight**: Understanding the threshold effect on multi-organ impairment may reveal pathophysiological mechanisms of deterioration

## Data Bindings (MIMIC-IV)

### Population
- Patients with admission diagnosis of infection or shock (ICD-9: 390-599, 785.5, 785.9, 787.0, 787.1)
- ICU stay duration ≥ 48 hours
- At least one organ support (vasopressors, dialysis, or mechanical ventilation)

### Tables and Columns
1. **hosp/admissions**: `subject_id`, `hadm_id`, `admissiontime`, `dischargetime`, `diagnoses_icd`
   - Filter for infection/shock admissions

2. **icu/icustays**: `subject_id`, `hadm_id`, `stay_id`, `intime`, `outtime`, `careunit`, `ingredients`
   - Define circulatory stabilization (cessation of vasopressors)
   - Track ICU stay duration

3. **icu/ingredientevents**: `subject_id`, `stay_id`, `caregiver_id`, `charttime`, `itemid`, `value`, `valueuom`
   - Vasopressors (filter itemid for vasopressor class)
   - Dialysis (filter itemid for dialysis class)
   - Mechanical ventilation (filter itemid for ventilation class)

4. **hosp/d_labitems**: `itemid`, `label`, `fluid`
   - Map creatinine (e.g., "CREATININE", "CRE")
   - Map WBC (e.g., "WBC", "WBC COUNT")
   - Map platelets (e.g., "PLATELET", "PLT")
   - Map other organ function markers

5. **icu/outputevents**: `subject_id`, `stay_id`, `caregiver_id`, `charttime`, `itemid`, `value`, `valueuom`
   - Urine output (filter itemid for urine output)

6. **icu/datetimeevents**: `subject_id`, `stay_id`, `caregiver_id`, `charttime`, `itemid`, `value`, `valueuom`
   - Additional time-series measurements

### Organ Impairment Definition
After circulatory stabilization (defined as 24 hours without vasopressors):
- **Kidney impairment**: Creatinine ≥ 2.0 mg/dL (or 180% of baseline) for ≥24 hours
- **Respiratory impairment**: Mechanical ventilation or PaO2/FiO2 < 300 mmHg for ≥24 hours
- **Cardiovascular impairment**: Vasopressor requirement or MAP < 65 mmHg for ≥24 hours
- **Hepatic impairment**: Bilirubin ≥ 3.0 mg/dL for ≥24 hours
- **Hematologic impairment**: Platelets < 50,000/μL for ≥24 hours

Multi-organ impairment = ≥2 of the above systems impaired simultaneously for ≥24 hours

## Hypothesis Specification

### Primary Hypothesis
**H0**: Duration of multi-organ impairment after stabilization does not independently predict subsequent deterioration (adjusted HR = 1.0, p ≥ 0.05)

**H1**: Duration of multi-organ impairment after stabilization independently predicts subsequent deterioration with a critical threshold effect (adjusted HR > 1.5 for each hour beyond threshold, p < 0.001)

### Secondary Hypotheses
1. Multi-organ impairment duration predicts deterioration better than single-organ impairment duration
2. Multi-organ impairment duration predicts deterioration better than aggregate SOFA score at stabilization
3. The critical threshold of multi-organ impairment duration varies by patient subgroup (e.g., age, comorbidities)

## Baseline Comparisons

### Baseline 1: Single-Organ Impairment Duration
- Compare duration of single-organ impairment (kidney only, respiratory only, etc.) with multi-organ impairment duration
- Test if multi-organ duration provides incremental predictive value

### Baseline 2: Static SOFA Score
- Compare SOFA score at stabilization (or at 24h post-stabilization) with multi-organ impairment duration
- Test if temporal duration metrics outperform static scores

### Baseline 3: Single-Point Recovery Assessment
- Compare recovery status at a fixed time point (e.g., 72h post-stabilization) with temporal trajectory metrics
- Test if continuous monitoring outperform fixed-time assessment

## Falsification Criteria

The hypothesis will be considered **falsified** if:
1. Adjusted hazard ratio for multi-organ impairment duration < 1.3 (not even a weak association)
2. No threshold effect detected (risk increases linearly or not at all with duration)
3. Multi-organ impairment duration performs no better than baseline models (SOFA at stabilization, single-organ duration) in net reclassification improvement (NRI < 5%)
4. All associations are confounded by admission severity (no independent effect after adjusting for admission SOFA)

## Analysis Plan

### Step 1: Population Definition
- Identify patients with infection/shock admissions
- Filter for ICU stays ≥ 48 hours
- Identify patients who received organ support (vasopressors, dialysis, or ventilation)
- Define circulatory stabilization event (cessation of vasopressors for ≥24 hours)

### Step 2: Recovery Trajectory Construction
- For each patient, construct time series of organ function markers post-stabilization
- Define impairment windows (≥24 hours of impaired organ function)
- Calculate duration of multi-organ impairment (hours from first to last impaired period)

### Step 3: Outcome Definition
- Primary outcome: In-hospital mortality or deterioration requiring escalation (e.g., re-intubation, RRT, ICU transfer) within 7 days post-stabilization
- Secondary outcomes: 30-day mortality, length of stay, ICU length of stay

### Step 4: Statistical Analysis
- Cox proportional hazards model with multi-organ impairment duration as time-varying covariate
- Include adjustment for: admission SOFA, age, sex, comorbidities, admission severity score
- Test for threshold effect using restricted cubic splines or piecewise Cox models
- Compare predictive performance using:
  - C-index (discrimination)
  - NRI (net reclassification improvement)
  - IDI (integration discrimination improvement)
  - Calibration plots

### Step 5: Subgroup Analysis
- Stratify by: age (<65, ≥65), comorbidity burden, admission source
- Test for effect modification

## Method Comparison

### Baseline Method: Single-Point Assessment
- **What it does**: Assesses recovery at a fixed time point or uses static scores
- **What it misses**: Temporal dynamics, threshold effects, multi-organ coordination

### Proposed Method: Temporal Duration Metrics
- **What it reveals**:
  - Specific lag in recovery for different organ systems
  - Critical threshold beyond which deterioration risk increases
  - Coordination between organ systems (multi-organ vs single-organ)
  - Rate of recovery (slope of improvement)

### Alternative Method: Machine Learning Trajectory Model
- **What it could reveal**: Non-linear patterns that linear duration metrics miss
- **Trade-off**: Less interpretability, potential for data mining

## Clinical Decision-Making Implications

If the hypothesis is supported:
1. **Extended monitoring**: Patients with multi-organ impairment duration > threshold should receive extended monitoring
2. **Escalation criteria**: Deterioration risk should be based on duration of multi-organ impairment, not just current organ scores
3. **Resource allocation**: Hospitals should have protocols for patients with prolonged multi-organ impairment
4. **Clinical trials**: Future trials should stratify by multi-organ impairment duration

## Limitations and Unresolved Questions

### Data Limitations
- MIMIC-IV has gaps in some organ function measurements
- Circulatory stabilization definition may vary by institution
- Some organ impairments may be unmeasured (e.g., neurological)

### Clinical Adjudication Required
- Optimal definition of circulatory stabilization may vary
- Critical threshold values need clinical validation
- Intervention strategies based on findings need prospective testing

### Missing Evidence
- No validated clinical tool for multi-organ impairment duration
- No prospective validation of duration-based escalation criteria
- Mechanistic understanding of why multi-organ impairment predicts deterioration

## Key References (To Be Inspected)

K1: Foy et al. 2022, Nature Communications - "Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations"
K2: Yu et al. 2024, Int J Infect Dis - Group-based multitrajectory modeling for organ dysfunction
K3: Wan et al. 2026, J Adv Res - Validation of GBMTM for clinically actionable subphenotypes

## Next Steps

1. Inspect key references (K1, K2, K3) to understand prior work
2. Explore MIMIC-IV data to verify organ function markers and availability
3. Develop pilot analysis on a subset of data
4. Refine hypothesis based on data exploration
5. Complete reference delivery with key-references.json
6. Launch computational experiment with workers
