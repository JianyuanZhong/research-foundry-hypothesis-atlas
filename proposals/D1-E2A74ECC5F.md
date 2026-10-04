# Can an early ICU laboratory-observation signal support a transportable monitoring decision?

Status: substantive child of `[prior hypothesis]` (episode 16). This is an observational transportability and decision-consequence study, not a causal effect of laboratory testing, a hospital quality ranking, or evidence that an alert improves care.

## Scientific deliverable

At the fixed ICU-relative 360-minute landmark, the solver must newly freeze a first-stay cohort, revision/unit-aware laboratory codebook, early-state and observation-process features, whole-hospital folds, and two prespecified decision thresholds. It must fit paired risk models and produce:

1. a source-bound cohort flow, exact schema/column audit, analyte mapping, missingness and vital-observation ascertainment report, and fold manifest;
2. leakage-safe feature matrices based only on records known by minute 360;
3. out-of-fold zero-shot predictions in held-out hospitals for recorded ICU death by minute 1,800, plus competing alive ICU discharge;
4. calibration, integrated competing-risk Brier scores, macro-hospital uncertainty, and decision-curve/alert-burden summaries at the top 1%, 5% and 10% alert burdens;
5. a support-gated secondary analysis of next-window recorded physiologic instability from `vitalPeriodic`, with discharge/death competing and ascertainment reported;
6. a transparent process decomposition (state plus availability versus state plus availability plus laboratory observation process), a common-panel analysis, and a matched temporal alternative using exactly the same information;
7. conditional within-hospital state-risk-stratified process permutations, site-fingerprint ablations, and an interpretation trace linking each conclusion to computed outputs.

The actual deliverable is a new estimate of whether a patient-linked laboratory observation signal has reproducible, decision-relevant predictive information across hospitals at a fixed alert burden. Completion is established by frozen cohort/codebook/folds, fitted parameters, held-out predictions, uncertainty and decision outputs, falsification outputs, and a conclusion file whose claims are traceable to them. No result is asserted here.

## Supported and unresolved claims

The parent audit supports feasibility: 135,680 eligible adult first stays, 2,470 recorded ICU-death events by 1,800 minutes, 208 hospitals, 175 event-bearing hospitals, 195 hospitals with at least 20 eligible episodes, 2,209,118 revision-aware laboratory rows, and 111,655 episodes with at least one eligible landmark-known laboratory row. These are outcome-blind support counts, not evidence that testing predicts death or benefits patients.

The available evidence supports only that eICU contains dated laboratory records, monitor summaries, patient/hospital joins, and enough recorded-death events for a whole-hospital transport experiment. It does not establish clinician intent, latent physiologic deterioration, an order-to-result process, alert benefit, or external validity.

The unresolved claim is:

> Among adult first ICU stays who are eligible for a decision at minute 360, adding patient-level laboratory observation timing and intensity from [0,360] to measured early state and simple analyte availability will improve calibrated zero-shot identification of patients who die in the ICU by minute 1,800 at a prespecified alert burden in held-out hospitals; any gain that disappears under within-hospital state-risk-stratified process permutation, common-panel restriction, or site-fingerprint adjustment is workflow/measurement information rather than robust patient-level transportable evidence.

The clinically consequential interpretation is whether a new hospital could use the signal to allocate a scarce intensified-monitoring action (for example, review or higher-frequency reassessment) to a fixed top 1%, 5% or 10% of patients. This is a hypothetical decision analysis: eICU has no randomized monitoring policy, alert exposure, staffing cost, clinician response, or patient benefit. A positive net-benefit curve therefore means only that an evaluated risk ranking is calibrated enough to be potentially useful under stated utility weights, not that monitoring would improve outcomes.

## Population and time ordering

Use the first adult ICU stay per `uniquepid` in the frozen eICU snapshot:

- age >=18, treating age >89 as 90;
- positive numeric `unitdischargeoffset`;
- smallest valid numeric `unitvisitnumber`, ties broken by `patientunitstayid`;
- `unitdischargeoffset > 360`, so the decision landmark is observable.

The primary landmark feature window is ICU-relative [0,360] minutes. At minute 360, use only laboratory rows with `labresultoffset` in [0,360] and `labresultrevisedoffset <=360` or null under a prespecified null-revision convention. A result first visible after the landmark, including a late revision, is unavailable to the decision. The primary outcome window is (360,1800] minutes. For causal-order clarity, a stay discharged or recorded dead at or before minute 360 is excluded; death or alive ICU discharge after the landmark is an outcome/competing event, never a predictor.

A separately labeled sensitivity analysis may use [max(`hospitaladmitoffset`,-360),360] to test whether pre-ICU timing changes transport. It must not be pooled with the primary ICU-relative analysis.

## Exact source bindings

Snapshot: `[source checksum]`.

All files below are read-only ordinary gzip files (archive member `ordinary file`) under:

`[internal dataset path]`

- `patient.csv.gz`, table `patient`, catalog file `datasets/eicu/table-ab037c09d7df9a3c.json`, schema [source checksum]. Join key `patientunitstayid`; person key `uniquepid`. Use `age`, `gender`, `ethnicity`, `hospitalid`, `unitvisitnumber`, `unitstaytype`, `admissionweight`, `hospitaladmitoffset`, `hospitaladmitsource`, `unitdischargeoffset` and `unitdischargestatus`. Do not invent `unitadmitoffset`.
- `hospital.csv.gz`, table `hospital`, catalog file `datasets/eicu/table-811df7b2ef435e12.json`, schema [source checksum]. Join `patient.hospitalid = hospital.hospitalid`. Available descriptors are `hospitalid`, `numbedscategory`, `teachingstatus`, `region`; site fields are diagnostic only and excluded from the primary patient model.
- `lab.csv.gz`, table `lab`, catalog file `datasets/eicu/table-79bdb33275339b1a.json`, schema [source checksum]. Join on `patientunitstayid`. Use `labid`, `labresultoffset`, `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`, `labmeasurenameinterface`, and `labresultrevisedoffset`. Retain all rows in an audit, but numeric state/process features require a numeric result and a retained analyte/system/interface mapping. Conflicting units are not silently converted.
- `vitalPeriodic.csv.gz`, table `vitalPeriodic`, catalog file `datasets/eicu/table-a22c6d6981a32279.json`, schema [source checksum]. Join on `patientunitstayid`; use `observationoffset`, `temperature`, `sao2`, `heartrate`, `respiration`, `systemicsystolic`, `systemicdiastolic`, `systemicmean`, `pasystolic`, `padiastolic`, `pamean`, `cvp`, `etco2`, and `icp`. The catalog says these are five-minute medians of generally one-minute monitor averages, not raw waveforms.
- The full catalog and `datasets/eicu/metadata.json` record that longitudinal child tables join to `patientunitstayid` and offsets are minutes relative to ICU admission. Other sources remain available but are not substituted into the primary analysis. Narrative notes are not assumed to be genuine narrative, images are absent, and raw waveforms are unavailable.

The `vitalPeriodic` schema and raw header were inspected specifically for the new outcome. The audit source is not used to define the laboratory exposure.

## Predictors

The common early-state block contains demographics/admission context and development-fold-transformed early physiology and lab values. For each retained analyte, derive first/last valid result, slope and range only when supported by at least two distinct result times, clinically prespecified threshold flags, an availability indicator, distinct measurement times and rows, last-result recency, first-to-last span, inter-test summaries, total distinct analytes, stable audited system/interface strata, and revision-known indicators. The process block contains timing/intensity/interface/revision features; it excludes hospital ID and site aggregates.

The `vitalPeriodic` early state uses robust hourly summaries and trend/threshold flags for the listed vital fields, with explicit per-field availability. It must not use the number of vital rows as a state variable in the primary state-only model; vital observation count is a process/ascertainment diagnostic. Development-fold medians, scaling, mappings, splines and thresholds are frozen without seeing held-out hospitals. No post-360 record, `apachePatientResult` actual-outcome field, or discharge information is a predictor.

## Outcomes and decision interpretation

### Primary outcome

The primary outcome is cumulative incidence of the first `patient.unitdischargestatus` normalized exactly to `Expired` with `unitdischargeoffset` in (360,1800]. Alive ICU discharge before 1,800 is a competing event. A stay still in ICU at 1,800 without recorded death is administratively censored. This is recorded ICU death, not all-hospital mortality, post-ICU mortality, or a causal testing endpoint.

The primary decision output compares B0 and B1 at fixed alert burdens q in {0.01,0.05,0.10}: flag exactly the top q fraction within each held-out hospital using only the model score, and report sensitivity, deaths captured, alerts per 100 eligible patients, macro-hospital variation, calibration, and time-dependent net benefit. Net benefit must be shown for false-positive: true-positive cost ratios corresponding to q (1:99, 1:19, 1:9) and as a sensitivity curve over a wider prespecified range. Because utilities are not observed, label this model-based decision-curve/alert-burden transport, not clinical utility. No threshold may be tuned on the held-out hospital.

A model is decision-relevant only if its improvement over B0 is directionally consistent across hospitals, has a confidence interval that excludes a practically negligible prespecified margin for the primary estimand (or is explicitly inconclusive), and does not trade a small macro-hospital gain for severe calibration or alert-burden failure. The margin and bootstrap procedure must be frozen before fitting; report estimates even when the gate fails.

### Support-gated next-window recorded instability

Audit and, if support passes, analyze an additional fixed early-state outcome. Among landmark-eligible stays, define a recorded instability event as the first row in (360,720] in `vitalPeriodic` with at least one valid value satisfying a prespecified component threshold:

- `systemicmean <=60`, or
- `sao2 <=88`, or
- `heartrate >=130`, or
- `respiration >=30`.

These are clinically interpretable recorded threshold crossings, not adjudicated deterioration. The solver must report per-component and composite support, early-window and next-window observation coverage, observation-time distributions, hospital event counts, and the fraction with death/discharge before a qualifying row. A missing next-window monitor row is not a negative outcome.

The primary analysis for this secondary endpoint is among stays with at least one valid `vitalPeriodic` observation in both [0,360] and (360,720], with the observation-ascertainment restriction reported as part of the estimand. Death and alive ICU discharge before a threshold crossing are competing events; stays discharged or dead before 360 are excluded; the event time is the first qualifying observation. If both windows are not observed in at least 80% of landmark-eligible stays, or fewer than 20 hospitals have >=10 analyzable events and no fewer than 10 events in a held-out fold, this endpoint is descriptive only and the primary decision analysis remains the recorded-death alert-burden analysis. The 80%/20-hospital/10-event rule is a readiness gate, not a claim that missingness is ignorable.

Also report a separate next-window monitoring-presence outcome (any valid `vitalPeriodic` row in (360,720]) as a workflow/ascertainment diagnostic. It must never be called deterioration. If lab-process effects predict presence more strongly than threshold crossing, that supports workflow-fingerprint interpretation.

## Models and same-question comparison

Freeze cohort, codebook, windows, outcomes, folds and transformations before fitting.

- B0, the transparent baseline, is a pooled discrete-time cause-specific elastic-net logistic model with hourly rows from 360 through 1,800 and separate recorded-death and alive-discharge heads. It uses the common early state and simple analyte/vital availability, not laboratory timing/intensity or site ID.
- B1 is the primary transparent process extension: identical rows, outcomes, folds, state and availability as B0, adding only patient-level lab observation timing/intensity, audited interface/revision channels and inter-test features. It is the main test of incremental process information.
- T is the substantive temporal alternative: a one-layer GRU or temporal convolution over six one-hour bins in [0,360], with the same value, availability, lab-process, vital-state, elapsed-time, interface and revision channels supplied to B1. It has death, discharge and next-observation auxiliary heads; the auxiliary head characterizes temporal observation structure and is not a clinical endpoint. It can reveal order, persistence, co-movement and abrupt change that B1's summaries lose. It must be compared to B1 on identical test episodes, horizons, folds and decision burdens, not rewarded for a small AUROC increase.

Use five grouped outer folds holding out approximately 20% of hospitals once. Within each outer training partition, split hospitals approximately 75%/25% for fitting, regularization, early stopping and codebook decisions; keep all stays for a `uniquepid` together. Stratify by hospital eligible/event counts where possible. A patient-random split is a secondary optimism diagnostic, not the primary result. Report macro-hospital and patient-weighted estimates, paired fold differences, calibration-in-the-large/slope, integrated cause-specific and cumulative-incidence Brier scores, and hospital-then-patient bootstrap uncertainty.

## Falsification and confounding checks

1. Permute each patient-level process vector within hospital and B0-risk decile (and separately within early-state risk strata), preserving marginal workflow intensity but breaking patient linkage. A genuine patient-linked process contribution should collapse toward B0; persistence indicates leakage, residual site structure or workflow fingerprint.
2. Refit on a common analyte/system/interface panel selected without outcomes. A gain that disappears is not robust across laboratory interfaces.
3. Remove interface/revision channels, then remove all process channels except counts/recency. This identifies whether signal is documentation/interface artifact.
4. Add hospital descriptors only in a diagnostic site-fingerprint model. Site features may predict transport but cannot establish patient-level evidence.
5. Evaluate the next-window monitoring-presence outcome and vital observation coverage. Concordance with presence rather than threshold crossings is adverse for a physiologic interpretation.
6. Use a negative-control timing feature based on a post-360 record only in a deliberately separate leakage test; any signal there is a pipeline failure, not evidence.
7. Repeat with death/discharge competing-risk labels, no competing-event shortcut, and the fixed pre-ICU sensitivity window. Do not interpret a change as causal.
8. Check leave-one-hospital and analyte-family influence, fold event support, and calibration drift. No external validation or causal policy identification is possible from this snapshot.

## Evidence gates

Supportive evidence requires: B1 improves the prespecified macro-hospital integrated Brier and calibrated net benefit over B0 at a fixed burden with uncertainty and direction reasonably consistent across held-out hospitals; the process-permutation null removes the increment; the common-panel and interface/revision ablations do not erase it; and, if the instability endpoint passes its support gate, the signal predicts recorded threshold crossing beyond early state without being explained by monitoring presence.

Adverse evidence is: no calibrated/transportable increment, a gain only in patient-weighted metrics or one site, persistence after linkage-breaking permutation, dependence on site/interface fields, stronger prediction of monitoring presence than threshold crossing, severe fold calibration drift, or a next-window endpoint failing ascertainment support. These outcomes would favor state/availability features, site-specific recalibration, or not using laboratory observation process for monitoring allocation.

Inconclusive evidence includes wide intervals, sparse held-out events, unstable analyte mapping, inadequate next-window vital ascertainment, or a small Brier change without stable decision-curve improvement. Inconclusive is not confirmation or refutation.

Even supportive results establish only observational predictive transport and a hypothetical ranking under assumed utilities. Clinical adjudication would be needed to establish true physiologic deterioration; order data, clinician intent, staffing costs, interventions, response, harms and patient-centered outcomes would be needed to establish monitoring benefit; prospective silent deployment and external validation would be needed before operational use.

## Alternatives, compute and deferrals

The measured discovery compute is the bounded CPU source audit of `patient.csv.gz` and `vitalPeriodic.csv.gz`; it did not fit a clinical model and its output is support evidence only. The configured discovery budget is 7,200 science seconds with at most two concurrent jobs. The future solver planning envelope is 16 CPUs, 262,144 MiB, up to 8 allocated GPUs, and 28,800 seconds; this is planning capacity, not an executed solver authorization.

B0/B1 are CPU-first: grouped elastic-net models and bootstrap summaries should fit within the solver envelope, but exact runtime is unverified until implementation. T is a bounded one-layer temporal model on six bins, with early stopping and no hyperparameter sweep beyond the inner hospital validation split; one allocated A100 is an option if measured CPU runtime or repeated bootstrap makes it necessary. The deployment has A100-SXM4-80GB devices, but ordinary-shell CUDA absence is not evidence and no GPU fitting was performed here. GPU use has no scientific priority.

A joint mechanistic observation-intensity model is retained as a deferred alternative: it would jointly model laboratory observation events and death conditional on the same early state, testing whether an informative-observation mechanism explains the increment. It is not made primary because the data have results rather than complete orders, clinician intent, staffing and intervention histories, so its mechanism would be weakly identified. Revisit it if order timestamps and validated observation-policy labels become available. A Delphi-like generative sequence reproduction is also deferred: dated structured inputs exist, but the original full cohort/training and external validation are unavailable; T is an explicitly different bounded adaptation, not a reproduction. An ALADYNOULLI-style latent longitudinal model is deferred because the short ICU window and absent genetic inputs do not answer a distinct clinical decision question.

No neural method is excluded categorically; T is selected conditionally because it tests a substantive information-loss question. If support, convergence, calibration or solver time fails, report that and retain B0/B1 as the complete transparent study rather than silently changing the question.
