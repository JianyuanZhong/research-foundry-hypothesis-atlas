> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Working proposal — MIMIC-IV island, episode 25 (EVOLUTION crossover: separable estimand × HbA1c-independent anchor)

Branch: `work/evo-shr-crossover/` (this actor, `[producer attribution withheld]`).
Operation **crossover**, seq 0, board_revision 225.
Parents (from `choose_work`): `[prior hypothesis]` (separable additive/log-ratio estimand,
mu 33.50, valid) × `[prior hypothesis]` (HbA1c-independent chronic-glycemia anchor,
mu 32.08, valid). Both are children of `[prior hypothesis]` (unused expert seed
`[starting question]`, "Acute glucose elevation relative to chronic glycemia").

Status: **DESIGN + BOUNDED BINDING VERIFICATION. No cohort outcome rows were analysed.**
Itemids/columns/keys were re-verified THIS episode directly against the frozen archive
`mimic-iv-3.1.zip` ([source checksum]);
probe transcript in `work/evo-shr-crossover/evidence/binding-verify-2026-10-13.txt`. **No clinical truth is claimed.**

## 0. What this crossover adds (the two remaining defects repaired together)

The SHR (stress-hyperglycemia-ratio) program has two admitted defects that the two parents fixed
**separately** but never **together**:

1. **Non-identifiability of "independent SHR."** `SHR = G_adm / (28.7·HbA1c − 46.7)` shares its
   numerator with absolute admission glucose `G_adm`. Entering "SHR" and "absolute glucose" together
   in one logistic model is near-degenerate, so *any* result (null or positive) is hard to interpret.
   Parent `ca6f5e81` repairs this by a **prespecified additive decomposition**: enter `G_adm` and the
   chronic-glucose term `Gc` separately as **full-rank** terms and read the **separable log-ratio**
   contrast `RG = log G_adm − log Gc` (equivalently the linear contrast `β_{G_adm} − β_{Gc}`), with a
   decisive **M1→M2** discrimination contrast.
2. **Dependence on selectively measured same-stay HbA1c.** In ICU, HbA1c is measured in a
   severity/dysglycemia-enriched subset, so "chronic glycemia = same-stay HbA1c" makes the exposure
   partly a cohort-composition variable. Parent `913a1b` repairs this by an **HbA1c-independent
   chronic anchor**: the most recent glucose/HbA1c from a **strictly earlier `hadm_id`**, or an
   outpatient `omr` value, within a **365-day pre-index lookback** joined by `subject_id` across
   `hadm_id`, so the primary acute-vs-chronic contrast does **not** use same-stay HbA1c.

This crossover applies **both** fixes to one estimand: a **collinearity-free** relative-glycemia
estimate whose chronic term comes from an **HbA1c-independent anchor**. The substantive gain is
that the M1→M2 increment can now be attributed to *relative glycemia* rather than to the
HbA1c-measurement-selection mechanism that both parents could only condition on.

## 1. Unresolved question and clinical importance

SHR is being promoted as a "readily available, cost-free tool for clinical risk stratification" and
trial-enrichment marker [K1], and is used as an exposure for downstream outcomes [K1]. The unresolved
question is **what the SHR/relative-glycemia association is**:

> Does the *relative* (acute-on-chronic) glycemia component add **28-day mortality** information
> **beyond absolute admission glucose and severity**, and is that increment **separable** from
> (i) selective measurement of same-stay HbA1c and (ii) HbA1c invalidity in acute illness?

**Consequence of resolving.** If the relative component is separable and the increment survives
removing same-stay HbA1c dependence and measurement-propensity weighting, then a
metabolic-reserve / acute-on-chronic axis is defensible for triage or trial enrichment. If the
increment dies at M1→M2 (R-absolute) or tracks measurement selection (R-select), then SHR should
**not** be adopted as a stratification/enrichment marker, preventing a redundant biomarker from
entering practice or trial design. Either direction changes a decision; an honest **inconclusive**
(power-gate failure) also changes the decision (defer pending larger anchored data).

## 2. Already-supported evidence vs the untested claim

**Supported by inspected evidence (not re-tested here):**
- SHR is *associated* with short-term/28-day mortality in selected ICU populations (K1: adjusted
  HR 1.37, 95% CI 1.15–1.64 in MIMIC-IV v3.1; K3: nonlinear threshold association). This is a
  largely settled *association*, not the question tested here.
- HbA1c/SHR is **selectively observed** in MIMIC-IV; a prior author explicitly concedes that many
  eligible patients were excluded because SHR was incalculable due to missing glucose/HbA1c, "which
  may have introduced selection bias" (K3). This supports the R-select rival's premise.
- Methodological: negative controls are a recognized bias-detection tool but require explicit
  feasibility/validity reasoning and interpretation rules (K2).

**Untested claim this experiment tests (hypothesis, not conclusion):**
- At the same absolute admission glucose and severity, the relative glycemia component carries
  **incremental prognostic information** that is **identifiable** without same-stay HbA1c and does
  **not** reduce to measurement selection. This is an **incremental-prognostic-information /
  separability** claim. It is *not* a causal or mechanistic claim.

## 3. Four rivals and their differing observable predictions

All four are discriminated on the **same fitted outputs** (no peeking/re-labelling):

- **H-relative (leading).** Relative elevation identifies risk at the same absolute glucose.
  Prediction: `Gc`/`RG` term is non-null with sign implying higher risk at high acute / low chronic
  glucose; the M1→M2 increment holds; the increment **survives** measurement-propensity IPW;
  negative-control EXPOSURE (anchor `Gc` alone) is null or clearly smaller/differently shaped;
  negative-control OUTCOME is null; smooth (monotone-rising) RCS dose-response.
- **R-absolute (rival).** Only absolute glucose and severity matter. Prediction: `Gc`/`RG` adds
  ~0 discrimination beyond M1; CI includes 0; negative controls null.
- **R-select (rival, informative measurement).** "HbA1c measured" is a severity/dysglycemia-selected
  event; apparent effects are cohort composition. Prediction: the `RG` effect **attenuates markedly**
  under measurement-propensity IPW; the **negative-control OUTCOME** shows a parallel (non-null)
  signal; anchored-vs-unanchored population differs in severity; A1 attributes a large share of the
  M1→M2 increment to the selection channel.
- **R-validity (rival, measurement error).** HbA1c is unreliable in acute illness (anemia,
  transfusion, renal failure). Prediction: the effect is **unstable across anemia/transfusion/renal
  strata** and **shrinks** under measurement-error / error-in-variable correction; A1's measurement
  submodel absorbs it. (Note: because the *primary* anchor is prior-admission/OMR, R-validity bears
  on the same-stay-HbA1c sensitivity arm and on any HbA1c-derived anchor; it is bounded, not removed.)

Separation logic: H-relative survives glucose adjustment **and** IPW **and** a null negative control;
R-absolute dies at M1→M2; R-select shows strong IPW attenuation plus a non-null negative-control
outcome; R-validity shows stratum instability.

## 4. Population, temporal boundaries, variables, outcomes (frozen design)

**Source.** Frozen archive `mimic-iv-3.1.zip`; members
`mimic-iv-3.1/hosp/{labevents,d_labitems,admissions,patients,diagnoses_icd,d_icd_diagnoses,omr}.csv.gz`
and `mimic-iv-3.1/icu/{icustays,chartevents}.csv.gz`.

**Population.** Adults `patients.anchor_age ≥ 18` with a **first ICU stay per subject**
(min `icustays.intime` per `subject_id`), a measurable **admission glucose**, and a measurable
**HbA1c-independent chronic anchor** (§4 anchor). Exclusion: no anchor; admission glucose outside
`[20, 600] mg/dL`; duplicate/degenerate timestamps.

**Index time `t0` = first `icustays.intime` (per subject).**
- **Admission glucose `G_adm`** = first `labevents` glucose in `[t0 − 6h, t0 + 24h]`, itemid
  **50931** (Glucose/Chemistry); sensitivity **50809** (Glucose/Blood Gas), **52027**
  (Glucose, Whole Blood/Blood Gas), **52569** (Glucose/Chemistry). `valuenum` in mg/dL.
- **Same-stay HbA1c** = itemid **50852** ("% Hemoglobin A1c"); sensitivity **50854** ("Absolute A1c")
  in `[t0 − 24h, t0 + 24h]` — used **only** for the negative-control EXPOSURE and the sensitivity arm,
  **never** for the primary chronic anchor.
- **HbA1c-independent chronic anchor `Gc`** (primary): most recent prior value **before `t0`** within a
  **365-day lookback**, joined by `subject_id` across `hadm_id`:
  (a) prior-admission **glucose** `labevents` value from a strictly earlier `hadm_id`
      (`charttime < t0`, same glucose itemids), or
  (b) prior-admission **HbA1c** (itemid 50852) converted by the ADAG relation
      `Gc = 28.7·HbA1c% − 46.7` mg/dL, or
  (c) outpatient `hosp/omr` glucose/HbA1c row (`result_name` matching glucose/A1c-style rows) before `t0`.
  Preference order (a) → (b) → (c), most recent first; the chosen source and its `charttime` are recorded.
- **Primary relative exposure** `RG = log G_adm − log Gc` (equivalently, fit `G_adm` and `Gc` as two
  full-rank additive terms and read the `β_{G_adm} − β_{Gc}` contrast). RCS on `Gc` for shape.
- **Negative-control EXPOSURE:** the chronic-anchor glycemia `Gc` **alone** (no acute term),
  pre-registered to be **null** after adjustment.
- **Primary OUTCOME:** **28-day all-cause mortality** from `admissions.deathtime` (event = death within
  28 days of `t0`); when `deathtime` is null the subject is censored at `admissions.dischtime` →
  **hospital-recorded mortality only** (out-of-hospital death unobservable; see §9).
- **Negative-control OUTCOME:** a pre-specified in-hospital **non-glycemic deterioration** composite
  that glycemia should not plausibly drive (lead candidate: new renal-replacement dialysis initiation,
  item-bound from ICU procedure/event tables — final itemid selection requires **clinical adjudication**,
  see §9). Pre-registered to be null.
- **Covariates (severity / confounders):** `anchor_age`, `gender`, `admission_type`, known-diabetes
  flag (`diagnoses_icd` + `d_icd_diagnoses`), sepsis flag, baseline creatinine (itemid **50912**/*52546*),
  anemia flag, transfusion flag, a SOFA-style severity score from `chartevents`/`labevents`.
- **Adjustment ladder (prespecified):**
  - **M0** = age + sex + severity (base)
  - **M1** = M0 + absolute admission glucose `G_adm`
  - **M2** = M1 + chronic term `Gc` entered separately (full-rank) → **decisive M1→M2 contrast**:
    does the relative term add beyond absolute glucose? Report LR-test Δ and ΔAUROC(held-out 30%).
  - **M3** = M2 + **measurement-propensity IPW** (propensity for the chronic anchor being observed from
    severity/measurement-intensity covariates) + negative-control exposure/outcome fits.
- **Split (locked):** earliest **70%** / latest **30%** by `icustays.intime`; MIMIC-IV date-shifting
  makes this an ordering proxy, not calendar time. The 30% hold-out is used for the ΔAUROC and the
  M1→M2 confirmation; **no re-peeking**.

## 5. Analysis

- Primary: **ΔAUROC (M1→M2)** on the held-out 30% with bootstrap CI; likelihood-ratio test for the
  `Gc` term; RCS shape over `Gc`; E-value for the `Gc`/`RG` coefficient (bias magnitude needed to
  explain it away).
- Measurement-selection: M2 vs M3 IPW-attenuation of the `Gc`/`RG` coefficient.
- Negative controls: fitted effect of chronic-anchor `Gc` alone (exposure) and of the non-glycemic
  deterioration composite (outcome).
- Stratum stability (R-validity): coefficient across anemia/transfusion/renal strata.
- "Relative" estimand reported two equivalent ways: separable additive `β_{G_adm} − β_{Gc}` contrast
  and the log-ratio `RG` model, to make the reparametrization explicit.

## 6. Bounded power gate (prespecified; a legitimate INCONCLUSIVE outcome)

Proceed to outcome inference **only if** the primary analysis set has
**≥ 300 anchored patients AND ≥ 60 recorded 28-day deaths**, and each of the anemia, transfusion and
renal strata has **≥ 40** anchored patients. Otherwise the branch is **INCONCLUSIVE by design**
(defer to larger anchored data), *not* a negative result. These thresholds are deliberately set so
that a modest absolute glucose increment of clinical interest is detectable; they are a gate, not a
rescaled surrogate for the phenomenon.

## 7. Method exploration (same question): baseline B0 vs substantive alternative A1

- **B0 (simple, interpretable, CPU):** penalized **L2 logistic regression** on M0–M3; outputs adjusted
  ORs with CIs, LR-test and ΔAUROC for M1→M2, RCS shape, E-value. Minutes on CPU.
- **A1 (substantive alternative, CPU, < 1 h):** **selection-aware joint latent measurement-selection +
  outcome model** — a two-equation model that (i) models the probability that the anchor / same-stay
  HbA1c is *measured* (selection equation) and (ii) models the outcome with a **latent factor shared**
  between selection and outcome; fitted by **expectation–maximization**.
- **What A1 reveals that B0 cannot:** R-select is a *latent-selection* problem. If inclusion into
  "has a chronic anchor" (and/or same-stay HbA1c) depends on an unmeasured factor that also affects
  death, B0's IPW-adjusted coefficient is still biased and B0 **cannot say by how much**; A1 identifies
  and **quantifies** the selection channel. Negligible A1 selection contribution strengthens
  H-relative; a large contribution supports R-select. Neither B0 nor A1 establishes mechanism.
- **Why not more complex:** a neural/sequence model is not scientifically needed here — the estimand
  is a low-dimensional separability contrast; complexity would not change the discriminating
  comparison. **No GPU is required or requested.**

## 8. Scientific deliverable and completion

Deliverable: a **newly fitted B0 and A1** on the frozen cohort producing
(i) adjusted `G_adm` and `Gc`/`RG` effect estimates with CIs and RCS shape,
(ii) the **M1→M2** LR-test/ΔAUROC with bootstrap CI on the held-out 30%,
(iii) the **measurement-selection decomposition** (M2 vs M3 IPW; A1 selection share),
(iv) **negative-control** exposure and outcome results,
(v) the **E-value**, and
(vi) the **power-gate verdict** (proceed / inconclusive).
These six outputs establishing completion — not a p-value alone.

## 9. Honest limits, missing evidence, clinical adjudication

- Single-centre retrospective MIMIC-IV; **association / incremental-prognostic-information only**,
  no causal or mechanistic claim.
- **Mortality is hospital-recorded** (`admissions.deathtime`); out-of-hospital death is not observable
  in the configured tables → 28-day mortality is partly interval-censored. National Death Index
  linkage is **not available**.
- HbA1c reliability in acute illness (anemia, transfusion, renal failure) is a **clinical/laboratory
  adjudication** issue; R-validity can only be bounded, not resolved here.
- The **negative-control outcome itemid needs clinical adjudication** (a decision, not a computation);
  the composite is imperfect.
- The **anchor population is itself selected** (patients with prior records differ); the power gate
  and A1's selection equation address but do not remove this.
- **Cross-facility anchoring assumption:** only same-`subject_id` records inside MIMIC-IV are used;
  prior glycemia from outside the system is unobservable. `omr` two-decimal `result_value` must be
  parsed and non-glucose rows filtered.
- **Not measured this episode:** full-file anchored cohort size, HbA1c-measurement prevalence, and
  event count — the power gate is **unresolved** until a bounded compile/readiness job computes them.
- Mechanism-level claims (microcirculatory vs stress) require **another study**; external validation
  would require a second centre.

## 10. Data bindings (verified this episode against the frozen archive)

- Archive: `[internal dataset path]`,
  [source checksum] (matches
  `datasets/mimic/README.md`). Members and columns confirmed: `icustays` (subject_id,hadm_id,stay_id,
  intime,outtime,los), `admissions` (hadm_id,admittime,dischtime,deathtime,admission_type,
  hospital_expire_flag), `patients` (subject_id,gender,anchor_age,anchor_year,dod), `omr`
  (subject_id,chartdate,seq_num,result_name,result_value), `labevents` (labevent_id,subject_id,hadm_id,
  itemid,charttime,valuenum,valueuom), `d_labitems` (itemid,label,fluid,category).
- `d_labitems` rows re-read **this episode**: 50931 Glucose/Chemistry; 50809 Glucose/Blood Gas;
  52027 "Glucose, Whole Blood"/Blood Gas; 52569 Glucose/Chemistry; 50852 "% Hemoglobin A1c"/Chemistry;
  50854 "Absolute A1c"/Chemistry; 50912 Creatinine/Chemistry; 52546 Creatinine/Chemistry.
- **Join keys:** `subject_id`, `hadm_id`, `stay_id`. Cross-admission anchor joins a subject's earlier
  `hadm_id` by `subject_id` and `charttime < t0`. **MIMIC-IV only — never join across datasets.**
- **Time fields:** `charttime` (labs/omr day), `intime`/`outtime` (icustays), `admittime`/`dischtime`/
  `deathtime` (admissions).

## 11. Disposition of the three research-ambition demonstrations (brief)

- **Natural-history generative transformer** (Nature 2025, DOI 10.1038/s41586-025-09529-3): **not
  pursued** — the ambition (unsupervised disease-trajectory generation) is out of scope for a
  falsifiable glycemia-separability test; would require a longitudinal sequence corpus and GPU
  training far beyond this question's estimand. Documented, not attempted.
- **Longitudinal routine-clinical-data cancer detection** (Cell 2026, DOI 10.1016/j.cell.2026.07.009):
  **explicit missing dependency** — main article/STAR Methods unavailable (403/401); no inspection of
  the method claimed. Not adapted.
- **Bayesian longitudinal EHR+genetic discovery** (Nature 2026, DOI 10.1038/s41586-026-10780-5):
  **data-bound adaptation declined here** — the genetic component has no binding in the MIMIC-IV
  island (no genotype data); a Bayesian variant of the selection model (A1) is retained in principle
  as a bounded CPU alternative, not as a genetic framework. Recorded for completeness.

## 12. Key works [K1][K2][K3]

Bibliography and receipts in `work/evo-shr-crossover/key-references.json`; inspected excerpt snapshots
in `work/evo-shr-crossover/evidence/` (abstract_only; bytes hashed in the receipts).

- **[K1]** Wu Y, Wang K. 2026. *Front Endocrinol (Lausanne)* 17:1909554, DOI 10.3389/fendo.2026.1909554.
  SHR trajectory prognostic work in MIMIC-IV v3.1: Class-3 vs Class-1 adjusted HR 1.37 (1.15–1.64);
  "the persistently high trajectory reflected acute glycemic deviation from the **HbA1c-defined**
  background"; membership driven by HbA1c **and** first-12h glucose together. Supports the H-relative
  reading but shows the HbA1c-defined chronic anchor and absolute glucose remain **entangled** — the
  identifiability gap this crossover removes.
- **[K2]** Bots SH, et al. 2026. *Int J Epidemiol* 55(5):dyag163, DOI 10.1093/ije/dyag163. Negative-control
  guidance: how to select/apply/interpret negative controls, with feasibility/validity considerations.
  Supplies the interpretation rules for the pre-registered negative-control exposure/outcome; supplies
  no glycemia-specific effect size.
- **[K3]** Zhang P, Zhang X, Zhao H, Zhang Y. 2026. *J Cardiothorac Surg* 21(1):660,
  DOI 10.1186/s13019-026-04488-w. Closest MIMIC-IV SHR cohort; explicitly concedes that "a substantial
  proportion of potentially eligible patients were excluded because SHR could not be calculated owing
  to missing glucose or HbA1c measurements, which may have introduced selection bias." Directly
  motivates R-select and the power gate; does not itself test separability.
