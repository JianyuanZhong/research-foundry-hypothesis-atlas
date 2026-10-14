> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Hypothesis: Longitudinal Metabolic Deterioration Predicts Multimorbidity Risk Beyond Baseline Levels

## Scientific Question

**Among UK Biobank participants with repeated metabolic measurements, does the extent of deterioration in metabolic biomarkers between two measurement timepoints provide additional information about risk of cardiovascular and kidney multimorbidity beyond their current disease levels?**

Specifically, we test whether:
1. Participants showing greater deterioration in metabolic measures (e.g., increasing lipids, decreasing kidney function markers, worsening glucose metabolism) have higher risk of developing multimorbidity (CVD + CKD, CVD + T2D, or all three) compared to those with stable or improving metabolic profiles
2. This deterioration-based risk signal is independent of baseline disease status and traditional risk factors
3. A deterioration-adjusted risk score outperforms baseline-only risk scores in predicting multimorbidity progression

## Background and Rationale

### Existing Knowledge

Recent work in UK Biobank has demonstrated that biological aging and metabolic deterioration are strong predictors of cardio-renal-metabolic (CRM) comorbidity. However, a critical unresolved question remains:

**Does the *trajectory* of metabolic deterioration provide incremental predictive value beyond current disease status?**

Three key studies demonstrate the state-of-the-art in this domain:

1. **Lin et al. (2025) [K1]**: "Biological aging predicts progression to cardio-renal-metabolic comorbidity in UK Biobank" - demonstrated that proteomic aging clocks strongly predict CRM progression, but treated progression as a homogeneous endpoint without examining whether deterioration trajectories differ by multimorbidity pattern.

2. **ALADYNOULLI [K2]**: A Bayesian framework that jointly models longitudinal EHRs with germline genetics to identify disease signatures. While this work captures temporal dynamics, it focuses on single-disease prediction and does not explicitly test whether deterioration trajectories predict multimorbidity patterns.

3. **Oncoformer [K3]**: A transformer model for disease trajectory prediction that captures temporal dependencies. However, like Delphi-2M, it treats diseases in isolation and does not examine whether deterioration-based signals are particularly informative for multimorbidity progression.

### Unresolved Question

The critical unresolved question is: **Do longitudinal changes in metabolic biomarkers provide risk information that is distinct from, and potentially superior to, baseline disease status when predicting multimorbidity progression?**

This question matters because:
- Current risk prediction models primarily use baseline characteristics
- Early detection of metabolic deterioration could enable preventive interventions before disease onset
- Multimorbidity patterns may require different risk factors than single-disease progression
- Understanding whether deterioration trajectories are informative could guide dynamic risk assessment strategies

## Clinical Importance

1. **Preventive Medicine**: Identifying individuals at risk of developing multimorbidity based on metabolic deterioration could enable earlier interventions before disease onset.

2. **Risk Stratification**: Deterioration-based risk scores could complement traditional baseline risk scores, potentially improving prediction accuracy for high-risk individuals.

3. **Multimorbidity Understanding**: Examining whether specific deterioration patterns predict particular multimorbidity combinations (e.g., CVD+CKD vs CVD+T2D) could reveal biological mechanisms underlying comorbidity clustering.

4. **Dynamic Risk Assessment**: Establishing whether longitudinal changes provide incremental value supports development of dynamic risk models that update predictions as new data becomes available.

## Study Population

- **Source**: UK Biobank (ukb dataset)
- **Population**: Participants with at least two metabolic measurements separated by ≥6 months, with incident CVD, CKD, or T2D during follow-up
- **Inclusion Criteria**:
  - Age ≥40 at first metabolic measurement
  - At least two valid metabolic measurements
  - Follow-up duration ≥6 months between measurements
  - Incident CVD, CKD, or T2D during follow-up after second measurement
- **Exclusion Criteria**:
  - Pre-existing CVD, CKD, or T2D at first measurement
  - Missing key metabolic variables
  - Follow-up duration <6 months between measurements

## Main Data and Table Bindings

### Primary Tables

1. **health_outcomes** (`table-3cfae45e0905b0e3.json`)
   - Columns: `eid`, disease-specific outcome columns (e.g., `27980-0.0`, `27981-0.0`, etc.)
   - Use: Define incident CVD, CKD, and T2D outcomes
   - Join key: `eid`

2. **additional_exposures** (`table-099f610bfb23a632.json`)
   - Columns: `eid`, biomarker measurements (e.g., `21100-0.0`, `22700-0.0`, etc.)
   - Use: Extract metabolic biomarkers (lipids, kidney function, glucose)
   - Join key: `eid`

3. **population** (`table-38565c9e35e7cb6c.json`)
   - Columns: `eid`, baseline demographics (age, sex, ethnicity)
   - Use: Covariates for adjustment
   - Join key: `eid`

### Key Variables

**Metabolic Biomarkers** (from additional_exposures):
- Lipid panel: LDL-C, HDL-C, triglycerides, total cholesterol
- Kidney function: eGFR, cystatin C
- Glucose metabolism: fasting glucose, HbA1c
- Inflammatory markers: CRP, IL-6 (if available)

**Disease Outcomes** (from health_outcomes):
- Cardiovascular disease (CVD): MI, stroke, heart failure, peripheral artery disease
- Chronic kidney disease (CKD): eGFR <60, dialysis, kidney transplantation
- Type 2 diabetes (T2D): Diabetes diagnosis, medication initiation

**Deterioration Metrics** (derived):
- Change in each biomarker between measurement 1 and 2
- Composite deterioration score (e.g., z-score of changes)
- Deterioration trajectory classification (improving, stable, deteriorating)

## Suggested Approach

### Step 1: Data Preparation
1. Filter participants with ≥2 metabolic measurements ≥6 months apart
2. Define measurement timepoints (T0 = first measurement, T1 = second measurement)
3. Calculate biomarker changes: ΔBiomarker = Biomarker_T1 - Biomarker_T0
4. Define incident disease as first occurrence after T1
5. Classify multimorbidity patterns:
   - Single disease: CVD-only, CKD-only, T2D-only
   - Dual disease: CVD+CKD, CVD+T2D, CKD+T2D
   - Triple disease: CVD+CKD+T2D

### Step 2: Baseline Risk Modeling
1. Fit traditional risk models using baseline characteristics (age, sex, BMI, baseline biomarkers)
2. Evaluate prediction performance using AUROC and C-index
3. Use Cox proportional hazards regression with time-to-first-event outcome

### Step 3: Deterioration-Based Modeling
1. Develop deterioration-adjusted risk scores:
   - Simple: Baseline risk + deterioration score
   - Complex: Machine learning model using both baseline and deterioration features
2. Fit Cox models with deterioration-adjusted predictors
3. Evaluate prediction performance

### Step 4: Comparative Analysis
1. Compare AUROC and C-index between baseline-only and deterioration-adjusted models
2. Test if deterioration signal is independent of baseline status (interaction terms)
3. Examine whether deterioration predicts multimorbidity patterns differently than single disease

### Step 5: Sensitivity Analyses
1. Adjust for reverse causation (exclude participants with disease symptoms before T0)
2. Test robustness to different time windows
3. Stratify by genetic risk (if polygenic risk scores available)

## Scientific Significance

This study addresses a critical gap in longitudinal disease prediction: **whether temporal changes in biomarkers provide risk information distinct from baseline status for multimorbidity progression.**

If the hypothesis is supported, it would:
1. Establish that deterioration trajectories are informative for multimorbidity risk
2. Support development of dynamic risk assessment tools
3. Identify biomarker patterns that precede multimorbidity onset
4. Inform preventive strategies targeting metabolic deterioration

## Main Limitations

1. **Reverse Causation**: Metabolic deterioration may be partly driven by early undiagnosed disease
2. **Measurement Frequency**: Two measurements may not capture true trajectory
3. **Missing Data**: Not all participants have complete biomarker panels
4. **Generalizability**: UK Biobank participants may not represent all populations
5. **Treatment Effects**: Disease-modifying treatments may alter biomarker trajectories

## Key References

The proposal requires three key references with proper claim mappings. Based on the domain, the following three works are most relevant:

1. **Lin et al. (2025)** - Biological aging and CRM comorbidity in UK Biobank
2. **ALADYNOULLI** - Bayesian framework for longitudinal EHR and genetic discovery
3. **Oncoformer** - Transformer model for disease trajectory prediction

These references will be attached as inspected source excerpts with proper claim mappings in the key-references.json file.

## Method Comparison

This proposal includes a substantive method comparison:

**Baseline Method**: Traditional Cox proportional hazards regression with baseline characteristics only
- Represents current state-of-the-art for static risk prediction
- Uses established risk factors (age, sex, baseline biomarkers)

**Alternative Method**: Deterioration-adjusted risk modeling
- Incorporates longitudinal changes in biomarkers
- Tests whether temporal dynamics provide incremental value
- May use machine learning for non-linear deterioration patterns

**What the Alternative Could Reveal**:
- Whether deterioration trajectories are independent risk signals
- Whether specific biomarker changes predict particular multimorbidity patterns
- Whether dynamic risk assessment improves over static models
- The clinical utility of monitoring metabolic changes for early intervention

## Falsification Criteria

The hypothesis will be considered falsified if:
1. Deterioration-adjusted models show no improvement over baseline-only models (AUROC difference <0.01)
2. Deterioration signal is fully explained by baseline status (no significant interaction terms)
3. Deterioration patterns are random with respect to multimorbidity outcomes
4. Sensitivity analyses show results are driven by reverse causation or measurement artifacts

## Computational Requirements

- **Dataset**: UK Biobank (ukb dataset, ~581M rows in main file)
- **Tables**: health_outcomes, additional_exposures, population
- **Join key**: eid (participant ID)
- **Analysis**: Python with pandas, scikit-learn, lifelines
- **GPU**: Not required (tabular analysis on CPU)
- **Time budget**: ≤3600 seconds for full analysis

## Next Steps

1. Inspect table schemas to confirm available variables
2. Verify biomarker and disease outcome columns
3. Develop data cleaning and preprocessing pipeline
4. Implement baseline and deterioration models
5. Perform comparative analysis
6. Generate results and interpret clinical significance

## Evidence Requirements

- **Key references**: Three inspected works with proper claim mappings (Lin et al., ALADYNOULLI, Oncoformer)
- **Data bindings**: Concrete table names, columns, and join keys
- **Results**: AUROC, C-index, hazard ratios for deterioration signal
- **Sensitivity analyses**: Reverse causation adjustment, time-window robustness
