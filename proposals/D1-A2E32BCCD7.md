> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Scientific Proposal: Vasopressor Timing Predicts Mortality Beyond Hypotension Duration

## 1. Unresolved Question and Clinical Importance

### The Core Question
While prior work has established that **duration of hypotension** predicts acute kidney injury (AKI) [K1], [K2], a critical unresolved question remains: **Does the TIMING of vasopressor initiation relative to hypotension onset independently predict mortality, beyond what hypotension duration and minimum blood pressure explain?**

This is not merely an incremental addition of another covariate. The timing dimension captures a fundamentally different clinical process:
- **Duration-based measures** reflect the total burden of hypotension exposure
- **Timing-based measures** reflect the speed of clinical recognition and intervention

### Why This Matters Clinically

1. **Quality of Care Signal**: Early vasopressor initiation may indicate earlier recognition of hemodynamic instability, potentially reflecting better team coordination, monitoring, or clinical expertise.

2. **Treatment Effect Modification**: The relationship between hypotension and mortality may be modified by how quickly treatment is initiated. Delayed initiation could represent:
   - Diagnostic uncertainty ("is this hypotension or shock?")
   - Resource constraints (vasopressor availability)
   - Clinical hesitation (fear of complications)

3. **Risk Stratification**: A timing-based risk score could complement duration-based scores to improve mortality prediction, potentially identifying high-risk patients who need more aggressive monitoring or earlier intervention.

### The Gap in Existing Work

Existing studies (e.g., [K1], [K2]) have focused on:
- Duration below MAP thresholds
- Minimum blood pressure achieved
- Cumulative vasopressor exposure

But none have systematically tested whether **initiation timing** (time from hypotension onset to first vasopressor dose) provides independent prognostic information beyond duration and minimum pressure.

## 2. Primary Hypothesis

**In critically ill patients with vasopressor-dependent hypotension, the time interval from hypotension onset to first vasopressor administration predicts 28-day mortality independently of hypotension duration, minimum mean arterial pressure, baseline severity (APACHE II), age, and hospital characteristics.**

### Primary Hypothesis (Testable Claim)
At a fixed hypotension duration (e.g., 2 hours) and fixed minimum MAP (e.g., 60 mmHg), patients who receive vasopressors **earlier** (shorter time from hypotension onset to first dose) have **lower** 28-day mortality.

### Secondary Hypotheses
1. The association between vasopressor initiation timing and mortality is modified by:
   - Baseline severity (APACHE II score)
   - Hospital teaching status
   - Patient age

2. The predictive value of initiation timing is attenuated when controlling for hypotension duration and minimum MAP.

## 3. Study Population

### Inclusion Criteria
- Adult patients (age ≥ 18)
- ICU stay duration ≥ 48 hours
- At least 24 hours of continuous blood pressure monitoring (vitalAperiodic with noninvasivemean > 0)
- Received at least one vasopressor during ICU stay (infusionDrug with drugname in vasoactive class)
- Minimum MAP ≥ 50 mmHg during study period

### Exclusion Criteria
- Patients who received vasopressors before ICU admission (from admissionDrug)
- Patients with < 12 hours of continuous vital sign monitoring
- Patients who died within 6 hours of ICU admission (insufficient observation window)

### Population Size Estimate
Based on eICU-CDR v2.0:
- ~15,000 ICU admissions annually
- ~5-10% receive vasopressors: ~750-1,500 patients
- After exclusions: ~500-800 patients eligible for analysis

## 4. Data Bindings

### Primary Tables

#### 4.1 vitalAperiodic (table-72ace5b89971196b.json)
**Purpose**: Identify hypotension onset and calculate duration

**Columns Used**:
- `patientunitstayid`: Primary key, joins all tables
- `observationoffset`: Temporal column (minutes from ICU admission)
- `noninvasivemean`: Mean arterial pressure in mmHg
- `noninvasivesystolic`, `noninvasivediastolic`: For MAP calculation if needed

**Query Logic**:
```sql
-- Identify hypotension episodes (MAP < 60 mmHg)
SELECT patientunitstayid,
       MIN(observationoffset) as hypotension_onset,
       MAX(observationoffset) as hypotension_end
FROM vitalAperiodic
WHERE noninvasivemean < 60
GROUP BY patientunitstayid
```

#### 4.2 infusionDrug (table-18e1a8caaa91eb44.json)
**Purpose**: Identify vasopressor initiation timing

**Columns Used**:
- `patientunitstayid`: Primary key, joins all tables
- `infusionoffset`: Temporal column (minutes from ICU admission)
- `drugname`: Filter for vasopressors

**Vasopressor Drug Names** (from medical knowledge, to be validated):
- Norepinephrine, Dopamine, Epinephrine, Phenylephrine, Vasopressin, Angiotensin II
- Potentially: Dobutamine (inotropes, but often grouped with vasoactive drugs)

**Query Logic**:
```sql
-- Find first vasopressor administration
SELECT patientunitstayid,
       MIN(infusionoffset) as first_vasopressor_time
FROM infusionDrug
WHERE drugname IN ('norepinephrine', 'dopamine', 'epinephrine', 'phenylephrine', 'vasopressin')
GROUP BY patientunitstayid
```

#### 4.3 apacheApsVar (table-67711a86e012835e.json)
**Purpose**: Baseline severity and clinical covariates

**Columns Used**:
- `patientunitstayid`: Primary key
- `meanbp`: Mean blood pressure at assessment
- `creatinine`, `bun`, `glucose`: Renal function and metabolic status
- `heartrate`: Cardiac status
- `temperature`: Thermoregulation
- `sodium`: Electrolyte status
- `wbc`: Infection risk

**Note**: This table is cross-sectional (no temporal columns), so use values closest to admission or as baseline.

#### 4.4 apachePatientResult (table-754bebf64d3d9909.json)
**Purpose**: APACHE II severity score

**Columns Used**:
- `patientunitstayid`: Primary key
- `apachescore`: APACHE II score
- `actualicumortality`: Observed in-hospital mortality (for validation)

#### 4.5 patient (table-ab037c09d7df9a3c.json)
**Purpose**: Demographics

**Columns Used**:
- `patientunitstayid`, `uniquepid`: Primary keys
- `age`: Age at admission
- `gender`: Sex
- `ethnicity`: Demographic stratification
- `hospitalid`: Hospital-level clustering

#### 4.6 hospital (table-811df7b2ef435e12.json)
**Purpose**: Hospital-level confounders

**Columns Used**:
- `hospitalid`: Primary key
- `teachingstatus`: Teaching vs. non-teaching hospital
- `region`: Geographic region

#### 4.7 lab (table-79bdb33275339b1a.json)
**Purpose**: Additional renal function measures

**Columns Used**:
- `patientunitstayid`: Primary key
- `labresultoffset`: Temporal column
- `labname`: Filter for creatinine-based tests
- `labresult`: Creatinine value

**Note**: May need to join with lab dictionary to map labname to creatinine

### Join Logic

```sql
-- Complete join specification
SELECT
    p.patientunitstayid,
    p.uniquepid,
    p.age,
    p.gender,
    h.hospitalid,
    h.teachingstatus,
    h.region,
    a.apachescore,
    v.hypotension_onset,
    v.hypotension_end,
    v.duration_hours,
    v.min_map,
    i.first_vasopressor_time,
    i.time_to_vasopressor,
    a2.actualicumortality,
    CASE
        WHEN a2.actualicumortality = 1 THEN 1
        ELSE 0
    END as mortality_28d
FROM patient p
JOIN hospital h ON p.hospitalid = h.hospitalid
JOIN apachePatientResult a ON p.patientunitstayid = a.patientunitstayid
LEFT JOIN vitalAperiodic v ON p.patientunitstayid = v.patientunitstayid
    AND v.observationoffset BETWEEN p.hospitaladmitoffset AND p.hospitaldischargeoffset
LEFT JOIN infusionDrug i ON p.patientunitstayid = i.patientunitstayid
    AND i.infusionoffset BETWEEN p.hospitaladmitoffset AND p.hospitaldischargeoffset
WHERE ... -- inclusion criteria
```

## 5. Primary Outcome

### 28-Day Mortality
- **Definition**: Death within 28 days of ICU admission
- **Source**: apachePatientResult.actualicumortality (if available) OR patient.hospitaldischargestatus
- **Limitation**: May be incomplete if discharge status unknown; consider 30-day mortality from external sources if needed

### Alternative Outcomes (if primary unavailable)
- In-hospital mortality (apachePatientResult.actualicumortality)
- ICU mortality
- Length of stay > 7 days

## 6. Exposure Variables

### Primary Exposure: Time to Vasopressor
- **Definition**: Minutes from hypotension onset to first vasopressor administration
- **Distribution**: Will likely be right-skewed; consider log transformation or categorical groups
- **Categories**:
  - ≤ 30 minutes (very early)
  - 31-60 minutes (early)
  - 61-120 minutes (intermediate)
  - > 120 minutes (delayed)

### Secondary Exposures
- **Hypotension Duration**: Hours below MAP threshold
- **Minimum MAP**: Lowest mean arterial pressure achieved
- **Cumulative Vasopressor Dose**: Total volume/rate over time

## 7. Covariates

### Demographic
- Age (continuous)
- Gender (male/female)
- Ethnicity (stratify if sample size permits)

### Clinical Severity
- APACHE II score
- SAPS III (if available in apachePatientResult)
- SOFA score (if calculable from apacheApsVar)

### Hospital Characteristics
- Teaching status
- Region
- ICU type (if available)

### Physiological
- Baseline creatinine (from apacheApsVar or lab)
- Baseline glucose
- Baseline sodium
- Baseline hematocrit

### Treatment
- Concurrent medications (from infusionDrug or medication tables)
- Mechanical ventilation status
- Dialysis status

## 8. Statistical Analysis Plan

### Primary Analysis: Cox Proportional Hazards

```python
# Pseudocode for Cox model
import statsmodels.api as sm

# Model 1: Time to vasopressor as primary predictor
cox_model = CoxPHModel(
    event_time='time_to_mortality',
    event='mortality_28d',
    covariates=[
        'time_to_vasopressor',
        'hypotension_duration',
        'min_map',
        'apachescore',
        'age',
        'gender',
        'teachingstatus',
        'region'
    ]
).fit()
```

### Secondary Analyses

1. **Stratified Analysis by Baseline Severity**
   - Separate models for APACHE II ≤ 15, 16-25, ≥ 26
   - Test for interaction between time_to_vasopressor and severity

2. **Stratified Analysis by Hospital Type**
   - Teaching vs. non-teaching hospitals
   - Test for interaction

3. **Sensitivity Analysis: Alternative MAP Thresholds**
   - Repeat analysis with MAP thresholds of 55, 65, 70 mmHg
   - Assess robustness

4. **Alternative Exposure: Duration Below Higher Threshold**
   - Duration below MAP 70 mmHg (vs. 60 mmHg)
   - Test for consistency

5. **Time-Varying Exposure Analysis**
   - Treat vasopressor initiation as time-dependent covariate
   - Assess if effect modifies over time

### Model Diagnostics
- Proportional hazards assumption (Schoenfeld residuals)
- Collinearity (VIF)
- Missing data patterns
- Distribution of key variables

## 9. Falsification Criteria

The hypothesis will be **falsified** if:
1. Time to vasopressor initiation shows **no association** with mortality after adjusting for duration and minimum MAP (p > 0.05)
2. Time to vasopressor shows an **inverse association** (later initiation = lower mortality)
3. The association is **entirely explained** by duration or minimum MAP (no independent effect)

The hypothesis will be **supported** if:
1. Time to vasopressor shows an **independent inverse association** with mortality (early initiation = lower mortality)
2. The association persists after adjusting for duration, minimum MAP, and all covariates
3. The effect size is clinically meaningful (e.g., HR < 0.8 for early vs. delayed)

## 10. Baseline and Alternative Methods

### Baseline Method: Univariate and Bivariate Analysis
- Compare mortality rates by time to vasopressor category (chi-square test)
- Calculate crude hazard ratios

### Alternative Method 1: Logistic Regression (for binary outcomes)
- Model 28-day mortality as binary outcome
- Compare coefficients for time to vasopressor

### Alternative Method 2: Machine Learning (Random Forest)
- Build model predicting mortality
- Compare feature importance of time to vasopressor vs. duration vs. minimum MAP
- **Scientific Value**: Can reveal non-linear relationships and interactions that linear models miss

### Alternative Method 3: Dynamic Risk Prediction
- Build time-varying risk model that updates as new data arrives
- Assess whether early vasopressor initiation changes predicted risk trajectory

### Method Selection Reasoning
- **Cox regression** is primary because it handles time-to-event data appropriately
- **Machine learning** serves as alternative to check for non-linear effects
- **Dynamic prediction** tests whether the timing effect is truly temporal or static

## 11. Clinical Significance

### If Supported
1. **Quality Improvement**: Hospitals could identify teams that delay vasopressor initiation and provide targeted training
2. **Risk Stratification**: Add timing-based component to existing hypotension risk scores
3. **Clinical Decision Support**: Alert clinicians when vasopressor initiation is delayed
4. **Research Directions**: Investigate whether early initiation improves outcomes (RCTs)

### If Not Supported
1. **Focus Shift**: Emphasize duration and minimum pressure measures instead
2. **Mechanism Inquiry**: Explore why timing doesn't matter (e.g., vasopressors may not be the primary driver of outcomes)
3. **Data Limitations**: Acknowledge that timing data may be unreliable in EHR

## 12. Limitations and Unresolved Questions

### Data Limitations
1. **Incomplete Vasopressor Data**: EHR may not capture all vasoactive medications
2. **Timing Accuracy**: "First dose" may be recorded as order time, not administration time
3. **Missing Outcomes**: apachePatientResult.actualicumortality may be incomplete
4. **No External Validation**: Results limited to single dataset

### Clinical Unresolved Questions
1. **Causality**: Does early initiation cause better outcomes, or do sicker patients get delayed treatment?
2. **Optimal Threshold**: What is the "safe" upper limit for time to vasopressor?
3. **Drug-Specific Effects**: Does the effect vary by vasopressor type?
4. **Patient-Specific Effects**: Does the optimal timing depend on patient characteristics?

## 13. Required Key References

### K1: Hypotension Duration and AKI
- Paper demonstrating duration-based hypotension predicts AKI
- Establishes the importance of temporal dynamics in hemodynamic monitoring

### K2: Minimum Blood Pressure vs. Duration
- Paper comparing static vs. dynamic measures
- Provides context for the duration vs. timing question

### K3: Vasopressor Use in Critical Care
- Review or study on vasopressor initiation timing
- Provides baseline understanding of current practice

## 14. Implementation Plan

### Phase 1: Data Exploration (Week 1)
- Validate vasopressor drug names in infusionDrug table
- Assess hypotension event rates
- Check availability of outcome data
- Explore distributions of time to vasopressor

### Phase 2: Primary Analysis (Week 2-3)
- Build Cox model with time to vasopressor as primary predictor
- Test proportional hazards assumption
- Assess effect size and precision

### Phase 3: Secondary Analyses (Week 4)
- Stratified analyses
- Sensitivity analyses
- Machine learning comparison

### Phase 4: Interpretation and Reporting (Week 5)
- Clinical interpretation
- Limitations
- Recommendations

---

This proposal addresses a critical gap in understanding the relationship between hemodynamic instability and mortality. By testing whether the **timing of intervention** provides independent prognostic information beyond **duration and intensity** measures, this study could inform quality improvement initiatives and potentially guide clinical decision support systems.
