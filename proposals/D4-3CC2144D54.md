> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Hypothesis: Discordant Disease Signatures Predict Divergent Cardiovascular-Diabetes Trajectories Better Than Single-Disease Models

## Scientific Question

**Among UK Biobank participants with cardiovascular disease (CVD) or type 2 diabetes (T2D), do latent disease signatures (identifying underlying biological processes) predict progression to divergent outcome trajectories (CVD-only, T2D-only, or comorbid CVD+T2D) more accurately than single-disease prediction models, and do these signatures show differential predictive value by genetic predisposition?**

## Background and Rationale

### Existing Knowledge

Three key studies demonstrate the state-of-the-art in longitudinal disease prediction:

1. **Delphi-2M [K1]**: A transformer-based model trained on 0.4 million UK Biobank participants that predicts rates of 1,000+ diseases, capturing temporal dependencies and comorbidity clusters. However, it treats diseases in isolation and doesn't explicitly integrate genetic information.

2. **ALADYNOULLI [K2]**: A Bayesian framework that jointly models longitudinal EHRs with germline genetics to identify 21 replicable disease signatures. These signatures show high cross-cohort stability and alignment with established disease biology (e.g., familial hypercholesterolaemia enriches in cardiovascular signature). The model correctly accommodates simultaneous and chronic conditions through a mixture-of-probabilities formulation.

3. **Oncoformer [K3]**: A multimodal model for cancer detection using EHRs and imaging, with adversarial training for robustness against missing data and cohort-specific biases. Demonstrates AUROC >0.86 for cancer prediction with 90-day washout.

### Unresolved Question

While ALADYNOULLI identifies latent disease signatures and demonstrates improved prediction over baseline models, three critical gaps remain:

1. **Outcome-specific signature utility**: ALADYNOULLI predicts disease rates but does not explicitly test whether the same signatures provide different predictive value for divergent outcome trajectories (single vs. comorbid disease progression).

2. **Genetic stratification**: The model identifies genetic associations with signatures but does not systematically test whether signature-based prediction improves stratification by genetic risk.

3. **Clinical interpretability**: While signatures are biologically interpretable, their differential utility across outcome trajectories remains untested.

This question is clinically important because:
- **Personalized risk stratification**: Different signature profiles may identify patients at risk for single vs. comorbid progression, enabling tailored prevention strategies.
- **Resource allocation**: Understanding trajectory-specific risks helps prioritize intensive follow-up for high-risk comorbid groups.
- **Mechanistic insight**: Differential signature predictive value may reveal distinct biological pathways driving single vs. comorbid progression.

## Substantive Advance Over Existing Knowledge

This proposal advances beyond ALADYNOULLI by:

1. **Testing trajectory-specific utility**: Rather than treating CVD and T2D as homogeneous endpoints, we explicitly test whether disease signatures provide different predictive value for single vs. comorbid progression.

2. **Integrating genetic stratification**: We systematically test whether signature loadings improve prediction when stratified by polygenic risk scores (PRS).

3. **Comparing against appropriate baselines**: We compare signature-based models against both traditional risk scores (Pooled Cohort Equation, FINDRISC) and single-disease prediction models, isolating the incremental value of latent signature modeling.

## Hypothesis Statements

### Primary Hypothesis
Among UK Biobank participants with baseline CVD or T2D, latent disease signatures predict progression to comorbid CVD+T2D trajectories more accurately than they predict single-disease progression, with signature loadings showing differential associations by polygenic risk score.

### Secondary Hypothesis
A signature-based Cox model outperforms traditional risk scores (PCE, FINDRISC) and single-disease models in predicting 5-year incidence of comorbid CVD+T2D, with improvement driven by signature loadings rather than individual disease history.

## Study Population and Main Data

**Population**: UK Biobank participants (UKB672073) with:
- Baseline diagnosis of CVD (ICD-10 I20-I25) or T2D (ICD-10 E11)
- No prior CVD+T2D comorbidity at baseline
- Follow-up data through 2022 (Online_Follow_up.csv)

**Main Data Sources**:
1. **ukb672073.csv (main table)**:
   - Columns: `eid` (participant ID), disease indicators (3-0.0, 3-1.0, 4-0.0, 4-1.0, 87-0.0, 87-1.0, etc. representing cardiovascular and metabolic diseases)
   - Temporal: Follow-up dates from Online_Follow_up.csv

2. **ukb672073_Biological_Samples.csv**:
   - Proteomic measurements for biomarker extraction

3. **ukb672073_Genomics.csv**:
   - Polygenic risk scores for CVD and T2D

4. **ukb672073_Population_Characteristics.csv**:
   - Age, sex, ethnicity, BMI

## Suggested Approach

### Step 1: Define Outcome Trajectories
- **Single-CVD**: CVD incident only
- **Single-T2D**: T2D incident only
- **Comorbid-CVD+T2D**: Both CVD and T2D incident

### Step 2: Extract Disease Signatures
Using ALADYNOULLI framework (adapted to UKB proteomics and EHR data):
- Identify latent disease signatures from longitudinal EHR diagnoses and proteomic data
- Compute individual signature loadings at baseline and time-varying

### Step 3: Model Building
- **Baseline**: Traditional risk scores (PCE for CVD, FINDRISC for T2D)
- **Single-disease models**: Cox models with individual disease history
- **Signature models**: Cox models with signature loadings as time-varying covariates
- **Stratified models**: Signature models stratified by PRS quartiles

### Step 4: Evaluation Metrics
- AUROC, C-index for discrimination
- Calibration plots
- Brier scores
- Net reclassification improvement (NRI)

### Step 5: Falsification Criteria
Hypothesis is **falsified** if:
- Signature-based models do not outperform single-disease models for comorbid outcomes (C-index difference < 0.01)
- No differential predictive value by PRS (interaction p-value > 0.05)
- Traditional risk scores perform as well as or better than signature models

## Key References

Three key references support this hypothesis:

1. **Delphi-2M** - Demonstrates transformer-based disease prediction with temporal dependencies but lacks genetic integration
2. **ALADYNOULLI** - Provides Bayesian framework for latent disease signatures with genetic integration
3. **Oncoformer** - Shows multimodal prediction with adversarial training for robustness

## Clinical Adjudication Required

This proposal requires:
1. **Expert review of signature interpretation**: Biological plausibility of identified signatures
2. **Clinical validation in external cohort**: Independent validation in Danish registries (as Delphi-2M validated externally)
3. **Mechanistic studies**: Experimental validation of signature-associated biological pathways

## Missing Evidence

- Full ALADYNOULLI implementation details for UKB proteomics adaptation
- External validation of signature trajectories
- Prospective clinical trial data for intervention testing
