> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 23 successor: does lactate nonclearance retain prognostic information after early organ-context adjustment?

## Unresolved question and clinical importance

The locked parent establishes a positive, noncausal association between less than 20% lactate clearance and hospital death among a narrowly selected EICU phenotype: adults with an early norepinephrine record, serial lactates, documented baseline monitor context, and at least six final-hour MAP observations with at least 80% at or above 65 mm Hg. Its C=10 overlap estimate was a +24.389 percentage-point mortality risk difference, but the copied-hospital/person 95% interval was +6.121 to +42.882, so the prespecified +10-point magnitude remains inconclusive. That result does not show that lactate is informative beyond organ dysfunction already present before the follow-up lactate, nor that it reflects tissue hypoperfusion.

The next clinically consequential question is whether the lactate trajectory contributes prognostic information after accounting for observable renal/hepatic clearance context and early vasopressor exposure. If it does, a synchronized prospective study could evaluate whether this phenotype is useful as a multimodal reassessment marker. If it does not, the association may largely be a proxy for measurable organ dysfunction or treatment intensity, weakening the case for a lactate-specific escalation trigger.

**Primary falsifiable hypothesis:** in the parent's exact 216-person, ten-hospital target, after adding strictly pre-follow-up organ-context and recorded pressor-exposure covariates to the parent's fixed exposure-overlap model, the standardized mortality risk difference for nonclearance (<20% relative fall) versus clearance (at least 20%) remains at least +10 percentage points. The estimand is a conditional prognostic association in the measured-overlap target, not a causal effect and not proof of impaired tissue perfusion.

This is a substantive incremental-information test, not a new lactate cutoff or a search over MAP/lactate windows. The parent's result and classification remain preserved; this experiment asks whether its signal survives a prespecified, temporally prior clinical-context adjustment.

## Evidence boundary

The strongest available evidence is the parent's complete-source result: all population and overlap gates passed; the point estimate was positive and all ten leave-one-hospital-out estimates were positive, but the +10-point claim was inconclusive. The parent also reports that Diab et al. (Frontiers in Medicine 2025; DOI 10.3389/fmed.2025.1679297) found a borderline adjusted association between >10% clearance and death in a single-center sepsis/shock cohort, while Tóth et al. (Annals of Intensive Care 2026; DOI 10.1016/j.aicoj.2026.100106) found no significant mortality benefit from tissue-perfusion-guided therapy across eight trials. Those findings motivate separating prognosis from intervention; neither establishes this EICU phenotype or the incremental claim below.

The available EICU rows cannot establish arterial specimen identity, lactate collection/order rationale, true norepinephrine initiation or dose, fluid administration, tissue perfusion, organ-support intent, exact death time/cause, or treatment limitation. A positive conditional association therefore cannot justify fluid, vasopressor, inotrope, or lactate-target recommendations.

## Population and time order

Use the parent population without changing its selection rules:

1. Scan all source rows, with no sampling. Adults have numeric `patient.age >=18` (EICU released `>89` is treated as 90). In each stay, T0 is the minimum `infusionDrug.infusionoffset` in [0,1440] whose case-folded `drugname` contains norepinephrine or levophed. Dose/rate do not establish eligibility. Retain the earliest T0 stay per `uniquepid`, ties by `patientunitstayid`.
2. Define L=T0+480. Require `patient.unitdischargeoffset>=L`, `hospitaldischargeoffset>=L`, and exact `hospitaldischargestatus` Alive or Expired. Outcome D is exact hospital status Expired.
3. Construct baseline lactate B exactly as the parent: latest valid `lab` lactate collection in [T0-360,T0], numeric 0.2-30 mmol/L and revised by T0+60; conflicting valid revisions invalidate that collection, identical duplicates retain the smallest `labid`; require B>=2.
4. Construct follow-up F exactly as the parent from [T0+120,L], valid and revised by L, resolving each collection offset by greatest eligible revision and excluding conflicting values; choose the clean offset nearest T0+360, then earlier, then smallest `labid`. Set X=1 when (B-F)/B<0.20 and X=0 otherwise. Retain the follow-up elapsed time E=F_offset-T0.
5. Require the parent's final-hour MAP recovery and baseline monitor context: at least six unique valid `vitalPeriodic.observationoffset` values in [T0+420,L], at least 80% median `systemicmean >=65, and at least three unique offsets in [T0-60,T0) with valid systemicmean and heartrate. Duplicate offsets are collapsed by median as in the parent.
6. Preserve the parent's outcome-blind site gate: at least five X=0 and five X=1 people per hospital, then require at least eight hospitals, 50 people, and at least 20 hospital deaths in each exposure group. The parent audit found 216 people in ten hospitals (106 clearance, 110 nonclearance); these counts must be independently reconciled before analysis.

## New, strictly pre-follow-up covariates

The primary incremental model uses only measurements available before the selected F collection. For each person, define an early context boundary Q=min(F_offset, T0+120), and use source observations with measurement/collection offset <Q. This makes the covariates strictly earlier than the follow-up lactate even when F is at the earliest allowed time.

From `lab`, for each analyte below select the latest valid collection in [T0-360,Q), with its result revised by Q; apply the same greatest-revision/conflict invalidation rule used for lactate and require the documented analyte unit:

- creatinine, `labname='creatinine'`, expected `labmeasurenamesystem='mg/dL'`;
- total bilirubin, `labname='total bilirubin'`, expected `mg/dL`;
- AST (SGOT) and ALT (SGPT), expected `Units/L`;
- BUN, `labname='BUN'`, expected `mg/dL`.

Do not merge unit-incompatible labels or infer missing values from text. For skewed analytes use predeclared log1p-transformed values after physiologic-range checks; retain a missingness indicator for each analyte. The primary organ-context block is the latest creatinine, total bilirubin, AST/ALT (use the maximum of AST and ALT when both are present; otherwise missing), and BUN, plus their missing indicators. A complete-case organ-block analysis is a secondary sensitivity, not a replacement if missingness is substantial.

From `infusionDrug`, summarize only records with infusionoffset in [T0,Q): indicators for any matching norepinephrine/levophed record and any other vasopressor record (epinephrine, phenylephrine, vasopressin, dopamine), plus the count of distinct recorded pressor-name families. Do not convert rates to dose-equivalents: `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, and `patientweight` are retained only as descriptive data because units, start/stop semantics and administration status are not reliably adjudicated. Add an indicator for a non-norepinephrine pressor record. These summaries are recorded exposure proxies, not treatment dose or indication.

The parent covariate block remains: age, gender indicators including missing, B, baseline median MAP/heart rate, T0, E, final-hour median MAP and fraction of MAP medians >=65, and hospital indicators. No outcome, death status, discharge time, post-Q laboratory value, or post-Q medication record may enter population selection, preprocessing, model fitting, or feature construction.

## Estimand and baselines

The primary estimand is the overlap-weighted standardized difference P(D=1|X=1)-P(D=1|X=0) in the parent's target after balancing the expanded measured context. It is an association conditional on measured covariates, not a propensity-score causal effect. Fit a fixed scikit-learn logistic regression for X with C=10, penalty=l2, solver=lbfgs, max_iter=10000. Winsorize continuous covariates at pooled 1st/99th percentiles and standardize using pooled means and population SDs; include missing indicators and hospital indicators. Use weights 1-e for X=1 and e for X=0, normalized to mean one within exposure group. No mortality enters the exposure model.

Report these prespecified comparisons:

- parent primary C=10 overlap estimate using the parent's covariates;
- organ-context-adjusted C=10 estimate (primary);
- organ-context plus pressor-proxy estimate (secondary);
- unweighted crude RD and hospital-only overlap RD as descriptive baselines;
- complete-case organ-context sensitivity;
- a model-discrimination secondary check comparing nested mortality models with and without X using cross-validated within-hospital splits, only if each fold has valid events; do not let predictive improvement replace the RD hypothesis or imply utility.

The parent’s +10 boundary remains the primary clinical materiality anchor. It is a decision threshold for this experiment, not a validated minimum clinically important difference.

## Feasibility, uncertainty and falsification

Before outcomes are read, report counts and missingness for every new covariate, the number of people with a complete organ block, the number with any pressor-proxy record before Q, hospitals with at least five people per exposure after the new complete-data rule, and the overlap population under the primary missing-indicator construction. If the exact parent target cannot be reconciled, if fewer than 50 people/eight hospitals/20 deaths per exposure remain, or if either exposure ESS is below 40, the propensity range leaves [0.02,0.98], maximum person-weight fraction exceeds 5%, maximum hospital-weight fraction exceeds 35%, maximum absolute weighted SMD exceeds 0.10, or more than 5% of 5,000 bootstrap replicates fail, classify the experiment inconclusive.

Use the parent's hierarchical uncertainty exactly: seed 20260921; sample the ten hospitals with replacement as unique hospital-copy IDs, then sample unique `uniquepid` clusters within each copied hospital and exposure group to the original size as unique person-copy IDs; recompute preprocessing, expanded exposure model, weights, and estimate in each replicate; retain repeated copies. Require 5,000/5,000 successful replicates and use the 2.5th/97.5th percentiles for the RD interval. Report all model-column SMDs, propensity range, ESS, weight concentration, failure count, and ten leave-one-hospital-out primary estimates.

Primary classification:

- **Supportive:** all gates pass and the adjusted RD interval lower bound is at least +10 points, with at least 80% of finite site-deletion estimates positive. This supports a persistent measured-context-adjusted prognostic association of the prespecified magnitude.
- **Adverse to the magnitude:** all computational gates pass and the adjusted RD interval upper bound is below +10 points. This falsifies the >=+10 conditional association, but does not show no prognostic value, no association, or benefit from another intervention.
- **Opposite direction:** all gates pass and the adjusted RD interval upper bound is below zero. This supports an adjusted direction opposite to the hypothesis, but does not establish that clearance is protective.
- **Inconclusive:** any gate fails, computation is undefined, intervals contain +10, or site deletions are too unstable. A positive point estimate alone is not supportive.

A result can be parent-positive but organ-adjusted adverse: that would indicate attenuation compatible with measured organ-context explanation, while remaining noncausal because residual confounding and measurement selection remain. A result that remains positive but inconclusive for +10 supports persistence of direction only, not the materiality threshold.

## Exact source bindings and provenance

Use the EICU snapshot `[source checksum]` and the read-only ordinary gzip files under `[internal dataset path]` (no nested archive members):

- `patient.csv.gz`, table `patient`, [source checksum]: `patientunitstayid`, `uniquepid`, `age`, `gender`, `hospitalid`, `unitdischargeoffset`, `hospitaldischargeoffset`, `hospitaldischargestatus`.
- `infusionDrug.csv.gz`, table `infusionDrug`, [source checksum]: `infusiondrugid`, `patientunitstayid`, `infusionoffset`, `drugname`, `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, `patientweight`.
- `lab.csv.gz`, table `lab`, [source checksum]: `labid`, `patientunitstayid`, `labresultoffset`, `labname`, `labresult`, `labresultrevisedoffset`, `labmeasurenamesystem`, `labmeasurenameinterface`, including the exact analyte/unit restrictions above.
- `vitalPeriodic.csv.gz`, table `vitalPeriodic`, [source checksum]: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `systemicmean`, `heartrate`.
- `apacheApsVar.csv.gz`, table `apacheApsVar`, [source checksum] (optional descriptive sensitivity only): `patientunitstayid`, `creatinine`, `bilirubin`, `meanbp`, `heartrate`, `ph`, `pao2`, `pco2`, `fio2`; it has no event timestamp, so it must not be used in the primary temporally ordered organ adjustment.
- `hospital.csv.gz`, table `hospital`, [source checksum] (optional site descriptors): `hospitalid`, `numbedscategory`, `teachingstatus`, `region`.

Event tables join to `patient` on `patientunitstayid`; earliest-person selection and resampling use `uniquepid`; hospital clustering uses `hospitalid`; all times are integer ICU-relative minutes. The four configured HCC, MIMIC, EICU and UKB datasets remain accessible read-only, but this experiment uses EICU only. Record actual row counts, filtering, invalidation, missingness and any source discrepancies in a workspace audit. No private rows or notes may be sent to public search.

## What this can and cannot establish

Computationally checkable claims include exact cohort reconstruction, temporal ordering, analyte/unit and revision rules, complete scans, overlap diagnostics, bootstrap execution, interval calculation, site deletions, and deterministic classification. A supportive adjusted interval would establish only a reproducible association conditional on the recorded context in this selected EICU snapshot. An adverse interval would reject only the prespecified conditional +10 magnitude.

Neither result establishes tissue hypoperfusion, organ-clearance mechanism, norepinephrine administration/dose, causal exchangeability, safety, target selection, clinical utility, or treatment benefit. Clinical adjudication is needed for specimen identity, assay timing, treatment intent, liver/renal failure definitions, perfusion markers, and limitations of care. Independent synchronized data are needed for transportability and magnitude resolution; a prospective decision-impact study is needed for utility; a randomized or credible target-trial study is needed for treatment effects.

## Verifier requirements

The compiler/verifier must recompute every source binding, temporal inequality, revision/conflict rule, parent reconciliation, new-covariate missingness and unit audit, overlap model, copied-cluster bootstrap, diagnostics, intervals, site deletions and deterministic classification. It must test interpretations in supportive, adverse, inconclusive and parent-positive/adjusted-adverse fixture cases. It must reject a conclusion that calls the adjusted RD causal, labels recorded MAP as perfusion, treats pressor names/rates as administered dose, claims sepsis generalization, or asserts clinical utility from QA. It should report separately which statements are computationally checkable and which require expert adjudication or another study.
