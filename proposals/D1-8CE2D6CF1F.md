> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Frozen-calendar transport of assay payload versus the local observation process in HCC

## Scientific deliverable

The future solver must newly construct and freeze an adult, first-observed HCC-coded admission cohort; fit nested Q/M/P models and a matched time-aware multistate alternative using only the 2012–2018 development era; generate primary predictions without any later-era refitting; and report locked 2021–2025 proper-score contrasts, calibration, era interaction, the return-versus-observation decomposition, and all data-quality and falsification ledgers. It must additionally fit a separately labelled 2019–2020 bridge recalibration sensitivity and compare it with the strictly frozen result. Completion is the artifact set and an evidence-bounded interpretation, regardless of whether the hypothesis is supported. No model was fit and no clinical result is claimed in discovery.

## Question, evidence, and hypothesis

The unresolved clinical-research question is whether the content of previously measured laboratory assays contains information about a near-term local return beyond two different reasons a result may be present in an EHR: how intensely the patient was observed/captured (Q) and which assays were selected and sampled (M). The transport question is whether that information increment survives calendar change in panels, laboratory workflows, referral patterns and documentation.

Among adults with a first locally recorded HCC-keyed inpatient encounter, does strictly prior, assay-specific laboratory result content (P) improve calibrated prediction of a subsequent locally recorded return beyond strict capture/process history (Q) and assay menu/sampling history (M), and does that P-minus-M increment remain stable when a complete model frozen on 2012–2018 is evaluated directly in 2021–2025? A second, jointly interpreted question is whether any P increment is return-specific or is equally explained by a later local documentation/observation process.

Primary hypothesis: in the locked 2021–2025 era, the strictly frozen P-minus-M model improves held-out prediction of the 30-day locally recorded return state, with a direction and magnitude compatible with its 2012–2018 held-out estimate. The process-specific hypothesis is that P-minus-M is larger for the return state than for later observation among people without a 30-day return. The 2019–2020 bridge recalibration is a secondary deployment sensitivity: it tests whether local recalibration can restore performance, not whether the earlier model transported unchanged. These are calibrated information hypotheses, not causal, biologic or utility claims.

This is falsifiable. Frozen P-minus-M is adverse if null/harmful in the later era, reverses beyond the prespecified interaction bound, or is reproduced by a process-only comparator. The return-specific claim is falsified if the increment is confined to later observation, if assay-identity permutation preserves it, or if the later observation model explains it as well as the return model. A result is inconclusive when event/assay support, timestamp validity or follow-up is inadequate. If only bridge-recalibrated predictions are favorable while frozen predictions fail, the finding supports local recalibration need, not calendar transport.

What is currently supported is only data feasibility and provenance: the frozen HCC snapshot contains the listed structured fields and native times, and prior bounded audits found sparse genuinely prior history and substantial procedure/time irregularity. No local model result supports the hypothesis. A positive frozen result would advance knowledge by separating an assay-payload signal from a changing observation regime and by testing whether it survives an actual calendar shift without recalibration. It could justify prospective silent validation of a follow-up score; it cannot authorize clinical deployment. A bridge-only improvement would inform recalibration planning but would not establish portability. Neither result establishes active HCC, stage, liver reserve, recurrence, treatment selection, benefit or safety.

## Population and temporal estimand

Use HCC snapshot `[source checksum]`, catalog [source checksum], and the ordinary read-only CSV paths bound below. Normalize Unicode/whitespace in the two join keys for audit while retaining raw values and reporting unmatched and multiplicity counts.

1. Join diagnoses to encounters on the exact two-key pair (`patient master index`, `encounter number`). A record is HCC-keyed when normalized `diagnosis name` contains `hepatocellular carcinoma` or case-insensitive “hepatocellular carcinoma”. Report matched strings and `diagnosis type`; diagnoses has no native time and is cohort selection only.
2. Include age >=18, parseable nonnegative native `Admission Time` and `Discharge Time`, and anchor admission in [2012-01-01, 2026-01-01). Retain the earliest eligible HCC-keyed encounter per normalized patient ordered by `Admission Time`, then `Visit Number`. Do not silently replace an invalid earliest record with a later one. Set t0 to `Admission Time` and td to `Discharge Time`; require td+90 days < 2026-01-01.
3. Define the exhaustive post-discharge observed-transition label Y90:
   - R30: the earliest other same-patient encounter with parseable `admission time` in [td, td+30 days), requiring admission >=td;
   - O90: no R30 and at least one other same-patient encounter beginning in [td+30 days, td+90 days);
   - U90: neither R30 nor O90 is observed locally.

Equal-time encounter ties and all candidate keys are audited. U90 means “no qualifying local row,” not no outside care, survival, cure or complete follow-up.

The primary clinical estimand is the paired held-out P-minus-M contrast for the R30 probability under the three-state Y90 distribution, evaluated first with the completely frozen 2012–2018 model in 2021–2025. The observation-process estimand is the paired P-minus-M contrast for O90 versus U90 among Y90 != R30, plus the difference between the R30 and O90 contrasts. L=60 and L=180 versions are sensitivity analyses only when administrative follow-up permits them.

Calendar transport is prespecified and separated into two estimands:

- Primary strict transport: fit every model component on anchors in 2012–2018 only, including rare-assay vocabulary, transformations, numeric parsing/impossible-value rules, standardization, regularization choice, coefficients and calibration; lock the resulting scoring function; score 2021–2025 once without refitting or recalibrating it.
- Secondary bridge recalibration: keep the 2012–2018 feature map and coefficients fixed, fit only a prespecified intercept/temperature or multinomial calibration map on 2019–2020, and apply that map to 2021–2025. It is not allowed to alter features, model family, coefficients or the primary result.

The 2019–2020 bridge is therefore quarantine data for the secondary sensitivity, not feature selection, vocabulary expansion, threshold selection, primary calibration, model locking or informal inspection. Calibration of the primary frozen model must use fit-only resampling/internal validation within 2012–2018. Report 2012–2018 held-out, strict-frozen 2021–2025, and bridge-recalibrated 2021–2025 estimates with the later-minus-earlier interaction. If an era has inadequate R30, O90 or assay support, its contrast is inconclusive and is not rescued by pooling, recalibration, or moving boundaries. A patient-level random split (patient hash modulo 100: 0–59 fit, 60–69 selection/calibration, 70–79 locked evaluation, 80–99 inaccessible) is a secondary precision analysis, not a substitute for the calendar test. Split before row expansion; no patient, linked history row or future row crosses a partition.

## Information sets and observation-process controls

All information sets stop strictly before t0. Primary prior-history rows must be linked by the two-key pair to a non-anchor encounter with parseable native admission and discharge, linked discharge < t0, and linked admission < t0. Their source-native event/availability time must be parseable and in [t0-730 days,t0): labs use `Test time`; procedures `Start time`; orders `Order placement time`; medications `Start time`; examinations `Start time`. Anchor-linked rows are excluded from the primary history even if their event timestamp precedes admission. Publish invalid/missing-time, missing-linked-discharge, overlap, anchor-linked, post-t0, duplicate, unmatched-join and row-inflation counts. This is an availability attribution rule, not proof that a clinician saw a result at that time.

Exclude direct identifiers such as `name`, `ID card number`, `mobile phone number`, `medical insurance/visit card number` and `inpatient number`.

- Q (strict capture/process): age, sex, department, admission calendar era and time-of-day; count/duration/recency of prior completed encounters; source-specific prior row counts and distinct linked-encounter counts for labs, procedures, orders, medications and examinations; number of source types; invalid/excluded-time counts; left-truncation and no-history flags. Q contains no assay identity, assay result or procedure/order content.
- M (assay menu/sampling): prior laboratory `test` identity, assay-specific counts and distinct encounters, recency/span, sampling-time count, `specimen type` availability/missingness and result-missingness indicators. Rare assay handling and vocabulary are fit-only in 2012–2018 and frozen before any later scoring.
- P (assay payload): assay-specific `qualitative result`, valid assay-specific `quantitative result`, `specimen type`, and within-assay change/slope only when at least two distinct valid `test time` values exist. Numeric parsing and impossible-value rules are frozen from 2012–2018 before all locked predictions. Values are never pooled across assays because the catalog says there is no separate lab-unit column; missing results remain explicit missingness features.

The mandatory measurement-process negative control is not a claim that future observations are clinically irrelevant. Among R30 nonreturns, define O90 from future encounters and additionally report future documentation intensity in [td+30,td+90): encounter count and, separately, timestamp-valid row counts for labs, procedures, orders, medications and examinations. These are held-out observation-process outcomes, never predictors. If P-minus-M is strong for O90/intensity but not R30, the most defensible explanation is documentation/monitoring selection rather than a return-specific assay payload. A process-only Q-to-M model and an assay-identity-permuted P model are mandatory controls.

## Matched models and what the alternative reveals

Both methods use exactly the same cohort, Q/M/P raw rows, pre-t0 windows, calendar/random partitions and locked cases. Neither receives documents, pathology, images, vitals or transfers. They differ only in representation/likelihood, not in available information.

Transparent baseline B: fit regularized logistic B_Q, B_M and B_P for R30 versus non-R30, and multinomial regularized logistic models for Y90; fit-only standardization, rare-category handling, penalty and calibration are shared. For the observation analysis, fit the same nested models to O90 versus U90 within non-R30 and to future documentation counts using a prespecified count/link model. B provides an auditable nested information contrast but loses the ordering and competing nature of return versus later observation.

Substantive alternative H: fit matched discrete-time complementary-log-log competing-transition models with coherent hazards for R30 in [0,7), [7,14), [14,30), then O90 in [30,60), [60,90) conditional on no R30, using the same Q/M/P feature vectors, patients and outcomes. With interval offsets and prespecified regularization, derive coherent probabilities for R30, O90 and U90 and a companion observation-intensity likelihood. H exposes whether a calendar shift changes the return hazard, the later observation hazard, or both, and prevents independently fitted probabilities from violating the Y90 state structure. It also reveals whether assay payload modifies early return timing while M/Q only alter observation intensity—information the pooled baseline loses. H is selected for this scientific information, not because it is more complex or expected to score better.

A learned irregular sequence encoder is deferred, not prohibited. It would consume the same eligible pre-t0 assay event sequence with times, assay identity, result/missingness and specimen type and would be scientifically useful only if the locked P-minus-M signal is stable and residual nonlinear/order information is demonstrated after H. A small neural model now would add optimization and calibration variance without resolving the primary endpoint/process/transport ambiguity. Revisit it if support thresholds pass, H residuals show reproducible sequence nonlinearity, and CPU fitting is insufficient for the required repeated fits; one allocated A100 using `cuda:0` is then a possible planning option. Do not interpret deferral as evidence against neural methods.

## Estimation, uncertainty and decision interpretation

Primary scores are paired held-out multiclass log loss and multiclass Brier score for Y90, with binary R30 and conditional O90 decompositions. Lower is better. Report calibration intercept/slope and reliability by state, prevalence, era and model, plus B_P-minus-B_M, H_P-minus-H_M, B_M-minus-B_Q, H_M-minus-H_Q, and strict later-minus-earlier and bridge-versus-strict contrasts. Do not call P-minus-Q assay payload; retain it only as a continuity contrast.

Use at least 1,000 patient-clustered paired bootstrap resamples, preserving every row, transition and linked history for a patient. For strict transport, resample locked 2021–2025 patients without refitting the frozen model; for the earlier comparison, resample the 2012–2018 held-out patients; for bridge recalibration, repeat the complete bridge-fit/calibration application inside each bootstrap replicate or report a clearly labelled fixed-bridge approximation. Report 95% intervals and a prespecified clinically negligible-score-difference margin chosen before locked evaluation; do not replace uncertainty with a p-value. Apply minimum support gates for each era, state and interval, and publish denominators and missingness. Optional threshold/net-benefit plots at 5%, 10% and 20% are descriptive only and cannot establish utility.

Decision interpretation is gated. Favorable strict frozen performance with compatible era contrast and adequate calibration can justify only a prospective silent validation plan. Favorable bridge-recalibrated performance when strict performance fails means the score requires local recalibration; it is not evidence of unchanged transport. Failure of both is adverse for the tested transport hypothesis. Wide intervals, sparse states, dominant U90, severe measurement invalidity or unresolved reconciliation are inconclusive. None supports treatment selection, surveillance efficacy, patient counseling, causal effects or deployment without added clinical adjudication, external validation and prospective utility assessment.

Planning envelope: up to 16 CPUs, 262144 MiB RAM, 8 GPUs and 28800 seconds. CPU-first is a planning estimate, not a measurement; sparse regularized B and H should plausibly fit, but actual feature materialization, memory and bootstrap runtime remain unverified. GPU is not required by this design. Discovery used no full solver fit, GPU training or paid model training.

## Falsification and audit criteria

Mandatory falsifications are:

1. permute payload values within assay and calendar era while preserving identity, times, counts and missingness;
2. permute assay identities while preserving values, times and row counts;
3. shuffle complete prior histories within the patient split while preserving Q;
4. shuffle within-patient laboratory times while preserving values and assay identities;
5. permute calendar-era labels for the interaction test;
6. rerun Q/M process-only models and compare their observation/intensity contrasts;
7. verify no post-t0, anchor-linked, current-anchor, future-window or split-leaked feature;
8. reconcile all-state and observation-stratum scores, coherent H probabilities, duplicate/multiplicity joins and the inherited prior-history count discrepancy before interpretation;
9. verify that no 2019–2020 row, statistic, vocabulary item, calibration parameter or analyst choice enters the strict-frozen scoring function.

Supportive evidence requires a favorable strict-frozen later-era P-minus-M for R30 with calibrated predictions and an interval excluding clinically negligible harm; stable or prespecified-compatible strict later-minus-earlier interaction; attenuation under payload permutation; no comparable Q/M-only explanation; H and B directionally concordant; and, ideally, a larger R30 than O90 payload contrast with adequate support. A supportive result means incremental information in locally recorded prior assay payload under the tested local calendar shift. Bridge recalibration may improve absolute calibration, but cannot upgrade an unsupported strict transport result.

Adverse evidence includes null/harmful strict later-era P-minus-M, clinically important sign reversal, process-only reproduction, persistence after payload permutation, assay-identity permutation survival, a signal confined to O90/documentation intensity, or strict failure masked by bridge recalibration. A negative result does not show that assays lack biology; it shows that this observed local payload is not a stable return signal under the tested regime.

Inconclusive evidence includes sparse later-era events/assays, dominant U90, wide interaction intervals, high invalid-time or missing-result burden, unstable assay vocabulary/parser, inadequate follow-up, unresolved join/count reconciliation, boundary sensitivity, or inability to reproduce the strict lock ledger. A solver must report adverse and inconclusive states rather than select the hypothesis-confirming interpretation.

## Exact HCC source bindings

All longitudinal joins use normalized (`Patient Master Index`, `Encounter Number`) with multiplicity and unmatched audits. All are ordinary files; no archive member is used.

| table / schema record | exact read-only source path | required columns | native time and role |
|---|---|---|---|
| encounters / `datasets/hcc/table-b743286cb1249287.json` | `[internal dataset path]` | `Patient master index`, `Encounter number`, `Age`, `Sex`, `Encounter time`, `Admission time`, `Discharge time`, `Encounter department` | `Admission time`, `Discharge time`; anchor, history, endpoint |
| diagnoses / `datasets/hcc/table-12710723c3df0c99.json` | `[internal dataset path]` | `Patient master index`, `Encounter number`, `Diagnosis name`, `Diagnosis type` | no native time; cohort selection only |
| labs / `datasets/hcc/table-38aad8c54471332f.json` | `[internal dataset path]` | `Patient Master Index`, `Encounter Number`, `Test`, `Qualitative Result`, `Quantitative Result`, `Specimen Type`, `Test Time` | `Test Time`; M/P history and future process count |
| procedures / `datasets/hcc/table-d5eae16f8f8093d9.json` | `[internal dataset path]` | `Patient master index`, `Visit number`, `Surgery`, `Start time`, `End time`, `Surgery source` | `Start time`; Q history and future process count |
| orders / `datasets/hcc/table-6b93dcf0ea823702.json` | `[internal dataset path]` | `patient master index`, `visit number`, `non-drug orders`, `order time`, `start time`, `end time`, `order duration`, `order status`, `frequency` | primary `order time`; Q history and future process count; no treatment-intent interpretation |
| medications / `datasets/hcc/table-4f6ecaeb6e8f69c2.json` | `[internal dataset path]` | `patient master index`, `visit number`, `medication`, `single-dose medication amount`, `single-dose medication amount unit`, `frequency`, `start time`, `end time`, `route of administration`, `drug type` | `start time`; Q history and future process count only |
| examinations / `datasets/hcc/table-fd016d2731b9d6c6.json` | `[internal dataset path]` | `Patient master index`, `Encounter number`, `Examination`, `Examination findings`, `Examination diagnosis`, `Start time`, `Machine model`, `Examination number` | `Start time`; Q history and future process count; text not primary payload |
| vitals / `datasets/hcc/table-8436de9cba74b8ca.json` | `[internal dataset path]` | `patient master index`, `encounter number` | no usable fields beyond identifiers; audit only |
| transfers / `datasets/hcc/table-320c20f732e71789.json` | `[internal dataset path]` | `Patient master index`, `Encounter number` | identifier-only; cannot establish outside transfer/death |
| clinical_documents / `datasets/hcc/table-66afca58512c2fca.json` | `[internal dataset path]` | identifiers and narrative fields including `Chief Complaint`, `History of Present Illness`, `Past Medical History`, `Admission Status`, `Treatment Course`, `Discharge Status`, `Operative Course` | no native time; excluded from primary timed inputs |
| pathology / `datasets/hcc/table-0a4ee86a446c605c.json` | `[internal dataset path]` | `Patient Master Index`, `Encounter Number`, `Pathology`, `Examination Findings`, `Examination Diagnosis`, `Machine Model` | no native time; excluded from primary timed inputs |
| front_page / `datasets/hcc/table-38b3224239acc33f.json` | `[internal dataset path]` | `patient master index`, `encounter number` | identifier-only; audit only |

The HCC metadata records no separate laboratory unit column; height/weight units are unverified. The local text-extraction detector is explicitly unsupported for comprehensive diagnosis extraction and other concepts. No HCC images or waveforms are available.

## Evidence limits and revisit criteria

The three demonstration packages were used as method context only. The natural-history package supports the idea of dated structured-history adaptation, but its external Danish cohort is unavailable; the Bayesian package supports an irregular latent-trajectory adaptation, but the original genetic inputs are unavailable; and the cancer package has an available supplement but the main paper/full STAR Methods and images are unavailable. None establishes this HCC hypothesis or supplies an HCC clinical gold standard.

This study cannot identify active HCC versus historical/coded HCC, stage/resectability, tumor burden, liver reserve, indication, intent, treatment receipt/completion, response, mortality, outside-care completeness, causal effects, clinical utility, or safe clinical deployment. It also lacks laboratory units/reference ranges, result-release timestamps, discharge disposition, native diagnosis time, timed imaging/pathology, and external validation. Those claims require expert adjudication, additional linked sources or a prospective/causal/utility study.

Revisit a learned irregular encoder only after stable strict-frozen later-era P-minus-M, adequate event support and reproducible residual sequence nonlinearity. Revisit outcome adjudication and treatment questions only after adding native diagnosis/measurement-release times, imaging/pathology, stage, intent/receipt, mortality/outside-care linkage and expert review. If strict later-era support fails, do not redefine the era or rescue transport with bridge recalibration; park the calendar transport estimand and retain only a clearly labelled pooled descriptive assay-payload result. If strict transport is supported but calibration drifts, recalibration and prospective silent validation become the next study, not an automatic clinical rollout.
