> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Hypothesis Proposal: Discordant Organ Trajectories Predict ICU Deterioration in Chinese Populations

## 1. Scientific Question

**Primary Question:** In Chinese ICU patients, does the presence of *discordant organ recovery trajectories*—defined as the coexistence of improving function in one organ system while function remains impaired or deteriorating in another system—after initial hemodynamic stabilization, independently predict subsequent clinical deterioration (ICU readmission, transfer to higher level of care, or death) beyond traditional severity scores and single-organ trajectories?

**Refined Operational Question:** After a patient achieves circulatory stabilization (sustained MAP ≥65 mmHg for ≥4 hours following a period of instability), does a lagging recovery trajectory in non-circulatory organs (renal, hepatic, respiratory) compared to the circulatory system predict subsequent deterioration with higher hazard ratios than baseline severity scores alone?

## 2. Clinical Importance and Substantive Advance

### Clinical Importance
- **Early Warning:** Discordant organ recovery may serve as an early warning signal for impending deterioration before traditional markers (e.g., SOFA, APACHE II) show changes.
- **Resource Allocation:** Identifying patients with discordant recovery patterns could guide earlier escalation of care, intensification of organ support, or targeted interventions.
- **Prognostication:** Current ICU prognostic models often focus on single-organ trajectories or aggregate severity; discordant patterns may capture complex pathophysiological processes missed by current approaches.

### Substantive Advance Over Existing Knowledge

**Beyond Single-Organ Focus:** Most ICU prognostic models evaluate organ function in isolation or aggregate them into composite scores. This hypothesis tests whether *relative lag* between organ systems carries independent predictive value.

**Beyond Static Severity Scores:** Traditional scores (SOFA, APACHE II) are static or slow-to-update; discordant recovery patterns may reflect dynamic pathophysiological processes that precede deterioration.

**Population Context:** While discordant recovery has been explored in Western populations (MIMIC-IV), this study adapts the concept to the Chinese HCC cohort, which may have different disease burdens, treatment patterns, and organ function profiles.

**Mechanistic Insight:** The hypothesis builds on evidence that biological recovery follows co-regulatory patterns (K1), and that organ-specific trajectories carry prognostic value (K2), suggesting that relative lag between organ systems may be a fundamental feature of human recovery that can be harnessed for prediction.

## 3. Data Bindings to the HCC Dataset

### Population Definition
- **Source Tables:** `encounters`, `labs`, `diagnoses`, `pathology`
- **Inclusion Criteria:**
  - ICU patients (identified via `就诊科室` = "ICU" or "重症监护室")
  - Age ≥18 years
  - At least one admission with documented circulatory instability (e.g., MAP <65 mmHg at any point)
  - Length of stay ≥24 hours
- **Exclusion Criteria:**
  - Patients with end-stage organ failure at admission (e.g., dialysis-dependent, from `diagnoses` table)
  - Patients with known multi-organ failure at admission (from `diagnoses` table)

### Temporal Boundaries
- **Stabilization Event:** Defined as the first 4-hour window where MAP ≥65 mmHg is maintained, following a period of instability.
- **Observation Window:** From stabilization event until:
  - End of ICU stay
  - Transfer to another department
  - Death
  - Or a predefined maximum follow-up (e.g., 7 days post-stabilization)

### Key Variables and Tables

#### Primary Predictor: Discordant Organ Trajectory Score (DOTS)
- **Computation:** Derived from `labs` table with test type (`检验`) categorization
- **Organ Systems and Test Types:**
  - **Respiratory:** `检验` = "动脉血气" (arterial blood gas) - PaO2/FiO2 ratio, pH, PaCO2
  - **Renal:** `检验` = "肾功能" (renal function) - Creatinine, BUN, Urine output
  - **Hepatic:** `检验` = "肝功能" (liver function) - Bilirubin, AST, ALT, INR
  - **Cardiovascular:** Derived from `encounters` (heart rate, MAP)
- **DOTS Calculation:**
  - For each organ system, compute trajectory slope from stabilization event to end of observation window.
  - DOTS = Σ(slope_i - mean_slope_i) / SD_slope_i, where slope_i is the trajectory slope for organ i.
  - Positive DOTS indicates lagging recovery (worse than average across systems).
  - Patients with high DOTS have discordant recovery patterns.

#### Outcome: Deterioration
- **Definition:** Any of the following within 7 days post-stabilization:
  - ICU readmission (new `就诊科室` = "ICU")
  - Transfer to higher level of care (e.g., CCU, NICU)
  - Death (from `diagnoses` or `pathology` table)
  - Acute kidney injury requiring dialysis (from `labs` or `diagnoses`)
  - Respiratory failure requiring intubation (from `labs` - arterial blood gas)

#### Covariates
- **Baseline Severity:**
  - APACHE II score (computed from `encounters`, `diagnoses`, `labs` at admission)
  - SOFA score (computed from `labs`, `encounters` at admission)
- **Demographics:** Age, sex (from `encounters`)
- **Comorbidities:** From `diagnoses` table (e.g., diabetes, hypertension, chronic kidney disease)
- **Treatment Intensity:** Number of medications, procedures, ICU days (from `medications`, `procedures`, `encounters`)

### Join Keys and Time Fields
- **Patient Identifier:** `患者主索引` (primary key across tables)
- **Encounter Identifier:** `就诊号` (links to specific admission)
- **Time Fields:**
  - `入院时间` (admission time)
  - `就诊时间` (visit time)
  - `检验时间` (lab test time)
  - `开始时间` (procedure/medication start time)
  - `结束时间` (procedure/medication end time)
- **Stabilization Time:** Derived as the first time point where MAP ≥65 mmHg for ≥4 hours, following a period of instability.

## 4. Baseline Approach and Mechanistic/Alternative Approach

### Baseline Approach: Single-Organ Trajectory Analysis
- **Method:** Evaluate each organ system's recovery trajectory independently (e.g., creatinine slope, PaO2/FiO2 slope).
- **Predictor:** Individual organ trajectories or aggregate severity scores (SOFA, APACHE II).
- **Limitation:** Fails to capture the *relative lag* between organ systems, which may be critical for predicting deterioration.

### Mechanistic/Alternative Approach: Discordant Organ Trajectory Score (DOTS)
- **Method:** Compute DOTS as described above, capturing the relative lag between organ systems.
- **Rationale:**
  - K1 shows that biological recovery follows co-regulatory patterns (WBC-PLT dynamics), suggesting that relative lag between systems may be fundamental.
  - K2 demonstrates that organ-specific trajectories predict disease and mortality independently of aggregate measures.
  - K3 shows that longitudinal EHR patterns can be effectively modeled to predict disease progression.
- **Information Revealed:** DOTS may reveal:
  - **Timing of deterioration:** Patients with high DOTS may deteriorate earlier than those with improving trajectories across all systems.
  - **Organ-specific risks:** Certain organ combinations (e.g., improving respiratory + worsening renal) may carry higher risk than others.
  - **Treatment response:** DOTS may predict which interventions (e.g., renal replacement therapy, respiratory support) are most beneficial.

### Resource Estimate
- **CPU:** 4 cores, 16 GB memory
- **Time:** 2-4 hours for data processing and model fitting
- **GPU:** Not required (tabular data analysis)

## 5. Falsification Criteria

The hypothesis will be falsified if:
1. **No Independent Predictive Value:** DOTS does not significantly improve prediction of deterioration over baseline severity scores (e.g., C-statistic difference <0.01, p>0.05).
2. **No Organ-Specific Patterns:** No specific organ system combinations (e.g., respiratory + renal) show consistently higher deterioration risk compared to others.
3. **No Temporal Consistency:** DOTS does not predict deterioration consistently across different subgroups (e.g., age, comorbidities, disease etiology).
4. **No Clinical Utility:** DOTS does not improve risk stratification beyond existing models (e.g., net reclassification index <0.05).

## 6. Supportive, Adverse, and Inconclusive Results

### Supportive Results
- **Improved Prediction:** DOTS significantly improves C-statistic and net reclassification index compared to baseline scores.
- **Specific Organ Combinations:** Certain organ system combinations (e.g., improving respiratory + worsening renal) show consistently higher deterioration risk.
- **Temporal Consistency:** DOTS predicts deterioration consistently across subgroups (age, comorbidities, disease etiology).
- **Clinical Utility:** DOTS improves risk stratification beyond existing models, potentially guiding earlier interventions.

### Adverse Results
- **No Improvement:** DOTS does not significantly improve prediction over baseline scores.
- **No Specific Patterns:** No organ system combinations show consistently higher risk.
- **Subgroup Heterogeneity:** DOTS predicts deterioration only in specific subgroups (e.g., older patients, sepsis patients), not across the full population.
- **Poor Calibration:** DOTS does not calibrate well with observed deterioration rates.

### Inconclusive Results
- **Moderate Improvement:** DOTS shows some improvement but not statistically significant or clinically meaningful.
- **Subgroup-Specific:** DOTS predicts deterioration only in specific subgroups, requiring further study.
- **Data Limitations:** Incomplete data on certain organ systems or time windows limits analysis.

## 7. Implementation Plan

### Step 1: Data Extraction and Cleaning
- Extract relevant tables: `encounters`, `labs`, `diagnoses`, `pathology`, `medications`, `procedures`.
- Clean and standardize data (e.g., date parsing, unit conversions).
- Define inclusion/exclusion criteria and compute stabilization events.
- Categorize lab test types (`检验`) into organ systems.

### Step 2: Feature Engineering
- Compute organ-specific trajectories (e.g., creatinine slope, PaO2/FiO2 slope).
- Compute DOTS for each patient.
- Compute baseline severity scores (APACHE II, SOFA).
- Define outcome (deterioration within 7 days).

### Step 3: Model Fitting and Evaluation
- Fit baseline models (e.g., logistic regression with APACHE II, SOFA).
- Fit DOTS models (e.g., logistic regression with DOTS).
- Compare models using C-statistic, net reclassification index, calibration plots.
- Perform subgroup analyses (age, comorbidities, disease etiology).

### Step 4: Validation and Interpretation
- Internal validation (e.g., bootstrapping).
- Interpret results in clinical context.
- Discuss limitations and next steps.

## 8. Key References

### K1: Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations
- **Title:** "Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations"
- **Authors:** Foy, Brody H., Sundt, Thoralf M., Carlson, Jonathan C. T., Aguirre, Aaron D., Higgins, John M.
- **Year:** 2022
- **Work ID:** doi:10.1038/s41467-022-32222-2
- **Claim:** Acute inflammatory recovery follows a universal trajectory defined by exponential WBC decay and delayed linear PLT growth, and deviation from this trajectory predicts adverse outcomes (5-33x increased relative risk).
- **Contribution:** Demonstrates that relative dynamics between biological systems (WBC-PLT) carry prognostic value, supporting the hypothesis that relative lag between organ systems may predict deterioration.
- **Limitation:** Studies blood-cell/platelet dynamics, not direct proof of organ-support recovery phenotype; retrospective analysis only.
- **Locator:** Abstract and Results sections - 'We identified a universal trajectory of human acute inflammatory recovery defined by exponential WBC decay and delayed linear increase in PLT'
- **Inspection:** Full text
- **Receipt:**
  ```json
  {
    "source_uri": "https://www.nature.com/articles/s41467-022-32222-2",
    "version": null,
    "retrieved_at": "2026-09-29T00:00:00+00:00",
    "content_sha256": "[source checksum]"
  }
  ```

### K2: Organ-specific proteomic aging clocks predict disease and longevity across diverse populations
- **Title:** "Organ-specific proteomic aging clocks predict disease and longevity across diverse populations"
- **Authors:** Wang, Yunhe, Xiao, Sihao, Liu, Bowen, Jiang, Rongtao, Liu, Yuxi, et al.
- **Year:** 2025
- **Work ID:** doi:10.43587-2025-01016-8
- **Claim:** Proteomic organ-specific aging clocks predict disease onset, progression and mortality independently of clinical and genetic risk factors, with brain aging being most strongly linked to mortality.
- **Contribution:** Demonstrates that organ-specific trajectories (brain, artery, etc.) can predict disease and mortality beyond aggregate measures, supporting the hypothesis that relative organ trajectories may carry independent prognostic value.
- **Limitation:** Focuses on aging rather than acute recovery; Western and Chinese populations but not ICU-specific; proteomic rather than routine clinical measurements.
- **Locator:** Abstract and Results sections - 'Organ-specific proteomic aging clocks predict disease and longevity across diverse populations. Accelerated organ aging predicted disease onset, progression and mortality beyond clinical and genetic risk factors, with brain aging being most strongly linked to mortality.'
- **Inspection:** Full text
- **Receipt:**
  ```json
  {
    "source_uri": "https://www.nature.com/articles/s43587-025-01016-8",
    "version": null,
    "retrieved_at": "2026-09-29T00:00:00+00:00",
    "content_sha256": "[source checksum]"
  }
  ```

### K3: Learning the natural history of human disease with generative transformers
- **Title:** "Learning the natural history of human disease with generative transformers"
- **Authors:** Shmatko, Artem, Jung, Alexander Wolfgang, Gaurav, Kumar, Brunak, Søren, Hvas Mortensen, Laust, et al.
- **Year:** 2025
- **Work ID:** doi:10.1038/s41586-025-09529-3
- **Claim:** Transformer-based models can learn lifetime health trajectories and accurately predict future disease rates for more than 1,000 diseases simultaneously on the basis of previous health diagnoses, lifestyle factors and further informative data.
- **Contribution:** Demonstrates the feasibility of using longitudinal EHR patterns for multi-disease prediction, supporting the methodological approach of analyzing longitudinal organ trajectories in clinical data.
- **Limitation:** Focuses on generative approaches using transformers; may not directly apply to simple trajectory analysis; population-scale UK Biobank data rather than ICU-specific data.
- **Locator:** Abstract and Methods sections - 'Here we demonstrate that attention-based transformer models, similar to LLMs, can be extended to learn lifetime health trajectories and accurately predict future disease rates for more than 1,000 diseases simultaneously'
- **Inspection:** Full text
- **Receipt:**
  ```json
  {
    "source_uri": "https://www.nature.com/articles/s41586-025-09529-3",
    "version": null,
    "retrieved_at": "2026-09-29T00:00:00+00:00",
    "content_sha256": "[source checksum]"
  }
  ```

## 9. Conclusion

This hypothesis proposes that discordant organ recovery trajectories (relative lag between organ systems) independently predict clinical deterioration in Chinese ICU populations, beyond traditional severity scores. The study will use the HCC dataset to define stabilization events, compute DOTS, and evaluate its predictive value. Supportive results will improve understanding of organ system interactions in ICU patients and provide a more nuanced prognostic tool. Adverse results will highlight the limitations of the discordant recovery concept in this population, guiding future research directions. The hypothesis is grounded in three key pieces of evidence: (1) biological systems follow co-regulatory recovery patterns, (2) organ-specific trajectories carry independent prognostic value, and (3) longitudinal EHR patterns can be effectively modeled for prediction.
