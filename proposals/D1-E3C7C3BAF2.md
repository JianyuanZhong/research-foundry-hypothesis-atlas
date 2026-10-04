# Hospital-held-out quota stability of incremental repeat-lactate review

## Child purpose and preserved estimand

This child repairs the remaining deployment weakness in both assigned parents. [prior hypothesis] tested a fixed 10% mortality-review queue and included a 20% descriptive queue; [prior hypothesis] made probability calibration a deployment requirement but used an integrated threshold utility rather than the queue estimand. Neither parent prespecified whether the incremental repeat-lactate signal remains directionally stable when review capacity is tighter or broader, nor whether probabilities remain compatible with the patients actually placed in each queue at hospitals that were unseen during fitting.

The primary scientific estimand is preserved exactly:

Delta10 = Capture10(R_value) - Capture10(R_age).

Within each eligible hospital h, the top k_h=ceil(0.10*n_h) patients are selected by descending held-out calibrated risk, with ascending patientunitstayid as the tie-breaker. The primary hypothesis remains H10: Delta10 >= 0.03, a three-percentage-point gain in eventual hospital-death capture at the same 10% review capacity.

The meaningful child addition is a locked deployment-stability panel, not a new primary estimand:

q in {0.05, 0.10, 0.20}; Delta_q = Capture_q(R_value) - Capture_q(R_age); k_h(q)=ceil(q*n_h).

The 5% and 20% contrasts are secondary quota-stability estimands. They cannot change the primary hypothesis, cohort, clocks, feature schema, outcome, margin, or comparator. All three quotas are fixed before any model result is inspected: 5% represents a scarce specialist-review queue, 10% is the inherited primary capacity, and 20% is a broader escalation queue. Whether those capacities are clinically realistic must be confirmed by clinicians and service leaders; EICU contains no staffing or review-log data.

## Clinical question and evidence boundary

The unresolved clinical deployment question is:

If a repeat lactate is already available at an L24 reassessment, does its numeric value add a calibrated, hospital-transportable prioritization signal beyond the same non-lactate state and repeat-lactate measurement age, consistently enough to support fixed-capacity mortality review?

A supportive result would advance knowledge from an in-sample or pooled ranking increment to a transportability-qualified, capacity-sensitive modeled re-ranking result. It would still not show that ordering a lactate, reviewing a flagged patient, changing treatment, or improving survival is beneficial.

The strongest supported evidence before this experiment is narrower. The inherited EICU audit supports feasibility of the outcome-blind late-lactate cohort and supports that serial lactate can be associated with subsequent hospital-discharge mortality in this selected population. The audited flow is 1,229 people, 507 deaths, 722 survivors, and 33 hospitals after the locked gates. The parents also establish why an apparent point increment is insufficient: hospital-held-out predictions can be miscalibrated, and a ranking gain at one quota need not be stable at another. The Europe PMC search performed for this proposal returned contemporary biomarker/prognostic and internal-validation work, but that literature does not supply EICU-specific review actions, clinically elicited utilities, or a transportable quota-calibration result (frozen search source ID [source checksum]; retain the query and retrieval provenance as context, not definitive evidence).

The experiment tests only the unresolved conditional predictive claim. It does not test a causal effect of repeat-lactate ordering, a treatment effect, a mortality-reduction claim, occult hypoperfusion, or a clinical utility value elicited from patients or clinicians.

## Frozen population and asymmetric clocks

Use the complete EICU snapshot, with no row-level sampling. Chunking a source file for memory is allowed only if it produces exactly the same result as a full scan. Source files remain read-only. Record every flow count and every exclusion reason.

1. From patient.csv.gz / table patient, map literal or numeric age >89 to 90 and retain age >=18. Keep patientunitstayid, uniquepid, gender, hospitalid, hospitaldischargeoffset, and hospitaldischargestatus.

2. From infusionDrug.csv.gz / table infusionDrug, among adults, identify each earliest infusionoffset in [0,1440] whose case-folded drugname contains norepinephrine or levophed. Call that offset t0. The drug row is an exposure proxy only; it is not assumed to prove administration, dose, indication, or continuous treatment.

3. For each uniquepid, retain the lexicographically smallest (t0, patientunitstayid). Define the landmark L24=t0+1440 ICU-relative minutes.

4. Require hospitaldischargestatus in {Alive,Expired} and hospitaldischargeoffset >= L24. Define D=1 for Expired, D=0 for Alive. Do not infer death time or cause.

5. Baseline B is a valid lab row with case-folded/trimmed labname=lactate, labmeasurenamesystem=mmol/L, finite labresult in [0.2,30], labresultoffset in [t0-360,t0], and labresultrevisedoffset <=t0+60. At each patient/collection offset retain the greatest eligible revision. If values conflict at the greatest revision, invalidate that collection; if tied values are identical, retain the smallest labid. Select the latest valid collection and require B>=2.

6. Follow-up F uses the same analyte, unit, range, revision/conflict/tie rules, labresultoffset in [t0+720,L24], and labresultrevisedoffset <=L24. Select the collection nearest t0+1080, then the earlier collection, then smallest labid. This asymmetric rule is essential: baseline results may be revised through t0+60, but a repeat result must be known by L24. A row collected before L24 but revised after L24 is unavailable.

7. Apply the inherited outcome-blind hospital gate: retain a hospital only if it has at least five cohort members with clearance 1-F/B >=0.20 and at least five below 0.20. Clearance is a site-eligibility rule only; never use it as a predictor, stratifier, adjustment, outcome, or rescue.

8. Recompute and report the expected audit: 1,229 people, 507 deaths, 722 survivors, 33 hospitals. The inherited audit reported one conflicting final-revision baseline collection, six identical final-revision baseline duplicates, no final-revision follow-up conflict/duplicate, and no discharge exactly at L24. These are checks, not permission to change rules. Do not use the prohibited L24+60 follow-up revision deadline.

The outcome is hospital-discharge death after the L24 eligibility requirement. It is not 24-hour mortality and not time-to-death.

## Measurement-process audit

Construct, separately and without using D for selection, the adult one-person first-pressor availability frame after steps 1-3. For each frame member record L24/discharge eligibility, valid B, valid F under the L24 revision deadline, and hospital-gate membership. Report stage counts and hospital distributions, plus descriptive age, gender, t0, hospital, and discharge-eligibility comparisons for the frozen cohort and members excluded at each stage. If D is available, report it only descriptively. Do not reweight, adjust, select a subgroup, or use the audit to alter the primary cohort. This documents selection by repeated measurement and continued observation; it cannot identify a causal ordering or measurement effect.

## Locked models and predictors

Use exactly the parent-17 decomposition:

- R_-age: common non-lactate state features only.
- R_age: R_-age plus repeat-lactate measurement age (L24-F_offset)/720.
- R_value: R_age plus ln(F) and ln(F)^2.

The primary contrast is R_value versus R_age, which holds the repeat-measurement process variable fixed. R_age versus R_-age is a process diagnostic, not a causal estimate.

Common predictors are age and age squared; Female and Male indicators with Other/Unknown omitted; t0/1440 and its square; baseline collection lag (t0-B_offset)/360; ln(B) and ln(B)^2; for each fixed non-lactate laboratory key, the latest valid value in [t0,L24], measurement age, and missing indicator; and for heart rate, respiration, and SpO2 in vitalPeriodic, last, median, minimum, maximum, count of unique valid timestamps, and no-valid-observation indicator from [L24-360,L24]. The fixed laboratory keys are potassium|mmol/L, sodium|mmol/L, chloride|mmol/L, BUN|mg/dL, glucose|mg/dL, creatinine|mg/dL, bicarbonate|mmol/L, calcium|mg/dL, Hgb|g/dL, platelets x 1000|K/mcL, WBC x 1000|K/mcL, albumin|g/dL, total bilirubin|mg/dL, paO2|mm Hg, paCO2|mm Hg, and pH with missing or blank labmeasurenamesystem.

For all laboratories enforce finite coercion, exact analyte/unit/window/range, the asymmetric revision deadlines, conflict invalidation, duplicate collapse, and latest-collection rules. For vitalPeriodic, accept heart rate 20-250/min, respiration 2-80/min, and SpO2 40-100%; at each patient/timestamp invalidate contradictory valid values and collapse identical ties to the smallest vitalperiodicid. Counts are resolved timestamps, not export rows; use observationoffset <=L24 and the stated 360-minute window. Missing streams retain missing values, count zero, and indicator one. No source row supplies an entry, validation, display, or bedside-view timestamp.

Fit each model as unweighted L2 logistic regression with intercept, C=1, lbfgs, max_iter=10000, tol=1e-8, no class weighting, seed 20260961. In every fit, winsorize continuous predictors at training 1st/99th percentiles, standardize by training mean and population SD, mean-impute missing continuous predictors after scaling to zero, and leave missing indicators unscaled. A feature with no finite training values or zero post-winsorization SD fails the fold; no feature may be dropped.

## Unseen-hospital predictions and calibration

Use unchanged 33-fold leave-one-hospital-out evaluation. Each outer test hospital is entirely unseen during model fitting and calibration.

For each outer hospital h and each model: fit the base model on the other hospitals with training-only preprocessing; within the outer training hospitals generate inner hospital-out-of-fold predictions using the same model, features, preprocessing, and solver; fit a separate two-parameter Platt recalibrator to each model's inner predictions, q=logistic(a+b*logit(p_raw)), using unweighted L2 logistic regression on (1,logit(p_raw)), C=1, lbfgs, max_iter=10000, tol=1e-8, seed 20260961; and apply the recalibrator only to the outer hospital's base predictions. Each inner prediction comes from a model that did not use that person's outcome or hospital. Clip finite probabilities to [1e-15,1-1e-15] before logit; nonfinite values or fit failure are Not computable, with no raw fallback. Outer outcomes never affect fitting, calibration, thresholds, feature choices, quota choices, or site gating.

Primary calibration guardrails are computed from pooled outer-held-out predictions for each model: calibration-in-the-large absolute risk difference <=0.05; calibration slope from D ~ 1+logit(q) in [0.80,1.20]; and at least 80% of hospitals with finite n, mean q, and observed death rate within 0.10 risk units. Report hospital-specific intercept, slope, mean predicted risk, observed risk, and sample size; these reports do not permit post hoc recalibration.

Add a quota-specific calibration compatibility diagnostic, not a replacement calibration estimator. For each model and q in {0.05,0.10,0.20}, calculate among flagged top-q people, pooled mean(q) and observed death fraction, and their difference; also report the same difference per held-out hospital. Require for a quota-compatible secondary label that the pooled absolute difference is <=0.05 and at least 80% of hospitals have absolute difference <=0.10 for both R_age and R_value at every q. This checks whether a probability attached to the reviewed subset is descriptively compatible with its observed event frequency. It does not establish clinical utility or causal calibration under a future policy.

## Queue outcomes and uncertainty

For each outer held-out hospital, model, and q, set k_h(q)=ceil(q*n_h) and select by descending q, ties ascending patientunitstayid. Selection may use only held-out q, n_h, and patientunitstayid. Never use D, clearance, the availability audit, or any result to select a queue.

For q in {0.05,0.10,0.20}, report for R_-age, R_age, and R_value: flagged count, deaths flagged, Capture_q, sensitivity, precision, false positives, deaths not flagged, and per-hospital results. Report paired additions/removals between R_value and R_age, rank-switch fractions, and Delta_q. Report raw uncalibrated models only descriptively. Retain the parent's decision-curve diagnostic at p=0.30,0.35,...,0.50 only as a secondary diagnostic; it cannot relabel H10.

The primary uncertainty is 2,000 copied-hospital bootstrap replicates, seed 20260961. Sample hospitals with replacement; preserve each original/copy as a held-out group and exclude it from the appropriate training and inner-calibration fits. Refit the complete outer and inner procedures, calibration, and all three quotas in every replicate. Store hospital-copy membership. Require at least 95% finite/converged replicates for computability and report percentile intervals for every Delta_q, calibration metric, and quota-calibration diagnostic.

For each original hospital also report its fixed-prediction held-out result and a leave-one-hospital-out deletion summary. The primary stability diagnostic is the proportion of hospitals with Delta_q,h >=0, where Delta_q,h is that hospital's death-capture difference divided by its observed deaths, for each q. A quota-stable profile requires at least 80% nonnegative hospital-specific deltas at each q and no quota-specific bootstrap interval with upper bound <0. Deletions and hospital signs are diagnostics, not rescue analyses.

## Ordered labels and falsification

Apply these rules in order.

1. Not computable: any catalog/source/header/hash mismatch; altered flow; missing key or time field; wrong age, t0, L24, discharge, revision, conflict, duplicate, feature, fold, calibration, queue, or bootstrap rule; post-L24 feature leakage; nonfinite/nonconverged required fit; incomplete held-out predictions; fewer than 2,000 valid bootstrap replicates; or any unapproved threshold/quota/model change. Do not convert this to a scientific result.

2. Supportive and quota-compatible: all computation gates and both model calibration guardrails pass; the 95% copied-hospital interval for primary Delta10 has lower bound >=+0.03; the quota profile is stable (>=80% nonnegative hospital-specific deltas at q=0.05, 0.10, and 0.20, and no quota interval upper bound <0); and quota-specific calibration compatibility passes for both models at every q. This supports only calibration-compatible incremental modeled re-ranking conditional on an already available repeat lactate, with stability over these fixed capacities.

3. Supportive primary but quota-fragile: the primary supportive conditions pass but the quota-stability or quota-calibration panel fails. This supports the fixed 10% conditional queue claim only, and argues against treating it as capacity-robust deployment evidence.

4. Opposite: all computation gates pass and primary Delta10's 95% interval has upper bound <0. This opposes incremental value for the frozen comparator, population, horizon, and 10% queue. It does not refute all lactate prognostic information.

5. Adverse to materiality: all computation and calibration gates pass, the primary interval is wholly nonnegative, but its upper bound is <+0.03. This rejects the prespecified three-point 10% materiality margin while allowing a smaller gain. If a secondary quota has an interval wholly below zero, label that quota adverse/opposite in its profile even if the primary is not.

6. Inconclusive or operationally uninterpretable: every other computable case, including an interval spanning +0.03, calibration guardrail failure, quota intervals spanning zero, unstable hospital signs, quota-calibration mismatch, or discordance between primary and quota results. A favorable point estimate, AUROC, Brier score, or one favorable hospital cannot override this label.

Supportive wording must remain “calibration-compatible modeled incremental queue re-ranking conditional on an already available repeat lactate.” Never say that lactate should be ordered, that review improves survival, that the value was visible to a clinician, or that a score is safe or beneficial.

## Exact read-only bindings

Catalog: [internal dataset path], [source checksum].

EICU snapshot: [source checksum].

All four primary inputs are ordinary gzip CSV files with no hidden archive member:

- patient.csv.gz, table patient, source [internal dataset path] 2.0数据/patient.csv.gz, [source checksum]; schema datasets/eicu/table-ab037c09d7df9a3c.json; required columns patientunitstayid, patienthealthsystemstayid, uniquepid, gender, age, hospitalid, hospitaldischargeoffset, hospitaldischargestatus; temporal field hospitaldischargeoffset; join key patientunitstayid, person key uniquepid, hospital/fold key hospitalid.

- infusionDrug.csv.gz, table infusionDrug, source [internal dataset path] 2.0数据/infusionDrug.csv.gz, [source checksum]; schema datasets/eicu/table-18e1a8caaa91eb44.json; required columns infusiondrugid, patientunitstayid, infusionoffset, drugname; temporal field infusionoffset; join key patientunitstayid.

- lab.csv.gz, table lab, source [internal dataset path] 2.0数据/lab.csv.gz, [source checksum]; schema datasets/eicu/table-79bdb33275339b1a.json; required columns labid, patientunitstayid, labresultoffset, labtypeid, labname, labresult, labresulttext, labmeasurenamesystem, labmeasurenameinterface, labresultrevisedoffset; collection/revision fields labresultoffset and labresultrevisedoffset; join key patientunitstayid.

- vitalPeriodic.csv.gz, table vitalPeriodic, source [internal dataset path] 2.0数据/vitalPeriodic.csv.gz, [source checksum]; schema datasets/eicu/table-a22c6d6981a32279.json; required columns vitalperiodicid, patientunitstayid, observationoffset, sao2, heartrate, respiration; collection field observationoffset; join key patientunitstayid.

The complete catalog confirms the four paths, schemas, columns, and ordinary-file archive status. Other EICU tables and the separately configured HCC/MIMIC/UKB datasets are not pooled: they do not contribute a validated review action, clinically elicited utility, or exchangeable time semantics.

## Outputs and verifier boundaries

Write only derived workspace artifacts: catalog/source/header/hash manifest; availability-frame flow; exact cohort flow; revision/conflict/tie audit; feature/snapshot manifest; outer and inner fold assignments; private held-out predictions and recalibration parameters; pooled and per-hospital calibration; queue membership and metrics for all q; quota compatibility; hospital signs/deletions; bootstrap membership/results; deterministic label; and a structured claim file linking each conclusion to computed output fields. Never modify sources or publish person-level rows or clinical notes.

A verifier can recompute source hashes and headers, joins, age mapping, t0/one-person selection, L24 and discharge gates, asymmetric revision rules, features, fold exclusion, calibration exclusion, probabilities, queue membership, ties, capture contrasts, bootstrap intervals, quota diagnostics, and ordered labels. It can reject leakage, post hoc quota choice, raw-probability substitution, random patient splits, altered margins, and unsupported causal or benefit language.

A verifier cannot establish that a norepinephrine row represents administration, that a revision offset equals clinician visibility, that a repeat lactate was ordered for a particular reason, that any probability is clinically acceptable without expert workflow review, that a 5/10/20% quota is feasible, or that review changes treatment, harm, workload, cost, or survival. Those require informatic and clinical adjudication plus a prospective external validation and policy-impact study. The configured reserved partition is not available and must not be called external validation.

## Required next study

Before deployment, clinicians and informaticians must adjudicate pressor semantics, specimen/result/display timestamps, assay identity, and the intended review action. A genuinely independent prospective cohort should synchronize order, specimen, result, display, review, treatment, staffing, and outcome clocks and predefine the quota. Only a prospective policy-impact study, ideally randomized or otherwise strongly controlled, can test whether acting on a repeat-lactate queue improves patient outcomes and whether its false-positive workload, harms, cost, and preferences are acceptable.
