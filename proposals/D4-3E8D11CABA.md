# UKB two-panel metabolic change and cardiometabolic multimorbidity: source-binding repair

## Episode-23 successor and scientific deliverable

This is a substantive child of `[prior hypothesis]`. The parent’s clinical question, participation-aware estimand, simultaneous-event repair, observed-boundary caveat, and matched model comparison are retained. A direct catalog/schema audit found a material executable defect: HbA1c, HDL, triglycerides, creatinine and cystatin-C fields are in the read-only `biological_samples` table, not `main`. This child corrects that binding and requires a five-source audit. A solver following the parent literally could fail to load the assay exposures or claim a four-table join that cannot supply them.

The future solver must newly construct and freeze the five-source/header/hash and overlap audit; paired assessment-date and assay features; stable one-domain landmark cohort; two-stage return/completeness flow; tie-aware event file; C_obs/cutoff audit; matched B0/M1/M2 route/multi-domain/death models; locked predictions; uncertainty; timing/phenotype/selection sensitivities; falsification outputs; and an output-linked supportive, adverse, or inconclusive conclusion. Readiness, a significant coefficient, or model convergence is not completion.

## Unresolved question and hypothesis

Available evidence supports that baseline metabolic indices associate with incident cardiometabolic disease and that progression can be represented with multistate or competing-risk models. It does not establish whether a dated within-person change between two UKB assessment-linked panels adds prognostic information beyond the panel-1 level, existing disease domain, disease duration, and prespecified covariates. A two-panel field-instance export also cannot establish specimen collection timing or clinical onset.

Primary hypothesis:

> Among UKB participants aged 40–69 who have exactly one of diabetes, cardiovascular disease, or chronic kidney disease recorded at both assessment-linked panels, remain in the same one-domain state at panel 1, and have complete paired HbA1c, triglyceride, and HDL measurements, worsening assessment-linked change predicts the first subsequent additional cardiometabolic domain beyond panel-1 levels, existing-domain identity, duration, and prespecified covariates.

The primary estimand is conditional internal prognosis among people with an observed valid second assessment and complete paired assays. It is not a causal effect of changing a biomarker, a biological slope, a clinical-onset claim, a monitoring benefit, a treatment recommendation, or a result transportable to non-returners. The scientific advance is an incremental, route-aware test of dated change versus current level under explicit observation/completeness selection, rather than another baseline association or an unconstrained model contest.

## Exact UKB bindings and availability

Snapshot: `[source checksum]`.

All sources are ordinary read-only CSVs, with no archive members, joined horizontally one-to-one on `eid`; overlapping fields must agree. The source catalog schemas and exact files are:

| table | exact source path | catalog schema | required fields |
|---|---|---|---|
| `main` | `[internal dataset path]` | `datasets/ukb/table-e4a9e4d8baa71a9d.json` | `53-0.0`, `53-1.0` assessment-date proxies |
| `assessment` | `[internal dataset path]` | `datasets/ukb/table-901ef6c7ddce2d51.json` | `53-0.0/1.0`; BMI `21001-0.0`; SBP `4080-0.0`; DBP `4079-0.0`; smoking `20116-0.0`; center `54-0.0` |
| `biological_samples` | `[internal dataset path]` | `datasets/ukb/table-c6b666d905f3b02f.json` | HbA1c `30750-0.0/1.0`; HDL `30760-0.0/1.0`; triglycerides `30870-0.0/1.0`; secondary creatinine `30700-0.0/1.0`; cystatin-C `30720-0.0/1.0` |
| `health_outcomes` | `[internal dataset path]` | `datasets/ukb/table-3cfae45e0905b0e3.json` | ICD-10 `41270-0.0`–`41270-0.258) with same-suffix `41280-0.0`–`41280-0.258`; ICD-9 `41271-0.0`–`41271-0.46` with `41281-0.0`–`41281-0.46`; death `40000-0.0/1.0` |
| `population` | `[internal dataset path]` | `datasets/ukb/table-38565c9e35e7cb6c.json` | sex `31-0.0`; recruitment age `21022-0.0` |

Source hashes: main `[source checksum]`; assessment `[source checksum]`; biological_samples `[source checksum]`; health_outcomes `[source checksum]`; population `[source checksum]`.

The catalog reports 30,799, 18,159, 1,775, 4,896 and 34 columns respectively; direct header inspection confirmed the required fields. A bounded first-10,000-data-row audit found 10,000 unique eids per source, 388 nonempty second-date values in main/assessment, and 271/297/329 nonempty second-panel HbA1c/HDL/triglyceride values in the biological-samples file. These are availability probes, not cohort estimates. Full duplicate, overlap, agreement, missingness, range, and event support checks are mandatory.

UKB field-instance arrays do not prove elapsed time. Per-field coding and units are incomplete; negative numeric values have no global missing interpretation and must not be globally recoded. The snapshot has no raw images, waveforms, verified narrative clinical text, or sequence/variant bundle. The genomics table is phenotype/derived metadata, not a sequence bundle.

## Cohort and time rules

Normalize code case and whitespace and freeze the phenotype:

- diabetes: ICD-10 E10–E14 or ICD-9 250;
- cardiovascular disease: ICD-10 I20–I25, I50, I60–I69 or ICD-9 410–414, 428, 430–438;
- chronic kidney disease: ICD-10 N18/N19 or ICD-9 585;
- negative-control disease: appendicitis, ICD-10 K35 or ICD-9 540.

A domain record requires a valid same-suffix code/date pair. Scan every listed suffix and take the minimum valid paired date for each domain. Code-only/date-only cells are audited but are not events. These are first recorded/coded dates, not adjudicated clinical onset.

Require age 40–69 inclusive, valid sex, five-source overlap, valid d0=`53-0.0` and d1=`53-1.0`, d0<d1, a 365–3,650-day gap, and agreement between main and assessment dates after normalization. Require finite paired core assays from `biological_samples` at instances 0 and 1. At both d0 and d1, exactly one target domain must be present, the same domain must persist, and its first coded date must be no later than d0. Exclude death on or before d1. Define duration=(d1−first-domain-date)/365.25. Do not infer assay instances 2/3. The field-53 interval is an assessment-date interval, not verified specimen timing.

Primary time zero is d1. Follow to the earliest post-d1 additional target-domain date, death, the observed censor boundary, or five years after d1. Death is absorbing and competing. A same-day death takes precedence over a new-domain record; reverse precedence is a sensitivity. If two or more new domains have the same earliest date, classify the event as a separate `SECOND_DOMAIN_MULTI` cause and retain its member set. A unique event is `SECOND_DOMAIN_UNIQUE` with its route label. Emit `DEATH` and `CENSOR` categories as well.

The maximum finite date in all `41280-*`, `41281-*`, and `40000-*` fields is `C_obs`, not automatically an administrative closure date. Report its value and date-range/source audit. Five-year incidence, calibration, and decision-curve claims are supportive only if source-level administrative completeness is documented; otherwise they remain conditional on an observed-boundary assumption. A d1+365 delayed-entry survivor analysis, gaps 182–5,475 days, lags 0/2/5 years, and alternative stable-domain definitions are labeled sensitivities, not replacements for the primary estimand.

For marker j, compute assessment-linked annualized change (x1−x0)/((d1−d0)/365.25); reverse HDL so worsening is positive. Standardize using fit-partition parameters only. Do not call this a biological slope.

## Participation and completeness

Report a flow that separates:

1. all rows and five-way eid overlap;
2. d0 date/age/sex and d0 one-domain eligibility;
3. valid d1 date in the allowed gap (return/date-observation process);
4. d1 same-domain survival eligibility;
5. complete d0 core assays;
6. complete d1 core assays;
7. final primary composite, unique-route, multi-domain, death and censor support.

Model d1 date observation among d0-eligible participants using only d0-available age, sex, domain, duration, d0 markers, d0 assessment covariates, center, calendar and gap. Show observation and assay completeness by domain, sex, center, gap and calendar. This diagnoses selection; it does not prove that missing d1 dates mean nonattendance or identify nonreturner outcomes.

Among d1-stable participants with complete d0 assays and a valid d1 date, model complete d1 assays using d0 assays, dates/gap, age, sex, domain, duration, center and d1 date availability. Fit stabilized IPCW in training data, clip at fit 1st/99th percentiles, check positivity and effective sample size, and refit the pipeline. Label it assay-completeness/observed-repeat sensitivity, not return-selection correction. A separately labeled return-weighted exploratory analysis is allowed only with stated d0 missing-at-random assumptions and adequate positivity; failure makes that sensitivity inconclusive.

## Matched models and substantive alternatives

All models use the same population, event architecture, death hazard, time zero, censoring, split, preprocessing, weights, uncertainty and locked evaluation.

- B0, the simple baseline, fits route-specific cause-specific Cox hazards for each existing-domain to unique-new-domain transition plus explicit death. Inputs are panel-1 HbA1c, triglyceride, HDL, existing domain, duration, age, sex, gap, BMI, SBP, DBP, smoking and center, with fit-frozen splines for continuous variables. No change variables enter B0.
- M1 fits the identical hazards and inputs and adds the three dated changes, with change-by-domain interactions only where route support was prespecified. It directly tests the incremental-information hypothesis.
- M2 fits the same architecture and adds a fixed common-axis change: fit-partition standardize HbA1c, triglyceride and reverse-HDL, set S_t=mean(z_HbA1c,t,z_TG,t,z_reverseHDL,t), and add deltaS=S1−S0 plus prespecified deltaS-by-domain terms. M1 can reveal discordant marker-specific history that M2 averages away; M2 can reveal coordinated burden that M1 obscures. M1-only support suggests marker-specific information, M2-only support common-axis information, and support for both complementary information.

A two-panel attention/recurrent model is deferred for a scientific reason: two observations provide little sequence structure, and extra capacity cannot resolve selected return, date-proxy timing, or coded-onset uncertainty. A four-instance slope/mixed-effects model is unavailable because verified assay instances 2/3 are not present. These are deferrals, not neural-network or GPU bans. Revisit with at least three verified dated panels or a bounded diagnostic showing stable added scientific information.

The actual scientific deliverable is newly fitted B0, M1 and M2 coefficients and route/death cumulative-incidence predictions, plus uncertainty, locked evaluation, tie/event outputs, participation/completeness diagnostics and falsification results. A CPU-first tabular fit is proportionate; future solver planning may use the configured 16-CPU/8-GPU/262,144-MiB/28,800-second envelope, while this discovery episode has 7,200 seconds. Estimates are planning estimates, not measured full-fit runtime; no GPU is required or rewarded.

## Split, uncertainty, evaluation and falsification

Hash participants, never rows, with SHA-256(namespace `ehr-hypothesis-discovery-v1`, dataset, eid) modulo 100: 0–59 fit, 60–69 model/threshold decisions, 70–79 locked test, 80–99 reserved and unread. Fit transformations, weights, splines, model choices and thresholds only in fit/tuning data.

The solver must emit the frozen hashed participant-level event file containing d1, earliest event date, event category, unique route if applicable, multi-domain member set, death-tie flag, censor boundary and split. Emit a tie table by existing domain, event category, split and locked-test status, including code-only/date-only cells, invalid dates, pre-d1 events, unique routes, multi-domain events and same-day death ties.

Report route coefficients and 95% intervals; five-year or boundary-supported route/death cumulative incidence; integrated/time-dependent Brier; calibration intercept/slope/error; discrimination; restricted mean event-free survival; and paired 200-resample participant-bootstrap intervals for M1−B0, M2−B0 and M1−M2. Refit preprocessing/selection inside bootstrap where feasible. Report hypothetical 5%, 10% and 20% review thresholds with alert rate, sensitivity, specificity, PPV, number needed to review and decision-curve net benefit, without calling thresholds validated actions.

Supportive requires at least 20 total and 5 locked-test composite events, adequate support for every claimed unique route, stable five-source/tie construction and weighting, a prespecified worsening-direction interval excluding the null for M1 or M2, and locked-test uncertainty supporting incremental Brier/calibration or prespecified 10% net-benefit improvement versus B0. It must not reverse under assay-completeness weighting or one-year lag, and appendicitis and within-state change permutation must not show a comparable signal. Five-year supportive language additionally requires administrative cutoff provenance.

Adverse is an informative null/reversal or worse locked performance, disappearance after duration or assay-completeness adjustment, comparable appendicitis/permutation signal, or no incremental information from dated change. This falsifies the selected conditional coded-event prognostic claim, not all biomarker biology or causal effects.

Inconclusive is inadequate composite/route support, failed positivity or effective sample size, unstable five-source joins or code/date/tie pairing, unverified outcome boundary for the claimed horizon, poor convergence/calibration, intervals spanning meaningful benefit and no benefit, or an unresolvable selection/timing/phenotype sensitivity. A threshold result without expert-approved action is inconclusive for policy value.

Computationally checkable claims include source hashes and headers, five-way eid joins, source-field locations, paired code/date construction, flow, date gaps/duration, event/tie/censor files, fitted models, locked predictions, uncertainty, calibration, Brier, decision curves, permutation and sensitivity outputs. Clinical onset, reasons for return/testing, treatment/adherence, causal effects, monitoring benefit, utility, transportability, nonreturner generalization, and policy validity require clinical adjudication, unavailable evidence, expert review or another study.

## Demonstration and seed dispositions

The accessible natural-history demonstration supports the value of structured dated disease histories; no Danish external validation or reproduction is claimed. The Bayesian longitudinal/genetic demonstration was not reproduced; this EHR-only question does not require missing genetic inputs, and the local genomics file is not a sequence bundle. The cancer demonstration’s supplement was inspected for ablation context, but the main article and complete STAR Methods remain unavailable and raw images are absent; no multimodal cancer claim is made.

UKB seeds 01 infection/severity, 02 organ aging, 03 kidney discordance/AKI, 04 fat distribution, 05 sleep/accelerometry, 06 post-infection proteomics, 07 CHIP, 08 cancer reserve and 10 genetic protection remain deferred rather than disproven because exact local timing, modality, staging, rare-event support, validated PRS or external-validation dependencies are missing or unverified. Seed 09 is retained only as the origin of this narrowed two-panel question. The present child does not claim that any seed reference establishes the hypothesis.

## Future solver completion

Completion requires the exact five-source/header/hash and overlap audit; deterministic assay/date and code/date construction; stable d1 cohort; two-stage participation/completeness flow; tie-aware endpoint and C_obs audit; matched B0/M1/M2 route/multi-domain/death models; locked predictions and evaluation; uncertainty; timing, phenotype, selection, appendicitis and permutation sensitivities; and a conclusion linked to output files and classified supportive, adverse or inconclusive. No full-cohort event count, positivity result, administrative closure, full fit or scientific conclusion is claimed in this discovery episode.
