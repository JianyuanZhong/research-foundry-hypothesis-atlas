> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Proposal (rival-separation branch) — pre-ICU-discharge residual instability, MIMIC-IV island, ep 33

Candidate: child of `[prior hypothesis]` (mu 36.12, validated ep 32; feasibility gate executed).
Operation: **evolve**. Origin: expert seed `[starting question]`. Parent frozen — not redefined.
Status: **DESIGN ONLY. No model fitted and no association estimated in this discovery episode; no hypothesis
outcome tested.** Every itemid/column/member below was re-read THIS episode from the frozen archive
(`work/gen-rival/binding-probe.md`). Cohort/event counts in §5 are the parent's inherited descriptive
feasibility gate, **not** an outcome. No clinical truth is claimed.

## 1. Unresolved question and clinical importance

Extubating/transferring a patient out of the ICU is a high-stakes, weakly-standardised decision; the adverse
outcomes it is meant to prevent are **unplanned ICU readmission** and **post-discharge death**. Clinicians
judge "readiness" dynamically (is O2 demand still climbing, are vitals still swinging?), but static severity
scores ignore trajectory. The open question:

> Among adults discharged **alive** from their first ICU stay (LOS ≥ 24 h, `t0 = icustays.outtime`), does a
> prespecified dynamic **"residual instability"** footprint in the fixed window `[t0-24h, t0)` add **held-out
> prognostic discrimination** for (a) 48 h unplanned ICU readmission and (b) 7-day post-discharge death
> **beyond a same-window static last-day severity snapshot** — or is the apparent signal an artifact of
> **(i) reserved overall severity** and **(ii) observation intensity** (sicker patients are charted more
> often, which mechanically inflates any variability/trend summary computed from chart events)?

This branch's advance over the frozen parent is to make the **observation-intensity rival fully separable**
and the **null informative**: a value-free negative-control exposure, an observation-frequency-matched
control rung, an incremental-information estimand with a prespecified equivalence margin, and a substantive
learned/sequence alternative against an interpretable static baseline. [K3] is the direct prior showing that,
on MIMIC-IV, apparent readmission predictors can be non-actionable severity/administrative proxies; we turn
that warning into a discriminating test.

## 2. Hypothesis vs conclusion (what is already supported vs what is tested)

- **Already supported (NOT re-tested):** pre-discharge physiology is *associated* with post-ICU adverse
  events and pre-discharge readmission-prediction models report discrimination [K1]; the readmission-
  prediction literature is heterogeneous and high-ROB [K2]; MIMIC-IV readmission signal can be
  non-actionable severity/frailty/administrative confounding [K3]. Nothing here says a *dynamic* footprint
  adds *incremental* held-out information.
- **Untested claim this experiment resolves (the deliverable):** the dynamic footprint adds **incremental**
  held-out discrimination beyond a same-window static severity model **AND** beyond an observation-
  intensity-matched model **AND** beyond a value-free chart-event-count model. This is a **predictive-utility
  / prognostic-information** claim, **not** a causal claim.

## 3. Leading claim vs strongest rival (explicit discriminating observation)

- **H1 (leading):** the prespecified dynamic instability footprint adds held-out `ΔAUROC` / `ΔAUPRC` over
  the static model, and this increment exceeds the value-free count-only (NCO) increment and survives the
  observation-frequency-matched rung (M-obs).
- **H0 (strongest rival):** the footprint's apparent signal is fully explained by (a) overall severity and
  (b) **observation intensity** (charting/review frequency) — a measurement/sampling artifact, not a distinct
  physiologic state [K3].
- **Discriminating observation:** the paired held-out increment of **M1 over M0**, compared against the NCO
  increment and the M-obs rung, under the **same model class**, plus a permuted-label negative control.
- **What each result would / would not establish:** a positive, control-surviving increment establishes
  **predictive utility only** — NOT that delaying discharge or lightening support improves outcomes (that
  needs prospective / target-trial work). A null inside the equivalence margin bounds what routine
  pre-discharge vitals encode; it does not prove instability is physiologically meaningless.

## 4. Population, temporal boundaries, keys (FROZEN — retained from parent)

- Source (read-only): `mimic-iv-3.1.zip` [source checksum];
  members are INNER `.csv.gz` streams under prefix `mimic-iv-3.1/` (read `gzip.GzipFile(fileobj=zf.open(...))`).
- Base `icu/icustays` (`subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`).
  **Index stay = first by `intime` per `hadm_id`.** Adults (`hosp/patients.anchor_age >= 18`). **ICU LOS ≥ 24 h**
  (`icustays.los >= 1.0`). **Discharged alive:** exclude `hosp/admissions.deathtime` inside `[intime, outtime]`.
- **`t0 = icu/icustays.outtime`.** Predictor window `[t0-24h, t0)`; primary outcome window `(t0, t0+48h]`
  (unplanned ICU readmission = a **new `stay_id`** for the same `subject_id`); secondary `(t0, t0+7d]`
  post-discharge death (`admissions.deathtime` or `patients.dod`).
- **LOCKED 70/30 temporal split by `t0`** (no re-splitting): earliest 70 % = development, latest 30 % =
  held-out. Split computed once on development; held-out never used for selection.

## 5. Cohort/event counts (inherited descriptive feasibility gate — NOT an outcome)

Eligible: **62,466** stays. 48 h unplanned readmission **2,964 (4.74 %)**; 7-day post-`t0` death
**1,521 (2.43 %)**; either **4,267 (6.83 %)**. Locked split boundary `t0 = 2169-10-11 22:55:40` →
dev ≈ **43,726** / held-out ≈ **18,740** (~1,280 combined held-out events; ≥ 10 events/predictor). Power gate
**MET**. *Not executed:* per-stay chartevents coverage in `[t0-24h, t0)` (full ~3.4 GB scan) — deferred.

## 6. Variables and exact verified bindings (re-verified THIS episode)

Join keys `subject_id, hadm_id, stay_id`; event time `charttime`.
**Vitals (icu/chartevents):** HR `220045`; arterial SBP `220050`; non-invasive SBP `220179`; RR `220210`/`224690`;
SpO2 `220277`; temp C `223762` / F `223761`. **O2 requirement:** FiO2 `223835`; O2 flow `223834`;
additional-cannula O2 flow `227287`; PEEP set `220339`; vent mode `223849`. **Labs (hosp/labevents):** lactate
`50813`; bilirubin total `50885`; creatinine `50912`; platelets `51265`; WBC `51301`. **Static severity:**
last-day values of the above + `hosp/admissions.admission_type` + age + ICU LOS + Charlson from
`hosp/diagnoses_icd` (`subject_id,hadm_id,seq_num,icd_code,icd_version`). **Transfer context:** `hosp/transfers`
(`subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`). **Observation intensity (key variables
this branch):** per-window chart-event COUNT from `icu/chartevents` and lab-order COUNT from `hosp/labevents`
over `[t0-24h, t0)`, using `charttime` only (**value-free**).
**Verified present THIS episode:** all 13 ICU itemids + 5 lab itemids + all 9 member headers
(`work/gen-rival/binding-probe.md`). **Unverified:** archive byte hash (inherited); per-stay chartevents
coverage; labevents streamed only as header+2-row probe. Any other itemid is non-binding.

## 7. Method ladder (same question; explicit, comparable alternatives)

- **M0 / B0 — static, interpretable (baseline).** Penalized logistic regression on **last-24 h levels** of the
  vitals+labs above (last-value in window) plus age, ICU LOS, `admission_type`, Charlson. The anchor.
- **M1 — dynamic footprint.** M0 **+** prespecified dynamic summaries over `[t0-24h,t0)`: within-window
  slope/trend and variability (SD / range) of HR, RR, SpO2, SBP; FiO2 and O2-flow trend; direction-of-change.
  Continuous features standardized on the development split only.
- **M-obs — observation-frequency-matched rung.** M0 **+** per-window chart-event count **and** lab-order
  count. The dynamic increment must exceed this rung. *(Value-bearing but intensity-only control.)*
- **NCO — value-free negative-control exposure.** A model of the **SAME class** fit to **chart-event COUNT
  only** (no clinical values, no labs), calibrated to the same window length. **Predeclared artifact
  signature:** if M1's increment over M0 is **not larger** than NCO's increment over M0
  (`Δ(M1−M0) ≤ Δ(NCO−M0)`), the H1 signal is **not separable from observation intensity**.
- **A1 — substantive learned/sequence alternative** (Branch B, `work/gen-method/`). An irregularly-sampled
  sequence model (or learned windowed representation) over the raw 24 h trajectory, to test whether
  trajectory **shape** adds information that M1's hand-picked scalar summaries lose. What A1 could reveal
  that M0/M1 lose: timing/ordering and interactions among sampled observations (e.g. a late upturn in O2
  demand) collapsed by mean/SD. Inputs: same window, per-series padded (time-since-`t0`, value) sequences;
  target/split/uncertainty identical to M0/M1; baseline comparison = `Δ(A1−M0)` and `Δ(A1−M1)`; approximate
  budget: GPU job, ≤ 8 A100-hours, single train per outcome. **Selection/deferral reason recorded in
  `work/gen-method/method-comparison.md`.** *If A1 is deferred, M1 vs M0 vs M-obs vs NCO remains the
  completed scientific deliverable.*

## 8. Primary estimand, analysis and uncertainty

- **Primary estimand:** held-out incremental discrimination **ΔAUROC(M1−M0)** and **ΔAUPRC(M1−M0)** on the
  locked 30 % split, paired (same rows), with **1000-sample bootstrap 95 % CIs**. Co-primary comparison
  **Δ(M1−M-obs)** and the **NCO** increment.
- **PRESPECIFIED EQUIVALENCE MARGIN:** a null is **informative** only if the M1−M0 increment is inside the
  band **ΔAUROC ≤ 0.005** with a tight CI (upper bound < 0.005) — i.e. the dynamic footprint adds less than
  a clinically negligible amount over the static snapshot.
- **Decision bands (prespecified, per outcome):**
  - **Supportive (H1):** `ΔAUROC(M1−M0)` 95 % CI lower bound **> 0.005** (and > 0), **AND** increment
    **> NCO** increment, **AND** it **survives M-obs** (attenuation < 50 %), **AND** permuted-label
    `ΔAUROC ≈ 0` (CI includes 0).
  - **Adverse / informative negative (H0):** `ΔAUROC(M1−M0)` 95 % CI **upper bound < 0.005** (whole CI inside
    the equivalence band), **or** increment **≤ NCO**, **or** increment **materially attenuated (> 50 %)** by
    adding M-obs.
  - **Inconclusive:** CI **spans** 0.005; or wide CI / miscalibration; or held-out event count below the
    power gate.
- **Permuted-label negative control:** refit M1/M0 with outcomes permuted within the held-out split; expected
  `ΔAUROC ≈ 0`. A non-zero permuted increment signals leakage → result void.

## 9. Falsification criterion

H1 is **falsified** if the dynamic increment does **not exceed** the value-free negative-control (NCO)
increment **and/or** does not survive the M-obs frequency-matched rung (attenuation > 50 %), or if the
held-out `ΔAUROC` CI lies wholly inside the equivalence band. A null then means: routine pre-discharge vitals
carry no incremental trajectory information beyond level and charting frequency (bounded negative), not that
instability is physiologically meaningless.

## 10. What the future solver must newly fit/estimate (deliverable)

Build the frozen cohort; fit **M0, M1, M-obs, NCO** (and optionally M0+M1 combined, A1) on the development
split; evaluate on the held-out split; produce `ΔAUROC`/`ΔAUPRC` with bootstrap CIs, the permuted-label
control, and the per-band verdict of §8. **Completion outputs:** cohort definition + counts; fitted M0
coefficients; a held-out metrics table (AUROC/AUPRC per model + paired deltas + CIs + permuted control); the
supportive/adverse/inconclusive verdict. Reference solution optional (open-ended research).

## 11. Honest limits (accepted)

Single-centre retrospective (MIMIC-IV, one academic centre); binary "unplanned" readmission provenance is
**not** in the archive and **needs clinical adjudication** (MIMIC-IV `notes`, absent here); discharge
destination/bed-pressure confounding adjusted for, not removed; **observation intensity is TESTED (NCO,
M-obs) but not removed** — a surviving increment is prognostic utility, not proof of a distinct mechanism;
all three key works are `abstract_only` inspections. **Association / prognostic-information only — no causal
claim.**

## 12. Key references (inspected; see `key-references.json`)

- **[K1]** Lim L, et al. Multicenter validation of an ML model to predict ICU readmission within 48 h after
  discharge. eClinicalMedicine 2025;81:103112. doi:10.1016/j.eclinm.2025.103112. Inspected: abstract
  (`abstract_only`). Bounds: a pre-discharge 48 h readmission signal is learnable, but the model is opaque
  and not developed on MIMIC-IV.
- **[K2]** Zheng Z, et al. Predictive models for ICU patient readmission based on machine learning: a
  systematic review. J Intensive Care Soc 2026;27(3):308-323. doi:10.1177/17511437261431540. Inspected:
  abstract (`abstract_only`). Bounds: 31 models, pooled AUC 0.82 but all high-ROB; risk 1.3–13.7 %.
- **[K3]** Remoundou K, et al. Mitigating clinical confounding in AI models: associative vs causal-fused AI
  for ICU readmissions. Healthcare (Basel) 2026;14(14):2067. doi:10.3390/healthcare14142067. Inspected:
  abstract (`abstract_only`). Direct rival/limitation: on MIMIC-IV, associative models leaned on
  non-actionable proxies — exactly the observation-intensity/severity artifact the NCO and M-obs rungs test.

Snapshots attached: `K1_snapshot.md`, `K2_snapshot.md`, `K3_snapshot.md` (per-file SHA-256 in the receipts).
