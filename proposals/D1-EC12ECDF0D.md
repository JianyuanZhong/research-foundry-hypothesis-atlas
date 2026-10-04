# Does laboratory observation behavior change ICU escalation decisions across hospitals?

## Scientific deliverable and substantive advance

The future solver must newly construct an auditable, leakage-safe six-hour eICU stay ledger; fit a transparent matched clinical-only/process-augmented pair and a matched temporal latent-state/observation-process pair on identical stays and inputs; and quantify whether laboratory-observation behavior changes a fixed 10% escalation decision in a way that does not transport across hospitals.

Completion requires:

1. cohort flow, source/header/schema/unit audit, accepted analyte rules, exact feature ledger, duplicate and offset audit, and whole-hospital split audit;
2. out-of-fold development and held-out-hospital predictions for B0/B1 and S0/S1;
3. the primary decision-utility transport penalty at threshold 0.10, plus the proportion and outcome rate of process-induced threshold crossings;
4. AUROC, AUPRC, Brier score, log loss, calibration intercept/slope, reliability, action rate, event rate among action-positive and action-negative groups, and decision curves at 0.05/0.10/0.20;
5. ordered expired-exit/alive-exit cumulative-incidence functions, hospital-wise effects, process-only diagnostics, second-hash stability, uniquepid-cluster sensitivity and predeclared falsification permutations; and
6. a supportive, adverse or inconclusive conclusion linked to computed outputs, with computational claims separated from clinical claims.

No model has been fitted in discovery and no clinical result is claimed.

The scientific deliverable is not a new risk score alone. It is an estimate of whether the process variables change the deployment decision, how often they do so, whether those crossings are concentrated in particular hospitals, and whether a temporal observation-aware model attributes the difference to an observation channel rather than to a more faithfully represented clinical state.

## Evidence boundary, unresolved question and importance

The assigned parent establishes only a feasible, untested design: the frozen snapshot contains ICU-relative laboratory results and revision offsets, physiologic observations, hospital identifiers, admission severity fields and documented unit-exit status. The eICU-02 seed and parent do not establish that a laboratory row represents an order, clinician intent, test availability or turnaround, and no fitted transport result is available.

The unresolved claim is:

> At minute 360, among adult ICU stays with adequate follow-up, does adding only observable laboratory-observation behavior cause a clinically consequential change in a 10% expired-unit-exit escalation decision—especially extra action among clinically low-risk stays—and does that decision effect lose utility or calibration on hospitals held out from fitting?

This is a noncausal transport and measurement hypothesis. “Cause” in the operational definition means that the fitted process-augmented decision differs from the matched clinical-only decision; it does not mean clinician testing caused patient death or treatment harm.

The clinical importance is decision-specific. A model that uses testing behavior may direct monitoring or escalation review toward a hospital’s measurement regime rather than patient state. The parent measured a development-to-holdout net-benefit penalty. This successor makes the consequence explicit by decomposing that penalty into threshold crossings: stays positive only under the process model, stays negative only under it, their observed event rates, hospital concentration, and the resulting net benefit. This can inform whether process variables should be excluded, quarantined as a deployment warning, or retained only with site adaptation. It still cannot justify a care policy without action-cost and clinical-adjudication data.

The strongest supported claim before fitting is therefore data availability and design feasibility, not testing-practice dependence, mortality prediction, causality or clinical benefit.

## Population, time boundary and outcome

Use each eICU ICU stay as one observation; never concatenate later ICU stays. Include adults with patient.age >= 18, parse age > 89 as 90 with an age-censored flag, and require nonmissing patient.unitdischargeoffset > 360. The prediction landmark is ICU minute 360. No predictor may use a row, revision or derived value whose relevant time is after minute 360.

The primary target is documented expired ICU-unit exit by minute 2880, 48 hours from ICU admission. Set event time to patient.unitdischargeoffset only when patient.unitdischargestatus=Expired. Alive before minute 2880 is a competing alive-unit exit. A known-status stay with unitdischargeoffset > 2880 is event-free at the administrative boundary. NULL/other status is unknown-status censoring, never recoded as alive. Stays exiting at or before minute 360 are excluded. The primary binary target is expired exit by 2880 among known-status stays; the ordered models use the same target with alive exit retained as a competing state.

This is a documented ICU-unit-exit outcome, not exact biological death, post-ICU mortality or a treatment endpoint. A secondary all-hospital-discharge mortality analysis, if produced, must remain a separate labelled sensitivity and cannot replace or pool with the primary endpoint.

## Exact source bindings and provenance

Use the eICU snapshot [source checksum], with catalog [internal dataset path], catalog [source checksum]. All source files are read-only ordinary gzip files; the archive member is the ordinary file, not a nested archive.

- Patient source: [internal dataset path] 2.0数据/patient.csv.gz, source [source checksum]. Table patient, schema datasets/eicu/table-ab037c09d7df9a3c.json, schema [source checksum]. Join key patientunitstayid. Use gender, age, ethnicity, hospitalid, hospitaladmitsource, admissionweight, unittype, unitvisitnumber, unitdischargeoffset, unitdischargestatus and uniquepid; use no hospital-discharge field as a substitute for the ICU boundary.

- Laboratory source: [internal dataset path] 2.0数据/lab.csv.gz, source [source checksum]. Table lab, schema datasets/eicu/table-79bdb33275339b1a.json, schema [source checksum]. Join patientunitstayid. Use labid, labresultoffset, labtypeid, labname, numeric labresult, labresulttext only for audit, labmeasurenamesystem, labmeasurenameinterface and labresultrevisedoffset.

- Periodic physiology source: [internal dataset path] 2.0数据/vitalPeriodic.csv.gz, source [source checksum]. Table vitalPeriodic, schema datasets/eicu/table-a22c6d6981a32279.json, schema [source checksum]. Join patientunitstayid. Use vitalperiodicid, observationoffset, temperature, sao2, heartrate, respiration and systemicmean; deduplicate exact vitalperiodicid before aggregation.

- Admission severity source: [internal dataset path] 2.0数据/apachePatientResult.csv.gz, source [source checksum]. Table apachePatientResult, schema datasets/eicu/table-754bebf64d3d9909.json, schema [source checksum]. Join patientunitstayid. Use acutephysiologyscore, apachescore, predictedicumortality and predictediculos as admission covariates. Every actual* column is a label/audit and forbidden as a predictor.

- Hospital context source: [internal dataset path] 2.0数据/hospital.csv.gz, source [source checksum]. Table hospital, schema datasets/eicu/table-811df7b2ef435e12.json, schema [source checksum]. Join hospitalid. Use numbedscategory, teachingstatus and region only for split descriptions and transport tables, never as a patient predictor.

The dataset metadata specifies offsets in minutes from ICU admission; patient-level grouping uses uniquepid, not ICU-stay rows. The public release has no images or raw waveforms; vitalPeriodic is a five-minute summary of monitor observations. Narrative portions are removed and retained note fields are not needed for this question. The full source catalog and these table schemas, rather than a paper, establish availability.

## Leakage-safe ledger and process decomposition

Before fitting, print source row counts, duplicate-ID counts, invalid offsets, nonnumeric values, measurement-system/interface strings, unit proxies, per-hospital support and all exclusions. Deduplicate exact labid and vitalperiodicid.

A primary lab row is eligible only when 0 <= labresultoffset <= 360 and, if labresultrevisedoffset is nonblank, labresultrevisedoffset <= 360. A sensitivity ignores the revision cutoff and is labelled less availability-conservative. This uses result offset as availability time because the source has no order or turnaround timestamp; that is an observational assumption, not an order-time claim.

Freeze a 12-analyte panel by case-folded exact labname: creatinine, bun, sodium, potassium, chloride, glucose, lactate, wbc, hemoglobin, hematocrit, bilirubin and albumin. Do not add aliases after viewing held-out performance. For each analyte, a development-only accepted nonblank labmeasurenamesystem/labmeasurenameinterface pair must be specified; only rows matching it enter value summaries, and no unit conversion is permitted. If no analyte has a stable pair, remove that analyte’s value features but retain its observation indicators and mark the value branch unavailable. Conflicting, blank or nonnumeric results are excluded from value summaries and counted in the audit. Do not model labresulttext.

Clinical summaries for each accepted analyte are median, minimum, maximum, interquartile range, last value and least-squares slope over 0–360. Vital summaries use the same six statistics for temperature, sao2, heartrate, respiration and systemicmean; fewer than two time points yields a missing slope. Development medians impute missing summaries without flags. All imputation, scaling and accepted-pair decisions are development-only.

The process block contains only observation metadata: total lab rows, numeric lab rows, unique case-folded analytes, panel-analyte presence indicators, counts in [0,120] and (120,360], first/last labresultoffset, median gap across distinct offsets, fraction with explicit system/interface and rows with nonblank labresultrevisedoffset <=360. It excludes hospitalid, all unit-discharge fields, outcomes and post-landmark rows. The clinical block contains the same accepted laboratory values and vital summaries but no lab counts, missingness/presence indicators, gaps or revision metadata. B0/B1 therefore test incremental observation information beyond observed values under the same measurement limits.

For S0/S1, place the identical accepted laboratory and vital observations into 12 half-hour bins over 0–360, retaining value masks, observation times and the process indicators above. S0 allows the latent severity state to generate expired/alive hazards but blocks process-channel inputs from those hazard heads. S1 adds the process channel. Process-channel parameters may explain observation behavior, but hospital identity is never an individual predictor; any development-only hospital random intercept is excluded from deployment scoring and is used only to quantify training-site observation heterogeneity. The state dimension is fixed at 3 before fitting.

## Split, decision estimands and evaluation

Construct connected components of hospitals linked by any shared uniquepid in patient. Assign each component to 80% development or 20% held-out hospitals using SHA-256 of fixed string eicu-testing-practice-decision-v1 + NUL + sorted component hospital IDs, modulo 100; buckets 0–79 are development and 80–99 held out. Do this before cohort summaries, accepted units, imputation, model fitting, threshold choice or standardization. Report component sizes and loss. A second fixed namespace is a stability sensitivity. This is internal transport, not external validation; no independent validation partition is claimed.

Within development, use five deterministic hospital folds for out-of-fold predictions. No patient, hospital component or uniquepid may cross the outer split. If fewer than 10 held-out hospitals or fewer than 25 expired exits are available for a transport analysis, that analysis is inconclusive.

For each model m, let p_m^D and p_m^H be out-of-fold development and frozen held-out-hospital probabilities. Define action A_m(q)=1[p_m(q)>=q]. The primary decision estimand is the transport penalty in net benefit for the process augmentation:

D_NB10 = [NB_B1^D(0.10)-NB_B0^D(0.10)] - [NB_B1^H(0.10)-NB_B0^H(0.10)].

The same quantity is computed for S1 versus S0. NB = TP/N - FP/N * q/(1-q), with no post-hoc threshold or held-out recalibration.

The new primary decision decomposition is:

- Crossing-in: CI10 = P(A_B1(0.10)=1, A_B0(0.10)=0), and its observed expired-exit rate.
- Crossing-out: CO10 = P(A_B1(0.10)=0, A_B0(0.10)=1), and its observed expired-exit rate.
- Crossing contribution to net benefit: CΔNB10 = P(Y=1 and crossing-in) - q/(1-q)P(Y=0 and crossing-in) - P(Y=1 and crossing-out) + q/(1-q)P(Y=0 and crossing-out). This is exactly the B1-minus-B0 threshold-utility contribution of discordant decisions; report its development and held-out values, hospital-weighted and patient-weighted. Define decision regret as -CΔNB10 when the process model loses utility.
- Hospital concentration: the fraction of held-out hospitals in which the process model’s crossing contribution is adverse, and the 90th-minus-10th percentile hospital spread of crossing-in rate and calibration error.

The primary clinical-importance rule is supportive of process-sensitive decision harm only if B1 has a development NB10 gain >=0.005, D_NB10 >=0.005 with a two-sided 95% hospital-cluster interval excluding zero, held-out CΔNB10 is adverse by at least 0.005 or its interval excludes zero in the adverse direction, crossing-in has a lower observed event rate than crossing-out when both are estimable, the direction reproduces for S1/S0 and the second split, and at least 75% of evaluable held-out hospitals have nonnegative process-model transport loss. This is a deployment warning, not evidence that testing caused harm. The crossing result cannot be called supportive if it is driven by fewer than 10 held-out hospitals or 25 expired exits.

Adverse evidence is a process-augmented model with no material development gain and no larger held-out loss, with held-out calibration and decision utility no worse than B0 under the prespecified margin. It also includes a null or reversed crossing pattern with stable support. Inconclusive evidence includes sparse endpoints, inadequate overlap, unstable accepted units, missing accepted value units, nonconvergence or failed identifiability of S0/S1, wide intervals crossing both zero and the clinical margin, model-family discordance, or a large change under the revision-conservative sensitivity. These labels describe the hypothesis, not the quality of a hospital or a clinical policy.

Report per-hospital paired contrasts, patient-weighted and equal-hospital summaries, AUROC, AUPRC, Brier, log loss, calibration intercept/slope, fixed-bin reliability, expected calibration error, action rates and decision curves at q=0.05/0.10/0.20. For S0/S1 report 30-minute expired and alive cause-specific hazards and expired cumulative-incidence functions through 2880, including observed-versus-predicted CIF calibration. Use 500 whole-hospital bootstrap replicates for the primary interval and model contrasts; report a uniquepid-cluster bootstrap sensitivity. Refit bootstrap results, if attempted, are separate training uncertainty.

## Falsification and interpretation

The implementation must pass these checks:

1. Permute the outcome within development hospitals before fitting. AUROC should collapse toward 0.5 and net benefit should disappear; persistent signal indicates leakage or split failure.
2. Permute process feature vectors within hospital while preserving clinical features and outcomes. The process-specific incremental gain and crossing concentration should disappear; persistence indicates the process block is proxying another feature or leakage.
3. Fit the process-only diagnostic. It must not be presented as a patient-risk model. If it nearly reproduces B0 discrimination and calibration, report that testing behavior is highly informative but do not call it clinical state.
4. Re-run the primary analysis under revision-conservative, revision-ignored and exact vital-deduplication rules. A materially different crossing or transport result is evidence that result-availability semantics are unresolved.
5. Fit hospital-ID and hospital-metadata diagnostics only as non-deployable checks. Their failure in holdout is not proof that process variables are causal or transportable.
6. Deliberately attempt to add actual* fields, unitdischargestatus, unitdischargeoffset and post-360 rows; the pipeline must reject them before fitting.
7. For S0/S1, repeat fitting from at least five deterministic initializations. Failure of latent-state stability, hazard calibration or held-out transport is an alternative-model failure and makes the mechanistic comparison inconclusive, not a license to select the most favorable run.
8. A positive decision effect must remain when action rates, raw event rates, calibration and component crossing counts are reported. A small AUROC gain without a decision effect is not supportive.

Supportive results mean that process features reproducibly change a fixed escalation decision, the direction and outcome composition of crossings indicate clinically plausible excess action or lost action, and the result survives whole-hospital transport, the ordered alternative and stability checks. This supports a warning about process-sensitive deployment or a need for site adaptation; it does not establish that testing causes mortality, that extra action harms patients, or that a policy should change.

Adverse results mean the process block adds no material decision utility or transports at least as well as the clinical block, with no adverse crossing pattern. The seed hypothesis is weakened. Inconclusive results mean support, identifiability or uncertainty is inadequate; no deployment recommendation follows.

Computationally checkable claims are the frozen source hashes and headers, exact joins, ordinary gzip status, offset filters, duplicate handling, feature ledger, split integrity, target construction, threshold decisions, model fits, predictions, CIFs, bootstrap intervals and permutation results. Clinical adjudication or additional data are required to determine whether lab rows represent orders, clinician intent, test availability, turnaround, assay/specimen comparability, true physiologic missingness, actionable mortality risk, or harm from escalation. The public snapshot lacks treatment indication, action-cost utilities, bedside clinician decisions, reliable order timestamps, raw waveforms, full narrative context, post-discharge outcomes and adjudicated biological death timing. Expert review, prospective evaluation and another database would be required before changing hospital policy.

## Method comparison and compute

The transparent B0/B1 pair is the matched baseline: same cohort, features, preprocessing, splits, thresholds and outcomes, with process variables as the only deliberate difference. It is auditable and directly yields the decision-regret estimand.

The substantive S0/S1 alternative is a CPU-first low-dimensional temporal state-space model with 12 half-hour bins, a fixed three-dimensional latent severity state, value/mask emissions, a separate observation channel and competing expired/alive hazard heads. It can reveal whether process information changes decisions because it tracks temporal observation behavior and exit-state ordering, information discarded by six-statistic logistic summaries. It is not selected because it is complex; it is selected because observation regime versus latent clinical state is the scientific mechanism.

Fit S0/S1 with deterministic initialization, development-fold stopping and regularization. Both alternatives use identical accepted inputs and must report the same decision estimands. Defer S0/S1 if paired observations are too sparse, repeated fits are non-identifiable, or the prespecified convergence/calibration gate fails; then report the transparent result and label the mechanism comparison inconclusive. A generic boosted tree is retained only as a revisit option: it could expose nonlinear interactions but cannot separate observation channel from state. A transformer is deferred because six-hour structured sequences do not require a large representation for this mechanism question. Revisit either only if residual diagnostics show a prespecified clinically interpretable nonlinearity.

Verified compute facts are the configured discovery limit (7200 science seconds), two concurrent jobs, eight available A100-SXM4 80-GB devices and the allowed CPU/GPU images. The future solver plan is CPU-first: 8 CPUs, 32 GB RAM and up to 2 hours for ledger construction, five-fold fits, state-space fits and 500 hospital bootstrap replicates, with checkpoints for ledgers and predictions. Full fitting runtime, memory and state-space convergence are unverified. GPU is not required for B0/B1; an allocated A100 may be considered for S0/S1 only if the separate solver envelope permits it. Discovery did not fit the models.

## References and evidence boundary

The assigned parent [prior hypothesis] was inspected as the primary design predecessor. The expert eICU-02 card was inspected as an untested seed. The eICU dataset README, full catalog, metadata and all five relevant table schemas were inspected. The research-ambition README and methods-and-compute guide were inspected; they support considering a bounded learned/latent adaptation after checking dates, outcomes, splits and calibration, but do not establish this proposal’s result. No unavailable article text or supplementary method is claimed, and no fitted result is claimed.
