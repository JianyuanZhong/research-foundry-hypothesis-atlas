> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Asynchronous Organ Recovery in Critically Ill Patients

**Seed ID:** `[starting question]`
**Dataset:** MIMIC-IV
**Status:** Developed with complete reference citations and concrete data bindings

## Hypothesis to Test

After circulatory stabilization, patients whose kidney or respiratory function remains impaired are more likely to deteriorate again, independent of baseline severity.

Formally: In patients with sepsis or shock who achieve hemodynamic stability (defined by cessation of vasopressor requirement and resolution of hypotension), the presence of residual organ dysfunction (persistent elevation in creatinine or hypoxemia requiring supplemental oxygen) within 24-48 hours post-stabilization predicts subsequent clinical deterioration (requiring escalation of organ support or death) within 7 days, after adjusting for baseline SOFA score and confounders.

## Study Population and Main Data

**Population:** Patients with confirmed sepsis or septic shock in MIMIC-IV (ICU admissions with sepsis-related diagnoses)

**Main data tables:**
- `icu/icustays`: ICU stays with admission time, discharge time, SOFA scores, vasopressor use
- `icu/chartevents`: Vital signs, oxygen therapy, hemodynamic parameters
- `icu/ingredientevents`: Medication administration including vasopressors, diuretics
- `hosp/labevents`: Laboratory measurements including creatinine, lactate, white blood cell count
- `hosp/d_icd_diagnoses`: ICD-10 diagnoses for sepsis identification
- `icu/outputevents`: Urine output (for kidney function assessment)

**Key variables:**
- `STABILIZATION_TIME`: Timestamp when patient achieves hemodynamic stability (last vasopressor dose + 6 hours post-cessation)
- `KIDNEY_IMPAIRMENT`: Binary flag for persistent creatinine elevation (> baseline + 0.3 mg/dL or > 1.5x baseline) within 24-48h post-stabilization
- `RESPIRATORY_IMPAIRMENT`: Binary flag for persistent hypoxemia (PaO2/FiO2 < 300 mmHg or SpO2 < 90% on supplemental O2) within 24-48h post-stabilization
- `DETERIORATION`: Binary outcome (death or requiring escalation of organ support within 7 days post-stabilization)

## Scientific Significance

1. **Captures recovery dynamics not represented by single SOFA assessment**: Traditional severity scoring uses single-timepoint SOFA scores that cannot capture the temporal dynamics of organ recovery. This study tests whether multi-organ recovery trajectories provide prognostic information beyond static severity.

2. **Identifies modifiable risk factors**: If residual organ impairment predicts deterioration, interventions targeting early detection and management of persistent organ dysfunction could improve outcomes.

3. **Advances trajectory-based prognosis**: Moving beyond static risk scores to dynamic, time-dependent prognostic models that account for recovery trajectories.

## Baseline Approach

**Model:** Cox proportional hazards regression with static baseline SOFA score as covariate

**Hypothesis:** Patients with persistent kidney or respiratory impairment after stabilization have higher hazard of deterioration compared to those without, after adjusting for baseline SOFA score.

**Expected null result:** No significant association between post-stabilization organ impairment and subsequent deterioration (HR ≈ 1, p > 0.05).

## Alternative Approach

**Model:** Gradient boosting classifier (XGBoost/LightGBM) with multi-organ recovery trajectory features

**Features:**
- Time-dependent features: Recovery trajectory slope (rate of change in organ function over 24-48h post-stabilization)
- Interaction terms: Baseline SOFA × post-stabilization organ impairment
- Temporal features: Time since stabilization, time to deterioration

**Hypothesis:** The ML model with multi-organ recovery trajectories achieves significantly better discrimination (AUC difference > 0.05, p < 0.01) than the baseline Cox model.

**Expected alternative result:** ML model significantly outperforms baseline, supporting the hypothesis that dynamic recovery trajectories contain prognostic information beyond static severity scores.

## Data Bindings

**MIMIC-IV table mappings:**
- Sepsis identification: `hosp/d_icd_diagnoses` with ICD-10 codes for sepsis (A40-A47, R65.20, etc.)
- Hemodynamic stability: `icu/ingredientevents` for vasopressor administration + `icu/chartevents` for blood pressure monitoring
- Kidney impairment: `hosp/labevents` with creatinine measurements, linked via `hosp/patients` and `icu/icustays`
- Respiratory impairment: `icu/chartevents` with SpO2, PaO2, FiO2 measurements
- Deterioration outcome: `icu/icustays` with discharge disposition (death vs. transfer vs. home) + `hosp/d_icd_diagnoses` for readmission within 7 days

**Join keys:**
- `hosp/patients` (patient_id)
- `icu/icustays` (stay_id, linked to patient_id via `hosp/patients`)
- `hosp/labevents` (patient_id, time)
- `icu/chartevents` (patient_id, time)
- `icu/ingredientevents` (patient_id, time, itemcode)

## Falsification Criteria

The hypothesis is **falsified** if:
1. No significant association between post-stabilization organ impairment and subsequent deterioration after adjusting for baseline severity (p > 0.05 for association test)
2. The ML model does not significantly outperform the baseline Cox model (AUC difference < 0.05, p > 0.01 for comparison)
3. The association disappears after adjusting for key confounders (age, comorbidities, severity of initial insult)

The hypothesis is **supported** if:
1. Significant association between post-stabilization organ impairment and subsequent deterioration (p < 0.01)
2. ML model significantly outperforms baseline (AUC difference > 0.05, p < 0.01)
3. Association persists after adjusting for confounders

The hypothesis is **inconclusive** if:
1. Results are mixed or inconsistent across organ systems
2. Key confounders cannot be adequately measured
3. Sample size is insufficient for definitive conclusions

## Limitations

1. **Selection bias in measurements**: Not all patients have repeated laboratory or vital sign measurements; recovery trajectories may be incompletely observed
2. **Definition of stabilization**: Hemodynamic stability is defined by vasopressor cessation, but may not fully capture physiological recovery
3. **Confounding**: Unmeasured confounders (e.g., source of infection, specific organ damage) may affect results
4. **Temporal resolution**: Data granularity limits precise timing of stabilization and deterioration events
5. **External validity**: Results may not generalize to other ICU populations or settings

## Key References

### K1: Gerstung et al. 2025 (Nature)
**Title:** Learning the natural history of human disease with generative transformers
**Authors:** Shmatko A, Jung AW, Gaurav K, Brunak S, Mortensen LH, Birney E, Fitzgerald T, Gerstung M
**DOI:** 10.1038/s41586-025-09529-3
**PMID:** 40963019
**Claim:** Demonstrates that transformer models can learn disease progression patterns from population-scale data, supporting the use of ML approaches for trajectory-based prognosis.
**Contribution:** Provides methodological justification for using transformer/ML models to learn disease progression patterns from MIMIC-IV data.
**Limitation:** Focuses on cancer progression, not critical illness; does not address organ-specific recovery trajectories.
**Locator:** Abstract and Methods sections describing the transformer architecture and training approach.
**Inspection:** abstract_only

### K2: Ma et al. 2026 (BMC Medical Informatics and Decision Making)
**Title:** Lactate trajectories and outcomes in critically ill patients with septic shock: a retrospective analysis of the MIMIC-IV database
**Authors:** Ma Y, Du L, Tang H
**DOI:** 10.1186/s12911-026-03352-0
**PMID:** 41606597
**Claim:** Time-dependent lactate trajectories provide prognostic information beyond static lactate measurements in septic shock patients.
**Contribution:** Directly relevant to the study design, demonstrating that temporal patterns in biomarkers (lactate) predict outcomes in critical illness.
**Limitation:** Focuses on single biomarker (lactate), not multi-organ recovery trajectories.
**Locator:** Abstract and Results sections on trajectory analysis methods.
**Inspection:** abstract_only

### K3: Reichardt et al. 2025 (European Journal of Trauma and Emergency Surgery)
**Title:** Absolute lymphocyte count trajectory predicts clinical outcome in severely injured patients
**Authors:** Reichardt LM, Hindelang B, Süberkrub L, Hamberger KL, Graw JA, Schuetze K, Zechendorf E, Mannes M, Halbgebauer R, Wohlgemuth L, Gebhard F, Huber-Lang M, Relja B, Bergmann CB
**DOI:** 10.1007/s00068-025-02864-0
**PMID:** 40314767
**Claim:** Trajectory-based analysis of lymphocyte count predicts clinical outcome in trauma patients, supporting the value of dynamic biomarker monitoring.
**Contribution:** Provides empirical evidence that trajectory-based analysis of biomarkers improves prognostic accuracy.
**Limitation:** Focuses on trauma population, not sepsis/critical illness; single biomarker (lymphocyte count).
**Locator:** Abstract and Methods sections on trajectory modeling.
**Inspection:** abstract_only

## Next Steps

1. **Data exploration**: Inspect MIMIC-IV tables to verify variable availability and define precise recovery criteria
2. **Baseline analysis**: Implement Cox model with static SOFA to establish null hypothesis baseline
3. **ML implementation**: Develop gradient boosting model with multi-organ recovery trajectory features
4. **Validation**: Split data into training/validation/test sets; perform cross-validation
5. **Interpretability**: Use SHAP values to interpret ML model predictions and ensure clinical interpretability
6. **Clinical validation**: Assess whether findings would inform early treatment modification in practice

## Required Clinical Adjudication

The following require clinical expert review:
1. **Definition of hemodynamic stability**: Clinical criteria for "circulatory stabilization" may vary; expert consensus needed
2. **Definition of deterioration**: Clinical judgment on what constitutes "requiring escalation of organ support"
3. **Confounding adjustment**: Expert review needed to identify appropriate covariates and methods for time-varying confounding
4. **Clinical applicability**: Assessment of whether findings would translate to clinical practice and impact decision-making

## Resource Requirements

**CPU:** 4 cores, 8GB memory for data processing and model training
**GPU:** Not required for this analysis (gradient boosting can run on CPU)
**Time:** 2-4 hours for complete analysis including data exploration, model training, and interpretation

---

*This proposal has been developed from expert seed `[starting question]` with complete reference citations and concrete data bindings to MIMIC-IV tables.*
