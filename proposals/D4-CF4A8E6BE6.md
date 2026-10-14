> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Metabolic Deterioration Rate and Multimorbidity Risk in the UK Biobank

**Episode:** 10
**Dataset:** UK Biobank (ukb672073)
**Expert Seed:** [starting question]
**Status:** Proposal ready for computational development

---

## Hypothesis to Test

**Primary Question:** Among UK Biobank participants aged 40-70 at baseline assessment center visit, does the *rate of change* (deterioration) in metabolic measures over serial assessments provide independent information about incident cardiovascular and kidney multimorbidity beyond their baseline levels? [K3]

**Specific Prediction:** Participants who show increasing deterioration in metabolic measures (e.g., worsening metabolic syndrome components, rising blood pressure, increasing glucose, worsening lipid profiles) between baseline and second assessment have higher risk of developing incident cardiovascular disease, chronic kidney disease, or multimorbidity (both conditions) within 10 years, compared to those with stable or improving metabolic profiles, even after adjusting for baseline metabolic levels and demographic confounders.

---

## Scientific Significance

Current multimorbidity risk prediction relies on static baseline measures from a single assessment center visit. However, the UK Biobank offers serial assessments (baseline and second wave ~5 years apart) that could capture metabolic trajectories. Understanding whether the *rate of change* in metabolic health (rather than just baseline status) predicts disease could:

1. **Improve risk stratification** for intermediate-risk individuals who may be missed by baseline-only models
2. **Enable earlier intervention** by identifying those with rapidly deteriorating metabolic profiles
3. **Inform dynamic risk models** that update predictions as new assessment data becomes available
4. **Distinguish between static risk factors and dynamic deterioration** - the latter may represent more modifiable pathways to disease

This question addresses a fundamental limitation in current risk models that treat individuals with similar baseline risk as equivalent, ignoring that some may be on a trajectory toward worse outcomes.

**Supporting Evidence:** Recent research demonstrates that rapid progression of cardiovascular-kidney-metabolic (CKM) syndrome independently predicts accelerated frailty worsening, supporting the concept that dynamic progression of metabolic conditions carries prognostic information beyond baseline staging [K1]. Similarly, the PREVENT equations demonstrate that incorporating CKM factors (including eGFR, hemoglobin A1c) improves cardiovascular risk prediction, highlighting the importance of integrating kidney function into metabolic risk assessment [K2]. Furthermore, global studies show that risk factor trajectories (modification of hypertension and smoking in midlife) are associated with significant additional life-years free of cardiovascular disease, suggesting that dynamic changes in risk factors carry prognostic information beyond baseline status [K3].

---

## Study Population and Main Data

### Population
- **UK Biobank participants** aged 40-70 years at baseline (assessment center visit)
- **Inclusion criteria:**
  - Completed both baseline and second assessment waves
  - Have at least one metabolic measure at baseline and one at second wave
  - No incident multimorbidity outcome within first 2 years (to avoid reverse causation)
- **Exclusion criteria:**
  - Missing key metabolic measures at either timepoint
  - Missing age, sex, or assessment center ID
  - Known multimorbidity diagnosis at baseline

### Main Data Tables

1. **population** (`table-38565c9e35e7cb6c.json`)
   - `eid`: Participant ID (join key)
   - `age_at_assessment`: Age at baseline assessment
   - `sex`: Sex (0=Female, 1=Male)
   - `assessment_center_id`: Assessment center identifier

2. **main** (`table-e4a9e4d8baa71a9d.json`)
   - `eid`: Participant ID (join key)
   - `height_m`: Height in meters
   - `weight_kg`: Weight in kilograms
   - `bmi`: BMI (kg/m²)
   - `blood_pressure_systolic`: Systolic blood pressure (mmHg)
   - `blood_pressure_diastolic`: Diastolic blood pressure (mmHg)
   - `diabetes_status`: Diabetes diagnosis (0=No, 1=Yes)
   - `assessment_wave`: Assessment wave (1=baseline, 2=second wave)

3. **biological_samples** (`table-c6b666d905f3b02f.json`)
   - `eid`: Participant ID (join key)
   - `27982-1.0`: Creatinine (mg/dL) at baseline
   - `27983-1.0`: Cystatin C (mg/L) at baseline
   - `27982-2.0`: Creatinine (mg/dL) at second wave
   - `27983-2.0`: Cystatin C (mg/L) at second wave
   - `27980-1.0`: Grip strength (kg) at baseline
   - `27980-2.0`: Grip strength (kg) at second wave

4. **health_outcomes** (`table-3cfae45e0905b0e3.json`)
   - `eid`: Participant ID (join key)
   - `28000-0.0`: Incident cardiovascular disease (1=Yes, 0=No)
   - `28000-1.0`: Incident cardiovascular disease (1=Yes, 0=No) with diagnosis code
   - `28001-0.0`: Incident chronic kidney disease (1=Yes, 0=No)
   - `28001-1.0`: Incident chronic kidney disease (1=Yes, 0=No) with diagnosis code
   - `28002-0.0`: Incident multimorbidity (both CVD and CKD) (1=Yes, 0=No)
   - `28003-0.0`: Incident multimorbidity (both CVD and CKD) (1=Yes, 0=No) with diagnosis code
   - `28005-0.0`: Time to incident outcome (years from baseline)
   - `28005-1.0`: Time to incident outcome (years from baseline) with censoring indicator
   - `28005-2.0`: Time to incident outcome (years from baseline) with censoring indicator
   - `28005-3.0`: Time to incident outcome (years from baseline) with censoring indicator

---

## Scientific Approach

### Baseline Model
A stratified Cox proportional hazards model with baseline metabolic levels as main effects:
- **Exposures:** Baseline BMI tertile, baseline systolic BP tertile, baseline creatinine eGFR category, baseline diabetes status
- **Covariates:** Age, sex, assessment center, smoking status, alcohol use
- **Outcome:** Time to incident multimorbidity (CVD + CKD)
- **Primary effect measure:** Hazard ratios (HR) for each exposure category

### Alternative Model
An extended Cox model incorporating metabolic deterioration rate:
- **Exposures:**
  - Change in BMI (second wave - baseline)
  - Change in systolic BP (second wave - baseline)
  - Change in creatinine eGFR (second wave - baseline)
  - Change in diabetes status (0→1 indicates new diagnosis)
  - **Deterioration rate** (composite score of worsening metabolic measures)
- **Interactions:** Baseline metabolic level × Change in metabolic measure
- **Covariates:** Same as baseline model
- **Primary effect measure:** HR for deterioration rate categories and interaction terms

### Deterioration Rate Definition
A composite deterioration score will be created based on:
1. **BMI change:** Weight gain ≥5% or BMI increase ≥2 kg/m²
2. **Blood pressure change:** Systolic BP increase ≥10 mmHg or diastolic BP increase ≥5 mmHg
3. **Kidney function change:** eGFR decline ≥30% or creatinine increase ≥0.3 mg/dL
4. **New diabetes diagnosis:** 0→1 transition

Participants will be categorized into:
- **Stable:** No deterioration in any measure
- **Mild deterioration:** 1-2 measures worsening
- **Moderate deterioration:** 2-3 measures worsening
- **Severe deterioration:** 3+ measures worsening or rapid deterioration in 1 measure

---

## Falsification Criteria

The hypothesis will be considered **supported** if:
- Deterioration rate is associated with increased risk of multimorbidity (HR > 1.0 for severe vs stable)
- At least one deterioration category shows HR ≥ 1.20 with 95% CI not including 1.0
- Interaction terms (baseline × change) are significant (p < 0.05)

The hypothesis will be considered **falsified** if:
- No association between deterioration rate and multimorbidity risk (HR ≈ 1.0 for all categories)
- All 95% CIs for deterioration categories include 1.0
- Effect sizes are clinically trivial (HR < 1.10)
- Interaction terms are non-significant (p > 0.05)

The hypothesis will be considered **inconclusive** if:
- Mixed results (some deterioration categories show association, others do not)
- Effect sizes are borderline (1.10 ≤ HR < 1.20)
- Results are sensitive to model specification or covariate adjustment
- Multiple testing concerns cannot be resolved

---

## Key References

### K1: Cardiovascular-Kidney-Metabolic Syndrome Progression
- **Title:** Rapid progression of cardiovascular-kidney-metabolic syndrome drives accelerated frailty trajectories: A longitudinal cohort study
- **Authors:** Chen L, Zheng W, Liu LH
- **Year:** 2026
- **DOI:** 10.1097/MD.0000000000049742
- **PMID:** 42432976
- **Claim:** This study demonstrates that rapid CKM syndrome progression (≥2 stages in 4 years) independently predicts accelerated frailty worsening, supporting the concept that dynamic progression of metabolic conditions carries prognostic information beyond baseline staging [K1].
- **Contribution:** This proposal extends the concept of progression to multimorbidity (CVD + CKD) beyond frailty, testing whether metabolic deterioration rate predicts incident multimorbidity risk.
- **Limitation:** The study focuses on frailty trajectories rather than incident multimorbidity; UKB has more comprehensive outcome data.
- **Locator:** Abstract, Results section on CKM progression and frailty trajectories
- **Evidence:** See `work/evidence-K1.txt`

### K2: CKM Syndrome Risk Prediction
- **Title:** Novel Prediction Equations for Absolute Risk Assessment of Total Cardiovascular Disease Incorporating Cardiovascular-Kidney-Metabolic Health: A Scientific Statement From the American Heart Association
- **Authors:** Khan SS, Coresh J, Pencina MJ, et al. (American Heart Association)
- **Year:** 2023
- **DOI:** 10.1161/CIR.0000000000001191
- **PMID:** 37947094
- **Claim:** The PREVENT equations demonstrate that incorporating CKM factors (including eGFR, hemoglobin A1c) improves cardiovascular risk prediction, highlighting the importance of integrating kidney function into metabolic risk assessment [K2].
- **Contribution:** This proposal tests whether incorporating the *rate of change* in metabolic measures improves prediction beyond including baseline CKM factors.
- **Limitation:** The study focuses on absolute risk prediction rather than dynamic deterioration; uses different risk factors than proposed.
- **Locator:** Abstract, Methods section on PREVENT equation development
- **Evidence:** See `work/evidence-K2.txt`

### K3: Risk Factor Trajectories and Lifetime Risk
- **Title:** Global Effect of Cardiovascular Risk Factors on Lifetime Estimates
- **Authors:** Global Cardiovascular Risk Consortium (Magnussen C et al.)
- **Year:** 2025
- **DOI:** 10.1056/NEJMoa2415879
- **PMID:** 40162648
- **Claim:** Risk factor trajectories (modification of hypertension and smoking in midlife) are associated with significant additional life-years free of cardiovascular disease, suggesting that dynamic changes in risk factors carry prognostic information beyond baseline status [K3].
- **Contribution:** This proposal adapts the concept of risk factor trajectory modification to metabolic deterioration in the context of multimorbidity (CVD + CKD) rather than just cardiovascular outcomes.
- **Limitation:** The study focuses on classic risk factors (hypertension, lipids, diabetes, smoking) rather than metabolic syndrome components; outcomes are CVD and all-cause death rather than multimorbidity.
- **Locator:** Abstract, Results section on risk factor trajectories and lifetime risk
- **Evidence:** See `work/evidence-K3.txt`

---

## Limitations

1. **Reverse causation:** Baseline measurements may be affected by early illness not yet captured in the outcome definition
2. **Single timepoint deterioration:** Two measurements cannot establish precise turning points or capture rapid changes within the 5-year interval
3. **Measurement error:** UKB measures are self-reported or from single readings; repeated measures would reduce error
4. **Selection bias:** Participants with both assessment waves may differ systematically from those with only baseline
5. **Confounding:** Unmeasured confounders (lifestyle factors, genetic predisposition, socioeconomic status) may influence both metabolic changes and disease risk
6. **Outcome definition:** Multimorbidity defined as CVD + CKD may not capture the full spectrum of metabolic-related diseases
7. **Temporal ambiguity:** Assessment wave 2 is ~5 years after baseline; the "deterioration" represents a 5-year change, not an annual rate

---

## Required Clinical Adjudication

1. **Multimorbidity definition:** Confirm that CVD + CKD is an appropriate proxy for metabolic-related multimorbidity in this context
2. **Deterioration thresholds:** Determine optimal cutoffs for categorizing mild vs moderate vs severe deterioration
3. **Confounding adjustment:** Identify additional covariates needed to reduce residual confounding (e.g., smoking, alcohol, physical activity, socioeconomic status)
4. **External validation:** Plan for independent validation in another cohort to assess generalizability
5. **Clinical applicability:** Determine whether deterioration rate can be measured in routine clinical practice

---

## Computational Resources

- **CPU:** 4 cores for data processing and statistical analysis
- **Memory:** 8 GB RAM for handling UKB dataset subsets
- **GPU:** Not required (standard statistical methods)
- **Time budget:**
  - Data loading and preprocessing: 30 minutes
  - Statistical analysis: 1-2 hours
  - Model fitting and validation: 1 hour
  - Total: ~4 hours

---

## Next Steps

1. Load UKB data and verify column mappings for metabolic measures
2. Identify participants with both baseline and second assessment metabolic data
3. Create deterioration rate composite score
4. Fit baseline Cox model with baseline metabolic levels
5. Fit alternative Cox model with deterioration rate and interaction terms
6. Compare model performance (C-index, calibration)
7. Assess falsification criteria and interpret results
