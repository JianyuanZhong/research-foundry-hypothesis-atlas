> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Bone-muscle discordance and incident fracture risk: a two-pathway hypothesis

## Scientific question and clinical importance

Among UK Biobank participants with low bone mineral density (BMD), does low grip strength identify a subgroup with higher incident fracture risk beyond what BMD alone predicts, and is this excess risk partly explained by falls?

The clinically important unresolved question is whether frailty in the context of low BMD represents a single latent process (where muscle weakness is merely a marker of overall biological ageing) or two separable pathways: (1) bone fragility driving fracture independent of muscle, and (2) muscle weakness driving falls that then cause fracture. This distinction has direct implications for screening and prevention: if the two pathways are separable, then dual anti-resorptive + resistance-exercise interventions would be more effective than bone-targeted therapy alone for the discordant subgroup.

The leading explanation (single latent process) is that low BMD and low grip strength are both downstream of a shared ageing/frailty trajectory, so their co-occurrence adds no independent fracture risk beyond what either measure alone predicts. The strongest rival (two separable pathways) is that bone fragility and muscle weakness have distinct biological drivers and that the interaction between low BMD and low grip strength produces a multiplicative or supra-additive increase in fracture risk, with falls as a mediator of the muscle-weakness pathway.

## Data binding and verification status

All fields are from the UK Biobank/ukb672073 split tables, available in the prepared Parquet views.

| Field | UKB ID | Description | Availability |
|-------|--------|-------------|--------------|
| L1-L4 BMD | 23204 | Bone mineral density, lumbar spine | Verified in Parquet |
| Femur neck BMD (right) | 23208 | Bone mineral density, femoral neck | Verified in Parquet |
| Hand grip strength (left) | 46 | Grip strength, kg | Verified in Parquet |
| Hand grip strength (right) | 47 | Grip strength, kg | Verified in Parquet |
| Falls in last year | 2296 | Self-reported falls | Verified in Parquet |
| Diagnoses - ICD10 | 41270 | ICD10 diagnosis codes | Verified in Parquet |
| Date of first in-patient diagnosis | 41280 | Date of ICD10 diagnosis | Verified in Parquet |
| Date of attending assessment centre | 53 | Baseline visit date | Verified in Parquet |

Fracture outcome: ICD10 codes for fracture (S02, S12, S22, S32, S42, S52, S62, S72, S82, S92, M48.5, M80, M81, M83, M84, M85, M86, M87, M88, M89, M90, M91, M92, M93, M94, M95, M96, M97, M98, M99, Z09, Z11, Z12, Z13, Z14, Z15, Z16, Z17, Z18, Z19, Z20, Z21, Z22, Z23, Z24, Z25, Z26, Z27, Z28, Z29, Z30, Z31, Z32, Z33, Z34, Z35, Z36, Z37, Z38, Z39, Z40, Z41, Z42, Z43, Z44, Z45, Z46, Z47, Z48, Z49, Z50, Z51, Z52, Z53, Z54, Z55, Z56, Z57, Z58, Z59, Z60, Z61, Z62, Z63, Z64, Z65, Z66, Z67, Z68, Z69, Z70, Z71, Z72, Z73, Z74, Z75, Z76, Z77, Z78, Z79, Z80, Z81, Z82, Z83, Z84, Z85, Z86, Z87, Z88, Z89, Z90, Z91, Z92, Z93, Z94, Z95, Z96, Z97, Z98, Z99) in table 41270, with date from 41280.

Temporal boundaries: baseline BMD and grip strength from the assessment centre visit (field 53). Incident fracture defined as first ICD10 fracture diagnosis after baseline. Follow-up from baseline to first fracture, death, or end of follow-up.

## Competing explanations and falsification

**Leading claim (two separable pathways):** Low BMD and low grip strength have distinct biological drivers. The interaction between low BMD and low grip strength produces a supra-additive increase in fracture risk. Falls mediate the muscle-weakness pathway.

**Strongest rival (single latent process):** Low BMD and low grip strength are both downstream of a shared ageing/frailty trajectory. Their co-occurrence adds no independent fracture risk beyond what either measure alone predicts. The apparent interaction is explained by residual confounding from shared frailty, medication use, or physical activity.

**Falsification criteria:**
1. If the BMD × grip strength interaction is null (p > 0.10) in the Cox model, the two-pathway hypothesis is not supported.
2. If the combined low-BMD/low-grip group shows no excess hazard ratio beyond either measure alone (HR < 1.2), the two-pathway hypothesis is not supported.
3. If the excess risk is fully explained by prior falls (interaction becomes null after adjustment for falls), the two-pathway claim is weakened.
4. If the gradient-boosted survival model does not improve held-out C-index over BMD-only and BMD+grip models, incremental predictive information is not supported.

## Method comparison

**Baseline (Cox regression):**
- Model 0: BMD only
- Model 1: BMD + grip strength
- Model 2: BMD + grip strength + interaction
- Model 3: Model 2 + falls in last year
- Model 4: Model 3 + age, sex, BMI, smoking, alcohol, physical activity, medication use

Primary estimand: hazard ratio for the BMD × grip strength interaction in Model 2.

**Learned alternative (XGBoost survival):**
- Features: BMD, grip strength, falls, age, sex, BMI, smoking, alcohol, physical activity, medication use
- Target: time-to-fracture
- Evaluation: held-out C-index, compared to Cox models
- Selection criterion: XGBoost must improve C-index by >0.01 over the best Cox model to support incremental predictive information

## Supportive, adverse, and inconclusive results

**Supportive:** Significant BMD × grip strength interaction (p < 0.05), excess HR > 1.2 for the combined low-BMD/low-grip group, and XGBoost C-index improvement >0.01. This would support the two-pathway hypothesis and motivate dual anti-resorptive + resistance-exercise interventions.

**Adverse:** Null interaction, no excess HR, and no C-index improvement. This would support the single latent process explanation and suggest that bone-targeted therapy alone is sufficient.

**Inconclusive:** Weak interaction (p 0.05-0.10), marginal HR (1.0-1.2), or no C-index improvement. This would require further investigation with larger samples or different frailty measures.

## Key references

[K1] Nature Communications 2026: Bone-muscle discordance and fracture risk. Supports the plausibility of separable bone and muscle pathways in fracture risk.

[K2] UK Biobank field documentation: Exact field definitions for BMD, grip strength, falls, and ICD10 diagnoses.

[K3] XGBoost survival analysis methodology: Held-out C-index evaluation for survival prediction.

## Limitations

- Hospital admissions do not capture all fractures; outpatient fractures are missed.
- Falls in the last year are self-reported and subject to recall bias.
- The two-pathway hypothesis is not causal; it is a predictive and descriptive claim.
- The analysis is observational; residual confounding from unmeasured frailty factors is possible.
