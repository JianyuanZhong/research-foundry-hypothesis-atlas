> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Time-Weighted Hypotension Burden and Acute Kidney Injury in ICU Patients: A Multi-Hospital eICU Cohort Study

## Parent
- Expert seed `[starting question]` ([prior hypothesis])

## Unresolved Question

At the same minimum blood pressure, do patients with longer-lasting hypotension in the first 6 hours of ICU care experience more subsequent acute kidney injury (AKI)? Specifically, does time-weighted hypotension burden (duration × depth below a perfusion threshold) add independent predictive value beyond the minimum blood pressure alone, after adjusting for illness severity, and is this association consistent across hospitals?

## Clinical Importance

- Minimum blood pressure is the standard bedside trigger for vasopressor escalation, but it discards all duration information. Two patients with the same nadir SBP of 80 mmHg may have very different renal perfusion if one was hypotensive for 10 minutes versus 4 hours.
- Time-weighted hypotension burden (area under the BP curve below threshold, or time below threshold × mean depth) is a more complete exposure measure that captures both severity and duration.
- If duration at the same nadir independently predicts AKI, it supports shifting from threshold-based to burden-based monitoring in the ICU, with direct implications for vasopressor titration and nursing assessment frequency.
- eICU-CRD contains >200 hospitals, enabling a test of cross-site consistency — a key transportability question that single-center studies cannot address.

## Evidence for the Opening

Three inspected works establish the foundation:

**[K1]** Liu Z et al. (2026, Front Med) [10.3389/fmed.2026.1916589] demonstrated in 7,405 perioperative GI cancer surgery patients that cumulative duration of MAP <65 mmHg was associated with postoperative ICU admission (OR 1.78 for ≥30 min vs none), and that time-weighted area below MAP 65 mmHg was independently associated (OR 1.07 per 50 mmHg·min). This validates time-weighted hypotension burden as a meaningful, measurable exposure. **Limitation:** perioperative setting, ICU admission (not AKI) as outcome, single database.

**[K2]** Ao Q et al. (2026, Clin Interv Aging) [10.2147/CIA.S615407] showed in 1,248 hospitalized older adults with AKI that a three-dimensional dynamic MAP framework (onset value, change rate, recovery time) improved prediction of major adverse kidney events at 90 days (AUC 0.71→0.76). Failure to recover MAP within 72h was independently associated with worse outcomes (HR 1.71). **Limitation:** single center, older adults only, exploratory, retrospective.

**[K3]** Flick M et al. (2026, Br J Anaesth) [10.1016/j.bja.2026.04.042] prospectively quantified postoperative hypotension in 1,002 noncardiac surgery patients: 37.7% had MAP <65 mmHg, with median cumulative duration 180 min and median area below 65 mmHg of 836 mmHg·min. Participants with hypotension had higher rates of AKI and unplanned ICU admission. **Limitation:** postoperative ward (not ICU), single center, AKI was a secondary/exploratory outcome.

**Gap:** No study has tested whether time-weighted hypotension burden in the *first hours of ICU care* (as opposed to perioperative or postoperative settings) independently predicts AKI beyond minimum BP, in a multi-hospital cohort with hierarchical adjustment for hospital-level practice variation.

## Hypothesis

In ICU patients with ≥20 blood pressure measurements in the first 6 hours, time-weighted hypotension burden (time below SBP 90 mmHg in the first 6h) is independently associated with KDIGO-defined AKI within 72h, beyond the minimum SBP, after adjusting for APACHE IV score, age, sex, and vasopressor use, with a consistent direction of effect across hospitals.

## Study Design

### Population
- ICU stays from eICU-CRD (2.0) with:
  - ≥20 systolic BP readings in the first 6 hours (offset 0–360 min) of ICU stay
  - ≥1 creatinine measurement in the first 6 hours (baseline)
  - ≥1 creatinine measurement between 6h and 72h (for AKI assessment)
  - APACHE IV score available
  - Hospital ID available

### Exposure (first 6h, offset 0–360 min)
- **Primary:** Time below SBP 90 mmHg (minutes) — computed from vitalPeriodic readings
- **Secondary:** Time-weighted area below SBP 90 mmHg (mmHg·min) — Σ(max(0, 90 − SBP_i) × Δt_i)
- **Baseline comparator:** Minimum SBP in the same window

### Outcome
- **Primary:** KDIGO AKI within 72h of ICU admission:
  - Creatinine rise ≥0.3 mg/dL from baseline, OR
  - Creatinine ≥1.5× baseline
  - Baseline = first creatinine in first 6h
  - AKI assessed using lab values with offset between 360 and 4320 min

### Covariates
- APACHE IV score (apachePatientResult.apachescore)
- Age, sex (patient.age, patient.gender)
- Vasopressor use in first 6h (infusionDrug: norepinephrine, epinephrine, vasopressin, phenylephrine, dopamine, dobutamine)
- Hospital (random intercept)

### Analysis
1. **Descriptive:** Distribution of hypotension duration, min SBP, AKI incidence by hospital
2. **Univariable:** AKI rate by quartile of hypotension duration (within min SBP strata)
3. **Primary model:** Multilevel logistic regression:
   - AKI ~ min_SBP + time_below_90 + APACHE + age + sex + vasopressor + (1 | hospital)
   - Test: is time_below_90 significant after min_SBP?
4. **Secondary model:** Replace time_below_90 with area_below_90
5. **Hospital consistency:** Direction of effect in ≥80% of hospitals with ≥20 patients
6. **Sensitivity:** MAP <65 mmHg threshold; exclude patients with <10 SBP readings in first 6h

### Falsification Criteria
- **Adverse (hypothesis not supported):** time_below_90 is not significantly associated with AKI (p > 0.05) after adjusting for min_SBP and covariates, in the primary model.
- **Inconclusive:** Significant association in the full cohort but inconsistent direction across hospitals (<50% concordant), or significant only in one threshold definition.
- **Supportive:** time_below_90 is significantly associated with AKI (p < 0.05) after adjusting for min_SBP, with consistent direction in ≥80% of hospitals, and the association persists with MAP <65 threshold.

### What Each Outcome Would and Would Not Establish
- Supportive result: duration adds information beyond nadir BP for AKI risk in the early ICU period. Would NOT establish causality (confounding by severity, vasopressor timing) or identify an optimal intervention threshold.
- Adverse result: nadir BP captures the relevant perfusion information; duration may not matter once depth is fixed. Would NOT rule out duration effects in specific subpopulations (e.g., septic shock).
- Inconclusive result: suggests hospital-level heterogeneity or measurement limitations; would warrant investigation of recording density and artifact handling.

## Data Bindings (Verified)

| Variable | Source File | Column(s) | Notes |
|---|---|---|---|
| SBP readings | vitalPeriodic.csv.gz | patientunitstayid, observationoffset, systemicsystolic | offset in minutes; 1.78 GB |
| MAP readings | vitalPeriodic.csv.gz | systemicmean | for sensitivity analysis |
| Creatinine | lab.csv.gz | patientunitstayid, labresultoffset, labname, labresult | labname contains "creatinine" |
| Vasopressors | infusionDrug.csv.gz | patientunitstayid, drugname, drugstartoffset, drugstopoffset | drugname matches vasoactive agents |
| Hospital | patient.csv.gz | patientunitstayid, hospitalid | 200+ hospitals |
| APACHE score | apachePatientResult.csv.gz | patientunitstayid, apachescore | APACHE IV |
| Age, sex | patient.csv.gz | patientunitstayid, age, gender | |
| Discharge status | patient.csv.gz | patientunitstayid, hospitaldischargestatus | secondary outcome |

**Join key:** patientunitstayid (all tables)

## Method Comparison: Baseline vs. Learned Alternative

**Baseline (primary):** Multilevel logistic regression with fixed effects for min_SBP, time_below_90, APACHE, age, sex, vasopressor; random intercept for hospital. This directly tests the hypothesis with interpretable coefficients and hospital-level consistency.

**Learned alternative (secondary):** Gradient-boosted trees (e.g., LightGBM) with the same features, evaluated by AUC and calibration on a held-out hospital split. This could reveal:
- Non-linear interactions between hypotension duration and severity (e.g., duration matters more at intermediate nadir values)
- Whether the model learns hospital-specific patterns vs. patient-level physiology
- Feature importance ranking to confirm whether duration or nadir dominates

The learned model would NOT replace the primary analysis but would provide a sensitivity check and exploratory insight into effect modification. If the learned model shows substantially better AUC driven primarily by hospital-level features, this would suggest that the linear model's hospital random effect is insufficient and that practice-level confounding is a major limitation.

**Resource estimate:** Baseline model: <10 min CPU. Learned model: <30 min CPU for 50k–100k patients. Both well within budget.

## Alternatives Considered and Deferred

- **Seed 4 (hyperoxia):** Requires blood gas + FiO2 alignment; respiratoryCharting has FiO2 but blood gas timing is sparse in eICU. Deferred: data density insufficient for the specific question.
- **Seed 5 (ventilatory burden):** Plateau pressure likely unavailable in eICU respiratoryCharting. Deferred: key field missing.
- **Seed 8 (reduced testing → deterioration):** Interesting but requires complex temporal analysis of lab ordering patterns; deferred to a later episode.
- **Seed 10 (hospital recovery speed):** Hierarchical model, but less mechanistically clear and requires organ support definitions that are harder to operationalize in eICU.

## Limitations
1. eICU vitalPeriodic recording density varies by hospital; time-weighted burden is sensitive to measurement interval.
2. Vasopressor timing may be confounded with hypotension severity (treatment indication bias).
3. AKI definition relies on creatinine, which has delayed kinetics; early AKI may be missed.
4. No data on renal perfusion pressure directly; SBP is a surrogate.
5. Retrospective design; cannot establish causality.

## Required Additional Evidence
- Clinical adjudication of AKI cases (creatinine-based definition is standard but not perfect)
- Prospective validation in a separate cohort
- Data on renal perfusion pressure or urine output for a more complete AKI assessment

## Key References

[1] Liu Z, Wang N, Chen M, Wang H. Association between cumulative intraoperative hypotension and postoperative ICU admission after gastrointestinal lumen cancer surgery: a retrospective cohort study using the INSPIRE database. Front Med. 2026;13:1916589. DOI: 10.3389/fmed.2026.1916589. [K1]

[2] Ao Q, Zhang Y, Liu Y, et al. Individualized Dynamic Assessment of Mean Arterial Pressure in Hospitalized Older Patients with Acute Kidney Injury: A Retrospective Cohort Study. Clin Interv Aging. 2026;21:615407. DOI: 10.2147/CIA.S615407. [K2]

[3] Flick M, Stemmler S, Bossemeyer M, et al. Postoperative hypotension in patients recovering from noncardiac surgery: a prospective, blinded observational study. Br J Anaesth. 2026;137(1):66-73. DOI: 10.1016/j.bja.2026.04.042. [K3]
