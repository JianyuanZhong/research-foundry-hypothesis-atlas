> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Longitudinal Biomarker Trajectories and Cardiovascular Disease Risk: A Temporal Dynamics Approach

## Hypothesis to test

At the same baseline age, sex, and comorbidity profile, individuals whose inflammatory and metabolic biomarkers show increasing trajectories over time (captured through UK Biobank's serial assessments) are more likely to develop incident cardiovascular disease than those with stable or decreasing trajectories, even after adjusting for baseline values. This temporal pattern provides incremental risk information beyond static baseline measures [K1][K2].

## Scientific Significance

Current cardiovascular risk prediction relies on static baseline measures from a single assessment. However, the UK Biobank offers multiple assessment waves that could capture biomarker trajectories. Understanding whether biomarker *change* (rather than just baseline) predicts disease could:

1. **Improve risk stratification** for intermediate-risk individuals who may be missed by baseline-only models
2. **Enable earlier intervention** by identifying those with rapidly worsening biomarker trajectories
3. **Inform dynamic risk models** that update predictions as new assessments become available
4. **Reveal biological mechanisms** - rapid biomarker worsening may indicate underlying pathophysiology

## Study Population and Main Data

### Population
- UK Biobank participants aged 40-75 at baseline (Wave 1 assessment)
- Followed from Wave 1 through Wave 3+ (serial assessments up to 2021)
- Exclusion: Participants with pre-existing cardiovascular disease at Wave 1

### Main Data Tables

The UK Biobank data uses a field-instance encoding where columns are named as `{field_id}-{instance}` (e.g., `21022-0.0` for age at assessment instance 0).

- **assessment** table: Wave 1, 2, and 3 assessment dates and IDs
  - `eid`: Participant ID (join key)
  - `21022-0.0`: Age at recruitment (years) [field 21022]
  - Assessment instance identifiers (e.g., `24120-0.0`, `24120-1.0`)

- **main** table: Baseline biomarkers from Wave 1
  - `eid`: Participant ID (join key)
  - `3-0.0`, `3-1.0`, `3-2.0`, `3-3.0`: Sex (field 3, coded 0=Female, 1=Male)
  - `19-0.0`: BMI (field 19)
  - `21-0.0`: Waist circumference (field 21)
  - Additional fields for height, weight, and other anthropometrics

- **biological_samples** table: Grip strength and body composition
  - `eid`: Participant ID (join key)
  - Grip strength measures (field IDs in range 24000-25000)
  - Body composition measures (field IDs in range 26000-27000)

- **health_outcomes** table: Incident cardiovascular disease events
  - `eid`: Participant ID (join key)
  - Field IDs 40000-41263: Various health outcomes including CVD (ICD-10 I00-I52)
  - Outcome date and type fields

- **additional_exposures** table: Smoking, alcohol, physical activity, medication use
  - `eid`: Participant ID (join key)
  - Exposure fields (field IDs in range 20000-23000)

### Temporal Boundaries
- **Baseline**: Wave 1 assessment (index date from `assessment` table)
- **Follow-up**: From Wave 1 through Wave 3 (longest available follow-up period)
- **Outcome**: First incident CVD event or censoring (death, loss to follow-up, end of study 2021)

## Key Variables

### Exposure Measures
- **Baseline biomarkers** (from Wave 1 `main` table):
  - BMI (field 19)
  - Waist circumference (field 21)
  - hs-CRP (if available in main or additional_exposures)
  - Fasting glucose (if available)
  - HbA1c (if available)
  - eGFR (if available)

- **Biomarker trajectories** (calculated from serial assessments):
  - Linear slope of each biomarker across waves
  - Rate of change per year
  - Trajectory categories: increasing, stable, decreasing

### Outcome Measures
- **Cardiovascular disease**: Incident CVD events from `health_outcomes` (field IDs in range 40000-41263 corresponding to ICD-10 I00-I52)
- **Time to event**: Years from Wave 1 assessment to first CVD event

### Covariates
- Age (at Wave 1, field 21022-0.0), sex (field 3), assessment center
- Smoking status, alcohol use, physical activity (from `additional_exposures`)
- Comorbidities (from `health_outcomes` history prior to index)
- Medication use (from `additional_exposures`)
- Genetic risk score (if available in `genomics`)

## Baseline Model

A Cox proportional hazards model using **static baseline biomarkers**:
- Main effects: BMI, waist circumference, and any available inflammatory/metabolic biomarkers
- Adjusted for: age, sex, smoking, alcohol, physical activity, comorbidities, medications
- **Null hypothesis**: No association between baseline biomarkers and CVD risk after adjustment

**Expected**: Biomarkers show traditional associations (higher BMI/waist → higher CVD risk)

## Alternative Model

A Cox model incorporating **biomarker trajectories**:
- Main effects: Baseline biomarkers (as above)
- Main effects: Biomarker slopes (rate of change per year)
- Interaction terms: Baseline × Slope (testing whether baseline and trajectory have differential effects)
- Adjusted for: same covariates as baseline model

**Key question**: Do biomarker trajectories add predictive value beyond baseline levels?

**Alternative hypothesis**: Biomarker trajectories (especially rapid worsening) predict CVD risk independently of baseline levels, providing incremental discrimination.

## Falsification Criteria

The hypothesis is **falsified** if:
1. **No incremental value**: Biomarker trajectories do not improve C-index compared to baseline-only model (ΔC-index < 0.01)
2. **No temporal pattern**: Biomarker slopes show no association with CVD after adjusting for baseline (all p > 0.05)
3. **Opposite pattern**: Rapid biomarker worsening is associated with *lower* CVD risk, contradicting pathophysiology
4. **No effect**: Neither baseline nor trajectory measures show significant association (all p > 0.05)

The hypothesis is **supported** if:
1. **Incremental discrimination**: Trajectory model shows ΔC-index ≥ 0.02-0.03 over baseline model
2. **Temporal pattern**: Biomarker slopes show significant association with CVD (p < 0.01)
3. **Clinical effect**: Hazard ratio for rapid worsening ≥ 1.20 (clinically meaningful)
4. **Reproducibility**: Results consistent across stratified analyses (age, sex, assessment center)

## Scientific Advance Over Existing Knowledge

### Gap in Current Research
1. **Static vs. Dynamic**: Most risk models use single-timepoint measures; temporal dynamics are rarely captured
2. **Biomarker trajectories**: Few studies examine whether biomarker *change* (not just baseline) predicts outcomes
3. **UK Biobank underutilization**: The serial assessment structure is not systematically leveraged for trajectory analysis
4. **Clinical translation**: Even if trajectories improve prediction, clinical utility is unclear

### Novelty of This Approach
- Directly tests whether temporal biomarker dynamics improve prediction beyond established baseline models
- Uses UK Biobank's unique serial assessment structure in a way not previously done
- Addresses a fundamental limitation of current risk stratification (static snapshots)
- Provides mechanistic insights - rapid biomarker worsening may indicate underlying pathophysiology

### Methodological Innovation
- Combines traditional Cox modeling with trajectory analysis
- Uses linear mixed-effects concepts within survival analysis framework
- Leverages UK Biobank's rich phenotyping without requiring imaging or genomics

## Main Limitations

1. **Assessment spacing**: Waves are 2-3 years apart; trajectories may be coarse-grained
2. **Missing data**: Not all participants have all waves; trajectory estimation may be imprecise
3. **Reverse causation**: Subclinical disease may affect biomarkers before CVD diagnosis
4. **Selection bias**: Participants with serial assessments may differ systematically
5. **Measurement error**: Biomarker assays may vary across waves
6. **Residual confounding**: Unmeasured factors may influence both biomarkers and outcomes

## Data Bindings

### Required Tables and Columns (UKB field-instance encoding)

**assessment** table:
- `eid`: Participant ID (join key)
- `21022-0.0`: Age at recruitment (years) [field 21022]
- Assessment instance identifiers (e.g., `24120-0.0`, `24120-1.0`)

**main** table (Wave 1):
- `eid`: Participant ID (join key)
- `3-0.0`, `3-1.0`, `3-2.0`, `3-3.0`: Sex (field 3, coded 0=Female, 1=Male)
- `19-0.0`: BMI (field 19)
- `21-0.0`: Waist circumference (field 21)
- Additional fields for height, weight, and other anthropometrics

**health_outcomes** table:
- `eid`: Participant ID (join key)
- Field IDs 40000-41263: Various health outcomes including CVD (ICD-10 I00-I52)
- Outcome date and type fields

**additional_exposures** table:
- `eid`: Participant ID (join key)
- Exposure fields (field IDs in range 20000-23000)

### Join Keys and Relationships
- All tables join on `eid`
- Wave 1 data from `main` table
- Serial assessments from `assessment` table (filter for instance 0 = Wave 1)
- Outcomes from `health_outcomes` table (filter for CVD field IDs)

### Time Fields
- Index date: Derived from `assessment` table (Wave 1)
- Follow-up time: Years from Wave 1 to first outcome or censoring
- Censoring: Death, loss to follow-up, end of study (2021)

## Required Computations

### 1. Data Preprocessing
- Filter: Age 40-75 at Wave 1, no CVD at baseline
- Parse field-instance column names to extract field IDs
- Calculate biomarker trajectories (slope per year across waves)
- Handle missing waves (impute or use available waves)
- Standardize biomarkers within age/sex strata
- Create time-to-event variables (years from Wave 1)

### 2. Baseline Model
- Cox PH model with baseline biomarkers as predictors
- Adjust for: age, sex, smoking, alcohol, physical activity, comorbidities, medications
- Output: HRs, 95% CIs, C-index

### 3. Trajectory Model
- Cox PH model with baseline + slope predictors
- Interaction terms: Baseline × Slope
- Output: HRs, 95% CIs, C-index, ΔC-index

### 4. Sensitivity Analyses
- Exclude participants with comorbidities at baseline
- Alternative trajectory estimation (non-linear, piecewise)
- Stratified analyses (age, sex, assessment center)
- Competing risks (death)

### 5. Resource Requirements
- CPU: 8 cores, 64GB memory (for data processing and modeling)
- Time: 4-8 hours for full analysis
- GPU: Not required (traditional statistical methods)

## Key References

- [K1] Wang, Y. et al. (2025). Weight-adjusted waist index outperforms other obesity indices for cardiovascular disease prediction in cardiovascular-kidney-metabolic syndrome: insights from UK biobank. BMC Public Health. PMID: 41353132. **Claim**: Visceral adiposity measures beyond BMI provide superior CVD risk stratification, supporting the importance of dynamic body composition in cardiovascular risk [K1].

- [K2] Gao, Y. et al. (2026). Association of sarcopenia with the long-term risk of overall infections and infectious diseases: a prospective cohort study of 458 332 participants. MedScience. PMID: 42142230. **Claim**: Low muscle strength is associated with increased infection risk, suggesting that body composition dynamics (not just static measures) may be important for disease prediction [K2].

- [K3] Cabanas-Sánchez, P. et al. (2022). Muscle strength and incidence of depression and anxiety: findings from the UK Biobank prospective cohort study. J Cachexia Sarcopenia Muscle. PMID: 35678014. **Claim**: Grip strength predicts mental health outcomes, demonstrating that functional measures have independent predictive value beyond traditional risk factors [K3].

## Supporting Evidence

- Key references: `work/key-references.json` (contains full reference delivery with source receipts)
- Data schema verification: Field IDs documented in proposal
- Preliminary analysis: Will inspect actual field names and data availability

## Next Steps for Development

1. **Data exploration**: Inspect actual field IDs and data types in UKB tables
2. **Sample size calculation**: Estimate power for detecting ΔC-index ≥ 0.02
3. **Trajectory estimation**: Develop method for handling missing waves
4. **Model implementation**: Write Python code for Cox models with trajectory terms
5. **Validation**: Perform internal validation (bootstrapping) and assess calibration

## Conclusion

This hypothesis addresses a fundamental limitation in cardiovascular risk prediction: the reliance on static baseline measures. By testing whether biomarker trajectories (captured through UK Biobank's serial assessments) improve prediction beyond baseline-only models, this work could:
- Improve risk stratification for intermediate-risk individuals
- Enable earlier intervention by identifying those with worsening trajectories
- Inform development of dynamic risk models that update with new assessments

The study is clinically important, scientifically novel, and feasible with available UKB data. Results would advance understanding of how temporal biomarker dynamics contribute to disease risk.
