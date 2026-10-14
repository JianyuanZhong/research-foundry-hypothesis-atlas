> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Hypothesis: Asynchronous Organ Recovery in Critical Illness

## Scientific Question

**Hypothesis:** In critically ill patients, the recovery trajectory of individual organs follows distinct temporal patterns, and the timing of recovery in one organ predicts the timing of recovery in other organs. This "asynchronous recovery" phenomenon may have important implications for:
1. When to anticipate multi-organ recovery
2. When to expect complications from incomplete recovery
3. Optimal timing for ICU discharge planning

## Unresolved Question

While existing literature describes organ dysfunction at admission, there is limited evidence on the **temporal dynamics of organ recovery** and how these trajectories interact. The expert seed eicu-01 ("Asynchronous organ recovery") [K2] hints at this question but lacks:
- A precise operational definition of "asynchronous" recovery
- Quantitative measures of recovery timing and coordination
- Testing across multiple organ systems simultaneously

## Clinical Importance

1. **ICU Discharge Planning**: Understanding which organ recovers first may inform when patients can safely leave ICU
2. **Complication Prevention**: If one organ recovers before others, it may be vulnerable to complications from incomplete recovery
3. **Treatment Optimization**: Knowledge of recovery coordination could guide when to escalate or de-escalate organ-specific support

## Substantive Advance Over Existing Knowledge

Current critical care literature typically:
- Describes organ dysfunction at admission or at specific timepoints
- Assesses recovery as binary (improved vs. not improved)
- Does not quantify the temporal coordination of multi-organ recovery

This study would:
- Define and measure **asynchrony** as a continuous variable (lag between organ recovery milestones)
- Test whether asynchrony predicts adverse outcomes (mortality, prolonged ventilation, readmission)
- Identify which organ pairs show the strongest temporal coordination

## Data Bindings (eICU Dataset)

### Primary Tables

Based on the eICU dataset catalog [K3] (`[internal dataset path]`):

1. **apacheApsVar** (`table-67711a86e012835e.json`)
   - Source: `baidu_downloads/eicu_mimic/eicu数据 库/EICU 2.0 数据/apacheApsVar.csv.gz`
   - Identity column: `patientunitstayid`
   - Key columns: `intubated`, `vent`, `dialysis`, `respiratory`, `hematocrit`, `creatinine`, `pao2`, `fio2`
   - Purpose: Organ dysfunction scores at ICU admission and during stay

2. **apachePredVar** (`table-b1f86cc4a8d9f2a2.json`)
   - Source: `baidu_downloads/eicu_mimic/eicu数据 库/EICU 2.0 数据/apachePredVar.csv.gz`
   - Identity column: `patientunitstayid`
   - Key columns: `verbal`, `motor`, `eyes`, `creatinine`, `ventday1`, `oobventday1`, `oobintubday1`, `admitdiagnosis`
   - Purpose: Predicted organ scores and admission characteristics

3. **vitalPeriodic** (`table-a22c6d6981a32279.json`)
   - Source: `baidu_downloads/eicu_mimic/eicu数据 库/EICU 2.0 数据/vitalPeriodic.csv.gz`
   - Identity column: `patientunitstayid`
   - Temporal column: `observationoffset` (minutes from ICU admission)
   - Key columns: `systemicmean`, `systemicsystolic`, `systemicdiastolic`, `pao2`, `sao2`, `heartrate`
   - Purpose: Continuous vital sign measurements for defining recovery trajectories

4. **intakeOutput** (`table-ebba5dc91b1d37e7.json`)
   - Source: `baidu_downloads/eicu_mimic/eicu数据 库/EICU 2.0 数据/intakeOutput.csv.gz`
   - Identity column: `patientunitstayid`
   - Purpose: Fluid balance metrics (optional, for confounding analysis)

5. **infusionDrug** (`table-18e1a8caaa91eb44.json`)
   - Source: `baidu_downloads/eicu_mimic/eicu数据 库/EICU 2.0 数据/infusionDrug.csv.gz`
   - Identity column: `patientunitstayid`
   - Purpose: Vasopressor/medication records (for treatment adjustment)

6. **patient** (`table-ab037c09d7df9a3c.json`)
   - Source: `baidu_downloads/eicu_mimic/eicu数据 库/EICU 2.0 数据/patient.csv.gz`
   - Identity column: `uniquepid`
   - Purpose: Patient demographics, hospital ID

### Key Variables

**Organ Dysfunction Scores (from apacheApsVar [K1]):**
- Respiratory: `vent` (ventilator use), `respiratory` (Apache respiratory score)
- Cardiovascular: `dialysis` (dialysis use, as proxy for cardiovascular support)
- Renal: `creatinine`, `hematocrit` (from apachePredVar)
- Neurological: `verbal`, `motor`, `eyes` (from apachePredVar)

**Recovery Definition:**
- For each organ, define "recovery" as return to baseline (e.g., score ≤ 2 points above admission)
- Recovery time = time offset (in minutes) when recovery milestone is achieved
- Asynchrony = difference in recovery times between organ pairs

**Outcomes:**
- Mortality: `diedinhospital` (from apachePredVar)
- Prolonged ventilation: `oobventday1` (out-of-bounds ventilation days)
- Readmission: `readmit` (from apachePredVar)

### Population

- ICU patients with complete Apache II and predicted organ scores
- Minimum 5 days of ICU stay (to observe recovery trajectories)
- At least one organ with documented recovery trajectory
- Exclude patients with pre-existing chronic organ failure (using pastHistory table if available)
- Hospital-level stratification possible via `hospital` table

## Baseline Approach

**Baseline Model**: Linear regression of organ recovery time on admission severity (APACHE II score)

This baseline tests whether more severe patients recover more slowly, but does not address:
- Temporal coordination between organs
- Whether recovery of one organ predicts another
- Non-linear recovery patterns

## Substantive Alternative

**Learning-Based Approach**:
- Train a survival model (e.g., Cox proportional hazards) predicting time to multi-organ recovery
- Use a deep learning approach (e.g., RNN/LSTM) to model multi-organ recovery trajectories
- Test whether features capturing asynchrony (e.g., lag between organ recovery) improve prediction

**What the Alternative Reveals:**
- Non-linear recovery patterns that linear models miss
- Organ-specific recovery rates that vary by patient characteristics
- Predictive value of asynchrony beyond admission severity

## Falsification Criteria

The hypothesis would be **falsified** if:
1. Organ recovery follows parallel trajectories with no significant asynchrony (all recovery lags are zero)
2. Asynchrony has no association with outcomes (mortality, prolonged ventilation, readmission)
3. Admission severity alone explains all variation in recovery timing

## Outcomes of Interest

1. **Supportive**: Organ recovery is asynchronous; asynchrony predicts adverse outcomes
   - Lung-kidney asynchrony: Respiratory recovers before kidney (common in ARDS with AKI)
   - Cardiovascular-renal asynchrony: Vasopressor-dependent patients show delayed renal recovery

2. **Adverse**: Organ recovery is synchronous; asynchrony is not a meaningful predictor
   - All organs recover at similar rates regardless of individual dysfunction

3. **Inconclusive**: Mixed patterns; requires more granular analysis
   - Some organ pairs show asynchrony, others don't
   - Requires subgroup analysis by admission severity or organ failure type

## Analysis Plan

1. **Define recovery milestones** for each organ system:
   - Respiratory: Time from admission to cessation of ventilation (or return to baseline SpO2)
   - Renal: Time from admission to creatinine return to baseline
   - Neurological: Time from admission to return of verbal/motor function
   - Cardiovascular: Time from admission to cessation of vasopressors

2. **Calculate asynchrony metrics**:
   - Lag between organ pairs (e.g., kidney recovery lag = kidney recovery time - respiratory recovery time)
   - Overall recovery coordination score
   - Time to first multi-organ recovery

3. **Test associations with outcomes**:
   - Cox regression for time-to-event outcomes (mortality, readmission)
   - Survival analysis comparing synchronous vs. asynchronous recovery
   - Compare recovery times between patients with high vs. low asynchrony

4. **Stratify by**:
   - Admission severity (APACHE II score)
   - Organ failure type (single vs. multi-organ failure)
   - Treatment intensity (vasopressor use, mechanical ventilation)

## Missing Evidence / Clinical Adjudication Required

1. **Ground truth for organ recovery**: Clinical judgment on what constitutes "recovery" for each organ
   - Need expert review to validate automated recovery definitions

2. **Treatment confounding**: Need to adjust for interventions that may accelerate or delay recovery
   - Vasopressor dosing, ventilator settings, renal replacement therapy

3. **External validation**: Results should be validated on independent cohort
   - May need MIMIC-IV or other ICU datasets for validation

4. **Causal inference**: Observational design cannot prove causation
   - Asynchrony may be a marker rather than a driver of outcomes

## Resource Requirements

- **CPU**: Moderate (data processing, statistical analysis)
- **GPU**: Optional for deep learning alternative
- **Time**: 1800 seconds for computation (per compute_limits)
- **Memory**: 4-8 GB for data loading and analysis

## Next Steps

1. Inspect eICU data structure to confirm variable availability (done via table schemas)
2. Develop data extraction and cleaning scripts
3. Define precise recovery metrics with clinical validation
4. Run baseline analysis
5. Implement alternative model if scientifically justified
6. Perform subgroup analyses and sensitivity checks

## Key References

The following three works inform this hypothesis [K1][K2][K3]:

1. **eICU Collaborative Research Database documentation** [K1] - Provides the data structure and conventions for organ dysfunction scoring
   - Source: https://physionet.org/content/eicu-crd/2.0/
   - Relevant: Apache II score methodology and organ dysfunction definitions

2. **Expert seed card: Asynchronous Organ Recovery (eicu-01)** [K2] - Provides the initial hypothesis direction on asynchronous organ recovery
   - Source: `[internal dataset path]`
   - Contribution: Initial hypothesis direction, data bindings validated

3. **Apache Predicted Variables table (apachePredVar)** [K3] - Contains predicted organ scores (verbal, motor, eyes, creatinine) and admission characteristics that can be used to define baseline organ function and track recovery
   - Source: `[internal dataset path]` (table-b1f86cc4a8d9f2a2.json)
   - Relevant: Organ score definitions and recovery baseline establishment

## Bibliography

- [K1] EICU Collaborative Research Database. eICU-CRD 2.0 documentation. PhysioNet, 2018. https://physionet.org/content/eicu-crd/2.0/
- [K2] Expert Research Team. Asynchronous organ recovery hypothesis. Expert seed card eicu-01, 2026.
- [K3] EICU Collaborative Research Database. apachePredVar table schema. Local dataset catalog, 2026.
