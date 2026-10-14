> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Working proposal — MIMIC-IV island, episode 23 (RESTART, new direction)

Candidate: new restart (no scientific parent). Origin: unused expert seed
`[starting question]` (-> [prior hypothesis]) — "Heterogeneity in the
effects of transfusion".
Status: **DESIGN STAGE. No cohort outcome rows were analysed in discovery.** Itemids,
labitems and columns below were re-read THIS episode directly from the frozen archive
`mimic-iv-3.1.zip` ([source checksum]).
No clinical truth is claimed.

## 1. Unresolved question and its clinical importance

Transfusion thresholds (restrictive Hb ~7-8 g/dL vs liberal ~9-10 g/dL) are the central
uncertainty in ICU transfusion medicine. The TRICC result [K3] left open whether the
subgroup with myocardial ischemia / oxygen supply-demand imbalance is harmed by a
restrictive strategy; the MINT trial tested exactly this in acute MI [K2]; and MIMIC-IV
causal-forest work found measurable heterogeneity of RBC-transfusion effects among septic
patients with Hb 7-9 g/dL [K1] — but that heterogeneity is exploratory and **not**
attributed to a prespecified oxygen supply-demand mechanism, and cannot separate a genuine
supply-demand modifier from confounding by indication (sicker patients get transfused) or
informative measurement (Hb checked more often in unstable patients).

**Hypothesis to test:** at the same pre-decision hemoglobin, the association between
receiving an RBC transfusion and subsequent deterioration differs by a **prespecified
oxygen supply-demand imbalance** state (ischemia / shock / high lactate), i.e. a
transfusion x supply-demand interaction is non-null, and this interaction survives
confounding-by-indication and measurement-intensity controls, whereas a "generic
severity" negative control does not.

**The strongest plausible rival** is not "no effect" but "apparent heterogeneity is
selection": transfusion is a physician decision correlated with instability, so the
modifier could be severity per se, not supply-demand imbalance. The discriminating test
compares the supply-demand interaction against a prespecified severity-only (negative
control) interaction and an informative-measurement (observation-intensity) adjustment.

## 2. Study population, temporal boundaries, variables, outcomes

- Table `mimic-iv-3.1/icu/icustays.csv.gz` (subject_id, hadm_id, stay_id, intime, outtime);
  adults >=18 (patients.csv.gz anchor_age); first ICU stay per hadm_id.
- Hemoglobin (labevents): itemid 51222 (Hematology), 50811 (Blood Gas), 51640 (Chemistry)
  are the candidate Hb series; verified present in `hosp/d_labitems.csv.gz` this episode.
  Pre-decision anchor t0 = first Hb in [intime, intime+24h].
- RBC transfusion (inputevents): itemids **225168 (Packed Red Blood Cells)** and
  **220996 (Packed Red Cells)**; also OR products 226368 ("OR Packed RBC Intake").
  Verified present in `icu/d_items.csv.gz` this episode. Exposure = any RBC unit given in
  (t0, t0+6h].
- Supply-demand imbalance (prespecified, from diagnoses_icd + labs + vitals): acute MI /
  ischemic heart disease ICD-9/10 codes in `diagnoses_icd.csv.gz` (d_icd_diagnoses to map),
  arterial lactate 50813, shock/vasopressor use (inputevents).
- Outcome: composite deterioration = 28-day all-cause in-hospital mortality
  (admissions.deathtime) OR new vasopressor/RRT escalation after t0+6h by day 28.
- Join keys: subject_id / hadm_id / stay_id. Time fields: intime/outtime/deathtime/dischtime.
- Locked split: earliest 70% / latest 30% by icustays.intime (temporal holdout).

## 3. Confounders, baselines, falsification

- Adjustment ladder: M0 (age, sex, SOFA components) -> M1 (+pre-decision Hb, lactate,
  vasopressor) -> M2 (+transfusion-propensity) -> M3 (+Hb measurement-intensity / observation
  features).
- Primary estimand: transfusion x supply-demand interaction OR (logistic) or HR (Cox).
- Baseline method B0: penalized logistic/Cox with the prespecified interaction, fixed
  M0->M3 ladder. Substantive alternative A1: causal-forest / targeted-learning HTE model
  on the same question, refitting the interaction from data rather than assuming it, so a
  genuine non-linear supply-demand modifier can be detected that B0's single interaction
  term may miss; disagreement between B0 and A1 is itself informative.
- **Supportive:** interaction OR>1 in the supply-demand stratum, CI excludes 1, survives
  M0->M3, negative-control (severity-only) interaction null, stable in temporal holdout.
- **Adverse:** interaction null after M0/M1; or the supply-demand interaction is fully
  attenuated by the severity negative control (=> selection/confounding-by-indication
  explains it); or effect present only in the highest measurement-intensity strata.
- **Inconclusive:** wide CI / power gate (few events in the prespecified stratum),
  instability across strata. An imprecise null does not refute the modifier.

## 4. Feasibility, budgets, limits

- CPU-only; MIMIC-IV tabular extraction + penalized regression + a bounded causal-forest
  fit. No GPU required; a GPU is not scientific substitute. Estimated < 1h CPU for the
  full pipeline (future solver envelope: 16 CPU / 256 GB, 28800 s).
- Method-week dependency: n/a (single dataset).
- Honest limits: single-centre retrospective; association, not causal; transfusion is
  confounded by indication; out-of-hospital death unobservable; Hb measurement is
  selective so stratum prevalence/event counts are unverified (power gate applies);
  ischemia is coded/lab-proxy, not adjudicated; a causal/HTE claim needs an RCT or
  external validation.

## 5. Key evidence (three inspected works)

- [K1] Yang P et al. 2025, Front Pharmacol — causal-forest HTE of RBC transfusion in
  septic patients with Hb 7-9 g/dL (MIMIC-IV/MIMIC-III). Supports: heterogeneity exists.
  Limits: exploratory, sepsis-only, subgroup by ITE quantiles not by a prespecified
  oxygen supply-demand mechanism; cannot separate selection.
- [K2] Cooper HA et al. 2026, Crit Care Med — MINT subanalysis, critically ill vs
  noncritically ill AMI+anemia, restrictive vs liberal. Bounds: current RCT evidence in
  the ischemic subgroup.
- [K3] Hebert PC et al. 1999, NEJM (TRICC) — origin of the ischemic-subgroup concern that
  motivates a supply-demand modifier.

## 6. Dispositions for the three demonstrations (domain requirement)

- Cross-organ asynchrony / post-stabilization sedation demonstrations: saturated in
  episodes ~2-20; not re-opened.
- The SHR demonstration (ep-22, [prior hypothesis]) remains the board
  top; kept as anchor, not re-developed this episode to avoid a duplicate.
