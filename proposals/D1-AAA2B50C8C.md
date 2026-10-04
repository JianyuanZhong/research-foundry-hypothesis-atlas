# Proposal: separating disease-linked escalation from care-capture intensity after TACE

## Episode, parent, and actual deliverable

This episode-6 successor evolves [prior hypothesis]. It retains the HCC dataset island, one index episode per patient, day-45 landmark, paired AFP/hepatic proxy exposure, competing recorded actions, negative-control trajectory, observation-process adjustment, and strict evidence boundary. The substantive repair is to make the scientific estimand explicitly two-part:

1. Does the early trajectory associate specifically with a subsequent liver-directed recorded action, after accounting for the opportunity to be observed?
2. Does it instead primarily predict continued local contact, which would make it unsuitable as a disease-specific escalation signal?

The future solver must newly construct the cohort, fit the prespecified models, estimate cause-specific action contrasts and cumulative incidences, and produce an observation-specificity report. Discovery does not claim to have solved the question.

## Unresolved clinical question and falsifiable hypothesis

After TACE, an early fall in AFP with stable hepatic-function proxies might indicate a lower likelihood of the next liver-directed intervention. But repeat intervention is a clinician-recorded action, not a direct measure of viable tumor. Testing and return to the institution are themselves selective. The strongest supported local-data claim is only that this snapshot contains structured HCC diagnoses, dated TACE-like/procedure records, dated AFP and hepatic proxy labs, dated examination records, and encounter history. It does not establish radiologic response, tumor burden, treatment intent, death, or outside care.

Primary hypothesis:

> In adults with a structured HCC diagnosis and first recorded TACE-like action, among those with a paired early biomarker trajectory, a prespecified transformed-AFP improvement plus non-deteriorating hepatic proxies is associated with a lower 46–365-day cumulative incidence of a first subsequent liver-directed action, and this association is stronger than its association with a non-liver procedure capture control after adjustment for day-45-known observation opportunity. A pre-index analogue is weaker.

The estimand is an adjusted prognostic association with recorded care, not a causal effect and not a treatment recommendation. The critical adverse result is not simply a null: if the trajectory predicts non-liver capture similarly, or its liver-directed association disappears after process adjustment/weighting, the disease-specific interpretation is falsified while a generic prognosis/care-contact association may remain.

## Population, time, exposure, and outcomes

Use one index per patient. In procedures, identify the earliest row with case-insensitive 'TACE', '动脉化疗栓塞', or both '肝动脉' and '栓塞' in 手术. Collapse qualifying rows for one patient within 24 hours into one index episode, retaining the raw procedure vocabulary and counts. Anchor on 开始时间; the parent audit reports no missing procedure start. Require age >=18 and nonmissing sex from the joined index encounter, a 诊断名称 containing literal 肝细胞癌 joined to an encounter between 180 days before and 7 days after index, index date no later than 2025-01-01, and sufficient local ascertainment through day 365. Unknown follow-up is excluded from the primary denominator and reported, never coded as no event.

The single prediction landmark is day 45 after index. No post-day-45 record enters features. Require the primary paired cohort to have the last parseable AFP in days -30 to -1 and the first in days 7–45. Set z=log1p(AFP), define improvement as z_post <= 0.5*z_pre, and retain continuous change, missingness and inequality flags. For each of albumin, total bilirubin, the coagulation-ratio proxy and platelet count, use the last pre and first early-post value; define non-deterioration as early >= pre for albumin/platelets and early <= pre for bilirubin/coagulation ratio. The joint phenotype is AFP improvement plus non-deterioration in at least two of these four assays. The assay is not called INR, no ALBI/MELD or unit-dependent cutoff is computed, and the source has no unit column.

From days 46–365 classify the first subsequent procedure into mutually exclusive categories:

- repeat TACE-like, using the same frozen TACE rule;
- alternate liver-directed: name contains 切除, 消融, 射频, or 微波, but not TACE-like;
- non-liver capture control: first procedure in neither category.

Report repeat TACE and alternate liver-directed separately, the combined liver-directed category, and the non-liver control as competing first actions. Include literal-name and 90-/180-day sensitivities. No non-event means treatment success.

The pre-index negative-control exposure repeats the trajectory construction in days -120 to -91 and -90 to -46, without calling it a response. A similar association from this analogue is evidence for generic patient prognosis or selection, not post-TACE specificity.

## Exact source bindings and provenance

All sources are read-only. HCC snapshot is [source checksum]. Every source is an ordinary CSV; there are no archive members. Full schema files are in datasets/hcc/.

- encounters, datasets/hcc/table-b743286cb1249287.json, source [internal dataset path], [source checksum]. Join key is (患者主索引, 就诊号). Use 年龄, 性别, 就诊时间, 入院时间, 出院时间, and optionally 就诊科室; use admission time, falling back to visit time, for index anchoring and discharge only for ascertainment.

- procedures, datasets/hcc/table-d5eae16f8f8093d9.json, source [internal dataset path], [source checksum]. Join on the same two keys. Use 手术, 开始时间, 结束时间, 手术来源; use start time for index and outcome dates.

- diagnoses, datasets/hcc/table-12710723c3df0c99.json, source [internal dataset path], [source checksum]. Use 诊断名称 and 诊断类型, join to encounters on the two keys, and assign diagnosis time from the joined encounter. Diagnosis text cannot adjudicate stage or recurrence.

- labs, datasets/hcc/table-38aad8c54471332f.json, source [internal dataset path], [source checksum]. Use 检验, 定性结果, 定量结果, 标本类型, 检验时间; exact assay names are 甲胎蛋白, 白蛋白, 总胆红素, 凝血酶原时间比值, and 血小板计数. Parse numeric values deterministically, preserve inequalities/qualitative flags, and do not pool across assays or units.

- examinations, datasets/hcc/table-fd016d2731b9d6c6.json, source [internal dataset path], [source checksum]. Use 检查, 检查所见, 检查诊断, 开始时间, 机器型号, 检查号, joining on the same keys. Deduplicate exact rows and retain counts. A frozen opportunity screen requires a liver/abdomen term (肝, 腹部, 上腹, 肝动脉, 门静脉, PET/CT) and an imaging term (CT/MRI/磁共振/增强/造影/超声/PET), excluding biopsy/puncture/drainage/catheter/surgery/ablation/intervention terms. This is recording opportunity only; report language is unvalidated.

Optional orders, schema datasets/hcc/table-6b93dcf0ea823702.json, source data_医嘱(非药品)_2062526727266216118.csv, can supply pre-index or day-45-known order-family/capture features using 开立时间, 开始时间, 结束时间; an order is not completion. Medications can supply pre-index history or capture only, never administration or intent. clinical_documents and pathology have no temporal columns and cannot enter dated prediction. vitals, transfers, and front_page are identifier-only and add no clinical payload.

## Models and scientifically substantive method comparison

All primary models use the same paired cohort and split.

B0 is a regularized cause-specific discrete-time hazard model with multinomial competing actions, using age, sex, department/procedure family, pre-index HCC/cirrhosis/portal-vein/liver-lung-bone metastasis/ascites indicators and counts, previous liver-directed procedure counts, pre-window assay levels/missingness, and day-45 observation opportunity.

B1 adds the frozen AFP/hepatic phenotype and continuous changes. B2 adds only day-45-known observation variables: distinct encounter days, lab row/day counts, assay-specific availability and first-observation timing, examination counts/days-to-first/family flags, and explicitly labeled completed-record proxies if available. These nested models answer whether the trajectory adds information beyond severity and capture.

M3 is the substantive alternative: an irregular-time, low-rank state-space model with an AFP-informed latent activity proxy and a hepatic-function proxy, patient random intercepts/slopes, assay-specific observation submodels conditional on prior observations, baseline covariates and latent state, and competing action hazards. It produces posterior day-45 state/slope estimates and uncertainty without future smoothing. This can reveal whether asynchronous shape and informative measurement timing carry information that a single phenotype discards; it cannot reconstruct unmeasured tumor burden or access.

Evaluation is locked by index date: 2010–2022 fit, 2023 tuning, 2024–2025-01-01 test; no patient crosses splits. If date support fails, use fixed patient-hash buckets and record the fallback. Fit all parsers, imputers, penalties, latent settings, observation models and weights without locked-test outcomes. Compare B0/B1/B2/M3 on the same paired patients using cause-specific Brier score, mean log score, calibration intercept/slope, AUROC/PR-AUC only when event support makes them interpretable, and 1-year cumulative-incidence contrasts. Use patient bootstrap or a declared robust interval procedure. For the all-index sensitivity, fit paired-cohort completeness using training data only, inspect stabilized weight overlap, truncate at 1st/99th percentiles, and report failure as inconclusive.

The simple model is retained because incremental information is the scientific test. The latent alternative is retained because it tests whether irregular asynchronous biomarker and observation dynamics, rather than a hand-defined threshold, explain action-specific prediction. A transformer adaptation of the natural-history demonstration is deferred: structured dated history exists, but for one institutional recorded-action endpoint its extra capacity is not necessary to identify the observation-versus-disease question and would make vocabulary/leakage auditing harder. The multimodal cancer demonstration cannot be reproduced because images are absent; its lab-only concept is represented by B1/B2/M3 without claiming reproduction. The Bayesian demonstration motivates M3’s latent longitudinal structure, but no verified genetics are available and no genetic analysis is proposed. No HCC expert seed was supplied; the expert-seed library is retained as untested non-HCC material rather than forced into this island.

## Decision rules and evidence limits

Supportive results require a repeat-TACE/liver-directed contrast in the prespecified direction, a 95% interval excluding the null (operationally, contrast ratio <=0.80 for repeat TACE), direction preserved under literal naming and 90-/180-day windows, <30% attenuation after B2 and weighting, stronger liver-directed than non-liver-control association, weaker pre-index analogue, and M3 mean-log-score improvement >=0.02 without worse calibration. These are research criteria, not treatment thresholds.

Adverse results include reversal/null, >=30% attenuation after observation adjustment, a strong trajectory-by-testing interaction, comparable association with the non-liver capture control, pre-index analogue as strong as the post-index trajectory, competing-action reversal, unstable sensitivities, poor calibration, or an M3 gain disappearing under leakage/observation controls. A strong alternate liver-directed action means a repeat-TACE-only conclusion is incomplete.

Inconclusive results include too few paired patients/events, failed weight overlap, wide intervals, high unknown follow-up, insufficient examination timing, M3 nonconvergence, or absent adjudication. Inconclusive is not confirmation.

Support would establish only a reproducible, observation-adjusted association with a local recorded pathway and motivate prospective biomarker-triggered reassessment. Adverse evidence would warn against treating the trajectory as disease-specific escalation evidence. The data cannot establish recurrence, radiologic response, viable tumor, BCLC stage, treatment intent, mortality, outside-care actions, true decompensation, causal effects, utility, or external validity. These require time-aligned expert imaging/pathology review, mortality/claims linkage, intent data, and prospective or external validation. The verifier can check computation, leakage, uncertainty, output-linked interpretation and these evidence rules, but not clinical truth.

## Completion artifacts and resources

The required deliverable is newly fitted/estimated outputs, not a narrative-only answer: cohort_manifest.csv/parquet, split_manifest.csv, predictions.csv/parquet, metrics.json, bootstrap_intervals.json, procedure_vocabulary_audit.csv, examination_proxy_audit.csv, observation_specificity.csv, negative_control.csv, interpretation.json, and limitations.csv, each carrying snapshot/schema hashes and actual filtering counts. Completion requires model coefficients/latent parameters, cause-specific predictions and cumulative incidences, uncertainty, calibration/log-score comparison, and explicit mapping from every interpretation claim to computed outputs.

The parent audit measured approximately 338,040 procedure rows, 1,810,646 diagnosis rows, 28,159,928 lab rows, 190,022 AFP rows and 419,996 examination rows; a full solver fit is unverified. B0–B2 are expected to fit on CPU with declared memory/time. M3 may use a bounded CPU fit or one allocated A100 through job_submit with cuda:0; GPU availability is verified at the deployment level but runtime and convergence are unmeasured. No proposer/solver weights are trained.
