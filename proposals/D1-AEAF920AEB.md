> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Adjuvant post-resection TACE in HCC: adding a pre-specified TIMING/INITIATION-GRADIENT internal-validity test for the MVI-stratified effect

Island: **hcc** (single-institution Chinese hospital HCC records; snapshot `[source checksum]`).
Evolution of parent `[prior hypothesis]` (valid, board leader, mu 33.67; operation = evolve, episode 32).
The parent design is inherited **VERBATIM** (Sections 1–3, 6, 8 below restate it unchanged, including the parent's
session-count dose-response element, which this child keeps). Exactly **ONE** new decision-changing element is added
(Section 4A: a within-window timing/initiation-gradient test, orthogonal to session count). No other element is modified.

---

## 1. Unresolved question and clinical importance (unchanged, inherited verbatim)

After curative-intent hepatectomy for HCC, post-operative adjuvant TACE (PA-TACE) is used in Chinese practice for
"high-risk" patients (microvascular invasion, MVI; portal-vein tumour thrombus), on the rationale of eradicating
microscopic residual disease. Yet the newest adjuvant-therapy evidence is negative for early-stage HCC as a whole
([K2] KEYNOTE-937: active surveillance remains standard of care; [K3]: adjuvant approaches show limited/inconsistent
phase-III benefit and unresolved patient selection). Whether PA-TACE has a **causal** benefit and whether that benefit
is **concentrated in MVI+ patients** is unresolved and decides a real choice: whether to give adjuvant TACE to an
MVI+ resected patient. [K1] shows PA-TACE responders are identifiable and that AFP + microvascular infiltration enter
the prognostic model, i.e., MVI is a plausible effect modifier worth a proper causal test.

## 2. Leading claim vs strongest rival (unchanged, inherited verbatim)

- **H_effect (leading):** PA-TACE reduces early recurrence in resected HCC, concentrated in MVI+ patients (residual
  microscopic disease) and ~null in MVI-negative patients.
- **R_conf (strongest rival):** any crude association is **confounding by indication + immortal-time / lead-time
  bias** — higher-risk, fitter patients are both more likely to receive PA-TACE and to survive to receive it, and
  are monitored more intensively (detection bias). Under R_conf the MVI-stratified "benefit" is a selection artefact.
- **R_null:** no causal effect; association is entirely explained by measured confounding + monitoring intensity.

## 3. Design (frozen, inherited verbatim)

- **Population:** patients with an HCC diagnosis (diagnoses table) AND >=1 **curative-intent hepatectomy** procedure
  (procedures `手术` label family: 肝叶切除 / 肝叶部分切除 / 腹腔镜下肝部分切除 / 特殊肝段切除 / 半肝 / 段切除).
- **Index** = date (`开始时间`) of the earliest qualifying resection. **Landmark** t0 = index + 90 d.
- **Exposure:** **adjuvant TACE** = a TACE/embolization procedure (`手术` matching 栓塞|TACE|化疗栓塞|介入) whose start
  date is in `(index, index+90d]`, ascertained **only inside the landmark window** (removes immortal time);
  comparator = no TACE in `(index,index+90d]`. Late/other TACE is not the exposure.
- **Effect modifier:** **MVI status** from pathology (`病理` / `检查所见` / `检查诊断` containing MVI|脉管癌栓|微血管|血管侵犯).
- **Outcome:** early recurrence (<=24 months post-landmark) via the branch's lexical imaging endpoint on examinations
  (`检查所见`/`检查诊断` containing 复发|新发|进展|转移|增多), with death as a competing event; censor at last contact
  (`出院时间`/last record). Endpoint requires radiologist mRECIST adjudication (stated limitation).
- **Baseline model (M0):** single-cohort Cox/logistic recurrence ~ adjuvantTACE + MVI + adjuvantTACE x MVI + era/
  age/ALBI/AFP covariates. Reports crude and adjusted HRs and the interaction.
- **Alternative model (M1, target-trial emulation):** same landmark, plus **propensity/overlap weighting** for PA-TACE
  indication (age, ALBI, AFP, tumour burden, resection type, era), a **negative-control outcome** (a TACE-implausible
  event), and imaging-cadence (monitoring-intensity) adjustment / IOO weighting.
- **Evaluation / split:** temporal split (fit earlier era, evaluate later) + 5-fold CV; adjusted HRs with 95% CI,
  interaction LRT, C-index/AUROC with calibration, decision-curve net-benefit vs "treat all/none".
- **Parent session-count element (kept, inherited):** within-exposed session-count dose-response + E-value quantitative
  bias bound, reusing the negative-control outcome.

## 4. THE ONE ADDED ELEMENT (this episode): timing / initiation-gradient internal-validity test

**Rationale / what it is meant to separate.** The parent's session-count gradient probes *how much* TACE is given, but
two different processes can move with session count (sicker patients get more sessions; more sessions also reflect
longer survival/follow-up), so it is an imperfect separator of a genuine effect from selection. This element adds an
**orthogonal, differently-failing** prediction using *when* the first adjuvant TACE is started within the fixed
90-day landmark window: `T = days(index -> first qualifying TACE in (index, index+90d])`, T ∈ (0,90]. Clinicians
commonly wait to start adjuvant TACE until postoperative liver function and clinical status recover — i.e., patients
who start **later** are, on average, **healthier** post-operatively (healthy-initiation / survivor-selection). Two
rival processes therefore make **opposite** directional predictions on the recurrence–timing association:

- **H_effect (causal):** residual microscopic disease is best eradicated by treating it early; if anything, **earlier**
  initiation (smaller T) predicts **lower** recurrence, or there is a specific early optimum window, and the sign is
  **stable under M1 weighting/E-value** and **absent for the negative-control outcome**.
- **R_conf / healthy-initiation:** because later initiators are fitter and better survivors, **later** initiation
  (larger T) predicts **lower** recurrence — the *reversed* sign. A reversed gradient is positive evidence for the
  selection rival and would materially undermine an MVI "benefit" read as causal.

This is a different failure mode from session count and is pre-specified with a **signed** directional prediction, so
the two explanations are separable even though both can, in principle, produce a protective-looking MVI effect.

### 4A(i) Pre-specified timing sub-analysis (within the exposed cohort)
- **Timing variable:** `T60` = binary **early initiator** = first-window TACE at `T <= 60 d` (vs `60 < T <= 90 d`),
  and (secondary) `T` as a **restricted cubic spline (3 knots)** to allow a non-monotone optimum. Pre-specified primary
  contrast is `T60`. Choice of 60 d is fixed a priori as the branch's natural dividing point (median measured at ~45 d;
  see Section 7), not chosen after looking at outcomes.
- **Estimand:** within-exposed adjusted hazard ratio of early vs late initiation, `HR_T60`, from M1 (overlap-weighted)
  and M0 (unadjusted/adjusted Cox), plus the spline shape of `HR(T)`.
- **Orthogonality check:** `T60` is entered **together with** the parent's session-count term so the timing effect is
  not merely a proxy for number of sessions; report the correlation of `T` with session count and the variance-inflation
  factor. If collinear (|r| > 0.7), report `T60` both with and without the session term and pre-commit to interpreting
  the session-count-adjusted estimate as primary.
- **Interaction with MVI:** `T60 x MVI` tested; H_effect predicts the early-initiation benefit is larger in MVI+.

### 4A(ii) Reused internal-validity machinery (from parent, unchanged)
- **Negative-control outcome:** repeat the `T60` contrast against the parent's TACE-implausible negative-control event.
  A true timing effect should be ~null there; a nonzero `HR_T60` on the negative control indicates residual
  selection/detection bias and **disqualifies a supportive timing read**.
- **E-value:** compute the E-value for the observed `HR_T60` (and for the MVI-stratified `HR_T60xMVI`) to bound how
  strong an unmeasured confounder would need to be to explain it away; a small E-value (<1.3) is treated as fragile.

### 4A(iii) Pre-specified directional prediction (the falsifiable core)
Because healthy-initiation predicts the **reversed** sign and a causal treatment effect predicts the **forward** sign
(or an early optimum), the sign of the timing coefficient is a genuine discriminator:
- **Forward (supportive of H_effect):** early initiators have **lower** recurrence (`HR_T60 < 1.0`, 95% CI excluding
  1.0 in the protective direction), the spline shows an early optimum, the negative-control `HR_T60 ≈ 1`, and the
  E-value is >= 1.3.
- **Reversed (supportive of R_conf):** `HR_T60 > 1.0` (later initiators do better) — evidence that the "protective"
  association is healthy-initiation, and the MVI benefit should not be read as causal.
- **Flat (inconclusive / precise-null):** CI spanning 1.0 with a narrow width — no usable timing signal either way.

## 5. Falsification criteria (Supportive / Adverse(R_conf) / Inconclusive / precise-null) with retraction

All evaluated on the **held-out later-era temporal split** and the negative-control outcome; discovery computes none.

- **Supportive branch (H_effect):** M1 `HR_T60 < 1.0`, 95% CI upper bound < 1.0; spline shows a monotone-forward or
  early-optimum shape; negative-control `HR_T60` CI includes 1.0; E-value >= 1.3; consistent in MVI+ (interaction
  `HR_T60xMVI < 1.0`). → Retain the MVI-concentrated causal-benefit claim with the timing element as corroboration.
- **Adverse branch (R_conf):** M1 `HR_T60 > 1.0`, 95% CI lower bound > 1.0 (later initiators recur less), OR a
  forward crude `HR_T60` that **reverses** or attenuates to the null under M1 overlap weighting (bias correction moved
  the estimate), OR a non-null negative-control `HR_T60`. → **Retract** the causal/MVI-concentrated reading; report
  the association as healthy-initiation / confounding by indication.
- **Inconclusive branch:** wide CIs or sign discordance between M0 and M1 or across the temporal split (e.g., M0
  forward and M1 reversed with overlapping CIs). → No timing claim; state that timing is unidentifiable in this cohort
  and that a larger/multicentre sample or a randomization is required.
- **Precise-null branch:** CI excludes a clinically meaningful hazard ratio (e.g., entirely within [0.85, 1.15]) with a
  null point estimate, on both M0 and M1 and the negative control. → Report that timing of initiation, as measured,
  has no material association with early recurrence in this cohort; this neither confirms nor refutes a causal effect
  of receiving TACE, and bounds the timing dimension only.
- **Pre-committed retraction condition:** if the negative-control outcome shows a `T60` association of comparable
  magnitude/sign to the recurrence model, **all** supportive reads are retracted regardless of the recurrence HR.

## 6. Analysis, baselines and split (unchanged, inherited verbatim; timing term added to the same models)

M0 single-cohort Cox vs M1 target-trial emulation with propensity/overlap weighting + negative-control outcome +
imaging-cadence/IOO adjustment + temporal split + net-benefit. The timing term `T60` (+ spline) and `T60 x MVI` are
added to the **same** M0/M1 specifications; nothing else changes. Honest method note: a fully time-varying MSM on
initiation-time was considered and **deferred** — per-session drug dose and a clean per-day treatment rhythm are not
recorded, so a session/timing-gradient descriptive-plus-weighted test is the defensible bounded choice; a
dose-based MSM would require pharmacy-level dosing not present here.

## 7. Verified data bindings (measured this episode, snapshot 3f97e661; source paths under `[internal dataset path]`)

- procedures `data_手术_8024330590283626027.csv` (SHA-256 `68e383ad…736b13`): 338,040 rows / 43,062 patients;
  cols `患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源`; join key `患者主索引(+就诊号)`.
  - TACE-ish `手术` = 109,215 rows / 20,152 patients; sessions/patient min 1, max 61, mean 5.42.
  - Resection-ish labels (regex 肝切除|肝叶…|肝部分…|腹腔镜下肝部分切除|特殊肝段切除|半肝|段切除|部分肝切除|肝右叶部分切除|肝左叶部分切除|肝段切除): 38,508 rows / 19,531 patients.
  - Patients with >=1 resection index: **20,318**; index `开始时间` range 2010-04-25 … 2025-12-31.
  - Patients with resection index AND any TACE: **5,400**; days(index→first TACE) median **45**, IQR 34 … 319;
    **2,737** patients have first TACE in `(0, 90]` (the timing-cohort size), 676 at day <= 0.
- pathology `data_病理_3292603985559017792.csv` (SHA-256 `7ad2d61c…2c3d41`): 46,395 rows / 28,184 patients;
  text cols `检查所见, 检查诊断` (non-null 45,182 / 46,293). MVI/vessel-keyword rows (脉管癌栓|微血管|血管侵犯|癌栓|MVI):
  **21,371 rows / 19,174 patients**.
- labs `data_检验_609065997844652188.csv`: cols `检验, 定性结果, 定量结果, 标本类型, 检验时间` (AFP, albumin, bilirubin).
- examinations `data_检查_4203595081195465282.csv`: text `检查所见, 检查诊断`, time `开始时间` (recurrence/imaging cadence).
- encounters `data_基本信息_2500296761091079089.csv`: age/sex; diagnoses `data_诊断_7504718184492840569.csv`: HCC dx.
- Join keys `患者主索引(+就诊号)`; snapshot `3f97e661`. All source files read-only; no cross-dataset patient joins.

## 8. Limitations and honesty (unchanged, inherited verbatim + timing additions)

- **No outcome, HR, T60 distribution, spline, E-value or net-benefit is computed in discovery** — those are solver
  outputs. This proposal reports measured *binding* counts only (Section 7).
- Per-session drug dose unavailable → session-count/session-timing only; a dose-based MSM is explicitly not chosen.
- Timing estimand assumes the 90-day window is a fixed landmark and that first-TACE day is measured without error;
  same-day/negative-day TACE (676 patients) are excluded from the timing cohort by the `(0,90]` rule (recorded).
- Lexical recurrence endpoint is unvalidated; requires radiologist **mRECIST adjudication** (clinical, not computable
  here). MVI free-text extraction is imperfect and requires pathologist adjudication. Recurrence ascertainment depends
  on imaging follow-up (monitoring intensity addressed but not eliminated). Single institution; no lab units recorded.
- E-value bounds the strength of unmeasured confounding, not its existence; the timing direction is only a
  discriminator, not proof of mechanism.
- No cross-dataset join; no patient-level records sent to any public search.

## 9. Key references (abstract-only inspected; see `facet-work/evo-A/key-references.json` and `K{1,2,3}-excerpt.txt`)

[K1] Ou AX et al. 2025, doi:10.62347/bqok1208 (PMID 41244123).
[K2] Mingazzini A et al. 2026, doi:10.2147/jhc.s613651 (PMID 42764956).
[K3] Pantzios S et al. 2026, doi:10.1016/j.isci.2026.117084 (PMID 42620713).
Receipts/hashes inherited verbatim from parent `[prior hypothesis]`; the three attached excerpt bytes
were re-hashed this episode and match (K1 `bb0d0e51…5dd4`, K2 `2d3c050a…a817`, K3 `b5889a2a…a87f`). Claim mappings
rechecked against the timing addition: all three bound the MVI-stratified adjuvant-TACE question; none establishes a
timing/initiation effect, so the timing element is framed as an internal-validity discriminator, not a literature claim.
A bounded Europe PMC search for timing-of-initiation work returned no closer primary source; that gap is stated honestly.
