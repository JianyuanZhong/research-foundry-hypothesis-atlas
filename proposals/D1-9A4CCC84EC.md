# Conditional observation intensity and mortality-model transport across eICU hospitals

## Status and actual scientific deliverable

This is a compilation-ready, falsifiable experiment, not an executed model result. It is a substantive child of [prior hypothesis] and preserves its audited 24-hour eligibility frame, laboratory panel, landmark, outcome horizon, and read-only bindings.

The future solver must newly fit: (1) a matched elastic-net value-only versus value-plus-observation mortality pair; (2) a simple physiology-matched perturbation baseline; and (3) an outcome-blind hierarchical observation-intensity model that decomposes laboratory measurement events into a shared response to observed physiology/history, a partially pooled hospital template, and a patient-level residual. It must apply both attribution methods on identical whole-hospital holdouts and quantify whether the observation-aware model's excess transport loss is preferentially removed by hospital-template normalization rather than by breaking patient-specific residual observation signal.

Completion is established by frozen cohort and split manifests; fitted mortality and intensity models; held-out mask and mortality predictions; matched and model-based perturbations; transport, calibration, decision, uncertainty and overlap outputs; and conclusion records linked to computed fields. The hypothesis need not be confirmed.

## Scientific opening, supported claim, and unresolved hypothesis

The strongest existing evidence supports only these claims. Laboratory presence, frequency, and timing can carry outcome-associated healthcare-process information beyond result values [K1]. eICU mortality-model discrimination and calibration can vary across hospitals [K2]. Recurrent models can learn from values, masks, and elapsed times in irregular clinical sequences [K3]. None establishes that hospital testing policy causes transport failure, or even that a transport penalty attributed to masks is not measured severity, clinician concern, or interface behavior.

The unresolved hypothesis is:

Among adults still in the ICU and hospital at 24 hours, a first-day laboratory observation channel will improve source-hospital prediction of death during ICU minutes 1441-11520, but the excess loss of that gain at unseen hospitals will be carried primarily by the hospital-template component of observation intensity after conditioning on prior measured physiology and case mix, rather than by a shared physiology-responsive component or patient-specific residual observation signal.

This is a predictive attribution hypothesis, not a causal policy-effect hypothesis. Its clinical importance is model safety: an internally useful mortality signal should not silently become miscalibrated when the same model is moved to a hospital with different ordering, batching, documentation, or interface practices. The substantive advance over the inspected work and parent is conditional decomposition. Marginal mask divergence and raw channel shuffling cannot tell a local workflow template from the fact that sicker patients are measured more often; the proposed observation model makes those explanations yield different, prospectively specified perturbations.

## Population, temporal boundaries, and outcomes

The eligibility frame is exactly the parent's audited size-only cohort:

- Map age "> 89" to 90; require numeric age at least 18, unitvisitnumber=1, unitdischargeoffset>1440, and hospitaldischargeoffset>1440.
- Determine hospital eligibility before person exclusion using at least 500 eligible landmarks; do not select hospitals by outcome count.
- Exclude every row for any uniquepid represented at more than one eligible hospital. Retain repeated admissions within one hospital and keep every admission for a uniquepid in one split.
- Do not require any laboratory measurement.
- Use the same 69 hospitals, 81,176 stays, 72,158 people, and 4,897 audited seven-day deaths; the post-exclusion minimum is 430 stays and 14 deaths per hospital.

The 81,176-stay frame contains 595 stays without hospitaldischargestatus in {Alive, Expired}. They may contribute input-window masks to the outcome-blind observation-intensity fit, but they are never coded as alive and are excluded from mortality fitting and evaluation. Thus the supervised primary set has 80,581 labeled stays and the same 4,897 deaths. Cohort-flow.json must show both denominators.

The exposure window is ICU minute 0 through 1440. Use bins [0,120), [120,240), ..., [1320,1440], with minute 1440 assigned to the last bin. A result is available only when 0<=labresultoffset<=1440 and max(labresultoffset, nonmissing labresultrevisedoffset)<=1440.

Primary outcome: hospitaldischargestatus="Expired" and 1440<hospitaldischargeoffset<=11520, i.e. death recorded in the index hospital during the seven days after the 24-hour landmark. Alive discharge before the horizon is a non-event; death after the horizon is outside this binary horizon. Secondary outcomes are death by offset 4320, alive ICU discharge by 11520, alive hospital discharge by 11520, and a descriptive three-state day-7 outcome. No post-discharge death is available.

## Exact read-only bindings

Snapshot: [source checksum]. Each source is an ordinary gzip CSV, not an archive member, under [internal dataset path] 2.0数据/. Sources remain read-only; all derived artifacts go in the workspace.

1. patient.csv.gz, table patient, [source checksum]. Primary key/join patientunitstayid; person grouping uniquepid and patienthealthsystemstayid; split key hospitalid. Required columns: age, gender, ethnicity, unitvisitnumber, unittype, unitadmitsource, unitstaytype, apacheadmissiondx, unitdischargeoffset, unitdischargestatus, unitdischargelocation, hospitaldischargeoffset, hospitaldischargestatus, hospitaldischargelocation.

2. lab.csv.gz, table lab, [source checksum]. Row key labid; many-to-one join patientunitstayid. Required fields: labresultoffset, labresultrevisedoffset, labname, labresult, labresulttext, labmeasurenamesystem, labmeasurenameinterface. De-duplicate labid. The primary analysis keeps all distinct measurements; exact stay/labname/offset/value collapse is an artifact sensitivity.

3. apachePatientResult.csv.gz, table apachePatientResult, [source checksum]. Join patientunitstayid. Select the single audited apacheversion="IVa" row and use only acutephysiologyscore and apachescore in measured-severity sensitivity analyses. Never use predicted or actual mortality/LOS fields.

4. apacheApsVar.csv.gz, table apacheApsVar, [source checksum]. Join patientunitstayid. Use vent, intubated, dialysis, urine, eyes, motor, verbal as measured support/severity proxies; documented -1 values are missing. These fields lack event timestamps and therefore cannot enter the primary temporally ordered observation-intensity model.

5. carePlanEOL.csv.gz, table carePlanEOL, [source checksum]. Row key cpleolid; join patientunitstayid; time fields cpleoldiscussionoffset and cpleolsaveoffset; activeupondischarge. Exclude or stratify records saved or discussed in minutes 0-1440 in sensitivity analysis. This is incomplete documentation, not goals-of-care adjudication.

6. hospital.csv.gz, table hospital, [source checksum]. Key hospitalid; numbedscategory, teachingstatus, region are descriptive heterogeneity fields only, never primary predictors or outcome-model tuning inputs.

Exact labname panel: sodium, potassium, chloride, bicarbonate, BUN, creatinine, glucose, calcium, Hgb, WBC x 1000, platelets x 1000, albumin, lactate, pH. The audited availability range is 92.5% for potassium to 28.1% for lactate; pH is 39.2% and albumin 45.2%. The zero-support exact string bilirubin remains excluded. The audit found 1,572,519 numeric panel rows available by landmark, 28,762 nominally in-window rows revised after landmark, and 5,069 exact stay/name/time/value duplicates. A clinician-approved fixed system-unit conversion map and physiologic plausibility ranges are required before fitting; interface strings are diagnostics only.

All four configured datasets remain directly accessible and read-only. This experiment uses eICU because the hypothesis and 69-hospital boundary are eICU-specific; no cross-dataset validation is claimed.

## Shared preprocessing and value representation

All unit mapping, clipping, vocabulary, scaling, imputation, and tuning statistics are learned or approved without target outcomes. Create 12 two-hour bins. For each analyte/bin retain the last value available by the bin end after unit harmonization. Build value summaries (first, last, minimum, maximum, robust slope and 12-bin trajectory) and explicit process channels (binary mask, count, first/last time, elapsed time, inter-measurement gaps and 15-minute co-order count).

Before first observation, impute from training-hospital conditional distributions; afterward carry forward the last available value. Use five fixed posterior-predictive draws and average mortality probabilities. Neither the imputer nor the value-only outcome model receives raw masks, counts, time gaps, hospital ID, interface, revision delay, or target outcome. Report how well the completed value tensor predicts original masks; value-only means explicit-process-blinded, not proof that selection information has been erased.

Common covariates are age, gender, ethnicity, unittype, unitadmitsource, unitstaytype and a training-only vocabulary for apacheadmissiondx. No discharge field, hospital descriptor, APACHE outcome prediction, post-landmark datum, interface string, or revision delay is a primary predictor.

## Frozen hospital-held-out splits

Assign the 69 hospitals to ten outer folds. Within quartiles of pre-outcome eligible hospital size, sort hospitals by SHA-256 of "eicu-obs-intensity-v2|hospitalid" and allocate round-robin to folds. Record hospital IDs and hashes before outcome modeling. Each hospital is an untouched mortality test site once.

Within the remaining source hospitals, assign uniquepid by SHA-256 of "eicu-obs-intensity-v2|uniquepid" to development 70%, calibration 15%, and internal test 15%. All admissions for a person stay together. Mortality tuning, early stopping and recalibration use only source development/calibration rows. Target outcomes are never used for preprocessing, model fitting, intensity-template inference, perturbation construction, threshold choice, or stopping.

For each target hospital h, directly standardize the source internal test to h on age, sex, ICU type and broad admission-diagnosis strata. Report overlap, effective sample size and uncapped/capped weights. If effective sample size is below 200 or a capped weight would exceed 20, mark that hospital's standardized comparison as poor-overlap rather than silently extrapolating.

## Simple matched baseline

Fit on identical rows and splits:

- B-V: elastic-net logistic mortality model on common covariates and value trajectories/summaries, with training-only standardization and no missing indicator.
- B-VO: the identical model and hyperparameter grid plus explicit mask/count/gap/co-order summaries. Select penalty and mixing parameter by source calibration log loss; fit five imputation draws and average probabilities.

Use inverse-frequency class weights only during optimization and retain unweighted probabilities; recalibrate each model with source calibration data using logistic intercept and slope. Search elastic-net mixing in {0, 0.25, 0.5, 0.75, 1} and inverse regularization C in {0.01, 0.1, 1, 10, 100}; ties choose the stronger penalty. Freeze this grid before outer evaluation.\n\nFor attribution, construct two outcome-blind donor operations after freezing predictions. Match exactly on target hospital where required, ICU type and broad diagnosis, and within calipers on B-V risk, age and multivariate value-trajectory distance. The primary match excludes APACHE to retain all labeled rows; repeat within APACHE-IVa quartile/missingness and vent/intubated/dialysis strata.

- Person-signal disruption: within a target hospital, swap the complete process vector among matched patients. Hospital marginals are preserved while association with the individual is broken.
- Site-template substitution: use a matched donor from another hospital and swap only the process vector, keeping recipient covariates, completed values and outcome fixed.

Use optimal full matching without replacement within each replicate, 100 prespecified random tie-break seeds. Require at least 80% recipient coverage and standardized mean differences below 0.10 for age, B-V risk and value summaries; otherwise the matched attribution result is inconclusive. These are synthetic, internally inconsistent records and diagnose model reliance, not effects of changing care.

## Learned mechanistic alternative: observation-intensity decomposition

Fit an outcome-blind discrete-time model for whether analyte a is newly available in bin t:

logit P(M_iat=1 | V_i,t, O_i,t, h) = alpha_a,t + f_theta(V_i,t, X_i)_a + g_phi(O_i,t)_a + lambda_a^T z_h + kappa_t^T z_h.

V_i,t contains only normalized laboratory values and abnormality distances available before bin t plus common covariates X_i. O_i,t separately contains prior masks, cumulative counts and elapsed times. f_theta and g_phi are separate one-layer 32-unit GRU encoders shared across hospitals, preventing prior observation history from being mislabeled as physiology. z_h is a four-dimensional shrinkage-penalized hospital embedding; analyte and time loadings yield a partially pooled hospital template. Missing labels and mortality outcomes never enter this likelihood. Optimize Bernoulli negative log likelihood with Adam, batch size 256, learning rate in {0.0003, 0.001}, L2 hospital-embedding penalty in {0.001, 0.01, 0.1}, maximum 100 epochs, patience 10, and five fixed seeds; choose only by source calibration mask log loss. Keep the global and hospital parameter count and convergence diagnostics in the model manifest.

For an unseen target hospital, freeze alpha, f_theta, lambda and kappa and estimate z_h from that hospital's unlabeled first-day values/masks only. This transductive step is allowed solely for attribution diagnostics and cannot recalibrate or replace the zero-shot mortality model. The components are:

- stable measured-physiology response: alpha+f_theta;
- shared observation-history response: g_phi, interpreted only as a monitoring-memory/concern proxy;
- hospital template: lambda^T z_h+kappa^T z_h;
- person-level residual: observed mask minus full fitted probability.

Compare held-out mask log loss, Brier score and calibration with a marginal analyte-by-bin frequency model and a nonrecurrent elastic-net intensity model. The learned decomposition is admissible for claim support only if its hospital-held-out mask log-loss interval is below the marginal baseline and calibration is not materially worse. Otherwise retain the matched baseline and label mechanistic attribution failed/inconclusive.

Using common random numbers, generate 100 masks per patient under: (a) the fitted target hospital template; (b) the pooled source template z=0 while preserving each patient's physiology and shared observation-history responses; (c) the target template with the shared observation-history component neutralized to the source median while preserving physiology; and (d) a target template with person residuals permuted within fitted-propensity deciles. Simulate bins sequentially so generated prior masks update O_i,t; never replace or synthesize laboratory values. Recompute only explicit process channels and pass them through frozen B-VO while keeping the completed value tensor fixed.

This alternative reveals time-ordered remeasurement after abnormal values, partial pooling across sparse analyte/bin cells, and a conditional hospital template. The matched baseline loses that temporal response and can confuse case-mix imbalance with policy. Conversely, the learned model is assumption-dependent; agreement between both methods is required for a strong attribution statement.

## Estimands and evaluation

Primary metric is log loss. For model m and target hospital h, define Delta_m^E(h)=LL_m^E(h)-LL_BV^E(h), and Delta_m^I(h)=LL_m^(I standardized to h)-LL_BV^(I standardized to h). The hospital-level transport excess is T_h=Delta_BVO^E(h)-Delta_BVO^I(h). The primary summary is the hospital median T_h; positive values mean explicit observation information loses more incremental value at the hospital boundary.

The source utility estimand is the source-internal LL_BVO-LL_BV. The hypothesis requires an internal gain, not merely a transport contrast.

For each attribution method q, recompute T after pooled-source site-template normalization and define A_site,q=T_raw-T_site-neutral,q. Positive A_site means removing the estimated site template reduces excess transport loss. For the learned model also define A_shared,OI=T_raw-T_shared-history-neutral,OI. Separately define C_person,q=LL_person-shuffled^E-LL_raw^E; positive values mean patient-specific residual observation signal was useful in the target. Contrasting A_site with A_shared and C_person distinguishes the prespecified explanations, but none is causal mediation and C_person is not clinician intent.

Secondary analyses:

- Jensen-Shannon marginal observation divergence versus learned conditional hospital-template distance as predictors of T_h;
- AUROC, AUPRC, Brier, calibration intercept/slope, observed/expected risk, and decision-curve net benefit at 2%, 5%, 10% and 20%, plus alerts per 100 and deaths captured;
- 48-hour death, alive ICU discharge, alive hospital discharge and three-state day-7 outcomes;
- hospital predictability from raw process channels, from conditional residuals, and after interface restrictions;
- repeat the pair after adding APACHE-IVa acutephysiologyscore/apachescore and APACHE support proxies, within severity strata, and after excluding first-day EOL records.

Use 2,000 paired hierarchical bootstrap replicates: resample hospitals, then uniquepid within hospital; keep all model comparisons, matches and common-random-number perturbations paired. Report Monte Carlo error and five-seed model variability separately. Control false discovery rate for hospital-specific intervals. Do not treat stays as independent hospitals.

## Artifact, severity, concern, and timing checks

Interface/documentation artifact checks are prespecified: exact-duplicate collapse; result-offset-only versus conservative revised-offset availability; restriction to system-unit/analyte combinations represented in at least 90% of source hospitals; exclusion of unresolved range/unit hospitals; and regression of learned hospital-template coordinates on interface, unit and revision-delay summaries. Interface fields never enter mortality prediction.

Measured-severity checks add APACHE-IVa scores and support variables only in linked subsets. The bounded audit found 72,552 IVa score records and 79,013 APACHE variable records in the 81,176-stay frame. Because APACHE is partly constructed from first-day measurements and lacks event timestamps here, attenuation is evidence compatible with measured severity, not proof of confounding control.

The person residual is only a proxy for unmeasured concern. Persistence within measured physiology/severity strata is compatible with concern, protocol response, treatment, staffing, and omitted illness features. eICU lacks order-entry time/reason, clinician identity, staffing and local protocols, so clinician intent cannot be adjudicated.

## Falsification and interpretation

Support for the bounded site-specific reliance hypothesis requires all of:

1. The 95% interval for source-internal LL_BVO-LL_BV is below zero.
2. The 95% interval for the median T_h is above zero, with no single hospital determining direction.
3. Both the valid matched analysis and admissible learned decomposition give A_site>0 with 95% intervals above zero, and site-template normalization reduces more excess transport loss than either shared observation-history neutralization or person-residual disruption.
4. Learned conditional template distance relates positively to T_h and outperforms marginal divergence for that association under leave-one-hospital-out evaluation.
5. Direction persists after APACHE/EOL and unit/interface checks and is reflected in calibration or decision consequences, not only AUROC.

This supports only that site-pattern information measurably carries transport fragility for this cohort, endpoint and era.

Evidence adverse to site-specific attribution includes a precise T at or below zero; stable observation gain on unseen hospitals; A_site at or below zero by both methods; person-signal disruption accounting for the gain while site substitution adds no excess loss; marked attenuation after measured-severity conditioning; or disappearance under interface/revision cleanup. The latter results redirect interpretation toward shared concern, measured severity, or documentation artifact; they do not make the study unsuccessful.

Results are inconclusive if intervals span supportive and adverse regions, matching coverage/balance fails, the learned intensity model fails its held-out mask gate, standardization overlap is poor, model classes disagree, target events are too sparse, or findings are dominated by EOL/interface strata. An imprecise null does not establish invariance. No alternate subgroup, threshold or outcome may replace the primary result after inspection.

Even supportive results cannot establish that testing policy causes mortality, that tests are unnecessary, that changing test frequency improves outcomes, or that an alert is safe. Those claims require order intent and protocol data, clinician review, contemporary external validation, and a prospective or quasi-experimental study.

## Machine-checkable solver outputs and verifier contract

Required outputs:

- cohort-flow.json: all exclusions, 81,176 eligibility frame, 595 unknown-outcome rows, 80,581 supervised rows, and per-hospital events;
- source-manifest.json and unit-harmonization.csv: exact paths, hashes, columns, conversions, exclusions and clinical approvals;
- split-manifest.json: hospital folds, person hashes, seeds and leakage assertions;
- features.parquet schema plus feature-manifest.json: bin boundaries, availability clock and channel assignment;
- model-manifest-BV.json, model-manifest-BVO.json and model-manifest-OI.json: packages, hyperparameters, seeds, fit partitions and artifact hashes;
- mortality-predictions.parquet and mask-predictions.parquet with fold, split and model identifiers;
- matching-diagnostics.json, perturbations.parquet and simulation-diagnostics.json with seeds, coverage, balance, altered rates and common-random-number IDs;
- metrics.json, hospital-metrics.csv, bootstrap-intervals.csv, calibration/decision curves and sensitivity tables;
- claims.json, where every statement names exact output fields and is labeled supportive, adverse or inconclusive.

The verifier can recompute cohort/time logic, joins, availability, split leakage, feature exclusions, model targets, held-out metrics, matching balance, perturbation determinism, estimands and conclusion rules. It must test synthetic supportive, adverse and inconclusive bundles and reject correct calculations paired with causal, intent, appropriateness or deployment claims. It cannot adjudicate unit plausibility, protocol meaning, clinician concern, testing necessity, decision thresholds, fairness, causality or prospective safety.

## Method selection and resources

Selected simple method: elastic-net B-V/B-VO plus transparent matching, because it isolates the explicit information-set contrast and exposes balance/overlap. Selected learned alternative: the outcome-blind recurrent intensity decomposition, because the scientific uncertainty is where an observation event came from, not whether a larger mortality model gains a fraction of AUROC.

Deferred alternatives:

- The parent's GRU-D mortality pair combines outcome-model capacity with process reliance and does not itself identify site template versus concern; revisit only after the decomposition shows transportable temporal interactions that elastic net cannot represent.
- Gradient-boosted mortality models add nonlinearity but not attribution; revisit for documented underfit.
- Domain-adversarial training is mitigation before attribution; revisit only if site-template dependence is supported.
- A fully joint latent-physiology marked point process could model unobserved states but is weakly identified from this panel; revisit with order reasons, treatments, richer vitals or external protocol data.
- A causal policy study is deferred because required policy-change or instrument data are absent.

Measured parent preprocessing probes took 59.8 seconds for patient work and 45.8 seconds for panel extraction with four CPUs; the current APACHE/EOL linkage check took 2.8 seconds. These are feasibility measurements, not model runtimes. Unverified solver plan: 12-16 CPUs, 96-128 GiB RAM and one allocated A100 80-GB GPU; 2-3 CPU-hours for extraction/imputation/bootstrap and 4-7 GPU-hours for ten-fold intensity fitting and five seeds, under 100 GB derived storage and the configured ceiling of 16 CPUs, 8 GPUs, 262,144 MiB and 28,800 seconds. Elastic nets and metrics are CPU work. The cached ehr-campaign-gpu:20260908 environment should be checked for PyTorch, pandas, scikit-learn and pyarrow; a missing package is an infrastructure dependency, not scientific infeasibility.

## Exactly three inspected works

[K1] Agniel D, Kohane IS, Weber GM. Biases in electronic health record data due to processes within the healthcare system: retrospective observational study. BMJ. 2018;361:k1479. doi:10.1136/bmj.k1479. Relevant full-text abstract, introduction, methods and results passages were inspected; the attached file is a provider-returned excerpt, not the complete source.

[K2] Singh H, Mhasawade V, Chunara R. Generalizability challenges of mortality risk prediction models: A retrospective analysis on a multi-center database. PLOS Digital Health. 2022;1:e0000023. doi:10.1371/journal.pdig.0000023. Relevant full-text abstract, results, discussion and limitations passages were inspected from the attached provider excerpt.

[K3] Che Z, Purushotham S, Cho K, Sontag D, Liu Y. Recurrent Neural Networks for Multivariate Time Series with Missing Values. Scientific Reports. 2018;8:6085. doi:10.1038/s41598-018-24271-9. Relevant full-text abstract, methods, dataset and results passages were inspected from the attached provider excerpt.

## Provenance and limits

This proposal reuses the parent's inspected evidence receipts without implying new source acquisition; all three claim mappings were rechecked for this revision. Public excerpts and derived audits may be attached, but private rows must not be published. The eICU snapshot reflects participating hospitals in 2014-2015 and one tele-ICU ecosystem. Laboratory result time is not order time, revised time is only a conservative availability proxy, APACHE timing is insufficient for a primary temporal covariate, EOL documentation is incomplete, and post-discharge mortality is unavailable.
