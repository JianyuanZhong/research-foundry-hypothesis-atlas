> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Post-resection adjuvant TACE timing gradient in HCC: adding a pre-specified outcome-MISCLASSIFICATION (ascertainment) bias analysis to the timing estimand

Island: **hcc** (single-institution Chinese HCC records; snapshot `[source checksum]`).
Episode 33, hcc island. Operation: **crossover** of two assessed-valid parents:
- `[prior hypothesis]` (board leader, mu 32.76; post-resection adjuvant-TACE / MVI target-trial-emulation **with the within-window TIMING/INITIATION-GRADIENT element**), and
- `[prior hypothesis]` (mu 25.0; **latent-class outcome-ascertainment validation** of the unvalidated lexical-progression endpoint).

Both parents are inherited **VERBATIM**. Exactly **ONE** new decision-changing element is added (Section 4A): a
pre-specified **probabilistic outcome-misclassification bias analysis** applied to the timing estimand HR_T60, with a
pre-committed retraction rule. No other element of the parent designs is modified. **No outcome/HR/Se/Sp was computed in discovery.**

---

## 1. Unresolved question and clinical importance

After curative-intent hepatectomy for HCC, post-operative adjuvant TACE (PA-TACE) is used in Chinese practice for
"high-risk" patients (microvascular invasion, MVI) on the rationale of eradicating microscopic residual disease. Yet the
newest adjuvant-therapy evidence is negative/heterogeneous for early-stage HCC as a whole ([K2], [K3]). The board leader
([parent A]) proposes a **within-window timing gradient** (earlier first adjuvant TACE, <=60 d vs 60-90 d post-resection)
as an orthogonal, decision-changing test whose **sign** separates a genuine causal benefit (HR_T60<1) from
healthy-initiation/confounding-by-indication (HR_T60>1, later = fitter patients).

**Unresolved rival not yet addressed by either parent:** the recurrence endpoint is an *unvalidated lexical
reconstruction* from archived records. If ascertainment intensity **differs by exposure** — patients started on
post-operative TACE are typically imaged more intensively in the following months, so recurrence is *detected earlier*
in the early-initiation arm — then the apparent timing "effect" (either direction) can be an **artifact of differential
detection/measurement**, not of treatment. This is a failure mode distinct from confounding by indication and from the
parent's already-included imaging-cadence/IOO covariate adjustment (which adjusts for *counts*, not for
*differential endpoint misclassification*).

Clinically important: PA-TACE timing is an actionable, low-cost decision; if the timing signal is a surveillance
artifact, guidelines/practice built on registry recurrence endpoints would be misled.

## 2. Data and bindings (verified this episode on the frozen snapshot)

Source root: `[internal dataset path]` (read-only).

- **procedures** `data_手术_8024330590283626027.csv` (35,207,405 B; [source checksum]).
  Columns `患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源`. Join key `患者主索引`(+`就诊号`).
  Measured this episode: 338,040 rows / 43,062 patients; TACE-ish (`TACE|tace|栓塞|化疗栓塞`) 109,424 rows / 20,165 pts;
  resection-ish (`切除|根治`) 71,598 rows / 26,782 pts; `开始时间` range 2005-06-19 .. 2026-01-01.
- **pathology** `data_病理_3292603985559017792.csv` (41,907,200 B; [source checksum]).
  Columns `患者主索引, 就诊号, 病理, 检查所见, 检查诊断, 机器型号`. MVI from `检查所见`/`检查诊断` free text (verbatim lexical set in the parent).
- **examinations** `data_检查_4203595081195465282.csv` — report text for the **independent imaging progression indicator** (bias analysis).
- **labs** `data_检验_609065997844652188.csv` — AFP draws for the **independent lab progression indicator** (same-draw convention inherited).
- **transfers** `data_出入转_7369490831683459252.csv` — `出院时间` for last-contact censoring.
- **encounters** `data_基本信息_2500296761891079109.csv` — linkage/demographics; **diagnoses** `data_诊断_7504718184492840569.csv` — HCC dx.

## 3. Population, temporal boundaries, estimand (inherited verbatim)

- Population: HCC diagnosis + >=1 curative hepatectomy; **index = earliest resection `开始时间`**; **t0 = index + 90 d**.
- Exposure: any TACE in `(index, index+90d]`; **timing cohort** = first windowed TACE in `(0, 90]` d.
- Primary timing variable **T60**: early initiators <=60 d vs 60 < T <= 90 d (fixed a priori); secondary 3-knot RCS for a non-monotone optimum.
- Outcome: **<=24-month recurrence** (lexical) with **death as competing event**; censor at last contact (`出院时间`) / 2025-12-31.
- Temporal boundary: index in 2010-01-01..2023-12-31 to allow >=24-month follow-up.

## 4. Analysis (inherited) and the added element

- **M0 (baseline):** single-cohort Cox of T60 with the session-count term, MVI interaction, and the parent's covariate set; overlap-weighted target-trial emulation + negative-control outcome + temporal split + net-benefit (parent M1 machinery).
- **M1 (parent):** target-trial emulation (propensity/overlap weighting) + pre-committed negative-control-outcome retraction rule + E-value.
- **4A (ADDED, decision-changing).** **Probabilistic outcome-misclassification bias analysis of HR_T60.**
  1. Build >=2 **conditionally-independent indicators** of true progression: (i) lexical recurrence flag; (ii) imaging-text progression signal (examinations); (iii) sustained AFP-rise signal (labs). *[indicator label sets inherited/frozen from parent B; not re-derived here]*
  2. Fit a **latent-class measurement-error model** to estimate **exposure-stratified** sensitivity/specificity; report Se/Sp with uncertainty.
  3. **Monte-Carlo propagate** the Se/Sp draws through the Cox timing model (misclassification-corrected log-HR_T60 + 95% interval), reusing the parent's overlap weights.
  - **Pre-committed retraction rule:** if the corrected **HR_T60 95% interval crosses 1**, or its **sign reverses relative to the M0 estimate**, the parent's supportive timing read is **retracted** (adverse/inconclusive).
  - **Collinearity guard:** correction enters jointly with the session term; VIF pre-checked (inherited).

**Method comparison (baseline vs substantive alternative, recorded before selection).** M0 loses the question of whether the
endpoint itself is differentially measured across exposure; M6 (latent-class-corrected Cox) is the only variant that can
separate a real timing gradient from an exposure-differential detection artifact. Chosen over a purely predictive model
because the deliverable is an **estimand** (bias-corrected HR_T60), not discrimination. Resource estimate: CPU-only,
bounded (bootstrap/Monte-Carlo ~1e3-1e4 draws over ~2.7e3 timing-cohort patients) — well within the solver envelope.

## 5. Falsification (branch-level; conclusions tied to computed outputs)

- **Supportive:** corrected HR_T60<1, interval excludes 1, null on negative control, E-value>=1.3.
- **Adverse (ascertainment):** corrected interval crosses 1 or sign reverses -> timing gradient is an ascertainment artifact (retraction rule fires).
- **Adverse (confounding by indication):** uncorrected HR_T60>1 that reverses/attenuates under overlap weighting.
- **Inconclusive:** >50% imaging-negative/missing indicators or Se/Sp unidentifiable (latent class non-convergent) -> pre-declared inconclusive.
- **Precise null:** tight corrected interval around 1.

## 6. Disposition of the three expert research demonstrations

- **Natural-history generative transformers** (Nature 2025, 10.1038/s41586-025-09529-3): deferred — no multi-organ generative infra; estimand is a single-event landmark Cox.
- **Longitudinal routine clinical data for cancer** (Cell 2026, 10.1016/j.cell.2026.07.009): main text unavailable (HTTP 403/401 by publisher; only supplement inspected) -> no method imported; conceptual only.
- **Bayesian longitudinal EHR + genetic discovery** (Nature 2026, 10.1038/s41586-026-10780-5): conceptually the closest (measurement-error/latent structure), but no paired genetic data on this island; the **latent-class measurement-error** borrowing (Section 4A) is the bounded adaptation.

## 7. Essential adjudication / unavailable evidence

No mRECIST/pathologist gold standard replaces the lexical endpoint; free-text MVI extraction and lexical recurrence require
expert adjudication before clinical use. Single institution; E-value bounds confounding strength, not existence; no
outcomes/HR/Se/Sp computed in discovery. No cross-dataset patient joins.

## 8. Key references

See `key-references.json` (K1-K3, abstract-only, hashed excerpt receipts attached).
