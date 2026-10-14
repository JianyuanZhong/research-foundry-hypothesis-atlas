> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Working proposal — MIMIC-IV island, episode 40 (Lead evolution)

Parent (scientific ancestry): `[prior hypothesis]` (board leader, mu 33.73, 10
comparisons, valid, reference_delivery complete). Operation: **evolve** (goal recorded in
`choose_work`, board_revision 407). Branch: SHR / relative-glycemia adversarial falsification.
This is a different branch from the episode-39 readmission evolution, so it is not marginal
repetition of the immediately prior episode.

Status: **DESIGN STAGE + one EXECUTED bounded feasibility probe** (`work/[producer attribution withheld]/work/ep40-evolution/binding-probe.txt`).
No cohort outcome rows were analysed; no outcome model was fit. Every number is labelled
COMPUTED or NOT-COMPUTED. No clinical or causal truth is claimed.

## 0. Hypothesis vs already-supported conclusion

Already supported (NOT the novel claim): relative glycemia (stress hyperglycemia ratio,
SHR = admission glucose / HbA1c-derived chronic glucose) is *associated* with short-term ICU
mortality in MIMIC-IV and in a second cohort [K1]; lab-test order-presence/timing can predict
survival, so observation processes can manufacture prognostic signal. The parent already
predeclared an equivalence-margin ladder: M0 severity < M1 +relative glycemia < M2 +shared
latent factor < M3 observation intensity, with falsifiers S1 label-permutation, S2 value-free
measurement-only negative control, S3 negative-control outcome, S4 within-subject discordance.

Unresolved claim this experiment tests (the substantive advance): the parent leaves its
strongest rival — a **patient-level** chronic-frailty + testing-propensity common cause —
only "bounded, not eliminated" by cross-sectional (between-subject) adjustment. This child
asks, and makes falsifiable, two questions the parent does not:

- **Q-A (within vs between).** Is the SHR–mortality increment a *stay-level acute-severity*
  signal, or mainly a *between-patient* marker of time-invariant frailty/comorbidity and each
  patient's testing propensity? These differ on the within-subject contrast: if the SHR
  coefficient reverses toward/below zero (or loses the increment) when estimated *within*
  subject across a patient's repeated ICU stays, the cross-sectional signal is dominantly
  between-patient.
- **Q-B (decision relevance).** Even if the increment is nonzero, does it change decisions at
  clinically plausible thresholds? This is a decision-curve net-benefit question, not an
  incremental-AUC question.

Closest inspected work [K1] reports only between-subject trajectory associations and no
within-subject decomposition or net-benefit analysis; [K2] bounds the effect (attenuation,
non-sepsis null); [K3] supports the rival that SHR behaves as a non-specific severity/monitoring
correlate (SHR predicted 72-h delirium and had no significant direct mortality effect after
mediation). The strongest rival is therefore R-nonspecific/R-frailty, and it is separable from
the leading claim H-acute on the Q-A contrast.

## 1. Population and temporal boundaries (frozen)

- Source (read-only): `[internal dataset path]`,
  [source checksum] (declared in `datasets/mimic/README.md`;
  not re-hashed this episode — member list/headers were read directly).
- Members (COMPUTED this episode): 34 zip members, 31 `.csv.gz`. No `ed/` module in this archive.
- Primary cohort (parent, unchanged): adults ≥18 (hosp/patients.anchor_age, gender), **first ICU
  stay per subject** (`icu/icustays`, min `intime`), `stay_id` key.
- NEW within-subject cohort (COMPUTED this episode): subjects with ≥2 ICU stays = **16,242
  subjects / 45,334 stays**; single-stay = 49,124; subjects with ≥2 `hadm_id` = 11,743. This
  cohort is what makes Q-A estimable.
- Anchor `t0` = ICU `intime` of the index stay. Predictor window `[t0-6h, t0+24h]` (parent).
- Outcome: 28-day mortality = death ≤ t0+28d via `hosp/admissions.deathtime` joined on `hadm_id`.
- One locked temporal split (70/30) by index `intime`, boundary recorded at fit time; no
  re-splitting after peeking.

## 2. Variables, tables, join keys, time fields

- `icu/icustays`: `subject_id, hadm_id, stay_id, intime, outtime, los` (keys/join).
- `hosp/patients`: `subject_id, anchor_age, gender`.
- `hosp/admissions`: `subject_id, hadm_id, admission_type, deathtime`.
- `hosp/labevents` (glucose `50931`; HbA1c `50852`+`50854`; via `hosp/d_labitems` itemid
  labels): `subject_id, hadm_id, itemid, charttime, value, valuenum`. Admission glucose = first
  value in window; chronic glucose = HbA1c-derived (HbA1c→eAG); `SHR = admission_glucose / eAG`.
- Observation intensity (R-select): count of glucose + other lab measurements per stay in the
  window; a value-free measurement-only indicator is the S2 negative-control exposure.
- Severity block M0: age, first `SOFA`-proxy items (GCS/MAP/lactate/creatinine itemids as used
  by prior accepted children), admission type.
- Alternative within-subject estimator uses repeated stays of the same `subject_id`.

## 3. Estimands, baselines, analysis

- Primary (parent, retained): ΔAUC = AUC(M1) − AUC(M0) for 28-day mortality, with equivalence
  margin ΔAUC ≤ 0.005 (informative null).
- NEW Q-A: between-subject vs within-subject SHR contrast. Fit (i) a between-subject penalized
  logistic (B0 baseline) and (ii) a conditional/fixed-effects model (conditional logistic by
  `subject_id`, or within-subject demeaned/strata) among multi-stay subjects. Report both SHR
  coefficients with bootstrap CIs and the difference Δcoef = β_within − β_between.
- NEW Q-B: decision-curve net benefit NB(threshold) for M0 vs M1 at thresholds 5%/10%/20%;
  ΔNB = NB(M1) − NB(M0), equivalence margin ΔNB ≤ 0.005 (informative null), reported with
  bootstrap CIs and a decision-relevance band.
- Method comparison (recorded): **B0** interpretable penalized logistic (baseline). **A1**
  joint measurement-selection + outcome model that models the testing process and the outcome
  jointly (what A1 reveals that B0 loses: whether the SHR coefficient survives once the
  observation/order process is modelled rather than only adjusted). **A2** conditional
  within-subject model (Q-A). A small irregular-time encoder is a deferred alternative for the
  future solver (only if B0/A1 leave the measurement process unresolved).

## 4. Falsification criteria and interpretation

Retained falsifiers: S1 label-permutation ΔAUC ≤ 0.005; S2 value-free negative-control
exposure equivalence; S3 negative-control outcome; S4 within-subject discordance.

- **Q-A supportive (H-acute)**: Δcoef ≈ 0, i.e. the within-subject SHR coefficient is preserved
  (CI overlaps between-subject coefficient) and the within-subject increment stays > 0.
- **Q-A adverse (R-frailty/R-nonspecific)**: Δcoef strongly negative or within-subject SHR
  coefficient ≈ 0 / reversed with a CI excluding the between-subject coefficient ⇒ the signal
  is dominantly patient-level, not stay-level. This is a valuable NEGATIVE finding.
- **Q-A inconclusive**: wide CI spanning both equivalence-relevant alternatives or too few
  multi-stay subjects with events in the window (report exact N_anchor/events_anchor).
- **Q-B supportive (decision-relevant)**: ΔNB > 0 with CI lower > 0 at ≥1 prespecified threshold
  and consistent sign across thresholds.
- **Q-B adverse (decision-irrelevant)**: ΔNB ≤ 0 or CI includes 0 at all thresholds ⇒ an
  informative-null/negative result.
- **Q-B inconclusive**: sign disagreement across thresholds with wide CIs.

Overall: support requires the ladder increment surviving S1–S4 **and** either a preserved
within-subject coefficient or a positive ΔNB (predeclared); otherwise the honest report is
adverse or inconclusive. A null is not refutation of the platform association.

## 5. Honest limits

Design stage + one bounded feasibility/cohort probe only. Outcome-model magnitudes, N_anchor,
events_anchor, Δcoef and ΔNB are **NOT-COMPUTED**. HbA1c validity in CKD/anaemia and the
negative-control "no glycemia mechanism" assumption require clinical adjudication. Measurement
selection is bounded by predeclared tests, not eliminated. Single-centre retrospective;
association / incremental-prognostic-information only; no causal or mechanistic claim. The
multi-stay cohort size (16,242) is COMPUTED; its event yield in the window is NOT-COMPUTED.

## 6. Three-demonstration dispositions (recorded)

1. *Learning the natural history of human disease with generative transformers* — not pursued;
   the longitudinal generative foundation model needs a pretraining scale outside the frozen
   discovery budget (the bounded irregular-time sequence model is the recorded adaptation
   already deferred on this branch).
2. *Advancing cancer detection using longitudinal routine clinical data* — blocked: the main
   article and STAR Methods returned HTTP 403/401; only the supplement is present, so its
   methods cannot be inspected or reproduced here.
3. *A Bayesian framework for longitudinal EHR and genetic discovery* — blocked: no genotype
   modality in the MIMIC snapshot; genetic discovery is not resolvable.

## 7. Key references

[K1] Wu & Wang 2026, Front Endocrinol, doi:10.3389/fendo.2026.1909554 (abstract-only).
[K2] Chen, Ren & Sun 2026, Research Square preprint, doi:10.21203/rs.3.rs-10754094/v1 (abstract-only).
[K3] Huang et al. 2026, Metabolism Open 31:100490, doi:10.1016/j.metop.2026.100490 (abstract-only).
Structured receipts in `work/key-references.json`; snapshot bytes in `work/evidence/`.
