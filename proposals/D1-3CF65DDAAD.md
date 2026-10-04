# Domain-discordant support recovery after ICU discharge

## Scientific deliverable

The future solver must newly construct and audit a leakage-safe MIMIC-IV 3.1 first-ICU-discharge cohort; derive separate respiratory and hemodynamic support-recovery states from the final 12 hours; estimate competing 6-, 24-, and 48-hour risks; fit a transparent domain-interaction baseline and a substantive two-domain duration-aware latent alternative; and report locked patient-level predictions, uncertainty, calibration, topology/coverage diagnostics, and falsification results.

Completion requires these workspace outputs:

- `cohort_audit.parquet`: one row per eligible first ICU stay with `subject_id,hadm_id,stay_id`, `intime,outtime,dischtime,deathtime`, cohort flags, first-stay selection, and temporal-integrity/missingness counts.
- `hourly_features.parquet`: one row per stay-hour in `[outtime-12h,outtime)`, with chart-time physiology, explicit observation masks, source/channel flags, vasoactive interval overlap, respiratory recorded-support evidence, and no post-landmark field.
- `domain_state_audit.parquet`: respiratory and hemodynamic final/preceding-half burden, recent/durable/active/residual/unobserved state, support-free recorded buffers, transition corroboration, coverage and contradictory-time flags.
- `outcomes_competing.csv`: mutually exclusive first-event time and type, including aggregate ICU return, transition-confirmed ICU return, topology-unconfirmed/immediate ICU return, in-hospital death, alive hospital discharge, follow-up, ties and observability.
- `baseline_test_predictions.parquet` and `factor_hsmm_test_predictions.parquet`: locked 6/24/48-hour cause-specific risks/CIFs and patient-level predictions.
- `cif_domain_associations.csv`: group-specific standardized CIFs, absolute contrasts, domain interaction contrasts, adjusted cause-specific associations and uncertainty.
- `calibration_brier.csv`, `bootstrap_intervals.csv`, `state_diagnostics.csv`, `topology_coverage.csv`, and `falsification_results.csv`.
- `interpretation.md`: every claimed result mapped to an output row and estimate/interval, labelled supportive, adverse or inconclusive, with computational and clinical claims separated.

No result is asserted by this proposal.

## Unresolved question, strongest existing claim, and hypothesis

The expert seed `[starting question]` asks whether persistent oxygen need or vital-sign fluctuation before ICU discharge predicts ICU return or death. Earlier board work made that idea executable by defining a first-ICU-outtime landmark, source-specific recorded-support buffers, and competing outcomes. The selected parent further separated ICU returns after an observed non-ICU interval from returns without one. Those data-bound designs support only that the snapshot contains dated ICU outtimes, physiology, support evidence, transfer intervals and subsequent in-hospital events. The bounded topology diagnostic in this episode supports feasibility and shows that 3,267 of 3,299 48-hour returns had an observed preceding non-ICU interval, whereas only 32 did not. It does not support a clinical association, a causal effect, a safe-discharge rule, or a claim that the unconfirmed pathway is common.

The remaining clinically important uncertainty is whether “recent support withdrawal” is one recovery state. Respiratory support withdrawal and vasoactive-support cessation represent different physiologic domains and may be discordant: a patient can have low final MAP/respiratory burden while having only recently stopped vasopressors, only recently lost respiratory support, or recently stopped both. Pooling these states can hide a clinically useful distinction and can make an association appear to be a generic discharge-process artifact.

Primary falsifiable hypothesis:

> Among adults at a first ICU outtime who have low final recorded respiratory and MAP burden with adequate, source-concordant observation, recent respiratory-support withdrawal and recent vasoactive-support withdrawal have different adjusted 48-hour cumulative incidences of first ICU return or in-hospital death, and dual recent withdrawal has a non-additive excess relative to durable recorded-off recovery. The domain pattern will be more informative for ICU return after an observed non-ICU interval than for death; the rare topology-unconfirmed return will be reported as a descriptive process/observability sensitivity, not treated as a powered effect-modifier claim.

The estimand is prognostic, not causal: adjusted absolute CIF contrasts and their uncertainty for the mutually exclusive first events at 6, 24 and 48 hours, plus the interaction contrast on the absolute-risk scale, standardized over prespecified pre-outtime covariates. The reference is durable recorded-off in both domains. The primary exposure categories are durable/durable, recent respiratory only, recent vasoactive only, recent in both, and active/residual/discordant/unobserved/inadequate-coverage categories retained for audit and secondary analysis. “Recorded-off” means absence of qualifying evidence in the locked source-specific observation/interval rules; it does not mean that support was continuously absent.

Supportive results would be a reproducible domain-specific or dual-withdrawal contrast, adequate positivity/coverage, and stable calibration and estimates across the prespecified coding/window/topology falsifications. Adverse results would be null or reversed contrasts, no interaction, a signal explained by masks or source channel, or a signal that disappears when aggregate versus topology-specific outcomes or discharge-as-competing-event handling is changed. Inconclusive results would include too few events in a domain cell, unstable or contradictory support intervals, non-positivity, broad intervals, poor topology observability, or latent-state non-identifiability. Even supportive results would establish a retrospective prognostic marker for external and clinician-adjudicated validation, not that withdrawal causes deterioration or that discharge should be delayed.

## Clinical importance and substantive advance

ICU discharge is a consequential transition under bed scarcity and limited ward monitoring. A single last MAP, oxygen value, or pooled “support present” indicator may treat distinct recovery pathways as equivalent. If only recent respiratory withdrawal is associated with post-transition return, monitoring and respiratory reassessment would be more plausible targets than treating all recent support cessation as one risk state. If vasoactive-only or dual withdrawal carries the stronger association, circulatory reserve and medication-transition review may be more relevant. If no domain distinction survives, that negative result is clinically useful: it argues against adding unsupported domain-specific complexity to discharge surveillance.

The advance is a falsifiable separation of physiologic domains at a fixed landmark with an explicit interaction and a competing-event estimand. It does not claim to solve bedside readiness. The transition-confirmed ICU-return label is used as a secondary process-sensitive outcome because it is much better supported than the unconfirmed class in the bounded diagnostic. Aggregate ICU return and death remain primary clinical outcomes; alive hospital discharge is an observed competing event rather than censoring. This avoids turning a rare or administratively uncertain topology into a stronger claim than the data can support.

## Population, landmark, temporal boundaries and joins

Use the read-only MIMIC-IV 3.1 source
`[internal dataset path]`,
[source checksum].
The catalog snapshot is `[source checksum]`.
All source members are read-only. The exact local schema records are in
`datasets/mimic/README.md`, `datasets/mimic/metadata.json`, and the table JSON files
named below.

Join `hosp/patients` to `icu/icustays` by `subject_id`, and
`hosp/admissions` to `icu/icustays`, `hosp/transfers`, and all same-admission
event tables by `subject_id,hadm_id`. Select the earliest ordered
`icu/icustays.intime` per `subject_id,hadm_id`. Include `anchor_age >= 18`, retaining
MIMIC's `anchor_age=91` representation. Require non-null
`icustays.intime < icustays.outtime < admissions.dischtime`, valid patient/admission
joins, no `admissions.deathtime <= outtime`, and an available discharge time. The
landmark is `icustays.outtime). Patients are not required to be clinically “ready”:
that concept is unavailable and must not be inferred.

Predictors use only source times in the half-open window
`[outtime-12 hours,outtime)), split into preceding and final six-hour halves. Use
`charttime` for chart observations and `starttime,endtime` for intervals. Do not use
`storetime` as clinical time; no post-outtime transfer, discharge, note, or outcome field
may enter predictors. Follow each eligible landmark to
`min(outtime+48 hours, admissions.dischtime)`.

Primary mutually exclusive first events are:

1. aggregate ICU return: a later `icu/icustays.intime > outtime` for the same
   `subject_id,hadm_id` within 48 hours;
2. in-hospital death before another event, using
   `admissions.deathtime > outtime` within 48 hours;
3. alive hospital discharge before another event, using
   `admissions.dischtime > outtime` within 48 hours.

For the topology sensitivity, split aggregate return into transition-confirmed return
when a valid `hosp/transfers` interval has `intime >= outtime`,
`outtime <= later icustays.intime), and a non-ICU `careunit`; otherwise label it
topology-unconfirmed/immediate. Define the non-ICU set from distinct non-null
`icustays.first_careunit` and `last_careunit` values in the frozen snapshot, not
string heuristics. Require transfer `intime < outtime`; preserve invalid/missing
topology as diagnostic fields. Do not label returns planned/unplanned or clinically
deteriorating. Use a locked tie rule (death, confirmed return, unconfirmed return,
alive discharge) and a timestamp-tolerance sensitivity. The primary inferential outcome
is aggregate return/death/discharge; topology-specific CIFs are secondary and the
32-case unconfirmed count from discovery is a readiness warning, not a computed
study result.

The primary analysis reports group-specific adjusted CIFs and absolute differences at
6/24/48 hours. Secondary analyses report cause-specific hazards, domain interaction
contrasts, and the topology split among returns. A discharge-as-censoring analysis is
only a sensitivity showing the estimand change and cannot replace the competing-event
analysis.

## Exact source paths, archive members and variables

- `icu/icustays`, table file
  `datasets/mimic/table-7d5c8feb0fb0dbd4.json`, archive member
  `mimic-iv-3.1/icu/icustays.csv.gz`. Columns:
  `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`.
  Use `stay_id` to assert event-feature linkage and the three identifiers to audit
  the first-stay selection.
- `hosp/admissions`, table file
  `datasets/mimic/table-e8ec3e6e4c428559.json`, archive member
  `mimic-iv-3.1/hosp/admissions.csv.gz`. Columns include
  `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admission_location,
  discharge_location,insurance,language,marital_status,race,edregtime,edouttime,
  hospital_expire_flag`. Use only pre-index admission fields as adjustment variables;
  `dischtime,deathtime` are outcomes; `discharge_location` is an outcome-process
  audit and never a predictor.
- `hosp/patients`, table file
  `datasets/mimic/table-9154f8c46cade9af.json`, archive member
  `mimic-iv-3.1/hosp/patients.csv.gz`. Columns:
  `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`. Join by
  `subject_id); use `gender,anchor_age,anchor_year_group), not `dod).
- `hosp/transfers`, table file
  `datasets/mimic/table-685b6b74d0d7c547.json`, archive member
  `mimic-iv-3.1/hosp/transfers.csv.gz`. Columns:
  `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`. Use only
  post-landmark rows for outcome topology, never predictors.
- `icu/chartevents`, table file
  `datasets/mimic/table-8208609a785ea7e8.json`, archive member
  `mimic-iv-3.1/icu/chartevents.csv.gz`. Columns:
  `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,
  valueuom,warning`. Use locked item IDs HR 220045; arterial MAP 220052; NIBP MAP
  220181; RR 220210; SpO2 220277; O2 flow 223834; FiO2 223835; PEEP 220339; and
  temperature 223761/223762. Assert all three stay identifiers match the index.
  Use `icu/d_items`, archive member `mimic-iv-3.1/icu/d_items.csv.gz`, table
  `datasets/mimic/table-d1023acc404fd1d4.json`, columns
  `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,
  highnormalvalue`, to audit labels and units.
- `icu/inputevents`, table file
  `datasets/mimic/table-d193e854c19eb4ba.json`, archive member
  `mimic-iv-3.1/icu/inputevents.csv.gz`. Columns include
  `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,
  rate,rateuom,statusdescription` and the remaining recorded order fields. Use
  norepinephrine 221906; epinephrine 221289/229617; dopamine 221662; phenylephrine
  221749/229630/229631/229632; vasopressin 222315. Construct valid overlap intervals
  from `starttime,endtime`, preserve item/unit identity, and exclude only a locked
  explicitly invalid/cancelled status rule.
- `icu/procedureevents`, table file
  `datasets/mimic/table-f6493e8403a0abe7.json`, archive member
  `mimic-iv-3.1/icu/procedureevents.csv.gz`. Columns include
  `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,statusdescription`.
  Use intubation 224385, extubation 227194 and NIV 225794 only as transition
  corroboration; never treat a short procedure row as continuous ventilation.
- `icu/outputevents`, table file
  `datasets/mimic/table-a7ad1c4cdcdbfe0a.json`, archive member
  `mimic-iv-3.1/icu/outputevents.csv.gz`. Columns
  `subject_id,hadm_id,stay_id,charttime,itemid,value,valueuom` (plus caregiver/store
  fields). Use only for a prespecified urine-output coverage/descriptive sensitivity;
  it is not a measured renal-recovery endpoint.
- `hosp/labevents`, table file
  `datasets/mimic/table-bf701d962c63287c.json`, archive member
  `mimic-iv-3.1/hosp/labevents.csv.gz`. Columns include
  `subject_id,hadm_id,itemid,charttime,valuenum,valueuom,flag`. Creatinine and
  hemoglobin may be descriptive pre-index covariates only when timing and coverage
  pass audit; no post-outtime values.
- `note/discharge`, table file
  `datasets/mimic/table-69be322e2b58015b.json`, separate source
  `[internal dataset path]`.
  Columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`.
  Exclude text from primary predictors: it can contain post-index disposition and lacks
  a validated ICU-outtime readiness label. Reserve it for future clinician adjudication.

## Exposure construction

Compute one-hour medians and masks for MAP, HR, RR, SpO2, FiO2, O2 flow and PEEP in
the 12-hour window. Keep arterial and NIBP MAP, and FiO2/O2-flow/PEEP, as separate
channels. Define a low final burden in both domains using the locked parent convention:
MAP burden and respiratory burden below one-third in the final six hours, with at least
two observed MAP bins and two respiratory bins in each half. The solver must state the
exact normalization and threshold implementation before fitting and apply it unchanged
to test data.

For the hemodynamic domain, qualifying support is a valid overlap with one of the
listed vasoactive input intervals; for the respiratory domain, qualifying recorded
support is channel-specific chart evidence and the procedure markers are transition
corroboration only. Define recent withdrawal as qualifying support evidence in the
preceding six-hour half with a recorded support-free buffer of 0 to <6 hours at outtime;
define durable recorded-off as no qualifying evidence in the final half and a valid
buffer of at least 6 hours or no qualifying evidence in the full 12 hours. Label active,
residual, discordant, unobserved and inadequate-coverage cases rather than forcing them
into the two primary states. The exposure is recorded evidence, not continuous absence
or proof of physiologic recovery.

Primary domain contrast is the five-level pattern among adequately observed low-final-
burden stays: durable/durable; recent respiratory only; recent vasoactive only; recent
in both; and an explicitly reported other/discordant category. A joint interaction
model and one-domain-at-a-time contrasts are prespecified. A parent-minimum-buffer and
6-hour versus 12-hour window sensitivity is required.

## Baseline and substantive learned/mechanistic alternative

Use patient-level 70/15/15 train/validation/test splits by `subject_id`, fixed seeds
17, 29 and 43. All item mapping, transformations, imputation, threshold selection,
model fitting and tuning are restricted to training/validation. The identical
pre-outtime predictor set is supplied to both methods: domain pattern/buffers, final and
preceding-half burdens, one-hour values/masks, channel/source flags, HR/RR/SpO2,
gender/age/year-group, ICU LOS, first/last careunit, admission type and limited
admission covariates. Do not supply outcome topology, discharge location, post-outtime
transfers, or notes.

Simple baseline: prespecified cause-specific Cox models for aggregate ICU return, death
and alive discharge with the domain-pattern terms and compact covariates; use a nested
snapshot-only model omitting support-free duration and order. Standardize predicted
cause-specific CIFs to the held-out population and report Aalen–Johansen, calibration
intercept/slope, IPCW Brier scores, absolute CIF contrasts and patient-bootstrap 95%
intervals. The baseline tests the scientific interaction directly and remains primary
if the alternative is not identifiable.

Substantive alternative: a two-domain factorized hidden semi-Markov model with separate
respiratory and hemodynamic states (durable recorded-off/low burden, recent withdrawal,
active/residual support, and unobserved/discordant), sparse transitions, explicit dwell
distributions and event-specific discrete hazards over eight six-hour intervals. Fit
emissions, transitions and hazards only on training data; select restrictions on
validation; lock test posterior state probabilities and CIFs. Report state occupancy,
dwell-time, transition, posterior entropy and event-hazard diagnostics. Its scientific
value is not a score contest: it can reveal whether the sequence and duration of the
two recovery domains identify distinct latent trajectories that a last-value or pooled
support summary loses. Retain it only if states are identifiable, diagnostics reproduce
across split seeds, and its held-out CIF calibration or domain-specific separation
meets a predeclared margin; otherwise report the transparent baseline.

The planned full study is within the solver-planning envelope of 16 CPUs, 262,144 MiB
RAM, up to 8 A100 GPUs and 28,800 seconds. Full extraction, repeated Cox/bootstrap
fits and the latent model are unmeasured estimates. The compact baseline is expected
to be CPU-suitable; the factorized latent model can begin on multicore CPU and request
one allocated A100 only if profiling shows matrix-intensive repeated fitting benefits.
No GPU is scientifically required, and no solver fit is claimed here. This episode used
the separate 7,200-second discovery budget for catalog inspection and a bounded
read-only diagnostic.

## Falsification and interpretation gates

Predeclare and report:

- shuffle hourly order within stay while preserving values and masks;
- remove masks, use masks only, remove support evidence, and remove physiology;
- substitute storetime for charttime and last-value coding for interval overlap;
- separate arterial/NIBP and FiO2/O2-flow/PEEP channels;
- remove procedure corroboration and test it only as transition evidence;
- vary the 6-hour buffer and 6/12-hour feature windows;
- compare joint versus one-domain-only patterns and the parent pooled-support exposure;
- collapse topology to aggregate ICU return, then report topology-specific estimates only
  with event counts and observability intervals;
- vary strict transfer interval bounds with a locked timestamp tolerance;
- run a negative-control pseudo-landmark before outtime;
- stratify by first/last careunit, admission type and recorded discharge pathway as
  descriptive sensitivity, never turning discharge location into a predictor;
- show alive discharge as competing event beside discharge-as-censoring sensitivity; and
- audit contradictory times, missing transfer intervals, support-channel coverage,
  item-label/unit mapping, and renal/urine-output coverage.

Supportive evidence requires adequate domain-cell positivity and observation coverage;
stable domain contrasts in aggregate competing-event estimates; no material collapse
under the order/mask/source/channel/window falsifications; and, for the secondary
topology claim, enough confirmed-return events with a clearly documented rare
unconfirmed class. A latent model must have reproducible state diagnostics and
calibrated held-out predictions. This supports a retrospective domain-specific marker
for clinician-adjudicated external validation.

Adverse evidence includes null/reversed domain contrasts, a contrast explained by
measurement masks or discharge pathway, no reproducible dual-domain interaction, poor
calibration, or latent-state non-identifiability. This would argue against using
domain-specific recorded-support patterns as evidence of distinct early failure.

Inconclusive evidence includes non-positivity, rare recent/dual cells, wide intervals,
unstable ties or topology assignment, insufficient transfer observability, or missing
death/discharge times. Report no clinical rule in these cases.

## Evidence limits and required next study

MIMIC cannot establish continuous support between observations, actual work of
breathing, true hemodynamic reserve, clinician intent, goals of care, treatment
limitations, staffing, bedside readiness, discharge rationale, planned/unplanned
return, preventability, post-discharge safety, or causal effects of stopping support.
Administrative transfers and discharge location do not adjudicate clinical deterioration.
Raw waveforms and MIMIC-CXR images are absent. A clinician-reviewed transition/readiness
endpoint, external validation, and prospective or causal study would be required before
a discharge policy, monitoring threshold, or treatment recommendation.

This is a bounded adaptation of the research-ambition examples, not a reproduction.
The dated disease-sequence example motivates ordered structured-history features, but its
UKB/Danish cohort and full external-validation claim are unavailable here. The Bayesian
latent-trajectory example motivates the EHR-only factorized hidden-state alternative,
but genetic inputs and complete reproduction dependencies are absent. The cancer
multimodal example is not pursued because the required images are unavailable and the
main paper/complete STAR Methods were not available in the reference bundle. The
MIMIC expert seed 10 is the question source, not evidence that the hypothesis is true.

Every conclusion must cite a row in `cif_domain_associations.csv`,
`calibration_brier.csv`, `state_diagnostics.csv`, `topology_coverage.csv` or
`falsification_results.csv`, quote the estimate and interval, and carry one of the
supportive/adverse/inconclusive labels. Computation can establish cohort construction,
event ordering, recorded-domain associations, calibration, uncertainty and sensitivity
consistency. It cannot establish clinical truth, causality, readiness or utility.
