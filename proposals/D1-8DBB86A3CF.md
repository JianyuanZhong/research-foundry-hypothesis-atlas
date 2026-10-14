> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Evolution proposal — MIMIC-IV island, episode 35

Parent: `[prior hypothesis]` (ep-34 Evolution child of board-top
`[prior hypothesis]`, expert seed `[starting question]`,
"Residual instability before ICU discharge"). Operation: **evolve** (choose_work,
board_revision 339). Question, population, temporal boundaries, outcomes and the locked
70/30 split are inherited **unchanged**; this episode repairs the parent's one admitted,
non-blocking defect and hardens identification against its strongest rival.

Status: **design + one bounded computed feasibility/power gate.** No B0/B1/A1 model was
fitted; no association was estimated. Numbers labelled COMPUTED come from the frozen
archive via the episode gate job; everything else is design (NOT-COMPUTED).

## 0. Hypothesis vs. supported conclusion

Supported (not re-tested): a dynamic pre-discharge data stream can carry 48 h readmission
signal [K1] and dynamic *variability* of ICU lab streams carries prognostic signal [K2].
Leading claim (H1, tested here): the pre-discharge **instability footprint** — dispersion
and trend of continuously charted vitals and rising oxygen requirement in the 24 h before
ICU discharge — adds held-out discrimination of 48 h readmission / 7-day post-discharge
death **beyond static severity**.
Strongest rival (H0): that footprint is a proxy for ICU **observation/monitoring intensity
or care-escalation** rather than patient instability — EHR measurement is not missing at
random and depends on patient/workload factors [K3].

## 1. What this child adds (the repair)

1. The parent's cohort/power gate was **unobserved**; the per-stay chartevents coverage
   check was deferred to readiness. This child computes the gate now (see §4).
2. The parent admitted the value-ordered/notes escalation channel was **not captured**.
   This child predeclares a value-free **escalation/documentation-order negative control**
   (C-order) with an explicit falsification rule, in addition to the parent's D1–D4 blocks.

## 2. Population and temporal boundaries (FIXED, inherited)

- Adult (patients.anchor_age >= 18), first ICU stay per `hadm_id`, LOS >= 24 h, discharged
  alive from the ICU. Keys: `subject_id`, `hadm_id`, `stay_id`.
- Landmark `t0 = icustays.outtime`; predictor window `[t0-24h, t0)`.
- Outcomes: (a) ICU readmission within 48 h of `t0`; (b) death within 7 days of hospital
  `dischtime` (`admissions.dischtime`, `patients.dod`). Composite = either.
- Locked 70/30 **temporal** split by `t0`.

## 3. Variables and bindings (source: frozen `mimic-iv-3.1.zip`, sha256 `0dd448e3...`)

- `mimic-iv-3.1/icu/icustays.csv.gz` (stay_id, subject_id, hadm_id, intime, outtime,
  last_careunit); `mimic-iv-3.1/hosp/admissions.csv.gz` (hadm_id, dischtime, deathtime,
  hospital_expire_flag, discharge_location); `mimic-iv-3.1/hosp/patients.csv.gz`
  (subject_id, anchor_age, dod).
- `mimic-iv-3.1/icu/chartevents.csv.gz` (subject_id, hadm_id, stay_id, itemid, charttime,
  storetime, value, valuenum, caregiver_id) for the 13 pre-verified vitals itemids.
- `mimic-iv-3.1/hosp/labevents.csv.gz` (subject_id, hadm_id, itemid, charttime, storetime,
  value, valuenum, order_provider_id, priority) for the 5 pre-verified labs.
- `mimic-iv-3.1/icu/d_items.csv.gz`, `mimic-iv-3.1/hosp/d_labitems.csv.gz` for item labels.

## 4. Computed feasibility/power gate (COMPUTED this episode)

A bounded CPU job (`work/ep35-gate/gate.py`, job `[research job]`) streams
only `icustays`, `admissions`, `patients` from the frozen zip to count the eligible cohort,
both event counts and the 70/30 split boundary. Its printed counts are reported verbatim in
`work/ep35-gate/gate.out` when present and otherwise in the change note. Residual coverage
gate (NOT-COMPUTED here, first-class readiness check): the fraction of eligible stays with
>=1 of the 13 vitals itemids charted inside `[t0-24h, t0)`, and the per-stay observation
count. If coverage < 0.60 the study is declared underpowered at readiness.

## 5. Falsification ladder and criteria (inherited, plus C-order)

M0 static severity (age, admission_type, first-day SOFA-surrogate labs, Charlson/Elixhauser
from `diagnoses_icd`) -> M1 (+level means only) -> M2 (+decoupled dynamics). Paired
Delta-AUROC/Delta-AUPRC with DeLong + 1000-bootstrap CIs on the locked split; permuted-label
negative control; M-obs competing block (charting frequency, caregiver_id switches,
storetime-charttime lag, cadence regularity).

Predeclared: **supportive** Delta1(M0->M2) >= 0.02 with CI lower bound > 0.005 AND
Delta2 crossing M-obs retention >= 0.015 (>=75% of Delta1 survives) AND permuted-label
<= 0.005 AND C-order dynamic increment <= 0.005. **Adverse** Delta1 <= 0.01, or CI includes
0, or <50% of Delta1 survives M-obs, or C-order dynamic increment >= 0.01 (footprint is
documentation-order/escalation artifact). **Inconclusive** otherwise / wide CI / coverage
gate fail.

C-order construction (value-free): order charted events within each stay by `storetime`
(documentation order), and build the SAME dispersion/trend features from a
"documentation-order" tensor that uses only the ORDER index (not the measured value) and
per-stay lag statistics. If H1 is true, real-value dynamics must beat this value-free
order surrogate; if they do not, H0 is favoured.

## 6. Method comparison (recorded before selection)

- B0 interpretable penalized logistic (static severity) and B1 (+level means), the simple
  baseline. A1 small GRU over the irregular charted sequence with time-since-last-observation
  channels. B1 could reveal whether level alone explains the signal; A1 could reveal whether
  temporal ORDERING (irregularity, lead-lag) carries information that scalar SD/slope loses.
  All CPU-feasible; A1 optional on one allocated GPU if a probe shows CPU convergence fails.
- Chosen for this deliverable: the nested B0/B1 + decoupled-M2 ladder with the M-obs and
  C-order falsifiers (interpretable, directly tests H0). A1 kept as a deferred alternative;
  justification to revisit: if B-ladder shows Delta1 present but Delta2 retention borderline.

## 7. Honest limits

- Design + gate only; no model fitted, no association estimated; single-centre retrospective.
- The value-ordered/notes escalation channel is probed via C-order but not fully removed;
  "unplanned" readmission and post-discharge death partly need clinical adjudication.
- Association / incremental-prognostic-information only; no causal or treatment claim.
