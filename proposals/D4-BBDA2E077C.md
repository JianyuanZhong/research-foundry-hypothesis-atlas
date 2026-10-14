> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB-11: T2D Polygenic Risk Expression in Different Ectopic Fat Backgrounds — Does Liver Fat Mediate or Parallel Genetic Susceptibility?

## 1. Unresolved Question and Clinical Importance

Polygenic risk scores (PRS) for type 2 diabetes (T2D) identify individuals with genetically elevated susceptibility, but the clinical interpretation of a high PRS in the context of measured organ fat remains unclear. Two mechanistically distinct models are proposed:

- **Mediation model:** T2D PRS acts primarily through promoting ectopic fat deposition (liver, pancreas), and the PRS→T2D risk is largely channeled through liver fat. In this model, high-PRS individuals with low liver PDFF should have substantially lower T2D risk than high-PRS individuals with high liver PDFF, and the PRS effect should attenuate after adjusting for liver PDFF.

- **Parallel pathway model:** T2D PRS acts through multiple independent pathways (β-cell function, insulin sensitivity, hepatic lipogenesis) that are only partially captured by liver fat. In this model, high-PRS individuals retain elevated T2D risk regardless of liver PDFF, and the PRS effect persists after adjustment for liver PDFF.

**The unresolved question:** In UK Biobank participants with T2D PRS, liver PDFF (MRI-measured), and HbA1c, does the T2D PRS × liver PDFF interaction significantly modify incident T2D risk? Specifically, is the PRS effect attenuated (mediation) or preserved (parallel pathway) in the context of low vs. high liver fat?

This question is clinically important because:
1. **Risk stratification:** If PRS effect is mediated through liver fat, then high-PRS individuals with low liver PDFF may be overestimated in risk, and imaging-based monitoring may be the appropriate follow-up strategy. If PRS retains independent effect, genetic risk cannot be reduced by fat distribution and requires separate management.
2. **Mechanistic insight:** The interaction pattern distinguishes whether liver fat is a mediator or a parallel risk factor in the PRS→T2D pathway, informing therapeutic target selection (e.g., liver-directed vs. β-cell-directed interventions).
3. **Precision prevention:** For high-PRS individuals, knowing whether their risk is "fat-driven" or "genetically autonomous" could guide the intensity and type of preventive interventions.

## 2. Hypothesis (Specific, Falsifiable)

In UK Biobank participants with T2D PRS, liver PDFF, and HbA1c at baseline, and no prior T2D:

**H1 (Interaction):** The T2D PRS × liver PDFF interaction significantly modifies incident T2D risk (ICD10 E10/E11). Specifically, high-PRS (top 20%) individuals with high liver PDFF (above median) have a significantly higher hazard of incident T2D than high-PRS individuals with low liver PDFF, beyond what is explained by the main effects of PRS and PDFF alone.

**H2 (Mediation vs. Parallel):** The T2D PRS main effect is attenuated by >30% after adjustment for liver PDFF (mediation model) vs. <10% attenuation (parallel pathway model).

**Falsification criteria:**
- H1 falsified if interaction HR 0.90–1.10 (95% CI) after full adjustment (age, sex, BMI, HbA1c, 10 genetic PCs).
- H2 inconclusive if attenuation is 10–30% (intermediate model requiring further investigation).

## 3. Clinical Importance

T2D affects ~500 million people worldwide. PRS-based risk stratification is entering clinical practice, but the interpretation of a high PRS in the context of measured organ fat is unresolved. This study directly addresses whether the genetic risk is "expressed through" liver fat or operates through independent pathways, with direct implications for:
- **Preventive strategy:** Fat-directed (lifestyle, bariatric surgery) vs. β-cell-directed (metformin, GLP-1 RA) interventions for high-PRS individuals.
- **Monitoring:** Whether liver imaging (MRI-PDFF, MRS) should be part of the follow-up for high-PRS individuals.
- **Risk communication:** Whether a high PRS in a lean-organ-fat individual represents a genuine elevated risk or a false-positive genetic signal.

## 4. Data Bindings (Verified)

All tables use the ukb672073 identifier namespace, joined on `eid`.

| Variable | Field ID | Parquet | Non-missing |
|----------|----------|---------|-------------|
| T2D PRS | 26285-0.0 | [UKB data file] | 486,132 |
| PRS subgroup | 26200-0.0 | [UKB data file] | 486,132 |
| Genetic PCs | 22009-0.1..0.10 | [UKB data file] | 486,132 |
| Liver PDFF | 21088-2.0 | [UKB data file] | 30,358 |
| Pancreas PDFF | 21090-2.0 | [UKB data file] | 29,464 |
| BMI | 21001-0.0 | [UKB data file] | 499,263 |
| AC date | 53-0.0 | [UKB data file] | 502,370 |
| HbA1c | 30750-0.0 | [UKB data file] | 466,379 |
| ICD10 diagnoses | 41270-0.0..0.258 | [UKB data file] | 502,370 |
| ICD10 dates | 41280-0.0..0.258 | [UKB data file] | 502,370 |
| Cancer registry | 40005/40006 | [UKB data file] | 502,370 |
| Sex | 31-0.0 | [UKB data file] | 502,370 |
| Age | 34-0.0 | [UKB data file] | 502,370 |

**Verified overlap:** PRS ∩ liver PDFF ∩ HbA1c = **27,922 participants**.
**T2D events in overlap (ICD10 E10/E11):** **1,244**.
**Pre-existing T2D (HbA1c ≥ 48 mmol/mol):** 0 in overlap (all participants are T2D-free at baseline by HbA1c criterion).
**Expected analyzable cohort:** ~27,922 with ~1,244 T2D events.

## 5. Study Design

### Population
- UK Biobank participants with T2D PRS (26285), liver PDFF (21088-2.0), and HbA1c (30750) at baseline.
- Exclusion: HbA1c ≥ 48 mmol/mol (6.5%) at baseline (pre-existing T2D).
- Exclusion: ICD10 E10/E11 before AC date (pre-existing T2D diagnosis).
- Final cohort: ~27,922 participants.

### Exposure
- **T2D PRS:** Continuous (z-scored) and categorical (top 20% vs. rest).
- **Liver PDFF:** Continuous (%, visit 2) and categorical (above/below median).
- **Interaction:** PRS × liver PDFF (continuous × continuous, and categorical × categorical).

### Outcome
- **Incident T2D:** ICD10 E10/E11 in 41270 (259 instances) or 40006 (cancer registry, 22 instances), occurring after AC date (53-0.0).
- **Follow-up:** From AC date to T2D diagnosis date (41280) or end of data (2026).

### Covariates
- Age (34-0.0), sex (31-0.0), BMI (21001-0.0), HbA1c (30750-0.0), 10 genetic principal components (22009-0.1..0.10).

### Analysis
1. **Primary:** Cox PH with PRS × liver PDFF interaction, adjusted for age, sex, BMI, HbA1c, 10 PCs.
2. **Mediation test:** Cox PH with PRS (main effect) with and without liver PDFF adjustment; compare HR attenuation.
3. **Sensitivity:**
   - RCS (4 knots) for PRS × liver PDFF dose-response.
   - Stratified by BMI tertile (to test if interaction is BMI-dependent).
   - Pancreas PDFF (21090-2.0) as secondary ectopic fat measure.
   - Exclusion of first 2 years of follow-up (to reduce reverse causation).
4. **Negative control:** PRS × BMI interaction (BMI is a known T2D risk factor; expect no interaction).

### Falsification
- H1 (interaction) falsified: interaction HR 0.90–1.10 (95% CI) after full adjustment.
- H2 (mediation) inconclusive: PRS HR attenuation 10–30% after liver PDFF adjustment.

## 6. Key References

### K1: Wang X et al. (2026). Interaction between fatty pancreas disease and genetically predicted GIP on incident T2D: UK Biobank.
- **Work ID:** doi:10.3389/fendo.2026.1850528 (PMC13283794)
- **Claim:** Genetically predicted GIP levels modify the risk of T2D associated with fatty pancreas disease (FPD), with significant interaction (p=0.015–0.018) [K1]. FPD is associated with greater T2D risk in individuals with higher genetically predicted GIP (HR 2.64, 95% CI 1.86–3.76).
- **Contribution:** This study tests a specific genetic variant (GIPR E354Q) and a single pancreatic fat measure. Our study extends this to the full T2D PRS (486K variants) and liver PDFF (continuous MRI measure), testing whether the broader genetic susceptibility to T2D is modified by liver fat, not just pancreatic fat.
- **Limitation:** Uses a single loss-of-function variant rather than a full PRS; pancreatic fat (binary FPD) rather than continuous liver PDFF; 276 T2D events (smaller than our 1,244).
- **Locator:** Abstract, Results, Conclusion (full text inspected).
- **Inspection:** full_text

### K2: Peng R et al. (2026). Abdominal MRI-derived liver, visceral fat, and pancreatic phenotypes improve prediction of incident T2D.
- **Work ID:** doi:10.1002/dmrr.70235 (PMC13631372)
- **Claim:** Liver PDFF, liver volume, visceral fat volume, and pancreas volume improve T2D prediction beyond clinical risk models (C-index 0.849 vs. 0.820 for clinical model alone; NRI 56.2%, IDI 0.022) [K2]. 36,833 UKB participants, 570 T2D events, median follow-up 7.38 years.
- **Contribution:** This study establishes that liver PDFF is a strong predictor of incident T2D in UKB. Our study adds the genetic dimension: does the T2D PRS effect depend on liver PDFF level? The interaction test is the key novel contribution beyond the main-effect prediction.
- **Limitation:** No genetic data (PRS); prediction model rather than interaction test; 570 T2D events (smaller than our 1,244).
- **Locator:** Abstract, Results (full text inspected).
- **Inspection:** full_text

### K3: Chen H et al. (2025). Genetic insights of waist-to-height ratio on the risk of steatotic and advanced liver diseases: GWAS and PRS-based analyses.
- **Work ID:** doi:10.1186/s40246-025-00832-8 (PMC12581380)
- **Claim:** WHtR PRS is associated with increased risk of NAFLD (OR 1.10), MASLD (OR 1.13), and liver fibrosis (OR 1.11) in UKB [K3]. Gene-environment interaction analysis shows that metabolic status, diabetes, and dietary patterns modulate the genetic liability to high WHtR to the risk of NAFLD/MASLD/liver fibrosis.
- **Contribution:** This study demonstrates that PRS × metabolic status interactions are detectable in UKB for liver disease outcomes. Our study applies the same interaction framework to the T2D PRS × liver PDFF interaction for T2D incidence, testing whether the genetic risk to T2D is modified by measured liver fat.
- **Limitation:** WHtR PRS (not T2D PRS); liver disease outcomes (not T2D incidence); interaction with metabolic status (not liver PDFF); 2,280 SNPs for WHtR (not 486K for T2D).
- **Locator:** Abstract, Results (full text inspected).
- **Inspection:** full_text

## 7. Alternative Explanations and Sensitivity Analyses

1. **Imaging healthy-user selection:** UKB MRI cohort is healthier than the general population. Mitigation: the interaction test is within the MRI cohort, so selection affects both groups equally. Sensitivity: compare with non-MRI UKB participants (if PRS and T2D events are available).
2. **Reverse causation:** Early T2D could affect liver fat (e.g., through metabolic changes). Mitigation: exclusion of first 2 years of follow-up; HbA1c < 48 mmol/mol at baseline.
3. **PRS training overlap:** Standard T2D PRS (26285) is trained on non-UKB populations, reducing overfitting. Mitigation: use the standard PRS (not a UKB-trained one).
4. **Single PDFF measurement:** Liver PDFF is measured once (visit 2). Mitigation: pancreas PDFF (21090-2.0) as secondary measure; sensitivity with visit 3 PDFF (21088-3.0) if available.
5. **BMI confounding:** Liver PDFF is strongly correlated with BMI. Mitigation: adjustment for BMI; stratification by BMI tertile; PRS × BMI negative control.
6. **ICD10 misclassification:** T2D diagnosis via ICD10 E10/E11 may miss milder cases. Mitigation: HbA1c ≥ 48 mmol/mol as secondary outcome; sensitivity with 40006 cancer registry.

## 8. Method Comparison

- **Primary:** Cox PH with PRS × liver PDFF interaction (continuous × continuous).
- **Baseline:** Cox PH with PRS and liver PDFF as main effects only (no interaction).
- **Learned alternative:** XGBoost with PRS, liver PDFF, BMI, HbA1c, age, sex as features; SHAP interaction values for PRS × PDFF. This tests whether the interaction is nonlinear or captured by a flexible model.
- **Rationale:** The Cox PH interaction is the primary test because it directly addresses the scientific question (does PRS effect depend on PDFF?). XGBoost is a sensitivity analysis for nonlinearity. The baseline (main effects only) is the null model.

## 9. What Supportive, Adverse, and Inconclusive Results Would Mean

- **Supportive (interaction HR > 1.10):** T2D PRS effect is amplified by high liver PDFF. This supports the mediation model: genetic risk is expressed through liver fat. Clinical implication: high-PRS individuals with low liver PDFF may be overestimated in risk; liver imaging should be part of the follow-up.
- **Adverse (interaction HR < 0.90):** T2D PRS effect is attenuated by high liver PDFF (counterintuitive). This would suggest a complex interaction where liver fat protects against the genetic risk, possibly through a compensatory mechanism. Would require further investigation.
- **Inconclusive (interaction HR 0.90–1.10):** No significant interaction. This supports the parallel pathway model: T2D PRS acts through multiple independent pathways, and liver fat is a parallel risk factor rather than a mediator. Clinical implication: high-PRS individuals retain elevated risk regardless of liver fat; genetic risk cannot be reduced by fat-directed interventions.

## 10. Feasibility and Resource Budget

- **Cohort:** 27,922 participants, 1,244 T2D events.
- **Compute:** Cox PH (CPU, <1 hour), XGBoost (CPU, <1 hour), RCS (CPU, <1 hour). Total: <4 CPU-hours.
- **Data access:** All fields verified in the bound parquets. No additional data acquisition needed.
- **Solver envelope:** 16 CPUs, 2 GPUs, 256 GB RAM, 8 hours. The analysis fits well within this envelope.

## 11. Limitations

1. Single liver PDFF measurement (visit 2); biological variability may attenuate the interaction.
2. ICD10 E10/E11 depends on hospital admission; milder T2D may be missed.
3. No medication data in the bound parquets; statin or metformin use could affect liver PDFF.
4. UKB self-selection and European ancestry limit generalizability.
5. No Mendelian randomization; causality not testable.
