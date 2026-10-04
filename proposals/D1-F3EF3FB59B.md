# Frozen-calendar assay result content versus measurement opportunity for subsequent HCC local encounters

## Scientific deliverable and substantive advance

The future solver must newly construct a reproducible, time-safe HCC cohort and feature ledger; fit nested Q/M/P models and a matched competing-transition model; freeze the complete primary scoring pipeline using only index anchors from 2012–2018; score that unchanged function directly in 2021–2025; and produce locked predictions, proper-score contrasts, uncertainty, calibration, audit and falsification outputs. It must separately report a prespecified 2019–2020 bridge recalibration sensitivity. Completion is the artifact set and an evidence-bounded interpretation, whether supportive, adverse or inconclusive. No model was fitted and no clinical result is claimed here.

The substantive advance is identification of a clinically relevant information question that separates three often-confounded sources of signal:

- Q: general local capture and observation/process intensity;
- M: laboratory measurement opportunity—assay selection, sampling, specimen/result availability and parse validity; and
- P: only assay-specific observed qualitative or quantitative result content.

The proposal therefore tests whether values themselves add information beyond the opportunity to obtain and document them, and whether that increment survives an actual calendar shift. It does not call a local encounter a readmission, planned treatment, recurrence or deterioration.

## Unresolved question, evidence and falsifiable hypothesis

The strongest available evidence supports only provenance and feasibility: the frozen HCC snapshot has joinable encounter, diagnosis, laboratory and process tables with the native fields and times bound below. Direct schema/header inspection confirms laboratory assay, qualitative result, quantitative result, specimen type and laboratory time, but no laboratory-unit/reference-range field. It does not establish that a coded diagnosis is active HCC, that a result was released or seen at a particular time, or that an encounter was planned or clinically necessary. No model was fitted.

The unresolved question is:

> Among adults at their first locally recorded HCC-coded encounter, does strictly pre-index assay result content P improve calibrated prediction of a subsequent local encounter within 30 days after discharge beyond general capture/process Q plus measurement opportunity M, and does that P-minus-M increment transport when a complete score frozen in 2012–2018 is applied directly to 2021–2025?

Primary hypothesis: in the locked 2021–2025 era, P will improve held-out prediction of the exhaustive R30/O90/U90 local-observation endpoint over Q+M, with a direction compatible with the prespecified 2012–2018 held-out estimate. The process hypothesis is that the P-minus-M increment is greater for R30 than for later observation O90 among those without R30. The transport claim is specifically unchanged scoring-function transport; it is not rescued by bridge recalibration.

Support would mean recorded assay values contain incremental, calibrated information beyond measurement opportunity under the tested local regime. Adverse evidence is null or harmful P-minus-M, a material sign reversal across eras, reproduction by Q/M or permutations, or a signal confined to later observation/documentation. Inconclusive evidence includes sparse later-era events or assays, wide intervals, dominant U90, invalid timing, unresolved joins, unstable parsing/vocabulary, or failure of the lock ledger. None establishes biology, causality, utility or clinical benefit.

## Population, endpoint and temporal boundaries

Use HCC snapshot `[source checksum]` and catalog [source checksum]. All sources are ordinary read-only CSV files; no archive member is used.

1. Normalize Unicode and whitespace in `患 者主索引` and `就诊号` for audit while retaining raw keys. Join diagnoses to encounters on that exact pair. An HCC-coded encounter has normalized `诊断名称` containing `肝细胞癌` or case-insensitive “hepatocellular carcinoma”; report matched strings and `诊断类型`. Diagnoses have no native time and select the cohort only.
2. Include age >=18, parseable nonnegative `入院时间` and `出院时间`, and index admission in [2012-01-01, 2026-01-01). Select the earliest eligible HCC-coded encounter per normalized patient by admission time then `就诊号`; do not replace an invalid earliest candidate with a later record. Set t0=`入院时间`, td=`出院时间`, and require td+90 days < 2026-01-01 for the primary label.
3. Encounter identity is the normalized two-key pair. Audit exact duplicate rows before collapsing them. Keep distinct encounter keys distinct. A candidate subsequent encounter must have a distinct key, parseable admission, and admission >= td; a row with admission < td is not a return even if its discharge is later. Report same-time distinct-key ties and deterministic tie handling.
4. Define the exhaustive endpoint Y90:
   - R30: at least one distinct subsequent local encounter with admission in [td, td+30 days);
   - O90: no R30 and at least one distinct subsequent local encounter with admission in [td+30 days, td+90 days);
   - U90: neither qualifying local row is observed.
   
   R30 is the primary named endpoint component, but means only a subsequent local encounter record. Report [td,td+24h) as an immediate-boundary stratum and repeat R30 as [td+24h,td+30d) in sensitivity. L60/L180 are secondary only when follow-up permits. U90 means no qualifying local row, not no care, survival, cure or complete follow-up.
5. The primary estimand is the paired held-out P-minus-M contrast in multiclass proper scores for Y90 and its R30 probability, evaluated directly in 2021–2025 by the frozen 2012–2018 score. The process estimand is P-minus-M for O90 versus U90 among non-R30 and the R30-minus-O90 contrast. Future documentation intensity in [td+30d,td+90d) is an outcome/negative control, never a predictor.

## Genuine frozen calendar transport

The primary calendar experiment has three disjoint roles:

- Development/locking: all feature vocabulary, transformations, numeric/qualitative parsing and impossible-value rules, standardization, regularization selection, coefficients and primary calibration are learned only from 2012–2018 anchors. A prespecified internal patient-level split within 2012–2018 supplies a held-out earlier-era estimate; all rows and linked history remain together.
- Quarantine bridge: 2019–2020 is not used for feature selection, vocabulary expansion, threshold selection, primary calibration, coefficient fitting, model-family selection, analyst inspection or any modification of the strict score. It may be used once, and only in a labelled secondary sensitivity, to fit a prespecified intercept/temperature or multinomial calibration map with the 2012–2018 feature map and coefficients fixed.
- Locked transport evaluation: apply the complete unmodified 2012–2018 score once to 2021–2025. Do not pool eras, move endpoint boundaries, refit, recalibrate, or redefine U90 to rescue transport. Report the earlier held-out estimate, strict-frozen 2021–2025 estimate, later-minus-earlier interaction, and separately the bridge-recalibrated 2021–2025 estimate.

The bridge can show local recalibration need; it cannot upgrade a failed strict-transport claim. If 2021–2025 has inadequate support, transport is inconclusive rather than pooled with another era. A patient-hash split (SHA-256 normalized patient key modulo 100: 0–59 fit, 60–69 selection/calibration, 70–79 locked evaluation, 80–99 inaccessible) is a secondary precision analysis only, never a substitute for the calendar experiment.

## Time-safe information blocks: Q, M and P

All predictors stop strictly before t0. A primary history row must join, via the two-key pair, to a non-index encounter with parseable admission and discharge, linked admission < t0 and linked discharge < t0, and have its native event/availability time in [t0-730d,t0):

- labs: `检验时间`;
- procedures: `开始时间`;
- orders: `开立时间`;
- medications: `开始时间`;
- examinations: `开始时间`.

Exclude index-linked rows even when their event time precedes admission. Publish invalid/missing-time, missing-linked-discharge, overlap, index-linked, post-t0, duplicate, unmatched-join and row-inflation counts. This is a conservative availability rule, not proof of result release or clinician awareness. Exclude direct identifiers.

Q contains general capture/process only: age, sex, department, admission time-of-day/era; prior completed-encounter count, duration and recency; source-specific row counts and distinct linked-encounter counts for labs, procedures, orders, medications and examinations; source-type count; invalid/excluded-time counts; left-truncation and no-history flags. Q contains no assay identity, result, specimen type or result-availability flag.

M contains measurement opportunity only: assay identity, assay-specific counts and distinct encounters, sampling-time count, recency/span, specimen type, result-present/missingness flags, invalid numeric/qualitative parse flags and assay-specific availability patterns. M contains no value magnitude or qualitative result content.

P contains only observed assay result content: valid assay-specific quantitative values and valid assay-specific qualitative values, plus within-assay change/slope only when at least two distinct valid `检验时间` values exist. P contains no specimen type, assay count, sampling count, result-present flag, parse-validity flag or missingness indicator. Values are never pooled across assays because no lab-unit/reference-range column exists; units are not inferred. Any missing-value representation must not reconstruct M. P-minus-Q may be reported as a continuity contrast, but P-minus-M is the result-content estimand.

## Matched baseline and substantive alternative

Both alternatives use identical cohort, time window, Q/M/P ledger, calendar roles, preprocessing, split, labels, locked cases and uncertainty procedure.

Baseline B is an auditable nested regularized logistic model for R30 and multinomial logistic model for Y90: B_Q, B_QM and B_QMP. It isolates the measurement-opportunity and result-content increments but loses competing event timing.

Alternative H is a matched discrete-time complementary-log-log competing-transition model: R hazards in [0,7), [7,14), [14,30), followed by O hazards in [30,60), [60,90) conditional on no R30, with the same Q/M/P inputs and interval offsets. It derives coherent R30/O90/U90 probabilities and reveals whether an apparent P increment is localized to early encounter hazard or later observation hazard—information pooled B loses. It is retained for this scientific distinction, not expected predictive gain.

The deferred alternative is an irregular sequence encoder using the same eligible pre-t0 laboratory events (time, assay identity, value, missingness and specimen type). It is not excluded because it is neural or may use a GPU. It is deferred because the primary P/M identification and calendar lock must be resolved before adding optimization/calibration variance. Revisit only if strict P-minus-M is supported or scientifically stable, event/assay support passes, and H residuals show reproducible ordering/nonlinearity. If revisited, compare on identical splits and proper scores; an allocated A100 would use `cuda:0`, but GPU feasibility is unmeasured.

Approximate future planning, not measured discovery: CPU-first B/H ledger and fits 1–4 hours; bootstrap and falsification 1–4 hours; optional sequence alternative 2–8 hours, all within <=16 CPUs, 262144 MiB RAM and 28800 seconds, with <=8 allocated GPUs. Discovery measured only schema/catalog/header and bounded feasibility inspection; no full fit, GPU probe or reference execution was run.

## Estimation, uncertainty and falsification

Primary outputs are paired held-out multiclass log loss and multiclass Brier score for Y90, with binary R30 and conditional O90 decompositions; lower is better. Report calibration intercept/slope, reliability by state, prevalence, missingness and era. Report B_QM minus B_Q, B_QMP minus B_QM, and the corresponding H contrasts; the primary result-content contrast is B_QMP minus B_QM and H_QMP minus H_QM. Report strict later-minus-earlier interaction and bridge-versus-strict difference. Select a clinically negligible score-difference margin before locked evaluation.

Use >=1,000 patient-clustered paired bootstrap resamples, preserving every linked row, transition and history per patient. Resample earlier held-out patients and locked 2021–2025 patients without refitting for strict evaluation; for bridge recalibration, repeat bridge fitting/application inside each replicate or label a fixed-bridge approximation. Report 95% intervals, denominators, event/assay support and calibration uncertainty. No p-value substitutes for uncertainty.

Mandatory falsifications and audits:

1. Permute P values within assay and calendar era while preserving M, times, row counts and missingness.
2. Permute assay identities while preserving values, times and row counts.
3. Permute specimen/result-availability labels to test the M process block.
4. Shuffle complete prior histories within partition while preserving Q.
5. Shuffle within-patient laboratory times while preserving assay/value identity.
6. Perturb calendar-era labels only in a prespecified interaction audit.
7. Repeat the 24-hour boundary definition and report immediate-boundary states.
8. Verify no post-t0, index-linked, current-anchor, future-window, duplicate-key or split-leaked feature.
9. Reconcile Y90 probabilities with binary R30/O90 scores and H competing-transition probabilities.
10. Compare future encounter/documentation intensity among R30 nonreturns; these are outcomes only.
11. Prove by lock manifest/hash that no 2019–2020 row, statistic, vocabulary, calibration parameter or analyst choice entered the strict score.

Supportive gates require: favorable strict-frozen 2021–2025 P-minus-M with a 95% interval excluding prespecified clinically negligible harm; compatible earlier direction and interaction; calibrated predictions; attenuation under payload permutation; no comparable Q/M-only explanation; no leakage sentinel; and directional concordance of B and H. Stronger return-specific support additionally requires a larger R30 than O90 contrast and stability to the 24-hour boundary.

Adverse gates are null/harmful later P-minus-M, material sign reversal, process-only reproduction, permutation persistence, leakage, or a signal limited to O90/documentation. Bridge-only improvement is adverse for unchanged transport but may support a recalibration-needed interpretation. Inconclusive gates are sparse support, wide intervals, dominant U90, unstable parser/vocabulary, invalid timestamps, unresolved count/join reconciliation, boundary instability, nonconvergence or inability to reproduce the strict lock.

## Exact HCC source bindings

All joins use normalized (`患者主索引`, `就诊号`) with raw-key, unmatched, multiplicity and duplicate audits. Paths are exact read-only ordinary files.

| table / schema | exact source path | required fields; native time and role |
|---|---|---|
| encounters / `table-b743286cb1249287` | `[internal dataset path]` | `患者主索引`, `就诊号`, `年龄`, `性别`, `就诊时间`, `入院时间`, `出院时间`, `就诊科室`; admission/discharge define cohort, history and endpoint |
| diagnoses / `table-12710723c3df0c99` | `[internal dataset path]` | `患者主索引`, `就诊号`, `诊断名称`, `诊断类型`; no native time, cohort selection |
| labs / `table-38aad8c54471332f` | `[internal dataset path]` | `患者主索引`, `就诊号`, `检验`, `定性结果`, `定量结果`, `标本类型`, `检验时间`; native lab time, M/P history and future process audit |
| procedures / `table-d5eae16f8f8093d9` | `[internal dataset path]` | `患者主索引`, `就诊号`, `手术`, `开始时间`, `结束时间`, `手术来源`; native start time, Q history/process |
| orders / `table-6b93dcf0ea823702` | `[internal dataset path]` | `患者主索引`, `就诊号`, `医嘱(非药品)`, `开立时间`, `开始时间`, `结束时间`, `医嘱时限`, `医嘱状态`, `频次`; use order time for Q, no intent claim |
| medications / `table-4f6ecaeb6e8f69c2` | `[internal dataset path]` | `患者主索引`, `就诊号`, `用药`, `单次用药计量`, `单次用药计量单位`, `频次`, `开始时间`, `结束时间`, `用药方式`, `药品类型`; native start time, Q history/process only |
| examinations / `table-fd016d2731b9d6c6` | `[internal dataset path]` | `患者主索引`, `就诊号`, `检查`, `检查所见`, `检查诊断`, `开始时间`, `机器型号`, `检查号`; native start time, Q process only |
| vitals / `table-8436de9cba74b8ca` | `[internal dataset path]` | keys only; identifier-only, audit not usable payload |
| transfers / `table-320c20f732e71789` | `[internal dataset path]` | keys only; identifier-only, cannot establish outside transfer |
| clinical_documents / `table-66afca58512c2fca` | `[internal dataset path]` | keys plus `主诉`, `现病史`, `既往史`, `入院情况`, `诊疗经过`, `出院情况`, `手术经过`; no native event time, excluded from time-safe primary inputs |
| pathology / `table-0a4ee86a446c605c` | `[internal dataset path]` | `患者主索引`, `就诊号`, `病理`, `检查所见`, `检查诊断`, `机器型号`; no native event time, excluded from time-safe primary inputs |
| front_page / `table-38b3224239acc33f` | `[internal dataset path]` | keys only; identifier-only, audit not usable payload |

## Clinical evidence gates and limitations

The experiment can computationally establish only cohort/row provenance, feature timing and block membership, endpoint construction under the stated local-record definition, proper-score differences, calibration, uncertainty, era interaction, permutation behavior, and reproducibility of the strict lock. Even favorable outputs cannot establish active HCC, stage, resectability, tumor burden, liver reserve, diagnosis timing, treatment indication/intent/receipt/completion, response, mortality, outside-care completeness, causal effect, clinical utility or safe deployment.

Those stronger claims require clinical adjudication and additional evidence: validated active-HCC/stage and outcome labels, result-release/availability timestamps, laboratory units/reference ranges, timed imaging/pathology, discharge disposition and planned/unplanned status, treatment receipt and intent, mortality/outside-care linkage, external validation and prospective silent utility/implementation evaluation. Clinical records remain read-only; analyses and derived ledgers belong in the workspace.
