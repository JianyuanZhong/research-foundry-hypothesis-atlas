# Episode 2 clinical translation: CBC discordance, timing, and repeat-measurement selection

## Revised hypothesis and scientific deliverable

The clinically consequential question is whether a fall in haemoglobin relative to a rise in platelets (CBC discordance) is a cancer-type-specific signal, and whether that signal is confined to the period immediately preceding diagnosis or persists as a longer-latency association. A useful result would change how a future clinical study designs repeat-CBC surveillance: it could support a hypothesis for CRC-focused investigation, a hematologic-cancer warning pattern, or reassurance that the discordance is not type-specific. This UKB analysis cannot itself authorize referral or reassurance.

The strongest available evidence supports narrower claims. [K1] shows that static anaemia/haemoglobin is associated with CRC in primary-care records. [K2] reports retrospective longitudinal CBC changes before CRC and metastatic phenotype, but explicitly requires prospective external validation. [K3] concerns mostly post-diagnosis RDW prognosis and highlights heterogeneous timing and thresholds. None establishes that two prediagnostic CBCs distinguish CRC from hematologic cancer, that an association survives a long-latency test, or that it has clinical utility.

The untested claim is:

> Among UKB participants cancer-free at a second complete CBC, a relative platelet rise with haemoglobin decline has a larger association with subsequent CRC than with subsequent hematologic cancer, and the CRC-versus-hematologic contrast remains directionally present from 2–7 years after the second CBC rather than appearing only in the 0–2-year diagnostic-proximity window.

The principal deliverable is newly fitted, uncertainty-quantified evidence for:

1. An early-versus-late cause-specific cancer-type contrast, with explicit competing death/other-cancer handling.
2. A selection stress test quantifying how much requiring a second complete CBC changes the analytic population, using baseline-only inverse-probability-of-repeat-observation weights and overlap diagnostics.
3. A transparent baseline versus a bounded learned alternative on identical inputs, evaluated for calibrated absolute CRC and hematologic risk rather than rewarded for a small AUC gain.
4. A registry-bounded translation assessment: whether CBC information adds calibrated, temporally valid risk separation beyond clinical covariates. This is not a clinical triage validation because referral decisions, symptoms, diagnostic work-up, stage, pathology, and healthcare-use data are unavailable.

Completion requires the fitted coefficient contrasts and confidence intervals, selection/overlap diagnostics, event and person-time tables, held-out predictions, calibration/Brier/log-score outputs, pre-specified sensitivity analyses, and a conclusion labelled supportive, adverse, or inconclusive. A plan or readiness probe is not completion.

## Exact UKB data binding

This experiment uses one same-namespace table and no joins.

- Catalog table: `datasets/ukb/table-5d49a6760e7ffdbd.json`, table name `ukb671626.csv (Parquet)`.
- Read-only convenience source: `[internal dataset path]`.
- Original lineage: `[internal dataset path]`.
- Catalog source IDs: `[UKB data file]` and `[UKB data file]`; Parquet SHA-256 is `[source checksum]`.
- The catalog records 502,371 rows, identifier `eid`, identifier namespace `ukb671626`, and an ordinary-file archive member. Do not join `eid` to `ukb672073`, dta, Olink, or any other namespace.

Required source columns:

- CBC: `30000-{0,1,2}.0` WBC, `30020-{0,1,2}.0` haemoglobin, `30070-{0,1,2}.0` RDW, and `30080-{0,1,2}.0` platelets.
- Assessment dates: `53-0.0`, `53-1.0`, `53-2.0`.
- Baseline adjustments: `31-0.0` sex, `21003-0.0` age at assessment, `21001-0.0` BMI, `20116-0.0` smoking status, `30710-0.0` CRP. `30710-1.0` is an optional sensitivity feature only, not a required primary field.
- Registry outcomes: paired `40005-{0..21}.0` diagnosis dates and `40006-{0..21}.0` ICD-10 codes, plus `40000-0.0` death date. Retain `40001-0.0` only for audit; it does not define cancer type.

For every registry slot, discard an unpaired date or code. Classify C18/C19/C20 prefixes as CRC, C81–C96 prefixes as hematologic cancer, and other primary malignant C00–C97 prefixes as other cancer, excluding C77–C79 secondary malignancy codes from all three primary categories. The first qualifying date after the relevant landmark defines the event. Report the code/date-pair audit and any duplicate or implausible dates before fitting.

A bounded selected-column audit against the exact Parquet source completed in 16.5 seconds. It found 478,033 complete instance-0 CBC/date records, 18,377 complete instance-0/1 records with increasing assessment dates, and a median assessment gap of 1,606 days (10th–90th percentile 1,069–1,947 days). Among the 18,377, 16,580 were cancer-free at T1 (the second assessment date). In the resulting descriptive timing audit, first events were:

| Window after T1 | CRC | Hematologic | Other cancer | Death |
|---|---:|---:|---:|---:|
| 0–730 days | 45 | 27 | 425 | 30 |
| >730–2,555 days | 100 | 75 | 1,166 | 224 |

These are audit counts, not fitted results. The complete-second-CBC fraction is 3.84% of complete instance-0 records. This is a major selection issue, not a footnote. The hematologic count is also sparse; a temporal holdout will have fewer events than the full descriptive cohort and must not be treated as a definitive hematologic prediction benchmark.

## Population, selection estimands, and timing

Define T0 = `53-0.0`, T1 = `53-1.0`, and the optional third-assessment time T2 = `53-2.0`.

The primary repeated-measurement cohort requires nonmissing `eid`, T0, T1, all eight CBC values at instances 0 and 1, and T1 > T0. Exclude anyone with any nonmissing cancer date on or before T1. This is a cohort cancer-free at the observed second CBC, not proof that occult disease is absent.

Define the early window as T1 to T1+730 days. Define the late window as T1+730 days to T1+2,555 days, with left truncation at T1+730: retain only those without CRC, hematologic cancer, other cancer, or death through the delayed-entry boundary. Follow to the earlier of T1+2,555 and 2022-12-31. The fixed administrative boundary is set before analysis; the catalog audit found the latest nonmissing cancer date 2022-06-01 and death date 2022-12-19. A 7–10-year result may be reported only as exploratory if administrative support exists.

The early estimand is the cause-specific association of the frozen CBC features with first CRC or hematologic cancer within two years of T1 among those cancer-free at T1. The late estimand is the corresponding association conditional on remaining cancer-free and alive through two years, from delayed entry to seven years. The key contrast is:

delta_w = beta_CRC,w,DHP - beta_HEM,w,DHP
for window w = early or late, and the temporal question is whether delta_late differs from zero and from delta_early. A late result is not a causal effect and is not independent of survival; its interpretation is deliberately conditional on remaining event-free.

For each target, other cancer and death are competing events in cumulative-incidence calculations. In cause-specific hazard models they leave the target risk set at their first occurrence. Report cause-specific hazards and Aalen–Johansen cumulative incidence; Fine–Gray is secondary and cannot replace the primary cause-specific estimand.

### Repeat-measurement selection control

Let S=1 indicate a complete, valid second CBC/date with T1>T0 among people with complete instance-0 CBC/date and no cancer date on or before T0. Estimate P(S=1 | T0 information) using only `31-0.0`, `21003-0.0`, `21001-0.0`, `20116-0.0`, `30710-0.0`, the four instance-0 CBC values, T0 calendar year, and no post-T0 information. Fit this observation model inside each development fold. Apply stabilized inverse-probability-of-repeat-observation weights to S=1 participants, with truncation rules fixed at the 1st and 99th development percentiles. Report the selection model’s AUC, calibration, weight distribution, effective sample size, baseline standardized differences, and positivity failures.

The weighted analysis does not recover unmeasured healthcare use. There is no verified visit/frequency/referral field in this one-table binding that can establish why a second CBC was obtained. Therefore the selection control tests measured baseline transportability and quantifies sensitivity to repeat-observation selection; it cannot prove that the CBC contrast is free of indication or healthcare-use bias.

Additional selection/timing controls are:

- Repeat the analysis in the central observed assessment-gap range, with bounds learned from T0/T1 dates in development and frozen before outcome analysis.
- Include assessment gap and T0 calendar year in every model; stratify or adjust for baseline CBC level, CRP, age, sex, BMI, and smoking.
- Compare unweighted and weighted estimates, and report complete-instance-0 denominators rather than presenting the 18,377 repeat-CBC participants as a general UKB population.
- Use instance 0/2 only as a small, explicitly labelled sensitivity cohort; do not treat three instances as a dense trajectory.
- Report missingness and selection by T0 calendar period and baseline CBC abnormality. Do not impute a missing second CBC as normal.

## Frozen predictors

Within each training fold, standardize the four CBC variables using instance-0 training means and standard deviations, applied unchanged to instance 1. Let d_j be instance-1 minus instance-0 standardized value.

- DHP = d_platelet − d_haemoglobin. Larger values represent relative platelet rise and haemoglobin fall.
- DML = mean(abs(d_WBC), abs(d_haemoglobin), abs(d_RDW), abs(d_platelet)).

Both methods include the four baseline CBC z-scores and four changes separately, so DHP cannot hide baseline severity or regression-to-the-mean effects. Prespecified covariates are age, sex, BMI, smoking, CRP0, assessment gap, and T0 calendar year. CRP change is sensitivity-only. No outcome-guided thresholds, post-T1 measurements, registry-derived predictor, or outcome-based subgroup is permitted.

## Method comparison

### A. Transparent baseline: weighted piecewise competing-risk regression

Fit cause-specific Cox models for CRC and hematologic cancer with a common covariate set and separate DHP coefficients for 0–2 and 2–7 years since T1. Equivalently, use a stacked cause-specific formulation with cause-by-DHP and period-by-DHP interactions and robust participant-clustered variance. Fit both unweighted and selection-weighted versions. Use a prespecified ridge penalty only if separation or convergence fails, record the penalty and convergence status, and use robust bootstrap intervals that repeat the full selection-weight estimation.

Estimate delta_early, delta_late, their difference, hazard ratios per one SD of DHP, and 95% confidence intervals. Include DML as a secondary prespecified contrast, not a replacement outcome. Report Schoenfeld/time-varying-effect diagnostics and 2- and 5-year Aalen–Johansen cumulative incidence for CRC, hematologic cancer, other cancer, and death.

This baseline directly tests the scientific contrast, is auditable by clinicians, and makes the survival/competing-risk interpretation explicit. It loses nonlinear thresholds, interactions such as DHP being informative only at low haemoglobin, and richer joint CBC configurations.

### B. Learned alternative: bounded discrete-time multi-task competing-risk model

Fit a modest CPU gradient-boosted discrete-time model on exactly the same eligible participants and the same baseline-only information: raw CBC values at instances 0 and 1, their four changes, DHP/DML, age, sex, BMI, smoking, CRP0, assessment gap, and calendar year. No cancer date, event type, or post-T1 value enters a feature. Use the same selection weights as the corresponding baseline analysis.

Expand each participant into one-year intervals from T1 to seven years, stopping at the first cancer/death or censoring. The target at each interval is CRC, hematologic cancer, other cancer/death, or no event. Use a fixed small HistGradientBoostingClassifier (or an equivalent documented implementation), with hyperparameters selected only in rolling temporal development folds. Convert interval hazards to target-specific cumulative-incidence predictions.

The substantive comparison is not “which model has the highest AUC.” Compare:

- M0: age, sex, BMI, smoking, CRP0, gap, and calendar year;
- MA: M0 plus the frozen CBC levels, changes, DHP and DML in the transparent model;
- MB: M0 plus identical raw CBC information in the learned model.

On the untouched latest 30% of landmark dates, report two-year early and five-year delayed-entry CRC and hematologic calibration intercept/slope, calibration plots, Brier score, competing-risk log score, observed-versus-predicted cumulative incidence, and participant-bootstrap 95% intervals. Time-dependent AUC/Uno C-index is secondary. Report descriptive risk strata at fixed 0.5%, 1%, 2%, and 5% risks only; these are not validated referral thresholds. A model cannot support reassurance if its low-risk strata are miscalibrated or omit early events.

The learned alternative could reveal clinically relevant nonlinear CBC ranges, multi-lineage interactions, or a time profile missed by DHP. It cannot identify occult bleeding, inflammation, clonal haematopoiesis, or a mechanism. If it improves discrimination without calibration or without a stable type-specific temporal pattern, it does not advance the scientific claim.

### Split and uncertainty

Sort by T1 and hold out the latest 30% of landmark dates. Keep participants intact. In the earliest 70%, use rolling temporal folds for preprocessing, selection weights, hyperparameters, and calibration. Do not use held-out cancer outcomes to select features, thresholds, transformations, or the model.

The full cohort coefficient analysis may use the prespecified weighted cohort after the split is frozen, but the holdout is the only confirmation of predictive calibration. The solver must report counts of CRC and hematologic events in every split and window. If the held-out hematologic count is below 20, omit hematologic discrimination claims and label calibration/contrast estimates imprecise; do not replace temporal splitting with a random split. If an event count is small but nonzero, use profile/penalized intervals and participant bootstrap, with the sparse-event limitation prominent. The audit’s 75 late hematologic events are a full-cohort descriptive count, not a promise that the holdout will contain enough.

## Falsification and interpretation

Supportive evidence requires all of the following:

- DHP has the prespecified CRC-relative-to-hematologic direction in the late window, with an uncertainty interval excluding zero when the event support and model diagnostics are adequate; otherwise it is inconclusive.
- The result is not present only in 0–2 years, and the direction is not eliminated by measured-selection weighting, central-gap restriction, baseline severity adjustment, or the instance-0/2 sensitivity.
- The pattern is more type-specific than a comparable association with other primary cancers.
- The learned model shows stable temporal-fold effects or interactions and improves held-out competing-risk calibration/log score or clinically interpretable absolute-risk separation over M0/MA, not merely a small AUC.
- The outcome/code pairing, competing-event ordering, and uncertainty outputs pass audit.

Adverse evidence is a late contrast with the opposite direction and adequately narrow uncertainty, a contrast that vanishes after the delayed-entry or selection controls, comparable prediction of other cancers, or learned-model calibration failure on the temporal holdout. This would narrow the claim to generic or near-diagnostic CBC/cancer association and would argue against a long-latency cancer-type triage signal.

Inconclusive evidence includes wide intervals caused by the hematologic event count, poor overlap or extreme repeat-observation weights, materially different weighted and unweighted estimates without a defensible measured-selection explanation, unstable instance-0/2 replication, non-proportional effects not captured by the prespecified piecewise model, or acceptable discrimination with poor calibration. An imprecise null does not refute the hypothesis. It supports a larger clinical cohort with denser CBC dates and adjudicated diagnostic pathways.

A negative-control pipeline check will permute CRC versus hematologic labels among participants with the same event date within development only; the type interaction should collapse toward zero. A specificity check will compare the same DHP contrast with other primary cancer codes. These checks test computation and label handling, not clinical truth.

## Clinical translation and limits

A supportive result would establish only a temporally ordered, cancer-type-specific registry association in a highly selected repeat-measurement subset. It could justify an externally validated clinical study asking whether a repeat CBC pattern should trigger targeted evaluation. It would not justify telling a patient that CRC is likely, hematologic cancer is excluded, or no referral is needed. Even calibrated absolute risks are not clinical utility without a target population, prevalence transport, treatment/referral thresholds, harms, and prospective impact evaluation.

The source lacks pathology adjudication, stage, symptoms, FIT/colonoscopy, iron/ferritin, reticulocytes, smear/marrow studies, infection timing, medications, transfusions, treatment, and direct healthcare-use intensity. Registry ICD codes may not resolve primary versus secondary disease beyond the prespecified coding rule. The association cannot distinguish occult bleeding, inflammation, nutritional deficiency, clonal haematopoiesis, reverse causation, or measurement/indication bias. Expert review and external validation are required for all mechanism and action claims.

An automatic verifier can check exact source paths/columns, read-only lineage, event derivation, split, weights, fitted outputs, confidence intervals, calibration, and whether conclusions match supportive/adverse/inconclusive criteria. It cannot adjudicate pathology, establish mechanism, or establish clinical utility.

## Alternatives and resource decision

The baseline and learned alternative address the same scientific uncertainty with matched inputs, target, split, and uncertainty evaluation. The baseline is selected as the primary inferential method because delta_early and delta_late are transparent and clinically interpretable. The learned alternative is retained because nonlinear CBC configurations may carry information the contrast loses and because calibration/absolute-risk performance is relevant to a future triage study.

A latent Gaussian-process/state model or transformer is deferred. The verified table has only two broadly complete CBC assessments (the instance-2 complete count was 5,862 in the inherited audit), no dense laboratory dates for most participants, and no need to infer a mechanistic state from sparse measurements. It could be revisited if a future source supplies dense longitudinal CBCs and sufficient hematologic events. This is a scientific deferral, not a blanket rejection of neural or GPU methods.

The bounded audit used 2 CPUs and 16 GiB for 16.5 seconds; no full fit or bootstrap timing was measured. Future solver planning is 8–16 CPUs, 32–64 GiB, and up to 28,800 seconds for feature construction, weighted piecewise models, rolling folds, the modest tree model, and 200–500 participant bootstrap replicates. GPU use is not needed for the proposed tree model; the hardware guidance was consulted and no GPU is requested. These are planning estimates, not completed-study results.

## Three inspected key works

- [K1] Hamilton W, Lancashire R, Sharp D, Peters TJ, Cheng KK, Marshall T. “The importance of anaemia in diagnosing colorectal cancer: a case-control study using electronic primary care records.” *British Journal of Cancer* (2008). DOI: 10.1038/sj.bjc.6604165. Abstract-only inspection; supports static anaemia/CRC diagnostic association but not repeated CBC or competing cancer types.
- [K2] Sala RJ, Ery J, Cuesta-Peredo D, Muedra V, Rodilla V. “Haematological pre-staging of colorectal cancer: Longitudinal trends identify high-risk metastatic phenotypes 24 months prior to diagnosis.” *Translational Oncology* (2026). DOI: 10.1016/j.tranon.2026.102954. Abstract-only inspection; motivates the timing question but is retrospective and CRC-only.
- [K3] Fan R, Zhang Y, Feng J. “Red cell distribution width as a prognostic predictor for colorectal cancer: a meta-analysis.” *Clinical and Translational Oncology* (2026). DOI: 10.1007/s12094-026-04347-z. Abstract-only inspection; bounds RDW interpretation through heterogeneous post-diagnosis prognosis evidence.

Attached source snapshots are [episode2-K1-hamilton-2008.txt](episode2-K1-hamilton-2008.txt), [episode2-K2-sala-2026.txt](episode2-K2-sala-2026.txt), [episode2-K3-fan-2026.txt](episode2-K3-fan-2026.txt), and [episode2-key-references.json](episode2-key-references.json). The bounded audit output is [episode2-selection-diagnostic.json](episode2-selection-diagnostic.json), with the source data remaining read-only.
