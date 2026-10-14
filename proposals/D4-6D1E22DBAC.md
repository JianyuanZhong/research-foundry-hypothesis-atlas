> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Bone-muscle discordance and incident fracture risk: a two-pathway design without residualization

## Scientific question and clinical importance

Among UK Biobank participants aged ≥50 with valid DXA BMD and grip strength, does low grip strength predict incident fracture risk independently of BMD, and does this excess risk differ by baseline fall history?

The clinically consequential unresolved question is whether low BMD and low grip strength represent a single latent frailty process (where muscle weakness is merely a marker of overall biological ageing) or two separable pathways: (1) bone fragility driving fracture independent of muscle, and (2) muscle weakness driving falls that then cause fracture. This distinction has direct implications for screening and prevention: if the two pathways are separable, then dual anti-resorptive + resistance-exercise interventions would be more effective than bone-targeted therapy alone for the discordant subgroup.

The leading explanation (single latent process) is that low BMD and low grip strength are both downstream of a shared ageing/frailty trajectory, so grip strength adds no independent fracture risk beyond what BMD alone predicts after adjustment. The strongest rival (two-pathway hypothesis) is that muscle weakness contributes an independent fall-related fracture pathway that is not captured by BMD, so the discordant subgroup (low BMD + low grip) has a super-additive fracture risk.

## Why this design avoids the residualization problem

The parent hypothesis ([prior hypothesis]) defined the primary exposure as a standardized grip-strength residual (SGR) constructed by residualizing grip strength on BMD, age, sex, and BMI. This residualization can induce collider bias or residual confounding: conditioning on a post-baseline composite variable (the residual) can open non-causal pathways and make the association with fracture reflect residual confounding rather than a separable muscle pathway.

This child replaces the SGR estimand with a **direct BMD × grip-strength interaction model** in Cox regression, stratified by fall history. The interaction model tests whether the fracture risk associated with low grip strength is modified by BMD level, without constructing a residual that conditions on BMD. This directly tests the two-pathway claim: if the interaction is significant and positive, it indicates that the fracture risk associated with low grip is stronger at lower BMD levels, consistent with a super-additive two-pathway process.

## Exact estimand

**Primary estimand: BMD × grip-strength interaction hazard ratio**

1. Fit a Cox proportional hazards model with BMD (continuous, per SD) and grip strength (continuous, per SD) as main effects, plus their product interaction term.
2. The primary estimand is the hazard ratio for the BMD × grip-strength interaction (HR_interaction), which quantifies whether the fracture risk associated with low grip strength is modified by BMD level.
3. A positive interaction HR (>1.0) indicates that the fracture risk associated with low grip is stronger at lower BMD levels, consistent with a super-additive two-pathway process.
4. A null interaction HR (≈1.0) indicates that the fracture risk associated with low grip is independent of BMD level, consistent with a single latent process.

**Secondary estimand: grip-strength hazard ratio stratified by fall history**

- Cox model with grip strength (continuous, per SD) and BMD (continuous, per SD), stratified by baseline fall history (yes/no).
- The grip-strength HR in the falls-positive subgroup versus the falls-negative subgroup tests whether the muscle-weakness pathway is more prominent in people with a history of falls.

**Why a direct interaction model rather than a residual?**
- The interaction model tests the two-pathway claim directly, without constructing a residual that conditions on BMD.
- The interaction HR is interpretable as "the multiplicative modification of the grip-strength effect by BMD level."
- The interaction model avoids the collider bias and residual confounding that can arise from residualization.
- The interaction model is more robust to the arbitrary cutoffs that can arise from categorical discordance groups.

## Population and temporal boundaries

- **Source**: UK Biobank assessment-center data, `ukb672073_Assessment_Center.csv` (Parquet: `[UKB data file]`) and `ukb672073_Health_Related_Outcomes.csv` (Parquet: `[UKB data file]`), joined on `eid`.
- **Population**: Participants aged ≥50 at baseline assessment with valid DXA (L1-L4 BMD field 23204 and/or femoral neck BMD field 23208), valid grip strength (fields 46/47), and no prior fracture diagnosis in the 2 years before baseline.
- **Baseline**: Date of attending assessment centre (field 53).
- **Follow-up**: From baseline to first incident fracture diagnosis (ICD10 field 41270, date field 41280), censoring at study end, loss to follow-up, or death. Maximum follow-up 10 years.
- **Temporal ordering**: All exposure variables (BMD, grip strength, falls, covariates) are measured at baseline (field 53 date). The outcome (incident fracture) must occur after baseline. Falls (field 2296) are baseline-reported (last 12 months), so they are a baseline covariate, not a time-varying mediator.

## Primary outcome

Incident fracture: first ICD10 code in field 41270 matching fracture codes (S02, S12, S22, S32, S42, S52, S62, S72, S82, S92, M48.31, M80-M84) with date in field 41280 after baseline.

## Key variables and exact bindings

| Variable | Field | Source table | Type |
|----------|-------|-------------|------|
| L1-L4 BMD | 23204 | Assessment_Center | numeric (g/cm²) |
| Femoral neck BMD | 23208 | Assessment_Center | numeric (g/cm²) |
| Grip strength (dominant) | 46 | Assessment_Center | numeric (kg) |
| Grip strength (non-dominant) | 47 | Assessment_Center | numeric (kg) |
| Falls in last year | 2296 | Assessment_Center | binary/ordinal |
| Fracture diagnosis | 41270 | Health_Related_Outcomes | ICD10 codes (array) |
| Fracture date | 41280 | Health_Related_Outcomes | date (array) |
| Assessment date | 53 | Assessment_Center | date |
| Age | 34 | Population_Characteristics | numeric |
| Sex | 31 | Population_Characteristics | binary |
| BMI | 40 | Assessment_Center | numeric |

Join key: `eid` (participant ID) across Assessment_Center, Population_Characteristics, and Health_Related_Outcomes tables.

## Adjustment hierarchy and temporal ordering

**Model 1 (unadjusted)**: Cox with BMD (continuous, per SD) and grip strength (continuous, per SD) only.

**Model 2 (demographic adjustment)**: Cox with BMD + grip strength + age + sex.

**Model 3 (full adjustment)**: Cox with BMD + grip strength + age + sex + BMI + falls (field 2296).

**Model 4 (interaction)**: Cox with BMD × grip-strength interaction + age + sex + BMI + falls.

**Model 5 (falls stratification)**: Cox with grip strength + BMD, stratified by baseline falls (yes/no).

The adjustment hierarchy is pre-specified: Model 4 is the primary adjusted model. Falls are included in the primary model because they are a baseline-reported covariate (last 12 months) and are a potential mediator of the muscle-weakness pathway. However, because falls are measured at baseline (not time-varying), they cannot be used for causal mediation analysis. The falls stratification (Model 5) is a sensitivity analysis to test whether the grip-strength effect differs by fall history.

**Why not adjust for falls in the primary model?**
- Falls are a baseline-reported covariate, not a time-varying mediator. Adjusting for them in the primary model is appropriate for confounding control but does not establish mediation.
- The primary estimand (BMD × grip-strength interaction) is defined without falls adjustment. Falls adjustment is a sensitivity analysis.

## Competing explanations and falsification

**Single latent process (null hypothesis)**: After adjustment for age, sex, BMI, and falls, the BMD × grip-strength interaction HR is not significantly different from 1.0 (p > 0.10). Additionally, the grip-strength HR is not significantly different from 1.0 (95% CI includes 1.0, p > 0.10).

**Two-pathway hypothesis (alternative)**: The BMD × grip-strength interaction HR is significantly > 1.0 (p < 0.05, 95% CI lower bound > 1.0), indicating super-additive risk. Additionally, the grip-strength effect is stronger in the falls-positive subgroup (Model 5).

**Inconclusive**: Interaction HR > 1.0 but 95% CI includes 1.0, or grip-strength HR > 1.0 but 95% CI includes 1.0.

**Falsification criteria (summary)**:

| Result | Interpretation |
|--------|---------------|
| Interaction HR > 1.0, 95% CI > 1.0, grip-strength HR > 1.0, 95% CI > 1.0 | Supports two-pathway hypothesis |
| Interaction HR ≈ 1.0, 95% CI includes 1.0 | Supports single latent process |
| Interaction HR > 1.0 but 95% CI includes 1.0, or grip-strength HR > 1.0 but 95% CI includes 1.0 | Inconclusive; needs larger sample or different analysis |
| Interaction HR < 1.0, 95% CI < 1.0 | Contradicts two-pathway hypothesis; suggests muscle weakness is protective or the interaction is mismeasured |
| Boosted C-index > Cox C-index by > 0.02 with non-rectangular PD plots | Suggests complex interaction beyond multiplicative model |

## Method comparison

### Baseline: Cox proportional hazards regression
- Model 1: Cox with BMD (continuous, per SD) and grip strength (continuous, per SD) only
- Model 2: Cox with BMD + grip strength + age + sex
- Model 3: Cox with BMD + grip strength + age + sex + BMI + falls (primary adjusted model)
- Model 4: Cox with BMD × grip-strength interaction + age + sex + BMI + falls
- Model 5: Cox with grip strength + BMD, stratified by baseline falls
- Estimand: HR for BMD × grip-strength interaction and HR for grip strength (per SD)

### Learned alternative: Gradient-boosted survival model
- Algorithm: XGBoost with survival objective (or gradient-boosted trees with Cox partial likelihood)
- Features: BMD, grip strength, BMD × grip interaction, age, sex, BMI, falls, plus up to 10 additional covariates (smoking, alcohol, physical activity)
- Training: 80% train / 20% held-out test split (stratified by fracture status)
- Evaluation: Concordance index (C-index) on held-out data; comparison with baseline Cox C-index
- Additional: Partial dependence plots for BMD and grip strength to visualize interaction

### What the learned model reveals that the baseline loses
The Cox model assumes proportional hazards and a specific parametric form for the interaction. The gradient-boosted model can capture non-linear and higher-order interactions between BMD and grip strength that a two-way Cox interaction cannot. If the boosted model shows substantially better held-out C-index and the partial dependence plots reveal a non-rectangular interaction pattern, this would suggest the two-pathway hypothesis is more complex than a simple multiplicative interaction.

## Falsification criteria (summary)

| Result | Interpretation |
|--------|---------------|
| Interaction HR > 1.0, 95% CI > 1.0, grip-strength HR > 1.0, 95% CI > 1.0 | Supports two-pathway hypothesis |
| Interaction HR ≈ 1.0, 95% CI includes 1.0 | Supports single latent process |
| Interaction HR > 1.0 but 95% CI includes 1.0, or grip-strength HR > 1.0 but 95% CI includes 1.0 | Inconclusive; needs larger sample or different analysis |
| Interaction HR < 1.0, 95% CI < 1.0 | Contradicts two-pathway hypothesis; suggests muscle weakness is protective or the interaction is mismeasured |
| Boosted C-index > Cox C-index by > 0.02 with non-rectangular PD plots | Suggests complex interaction beyond multiplicative model |

## Key references

[K1] Wang W, Zhen J, Zhu X. Joint association of low bone mass and reduced relative handgrip strength with fragility fracture risk in adults aged 50-59 years: A cross-sectional study from NHANES 2013-2014. Medicine (Baltimore). 2026;105(26):e49483. doi:10.1097/MD.0000000000049483.

[K2] Schousboe JT, et al. Sarcopenia, obesity, and sarcopenic obesity in men and women: results from the Study of Osteoporotic Fractures. Osteoporosis International. 2011;22(11):3195-3204. doi:10.1007/s00198-011-1614-z.

[K3] Morley JE, et al. Sarcopenia: current concepts. J Am Med Dir Assoc. 2001;2(4):186-192. doi:10.1016/S1524-976X(01)00096-8.
