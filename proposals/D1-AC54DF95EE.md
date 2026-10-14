> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Insulin-associated hypoglycemia in eICU: does falling renal function or interrupted nutrition amplify risk beyond insulin intensity, and does the signal transport across hospitals?

Lead working proposal — eICU 2.0 island, **episode 17**. Operation: **evolve** of true parent
`[prior hypothesis]` (raw operator import of expert seed `[starting question]`
"Hypoglycemia after insulin"; now assessed valid). Status: **design frozen by the Lead for
compilation**. A bounded Lead probe was submitted on the REAL source files; numbers reported below
only if the job completed before this file was frozen — otherwise the probe is reported as PENDING
and no number is claimed. **No reference/solver solution was executed at discovery** — this is
readiness, not a solved result.

## Unresolved question and clinical importance
Hypoglycemia is a common, potentially lethal ICU adverse event. [K1] NICE-SUGAR showed a strategy that
produced more severe hypoglycemia raised 90-day mortality (27.5% vs 24.9%, OR 1.14, P=0.02), so
identifying *which* insulin-treated patients are most vulnerable is decision-relevant. Two mechanisms
are plausible amplifiers: falling renal function (reduced insulin/glucose clearance) and interrupted
nutrition (glucose supply removed while insulin continues). [K2] confirms the harm/benefit of tight
glucose control is context-dependent, explicitly naming nutritional supply, insulin boluses and
measurement accuracy. [K3] establishes eICU as a multi-hospital, granular source able to test whether
any signal is a patient property or a hospital-practice fingerprint. The medical decision at stake:
whether a renal-/nutrition-aware insulin safeguard is justified.

## Claims
- **Supported already:** hypoglycemia is a decision-relevant harm in ICU [K1]; the harm of aggressive
  control is context-dependent (nutrition, insulin delivery, measurement) [K2]; eICU supports
  time-aligned lab/medication/nutrition analysis across hospitals [K3].
- **Tested (unresolved):** at matched insulin exposure intensity, a within-patient fall in renal
  function (rising creatinine) and an interruption of enteral/parenteral nutrition independently
  predict subsequent glucose <70 mg/dL within the same stay, and the effect transports across hospitals.
- **Leading rivals:** R1 severity/illness confounding; R2 between-hospital monitoring/dosing practice;
  R3 measurement/artifact (glucose record density, spurious values); R4 reverse-causation/indication
  (sicker patients receive both more insulin and more glucose checks).

## Population, temporal boundaries, variables, outcome (bindings)
- Population: adult eICU unit stays, `age>=16`, `unitdischargeoffset>=1440` min, decisive
  `unitdischargestatus`, hospitals with >=200 eligible stays; require >=2 glucose values in (0,48] h
  and >=1 insulin record in (0,24] h.
- Sources (read-only): `patient.csv.gz` (`patientunitstayid`,`uniquepid`,`hospitalid`,`age`,
  `unitdischargeoffset`,`unitdischargestatus`); `infusionDrug.csv.gz` (`infusionoffset`,`drugname`,
  `drugrate`); `medication.csv.gz` (`drugname`,`dosage`,`routeadmin`,`startoffset`/`stopoffset`);
  `lab.csv.gz` (`labresultoffset`,`labname`,`labresult`); `intakeOutput.csv.gz`
  (`intakeoutputoffset`,`celllabel`/`cellpath`,`cellvaluenumeric`); `apachePatientResult.csv.gz`
  (`apachescore`,`predictedicumortality`). Join key: `patientunitstayid`. All offsets in MINUTES.
- Exposure (landmark 0–24 h): insulin intensity = count + summed dose of insulin records in (0,24] h;
  Δrenal = (min creatinine in (0,24] h) → (creatinine at/after 24 h) as absolute and % rise;
  nutrition = presence of enteral/TPN intake in the (6,24] h window and the gap since the last
  nutrition record (missing != cessation; audited via timestamp gaps).
- Landmark hour-24; outcome window (24,48] h with a full observation requirement on both ends.
- Primary outcome: first `labname=glucose` value <70 mg/dL in (24,48] h (physiologic filter
  10<=glucose<=800). Secondary: glucose <54 mg/dL; unit/hospital death in (24,72] h.
  Negative-control outcome: hypoglycemia already present AT the hour-24 landmark (prevalent) — a real
  insulin–renal–nutrition mechanism should predict incident, not prevalent, events.

## Baselines, learned alternative, discriminating test
- Baseline (simple): logistic regression — insulin intensity + severity (APACHE) + landmark glucose +
  age + monitoring density.
- Learned alternative (substantive): gradient-boosted trees on 24 h joint trajectory features
  (creatinine slope, nutrition gap, insulin dose curve, glucose variability) that can express
  non-linear dose × context interactions (high insulin × falling renal function × nutrition gap) a
  single linear term cannot; the deliverable is the *shape/interaction* of the amplification, not a
  leaderboard gain.
- H1 vs R1: incremental discrimination (ΔAUROC, nested LR test) after severity adjustment.
  R2: hospital random intercept + random slope plus leave-one-hospital-out transport (ΔAUROC,
  calibration, O:E, Brier). R3: monitoring-density adjustment + glucose-filter sensitivity.
  R4: landmark design + prevalent-event negative control + explicit indication adjustment.

## Falsification / interpretation
- **Supportive (H1):** adjusted Δrenal and nutrition-gap terms non-null (bootstrap CI excluding 0)
  with expected direction AND incremental discrimination after R1/R2/R3 adjustment AND negative-control
  null.
- **Adverse (R1/R2/R4):** terms ~null after adjustment, or predict *prevalent* hypoglycemia (artifact),
  or vanish on transport → insulin intensity + severity suffice; no renal/nutrition-specific safeguard
  is justified by this data.
- **Inconclusive:** wide CIs, non-transportable estimates, or insufficient insulin/glucose/nutrition
  records.
None establishes causality or a treatment threshold; those require adjudicated clinical data and
expert review and are outside the computable experiment.

## Data requirements and honest gaps
- Insulin administration strings must be enumerated on the real files (probe step) before the solver
  can define intensity; documented as a binding prerequisite.
- eICU has no reliable continuous enteral-nutrition flag: `intakeOutput` celllabels are heterogeneous
  and missing != cessation (seed limitation). Nutrition is therefore an explicitly confounded,
  exploratory term with sensitivity analysis **and a mechanistically clean nutrition claim is NOT
  established by this design**.
- No order-set/staffing data → R2 (practice) is only partially separable.

## Method-selection note
CPU-feasible; no GPU needed. Comparing a simple logistic baseline against a GBT trajectory alternative
tests the shape and interaction of the amplification, not a leaderboard increment.

## Key references
[K1] NICE-SUGAR (Finfer 2009, NEJM, doi:10.1056/NEJMoa0810625) — abstract_only.
[K2] Gunst 2026 (Med Clin North Am, doi:10.1016/j.mcna.2026.01.015) — abstract_only.
[K3] Pollard 2018 (Sci Data, doi:10.1038/sdata.2018.178) — abstract_only.
