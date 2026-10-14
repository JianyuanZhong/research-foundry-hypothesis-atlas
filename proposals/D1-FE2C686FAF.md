> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Observation-process features inflate internal ICU mortality discrimination but degrade hospital transport

Lead working proposal - eICU 2.0 island, episode 3. Parent: `[prior hypothesis]` (valid, episode 2). Operation: evolve (reference delivery + observed numbers). Seed origin: `[starting question]`.

Status: design frozen by Lead for compilation. Bounded probe executed (numbers below). A reference solution is optional for this open-ended research task.

## Unresolved question and clinical importance

ICU mortality models built on EHR data are increasingly deployed at hospitals other than the development site. A recurring design choice is whether to feed the model information about the *measurement process itself* - how many labs were drawn, how many analytes were ordered, which analytes were never measured. [K1] showed, across 272 lab tests in 669,452 patients, that the *presence of a test order* alone was significantly associated with survival in 233/272 (86%) tests, and that order timing beat the test value for prediction in 118/174 (68%) tests: EHR data encode healthcare processes, not only patient state. If that process signal partly reflects local surveillance conventions (order sets, protocols, staffing) rather than physiology, a model that gains internal performance from it should mis-calibrate when transported, and internal validation will not reveal the risk. [K3] argues that this transportability failure mode is under-weighted in clinical ML evaluation. Resolving it changes a consequential deployment decision: which feature families are safe to ship, and whether target-site recalibration is required.

## Claims tested

- **H1 (leading).** Observation-process features added to a value-anchored model raise internal (within-hospital) discrimination but incur a larger whole-hospital transport penalty - worse calibration slope and observed/expected (O:E) ratio - than the value-only model of matched complexity.
- **R1 (rival, severity).** Process features largely proxy true illness severity (sicker patients are tested more), so they transport at least as well as value summaries; any penalty matches the value-only model.
- **R2 (rival, model class).** Any penalty is a linear-model artifact and shrinks under gradient-boosted trees.

Distinguishing observation: the **difference-in-penalty** between V+P and V under leave-one-hospital-out (LOHO) transport. Supportive H1 needs the V+P penalty to exceed V's; R1 predicts near-zero difference; R2 predicts the difference shrinks under GBT.

## Design

- **Population.** eICU 2.0 adult ICU stays with numeric `age` >= 16, `unitdischargeoffset` >= 1440 min, and a decisive outcome (`patient.hospitaldischargestatus` in {Expired, Alive}). One row per `patientunitstayid`.
- **Outcome.** Hospital mortality (`patient.hospitaldischargestatus == 'Expired'`), cross-checked against `apachePatientResult.actualhospitalmortality`.
- **Temporal boundary.** Features from the first 24h only (`lab.labresultoffset` in [0,1440] min from unit admit). No post-24h labs.
- **Feature sets.**
  - **V (value-only):** first-24h min/max/mean of 10 prespecified analytes (creatinine, lactate, WBC, platelets, bilirubin, sodium, potassium, glucose, BUN, hemoglobin; exact `labname` strings bound at run time from `lab.labname`), plus age, gender, coarse `apacheadmissiondx` category. Missing value = absent.
  - **V+P:** V plus observation-process features: total lab rows in [0,1440], count of distinct `labname`, and one measured/not-measured indicator per analyte.
- **Models.** L2-penalized logistic regression (baseline) and gradient-boosted trees (substantive alternative). APACHE IVa `predictedhospitalmortality` is an existing-score comparator.
- **Validation.** (i) Development: within-hospital stratified 5-fold. (ii) Transport: leave-one-hospital-out, restricted to hospitals with >= 200 stays (whole hospitals held out; no patient overlap).
- **Metrics.** AUROC, calibration slope, O:E ratio, Brier score, net benefit at 5% and 10% thresholds.
- **Primary estimand.** Delta = [(AUROC_internal - AUROC_LOHO) for V+P] - [same for V]; analogous contrast for calibration slope.
- **Falsification (pre-specified).** H1 supported only if the V+P AUROC transport drop exceeds V's by >= 0.02 **and** V+P calibration slope is >= 0.1 lower under transport than V's. H1 refuted if the V+P penalty <= the V penalty. Otherwise inconclusive.
- **Exploratory (labeled).** Per-target-hospital V+P calibration error vs that hospital's median first-24h lab count per stay, adjusted for case-mix. Not a mechanism claim.

## Baseline vs learned/mechanistic alternative

The L2 logistic baseline tests whether a simple linear combination of value summaries transports. The GBT alternative fits the same feature sets with learned nonlinearities and interactions (e.g. surveillance intensity x severity), separating H1 from R2 - which the baseline cannot. Deliverable established by: fitted V and V+P models under both model classes, with internal and LOHO AUROC/calibration/O:E/Brier/net-benefit outputs and the difference-in-penalty contrast with uncertainty intervals.

## Observed data-probe numbers (executed this episode)

Probed read-only source files (see Bindings): `patient.csv.gz` = **200,859** unit stays, **208** distinct `hospitalid`. Analysis-eligible (age>=16, unitdischargeoffset>=1440): **128,148** stays, of which **127,006** have a decisive outcome; hospital mortality **8.85%**; all **208** hospitals retained. `hospital.csv.gz` = 208 rows. `lab.csv.gz` = 39,132,531 rows (epoch-2 count).

## Bindings (source paths, tables, keys, time fields)

- Database root: `[internal dataset path]` (read-only).
- `patient.csv.gz` -> table `patient`: `patientunitstayid` (key), `hospitalid`, `age`, `unitdischargeoffset`, `unitadmittime24`, `apacheadmissiondx`, `gender`, `hospitaldischargestatus`. SHA-256 (catalog).
- `lab.csv.gz` -> table `lab`: `patientunitstayid` (join key), `labresultoffset` (time, minutes from unit admit), `labname`, `labresult`, `labresultrevisedoffset`.
- `apachePatientResult.csv.gz` -> table `apachePatientResult`: `patientunitstayid`, `actualhospitalmortality`, `predictedhospitalmortality`.
- `hospital.csv.gz` -> table `hospital`: `hospitalid` (key), `teachingstatus`, `region`. Snapshot [source checksum].
- No cross-dataset patient joins; eICU identifiers only.

## What each result means

- **Supportive:** transport penalty concentrated in process features -> exclude observation-process features, or mandate target-site recalibration, before deployment.
- **Adverse:** process features transport at least as well as value summaries -> the severity reading (R1) is strengthened; process features are not a transportability hazard.
- **Inconclusive:** wide intervals or too few hospitals in the transport set -> requires pooled MIMIC+eICU replication and prospective site validation.

## Scope and limits

All outcomes are computational statements about model behavior, not proof of a causal mechanism and not a hospital quality ranking. The causal "surveillance practice" reading needs chart/order-set/workflow data absent from eICU [K2]. Conclusions are limited to eICU US ICUs (~2014-2015). Analyte-specific missingness handling could bias V+P if a lab is systematically never ordered at some hospitals; this is addressed by the "measured" indicators and by reporting V+P both with and without them as a sensitivity analysis. Clinical adjudication is required before any deployment or quality-of-care interpretation.

## Key references

- [K1] Agniel D, Kohane IS, Weber GM. Biases in electronic health record data due to processes within the healthcare system: retrospective observational study. BMJ 2018;361:k1479. doi:10.1136/bmj.k1479. Inspected (abstract_only).
- [K2] Pollard TJ, Johnson AEW, Raffa JD, Celi LA, Mark RG, Badawi O. The eICU Collaborative Research Database, a freely available multi-center database for critical care research. Sci Data 2018;5:180178. doi:10.1038/sdata.2018.178. Inspected (full-text passage).
- [K3] Futoma J, Simons M, Panch T, Doshi-Velez F, Celi LA. The myth of generalisability in clinical research and machine learning in health care. Lancet Digit Health 2020;2(9):e489-e492. doi:10.1016/S2589-7500(20)30186-2. Inspected (abstract_only).
