> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Proposal: Post-resection (0–30 d) liver synthetic-function trajectory and early (≤1-year) HCC recurrence after hepatic resection — independence from preoperative labs

Episode 7 (HCC island). Scientific restart within the HCC island; the two parked HCC branches
([prior hypothesis]: pre-op-lab 1-yr recurrence; [prior hypothesis]:
pre-op-lab 1-yr TACE-uptake) are context, not scientific parents. All data bindings measured this
episode on the local HCC snapshot [source checksum]
(read-only, [internal dataset path]). Companion files: work/hcc-postop-liver-feasibility.md
(measured numbers), work/hcc-postop-liver-design.md (working design note), work/refs/key-references.json.

## 1. Clinical question and why it matters

After curative-intent hepatic resection for HCC, the first 30 days are a distinct clinical decision
point: surveillance intensity, adjuvant-therapy eligibility, and transplant listing are decided on
the basis of postoperative recovery. The unresolved question is whether the **post-resection
trajectory of liver synthetic function (albumin, total bilirubin, INR/PT) in the first 30 days**
carries prognostic signal for early (≤1-year) recurrence **independent of preoperative labs**, and
whether it identifies a post-resection deterioration subgroup with substantially higher 1-year
recurrence risk.

This is a different estimand from the parked branches, which use PREOPERATIVE labs (information
available before the surgical decision). Post-resection synthetic function reflects residual
functional liver mass, post-hepatectomy liver failure (PHLF), and early occult disease burden —
none of which are captured by pre-op labs.

Closest inspected works: K1 (Omori 2026) shows post-hepatectomy ALBI trajectories at POD 90/180
predict OS/RFS; K2 (Horie 2026) shows PHLF ≥B worsens survival-after-recurrence but NOT
time-to-recurrence — the key rival bound; K3 (Wang 2021) shows pre-op labs predict post-hepatectomy
liver dysfunction with C-stat ~0.85–0.88 — the null hypothesis the independence test must beat.
None of these tests the 0–30 d window for 1-yr recurrence independent of pre-op labs.

## 2. Leading explanations and what separates them

- A (residual liver mass / decompensation): post-op decline reflects regenerative capacity and
  PHLF. Prediction: signal concentrated in pre-op-impaired patients; adds information beyond
  pre-op labs in that subgroup.
- B (early occult recurrence / tumor burden): post-op decline reflects occult tumor burden.
  Prediction: signal persists in pre-op-normal patients; more strongly associated with
  imaging-confirmed / >90-d recurrence than with ≤90-d re-diagnosis.
- Rival C (surveillance/selection artifact): sicker patients get more post-op labs and more early
  follow-up, inflating both trajectory and diagnosis-text outcome. Prediction: association
  attenuates on the >90-d outcome and when testing frequency is included as a covariate.

Separating observations (all computable): (1) independence of B2 over B1 (NRI/IDI); (2) outcome
specificity (base vs >90-d vs imaging-confirmed); (3) pre-op-stratified effect; (4)
testing-frequency adjustment.

## 3. Population and temporal boundaries

- Population: first hepatic resection 2013-01-01 to 2018-12-31. Lexical rule (this episode):
  手术 matches (肝叶|肝部分|部分肝|肝段|半肝|肝肿瘤|肝(肿瘤)?切除) and excludes
  (移植|活检|穿刺|探查). Measured n = 8,370 (2013:1,481; 2014:1,341; 2015:1,485; 2016:1,383;
  2017:1,129; 2018:1,551). The solver must fix this rule and record exact n. (Parked branch A used
  a narrower rule, n=7,701; branch B a broader rule, n=8,950. The design is insensitive to the
  ±15% rule difference.)
- Analysis sub-cohort: patients with ≥2 post-resection measurements in ALL of ALB, TBIL, INR.
  Measured n = 7,329 (87.6% of cohort). Sensitivity: ≥1 post-op measurement in all three.
- Index date: resection date (手术.开始时间 of first matching procedure).
- Feature window: 0–30 d post-resection (检验时间). Pre-op covariate window: −30 to 0 d.
- Outcome window: 0–365 d post-resection. Base: first HCC-diagnosis encounter >0 d and ≤365 d.
  Sensitivity A: >90 d and ≤365 d. Sensitivity B: imaging-confirmed (检查.检查 contains 增强 and
  (上腹部|腹部|肝|PET), same 就诊号 as the event encounter). Sensitivity C: A∩B.
- Censoring: last encounter date (基本信息.就诊时间); no mortality data.

## 4. Variables (exact bindings)

Join keys: (患者主索引, 就诊号) across all tables. Time fields: 检验时间 (labs), 开始时间
(procedures), 就诊时间 (encounters). All "YYYY-MM-DD HH:MM:SS". UTF-8 with BOM (utf-8-sig).
No unit column in labs; units inferred from analyte name.

- Outcome: 1-yr HCC recurrence (diagnosis-text proxy). Source: data_诊断_7504718184492840569.csv
  (诊断名称 contains 肝细胞癌 or 原发性肝癌); encounter date from data_基本信息
  (就诊时间). Event time = first qualifying encounter date; censoring time = last encounter date.
- Post-op trajectory features (per analyte ALB 白蛋白, TBIL 总胆红素, INR 国际标准化比值, plus
  context ALT 丙氨酸氨基转移酶, GGT γ-谷氨酰转肽酶, PLT 血小板计数): first, last, min, max,
  change (last−first), least-squares slope (units/day), n of measurements. 6×3 = 18 primary +
  18 context = 36 features. Derived: post-op ALBI score at first and last draw (ALBI =
  log10(TBIL_µmol/L) + 2.56×log10(ALB_g/L) − 0.96×log10(ALB) — solver must fix the exact formula
  and unit conversion), ALBI change. Plausibility filter (recorded): ALB [10,60] g/L, TBIL
  [0,500] µmol/L, INR [0.5,5.0], ALT/GGT [0,2000] U/L; out-of-range rows excluded from that
  analyte's series (implausible values exist: INR min 0.0 max 201.0 measured).
- Pre-op covariates (B1 baseline): nearest pre-surgery value per analyte (ALB, TBIL, INR, ALT,
  GGT, PLT, WBC, HGB), missingness indicators, age, sex, resection year. Pre-op availability in
  sub-cohort: WBC 93.7%, HGB 88.6%, PLT 87.2%, INR/PT 81.1%, ALT/GGT 75.3%, ALB/TBIL 74.3%;
  AFP 0% (assay 2019+ only). Median 1 measurement in window.
- Testing-frequency covariate: total number of post-op lab rows in 0–30 d (rival C control).

## 5. Models

- B0 (clinical baseline): logistic regression on age, sex, resection year.
- B1 (pre-op labs): B0 + pre-op lab set (nearest value + missingness indicators).
- B2 (post-op trajectory, the hypothesis model): B1 + post-op trajectory features. Penalized
  logistic (L1/L2, 5-fold CV for penalty) — primary.
- B3 (learned alternative): gradient-boosted trees (LightGBM) on the same B2 feature set.
  Substantive alternative: tests whether non-linear interactions (ALB drop × pre-op ALB, TBIL
  rise × INR rise, slope × n) and threshold effects add information the penalized linear model
  loses, and yields feature importances that map onto the A/B/C explanations.
- Primary estimand: 1-yr cumulative incidence (Fine-Gray subdistribution, full sub-cohort,
  censoring at last encounter) — same censoring-aware design as parked branch A. Model scores
  entered as single covariates; terciles cut on test-set predicted probability.
- Split: temporal — train 2013–2016 (n≈5,160), test 2017–2018 (n≈2,169); no patient overlap.
  Secondary: 5-fold CV within 2013–2018 for penalty selection only.

## 6. Evaluation and falsification thresholds (pre-specified)

For each model on the held-out test set: (a) time-dependent C-index at 1 y with DeLong CI;
(b) top-vs-bottom tercile 1-yr cumulative-incidence gap; (c) calibration slope/intercept;
(d) NRI/IDI of B2 vs B1 (the INDEPENDENCE question) and of B3 vs B2.

- Supportive: B2 (or B3) test C-index ≥ 0.62 AND tercile gap ≥ 10 pp AND NRI of B2 over B1
  positive with CI excluding 0 (independence from pre-op labs), with the >90-d sensitivity
  concordant. Deterioration subgroup: top tercile of B2/B3 score has 1-yr recurrence rate ≥ 15 pp
  above bottom tercile on the >90-d outcome.
- Adverse: B2/B3 test C-index ≤ 0.58 OR tercile gap ≤ 5 pp OR NRI of B2 over B1 ≤ 0 → post-op
  trajectory adds no independent signal; record as a negative result (the descriptive null in the
  feasibility file would be confirmed).
- Inconclusive: 0.58 < C-index < 0.62 → weak signal; report with CIs, no utility claim.

Interpretation grid (pre-specified):
- B2 supportive on base AND >90-d → post-op trajectory carries independent early-recurrence
  signal; next steps: external validation, decision-curve analysis, adjudicated recurrence.
- B2 supportive on base, adverse on >90-d → signal driven by ≤90-d re-diagnosis / surveillance
  intensity (rival C); downgrade to "predicts early post-op HCC re-diagnosis, not necessarily
  true recurrence."
- B2 adverse on base but pre-op-impaired subgroup shows strong post-op effect → supports
  explanation A (residual mass/PHLF) in a selected population; general claim not supported.
- B2 adverse everywhere → post-op 0–30 d synthetic-function trajectory is not an independent
  early-recurrence marker in this cohort; parked pre-op-lab branches remain the better lab-only
  route.
- B3 > B2 with interpretable importances (ALB-drop × pre-op-ALB) → mechanistic hint toward A;
  TBIL/INR-rise dominance → hint toward B. Directional only.

## 7. Measured outcome counts (this episode)

- Full cohort (n=8,370): 2,193 (26.2%) with a 1-yr HCC-diagnosis event. First event ≤90 d:
  1,483 (67.6% of events); >90 d: 1,147.
- Sub-cohort (n=7,329): 1,920 (26.2%) base 1-yr events; 957 (13.1%) with >90 d; 283 (3.9%)
  imaging-confirmed (date-matched approximation — solver must match on 就诊号 exactly).
- Censoring: 5,216/7,329 (71.2%) have last encounter <365 d after resection. No mortality table.
- Descriptive deterioration subgroups (naive rules, unadjusted): ALB drop≥5 (n=700, 23.3%);
  TBIL rise≥2 (n=1,405, 19.5%); INR rise≥0.2 (n=136, 34.6%); OR-combined (n=2,094, 21.4% vs
  28.1% rest). HONEST NULL-LEANING: the naive deterioration group does NOT show higher 1-yr
  recurrence unadjusted. The designed adjusted/learned experiment with the >90-d outcome is what
  tests the hypothesis; an adverse result is a real, valuable possibility.

## 8. What the future solver must fit/estimate (deliverables)

1. Cohort table: sub-cohort patients with post-op trajectory features, pre-op covariates, outcome
   flags (base/A/B/C), event time, censoring time, testing-frequency covariate.
2. B0/B1/B2/B3 models (penalized logistic with CV-selected penalty; LightGBM with CV
   hyperparameters), fit on 2013–2016, evaluated on 2017–2018.
3. Full-sub-cohort Fine-Gray subdistribution HRs + 1-yr cumulative incidence with CIs for each
   model score; tercile tables for base/A/B/C outcomes.
4. Held-out time-dependent C-index (DeLong CIs), calibration, NRI/IDI (B2 vs B1, B3 vs B2).
5. Pre-op-stratified analysis: B2 effect within pre-op-normal vs pre-op-impaired (ALBI grade)
   subgroups.
6. Sensitivity: ≥1 post-op lab sub-cohort; testing-frequency-adjusted model.

Completion = all metrics computed and reported. Clinical truth (true recurrence, causality,
external validity) is NOT established by this experiment; chart review and external validation are
required for those claims.

## 9. Resource estimate (CPU only)

- 检验 full scan (2.2 GB): ~80–100 s per pass on 4 CPU (measured); 2 passes (pre + post windows)
  ≈ 4 min. 检查 scan (1.14 GB) for imaging-confirmation sensitivity: ~10 s per pass.
- Cohort assembly + Fine-Gray + B0–B3 fitting (CV) + 4 outcome definitions + stratified analyses:
  < 2 h on 4–16 CPU, 32 GB RAM. No GPU (tabular, n≈7,300, ~50 features).
- Fits the solver envelope (16 CPU, 256 GB, 8 h) with large margin. A sequence model (e.g., LSTM
  on lab series) is NOT justified at n≈7,300 with 3–4 time points per analyte — the learned
  alternative is gradient boosting on summary features, the scientifically substantive non-linear
  option here.

## 10. Limitations (honest)

1. Outcome is a diagnosis-text proxy (unstructured 诊断名称); 67.6% of 1-yr events are ≤90 d
   post-resection (likely re-statement of the original tumor during post-op workup). The >90-d
   and imaging-confirmed sensitivities address this but reduce event counts (957 / 283).
2. ~71% censored before 365 d (loss to facility or death-unknown); no mortality table.
3. No structured MVI, tumor size/number, resection margin, or imaging features (same as parked
   branches).
4. Single center; no external validation.
5. Post-op testing is selective (sicker patients get more labs) — rival C; controlled by
   testing-frequency covariate and >90-d outcome.
6. AST not available under the expected name (天门冬氨酸氨基转移酶 = 0 rows); context analyte
   dropped.
7. Pre-op labs are sparse (median 1 measurement; ~26% missing for the synthetic trio); B1 baseline
   is a partial version of K3's predictor set (no portal hypertension, no resection extent).

## 11. Key references (three inspected works; abstract-only)

- [K1] Omori M, et al. Postoperative liver function trajectories and risk factors after hepatectomy
  for hepatocellular carcinoma. Surg Today. 2026;56(10):2378-2386. PMID 42319440,
  DOI 10.1007/s00595-026-03331-y.
- [K2] Horie H, et al. Reframing Post-Hepatectomy Liver Failure as a Determinant of
  Post-Recurrence Survival in HCC. J Hepatobiliary Pancreat Sci. 2026;33(5):343-351.
  PMID 41674000, DOI 10.1002/jhbp.70087.
- [K3] Wang YY, et al. Development and Validation of a Nomogram to Preoperatively Estimate
  Post-hepatectomy Liver Dysfunction Risk and Long-term Survival in Patients With HCC.
  Ann Surg. 2021;274(6):e1209-e1217. PMID 32097166, DOI 10.1097/SLA.0000000000003803.

All three inspected at abstract level from frozen Europe PMC REST responses this episode
(abstract_only; full text not inspected). Receipts in work/refs/key-references.json; attached
source bytes: work/refs/k1.json, work/refs/k2.json, work/refs/k3.json (SHA-256 in receipt).
