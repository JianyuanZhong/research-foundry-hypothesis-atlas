> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Hypothesis Proposal: Pre-TACE Tumor Imaging Characteristics Predict Treatment Response Beyond Clinical Markers

## Unresolved Question

**Primary Question:** Do pre-TACE tumor characteristics extracted from imaging examination reports (tumor size, vascular invasion patterns, satellite nodules, heterogeneity indicators) predict treatment response (progression-free survival, recurrence-free survival) and treatment-related complications better than, or in addition to, standard clinical markers (Child-Pugh score, serum biomarkers)?

**Secondary Question:** Is there a specific imaging phenotype (e.g., vascular invasion pattern, tumor heterogeneity) that identifies patients who will have durable responses to TACE versus those who will relapse early, independent of tumor burden and liver function?

## Clinical Importance

1. **Treatment Selection Optimization**: Current HCC treatment guidelines rely heavily on Child-Pugh score and tumor burden (BCLC staging), but these may not accurately predict individual treatment response. Identifying patients with specific imaging phenotypes could guide treatment selection between TACE, radiofrequency ablation, systemic therapy, or transplant evaluation.

2. **Early Relapse Prediction**: Patients with specific imaging characteristics (e.g., vascular invasion, satellite nodules) may be at high risk of early recurrence despite appearing to have good baseline liver function. Early identification could trigger intensified surveillance or alternative therapies.

3. **Clinical Decision Support**: Radiologists and hepatologists may not routinely integrate imaging phenotype assessment into treatment decisions. This study would provide evidence for incorporating imaging-derived prognostic information into clinical workflows.

4. **Understanding Treatment Mechanisms**: If certain imaging features predict response, this could inform understanding of TACE mechanism (e.g., vascular invasion patterns affecting embolization efficacy).

## Substantive Advance Over Existing Knowledge

**Existing Literature:**
- **Child-Pugh score**: Captures liver synthetic function but not tumor biology or imaging features [K1]
- **Tumor burden**: Measured by size/number but may not capture heterogeneity or vascular invasion
- **Serum biomarkers**: AFP, bilirubin, albumin, INR - but these are indirect measures of disease activity

**What This Study Adds:**
- **Imaging phenotype as a distinct prognostic domain**: Unlike prior work focusing on clinical/laboratory markers, this explores tumor imaging characteristics as an independent prognostic domain. Evidence from Zhao et al. [K1] demonstrates that portal vein tumor thrombosis (PVTT) - an imaging-derived feature - has strong prognostic value after TACE (median OS 16.9 vs 6.1 months without vs with PVTT, P<0.001).
- **Integration of multimodal data**: Combines imaging reports with clinical and laboratory data to test whether imaging features add predictive value. Recent evidence from Jin et al. [K3] shows that radiomic features representing tumor heterogeneity can predict TACE response with high accuracy (AUC 0.94 training, 0.82 internal validation, 0.83 test set).
- **Specific imaging features**: Examines concrete imaging descriptors (vascular invasion, satellite nodules, heterogeneity) rather than generic "tumor characteristics". This specificity allows for clinical translation and mechanistic interpretation.
- **Temporal dynamics**: Can examine how imaging features at treatment initiation predict both short-term response and long-term outcomes.
- **Methodological approach**: Uses gradient boosting to capture non-linear relationships and interactions between imaging features and clinical markers, going beyond linear models that may miss important feature interactions.

**Key References Supporting the Hypothesis:**

[K1] Zhao et al. (2016) "Transarterial Chemoembolization for the Treatment of Advanced-Stage Hepatocellular Carcinoma" - Demonstrates that portal vein tumor thrombosis (PVTT) is a strong independent predictor of poor survival after TACE (median OS 16.9 vs 6.1 months without vs with PVTT, P<0.001), providing direct evidence that vascular invasion patterns are important prognostic factors.

[K2] Chang et al. (2020) "Recent Updates of Transarterial Chemoembolization in Hepatocellular Carcinoma" - Review article noting that new prognostic models including radiomics and deep learning are being developed to predict TACE outcomes, suggesting imaging-derived biomarkers may improve upon traditional clinical staging.

[K3] Jin et al. (2025) "Decoding tumor heterogeneity with imaging biomarkers predicts response to TACE plus immunotherapy and targeted therapy in HCC (CHANCE2204)" - Recent evidence that radiomic features representing tumor heterogeneity can predict TACE response with high accuracy (AUC 0.94 training, 0.82 internal validation, 0.83 test set), supporting the hypothesis that imaging-derived features have independent prognostic value.

## Data Bindings

### Primary Data Sources

1. **examinations table** (`HCC/data_\u68c0\u67e5_4203595081195465282.csv`)
   - Source ID: `table-fd016d2731b9d6c6.json`
   - Key columns:
     - `\u60a3\u8005\u4e3b\u7d22\u5f15` (patient_id) - join key
     - `\u5c31\u8bca\u53f7` (encounter_id) - join key
     - `\u68c0\u67e5` (examination_type) - filter for imaging (CT, MRI, etc.)
     - `\u68c0\u67e5\u6240\u89c1` (findings_text) - rich text with tumor descriptions
     - `\u68c0\u67e5\u8bca\u65ad` (diagnosis) - imaging diagnosis
     - `\u5f00\u59cb\u65f6\u95f4` (start_time) - temporal anchor
     - `\u673c\u5668\u578b\u53f7` (machine_type) - scanner type

2. **procedures table** (`HCC/data_\u624b\u672f_8024330590283626027.csv`)
   - Source ID: `table-d5eae16f8f8093d9.json`
   - Key columns:
     - `\u60a3\u8005\u4e3b\u7d22\u5f15` (patient_id) - join key
     - `\u5c31\u8bca\u53f7` (encounter_id) - join key
     - `\u624b\u672f` (procedure_name) - filter for "TACE"
     - `\u5f00\u59cb\u65f6\u95f4` (start_time) - treatment timestamp

3. **diagnoses table** (`HCC/data_\u8bca\u65ad_7504718184492840569.csv`)
   - Source ID: `table-12710723c3df0c99.json`
   - Key columns:
     - `\u60a3\u8005\u4e3b\u7d22\u5f15` (patient_id) - join key
     - `\u5c31\u8bca\u53f7` (encounter_id) - join key
     - `\u8bca\u65ad\u540d\u79f7` (diagnosis_name) - outcome indicators (recurrence, progression, etc.)
     - `\u8bca\u65ad\u7c7b\u578b` (diagnosis_type) - inpatient diagnosis

4. **labs table** (`HCC/data_\u68c0\u9a8c_609065997844652188.csv`)
   - Source ID: `table-38aad8c54471332f.json`
   - Key columns:
     - `\u60a3\u8005\u4e3b\u7d22\u5f15` (patient_id) - join key
     - `\u5c31\u8bca\u53f7` (encounter_id) - join key
     - `\u68c0\u9a8c` (test_name) - Child-Pugh components (bilirubin, albumin, INR)
     - `\u5b9a\u6027\u7ed3\u679c` (qualitative_result) - lab results
     - `\u68c0\u9a8c\u65f6\u95f4` (test_time) - temporal anchor

### Temporal Boundaries
- **Index time**: Pre-TACE imaging examination (within 30 days before TACE procedure)
- **Treatment time**: TACE procedure start time
- **Follow-up**: All diagnoses after TACE (recurrence, progression, death)
- **Outcome definition**: Time from TACE to first recurrence/progression/death

### Key Variables to Extract from Imaging Text

From `\u68c0\u67e5\u6240\u89c1` (findings_text), extract:
1. **Tumor size** (cm) - multiple measurements per tumor
2. **Number of tumors** - single vs. multiple lesions
3. **Vascular invasion** - portal vein, hepatic vein, tumor thrombus
4. **Satellite nodules** - presence/number of satellite lesions
5. **Heterogeneity indicators** - heterogeneous enhancement, necrosis, hemorrhage
6. **Extrahepatic spread** - distant metastasis, lymph node involvement
7. **Liver parenchyma** - cirrhosis, fibrosis, nodular regeneration

### Outcome Variables

1. **Primary outcome**: Progression-free survival (PFS) - time from TACE to first progression/recurrence
2. **Secondary outcomes**:
   - Recurrence-free survival (RFS)
   - Time to first hospitalization
   - Time to death
   - Decompensation events (jaundice, ascites, coagulopathy)

## Baseline Method

**Baseline Model**: Cox proportional hazards regression with:
- Covariates: Child-Pugh score (derived from bilirubin, albumin, INR from labs)
- Covariates: Tumor burden (tumor count, maximum diameter from imaging)
- Outcome: Time to recurrence/progression

**Rationale**: This represents current clinical practice - using liver function and tumor burden to predict outcomes.

## Learned/Mechanical Alternative

**Advanced Model**: Gradient Boosted Trees (XGBoost/LightGBM) with:
- Features: All Child-Pugh components + tumor burden + extracted imaging features
- Features: Interaction terms (e.g., tumor size \u00d7 Child-Pugh class)
- Features: Non-linear transformations (e.g., log(tumor size), tumor heterogeneity score)
- Outcome: Time to recurrence/progression

**What This Could Reveal**:
- Whether imaging features have independent predictive value beyond tumor burden
- Whether specific imaging phenotypes (vascular invasion patterns) are stronger predictors than size alone
- Whether interactions between liver function and imaging features matter (e.g., small tumors with vascular invasion may be worse than large tumors without)
- Whether a "tumor biology score" derived from imaging adds value to clinical staging

## Falsification Criteria

The hypothesis would be **falsified** if:
1. Imaging features (after adjusting for tumor burden) do not improve prediction accuracy (C-index) over baseline
2. No specific imaging phenotype shows consistent association with treatment response
3. All imaging features are fully explained by tumor burden (no independent contribution)
4. The imaging phenotype associations are inconsistent across subgroups (e.g., by Child-Pugh class)

The hypothesis would be **supported** if:
1. Imaging features add statistically significant predictive value (C-index improvement >0.02)
2. At least one imaging phenotype (e.g., vascular invasion, satellite nodules) shows strong, consistent association with recurrence
3. Imaging features predict response in patients with similar tumor burden but different imaging phenotypes
4. The imaging phenotype associations persist after adjusting for liver function and tumor burden

## Expected Clinical Impact

**Supportive Results**:
- Development of an imaging-based risk stratification tool for TACE patients
- Identification of high-risk imaging phenotypes that might warrant alternative therapies
- Potential integration into clinical decision support systems

**Adverse Results**:
- Reinforcement that clinical staging (Child-Pugh + tumor burden) is the most reliable predictor
- Suggests imaging text analysis may not be feasible or valuable for routine use
- Points to need for standardized imaging reporting to extract features

**Inconclusive Results**:
- Some imaging features predictive but sample size insufficient
- Need for external validation in other cohorts
- Technical feasibility issues (text extraction accuracy)

## Missing Evidence / Clinical Adjudication Required

1. **Precise outcome definition**: Need to verify what constitutes "recurrence" vs. "progression" in the diagnoses table
2. **Imaging feature extraction**: Manual extraction of features from text may be error-prone; need validation
3. **Temporal alignment**: Ensuring imaging is truly "pre-TACE" and not post-treatment
4. **External validation**: Results should be validated in an independent cohort
5. **Clinical utility**: Does the model actually change management in practice?

## Resources Required

- **CPU**: ~4-8 hours for data extraction, feature engineering, and model training
- **GPU**: Not required for this analysis (tabular data, tree-based models)
- **Time**: 1-2 days for complete analysis

## Next Steps

1. Validate data bindings by extracting sample records
2. Develop feature extraction pipeline for imaging text
3. Train baseline and advanced models
4. Compare performance metrics (C-index, calibration, decision curve analysis)
5. Perform subgroup analyses by Child-Pugh class, tumor burden, etc.
6. Document limitations and clinical applicability
