# Prompt FiO2 de-escalation after sustained high SpO2 in invasively ventilated adults: a multicenter eICU target-trial emulation

## Decision, question, and falsifiable hypothesis

**Clinical decision:** When an invasively ventilated adult has sustained near-maximal pulse-oximeter saturation while receiving FiO2 >=0.50, should the bedside team reduce FiO2 promptly or leave it unchanged?

**Unresolved hypothesis:** Among invasively ventilated adults who, during the first 48 ICU hours, have a current FiO2 of 0.50-1.00 and sustained SpO2 >=98%, an absolute FiO2 reduction of at least 0.10 within 60 minutes, versus no material FiO2 change, will reduce subsequent six-hour excess-oxygen exposure **without increasing the risk of sustained hypoxemia by more than 5 percentage points**.

This is a joint benefit/safety hypothesis. It is falsified as a clinically useful strategy if oxygen exposure is not reduced, if the adjusted upper confidence limit for excess sustained-hypoxemia risk is >=5 percentage points, or if overlap, measurement, or falsification checks prevent a credible contrast. A null or adverse finding is clinically valuable: it would argue against an indiscriminate FiO2-down alert in this population.

## Why this matters and what is genuinely new

Oxygen is immediately actionable, but SpO2 near the plateau of the oxyhemoglobin curve poorly distinguishes adequate oxygenation from arterial hyperoxemia. An inspected prospective study of 400 invasively ventilated adults found 1,669/4,631 (36.0%) observations had SpO2 >98%, yet only 398/1,669 (23.8%) were followed by FiO2 reduction within one hour (Chandrakar et al., 2025, DOI 10.4103/joacp.joacp_199_24). An inspected 2026 single-center retrospective study of 21,406 ICU adults reported that SpO2 >=98% was consistently associated with PaO2-defined hyperoxemia and that higher FiO2 increased its probability, with modification by pH and respiratory-failure severity (Delgado et al., DOI 10.3390/antiox15020235). These facts support clinical equipoise and the choice of an enriched decision state; they do **not** show that prompt FiO2 reduction is safe or improves outcomes.

The substantive advance is to estimate the response to a specific bedside action at a reproducible decision point across many hospitals, rather than re-associate average SpO2 or PaO2 with mortality or compare broad oxygen targets. It directly tests whether a high-FiO2/high-SpO2 state can identify an actionable group in whom oxygen can be reduced without a short-term hypoxemic penalty. A supportive result would justify a prospective alert or closed-loop titration trial; it would not by itself justify practice change.

## Strongest supported claim versus claim under test

**Supported now:** eICU contains dense, ICU-relative FiO2 and SpO2 measurements with enough candidate decisions and both observed action groups to compute this experiment. External observational evidence supports that high SpO2/high FiO2 often represents avoidable oxygen exposure and that clinicians frequently do not reduce FiO2.

**Not yet supported and tested here:** Prompt reduction itself causes lower oxygen exposure without clinically important additional hypoxemia in otherwise comparable patients.

**Not testable here:** Whether this strategy reduces lung injury, mortality, cognitive injury, or long-term disability; whether an automated alert is safe; and whether an individual patient should be titrated. Those require prospective randomization, richer indication and signal-quality data, and clinical oversight.

## Target-trial specification

### Population and time boundaries

Unit is the ICU stay, with one index event per `patientunitstayid`. Include:

1. age >=18 years from `patient.age` (map `> 89` to 90 for adjustment and report it separately);
2. first qualifying event from ICU minute 0 through 2,880;
3. invasive airway at the event: the latest nonblank `respiratoryCare.airwaytype` in the preceding 1,440 minutes is one of `Oral ETT`, `Nasal ETT`, `Tracheostomy`, `Double-Lumen Tube`, or `Cricothyrotomy`;
4. baseline FiO2 (F0) 0.50-1.00 from exact respiratory-chart label `FiO2`; numeric values >1 are divided by 100 and only normalized values 0.21-1.00 retained;
5. at least three valid `vitalPeriodic.sao2` observations (50-100%) in [t0-30,t0], with median >=98% and minimum >=96%;
6. an ascertainment FiO2 record in [t0+45,t0+75] and continued ICU presence at t0+75.

`t0` is the first qualifying FiO2 chart time, not ICU admission or first intubation. The exposure landmark is t0+60 minutes. If several FiO2 values occur in the landmark window, select the one nearest t0+60 (earlier wins an exact tie). Outcomes begin at the landmark, eliminating overlap between exposure ascertainment and outcome follow-up. The estimand is consequently conditional on survival, ICU presence, invasive-airway confirmation, and FiO2 ascertainment through the landmark; it is not an admission-level intention-to-treat effect.

Primary analysis groups:

- **Prompt decrease:** landmark FiO2 <= F0-0.10.
- **No material change:** absolute landmark FiO2-F0 difference <0.05.
- Exclude from the primary contrast intermediate reductions, increases, and unobserved landmark settings, but enumerate them in the flow diagram. Sensitivities use >=0.05 reduction, a 30-minute landmark, and exact baseline FiO2 strata.

Do not exclude diagnoses by unvalidated free-text rules in the primary cohort. Prespecified sensitivity exclusions based on `admissionDx` and pre-t0 `diagnosis` strings will target cardiac arrest, carbon-monoxide poisoning, decompression illness, and organ-donation care, but must be clinician-adjudicated before interpretation.

### Estimands and outcomes

**Primary safety estimand:** adjusted marginal risk difference (prompt minus unchanged) for any sustained hypoxemia during minutes 60-420 after t0. Sustained hypoxemia is at least two successive valid five-minute summary observations with `sao2 <90`, no more than 10 minutes apart. The noninferiority margin is +5 percentage points. Also report risk ratio and number needed to harm with 95% confidence intervals.

**Co-primary exposure estimand:** adjusted mean difference in six-hour FiO2 area under the curve above 0.40, using a step function over respiratory-chart FiO2 settings from minutes 60-420. Carry a setting forward for at most 120 minutes; beyond that the interval is missing. Report hours at FiO2 >=0.60 as a directly interpretable companion.

**Secondary physiologic outcomes:** time-weighted proportion of valid SpO2 values <90, proportion >=98, minimum SpO2, and rescue escalation (FiO2 increase >=0.10 above the landmark value within six hours). Exploratory, explicitly noncausal outcomes are `actualhospitalmortality`, `hospitaldischargestatus`, `actualventdays`, and ICU length of stay. They are not primary because a one-hour action contrast is too confounded and eICU lacks the adjudication needed to attribute these downstream events.

Outcome completeness requires at least 36 valid SpO2 summaries (50% of expected six-hour five-minute bins); report results across >=25%, >=50%, and >=75% thresholds. Do not impute primary outcomes. Extubation, death, or discharge during follow-up is reported as a competing event. A sensitivity composite counts death before t0+420 as adverse; a separate sensitivity censors at documented loss of invasive airway. Conditioning on post-exposure extubation is not the primary analysis.

### Covariates, baselines, and analysis

All adjustment variables must be known at or before t0:

- F0; preceding 30-minute SpO2 median, minimum, slope, and variability;
- nearest preceding two-hour ventilator settings from exact labels `PEEP`, `Vent Rate`, `Tidal Volume (set)`, and `Plateau Pressure`;
- two-hour summaries of heart rate, respiration, systemic mean pressure, and noninvasive mean pressure;
- nearest preceding two-hour `labname` values `pH`, `paO2`, and `FiO2`, with explicit missingness flags;
- contemporaneous vasopressor presence from `infusionDrug.drugname` containing norepinephrine, epinephrine, phenylephrine, vasopressin, or dopamine and last rate at/before t0;
- time since ICU admission, local clock hour reconstructed from `unitadmittime24` plus offset, age, sex, ethnicity, admission weight, unit type/source, `apacheadmissiondx`, hospital, teaching status, region, and bed-count category.

Do not adjust for APACHE fields derived over the first ICU day in the primary model because they can include post-t0 physiology.

Report three baselines: crude group contrast; exact-stratified contrast within common F0 values (0.50, 0.60, 0.70, 0.80, 0.90, 1.00) and hospital; and the prespecified doubly robust estimate. For the latter, estimate propensity and outcome nuisance functions with five-fold cross-fitting grouped by hospital, using penalized logistic/generalized additive models with nonlinear continuous terms. Use AIPW after restricting to propensity 0.05-0.95; report the target population removed by trimming. Missing baseline covariates use hospital median plus missing indicator; compare with multiple imputation and complete cases.

Use 1,000 hospital-cluster bootstrap replicates for 95% confidence intervals, retaining all stays from each sampled hospital. Report balance as standardized differences before/after weighting, effective sample size, propensity distributions, weight tails, and arm-specific event counts. Test treatment heterogeneity only as prespecified interactions for F0 (0.50-0.60 vs >=0.70), PaO2/FiO2 category when a pre-t0 ABG exists, and vasopressor use; label these exploratory and give interaction intervals.

## Falsification and decision rules

A **supportive** result requires both: (a) the upper 95% CI for the adjusted sustained-hypoxemia risk difference is <+5 percentage points, and (b) the upper 95% CI for the adjusted FiO2-excess AUC difference is <0. It supports prospective testing of a prompt-decrease protocol in the measured overlap population, not causal safety in all ventilated adults.

An **adverse** result is a clearly higher hypoxemia risk (especially a CI entirely above +5 points), more rescue escalation, or no reduction in oxygen exposure. It argues against the proposed trigger or reduction size; it does not prove all conservative oxygen strategies are harmful.

An **inconclusive** result occurs if either co-primary interval crosses its decision boundary; there are <100 patients or <20 events in either arm after overlap restriction; >10% of otherwise eligible assigned patients are propensity-trimmed; post-weight absolute standardized differences exceed 0.10; effective sample size is <50% of the retained sample; >5% of weights require clipping above 20; fewer than 50% have adequate SpO2 outcome coverage in either arm; or conclusions change direction under the 25/50/75% coverage analyses.

Required falsification checks:

1. Re-run the treatment model against pre-t0 sustained hypoxemia in [t0-360,t0-60]. A non-null adjusted association of similar magnitude to the claimed post-treatment effect indicates unresolved confounding.
2. Show weighted SpO2 and FiO2 trajectories from t0-30 through the landmark; material pre-action divergence or residual F0 imbalance invalidates a causal reading.
3. Use a pseudo-exposure defined by the next FiO2 change after the six-hour outcome window; association with the already-completed primary outcome indicates selection/coding bias.
4. Repeat within exact F0 strata, within hospitals supporting both actions, leave-one-hospital-out, with a 30-minute landmark, and after excluding peri-extubation trajectories. A claim that depends on one hospital, one F0 level, or one charting rule is inconclusive.
5. Validate FiO2 normalization by tabulating raw strings and rejecting impossible normalized values; validate that airway status remains plausible in a stratified manual review.

## Exact eICU data binding

All joins use `patientunitstayid`; `patienthealthsystemstayid` and `uniquepid` identify repeated stays/people for flow counts and dependence checks. All offsets are minutes relative to ICU admission. Each source is a gzip-compressed ordinary CSV file (catalog archive member: `ordinary file`) and remains read-only.

| Table | Exact source path | Required columns and use |
|---|---|---|
| `patient` | `[internal dataset path]` | `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `age`, `gender`, `ethnicity`, `hospitalid`, `apacheadmissiondx`, `admissionweight`, `unitadmittime24`, `unitadmitsource`, `unittype`, `unitvisitnumber`, `unitdischargeoffset`, `hospitaldischargestatus` |
| `respiratoryCharting` | `[internal dataset path]` | `respchartid`, key, `respchartoffset` (clinical time), `respchartentryoffset` (documentation time), `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`; exposure, FiO2 AUC, ventilator covariates |
| `respiratoryCare` | `[internal dataset path]` | `respcareid`, key, `respcarestatusoffset`, `airwaytype`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`; invasive-airway confirmation and sensitivity timing |
| `vitalPeriodic` | `[internal dataset path]` | `vitalperiodicid`, key, `observationoffset`, `sao2`, `heartrate`, `respiration`, `systemicmean`; eligibility, confounders, outcomes. These are five-minute summaries, not raw waveforms. |
| `vitalAperiodic` | `[internal dataset path]` | key, `observationoffset`, `noninvasivemean`; pre-t0 hemodynamics |
| `lab` | `[internal dataset path]` | `labid`, key, `labresultoffset` (specimen/result time used), `labresultrevisedoffset`, `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`; pH/PaO2/FiO2 effect modification and sensitivity |
| `infusionDrug` | `[internal dataset path]` | `infusiondrugid`, key, `infusionoffset`, `drugname`, `drugrate`, `infusionrate`; vasoactive support |
| `hospital` | `[internal dataset path]` | join `patient.hospitalid=hospital.hospitalid`; `numbedscategory`, `teachingstatus`, `region` |
| `admissionDx` / `diagnosis` | corresponding `admissionDx.csv.gz` / `diagnosis.csv.gz` in the same directory | key; `admitdxenteredoffset`, `admitdxname`, `admitdxtext`; and `diagnosisoffset`, `diagnosisstring`, `icd9code`; clinician-adjudicated sensitivity exclusions only |
| `apachePatientResult` | `[internal dataset path]` | key, `actualhospitalmortality`, `actualicumortality`, `actualventdays`, `actualiculos`; exploratory outcomes only |

## Verified row-level feasibility and actual filtering

Catalog schemas, source headers, and rows were inspected. The exact `FiO2` label has 3,075,308 rows across 75,234 stays; `vitalPeriodic.sao2` has valid values in 189,609 stays, with 73,190 stays overlapping exact-label FiO2. In ICU minutes 0-2,880, 27,767 stays had at least one FiO2 0.50-1.00 record with >=3 preceding valid SpO2 observations and median SpO2 >=98% (the first broad screen did not yet impose airway status or minimum SpO2). Verified respiratory covariate labels include `PEEP` (1,464,808 rows/45,541 stays), `Vent Rate` (1,128,156/39,057), `Tidal Volume (set)` (1,034,549/37,448), and `Plateau Pressure` (372,398/23,390). Exact lab labels `paO2`, `pH`, and `FiO2` have 420,762, 413,071, and 360,107 rows, respectively.

A stricter reproducibility screen applying first event, minimum pre-SpO2 >=96%, recent explicit invasive-airway status, and the landmark rules yielded 2,662 candidate stays: 331 prompt decreases, 613 no-material-change comparators, 10 intermediate/increase records, and 1,708 without landmark FiO2 ascertainment. Of the 944 primary-arm stays, 908 (96.2%) had at least 36 valid six-hour SpO2 summaries. Baseline FiO2 was imbalanced (median 0.80 prompt vs 0.60 unchanged), but both actions occurred at common exact values: at F0 0.50 (65/186), 0.60 (60/206), 0.70 (18/24), 0.80 (38/25), 0.90 (10/8), and 1.00 (134/150), prompt/unchanged. This supports computation but makes exact F0 control and overlap diagnostics mandatory. Counts are feasibility results, not study outcomes.

Feasibility code and outputs: `oxygen_feasibility.py`, `oxygen_feasibility.json`, `oxygen_arm_feasibility.py`, and `oxygen_arm_feasibility.json`. Actual cohort compilation must emit a CONSORT-style flow and hashes; no unreported sampling is permitted.

## Causal and clinical limits

Treatment is not randomized. Clinicians may reduce FiO2 because of unrecorded trajectory, perfusion, secretions, procedures, or anticipated extubation; they may retain it because of instability. Pulse oximetry can be biased by perfusion, motion, dyshemoglobinemia, and skin pigmentation; eICU has five-minute summaries but no waveform quality, device metadata, or reliable narrative notes. FiO2 entries may be intermittent, copied, or documentation-delayed, and the strict landmark creates a selected charting population. The 1,708/2,662 candidates without a landmark setting make that selection especially important. Hospital practice and respiratory-chart coverage are heterogeneous. PaO2 is intermittent, and matched ABG physiology is unavailable for many decisions.

Clinical review is essential to adjudicate whether airway histories represent ongoing invasive ventilation, whether reductions are true titration rather than peri-extubation charting, and whether special indications for high oxygen were present. An automatic verifier can check cohort logic, offsets, normalization, joins, outcomes, estimates, intervals, balance, and whether the written conclusion obeys the prespecified result category. It cannot establish indication validity, pulse-oximeter accuracy, absence of unmeasured confounding, individual safety, or clinical benefit.

A stronger causal conclusion requires a prospective multicenter randomized trial of the trigger and decrement, with explicit oxygen indications, device and waveform quality, protocol adherence, adverse-event adjudication, and patient-centered outcomes. Mortality or organ-protection claims require a separately powered study.
