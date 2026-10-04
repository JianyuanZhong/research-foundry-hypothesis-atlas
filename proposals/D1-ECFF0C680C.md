# Prospectively separating portable laboratory-observation response from hospital templates in eICU

## Status and scientific deliverable

This is a substantive child of `[prior hypothesis]` and a planned experiment, not an executed result. It preserves the parent's fixed cohort, 24-hour landmark, seven-day in-hospital mortality outcome, target-standardized whole-hospital-held-out estimand, laboratory panel, artifact/severity/end-of-life/disposition gates, and noncausal limits.

The parent localizes transport loss with target-hospital template estimation, but that transductive diagnostic does not establish that a portable component can be learned before a new hospital is seen. The future solver must therefore newly fit, using source hospitals only:

1. the frozen value-only (B-V) and raw value-plus-observation (B-RAW) elastic-net pair;
2. a simple zero-shot template-subspace residualization (B-ZR);
3. an outcome-blind hierarchical recurrent measurement-hazard model with explicit shared patient-response and source-hospital template branches (H-INV), followed by the same class of mortality head; and
4. independent erasure, hospital-leakage, transport, artifact, severity, EOL and disposition tests on identical splits.

No target hospital's aggregate masks, values, outcomes, identity embedding, normalization constants, calibration fit, early stopping, or hyperparameter selection may enter B-ZR or H-INV. Target patient data are used only one patient at a time to generate frozen predictions. Target covariates may be aggregated afterward solely to construct the parent's target-standardized evaluation weights.

Completion requires cohort/split/source manifests; all fitted nuisance, representation and mortality models; source and target predictions; repeat-response and hospital-probe predictions; transport and target-standardized metrics; gate results; uncertainty; and a machine-readable conclusion tied to those outputs. Confirmation is not required.

## Scientific opening, evidence, and falsifiable claim

The strongest claim supported by inspected evidence is narrower than this proposal. Laboratory presence, frequency, and timing can carry outcome-associated healthcare-process information beyond values [K1]. eICU mortality models can lose discrimination and calibration across hospitals [K2]. Recurrent models can learn values, masks, and elapsed times in irregular clinical sequences [K3]. These works do not show that hospital-template signal can be removed prospectively without also deleting clinically meaningful patient-responsive monitoring, and do not show that an apparently invariant representation has not merely hidden hospital identity from a weak auditor.

The unresolved hypothesis is:

> In adults still in the ICU and hospital at hour 24, a source-only representation can separate a shared, patient-responsive component of first-day laboratory observation history from source-hospital timing/analyte templates, such that the shared component retains outcome-blind abnormality-triggered repeat-measurement information and incremental seven-day mortality prediction while reducing target-standardized whole-hospital transport loss and carrying no material hospital identity beyond measured case mix.

The strongest rival is two-sided. Template removal may erase concern-compatible monitoring because patient response and workflow occupy the same statistical directions; alternatively, a learned encoder may leave workflow shortcuts intact while merely making hospital identity hard for its training adversary to decode. The methods must therefore pass both a preservation gate and an independent site-leakage gate. Passing only one is not separation.

The clinical advance would be a prospective model-development decision. A supported result justifies studying a frozen portable observation representation before deployment; an erasure result favors value-only modeling or richer physiology; hidden-site leakage argues against claims of invariance; and absence of a raw transport penalty makes mitigation unnecessary for this endpoint. None authorizes changing test ordering.

## Frozen population, temporal boundary, and outcome

Use eICU snapshot [source checksum].

- Map age `> 89` to 90; require age >=18, `unitvisitnumber == 1`, `unitdischargeoffset > 1440`, and `hospitaldischargeoffset > 1440`.
- Determine hospital eligibility before person exclusion at >=500 eligible landmarks; never select on deaths or performance.
- Exclude all eligible rows for any `uniquepid` occurring at more than one eligible `hospitalid`; keep repeat stays at one hospital together in all splits/resampling.
- Do not require any lab result.
- Input window is ICU minute 0 through 1440 in 12 two-hour bins; minute 1440 belongs to the final bin.
- A laboratory result is available only when `0 <= labresultoffset <= 1440` and `max(labresultoffset, nonmissing labresultrevisedoffset) <= 1440`.

The inherited audited frame is 69 hospitals, 81,176 stays and 72,158 people. The 595 stays with hospital discharge status outside {Alive, Expired} may enter outcome-blind observation fitting but are excluded from all supervised mortality fits and metrics. The supervised cohort is 80,581 stays with 4,897 deaths.

Primary outcome: `hospitaldischargestatus == "Expired"` and `1440 < hospitaldischargeoffset <= 11520`, death in the index hospital during the seven days after the landmark. Alive discharge by the horizon is a non-event; later and post-discharge deaths are unavailable. Secondary fixed outcomes are death by offset 4320 and the parent's ordered day-7 disposition states: death; alive hospital discharge; alive ICU discharge without hospital discharge; still in the index ICU/hospital. The primary cohort is never conditioned on remaining hospitalized after hour 24.

## Exact read-only data bindings

All sources are ordinary gzip CSV files, not archive members, under
`[internal dataset path]`.
Sources remain read-only; all analyses and derived files are written in the workspace.

1. `patient.csv.gz`, table `patient`, [source checksum]. Join/stay key `patientunitstayid`; grouping keys `uniquepid`, `patienthealthsystemstayid`; site key `hospitalid`. Required columns: `age`, `gender`, `ethnicity`, `unitvisitnumber`, `unittype`, `unitadmitsource`, `unitstaytype`, `apacheadmissiondx`, `unitdischargeoffset`, `unitdischargestatus`, `unitdischargelocation`, `hospitaldischargeoffset`, `hospitaldischargestatus`, `hospitaldischargelocation`.
2. `lab.csv.gz`, table `lab`, [source checksum]. Row key `labid`; join key `patientunitstayid`; time fields `labresultoffset`, `labresultrevisedoffset`; required content/audit fields `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`, `labmeasurenameinterface`. De-duplicate `labid`; exact stay/name/time/value collapse is an artifact sensitivity.
3. `apachePatientResult.csv.gz`, table `apachePatientResult`, [source checksum]. Join `patientunitstayid`; select one audited `apacheversion == "IVa"` row; use only `acutephysiologyscore` and `apachescore` in severity gates. Never use predicted/actual mortality or LOS fields.
4. `apacheApsVar.csv.gz`, table `apacheApsVar`, [source checksum]. Join `patientunitstayid`; use `vent`, `intubated`, `dialysis`, `urine`, `eyes`, `motor`, `verbal` as non-laboratory severity/support fields; documented -1 sentinels are missing. Untimed fields cannot enter the primary ordered representation.
5. `carePlanEOL.csv.gz`, table `carePlanEOL`, [source checksum]. Row key `cpleolid`; join `patientunitstayid`; times `cpleolsaveoffset`, `cpleoldiscussionoffset`; field `activeupondischarge`. First-day exclusion/stratification is sensitivity only.
6. `hospital.csv.gz`, table `hospital`, [source checksum]. Key `hospitalid`; `numbedscategory`, `teachingstatus`, `region` are descriptive heterogeneity fields and never predictors.

The fixed exact `labname` panel is sodium, potassium, chloride, bicarbonate, BUN, creatinine, glucose, calcium, Hgb, WBC x 1000, platelets x 1000, albumin, lactate and pH. Bilirubin remains excluded because the inherited full scan found zero exact-name support. A frozen clinician-approved `labmeasurenamesystem` conversion and plausibility map is required. Interface strings and revision delays are audit-only.

Availability has already been bounded: 1,572,519 numeric panel rows available by the landmark; analyte support ranges from 22,835 stays for lactate to 75,120 for potassium; 28,762 nominally in-window rows were revised after the landmark; 5,069 exact stay/name/time/value duplicates were found. APACHE-IVa, APS and first-day EOL links cover 72,552, 79,013 and 461 frame stays, respectively. These are feasibility observations, not hypothesis results. No further data probe is needed before compilation.

## Shared preprocessing and frozen splits

Create 12 analyte-by-two-hour value and observation tensors. After unit conversion and range QC, retain the last available value per bin. Value summaries are first, last, minimum, maximum, robust slope and the imputed 12-bin path. Observation fields are mask, count, first/last time, elapsed time, intermeasurement gap, and 15-minute co-documentation batch size.

Before first observation, impute from source-training conditional distributions; after observation, carry forward. Use five fixed posterior draws. Scaling, winsorization, vocabulary, imputation, nuisance fitting and all tuning use source hospitals only. Common covariates are age, gender, ethnicity, ICU type/source/stay type and a source-training vocabulary for admission diagnosis. Hospital descriptors, IDs, discharge fields, APACHE outcome predictions, interface strings, revision delays and post-landmark data never enter a primary mortality model.

Use the parent's deterministic ten outer whole-hospital folds, hospital-size strata, and person-grouped source development/calibration/internal-test split. Every target hospital is absent from fitting and tuning. Inside each outer training set, construct nested leave-one-source-hospital-out folds for choosing B-ZR rank and H-INV hyperparameters. No outer target record, even without an outcome, enters these choices.

For target hospital h, directly standardize the frozen source internal-test predictions to h on the parent's age, sex, ICU type and broad diagnosis strata after all predictions are made. Publish uncapped/capped weights, effective sample size and support. Effective sample size <200 or any required capped weight >20 makes h poor-overlap and excludes it from the primary median while retaining a flagged descriptive result. This target standardization defines the estimand; it is not model adaptation.

## Matched outcome models

All mortality heads use identical labeled source rows, outcomes, common covariates, calibration procedure and hyperparameter grid.

- **B-V:** elastic-net logistic regression on common covariates and value paths/summaries only.
- **B-RAW:** B-V plus raw mask/count/gap/batch summaries.
- **B-ZR:** B-V plus the source-only residualized observation representation below.
- **H-INV:** B-V plus the source-only shared representation from the hierarchical recurrent model below.

Elastic-net mixing is {0, .25, .5, .75, 1}; inverse regularization C is {.01, .1, 1, 10, 100}; ties choose stronger penalty. Source calibration log loss selects tuning. Optimization may use class weights, but probability calibration and metrics are unweighted. Fit five imputation seeds and average predictions. The same linear mortality head prevents outcome-model capacity from masquerading as better separation.

## Simple baseline: zero-shot template-subspace residualization

Within each outer source-training set, fit an outcome-blind elastic-net discrete-time model for each analyte/bin measurement indicator using only past available values and abnormality distance, prior masks/counts/gaps, common covariates, analyte and clock terms. Do not include hospital in this pooled patient-state expectation.

For each source hospital, compute leave-one-person-out mean residual vectors in case-mix cells defined by age band, ICU type, broad diagnosis and decile of the B-V source risk score. Directly standardize these hospital residual means to the pooled source case mix. Stack the standardized hospital templates and obtain their weighted principal-component basis. Choose rank from {0,1,2,4,8,12} only in nested held-out source hospitals by the prespecified lexicographic rule: first satisfy the independent hospital-leakage equivalence gate below, then maximize abnormality-triggered repeat prediction; never inspect mortality outcomes for rank choice.

For every source or unseen target patient, subtract the pooled patient-state expectation and project the complete observation residual vector onto the orthogonal complement of the frozen source-template basis. The resulting features and patient-state expectation summaries form B-ZR. No target centering, quantiles, PCA refit or aggregate mask statistics are permitted.

This baseline is transparent and genuinely zero-shot. Its weakness is scientifically central: if concern-responsive patterns align with source template directions, projection will erase them.

## Learned alternative: hierarchical shared-response representation

Fit an outcome-blind recurrent discrete-time measurement-hazard model for next-bin analyte masks. Inputs at time t are only common covariates, values/abnormality and changes available through t, and prior observation history. The target is the 14-dimensional measurement mask at t+1. The model has:

- a shared 32-unit GRU patient-response branch;
- source-hospital random intercepts for analyte-by-bin routine intensity;
- rank-4 source-hospital random slopes on elapsed-time and abnormality-response terms;
- shrinkage penalties that pull hospital effects to zero; and
- an explicit reconstruction loss for the full source mask using shared plus hospital branches.

To keep the shared branch from simply encoding site, use nested leave-one-source-hospital-out meta-training: set the omitted hospital effects to the population mean, predict its next masks, and optimize shared parameters for that zero-shot likelihood. A gradient-reversal hospital discriminator on the shared summary is a training regularizer only, never evidence of invariance. Choose hidden size {16,32}, random-slope rank {0,2,4}, shrinkage {.001,.01,.1}, learning rate {.0003,.001}, maximum 100 epochs and patience 10 solely by nested source-held-out next-mask log loss plus the preservation/leakage gates. Use five fixed seeds.

At an unseen target, hospital intercepts/slopes are fixed to their source population mean (zero after centering). No target embedding is estimated. H-INV mortality features are the shared hidden-state summaries, shared predicted hazards, and sequential patient innovations after removing the model's source-population routine hazard. The site branch and raw masks are not passed to the mortality head.

The alternative can retain ordered remeasurement after abnormal values and partially pool sparse analyte/bin cells, information the linear projection loses. It can also hide site nonlinearly. Therefore its own discriminator is ignored at evaluation; independent frozen linear and gradient-boosted probes are required.

## The smallest discrimination experiment

### Preservation: concern-compatible patient response

Define an outcome-blind repeat task whenever an analyte has a valid measurement in bins 1-10: predict whether that analyte is measured again within the next two bins (four hours). Required predictors are preceding standardized abnormality magnitude, signed change when available, elapsed time, common covariates and prior process history. Evaluate held-out log loss and calibration in each unseen hospital.

For each representation, report incremental repeat-task deviance beyond a patient-state model without process representation, and the interaction between abnormality magnitude and representation. Also report normal-value repeats and clock-only repeats. A portable representation should improve abnormality-triggered repeat prediction in unseen hospitals, not merely reconstruct routine clock/analyte frequency. This remains concern-compatible; order reasons and intent are absent.

### Independent hospital leakage

After each representation is frozen, train two auditors not used in representation fitting: multinomial elastic net and gradient-boosted trees. Predict hospital among source-internal patients with person-grouped splits, then repeat as a post-hoc pooled audit of outer-held-out representations. Compare balanced accuracy and cross-entropy with auditors using common covariates and value history alone. The equivalence margin is a prespecified 0.02 absolute balanced-accuracy advantage over that measured-case-mix reference; both probe intervals must lie below the margin. Report hospital reconstruction from the excluded site branch as a positive control.

Low adversary accuracy alone is insufficient. If either independent probe exceeds the margin, the method may have hidden rather than removed site information and fails the primary separation claim.

### Template transplant and negative controls

Using only source-trained template basis/effects, transplant each source hospital template into source-internal patients while values and shared patient features remain fixed; B-ZR and H-INV predictions should be materially less sensitive than B-RAW. In targets, apply no estimated target template. Run 10%/30% MCAR deletion and source-template-shaped deletion as generic information-loss controls; never synthesize a lab value. A method that is equally sensitive to generic deletion and template transplant has not shown selective workflow removal.

## Transport estimands

For representation r in {RAW, ZR, H-INV} and target hospital h, define incremental utility over B-V:

`U_r^E(h) = LL_BV^E(h) - LL_r^E(h)`

`U_r^I(h) = LL_BV^(source internal standardized to h) - LL_r^(source internal standardized to h)`.

Positive U is useful. Transport loss is `D_r(h)=U_r^I(h)-U_r^E(h)`; positive D means incremental process utility is lost across the hospital boundary. The primary summaries are hospital-median U and D with size-weighted estimates secondary.

The prospective separation contrast is `S_r = median_h[D_RAW(h)-D_r(h)]`; positive S means the source-only representation reduces raw-process transport loss. Retained signal is `R_r = median_h U_r^I(h)` plus held-out repeat-task deviance. H-INV versus B-ZR is a matched comparison on the same patients and folds. Report log loss, Brier, AUROC, AUPRC, calibration intercept/slope, observed/expected ratio, and decision-curve net benefit at 2%, 5%, 10%, 20%, alerts per 100 and deaths captured.

Use 2,000 paired hierarchical bootstrap replicates resampling hospitals then people; keep all model and representation contrasts paired. Report hospital heterogeneity, five-seed variability and Monte Carlo error separately. No target outcome may choose a threshold, representation or conclusion rule.

## Required severity, artifact, EOL, and disposition gates

- **Severity/case mix:** repeat in the 72,552 IVa-linked and 79,013 APS-linked subsets, first with non-laboratory support variables and then with full APACHE score. Repeat within severity strata. Because these fields are untimed and partly measurement-derived, attenuation is compatible with measured severity; persistence does not identify concern.
- **Interface/timing artifact:** repeat after exact duplicate collapse; result-offset-only versus conservative revised-offset availability; restriction to system-unit/analyte combinations present in >=90% of source hospitals; exclusion of unresolved unit/range hospitals; and stratification by interface/revision-delay summaries. Interface fields never enter a model.
- **EOL:** repeat after excluding any first-day EOL save/discussion and separately the broad parent rule. The 461 linked records do not establish complete goals of care.
- **Disposition:** fit the same four heads for the prespecified day-7 multinomial state and report state calibration. If retained process signal primarily predicts alive ICU/hospital transition rather than death, interpret it as disposition/workflow compatible, not portable mortality concern.
- **No-lab and sparse-lab:** retain no-lab stays in B-V and all outcome denominators; report representation behavior and uncertainty rather than requiring complete panels.

A primary claim cannot be rescued by a sensitivity subset. Dominance by any gate makes the result adverse to the broad claim or inconclusive as specified below.

## Falsification and interpretation

Support for prospective separation requires all of the following:

1. B-RAW has source-internal incremental utility and positive transport loss, establishing a problem to separate rather than assuming one.
2. H-INV has positive source-internal mortality utility and improves unseen-hospital abnormality-triggered repeat log loss beyond patient state alone; its repeat gain is not dominated by normal-value clock repeats.
3. `S_H-INV > 0` with a 95% interval above zero, H-INV target utility is positive, and calibration or net benefit improves relative to B-RAW rather than AUROC alone.
4. Both independent hospital probes satisfy the 0.02 equivalence margin, while the excluded site branch reconstructs hospital as a positive control.
5. H-INV is less sensitive than B-RAW to source-template transplant without equal sensitivity to MCAR deletion; conclusions persist through severity, artifact, EOL and disposition gates.
6. H-INV retains more repeat-response and source mortality utility than B-ZR at comparable leakage. This establishes substantive value of learned temporal separation over simple projection.

The separation claim is **falsified/adverse** in any of four interpretable ways:

- **No shortcut problem:** B-RAW has no precise source gain or no excess transport loss.
- **Erasure:** leakage falls, but B-ZR or H-INV loses abnormality-triggered repeat skill and source utility, or performs no better than B-V.
- **Shortcut concealed:** source/target utility persists but either independent hospital probe exceeds the equivalence margin, template transplant remains damaging, or apparent robustness disappears after interface cleanup.
- **Not transportable:** the representation passes preservation/leakage gates internally but `S_r <= 0`, target calibration worsens, or target utility is nonpositive.

If B-ZR passes all gates and is noninferior to H-INV, the broader separation claim may be supported but the learned alternative is unnecessary. If H-INV preserves repeat signal but not mortality utility, the process component is transportable descriptively but not useful for this outcome. If mortality utility persists without repeat-response skill, it cannot be labeled concern-compatible.

Results are **inconclusive** if intervals overlap supportive and adverse regions; fewer than 30 outcome-supported hospitals pass overlap/QC; model rows differ; representation seeds disagree materially; either method fails convergence; the site-branch positive control fails; source-template rank is unstable; or artifact/EOL/disposition strata dominate with insufficient precision. An imprecise null is not invariance. No post-hoc subgroup, rank, threshold or outcome replaces the primary result.

Even a supportive result establishes predictive separation only for this eICU era, panel, endpoint and representation tests. It does not identify clinician intent, prove a causal testing policy, show tests are unnecessary, rank hospitals, or establish deployment safety. Those stronger claims require order-entry reasons, protocol/staffing/vendor data, clinician review, contemporary external data, a prospective silent validation, and ultimately an impact or quasi-experimental study.

## Required outputs and verifier contract

Required machine-readable outputs:

- `cohort-flow.json`, including 81,176 frame, 595 unknown outcomes, 80,581 supervised rows and per-hospital events;
- `source-manifest.json`, `unit-harmonization.csv`, `split-manifest.json`, and `feature-manifest.json`;
- `model-manifest-{BV,BRAW,BZR,HINV}.json`, including target-data prohibition checks, seeds, fits and hashes;
- `template-basis.parquet`, `hierarchical-components.parquet`, and source-only fit provenance;
- `mortality-predictions.parquet`, `repeat-predictions.parquet`, `hospital-probe-predictions.parquet`;
- `target-standardization.json`, overlap/effective-size diagnostics and hospital-level metrics;
- `transport-estimands.json`, `gate-results.json`, `bootstrap-intervals.csv`, calibration and decision curves;
- `claims.json`, where every conclusion names output fields and is labeled supportive, adverse or inconclusive.

The verifier can recompute cohort/time logic, joins, outcome labels, split leakage, absence of target aggregate fitting, feature-channel exclusions, residual projection, zero random effects at target, metrics, probes, perturbations, gates and conclusion rules. It must test synthetic bundles for support, erasure, hidden shortcut, absent raw transport problem and inconclusive uncertainty, and reject correct computation paired with causal, intent or deployment claims. It cannot adjudicate unit plausibility, clinical concern, order appropriateness, EOL meaning, alert thresholds, fairness, causality or safety.

## Method selection, alternatives, and resources

The simple baseline is selected because source-template projection is auditable and zero-shot. The hierarchical alternative is selected because patient-responsive remeasurement is sequential and may share directions with routine templates; partial pooling and leave-one-hospital-out hazard learning can retain that signal while isolating routine intercepts/slopes. The comparison tests a scientific uncertainty, not a small prediction gain.

Deferred alternatives:

- Domain-adversarial mortality training alone is rejected as the primary method because fooling its own discriminator can hide shortcuts; it remains only a regularizer challenged by independent probes.
- The parent's target embedding remains a transductive attribution sensitivity, not evidence of prospective portability.
- GRU-D mortality without an explicit site branch mixes outcome capacity and missingness reliance; revisit only if H-INV shows portable temporal information not captured by the common linear head.
- A joint latent-physiology point process could better model unobserved state but is weakly identified without orders, treatments and richer timed physiology.
- Causal policy estimation is deferred because policy changes, instruments, order reasons and complete treatment data are unavailable.

Measured preprocessing/linkage probes from the parent took 59.8 seconds, 45.8 seconds and 2.8 seconds on CPU. They establish data feasibility, not model runtime. Unverified future solver estimate: 12-16 CPUs, 96-128 GiB RAM and one allocated A100 80-GB GPU; 2-3 CPU-hours for extraction, elastic nets, probes and bootstrap, and 4-7 GPU-hours for nested/five-seed recurrent fits, under 100 GB derived storage. The configured ceiling is 16 CPUs, 8 GPUs, 262,144 MiB and 28,800 seconds. Cached `ehr-campaign-gpu:20260908` should be checked for PyTorch, pandas, scikit-learn, a gradient-boosting package and pyarrow. No discovery GPU probe is needed; feasibility is an unverified plan under documented allocation, not an executed benchmark.

## Exactly three inspected key works

[K1] Agniel D, Kohane IS, Weber GM. *Biases in electronic health record data due to processes within the healthcare system: retrospective observational study.* BMJ. 2018;361:k1479. doi:10.1136/bmj.k1479. Relevant full-text abstract, introduction, methods and results passages were inspected in the attached provider excerpt.

[K2] Singh H, Mhasawade V, Chunara R. *Generalizability challenges of mortality risk prediction models: A retrospective analysis on a multi-center database.* PLOS Digital Health. 2022;1:e0000023. doi:10.1371/journal.pdig.0000023. Relevant full-text abstract, results, discussion and limitations passages were inspected in the attached provider excerpt.

[K3] Che Z, Purushotham S, Cho K, Sontag D, Liu Y. *Recurrent Neural Networks for Multivariate Time Series with Missing Values.* Scientific Reports. 2018;8:6085. doi:10.1038/s41598-018-24271-9. Relevant full-text abstract, methods, datasets and results passages were inspected in the attached provider excerpt.

## Provenance and limits

The three parent excerpts were re-inspected and their unchanged byte hashes verified; they are provider-returned relevant excerpts, not complete original sources. This child changes the scientific contribution mappings but preserves the original receipts. Private source rows are not attached. eICU represents participating hospitals in 2014-2015 and one tele-ICU ecosystem. Result time is not order time, revised time is only a conservative availability proxy, clinician concern is unobserved, and post-discharge mortality is unavailable.
