> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Working proposal (Lead, HCC island, episode 21)

Status: design + bounded probe-verified bindings; RESULTS NOT COMPUTED HERE (discovery only).
Parent (chosen via choose_work, operation=evolve): `[prior hypothesis]`
(board leader, valid, mu ~34, generation 7, reference_delivery complete).

## 0. Disposition of the three expert demonstrations (this episode)
- **Natural-history generative transformers (Nature 2025, s41586-025-09529-3).** Adaptation not
  pursued this episode: the HCC island has no longitudinal multi-organ generative-training
  infrastructure and the parent's estimand is a single-event landmark Cox; a generative model would
  not test the frozen claim. Recorded as a deferral, not a missing dependency.
- **Longitudinal routine clinical data for cancer (Cell 2026, S009286742600807X).** Main article
  unavailable (HTTP 403/401); only supplement + metadata inspected upstream. The demonstration is the
  closest conceptual match (routine longitudinal EHR → cancer detection/treatment) and is relevant to
  the AFP-trajectory design, but its full methods could not be inspected, so no method is imported
  from it.
- **Bayesian longitudinal EHR + genetic discovery (Nature 2026, s41586-026-10780-5).** Inspected
  (article + supplement text). Its longitudinal Bayesian state model is conceptually close to the
  "informative observation" threat here; a full joint observation-process model is explicitly
  DEFERRED (revisit condition in Section 5) because it is assumption-bound and not needed to answer
  the validity question first.

## 1. Unresolved question and clinical importance
After liver-directed therapy (LDT: TACE / resection / ablation) for HCC, follow-up repeats serum AFP,
albumin and bilirubin. The parent asks whether the *within-patient AFP trajectory* adds prognostic
information beyond **baseline AFP** and beyond **same-draw ALBI kinetics** for time to radiologic local
progression, free of immortal-time/lead-time bias. Clinically this decides whether serial AFP should
drive risk-adapted imaging intensity after LDT.

The parent's own worst objection: the primary progression endpoint is an **unvalidated lexical
extraction** from examination reports, and its only validation plan is a **manual 150-report audit** —
human-dependent, unbounded, and it *assumes* rather than estimates the Se/Sp it propagates. If the
lexical endpoint is badly misclassified, every hazard ratio (including the parent's) is
uninterpretable. This episode closes that gap with a COMPUTABLE validation.

## 2. Hypothesis (falsifiable)
- **H1 (leading claim):** a rising within-patient AFP slope on (index, t*] is associated with shorter
  time to local progression independently of baseline AFP and same-draw ALBI kinetics.
- **R0 (strongest rival):** the association is an artifact of outcome misclassification — it does not
  survive bias-correction for the lexical endpoint's (Se, Sp), or it is confined to reports that fail
  the latent-class classification.

## 3. Frozen inherited design (VERBATIM, unchanged)
- Population: HCC diagnosis (`诊断名称` contains `肝细胞癌`/`肝癌`) AND >=1 liver-directed procedure.
- Join key: `患者主索引` + `就诊号`. Index = earliest qualifying liver-directed procedure.
- Landmark t* = index + 180 d (90 d sensitivity).
- Exposure (AFP/ALBI slopes) fit ONLY on draws in (index, t*].
- Same-draw AFP + albumin + total-bilirubin pairing within +/-2 d on `检验时间`;
  ALBI = 0.66*log10(bilirubin) - 0.085*albumin.
- Endpoint: modality-restricted abdominal local progression from `检查` reports
  (`检查所见`/`检查诊断` contains 增大/进展/复发/新发/增多); `转移` = competing event; repeat
  liver-directed procedure = retreatment proxy (secondary). Censor via `出院时间`. No survival/mRECIST claim.
- Four rivals each mapped to a distinct test; conjunctive falsification; graded-vs-threshold monotone
  dose-response across AFP-slope quartiles.

## 4. THIS EPISODE'S ONE ADDED ELEMENT: computable latent-class outcome-ascertainment validation
Replace the parent's human 150-report audit with an entirely computational validation of the lexical
progression endpoint. Three pre-specified, conditionally-independent within-dataset indicators:
1. **Pathology-confirmed recurrence / viable tumor** — `data_病理_3292603985559017792.csv`
   (`患者主索引`,`就诊号`,`病理`,`检查所见`,`检查诊断`). LIMITATION (probe-verified this session):
   the pathology table has **no timestamp column**, so anchoring it to the landmark window is only
   possible through the linked `就诊号`/encounter ordering; this is a stated weakness and is why
   pathology is one of three indicators, not the sole reference.
2. **New systemic-therapy escalation** — `data_用药_5693407050835159466.csv`
   (`用药`,`开始时间`,`药品类型`) for HCC systemic agents (索拉非尼/仑伐替尼/瑞戈非尼/阿帕替尼/
   贝伐珠单抗/信迪利单抗/卡瑞利珠单抗 ...). Exact label set to be frozen after a probe of `用药`.
3. **Repeat liver-directed procedure after index** — `data_手术_8024330590283626027.csv`
   (`手术`,`开始时间`,`手术来源`), restricted to liver-directed labels, excluding diagnostic
   `肝动脉造影`.

Analysis:
(a) Fit a **latent-class model** (Hui-Walter; EM) for the binary lexical progression flag with the
    three indicators, under a pre-registered conditional-independence structure, to ESTIMATE
    prevalence, Se and Sp (bootstrap CI) from the data — no assumed prior range.
(b) **Bias-correct the primary per-1-SD AFP-slope Cox HR** using the estimated Se/Sp
    (matrix/quantitative bias analysis; Monte-Carlo propagation of the Se/Sp bootstrap distribution,
    >=20k draws). Report the corrected HR distribution and whether its 95% interval excludes 1 with the
    pre-specified sign.
(c) **Baseline (comparison):** naive agreement of the lexical flag with each single indicator and with
    an "any-2-of-3" composite, plus the uncorrected Cox HR.

### Falsification branches
- **Supportive:** latent-class Se/Sp identifiable with CI excluding 0.5/1 bounds (>=30 events) AND the
  bias-corrected per-1-SD AFP-slope HR CI excludes 1 with the pre-specified sign AND the monotone
  quartile trend persists (p_trend<0.05, Q2-vs-Q1 CI excludes 1).
- **Adverse:** corrected HR CI includes 1 (association attributable to misclassification), OR the
  effect is confined to reports the latent-class assigns to the "false-positive" class.
- **Inconclusive:** latent class non-identifiable / unstable (Se or Sp CI spans the non-informative
  bound); <30 interval-scheduled events; <10/quartile (tertile fallback pre-declared). Escalate to
  expert radiologist mRECIST adjudication.
- **Precise-null:** conjunctive equivalence vs baseline-only model M0 within +/-0.01 C-index.

### Remaining dependency (explicitly not computed here)
mRECIST radiologist adjudication remains the gold standard; the latent-class Se/Sp are
assumption-dependent (conditional independence). This experiment estimates and propagates
misclassification; it does NOT replace expert adjudication and does NOT establish causal mechanism.

## 5. Method comparison (baseline vs substantive alternative) — recorded before selection
- **M0 (baseline):** naive concordance + uncorrected landmark Cox (baseline AFP + baseline ALBI +
  age/sex/procedure type).
- **M4 (alternative):** latent-class (Hui-Walter) validation estimating Se/Sp from the data + bias
  analysis propagated through the same Cox. What M4 recovers that M0 loses: outcome validity is
  *estimated* rather than assumed, and the primary estimand becomes a bias-corrected association with
  a quantifiable uncertainty that can turn a positive signal into a null. Target: per-1-SD AFP-slope HR
  and its corrected distribution. Split: single-institution full cohort with bootstrap UIs (no
  held-out tuning needed for a descriptive association; a random 50% split is used as a stability check).
- **Budget:** CPU-only, minutes-scale (pandas + lifelines/statsmodels + a small EM loop).
- **Deferred with revisit conditions:** shared-parameter observation-process joint model and
  Fine-Gray competing-risks model — revisited only if the latent class is identifiable and a residual
  informative-observation objection remains.

## 6. Data bindings (exact sources; all under [internal dataset path], read-only)
| Purpose | File | Key columns | SHA-256 (from datasets/hcc/README.md) |
|---|---|---|---|
| procedures | `data_手术_8024330590283626027.csv` | 患者主索引,就诊号,手术,开始时间,结束时间,手术来源 | 68e383ad… |
| examinations | `data_检查_4203595081195465282.csv` | 患者主索引,就诊号,检查,检查所见,检查诊断,开始时间,检查号 | 4b650f40… |
| labs | `data_检验_609065997844652188.csv` | 患者主索引,就诊号,检验,定性结果,定量结果,标本类型,检验时间 | 9227b422… |
| encounters | `data_基本信息_2500296761891079109.csv` | 患者主索引,就诊号,年龄,性别,就诊时间,入院时间,出院时间 | 2efb2c90… |
| diagnoses | `data_诊断_7504718184492840569.csv` | 患者主索引,就诊号,诊断名称,诊断类型 | 70656580… |
| pathology (new) | `data_病理_3292603985559017792.csv` | 患者主索引,就诊号,病理,检查所见,检查诊断 | 7ad2d61c… |
| medications (new) | `data_用药_5693407050835159466.csv` | 患者主索引,就诊号,用药,开始时间,药品类型 | 9a070fc0… |

Probe verified THIS session: exact headers of labs/examinations/pathology/medications/procedures;
`诊断名称` contains `肝细胞癌` (e.g. 14801674/10_392492 原发性肝细胞癌…肿瘤复发); examinations
include 肝脾及门脉, 上腹部平扫+增强＋DWI+MRCP, 肝脏超声造影, 肝肿瘤射频治疗. Prior-episode probes
(inherited, disclosed) measured 43,815 HCC-dx patients and 40,689 loose liver-directed patients over
242,770 rows, index range 2010-04-25..2025-12-31.

## 7. What the solver must produce (deliverable definition)
Newly computed: (i) the three-indicator indicator matrix on the frozen population; (ii) latent-class
Se/Sp/prevalence with bootstrap CIs; (iii) the corrected per-1-SD AFP-slope HR distribution; (iv) the
baseline concordance table. Completion = `results.json` (corrected HR, CI, Se/Sp, event counts,
quartile trend) + `audit_frame.csv` (per-report indicator/composite classification).
