# Repeat-assessment biomarker history beyond the current panel

Parent: [prior hypothesis]
Status: frozen executable proposal; no scientific model has been fitted.

## Question, advance and hypothesis

For people with a verified repeat blood-biomarker assessment, does the prior panel add decision-relevant prognostic information beyond the current panel, age and sex, for a first later recorded cardiorenal/metabolic two-domain event?

This is a monitoring and risk-triage question. A supportive result could justify a prospective study of trajectory-aware follow-up; an adverse result would favor current values alone for this prognostic task. Neither result establishes that ordering repeat tests, changing treatment, or acting at a threshold improves outcomes.

The unresolved hypothesis is that annualized within-person change from instance 0 to instance 1 improves held-out five-year target-risk prediction and decision-curve net benefit beyond current instance-1 values, age and sex. Existing evidence available here supports only field presence, paired instances, participant joins and recorded outcome arrays. It does not establish that change is clinically meaningful, that codes represent disease onset, or that change improves prediction.

## Exact local data binding

Dataset guide: datasets/README.md. Catalog: [internal dataset path], [source checksum]. UKB snapshot: [source checksum].

Use only these read-only ordinary CSVs and their catalog tables:

1. biological_samples: [internal dataset path], [source checksum]; table biological_samples; schema datasets/ukb/table-c6b666d905f3b02f.json, 1,775 columns, schema [source checksum]. Required eid and these 16 literal columns: 30690-0.0, 30690-1.0, 30700-0.0, 30700-1.0, 30720-0.0, 30720-1.0, 30740-0.0, 30740-1.0, 30750-0.0, 30750-1.0, 30760-0.0, 30760-1.0, 30780-0.0, 30780-1.0, 30870-0.0, 30870-1.0.

2. main: [internal dataset path], [source checksum]; table main; schema datasets/ukb/table-e4a9e4d8baa71a9d.json, 30,799 columns, schema [source checksum]. Required eid, 21022-0.0 and 31-0.0. Local approved metadata verifies age at recruitment in years and sex coding9.

3. assessment: [internal dataset path], [source checksum]; table assessment; schema datasets/ukb/table-901ef6c7ddce2d51.json, 18,159 columns. Required eid, 53-0.0 and 53-1.0. These are assessment-date fields. They are not assumed to be exact specimen dates. Fields 55-0.0 and 55-1.0 are QA-only unless their coding is separately verified.

4. health_outcomes: [internal dataset path], SHA-256 [source checksum]; table health_outcomes; schema datasets/ukb/table-3cfae45e0905b0e3.json, 4,896 columns, schema [source checksum]. Required eid, 41270-0.0 through 41270-0.29, the position-matched 41280-0.0 through 41280-0.29, and 40000-0.0 and 40000-1.0.

The source headers exactly matched the corresponding schema column lists, and every required column was present. The catalog declares one-to-one horizontal joins by eid to population, with overlapping values required to agree. A full selected-column outcome scan measured 502,370 rows and 502,370 unique eids, 28 nonempty diagnosis-code cells without a same-position date, and no dates without a same-position code. Diagnosis dates reached 2022-10-31 and death dates reached 2022-12-19. An inherited scan measured 8,904 raw complete cases for the 16 biomarker cells. These are availability and integrity facts, not proof of endpoint completeness or clinical validity. The duplicate outcome columns in main are not used.

## Timing and population

Join the four tables by eid and audit uniqueness, overlap agreement and row counts before filtering. Retain participants with all 16 biomarker cells valid under a verified field dictionary, valid age and sex, valid assessment dates T0 = 53-0.0 and T1 = 53-1.0, T1 later than T0, and T1 no later than 2013-12-31. Define elapsed interval as (T1 minus T0) / 365.2425 years; require it to exceed 0.25 years and prespecify an upper bound before fitting. Exclude, rather than clip, impossible or implausible intervals.

The operational index is the participant-level T1 assessment date. The prospective interpretation is allowed only if an approved UKB field/protocol record verifies that biomarker instance 0 corresponds to the T0 assessment and instance 1 was collected at or before T1. The local files establish the existence and formatting of assessment dates, but not specimen timing, analyte identity, units, assay quality or missing-value codes. If alignment evidence is unavailable, the solver may report a temporally unresolved data association but must not call it prospective or use it to recommend monitoring.

The primary horizon is five calendar years after T1, H1 = T1 plus five years. Restricting T1 to 2013-12-31 makes H1 no later than 2018-12-31. A ten-year 2023 endpoint is removed: the local scan has no 2023 diagnosis/death dates and the catalog has no ascertainment-end field. Revisit it only with a later source and linkage metadata supporting 2023 coverage.

## Endpoint and ascertainment

Before fitting, require an ascertainment certificate stating the linkage type and complete diagnosis/date and death capture through every participant's H1, or provide a defensible individual observation-end date. An outcome row, an empty array, or the maximum observed event date is not evidence of complete event-free follow-up. If neither certificate nor end date exists, the five-year estimand is not estimable: output the failed gate, flow counts and data-integrity audit only.

Verify that 41270 is a diagnosis-code array, 41280 is its date array, their positions are paired, and the code system supports the prespecified mapping. Normalize only by trimming whitespace and uppercasing. For verified ICD-10 data, domains are metabolic E10,E11,E12,E13,E14; renal N18,N19; and cardiovascular I20,I21,I22,I23,I24,I25,I50. A code without a valid date at the same array position is not an event.

For each participant, exclude any recorded target-domain event on or before T1; this means no recorded event, not disease-free. The target endpoint is the earliest date strictly after T1 at which two distinct domains have valid codes. Domains recorded on the same date count together. Let E be that date and D the earliest valid death date from 40000-0.0 or 40000-1.0.

Use mutually exclusive statuses: target only if E is before D and E is no later than H1; death as a competing event if D is no later than H1 and D is no later than E, including a same-day tie; otherwise event-free only when observation is certified complete through H1. If observation ends earlier without either event, censor at that end date. Reverse same-day assignment is a sensitivity analysis.

Competing death is a separate cause in the cause-specific hazard model and target cumulative-incidence function; it is not an inverse-probability weight. Inverse-censoring weights, if needed, handle only right censoring and are estimated inside training folds. With certified complete five-year capture, weights equal one. The same status definition, horizon and weights are used for all models. At H1, the Brier target is one for target and zero for death, event-free follow-up or another valid competing status; censored records contribute only through their censoring weight. Decision-curve net benefit uses target cumulative incidence, with death treated as no target by H1. Thresholds 0.05 and 0.10 are analysis thresholds, not validated clinical action thresholds.

## Baseline and learned alternative

The primary baseline is designed to isolate biomarker history from timing artifacts:

- M0 current-only: the eight valid instance-1 values, age, sex, T1 calendar year and elapsed interval.
- M1 additive trajectory: M0 plus eight annualized slopes (instance-1 minus instance-0 divided by elapsed interval). A raw-change M1 is a prespecified sensitivity.
- M2 learned alternative: the M1 inputs plus prespecified current-by-slope interactions, fit with discrete-time gradient-boosted cause-specific hazard models.

M0 and M1 use the same discrete-time cause-specific hazard family with fold-local scaling and ridge tuning. M2 uses the same participant-level deterministic five-fold split, person-level separation, horizons, status construction and fold-local tuning. M2 is scientifically useful because threshold and discordant current-versus-slope patterns can be lost by an additive model; grouped current, slope, timing and interaction summaries are required. M2 is not retained merely for a small discrimination gain and is secondary to the M1-versus-M0 test.

The primary estimand is held-out five-year target cumulative-incidence Brier contrast, DeltaBS5 = BS5(M1) minus BS5(M0), where lower is better. Also report net-benefit contrasts at 0.05 and 0.10, calibration intercept/slope and plots, time-dependent discrimination, endpoint counts, joint slope-block inference and M2-versus-M1 contrasts. Use participant-clustered bootstrap intervals over held-out predictions, preserving folds. All imputation, scaling, tuning and feature filtering are fold-local; no outcome, death or post-index field enters exposure construction.

## Falsification and interpretation

Controls include date strictness, same-position code/date pairing, deterministic participant-level folds, no post-index leakage, age/sex-stratified permutation of slope vectors, raw-change sensitivity, same-day tie sensitivity and complete-case/missingness selection audits. A slope permutation should remove any M1 increment while retaining current values, outcomes and timing. Breaking code/date positions or permuting outcome dates must not improve the primary result.

Supportive evidence requires all gates to pass, DeltaBS5's 95% upper confidence bound below zero, positive net benefit at both analysis thresholds without material calibration degradation, and compatible raw-change, tie and domain sensitivities. Adverse evidence is near-null or worse M1, an interval excluding decision-relevant improvement, no decision-curve gain, or disappearance under permutation/integrity controls; this favors current values alone. Inconclusive evidence includes failed or unavailable gates, fewer than 100 target events, inadequate follow-up, intervals spanning useful gain and harm, instability across folds or endpoint definitions, or a changed conclusion under missingness handling. No conclusion may be drawn from readiness alone.

Computationally checkable claims are schema/header presence, joins, date parsing, position pairing, fold separation, model fitting, cumulative-incidence construction, leakage controls and numerical performance/uncertainty. Whether codes represent true disease onset, whether trajectory-aware monitoring benefits patients, treatment effect, biological mechanism, treatment thresholds and transportability require clinical adjudication, missing evidence, a prospective intervention or external validation.

## Alternatives and actual deliverable

A mechanistic signed deterioration score is deferred because units, assay/batch quality, exact specimen dates and more than two time points are unavailable. An AKI or kidney-discordance branch is deferred because the diagnosis arrays are not adjudicated acute episodes and lack serial creatinine, urine output and treatment context. A disease-history sequence transformer is deferred because this experiment has only two biomarker instances and no verified dated disease-history input; it would answer a different question. Revisit these branches with verified dictionaries, specimen dates, quality metadata, adjudicated outcomes, richer longitudinal records or external validation.

The future solver must newly fit M0, M1 and M2 if all gates pass, and produce the gate certificate, join audit, participant flow, endpoint/competing-event/censoring counts, fold assignments, fold-local preprocessing records, five-year out-of-fold cumulative-incidence predictions, Brier and decision-curve contrasts with 95% intervals, calibration/discrimination, slope-block inference, raw-change and tie sensitivities, grouped M2 patterns and permutation/integrity controls. A failed ascertainment or timing gate is itself a valid feasibility result, not support for or against the hypothesis.

## Compute

The header audit and 98.2-second two-CPU outcome scan are measured; no scientific fit is complete. The assessment date scan is a bounded availability diagnostic. Future fitting is estimated, not measured: 8-16 CPUs, 32-64 GiB RAM, CPU, and up to two hours for selected-column ingestion, five-fold M0/M1/M2 fitting, inner tuning, out-of-fold scoring, bootstrap and controls. The solver planning envelope is 16 CPUs, 262144 MiB, 8 GPU slots and 28800 seconds. GPU use is not prohibited, but this small tabular hazard fit has no demonstrated need for it. Discovery compute and future solver compute remain separate.
