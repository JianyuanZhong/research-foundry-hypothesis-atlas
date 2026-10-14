> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Working proposal (Lead) — MIMIC-IV island, episode 8 (evolution)

Candidate: evolution child of `[prior hypothesis]` (board top, mu 31.6, sigma 6.8, valid, refs complete).
Origin: expert seed `[starting question]` ("Asynchronous organ recovery").
Status: design frozen. Archive members and dictionary itemids **newly re-verified this episode** by reading
`icu/d_items.csv.gz` and `hosp/d_labitems.csv.gz` inside the frozen `mimic-iv-3.1.zip`. Cohort rows NOT analysed
in discovery. No clinical truth claimed.

## 1. Unresolved question

After circulatory stabilisation in sepsis/septic shock, some patients recover kidney and lung function together
while others recover one organ bed while the other stays impaired ("cross-organ recovery asynchrony"). The
parent tests whether asynchrony at a prespecified decision time t* predicts 7-day deterioration beyond the
same-time snapshot severity. The pivot that this child sharpens is **explanatory**, not predictive:

> Is measured renal-vs-respiratory recovery asynchrony *additional information* beyond (M1) a single shared
> latent recovery factor (the "one common recovery axis" rival, motivated by [K1]) and beyond (M3) organ-specific
> laboratory observation intensity (which makes sicker/more-monitored patients likelier to be *labelled*
> recovered)? Or does the asynchrony signal survive only as an artefact of one trajectory sampled unevenly
> between organs?

## 2. Observed vs conjectured (evidence)

- Observed [K1, full-text excerpt]: acute inflammatory recovery across trauma/ischaemia/infection follows a
  largely *universal single trajectory* (exponential WBC decay, delayed platelet growth) whose deviation predicts
  adverse outcome (9x RR of sepsis death). → Real: recovery dynamics are informative. Not established: that
  *cross-organ divergence* carries information beyond this one shared axis.
- Observed [K2, abstract-only]: dynamic multi-organ *interaction* trajectories define reproducible sepsis
  subphenotypes in MIMIC-III/eICU. → Real: multi-organ trajectory structure is informative and is prior art.
  Not established: a prespecified, interpretable asynchrony index adding beyond a shared latent factor with
  observation-intensity control.
- Observed/bounding [K3, abstract-only]: creatinine-based GFR estimation is biased in critical illness with
  large muscle-mass change; cystatin C improves injury detection there. → The renal limb of "recovery" is
  partly measurement-driven. Conjectured (to test): residual asynchrony is a genuine organ-divergence signal.
- Observed (archive, this episode): every itemid below exists in `d_items`/`d_labitems` of the frozen zip.
  Conjectured: enough septic ICU stays have both limbs measured around t* to estimate the contrasts.

## 3. Why it matters / advance

If asynchrony adds nothing beyond one shared factor + observation intensity, then a widely intuitive
"one organ is lagging" clinical read of recovery is an artefact and should not drive prognostication — a useful
negative result. If it survives, a two-organ asynchrony index at a fixed post-stabilisation landmark is a new,
cheap prognostic contrast. The advance over [K1]/[K2] is the *discriminating* ladder, not a small AUROC gain.

## 4. Design (frozen)

Population: adult (>=18) ICU stays with sepsis/septic shock. Sepsis = suspected infection + acute SOFA rise >=2
(operationalised from chart/lab events); septic shock = vasopressor + lactate >2 mmol/L. Unit = first ICU stay
per `hadm_id`; index = ICU `intime` (`icu/icustays`). exclusions: ICU stay <48 h, ESRD-on-chronic-dialysis,
no creatinine and no oxygenation measurement in the t* window.
Temporal boundaries: t* = first time after ICU admission with sustained MAP >=65 mmHg for >=2 h without
vasopressor escalation (defined from `chartevents` MAP + `inputevents` vasopressors). Measurement window =
[t*-24h, t*]; landmark = t*; outcome window = (t*, t*+7d]. Only data <= t* used as predictors (no future info).
Variables (bindings verified this episode):
  - Map/BP: `icu/chartevents` itemid 220052 (Arterial BP mean), 220181 (Non Invasive BP mean), `valuenum` mmHg.
  - Vasopressors (`icu/inputevents`, `rate`): 221906 norepinephrine, 221289 epinephrine, 222315 vasopressin,
    221749 phenylephrine, 221662 dopamine, 221653 dobutamine.
  - Renal recovery: `hosp/labevents` itemid 50912 creatinine (Blood, Chemistry); urine `icu/outputevents`
    itemids 226559, 226560, 226566, 226627, 226631, 226713 (`value` mL). Renal RRT (`icu/procedureevents`):
    225802, 225803, 225809, 225955, 225441 (dialysis).
  - Respiratory recovery: `icu/chartevents` FiO2 223835; `hosp/labevents` pO2 50821 (Blood, Blood Gas);
    ventilation `icu/procedureevents` 225792 (invasive), 225794 (non-invasive).
  - Severity snapshot at t*: same-time SOFA components, lactate `hosp/labevents` 50813, vasopressor dose.
  - Observation intensity: counts of renal vs respiratory measurements per unit time in [t*-24h, t*] (M3).
Join keys: `subject_id`, `hadm_id`, `stay_id` (`icu/icustays` links stays to `hosp` via `hadm_id`; labs via
`hadm_id`, chart/output/procedure/input events via `stay_id`). Time fields: `chartevents.charttime`,
`labevents.charttime`, `inputevents.starttime/endtime`, `outputevents.charttime`, `procedureevents.starttime/
endtime`, `icustays.intime/outtime`. Outcome: 7-day composite (death, new/persistent vasopressor escalation,
new/persistent RRT, sustained respiratory-support escalation) within (t*, t*+7d], from the same tables.
Asynchrony index: standardised (z) slowest normalised recovery time across the renal limb minus the respiratory
limb (renal recovery = creatinine falling toward baseline and/or urine output rising; respiratory recovery =
falling FiO2 requirement / rising P/F), signed so positive = kidney slot lags.

Model ladder (the discriminating comparison, same population/split for all):
  - M0 snapshot severity at t* (SOFA/lactate/vasopressor) — baseline.
  - M1 M0 + asynchrony index — the claim under test.
  - M2 M0 + a single shared latent recovery factor fitted across the four recovery features (factor model),
    i.e. the [K1]-motivated rival that discards organ-specific divergence.
  - M3 M1 + organ-specific observation-intensity covariates (the measurement rival).
Primary contrasts: delta-AUROC(M1 vs M0) and delta-AUROC(M1 vs M2), with bootstrap 95% CIs; M3 isolates
whether any M1 gain is explained by observation intensity. Method exploration: M0 (transparent snapshot
baseline) vs M2/M1 (learned latent-factor + residual divergence) on the SAME question; the learned factor is
what reveals whether the baseline's asynchrony term is a *real* organ-divergence axis or one common axis.
A small CPU fit (logistic/GLM; optional low-rank factor model) is sufficient; no GPU is required for the test.
Split: temporal — development = earliest 70% of ICU stays by `intime`, holdout = latest 30%; no patient overlap.
Falsification / decision rules (prespecified):
  - Supportive: delta-AUROC(M1 vs M0) > 0 with 95% CI excluding 0 AND delta-AUROC(M1 vs M2) > 0.01 with 95% CI
    excluding 0, surviving M3, and beating a permuted-label negative control.
  - Adverse: delta-AUROC(M1 vs M2) <= 0 (asynchrony adds nothing beyond the shared factor); or the M1 gain
    disappears once M3 observation-intensity is added.
  - Inconclusive: CIs overlap 0, or the cohort with both limbs measured near t* is too small (target >=500).

## 5. Solver deliverable

Cohort builder + the four locked fits M0–M3 on the temporal split; report the two primary contrasts with
bootstrap CIs, the M3 observation-intensity contrast, and the permuted-label control; classify the outcome as
supportive/adverse/inconclusive by the rules above. Success = the contrasts are computed and honestly
classified; NOT confirmation of the hypothesis.

## 6. Limits (accepted)

Single-centre retrospective (MIMIC-IV 3.1); no causal/mechanistic claim. Creatinine renal recovery is
confounded by muscle loss/RRT [K3] — adjusted and sensitivity-restricted, not removed; cystatin C is absent
from this extract. Observation intensity is adjusted, not removed. K2/K3 inspected abstract-only; K1 bounded
excerpt only. t* is itself treatment-influenced (vasopressor weaning) — timing artefact is a named rival.

## 7. Demonstration & seed disposition

- Nat Commun inflammatory-recovery (demo 1 / [K1]): adapted — used as the single-shared-factor rival, not
  reproduced.
- Cell cancer multimodal (demo 2): not pursued — its full text/STAR Methods are unavailable and chest imaging
  is outside the frozen MIMIC tabular extract.
- Nat Commun Bayesian longitudinal EHR (demo 3): partially adapted — the latent-factor M2 echoes a
  longitudinal-latent-structure idea, but genetics are absent so no genetic reproduction is attempted. The
  generative-Transformer demo requires trajectories/data depth not established here.
- Seed 01 developed (this candidate). Seeds 04/05/06/07/08 remain untested alternatives for later episodes.
