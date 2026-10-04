> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Does laboratory observation process add transportable information after adequate ICU state adjustment?

Status: episode-14 substantive child of [prior hypothesis]. This is an observational prognostic and measurement-process study, not a causal test-ordering study, a hospital quality ranking, or evidence of clinical benefit.

## Scientific deliverable

The future solver must newly freeze a leakage-safe eICU first-stay cohort, revision/unit codebook, time-matched laboratory and vital-state feature matrices, generic monitoring-process controls, five grouped whole-hospital folds, and competing-risk predictions. It must estimate whether patient-level laboratory observation timing and intensity add transportable information after a richer physiologic-state baseline.

Completion requires:

1. a cohort flow, source/schema/column audit, unit/interface/revision codebook, vital-summary convention, and fold manifest;
2. three nested feature blocks fit without post-landmark leakage: lab state/availability, lab-plus-vital state, and lab-plus-vital state plus laboratory process;
3. out-of-fold cumulative-incidence predictions for recorded ICU death and alive ICU discharge on held-out hospitals;
4. paired macro-hospital and patient-weighted integrated competing-risk Brier scores, calibration-in-the-large/slope, hospital-then-patient uncertainty, and fixed-alert-burden descriptions;
5. conditional process permutations, site-fingerprint and generic-monitoring falsifications, strict-codebook sensitivity, and an output-linked interpretation trace;
6. a predeclared compact temporal learner only if support, positivity, leakage checks, convergence and calibration pass; and
7. a clear supportive, adverse or inconclusive conclusion tied to computed output files.

The scientific output is an estimate of incremental, transportable predictive information and its failure modes. It is not a clinical decision rule.

## Strongest supported claim and unresolved claim

The parent-line outcome-blind audit found 135,680 eligible adult first-stay episodes at a six-hour landmark, 2,470 recorded ICU-death events in the next 24 hours, 208 hospitals, 175 event-bearing hospitals, 195 hospitals with at least 20 eligible episodes, 2,209,118 revision-aware laboratory rows, and 111,655 episodes with at least one landmark-known laboratory row. Those counts support a bounded whole-hospital experiment; they do not show that laboratory testing history predicts death, improves transport, reflects clinician intent, or represents a modifiable safety signal.

A bounded fresh patient scan in this episode found 130,350 stays under a simpler age/visit parser and 2,252 Expired records in (360,1800]; this is a diagnostic discrepancy, not a replacement for the frozen cohort. The solver must reconcile age greater-than-89 normalization, missing or invalid visit numbers, first-stay tie rules, and all inclusion filters before any model fitting.

The eICU-02 expert seed and the parent establish a plausible unresolved measurement question: models may exploit hospital-specific testing practice, but a patient's observation history might also contain information about clinical instability not captured by a narrow state block. The substantive unresolved claim is:

> Among adult first ICU stays with a fixed ICU-relative [0,360]-minute landmark, laboratory observation timing and intensity improve zero-shot prediction of recorded ICU death by 1,800 minutes beyond time-matched measured laboratory and vital state, explicit analyte availability, and generic monitoring intensity in genuinely held-out hospitals; any improvement should attenuate under within-hospital, state-risk- and availability-stratified process permutation, while a gain confined to site descriptors, interfaces, or patient-random splits is a workflow fingerprint rather than transportable patient information.

This is clinically consequential because a deployed risk model or monitoring policy can fail when testing practice changes between hospitals. The result could inform whether a deployment should retain laboratory-process features with explicit shift monitoring, prefer a state/availability model with recalibration, or avoid treating testing-based accuracy as robust. It cannot justify ordering or withholding tests.

The advance over the prior parent is identification, not a new model for its own sake: the primary comparison adds time-matched vital physiology and generic monitoring-process controls. If the laboratory-process increment disappears after those controls, the result prevents a misleading claim that lab workflow contains independent patient signal. If it persists across hospitals and falsifications, the study provides stronger evidence that the signal is patient-level and transportable, while still not establishing causality.

## Population, time boundaries and outcome

Use the first adult ICU stay per person from snapshot [source checksum]:

- age at least 18, with eICU age values greater than 89 normalized to 90;
- numeric positive unitdischargeoffset;
- smallest valid unitvisitnumber per uniquepid, ties broken by patientunitstayid;
- unitdischargeoffset greater than 360, so the primary landmark is observed.

The primary predictor window is ICU-relative minutes [0,360]. A secondary, separately labeled sensitivity includes max(hospitaladmitoffset,-360) through 360; it must not be pooled with the primary window. No result or revision after minute 360 may enter a predictor.

A primary laboratory result is landmark-known only if labresultoffset is in [0,360], labresultrevisedoffset is at most 360 or null under a prespecified null-revision convention, the numeric value parses, and its unit/system/interface mapping passes the frozen audit. Conflicting or unresolved units are excluded from numeric state features but retained in the audit.

The primary outcome is the first patient.unitdischargestatus normalized exactly to Expired with unitdischargeoffset in (360,1800]. Alive ICU discharge before 1,800 is a competing event. A stay remaining in the ICU without either event is administratively censored at 1,800. Report cause-specific hourly models only with the same competing-risk definition. This is recorded ICU death, not all-hospital mortality, post-ICU mortality, latent death, or a causal testing outcome.

## Exact source bindings

All sources are ordinary gzip files whose archive member is ordinary file, read-only, under:

[internal dataset path] 2.0 data/

The catalog and full schema references are datasets/eicu/README.md and datasets/eicu/metadata.json.

- patient.csv.gz, table patient, schema datasets/eicu/table-ab037c09d7df9a3c.json, [source checksum]. Join key patientunitstayid; person key uniquepid. Use age, unitvisitnumber, hospitalid, hospitaladmitoffset, unitdischargeoffset, unitdischargestatus, gender, ethnicity, unitstaytype, hospitaladmitsource, and admissionweight. There is no invented unitadmitoffset.
- hospital.csv.gz, table hospital, schema datasets/eicu/table-811df7b2ef435e12.json, [source checksum]. Join patient.hospitalid=hospital.hospitalid. Available descriptors are hospitalid, numbedscategory, teachingstatus, and region; site features are diagnostic only and no hospitalid enters the primary patient model.
- lab.csv.gz, table lab, schema datasets/eicu/table-79bdb33275339b1a.json, [source checksum]. Join patientunitstayid. Use labid, labresultoffset, labname, labresult, labresulttext, labmeasurenamesystem, labmeasurenameinterface, and labresultrevisedoffset. Retained analytes are outcome-blind and codebook-defined; conflicting units are never silently converted.
- vitalPeriodic.csv.gz, table vitalPeriodic, schema datasets/eicu/table-a22c6d6981a32279.json, [source checksum]. Join patientunitstayid; use observationoffset and available temperature, sao2, heartrate, respiration, systemicmean, pamean and other prespecified monitor summaries in [0,360]. eICU metadata identifies these as five-minute summaries, not raw waveforms.
- vitalAperiodic.csv.gz, table vitalAperiodic, schema datasets/eicu/table-72ace5b89971196b.json, [source checksum]. Join patientunitstayid; use observationoffset, noninvasivesystolic, noninvasivediastolic, noninvasivemean, and other available hemodynamic fields in [0,360].
- apacheApsVar.csv.gz, table apacheApsVar, schema datasets/eicu/table-67711a86e012835e.json, is available for a sensitivity/audit only because it has no per-variable timestamps; it cannot silently become a landmark predictor.
- apachePatientResult.csv.gz, table apachePatientResult, schema datasets/eicu/table-754bebf64d3d9909.json, is excluded from predictors because it contains actual outcome fields.
- carePlanEOL.csv.gz, table carePlanEOL, schema datasets/eicu/table-4a60395475cf75e7.json, may support a prespecified end-of-life timing sensitivity via cpleolsaveoffset, cpleoldiscussionoffset, and activeupondischarge; it does not adjudicate goals of care or latent death.

## Variables, models and estimands

For retained lab analytes, derive from [0,360] first/last values, slope and range when supported, threshold flags, any-value availability, distinct measurement times, row counts, time from first/last result to landmark, inter-test intervals, analyte count, stable system/interface strata and revision-known indicators. For retained vital fields, derive the same state summaries and explicit availability plus vital measurement counts/recency. Every transform, imputation, scale, unit map and categorical map is fitted in development hospitals only.

Define three nested blocks on identical episodes and folds:

- B0a: demographics/admission context, landmark-known laboratory value summaries and explicit laboratory availability;
- B0b, the primary adequacy baseline: B0a plus time-matched vital state summaries and vital availability;
- B1: B0b plus laboratory observation timing, intensity, revision and interface/process features, while reporting a balanced vital-process control block.

B0a, B0b and B1 are pooled elastic-net discrete-time cause-specific logistic models with hourly rows from minute 360 through 1,800 and separate recorded-death/alive-discharge heads. Regularization is selected only in development hospitals. The primary estimand is the paired outer-test difference in macro-hospital integrated competing-risk Brier score and calibration between B1 and B0b. B1-B0a and B0b-B0a decompose the apparent gain; patient-weighted results are secondary. Fixed-alert-burden summaries are descriptive and do not establish clinical utility.

The substantive learned alternative is a compact one-layer GRU or temporal convolution over six one-hour bins in [0,360], using the same lab/vital value, availability, count, recency, interface and revision channels. It has competing heads for recorded death and alive discharge. It can reveal order, persistence, abrupt co-movement and time-varying observation behavior that B1 summaries lose. It is deferred if event support, common feature support, leakage checks, convergence or calibration fail; it is not selected for neural complexity or GPU use. An auxiliary next-bin observation head is descriptive of the observation process, not a clinical endpoint.

Use five grouped outer folds holding out approximately 20% of hospitals once. Within each outer training partition, split hospitals into development/validation subsets for codebook choices, regularization and early stopping; keep all stays of a uniquepid together. Stratify hospital folds by eligible and event counts where feasible. A patient-random split is an optimism diagnostic, never the primary transport result.

## Falsification and interpretation

Before any inferential comparison, require prespecified minimum event and cell support, at least 10 hospitals with event/non-event support, no near-zero observation probabilities after trimming, acceptable effective sample size for any weighted sensitivity, and stable directions under strict versus broad unit/interface and revision rules. If these fail, report counts and descriptive uncertainty only and label the study inconclusive.

Run:

- within-hospital process-vector permutation conditional on B0b risk strata, analyte availability and hospital, preserving marginal process distributions;
- site-only models using hospital descriptors as a workflow-fingerprint diagnostic, never as the primary patient model;
- common-analyte/common-interface panels and strict unit/revision definitions;
- vital-process-only and lab-process-only swaps to test generic monitoring intensity;
- pre-landmark/placebo timing checks where supported;
- patient-random versus whole-hospital split comparison;
- optional end-of-life timing sensitivity, never relabeled as causal adjustment;
- interface/revision strata and complete-observable episode sensitivity.

Supportive evidence requires the gates to pass, B1 to improve macro-hospital calibration/Brier performance over B0b with uncertainty and stable direction across strict codebooks, no single-hospital dominance, and the process permutation/site-only diagnostics to remove or materially attenuate the increment. Concordant learned-model behavior is supportive only when it adds ordering/persistence information beyond the transparent feature summaries and remains calibrated on held-out hospitals. This supports prospective monitoring and transport research, not changed test-ordering.

Adverse evidence is a held-out-hospital null/reversal, disappearance after vital-state or generic-monitoring adjustment, dependence on a single interface/site, persistence under the conditional process permutation, or similar gain from site-only features. That would refute the proposed patient-level transport claim in this snapshot, not prove that testing is clinically unimportant.

Inconclusive evidence is sparse or non-positive support, unresolved revision/time leakage, unstable weights, competing-event miscalibration, fold support failure, or temporal nonconvergence. It must not be converted into hypothesis confirmation.

## Evidence limits and alternatives not chosen

The parent’s eICU-02 testing-practice direction is adapted, not reproduced. The eICU-01 vasopressor, eICU-03 hypotension, eICU-04 hyperoxia, eICU-05 ventilatory burden, eICU-06 nighttime discharge, eICU-07 transfer, eICU-08 reduced-testing, eICU-09 insulin/hypoglycemia, and eICU-10 recovery-speed seeds remain unselected this episode. The insulin/nutrition branch was deferred after its outcome-blind conservative joint cell had only three episodes and zero detected lows; documentation cannot be silently treated as feeding cessation.

The natural-history/Delphi demonstration motivates the bounded temporal comparison on dated structured eICU histories, but its UKB training and Danish validation are unavailable. The Bayesian longitudinal/genetic demonstration is not reproduced because genetic inputs and adjudicated physiology are unavailable; an EHR-only latent model is deferred because it would change the scientific assumptions and adds no necessary information before the baseline adequacy test. The cancer/Oncoformer demonstration is not reproduced: only its supplement was available, the main article and complete STAR Methods were not inspected, and eICU contains no chest-X-ray modality. All four configured dataset sources remain directly accessible read-only; this eICU proposal uses only the named eICU sources, and all derived analyses belong in the workspace.

## Compute and clinical boundary

Discovery used no GPU. The shared hardware instructions state that ordinary shells have no CUDA allocation; GPU availability must be tested only through an allocated job using cuda:0. The numeric future solver planning envelope is 16 CPUs, 262,144 MiB, up to 8 GPUs and 28,800 seconds, planning only. CPU is appropriate for the nested tabular fits; one allocated A100 is an optional bounded resource for the compact temporal fit, with CPU fallback. Exact learner convergence and memory/time are unverified.

The eICU data lack test-order intent, delivered calories, symptoms, raw waveforms, genuine narrative text, bedside glucose confirmation, chart-adjudicated AKI or death mechanism, external hospital validation and prospective alert response. Administration, causal effects, latent mortality, clinical benefit and deployment utility therefore require chart adjudication, expert review, external validation or a prospective/emulated-intervention study. Harbor can verify computation, source bindings, leakage control, support, uncertainty, calibration, transport and whether conclusions follow from outputs; it cannot establish those clinical claims.
