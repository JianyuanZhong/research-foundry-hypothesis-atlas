> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Timing of hypotension: does the LATE component of the MAP<65 burden add ICU AKI risk beyond total dose and depth?

Lead working proposal — eICU 2.0 island, **episode 37**. Operation: **evolve** of the valid,
delivery-complete board leader `[prior hypothesis]` (mu ~32.9, rubric
life-science-stage-aware-v1). Status: **design owned and frozen by the Lead for compilation**;
discovery executed only bounded read-only header probes and literature receipts. The fitted
estimator is **NOT executed here** — this is design + verified bindings, not a solved result.

## 1. Unresolved question and why it matters
ICU teams titrate fluids and vasopressors to a mean-arterial-pressure (MAP) target. Prior work
shows a cumulative MAP<65 burden (duration and time-weighted area below threshold) tracks
downstream organ injury and ICU escalation [K1], and that MAP targets are themselves an active
randomisation question (permissive-hypotension pilot, [K2]). The parent already asks whether
*total* time-below-65 adds AKI risk **conditional on the deepest MAP (depth)**, while controlling
BP-charting and creatinine-draw intensity, severity, and hospital fixed effects, and it added a
treatment-channel arm (norepinephrine-equivalent dose + fluid intake, [K3] mechanism).

What the parent leaves **untested** is the *temporal structure* of that burden. Two leading
mechanistic explanations make different predictions:
- **H-dose (ischemic cumulative dose):** only total burden and depth matter; the *timing* of the
  MAP<65 time contributes nothing.
- **H-persistence (unresolved hypoperfusion / time-to-correction):** burden concentrated **late**
  (still unresolved near the 24 h landmark) carries extra risk beyond an equal *total* dose that
  occurred **early** and had time to recover.
This is separable and decision-relevant: if H-persistence holds, *time-to-MAP-correction* is a
candidate monitoring target; if H-dose holds, cumulative burden/depth alone suffices and chasing
timing adds no information. The closest inspected work [K1] reports total burden and depth
("time-normalized burden") but does **not** decompose the burden by timing, so it cannot
separate these.

## 2. Population, temporal boundaries, variables (inherited from the parent, re-stated)
Inherits the parent's frozen cohort/estimand verbatim; the compiler must read the exact parent
values from the frozen parent artifact. Working values:
- **Population:** adult eICU 2.0 unit stays, `age >= 16`, unit stay long enough to define a
  24 h landmark (`unitdischargeoffset >= 1440` min), with >=1 baseline creatinine and >=1
  follow-up creatinine in the outcome window.
- **Temporal:** exposure window **(0,24] h** (`observationoffset` in minutes); **24 h landmark**;
  primary outcome window **>24 h** (parent primary (24,72] h; confirm exact parent window).
- **Exposure (this child adds only the decomposition):** from `vitalPeriodic.systemicmean`
  (5-min medians), cumulative minutes with MAP<65 mmHg in (0,24] h, split into
  **EARLY = (0,12] h** and **LATE = (12,24] h**; plus parent's total burden, nadir depth
  (`min(systemicmean)`), and treatment channel (NEE-equivalent dose, fluid intake).
- **Outcome:** new KDIGO creatinine-based AKI in the follow-up window (parent definition), from
  `lab` (`labresultoffset`, `labname=='creatinine'`, `labresult`); baseline creatinine = lowest
  pre-window value.
- **Adjustment:** severity (`apachePatientResult.apachescore`, `predictedicumortality`), hospital
  fixed effects (`patient.hospitalid`), charting-intensity (`n_map`) and creatinine-draw
  (`n_cr`) controls — all from the parent.
- **Join key:** `patientunitstayid` (units = minutes).

## 3. Verified bindings (this episode, real eICU 2.0 headers)
- `patient.csv.gz`: `patientunitstayid, age, gender, hospitalid, unitdischargeoffset, unitdischargestatus, hospitaldischargeyear` — CONFIRMED.
- `vitalPeriodic.csv.gz`: `patientunitstayid, observationoffset, systemicsystolic, systemicdiastolic, systemicmean` — CONFIRMED.
- `apachePatientResult.csv.gz`: `patientunitstayid, apachescore, predictedicumortality` — CONFIRMED.
- `lab.csv.gz`: `patientunitstayid, labresultoffset, labname, labresult` — CONFIRMED; `labname=='creatinine'` string verified in prior episodes by executed read (re-confirm in readiness).
Source root: `[internal dataset path]` (snapshot hash in `datasets/eicu/README.md`).

## 4. Baseline vs substantive learned/mechanistic alternative (same question)
- **Baseline:** hospital-fixed-effects logistic model with depth (`min MAP`) + **total** MAP<65
  burden + severity + charting/draw intensity. This is H-dose's implied model (timing ignored).
- **Substantive alternative:** the same model adding **EARLY and LATE burden** as separate terms
  (so the LATE coefficient is the timing contrast conditional on total burden/depth), plus an
  interaction with depth; a within-stratum (depth-decile) LATE OR is the confirmatory readout.
- **What the alternative reveals that the baseline loses:** whether risk is a function of *dose
  alone* or of *when the dose occurred* (persistence/recovery). Estimated by likelihood-ratio /
  coefficient contrast; reported with 95% CIs and a LOHO (leave-one-hospital-out) transport check.
- **Resource budget (estimate, unverified):** CPU only; tabular fits over ~10^5 stays; target
  < ~2 h on <=16 CPU / 64 GB (well inside solver envelope). No GPU required for the primary;
  not excluded if a sequence representation is later added.

## 5. Falsification criteria
- **Supportive (H-persistence):** LATE coefficient > 0 with 95% CI excluding 0 (and greater than
  the EARLY coefficient) *after* adjusting for total burden, depth, severity, hospital FE and
  charting/draw intensity; LOHO retains sign.
- **Adverse (H-dose):** LATE coefficient ~0 / CI includes 0, or LATE not distinguishable from
  EARLY once total burden is in the model.
- **Inconclusive:** wide overlapping CIs, sign instability across LOHO folds, or sensitivity to the
  charting/creatinine-draw controls.
- **Placebo/negative control:** an hour-<12-substituted pseudo-timing split and a negative-control
  outcome must not reproduce the LATE contrast.

## 6. Key references (inspected; see key-references.json + attached excerpts)
- **[K1]** Liu Z, Wang N, Chen M, Wang H. *Association between cumulative intraoperative
  hypotension and postoperative ICU admission after gastrointestinal lumen cancer surgery.*
  Front Med 2026;13:1916589. doi:10.3389/fmed.2026.1916589. Establishes cumulative MAP<65
  **duration and area** burden as associated with worse outcomes and reports depth/time-normalized
  burden; **does not** decompose timing → bounds but does not answer our question.
- **[K2]** Miranda DW, et al. *Rationale and design of a pilot randomized control trial of
  permissive hypotension after cardiac surgery: The PHACS trial.* Am Heart J Plus 2026.
  doi:10.1016/j.ahjo.2026.100852. Shows MAP targets are a live randomised clinical decision →
  clinical importance; a pilot design, not evidence on timing→AKI.
- **[K3]** Dubech A, Picod A, Pierre A, Preau S, Favory R, Garcia B. *Current and future strategies
  aiming at reducing catecholamine exposure in septic shock.* Crit Care 2026.
  doi:10.1186/s13054-026-06109-3. Norepinephrine exposure/duration entangles with hypotension
  duration → the treatment-intensity rival; a narrative review, no timing→AKI estimate.

## 7. Honest limits
- eICU-internal LOHO transport only; no external validation.
- MAP is a 5-min median; invasive vs cuff MAP not recorded → charting artifact bounded, not eliminated.
- `labname` not harmonised; creatinine ascertainment is detection-sensitive (mitigated by n_cr).
- NEE-equivalent conversion approximate; vasopressor strings not fully harmonised.
- Association/timing contrast, NOT causality or an intervention threshold.
- Discovery closed at design + verified bindings; the estimator, LR test, LOHO and placebo were
  **not executed** in this episode (readiness, not a solved result).

## 8. Scientific deliverable (what the solver must fit and report)
Fit the baseline and timing-alternative models on the frozen cohort/split; report EARLY/LATE
coefficients with CIs, the depth-stratified LATE contrasts, LR-test p-value, LOHO band, and the
placebo/negative-control results; conclude against the pre-specified supportive/adverse/
inconclusive rules. Deliverable = a fitted timing decomposition that separates H-dose from
H-persistence, with uncertainty — not a causal MAP target.
