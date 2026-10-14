> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Scientific Proposal: Pre-Diagnosis Liver Function Reserve Predicts Hepatocellular Carcinoma Progression

## Unresolved Question

**Does pre-diagnosis liver function reserve (measured by baseline albumin, bilirubin, and INR) predict disease progression and treatment response in hepatocellular carcinoma, beyond what is captured by established scoring systems like Child-Pugh or MELD?**

## Background and Rationale

The HCC dataset contains longitudinal laboratory measurements, diagnoses, and treatment records for patients with liver disease. Current clinical practice relies on composite scores (Child-Pugh, MELD) to stratify patients and guide treatment decisions. However, these scores may not fully capture the dynamic nature of liver function reserve during disease progression.

Recent literature suggests that individual liver function markers may outperform composite scores for predicting outcomes [K1]. The key unresolved question is whether baseline liver function markers (albumin, bilirubin, INR) measured before diagnosis can predict:
1. Disease progression patterns (tumor growth, complications)
2. Treatment response (response to ablation, surgery, or systemic therapy)
3. Outcomes beyond what Child-Pugh/MELD scores predict

## Clinical Importance

1. **Personalized treatment stratification**: Identifying patients with poor liver function reserve who may need more conservative approaches or earlier intervention.

2. **Treatment response prediction**: Patients with poor reserve may have worse outcomes from aggressive treatments (surgery, TACE).

3. **Dynamic monitoring**: Understanding how liver function changes during disease could inform adaptive treatment strategies.

4. **Model improvement**: The SPHR model from recent literature suggests individual markers may be more suitable than composite scores for certain outcomes [K1].

## Substantive Advance Over Existing Knowledge

Existing research focuses on:
- Child-Pugh/MELD scores as static prognostic tools [K3]
- Treatment outcomes based on established risk stratification
- Single-timepoint assessments of liver function

This proposal advances by:
1. **Temporal dynamics**: Analyzing how baseline liver function relates to longitudinal disease trajectory, not just binary outcomes [K2].
2. **Marker specificity**: Testing whether individual markers (albumin, bilirubin, INR) have independent predictive value beyond composite scores.
3. **Treatment interaction**: Examining how liver function reserve modifies treatment response.

## Study Population and Data Bindings

**Population**: Patients in HCC dataset with:
- Documented liver disease diagnoses
- Multiple laboratory measurements before diagnosis
- Follow-up data (diagnoses, treatments, outcomes)

**Data Tables** (HCC dataset):
- `diagnoses`: For identifying HCC patients and liver disease diagnoses
  - Column: `诊断名称` (Diagnosis name)
  - Column: `诊断类型` (Diagnosis type)

- `labs`: For laboratory measurements
  - Column: `定量结果` (Quantitative result) - for albumin, bilirubin, INR values
  - Column: `标准类型` (Standard type) - for lab test types

- `clinical_documents`: For treatment information and outcomes
  - Column: `手术名称` (Surgery name)
  - Column: `入院诊断` (Admission diagnosis)
  - Column: `出院诊断` (Discharge diagnosis)

- `orders`: For treatment interventions
  - Column: `开始时间` (Start time)
  - Column: `结束时间` (End time)

- `encounters`: For patient demographics
  - Column: `年龄` (Age)
  - Column: `性别` (Gender)

**Key Variables**:
- Baseline liver function: Albumin, Total Bilirubin, INR (from `labs` table, `定量结果` column)
- Diagnosis: HCC diagnosis code (from `diagnoses` table, `诊断名称` column)
- Treatment: Surgery/intervention types (from `clinical_documents` or `procedures` tables)
- Outcomes: Survival, disease progression, treatment response (from `clinical_documents`, `diagnoses`)

## Baseline Methods

1. **Logistic Regression**: Predicting binary outcomes (survival vs. progression) using baseline liver function markers.

2. **Cox Proportional Hazards**: Time-to-event analysis of disease progression or death.

3. **Child-Pugh Score Calculation**: Using albumin, bilirubin, INR, and other standard variables to create a traditional score.

## Alternative Methods

1. **Mixed-effects models**: Accounting for longitudinal measurements and patient-level random effects.

2. **Gradient Boosting (XGBoost/LightGBM)**: Non-parametric approach to capture non-linear relationships.

3. **Survival Forests**: Tree-based survival analysis that can handle censored data.

## Falsification Criteria

The hypothesis would be **falsified** if:
- Baseline liver function markers show no significant association with outcomes after adjusting for confounders.
- Child-Pugh/MELD scores perform equally or better than individual markers.
- No interaction between liver function and treatment response.

The hypothesis would be **supported** if:
- Individual markers predict outcomes independently of composite scores.
- Baseline markers predict disease trajectory patterns (not just binary outcomes).
- Liver function reserve modifies treatment response.

The hypothesis would be **inconclusive** if:
- Sample size is insufficient for robust statistical power.
- Key variables (e.g., complete lab measurements, accurate diagnosis) are missing.
- Temporal patterns cannot be established due to sparse follow-up.

## Required Data Quality

1. **Complete lab measurements**: Albumin, bilirubin, INR must be available for a meaningful subset of patients.
2. **Accurate diagnosis**: Clear identification of HCC vs. other liver diseases.
3. **Temporal ordering**: Lab measurements must precede diagnosis/treatment.
4. **Follow-up data**: Sufficient outcome information (survival, treatment response).

## Missing Evidence

1. **Complete lab panels**: Not all patients may have all required lab measurements.
2. **Imaging data**: Tumor size and stage information may be limited.
3. **Genetic/molecular data**: Not available in this dataset.
4. **External validation**: No independent cohort for validation.

## Computation Budget

- **CPU**: ~4 cores for data processing and model training
- **Memory**: 16-32 GB for handling longitudinal data
- **Time**: 2-4 hours for full analysis
- **GPU**: Not required (tabular analysis)

## Expected Deliverables

1. Descriptive statistics of liver function markers in HCC patients.
2. Baseline prediction models (logistic/Cox regression).
3. Alternative model comparisons.
4. Visualization of disease trajectories by liver function reserve.
5. Assessment of whether baseline markers predict trajectory patterns.

## Key References

- [K1] Wang P, Moses AS, Li C, Chen S, Qi X, Xu K, Shao HB, Han XJ. "Prognosis factors of predicting survival in spontaneously ruptured hepatocellular carcinoma." Hepatology International. 2022;16(6):1330-1338. DOI: 10.1007/s12072-022-10403-x. PMID: 36002714.
  - Key finding: Individual markers (INR, bilirubin, albumin) predict survival; SPHR model AUC=0.925 vs MELD AUC=0.767, Child-Pugh AUC=0.757.

- [K2] Goncalves C, et al. "Human acute inflammatory recovery is defined by co-regulatory dynamics of white blood cell and platelet populations." Nature Communications. 2022. DOI: 10.1038/s41467-022-32222-2.
  - Key concept: Temporal recovery dynamics distinguish different recovery trajectories.

- [K3] Angermayr B, Cejna M, Karnel F, et al. "Child-Pugh versus MELD score in predicting survival in patients undergoing transjugular intrahepatic portosystemic shunt." Gut. 2003;52(6):879-885. DOI: 10.1136/gut.52.6.879.
  - Key concept: Child-Pugh and MELD are established composite scores for liver function assessment.

## Supporting Evidence Files

- work/k1_excerpt.txt - Full excerpt of K1 paper
- work/k2_excerpt.txt - Full excerpt of K2 paper
- work/k3_excerpt.txt - Full excerpt of K3 paper
- work/key-references.json - Structured reference metadata

## Next Steps

1. **Data exploration**: Inspect lab tables for albumin, bilirubin, INR availability in Chinese column names.
2. **Diagnosis coding**: Map diagnoses to HCC and liver disease using `诊断名称` and `诊断类型`.
3. **Patient selection**: Identify patients with complete baseline labs and follow-up data.
4. **Model fitting**: Train baseline and alternative models.
5. **Validation**: Internal validation (cross-validation) and comparison of models.
