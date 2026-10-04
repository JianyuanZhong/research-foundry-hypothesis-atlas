# Candidate: A transportable, time-safe test of pH-conditioned hidden hyperoxemia

## Unresolved question and clinical advance

At a monitor SpO2 of 96–97%, clinicians may assume that arterial oxygen tension is not markedly excessive. Acid-base state can shift the hemoglobin saturation–PaO2 relation, but the clinically important unresolved claim is whether this creates a large, reproducible blind spot across heterogeneous ICUs. If it does, a prospective study could test selective repeat blood gases for acidemic patients; if it does not, a pH-conditioned warning would add complexity without reliable physiologic value.

**Primary falsifiable hypothesis:** in adults with a qualifying invasive-airway episode and a time-linked EICU blood-gas/monitoring observation during the first 72 ICU hours with SpO2 96–97%, the marginal standardized probability of PaO2 >120 mm Hg is at least 10 percentage points higher for pH <7.35 than for pH 7.35–7.45. The contrast must be positive in at least 70% of adequately supported hospitals. The estimand is an association between contemporaneously recorded measurements, not an effect of changing pH or FiO2.

The substantive advance over the existing lineage is a final, time-safe transportability protocol: it separates the pooled physiologic contrast from site-agnostic held-out prediction, uses only source-observed fields, freezes duplicate/revision and open-ended ventilation semantics, and makes the evidence required for any bedside rule explicit. It does not test oxygen toxicity, tissue hyperoxia, benefit from lowering FiO2, or patient outcomes.

## What evidence supports and what remains untested

The inherited evidence audit records an inspected full-text Europe PMC XML for Delgado et al. (Antioxidants 2026, DOI 10.3390/antiox15020235), a large single-center concurrent measurement study. It supports that SpO2 ≥98% often accompanies elevated PaO2, that SpO2 96–97% is generally more physiologic, and that pH and FiO2 modify the relationship. It does not support a +10-point acidemia contrast in EICU or transportability across hospitals. Evidence about oxygen-target strategies does not turn this measurement association into treatment evidence.

Thus the strongest supported claim is a single-center, same-time association with physiologic effect modification. This experiment tests the unresolved multi-hospital claim under EICU’s coarser monitoring and charting system. A recent-pH rule that could be used before obtaining a gas is a separate hypothesis and is not promoted here because the audited prior-pH sample is small.

## Population and time-safe construction

Use EICU snapshot `[source checksum]`. All source members are ordinary read-only `.csv.gz` files under `[internal dataset path]`; there is no archive member.

1. From `patient.csv.gz`, retain adults with numeric age ≥18; map `> 89` to 90 only for adjustment and report that category separately. Within each `patienthealthsystemstayid`, retain `unitvisitnumber=1`. Do not call this a first lifetime admission. Retain repeated health-system encounters and cluster inference by `uniquepid`. Require nonmissing `unitdischargeoffset` and keep candidate draws in [0, 4320] minutes and no later than that offset.
2. From `lab.csv.gz`, identify candidate draw times where `labtypeid=7` and `labname='paO2'` and `labname='pH'` occur at the same `patientunitstayid + labresultoffset`. Values must be PaO2 20–760 and pH 6.80–7.80. For each stay/name/draw, retain the greatest numeric `labresultrevisedoffset`, breaking an exact tie with greatest `labid`; if the retained revision still has multiple distinct in-range values, exclude that analyte/panel. Pivot only exact-offset pairs. Pair unambiguous type-7 `paCO2` (10–150) at the same offset when available; do not require it and use a missing indicator. The release has no specimen identifier, so this is a panel proxy, not proof of one arterial specimen.
3. Require one `respiratoryCare.csv.gz` row whose exact `airwaytype` is Oral ETT, Nasal ETT, Tracheostomy, Double-Lumen Tube, or Cricothyrotomy, with `ventstartoffset <= draw` and either (a) `ventendoffset > ventstartoffset` and `draw <= ventendoffset`, or (b) `ventendoffset=0` and `draw <= respcarestatusoffset`. This status-bounded interpretation of zero is frozen; it is not adjudicated ventilation truth. Do not use untimestamped APACHE ventilation flags for primary eligibility.
4. From `respiratoryCharting.csv.gz`, choose the latest nonfuture exact-label `respchartvaluelabel='FiO2'` record with `respchartoffset` in [draw−30, draw] and `respchartentryoffset <= draw`, breaking ties by greatest `respchartentryoffset`, then `respchartid`. Convert values 0.21–1.00 to percent; retain 21–100. Alternate labels are sensitivity-only. Report the entry-to-draw lag.
5. From `vitalPeriodic.csv.gz`, use valid `sao2` 70–100 at `observationoffset` in [draw−5, draw], with every retained observation offset <= draw. The primary value is the median of the available released five-minute summaries in that interval; these are monitor summaries, not raw waveforms or arterial SaO2. Report duplicate offsets and repeat as a last-summary sensitivity.
6. After complete linkage, retain the earliest eligible draw in each stay-specific six-hour block ([0,360), …, [3960,4320)), at most 12 per stay. No outcome-based sampling or post-draw variables are allowed. Report every attrition step, including revision conflicts, ventilation, FiO2, SpO2, and block thinning.

The primary analysis restricts to SpO2 96–97 and excludes alkalemia. Secondary analyses use PaO2 >150, continuous PaO2, PaO2 <60, continuous pH over SpO2 92–99, and the first 24 hours. The audited parent postprocess found approximately 869 exact-median target-band observations under its chart-offset FiO2 rule across 709 stays, 47 hospitals, and 7 exposure-balanced sites; this is feasibility provenance, not inferential evidence for this stricter entry-time-safe protocol. Recompute and report counts from the frozen rules; if the strict rule reduces the site count below five, classify the result as inconclusive.

## Variables, outcome, estimand, and baselines

Exposure is acidemia (pH <7.35) versus normal pH (7.35–7.45). The primary outcome is observed PaO2 >120 mm Hg. Secondary outcomes are PaO2 >150, continuous PaO2, and PaO2 <60 as a safety description—not tissue oxygen injury.

The primary estimand is the acidemic-minus-normal marginal standardized risk difference in observed PaO2 >120 among eligible SpO2 96–97 observations, standardizing over observed FiO2, SpO2, same-panel PaCO2, age, gender, unit type, admission source, and six-hour block. It is descriptive and noncausal.

Use three fixed baselines:

- B0: intercept and SpO2 only.
- B1: B0 plus FiO2 (per 10%), age, gender, unit type, admission source, six-hour block, and PaCO2 with a missing indicator.
- B2: B1 plus acidemia and a prespecified acidemia×FiO2 interaction.

A three-band FiO2 model (21–39, 40–59, 60–100) is the sole prespecified functional-form sensitivity; no outcome-selected spline is allowed. No APACHE values enter the primary model because they have no event time. APACHE `vent`, `intubated`, `pao2`, `fio2`, and `ph` are QC/sensitivity fields only.

## Analysis and transportability

Fit B0–B2 as logistic marginal models with a GEE clustered by `uniquepid`; use a hospital-clustered bootstrap (1,000 resamples, refitting every model) for the primary 95% interval and report failed fits. Standardize B2 by setting acidemia to 1 and 0 for every row and averaging predicted risks. The primary model contains no hospital indicator, so its estimand remains marginal and can be evaluated on an unseen site.

Define an adequate hospital before looking at outcome values as at least 30 primary-band observations, 5 acidemic observations, and 10 normal-pH observations. Do not use PaO2 event counts to select sites. If fewer than five hospitals meet this exposure/documentation gate after exact reconstruction, the transportability claim is inconclusive. For each such hospital, fit the reduced predeclared model (linear FiO2 per 10%, age, PaCO2/missingness, block, and acidemia) only when numerical support permits; otherwise report exact outcome/event denominators and mark that site contrast descriptive/unestimable rather than silently excluding it. Pool estimable site contrasts with a random-effects meta-analysis and report heterogeneity and a 95% prediction interval. The 70% site-sign criterion uses the full exposure-adequate denominator, with sparse or separated estimates explicitly flagged.

As a distinct portability check, perform leave-one-hospital-out evaluation with no hospital ID or hospital-derived feature. Train B1 and B2 on all other hospitals and evaluate the held-out hospital. Report calibration-in-the-large, calibration slope, Brier score, log loss, AUROC/AUPRC, and B2−B1 differences. These metrics test reproducibility of a measurement classifier; they do not establish clinical utility.

Model observation selection among otherwise eligible gas panels using only pre-draw patient, hospital descriptors, time block, and already observed respiratory variables. Repeat with stabilized inverse-observation weights truncated at the 1st/99th percentiles. Sensitivities are: one observation per stay; first 24 hours; last SpO2 rather than interval median; FiO2 lookback 60 minutes; exact alternate FiO2 labels; entry-time-safe FiO2; latest-revision panels; complete PaCO2; narrow closed nonzero ventilation intervals; broader airway proxy; and deletion of each adequate hospital. A lagged prior-pH prediction analysis is exploratory only, requires prior pH 30–360 minutes before the draw and no same-panel pH, and cannot upgrade the primary conclusion.

## Falsification criteria and interpretation

**Supportive** requires all of: pooled standardized RD point estimate ≥+10 percentage points with a two-sided 95% interval excluding 0; positive site-specific standardized contrast in ≥70% of exposure-adequate hospitals for which the predeclared model is estimable, with all nonestimable/sparse sites reported; no single exposure-adequate-hospital deletion reverses the pooled direction; and the site-agnostic B2 model is not materially worse than B1 on held-out Brier/log loss, with calibration slope 0.8–1.2. This supports a reproducible concurrent physiologic warning and justifies a prospective selective-ABG protocol study only.

**Adverse** means the upper 95% bound is below +10 points, which falsifies the prespecified clinically material magnitude even if a smaller positive association remains; or the overall contrast is ≤0 with an interval excluding 0; or a majority of adequate hospitals have nonpositive contrasts. Worse held-out calibration without a B2 gain is adverse to transportability. These outcomes favor the simpler SpO2/FiO2 interpretation but do not prove oxygen safety or benefit from any target.

**Inconclusive** means the interval spans both 0 and +10; fewer than five exposure-adequate hospitals remain; too few site models are estimable to evaluate the prespecified 70% sign criterion; the prediction interval spans clinically important negative and positive effects; fewer than 20% of otherwise eligible invasive panels retain both time-safe FiO2 and SpO2; more than 10% of bootstrap fits fail; or the direction reverses under prespecified timing, ventilation, weighting, or leave-one-site-out checks. Inconclusive is not a null finding.

## Exact source bindings and limitations

- `patient` / `patient.csv.gz`: `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `age`, `gender`, `ethnicity`, `hospitalid`, `unittype`, `unitvisitnumber`, `unitadmitsource`, `hospitaladmitsource`, `unitdischargeoffset`.
- `lab` / `lab.csv.gz`: `labid`, `patientunitstayid`, `labresultoffset`, `labresultrevisedoffset`, `labtypeid`, `labname`, `labresult`, `labmeasurenamesystem`, `labmeasurenameinterface`.
- `vitalPeriodic` / `vitalPeriodic.csv.gz`: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `sao2`.
- `respiratoryCare` / `respiratoryCare.csv.gz`: `respcareid`, `patientunitstayid`, `respcarestatusoffset`, `airwaytype`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`.
- `respiratoryCharting` / `respiratoryCharting.csv.gz`: `respchartid`, `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respchartvaluelabel`, `respchartvalue`.
- `hospital` / `hospital.csv.gz`: join `patient.hospitalid=hospital.hospitalid`; `numbedscategory`, `teachingstatus`, `region` are descriptive site variables only.
- `apacheApsVar` / `apacheApsVar.csv.gz`: `patientunitstayid`, `vent`, `intubated`, `pao2`, `fio2`, `ph`; no event timestamps, so QC/sensitivity only.
- `treatment` / `treatment.csv.gz`: `patientunitstayid`, `treatmentoffset`, `treatmentstring`; use only for a separately validated ECMO sensitivity, never as an unvalidated primary exclusion.

The exact source headers were checked against the catalog. The actual patient header does not contain a catalog-suggested `unitadmitoffset`; this proposal never uses it. Sources are read-only; all derived tables, attrition reports, models, and verification fixtures belong in the workspace.

EICU cannot establish arterial specimen identity, whether zero-ended respiratory-care records mean ongoing ventilation, airway persistence, artifact-free or device-comparable SpO2, or whether charted FiO2 equals delivered FiO2. Missingness may depend on pH/PaO2 and care intensity. These require clinical informatics/device review. EICU also lacks tissue oxygenation, organ-injury, patient-centered, and randomized treatment outcomes. Changing oxygen targets, claiming treatment benefit/toxicity, or deploying a pH rule therefore requires external prospective validation and a clinical trial.

## Verifier contract

The verifier can check the EICU snapshot/source hashes, headers, exact joins, revision and duplicate rules, type-7 and range predicates, discharge and 72-hour bounds, ventilation inequalities, nonfuture FiO2/SpO2, FiO2 conversion, block thinning, attrition, model formulas, bootstrap, held-out metrics, and deterministic interpretation gates. It must reject correct computation paired with a claim of oxygen toxicity or treatment benefit; accept a supportive result with the limited conclusion above; accept an upper CI below +10 as adverse to the material hypothesis; and accept wide/heterogeneous results labeled inconclusive. It cannot automatically adjudicate specimen identity, delivered FiO2, monitor calibration, true ventilation, or clinical benefit.
