> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Does documented vasopressor-rescue timing change the interpretation of early hypotension burden?

## Scientific deliverable and unresolved claim

The new deliverable is a fitted, uncertainty-quantified analysis of whether the association between early low-MAP burden and a later **observed creatinine-rise signal** differs according to the timing of the first documented target-vasopressor record relative to the first observed low MAP. The solver must produce a frozen source/header audit, a pre-low-baseline cohort flow, an interval ledger, matched nested competing-state fits, an ordered observation/transition fit, standardized timing-stratified contrasts with uncertainty, whole-hospital transport results, and every prespecified falsification analysis. Discovery has fitted no model and claims no clinical result.

The strongest claim supported before fitting is only that the frozen eICU 2.0 snapshot contains ICU-relative MAP observations, ICU-keyed laboratory result and revision times, infusion rows with agent names and offsets, ICU disposition, admission descriptors, and hospital identifiers that can be joined by the stated keys. The source audit does not establish that an infusion row means administration, that a treatment began at that offset, that hypotension caused renal injury, or that any strategy is beneficial.

The unresolved claim is:

> Among adult ICU stays with a creatinine measured before the first observed low MAP, does the 0–6-hour hypotension-burden gradient for a 6–48-hour observed creatinine rise differ materially between prompt, delayed, pre-low, and absent documented target-vasopressor records, after accounting for dynamic testing opportunity and competing ICU exit?

Primary falsifiable hypothesis: at the same minimum MAP, pre-low baseline creatinine, MAP coverage/trajectory, and admission risk, prompt documentation of a target vasopressor within 30 minutes after the first observed MAP <65 is associated with a different 48-hour observed-rise burden gradient than delayed or absent documentation. The prespecified directional expectation is attenuation with prompt documentation if the record approximates timely rescue; a reversal or amplification is equally adverse to that interpretation and is not evidence of pressor harm. A signed interaction whose absolute difference in burden gradients is at least 2 percentage points is the clinical-importance margin.

This is an observational prognostic and measurement/treatment-context hypothesis. A prompt-versus-delayed association cannot estimate a causal effect of starting a vasopressor, a dose target, or a MAP target. A stable difference would advance interpretation by showing that a scalar hypotension signal is treatment-context dependent; a null would support using the burden as a more treatment-context-invariant prognostic descriptor, subject to the endpoint’s observation limits.

## Population, temporal origin, exposure and treatment timing

Use the frozen eICU 2.0 snapshot `[source checksum]`. The primary unit is one ICU stay keyed by `patientunitstayid`; repeated ICU stays are retained. All stays sharing `uniquepid` are kept in one split and a `uniquepid`-clustered sensitivity analysis is required.

Time zero is ICU admission. All offsets are integer minutes relative to admission.

The primary cohort is:

- age >=18 using `patient.age`; parse `"> 89"` as 90 and retain an age-censored indicator;
- at least two numeric plausible `vitalPeriodic.systemicmean` observations in [0,360], restricted to 20–200 mmHg;
- at least one numeric qualifying creatinine in [0,60] minutes with `labname` case-folded to `creatinine` and both `labmeasurenamesystem` and `labmeasurenameinterface` verified as mg/dL;
- a nonnegative, nonmissing `patient.unitdischargeoffset`;
- a first observed low-MAP time in [0,360], defined by the earliest valid raw observed periodic systemic mean <65; treatment timing is not defined from an interpolated MAP;
- the first qualifying creatinine result time is at or before that first observed low-MAP time, so the primary renal baseline is not selected after exposure begins;
- no qualifying creatinine result >= baseline + 0.3 mg/dL after the baseline and through 360 minutes.

The broader parent cohort without the pre-low-baseline requirement is a mandatory sensitivity, labelled as potentially post-exposure-baseline selection. Stays without any observed low MAP remain in a descriptive companion cohort but do not enter the primary treatment-timing interaction.

The first qualifying creatinine is the row with the smallest `labresultoffset` in [0,60] satisfying the frozen label/unit rule, not the minimum value. Exact duplicate `labid` rows are deduplicated. If multiple valid rows remain at the selected offset, use their median and report the count. Urinary creatinine is excluded. Invalid numeric values and unknown/incompatible units are excluded rather than converted. The primary event uses result time; a revised-time sensitivity is allowed only when the revised time is before the relevant observation boundary.

Define the first low-MAP time from raw periodic observations. For treatment context, define the first **documented target-pressor record** as the smallest `infusionDrug.infusionoffset` in [0,360] for a case-insensitive name match to norepinephrine, vasopressin, phenylephrine, dopamine, or epinephrine. This is a documentation timestamp, not a verified administration onset. Define four mutually exclusive categories:

1. pre-low/concurrent: first matching record at or before the first low-MAP time;
2. prompt-after-low: first matching record strictly after the first low-MAP time and no later than 30 minutes after it;
3. delayed-after-low: first matching record more than 30 minutes after the first low-MAP time and no later than 360 minutes;
4. no documented target-pressor record by 360 minutes.

A same-minute low MAP and matching infusion record belongs to pre-low/concurrent. Report the five agent-family indicators and number of distinct families as secondary descriptive features, but do not use `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, or `patientweight` to infer dose, intensity, or treatment effect. The primary timing analysis is not conditioned on a clinician’s intention and does not call the categories “early treatment” or “late treatment” without the word documented.

The early MAP exposure window is [0,360]. Collapse duplicate stay/time periodic rows by the prespecified median. For the primary burden, linearly bridge gaps <=30 minutes only and retain observed minutes, bridged minutes, all unbridged gaps and coverage indicators. Calculate minimum observed MAP, time below 65, trapezoidal area-under-65 in mmHg-min, longest low-MAP run, low-episode count, fraction of observed coverage below 65, and recovery slope. The primary burden is area-under-65; total minutes below 65 and no-interpolation burden are secondary. Minimum MAP and non-burden trajectory are retained so the burden contrast is not merely a nadir comparison. The first-low timing category uses raw observations and is unchanged by interpolation.

## Outcome, observation process and competing ICU exit

For each eligible stay let `end_i=min(2880, unitdischargeoffset_i)`. Follow-up begins at the 360-minute landmark and ends at 2,880 minutes or the ICU boundary. A post-landmark creatinine result is observable only when its `labresultoffset` is strictly after 360, no later than `end_i), and occurs before unit exit; a same-minute result and exit are assigned to exit. The primary endpoint is the first qualifying result at least baseline +0.3 mg/dL.

The mutually exclusive first terminal outcomes in 30-minute intervals are:

- observed creatinine-rise signal;
- unit death before that signal, identified at the unit boundary by `unitdischargestatus="Expired"` or `unitdischargelocation="Death"`;
- alive unit discharge/transfer before that signal, using a non-death unit status/location;
- no event through 2,880 minutes while still within the observable unit boundary.

A qualifying test without a rise is not terminal. At every interval retain whether a qualifying creatinine was observed, its result if observed, all-numeric-lab activity, time since the last qualifying creatinine and time since any lab. No result at or after an interval may enter that interval’s predictors. Testing opportunity is therefore an explicit process quantity, not an assumption that an absent result means no renal rise.

The primary standardized estimands at 48 hours are:

- the observed-rise CIF burden gradient within each timing category, `CIF_obs(area-under-65=P75)-CIF_obs(area-under-65=P25)`;
- the interaction/difference in those gradients between prompt-after-low and delayed/no-record categories, with pre-low/concurrent and no-record/delayed components separately reported;
- the analogous qualifying-test CIF gradient;
- the model-based rise-given-test gradient;
- death and alive-exit CIF gradients.

All contrasts use the development-set burden 25th and 75th percentiles, standardize to the same minimum-MAP, baseline-creatinine, coverage, trajectory, static-covariate and admission-risk distribution, and preserve the timing category when estimating within-category gradients. The conditional tested-result quantity is a decomposition of the recorded process, not a causal population effect.

## Exact source bindings and read-only provenance

The catalog is `[internal dataset path]`, catalog [source checksum]. Each source below is a gzip ordinary file; there is no internal archive member. Source data are read-only. The complete eICU catalog contains 31 tables; these are the required bindings.

- Source `[internal dataset path]` (the catalog path has the exact directory spelling `eicu database/EICU 2.0 data`), table `patient`, schema `datasets/eicu/table-ab037c09d7df9a3c.json`, schema [source checksum], source [source checksum]. Join on `patientunitstayid`. Use `uniquepid`, `hospitalid`, `wardid`, `age`, `gender`, `ethnicity`, `hospitaladmitsource`, `unitadmitsource`, `unittype`, `unitstaytype`, `unitvisitnumber`, `unitdischargeoffset`, `unitdischargestatus`, and `unitdischargelocation`.

- Source `[internal dataset path]`, table `vitalPeriodic`, schema `datasets/eicu/table-a22c6d6981a32279.json`, schema [source checksum], source [source checksum]. Join on `patientunitstayid`; use `observationoffset` and `systemicmean` (and `vitalperiodicid` for duplicate audit).

- Source `[internal dataset path]`, table `vitalAperiodic`, schema `datasets/eicu/table-72ace5b89971196b.json`, schema [source checksum], source [source checksum]. Join on `patientunitstayid`; use `observationoffset` and `noninvasivemean` only for the independent non-invasive-MAP sensitivity. Do not combine invasive/periodic and non-invasive observations as independent measures.

- Source `[internal dataset path]`, table `lab`, schema `datasets/eicu/table-79bdb33275339b1a.json`, schema [source checksum], source [source checksum]. Join on `patientunitstayid`; use `labid`, `labresultoffset`, `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`, `labmeasurenameinterface`, and `labresultrevisedoffset`. No future result can enter a testing predictor.

- Source `[internal dataset path]`, table `infusionDrug`, schema `datasets/eicu/table-18e1a8caaa91eb44.json`, schema [source checksum], source [source checksum]. Join on `patientunitstayid`; use `infusiondrugid`, `infusionoffset`, `drugname`, and retain but do not interpret `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, `patientweight`. The name map and record-time rules above are frozen before split-specific fitting.

- Source `[internal dataset path]`, table `apacheApsVar`, schema `datasets/eicu/table-67711a86e012835e.json`, schema [source checksum], source [source checksum]. Join on `patientunitstayid`; use `creatinine`, `meanbp`, `heartrate`, `temperature`, `respiratoryrate`, `wbc`, `fio2`, `pao2`, `urine`, `intubated`, `vent`, and `dialysis` only as untimed admission-severity descriptors in a sensitivity model.

- Source `[internal dataset path]`, table `apachePatientResult`, schema `datasets/eicu/table-754bebf64d3d9909.json`, schema [source checksum], source [source checksum]. Join on `patientunitstayid`; use `apachescore`, `acutephysiologyscore`, and `predictedicumortality` for admission-risk sensitivity and calibration/descriptive checks only. Actual outcomes and actual lengths of stay are never predictors.

- Source `[internal dataset path]`, table `hospital`, schema `datasets/eicu/table-811df7b2ef435e12.json`, schema [source checksum], source [source checksum]. Join `hospitalid` to `patient.hospitalid`; use `numbedscategory`, `teachingstatus`, and `region` as transport context. No held-out hospital effect is estimated; held-out hospitals use development-population standardization.

The `intakeOutput` table exists in the full catalog but is not used to define a kidney endpoint: the available records do not by themselves provide complete adjudicated urine-output/KDIGO semantics. Notes and other tables are not silently substituted for missing treatment indication or renal adjudication.

## Matched transparent baseline and ordered mechanistic alternative

All models use the same eligible stays, pre-low-baseline rule, 30-minute rows, raw event times, name/unit maps, outcome ordering, splits, standardization, and held-out hospitals.

Transparent competing-state baseline: fit regularized additive cause-specific pooled-logistic models for observed rise, unit death and alive exit. The same non-burden MAP trajectory, minimum MAP, coverage, baseline creatinine, static covariates, admission-risk descriptors and interval time enter all nested models.

- B0 adds no burden, treatment timing or dynamic lab process.
- B1 adds area-under-65 burden.
- B2 adds the four documented timing categories and agent-family indicators.
- B3 adds area-under-65-by-timing interactions.
- B4 adds interval testing history and observation-boundary features.
- B5 removes the burden-by-timing interaction from B4.

Report coefficients, calibration and standardized 48-hour CIFs. The primary transparent estimand is the B4 interaction/gradient, with B5 as the matched no-interaction null. Report design-matrix condition numbers for burden and interaction terms; weak support or numerical instability is inconclusive, not repaired through arbitrary regularization.

Ordered mechanistic alternative: fit a piecewise-exponential multi-state model on the identical interval ledger and source-derived inputs. It represents the recorded sequence of first low MAP, documented pressor-record timing, subsequent raw MAP recovery, qualifying creatinine observation without rise, observed rise, unit death and alive exit. It has separate observation intensity, conditional recorded-rise, death and alive-exit transitions. Its recovery state is a recorded MAP state, not proof of physiological recovery; its pressor state is a recorded infusion state, not proof of administration.

This alternative can reveal whether the interaction is carried by the transition from low MAP to a documented pressor record, by later recorded MAP recovery, by increased creatinine testing, or by competing exit. The additive baseline preserves the same inputs but reduces them to marginal interval hazards and loses this order/decomposition. The alternative is scientifically substantive because the unresolved issue is treatment/measurement timing, not generic predictive performance. No transition is interpreted as mediation or a treatment effect.

Preprocessing, label/unit maps, missingness rules, scaling, regularization and any spline basis are learned only in development data. For transport, assign hospitals before fitting. If a `uniquepid` appears across hospitals, assign its connected hospital component to one split; report the number of affected hospitals and any loss of held-out coverage. All stays of one `uniquepid` remain in one partition.

## Uncertainty, transport and required outputs

Use 500 hospital-cluster bootstrap replicates for confidence intervals and a `uniquepid`-clustered bootstrap sensitivity. For observation-weighted sensitivity, estimate interval test probabilities in grouped development folds, truncate weights only at a prespecified development 1st percentile, and report the truncation fraction. This does not establish missing-not-at-random validity.

Hold out whole hospitals or connected hospital components. Report development and held-out hospital counts, timing-category support, event counts, burden overlap, per-hospital gradients, pooled held-out gradients and interactions, calibration intercept/slope, Brier score, AUROC/AUPRC as secondary summaries, and prediction coverage. The transport criterion for the primary prompt-versus-delayed/no interaction is a held-out estimate with the same sign and at least 2 percentage points, plus the same sign in at least 70% of held-out hospitals with >=50 primary-cohort stays. If support is inadequate, label transport inconclusive rather than ranking hospitals or calling residual differences quality differences.

The solver must emit:

1. catalog, source and schema hashes; exact headers; full creatinine label/unit map; disposition map; vasopressor name map; and all exclusion counts;
2. cohort flow including pre-low-baseline exclusions, missing boundary, early rise, MAP coverage, low-MAP presence, timing categories, and no post-landmark test;
3. stay-level and 30-minute tables containing keys, source offsets, raw/bridged MAP coverage, first-low time, first documented pressor time/category, agent family, testing history, competing state, and split;
4. B0-B5 coefficients, transition/observation parameters, convergence and condition diagnostics;
5. timing-stratified and interaction standardized 48-hour observed-rise, test-opportunity, conditional-rise, death and alive-exit CIF contrasts with confidence intervals;
6. calibration, secondary discrimination, overlap, hospital-held-out transport and per-hospital stability;
7. no-interpolation, non-invasive-MAP, lab-revision, confirmed-rise, unit-boundary, alternate 30/60-minute timing cut point, positive-rate-record sensitivity, agent-definition and Apache-severity sensitivities;
8. a conclusion labelled supportive, adverse or inconclusive, with every scientific claim linked to an emitted output and observational database evidence separated from causal/clinical claims.

## Falsification and interpretation

Support for the directional “prompt documented rescue attenuates the burden gradient” interpretation requires:

- the B4 burden-by-timing interaction and the ordered model’s timing-stratified gradients agree in direction;
- the prompt-versus-delayed/no difference is at least 2 percentage points and its uncertainty is not compatible only with a clinically trivial contrast;
- the sign is not eliminated by explicit lab-observation and competing-exit modelling;
- the direction and calibration are preserved in held-out hospitals with adequate timing-category support;
- the result is not eliminated by no interpolation, non-invasive MAP, lab revision, confirmed-rise, unit-boundary, alternate timing cut point, positive-rate-record, agent-definition or Apache sensitivities.

A materially different but consistently reversed interaction is adverse to the directional rescue-attenuation interpretation. It must not be described as evidence that pressors cause renal injury. A null interaction is adverse to the claim that documented timing materially changes the prognostic burden interpretation, but does not prove treatment equivalence or safety. If the burden gradient itself is stable across timing groups, that is a useful negative result about treatment-context heterogeneity, not a treatment recommendation.

Support for an observation-dependent explanation requires measurable variation in post-landmark test opportunity and a consistent decomposition showing that timing/burden contrasts attenuate when test opportunity and unit exits are represented. This supports ascertainment dependence of a recorded endpoint, not a biological renal null.

Inconclusive findings include unstable label/unit or disposition maps; too few hospitals, timing strata, tests, rises, deaths or exits; near-universal or near-absent pressor documentation/testing; no overlap in burden across timing groups; unstable connected-component transport split; nonconvergence; severe collinearity; extreme observation weights; or intervals spanning the 2-point margin. Inconclusive is not support.

Computationally checkable claims include source hashes and headers, joins, criteria, offsets, deduplication, treatment-timing categories, feature availability, split integrity, states, fitted parameters, standardization, intervals, calibration, transport summaries and sensitivity reproducibility. Clinical adjudication or another study is required to determine actual vasopressor administration/start/indication/dose, the intended MAP target, whether the infusion record is complete, pre-ICU renal reserve, urine-output criteria, KDIGO AKI, and whether an observed creatinine rise reflects true kidney injury. The design cannot establish that prompt pressor use helps or harms, that hypotension causes AKI, or that clinicians should change treatment. A causal treatment study needs validated administration and dose semantics, treatment intent, richer time-varying confounding control, and adjudicated renal outcomes.

## Resource plan, provenance and retained branches

Discovery used the local dataset guide, current schema JSON, direct source-header inspection, a bounded real-row check, and the parent proposal/support audit. The checks found 200,859 patient rows, 208 hospital rows, all five target agent-name families in the first 200,000 infusion rows, and creatinine/urinary-creatinine label separation in the first 200,000 laboratory rows. These are availability checks only.

The future solver planning envelope is 16 CPU, 262,144 MiB, up to 8 allocated A100 GPUs, and 28,800 seconds. Full source construction, model fitting and 500 bootstraps were not timed in discovery. CPU-first is appropriate for tabular interval models; GPU use is not required and an unallocated shell cannot establish GPU absence. If profiling finds a matrix bottleneck, one allocated A100 may be requested and used as `cuda:0`, with measured runtime reported separately. No model training of the proposer/solver is involved.

The actual scientific completion is a new pre-low-baseline treatment-timing cohort, the B0-B5 fits, the ordered observation/transition fit, timing-stratified burden gradients and interaction, uncertainty, transport, falsification analyses, and evidence-limited conclusion. The deferred learned sequence branch may be revisited only after stable residual sequence structure remains across both prespecified models and hospitals, and only with the same observed-rise/test/exit estimands and calibration. The deferred causal branch requires missing treatment and renal evidence listed above.
