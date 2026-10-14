> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Outcome-misclassification validation and bias-corrected AFP-trajectory test after liver-directed therapy for HCC

Island: hcc. Episode 22 (Lead). Operation: evolve/repair of [prior hypothesis] (ep21, repairable).
Parent of parent: board leader [prior hypothesis] (mu ~34, valid, refdel complete).
Status: design + probe-verified bindings and indicator label sets; RESULTS NOT COMPUTED HERE (discovery only).
The ep21 blocker (three inspected key works) is now resolved (Section 8, work/key-references.json).

## 0. Disposition of the three expert research demonstrations
- Natural-history generative transformers (Nature 2025, 10.1038/s41586-025-09529-3). Deferred, not a missing dependency:
  no longitudinal multi-organ generative-training infrastructure on this island; the frozen estimand is a single-event
  landmark Cox, which a generative model would not test.
- Longitudinal routine clinical data for cancer (Cell 2026, 10.1016/j.cell.2026.07.009). Main text unavailable (HTTP 403/401);
  only supplement+metadata inspected. Closest conceptual match but full methods not inspected, so no method imported.
- Bayesian longitudinal EHR + genetic discovery (Nature 2026, 10.1038/s41586-026-10780-5). Inspected (article+supplement).
  Its longitudinal state model is close to the informative-observation threat; a shared-parameter observation-process model
  is explicitly DEFERRED (revisit condition, S5).

## 1. Unresolved question and clinical importance
After liver-directed therapy (LDT: TACE / resection / ablation) for HCC, follow-up repeats serum AFP, albumin, total bilirubin.
Open question: does the within-patient AFP trajectory add prognostic information beyond baseline AFP AND beyond same-draw
liver-reserve (ALBI) kinetics for time to radiologic local progression, free of immortal-time/lead-time bias and of outcome
misclassification? Clinically this decides whether serial AFP should drive risk-adapted post-LDT imaging intensity.
The parent's worst objection remains: the primary progression endpoint is an unvalidated lexical extraction whose only
validation plan was a human-dependent 150-report audit that ASSUMED the Se/Sp it propagated. This replaces it with a
COMPUTABLE validation that ESTIMATES Se/Sp from the data.

## 2. Hypothesis (falsifiable)
- H1 (leading claim): a rising within-patient AFP slope on (index, t*] is associated with shorter time to local progression
  independently of baseline AFP and same-draw ALBI kinetics.
- R0 (strongest rival): the association is an artifact of outcome misclassification - it does not survive bias-correction for
  the lexical endpoint's (Se, Sp), or is confined to reports failing latent-class classification.
The discriminating comparison: H1 predicts a sign-stable, CI-excludes-1 bias-corrected HR; R0 predicts attenuation to the null
(or localisation to misclassified reports).

## 3. Frozen inherited design (VERBATIM, unchanged)
- Population: HCC diagnosis (诊断名称 contains 肝细胞癌/肝癌) AND >=1 liver-directed procedure.
- Join key: 患者主索引 + 就诊号. Index = earliest qualifying liver-directed procedure.
- Landmark t* = index + 180 d (90 d sensitivity). Exposure (AFP/ALBI slopes) fit ONLY on draws in (index, t*].
- Same-draw AFP + albumin + total-bilirubin pairing within +/-2 d on 检验时间; ALBI = 0.66*log10(bilirubin) - 0.085*albumin.
- Endpoint: modality-restricted abdominal local progression from 检查 reports (检查所见/检查诊断 contains 增大/进展/复发/新发/增多);
  转移 = competing event; retreatment proxy secondary; censor via 出院时间. No survival/mRECIST claim.
- Four rivals each mapped to a distinct test; conjunctive falsification; monotone dose-response across AFP-slope quartiles.

## 4. THIS EPISODE'S ONE ADDED ELEMENT: computable latent-class outcome-ascertainment validation
Replace the parent's human 150-report audit with an entirely computational validation of the lexical progression endpoint using
three pre-specified, conditionally-independent within-dataset indicators (label sets PROBE-VERIFIED this session, S6):
1. Pathology-confirmed recurrence/viable tumor - data_病理_3292603985559017792.csv (患者主索引,就诊号,病理,检查所见,检查诊断).
   LIMITATION (probe-verified): pathology has NO timestamp, so anchoring to the landmark window is possible only via the linked
   就诊号/encounter ordering; stated weakness, and the reason pathology is one of three indicators, not the sole reference.
2. New systemic-therapy escalation - data_用药_5693407050835159466.csv (用药,开始时间,药品类型). Frozen substring label set:
   {甲苯磺酸索拉非尼,索拉非尼,仑伐替尼,瑞戈非尼,阿帕替尼,贝伐珠单抗,信迪利单抗,卡瑞利珠单抗,替雷利珠单抗,多纳非尼,阿替利珠单抗,度伐利尤单抗,纳武利尤单抗,帕博利珠单抗}.
3. Repeat liver-directed procedure after index - data_手术_8024330590283626027.csv (手术,开始时间,手术来源), restricted to
   liver-directed labels EXCLUDING diagnostic 肝动脉造影. Frozen set: {经导管肝动脉栓塞术,动脉化疗栓塞,经动脉造影化疗栓塞术（TACE）,
   肝动脉造影化疗栓塞术,经导管肝动脉栓塞术+动脉化疗栓塞,肝叶部分切除术,肝叶切除术,腹腔镜下肝部分切除术,特殊肝段切除术,部分肝切除术,
   超声引导下肝病损微波消融术,超声引导下肝病损射频消融术}.

Analysis: (a) fit a latent-class (Hui-Walter; EM) model estimating prevalence and per-indicator Se/Sp from the three-indicator
pattern on the frozen population; (b) Monte-Carlo (20k) propagate estimated Se/Sp through the primary per-1-SD AFP-slope Cox HR,
report the bias-corrected HR distribution and whether its 95% interval excludes 1 with pre-specified sign; (c) concordance baseline
of the lexical endpoint vs latent-class class, discordance tabulated by descriptor (triggered vs interval-scheduled).

Falsification branches:
- Supportive: bias-corrected HR CI excludes 1 with pre-specified sign AND monotone quartile trend persists (inherited p_trend<0.05,
  Q2-vs-Q1 CI excludes 1, >=30 events) AND latent-class concordance adequate.
- Adverse: bias-corrected HR CI includes 1 (association attributable to misclassification), OR effect confined to reports failing
  latent-class classification (false-positive-driven signal).
- Inconclusive: Se/Sp not estimable/unstable (bootstrap CIs spanning 0.5), <30 interval-scheduled events, or <10 events/quartile
  (tertile fallback pre-declared) -> escalate to expert radiologist mRECIST adjudication or another study.
- Precise-null: conjunctive equivalence vs baseline-only M0 within +/-0.01 C-index.

## 5. Method comparison (baseline vs substantive alternative), recorded before selection
- M0 (simple baseline): baseline-value landmark Cox (baseline AFP + baseline ALBI + age/sex/procedure type).
- M4 (scientific alternative): joint mixed-effects models for AFP and ALBI slopes; individual BLUPs entered into the Cox.
  What M4 recovers that M0 loses: change-vs-level information and shrinkage across sparse/irregular schedules - it estimates the
  RATE of change rather than one anchor value, the point of a "trajectory" question. If the AFP-slope coefficient under M4 collapses
  toward 0 while baseline AFP stays prognostic, the trajectory framing is not supported.
- Deferred with revisit conditions: shared-parameter observation-process joint model and Fine-Gray - both computable from the same
  tables; revisited only if latent-class validation passes and a residual informative-observation objection remains. CPU-only, minutes-scale.

## 6. Data bindings (probe-verified this session against frozen sources; SHA-256 from datasets/hcc/README.md)
- procedures: [internal dataset path] (68e383ad...)
- examinations: [internal dataset path] (4b650f40...)
- labs: [internal dataset path] (9227b422...)
- encounters: [internal dataset path] (2efb2c90...)
- diagnoses: [internal dataset path] (70656580...)
- pathology: [internal dataset path] (7ad2d61c...)
- medications: [internal dataset path] (9a070fc0...)
Headers confirmed this session: labs 检验,定性结果,定量结果,标本类型,检验时间; procedures 手术,开始时间,结束时间,手术来源;
medications 用药,单次用药计量,频次,开始时间,结束时间,用药方式,药品类型; pathology 患者主索引,就诊号,病理,检查所见,检查诊断,机器型号;
examinations 检查,检查所见,检查诊断,开始时间,机器型号,检查号.

## 7. What the solver must produce (deliverable definition)
Newly computed: (i) three-indicator matrix on the frozen population; (ii) latent-class Se/Sp/prevalence with bootstrap CIs;
(iii) bias-corrected per-1-SD AFP-slope HR distribution (M0 and M4); (iv) baseline concordance table. Completion = results.json
(corrected HR+CI, Se/Sp, event counts, quartile trend) + audit_frame.csv (per-report indicator/composite classification).
A reference solution is optional for this open-ended validation.

## 8. Key references (three distinct inspected works; see work/key-references.json)
[K1] Masior et al., Cancers 2023 (doi:10.3390/cancers15153962, PMID 37568778) - AFP behaviour after first TACE is clinically
informative about tumour response (supports relevance; does not test a slope vs ALBI kinetics).
[K2] Donbraye et al., Front Vet Sci 2026 (doi:10.3389/fvets.2026.1704414, PMC12976743) - METHOD precedent: Se/Sp estimated with
NO gold standard by a conditional-independence latent-class model, with explicit dependence sensitivity (bounds the assumption).
[K3] Kumari et al., J Clin Exp Hepatol 2027 (doi:10.1016/j.jceh.2026.103669, PMID 42831061) - ALBI independently carries hepatic-reserve
prognostic information (bounds the claim: a rising AFP slope may reflect liver reserve, not tumour biology).

## 9. Honest limits
mRECIST radiologist adjudication remains the external gold standard and is NOT replaced; the conditional-independence assumption is
unverified (bounded by [K2]); the pathology indicator has no timestamp; single institution; no survival claim; no causal claim without
expert review or another study; no outcomes computed in discovery. The deliverable is a proposal for a computable validation test.
