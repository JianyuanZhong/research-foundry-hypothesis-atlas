> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Periprocedural AFP pulse vs tumour-burden set-point after liver-directed therapy for HCC: a mechanistic mixed-model test

Island: **hcc** (single-institution Chinese hospital HCC records; frozen snapshot `[source checksum]`).
Episode 44. Operation = **evolve**. Scientific parent (fixed by the Lead) = `[prior hypothesis]`
(valid; the "same-population restricted-slope" child that MEASURED the decay-clean filter to be non-estimable).
The parent's frozen design (Sections 2-3) is inherited **verbatim**. This child adds exactly **ONE** pre-specified,
decision-changing element (Section 4). Status at save: **design + inherited measured feasibility; NO HR, slope, LRT,
set-point or event count is computed in discovery.** The outcome model is the solver's first deliverable.

## 1. Unresolved question, clinical importance, and the advance over the parent
After liver-directed therapy (LDT: TACE / ablation / resection) for HCC, clinicians serialise serum AFP and must decide
when to re-image. The parent branch asks whether the *within-patient post-LDT AFP slope* predicts radiologic local
progression beyond baseline AFP and liver reserve (ALBI), inside the imaging-negative landmark stratum (IMGneg).

The branch's own last valid child produced a **measured** negative result: requiring "decay-clean" draws (drawn ≥30 d
after every procedure) leaves only ~116/51,381 patients (0.23%) eligible, and IMGneg decay-clean eligibility ~0.37%
(58/15,807); **99.35% of AFP draws fall within 30 d of a preceding procedure (median 1 day).** The parent's revised
estimator (a decay-clean OLS slope) is therefore essentially **non-estimable** on this snapshot, and its M0-vs-M_decay
contrast confounds *slope definition* with *population selection* (rival R_selection).

**The gap this child closes.** The release of AFP after LDT is not one process: serum AFP reflects (a) a transient
**periprocedural release pulse** proportional to necrosis / liver injury and regeneration, superimposed on (b) the
**underlying tumour-burden set-point**. [K2] explains that AFP kinetics after HCC-directed therapy are the net of
tumour-clone elimination, treatment-induced liver damage/regeneration and immune response, producing biphasic decline,
lag phases and "rebound" rises. A one-number OLS slope cannot separate a large benign post-procedure release from a
genuinely higher tumour burden: a patient with a big TACE-induced AFP pulse but a low decay-completed plateau is
misclassified as "rising". This is exactly why the decay-clean filter was proposed — and it is unaffordable here
because draws cluster around procedures. The advance is a **mechanistic estimator that uses ALL draws**, borrows
strength across patients, and returns the *decay-completed tumour-burden set-point* as the exposure. This is the
crossover the parent's own assessment named, and it is estimable precisely because the draws are dense near procedures.

## 2. Inherited frozen design (verbatim from parent)
- **Population:** HCC diagnosis (diagnoses `诊断名称`) AND ≥1 liver-directed procedure (procedures `手术`).
- **Index** = earliest qualifying LDT `开始时间`; **t\*** = index + 180 d (90 d sensitivity).
- **Exposure (parent M0):** per-patient OLS slope of log10(AFP) over draws with `检验时间` in (index, t\*]; AFP = labs
  `检验`='甲胎蛋白', numeric `定量结果`; **same-draw** pairing of albumin + total bilirubin within ±2 d of `检验时间`;
  ALBI = 0.66·log10(bilirubin) − 0.085·albumin; AFP/albumin/bilirubin look-alike exclusions.
- **Landmark imaging status** over examinations `开始时间` in [t\*−45 d, t\*+45 d]: IMGneg = a qualifying abdominal study
  whose `检查所见` AND `检查诊断` contain none of {增大, 进展, 复发, 新发, 增多, 转移}; IMGpos otherwise; IMGmissing if none.
- **Outcome:** modality-restricted abdominal **local progression** (lexical event = any of {增大, 进展, 复发, 新发, 增多})
  with `转移` as the competing event; censor via encounters `出院时间`. Secondary: retreatment proxy.
- **Covariates/controls:** age, sex, baseline tumour/procedure variables, **surveillance-intensity** (draw count, imaging
  cadence), ALBI-slope negative control; four rivals; conjunctive falsification; **no survival / mRECIST claim**.

## 3. Join keys and required columns (snapshot 3f97e661)
| table | source file (under `[internal dataset path]`) | columns used |
|---|---|---|
| diagnoses | `data_诊断_7504718184492840569.csv` | 患者主索引, 就诊号, 诊断名称, 诊断类型 |
| procedures | `data_手术_8024330590283626027.csv` | 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源 |
| labs | `data_检验_609065997844652188.csv` | 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间 |
| examinations | `data_检查_4203595081195465282.csv` | 患者主索引, 就诊号, 检查, 检查所见, 检查诊断, 开始时间, 机器型号, 检查号 |
| encounters | `data_基本信息_2500296761891079109.csv` | 患者主索引, 就诊号, 年龄, 性别, 入院时间, 出院时间, 就诊时间 |

Join key = `患者主索引` + `就诊号`; time fields `开始时间` / `检验时间` / `检查时间`(=检查−开始时间) / `出院时间`.
Source hashes are fixed by `datasets/hcc/metadata.json` (e.g. labs `9227b4228d…`, procedures `68e383ad2b…`,
examinations `4b650f4091…`, diagnoses `7065658050…`, encounters `2efb2c9023…`). Availability verified in the workspace
catalog this session; the parent's frozen ledger measured 43,815 HCC-dx patients and 40,689 loose liver-directed patients
(242,770 procedure rows), index range 2010-04-25..2025-12-31.

## 4. The ONE added, pre-specified, decision-changing element (Section 4)
**A periprocedural AFP pulse–decay nonlinear mixed-effects model (NLME) estimated on ALL post-index draws**, returning the
patient-level *decay-completed tumour-burden set-point* μ\_i as the exposure.

- **Draw set used:** every AFP numeric draw with `检验时间` ∈ (index, index + 365 d] (wider than t\* so the decay tail is
  observed). Define τ\_ij = days from draw j to the **most recent preceding** LDT `开始时间` (τ=0 at the procedure; if no
  procedure precedes the draw, τ = days since `index`).
- **Model (log10 scale, fixed decay half-life λ fixed at 5 d per [K2]'s decline-phase literature to keep it CPU-cheap):**
  log10 AFP\_ij = μ\_i + A\_i·exp(−τ\_ij/λ) + βᵀx\_ij + ε\_ij, with random effects (μ\_i, A\_i) ~ N(0, Σ) and fixed effects x
  for liver reserve/regeneration (ALBI draw value) and site-of-draw. Fit by maximum likelihood (statsmodels MixedLM / scipy).
- **Exposure:** μ\_i (per 1 log10), the decay-completed set-point — the tumour-burden level purged of the periprocedural
  release. A\_i (release amplitude) is retained as a *rival* exposure, not the primary one.
- **Primary test:** re-fit the frozen landmark Cox of local progression **within IMGneg** on μ\_i (per 1 log10) with the
  parent covariates, reporting HR + 95% CI; plus a 1-df LRT of μ\_i vs the parent all-draw OLS slope.
- **Pre-specified sensitivity:** λ ∈ {3, 7} d; (index, t\*] draw window; inclusion of A\_i as a covariate.

### Baseline vs scientifically-substantive alternative (method comparison, recorded before selection)
| | M0 (baseline; parent) | M\_pulse (alternative; this child) |
|---|---|---|
| estimator | per-patient OLS slope of log10 AFP over (index,t\*] | NLME pulse–decay, random set-point μ\_i |
| inputs | draws in (index,t\*] | ALL draws in (index,index+365 d], with τ to last procedure |
| what it returns | a single rate number | μ\_i (burden set-point) **and** A\_i (procedural release) |
| what it loses / recovers | cannot tell a benign release bump from a rising constitution | recovers the separation of release from burden; robust to draw-clustering near procedures |

M\_pulse is justified because it is the only estimator that is estimable under the measured draw structure (99.35% of
draws <30 d from a procedure) **and** answers the biological question the branch actually cares about. If the set-point
carries no signal while the release amplitude does, the parent's "rising AFP" signal was periprocedural artefact (rival
R\_release) — a result M0 cannot produce. CPU-only, minutes-to-tens-of-minutes; **GPU not required**.

## 5. Falsification criteria (pre-declared; conjunctive)
- **Supportive:** in IMGneg, μ\_i per 1 log10 HR > 1 with 95% CI excluding 1, **≥30 events**, M\_pulse fits better than
  M0 (ΔAIC > 10), and the association persists after adjusting for A\_i and surveillance intensity. ⇒ the decay-completed
  burden set-point is an imaging-independent early signal.
- **Adverse (R\_release):** μ\_i HR ≈ 1 while A\_i HR > 1 (release amplitude carries the signal), or M\_pulse ΔAIC ≤ 0 vs M0.
  ⇒ the parent AFP-slope association is attributable to the periprocedural release pulse, not tumour burden.
- **Inconclusive:** NLME fails to converge / μ\_i not identifiable (≥50% of patients with <3 usable draws or no decay-tail
  draw), IMGmissing > 50%, or IMGneg events < 30. ⇒ report as attainability-limited, not a null.
- **Precise-null:** μ\_i HR within ±0.10 of 1 with a tight CI and a flat ALBI-slope negative control. ⇒ no detectable
  set-point effect at this sample size.
Pre-declared: no mortality/mRECIST PFS end point; lexical imaging events are unvalidated without radiologist adjudication.

## 6. Clinical importance and what each outcome would change
A supportive result would give a defensible, draw-density-robust biomarker (the post-LDT AFP set-point) for risk-adapted
imaging intensity after LDT, computed from data that are already collected. A R\_release (adverse) result would warn that
serial AFP rises immediately after TACE are largely procedural and should not trigger re-imaging on their own — directly
relevant to the "normal/abnormal biomarker" interpretation trap [K3]. A precise-null result would bound the incremental
value of serial AFP in this setting. None of these is a causal or survival claim.

## 7. Disposition of the three demonstrations and deferred alternatives
- **D1 (generative transformers, natural-history):** deferred — a large-scale generative sequence model needs a
  longitudinal corpus with structured diagnosis codes absent here; not the closest evidence for this question.
- **D2 (longitudinal routine clinical data for cancer):** main article unavailable (publisher 403/401; only supplement);
  not usable as inspected full text.
- **D3 (Bayesian longitudinal EHR + genetics):** missing dependency — no genotypes in the HCC snapshot; deferred.
- **Deferred branch:** a shared-parameter joint model of the observation process and the event process (informative
  surveillance) — revisit if surveillance-intensity adjustment shows material sensitivity.
- Expert seed index is empty for this island.

## 8. Key works (details in `key-references.json`)
- [K1] Liu et al. 2025 — AFP/DCP response types after TACE independently predict PFS/OS. *Supports* the premise that
  post-TACE AFP change carries prognostic information. *Does not* separate procedural release from burden.
- [K2] Yang & Cao 2026 — AFP kinetics after HCC-directed therapy are the net of tumour-clone elimination, treatment-induced
  liver damage/regeneration and immune response, with biphasic decline / rebound / plateau phases. *Bounds* the mechanism
  and motivates a pulse–decay model. *Does not* provide a fitted estimator or a progression association.
- [K3] Kubatka et al. 2026 — the "specificity trap": abnormal biomarker results treated as cancer-specific and normal
  results used to reassure. *Bounds* the interpretation/decision logic. *Does not* study HCC post-LDT AFP.

## 9. Honest limits
Lexical imaging progression needs radiologist mRECIST adjudication; no mortality/mRECIST PFS ⇒ no survival claim; single
institution; no lab units (cross-assay pooling unsupported); NO outcomes computed in discovery (event/stratum/set-point
counts are the solver's first feasibility outputs). Any causal claim requires expert review or another study. Method
choice is explicitly not a claim of basic-science mechanism.
