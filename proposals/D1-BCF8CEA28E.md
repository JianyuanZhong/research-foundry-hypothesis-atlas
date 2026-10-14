> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Working proposal: robust discordant AKI recovery in MIMIC-IV

## Current question
In ICU patients with AKI, does creatinine-based recovery without concordant urine-output recovery identify a distinct higher-risk state for subsequent RRT escalation and 28-day mortality, beyond what creatinine recovery alone predicts?

## Why it matters
Creatinine is the standard recovery marker, but it can lag true kidney function and is affected by muscle mass, fluid status, and creatinine production. Urine output provides a complementary, more immediate functional signal. If discordant recovery carries excess risk, it could change how clinicians interpret AKI recovery and select patients for closer monitoring or RRT.

## Evidence inspected so far
- Expert seed 3: [prior hypothesis], which proposes this discordance question but lacks exact bindings and a temporal design.
- MIMIC-IV catalog: creatinine in hosp/labevents with d_labitems; urine output in icu/outputevents with d_items; fluid input in icu/ingredientevents; RRT in icu/procedureevents; mortality in hosp/admissions; patient linkage through subject_id, stay_id, and admission_id.
- The exact source archive is baidu_downloads/eicu_mimic_iv_v3.1.zip, with members mimiciv/hosp/labevents.csv.gz, mimiciv/hosp/d_labitems.csv.gz, mimiciv/icu/outputevents.csv.gz, mimiciv/icu/d_items.csv.gz, mimiciv/icu/ingredientevents.csv.gz, mimiciv/icu/procedureevents.csv.gz, mimiciv/hosp/admissions.csv.gz, and mimiciv/patients.csv.gz.

## Proposed robustness design
1. Define AKI using KDIGO creatinine criteria from hosp/labevents joined to d_labitems on itemid, subject_id, and stay_id/admission_id.
2. Define recovery at a fixed 48-hour window after AKI onset: creatinine recovery as a decline to within 0.1 mg/dL of baseline or to baseline, and urine-output recovery as a sustained increase above a prespecified threshold (e.g., >0.5 mL/kg/h) for at least 6 consecutive hours.
3. Classify four states: concordant recovery, creatinine-only recovery, urine-output-only recovery, and no recovery.
4. Compare subsequent RRT escalation (icu/procedureevents, itemid for RRT) and 28-day mortality (hosp/admissions.discharge_time minus admission_time) across states.
5. Control for baseline severity (SOFA components, APACHE components, age, sex, fluid balance, vasopressor use) and time-varying confounding with a prespecified adjustment model.
6. Sensitivity analyses: alternative recovery thresholds, alternative time windows, restriction to patients with complete urine-output recording, and exclusion of patients with baseline CKD.

## Competing explanations
- The discordance signal may reflect measurement artifact: urine output is selectively recorded, and creatinine is affected by muscle mass and fluid status.
- The signal may reflect severity: patients with discordant recovery may be sicker at baseline, and adjustment may attenuate the association.
- The signal may reflect treatment: RRT initiation may be more likely in patients with discordant recovery, creating a feedback loop.

## Method alternatives
- Baseline: prespecified logistic regression for 28-day mortality and Cox regression for time to RRT, with adjustment for baseline severity and fluid balance.
- Learned alternative: gradient-boosted trees with the same features and the same outcome, to test whether the discordance signal is captured by a flexible model and to identify interactions with severity and fluid status.
- The learned alternative could reveal nonlinear or interaction effects that the baseline loses, but it is not a substitute for the prespecified association test.

## Bounded diagnostic
A small diagnostic will estimate the number of patients with complete urine-output recording and the number of discordant states, to determine whether the study is feasible and whether the discordance signal is likely to be robust to selection.

## Key references
[K1] Comparison of Cystatin C and Creatinine in the Assessment of Measured Kidney Function during Critical Illness. This work supports the claim that creatinine can lag true kidney function and that complementary markers are needed.
[K2] KDIGO Clinical Practice Guideline for Acute Kidney Injury. This work supports the definition of AKI and recovery criteria.
[K3] A study on urine output as a marker of kidney function in critical illness. This work supports the claim that urine output is a more immediate functional signal than creatinine.

## What the study will and will not establish
- Supportive results would suggest that discordant recovery is a distinct higher-risk state, but they would not establish a causal mechanism.
- Adverse results would suggest that the discordance signal is not robust to alternative definitions or adjustment, and the question should be revised or abandoned.
- Inconclusive results would suggest that the study is underpowered or that the discordance signal is too heterogeneous to be captured by a single association test.

## Limitations
- The study cannot establish a causal mechanism for the discordance signal.
- The study is limited to MIMIC-IV and may not generalize to other populations.
- The study is limited by the selective recording of urine output and the lack of measured GFR.
