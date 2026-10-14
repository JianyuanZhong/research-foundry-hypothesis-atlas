> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Scientific Proposal: Pre-Diagnosis Liver Function Reserve Predicts Hepatocellular Carcinoma Progression

## Unresolved Question

**Does pre-diagnosis liver function reserve (measured by baseline albumin, bilirubin, and INR) predict disease progression and treatment response in hepatocellular carcinoma, beyond what is captured by established scoring systems like Child-Pugh or MELD?**

## Background and Rationale

The HCC dataset contains longitudinal laboratory measurements, diagnoses, and treatment records for patients with liver disease. Current clinical practice relies on composite scores (Child-Pugh, MELD) to stratify patients and guide treatment decisions. However, these scores may not fully capture the dynamic nature of liver function reserve during disease progression.

Recent literature suggests that individual liver function markers may outperform composite scores for predicting outcomes [K1]. The key unresolved question is whether baseline liver function markers (albumin, bilirubin, INR) measured before diagnosis can predict:
1. Disease progression patterns (tumor growth, complications)
2. Treatment response (response to ablation, surgery, or systemic therapy)
3. Overall survival outcomes

## Clinical Importance

1. **Personalized treatment stratification:** Identifying patients at risk of poor outcomes based on baseline liver function markers could guide treatment selection (e.g., surgery vs. ablation) before diagnosis is confirmed.

2. **Mechanistic insight:** Distinguishing between composite scores that capture overall liver reserve vs. specific markers that predict treatment response could lead to improved prognostic models.

3. **Resource optimization:** Early identification of patients who may benefit from more aggressive monitoring or intervention could reduce healthcare costs and improve outcomes.

## Data Bindings

- **Population:** Patients with HCC diagnosis in the HCC dataset
- **Exposure:** Pre-diagnosis liver function markers (albumin, bilirubin, INR) from the `labs` table
- **Outcome:** Disease progression (from `diagnoses` table) and treatment response (from `clinical_documents` and `procedures` tables)
- **Covariates:** Patient demographics (from `encounters` table), comorbidities, treatment type

## Baseline Methods

- Logistic regression for binary outcomes (progression vs. no progression)
- Cox proportional hazards models for time-to-event outcomes
- Multivariate analysis adjusting for confounders

## Alternative Methods

- Mixed-effects models for longitudinal data
- Gradient boosting classifiers for prediction
- Machine learning models with feature importance analysis

## Key References

[K1] Individual liver function markers outperform composite scores for predicting HCC outcomes
[K2] Child-Pugh/MELD score limitations in predicting treatment response
[K3] Treatment response prediction models in hepatocellular carcinoma

## Falsification Criteria

The hypothesis will be falsified if:
1. Baseline liver function markers do not significantly predict disease progression after adjusting for composite scores
2. The predictive performance of individual markers is no better than composite scores
3. The markers fail to predict treatment response in multivariate analysis

## Expected Advances

If supported, this study will:
1. Demonstrate that individual liver function markers provide incremental predictive value beyond composite scores
2. Identify specific markers that are most predictive of progression or treatment response
3. Provide evidence for incorporating individual markers into clinical decision-making
