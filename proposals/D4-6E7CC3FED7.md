> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Bone-muscle discordance and incident fracture risk: a two-pathway design without residualization

## Scientific question and clinical importance

Among UK Biobank participants aged ≥50 with valid DXA BMD and grip strength, does low grip strength predict incident fracture risk independently of BMD, and does this excess risk differ by baseline fall history?

The clinically consequential unresolved question is whether low BMD and low grip strength represent a single latent frailty process (where muscle weakness is merely a marker of overall biological ageing) or two separable pathways: (1) bone fragility driving fracture independent of muscle, and (2) muscle weakness driving falls that then cause fracture. This distinction has direct implications for screening and prevention: if the two pathways are separable, then dual anti-resorptive + resistance-exercise interventions would be more effective than bone-targeted therapy alone for the discordant subgroup.

The leading explanation (single latent process) is that low BMD and low grip strength are both downstream of a shared ageing/frailty trajectory, so grip strength adds no independent fracture risk beyond what BMD alone predicts after adjustment for age, sex, BMI, and metabolic covariates. The strongest rival is the two-pathway model: muscle weakness independently drives falls (and thus fractures) through a mechanism that is not captured by BMD, so the BMD × grip-strength interaction should be positive and significant after full adjustment.

## Key references

- [K1] Wang W, Zhen J, Zhu X. Joint association of low bone mass and reduced relative handgrip strength with fragility fracture risk in adults aged 50–59 years: A cross-sectional study from NHANES 2013–2014. Medicine (Baltimore). 2026. doi:10.1097/MD.0000000000049483. — Supports the joint association of low BMD and low grip strength with fragility fracture (OR 3.09, 95% CI 1.13–8.45), but is cross-sectional with only 77 fracture events and wide confidence intervals; cannot establish prospective independence or causal separability.
- [K2] Schousboe JT, et al. Dementia and musculoskeletal health: associations with bone fragility, functional trajectories, and probable sarcopenia in UK Biobank. Frontiers in Medicine. 2026. doi:10.3389/fmed.2026.1883046. — Bounds the single-latent-process rival by showing dementia-associated bone fragility, grip-strength decline, and probable sarcopenia co-occur in UK Biobank (n=151,751); however, the primary exposure is dementia, not the BMD × grip-strength interaction, so it does not test the two-pathway hypothesis directly.
- [K3] Morley JE, et al. Integrating frailty and sarcopenia into fragility fracture prevention: a bone–muscle–function framework. Frontiers in Medicine. 2026. doi:10.3389/fmed.2026.1881899. — Supports the conceptual framework of separable skeletal and muscle pathways in fracture prevention; the cited UKB sarcopenia-fracture HR (1.30) is from a different study and is not independently verified here. This is a perspective/review, not an original cohort study.

## Population and temporal boundaries

- **Population**: UK Biobank participants aged ≥50 at baseline with valid DXA BMD (field 23204, femoral neck or total hip) and grip strength (field 23208, mean of two measurements).
- **Exclusion**: Baseline fracture (ICD-10 codes for fracture in field 41270), missing BMD or grip strength, age <50.
- **Temporal ordering**: BMD and grip strength measured at baseline assessment (field 53, date of attending assessment centre). Incident fracture defined as first in-patient fracture diagnosis (field 41270, ICD-10 codes for fracture) occurring after baseline, with date from field 41280 (date of first in-patient diagnosis). Follow-up from baseline to first fracture, death, or end of follow-up.
- **Fall history**: Baseline self-reported fall in the past year (field 2296) used as a stratification variable, not a time-varying covariate.

## Variables and exact UKB bindings

| Variable | UKB Field | Description |
|----------|-----------|-------------|
| BMD | 23204 | DXA BMD (femoral neck or total hip), g/cm² |
| Grip strength | 23208 | Handgrip strength, mean of two measurements, kg |
| Age | 34 | Age at baseline, years |
| Sex | 31 | Self-reported sex |
| BMI | 40 | Body mass index, kg/m² |
| Fall history | 2296 | Falls in past year (yes/no) |
| Fracture (outcome) | 41270 | ICD-10 codes for fracture |
| Fracture date | 41280 | Date of first in-patient diagnosis |
| Assessment date | 53 | Date of attending assessment centre |
| Ethnicity | 52 | Ethnic category |
| Smoking | 1200 | Smoking status |
| Physical activity | 798 | Physical activity level |
| Diabetes | 48 | Self-reported diabetes |
| Hypertension | 48 | Self-reported hypertension |

## Estimand

The primary estimand is the **direct BMD × grip-strength interaction coefficient** in a Cox proportional hazards model for incident fracture. Specifically:

- **Primary model**: Cox regression with incident fracture as the outcome, BMD (continuous, per 1 SD) and grip strength (continuous, per 1 SD) as main effects, and their product term BMD × grip strength as the interaction.
- **Interpretation**: A positive and significant interaction coefficient indicates that the fracture risk associated with low grip strength is greater among those with low BMD (or vice versa), supporting the two-pathway model. A null interaction supports the single-latent-process explanation.
- **Why not residualization**: Residualizing grip strength on BMD (as in the parent candidate) can induce collider bias if BMD and grip strength share unmeasured confounders. The direct interaction model avoids this problem by estimating the joint effect without conditioning on a derived variable.

## Adjustment hierarchy

| Model | Adjustments | Purpose |
|-------|-------------|---------|
| Model 0 | Unadjusted | Crude association |
| Model 1 | Age, sex | Demographic adjustment |
| Model 2 | Model 1 + BMI, ethnicity, smoking, physical activity | Lifestyle adjustment |
| Model 3 | Model 2 + diabetes, hypertension | Metabolic adjustment |
| Model 4 | Model 3 + BMD × grip strength interaction | Primary estimand |

Sensitivity analysis: stratify by baseline fall history (field 2296) to examine whether the interaction differs in those with vs. without prior falls. This is a sensitivity analysis, not a causal mediation analysis.

## Baseline and learned alternative

### Baseline: Cox proportional hazards

- **Fit**: Cox regression with BMD, grip strength, and their interaction as predictors, with the adjustment hierarchy above.
- **Evaluation**: Hazard ratio for the interaction term with 95% CI; proportional hazards assumption checked with Schoenfeld residuals.
- **Resource**: CPU-feasible; ~50,000–100,000 participants with valid BMD and grip strength; Cox fit in <10 minutes on 4 CPUs.

### Learned alternative: Gradient-boosted survival model

- **Fit**: XGBoost survival model (or equivalent gradient-boosted Cox) with BMD, grip strength, and their interaction as features, plus the same adjustment covariates.
- **Evaluation**: Held-out C-index (time-dependent) compared to the Cox model. A C-index improvement >0.01 over the Cox model with a significant partial dependence for the interaction term would support non-linear or higher-order effects not captured by the Cox model.
- **Resource**: CPU-feasible; XGBoost survival fit in <30 minutes on 4 CPUs with 100,000 participants.
- **What it reveals**: The Cox model assumes a linear log-hazard effect and proportional hazards. The gradient-boosted model can capture non-linear BMD × grip-strength interactions and time-varying effects. If the gradient-boosted model shows a significant interaction that the Cox model misses, this would suggest the two-pathway effect is non-linear or time-dependent.

## Falsification criteria

The two-pathway hypothesis is **not supported** if:
1. The BMD × grip-strength interaction coefficient is non-significant (p > 0.05) in Model 4 after full adjustment.
2. The gradient-boosted model shows no held-out C-index improvement >0.01 over the Cox model.
3. The interaction is driven by a small number of extreme BMD or grip-strength values (sensitivity analysis with winsorization at 1st/99th percentiles).

The two-pathway hypothesis is **supported** if:
1. The interaction coefficient is positive and significant (p < 0.05) in Model 4.
2. The gradient-boosted model shows a C-index improvement >0.01 with a significant partial dependence for the interaction.
3. The result is robust to winsorization and stratification by fall history.

## Supportive, adverse, and inconclusive outcomes

- **Supportive**: Significant positive BMD × grip-strength interaction after full adjustment, with C-index improvement from the gradient-boosted model. This would support the two-pathway model and motivate dual anti-resorptive + resistance-exercise interventions for the discordant subgroup.
- **Adverse**: Null or negative interaction after full adjustment. This would support the single-latent-process explanation and suggest that BMD alone is sufficient for fracture risk stratification.
- **Inconclusive**: Interaction is marginally significant (0.05 < p < 0.10) or the C-index improvement is small (<0.01). This would warrant a larger study or a different design (e.g., longitudinal BMD and grip strength measurements).

## What this experiment does and does not establish

- **Establishes**: Whether low grip strength predicts incident fracture risk independently of BMD, and whether the BMD × grip-strength interaction is significant after adjustment for age, sex, BMI, lifestyle, and metabolic covariates.
- **Does not establish**: Causality. The association may reflect residual confounding by shared metabolic ageing, reverse causation (early subclinical fracture affecting grip strength), or measurement error. A causal interpretation would require a prospective cohort with repeated measurements or a randomized intervention.
- **Requires additional data for**: Longitudinal BMD and grip strength measurements to establish temporal ordering; genetic instruments for a Mendelian randomization analysis; external validation in an independent cohort.

## Compute and delivery

- **Discovery**: CPU-only; Cox fit and XGBoost survival fit on 4 CPUs, <1 hour total.
- **Solver envelope**: CPU-feasible; no GPU required. The solver must fit the Cox model and the gradient-boosted survival model, evaluate held-out C-index, and report the interaction coefficient with 95% CI.
- **Deliverable**: A fitted Cox model and gradient-boosted survival model, with the interaction coefficient, C-index comparison, and partial dependence plots.
