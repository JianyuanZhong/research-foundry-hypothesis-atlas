> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Hypothesis: Inflammatory Biomarker Trajectories Predict Multi-Organ Trajectory Divergence in Sepsis

## Unresolved Question

**Current knowledge gap:** Existing sepsis risk prediction focuses on either:
- Static admission characteristics (SOFA scores, APACHE II)
- Single-organ recovery metrics (e.g., creatinine alone for AKI)
- Concurrent multi-organ trajectories (whether concordant vs. discordant improvement predicts outcomes)

**What remains unknown:** How do *inflammatory biomarker dynamics* (procalcitonin, CRP, WBC trajectories) predict the *timing and magnitude* of multi-organ trajectory divergence? Specifically:
- Does the *rate of inflammatory change* predict when discordant organ patterns emerge?
- Can inflammatory trajectories identify patients at high risk of developing discordant organ trajectories before they manifest?
- Is there a specific inflammatory pattern (e.g., rapid decline vs. gradual increase) that precedes multi-organ deterioration?

## Clinical Importance

Sepsis remains the leading cause of death in critically ill patients. Current approaches:
- Rely on static scores that miss dynamic deterioration
- Focus on individual organs rather than system-wide patterns
- May miss early warning signals from systemic inflammatory responses

A better understanding of inflammatory dynamics could:
- Enable earlier identification of patients at risk of developing complex, discordant organ dysfunction
- Inform personalized monitoring strategies (e.g., when to intensify multi-organ surveillance)
- Guide targeted anti-inflammatory interventions to prevent organ trajectory divergence
- Reveal mechanistic links between systemic inflammation and multi-organ dysfunction patterns

## Substantive Advance Over Existing Knowledge

**Beyond single-organ metrics:** Current AKI recovery is often assessed by creatinine alone [K2]. This proposal tests whether inflammatory trajectories provide complementary information about *when* and *how* organ trajectories diverge.

**Beyond static scores:** SOFA scores are snapshots that may miss rapid deterioration. This proposal uses time-series analysis of inflammatory markers to capture dynamic patterns.

**Beyond concurrent trajectory analysis:** Existing work [K1] demonstrates that multi-organ patterns matter, but does not address the *mechanism* (inflammatory dynamics) that drives these patterns. This proposal tests whether inflammatory biomarkers can predict when discordant organ trajectories emerge.

**New mechanistic insight:** The hypothesis proposes that inflammatory biomarker trajectories are not just markers of severity, but *predictors* of multi-organ dysfunction patterns. This represents a shift from correlational to mechanistic understanding.

## Hypothesis Statement

**Primary hypothesis:** In septic patients, the *trajectory of inflammatory biomarkers* (procalcitonin, CRP, WBC) predicts the *timing and magnitude* of multi-organ trajectory divergence (discordant organ recovery patterns), independent of organ-specific measurements.

**Specific predictions:**
1. Patients with *rapidly declining* inflammatory markers have *lower* risk of developing discordant organ trajectories compared to those with stable or increasing markers.
2. The *rate of inflammatory change* (slope over time) is a stronger predictor of when discordant organ patterns emerge than absolute inflammatory values.
3. A machine learning model trained on inflammatory trajectories can predict the emergence of discordant organ patterns better than models using organ measurements alone.
4. There is a *temporal sequence*: inflammatory changes precede the emergence of discordant organ trajectories by a predictable lag period.

## Study Population and Main Data

**Population:** Adult patients in MIMIC-IV ICU stays with:
- Sepsis diagnosis (ICD-9/10 codes in d_icd_diagnoses)
- At least 3 ICU stays (to capture multiple admission events)
- Available inflammatory biomarker measurements at multiple time points
- Age ≥18 years
- No documented major bleeding events during ICU stay

**Main data tables with exact bindings:**

```
icu/icustays (table-7d5c8feb0fb0dbd4.json):
  - subject_id: patient identifier
  - hadm_id: hospital admission identifier
  - stay_id: ICU stay identifier
  - intime: admission timestamp
  - outtime: discharge timestamp
  - los: length of stay in days

hosp/labevents (table-bf701d962c63287c.json):
  - subject_id, hadm_id: join with icustays
  - charttime: timestamp of measurement
  - itemid: laboratory test code
  - value, valuenum, valueuom: lab values
  - ref_range_lower, ref_range_upper: reference ranges
  - Key itemids for inflammatory markers:
    - 23393: Serum creatinine (mg/dL) - for organ trajectory
    - Procalcitonin: Need to identify itemid (likely 23397 or similar)
    - CRP (C-reactive protein): Need to identify itemid (likely 23398 or similar)
    - WBC count: 23396 (cells/uL)

icu/chartevents (table-8208609a785ea7e8.json):
  - subject_id, hadm_id, stay_id: join with icustays
  - charttime: timestamp of measurement
  - itemid: measurement code
  - value, valuenum, valueuom: measurement values
  - Key itemids for organ measurements:
    - 127450: PaO2 (mmHg)
    - 29418: FiO2 (fraction)
    - 33066: SpO2 (%)
    - 33739: Mean arterial pressure (mmHg)
    - 33745: Norepinephrine dose (mcg/kg/min)
    - 33746: Epinephrine dose (mcg/kg/min)
    - 33747: Vasopressin dose (U/hr)

hosp/d_icd_diagnoses (table-b0aa21973044b4bd.json):
  - subject_id, hadm_id: join with icustays
  - icdcode, icdversion: diagnosis codes
  - Sepsis ICD codes: A40-A49, R65.2 (ICD-10); 038-039, 427.x (ICD-9)

hosp/patients (table-9154f8c46cade9af.json):
  - subject_id: patient demographics
  - age, sex, race, ethnicity
```

**Data availability check:** Before analysis, verify:
1. Procalcitonin and CRP itemids exist in hosp/labevents
2. Sufficient inflammatory measurements across time points (≥3 measurements per patient)
3. Sufficient organ measurements for trajectory analysis (≥3 measurements per organ)
4. Number of patients with ≥3 ICU stays is sufficient for analysis (target: >1000)

## Falsifiable Experiment Design

### Temporal Boundaries
- **Index time:** Time of first sepsis diagnosis (from d_icd_diagnoses)
- **Observation window:** 0-7 days post-diagnosis (to capture acute inflammation and organ recovery)
- **Follow-up:** 30-day in-hospital mortality and ICU readmission

### Primary Outcome
- **Discordant organ trajectory emergence:** Classification of whether patient develops discordant organ patterns (e.g., improving respiratory but worsening renal) within 0-7 days
- **Discordant trajectory magnitude:** Degree of divergence between organ trajectories (e.g., slope difference between respiratory and renal trajectories)

### Exposure: Inflammatory Biomarker Trajectory Patterns

**Pattern 1: Rate of Inflammatory Change**
- Calculate the slope of inflammatory markers (procalcitonin, CRP, WBC) over 0-7 days using linear regression
- High positive slope: Rapidly increasing inflammation
- High negative slope: Rapidly decreasing inflammation
- Near-zero slope: Stable inflammation

**Pattern 2: Inflammatory Trajectory Classification**
- Classify patients into:
  - *Rapidly improving:* Steep negative slope (rapid decline)
  - *Stable:* Near-zero slope
  - *Worsening:* Steep positive slope (rapid increase)

**Pattern 3: Multi-Biomarker Composite**
- Composite inflammatory score: Weighted combination of procalcitonin, CRP, WBC trajectories
- Compare trajectories of high vs. low composite scores

### Baseline Models

**Baseline 1: Single-Organ Models**
- Logistic regression using only creatinine at day 3 to predict discordant trajectory emergence
- Compare performance to inflammatory trajectory models

**Baseline 2: Static Scores**
- SOFA score at admission (computed from day 0 measurements)
- Compare performance to trajectory-based models

**Baseline 3: Single-Timepoint Multi-Organ**
- Multivariable logistic regression using all organ measurements at day 3 only
- Compare to inflammatory trajectory-based models

**Baseline 4: Organ Trajectory Alone**
- Model using only organ trajectory patterns (concordant vs. discordant) without inflammatory data
- Compare to inflammatory trajectory models

### Learning Alternative

**Model 1: Temporal Inflammatory Trajectory Model**
- Input: Time-series of inflammatory biomarkers (daily aggregates from 0-7 days)
- Architecture:
  - 1D convolutional layers (3 filters, kernel_size=3, stride=1) to capture short-term patterns
  - LSTM layer (64 units, batch normalization) to capture temporal dependencies
  - Dense output layer (sigmoid activation)
- Training: 80% training, 10% validation, 10% test split (stratified by outcome)
- Loss: Binary cross-entropy
- Evaluation: AUC, calibration, decision curve analysis

**Model 2: Combined Inflammatory-Organ Trajectory Model**
- Input: Both inflammatory biomarker trajectories AND organ trajectories
- Test whether combining inflammatory and organ data improves prediction

### Analysis Plan

1. **Descriptive:** Distribution of inflammatory trajectories by outcome
2. **Univariate:** Association of inflammatory trajectory patterns with discordant organ emergence (logistic regression with robust standard errors)
3. **Multivariate:** Adjust for confounders (age, sex, comorbidities, severity of initial insult, admission source)
4. **Model comparison:** Compare baseline models vs. learning models using:
   - AUC (area under ROC curve)
   - Brier score (calibration + discrimination)
   - Decision curve analysis (net benefit)
5. **Temporal analysis:** Test whether inflammatory changes precede organ trajectory divergence (lag analysis)
6. **External validation:** Apply models to time-split validation (train on 0-30 days, validate on 31-60 days)

### Falsification Criteria

The hypothesis would be **falsified** if:
1. Inflammatory trajectory patterns show no significant association with discordant organ emergence (OR < 1.2, p > 0.05 after adjustment)
2. Inflammatory trajectory models perform no better than organ trajectory models alone (AUC difference < 0.02, 95% CI includes 0)
3. No temporal precedence is observed (inflammatory changes do not precede organ trajectory divergence)

The hypothesis would be **supported** if:
1. Rapidly declining inflammatory markers are significantly associated with *lower* risk of discordant organ trajectories (OR < 0.8, p < 0.01 after adjustment)
2. Inflammatory trajectory models significantly outperform organ trajectory models alone (AUC improvement > 0.05, p < 0.01)
3. A significant temporal lag is observed (inflammatory changes precede organ trajectory divergence)

The hypothesis would be **inconclusive** if:
1. Inflammatory trajectories show weak association (OR 0.8-1.2, p 0.05-0.1)
2. Models show marginal improvement (AUC difference 0.02-0.04)
3. Results are inconsistent across subgroups or time periods

## Limitations and Unresolved Questions

1. **Missing inflammatory measurements:** Not all patients have complete inflammatory marker data. Need to handle missingness appropriately (multiple imputation or sensitivity analysis).

2. **Measurement frequency:** Inflammatory markers may not be measured at regular intervals. May miss rapid changes between measurements.

3. **Confounding by indication:** Treatment decisions may be influenced by inflammatory markers, creating feedback loops. Requires careful adjustment or instrumental variable analysis.

4. **Causality:** Observational study; cannot establish causation.

5. **External validity:** MIMIC-IV represents US ICUs; may not generalize to other settings.

6. **Itemid mapping:** Procalcitonin and CRP itemids need to be verified against d_items table.

## Required Additional Evidence

To fully validate this hypothesis, the following would be needed:
1. **External validation:** Apply findings to another ICU dataset (eICU, MIMIC-II/III, or other hospital)
2. **Prospective validation:** Test prediction model in real-time clinical setting
3. **Mechanistic insights:** Understanding *why* inflammatory trajectories predict organ divergence (e.g., inflammatory cascades, cytokine storms, immune dysfunction)
4. **Intervention trials:** Test whether recognizing inflammatory trajectory patterns improves outcomes with targeted interventions (e.g., early anti-inflammatory therapy)

## Computational Requirements

- **CPU:** 8 cores, 32GB RAM for data processing and model training
- **GPU:** 1 GPU, 16-24GB VRAM for deep learning model training (optional but recommended)
- **Time:** 3600 seconds total budget
  - Data processing: 600 seconds
  - Model training: 1800 seconds
  - Evaluation and analysis: 600 seconds

## Next Steps

1. **Phase 1 (Data verification):** Verify data availability, especially procalcitonin and CRP itemids
2. **Phase 2 (Baseline models):** Implement baseline models and compute performance
3. **Phase 3 (Learning models):** Develop and train inflammatory trajectory models
4. **Phase 4 (Model comparison):** Compare models and test hypothesis
5. **Phase 5 (Documentation):** Document findings, limitations, and implications

## Key References

**[K1]** Mistry A, et al. "Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations." *Nature Communications* 13, 2022. DOI: 10.1038/s41467-022-32222-2. Supports the hypothesis that multi-cellular dynamics (and by extension multi-organ) may be important for recovery assessment in sepsis.

**[K2]** Liu X, et al. "Comparison of Cystatin C and Creatinine in the Assessment of Measured Kidney Function during Critical Illness." *Critical Care Medicine* 2023. PMID: 37256861. Supports that single-organ metrics (creatinine alone) may be insufficient and alternative measures or multi-organ assessment could be better.

**[K3]** Gerstung O, et al. "Learning the natural history of human disease with generative transformers." *Nature* 2025. DOI: 10.1038/s41586-025-09529-3. Provides methodological precedent for using machine learning on longitudinal clinical data to improve risk prediction.
