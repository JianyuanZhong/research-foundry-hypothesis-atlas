# Episode 9 successor: transfer-proximal worsening beyond current state and ascertainment

Parent: `[prior hypothesis]`, assessed valid and assigned by the Lead.

This child preserves the parent’s scientific estimand: whether worsening in recorded physiologic abnormality during the last 24 hours of an ICU stay adds clinically meaningful prognostic information beyond current recorded burden, last values, and charting density. It repairs three residual ambiguities that could otherwise invalidate that interpretation:

1. `B_density2` is made ascertainment-only. Its earlier version included abnormality vectors, so it was not a density-only comparator and could absorb part of the trajectory signal before `F` or `Delta` was added.
2. The seven-day same-admission outcome explicitly treats alive hospital discharge as a terminal competing event. A patient discharged alive cannot later have a same-`hadm_id` ICU return, so treating discharge as ordinary censoring while calling the result a seven-day cumulative incidence is not coherent.
3. The operational event is named a subsequent ICU stay/re-entry, rather than an adjudicated “readmission” or clinical “return.” Exact-time and overlapping stays are chronology anomalies or ties, not silently interpreted clinical events.

No clinical result is claimed. The reference execution remains a prerequisite.

## Question, evidence boundary and advance

The unresolved question is whether a patient’s recorded vital abnormality is worsening as transfer approaches, conditional on the final recorded burden, the final last-value snapshot, and the amount of measurement in both windows. The clinical importance is the decision to move a patient from ICU monitoring and rescue capacity to a lower-acuity setting. A reproducible signal could motivate prospective evaluation of targeted post-ICU surveillance; a null or ascertainment-sensitive result would argue against treating a single last chart value as a sufficient discharge-readiness marker.

The primary hypothesis is:

> Among adults with a first eligible ICU stay ending before the same hospital admission ends, a larger transfer-proximal change in observed vital-abnormality burden from the preceding 24 hours to the final 24 hours (`Delta = F - P`) is associated with a higher seven-day cumulative incidence of a first subsequent same-admission ICU stay or in-hospital death before that stay, after adjustment for final burden, final last values, and measurement density in both windows.

This is a prognostic association and incremental-prediction hypothesis at ICU `outtime`. It is not a claim that transfer causes the outcome, that delaying transfer helps, or that an oxygen or monitoring intervention should be changed.

Before execution, the strongest evidence-supported claim is limited to data and provenance: the configured MIMIC-IV 3.1 snapshot contains the linked admissions, patients, ICU-stay, ICU chart-event, dictionary and hospital-transfer fields required for this operational experiment. Direct inspection of the fixed dictionary member confirms:

- 220045 Heart Rate, numeric, bpm
- 220052 Arterial Blood Pressure mean, numeric, mmHg
- 220181 Non Invasive Blood Pressure mean, numeric, mmHg
- 220210 Respiratory Rate, numeric, insp/min
- 220277 O2 saturation pulseoxymetry, numeric, %
- 223761 Temperature Fahrenheit and 223762 Temperature Celsius, numeric
- 223834 O2 Flow, 227287 O2 Flow (additional cannula), and 227582 BiPap O2 Flow, numeric, L/min
- 223835 Inspired O2 Fraction, numeric
- 226732 O2 Delivery Device(s) and 223758 Code Status, text

No available evidence establishes that `Delta` is independent of documentation, predicts a clinically adjudicated ICU readmission, identifies a safe transfer policy, or represents true bedside instability.

## Exact source bindings and provenance

The frozen MIMIC snapshot is `[source checksum]`.

Primary read-only source ZIP:

`[internal dataset path]`

Catalogued size: 10,551,747,784 bytes. Catalogued [source checksum].

Required archive members, table identities, joins, time fields and schema hashes are:

| Use | Table / archive member | Join and required fields | Schema SHA |
|---|---|---|---|
| admission anchor, discharge and death | `hosp/admissions`; `mimic-iv-3.1/hosp/admissions.csv.gz`; catalog `datasets/mimic/table-e8ec3e6e4c428559.json` | `(subject_id, hadm_id)`; `admittime, dischtime, deathtime, admission_type, admission_location, insurance, hospital_expire_flag`; `discharge_location` is audit-only | `[source checksum]` |
| age and sex | `hosp/patients`; `mimic-iv-3.1/hosp/patients.csv.gz`; catalog `datasets/mimic/table-9154f8c46cade9af.json` | `subject_id`; `gender, anchor_age, anchor_year_group`; `dod` is audit-only | `[source checksum]` |
| index and later ICU stays | `icu/icustays`; `mimic-iv-3.1/icu/icustays.csv.gz`; catalog `datasets/mimic/table-7d5c8feb0fb0dbd4.json` | `(subject_id, hadm_id, stay_id)`; `first_careunit, last_careunit, intime, outtime, los` | `[source checksum]` |
| exposure features | `icu/chartevents`; `mimic-iv-3.1/icu/chartevents.csv.gz`; catalog `datasets/mimic/table-8208609a785ea7e8.json` | `(subject_id, hadm_id, stay_id)`; `charttime, storetime, itemid, value, valuenum, valueuom, warning`; only `charttime` controls windows | `[source checksum]` |
| fixed labels only | `icu/d_items`; `mimic-iv-3.1/icu/d_items.csv.gz`; catalog `datasets/mimic/table-d1023acc404fd1d4.json` | `itemid`; `label, unitname, param_type`; join on `itemid`, do not expand the manifest | `[source checksum]` |
| movement/chronology audit only | `hosp/transfers`; `mimic-iv-3.1/hosp/transfers.csv.gz`; catalog `datasets/mimic/table-685b6b74d0d7c547.json` | `(subject_id, hadm_id)`; `transfer_id, eventtype, careunit, intime, outtime`; never use an inferred ward taxonomy as exposure or endpoint | `[source checksum]` |

All source rows remain read-only. The standalone note files
`[internal dataset path]`,
`discharge_detail.csv.gz`, `radiology.csv.gz`, and `radiology_detail.csv.gz` are not predictors. They cannot supply validated clinician intent, treatment limitation, functional readiness, actual oxygen delivery, reason for ICU re-entry, or adjudicated instability. Raw waveforms and MIMIC-CXR images are unavailable.

The dataset guide records deidentified subject-specific timestamp shifts; use within-subject intervals only. `anchor_year_group` is descriptive or a categorical covariate included identically in all models, never a chronological split.

The three research-ambition demonstrations are methodological context, not evidence for this hypothesis. Natural-history and Bayesian demonstration materials were not used to import a modality or a claim. The cancer demonstration’s main article and full STAR Methods remain unavailable; its available supplement is not treated as a substitute. The relevant expert seed is `[starting question]`, “Residual instability before ICU discharge,” from `references/expert-seeds/cards/mimic-10.md`; it is an untested question and motivates the topic, but does not establish it. The ten imported native-MIMIC seed candidates in `inputs.json` were assessed as repairable alternatives and none is selected as the parent: `[prior hypothesis]`, `[prior hypothesis]`, `[prior hypothesis]`, `[prior hypothesis]`, `[prior hypothesis]`, `[prior hypothesis]`, `[prior hypothesis]`, `[prior hypothesis]`, `[prior hypothesis]`, and `[prior hypothesis]`. Their repairable status is not evidence for this ICU-transition hypothesis.

## Population and temporal ordering

Use one explicit timezone-naive datetime parser. Cohort selection, index selection and chronology validation precede chart-event feature construction and future-outcome construction.

1. Join `icu/icustays` to `hosp/admissions` on `(subject_id, hadm_id)` and to `hosp/patients` on `subject_id`. Retain unmatched joins and all chronology failures in an aggregate audit.

2. A candidate ICU stay is eligible if all of the following hold:
   - `anchor_age >= 18`;
   - nonmissing `admittime, intime, outtime, dischtime`;
   - `admittime <= intime < outtime < dischtime`;
   - ICU LOS `outtime - intime >= 1` hour;
   - `deathtime` is missing or `outtime < deathtime <= dischtime`.

   The last rule operationalizes an ICU exit before any in-hospital death. A nonmissing death time after `dischtime), duplicate identity key, or impossible chronology is an audit failure; such an admission is excluded from the primary analytic manifest and counted, not repaired from another field. `hospital_expire_flag` is a consistency audit and never replaces `deathtime`.

3. Within each `(subject_id, hadm_id)`, sort eligible candidates by `intime), then numeric `stay_id`, and select exactly the earliest eligible stay. This uses no chart events and no future outcomes. Later ICU stays are used only for the operational endpoint and chronology audit. Preserve an all-candidate manifest with eligibility and exclusion reasons.

4. Set `t0 = outtime). Primary windows are contiguous and half-open:
   - preceding A: `[t0 - 48 hours, t0 - 24 hours)`;
   - final B: `[t0 - 24 hours, t0)).

   Exactly `t0 - 24h` belongs to B; exactly `t0` is excluded. Only rows with the selected `stay_id` are eligible. Rows with matching subject/admission but another stay are excluded. `storetime` is audit-only and cannot qualify a row or rescue a missing `charttime`.

5. The paired primary estimand requires at least four of six four-hour bins covered in both A and B. A covered bin has at least one valid observation in the fixed vital manifest. This is a measurement-eligibility estimand conditional on observed coverage, not a population-wide claim about all ICU exits. Every failed index remains in the audit manifest. Compare gate pass/fail by outcomes, care units, anchor-year group, partition and density.

6. The secondary all-eligible prediction estimand uses all otherwise eligible indexes. Missing A/B summaries receive development-fitted imputation and missing indicators. It is a prediction sensitivity and must never be described as the paired trajectory association.

## Fixed feature construction and trajectory estimand

Use only `valuenum` for numeric features. Apply validity before any aggregation:

- HR: 20–250 bpm;
- RR: 4–80 insp/min;
- SpO2: 50–100%;
- arterial and non-invasive MAP: 20–200 mmHg;
- temperature: 30–43 °C after Fahrenheit conversion `(F - 32)/1.8`;
- oxygen flows: nonnegative;
- FiO2: 0.21–1.00 if recorded as a fraction; values in (1,100] divided by 100; normalized values outside 0.21–1.00 invalid.

Invalid values are counted by item, window and bin and excluded; they are never repaired. For each bin, a valid vital observation is any valid HR, MAP, RR, SpO2 or temperature. An abnormal valid observation is HR <50 or >100, RR <8 or >24, SpO2 <92%, MAP <65 mmHg, or temperature <36 °C or >=38 °C. Arterial and non-invasive MAP remain separate. For the combined MAP audit feature only, use the minimum of valid arterial and non-invasive values in the bin.

For each window w:

- `covered_w` = number of covered bins;
- `abnormal_w` = number of covered bins with at least one abnormal valid vital;
- `burden_w = abnormal_w / covered_w`;
- `P = burden_A`;
- `F = burden_B`;
- `Delta = F - P`.

The estimand is change in observed, covered-bin abnormality, not change in latent physiology. A positive `Delta` means more abnormal covered bins near `t0`. Since the primary model includes `F` and adds `Delta`, its trajectory coefficient represents the planned preceding-to-final change conditional on the final burden. It is algebraically equivalent to adding P at fixed F, but `Delta` is the prespecified clinically readable contrast. Do not add P separately in the primary model.

Aggregate features may include six-bin coverage vectors, abnormality vectors, valid/invalid counts, per-domain counts and missingness indicators for audit and sensitivity analyses. No raw chart rows, raw values or notes are written to derived outputs.

For each final-window numeric domain, the last-value snapshot is the median of valid observations at the latest eligible `charttime`; ties at that `charttime` use the median of valid values. Keep domain-observed indicators. Retain separate arterial MAP, non-invasive MAP and combined MAP. Oxygen summaries are maximum valid flow across 223834, 227287 and 227582 and maximum normalized FiO2, with item-specific observed indicators. Device and code-status text are used only as observed/not-observed indicators and aggregate frequency audits; no text value is converted to support mode, treatment limitation or goals of care.

## Primary outcome and competing risks

The primary target is the seven-day cumulative incidence of an operational same-admission event, with alive discharge treated as terminal because the endpoint is deliberately restricted to the current `hadm_id`.

For each index, set `H = t0 + 7 days`. Candidate subsequent ICU stays are rows in `icu/icustays` with the same `(subject_id, hadm_id)`, different `stay_id`, nonmissing `intime`, and `intime > t0`. Select the earliest by `intime), then numeric `stay_id`. This is called a “subsequent ICU stay/re-entry,” not an adjudicated readmission or clinical return. A stay with `intime = t0` is a temporal tie; a stay beginning before `t0` that overlaps the index is a chronology anomaly. Both are excluded from the primary event label and reported separately, with fixed sensitivities assigning exact-time ties to re-entry or excluding all overlapping admissions. `hosp/transfers` is used only to audit chronology, not to invent an ICU/ward taxonomy.

Evaluate the earliest first event among:
   
- Cause 1, subsequent ICU re-entry: a qualifying later ICU stay at time `r`, with `r <= H`, `r <= dischtime`, and before any qualifying in-hospital death;
- Cause 2, in-hospital death before re-entry: nonmissing `deathtime = d`, `t0 < d <= min(H, dischtime)`, and no qualifying re-entry at or before d;
- Cause 3, alive hospital discharge: `dischtime = q <= H`, with no cause 1 or 2 at or before q and `deathtime` missing or strictly after q.

Exact equality among re-entry, death and discharge is an indeterminate event-time tie. Exclude it from the primary three-cause fit and report fixed sensitivities assigning ties by a declared deterministic priority. Never use `discharge_location` to infer alive status or readiness.

If none of causes 1–3 occurs by H, the index is event-free at the seven-day horizon. A discharge after H is not a cause-3 event for the H target. Death after a qualifying re-entry is not cause 2; the index is already cause 1. An alive discharge before H is not ordinary censoring: it is cause 3, after which a same-admission re-entry is impossible by definition. This yields a coherent Aalen–Johansen target for the composite `CIF1(H)+CIF2(H)`. The 12-hour, 48-hour and through-discharge analyses are secondary, explicitly different horizons.

This outcome cannot capture outpatient ICU use after discharge, another admission, reason for re-entry, treatment limitation, or whether the ICU stay was a clinically avoidable readmission. Those are unavailable.

## Nested baselines and model comparison

Use one all-index manifest, one subject-level partition and identical preprocessing for every model. Hash `subject_id` with SHA-256 into fixed 60% development, 20% validation and 20% locked test partitions; all admissions for one subject remain together. The hash is a reproducible split, not a calendar split.

The density baseline is repaired as follows. Abnormality vectors are retained in audit files but are prohibited from `B_density2`.

- `B0`: gender, anchor_age, admission_type, admission_location, insurance, first_careunit, last_careunit, ICU LOS, hours from `admittime` to `t0), and count of earlier ICU stays in the admission with `outtime <= t0`; fixed missing indicators. Include `anchor_year_group` categorically in every model or omit it from every model.
- `B_last`: `B0) plus final-window last valid HR, separate/combined MAP, RR, SpO2, temperature, oxygen flow and FiO2, with observed/missing indicators.
- `B_density2`: `B_last) plus only measurement-opportunity features from A and B: six-bin vital coverage indicators/counts, total valid and invalid rows, per-domain valid and invalid row counts, fixed `log1p` counts, oxygen observation indicators, and missingness indicators. It must contain no abnormality vector, abnormal bin count, burden, per-domain abnormal indicator or other value-derived abnormality.
- `B_final`: `B_density2) plus final burden `F) and prespecified final per-domain abnormal indicators.
- `B_traj`: `B_final) plus `Delta) only. This is the primary incremental contrast.
- `B_oxygen`: `B_traj) plus final and preceding maximum charted flow/FiO2. This is secondary bundled chart information, not delivered oxygen physiology.

Fit cause-specific ridge Cox models for causes 1, 2 and 3, with the same preprocessing and model recipe. Use a common prespecified penalty grid; choose the model penalty by inner development cross-validation minimizing the seven-day composite Brier score based on the three cause-specific hazards. Do not tune on the validation or locked test set. Fit no model for an event definition after seeing results. Validation is used once to estimate a fixed intercept-only calibration correction for the seven-day composite risk, with slope fixed at 1; report raw and validation-calibrated test metrics separately. The locked test is untouched until final evaluation.

Derive three-cause cumulative-incidence predictions from the fitted hazards. The primary predictive estimand is the paired locked-test difference in the raw seven-day composite Brier score, `Brier(B_traj) - Brier(B_final)`, where the binary target is cause 1 or 2 by H and cause 3/no event is 0. Report cause-specific CIFs, Aalen–Johansen estimates, calibration intercept/slope, and standardized risk contrasts. Do not treat cause 3 as a non-informative censoring event.

For a clinically interpretable scale, set the Delta contrast at the development 10th and 90th percentiles, apply those fixed values to each locked-test index while leaving its other covariates observed, and average the resulting predicted composite risks. Predefine a two-percentage-point absolute seven-day risk separation as the operational “clinically meaningful” threshold for interpretation. This is a reporting threshold, not a discharge cutoff, treatment threshold or claim of clinical utility. Also report the same contrast within development-derived final-burden quartiles; sparse strata are reported as sparse rather than pooled post hoc.

Report 95% intervals using 1,000 fixed-seed subject-bootstrap resamples of locked-test subjects for paired Brier, calibration and standardized-risk contrasts. Use a subject-clustered bootstrap or robust subject-level estimator for fitted coefficient summaries, with coefficients standardized by development-cohort SD. No p-value from a secondary sensitivity can override the primary locked-test comparison.

Pre-fit feasibility gates remain:

- at least 1,000 paired-primary indexes;
- at least 100 primary composite events (cause 1 or 2);
- at least 60% of all otherwise eligible indexes pass the paired gate;
- at least 20 composite locked-test events;
- at least 10 locked-test events of each cause 1 and 2 before cause-specific inferential summaries.

If the total or locked-test gate fails, report infeasible/sparse and do not lower a threshold, change the window or substitute an easier question. If the cause-specific gate fails, report descriptive cause-specific Aalen–Johansen estimates and uncertainty only. If paired eligibility is sparse but all-eligible prediction runs, label the estimands separately.

The reference execution is CPU-only, up to 4 CPUs and 16 GiB memory, with a 7,200-second science timeout. Read small admissions, patients, ICU-stay and dictionary members first; make one sequential projection pass through `icu/chartevents.csv.gz` for the fixed item IDs and all required windows, including placebo windows. Do not materialize all chartevents, make one archive pass per item, or write raw rows/notes. Outputs are aggregate manifests, audit counts, model summaries, sensitivity metrics and a conclusion ledger only.

## Falsification, ascertainment and integrity

Fail closed and report no scientific conclusion if any of the following occurs: duplicate primary index; selected feature row outside its assigned half-open window; `charttime >= t0); `storetime` used for eligibility; mismatched `stay_id`; unresolved impossible admission/ICU/death chronology; overlapping ICU stays used as ordinary events; event ties handled inconsistently; subject leakage across partitions; preprocessing fit on validation/test; prohibited post-`t0` predictors; or conclusions not linked to computed outputs.

Required checks:

1. **Earlier-window placebo.** Using the same primary index, outcomes, partitions and recipe, construct A0=`[t0-72h,t0-48h)` and B0=`[t0-48h,t0-24h)). Add the placebo change to `B_final) without changing the primary exposure. Use the intersection of the primary and placebo paired gates for the paired placebo comparison and report attrition. A similar or stronger placebo signal weakens the claim that the signal is transfer-proximal.

2. **Density-only audit.** Assert in code that `B_density2` has no abnormality vector, burden, abnormal count or abnormal indicator. Compare `B_last`, `B_density2`, `B_final` and `B_traj`. If `B_traj) adds no value over `B_final), or loses its signal when opportunity features are included, do not call it a physiologic trajectory result.

3. **Current-burden interpretation.** Apply development-only F quartile cut points to the locked test and report Delta coefficients and standardized risk contrasts within strata. A marginal signal that vanishes at comparable final burden is not evidence that worsening adds information beyond current state.

4. **Outcome-label negative control.** Keep the fitted locked-test predictions fixed. Permute the three locked-test outcome classes within the locked test, preserving class counts, and recompute composite Brier contrasts and calibration diagnostics. Do not invent permuted event times or refit a cause-specific process to impossible times. Repeated fixed-seed permutations should return to chance within the permutation distribution. Failure invalidates the metric/inference implementation, not the clinical hypothesis.

5. **Definition robustness.** Repeat with arterial MAP only, non-invasive MAP only, abnormal valid-row fraction rather than abnormal-covered-bin fraction, a two-hour exclusion of re-entries immediately after `t0`, 12/48-hour horizons, fixed exact-time tie assignments, and the all-eligible imputed prediction sensitivity. Large directional or calibration divergence is reported as definition and selection dependence.

6. **Chronology and terminal-discharge audit.** Verify that the earliest eligible later ICU stay is selected deterministically; overlapping and exact-time stays are never silently treated as returns; an alive discharge before H is a cause-3 event; and a same-time return/death/discharge tie follows the declared rule.

7. **Documentation audit.** Compare A/B burden, opportunity density, invalid rates and paired-gate failure by cause, first/last care unit, anchor-year group and subject partition. Audit device/code-status frequencies only as observed/not-observed aggregates. A result confined to highly charted records is an ascertainment warning.

8. **Shifted-window audit.** Confirm that each shifted window is disjoint from B and that every sensitivity reuses the frozen index and outcome manifest rather than selecting a new cohort after outcomes are known.

## Interpretation rules

Supportive results require a coherent primary pattern:

- `Delta` has a positive locked-test association with the composite, with directionally compatible cause-specific results where their gates pass;
- the primary `B_traj-B_final` Brier interval is below zero, or the prespecified development-based Delta P90-versus-P10 standardized composite-risk separation is at least two percentage points with a 95% interval excluding zero;
- the gain remains after the repaired density-only baseline, is not materially matched by the earlier placebo, and is not erased by MAP-source, re-entry-gap, tie or paired/all-eligible checks;
- a trajectory gradient remains in adequately populated final-burden strata; and
- outcome permutation behaves as a null metric check.

If only the coefficient direction is supportive but neither the Brier nor risk-separation criterion is met, report “association signal without demonstrated clinically meaningful incremental prediction,” not a fully supportive conclusion.

These results support only the narrower claim that the recorded change phenotype carries reproducible prognostic information beyond the specified recorded current state and measurement-opportunity proxies in this MIMIC cohort. They do not support a discharge threshold, transfer policy, causal effect, delivered-oxygen interpretation, or clinical utility.

Adverse results include a null/reversed locked-test Delta association, no incremental performance over `B_final), a stronger placebo, attenuation after density adjustment, disappearance within final-burden strata, or major instability across definitions. They argue that the recorded trajectory adds no reliable information beyond current recorded burden or is chiefly a general-acuity/documentation proxy. They do not establish that ICU transfer is safe.

Inconclusive results include failed event/coverage gates, sparse strata or paired windows, unstable intervals, contradictory competing-risk/placebo results, unresolved chronology, or a failed permutation/integrity check. A failed integrity or permutation check invalidates the computation; it is not evidence against the hypothesis.

## Claims that require more evidence

Computationally checkable claims are source/member/schema availability; fixed dictionary labels; join and index counts; chronology anomalies; window eligibility; valid/invalid counts; density-only feature membership; burden and Delta construction; event and tie labels; three-cause CIFs; locked-test metrics; bootstrap/permutation intervals; sensitivity outputs; and conclusion-ledger linkage.

MIMIC cannot adjudicate true bedside instability, work of breathing, actual oxygen delivery, device use, functional/cognitive readiness, staffing, ward capacity, clinician intent, treatment limitations, clinical reason for ICU re-entry, or whether a re-entry was preventable. Notes are not used to manufacture those labels. Observational associations cannot establish causality, transportability, an equitable threshold, prospective utility or a safe discharge policy. Those claims require clinician-adjudicated outcomes, richer prospective physiology and oxygen-delivery data, external validation, and a prospective surveillance or interventional/target-trial study.

## Required outputs and compiler contract

Write only derived aggregate files in the workspace:

- `cohort_outcome_manifest.jsonl`: one aggregate record per candidate/index with identity keys needed for internal joins, eligibility and exclusion flags, window coverage summaries, terminal event class/time, tie/anomaly flags and subject partition; no raw chart values or note text;
- `feature_audit.json`: aggregate counts by fixed item/window/bin, validity, missingness, gate status, and an explicit assertion that abnormal features are absent from `B_density2`;
- `model_metrics.json`: Aalen–Johansen three-cause estimates, cause-specific model summaries, raw/calibrated composite Brier, calibration and standardized-risk contrasts with intervals;
- `sensitivity_metrics.json`: placebo, density, MAP source, abnormal-row fraction, re-entry-gap, tie, horizon, permutation, chronology and all-eligible outputs;
- `conclusion_ledger.json`: every scientific conclusion linked to exact output file and row/field, estimand, estimate and uncertainty, with a flag for computationally checkable versus requiring adjudication, unavailable evidence or another study.

The verifier must check both computation and interpretation. It must include correct computations paired with unsupported causal/clinical-utility claims, and supportive, adverse and inconclusive result patterns interpreted according to the rules above. Verification cannot establish bedside validity, adjudicated re-entry reasons, causal effects, treatment limitation, or clinical utility.
