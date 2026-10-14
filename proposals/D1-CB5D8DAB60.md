> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Is the post-LDT AFP set-point–progression association believable? A pre-registered endpoint-measurement gate

Island: **hcc** (snapshot `[source checksum]`).
Episode 45. Operation = **evolve**. Scientific parent (Lead-fixed) = `[prior hypothesis]`
(mu 32.23, assessed **valid**; periprocedural AFP pulse-decay NLME returning the decay-completed tumour-burden
set-point mu_i). Parent science preserved verbatim (Sec. 3). This child adds exactly **ONE** pre-specified,
decision-changing element (Sec. 4). Status: design + binding probe; **no HR, kappa, slope, event count or model
is computed here** (discovery). These are the solver's first deliverables.

## 1. Unresolved question and why it matters
After liver-directed therapy (LDT) for HCC, the whole branch asks whether a within-patient AFP trajectory predicts
radiologic progression beyond baseline AFP/ALBI. [K1] shows AFP is imperfect even against ultrasound screening
(7 ng/mL raises sensitivity but drops specificity 97.28%->92.24%). [K3] shows "progression" in HCC is
criteria-dependent (RECIST 1.1 vs mRECIST). [K2] shows response classification is dominated by measurement
choices (lesion selection, reader experience, follow-up schedule). The branch's own outcome is a **lexical** flag
harvested from Chinese free-text (increase/progression/recurrence/new-lesion terms) and **has never been
validated**; 40+ children deferred this to "the solver's first feasibility output". Every HR on this branch is
interpretable only if that flag measures progression. **Claim to be tested:** the free-text progression event is
measured accurately enough to support an AFP-trajectory hazard (kappa >= 0.60 AND PPV >= 0.70 AND negation-error
<= 10%). **Strongest rival (R_endpoint):** the flag conflates negated text ("未见复发"/"无进展"), prevalent vs
incident progression, and metastatic-only statements, so it is a surveillance artifact, not tumour biology.

## 2. What answering it would change
A pass licenses the inherited AFP set-point Cox; a fail invalidates the progression claims of the whole branch and
is itself a valuable negative result. Association surviving adjustment is predictive utility, not mechanism.

## 3. Inherited frozen design (verbatim from parent)
Population = HCC diagnosis (`诊断名称`) AND >=1 liver-directed procedure (`手术`); index = earliest qualifying LDT
`开始时间`; t* = index+180 d (90 d sensitivity). Exposure = parent's periprocedural AFP pulse-decay NLME on ALL
draws -> set-point mu_i, with release amplitude A_i as rival. Labs based are AFP `检验`='甲胎蛋白' numeric
`定量结果`; ALBI = 0.66*log10(bilirubin)-0.085*albumin, same-draw +/-2 d pairing. Outcome (parent) = modality-
restricted abdominal local progression, lexical event in {增大,进展,复发,新发,增多}, 转移 as competing event,
censor via encounters `出院时间`. Covariates/controls: age, sex, baseline tumour/procedure vars, surveillance
intensity, ALBI-slope negative control; four rivals; conjunctive falsification; **no survival/mRECIST claim**.

## 4. The ONE added element: a gated, two-source, negation-aware endpoint validity experiment
Two **partly independent** structured ascertainments of incident local progression:
- **A (imaging impressions):** examinations `检查诊断`(+`检查所见`), abdominal liver studies; strip HTML markup;
  progression-positive only in affirmative context (negation-aware rules), local-hepatic change; 转移-only -> competing.
- **B (admission diagnoses):** diagnoses `诊断名称` at encounters after t*, same affirmative local-progression rule.
**Primary measurement estimand:** Cohen kappa(A,B), PPV of A vs B, and the fraction of A positives that are
negation-parse errors. **Pre-declared validity floor:** kappa >= 0.60 AND PPV >= 0.70 AND negation-error <= 10%.
Only if the floor is met is the inherited mu_i Cox (Sec. 3) reported.

## 5. Bindings (probed this episode, snapshot 3f97e661); sources under `[internal dataset path]`
| table | file | columns used |
|---|---|---|
| examinations | `data_检查_4203595081195465282.csv` | 患者主索引,就诊号,检查,检查所见,检查诊断,开始时间,检查号 |
| diagnoses | `data_诊断_7504718184492840569.csv` | 患者主索引,就诊号,诊断名称,诊断类型 |
| labs | `data_检验_609065997844652188.csv` | 患者主索引,就诊号,检验,定性结果,定量结果,标本类型,检验时间 |
| procedures | `data_手术_8024330590283626027.csv` | 患者主索引,就诊号,手术,开始时间,结束时间,手术来源 |
| encounters | `data_基本信息_2500296761891079109.csv` | 患者主索引,就诊号,年龄,性别,入院时间,出院时间 |
Join key = `患者主索引`+`就诊号`; time fields `开始时间`/`检验时间`/`出院时间`. Headers verified by
bounded read (e.g. 检查诊断 present; diagnosis names carry 复发/术后 terms). Files read-only; derived in workspace.

## 6. Falsification / branches
- **Supportive:** floor met -> report kappa/PPV then the inherited mu_i Cox HR+CI.
- **Adverse (R_endpoint):** floor fails -> free-text endpoint invalid; branch progression claims unsupported; STOP.
- **Inconclusive/feasibility:** A or B sparse (<30 concordant events) -> endpoint non-ascertainable; report counts.
- **R_selection:** if B (diagnosis names) is prevalent-only (timestamps cluster at index admission), disagreement is
  an ascertainment-window artifact, reported separately and not as biology.

## 7. Method comparison (recorded before selection)
- M0 (baseline): inherited single-source lexical flag as the event (branch default).
- M_meas (required alternative): two-source negation-aware gated endpoint.
What M0 loses: it cannot separate endpoint measurement error from biology; M_meas estimates the endpoint's own
error, which no exposure model can supply. A generative/longitudinal model (D1) or Bayesian EHR framework (D3) is
deferred: neither fixes a mis-measured outcome and D3 requires genetics absent here.

## 8. Honest limits / additions needed
No mortality/PFS (no survival claim); single institution; labs lack units; HTML markup in `检查所见` must be
stripped; the negation parser is rule-based and itself unvalidated -> **clinical (radiologist) adjudication of a
sample and/or another study is required to certify the endpoint**; no outcome computed in discovery.

## 9. Demonstrations & seeds dispositions
- D1 (Nat 2025 generative transformers, doi 10.1038/s41586-025-09529-3): deferred - target is endpoint validity, not
  a generative model; no compatible multi-organ longitudinal corpus here.
- D2 (Cell 2026 doi 10.1016/j.cell.2026.07.009): main text unavailable (403/401); supplement only - not relied on.
- D3 (Nat 2026 Bayesian EHR+genetics, doi 10.1038/s41586-026-10780-...): missing dependency - hcc snapshot has no
  genomics; blocked, not executable here.
- Expert seed index: `expert_seed_candidates` empty for hcc this run.
