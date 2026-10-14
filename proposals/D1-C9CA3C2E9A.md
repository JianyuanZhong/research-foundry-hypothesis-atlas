> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# Imaging-anchored progression endpoint: does the AFP trajectory beat the liver-reserve (ALBI) trajectory after liver-directed therapy for HCC?

Island: hcc (single-institution Chinese hospital HCC records). Episode 4. Child of
`[prior hypothesis]` (the episode-2/3 leader).
Status: design + probe-verified bindings; RESULTS ARE NOT COMPUTED HERE (discovery only).

## 1. Unresolved question, opening, clinical importance

After liver-directed therapy (TACE / resection / ablation) for HCC clinicians repeat routine
serum panels at follow-up, and the interval to re-imaging is one of the few levers the clinic
controls. The parent candidate asked whether the *within-patient trajectory* of AFP adds
prognostic information beyond the *baseline value*, and whether AFP kinetics add information
beyond liver-reserve (ALBI) kinetics measured in the same draws. **Its central unresolved
objection is the outcome**: it had to use time-to-liver-directed-retreatment, an explicitly
practice-pattern proxy, because progression/mortality were reported to need imaging or registry
adjudication [parent critique]. A trajectory that "predicts" a practice-pattern endpoint may
predict the *decision to retreat* (driven by the same labs) rather than tumour progression -
which is exactly [K3]'s warning that real-world longitudinal associations attenuate under proper
landmark/time-dependent analysis.

**Opening:** the imaging reports that were assumed unavailable are in fact present and dated
(`examinations`, 1.7M rows, with `检查诊断` progression/recurrence descriptors - probe P1).
So the outcome can be moved from a practice-pattern proxy to a **time-stamped radiologic
progression event**.

**Clinical importance:** if AFP kinetics independently predict radiologic progression beyond
baseline AFP *and* beyond contemporaneous liver-reserve kinetics, then tailored AFP-triggered
earlier re-imaging is justified. If only liver-reserve kinetics matter, AFP-only monitoring
should be de-emphasised and imaging intervals tied to liver function. Either way the answer
changes a surveillance-interval decision; a clean null is also useful.

## 2. Substantive advance over the parent and over [K1]-[K3]

- Over the **parent**: primary outcome becomes radiologically-anchored and dated rather than a
  practice-pattern retreatment proxy; the retreatment proxy is retained as a *secondary*
  endpoint for a pre-specified concordance check (does the imaging flag agree with the actual
  retreat decision?). This directly attacks the parent's stated worst objection.
- Over [K1] (AAPS): K1 uses a fixed >=50% AFP dichotomisation and static ALBI; we use a
  continuous same-draw trajectory with ALBI kinetics as the competing exposure.
- Over [K2]: K2 measures ALBI only at baseline; here liver-reserve *kinetics* is the explicit
  rival, so an AFP signal must survive adjustment for contemporaneous liver reserve.
- Over [K3]: K3 is methodological; we apply its landmark/time-dependent cautions to HCC.

## 3. Population, temporal boundaries, index and landmark

Source: the frozen hcc snapshot (`datasets/hcc/metadata.json`, snapshot_id
[source checksum]`).

- Unit: patient (`患者主索引`), encounter key `就诊号`.
- Population: patients with a documented HCC diagnosis in `diagnoses` (`诊断名称` matching
  HCC terms e.g. 肝细胞癌 / 原发性肝癌) AND >=1 liver-directed procedure in `procedures`
  (`手术` in {TACE, 肝切除/肝癌切除, 消融/射频, 微波...}, `开始时间` parseable).
- Index = earliest such procedure `开始时间`; restrict to 2010-07-29 .. 2026-01-01 (observed
  data range). Current implementation of the date range must respect the frozen snapshot.
- Landmark t* = index + 180 days (pre-specified; a 90-day landmark is a sensitivity variant).
  Exposure is fit **only** on draws in (index, t*]; follow-up starts at t* (removes
  immortal-time/lead-time bias and future-draw leakage, the parent's fix, retained here).
- Inclusion for the trajectory model: >=1 same-draw AFP+albumin+bilirubin pair in
  (index, t*] (draws matched within +/-2 days on `检验时间`).
- Endpoint cohort: patients alive/uncensored at t* with >=1 dated post-landmark imaging report.

## 4. Variables - exact bindings

All files are read-only sources; analyses/derived files live in the workspace.

| role | source file | columns | notes |
|---|---|---|---|
| index & retreatment procedure | `HCC/data_手术_8024330590283626027.csv` (table `procedures`) | `患者主索引`,`就诊号`,`手术`,`开始时间`,`结束时间` | `手术` literal procedure name; `开始时间` `%Y-%m-%d %H:%M:%S` |
| labs (AFP, albumin, total bilirubin) | `HCC/data_检验_609065997844652188.csv` (table `labs`) | `患者主索引`,`就诊号`,`检验`,`定量结果`,`定性结果`,`标本类型`,`检验时间` | exact analyte labels 甲胎蛋白 (AFP), 白蛋白 (albumin), 总胆红素 (total bilirubin); MANDATORY exclusion of look-alikes 甲胎蛋白异质体(AFP-L3), 前白蛋白, 糖化白蛋白, 体液总胆红素 |
| imaging progression | `HCC/data_检查_4203595081195465282.csv` (table `examinations`) | `患者主索引`,`就诊号`,`检查`,`检查所见`,`检查诊断`,`开始时间`,`检查号` | abdominal contrast/ultrasound/PET exams (probe P1); progression term list below |
| HCC dx & secondary recurrence text | `HCC/data_诊断_7504718184492840569.csv` (table `diagnoses`) | `患者主索引`,`就诊号`,`诊断名称`,`诊断类型` | free-text dx incl. 复发/转移; NOT time-stamped -> secondary only |
| narrative (出院诊断/诊疗经过) | `HCC/data_病历文书_8434587325530196878.csv` (table `clinical_documents`) | `患者主索引`,`就诊号`,... | secondary concordance only |
| demographics/covariates | `HCC/data_基本信息_2500296761891079109.csv` (table `encounters`) | `患者主索引`,`就诊号`,`年龄`,`性别`,`就诊时间`,`入院时间`,`出院时间` | age/sex for adjustment; censoring uses `出院时间` |

Join key everywhere: **(`患者主索引`, `就诊号`)**. No cross-dataset joins (domain rule).

## 5. Outcomes and adjudication (honest)

- **Primary (proposed):** time from t* to first dated post-landmark `examinations` report whose
  `检查诊断` (or `检查所见`) documents progression/recurrence, over abdominal contrast/ultrasound/
  PET exams. Term set: 进展, 复发, 转移, 新增, 增大, 活性(残留/存活), together with explicit
  negation / historical-marker handling. **This lexical extraction is UNVALIDATED** (metadata.json
  validates only a cirrhosis lexical-context detector enabling explicit negation / historical /
  uncertainty / family-history / hypothetical axes). It is therefore a *candidate* endpoint that
  must pass a mandatory validation sub-step before any inferential claim:
  1. face-validity audit of >=200 flagged and >=200 unflagged reports by term-level inspection
     (the discovery/solver reports the observed precision/recall against manual review of a
     sampled subset; the sampled audit is deterministic and its script/seed are published);
  2. concordance with the independently time-stamped **retreatment proxy** from `procedures`
     (kappa + time-ordering) and with non-time-stamped recurrence text in `diagnoses`.
  If the validation sub-step fails a pre-set agreement floor, the primary endpoint reverts to
  the retreatment proxy and the imaging endpoint is reported as exploratory - this is an
  explicit, pre-registered fallback, not a silent substitution.
- **Secondary:** retreatment proxy (parent's endpoint); discharge-status count only.
- **NOT available / needs adjudication or another study:** mortality (death diagnosis only
  ~29 patients in a prior probe; under-ascertained), mRECIST objective response, and true
  progression-free survival need imaging read by a radiologist or registry linkage. No survival
  claim will be asserted from in-hospital death fields.

## 6. Baselines, substantive alternative, analysis

- **M0 baseline (simple):** Cox on baseline-only covariates: log10 AFP at index, ALBI grade at
  index (ALBI = 0.66*log10(bilirubin[umol/L]) - 0.085*albumin[g/L] using the source's lab units;
  no unit column -> within-assay only), age, sex, treatment type, imaging-intensity count.
- **M4 substantive alternative (same question):** per patient, fit AFP and ALBI as joint linear
  mixed-effects trajectories in (index, t*] on same-draw pairs (random intercept + slope), export
  empirical-Bayes slopes, then enter both slopes in a landmark Cox from t*. **What the alternative
  reveals that the baseline loses:** whether *change* adds information beyond *level*, and, by
  having ALBI slope in the same model, whether AFP slope is tumour-burden information rather than
  liver-reserve information. A third variant replaces the two slopes with the joint M4 model's
  fitted value at t* to separate trajectory shape from end-of-window level.
- **Model comparison target:** held-out (5-fold, patient-level) delta-C-index of M0 vs M4, and
  the two slope HRs with 95% CIs. Fitting on CPU (mixed-effects + Cox; ~10k-30k patients) is
  cheap; a torch/GAM variant is optional and only if the slope model underfits.

## 7. Rival explanations and their discriminating tests

1. **Baseline severity / liver reserve** - test: AFP slope and ALBI slope in the same model; the
   predicted attenuation of the AFP HR when ALBI is present ([K2]'s axis).
2. **Surveillance / imaging & draw intensity** - test: add post-index draw count and imaging count
   as covariates; sensitivity restricted to patients with >=3 paired draws in the window (parent's
   fix). Adverse prediction: slope HR moves toward 1 when intensity is modelled.
3. **Regression to the mean / lead-time** - test: restrict to >=2 pre-index AFP draws and add a
   pre-index slope proxy; measure attenuation.
4. **Measurement / extraction** - the imaging flag is text-derived and unvalidated (see 5);
   labs have no unit column so cross-assay pooling is not attempted.

## 8. Falsification criteria (pre-specified, conjunctive)

Null/equivalence if BOTH (a) the 95% CI of the AFP-slope HR and the ALBI-slope HR in M4 include 1,
AND (b) the bootstrap 95% CI of the held-out delta-C-index (M4 - M0) lies within +/-0.01.

- **Supportive:** >=1 slope HR excludes 1 with the predicted direction AND delta-C-index CI
  excludes 0 in the same direction; then the specific marker is informative beyond baseline.
- **Adverse:** the AFP-slope HR attenuates into the null once ALBI slope and draw intensity enter
  (K3-style attenuation), i.e. the apparent trajectory signal is a liver-reserve/surveillance
  artefact - a genuinely useful negative.
- **Inconclusive:** wide CIs from low event count, or the imaging flag failing its validation
  floor, or median follow-up from t* too short; report event rate and follow-up as the first
  feasibility outputs and do not force a directional conclusion.

## 9. Deliverable, alternatives not chosen, and limits

What must be newly fitted: the validation sub-step (precision/recall of the imaging progression
flag), the joint AFP/ALBI mixed-effects trajectories, and the landmark Cox models M0/M4 with
delta-C-index. Completion = event rate + validation agreement + both slope HRs + delta-C-index,
all linked to computed outputs.

Alternatives not chosen: (i) a sequence/deep model over lab trajectories (would need many more
draws per patient and would still need the same endpoint) - deferred, not banned; the mixed
model is the substantively appropriate learned component here. (ii) mortality/PFS endpoints -
blocked by ascertainment/adjudication, documented in section 5. In later episodes the imaging
endpoint could be revisited with a validated NLP extractor.

Honest limits: single institution; labs lack units; imaging flag unvalidated until the sub-step
passes; retreatment is a practice-pattern proxy; no causal/mechanistic claim (an association
surviving adjustment does not identify mechanism); key references are abstract-only; no outcomes
computed in this discovery episode.

Dispositions of the three demonstrations (required): (D1) generative-transformer natural history -
requires large multimodal longitudinal sequences absent here; bounded adaptation (a generative lab-trajectory
model) is deferred because the question is answerable with mixed-effects/Cox. (D2) Cell 2026
longitudinal routine clinical data - main article unavailable (403/401, only supplement retrieved),
so full methods cannot be inspected; not reproduced. (D3) Bayesian longitudinal EHR+genetic
framework - requires genetics, absent in this source (explicit missing dependency); its joint
longitudinal idea informs the mixed-effects component. Expert seeds: `expert_seed_candidates` is
empty in inputs.json, so no seed was retrievable this episode.
