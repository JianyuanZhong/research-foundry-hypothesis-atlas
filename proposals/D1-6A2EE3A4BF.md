> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Working proposal - MIMIC-IV island, episode 30 (method/estimand evolution)

Parent (frozen science): `[prior hypothesis]` (ep-29 RESTART onto unused
seed `[starting question]`, "Residual instability before ICU discharge"). This child
**keeps the parent's question, population, temporal split and outcome** and hardens the
**method / estimand / rival-separation** layer only. Origin seed card: `mimic-10.md`
(hypothesis: patients with persistently high oxygen requirement or fluctuating vital signs
before ICU discharge are more likely to return to ICU or die in hospital; limitations to
account for: treatment limitations, discharge destination, competing risk of death).

Status: **design + method-hardening stage. The bounded cohort/power gate is NOT COMPUTED in
this episode** (see §7 COMPUTED vs NOT-COMPUTED). No cohort outcome rows were analysed. This
episode contributes the predeclared method comparison, estimand, error-control and rival
separation, plus three inspected key works. No clinical truth claimed.

## 1. Unresolved claim vs already-supported conclusions

**Already supported (NOT re-tested here):** (a) ICU-readmission prediction models are only
moderately discriminative and confounded by non-actionable proxies [K1]; (b) dynamic
*variability* of time-varying physiologic analytes carries prognostic information in critical
illness [K2]; (c) continuous/ordered vital-sign learning is feasible and can outperform
episodic snapshot monitoring for near-term deterioration [K3]. None of these **separates
pre-discharge within-window variability/trend from the mean level of the same signals**,
none includes a **value-free observation-intensity negative control**, and none targets the
**ICU-discharge decision** with a 7-day readmission/death outcome.

**Unresolved claim the experiment tests (H-instability):** in a fixed pre-discharge window
`[outtime - 12h, outtime]`, within-window **variability/trend and rising O2 requirement** of
continuously charted vitals carry prognostic information for 7-day ICU readmission or
in-hospital death **beyond (i) the mean/last level of the same signals and (ii) observation /
review intensity**.

**Strongest rival (R-level/measurement):** apparent "instability" is fully explained by the
mean severity level at discharge and by who gets watched/charted. Sicker, more-watched
patients generate more vital-sign entries, wider apparent ranges, and denser documentation -
all outcome-correlated but value-free artifacts.

### Distinct, falsifiable predictions (the core separation)
- **H-instability predicts:** variability/trend summaries add discrimination over level-only
  (ΔAUROC(B1−B0) > margin) AND the value-free observation-only model M-obs does NOT reach the
  variability model's performance (M-obs is clearly worse than B1); the learned A1 adds
  discrimination over scalar summaries (ΔAUROC(A1−B1) > margin) because *ordering/shape/
  cross-signal timing* carry signal that SD/IQR/slope compress away.
- **R-level/measurement predicts:** B1 ≈ B0 (equivalence: |ΔAUROC(B1−B0)| within margin) and/or
  M-obs ≈ B1 (observation count/timing alone reproduces "instability" prediction); A1 ≈ B1
  (ordering adds nothing beyond the variability summaries).
- **Both descriptions can hold partly** (level + observation intensity are real and additive):
  the design reports the decomposed ΔAUROC and the M-obs gap, not a single accept/reject.

Note: the observation-intensity concern is *tested, not removed*. A partial M-obs signal does
not by itself refute H-instability, but if M-obs approaches B1, H-instability is **not
identified** and the honest report is inconclusive-with-rival-support.

## 2. Population, temporal boundaries, bindings (inherited, re-verified by parent)

- Source: `[internal dataset path]`
  ([source checksum]; 34 members)
  and `note/discharge_detail.csv.gz` (deferred, secondary). Nested-gzip reader pitfall (parent
  note): `mimic-iv-3.1.zip` members are themselves `.csv.gz`; read the archive member then
  gunzip the member stream (double decompression), not the outer zip alone.
- Unit of analysis: ICU stay (`icu/icustays.stay_id`); keys `subject_id`,`hadm_id`,`stay_id`
  (MIMIC-IV single namespace; never cross-dataset).
- Inclusion: first ICU stay per `hadm_id`; `los >= 1.0` day; discharged **alive** from ICU
  (no `hosp/admissions.deathtime` inside the ICU interval); window fully inside the stay.
- Predictor window: **[outtime − 12 h, outtime]** (pre-discharge information only).
- Outcome (landmark at `outtime`): **7-day unplanned ICU readmission OR in-hospital death**:
  (a) subsequent `icustays` row same `hadm_id` with `intime` in (outtime, outtime+7d];
  (b) `admissions.deathtime` in (outtime, outtime+7d] same `hadm_id`.
- **Locked temporal split by `patients.anchor_year_group`** (same for ALL models): train =
  earliest groups, validation = middle group, test = latest group. (Exact group boundaries are
  set once in the readiness job from observed `anchor_year_group` value counts and then
  frozen; they are NOT computed in this episode.)
- Verified columns / itemids (re-read by the parent from the archive; reused here):
  `icustays(subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los)`;
  `admissions(...,admittime,dischtime,deathtime,...,hospital_expire_flag)` and
  `discharge_location`; `patients(subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod)`;
  `chartevents(subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,
  valueuom,warning)`. Itemids: HR **220045**; arterial MAP **220052**; NIBP MAP **220181**;
  RR **220210**/**224690**; SpO2 **220277**; FiO2 **223835**; temp **223761**/**223762**;
  invasive vent **225792**; non-invasive vent **225794**; PEEP **220339**; O2 device **226732**;
  urine Foley **226559** (dictionary `icu/d_items.csv.gz`). Vasopressor-active uses
  `icu/inputevents.csv.gz` + `icu/d_items.csv.gz`; ventilation-active uses
  `icu/procedureevents.csv.gz` (225792/225794) plus chartevents vent itemids.

## 3. Method comparison on the SAME question and split

All models share the identical cohort, the identical locked temporal split, the identical
label, and the identical test set. Hyperparameters chosen on the validation group only.

- **B0 (interpretable baseline, level-only).** Penalized logistic regression (L2, nested CV
  for λ) on snapshot **level** features: last pre-discharge MAP, HR, RR, SpO2, FiO2, temp;
  vasopressor-active flag; ventilation-active flag; age; sex; ICU LOS. This is what a
  level-only discharge score sees.
- **B1 (primary instability model, interpretable).** B0 **+** within-window per-signal
  variability/trend summaries: SD, IQR, range, coefficient of variation, Theil–Sen slope,
  fraction of time outside reference band, and O2-requirement trend (FiO2 slope, O2-device
  escalation); plus **observation-intensity features** (per-signal measurement counts and
  charting gaps) so that B1 is not merely a proxy for being watched.
- **A1 (substantive learned alternative).** A small **temporal encoder over the irregular
  multivariate 12h series** of the same itemids. Primary specification: a masked recurrent
  encoder (GRU, hidden 64–128, 1–2 layers) over a time-binned series with **(i)** per-signal
  observation masks and **(ii)** a "time-since-last-value" channel, concatenating all signals
  so the model can learn **cross-signal coupling timing**. Secondary specification if A1 is
  unstable: an **irregular-time attention encoder** (transformer with continuous-time /
  time-since-observation embeddings) or a **functional/GP summary** across the window.
  Inputs identical to B1's raw streams; target and split identical.
  **Why A1 can reveal what B1 loses:** scalar summaries (SD/IQR/slope) are permutation- and
  shape-invariant — they discard the *order*, *trajectory shape* (e.g., monotone decline vs
  transient dip then recovery), *timing* (instability concentrated at the end of the window),
  and *cross-signal coupling timing* (HR rise preceding RR rise; SpO2 fall coupled with
  FiO2/PEEP escalation). A1 can exploit those; B1 cannot by construction.
- **M-obs (value-free observation-frequency negative control).** Penalized logistic on ONLY
  value-free cadence features: per-signal counts of chart events in the window, charting-gap
  statistics, number of distinct `caregiver_id`, presence/timing of new device documentation.
  No physiologic value enters. If M-obs ≈ B1, the "instability" signal is not identified.
- **Label-permutation control.** Fit B1 and A1 on outcome labels permuted within the training
  split; expected ΔAUROC ≈ 0 (guards leakage/overfitting).

### Primary and secondary estimands
- **Primary:** ΔAUROC(**B1 − B0**); ΔAUROC(**A1 − B1**). Predeclared **equivalence margin 0.01**
  AUROC (|Δ| < 0.01 = equivalence / no material increment).
- **Secondary:** calibration (slope, intercept, Brier); decision-curve **net benefit** over
  clinically relevant thresholds at the observed 7-day event rate; **M-obs vs B1** gap.
- **Uncertainty:** **bootstrap cluster CIs (1000 resamples, clustered by `subject_id`)** for
  every ΔAUROC; report point estimate + 95% CI; conclusions keyed to the CI, not the point.
- **Secondary outcome decomposition (competing risk):** repeat with (i) readmission-only and
  (ii) death-only outcomes, and a **cause-specific / Fine–Gray competing-risk** check treating
  death as a competing event for readmission.

### Resource and time budget (A100 available via `ehr_job_submit(gpus=1)`)
- B0/B1/M-obs penalized logistic on CPU: seconds–minutes (ESTIMATED; not run here).
- A1 GRU (~0.05–0.5M params), series ≤ ~720 hourly bins × ~10 channels, tens of thousands of
  stays, 5 seeds × (train/val/test): **ESTIMATED 1–3 A100 GPU-hours, < 8 GB**; CPU fallback
  feasible but slower. **NOT measured; no compute launched in this episode.**
Constraints must respect `inputs.json.compute_limits`; discovery vs solver budgets are
separate and no expensive pilot is required here.

## 4. Predeclared SUPPORTIVE / ADVERSE / INCONCLUSIVE outcomes

Keyed to the 95% cluster-bootstrap CI of the relevant ΔAUROC, margin **0.01**:
- **SUPPORTIVE (H-instability):** ΔAUROC(B1−B0) CI excludes the equivalence band on the
  positive side AND ΔAUROC(A1−B1) CI excludes it on the positive side AND M-obs is clearly
  below B1 (CI gap > margin). Meaning: pre-discharge variability/trend, and ordered signal
  beyond scalar summaries, add discrimination not explained by level or watching.
- **ADVERSE (R-level/measurement):** ΔAUROC(B1−B0) CI entirely within the equivalence band
  (levels suffice) OR M-obs ≈ B1 (CI within band). Meaning: the apparent instability signal is
  level and/or observation-intensity; the leading claim is not identified.
- **INCONCLUSIVE (informative negative allowed):** CIs too wide to separate from the margin
  (underpowered) OR an intermediate pattern (B1−B0 > margin but A1−B1 within band, etc.).
  Report as inconclusive with the observed point estimates and the M-obs gap; do not upgrade
  to supportive. **A too-wide CI is not refutation.** The label-permutation ΔAUROC must be ~0
  or the run is invalid (leakage).

## 5. Strongest alternative explanations (addressed, not "adjusted away")

- **Discharge destination / treatment-limitation confounding:** a patient sent to a ward,
  step-down, or hospice/palliative pathway differs in readmission/death risk for reasons other
  than physiology. Available covariate: `admissions.discharge_location`. Sensitivity: stratify
  / adjust for discharge destination; and exclude/adjust for documented treatment-limitation
  (code-status / comfort-measures) where identifiable. **Treatment-limitation / code-status
  itemids are NOT verified this episode and require adjudication** (a required dependency, not
  assumed present).
- **Competing risk of death:** death precludes ICU readmission. Mitigated by the composite
  primary outcome, by reporting readmission-only and death-only endpoints separately, and by a
  cause-specific / Fine–Gray competing-risk secondary analysis. Interpret the composite as a
  discharge-safety signal, not a readmission mechanism.
- **Selection by who gets charted:** information-content features (density/cadence) are
  outcome-correlated. Mitigated by B1's explicit observation-intensity features and by the
  value-free **M-obs** negative control; if M-obs approaches B1 the claim is not identified.
- **Predictive utility vs causal/mechanistic claim:** all conclusions are prognostic
  association only. A positive ΔAUROC does NOT establish a mechanism or that acting on
  variability improves outcomes; that needs an interventional study.

## 6. Reporting contract for the future solver

Report, on the locked test set: B0/B1/A1/M-obs AUROC with cluster-bootstrap CIs, both ΔAUROC
with the 0.01 equivalence band, calibration slope/intercept and Brier, decision-curve net
benefit at the observed event rate, the M-obs−B1 gap, and the label-permutation ΔAUROC.
Report sex/age/LOS summaries and the anchor_year_group boundaries actually used. Mark any
clinical-adjudication-dependent field explicitly.

## 7. COMPUTED vs NOT-COMPUTED (this episode)

- COMPUTED: itemid/column/path bindings reused verbatim from the parent's archive inspection;
  three key works inspected (K1/K2 abstract_only; K3 full_text targeted sections); attached
  source snapshots hashed (see `key-references.json`).
- NOT-COMPUTED (honest open items): the **bounded cohort/power gate** (cohort size, primary
  event count, per-split counts, `anchor_year_group` value counts, equivalence-margin
  feasibility); any model fit; the nested-gzip reader is described but not executed here.
  These remain a first-class **readiness check**, not a passed result. An underpowered or
  under-prevalent gate legitimately yields INCONCLUSIVE.

## 8. Key references

- **[K1]** Remoundou K, Koumantakis E, Roussaki I (2026). *Mitigating Clinical Confounding in
  AI Models: A Comparative Analysis of Associative and Causal-Fused AI for ICU Readmissions.*
  Healthcare (Basel) 14(14):2067. doi:10.3390/healthcare14142067. PMID 42512583. - bounds the
  claim: MIMIC-IV 30-day ICU-readmission models reach only moderate AUROC (~0.65–0.73) and lean
  on non-actionable proxies; readmission prediction is confounded. (abstract_only)
- **[K2]** Zhang J, Zhang W, Zeng B, Xie L, Zhu J (2026). *Dynamic Variability of Sodium and
  Potassium Predicts Mortality in Critically Ill Patients With Ischemic Stroke.* Brain Behav
  16(9):e71626. doi:10.1002/brb3.71626. PMID 42696496. - supports
  transfer: dynamic *variability* carries prognostic information in critical illness, but does
  not separate variability from level and does not control measurement frequency. (abstract_only)
- **[K3]** Scheid MR, Friedmann B, Oppenheim M, Hirsch JS, Zanos TP (2025). *Development and
  validation of a clinical wearable deep learning based continuous inhospital deterioration
  prediction model.* Nat Commun 16:9513. doi:10.1038/s41467-025-65219-8. PMID 41184270. -
  supports A1's premise: ordered/continuous vital-sign learning (RNN over 9 continuous inputs,
  888 patients) is feasible and continuous monitoring can catch change that episodic monitoring
  misses; it is non-ICU, 24h-horizon, and does not separate variability from level. (full_text,
  targeted sections)

Additional inspected context (not a key-ref slot): the parent's frozen design and the seed
card `mimic-10.md`, which flags treatment limitations, discharge destination and competing
risk of death as the required confounders this design now addresses explicitly.

## 9. Honest limits

Single-centre retrospective; prognostic-information claim only, **no causal/mechanistic
claim**; "unplanned" readmission provenance needs clinical adjudication (notes, deferred);
treatment-limitation/code-status covariates need verification (adjudication dependency);
observation intensity is tested not removed; power/cohort gate and temporal-split boundaries
are open readiness items (NOT computed here). Child of the parent; population, window, split
and outcome are unchanged.
