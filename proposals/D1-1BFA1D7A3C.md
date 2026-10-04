> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Capacity-response value of late lactate for a 24-hour mortality-review queue

## Unresolved question and substantive advance

At a fixed 24-hour reassessment after an early recorded norepinephrine/Levophed entry, does adding a repeat lactate change which patients should occupy a scarce mortality-risk review queue across a range of prespecified queue capacities?

The valid parent, [prior hypothesis], made the decision layer computable by comparing top-10% within-hospital queues at the same capacity. Its unresolved limitation is that a single 10% quota is arbitrary and cannot show whether an apparent gain is useful only at one resource constraint. This successor tests the capacity-response relationship directly: 5%, 10%, 15%, and 20% of each hospital's eligible cohort, with the same number of slots under the comparator and late-lactate models at every capacity. The result can inform whether any modeled re-ranking advantage is robust to the amount of review capacity a service can actually staff.

This is a fixed-capacity ranking estimand. EICU contains no mortality-review action, queue, workload, cost, clinical utility trade-off, or bedside-visibility timestamp. Thus even a supportive result is not clinical utility, benefit, safety, or a recommendation to order lactate.

## Strongest supported claim and the new hypothesis

The strongest available evidence is the executed prior EICU analysis recorded by the parent: an earlier 1,084-person/31-hospital analysis found a positive modeled decision-value difference after adding observed late lactate to entry lactate and retrospective APACHE-IVa predicted mortality (+1.982 per 100, bootstrap interval +0.483 to +3.351), and the stricter audit established that the exact inherited cohort can be reconstructed with 1,229 people, 507 deaths, 722 survivors, and 33 hospitals. That evidence supports feasibility and the possibility that serial lactate contains prognostic information against a sparse comparator. It does not establish a calibrated fixed-capacity queue gain, its persistence across capacities, or any benefit from acting.

The unresolved claim is that, in the exact inherited EICU risk set, adding late lactate to the frozen laboratory-plus-cardiorespiratory comparator produces a positive and material average improvement in hospital-death capture across 5%, 10%, 15%, and 20% within-hospital review capacities.

For hospital h and capacity c, let k_h(c)=ceil(c n_h), select the k_h(c) people with the largest held-out calibrated risk, and break equal-risk ties by ascending patientunitstayid. Let Capture_c(q) be deaths among selected people divided by all deaths in the full cohort. Define the primary capacity-response estimand DeltaCurve = (Delta_0.05 + Delta_0.10 + Delta_0.15 + Delta_0.20)/4, where Delta_c=Capture_c(q1)-Capture_c(q0). The primary materiality margin is +2.0 percentage points in death capture, averaged equally over the four predeclared capacities. The hypothesis is DeltaCurve >= +2.0 percentage points, with the interval and guards below determining the label. The capacities and margin are fixed before execution and are not selected from results.

A capacity-specific secondary table must report the paired differences at all four capacities, flagged counts, capture, sensitivity, precision, false positives, deaths not flagged, and queue membership changes. It cannot rescue a failed primary claim.

## Population, outcome, and time boundaries

No row-level sampling is allowed; chunking is memory management only.

1. Read EICU patient.csv.gz. Map literal > 89 and numeric age > 89 to 90 and retain age >=18.
2. In infusionDrug.csv.gz, among adult stays, identify the earliest infusionoffset in [0, 1440] whose case-folded drugname contains the literal norepinephrine or levophed. Call this t0. The parent audit found 16,299 qualifying stays before one-person selection.
3. Per uniquepid, retain the lexicographically smallest (t0, patientunitstayid); define L24=t0+1440 minutes.
4. Require hospitaldischargestatus in {Alive,Expired} and hospitaldischargeoffset >= L24.
5. Define baseline lactate B from lab.csv.gz: case-folded/trimmed labname=lactate, labmeasurenamesystem=mmol/L, finite labresult in [0.2,30], labresultoffset in [t0-360,t0], and labresultrevisedoffset <= t0+60. At each collection time retain the greatest eligible revision; invalidate differing values tied at that final revision; collapse identical ties to the smallest labid; select the latest valid collection. Require B>=2.
6. Define follow-up lactate F with the same analyte, unit, range, revision/conflict/tie rules, labresultoffset in [t0+720,L24], and labresultrevisedoffset <= L24. Select the collection nearest t0+1080, then the earlier collection, then smallest labid.
7. Apply the inherited outcome-blind hospital gate: each retained hospital must have at least five people with clearance (1-F/B)>=0.20 and at least five below 0.20. Clearance is a cohort gate only; it is not a predictor, subgroup, estimand, or rescue analysis.
8. Freeze the hospitals and define D=1 iff hospitaldischargestatus=Expired; otherwise D=0.

The independently audited target is exactly 1,229 people, 507 deaths, 722 survivors, and 33 hospitals. The audit found one conflicting final-revision baseline collection (invalidated), six identical final-revision baseline duplicates (collapsed), no final-revision follow-up conflict or duplicate, and no discharge exactly at L24. The prohibited alternate common revision deadline L24+60 must not be substituted.

This selected population conditions on an early recorded pressor row, survival/continued hospitalization to L24, measured baseline and repeat lactate, data-release timing, and the site gate. The pressor row is not verified administration or dose. D is hospital discharge status after L24, not an adjudicated death time or cause.

## Predictors and comparator

R0 is the frozen laboratory-plus-physiology comparator. It includes age and age squared; Female and Male indicators with Other/Unknown omitted; t0/1440 and its square; baseline collection lag (t0-B_offset)/360; ln(B) and ln(B)^2; follow-up measurement age (L24-F_offset)/720; for each fixed non-lactate laboratory key, the latest valid value in [t0,L24], its measurement age, and a missing indicator; and for each of heartrate, respiration, and sao2 in vitalPeriodic, last, median, minimum, maximum, count of unique valid timestamps, and a no-valid-observation indicator from [L24-360,L24].

The fixed non-lactate keys are potassium|mmol/L, sodium|mmol/L, chloride|mmol/L, BUN|mg/dL, glucose|mg/dL, creatinine|mg/dL, bicarbonate|mmol/L, calcium|mg/dL, Hgb|g/dL, platelets x 1000|K/mcL, WBC x 1000|K/mcL, albumin|g/dL, total bilirubin|mg/dL, paO2|mm Hg, paCO2|mm Hg, and pH with missing or blank labmeasurenamesystem. R1 adds only ln(F) and ln(F)^2. Do not add clearance, B-by-F interaction, extra counts, feature selection, or outcome-derived transformations.

For labs, use finite numeric coercion and the exact analyte, unit, window, revision, conflict, duplicate, and collection-selection rules above. For vitalPeriodic, accept heart rate 20-250/min, respiration 2-80/min, and SpO2 40-100%; at each patient/timestamp invalidate contradictory valid values and collapse identical valid ties to the smallest vitalperiodicid. Counts are resolved timestamps, not export rows. Missing streams retain missing values, count zero, and indicator one. Exclude observations after L24. The parent audit found coverage of 1,218/1,229 (99.10%) for heart rate, 1,126/1,229 (91.62%) for respiration, and 1,176/1,229 (95.69%) for SpO2, all above the 80% gates. vitalPeriodic has no entry, validation, or display timestamp; exact bedside visibility is unavailable.

## Leakage-safe model and queue computation

Use unchanged 33-fold leave-one-hospital-out outer prediction. In each fold fit R0 and R1 on the other hospitals as unweighted L2 logistic regression with intercept, C=1, lbfgs, max_iter=10000, tol=1e-8, no class weighting, seed 20260961.

For every outer-training set, generate inner hospital-out-of-fold predictions using the same feature definitions and preprocessing. Fit separate two-parameter Platt recalibrators for R0 and R1 by unweighted L2 logistic regression of D on (1, logit(raw prediction)); apply only to the held-out hospital. Clip finite probabilities to [1e-15,1-1e-15] before logit; nonfinite values are failures. Do not use outer outcomes for fitting, recalibration, capacities, ties, or feature choices. Pool exactly one finite q0 and q1 per person.

Winsorize continuous predictors at training 1st/99th percentiles; standardize using training mean and population SD; mean-impute missing continuous predictors after scaling to zero; do not scale missing indicators. A feature with no finite training values or zero post-winsorization SD makes the fold noncomputable; no feature may be dropped.

For each outer-held-out hospital independently and for each c in {0.05,0.10,0.15,0.20}, choose k_h(c)=ceil(c n_h) people using q0 and q1 separately. Equal-risk ties are broken by ascending patientunitstayid. The q0 and q1 queues therefore have identical capacity within each hospital. Queue formation uses only q, n_h, and patientunitstayid and is outcome-blind. Report paired membership changes and all four capacity-specific capture differences. Treat-all and treat-none violate a fixed capacity and are secondary decision-curve diagnostics only.

## Computability gates and uncertainty

Require matching source hashes, schema headers, and exact cohort flow: >=1,000 people, >=30 hospitals, >=200 deaths, >=200 survivors, both outcomes at every hospital, maximum hospital share <=15%, all physiology coverage gates, finite positive training variation for every feature in every outer fold, one finite prediction per person/model, all four capacity cells, and valid convergence of nested fitting.

The primary interval is a two-sided percentile 95% interval for DeltaCurve from 2,000 copied-hospital bootstrap replicates with seed 20260961. Sample the 33 hospitals with replacement. Copies of one original hospital remain one held-out group and all copies are excluded from that fold's training set. Refit preprocessing, R0/R1, inner cross-fitting, recalibration, and all four queues in every replicate. At least 95% of replicates must be finite and converged. Also report fixed-prediction leave-one-hospital-out deletions with capacity-specific and curve differences, pooled calibration intercept/slope, and site pass rates; at least 80% of finite deletions must have positive DeltaCurve for supportive classification. Deletions are diagnostics, not a rescue.

For both q models, require calibration-in-the-large absolute risk difference <=0.05; pooled calibration slope in [0.80,1.20]; and at least 80% of hospitals with finite mean prediction and observed death rate within 0.10 risk-scale units of one another. These probability guards support interpretation of the risk ranking but do not turn the queue into clinical utility.

## Prespecified interpretation and falsification

Apply computation gates before labels.

- Supportive: all gates and both calibration guardrails pass; the copied-hospital 95% interval lower bound for DeltaCurve is >=+2.0 percentage points; at least 80% of finite hospital deletions have positive DeltaCurve; every capacity-specific point estimate is nonnegative; and no capacity-specific interval has an upper bound <0. This supports a calibrated modeled late-lactate re-ranking advantage that is directionally robust across the four fixed capacities in this selected EICU network.
- Calibration-failed / operationally uninterpretable: the DeltaCurve lower bound meets +2.0 but a calibration guardrail fails. The ranking result may be an association, but calibrated probability and queue interpretation are not accepted.
- Opposite: the DeltaCurve interval upper bound is <0. This opposes incremental late-lactate re-ranking across the prespecified capacity curve.
- Adverse to materiality: the interval upper bound is <+2.0 but >=0, without an earlier branch. This falsifies the locked average two-point materiality claim, not every smaller gain or every capacity.
- Inconclusive: the interval spans +2.0 without meeting another branch, deletion direction is unstable, or capacity-specific results are materially discordant without a clean opposite result.
- Not computable: any source/header/hash, cohort, timing, feature, fold, calibration, prediction, queue, bootstrap, or deletion gate fails. Do not replace the cohort, windows, capacities, tie rule, model, calibration, outcome, or uncertainty method.

Support is reported only as “calibration-supported modeled queue re-ranking across prespecified capacities.” It cannot be reported as improved survival, clinical benefit, occult-hypoperfusion detection, a reason to order repeat lactate, a validated mortality-review policy, or proof that q was visible before a decision. Adverse or opposite results reject the fixed incremental ranking claim in this selected setting, not all prognostic information in lactate. Inconclusive results require an independent cohort with predeclared capacity and workflow definitions.

## Evidence limits and next study

The experiment can check exact cohort construction, temporal eligibility, laboratory revision and conflict rules, leakage-safe model fitting, calibrated predictions, queue membership, capacity-specific death capture, copied-cluster uncertainty, and the deterministic label. It cannot establish arterial versus venous specimen, assay identity or validity, actual norepinephrine administration/dose, ordering indication, device validity, clinician view time, intervening fluids/vasopressors/source control, treatment changes, limitations of care, death time/cause, workload, cost, patient preferences, acceptable false-positive burden, or external transportability. It cannot estimate the causal effect of ordering or acting on repeat lactate.

Clinical informatics adjudication is required for specimen/assay semantics, pressor semantics, and display/order timestamps. Clinicians and stakeholders must determine whether 5-20% review capacities, the intended review action, and the two-point margin are operationally meaningful. A prospective external validation should preregister the capacity curve, assay/workflow, and action/view timestamps. A prospective impact study, ideally randomized for a policy change, is required to determine whether ordering or acting changes survival, safety, workload, or cost.

## Exact source bindings and provenance

Catalog: [internal dataset path], [source checksum].

EICU snapshot: [source checksum]. All inputs are read-only ordinary gzip CSV files; no archive member is used.

- [internal dataset path] 2.0 data/patient.csv.gz; table patient; schema datasets/eicu/table-ab037c09d7df9a3c.json; [source checksum]; required columns patientunitstayid, uniquepid, age, gender, hospitalid, hospitaldischargeoffset, hospitaldischargestatus; time fields hospitaldischargeoffset and ICU-relative offsets.
- [internal dataset path] 2.0 data/infusionDrug.csv.gz; table infusionDrug; schema datasets/eicu/table-18e1a8caaa91eb44.json; [source checksum]; required columns infusiondrugid, patientunitstayid, infusionoffset, drugname; time field infusionoffset.
- [internal dataset path] 2.0 data/lab.csv.gz; table lab; schema datasets/eicu/table-79bdb33275339b1a.json; [source checksum]; required columns labid, patientunitstayid, labresultoffset, labname, labresult, labmeasurenamesystem, labresultrevisedoffset; time fields labresultoffset, labresultrevisedoffset.
- [internal dataset path] 2.0 data/vitalPeriodic.csv.gz; table vitalPeriodic; schema datasets/eicu/table-a22c6d6981a32279.json; [source checksum]; required columns vitalperiodicid, patientunitstayid, observationoffset, sao2, heartrate, respiration; time field observationoffset.

All four tables join on patientunitstayid; uniquepid is used only for one-person selection; hospitalid defines gates, outer and inner folds, bootstrap clusters, and deletions; all offsets are minutes from ICU admission. Other configured datasets remain directly available but are not pooled because clocks, outcomes, measurement processes, and units are not harmonized. The source catalog and complete EICU metadata were inspected. The research-ambition README was inspected; its demonstrations were treated as examples rather than evidence, and the unavailable cancer main article/full STAR Methods were not claimed as read.
