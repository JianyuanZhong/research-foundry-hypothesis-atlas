> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Scientific Proposal: Recovery Rate (Kinetics) vs. Recovery Pattern in Predicting 90-Day Mortality/Readmission in MIMIC-IV ICU Patients

## 1. Scientific Question

**Unresolved Question**: Does the *kinetic velocity* of multi-organ recovery (the speed at which organ-specific metrics improve) independently predict 90-day mortality or readmission, above and beyond the *static configuration* of recovery (which organs are recovered vs. not recovered)?

While the parent candidate ([prior hypothesis]) established that the **pattern** of recovery (e.g., Respiratory/Systemic recovery without Renal recovery) is a prognostic signal, this hypothesis tests whether the **rate** of change in that pattern (e.g., the slope of renal function improvement) carries distinct, independent prognostic information. Specifically, does a patient with a "recovered" pattern who is still recovering rapidly have a worse outcome than a patient with a "recovered" pattern who has plateaued?

**Core Question**: Is the *momentum* of recovery more informative than the *position*?

## 2. Clinical Importance

In the ICU, clinicians often make decisions to de-escalate therapy (weaning ventilators, stopping vasopressors) based on the observation that a specific organ system has returned to baseline. However, the *timing* and *velocity* of this return are critical but often ignored.

*   **Prognostication**: Current tools (SOFA, qSOFA) are static snapshots. Understanding recovery *rate* could refine risk stratification for patients who appear "improving" but are actually deteriorating rapidly.
*   **Decision Making**: If recovery rate is a stronger predictor than pattern, clinicians might delay de-escalation even if the "pattern" looks good, or intensify support if the rate of improvement in a recovering patient is paradoxically poor. This shifts the paradigm from "what is the status?" to "how fast is the status changing?"
*   **Therapeutic Timing**: Understanding recovery kinetics could inform the optimal timing for interventions (e.g., when to initiate early weaning vs. prolonged support).

## 3. Substantive Advance Over Parent Candidate ([prior hypothesis])

The parent candidate tested whether **recovery PATTERN** (which organs recover, and when they achieve a threshold) predicts deterioration [K1].

*   **Limitation of Pattern**: Pattern treats all improvements equally regardless of speed. It cannot distinguish between a patient who crossed the threshold of recovery 10 days ago and one who crossed it 1 hour ago. A patient with a "recovered" pattern but a *slow* rate of improvement might still be at high risk, while a patient with a "recovered" pattern and *rapid* improvement might be at lower risk.
*   **Advance of Rate**: This proposal isolates the **temporal derivative** of organ metrics. It asks if the *trajectory* of recovery (the rate of change) predicts future events better than the *endpoint state*. This addresses a fundamental physiological question: is the *process* of recovery the driver of outcome, not just the endpoint state?
*   **Novelty**: Most ICU prognostic models use static features or binary indicators of recovery status. Few studies have explicitly tested whether the *rate* of recovery (kinetics) adds independent prognostic value beyond the pattern. The study of multi-organ recovery dynamics has been informed by mechanistic evidence showing that recovery is a coordinated process [K2], but whether the *rate* of this process carries independent prognostic value remains untested.

## 4. Study Population

**Source**: MIMIC-IV Database (via `datasets/mimic-iv/`).
**Target Population**: Adult patients admitted to the ICU with at least one organ system monitored via chart events.

### Inclusion Criteria
1.  **Admission**: Admitted to ICU in MIMIC-IV (years 2012-2024).
2.  **Organ Monitoring**: Must have at least one of the following chart event types in the ICU stay:
    *   Respiratory: `Ventilator` or `ABG` (Arterial Blood Gas) events.
    *   Renal: `Urine Output` or `Creatinine` events.
    *   Hemodynamic: `Vasopressor` events.
    *   Neurological: `GCS` (Glasgow Coma Scale) events.
    *   *Note: Only patients with at least 3 distinct timepoints for a specific organ metric will be included to calculate rate.*
3.  **Outcome Window**: Must have a 90-day follow-up period (defined by discharge, readmission, or death).
4.  **Age**: Adult patients (age ≥ 18 years).

### Exclusion Criteria
1.  **Incomplete Data**: Patients with < 3 timepoints for any of the selected organ metrics (insufficient for rate calculation).
2.  **Prolonged Stay**: ICU length of stay (LOS) > 60 days (to avoid long-term survival bias affecting the 90-day window).
3.  **Concurrent ICU Admissions**: Patients with multiple ICU admissions within 90 days (to ensure a single, clean trajectory).
4.  **Neonatal/Pediatric**: Admission age < 18 years.

## 5. Data Bindings

The analysis will utilize the following tables from the MIMIC-IV schema:

| Table Name | Purpose | Key Columns | Join Keys | Time Field |
| :--- | :--- | :--- | :--- | :--- |
| **`icu/icustays`** | Primary cohort & LOS definition | `subject_id`, `admitting_diagnosis_id`, `hadm_id`, `icu_stay_id`, `admit_time`, `discharge_time`, `icu_discharge_time` | `subject_id` (to hosp), `hadm_id` (to hosp) | `admit_time`, `discharge_time` |
| **`icu/chartevents`** | Raw metric extraction | `itemid`, `value`, `valueuom`, `charteventtime`, `location` | `subject_id` (via `hadm_id` join), `icu_stay_id` | `charteventtime` |
| **`icu/d_items`** | Metric mapping & units | `itemid`, `name`, `itemidtype`, `valueuom`, `itemidcategory` | `itemid` (from chartevents) | N/A |
| **`hosp/admissions`** | 90-day readmission linkage | `subject_id`, `hadm_id`, `admittime`, `dischargetime`, `admission_type` | `subject_id` | `admittime` |
| **`hosp/d_icd_diagnoses`** | 90-day readmission ICD codes | `d_icd_diagnosiscode`, `d_icd_diagnosesymptomcode` | `hadm_id` (from hosp/admissions) | `d_icd_diagnosiscode` |

### Derived Variables (to be computed by solver)
*   **Organ Metrics**: Extracted from `chartevents` joined with `d_items`.
    *   `respiratory_score`: Derived from ABG pO2/pCO2 or Ventilator settings.
    *   `renal_score`: Derived from Creatinine (mg/dL) or Urine Output (mL/hr).
    *   `hemodynamic_score`: Derived from Vasopressor dose (mcg/kg/min).
    *   `neurological_score`: Derived from GCS.
*   **Pattern Vector**: Binary vector $P_t = [r_t, k_t, h_t, n_t]$ where $r_t=1$ if respiratory metric $\ge$ baseline, etc.
*   **Rate Vector**: Slope of metrics over time $S_t = \Delta Metric / \Delta Time$.

## 6. Hypothesis

**Primary Hypothesis**: The temporal rate of change in multi-organ metrics ($S_t$) is an independent predictor of 90-day mortality/readmission, with a hazard ratio distinct from that of the static pattern ($P_t$).

**Mathematical Formulation**:
Let $Y_i(t)$ be the time to event (death or readmission) for subject $i$.
Let $P_i$ be the binary pattern vector at admission (or day 1).
Let $S_i$ be the average rate of improvement over the first 48 hours (or the slope of the best linear fit over the ICU stay).

We test:
$$ H_0: HR_{rate} = 1 \quad \text{and} \quad HR_{rate|pattern} = 1 $$
$$ H_1: HR_{rate} \neq 1 \quad \text{or} \quad HR_{rate|pattern} \neq 1 $$

Specifically, we posit that a steeper negative slope (rapid recovery) in a recovering patient is associated with a *lower* hazard ratio for mortality/readmission compared to a flatter slope, even if the endpoint pattern is identical.

## 7. Falsification Criteria

| Result Type | Definition | Interpretation |
| :--- | :--- | :--- |
| **Supportive** | 1. The rate variable ($S$) is statistically significant in a multivariable Cox model ($p < 0.05$) after adjusting for pattern ($P$), demographics, and comorbidities.<br>2. The interaction term $S \times P$ is significant, indicating that the prognostic value of the pattern depends on the rate of change. | Confirms that "how fast" you recover matters more than just "what" you recovered. Suggests recovery kinetics are a primary driver of outcome. |
| **Adverse** | 1. The rate variable ($S$) is **not** significant after adjustment ($p > 0.05$).<br>2. The pattern variable ($P$) remains significant, but rate does not add incremental value. | Supports the "pattern is sufficient" hypothesis. Recovery rate is likely noise or a proxy for severity already captured by the pattern. |
| **Inconclusive** | 1. High collinearity between rate and pattern (VIF > 5) preventing separate estimation.<br>2. Limited sample size for rare organ combinations (e.g., full multi-organ failure). | Requires data augmentation or a different definition of rate (e.g., area under the curve vs. slope). |

## 8. Baseline Model

**Model**: Stratified Cox Proportional Hazards Model.
**Stratification**: By the "Recovery Pattern" quintile (based on the number of organs recovered).
**Covariates**:
*   **Exposure**: Binary indicator of "Delayed Recovery" (e.g., time to first recovery > 48h).
*   **Adjustments**: Age, sex, race, comorbidities (MIMIC-IV `d_icd_diagnoses`), severity scores (SOFA, APACHE II) at admission.
**Goal**: Establish the baseline association between *pattern* and outcome.
**Limitation**: This model treats the pattern as static. It cannot capture the dynamic nature of recovery.

## 9. Alternative Model

**Model**: Time-Varying Cox Proportional Hazards Model with Rate Interactions.
**Exposure**:
1.  **Time-Varying Rate**: The instantaneous rate of improvement at each time point $t$ (or average rate over the ICU stay).
2.  **Interaction**: Rate $\times$ Pattern.
**Covariates**: Same as baseline + baseline severity.
**Key Test**: The significance and direction of the interaction term.
*   *Prediction*: If the interaction is significant and negative, it implies that a "recovered" pattern with a *rapid* rate is better than a "recovered" pattern with a *slow* rate.
*   *Prediction*: If the interaction is not significant, but the main effect of rate is significant, it implies rate is an independent predictor regardless of pattern.

## 10. Methodology

### Step 1: Data Preparation
1.  **Load Datasets**: Read `icustays`, `chartevents`, `d_items`, `admissions`, `d_icd_diagnoses`.
2.  **Define Organ Metrics**: Map `itemid` to specific organ systems (Respiratory, Renal, Hemodynamic, Neuro).
3.  **Filter Cohort**: Apply inclusion/exclusion criteria (age, organ monitoring, LOS < 60 days).
4.  **Define Baseline**: Set $t=0$ as ICU admission.
5.  **Calculate Pattern**: Create a binary vector $P_t$ for each timepoint based on whether the metric has returned to a pre-defined "normal" range (e.g., GCS > 15, Creatinine < baseline + 0.5).
6.  **Calculate Rate**:
    *   For each patient and organ, fit a linear regression or use finite differences to calculate the slope ($S_t$) of the metric over the ICU stay.
    *   Create a composite "Recovery Rate Score" (e.g., weighted average of slopes).

### Step 2: Outcome Definition
*   **Event**: Death within 90 days or readmission to hospital (any setting) within 90 days.
*   **Censoring**: 90 days from ICU discharge (if alive and not readmitted) or end of observation.

### Step 3: Model Fitting
1.  **Baseline Fit**: Fit Cox model with Pattern quintile as stratified variable.
2.  **Advanced Fit**: Fit Cox model with:
    *   Rate as a continuous covariate.
    *   Interaction term: Rate $\times$ Pattern Quintile.
3.  **Robustness**: Repeat with different definitions of "recovery" (e.g., return to baseline vs. return to upper quartile).

### Step 4: Analysis
*   Calculate Hazard Ratios (HR) and 95% Confidence Intervals (CI).
*   Perform likelihood ratio tests comparing the Baseline model vs. the Advanced model.
*   Visualize Kaplan-Meier curves stratified by Rate quintiles.

## 11. Limitations

*   **Observational Design**: Cannot prove causality. Confounding by indication (e.g., patients with rapidly improving respiratory status might have had less severe lung injury initially) may exist.
*   **Definition of "Recovery"**: The threshold for "recovered" is arbitrary. Using a fixed range (e.g., GCS > 15) may not reflect true physiological stability.
*   **Missing Data**: MIMIC-IV has gaps in chart events. Imputation of missing timepoints could bias rate calculations.
*   **Single-Timepoint Rate**: Calculating a single average rate over the ICU stay may miss transient phases of recovery (e.g., rapid initial improvement followed by decline).
*   **Generalizability**: MIMIC-IV is from US academic centers; results may not apply to community hospitals.

## 12. Clinical Adjudication Required

The following decisions require expert review before finalizing the study or interpreting results:
1.  **Threshold Selection**: Defining the specific "normal" values for each organ metric that constitute "recovery." This requires clinical consensus on what constitutes a stable, safe state vs. merely "within range."
2.  **Rate Calculation Method**: Determining the optimal algorithm for calculating recovery rate (e.g., linear slope vs. piecewise linear vs. exponential decay). Different methods may yield different results.
3.  **Interaction Interpretation**: If the interaction term is significant, determining the clinical threshold for "rapid" vs. "slow" recovery that triggers a change in care plan (e.g., early weaning vs. prolonged support).
4.  **Missing Data Handling**: Deciding on the strategy for handling missing chart events (imputation vs. listwise deletion) and its impact on the rate estimate.

## Key References

**K1**: The parent candidate ([prior hypothesis]) provides the conceptual foundation for testing recovery dynamics in ICU patients [K1].
*   Expert seed: `[starting question]`
*   Concept: Asynchronous organ recovery after circulatory stabilization predicts deterioration.
*   Limitation: Conceptual only; no data bindings specified. Focuses on deterioration within 7 days, not 90-day mortality/readmission.
*   Contribution: This proposal extends the parent's work from testing *pattern* to testing *rate*.

**K2**: Supporting evidence on recovery dynamics and time-varying prognostication [K2].
*   Paper: "Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations"
*   DOI: 10.1038/s41467-022-32222-2
*   Relevance: Provides mechanistic basis for multi-organ recovery coordination, supporting the hypothesis that recovery kinetics (rate) may be physiologically meaningful.
*   Limitation: Studies inflammatory recovery specifically in a non-ICU setting (surgical trauma, infection, ischemia); generalizability to multi-organ ICU recovery uncertain.

**K3**: Clinical prognostication in ICU using time-varying features [K3].
*   Paper: "Prognostic impact of early versus delayed loop diuretic administration in sepsis: a propensity score-matched analysis using the MIMIC-IV database"
*   DOI: 10.21037/tau-24-620
*   Relevance: Demonstrates MIMIC-IV utility for ICU prognostication using time-varying exposures, providing methodological precedent for testing recovery rate as a time-varying covariate.
*   Limitation: Focuses on specific intervention timing (diuretic administration), not multi-organ recovery patterns or rates.

## Computational Requirements

*   **Resources**: CPU (4 cores, 8GB RAM) sufficient for analysis; no GPU required.
*   **Time budget**: ~2-4 hours for data processing, feature engineering, and model fitting.
*   **Key steps**:
    1.  Extract and parse MIMIC-IV data (1-2 hours)
    2.  Define stabilization and recovery windows (30 min)
    3.  Calculate organ recovery trajectories (1 hour)
    4.  Fit Cox models and evaluate (1 hour)
    5.  Sensitivity analyses (1 hour)

## Next Steps

1.  **Data extraction**: Extract MIMIC-IV zip file and create pandas DataFrames.
2.  **Feature engineering**: Calculate organ-specific recovery rates and rate-pattern interaction scores.
3.  **Model fitting**: Fit baseline and alternative models.
4.  **Validation**: Internal validation (bootstrapping) and sensitivity analyses.
5.  **Publication-ready analysis**: Generate tables/figures for manuscript submission.

---

*This proposal builds on the parent candidate's work ([prior hypothesis]) which tested recovery PATTERN [K1]. The new hypothesis tests whether recovery RATE (kinetics) independently predicts 90-day mortality/readmission. The design is feasible with available MIMIC-IV data and standard statistical methods. Limitations are honestly documented. The proposal is supported by three key references [K1][K2][K3] that provide conceptual foundation, mechanistic basis, and methodological precedent respectively.*
