> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Decision-conditional test of the post-LDT AFP slope: does it predict progression when the landmark imaging is clean?

Island: hcc (single-institution Chinese hospital HCC records; snapshot `[source checksum]`).
Episode 25 (operation = evolve). Scientific parent (fixed by the Lead): `[prior hypothesis]`
(valid; post-LDT AFP/ALBI landmark design + first-modality effect modification + surveillance-intensity
detection-bias discrimination test). The parent's frozen design is inherited **verbatim** (Section 3).
This child adds exactly ONE pre-specified, decision-changing estimand (Section 4).
Status: design + this-episode bounded feasibility probe; **no outcome model, HR or interaction test is
computed here** (discovery). Results are the solver's first feasibility outputs.

## 1. Unresolved question and clinical importance
After liver-directed therapy (LDT: TACE / resection / ablation) for HCC, surveillance couples serial
serum AFP with scheduled cross-sectional imaging. The parent branch asks whether the within-patient
post-LDT AFP slope predicts time to local progression, and whether that hazard differs by first modality,
after correcting for detection/observation bias. Every prior episode attacks *validity threats* on the
**pooled** estimand. None asks the question that actually governs the clinical decision:

> When the landmark imaging is **radiographically clean** (no progression descriptor), does a rising AFP
> slope still carry independent prognostic information, or is the AFP signal confined to patients whose
> imaging already shows suspicion?

This is the surveillance-adjunct decision: whether serial AFP should intensify imaging when the current
scan is uninformative. If the slope only predicts progression among imaging-suspicious patients, AFP adds
no early signal where imaging is clean and risk-adapted imaging on AFP alone is not justified [K1,K3].

## 2. Hypothesis (falsifiable)
- H1 (leading claim): among patients with a **clean landmark imaging** (IMGneg), a higher within-patient
  AFP slope over (index, t*] still predicts a higher hazard of subsequent local progression.
- Strongest rival R_concordance: the pooled AFP-slope hazard is an **imaging-concordance artifact** — AFP
  rises in patients whose landmark/interval imaging already carries sub-threshold suspicion, so within the
  stringently IMGneg stratum the slope HR attenuates to ~1 while it remains elevated in IMGpos.
- Secondary rival R_timing: an apparent IMGneg signal is produced by intervening scans in (t*, event) that
  are scheduled *because* AFP rose (informative observation; the parent's surveillance-intensity machinery
  is reused, not replaced).

## 3. Inherited frozen design (verbatim; not modified)
Population = HCC diagnosis + >=1 liver-directed procedure; index = earliest qualifying procedure; landmark
t* = index + 180d (90d sensitivity). Exposures (per-patient AFP slope and ALBI slope) fit ONLY on draws in
(index, t*]; same-draw AFP + albumin + total-bilirubin pairing within +/-2d on 检验时间;
ALBI = 0.66*log10(bilirubin) - 0.085*albumin. Primary endpoint = modality-restricted abdominal
**local-progression** event {增大, 进展, 复发, 新发, 增多} on examinations, with 转移 (metastasis) as a
competing event; censoring via 出院时间; retreatment proxy secondary; four rivals; conjunctive
falsification; no survival/mRECIST claim.

## 4. This child's ONE added element: decision-conditional imaging stratum
Define landmark imaging status from the `examinations` table over window [t*-45d, t*+45d]:
- IMGneg = a qualifying abdominal cross-sectional/US study whose 检查所见 AND 检查诊断 contain **none** of
  {增大, 进展, 复发, 新发, 增多, 转移};
- IMGpos = a qualifying study containing a progression/metastasis descriptor;
- IMGmissing = no qualifying study in the window.

Primary re-fit: the frozen landmark Cox (per-1-SD AFP slope + ALBI slope + first modality + age/sex +
draw intensity) is re-estimated **within the IMGneg stratum**, reporting the AFP-slope HR and 95% CI.
Pre-specified heterogeneity: add a landmark-imaging-status x AFP-slope interaction and report a 1-df LRT.
Reused from the parent: the (a) surveillance-intensity covariates over (t*, censor], (b) AFP-independent
ALBI-slope negative control, and (c) intensity-adjusted re-test (deltaHR + 95% CI).

Branches (pre-declared):
- Supportive: IMGneg AFP-slope HR > 1 with 95% CI excluding 1, >=30 events, monotone quartile trend
  (p_trend < 0.05), and the IMGneg/IMGpos interaction not significant (signal transportable).
- Adverse = R_concordance: IMGneg HR ~1 (CI includes 1) while IMGpos HR > 1, OR interaction p < 0.05 with
  IMGpos > IMGneg -> the slope is not an imaging-independent early signal.
- Inconclusive: IMGneg events < 30, OR IMGmissing > 50%, OR landmark images lack dated 开始时间.
- Precise-null: IMGneg HR within +/-0.10 of 1 with a tight CI and flat ALBI negative control.

## 5. Method alternatives (baseline vs substantive alternative)
- M0 (baseline) = parent's pooled landmark Cox + modality interaction.
- M6 (this child) = M0 restricted to IMGneg + imaging-status interaction.
What M6 recovers that M0 loses: separation of "AFP tracks existing imaging suspicion" (concordance) from
"AFP is an imaging-independent early biomarker" — the decision-relevant distinction. A shared-parameter
observation-event joint model is deferred (revisit if R_timing survives the intensity adjustment).
Budget: CPU-only, minutes to low tens of minutes; GPU not required.

## 6. Data bindings (frozen snapshot)
- Join key in every table: `患者主索引` + `就诊号`.
- `procedures/data_手术_8024330590283626027.csv`: columns 手术, 开始时间, 结束时间, 手术来源.
- `labs/data_检验_609065997844652188.csv`: columns 检验, 定性结果, 定量结果, 检验时间 (labels 甲胎蛋白,
  白蛋白, 总胆红素; mandatory look-alike exclusions).
- `examinations/data_检查_4203595081195465282.csv`: columns 检查, 检查所见, 检查诊断, 开始时间, 检查号.
- `encounters/data_基本信息_2500296761891079109.csv`: 年龄, 性别, 入院时间, 出院时间 (censoring).
- This-episode bounded probe measured (see work/gen-imaging-conditional/): cohort, IMGneg/IMGpos counts and
  post-landmark event counts per stratum.

## 7. Honest limits
Lexical progression endpoint requires radiologist mRECIST adjudication; no mortality/mRECIST PFS -> no
survival claim; single institution; lab results carry no units; NO outcomes computed in discovery; any
causal claim needs expert review or another study.

## Key works
[K1] Chen J, Huang Y, Zhou D (2026) — persistent AFP/DCP rise with negative liver imaging preceding occult
progression (case report; supports the decision premise, single-case limitation).
[K2] Hlauschek et al. (2026) — immortal-time/lead-time bias in observational therapy analyses (methodological
bound inherited from the parent).
[K3] Bokhary R (2026) / AFP-screening editorial (2026) — AFP/imaging surveillance detection limits (bounds
the surrogate role of AFP when imaging is clean).
