> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Sustained hyperoxia burden in the first 24 h of vasopressor-treated ICU stays: an independent prognostic marker, and does pulmonary status modify the association?

**Dataset:** eICU-CRD 2.0 (local snapshot) · **Parent seed:** `[prior hypothesis]` ([starting question])
**Status:** complete, bounded, falsifiable study proposal with verified data bindings (measured counts from job `[research job]`, script `work/episode4-measure.py`, outputs `work/episode4-measurements.json` / `.md`).

---

## 1. Unresolved question and why it matters clinically

**Question.** In ICU patients receiving vasopressor infusions in the first 24 h, when oxygenation is adequate, does *sustained* hyperoxia burden — time with PaO2 ≥ 150 mmHg (and, secondarily, time with FiO2 ≥ 0.6) in 0–24 h — add independent prognostic information for in-hospital mortality beyond severity, and does the association differ by pulmonary status (mechanical ventilation / pulmonary diagnosis)?

**Why it matters.** Oxygen is the most commonly administered "drug" in the ICU, and default high FiO2 is common practice in ventilated, vasopressor-treated patients. If sustained hyperoxemia in the first 24 h is an *independent* prognostic marker — especially if stronger in pulmonary disease — it (a) gives clinicians a bedside-quantifiable exposure to track and possibly titrate, (b) informs which patients should be prioritized in oxygen-target trials, and (c) clarifies whether hyperoxia is a toxicity signal or merely a marker of illness. The largest recent RCT in this space (UK-ROX [K2]) randomized a conservative SpO2 target in 16,500 ventilated patients and found **no 90-day mortality benefit** (adjusted risk difference 0.7 pp, 95% CI −0.7 to 2.0). A null trial of a *target strategy* does not tell us whether the *measured burden* of severe hyperoxemia (PaO2 ≥ 150 sustained for hours) carries prognostic information, nor whether that information is concentrated in pulmonary patients — the question this study addresses.

**Evidence already supporting part of the claim.** Observational work in eICU cardiac-arrest patients found 24-h hyperoxic PaO2 trajectories associated with higher in-hospital mortality after adjustment (aRR up to 1.20) [K3], and a mixed CICU cohort found a J-shaped admission-PaO2–mortality association (aOR 1.17 per 100 mmHg; PaO2 > 300 vs 60–100 aOR 2.37) (Jentzer et al. 2024, PMID 39025170 — supporting citation, not a key reference). These use **static admission values or trajectory groups** in **restricted populations** (post-arrest, cardiac ICU). The unresolved claim is whether a *time-integrated burden* measure in the *broader vasopressor-treated population* is independently prognostic and whether pulmonary status modifies it.

## 2. Rival explanations and the observable comparison that separates them

| # | Explanation | Prediction on the pre-specified comparisons |
|---|---|---|
| R1 | **Hyperoxia toxicity** (oxidative injury; worse with pulmonary disease) | Adjusted association with mortality **stronger in the ventilated / pulmonary-diagnosis subgroup** than in non-ventilated / non-pulmonary (interaction OR > 1, significant); association persists after severity adjustment. |
| R2 | **Severity/prognosis marker** (hyperoxia reflects low O2 consumption, refractory shock, end-organ failure) | Association **persists after severity adjustment** (age, sex, APACHE, shock type) and is **similar or stronger in non-pulmonary shock** (interaction ≈ 1 or < 1); effect driven by the most severe patients. |
| R3 | **Practice artifact** (default high FiO2 in ventilated patients; hospital-specific oxygen culture) | Association **disappears or nearly disappears after adjusting for ventilation + severity**, or is **hospital-specific** (leave-one-hospital-out estimates unstable; effect concentrated in a few hospitals). |

**Observable comparison that separates them.** The design separates R1 from R2 with the **ventilation × hyperoxia-burden interaction** (R1: interaction > 1; R2: interaction ≈ 1 or < 1) and separates R3 from both with (i) attenuation after adding the ventilation indicator and (ii) **leave-one-hospital-out consistency** (R3: unstable/hospital-specific; R1/R2: stable across hospitals). Note the estimand: conditioning on "adequate oxygenation" (PaO2 available, ≥ 6 h coverage) changes the population to one in which hyperoxia is *measured*; the comparison is prognostic, not causal (see §8).

## 3. Population, temporal boundaries, variables, outcome, exclusions

All offsets are minutes from unit admission; the study window is **[0, 1440]**. Join key everywhere: `patientunitstayid`. Source dir (read-only): `[internal dataset path]`.

**Inclusion (primary, PaO2-based):**
1. ≥ 1 vasopressor infusion row in `infusionDrug.csv.gz` with `infusionoffset` ∈ [0,1440] and `drugname` matching (case-insensitive) `norepinephrine|epinephrine|vasopressin|phenylephrine|dopamine|angiotensin|dobutamine|milrinone` → **22,614 stays** (measured; the Lead's unwindowed count was 26,234 — the difference is the [0,1440] window).
2. ≥ 2 `paO2` rows in `lab.csv.gz` (`labname == 'paO2'`) with `labresultoffset` ∈ [0,1440] and numeric `labresult` → **10,770 stays** (measured).
3. **Adequate oxygenation / coverage:** ≥ 6 h of PaO2 coverage, i.e. (last − first PaO2 offset) ≥ 360 min → **7,996 stays** (measured).

**Secondary (FiO2-based):** same vasopressor criterion plus ≥ 2 FiO2 respcharting rows in `respiratoryCharting.csv.gz` (`respchartvaluelabel` ∈ {'FiO2','FIO2 (%)','O2 Percentage'}, `respchartoffset` ∈ [0,1440]) → **14,564 stays**; union with PaO2-based → **15,980 stays** (measured).

**Outcome.** In-hospital mortality: `patient.hospitaldischargestatus` starting with 'EXPIRED' (case-insensitive). Distinct values verified in the full patient table: `Alive` (181,104), `Expired` (18,004), blank (1,751). Blank = censored/unknown, excluded from the denominator. **Measured event counts:** PaO2-based population n=10,770, deaths=3,084 (28.6%); primary analysis population (≥ 6 h coverage) n=7,996, deaths=2,408 (ventilated 1,664/5,819 = 28.6%; non-ventilated 744/2,177 = 34.2%).

**Exclusions:** no vasopressor in window; < 2 PaO2 rows in window; < 6 h PaO2 coverage (primary); `hospitaldischargestatus` blank (outcome); `age` missing or < 18 (recorded, not excluded — eICU is adult); multiple unit stays per patient (one row per `patientunitstayid`; index-stay logic per eICU-CRD documentation [K1]).

**Variables with exact bindings:**

| Variable | Table / column(s) | Definition |
|---|---|---|
| Hyperoxia burden (primary exposure) | `lab.csv.gz`: `labname='paO2'`, `labresultoffset`, `labresult` | Hours in [first, last] PaO2 measurement within 0–24 h with interpolated PaO2 ≥ 150 mmHg. **Linear interpolation** between consecutive measurements; time above threshold computed analytically per segment; **censored at the last measurement** (no extrapolation beyond it); require ≥ 6 h coverage. Measured distribution (n=7,996): median 0.0 h, p75 0.16 h, p90 5.96 h, max 23.6 h; 21.4% of stays ≥ 1 h, 9.95% ≥ 6 h, 3.5% ≥ 12 h. |
| Hyperoxia burden (secondary) | `respiratoryCharting.csv.gz`: FiO2 labels above | Hours with FiO2 ≥ 0.6 in [first, last] FiO2 measurement in 0–24 h, same interpolation/censoring rules, ≥ 6 h coverage. (FiO2 values may be recorded as fraction or percent; unit-normalization rule: value > 1.5 treated as percent and divided by 100 — to be verified on the first solver pass and documented.) |
| Mechanical ventilation | `respiratoryCare.csv.gz`: `ventstartoffset`, `airwaytype` | Ventilated if any `ventstartoffset` ∈ [0,1440] **or** any `airwaytype` matching `intubat|et tube|ETT|tracheostomy|trach` (case-insensitive). Measured: 71.8% of PaO2-based population. |
| Pulmonary diagnosis | `admissionDx.csv.gz` (`admitdxtext`) + `diagnosis.csv.gz` (`diagnosisstring`) | Any text matching (case-insensitive) `pneumonia|respiratory failure|respiratory arrest|acute respiratory distress|ARDS|pulmonary edema|pulmonary embolism|pulmonary embolus|atelectasis|pleural effusion|pneumothorax|asthma|COPD|chronic obstructive pulmonary|pulmonary fibrosis|pulmonary hypertension|pulmonary disease|bronchitis|aspiration pneum|tracheobronch`. Measured: 56.6% of PaO2-based population. |
| Severity | `apachePatientResult.csv.gz`: `apachescore` | Treated as a covariate, **not** a validated score: prior episode observed range 0–211. Primary analysis uses the raw value; sensitivity analysis winsorizes at 1st/99th percentiles and additionally refits with the score excluded. |
| Shock type | `infusionDrug.csv.gz`: `drugname` of in-window vasopressor rows | Categories: norepinephrine-based, vasopressin-based, catecholamine-mixed, other; plus inotropic-only (dobutamine/milrinone) flag. |
| Demographics | `patient.csv.gz`: `age`, `gender`, `hospitalid`, `unittype` | Age continuous (spline in sensitivity), sex binary, hospital as cluster. |

**Actual sampling/filtering record:** full-table scans of the seven files above (no sampling); window [0,1440]; regexes as listed; no rows discarded beyond the stated exclusions. Runtime ~80 s on 8 CPUs.

## 4. Analysis plan

**Primary estimand.** In the PaO2-based, ≥ 6 h coverage population (n=7,996; 2,408 deaths), the **adjusted odds ratio for in-hospital mortality per additional 1 h of PaO2 ≥ 150 burden**, and equivalently per quartile (Q4 vs Q1), estimated in a **hospital-clustered (GLMM) logistic model**.

**Baseline model (M0):** age, sex, APACHE score, shock type, mechanical ventilation, pulmonary diagnosis, hospital (random intercept).

**Augmented model (M1):** M0 + hyperoxia burden (continuous, and quartile in sensitivity). Primary contrast: coefficient of burden in M1; model comparison M0 vs M1 (likelihood-ratio test, change in AUC/c-index with 95% CI via bootstrap).

**Interaction (pre-specified):** M1 + burden × ventilation and burden × pulmonary-diagnosis (two separate interaction terms, each tested; both reported). This is the comparison that separates R1 (interaction > 1) from R2 (interaction ≈ 1 or < 1).

**Cross-hospital consistency:** leave-one-hospital-out refits of M1 (125 hospitals with events; report the distribution of the burden coefficient, its range, and the fraction of folds with the same sign; hospitals with < 20 events reported descriptively only).

**Secondary analyses:** (i) FiO2 ≥ 0.6 h burden in the FiO2-based population (n≈14,564, 4,168 deaths); (ii) union population with an oxygenation-source indicator; (iii) APACHE winsorized/excluded sensitivity; (iv) burden restricted to the first 6 h vs 6–24 h; (v) gradient-boosted trees (below).

**Multiple comparisons:** the interaction, quartile and secondary analyses are confirmatory-of-the-primary or descriptive; the primary claim requires the continuous-burden coefficient in M1.

## 5. Pre-specified supportive / adverse / inconclusive criteria

Tied to measured events (primary population: 2,408 deaths / 7,996; ventilated 1,664/5,819; non-ventilated 744/2,177):

- **Supportive of independent prognostic value (R1/R2):** adjusted OR per 1 h burden **≥ 1.05 with 95% CI excluding 1.0** in M1, **and** the M1 c-index exceeds M0 by **≥ 0.005**, **and** ≥ 80% of leave-one-hospital-out folds have the same sign. If additionally the ventilation (or pulmonary) interaction OR > 1 with CI excluding 1 → supportive of the **toxicity-predominant (R1)** reading; if interaction ≈ 1 (CI crossing 1) with a persistent main effect → supportive of the **severity-marker (R2)** reading.
- **Adverse (against independent value / for R3):** adjusted OR per 1 h **≤ 1.02 with 95% CI crossing 1.0**, or the M1 c-index gain **< 0.005**, or ≥ 20% of leave-one-hospital-out folds flip sign → the association is **not independently prognostic** in this population (practice-artifact or null reading).
- **Inconclusive:** OR between 1.02 and 1.05 with CI crossing 1, or c-index gain 0.002–0.005, or interaction CI spanning 0.5–2 → underpowered or too heterogeneous to decide; report as such and specify what additional data (e.g., longer follow-up, FiO2-concordant pairs, external cohort) would be needed.

A null main effect with a *significant* interaction is a valid, reportable result (heterogeneity without a main effect) and is not treated as failure.

## 6. Method comparison: interpretable baseline vs learned alternative

**Baseline (primary):** hospital-clustered logistic regression (GLMM) with the burden term and pre-specified interactions. Chosen because the scientific question is *prognostic association and effect modification*, where a coefficient and its interaction are directly interpretable, pre-specifiable, and auditable; with ~2,408 events and ~10 covariates the events-per-variable ratio is adequate.

**Learned alternative (secondary, pre-specified):** gradient-boosted trees (e.g., LightGBM/XGBoost, CPU) on the same features plus burden, with hospital as a categorical feature and 5-fold hospital-blocked cross-validation for the c-index; then partial-dependence and SHAP interaction values for burden × ventilation and burden × pulmonary diagnosis.

**What the alternative could reveal that the baseline loses:** (i) **nonlinearity** of the burden–mortality dose-response (e.g., threshold at ~6 h, where 9.95% of stays sit — the linear term cannot express this); (ii) **higher-order or asymmetric effect modification** (burden × ventilation × pulmonary dx) that a two-way interaction model cannot capture; (iii) a realistic check on whether tree-learned "hyperoxia importance" is an artifact of severity confounding (compare SHAP values of burden vs APACHE).

**Why the primary remains the interpretable model:** the falsification criteria (§5) are stated in terms of an adjusted OR and interaction OR; a black-box c-index gain cannot distinguish R1/R2/R3. The tree model is a sensitivity analysis for nonlinearity and heterogeneity, not the primary claim.

**Deferred alternatives and revisit criteria:**
- *Survival analysis with time-to-death* (eICU has `hospitaldischargeoffset`): deferred because the outcome is in-hospital mortality (binary) per the seed's framing; revisit if a substantial fraction of deaths occur after 24 h and a time-varying-exposure formulation (burden in 0–24 h predicting later death) becomes the question.
- *Marginal structural models / inverse-probability weighting* to move toward a causal reading of "reducing hyperoxia burden": deferred — requires modeling the treatment (oxygen titration) process, which eICU charting cannot fully support (no FiO2–PaO2 concordant decision data); revisit with a dataset containing paired FiO2 and PaO2 over time or an RCT.
- *Trajectory modeling (GBTM) of PaO2* as in [K3]: deferred — trajectory groups are hard to pre-specify and less interpretable than the burden integral; revisit if the linear-burden analysis is null but the p90–p75 gap (5.96 vs 0.16 h) suggests a high-burden subgroup effect.
- *GPU/sequence models*: not scientifically useful here — the exposure is a single scalar per stay; no sequence structure justifies the cost.

## 7. Limitations

1. **SpO2 cannot quantify hyperoxemia** (per the seed): SpO2 saturates near 100%, so hyperoxemia is only measurable via PaO2 (arterial blood gas) or high FiO2; this restricts the population to stays with ≥ 2 ABGs in 24 h (10,770 of 22,614 vasopressor stays) and introduces **selection** — ABGs are drawn for sicker, more monitored patients.
2. **Interpolation assumptions:** linear interpolation between sparse ABGs (median burden 0 h; p90 5.96 h) can misestimate short hyperoxic episodes; censoring at the last measurement means burden is a *lower bound* on true 24-h burden.
3. **APACHE field range:** observed 0–211 in a prior episode; the score is used as a covariate with winsorization sensitivity, not as a validated severity index.
4. **Vasopressor unit heterogeneity:** drug rates are recorded in mixed units (ml/hr, mcg/min, mcg/kg/min); shock-type categorization is therefore coarse, and dose intensity is not used.
5. **FiO2 unit ambiguity:** respcharting may record fraction or percent; the normalization rule must be verified before the secondary analysis.
6. **Observational design:** the estimand is prognostic association in a selected (monitored) population; hyperoxia is a treatment choice confounded by severity and practice.
7. **Single snapshot, 2014–2015, US:** oxygen practices may have shifted since; no external validation.

## 8. What would require additional data or another study

- **Causal claims** ("reducing hyperoxia burden improves survival") require an RCT or a design with credible treatment-assignment modeling (MSM with rich FiO2/PaO2 decision data) — not supported by this dataset.
- **External validation** of the burden–mortality association (MIMIC-IV has ABG and FiO2 data and is a natural candidate) requires a separate study.
- **Mechanistic claims** (oxidative injury) require biomarkers or animal work; this study can only localize the association to pulmonary vs non-pulmonary patients.
- **Clinical adjudication** of whether a given hospital's oxygen practice is "default high FiO2" (R3) cannot be established from charting alone; hospital-level descriptive reporting is the limit of what this data supports.

## Key references (3 inspected works; see `work/key-references.json` for receipts and hashes)

- **[K1]** Pollard T, Johnson AEW, Raffa JD, Celi LA, Mark RG, Badawi O. *eICU Collaborative Research Database (version 2.0).* PhysioNet, 2019. doi:10.13026/C2WM1R. — Documents the multi-center database (200k+ admissions, 208 hospitals, 2014–2015) including labs, treatments, APACHE and diagnoses; supports availability of all tables bound here. (Full documentation page text inspected; frozen snapshot attached.)
- **[K2]** Martin DS, Gould DW, Shahid T, et al. (UK-ROX Investigators). *Conservative Oxygen Therapy in Mechanically Ventilated Critically Ill Adult Patients: The UK-ROX Randomized Clinical Trial.* JAMA. 2025;334(5):398–408. doi:10.1001/jama.2025.9663. PMID 40501321. — Bounds the toxicity claim: a conservative SpO2 strategy (−29% oxygen exposure) did **not** reduce 90-day mortality (adjusted RD 0.7 pp, 95% CI −0.7 to 2.0). (Abstract only; full text not inspected.)
- **[K3]** Hu J, Zhong L, Zong D, Lu J, Xie B, Ji X. *A study of the trajectory of arterial oxygen tension dynamics after successful resuscitation of cardiac arrest patients and its impact on prognosis.* Zhonghua Wei Zhong Bing Ji Jiu Yi Xue. 2025;37(9):843–847. doi:10.3760/cma.j.cn121430-20241015-00843. PMID 41146506. — The consequential rival/limitation: in 3,866 eICU cardiac-arrest patients, 24-h hyperoxic PaO2 trajectories were associated with higher in-hospital mortality after adjustment (aRR up to 1.20), showing hyperoxia can mark severity/prognosis in a restricted eICU population — but not in the broader vasopressor population and not stratified by pulmonary status. (Abstract only; full text not inspected.)

Additional supporting citation (not a key reference): Jentzer JC, et al. *Arterial hyperoxia and mortality in the cardiac intensive care unit.* Curr Probl Cardiol. 2024;49(10):102738. PMID 39025170 — J-shaped admission-PaO2–mortality association in a mixed CICU cohort (aOR 1.17 per 100 mmHg; PaO2 > 300 aOR 2.37 vs 60–100).
