> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB-12: CAD Polygenic Risk Score Expression in Different Lipoprotein and Inflammatory Backgrounds

## Unresolved Question

Among individuals with high coronary artery disease (CAD) polygenic risk score (PRS), does elevated C-reactive protein (CRP) predict higher residual CAD risk independent of apolipoprotein B (ApoB) levels? Specifically, do high-PRS individuals with low ApoB but elevated CRP have higher incident CAD event rates than high-PRS individuals with low ApoB and low CRP?

### Why This Question Matters

CAD risk is driven by two major biological pathways: lipid-mediated atherogenesis (captured by ApoB, the number of atherogenic particles) and inflammation (captured by CRP, a downstream marker of the IL-1β/IL-6/CRP axis). The CANTOS trial [K2] established that IL-1β inhibition reduces cardiovascular events independent of lipid lowering, confirming inflammation as an independent causal pathway. Mendelian randomization studies [K3] have shown that ApoB is a causal determinant of CHD risk, largely independent of LDL-C. Polygenic risk scores for CAD [K1] capture genetic susceptibility to the disease but do not distinguish which biological pathway drives an individual's risk.

The clinical question is: in a person with high genetic CAD risk but well-controlled lipids (low ApoB), does elevated inflammation (high CRP) identify a subgroup at materially higher residual risk? If so, this would support targeted anti-inflammatory therapy in genetically high-risk, lipid-controlled individuals—a precision medicine strategy not currently in guidelines.

### What Is Already Known vs. What Is Unresolved

**Known:**
- CAD PRS predicts incident CAD in large cohorts [K1]
- CRP is an independent marker of cardiovascular risk; IL-1β inhibition reduces events [K2]
- ApoB is a causal determinant of CHD risk [K3]
- The UKB contains PRS, ApoB, CRP, and CAD outcome data for ~500K participants

**Unresolved:**
- Whether the CAD PRS effect is modified by ApoB and/or CRP levels
- Whether high-PRS + low-ApoB + high-CRP individuals have higher residual CAD risk than high-PRS + low-ApoB + low-CRP individuals
- Whether the interaction between genetic risk and inflammatory status is clinically meaningful (i.e., does it change management decisions?)

## Falsifiable Hypothesis

**H1:** Among UKB participants with CAD PRS in the top 20% and ApoB below the median, those with CRP ≥ 3 mg/L have a ≥ 30% higher hazard ratio for incident CAD (I20-I25) compared to those with CRP < 3 mg/L, after adjustment for age, sex, BMI, smoking, and genetic principal components.

**Falsification criteria:**
- **Supportive:** HR ≥ 1.30 with 95% CI not crossing 1.0 → supports the hypothesis that inflammation drives residual risk in genetically high-risk, lipid-controlled individuals
- **Adverse:** HR ≤ 1.05 or 95% CI crossing 1.0 → argues against a clinically meaningful inflammatory component to residual CAD risk in this subgroup
- **Inconclusive:** HR between 1.05 and 1.30 with wide CI → insufficient power or effect size to draw firm conclusions; would require larger cohort or longer follow-up

## Data Bindings

### Source Files (read-only)
| Table | File | Key Fields |
|-------|------|------------|
| Genomics (CAD PRS) | `[internal dataset path]` | `eid`, `26227-0.0` (CAD PRS), `22009-0.0` through `22009-39.0` (genetic PCs) |
| Main Clinical (ApoB, CRP) | `[internal dataset path]` | `eid`, `30640-0.0` (ApoB), `30710-0.0` (CRP), `53-0.0` (assessment date) |
| HRO (CAD events) | `[internal dataset path]` | `eid`, `41270-0.0` through `41270-0.258` (ICD-10 codes), `41280-0.0` through `41280-0.258` (event dates) |

### Join Keys
- All three tables join on `eid` (UKB participant ID)

### Temporal Boundaries
- **Baseline:** Assessment date (field 53-0.0) in main clinical table
- **Exclusion:** Participants with I20-I25 codes in HRO before assessment date are excluded (baseline CAD)
- **Follow-up:** From assessment date to first I20-I25 event date (field 41280) or censoring (death, loss to follow-up, end of data)

### Event Definition
- **Primary outcome:** First incident CAD event, defined as any ICD-10 code I20-I25 (angina, acute MI, post-MI, other acute ischemic, chronic ischemic) in HRO table (field 41270)
- **Secondary outcome:** First MI (I21-I22) only

### Population
- UKB participants with non-null CAD PRS (26227), ApoB (30640), CRP (30710), and assessment date (53)
- Exclusion: baseline CAD (I20-I25 before assessment date), age < 40 or > 85

## Method Design

### Primary Analysis: Cox Proportional Hazards Model

**Model 1 (Main effect):**
Cox PH model with time-to-first-CAD-event as outcome, CRP (continuous, log-transformed) as exposure, adjusted for:
- Age, sex, BMI, smoking status
- Genetic principal components (first 10, fields 22009-0.0 through 22009-9.0)
- ApoB (continuous, log-transformed) — to isolate the inflammatory effect independent of lipid level

**Model 2 (Interaction):**
Cox PH model with PRS × CRP interaction term, stratified by ApoB quartile:
- Within each ApoB quartile, test whether CRP modifies the PRS effect on CAD risk
- Primary contrast: within the lowest ApoB quartile, compare HR for CRP ≥ 3 vs < 3 mg/L in top 20% PRS vs bottom 80% PRS

**Model 3 (Three-way interaction):**
Cox PH model with PRS × ApoB × CRP three-way interaction to test whether the CRP effect on CAD risk is strongest in the high-PRS, low-ApoB subgroup.

### Baseline Comparison
- **Null model:** Cox PH with age, sex, BMI, smoking, PCs only (no PRS, ApoB, or CRP)
- **Model 1 vs Null:** Compare C-index to assess incremental predictive value of PRS + ApoB + CRP
- **Subgroup-specific HRs:** Report HRs for each PRS × ApoB × CRP stratum

### Sensitivity Analyses
1. **Gradient boosting (XGBoost) time-to-event model:** Fit on the same cohort with PRS, ApoB, CRP, age, sex, BMI, smoking, PCs as features. Compare feature importance and SHAP values to Cox PH to check for non-linear interactions.
2. **CRP as binary (≥ 3 vs < 3 mg/L):** Per JUPITER trial threshold
3. **ApoB as binary (below vs above median):** Simplified contrast
4. **Exclude participants on statins:** To reduce confounding by lipid-lowering therapy
5. **Lp(a) adjustment:** If Lp(a) data available (field 30790), adjust for Lp(a) to isolate the inflammatory effect from the genetically determined Lp(a) pathway

### Statistical Considerations
- Two-sided α = 0.05, with Bonferroni correction for the 3 primary models
- Power: With ~400K participants, ~50K expected CAD events, and ~10% in the high-PRS/low-ApoB/high-CRP stratum, the study is powered to detect HR ≥ 1.15 at 80% power
- Proportional hazards assumption checked with Schoenfeld residuals
- Missing data: Complete case analysis for primary; multiple imputation sensitivity analysis

## Alternative Explanations and How to Address Them

1. **CRP as a consequence of CAD (reverse causation):** Addressed by excluding baseline CAD and requiring ≥ 1 year between assessment and event in sensitivity analysis.
2. **Confounding by statin use:** Statins lower both CRP and ApoB. Addressed by excluding statin users in sensitivity analysis and by the MR evidence [K3] that ApoB is causal.
3. **Genetic confounding:** CAD PRS variants may affect CRP or ApoB levels. Addressed by adjusting for genetic PCs and by the fact that PRS captures many small-effect variants while CRP/ApoB are measured phenotypes.
4. **Measurement error in CRP:** Single CRP measurement has biological variability. Addressed by using log-transformation and by the fact that CRP ≥ 3 mg/L is a well-established threshold with consistent effect sizes across studies.
5. **Selection bias:** UKB participants are healthier than the general population. This limits generalizability but does not bias the internal comparison within the cohort.

## Method Comparison: Cox PH vs Gradient Boosting

**Cox PH (primary):**
- Advantages: Interpretable HRs, well-understood assumptions, directly tests the interaction hypothesis, standard for time-to-event data
- Limitations: Assumes proportional hazards, linear effects, may miss non-linear interactions

**Gradient Boosting (sensitivity):**
- Advantages: Captures non-linear interactions, no proportional hazards assumption, can reveal complex PRS × ApoB × CRP patterns
- Limitations: Less interpretable, requires careful hyperparameter tuning, risk of overfitting with 400K samples
- What it reveals that Cox PH loses: Non-linear dose-response curves, threshold effects, and higher-order interactions that may not be captured by the specified interaction terms

**Decision:** Cox PH is the primary method because the hypothesis is specifically about a hazard ratio contrast in a defined subgroup. Gradient boosting is a sensitivity analysis to check robustness and to explore whether the interaction pattern is non-linear.

## Key References

[K1] Klarin DM, Natarajan P. "Clinical utility of polygenic risk scores for coronary artery disease." Nat Rev Cardiol. 2021;18(5):291-301. DOI: 10.1038/s41569-021-00638-w. PMID: 34811547.
- **Claim supported:** CAD PRS can predict incident CAD in multiple cohorts and identify individuals who benefit from LDL-C lowering strategies. PRS is a quantitative metric of genetic susceptibility that improves risk prediction beyond traditional factors.
- **Contribution of this proposal:** Extends PRS utility by testing whether the PRS effect is modified by measured inflammatory (CRP) and lipid (ApoB) phenotypes, moving from population-level prediction to pathway-specific risk stratification.
- **Limitation:** Review article; does not provide new cohort data. Does not test PRS × CRP or PRS × ApoB interactions.
- **Inspection:** Full text inspected (Nature Reviews Cardiology HTML, 517KB).

[K2] Ridker PM, Everett BM, Thuren T, et al. CANTOS Trial Group. "Antiinflammatory Therapy with Canakinumab for Atherosclerotic Disease." N Engl J Med. 2017;377(12):1119-1131. DOI: 10.1056/NEJMoa1707914. PMID: 28845751.
- **Claim supported:** IL-1β inhibition with canakinumab reduced cardiovascular events in post-MI patients with elevated CRP, independent of lipid lowering. CRP is a valid marker of the inflammatory pathway contributing to atherosclerotic cardiovascular disease.
- **Contribution of this proposal:** Tests whether the inflammatory pathway (indexed by CRP) contributes to residual CAD risk in genetically high-risk individuals with controlled lipids, extending the CANTOS finding from a secondary prevention RCT to a primary prevention observational cohort.
- **Limitation:** CANTOS was in post-MI patients (secondary prevention), not primary prevention. Does not test PRS × CRP interaction. Full text not available (subscription required); metadata and abstract inspected.
- **Inspection:** Abstract and metadata only (Europe PMC JSON, 249KB).

[K3] Richardson TG, Sanderson E, Palmer TM, Ala-Korpela M, Ference BA, Davey Smith G, Holmes MV. "Evaluating the relationship between circulating lipoprotein lipids and apolipoproteins with risk of coronary heart disease: A multivariable Mendelian randomisation analysis." PLoS Med. 2020;17(3):e1003062. DOI: 10.1371/journal.pmed.1003062. PMID: 32203549.
- **Claim supported:** ApoB is a causal determinant of CHD risk, largely independent of LDL-C, as shown by multivariable Mendelian randomization. The atherogenic particle number (ApoB) is the key lipid mediator of cardiovascular risk.
- **Contribution of this proposal:** Uses the causal evidence for ApoB to justify stratifying by ApoB level when testing whether CRP adds independent risk. Tests whether the ApoB-independent inflammatory pathway (CRP) is most relevant in the low-ApoB, high-PRS subgroup.
- **Limitation:** MR study; does not provide direct observational evidence of PRS × ApoB × CRP interaction. Does not test whether the ApoB-CRP relationship differs by genetic risk level.
- **Inspection:** Full text inspected (PLOS Medicine HTML, 305KB).

## Additional Context

**Seed paper:** The Nature Communications 2025 metabolomics GWAS paper (s41467-025-60058-z) provides context on the genetic architecture of circulating metabolites in UKB, confirming that lipid and inflammatory markers are strongly genetically determined and that pleiotropic loci link metabolic pathways to disease. This supports the biological plausibility of testing PRS × metabolite interactions.

## Feasibility

- CAD PRS: 486,132 non-null
- ApoB: 467,086 non-null
- CRP: 468,446 non-null
- CAD events (I20-I25): 60,725 in HRO
- Expected overlap after exclusions: ~400K+ participants
- Expected events in analysis cohort: ~50,000+
- Compute: CPU-only, ~30 min for Cox PH models, ~1 hr for gradient boosting

## What Supportive, Adverse, and Inconclusive Results Would Mean

**Supportive (HR ≥ 1.30, CI not crossing 1.0):**
- Would suggest that in genetically high-risk, lipid-controlled individuals, elevated inflammation is a major driver of residual CAD risk
- Would support targeted anti-inflammatory therapy (e.g., colchicine, canakinumab) in this subgroup
- Would justify a prospective RCT of anti-inflammatory therapy in high-PRS, low-ApoB, high-CRP individuals
- Would not establish causality (observational study); would require RCT confirmation

**Adverse (HR ≤ 1.05 or CI crossing 1.0):**
- Would argue against a clinically meaningful inflammatory component to residual CAD risk in this specific subgroup
- Would suggest that in genetically high-risk, lipid-controlled individuals, the remaining risk is not primarily inflammatory
- Would redirect attention to other residual risk mechanisms (e.g., Lp(a), thrombotic, metabolic)
- Would not refute the CANTOS finding (different population, secondary prevention)

**Inconclusive (HR 1.05-1.30, wide CI):**
- Would indicate insufficient power or a modest effect size
- Would require a larger cohort, longer follow-up, or a different inflammatory marker
- Would not support or refute the hypothesis definitively
- Would warrant a sensitivity analysis with alternative CRP thresholds or a different inflammatory marker (e.g., IL-6, fibrinogen)

## Claims Requiring Clinical Adjudication

- Whether the observed HR difference is clinically meaningful for treatment decisions (requires expert cardiology adjudication)
- Whether the PRS × CRP interaction is generalizable to non-UKB populations (requires external validation)
- Whether anti-inflammatory therapy would be safe and effective in this specific subgroup (requires RCT)
- The optimal CRP threshold for risk stratification (requires clinical trial data)

## Computationally Checkable Claims

- The HR for CRP in the high-PRS/low-ApoB subgroup (Cox PH model)
- The PRS × CRP interaction p-value
- The C-index improvement from adding PRS + ApoB + CRP to the null model
- Feature importance rankings from gradient boosting
- The number of participants and events in each stratum
