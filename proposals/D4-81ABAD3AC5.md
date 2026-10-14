> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB-12 Child: CAD Polygenic Risk in Different Lipoprotein and Inflammatory Backgrounds — Residual CAD Risk in High-PRS, Low-ApoB Individuals by CRP Level, Adjusted for Lp(a)

## 1. Unresolved Question and Clinical Importance

The parent study ([prior hypothesis]) tested whether elevated CRP predicts incident CAD in the high-PRS/low-ApoB stratum, but could not adjust for Lp(a) — the strongest remaining confounder for this stratum. Lp(a) is genetically determined (90% heritability), strongly associated with CAD (HR ~1.3 per SD), not affected by statins, and is an independent causal risk factor for atherosclerotic cardiovascular disease [K3]. In the high-PRS/low-ApoB stratum, elevated Lp(a) could explain residual CAD risk that appears to be "inflammatory" when Lp(a) is not adjusted for.

**The unresolved question:** Does the CRP signal in the high-PRS/low-ApoB stratum persist after adjustment for Lp(a)? If the CRP HR attenuates toward null after Lp(a) adjustment, the apparent inflammatory signal is likely mediated by Lp(a) (which is genetically correlated with both CRP and CAD). If the CRP HR persists, it supports an independent inflammatory pathway beyond the Lp(a) axis.

**Clinical importance:** Lp(a) is now recommended for routine cardiovascular risk assessment (2021 AHA/ACC guideline, 2023 ESC guideline). If CRP adds independent prognostic information beyond Lp(a) in genetically high-risk, lipid-normal individuals, it supports a two-biomarker risk stratification strategy (Lp(a) + CRP) for this subgroup. If CRP does not add information, Lp(a) alone suffices for risk stratification in this stratum.

## 2. Hypothesis (Specific and Falsifiable)

Among UK Biobank participants with no prior CAD at baseline, **within the stratum of top-20% CAD PRS and ApoB below the population median, individuals with CRP ≥ 3 mg/L have a higher hazard of incident CAD (inpatient ICD10 I20–I25) than individuals with CRP < 3 mg/L, independent of Lp(a) level.**

Primary estimate: Cox proportional-hazards hazard ratio (HR) for the CRP contrast within the high-PRS/low-ApoB stratum, adjusted for age, sex, genetic principal components (first 10), self-reported ancestry, and Lp(a) (continuous, log-transformed).

**Falsification criterion:** if the fully adjusted HR for CRP ≥ 3 vs < 3 mg/L in the target stratum (with Lp(a) adjustment) falls in 0.90–1.10, the hypothesis is considered falsified (no clinically meaningful inflammatory residual risk independent of Lp(a)); HR < 0.90 or > 1.10 with a 95% CI excluding 1.0 supports the hypothesis.

## 3. Relationship to Closest Prior Work (K1–K3)

- **[K1] Klarin & Natarajan 2021 (Nat Rev Cardiol)** — full text inspected. Establishes that CAD PRS predict incident CAD across cohorts and that high-PRS individuals derive the greatest relative and absolute benefit from LDL-C lowering (post hoc trial analyses). *What this work does not establish:* whether, after conditioning on measured ApoB and Lp(a), residual risk in high-PRS individuals is carried by inflammation. The review frames PRS as a tool for prioritizing subgroups but does not test PRS × ApoB × CRP × Lp(a) joint stratification prospectively.
- **[K2] Ridker et al. 2017, CANTOS (NEJM)** — abstract/metadata inspected (NEJM full text not accessible). Establishes that IL-1β blockade lowers recurrent cardiovascular events in post-MI patients with hs-CRP ≥ 2 mg/L, independent of lipid change. *What this work does not establish:* that baseline CRP stratifies *incident* (first) CAD risk in a primary-prevention population, or that the effect generalizes to genetically high-risk, lipid-normal individuals. CANTOS is a secondary-prevention RCT in enriched (post-MI, hs-CRP ≥ 2) patients; it motivates the inflammatory component but cannot supply the prospective, primary-prevention, PRS-stratified estimate this study targets.
- **[K3] Richardson et al. 2020 (PLoS Med)** — full text inspected. Establishes via multivariable MR that ApoB, not LDL-C, retains the robust causal relationship with CHD after conditioning on co-occurring lipid traits. *What this work does not establish:* the prospective, observational expression of the ApoB–inflammation decomposition inside genetically defined subgroups; MR estimates population-average causal effects and cannot characterize heterogeneity by PRS stratum. Additionally, this work does not test whether Lp(a) mediates the apparent CRP signal in the high-PRS/low-ApoB stratum.

**The specific advance over [K1]–[K3] and the parent study:** a prospective, PRS-stratified test of whether CRP carries residual incident-CAD risk in the high-PRS/low-ApoB stratum *after adjustment for Lp(a)* — a joint (genetic × lipid × inflammatory × Lp(a)) stratification that neither the parent study nor any of the three works performs. The parent study's leading rival (statin-treatment artifact) is partially addressed by the within-stratum design; this child addresses the *second* leading rival (Lp(a) confounding), which is the strongest remaining confounder for the high-PRS/low-ApoB stratum.

## 4. Study Design

### 4.1 Population and Temporal Boundaries
- **Source:** UK Biobank completed subset (ukb672073 split), three Parquet tables sharing the `eid` identifier namespace:
  - Genomics: `[UKB data file]` — 502,370 rows; columns `eid`, `26227-0.0` (standard CAD PRS), `22009-0.1`…`22009-0.40` (40 genetic principal components, **1-indexed**), `22006-0.0` (self-reported ancestry).
  - Hospital records: `[UKB data file]` — 502,370 rows; columns `41270-0.0`…`41270-0.258` (259 ICD10 diagnosis slots) and `41280-0.0`…`41280-0.258` (259 corresponding first-inpatient-diagnosis dates).
  - Main clinical: `[UKB data file]` — columns `30640-0.0` (ApoB, g/L, 467,085 non-null), `30710-0.0` (CRP, mg/L, 468,445 non-null), `30790-0.0` (Lp(a), nmol/L, 375,532 non-null), `53-0.0` (assessment date), `31-0.0` (sex), `34-0.0` (ethnicity).
- **Join key:** `eid` (same namespace across all three tables; no crosswalk needed).
- **Baseline definition:** assessment date from field 53. Exposure measurements (ApoB, CRP, Lp(a)) and PRS are baseline values.
- **Exclusions:**
  - Prevalent CAD at baseline: any inpatient ICD10 I20–I25 with date ≤ baseline date.
  - Missing CAD PRS, missing ApoB, missing CRP, or missing Lp(a).
  - Out-of-range CRP (< 0 or > 200 mg/L) and Lp(a) (< 0 or > 1000 nmol/L) excluded from primary analysis.
- **Expected analytic cohort:** 368,020 participants with all four exposures (verified).

### 4.2 Variables
- **Exposure strata (prespecified):**
  - High PRS: CAD PRS (`26227-0.0`) ≥ 80th percentile (p80 = 0.6335).
  - Low ApoB: ApoB (`30640-0.0`) < median (median = 1.017 g/L).
  - Inflammatory contrast: CRP (`30710-0.0`) ≥ 3 mg/L vs < 3 mg/L.
  - Lp(a) adjustment: Lp(a) (`30790-0.0`), continuous, log-transformed (nmol/L; median = 21.10, p90 = 131.20).
- **Outcome:** incident inpatient CAD, ICD10 I20–I25, first diagnosis after baseline date, from `41270`/`41280`.
- **Covariates:** age, sex (`31-0.0`), first 10 genetic PCs (`22009-0.1`…`22009-0.10`), self-reported ancestry (`22006-0.0`), Lp(a) (log-transformed, continuous).

### 4.3 Primary Analysis
- **Model:** Cox PH, restricted to the high-PRS/low-ApoB stratum:
  `hazard(CAD event) ~ CRP_high (≥3 vs <3) + log(Lp(a)) + age + sex + PC1..PC10 + ancestry`
- **Primary estimand:** HR for CRP ≥ 3 vs < 3 mg/L in the target stratum, adjusted for Lp(a), 95% CI.
- **Secondary contrasts:** (1) Same CRP contrast in high-PRS/high-ApoB stratum; (2) Same CRP contrast in low-PRS/low-ApoB stratum (negative control); (3) CRP as continuous; (4) Lp(a) as continuous; (5) ApoB × CRP and PRS × CRP interactions; (6) Lp(a) × CRP interaction.

### 4.4 Method Comparison
- **Primary:** Cox PH (interpretable HR, standard for time-to-event with prespecified contrasts).
- **Sensitivity:** XGBoost survival model on full cohort with features {CAD PRS, ApoB, CRP, Lp(a), age, sex, PC1..PC10, ancestry}, evaluated by C-index and calibration in the target stratum, with SHAP-style feature attribution.
- **Deferral:** No competing-risk Fine-Gray model in primary; no MR extension.

### 4.5 Alternative Explanations and Their Tests
1. **Lp(a) confounding (leading rival, NEW):** Test: primary model includes log(Lp(a)) as continuous covariate.
2. **Treatment/selection artifact:** Test: exclude participants reporting top-6 medication codes (statin-user exclusion).
3. **Reverse causation:** Test: lagged follow-up (exclude events in first 2 years).
4. **Measurement artifact:** Test: CRP ≥ 10 mg/L excluded in sensitivity.
5. **Population stratification:** Test: 10-PC adjustment standard; sensitivity with 20 PCs.

### 4.6 Interpretation of Possible Outcomes
- **Supportive (HR > 1.10, CI excluding 1.0 after Lp(a) adjustment):** evidence for independent inflammatory residual risk.
- **Adverse/falsified (HR 0.90–1.10 after full adjustment):** no clinically meaningful inflammatory residual risk independent of Lp(a).
- **Attenuation (HR > 1.10 without Lp(a), HR 0.90–1.10 with Lp(a)):** apparent inflammatory signal mediated by Lp(a).
- **Inconclusive (HR outside 0.90–1.10 but CI includes 1.0):** underpowered; report estimate and CI.

### 4.7 Computationally Checkable vs Clinical-Adjudication Claims
- **Computationally checkable:** cohort construction, exposure stratification, event ascertainment, Cox HRs and CIs, XGBoost discrimination/calibration, all sensitivity analyses.
- **Requires clinical adjudication:** medication code identification, CRP threshold optimality, whether supportive HR justifies anti-inflammatory therapy (requires RCT), cause-of-death misclassification.

## 5. Data Bindings (Verified)

| Table | Path | Rows | Key columns |
|---|---|---|---|
| Genomics | `[UKB data file]` | 502,370 | `eid`; `26227-0.0` (CAD PRS); `22009-0.1`…`22009-0.40` (PCs); `22006-0.0` (ancestry) |
| HRO | `[UKB data file]` | 502,370 | `41270-0.0`…`41270-0.258` (ICD10); `41280-0.0`…`41280-0.258` (dates) |
| Clinical | `[UKB data file]` | 502,370 | `30640-0.0` (ApoB); `30710-0.0` (CRP); `30790-0.0` (Lp(a)); `53-0.0` (date); `31-0.0` (sex); `34-0.0` (ethnicity); `20003-0.0`…`20003-0.47` (medications) |

Join key: `eid`. PC adjustment uses first 10 PCs, columns `22009-0.1` through `22009-0.10` (1-indexed).

**Verified feasibility counts:**
- All 4 exposures: 368,020
- Target stratum: 34,470
- CRP ≥ 3 in target: 7,178; CRP < 3: 27,292
- CAD events in target: 269
- CAD events in full cohort: 1,735
- Lp(a) in target: mean=46.91, median=21.70, p90=134.80 nmol/L
- CRP in full cohort: mean=2.58, median=1.32 mg/L
- ApoB in full cohort: mean=1.03, median=1.017 g/L
- PRS p80: 0.6335

## 6. Resources and Feasibility
- CPU-only sufficient: ~370K rows × 3 tables, Cox PH, XGBoost. Fits within solver envelope (16 CPU / 256 GB / 8 h).
- Event support: 269 CAD events in target stratum — adequate for primary HR with CI width ~±0.15.

## 7. Key References

- **[K1]** Klarin D, Natarajan P. Clinical utility of polygenic risk scores for coronary artery disease. *Nat Rev Cardiol*. 2021. DOI: 10.1038/s41569-021-00638-w. Full text inspected.
- **[K2]** Ridker PM, et al. Antiinflammatory Therapy with Canakinumab for Atherosclerotic Disease. *NEJM*. 2017;377:1119-1131. DOI: 10.1056/NEJMoa1707914. Abstract/metadata inspected.
- **[K3]** Richardson TG, et al. Evaluating the relationship between circulating lipoprotein lipids and apolipoproteins with risk of coronary heart disease. *PLoS Med*. 2020;17(3):e1003062. DOI: 10.1371/journal.pmed.1003062. Full text inspected.
