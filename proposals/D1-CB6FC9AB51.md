# Proposal: imaging-workflow-specific post-TACE recorded-care pathways after all-index early transitions

## Episode, parent, and substantive repair

This is an Episode-27 successor of assessed-valid parent `[prior hypothesis]`. It preserves the parent’s one first-index-per-patient HCC population, timed 24-hour TACE-like index construction, all-index early-transition accounting through day 45, L=14 and L=45 information boundaries, component-resolved AFP/albumin/total-bilirubin profile, observation/capture modeling, competing recorded-care states, patient-level temporal split, clustered uncertainty, and strict recorded-care evidence boundary.

The remaining clinically consequential ambiguity is narrower than “is there any later code?” A strict procedure-plus-same-encounter-order record can still be a planned, copied, canceled, or technically different record. The successor therefore makes a substantive pathway-specific repair: it asks whether that concordant pair is followed by a time-bounded liver-directed imaging-workflow record. The new endpoint is intended to identify a more coherent *locally recorded treatment-follow-up pathway*, not to label treatment completion or radiologic response.

The future solver’s deliverable is newly estimated, not a presumed positive result:

1. An all-index index/trajectory manifest with early absorbing transitions and observation opportunity for every eligible patient.
2. Mutually exclusive post-boundary evidence tiers: imaging-workflow-supported concordance, procedure-plus-order concordance without imaging workflow, procedure-only, broad/ambiguous, diagnostic/technical, non-liver and local-observation-loss.
3. A transparent evidence-tier multi-state analysis and a directionally timed multi-view pathway model, each with locked predictions, uncertainty, calibration, overlap/positivity diagnostics and falsification outputs.
4. A source-concordance audit showing which procedure, order and examination rows generated each tier, their exact times, encounter keys and status/narrative sensitivity flags.
5. An interpretation file linking every conclusion to a computed estimate, interval, endpoint tier, boundary, split and frozen criterion.

Completion does not require a supportive result. It requires the frozen manifests, both prespecified analyses or a documented convergence/feasibility deferral, uncertainty and falsification outputs, and an interpretation that does not upgrade recorded workflow to clinical truth.

## Strongest supported claim, unresolved claim and hypothesis

The strongest available evidence is data-structural, not clinical: the HCC snapshot has dated procedure, non-drug-order and examination rows joinable to encounters by patient and encounter keys; the examination table has a usable start time and examination-name field. A read-only bounded audit found 419,996 examination rows, 419,714 with nonmissing `开始时间`, and names containing liver/abdominal imaging terms, including `肝脾及门脉`, `上腹部平扫＋增强`, `肝脏超声造影` and `肝动脉CTA`. This establishes availability of workflow evidence. It does not establish that any procedure was completed, that an examination was clinically indicated or completed as intended, or that any imaging finding was a response.

The unresolved question is:

> Among all eligible HCC patients with a first locally recorded TACE-like index, does a favorable early AFP/albumin/total-bilirubin profile predict a lower subsequent probability of an imaging-workflow-supported, procedure-plus-order recorded pathway than a discordant profile, after accounting for the same pre-index history and local observation opportunity? Is any association specific to the pathway-supported tier, or is it present equally in procedure-only and generic workflow records?

Primary hypothesis, explicitly noncausal: compared with a discordant profile, a favorable early profile is associated with a lower standardized cumulative incidence of the first **P3 pathway-supported episode** by day 320 after the information boundary. P3 requires a strict TACE-like procedure, a same-encounter TACE-like non-drug order within ±24 hours, and a liver-directed imaging-workflow examination beginning 0–45 days after that procedure. The planned practical contrast is 3 percentage points, with a two-sided patient-clustered 95% interval excluding zero at both L=14 and L=45 as the minimum signal for a supportive result. This is a design margin, not an expected or observed result.

The substantive advance over the parent is an explicit test of treatment-pathway specificity. A P3 association that is absent from procedure-only and generic non-liver/diagnostic controls would be more clinically interpretable as a coordinated local-care pathway than the parent’s C2 endpoint alone. It still would not establish treatment completion, radiologic response, progression, benefit or appropriateness.

## Population, index and temporal boundaries

Use the all-index population; do not select on a later examination, order, procedure, complete laboratory pair or continued local follow-up.

1. Read `encounters` and `procedures` separately. In `procedures`, retain every row and missing/invalid time in an audit. For valid `手术开始时间`, aggregate rows within patient `患者主索引`, encounter `就诊号`, and a 24-hour window into an episode, retaining every source row and label; episode time is the earliest valid procedure start. A TACE-like index row passes the training-frozen lexical rule: literal `TACE`, literal `动脉化疗栓塞`, or both `肝动脉` and `栓塞`. Hepatic angiography alone is not an index.
2. Select the earliest timed TACE-like episode per patient; preserve ties and a deterministic tie rule. Require linked `encounters` age >=18 and nonmissing `性别`.
3. Require a `diagnoses` row whose `诊断名称` contains `肝细胞癌`, linked through the same two keys to an encounter with `就诊时间` in [t0−180 days, t0+7 days]. Diagnosis has no native timestamp, so this is an encounter-time ascertainment proxy only.
4. Set t0 <= 2025-01-01 23:59:59 UTC/local snapshot time convention. Use only records with valid local timestamps for timed states. The source snapshot extends to 2026-01-01 in the audit; report support for each patient’s complete 365-day horizon and do not call absent records death or outside care.
5. Retain every eligible index patient, including early events, incomplete profiles, no examination, no later local record and invalid child times. At each boundary report counts and reasons for non-observation; no complete-case analysis may replace the all-index analysis.
6. Preserve the parent’s day-45 continuity analysis as a secondary, explicitly conditional descriptive comparison. The primary analysis retains first early states as absorbing competing transitions.

Information boundaries and outcome windows:

- L=14: last eligible pre-index component observation and first eligible component observation in days 7–14 after t0.
- L=45: last eligible pre-index component observation and first eligible component observation in days 7–45 after t0.
- All predictors and observation models stop at L. The primary post-boundary risk process begins after L and is followed through 365 days after t0. Report first-event cumulative incidence at 30, 90 and 320 days after t0 when supported, plus post-boundary day-365 estimates.
- The full-index transition estimand starts at t0 and reports first transitions through day 45, including early P3/P2/P1/P0/diagnostic/non-liver/local-observation-loss states. A patient with an early state is not silently removed from later summaries.

## Exact outcome ontology and pathway rule

Construct mutually exclusive first post-boundary states by highest evidence tier at the earliest qualifying episode. All rows are retained in provenance, and all child tables are aggregated before joins.

**P3, primary pathway-supported recorded episode.** A strict TACE-like procedure episode with valid `手术开始时间`; a linked `orders` row on the same (`患者主索引`, `就诊号`) whose `医嘱(非药品)` passes the same training-frozen TACE-like order screen; order `开立时间`, `开始时间` or `结束时间` is within −24 to +24 hours of the procedure episode time; and at least one linked `examinations` row for the same patient with valid `开始时间` in [procedure time, procedure time +45 days], where `检查` passes the training-frozen liver-directed imaging-workflow screen. The primary screen uses only `检查` and `开始时间`, and retains `检查号`. It is a workflow record, not an image, report adjudication or response endpoint.

The imaging-workflow screen is frozen using training data before any test evaluation. It must include either (a) a liver/upper-abdominal anatomic term (`肝`, `肝脏`, `肝动脉`, `门脉`, `腹部`, `上腹`) plus an imaging/modality term (`超声`, `CT`, `MRI`, `磁共振`, `造影`, `增强`, `DWI`, `MRCP`, `CTA`, `CTV`), or (b) a training-observed liver-directed vascular/imaging combination containing `肝动脉`, `门脉`, `肝静脉`, `CTA`, `CTV` or `造影`. The final exact token list, case/Unicode normalization and exclusions are written to `lexical_freeze.json`; no post-test vocabulary editing is permitted. Broad terms such as `肝` alone do not pass.

**P2, concordant recorded therapeutic episode without imaging workflow.** The same strict procedure-plus-same-encounter-order concordance as P3, but no qualifying examination in the P3 window. This is the parent’s C2 tier and remains a required comparator.

**P1, procedure-only strict episode.** A strict timed TACE-like procedure episode not meeting P2/P3.

**P0, broad/ambiguous/mixed liver-directed episode.** A timed liver-directed procedure record not meeting the strict lexical rule, including ambiguous or mixed labels.

**D, diagnostic/technical-only state.** A timed procedure that matches a pre-specified diagnostic/technical vocabulary but not P0–P3.

**N, non-liver procedure state.** A timed procedure that is neither P0 nor D.

**O, local observation-loss state.** The parent’s administrative local-observation state, copied with its exact rule and time convention, is retained as an absorbing observation state and never treated as a clinical outcome. If the implementation must restate it, define it before fitting as no timestamped encounter or child-table record for 180 consecutive days before the end of the available local window, with the state time at the last valid local timestamp plus 180 days, censored at 365 days. Report this operational rule separately from clinical events.

For P3, the examination may be in a different encounter because follow-up can be outpatient; same-encounter examination is a secondary tight-pathway sensitivity. The order must remain same-encounter in the primary definition. Recompute P3 using procedure-to-examination windows 0–14, 0–45 and 0–90 days; order windows ±6, ±24 and ±72 hours; same-encounter versus patient-level examination matching; and exact observed order-status restrictions. A canceled or otherwise status-inconsistent order is not silently reclassified as completion. `检查所见` and `检查诊断` are narrative sensitivity fields only: their presence or lexical content may create a secondary “report-text-supported” tier, never the primary P3 tier or a radiologic label.

P3/P2 evidence is not placed into predictors for its own endpoint. The parent’s early recorded-plan and reassessment descriptors are descriptive context only. A later examination is not evidence of response merely because its name includes enhancement, CT, MRI, ultrasound or contrast.

## Exact HCC data bindings, joins and archive status

Snapshot: `[source checksum]`. Every listed HCC source is an ordinary file; no archive member is used. Source rows are read-only. The full catalog is `[internal dataset path]`, whose HCC entry and local schemas are bound by `datasets/README.md` and `datasets/hcc/README.md`.

All joins use (`患者主索引`, `就诊号`) after verifying duplicate behavior and aggregating each child table. No many-to-many raw join is allowed.

- `encounters`, schema `datasets/hcc/table-b743286cb1249287.json`, source `[internal dataset path]`, ordinary file: `患者主索引`, `就诊号`, `年龄`, `性别`, `就诊时间`, `入院时间`, `出院时间`, `就诊科室`. These anchor t0 linkage, diagnosis ascertainment, index covariates and local observation.
- `procedures`, schema `datasets/hcc/table-d5eae16f8f8093d9.json`, source `[internal dataset path]`, ordinary file: `患者主索引`, `就诊号`, `手术`, `开始时间`, `结束时间`, `手术来源`. These define episodes and recorded pathway events.
- `orders`, schema `datasets/hcc/table-6b93dcf0ea823702.json`, source `[internal dataset path]`, ordinary file: `患者主索引`, `就诊号`, `医嘱(非药品)`, `开立时间`, `开始时间`, `结束时间`, `医嘱期限`, `医嘱状态`, `频次`. These provide same-encounter order concordance and status sensitivity; they do not prove intent or completion.
- `examinations`, schema `datasets/hcc/table-fd016d2731b9d6c6.json`, source `[internal dataset path]`, ordinary file: `患者主索引`, `就诊号`, `检查`, `检查所见`, `检查诊断`, `开始时间`, `机器型号`, `检查号`. Primary P3 uses `检查`, `开始时间`, `检查号`; narrative fields are sensitivity-only.
- `diagnoses`, schema `datasets/hcc/table-12710723c3df0c99.json`, source `[internal dataset path]`, ordinary file: `患者主索引`, `就诊号`, `诊断名称`, `诊断类型`. It has no diagnosis timestamp; linked encounter time is only an ascertainment proxy.
- `labs`, schema `datasets/hcc/table-38aad8c54471332f.json`, source `[internal dataset path]`, ordinary file: `患者主索引`, `就诊号`, `检验`, `定性结果`, `定量结果`, `标本类型`, `检验时间`. Freeze exact assay names `甲胎蛋白`, `白蛋白`, `总胆红素` from training only; preserve numeric/qualitative/inequality values, specimen, timestamp, counts and missingness. There is no laboratory-unit column; do not call the profile ALBI/MELD or pool undocumented units.
- `medications`, schema `datasets/hcc/table-4f6ecaeb6e8f69c2.json`, source `[internal dataset path]`, ordinary file: `患者主索引`, `就诊号`, `用药`, `单次用药计量`, `单次用药计量单位`, `频次`, `开始时间`, `结束时间`, `用药方式`, `药品类型`. Use only as pre-boundary capture/context features; do not infer treatment intent or completion.
- `clinical_documents`, schema `datasets/hcc/table-66afca58512c2fca.json`, source `[internal dataset path]`, ordinary file: identifier keys plus `主诉`, `现病史`, `既往史`, `个人史`, `月经史`, `婚育史`, `家族史`, `入院诊断`, `入院情况`, `入院诊断__duplicate_2`, `诊疗经过`, `出院情况`, `出院诊断`, `手术名称`, `手术经过`. It has no usable row-level time; use only descriptive, non-timed sensitivity/context and never as a timed endpoint.
- `pathology`, schema `datasets/hcc/table-0a4ee86a446c605c.json`, source `[internal dataset path]`, ordinary file: identifier keys plus `病理`, `检查所见`, `检查诊断`, `机器型号`; no usable time. It cannot adjudicate timed response.
- `vitals`, schema `datasets/hcc/table-8436de9cba74b8ca.json`, source `[internal dataset path]`, ordinary file: identifier-only `患者主索引`, `就诊号`; no measurement payload.
- `transfers`, schema `datasets/hcc/table-320c20f732e71789.json`, source `[internal dataset path]`, ordinary file: identifier-only `患者主索引`, `就诊号`; no transfer timing.
- `front_page`, schema `datasets/hcc/table-38b3224239acc33f.json`, source `[internal dataset path]`, ordinary file: identifier-only `患者主索引`, `就诊号`; no usable clinical payload.

The source catalog confirms that images, raw waveforms and a validated clinical outcome label are unavailable. No private rows or notes are sent to public search.

## Variables and profile construction

Primary profile is the parent’s component-resolved early trajectory:

- For each assay, take the last eligible pre-index value and the first eligible value in days 7–L, retaining exact timestamp, assay label, specimen, qualitative result, inequality flag and missingness.
- Freeze assay-name normalization, numeric parsing and outlier rules on the fit split. Because units are absent, do not pool values across undocumented units; use assay-specific standardized changes or within-assay rank/quantile transforms fit on training only.
- A favorable profile is a predeclared joint category: AFP decreases or is not observed as increasing, albumin does not decrease beyond a training-frozen tolerance, and total bilirubin does not increase beyond a training-frozen tolerance. A discordant profile is the complementary numeric pattern with at least one adverse component and no favorable classification. Qualitative/inequality/incomplete records are an explicit third category; the all-index model retains them and reports a favorable-versus-discordant contrast only where the standardization is identified.
- The profile is predictive evidence, not a surrogate treatment response and not a causal exposure.

Pre-index covariates are age, sex, index department, diagnosis type, encounter timing, counts and recency of procedures/orders/examinations/labs/medications, prior TACE-like or liver-directed rows, pre-index examination workflow intensity, and availability/missingness of the three assays. Post-L predictors are prohibited for the primary contrast. The examination that creates P3 cannot be a predictor for P3.

## Estimands and analysis

Let k be P3, P2, P1, P0, D, N or O and L be 14 or 45. The primary predictive standardized contrast is:

`Delta_L,k(h) = P(first recorded state k by h | favorable profile, standardized to the eligible all-index pre-index history/capture distribution) - P(first recorded state k by h | discordant profile, same distribution)`.

The primary is `Delta_14,P3(320)` with `Delta_45,P3(320)` as a co-primary boundary replication. Report absolute risk differences, risk ratios only with stable denominators, and the entire state vector at days 30, 90, 320 and 365. The all-index t0-to-day-45 multi-state estimand reports early P3/P2/P1/P0/D/N/O transitions without conditioning them away. Conditional post-boundary summaries must identify the conditioning set and are secondary.

Use 2010–2022 index dates for fitting, 2023 for tuning/vocabulary and hyperparameter decisions, and 2024–2025-01-01 for a locked temporal test when event support permits. If date support prevents a complete split, use a predeclared patient-hash split and report the reason. No patient crosses splits. Fit lexical vocabularies, profile thresholds, standardization weights, observation weights, positivity rules and any model selection using training only.

### Simple evidence-tier baseline: B_pathway

Fit regularized discrete-time cause-specific hazards/multi-state models for the mutually exclusive evidence tiers. Use fixed intervals (0–14, 15–45, 46–90, 91–180, 181–320, 321–365 days after t0) plus exact event times in a sensitivity model. Use the same covariates, profile categories, boundary, split, early absorbing states and observation process for all tiers. Standardize predictions to the all-index pre-index distribution. Report coefficients, state-specific cumulative incidence, Brier score, dynamic log score, calibration slope/intercept, calibration curves, overlap/positivity and patient-clustered 95% bootstrap intervals (1,000 patient resamples if the solver envelope permits). This baseline directly tests whether adding imaging-workflow corroboration changes the scientific claim.

### Substantive mechanistic alternative: M_sequence

Fit a continuous-time/semi-Markov multi-view pathway model with observed source streams from procedures, orders and examinations. Its states are operational recorded states, not clinical latent disease states: no qualifying downstream record; strict procedure documented; same-encounter order corroborated; liver-directed imaging workflow observed; and competing diagnostic/non-liver/observation-loss states. Include source-specific capture/missingness terms, order-to-procedure and procedure-to-examination timing kernels, and patient-level history covariates. The model estimates the joint training likelihood of the observed event streams and predicts held-out next-source/time-window observations. Weakly informative transition/timing priors or penalization are fixed before test evaluation; repeat under at least three predeclared prior strengths because no adjudicated gold standard identifies source sensitivity or specificity.

Evaluate M_sequence against B_pathway on the same locked test patients and same estimand: held-out event-stream log score, next-source Brier score and calibration, transition-time calibration, convergence/identifiability diagnostics, and the standardized P3/P2/P1 contrasts with patient-level intervals. M_sequence is scientifically useful only if it converges, yields calibrated source/time predictions and clarifies whether the P3 estimate is stable to source discordance/prior sensitivity. Its advantage is information about directional sequence and timing that a hard mutually exclusive tier loses; it does not convert a latent recorded pathway into treatment completion or radiologic response.

No model is fitted in discovery. CPU is the planned default because both candidates are tabular/event-stream likelihood fits. The future solver envelope is at most 16 CPUs, 262,144 MiB memory and 28,800 seconds, within the configured science budget only if the solver actually schedules that workload; these are unverified planning estimates, not measured runtimes. A small tabular baseline should be feasible on CPU; repeated M_sequence fits are unverified and must checkpoint parameters and report convergence. A GPU is not required. If a solver uses the configured GPU image and requests one A100, it must use allocated `cuda:0`; GPU access is capacity information, not a scientific advantage. No GPU probe was run here.

## Falsification, interpretation and uncertainty

Required checks are pre-specified:

1. Reproduce the parent’s procedure-only strict contrast, C2/P2 concordance and all-index early-transition accounting before interpreting P3. Failure is a packaging/definition failure.
2. Compare P3, P2, P1 and P0. A profile contrast confined to P1/P0, while P3 is null or unstable, is adverse to a pathway-specific interpretation and supports coding/workflow explanations.
3. Test the imaging-workflow addition: compare no examination, same-encounter examination, 0–14, 0–45 and 0–90-day examination windows. Large changes with small window shifts are evidence of ascertainment sensitivity, not clinical response.
4. Permute examination times within patient while preserving examination names, encounter structure and measurement counts; rederive P3. A similar association after permutation falsifies a timing-specific pathway interpretation. Also run pre-index examination placebo windows.
5. Permute early assay values within patient among eligible assay times while preserving specimen and missingness; compare with pre-index placebo windows. A preserved profile contrast favors capture/temporal artifact.
6. Vary order windows ±6/24/72 hours, same-encounter versus patient-level examination joins, exact `医嘱状态` restrictions and missing/invalid time handling. Universal absence of P3 matches is infeasibility; instability is adverse to endpoint specificity.
7. Use diagnostic/technical, non-liver and generic examination-workflow controls. Similar contrasts weaken a liver-treatment-pathway interpretation.
8. Retain all early states through day 45; compare L=14/L=45, weighted/unweighted observation models, incomplete-profile category versus complete-pair sensitivity, and local observation-loss handling. No analysis may silently discard early events or missing follow-up.
9. Require adequate training/test overlap, no leakage of endpoint-generating orders/exams, calibration and patient-clustered intervals. For M_sequence additionally require convergence, held-out source prediction, timing calibration and prior-sensitivity intervals. Nonconvergence, prior domination or failed positivity is inconclusive, not evidence for either hypothesis.
10. Use negative-control temporal windows and a negative-control endpoint; a robust signal that appears equally for unrelated workflow endpoints is adverse.

Supportive evidence requires: successful parent continuity; a directionally compatible P3 contrast exceeding 3 percentage points with a 95% interval excluding zero at both boundaries; weaker or null P2/P1/P0 and unrelated workflow/placebo contrasts; stable examination and order timing sensitivities; adequate overlap/calibration; and M_sequence convergence with held-out source/time calibration and materially similar P3 estimates under prior sensitivity. This supports only an association between early recorded laboratory trajectory and a more specific *locally recorded care pathway*, motivating radiology/chart adjudication or prospective validation.

Adverse evidence includes P3 null/reversal while P1/P2 persists; an effect concentrated in broad/ambiguous or canceled/status-inconsistent records; sensitivity to arbitrary examination windows or time permutations; similar non-liver/diagnostic/placebo effects; poor overlap/calibration; or M_sequence instability. This favors coding, local workflow, measurement selection or temporal confounding explanations.

Inconclusive evidence includes sparse P3 cells, no valid time-concordant matches, missing/invalid timestamps, unstable training-frozen lexical screen, insufficient 365-day support, positivity failure, temporal-split failure, missing profile information that prevents identified standardization, latent nonidentification/prior domination or intervals crossing the design margin. Inconclusive does not establish absence of response, progression, treatment benefit or clinical irrelevance.

The verifier can check source paths, schema IDs, ordinary-file status, headers, duplicate-safe joins, lexical freezing, episode/tier construction, time windows, patient splits, leakage, transition/CIF calculations, held-out predictions, calibration, uncertainty and output-to-conclusion links. It cannot establish treatment intent, treatment completion, technical success, radiologic response, viable tumor, recurrence, progression, liver failure, mortality, survival, outside care, benefit, appropriateness, utility or external validity. Those require expert radiology/chart/pathology adjudication, linked mortality and outside-care data, and external or prospective validation.

## Required solver outputs and actual scientific completion

The solver must produce:

- `index_episode_manifest.csv`
- `trajectory_manifest_L14_L45.csv`
- `early_transition_manifest.csv`
- `outcome_pathway_manifest.csv`
- `source_concordance_audit.csv`
- `lexical_freeze.json`
- `observation_process.json`
- `transition_cif.json`
- `context_stratified_cif.json`
- `predictions.parquet`
- `metrics.json`
- `calibration.json`
- `bootstrap_intervals.json`
- `overlap_and_weights.json`
- `m_sequence_parameters.json`
- `m_sequence_checkpoint_or_deferral.json`
- `negative_control_and_permutation.json`
- `interpretation.json`
- `limitations.csv`

The actual scientific deliverable is the fitted/estimated comparison of B_pathway and M_sequence on the locked temporal test, with P3/P2/P1/P0 state-specific cumulative incidence, uncertainty, calibration and falsification results. A “supported” result is not required; a correctly computed adverse or inconclusive result completes the experiment. `interpretation.json` must map each conclusion to a computed output and explicitly prohibit claims of intent, completion, response, progression, causality, mortality, survival, benefit, utility or external validity.

## Deferred alternatives and revisit evidence

- A text transformer over `clinical_documents` is deferred: the table has no usable row-level time and no validated outcome labels, so it cannot resolve whether a dated pathway was completed. Revisit with time-stamped, validated clinical text and adjudicated endpoint labels.
- Direct image or multimodal modeling is deferred: the HCC source directory contains CSV reports but no image files. Revisit with image payloads and radiology labels.
- ALBI/MELD or unit-pooled reserve scores are deferred: laboratory units are absent and INR is not established in the bound assay design. Revisit with verified units, analyte mapping and validated thresholds.
- Causal treatment-policy or survival analysis is deferred: intent, assignment, completion, mortality, survival and outside-care capture are unavailable. Revisit with treatment indication/completion, linked mortality and external-care data.
- A generic transformer over all event sequences is deferred despite possible computational feasibility: without adjudicated labels it can model documentation order but cannot answer the endpoint-validity question better than M_sequence. Revisit if validated outcome labels or an external validation cohort becomes available.
- A purely procedure-plus-order endpoint remains required as P2 rather than selected as the primary scientific endpoint, because the added examination workflow is the assigned validity repair. If the P3 cell count or temporal support is inadequate, report P2/P1 estimates as endpoint-ascertainment diagnostics and mark the pathway-specific hypothesis inconclusive; do not silently demote P2 and claim the new hypothesis was tested.
