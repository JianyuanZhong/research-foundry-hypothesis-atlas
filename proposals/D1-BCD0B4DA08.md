> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Successor: calibrated late-lactate review value under nested hospital-held-out validation

## Decision and unresolved claim

The assigned parent is a valid complete-source experiment, but its clinically material claim remains unresolved. In 1,229 people from 33 hospitals, adding late lactate gave a point increment of +1.0097 modeled net reviews per 100, while the copied-hospital refit interval was -0.2906 to +2.0575. The interval crossed both zero and the +1 materiality margin. The R1 calibration slope was 0.589, so favorable AUROC, Brier score, log loss, and site-deletion point estimates cannot rescue the result.

The strongest claim supported by the parent and by the available literature is narrower: a repeat lactate measured after an early pressor landmark is associated with mortality and can change a mortality-risk score beyond a time-indexed laboratory/physiology state in this selected EICU cohort. This does not establish that ordering lactate improves care, that the result is transportable to a new hospital, or that acting on the score benefits patients.

The unresolved, falsifiable successor claim is:

> In the same prespecified cohort, after a calibration map is learned only from hospital-held-out predictions inside each outer training set, adding the released late lactate to R0 produces at least +1 modeled mortality-review net-benefit-equivalent per 100 people on outer held-out hospitals, while the calibrated R1 probabilities satisfy a prespecified transport-calibration guardrail.

This is a clinically consequential uncertainty because a score that shifts review decisions but is systematically too extreme can misallocate scarce review or escalation attention. The substantive advance is a direct test of whether the parent's apparent decision value survives a leakage-safe calibration procedure, rather than another uncalibrated confirmation or post hoc threshold/model search.

This remains a prognostic, noncausal experiment. It does not estimate treatment benefit, utility of a particular intervention, or patient benefit.

## Population, clocks, and outcome

Use the complete EICU snapshot `[source checksum]`, with no source-row sampling.

1. Read adult ICU rows from `patient`. Map literal age `> 89` and numeric age >89 to 90; retain age >=18. Define t0 as the earliest qualifying norepinephrine/Levophed entry in `infusionDrug` with `infusionoffset` in [0, 1,440] minutes.
2. Select one ICU stay per `uniquepid` using lexicographically smallest (t0, `patientunitstayid`). Retain known hospital outcome (`hospitaldischargestatus` in Alive/Expired) and require numeric `hospitaldischargeoffset >= L24`, where L24=t0+1,440.
3. Define baseline lactate B from `lab`: normalized `labname` lactate, `labmeasurenamesystem` mmol/L, valid numeric result 0.2--30 mmol/L, collection `labresultoffset` in [t0-360,t0], and `labresultrevisedoffset <= t0+60`. Select the latest eligible collection after the parent's deterministic revision/conflict/tie rules, require B>=2.
4. Define late lactate F from the same `lab` rows with the same validity and revision rules, collection in [t0+720,L24] and revision <=L24. Select the collection nearest t0+1,080 minutes, then the earlier collection, then smallest `labid`. The F measurement is part of the released L24 information; no row after L24 enters any predictor.
5. Freeze hospitals outcome-blind using the parent's historical X balance rule, X=1[(B-F)/B<0.20], requiring at least five people in each X category in every retained hospital. X is a cohort-balance filter only and is never a feature, stratifier, or outcome.
6. Define Y=1 as `hospitaldischargestatus == Expired`, otherwise Y=0. The estimand is hospital mortality through discharge among people alive/under observation to L24, not 28-day mortality or treatment response.

The expected audit flow is exactly 200,859 patient rows; 200,234 adults; 7,081 older-age mappings; 16,299 early-pressor stays; 14,786 selected people; 14,672 known outcomes; 13,023 through L24; 5,077 valid baselines; 3,117 B>=2; 1,506 eligible repeat lactates; and 1,229 final people in 33 hospitals (507 deaths, 722 survivors). A flow mismatch is a pre-model failure, not a license to revise eligibility.

## Predictors and baselines

R0 is exactly the parent's 166-feature laboratory-plus-cardiorespiratory state:

- age and age squared; Female and Male indicators (Other/Unknown omitted);
- t0/1,440 and its square; baseline lag; ln(B) and ln(B)^2; follow-up measurement age without F;
- for each of the same 23 non-lactate marker/system pairs, missingness, log1p count, last, recency, minimum, and maximum over [t0,L24];
- last, median, minimum, maximum, resolved timestamp count, and missingness for heart rate, respiration, and SpO2 over [L24-360,L24].

R1 is R0 plus only ln(F) and ln(F)^2 (168 features). No clearance, F/B, X, treatment, diagnosis, note, hospital, post-L24 value, or optional shape feature is permitted.

Both raw models use the parent's fixed unweighted L2 logistic regression: intercept, C=1, lbfgs, max_iter=10,000, tol=1e-8, no class weighting, seed 20260961. In each fit, observed continuous features are winsorized at the training 1st/99th percentiles, standardized using the training mean and population SD, and mean-imputed to zero after scaling. Test hospitals use only constants learned without them. The R0 and R1 models are fit separately.

The clinical baselines are treat-none and treat-all at the same fixed probability thresholds. The parent’s uncalibrated results are a descriptive audit comparator only; they cannot be used to choose thresholds, alter features, or declare success.

## Fixed nested calibration and validation

The outer validation is leave-one-hospital-out (LOHO) over the 33 retained hospitals. Each person receives exactly one outer held-out prediction.

For every outer test hospital h:

1. The outer training set is the other 32 hospitals. Fit raw R0 and R1 models using only this set and its preprocessing constants.
2. To estimate transport calibration without using h, partition the 32 outer-training hospitals deterministically: sort numeric `hospitalid`, assign consecutive hospitals round-robin to five groups by rank modulo 5. For each inner group, fit the corresponding raw model on the other four groups with preprocessing learned only there, predict the held-out group, and pool these five hospital-held-out predictions.
3. For each model separately, fit one fixed logistic recalibration map on the pooled inner out-of-fold predictions:
   `logit(p_cal) = alpha + beta * logit(p_raw)`.
   Use an unweighted binomial logistic fit with intercept. Clip raw probabilities only for finite logit evaluation to [1e-8, 1-1e-8]. No spline, isotonic map, subgroup map, threshold selection, or utility optimization is allowed. Nonfinite fits or separation are calibration failures.
4. Refit raw R0 and R1 on all 32 outer-training hospitals using the fixed parent procedure, apply each corresponding inner-fitted (alpha,beta) map to the held-out hospital, and retain calibrated p0 and p1. The held-out hospital's outcome is never used in fitting either the raw model or its calibration map.

Thus the primary contrast compares two equally calibrated, otherwise identical representations. Calibration is not fit on the outer test hospital, and the model is not expanded or retuned after seeing the parent result.

## Primary estimand and outcomes

For each threshold p in the fixed grid 0.30, 0.31, ..., 0.50, define:

`NB(p)=TP/N - FP/N * p/(1-p)`.

The sole primary estimand is calibrated `Delta-INB = 100/0.20 * integral_[0.30,0.50] [NB_R1_cal(p)-NB_R0_cal(p)] dp`, evaluated by trapezoidal integration on the 21 fixed thresholds. It is expressed as net true-positive-equivalent mortality reviews per 100 people. It is not a count of real reviews and does not assign a clinical harm weight.

Prespecify these outcomes:

- primary: Delta-INB and its 95% copied-hospital refit percentile interval;
- calibration: pooled outer-held-out R1 calibration slope and calibration-in-the-large (CITL), with the same quantities for R0; calibration curves by fixed risk bins [0,.1), [.1,.2), ..., [.9,1] are descriptive only;
- discrimination/proper-score diagnostics: AUROC, Brier, and log loss for R0 and R1 and their paired differences;
- threshold curve: all 21 R1_cal-R0_cal contrasts and comparison with treat-all/treat-none;
- robustness: the 33 fixed-prediction site deletions, each hospital's n and Delta-INB, and mean absolute calibrated probability change.

Calibration quantities are evaluated on outer-held-out predictions, not on apparent training predictions. The primary utility is person-weighted as in the parent. The cluster unit for uncertainty is hospital.

## Uncertainty and computational checks

Use the parent's 2,000-replicate copied-hospital refit bootstrap with seed 20260961. Each replicate samples the 33 retained hospital IDs with replacement, copies all rows from selected hospitals, keeps copies of an original hospital in the same validation group, and repeats the entire outer LOHO model fit, inner hospital-grouped calibration, outer refit, and metric calculation. It must not bootstrap people independently and must not reuse fixed predictions. Report the number and fraction of finite/converged replicates; require at least 1,900/2,000 for a computable result.

The implementation must write aggregate-only outputs: `results.json`, `threshold_curve.csv`, `site_deletion.csv`, `bootstrap_metrics.csv.gz`, and an independent audit. Do not publish patient-level feature matrices or predictions.

Pre-model gates:

- all four source hashes and headers match the catalog and the expected flow is exact;
- every retained hospital has both outcomes, maximum hospital share <=15%, and the parent's marker richness/vital coverage gates pass;
- all 23 marker definitions and the three vital streams are resolved with the parent's collection/revision/tie rules;
- all 33 outer folds and all inner calibration fits have finite, converged outputs;
- every person has one finite p0 and p1, and every bootstrap replicate meets the same finite/convergence rules.

The independent verifier must recompute the flow, source/header/hash checks, feature counts and forbidden-feature audit, nested-fold membership, calibration maps, all primary metrics, bootstrap percentile interval, site deletions, and ordered label. Synthetic fixtures must test calibration failure, utility support, utility opposition, adverse-to-materiality, mixed (utility material but calibration failed), inconclusive, and not-computable states. The verifier checks computation and inference from computed quantities, not clinical truth.

## Ordered interpretation and falsification

Apply rules in this order:

1. **Not computable:** any pre-model gate fails, fewer than 1,900 bootstrap replicates converge, or the required outer/inner predictions or calibration fits are nonfinite.
2. **Opposite:** the 95% Delta-INB interval has upper bound <0. This falsifies even the direction of incremental modeled value; favorable diagnostics cannot override it.
3. **Supportive:** the interval lower bound is >=+1 per 100, the R1 transport-calibration guardrail passes, and all required robustness checks pass: every threshold Delta-NB is >=-0.5/100, R1_cal beats the better of treat-all/treat-none at every fixed threshold, at least 80% of site deletions are positive, and both proper-score changes improve.
4. **Mixed:** the interval lower bound is >=+1 but the calibration or robustness guardrail fails. This supports material modeled discrimination/utility under the specified calculation but not a calibrated decision claim.
5. **Adverse to materiality:** the interval is >=0 and has upper bound <+1. This indicates that any incremental modeled value is too small or too uncertain to meet the clinically material margin, even if the point estimate is positive.
6. **Inconclusive:** the interval spans both zero and +1 (lower <0 and upper >=+1), or otherwise does not meet an earlier rule.

The R1 transport-calibration guardrail is prespecified as follows: pooled outer-held-out calibration slope point estimate in [0.80,1.20] with its 95% copied-hospital interval wholly within [0.80,1.20], and CITL point estimate in [-0.05,0.05] with its 95% interval wholly within [-0.05,0.05]. The R0 calibration results are reported for context; R1 is the added-information model whose calibration is safety-critical. These bounds are operational validity criteria, not proof of clinical safety.

Supportive, adverse, and inconclusive results have distinct meanings:

- Supportive would show a material, calibrated, hospital-held-out modeled review increment under a locked protocol. It would justify prospective synchronized validation with clinically elicited review utilities; it would not justify ordering lactate, changing treatment, or claiming survival benefit.
- Mixed would show that the point/interval supports material modeled increment but calibration is not trustworthy. It would motivate a larger independently collected dataset or a different prespecified calibration strategy, not threshold optimization.
- Adverse to materiality would show the point direction may be positive but the evidence excludes the +1 margin. It would argue against treating this late-lactate increment as materially useful under these review assumptions.
- Opposite would show evidence against even positive incremental modeled value.
- Inconclusive would preserve the uncertainty and require a larger independent, prospectively synchronized cohort rather than a favorable point-diagnostic narrative.

## Exact read-only source bindings and availability

All source files below are ordinary gzip files (archive member: `ordinary file`), read-only, and join to `patient` by `patientunitstayid`. `uniquepid` is the person-selection key and `hospitalid` is the held-out cluster/bootstrap/deletion key.

- `[internal dataset path]`; [source checksum]; table `patient`; schema `datasets/eicu/table-ab037c09d7df9a3c.json`; required columns `patientunitstayid, uniquepid, age, gender, hospitalid, hospitaldischargeoffset, hospitaldischargestatus`.
- `[internal dataset path]`; [source checksum]; table `infusionDrug`; schema `datasets/eicu/table-18e1a8caaa91eb44.json`; required columns `infusiondrugid, patientunitstayid, infusionoffset, drugname`.
- `[internal dataset path]`; [source checksum]; table `lab`; schema `datasets/eicu/table-79bdb33275339b1a.json`; required columns `labid, patientunitstayid, labresultoffset, labname, labresult, labmeasurenamesystem, labresultrevisedoffset`.
- `[internal dataset path]`; [source checksum]; table `vitalPeriodic`; schema `datasets/eicu/table-a22c6d6981a32279.json`; required columns `vitalperiodicid, patientunitstayid, observationoffset, sao2, heartrate, respiration`.

The full EICU catalog is `[internal dataset path]`, [source checksum]; the EICU guide is `datasets/eicu/README.md`; metadata is `datasets/eicu/metadata.json`; snapshot is `[source checksum]`. The catalog exposes all 29 EICU table schemas and their relationships; the four experiment sources above are the only tables needed.

Direct read-only access to the other configured datasets (HCC, MIMIC, UKB), including rows and notes where present, is retained. They are not pooled because their keys, sampling frames, outcomes, and time semantics are not exchangeable with this EICU estimand. eICU's metadata records no images, no raw waveforms (vitalPeriodic is a five-minute summary), and public narrative note sections are removed; structured note fields are not used. Lab revision time is a database proxy, not a verified specimen-result display time. These limitations are essential clinical evidence gaps.

## Current evidence and boundaries

The inspected demonstration files were used only to calibrate ambition: the Nature Delphi-2M article and supplementary information were read for longitudinal, time-aware validation; the cancer demonstration's supplement was read, while its main article and full STAR Methods remain unavailable; and the ALADYNOULLI article and supplement were read. None supplies evidence about this EICU late-lactate question.

Current public evidence includes:

- Yang et al., “Landmark-based early perfusion phenotyping for prognostic stratification in septic shock: derivation in MIMIC-IV and fixed-parameter external transportability assessment in eICU,” Frontiers in Medicine (2026), DOI `10.3389/fmed.2026.1880921`, acquired source `[source checksum]`. Its inspected full text describes lactate clearance within an 8-hour landmark and eICU transfer, but concludes that small, measurement-dense complete-case subsets and class-prevalence drift preclude robust transportability or bedside-decision claims.
- Li et al., “Dynamic Lactate-to-Albumin Ratio Trajectories and Outcomes in Sepsis-Associated Acute Kidney Injury: Evidence From MIMIC-IV and a Multicenter Chinese Cohort,” JMIR Medical Informatics (2026), DOI `10.2196/92838`. The inspected Europe PMC search record reports trajectory associations and external validation with modest discrimination, but observational association and a nomogram do not establish calibrated decision benefit.
- Methodological current evidence from the inspected Europe PMC prediction-model search supports evaluating calibration, external validation, and decision utility together; AUROC alone is insufficient. These search responses are untrusted model-mediated evidence and are not treated as proof of the proposed claim.

## Required clinical adjudication and next study

The files cannot adjudicate whether a qualifying infusion entry reflects verified norepinephrine administration or indication; whether a lactate was actually available to a bedside clinician by L24; specimen collection/processing/display latency; whether a risk review was appropriate; the harm/benefit weights behind the net-benefit threshold; cause and exact time of death; clinician actions, safety, treatment effects, or patient benefit. The model also inherits measurement-dependent missingness and selected repeat-lactate testing. These questions require expert review of synchronized orders/specimens/results and prospective implementation or impact study.

The successor therefore makes only computationally checkable claims about source integrity, deterministic cohort construction, time-safe feature availability, nested calibration, predictions, metrics, uncertainty, and the ordered label. Any stronger claim requires clinical adjudication, an independently collected synchronized validation cohort, and ultimately a prospective impact study.
