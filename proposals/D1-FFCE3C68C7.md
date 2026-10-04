> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Does hypotension burden survive trajectory and ascertainment adjustment? A dynamic, observation-aware eICU study

## Scientific deliverable and unresolved claim

The required new deliverable is a fitted, uncertainty-quantified decomposition of the early hypotension signal into: (i) minimum MAP, (ii) cumulative low-MAP burden, (iii) clinically interpretable persistence/recovery and vasopressor-response trajectory, and (iv) the laboratory-observation process. Completion requires a frozen cohort-flow table, source/value/coverage audits, a stay-interval analysis table, fitted nested models with standardized 48-hour competing-state contrasts and uncertainty, hospital-held-out calibration/transport results, and all prespecified falsification analyses. Discovery has not fitted these models or established a clinical result.

The strongest evidence already supported by the parent audit is only that the frozen eICU snapshot contains ICU-relative MAP, creatinine laboratory rows, disposition, infusion, severity, patient, and hospital fields that can be joined by the stated keys. It does not establish an association, a treatment effect, or clinical AKI.

The unresolved claim is whether early hypotension burden contains prognostic information beyond a treatment-relevant dynamic trajectory, and whether any apparent burden association is instead explained by how often creatinine is tested and therefore how often a creatinine rise can be observed.

Primary falsifiable hypothesis: among adult ICU stays that reach a 6-hour landmark without an early observed creatinine-rise signal, conditional on the same minimum MAP and measured baseline risk, a trajectory characterized by persistent low MAP, slow/non-recovery, or ongoing early vasopressor support has higher 6–48-hour cumulative incidence of an observed creatinine-rise signal than a trajectory with transient low MAP and recovery. The incremental area-under-65 burden contrast is expected to shrink substantially after these trajectory features are included; if a prespecified residual burden contrast remains clinically meaningful and transports to held-out hospitals, burden carries information not captured by the trajectory summary.

A co-primary measurement-process question is whether the burden/trajectory association with an observed creatinine rise is materially attenuated after accounting for pre-landmark renal testing opportunity and post-landmark creatinine-observation intensity. Such attenuation would support an ascertainment explanation for the database signal, not show that hypotension is harmless. Because testing is a response to illness and can be affected by discharge, treatment limitation, or interface failure, this is not a causal adjustment for clinical AKI.

Clinical importance: a persistent/non-recovering trajectory could identify patients for intensified renal surveillance or motivate a future intervention study. Conversely, a burden signal that disappears after trajectory and observation-process analyses would discourage interpreting a scalar time-under-threshold measure as a treatment target. The design cannot establish that raising MAP, changing vasopressors, or any other treatment prevents AKI.

## Population, landmark, and competing states

Use eICU 2.0 snapshot `[source checksum]`. Use one row per ICU stay keyed by `patientunitstayid`; include age >=18, parsing `age="> 89"` as 90 while retaining an age-censored indicator. Keep repeated stays as separate observations but assign all stays with the same `uniquepid` to one data split and use a uniquepid-clustered sensitivity.

Time zero is ICU admission and all offsets are minutes relative to ICU admission. Exposure/trajectory construction is [0,360] minutes; landmark is 360 minutes. Require:

1. At least two numeric `vitalPeriodic.systemicmean` observations in [0,360], after a prespecified plausible range of 20–200 mmHg.
2. At least one numeric creatinine row in [0,60] whose `labmeasurenamesystem` or `labmeasurenameinterface` is explicitly verified as mg/dL; unknown/incompatible units are excluded rather than converted.
3. The ICU stay reaches 360 minutes without unit discharge before the landmark.
4. The first qualifying baseline creatinine is not followed by a valid creatinine >= baseline + 0.3 mg/dL at an offset in (baseline offset,360]; such stays are excluded for an early observed-rise signal.

The baseline creatinine is the first qualifying mg/dL result at the smallest `labresultoffset` in [0,60], not the minimum. Deduplicate exact `labid` rows; if multiple valid rows share the selected offset, use their median and report the rule. Use result time, not revision time, for the primary event.

For each eligible stay, primary ICU observation ends at:
`end_i = min(2880, unitdischargeoffset_i)`
when a valid nonnegative `unitdischargeoffset` exists. Hospital discharge does not imply continued eICU laboratory observability after unit discharge.

From 360 minutes to `end_i`, define mutually exclusive first states:

- observed creatinine-rise signal: first valid creatinine at (360, end] >= baseline + 0.3 mg/dL;
- unit death: unit discharge is marked by an expiration/death status or location before the boundary;
- alive unit discharge/transfer or other unit observation loss before a signal;
- no observed rise through 2,880 minutes while still observable.

Print complete value maps for `unitdischargestatus`, `unitdischargelocation`, `hospitaldischargestatus`, and `hospitaldischargelocation`. If unit disposition is missing, report it and use a last-defensible ICU boundary only in a prespecified sensitivity; never impute continued lab observation. A later hospital death after alive unit discharge is a secondary disposition sensitivity, not primary continued creatinine observation.

The primary estimand is the training-fitted, standardized 48-hour cumulative incidence of an *observed creatinine-rise signal* before unit death or alive-unit observation loss, contrasting prespecified trajectory/burden profiles at the same minimum MAP, baseline creatinine, coverage, and admission risk. Before fitting, define a clinically nontrivial contrast as 2 absolute percentage points in 48-hour CIF for the prespecified 25th-to-75th profile comparison; a smaller estimate can still be reported but cannot support the primary clinical-importance claim. Report cause-specific and subdistribution sensitivity estimates, both labelled database-observable processes. Do not call this KDIGO AKI: pre-ICU renal reserve, complete urine output, dialysis context, and post-ICU laboratory follow-up are not reliably available for adjudication.

## Exact source bindings and construction

All source archive members below are ordinary files, and all sources remain read-only. The local catalog SHA-256 is `[source checksum]`; the source snapshot is `[source checksum]`.

- `[internal dataset path]`, table `patient`, frozen schema `datasets/eicu/table-ab037c09d7df9a3c.json`. Join key `patientunitstayid`; split key `uniquepid`. Use `age`, `gender`, `ethnicity`, `hospitalid`, `wardid`, `hospitaladmitsource`, `unitadmitsource`, `unittype`, `unitstaytype`, `unitvisitnumber`, `uniquepid`, and `unitdischargeoffset`, `unitdischargetime24`, `unitdischargelocation`, `unitdischargestatus`, plus hospital disposition fields only for the stated sensitivity. Negative offsets are excluded.
- `[internal dataset path]`, table `vitalPeriodic`, schema `datasets/eicu/table-a22c6d6981a32279.json`. Join `patientunitstayid`; time `observationoffset`; primary MAP `systemicmean`. The metadata identifies these as five-minute monitor summaries, not waveforms. Within [0,360], retain numeric values in 20–200, deduplicate same-time rows by median, and linearly interpolate only gaps <=30 minutes. Compute covered minutes, uncovered gaps, time below 65, area-under-65 (trapezoidal mmHg-min), minimum observed MAP, longest low-MAP run, and recovery slope.
- `[internal dataset path]`, table `vitalAperiodic`, schema `datasets/eicu/table-72ace5b89971196b.json`. Use `observationoffset` and `noninvasivemean` for an independent non-invasive-MAP sensitivity; do not merge simultaneous measurements as if they were independent or fill invasive gaps without a prespecified rule.
- `[internal dataset path]`, table `lab`, schema `datasets/eicu/table-79bdb33275339b1a.json`. Join `patientunitstayid`; times `labresultoffset` and `labresultrevisedoffset`; fields `labid`, `labname`, `labresult`, `labmeasurenamesystem`, `labmeasurenameinterface`. Freeze a case-insensitive creatinine label/value map before fitting. Use result time primarily; a last-revised-before-boundary sensitivity reports the effect of revision timing. Also derive lab testing-process variables: number of qualifying creatinine results, number of all numeric lab rows, time since last creatinine, inter-test intervals, and post-landmark creatinine observation indicators, without using a future result to predict its own event.
- `[internal dataset path]`, table `infusionDrug`, schema `datasets/eicu/table-18e1a8caaa91eb44.json`. Join `patientunitstayid`; time `infusionoffset`; fields `drugname`, `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, `patientweight`. Freeze case-insensitive name matching for norepinephrine, vasopressin, phenylephrine, dopamine, and epinephrine. Because the table lacks a universal dose unit, use early presence/onset and number of distinct infusion offsets as descriptive/trajectory features only; do not compare raw rates or claim titration effects without unit adjudication.
- `[internal dataset path]`, table `apacheApsVar`, schema `datasets/eicu/table-67711a86e012835e.json`. Join `patientunitstayid`; there is no time column. Use `creatinine`, `meanbp`, `heartrate`, `temperature`, `respiratoryrate`, `wbc`, `fio2`, `pao2`, `urine`, `intubated`, `vent`, and `dialysis` only as admission-severity descriptors/sensitivity covariates, not time-aligned pre-exposure measurements.
- `[internal dataset path]`, table `apachePatientResult`, schema `datasets/eicu/table-754bebf64d3d9909.json`. Join `patientunitstayid`; use `apachescore`, `acutephysiologyscore`, and `predictedicumortality` in sensitivity/descriptive calibration analyses. Do not use `actualicumortality`, actual lengths of stay, or actual ventilator days as predictors.
- `[internal dataset path]`, table `hospital`, schema `datasets/eicu/table-811df7b2ef435e12.json`. Join to `patient` on `hospitalid`; use `numbedscategory`, `teachingstatus`, and `region` as hospital context and for whole-hospital holdout. Do not use a hospital effect for a test hospital unless the transport rule is explicitly the training population intercept.

## Dynamic trajectory and observation-process definitions

Partition [0,360] into twelve 30-minute bins. For each bin, retain only information available by its endpoint. The B2 trajectory vector deliberately excludes cumulative area-under-65 and total minutes-below-65, which are reserved for the B1/B3 burden estimand. It uses bin-level MAP level (median systemicmean), bin minimum, covered minutes, and whether the bin contains a valid observation, plus the derived persistence/recovery features below. Define:

- persistence: longest consecutive low-MAP run and fraction of covered time below 65;
- recovery: slope from the lowest MAP to the last valid MAP, last-bin MAP, and a binary prespecified recovery-to >=65 state requiring a valid last-bin observation;
- instability: number of low-MAP episodes separated by >=30 covered minutes above 65;
- treatment-response context: whether a named vasopressor is present by the bin and whether infusion offsets increase after a low-MAP episode. This is not interpreted as a dose or causal treatment effect.

Testing-process features are kept separate from physiology: pre-landmark creatinine count, all-lab count, inter-test interval, and MAP/lab coverage. Post-landmark testing intensity is represented only at each 30-minute risk interval by labs observed since the previous interval and time since the last qualifying creatinine. These features are not allowed to use a lab result at or after the event interval. The primary trajectory estimand therefore uses pre-landmark process features; post-landmark process adjustment is an ascertainment decomposition sensitivity.

## Matched baseline, mechanistic alternative, and analysis

All models use the same landmark cohort, rows, unit-observation boundary, event definitions, covariates, split assignments, and held-out hospitals.

**Transparent nested baseline.** Fit regularized 30-minute cause-specific pooled-logistic models from 360 to 2,880 minutes with competing unit death and alive-unit observation loss. Model B0 contains baseline creatinine, minimum MAP, MAP coverage, age/sex/ethnicity, admission source/type, unittype, Apache sensitivity variables, early vasopressor presence, and hospital context. Model B1 adds area-under-65. Model B2 adds the prespecified persistence/recovery/instability/vasopressor trajectory vector, whose features exclude cumulative area-under-65 and total minutes-below-65. Model B3 contains both trajectory and area-under-65. Before fitting B3, report the development-set correlation/condition number for the burden and trajectory design; if the burden contrast is numerically unstable, label that estimand inconclusive rather than select a regularization-dependent result. The key burden estimand is the standardized B3-versus-B2 CIF contrast per 60 mmHg-min and between the 25th and 75th burden percentiles at fixed minimum MAP. The key trajectory estimand is B2 versus B0 at fixed minimum MAP, and the process audit is B2/B3 with pre-landmark process terms plus a separate post-landmark observation-process sensitivity. Use restricted cubic splines only if knots are frozen from training data; otherwise use prespecified linear/scaled terms.

**Mechanistic alternative.** Fit a cause-specific piecewise-exponential multi-state model with the same 30-minute intervals and four states: landmark/no signal, observed creatinine rise, unit death, and alive-unit observation loss. The transition hazard uses time-varying trajectory segments (persistence, recovery, low-MAP episodes, vasopressor presence), baseline creatinine, MAP coverage, static/admission covariates, and laboratory observation opportunity. A parallel observation submodel estimates the probability of a qualifying creatinine observation in each interval from only information available at that interval; use it to report inverse-observation-weighted and joint-process sensitivity estimates, not to assert an unmeasured true AKI outcome. Fit hospital effects only in training hospitals (random intercept or stratified training-hospital baseline); for an unseen hospital use the predeclared training-population intercept. Standardize all CIFs to identical minimum MAP and baseline risk.

This alternative reveals whether two patients with the same nadir and similar scalar burden differ because one has a single recoverable dip while the other has repeated/persistent low MAP with ongoing vasopressor support, and whether the apparent creatinine event is partly a consequence of testing opportunity. A scalar burden model cannot represent these distinctions. It is not selected because it is more complex or because it may improve a score; it is selected because these shape and ascertainment mechanisms are the scientific uncertainty.

Report coefficients/hazards, 48-hour CIF contrasts, calibration intercept/slope, Brier score, AUROC/AUPRC as secondary discrimination summaries, and hospital-held-out performance. Use hospital-clustered bootstrap intervals, with a uniquepid-clustered sensitivity. Do not compare models by a small prediction gain alone; require a stable clinically scaled estimand and mechanism-specific contrast.

Split hospitals into development and held-out sets before feature fitting, label-map confirmation, imputation, scaling, and knot selection. Use a fixed seed and report hospital counts and patient/stay overlap. Within development data, use grouped inner validation by hospital for regularization. No stay from a held-out hospital contributes to fitting, and all stays sharing a `uniquepid` remain in one partition.

## Falsification, interpretation, and evidence limits

Supportive trajectory evidence requires a >=2-percentage-point persistence/recovery contrast at fixed minimum MAP, directionally consistent confirmed-rise sensitivity, adequate uncertainty, and preserved direction/calibration in held-out hospitals. Support for unique burden requires a >=2-percentage-point B3-versus-B2 contrast that survives no-interpolation, coverage restriction, non-invasive-MAP, lab-revision, unit-boundary, and vasopressor-definition sensitivities. Support for an ascertainment explanation requires at least 50% attenuation of the corresponding standardized observed-rise contrast after the predeclared observation-process analysis, together with measurable between-patient variation in testing opportunity; it does not establish a biological null.

Adverse findings are a null/reversed trajectory contrast, a burden contrast explained by minimum MAP or trajectory, disappearance with density/unit-boundary/revision sensitivity, poor held-out calibration, or a process effect that is unstable across hospitals. These findings reject the corresponding prognostic interpretation but do not prove hypotension is safe or that testing caused the association.

Inconclusive findings include unstable unit/value maps, too few eligible stays or hospitals/events, sparse MAP/creatinine coverage, dominance of unit discharge/death, weak variation in trajectories or testing opportunity, nonconvergence, or intervals spanning the prespecified 2-percentage-point clinically meaningful contrast. Do not relabel an inconclusive database process as support.

Computationally checkable claims include source headers and schema hashes, label/unit maps, row counts, cohort flow, deduplication, coverage, joins, split integrity, state/event times, fitted parameters, standardized contrasts, uncertainty, calibration, held-out transport, and sensitivity stability. Clinical AKI adjudication, pre-ICU renal reserve, complete urine-output context, treatment intent/dose semantics, causes of missing tests or discharge, causal effects of MAP/vasopressors, and a bedside treatment threshold require expert review, richer data, or another prospective/causal study. The configured eICU release has no images, raw waveforms, or complete narrative clinical context; vitalPeriodic is a summary stream.

## Resource plan and solver outputs

Discovery used read-only source/catalog/schema/header inspection and prior bounded audit material; no full fit or clinical conclusion has been claimed. The future solver envelope is 16 CPU, up to 8 A100 GPUs, 262,144 MiB, and 28,800 seconds. The nested pooled-logistic and piecewise-exponential fits are expected to be CPU-first; this is an unverified estimate because full MAP/lab construction and hospital bootstrap time were not measured. A GPU is not required. If a learned temporal sensitivity is later justified by residual trajectory structure, it must use one allocated A100, `cuda:0`, identical inputs/splits/targets/calibration and a prespecified resource cap; no such model is needed for the primary study.

Required outputs:

1. source/header, schema-hash, value/unit, disposition, and infusion-name audits;
2. cohort flow and ICU observation-boundary table;
3. stay-level 30-minute analysis table with MAP coverage, nadir, burden, persistence/recovery, vasopressor context, creatinine baseline/event, laboratory testing process, competing state, and split;
4. B0–B3 coefficients, mechanistic transition/observation parameters, standardized 48-hour CIF contrasts, uncertainty and calibration;
5. held-out-hospital predictions and calibration/Brier/AUROC/AUPRC summaries;
6. no-interpolation, coverage, non-invasive-MAP, lab-revision, unit-disposition, confirmed-rise, uniquepid-cluster, and vasopressor-definition sensitivities;
7. a conclusion labelled supportive, adverse, or inconclusive, with every scientific claim linked to an emitted table or figure and with observational versus clinical/causal claims explicitly separated.

## Alternatives retained and revisit rule

The parent’s scalar burden versus mechanistic trajectory comparison is retained and made decisive through the B2-versus-B3 nested estimand. A pure GRU/temporal-convolution model is deferred because the immediate uncertainty is interpretable persistence/recovery versus ascertainment, not whether a black-box sequence can improve prediction; it may be revisited only if held-out residuals show stable unmodelled trajectory structure and a preregistered learned model can preserve the same estimand and observation accounting.

The eICU testing-practice direction is incorporated as a bounded observation-process analysis because its exact `lab` fields are available, but it is not promoted to a causal under-monitoring claim: clinician response, discharge, treatment limitation, and interface failure are not distinguishable. Hyperoxia and ventilatory-burden directions remain deferred. Their generic `respiratoryCharting` labels and `respiratoryCare` intervals require a frozen clinical label dictionary and expert validation; `apacheApsVar.fio2/pao2` lacks time, and available fields do not guarantee plateau pressure or tidal-volume semantics. Reconsider them only after label coverage and clinical adjudication are established.

The evidence that would justify revisiting the learned model is reproducible, held-out residual structure not explained by the trajectory features; the evidence that would justify revisiting respiratory hypotheses is expert-verified label/measurement coverage; the evidence that would justify a causal MAP-treatment study is an adjudicated AKI endpoint, treatment intent/dose timing, and a design addressing time-varying confounding.
