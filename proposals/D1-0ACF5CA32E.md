# Episode 79 successor: is numeric repeat-lactate queue value robust across review capacity?

## Unresolved question, importance, and advance

At a fixed 24-hour reassessment after an early recorded norepinephrine/Levophed entry, some ICU patients have a repeat lactate and others do not. The selected Episode 78 parent asks whether the numeric repeat value improves a hospital-held-out top-10% seven-day mortality-review queue after the repeat-observation process—availability, age, missingness, and contemporaneous non-lactate surveillance—is already represented. A single 10% quota is operationally understandable but arbitrary: a ranking signal useful only at that cut point may not inform hospitals with tighter or broader review capacity.

The strongest evidence available before this experiment is narrower. The indexed full record for Baysan et al. (2022; DOI 10.1097/CCE.0000000000000750; PMCID PMC9444407; frozen Europe PMC search source [source checksum]) reports 4,440 measured adults with sepsis and a modest rise in recalibrated APACHE-IV C-statistic from 0.62 to 0.64 after adding 24-hour lactate. It conditioned on an available 24-hour lactate and did not compare numeric value with a model representing repeat availability. The inspected full-text XML review by Sisk et al. (2021; DOI 10.1093/jamia/ocaa242; PMCID PMC7810439; frozen source [source checksum], [source checksum]) establishes that informative presence/observation is common in routine health data and that missing indicators and observation summaries are common predictive approaches; it does not validate the EICU proxies as clinician attention or establish this queue result.

Thus the supported claim is only that numeric late lactate and observation processes can be prognostic. The unresolved claim is:

**Primary falsifiable hypothesis H-curve:** in the frozen all-baseline/L24 EICU population, adding the numeric repeat-lactate value to a process-adjusted model yields an equal-capacity-scenario mean of at least 3 additional seven-day in-hospital deaths per 100 review slots over prespecified within-hospital capacities 5%, 10%, 15%, and 20%, with no adverse capacity, availability-stratum, equal-hospital, or eventual-death contradiction.

This is a substantive advance over the parent because the estimand is a prespecified capacity curve rather than one selected quota. The four capacities are equally weighted service scenarios, not estimated hospital demand or stakeholder utility. Support would justify independent prospective silent validation across actual capacity settings. It would not show that lactate should be ordered, that a result was seen, that review changes care, or that deaths are preventable.

The three papers in references/research-ambition/README.md are demonstrations of ambition only and are not evidence for H-curve. Their manifest and availability limitations were inspected. In particular, the cancer paper's main text and full STAR Methods remain unavailable and are not claimed as read.

## Frozen population and temporal boundaries

Use the complete EICU snapshot [source checksum] with no person sampling; chunking is memory management. Sources remain read-only and person-level derivatives remain private workspace files.

1. In patient, trim age; map only exact "> 89" to 90; numerically coerce other age values without capping; retain age >=18.
2. In infusionDrug, retain rows whose case-folded drugname contains "norepinephrine" or "levophed" and infusionoffset is in closed [0,1440]. Per ICU stay t0 is the smallest qualifying infusionoffset. This is a recorded row, not adjudicated administration, dose, indication, or true start.
3. Per uniquepid retain the lexicographically smallest (t0, patientunitstayid); set L24=t0+1440.
4. Require hospitaldischargestatus exactly Alive or Expired and finite hospitaldischargeoffset>=L24. Define Dinf=1 only for Expired.
5. Baseline lactate B: case-folded labname=lactate; case-folded labmeasurenamesystem=mmol/L; finite labresult [0.2,30]; labresultoffset in [t0-360,t0]; labresultrevisedoffset<=t0+60. At each collection offset retain greatest eligible revision; invalidate a final-revision tie with differing values; collapse identical ties to smallest labid; choose latest valid collection then smallest labid. Require B>=2.
6. Optional repeat F uses the same analyte, unit, value, revision, conflict, and duplicate rules; collection in [t0+720,L24] and revision by L24. Choose nearest t0+1080, then earlier labresultoffset, then smallest labid. Absence is retained.
7. Retain hospitals with >=30 eligible people and freeze them before outcomes/models. Require >=30 hospitals, >=1,000 people, >=200 eventual deaths and survivors, maximum hospital share <=15%, and both eventual classes in >=80% of hospitals. Independently reproduce the inherited audit: 2,302 people, 30 hospitals, 779 eventual deaths, 1,523 eventual survivors, 1,163 repeats. Any discrepancy requires documented source-version review, never denominator or capacity shopping.
8. Freeze high/low repeat-availability hospital strata from the median hospital F_available proportion before outcome fitting.

Set H7=L24+10,080=t0+11,520 minutes. D7=1 iff status is Expired and hospitaldischargeoffset<=H7; otherwise D7=0. Retain all eligible people: Alive discharge by H7, later Alive discharge, and Expired discharge after H7 are D7 non-events because they are known not to have an in-hospital death by H7. Reproduce 607 D7 events and 1,695 non-events, including 611 alive discharges by H7 and 1,084 still hospitalized/event-free at H7; require both D7 classes in every hospital. No post-L24 predictor or censoring weight is allowed. hospitaldischargeoffset is an administrative proxy, not an adjudicated death time; out-of-hospital deaths are unavailable.

## Variables and locked models

Fit the parent's four unweighted L2 logistic models to D7. R_state includes age and age squared; sex indicators with Other/Unknown reference; t0/1440 and square; baseline collection lag; ln(B) and square; latest valid L24 non-lactate values, ages, and missing indicators; and last/median/minimum/maximum/resolved-timestamp-count summaries for heart rate, respiration, and SpO2 in [L24-360,L24].

The 16 non-lactate streams, exact units, and valid ranges are: potassium|mmol/L|[1,10]; sodium|mmol/L|[100,180]; chloride|mmol/L|[50,150]; BUN|mg/dL|[1,300]; glucose|mg/dL|[20,1000]; creatinine|mg/dL|[0.1,20]; bicarbonate|mmol/L|[2,60]; calcium|mg/dL|[2,20]; Hgb|g/dL|[2,25]; platelets x 1000|K/mcL|[1,2000]; WBC x 1000|K/mcL|[0.1,500]; albumin|g/dL|[0.5,8]; total bilirubin|mg/dL|[0.1,50]; paO2|mm Hg|[20,700]; paCO2|mm Hg|[10,200]; pH|blank/missing unit|[6.5,8.0]. Resolve each by greatest revision available by L24, final-tie conflict invalidation, smallest-labid duplicate collapse, and latest resolved timestamp.

R_attention adds six lactate-excluded surveillance summaries over [t0+720,L24], revised by L24: ln(1+routine marker-time pairs) for the first 13 streams; ln(1+blood-gas marker-time pairs); ln(1+distinct labresultoffsets); observed-stream fraction; (L24-latest qualifying offset)/720; and no-row indicator. These are recorded-surveillance proxies, not orders, effort, concern, workload, display, or viewing.

R_process adds F_available, repeat age (L24-F_offset)/720 when available, and a missing-age indicator. R_full adds ln(F) and ln(F)^2; missing continuous F terms are training-fold imputed while availability remains explicit. The primary R_full-versus-R_process contrast therefore isolates numeric value conditional on this locked representation of observation process. R_full-R_attention and R_process-R_attention are descriptive decompositions and cannot alter the primary label.

For every outer hospital, train on all other hospitals only. In training only, winsorize continuous variables at 1st/99th percentiles, standardize with training mean and population SD, then impute continuous missing values to zero; do not scale binary indicators. Fit logistic regression with intercept, L2 penalty, C=1, lbfgs, max_iter=10,000, tol=1e-8, no class weights, seed 20260979, and no feature dropping. Score only the held-out hospital. Rank raw linear predictors; probabilities are descriptive only. Nonfinite values/scores, zero post-winsor variance, nonconvergence, or leakage make the required model noncomputable.

## Capacity-curve estimand, baselines, and uncertainty

Let C={0.05,0.10,0.15,0.20}. For each capacity c and hospital h, k_h(c)=ceil(c*n_h). Rank held-out R_full and R_process scores within hospital, ties by ascending patientunitstayid, and form Q_full,h(c) and Q_process,h(c).

For outcome o in {7,inf}, define
Delta_o(c) = [sum_h sum_{i in Q_full,h(c)} D_i^o - sum_h sum_{i in Q_process,h(c)} D_i^o] / sum_h k_h(c).
Report 100*Delta_o(c) as additional outcome-o deaths per 100 equal-capacity slots.

The primary estimand is A7=(1/4) sum_{c in C} Delta_7(c), an equal-scenario mean precision difference. The materiality margin is A7>=0.03. Report all four Delta_7(c), A7, the analogous Ainf, equal-hospital macro curve mean (average within-hospital precision contrasts across hospitals then capacities), and low/high availability-stratum curve means. Treat-all and treat-none have no meaningful equal-quota rank contrast; R_state/R_attention, process decomposition, AUROC, Brier, log loss, calibration, and measured-F-only analyses are descriptive baselines/sensitivities and cannot rescue H-curve.

At every c report queue cardinalities, events, false positives, sensitivity, unflagged events, overlap, exact ties, additions/removals, M(c)/K(c), net event gain G_o(c), and substitution yield only with its denominator. Enforce Delta_o(c)=G_o(c)/K(c)=[M(c)/K(c)]*[G_o(c)/M(c)] when M(c)>0; when M=0, Delta=0 and yield is undefined.

Use 2,000 copied-hospital refit bootstrap replicates, seed 20260979. Sample original hospitals with replacement; copies contribute copied evaluation rows and training weight, but every copy of an original remains one exclusion group so no score trains on any copy of its evaluated original. Repeat preprocessing, all four fits, predictions, four capacities, queues, decompositions, A7/Ainf, macro and strata. Percentile 95% intervals require >=1,900 finite replicates for A7, every Delta_7(c), Ainf, macro A7, and both stratum A7 values. Save joint replicate tuples and enforce algebra.

Perform fixed-design leave-one-original-hospital deletions. Support requires A7>0 in >=80% of finite deletions, each availability-stratum A7>0 in >=70%, and macro A7>0 in >=70%. Deletions do not rescue an interval.

## Ordered falsification and interpretation

Apply the first matching state:

1. **Not computable:** source/hash/header mismatch; unreconciled flow; failed population/outcome gate; changed cohort, feature, clock, capacity, quota, model, or tie rule; post-L24 or copied-hospital leakage; nonfinite/nonconvergent required fit; <1,900 finite required bootstraps; missing artifact; or algebra failure.
2. **Supportive capacity-robust numeric increment:** all gates pass; A7 lower 95% bound >=+0.03; every Delta_7(c) lower bound >=0; low/high availability and macro A7 lower bounds >=0; deletion gates pass; and Ainf lower bound >=0. This supports a material modeled numeric-value increment across the four locked capacity scenarios in this EICU snapshot.
3. **Adverse opposite direction:** A7 upper bound <0, or every capacity-specific upper bound <0.
4. **Adverse horizon tradeoff:** A7 lower bound >=+0.03 but Ainf upper bound <0.
5. **Adverse below materiality:** A7 upper bound <+0.03.
6. **Adverse capacity/process nonportability:** A7 lower bound >=+0.03 but any capacity-specific upper bound <0, or a low/high availability or macro A7 upper bound <0.
7. **Inconclusive:** every other computable pattern, including A7 spanning +0.03, any required guard interval spanning zero, or favorable points without the required bounds.

A positive average with one capacity interval spanning zero is inconclusive, not supportive; a negative point alone is not adverse unless a locked upper-bound rule is met. Secondary decompositions cannot upgrade or downgrade the primary state. Supportive, adverse, and inconclusive results all advance knowledge: respectively they motivate independent validation, falsify the direction/margin/robustness component stated, or show this snapshot cannot resolve it at the locked precision.

## Exact source bindings and evidence limits

Catalog: [internal dataset path], [source checksum]. All selected files are ordinary gzip CSV files (catalog member null/ordinary file); live headers and schemas were inspected.

- patient table: [internal dataset path] 2.0数据/patient.csv.gz; [source checksum]; schema datasets/eicu/table-ab037c09d7df9a3c.json. Required patientunitstayid, patienthealthsystemstayid, uniquepid, gender, age, hospitalid, hospitaldischargeoffset, hospitaldischargestatus.
- infusionDrug table: [internal dataset path] 2.0数据/infusionDrug.csv.gz; [source checksum]; schema datasets/eicu/table-18e1a8caaa91eb44.json. Required infusiondrugid, patientunitstayid, infusionoffset, drugname.
- lab table: [internal dataset path] 2.0数据/lab.csv.gz; [source checksum]; schema datasets/eicu/table-79bdb33275339b1a.json. Required labid, patientunitstayid, labresultoffset, labname, labresult, labmeasurenamesystem, labresultrevisedoffset.
- vitalPeriodic table: [internal dataset path] 2.0数据/vitalPeriodic.csv.gz; [source checksum]; schema datasets/eicu/table-a22c6d6981a32279.json. Required vitalperiodicid, patientunitstayid, observationoffset, heartrate, respiration, sao2.
- optional hospital table: [internal dataset path] 2.0数据/hospital.csv.gz; [source checksum]; schema datasets/eicu/table-811df7b2ef435e12.json. Required hospitalid, numbedscategory, teachingstatus, region; no hospital descriptor enters prediction.

All clinical joins use patientunitstayid; uniquepid defines one-person selection; hospitalid defines folds, quotas, strata, bootstrap groups, and deletion units. Offsets are ICU-relative minutes. The other configured HCC, MIMIC, UKB, and remaining EICU files remain read-only and directly accessible but are not pooled because no validated cross-dataset key or harmonization exists for this pressor-entry/L24/revision-aware estimand.

The verifier can recompute hashes/headers, population flow, clocks, revision/conflict/tie handling, feature origin, fold isolation, fits, ranks, quotas, curve estimands, substitutions, bootstrap intervals, deletions, algebra, and the ordered label. It must test correct computation paired with unsupported conclusions and fixtures for supportive, opposite, horizon-tradeoff, below-margin, capacity/process-nonportable, inconclusive, zero-substitution, and noncomputable cases.

It cannot establish true drug administration or indication; specimen type/quality; order, collection, release, display, or viewing times; actual review capacity/workload; clinician action; preventability; utility; fairness; causal effects; safety; cost-effectiveness; or external transportability. EICU has no images, raw waveforms, genuine narrative note text, death cause, or post-discharge mortality. Those claims require laboratory/workflow and critical-care adjudication, stakeholder utility elicitation, synchronized prospective external validation, and an impact study or randomized trial for patient benefit.
