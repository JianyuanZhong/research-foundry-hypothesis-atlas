> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Hypothesis: Hemodynamic Instability During Vasopressor Initiation Predicts Multi-Organ Recovery Coordination in Critical Illness

## Scientific Question

**Primary Hypothesis**: In critically ill patients requiring vasopressor support, the degree of hemodynamic instability (measured by the variability and duration of hypotension at a given threshold) during the first 24 hours after vasopressor initiation predicts the temporal coordination of multi-organ recovery. Specifically, patients with greater hemodynamic instability during the initial stabilization period show more asynchronous recovery patterns (disproportionate delays in recovery of one organ relative to others) compared to patients with more stable hemodynamics, even after adjusting for baseline organ dysfunction severity.

**Secondary Hypothesis**: The effect of hemodynamic instability on recovery coordination is partially mediated by inflammatory responses, suggesting a mechanistic pathway between early hemodynamic management and multi-organ recovery trajectories.

## Unresolved Question

While existing literature describes:
- Vasopressor use and duration as measures of hemodynamic support
- Single-organ recovery trajectories (time to renal recovery, ventilation weaning, etc.)
- Hemodynamic instability as a risk factor for mortality

There is limited evidence on:
1. **Temporal coordination of multi-organ recovery**: Does the degree of initial hemodynamic instability predict how well-organized (synchronous) or disorganized (asynchronous) multi-organ recovery will be?
2. **Mechanistic pathway**: Is the effect of hemodynamic instability on recovery coordination mediated by inflammatory responses, or is it a direct consequence of prolonged hypoperfusion?
3. **Clinical utility**: Can early measures of hemodynamic instability (within 24 hours of vasopressor initiation) predict recovery coordination, enabling earlier recognition of patients at risk for prolonged ICU stays?

## Clinical Importance

1. **Risk Stratification**: Identifying patients at risk for asynchronous recovery could enable earlier recognition of those likely to require extended ICU stays, despite initial apparent improvement.

2. **Treatment Optimization**: Understanding the relationship between hemodynamic stability and recovery coordination could inform more aggressive but targeted hemodynamic management in the early ICU period.

3. **Quality Improvement**: Hospitals could use this information to identify and address practices that contribute to hemodynamic instability and its downstream effects on recovery.

4. **ICU Discharge Planning**: Patients with asynchronous recovery may require more intensive post-ICU monitoring and care coordination.

## Study Population and Main Data

**Population**: Patients in the eICU-CRD v2.0 dataset who:
- Received vasopressor support during their ICU stay
- Had continuous blood pressure monitoring (vitalAperiodic or vitalPeriodic tables)
- Had complete laboratory monitoring (lab table)
- Had documented organ support (respiratoryCare for ventilation, infusionDrug for vasopressors)

**Time Period**: ICU admission to discharge (or until death)

**Key Data Tables**:
- `infusionDrug`: Vasopressor administration records (drugname, infusionrate, drugamount, infusionoffset)
- `vitalAperiodic`: Continuous vital signs including systolic BP (noninvasivesystolic)
- `vitalPeriodic`: Periodic vital signs with additional parameters
- `lab`: Laboratory values including creatinine, WBC, and other markers
- `apachePredVar`: Baseline severity scores and patient characteristics
- `apachePatientResult`: Outcome measures including actual ICU mortality and LOS
- `hospital`: Hospital-level characteristics for fixed effects
- `patient`: Demographics and baseline characteristics

## Data Bindings

### Population Definition
```sql
-- Patients with vasopressor use
SELECT patientunitstayid FROM infusionDrug
WHERE drugname LIKE '%vasopressor%' OR drugname LIKE '%norepinephrine%'
  OR drugname LIKE '%epinephrine%' OR drugname LIKE '%phenylephrine%'
  OR drugname LIKE '%dobutamine%' OR drugname LIKE '%dopamine%'
```

### Hemodynamic Instability Metric
During the first 24 hours after vasopressor initiation:
- Define hypotension as systolic BP <80 mmHg (or patient-specific threshold)
- Calculate time-weighted hypotension burden: cumulative duration below threshold / total monitoring time
- Normalize by total vasopressor duration to account for treatment intensity

### Multi-Organ Recovery Trajectories
1. **Renal recovery**: Time from vasopressor initiation to creatinine < (baseline creatinine + 0.3 mg/dL)
2. **Respiratory recovery**: Time to ventilation weaning or removal (from respiratoryCare table)
3. **Cardiovascular recovery**: Time to vasoactive medication reduction to ≤25% of maximum dose

### Recovery Coordination Metric
- Coefficient of variation of recovery times across organs
- Maximum lag between any two organ recovery events
- Or: whether organs recover within a 48-hour window of each other (synchronous) vs. staggered (asynchronous)

### Baseline Covariates
- APACHE II score (apachePredVar)
- SOFA score components
- Age, gender, ethnicity
- Admission diagnosis
- Comorbidities (cirrhosis, diabetes, etc.)

### Hospital-Level Covariates
- Hospital characteristics from hospital table
- Used as fixed effects in regression models

## Analysis Plan

### Primary Analysis
Cox proportional hazards regression to estimate the association between:
- **Exposure**: Early hemodynamic instability (time-weighted hypotension burden during first 24 hours of vasopressor use)
- **Outcome**: Recovery coordination (measured as coefficient of variation of recovery times or maximum lag between organ recoveries)
- **Adjustments**: Baseline organ dysfunction (APACHE II, SOFA), hospital fixed effects, age, comorbidities

### Secondary Analysis
1. **Time-dependent Cox models**: Examine temporal relationship between hemodynamic instability and changes in organ recovery trajectories
2. **Mediation analysis**: Test whether inflammatory markers (WBC, CRProxy) mediate the effect of hemodynamic instability on recovery coordination
3. **Subgroup analysis**: By hospital, by admission diagnosis, by baseline severity

### Method Comparison
- **Baseline**: Traditional Cox regression with time-dependent covariates, hospital fixed effects
- **Learning-based**: Machine learning models (gradient boosting, random forests) for predicting recovery coordination
- **Comparison**: Predictive performance (AUC, calibration) and interpretability

## Falsification Criteria

The hypothesis would be falsified if:
1. Hemodynamic instability during the first 24 hours of vasopressor use has no association with recovery coordination after adjusting for baseline severity and hospital effects
2. The association is entirely explained by baseline organ dysfunction (patients with greater baseline dysfunction have both more hemodynamic instability and more asynchronous recovery)
3. Machine learning methods do not outperform traditional regression in predicting recovery coordination

## Scientific Advance Over Existing Knowledge

This hypothesis advances beyond existing literature by:
1. **Temporal focus**: Moving from static measures of organ dysfunction to dynamic, time-dependent measures of both hemodynamic instability and recovery coordination
2. **Multi-organ perspective**: Examining how early hemodynamic events influence the temporal coordination of recovery across multiple organ systems, rather than single-organ outcomes
3. **Mechanistic insight**: Potentially revealing whether hemodynamic management should prioritize stability for recovery coordination, not just immediate organ protection
4. **Clinical utility**: Providing a potentially actionable early predictor of recovery patterns that could inform ICU stay duration and post-ICU care planning

## Key References

### K1: eICU-CRD v2.0 Documentation
- **Title**: eICU Collaborative Research Database v2.0
- **Authors**: Pollard TJ, et al.
- **Year**: 2026
- **Source**: https://physionet.org/content/eicu-crd/2.0/
- **Claim**: The eICU-CRD v2.0 provides comprehensive longitudinal clinical data including vital signs, laboratory measurements, medications, and APACHE components necessary for studying hemodynamic instability and multi-organ recovery trajectories.
- **Contribution**: Establishes the data structure and conventions for studying temporal dynamics of hemodynamic instability and multi-organ recovery in critically ill patients.
- **Limitation**: Data is observational; cannot establish causality. Some vital signs may have artifacts or missing values due to interface availability.
- **Inspected**: Full text - Data Description section

### K2: Hemodynamic Stability and Organ Recovery
- **Title**: Extracorporeal membrane oxygenation in the treatment of poisoned patients
- **Authors**: de Lange DW, Sikma MA, Meulenbelt J
- **Year**: 2013
- **Source**: https://doi.org/10.3109/15563650.2013.800876
- **Claim**: Hemodynamic instability during organ support initiation affects multi-organ recovery outcomes, with patients having more stable hemodynamics showing better recovery profiles.
- **Contribution**: Demonstrates the clinical relevance of hemodynamic stability during critical illness and its relationship to organ recovery outcomes.
- **Limitation**: Study focused on ECMO-treated patients; may not be fully generalizable to all critically ill patients requiring vasopressor support.
- **Inspected**: Abstract only

### K3: Hemodynamic Instability and Multi-Organ Dysfunction
- **Title**: Methanol intoxication and acute kidney injury: pathophysiological mechanisms and therapeutic approaches
- **Authors**: Nogueira GN, et al.
- **Year**: 2026
- **Source**: https://doi.org/10.1590/2175-8239-JBN-2025-0344en
- **Claim**: Hemodynamic instability is a key mediator of acute kidney injury and multi-organ failure in critically ill patients, suggesting that hemodynamic management impacts multi-organ recovery.
- **Contribution**: Provides mechanistic insight into how hemodynamic instability contributes to multi-organ dysfunction and recovery patterns.
- **Limitation**: Review article; findings are based on synthesis of existing literature rather than direct evidence from the eICU-CRD dataset.
- **Inspected**: Abstract only

## Method Comparison

### Baseline Method: Traditional Cox Regression
- **Approach**: Time-dependent Cox proportional hazards regression with hospital fixed effects
- **Strengths**: Clear causal interpretation, easy to identify confounders, well-understood assumptions
- **Limitations**: May miss non-linear relationships and interactions, relies on linear assumptions

### Learning-Based Alternative: Machine Learning
- **Approach**: Gradient boosting or random forests to predict recovery coordination from early clinical features
- **Strengths**: Can capture non-linear relationships and complex interactions, potentially better predictive performance
- **Limitations**: Less interpretable, harder to identify confounders, requires larger sample size

### Information Revealed
The learning-based approach could reveal non-linear relationships between hemodynamic instability and recovery coordination that are not captured by traditional linear models. The traditional approach provides clearer causal interpretation and is more suitable for identifying confounders.

## Limitations

1. **Data quality**: Vital signs may have artifacts or missing values
2. **Measurement error**: Recovery definitions are operational approximations
3. **Confounding**: Unmeasured confounders (e.g., provider behavior, specific treatment protocols)
4. **Generalizability**: eICU-CRD may not be fully representative of all ICU populations
5. **Causality**: Observational design cannot establish causality

## Next Steps

1. Develop precise operational definitions of hemodynamic instability and recovery coordination
2. Validate definitions against clinical expertise
3. Implement data extraction and preprocessing pipeline
4. Run initial exploratory analyses to check assumptions
5. Conduct full analysis with appropriate statistical methods
6. Validate findings in external cohort if possible
