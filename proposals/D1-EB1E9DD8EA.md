> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Does the DURATION of ICU hypotension add risk information beyond its DEPTH? A duration-vs-depth decomposition in eICU with a hospital-transport test

Lead working proposal — eICU 2.0 island, episode 16. Operation: **evolve** of true parent
`[prior hypothesis]` (valid, mu 25.0, comparison_count 0; episode-10 restart child
of expert seed `[starting question]` "Duration of hypotension"). Seed origin: `[starting question]`.
Status: design frozen by the Lead for compilation. **No reference/solver solution was executed at
discovery** — this is readiness, not a solved result.

## Unresolved question and clinical importance
ICU teams titrate blood pressure toward MAP targets (e.g. 65 mmHg) largely on the idea that *how low*
matters. Whether the *duration* of hypotension (time below threshold) carries decision-relevant risk
information **beyond depth (nadir) and mean** is genuinely unresolved and changes monitoring design:
if duration adds information, time-in-target / burden monitoring is justified; if depth/mean absorb it,
simpler nadir-based reasoning suffices and duration-weighted "burden" indices are not warranted as risk
measures. [K1] shows cumulative MAP<65 duration associates with downstream events but does NOT separate
duration from depth/mean. [K2] warns the reverse: improving hypotension metrics did not reduce AKI, so any
burden-index claim must survive a strict separability test. [K3] shows KDIGO creatinine AKI and
dose-response shape are estimable in eICU itself. This is an association/transport study, not causal.

## Claims
- Supported already: hypotension exposure is common and chart-dense in eICU; KDIGO-AKI is estimable [K3];
  cumulative duration associates with downstream events in a perioperative cohort [K1].
- Tested (unresolved): the duration component is separable from depth/mean within the same ICU stay and
  transports across hospitals.
- Leading rivals: **R1** depth/mean absorb the association (adjusted duration term ≈ null); **R2**
  severity + monitoring-density confounding; **R3** measurement/artifact (non-physiologic MAP); **R4**
  hospital-practice fingerprint (between-hospital variance dominates).

## Population, temporal boundaries, variables, outcome (bindings)
- Population: adult eICU unit stays, `age>=16`, `unitdischargeoffset>=1440` min, decisive
  `unitdischargestatus`, hospitals with >=200 eligible stays. (Parent-positive-control probe: patient
  200,859 rows / 128,148 with udo>=1440 / 208 hospitals.)
- Sources (read-only, headers re-verified this episode): `patient.csv.gz`
  (`patientunitstayid`,`uniquepid`,`hospitalid`,`age`,`unitdischargeoffset`,`unitdischargestatus`);
  `vitalPeriodic.csv.gz` (`observationoffset` minutes, `systemicmean`=MAP, `systemicsystolic`);
  `lab.csv.gz` (`labresultoffset`,`labname`=creatinine,`labresult`); `apachePatientResult.csv.gz`
  (`apachescore`,`acutephysiologyscore`,`predictedicumortality`); `infusionDrug.csv.gz`
  (`infusionoffset`,`drugname`). Join key: `patientunitstayid`.
- Exposure (first 24 h, offsets 0–1440): duration = minutes with `systemicmean<65`; nadir MAP; mean MAP;
  burden = area below 65 mmHg; sampling density = MAP-observation count. Physiologic filter:
  20<=MAP<=200 (R3).
- Landmark hour-24; outcome window (24,72] h.
- Primary outcome: AKI in (24,72] h by KDIGO creatinine criteria (rise >=0.3 mg/dL vs the 0–24 h
  reference, or >=1.5x reference). Secondary: unit/hospital death in (24,72] h.
- Negative-control outcome: AKI already present AT the hour-24 landmark (prevalent AKI).

## Baselines, learned alternative, discriminating test
- Baseline (simple): logistic — severity (APACHE) + nadir + mean MAP + age + monitoring density.
- Learned alternative (substantive): gradient-boosted trees on 24 h MAP time-series features
  (time-below-60/65/70 curves, slope, nadir timing, sampling density). Information the baseline loses:
  non-linear duration x depth x onset-timing interactions (long early low episode vs brief late dips)
  that a single linear duration term cannot express.
- Estimand/discriminator H1 vs R1: nested-model likelihood-ratio + incremental AUROC for duration over
  nadir+mean; pre-specified quintile dose-response monotonicity. R2: adjust severity + density, inspect
  attenuation. R4: leave-one-hospital-out transport (delta-AUROC, calibration, O:E, Brier) plus a
  within-hospital person-centered duration term.
- Child sharpenings over parent: (1) duration x depth interaction tested (not assumed); (2) the
  prevalent-AKI negative control; (3) within-hospital person-centered duration term.

## Falsification / interpretation
- Supportive (H1): adjusted duration term non-null with monotone gradient AND incremental discrimination
  CI excluding 0 after R1/R2 adjustment AND the negative-control outcome shows no duration effect.
- Adverse (R1/R2): duration term ≈ null after adjustment, or duration predicts prevalent AKI
  (artifact) → depth/severity suffices; duration-weighted burden indices not justified as risk measures.
- Inconclusive: wide CIs, non-monotone gradient, or transport failure with unstable estimates.
None of these establishes causality or a treatment threshold; those require adjudicated clinical data
and would be a separate study.

## Method-selection note
Baseline logistic (CPU) vs GBT time-series alternative is a substantive uncertainty test (shape /
separability), not a leaderboard gain. CPU-feasible; no GPU needed. Full solver run deferred to
compilation (solver envelope: 16 CPUs / 28800 s); discovery executed only small read-only checks.
