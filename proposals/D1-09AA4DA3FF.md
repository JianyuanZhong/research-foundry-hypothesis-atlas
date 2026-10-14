> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Successor hypothesis: persistent discordant AKI recovery beyond current state

Status: provisional research task, not a completed analysis. No cohort counts, event rates, effect estimates, or clinical conclusions are claimed.

## Proposed relationship

Among adults with an ICU stay and a prespecified creatinine-defined AKI episode who survive and remain observable at a fixed 48-hour landmark, a persistent pattern of creatinine improvement without concurrent urine-output improvement will identify higher subsequent risk of renal deterioration or in-hospital death than concordant recovery, after adjustment for the same landmark severity, treatment state, and observation intensity.

The unresolved claim is incremental prognostic information from a persistent trajectory. It is not a claim about renal mechanism, fluid status, causal treatment effect, or proof of true recovery.

## Evidence and rival explanations

The inherited evidence supports the measurement concern: creatinine-based estimates can be misleading during critical illness, while KDIGO-style AKI assessment combines creatinine and urine output. The closest inspected landmark work used creatinine, urine output, AKI stage, and severity to predict clinician-driven CRRT initiation, but treated that outcome as non-objective and did not establish this discordant-recovery association. These sources motivate the question; they do not support the proposed result.

The leading rival is that discordance is a proxy for current illness severity, diuretic or vasopressor exposure, differential urine-measurement intensity, or noise in one creatinine/urine summary. A current-state baseline can capture the landmark level and immediate slope but loses persistence, ordering, and co-movement. A trajectory alternative can reveal whether those temporal features add information beyond the current state. If the alternative does not improve held-out prediction or calibration, the data do not support the incremental claim.

## Exact MIMIC-IV bindings

Use only the read-only MIMIC-IV 3.1 archive:
`[internal dataset path]`
[source checksum]; catalog snapshot `[source checksum]`.

Required archive members and catalog schemas:
- `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`: `subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod`.
- `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`: `subject_id, hadm_id, admittime, dischtime, deathtime, hospital_expire_flag` plus admission context.
- `mimic-iv-3.1/hosp/d_labitems.csv.gz`, table `hosp/d_labitems`: `itemid, label, fluid, category`.
- `mimic-iv-3.1/hosp/labevents.csv.gz`, table `hosp/labevents`: `labevent_id, subject_id, hadm_id, itemid, charttime, storetime, value, valuenum, valueuom`.
- `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`: `subject_id, hadm_id, stay_id, intime, outtime, los`.
- `mimic-iv-3.1/icu/d_items.csv.gz`, table `icu/d_items`: `itemid, label, abbreviation, linksto, category, unitname`.
- `mimic-iv-3.1/icu/outputevents.csv.gz`, table `icu/outputevents`: `subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valueuom`.
- `mimic-iv-3.1/icu/inputevents.csv.gz`, table `icu/inputevents`: `subject_id, hadm_id, stay_id, starttime, endtime, itemid, amount, amountuom, rate, rateuom, statusdescription`.
- `mimic-iv-3.1/icu/procedureevents.csv.gz`, table `icu/procedureevents`: `subject_id, hadm_id, stay_id, starttime, endtime, itemid, value, valueuom, statusdescription`.

Join `hosp/patients` to `hosp/admissions` by `subject_id`; join admissions to `icu/icustays` by `subject_id, hadm_id`; join ICU event tables by `stay_id), with `subject_id, hadm_id` retained for consistency checks. Join lab rows to `hosp/d_labitems` and ICU event rows to `icu/d_items` by their respective `itemid`. Use only timestamps at or before the landmark for predictors: `labevents.charttime`, `outputevents.charttime`, `inputevents.starttime/endtime`, and `procedureevents.starttime/endtime`. MIMIC timestamps are subject-specific shifts; do not align patients across subjects by calendar date.

Use creatinine item `itemid=50912` from `hosp/labevents`, after verifying its label in `hosp/d_labitems`. Use urine-output items `226559, 226560, 226561, 226563, 226567, 226627` from `icu/outputevents`, verifying labels in `icu/d_items`; exclude `227489` GU irrigant/urine output from the primary definition. Treatment context may use verified inputevent items norepinephrine `221906`, epinephrine `221289`, phenylephrine `221749`, dopamine `221662`, vasopressin `222315`, furosemide `221794`, bumetanide `229639`, NaCl 0.9% `225158`, and NaCl 0.45% `225159`; these are context, not validated fluid status. Identify RRT in `icu/procedureevents` using `225441` hemodialysis, `225802` CRRT, `225803` CVVHD, `225809` CVVHDF, and `225955` SCUF; peritoneal dialysis `225805` is secondary. The exact AKI threshold, urine normalization, minimum coverage, and deterioration adjudication rules must be frozen before fitting.

## Population and outcomes

Restrict to adults (`anchor_age >= 18`) in the earliest eligible ICU stay with a creatinine-defined AKI episode. Define AKI with a prespecified KDIGO-compatible rule from serial creatinine, using a baseline and time-window rule fixed before cohort construction. Require survival, continued observation, and adequate pre-landmark measurements at 48 hours after the AKI anchor. Predictors are frozen at that landmark.

Primary outcomes after the landmark are renal deterioration (prespecified creatinine/urine-output worsening or verified RRT initiation) and hospital death. Secondary analyses may separate creatinine-only worsening, urine-output worsening, and RRT, but cannot substitute for adjudicated clinical deterioration. Report the number eligible, number with adequate coverage, discordant/concordant cells, and outcome counts before fitting.

## Baseline versus trajectory alternative

Baseline: a landmark logistic or Cox model with current creatinine, creatinine slope, urine-output summary, AKI stage, age/sex, severity, treatment state, and measurement intensity.

Alternative: a compact trajectory model using pre-landmark creatinine and urine-output sequences, including slopes, nadir, persistence, and co-movement, with the same patients, split, outcomes, and uncertainty procedure. It can reveal whether persistence and ordering contain information lost by a current-state summary. It cannot establish mechanism. CPU is adequate for both; GPU is not required unless the trajectory implementation becomes unexpectedly matrix-intensive.

Use identical patient-level temporal splits, held-out evaluation, calibration, discrimination, and uncertainty estimates. Sensitivity analyses vary reasonable landmark/coverage rules and adjust or stratify by urine-measurement density, diuretic/RRT exposure, and current severity. Support requires a prespecified directionally consistent association and reproducible incremental calibration/discrimination in held-out data, not explained solely by missing urine measurements, treatment exposure, or current severity. Adverse results are no incremental signal, reversal, or instability. Inconclusive results include sparse discordant cells, inadequate follow-up, or wide uncertainty.

## Missing evidence and deliverable

The future solver must newly construct the cohort, fit both models, estimate the discordance association and incremental prediction, and report held-out calibration/discrimination with uncertainty and sensitivity analyses. MIMIC lacks measured GFR, standardized cystatin C for all patients, reliable fluid-status adjudication, and complete urine measurement. Clinical adjudication of AKI/recovery and RRT indication is required before treatment or mechanistic claims. No numerical result is claimed here.
