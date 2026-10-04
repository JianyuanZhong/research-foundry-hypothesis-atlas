# Does sustained inspired-oxygen excess after adequate oxygenation carry different subsequent risk in acute pulmonary injury?

## Status, opening, and scientific deliverable

This is a substantive repair of `[prior hypothesis]` and a planned eICU experiment, not an executed result. It addresses a clinically consequential boundary left unresolved by conflicting trials. In a broad mechanically ventilated ICU population, conservative oxygen reduced oxygen exposure without changing ventilator-free days [K1]. In ARDS, pushing oxygen to a low target did not improve 28-day survival and generated an adverse safety signal [K2]. A recent mechanistic synthesis distinguishes inspired hyperoxia from arterial hyperoxemia and argues that mechanical stress and pre-existing lung injury may amplify oxygen toxicity, while acknowledging inconsistent clinical mortality evidence [K3].

The strongest evidence-supported claim is therefore limited: oxygen targets alter exposure; very low targets can be unsafe in ARDS; and inspired oxygen can expose lung tissue even when arterial saturation cannot quantify hyperoxemia. Existing evidence does **not** establish that excess oxygen after adequate oxygenation harms eICU patients, that any association is causal, or that pulmonary injury modifies it.

The unresolved hypothesis is: **among adult ICU patients alive and still in the ICU at 36 hours who had a PaO2 of 80–120 mm Hg paired with a valid FiO2 during hours 18–24, greater sustained FiO2 above 0.40 during oxygen-adequate hours 24–36 is associated with a larger subsequent seven-day in-hospital death cumulative incidence in a pre-exposure acute-pulmonary-injury proxy than in ICU states without a documented acute pulmonary diagnosis.** The primary estimand is the pulmonary-stratum interaction in seven-day risk difference per 0.10 increase in time-weighted excess FiO2. This is a conditional, descriptive/causal-contrast target among 36-hour survivors, not the effect of initiating oxygen at ICU admission.

The future solver must newly construct the cohort and hourly panel, fit an interpretable landmark baseline and a longitudinal joint model on identical hospital-grouped folds, estimate the interaction with uncertainty, and execute the rival-explanation and falsification tests below. Completion requires frozen cohort flow, coverage/positivity audit, balance and calibration files, primary/secondary estimates, hospital and measurement sensitivity results, and supportive/adverse/inconclusive interpretation tied to those outputs.

## Why this could change a decision

A broad average oxygen-target effect may combine patients whose injured lungs are susceptible to oxygen–ventilator interaction with patients receiving oxygen for other reasons. A credible stratum difference would justify enriching or stratifying a prospective oxygen-titration trial by **pre-exposure** acute pulmonary injury and ventilator stress. Absence of a precise difference would argue against that enrichment rule. Evidence that the signal is explained by contemporaneous deterioration, ABG sampling, ventilation intensity, or hospital charting would redirect effort from oxygen toxicity toward treatment-selection or measurement validation.

The leading explanation is a delayed oxygen–mechanical-stress interaction: once arterial oxygenation is adequate, sustained high inspired oxygen adds oxidative/alveolar injury, especially in already injured lungs. The strongest rivals are:

1. **severity/reverse causation:** clinicians raise FiO2 because deterioration has already begun;
2. **ventilator intensity:** PEEP, plateau pressure, tidal volume, or invasive ventilation causes both FiO2 choice and outcome;
3. **ABG/FiO2 measurement:** sicker patients and some hospitals measure gases and settings more often, making burden appear greater;
4. **treatment selection:** shock, procedures, or clinician concern determines oxygen and mortality;
5. **hospital practice/documentation:** local target and charting conventions generate an apparent interaction;
6. **phenotype error:** diagnosis strings plus P/F ratio are an imperfect acute-pulmonary-injury proxy, not clinical ARDS.

A toxicity-compatible pattern is a lagged dose–response after adequate saturation, stronger in the injury proxy, preserved after measured severity/ventilator/observation adjustment, and not concentrated in a few hospitals. A severity artifact should appear at or before oxygen escalation, attenuate with pre-escalation physiologic trajectories, and need not interact specifically with pre-exposure lung injury. A documentation artifact should track measurement density or hospital and fail source-removal/held-hospital checks.

## Population and immutable temporal alignment

Use each `patientunitstayid` as the index stay. Include age >=18 (map `age='> 89'` to 90 for adjustment only), first ICU stay per `patienthealthsystemstayid`, ICU admission offset 0, and `unitdischargeoffset>=2160` minutes. Exclude comfort-measures-only/end-of-life plans recorded by minute 1,440, burns, extracorporeal support if identifiable, impossible offsets, and duplicate/revised measurements after deterministic deduplication.

- **Baseline window:** minute 0 through 1,440.
- **Eligibility oxygenation window:** minute 1,080 through 1,440. Choose the last valid PaO2 80–120 mm Hg with nearest valid FiO2 within ±60 minutes; ties choose earlier FiO2. This pair is the baseline adequacy anchor.
- **Pulmonary status cutoff:** only diagnoses entered at or before minute 1,440 and the baseline pair may classify the stratum.
- **Exposure window:** minute 1,440 (inclusive) through 2,160 (exclusive).
- **Outcome time zero:** minute 2,160. Death, discharge, and all outcome measurements at or before this minute are excluded from follow-up.
- **Follow-up:** seven days, through minute 12,240, with live hospital discharge as a competing event.

This fixed double-landmark removes immortal time created by letting a future exposure duration define eligibility: everyone must already be alive and present at 36 hours before follow-up begins, and exposure length is identical. It does not remove reverse causation within hours 24–36; that is tested and adjusted explicitly. Results do not generalize to early deaths or short stays.

## Pre-exposure pulmonary strata without outcome leakage

The **acute-pulmonary-injury proxy** requires both:

1. a diagnosis/admission-diagnosis entered by minute 1,440 containing a prespecified acute term: ARDS/acute respiratory distress, pneumonia, aspiration, pulmonary edema, or acute respiratory failure; and
2. baseline PaO2/FiO2 <=300.

The primary comparison stratum is **other ICU states**: no prespecified acute pulmonary term recorded by minute 1,440, regardless of baseline P/F ratio. Patients with a pulmonary term but P/F >300 are excluded from the primary interaction and retained as a discordant sensitivity group. Chronic COPD/asthma alone does not qualify. Terms, regular expressions, and ICD mappings are frozen before outcomes are inspected.

This is not a Berlin ARDS diagnosis: eICU lacks reliable bilateral imaging adjudication and complete PEEP/timing confirmation. A blinded ICU-clinician review of a stratified sample of both algorithm-positive and algorithm-negative stays is essential before interpreting the interaction as ARDS-specific biology. Without it, the claim remains about the computable proxy.

## Exposure, outcome, and covariates

### Primary exposure

Normalize FiO2 recorded as 0.21–1.00 or 21–100%. Build 12 hourly bins in hours 24–36. In each bin, use the median FiO2 and median arterial/peripheral saturation. An hour is oxygen-adequate when SaO2/SpO2 >=94%; a paired PaO2 >=80 within ±60 minutes overrides a missing saturation. Hypoxemic hours (SpO2 <92% or PaO2 <60) do not contribute to “excess” and are separately counted as severity.

For adequate hours define `excess=(FiO2-0.40)+`. Primary exposure is the time-weighted mean excess across all 12 hours, with unobserved hours handled by the prespecified observation model rather than filled as low oxygen. Require at least six observed FiO2 hours and six adequate-status hours. For display and overlap checks only, “sustained excess” means FiO2 >0.40 in >=75% of observed adequate hours and “limited excess” means <=25%. Sensitivities use thresholds 0.30, 0.50, and 0.60; paired PaO2-area above 100 and 120 mm Hg; and FiO2-only burden. SpO2 is never treated as a measure of arterial hyperoxemia.

### Outcome

Primary outcome is seven-day in-hospital death after minute 2,160, using `hospitaldischargestatus` with `hospitaldischargeoffset`; live hospital discharge is competing. Report stratum-specific Aalen–Johansen risks and standardized risk differences. Secondary outcomes are ICU death, hospital death by discharge, and respiratory deterioration from hours 36–72 (new/increased invasive ventilation plus >=0.20 FiO2 rise, reported only after a coverage audit). Do not use `actualventdays` as a timestamped endpoint.

### Covariates known by the relevant decision time

At baseline: age, sex, ethnicity, admission source/type, unit type, hospital region/size/teaching status; APACHE IV score and predicted mortality; acute physiology variables; baseline PaO2, FiO2, P/F, pH, PaCO2, lactate, creatinine, bilirubin, platelets, WBC; vasopressor exposure; invasive ventilation; PEEP, plateau pressure, set/observed tidal volume, ventilator rate; SaO2; chronic lung/cardiac disease; sepsis, trauma, postoperative and neurologic diagnoses; and end-of-life indicators.

Hourly in exposure window: FiO2, SaO2, PaO2/PaCO2/pH when drawn, PEEP, plateau pressure, tidal volume, respiratory/ventilator rate, mean arterial pressure, heart rate, vasopressor receipt, and explicit missingness/source indicators. No values after minute 2,160 enter exposure, strata, weights, or covariates.

## Exact read-only eICU bindings

All source files are ordinary gzip-compressed CSVs under
`[internal dataset path]`.
All derived files go under `work/`; source bytes remain read-only.

- `patient.csv.gz` / table `patient`: `patientunitstayid` primary join key; `patienthealthsystemstayid` and `unitvisitnumber` for first-stay selection; `uniquepid` for patient-grouping; `hospitalid`; `age`, `gender`, `ethnicity`, `apacheadmissiondx`, admission fields; `unitdischargeoffset/status/location` and `hospitaldischargeoffset/status/location` for landmarks, events, and competing discharge.
- `lab.csv.gz` / `lab`: `patientunitstayid`; event time `labresultoffset` (not revision time); `labresultrevisedoffset` for deduplication; `labname`, `labresult`, `labresulttext`, units. Verified labels include `paO2`, `paCO2`, `FiO2`, `O2 Sat (%)`, `PEEP`, and routine severity labs.
- `respiratoryCharting.csv.gz` / `respiratoryCharting`: `patientunitstayid`; event time `respchartoffset`, entry time `respchartentryoffset`; `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`. Verified labels include `FiO2`, `FIO2 (%)`, `Set Fraction of Inspired Oxygen (FIO2)`, `SaO2`, `PEEP`, `PEEP/CPAP`, `Plateau Pressure`, `Tidal Volume (set)`, `Tidal Volume Observed (VT)`, `Mean Airway Pressure`, and `Vent Rate`.
- `respiratoryCare.csv.gz` / `respiratoryCare`: `patientunitstayid`; `respcarestatusoffset`, `ventstartoffset`, `ventendoffset`, prior vent offsets, `airwaytype`, `setapneafio2` for ventilation corroboration.
- `vitalPeriodic.csv.gz` / `vitalPeriodic`: `patientunitstayid`; `observationoffset`; `sao2`, `heartrate`, `respiration`, `systemicmean` and other invasive pressures. Use bounded selected-column reads.
- `diagnosis.csv.gz` / `diagnosis`: `patientunitstayid`; `diagnosisoffset`; `diagnosisstring`, `icd9code`, `diagnosispriority`, `activeupondischarge`. Outcome-blind pre-24-hour pulmonary and comorbidity mapping.
- `admissionDx.csv.gz` / `admissionDx`: `patientunitstayid`; `admitdxenteredoffset`; `admitdxpath`, `admitdxname`, `admitdxtext`.
- `apacheApsVar.csv.gz` / `apacheApsVar`: `patientunitstayid`; `intubated`, `vent`, physiology and admission `pao2`/`fio2`. These untimed summary fields are baseline covariates only, never exposure.
- `apachePatientResult.csv.gz` / `apachePatientResult`: `patientunitstayid`; `acutephysiologyscore`, `apachescore`, `apacheversion`, predicted mortality/LOS. Deduplicate versions deterministically; actual mortality/LOS/ventilation are outcomes or audit fields, never predictors.
- `apachePredVar.csv.gz` / `apachePredVar`: `patientunitstayid`; admission severity/comorbidity, `ventday1`, `day1pao2`, `day1fio2`. Baseline sensitivity only.
- `infusionDrug.csv.gz` / `infusionDrug`: `patientunitstayid`; `infusionoffset`; `drugname`, `drugrate`, `infusionrate`, `patientweight` for prespecified vasoactive-agent indicators; units are not harmonized into dose without a separate audit.
- `carePlanGeneral.csv.gz` / `carePlanGeneral`: `patientunitstayid`, `cplitemoffset`, `cplgroup`, `cplitemvalue`, `activeupondischarge`; and `carePlanEOL.csv.gz` / `carePlanEOL`: `patientunitstayid`, `cpleolsaveoffset`, `cpleoldiscussionoffset`, `activeupondischarge` for pre-landmark treatment-limitation exclusions.
- `hospital.csv.gz` / `hospital`: join `patient.hospitalid=hospital.hospitalid`; `numbedscategory`, `teachingstatus`, `region`.

All clinical streams join by `patientunitstayid`; never join physiologic rows on `uniquepid` alone. Offset units are minutes relative to ICU admission. Preserve event and entry/revision clocks separately to test delayed documentation.

## Bounded source audit already completed

The audit is support evidence, not a hypothesis result. The snapshot contains 200,859 stays at 208 hospitals. It found 420,762 `paO2` rows in 85,769 stays; 3,075,308 respiratory-charting `FiO2` rows plus 360,107 lab `FiO2` rows; 1,464,808 `PEEP` rows; and 372,398 `Plateau Pressure` rows. Acute-term support before hour 24 includes 10,397 ARDS, 19,154 pneumonia, 614 aspiration, 2,420 pulmonary-edema, and 30,130 respiratory-failure stays, with overlap.

A deliberately narrow probe requiring adult status, ICU presence to hour 36, a PaO2 80–120 during hours 18–24, and FiO2 within ±60 minutes found 2,280 stays across 124 hospitals. The pulmonary-injury proxy contained 993; 1,166 had no pre-24-hour acute pulmonary term; the remainder were discordant. A coarse FiO2-only exposure check found injury-proxy sustained/limited cells of 217/207 and no-pulmonary-diagnosis cells of 166/311 across 51/46 and 49/52 hospitals, respectively. These are upper-bound support counts because the final saturation-conditioned exposure and exclusions were not executed. Only three hospitals had >=10 observations in both extreme cells, motivating partial pooling rather than hospital fixed effects. The solver must stop before outcome modeling if either primary stratum has <150 analyzable stays, <40 deaths, effective sample size <100 after weighting, or exposure overlap below 5% in any prespecified propensity decile.

## Matched method comparison

### B0: interpretable landmark baseline

On the frozen hospital-grouped folds, fit a cause-specific discrete-time model for death and live discharge with restricted cubic spline for continuous excess FiO2, pulmonary stratum, their interaction, baseline covariates, summaries of hour-24–36 physiologic slopes, ventilator intensity, hypoxemic hours, ABG/FiO2/SaO2 counts, source indicators, and a hospital random intercept. Use doubly robust standardized risks: cross-fitted generalized propensity density for exposure plus outcome regression, truncating weights at prespecified 1st/99th percentiles. Report unadjusted Aalen–Johansen risks, adjusted seven-day risks, risk differences per 0.10 excess, interaction contrast, cluster bootstrap CIs by hospital, E-values only as sensitivity descriptors, and overlap/balance diagnostics.

B0 is selected as the primary analysis because coefficients, temporal alignment, and standardized risks are auditable. It loses within-window ordering: the same average FiO2 can reflect high oxygen before recovery, after recovery, or during worsening, and summaries cannot jointly represent treatment, physiology, and measurement processes.

### L1: substantive longitudinal alternative

Fit a Bayesian or neural state-space sequential g-computation model on the **same hourly variables, cohort, folds, and endpoint**. A latent respiratory-severity state emits SaO2/PaO2, PEEP, plateau pressure, tidal volume, and hemodynamics; separate heads model next-hour FiO2 treatment and whether an ABG/FiO2 measurement is recorded; an accumulated oxygen–mechanical-stress term `sum excess_FiO2 × standardized_plateau_or_PEEP` enters only lagged future state transitions and death hazard. Hospital receives a hierarchical documentation/treatment intercept, not a free patient-outcome shortcut. Fit outcome-blind state/treatment/measurement components on training folds, then the event head; use posterior predictive checks and held-hospital calibration.

Estimate standardized seven-day risk under observed treatment and a bounded regime that caps FiO2 at 0.40 **only in hours with adequate oxygenation**, leaving hypoxemic hours unchanged. Report this as model-based g-computation under sequential exchangeability, consistency, and positivity—not as an identified trial effect. Compare the stratum-specific risk contrast and lagged oxygen–ventilator interaction with B0. L1 is scientifically useful only if it improves held-hospital next-hour physiology and observation calibration, separates same-hour deterioration from delayed burden, and preserves overlap. It is not selected for a small AUROC gain.

### Identical splits and evaluation

Freeze five folds grouped by `hospitalid`, balancing hospital size, region, and outcome without splitting hospitals or `uniquepid`. Every fit, hyperparameter choice, threshold sensitivity, and calibration uses the same folds. Primary uncertainty is the hospital-cluster bootstrap for B0 and hospital-stratified posterior/ensemble intervals for L1. Evaluate held-fold event calibration, Brier score, integrated calibration index, ABG/FiO2 observation calibration, next-hour PaO2/SaO2 error, propensity overlap, effective sample size, and the primary interaction estimate. Do not choose a model by discrimination alone.

Estimated future-solver budget: extraction and panel construction 1–2 hours on 8–16 CPU cores and 64–128 GiB; B0 and 500 hospital bootstraps 1–3 hours on 16 CPUs; L1 1–3 hours on one allocated A100 80 GB (or 4–8 CPU hours if implemented as a Bayesian state-space model), plus sensitivity fits, all within the configured 16-CPU/8-GPU/262-GiB/8-hour planning envelope. These are unverified planning estimates; the only measured timings were bounded CPU source scans (about 15–93 seconds).

## Rival-explanation and falsification matrix

1. **Severity/reverse causation:** compare same-hour, 1–3-hour lagged, and 4–12-hour lagged associations; include pre-FiO2 PaO2/SaO2, pressure, hemodynamic slopes and hypoxemic hours. A signal beginning before or at escalation, with no delayed residual, favors severity.
2. **Ventilator intensity:** add PEEP, plateau, tidal volume and invasive-ventilation status; test excess-FiO2 × mechanical-stress interaction and repeat among invasively ventilated stays. If FiO2 loses association but pressure burden remains, oxygen-specific toxicity is not supported.
3. **ABG/FiO2 sampling:** model hourly observation hazards; inverse-intensity sensitivity; restrict to hospitals with >=70% required-hour coverage; downsample dense sites; compare PaO2-based and FiO2-based burden. An effect proportional to measurement count or removed by observation weighting supports sampling bias.
4. **Treatment selection:** report propensity overlap and balance; stratify by baseline P/F, shock/vasopressors, postoperative, neurologic, and sepsis status; exclude peri-intubation/procedural escalation hours. Non-overlap makes the result inconclusive, not causal.
5. **Hospital practice/documentation:** hierarchical hospital effects; leave-one-region-out and leave-highest-volume-hospitals-out fits; label-source removal; event-versus-entry-time sensitivity; between-hospital FiO2 and ABG-rate variance. A signal confined to a few sites or source conventions is adverse.
6. **Phenotype validity:** discordant group analysis, term-family removal, strict ARDS-only proxy, P/F thresholds 200/300, and blinded clinician review sample. Differential misclassification can invalidate the biological interaction even when computation is correct.
7. **Negative temporal control:** hour-24–36 oxygen burden must not predict a pre-exposure deterioration indicator defined entirely in hours 12–18 after baseline adjustment. Such an association indicates residual severity/documentation structure.
8. **Negative exposure control:** LPM O2 or documentation-entry delay, conditioned on actual FiO2, should not reproduce the pulmonary interaction. Replication indicates charting practice rather than oxygen dose.

No exploratory subgroup becomes confirmatory. Threshold alternatives and discordant phenotypes are reported together with multiplicity-aware intervals.

## Decision and falsification rules

**Supportive:** both B0 and an admissible L1 estimate a positive pulmonary-stratum interaction in seven-day risk, 95% intervals exclude zero (or posterior probability >0.975 under a prespecified weak prior), exposure overlap/ESS and calibration gates pass, delayed rather than pre-escalation patterns predominate, and hospital/source/observation sensitivities retain direction. This supports trial enrichment and a prospective validation study; it does not prove oxygen toxicity.

**Adverse:** a precise interaction interval excludes the prespecified clinically consequential +3 percentage-point differential risk per 0.10 excess; the association is equal or larger in other ICU states; the direction reverses; only contemporaneous/pre-exposure deterioration is present; ventilator burden explains it; or hospital/measurement controls abolish it. This argues against the proposed pulmonary-specific excess-oxygen explanation or against this phenotype.

**Inconclusive:** wide intervals include both 0 and +3 points; positivity/ESS fails; fewer than 40 deaths per stratum; exposure or pulmonary-label review performs poorly; B0 and admissible L1 materially disagree; or results depend on a few hospitals. An imprecise null is not refutation.

Continue to a prospective multicenter target trial only after supportive results plus clinical phenotype review. Revise toward measurement-validation work if observation/hospital controls dominate. Defer if overlap or event gates fail. Abandon the specific enrichment hypothesis after a precise adverse result replicated across methods.

## Claims and limits

Computationally checkable claims are cohort counts, temporal ordering, exposure construction, balance/positivity, measurement coverage, model calibration, standardized associations, interaction estimates, sensitivity results, and whether the submitted interpretation matches those outputs. An automatic verifier can test code, clocks, hashes, estimands, uncertainty, and conclusion logic.

Clinical adjudication is required to establish acute lung injury/ARDS, appropriateness of an FiO2 setting, treatment limitation, and whether post-landmark deterioration is biological rather than documentation. No eICU analysis can measure oxidative tissue injury or all clinician intent. Causal oxygen-target recommendations require stronger exchangeability evidence and preferably a prospective randomized study. External transport requires another dataset or trial.

## Alternatives considered and revisit conditions

A single maximum PaO2 exposure was rejected because it conflates sampling with burden and misses inspired hyperoxia [K3]. A simple mortality predictor was rejected because predictive utility does not answer the exposure-heterogeneity question. Hospital preference as an instrument was deferred because exclusion and monotonicity are implausible and documentation practice violates the instrument story. A marginal structural model with fully hourly treatment remains a useful extension if the final panel has adequate sequential positivity; otherwise it would manufacture precision. L1 is retained because ordering and explicit treatment/measurement processes can distinguish toxicity-compatible lag from severity and charting rivals that B0 summaries lose. Revisit an image-validated ARDS analysis only if chest-radiograph evidence and clinician adjudication become available.

## Compact bibliography

[K1] ICU-ROX Investigators and ANZICS Clinical Trials Group; Mackle D, Bellomo R, Bailey M, et al. *Conservative Oxygen Therapy during Mechanical Ventilation in the ICU.* N Engl J Med. 2020;382:989–998. doi:10.1056/NEJMoa1903297. Abstract inspected.

[K2] Barrot L, Asfar P, Mauny F, et al.; LOCO2 Investigators and REVA Research Network. *Liberal or Conservative Oxygen Therapy for Acute Respiratory Distress Syndrome.* N Engl J Med. 2020;382:999–1008. doi:10.1056/NEJMoa1916431. Abstract inspected.

[K3] Nadeau EE, Schwingshackl A, Sturgill JL, Waters CM. *Bench evidence, bedside uncertainty: hyperoxia, mechanical ventilation and lung injury.* Eur Respir Rev. 2026;35:260058. doi:10.1183/16000617.0058-2026. Version-of-record XML sections inspected.
