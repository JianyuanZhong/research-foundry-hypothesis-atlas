> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Does a worsening structured nursing-assessment acuity predict subsequent ICU deterioration and mortality beyond baseline severity and contemporaneous vitals?

A falsifiable, data-bound experiment on eICU-CRD 2.0 (new direction; table family `nurseAssessment` is unused by any delivered candidate).

## 1. Hypothesis

**H1 (falsifiable):** A rise in a composite nursing-assessment acuity score (ordinal-encoded LOC + Stimulus + Speech + Orientation + Edema) measured at an index time t predicts (a) subsequent ICU deterioration (new vasopressor start OR new mechanical ventilation within 24 h after t) and (b) ICU mortality, **incrementally beyond** a baseline model of admission APACHE score + contemporaneous vitals (mean arterial pressure, heart rate, SpO2 in the 12 h before t).

**H0:** No incremental signal — the nursing-assessment acuity change is redundant with APACHE + contemporaneous vitals (ΔAUC ≈ 0, 95% CI including 0).

**Strongest rival explanations (and the observation that separates them):**
- **R1 Reverse causation / leakage:** the nurse documents acuity *after* the deterioration has already begun (a nurse documenting "obtunded" at the same moment a vasopressor is started). *Separation:* require the acuity change at t to **precede** the outcome by ≥ 6 h (index-time control); a model using only acuity measured ≥ 6 h before the first vasopressor/vent event. If the signal disappears under the 6 h lead constraint, R1 is the driver.
- **R2 Severity confounding:** sicker patients both get worse nursing assessments and deteriorate. *Separation:* adjust for admission APACHE score (and age/sex); the incremental test is the acuity *change* beyond baseline severity.
- **R3 Documentation-intensity confounding:** hospitals/nurses who document more often generate more "changes" by chance. *Separation:* include assessments-per-stay as a covariate and test the acuity *change* (not raw count); a per-hospital documentation-density sensitivity analysis.

## 2. Scientific opening and closest inspected work

Structured nursing assessments (level of consciousness, response to stimulus, speech, orientation, edema) are documented repeatedly in the ICU and are a natural early-warning signal, yet they are almost never used as a *longitudinal change* feature in prognostic models, which instead rely on vitals and severity scores.

- **[K1] Bi et al. 2025** (AI in ICU nursing, narrative review, Digit Health) — the field is dominated by retrospective ML on MIMIC/eICU clustering around early-warning/risk prediction; reported discrimination frequently > AUC 0.80 **while calibration, external validation and human-factors evaluation were less often described**. It is a review: it does not test whether a *change* in a structured nursing-assessment field adds incremental signal beyond severity + vitals. (abstract_only)
- **[K2] Yousefifard et al. 2026** (NEWS predicting ICU outcomes, Crit Care Res Pract) — a **vitals-based** early-warning score (NEWS) reaches AUC 0.697 (admission) → 0.87 (24 h) for death and 0.936 (24 h) for adverse outcomes. This is the **contemporaneous-vitals baseline/rival** our H1 must beat. It uses vitals (consciousness as a single 0–3 item), not the rich structured nursing-assessment ordinal fields as a longitudinal change; single-center n=300. (abstract_only)
- **[K3] Martin-Loeches & Cai 2026** (Narrative-physiology discordance, Med Sci) — a position paper stating that documented clinical assessment adds only **~0.01 AUC** over established severity scores in the largest published ICU cohort, and warning that a naive "does the note add signal" test is confounded by **leakage and copy-forward** (documentation after deterioration). This sets the **null-ish prior** our ΔAUC must be compared against and the temporal-ordering control we adopt. (abstract_only)

**Gap this proposal fills:** none of the inspected works tests whether a *worsening in structured nursing-assessment acuity* (the ordinal LOC/stimulus/speech/orientation/edema fields of eICU `nurseAssessment`) predicts subsequent deterioration and mortality **incrementally beyond APACHE + contemporaneous vitals**, with explicit index-time (temporal-ordering) controls. K1 is a review, K2 is vitals-only and single-center, K3 is a position paper on free-text sentiment. The structured-nursing-acuity *change* as a prognostic feature is the untested quantity.

## 3. Population and data bindings (verified against frozen sources)

Dataset: eICU-CRD 2.0 snapshot (SHA-pinned in datasets/eicu/README.md). All offsets are **minutes relative to ICU admission** (verified in metadata + probe).

| Variable | Source file | Table | Column(s) | Join key | Time field |
|---|---|---|---|---|---|
| Nursing acuity (LOC, Stimulus, Speech, Orientation, Edema) | nurseAssessment.csv.gz (198 MB) | nurseAssessment | cellattribute, cellattributevalue | patientunitstayid | nurseassessoffset (min) |
| ICU mortality, demographics | patient.csv.gz (10 MB) | patient | unitdischargestatus, hospitalid, age, gender | patientunitstayid | unitdischargeoffset (min) |
| Severity | apachePatientResult.csv.gz (17 MB) | apachePatientResult | apachescore | patientunitstayid | (admission) |
| New vasopressor (deterioration) | infusionDrug.csv.gz (49 MB) | infusionDrug | drugname, infusionoffset | patientunitstayid | infusionoffset (min) |
| New mechanical ventilation (deterioration) | respiratoryCare.csv.gz (9 MB) | respiratoryCare | ventstartoffset, airwaytype | patientunitstayid | ventstartoffset (min) |
| Contemporaneous vitals (rival) | vitalPeriodic.csv.gz (1.8 GB) | vitalPeriodic | systemicmean, heartrate, sao2 | patientunitstayid | observationoffset (min) |

**Inclusion (pre-specified; from executed probe, probe_results.json):**
1. ≥ 1 nurseAssessment row with cellattribute='LOC' → 12,975 stays.
2. unitdischargestatus ∈ {Alive, Expired} → 12,972 stays (mortality 6.76%).
3. ≥ 1 non-null apachescore → **analysis cohort = 11,238 stays, 16 hospitals, mortality 6.97%.**
4. Exclude nurseassessoffset < 0 (pre-ICU; 173,638 rows dropped).

**Deterioration outcome (verified):** new vasopressor = first infusionDrug row with a vasopressor drugname (Norepinephrine/Vasopressin/Phenylephrine/Dopamine/Epinephrine in ml/hr, mcg/min, mcg/kg/min) at infusionoffset > 0 (21,285 such stays overall; 2,994 in the LOC cohort). New MV = respiratoryCare ventstartoffset > 0 (1,117 in the LOC cohort). Combined deterioration in the LOC cohort: **4,437 stays = 34.2%** (good event rate).

## 4. Outcomes
- **Primary:** (a) subsequent deterioration — new vasopressor OR new mechanical ventilation within 24 h after the index time t; (b) ICU mortality (unitdischargestatus == 'Expired').
- Both are binary. Deterioration is time-to-event relative to t (24 h window); mortality is at ICU discharge.

## 5. Features (pre-specified)
**Composite nursing-acuity score (per assessment):** ordinal-encode each field and sum:
- LOC: normal=0, lethargic=1, sedated=1, somnolent=2, obtunded=3, comatose=4.
- Stimulus: spontaneous=0, sound=1, pain=2, unresponsive=3.
- Speech: clear=0, garbled=1, slurred=1, inappropriate=1, dysphasic=1, aphasic=1, moan/grunt=2, none=3; **'ET/Trach' = missing** (intubated, not an acuity state).
- Orientation: to person=0, to place=1, to time=2, to situation=3; **'unable to assess' = missing**.
- Edema: no edema=0, generalized=1, anasarca=2.
- Score range 0–12. Missing fields → exclude that field's contribution and record the number of assessed fields (to control for documentation completeness).

**Acuity change:** Δacuity = score(t) − score(t−12 h), where t is the index time (the assessment nearest a pre-specified grid, e.g. every 12 h from 12 h to 72 h). Require both assessments present.

**Baseline covariates (common to baseline and full model):** admission APACHE score, age, gender, contemporaneous vitals in [t−12 h, t] (mean/min of systemicmean, heartrate, sao2 from vitalPeriodic), assessments-per-stay (documentation-intensity control).

## 6. Models (baseline vs learned alternative)
- **Baseline (M0):** multilevel logistic regression (hospital random intercept) with APACHE + contemporaneous vitals + demographics.
- **Full (M1):** M0 + Δacuity (and the level score at t as a secondary term).
- **Learned alternative:** HistGradientBoosting (xgboost not in base environment; HistGB is the available GBM — recorded) with the same features, to reveal whether the acuity effect is nonlinear/interacts with severity. The 2×2 (feature set × model class) interaction is the scientific question.
- Class weights for the imbalanced mortality outcome.

## 7. Validation scheme (pre-specified)
- **Temporal split (primary):** index time t ∈ [12 h, 72 h]; outcome window (t, t+24 h] for deterioration, discharge for mortality. No feature uses data after t (leakage control per [K3]).
- **6 h lead sensitivity:** re-estimate Δacuity using only assessments ≥ 6 h before the first vasopressor/vent event, to separate R1 (reverse causation).
- **Hospital stratification:** 16 hospitals in the cohort → hospital random intercept (primary) plus a fixed-effects sensitivity (the narrow hospital range is a limitation, stated).
- **Metrics:** AUROC (primary), calibration slope/intercept, Brier, decision-curve net benefit at 20/30/40% thresholds (deterioration) and 10/20% (mortality).
- **Primary estimand:** ΔAUC = AUC(M1) − AUC(M0) per outcome, with 1,000 stay-level bootstrap resamples → 95% CI. NRI/IDI as secondary.

## 8. Analysis
1. Build the acuity time series per stay; compute Δacuity on the 12 h grid.
2. Fit M0 and M1 (logistic + HistGB) on the temporal split.
3. ΔAUC with bootstrap CI; calibration; DCA.
4. 6 h lead sensitivity (R1 test); fixed-effects sensitivity (hospital range).
5. HistGB feature importance (SHAP if available) for M1.

## 9. Falsification criteria
- **Supportive (H1):** ΔAUC > 0 with 95% CI excluding 0 for ≥ 1 outcome AND ≥ 1 model class, AND the signal persists under the 6 h lead constraint (not fully explained by R1). Compare the magnitude to the [K3] ~0.01 AUC prior: a ΔAUC materially above 0.01 is a substantive advance; ≤ 0.01 is consistent with the prior.
- **Adverse (H0):** ΔAUC CI includes 0 (or ΔAUC < 0) — the nursing-acuity change is redundant with APACHE + vitals; the structured-assessment signal is not incremental.
- **Inconclusive:** < 200 deterioration events in the index window, or |ΔAUC| < 0.005, or the 6 h lead constraint removes the entire signal (cannot separate R1 from a true effect).

## 10. What results would and would not establish
- **Supportive:** a worsening structured nursing-assessment acuity carries incremental prognostic signal beyond severity + vitals for this dataset/outcome; such documentation could be used as an early-warning input. Would NOT establish causality (assessment → deterioration) or that the effect holds for other outcomes (LOS, decompensation) or datasets (MIMIC).
- **Adverse:** the structured nursing-acuity change is redundant with vitals/severity; the [K3] ~0.01 AUC prior holds for structured (not just free-text) documentation.
- **Inconclusive:** insufficient power or the signal is entirely a leakage artifact; motivates a larger index window or a different documentation family.

## 11. Limitations
- Observational; no causal claim about nursing assessment.
- Only **16 hospitals** in the LOC cohort (nurseAssessment is present in a subset of eICU sites) → narrow random-intercept range; fixed-effects sensitivity required.
- 'ET/Trach' and 'unable to assess' treated as missing, not states.
- Single time period (eICU 2014–2015); no temporal drift.
- The acuity score is a composite; individual-field contributions are secondary.
- Documentation intensity is a proxy; the assessments-per-stay covariate only partially controls R3.

## 12. Resource budget (discovery ≠ solver)
- CPU only. Data build: one pass over nurseAssessment (198 MB, ~17 s measured) + patient + apache + infusionDrug + respiratoryCare + a bounded vitalPeriodic sample. Feature matrix ≈ 11k × ~20 floats. Model fitting < 10 min. Bootstrap 1,000 × 4 models ≈ 20–40 min. **Total < 2 h CPU, no GPU.** Solver envelope: same order; no GPU requirement.

## 13. Solver deliverables (what must be fitted/estimated)
- Acuity time series + Δacuity matrix (parquet/csv) with provenance and inclusion audit.
- Per-model in-sample AUROC, calibration, Brier, DCA; ΔAUC with 95% CI (4 model×feature combinations × primary split + 6 h lead + fixed-effects sensitivities).
- Feature importance for M1-HistGB.
- Reproducible script + fixed seeds.
Completion is established by the ΔAUC estimate with CI and the 6 h lead sensitivity, not by any single AUROC.

## 14. Key references (inspected; frozen bytes attached)
- **[K1]** Bi A, Li T, Cheng G, Hu J. Artificial intelligence applications in intensive care unit nursing: A narrative review (2020-2025). Digit Health. 2025;11:20552076251406302. doi:10.1177/20552076251406302. (abstract_only)
- **[K2]** Yousefifard M, Heydarzadeh Jazi M, Esmaeili M, Asgari P. Investigating the Predictive Power of the National Early Warning Score in Predicting Outcomes Among Intensive Care Unit Patients. Crit Care Res Pract. 2026;2026:3647049. doi:10.1155/ccrp/3647049. (abstract_only)
- **[K3]** Martin-Loeches I, Cai H. From Sentiment to Signal: Narrative-Physiology Discordance as a Testable Target for Artificial Intelligence in Critical Care. Med Sci (Basel). 2026;14(5):595. doi:10.3390/medsci14050595. (abstract_only)
