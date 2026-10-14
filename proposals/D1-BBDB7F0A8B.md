> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Depth-conditioned hypotension DURATION and ICU AKI: a genuine ischemic dose, or a BP-charting / creatinine-draw artifact?

Lead working proposal - eICU 2.0 island, **episode 34**. Operation: **evolve** of true parent
`[prior hypothesis]` (valid, delivery-complete leader, mu 35.85, gen 4; assessed
this episode; episode-32 child of `[prior hypothesis]`). Status: **design owned and
frozen by the Lead for compilation**. Discovery bounds: only a bounded data/header probe and the
literature receipts below were executed this episode; **the fitted depth-vs-duration estimator is
NOT executed here** - this is design + verified bindings, not a solved result.

## 1. Unresolved question and why it matters
ICU teams titrate fluids/vasopressors to a MAP target. Time-weighted MAP<65 burden is the reference
exposure for creatinine-KDIGO AKI (base-model AUC 0.725 [K1]); cumulative MAP<65 duration shows a
graded association with downstream organ outcomes (aOR 1.78 for >=30 min [K2]). Both treat
hypotension as a single scalar burden. The decision-facing question is unresolved: **once a patient's
deepest MAP (depth) is known, does cumulative time-below-65 (duration) carry ADDITIONAL AKI risk - a
distinct ischemic dose that a "time below target" monitor should track - or does depth alone suffice,
or is the duration signal produced by how often BP and creatinine happen to be charted?**

Clinical importance: if a depth-conditional duration effect survives measurement-intensity control
and transports across hospitals, "time below target" is a monitoring target distinct from the low
excursion itself. If it collapses once charting intensity is modelled, duration alarms add no
information and would be a surveillance artifact.

## 2. Leading claim vs strongest rival (must be separable)
- **H1 (conditional ischemic dose):** duration adds AKI risk conditional on depth; the conditional
  duration effect is stable to BP-charting and creatinine-draw intensity and transports (LOHO).
- **R1 (depth-sufficiency):** duration adds nothing once the deepest MAP is known.
- **R2 (charting/surveillance artifact [K3]):** more charted values -> more recorded time-below-65
  AND more opportunity to detect a creatinine rise; the duration effect scales with BP-charting
  frequency and collapses under a time-normalized / per-observation exposure.
- **R3 (ascertainment):** the AKI event itself is detected by creatinine draws, whose intensity may
  co-vary with BP-charting intensity.

Separating observation: H1 requires the depth-conditional duration OR to stay >1 with CI excluding 1
after adding charting-intensity covariates AND under a heavily-regularized joint depth+charting
adjustment; R2 predicts the effect is materially absorbed (>50% OR reduction) or vanishes once the
exposure is defined per charted observation and the model includes BP-charting and creatinine-draw
rates. R1 predicts a null conditional duration OR at every step.

## 3. Data bindings (verified this episode on the real eICU 2.0 headers; join key `patientunitstayid`; all offsets in MINUTES)
- `patient.csv.gz` (200,859 stays): `patientunitstayid`, `uniquepid`, `hospitalid`, `age`,
  `unitvisitnumber`, `unitdischargeoffset`, `unitadmitsource`, `unitstaytype`.
- `vitalPeriodic.csv.gz`: `patientunitstayid`, `observationoffset`, `systemicmean` (MAP).
- `lab.csv.gz`: `patientunitstayid`, `labresultoffset`, `labname`, `labresult`, `labtypeid`.
- `apachePatientResult.csv.gz`: `patientunitstayid`, `apachescore`, `predictedicumortality`,
  `actualiculos` (hour-24 severity + baseline risk).
- `hospital.csv.gz`: `hospitalid` (208 rows) for hospital-level clustering/LOHO.
(Headers confirmed by direct read; row counts confirmed: patient 200,859; hospital 208.)

## 4. Population, exposure, outcome, temporal boundaries
- **Population:** first ICU stay per `uniquepid` (`unitvisitnumber==1`), `age`>=16, no chronic
  dialysis/ESRD at admission (exclude by `admissionDx`/`pastHistory` codes), `unitdischargeoffset`
  >= 1440 (>=24 h in unit). **Landmark = hour 24.**
- **Exposure window (0,24]h:** `duration_h` = cumulative hours in (0,24]h with `systemicmean`<65;
  `depth_min` = min `systemicmean` in (0,24]h; `n_map` = count of `systemicmean` observations in
  (0,24]h (BP-charting intensity); `frac_below` = duration_h / monitored hours (time-normalized).
- **Outcome:** creatinine-KDIGO AKI first met in **(24,168]h** from `lab` creatinine
  (rise >=0.3 mg/dL within 48 h vs the pre-landmark baseline, or >=1.5x baseline over 7 d);
  `n_cr` = creatinine draws in (0,24]h (draw intensity). This is the parent's outcome, re-timed to
  the hour-24 landmark so exposure precedes outcome (no post-landmark leakage into the exposure).
- **Covariates:** hour-24 `apachescore` (and `predictedicumortality`), age, sex (from `gender`),
  hospital id; charting/draw intensities `n_map`, `n_cr`.

## 5. Estimand, analysis, and method comparison
- **Primary estimand:** conditional OR of creatinine-KDIGO AKI per +5 min/h increase in `duration_h`,
  from a model with flexible depth (restricted cubic spline of `depth_min`) + RCS(`duration_h`),
  hospital random intercept. Report the depth-conditional duration OR and its 95% CI.
- **Baseline (simple):** fixed-effect logistic/Cox with linear or RCS depth + duration, hospital
  fixed effects.
- **Substantive alternative (learned/mechanistic):** within-patient marked point-process exposure
  model - the event hazard at time t depends on the accumulated depth-weighted area below 65
  attributed to each charted MAP observation, with a hospital random intercept, decomposing
  **within- vs between-hospital** duration variance. This is scientifically substantive because a
  single-scalar logistic cannot separate a within-patient dose signal from a between-hospital charting
  fingerprint; the point-process alternative exposes that decomposition.
- **Evaluation:** AUROC, calibration slope/ICI, O:E, Brier, decision-curve net benefit under (a)
  random 5-fold cross-validation and (b) **leave-one-hospital-out (LOHO) transport**; the primary
  scientific readout is the conditional duration OR and how it moves under measurement-intensity
  adjustment and LOHO.
- **Placebo/negative control:** a landmark placebo - `duration_h` measured in (12,24]h predicting AKI
  already present by the hour-12 landmark - must be null if the effect is a forward dose signal.
- **Sensitivity:** E-value for unmeasured confounding of the conditional duration OR; a
  shuffled-hospital LOHO null.

## 6. Falsification (pre-specified)
- **Supportive (H1):** adjusted depth-conditional duration OR > 1 with 95% CI excluding 1; OR
  reduction after adding `n_map`/`n_cr` < 25%; effect preserved under LOHO (CI still excluding 1);
  hour-12 placebo-landmark null. Only then is "time below target" a defensible distinct monitoring
  target.
- **Adverse (favors R1/R2):** conditional duration CI includes 1 after depth adjustment (R1), OR
  reduction >= 50% after charting adjustment or collapse under `frac_below` (R2), or effect fails to
  transport (LOHO CI includes 1 while random-split excludes it) (practice fingerprint).
- **Inconclusive:** minimum-detectable-effect rule - if the 95% CI half-width for the conditional
  duration OR exceeds the pre-specified informativeness bound (equivalent to a <0.02 AUC-equivalent
  contribution) or events < 500, report inconclusive, not null.

## 7. What each outcome would and would not establish
Supportive establishes a depth-conditional duration association that survives measurement control
and hospital transport - still an association, not a mechanism or an intervention threshold.
Adverse (R2/R1) is a useful negative: duration alarms would carry no depth-conditional information.
Either way, causal or treatment-target claims require a trial or external validation - beyond this
dataset.

## 8. Method-exploration record (baseline vs alternative)
Simple baseline (hospital-fixed logistic, linear/RCS depth+duration) is justified as the current
literature standard [K1,K2]. The point-process alternative is added because only it can decompose
within- vs between-hospital duration variance - the exact quantity that separates H1 from R2. Chosen
inputs: `vitalPeriodic.systemicmean`, `lab` creatinine, `apachePatientResult.apachescore`,
`hospital.hospitalid`. Fit target: conditional duration OR + decomposition; split: random 5-fold and
LOHO; evaluation: OR/CI, transport, AUROC/calibration/O:E/Brier/net-benefit; compute: CPU tabular
(~200k stays, ~39M lab rows streamed) - GPU not required; resource estimate measured from prior
branch probes (parent executed a streaming coverage probe in 128 s).

## 9. Honest limits / essential adjudication
- eICU-only internal LOHO transport, **not external validation**; no claim of causality or of an
  intervention threshold.
- `labname`/`labtypeid` not harmonized; creatinine identification is string-matched and requires
  documented adjudication of the creatinine label set.
- No order-set/staffing/capacity data -> no organizational-mechanism claim.
- `systemicmean` is charted vitalPeriodic MAP; whether it is invasive or cuff is not recorded, so the
  measurement-intensity artifact (R2) can only be bounded, not eliminated, within eICU.
- Discovery executed only a header/row probe and literature receipts; the fitted estimator remains to
  be run by the solver.

## 10. Disposition of the three demonstrations
- **D1 (natural-history sequence transformer):** needs multimodal longitudinal sequence inputs and
  pretraining corpora absent from eICU -> explicit missing dependency; not pursued.
- **D2 (longitudinal routine clinical data / model validation):** adapted via LOHO hospital transport,
  calibration (ICI/slope), O:E and decision-curve net benefit - method influence, not reproduction.
- **D3 (EHR + genetic Bayesian multi-omics):** needs genetic/multimodal inputs absent from eICU ->
  explicit missing dependency; not pursued.
- **Expert seed `[starting question]`** ("Reduced testing and subsequent deterioration") informed
  earlier branch episodes; the parent's hypotension-duration branch is the matured line selected here.
