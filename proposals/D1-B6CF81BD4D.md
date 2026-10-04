> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# A 24-hour mortality-review queue: late-lactate value versus the measurement process

## Substantive repair and clinical question

The parent’s fixed-capacity queue is computable, but its strongest remaining weakness is that a top-10% queue is only a ranking comparison within people who survived, remained hospitalized, and had a repeat lactate measured. That leaves two clinically different claims entangled: whether the numeric late-lactate value changes prioritization once available, and whether obtaining/reviewing a repeat lactate improves prioritization. EICU contains no validated order, specimen, result-display, clinician-view, review, or treatment timestamps. It cannot identify a causal test-ordering or review policy.

This successor therefore makes the conditional value-at-reassessment claim primary and adds a prespecified measurement-process decomposition and selection audit. It asks exactly what EICU can support: whether the numeric result already available at an L24 reassessment changes a fixed-workload mortality ranking. It does not turn that ranking result into evidence that ordering lactate or acting on a queue benefits patients.

### Primary falsifiable hypothesis

At exactly 24 hours after the first qualifying recorded norepinephrine/Levophed entry, among the frozen audited cohort with a valid baseline and repeat lactate, adding the numeric repeat lactate to a model that already contains the same non-lactate 24-hour state and repeat-lactate measurement-age variable improves within-hospital top-10% death capture by at least 3 percentage points at the same number of review slots.

For hospital h, let n_h be the frozen-cohort size and k_h=ceil(0.10 n_h). Let Q_age,h be the k_h people with the highest calibrated risk from R_age and Q_value,h the k_h people with the highest calibrated risk from R_value. Ties are broken by ascending patientunitstayid. D=1 is hospitaldischargestatus=Expired and D=0 is Alive.

Capture10(Q)=sum_h sum_{i in Q_h} D_i / sum_i D_i
Delta10_value=Capture10(Q_value)-Capture10(Q_age).

The locked hypothesis is H_value: Delta10_value >= 0.03. The 3-point margin is approximately 15 of the 507 deaths in the audited cohort. Use a two-sided 95% copied-hospital bootstrap interval, refitting the complete outer and inner procedures in every replicate. Quota, margin, clocks, models, and tie rule are fixed before results.

This is a conditional modeled ranking estimand: if a hospital has a defined 10%-capacity review queue at L24 and repeat lactate is already available, does the numeric value change prioritization enough to capture more eventual hospital deaths? It is not a treatment effect, test-ordering effect, review-benefit effect, or survival claim.

## Evidence-supported and unresolved claims

The inherited executed EICU work supports feasibility of the strict temporal cohort and supports serial lactate as an association/predictive signal for subsequent hospital discharge mortality in this selected population. The audited cohort is exactly 1,229 people, 507 deaths, 722 survivors, and 33 hospitals after the specified pressor, landmark, laboratory, outcome, and site gates. That does not establish this queue effect, its 3-point materiality, a clinically chosen capacity, or benefit from action.

The unresolved claim is H_value. The process decomposition distinguishes:

- R_-age: all common non-lactate snapshot features, excluding repeat-lactate measurement age;
- R_age: R_-age plus repeat measurement age, as in the parent no-value comparator;
- R_value: R_age plus ln(F) and ln(F)^2, where F is valid repeat lactate.

The primary contrast is R_value versus R_age. R_age versus R_-age is a process diagnostic, not a causal estimate. Report all three queue memberships, Capture10 and Capture20, and paired rank switches. If the process contrast is large while the value contrast is small, the result is measurement-process dependence, not evidence that the lactate value itself warrants a queue.

Required evidence is the four bound EICU tables, all rows needed to reproduce the cohort/features, catalog and schema hashes, exact L24 clocks, hospital labels, and discharge status. Unavailable evidence includes actual norepinephrine administration/dose, repeat-lactate ordering/specimen timestamps, assay validity, clinician visibility, review action/capacity, death time/cause, treatment changes, limitations of care, preferences, workload, harms, and outcomes under a review policy.

## Frozen population and clocks

No row-level sampling is allowed; chunking is memory management only and source files are read-only.

1. From patient.csv.gz, map literal or numeric age >89 to 90, retain age >=18, and use patientunitstayid, uniquepid, gender, hospitalid, hospitaldischargeoffset, and hospitaldischargestatus.

2. From infusionDrug.csv.gz, among adults, find each earliest infusionoffset in [0,1440] whose case-folded drugname contains norepinephrine or levophed. Call it t0. The inherited audit found 16,299 qualifying stays at this stage; execution must report every stage count.

3. Per uniquepid, retain the lexicographically smallest (t0, patientunitstayid). Define L24=t0+1440 minutes.

4. Require hospitaldischargestatus in {Alive,Expired} and hospitaldischargeoffset >= L24. Set D from discharge status. No death time or cause is inferred.

5. Baseline B is a valid lab row with case-folded/trimmed labname=lactate, labmeasurenamesystem=mmol/L, finite labresult in [0.2,30], labresultoffset in [t0-360,t0], and labresultrevisedoffset <=t0+60. At each collection time retain the greatest eligible revision; invalidate differing values tied at the final revision; collapse identical ties to smallest labid; select latest valid collection. Require B>=2.

6. Follow-up F uses the same analyte, unit, range, revision/conflict/tie rules, labresultoffset in [t0+720,L24], and labresultrevisedoffset <=L24. Select collection nearest t0+1080, then earlier collection, then smallest labid. A row revised after L24 is unavailable even if collected earlier.

7. Apply the inherited outcome-blind hospital gate: each retained hospital has at least five people with clearance 1-F/B >=0.20 and at least five below 0.20. Clearance is only a site gate, never a predictor, outcome, subgroup, adjustment, or rescue.

8. Freeze hospitals and expect exactly 1,229 people, 507 deaths, 722 survivors, and 33 hospitals. The audit found one conflicting final-revision baseline collection, six identical final-revision baseline duplicates, no final-revision follow-up conflict/duplicate, and no discharge exactly at L24. Do not use the prohibited L24+60 revision deadline.

The queue is formed once at L24. Outcome is hospital discharge death after L24 eligibility, not 24-hour mortality or time-to-death. The cohort is conditional on an early recorded pressor, continued hospitalization to L24, baseline and repeat measurement, and the site gate; the pressor row is not verified administration or dose.

### Measurement-process selection audit

Do not change the main cohort or labels. Separately construct an outcome-blind availability frame from the adult, one-person, first-pressor stays after steps 1–3. For each member, record discharge/L24 eligibility, valid B, valid F under the L24 revision deadline, and site-gate membership. Report stage counts and hospital distributions. Descriptively compare age, gender, t0, hospital, and discharge eligibility between the frozen cohort and frame members excluded by each availability stage. Do not reweight, adjust, select subgroups, or use outcomes for training/gating. If D is available, report it only descriptively. This audit quantifies selection by repeat measurement and continued observation; it does not identify a causal measurement effect.

## Predictors and decision-snapshot contract

All models use the parent fixed laboratory-plus-physiology feature set, with only the stated decomposition. No clearance, B-by-F interaction, feature selection, extra counts, or outcome transformation.

Common predictors: age and age squared; Female and Male indicators with Other/Unknown omitted; t0/1440 and square; baseline collection lag (t0-B_offset)/360; ln(B) and ln(B)^2; for each fixed non-lactate lab key, latest valid value in [t0,L24], measurement age, and missing indicator; and for heartrate, respiration, and sao2 in vitalPeriodic, last, median, minimum, maximum, count of unique valid timestamps, and no-valid-observation indicator from [L24-360,L24]. R_age and R_value additionally contain (L24-F_offset)/720; only R_value contains ln(F) and ln(F)^2.

Fixed laboratory keys are potassium|mmol/L, sodium|mmol/L, chloride|mmol/L, BUN|mg/dL, glucose|mg/dL, creatinine|mg/dL, bicarbonate|mmol/L, calcium|mg/dL, Hgb|g/dL, platelets x 1000|K/mcL, WBC x 1000|K/mcL, albumin|g/dL, total bilirubin|mg/dL, paO2|mm Hg, paCO2|mm Hg, and pH with missing or blank labmeasurenamesystem.

For all labs, enforce finite coercion, exact analyte/unit/window/range, revision deadline, conflict invalidation, duplicate collapse, and latest-collection rules. Any selected lab row revised after L24 is unavailable. For vitalPeriodic accept heart rate 20–250/min, respiration 2–80/min, SpO2 40–100%; at each patient/timestamp invalidate contradictory valid values and collapse identical ties to smallest vitalperiodicid. Counts are resolved timestamps, not export rows; use observationoffset <=L24. Missing streams retain missing values, count zero, and indicator one. vitalPeriodic has no entry, validation, display, or bedside-view timestamp.

Report inherited coverage: heartrate 1,218/1,229 (99.10%), respiration 1,126/1,229 (91.62%), SpO2 1,176/1,229 (95.69%). A row’s existence is not evidence of clinician visibility.

## Hospital-held-out modeling and calibration

Use unchanged 33-fold leave-one-hospital-out analysis. Fit R_-age, R_age, and R_value on other hospitals as unweighted L2 logistic regression with intercept, C=1, lbfgs, max_iter=10000, tol=1e-8, no class weighting, seed 20260961.

Per outer fold, winsorize continuous predictors at training 1st/99th percentiles; standardize by training mean and population SD; mean-impute missing continuous predictors after scaling to zero; do not scale missing indicators. A feature with no finite training values or zero post-winsorization SD fails the fold; no feature may be dropped.

Construct inner hospital out-of-fold predictions for each outer-training person with the same features, preprocessing, and settings. Fit separate two-parameter Platt recalibrators using unweighted L2 logistic regression of D on (1,logit(praw)), same solver/C/tolerance/seed. Apply only to outer predictions: q=logistic(a+b*logit(praw)). Before every logit clip finite probabilities to [1e-15,1-1e-15]; nonfinite is failure. Inner-fit failure is noncomputable, with no raw fallback. Outer outcomes never affect training, calibration, thresholds, or feature choices.

Primary pairing is q_value versus q_age in the same person/hospital; process pairing is q_age versus q_-age. All use the same folds, bootstrap draws, and tie-breaking. Calibration guardrails for every model: pooled calibration-in-the-large absolute risk difference <=0.05; pooled calibration slope from D ~ 1+logit(q) in [0.80,1.20]; and >=80% of hospitals with finite n, mean q, and observed death rate within 0.10 risk units.

Computability also requires exact cohort counts, >=1,000 people, >=30 hospitals, >=200 deaths and survivors, both outcomes per hospital, maximum hospital share <=15%, physiology gates, finite positive training variation for every feature in every fold, one finite q per model/person, and matching catalog/source hashes and headers.

## Queue estimands, baselines, uncertainty

For each m in {-age,age,value}, select k_h=ceil(0.10 n_h) within each hospital by descending q_m, ties ascending patientunitstayid. Selection uses only q, n_h, and identifier; never D, clearance, or audit results.

Primary output is Delta10_value=Capture10(q_value)-Capture10(q_age). Report Capture10, flagged count, sensitivity, precision, false positives, deaths not flagged, paired additions/removals, hospital-specific deltas, and Capture20 with k_h20=ceil(0.20 n_h) for all three models. Report Delta10_process=Capture10(q_age)-Capture10(q_-age), rank-switch fractions, and raw models descriptively only.

q_age is the mandatory baseline because it has the same measurement-process feature and differs from q_value only by numeric repeat-lactate value. q_-age is process diagnostic. Treat-all/none are not queue baselines. Retain the parent secondary calibrated decision-curve diagnostic at p=0.30,0.35,...,0.50 for R_age/R_value: NB=TP/N-FP/N*p/(1-p), with the exact parent trapezoid average divided by threshold width 0.20. It cannot relabel H_value.

Use 2,000 copied-hospital bootstrap replicates, seed 20260961. Sample hospitals with replacement, keep each original/copy as one held-out group and exclude it from appropriate training, refit outer models, inner calibration, and queues, and calculate all paired Capture10/Capture20 contrasts. At least 95% replicates must be finite/converged. Report percentile intervals for value/process contrasts and sensitivities. Fixed-prediction leave-one-hospital-out deletions report contrasts, calibration intercept/slope, and guardrail pass rates; >=80% finite deletions must retain a positive full-cohort value contrast for a supportive label. Deletions are diagnostics, not rescue.

## Falsification, labels, and interpretation

Apply computation gates first.

- Not computable: any source/header/hash, frame, cohort, timing, revision, feature, fold, calibration, prediction, queue, bootstrap, or deletion gate fails. Do not substitute random patient splits, pooled folds, raw probabilities, altered revision deadlines/windows/quotas, or another endpoint.
- Supportive conditional value: all gates and guardrails pass; the 95% copied-hospital interval lower bound for Delta10_value is >=+3 points; >=80% finite deletions are positive; and full-cohort Capture20 is not directionally opposite. Report the process contrast. This supports only calibration-compatible modeled incremental re-ranking of numeric late-lactate value at fixed L24 capacity.
- Measurement-process dependent: primary value is supportive but the process contrast is at least as large, or the value contrast loses positive direction after the prespecified process diagnostic. This cannot support ordering or measurement-policy claims.
- Calibration-failed/operationally uninterpretable: interval meets +3 but a value or baseline calibration guardrail fails.
- Opposite: primary interval upper bound <0; this opposes incremental value re-ranking for this comparator, quota, and selected population.
- Adverse to materiality: upper bound <+3 but >=0; this rejects the 3-point margin, not every smaller gain.
- Inconclusive: interval spans +3 without another branch, deletion direction unstable, process contrast materially discordant without a clean opposite result, or Capture20 directionally opposite without primary interval wholly below zero.

Supportive wording must be “calibration-supported modeled incremental queue re-ranking conditional on an already available repeat lactate.” Never claim lactate should be ordered, queue review improves survival, the test proves occult hypoperfusion, review is beneficial, or the result was visible. Adverse/opposite rejects this fixed conditional ranking claim, not all physiologic/prognostic information. The process audit is not confounding adjustment; only a prospective clinically adjudicated or randomized measurement policy can identify an ordering effect.

## Unavailable clinical evidence and next study

EICU cannot establish actual norepinephrine administration/dose/indication, repeat-lactate order/specimen/assay/result/display/view, clinician-directed versus deterioration-triggered measurement, time/cause of death, limitations of care, goals of care, review meaning/action/burden, staffing at 10%, treatment benefit/safety/workload/cost/preferences, or external transportability. Informatic adjudication is needed for pressor semantics, specimen/assay identity, and revision semantics. Clinician/stakeholder elicitation is needed for capacity and review action. Prospective external validation must predefine workflow, assay, order/result/display/review timestamps, slots, and horizon; prospective policy-impact study, ideally randomized, is needed for mortality, safety, workload, and cost.

## Exact read-only source bindings

Catalog: [internal dataset path], [source checksum].
EICU snapshot: [source checksum].

All four inputs are read-only ordinary gzip CSVs, no archive member. Join key is patientunitstayid; uniquepid is only for one-person selection; hospitalid defines gate, folds, bootstrap clusters, and deletions. Offsets are ICU-relative minutes.

1. patient.csv.gz, table patient, source [internal dataset path] 2.0 data/patient.csv.gz, [source checksum]. Required columns patientunitstayid, patienthealthsystemstayid, uniquepid, age, gender, hospitalid, hospitaldischargeoffset, hospitaldischargestatus; relevant time fields hospitaldischargeoffset and ICU-relative offsets.

2. infusionDrug.csv.gz, table infusionDrug, source [internal dataset path] 2.0 data/infusionDrug.csv.gz, [source checksum]. Required columns infusiondrugid, patientunitstayid, infusionoffset, drugname; time field infusionoffset.

3. lab.csv.gz, table lab, source [internal dataset path] 2.0 data/lab.csv.gz, [source checksum]. Required columns labid, patientunitstayid, labresultoffset, labname, labresult, labmeasurenamesystem, labresultrevisedoffset; time fields labresultoffset and labresultrevisedoffset.

4. vitalPeriodic.csv.gz, table vitalPeriodic, source [internal dataset path] 2.0data/vitalPeriodic.csv.gz, [source checksum]. Required columns vitalperiodicid, patientunitstayid, observationoffset, sao2, heartrate, respiration; time field observationoffset. No entry, validation, display, or bedside-view timestamp exists.

The executable must resolve this exact catalog path and fail rather than substitute a similar Unicode path. Other EICU tables and HCC/MIMIC/UKB are not pooled: their presence does not supply a validated mortality-review action, utility, or causal treatment record.

## Outputs and verifier boundaries

Write only derived/aggregate workspace files: catalog/source/header/hash manifest; availability-frame flow; exact cohort flow; revision/conflict/tie audit; feature/snapshot manifest; private fold predictions and inner parameters; calibration metrics; three-model queue membership; Capture10/Capture20, precision, death-not-flagged, process-decomposition, paired-switch, decision-curve, bootstrap, deletion, deterministic-label, and structured-claim files. Never modify sources or publish person-level rows/notes.

The verifier must recompute hashes, headers, joins, age/t0/one-person selection, L24 eligibility/outcome, revision deadlines and conflicts/ties, availability frame, cohort, features and timestamp resolution, fold-only preprocessing, all three nested models/calibration/clipping, queues/ties, metrics, decomposition, guardrails, bootstrap/deletions, and labels. Fixtures must cover supportive conditional-value, measurement-process-dependent, calibration-failed, opposite, adverse, inconclusive, and not-computable outputs. Reject numerically correct results paired with claims of survival benefit, ordering indication, occult-hypoperfusion proof, treatment/safety benefit, bedside visibility, or external transportability. The verifier can check computation and conclusion-to-output consistency; it cannot establish queue appropriateness, assay validity, review burden, causal benefit, safety, patient preference, or missing adjudications.
