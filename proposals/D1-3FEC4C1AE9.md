# Pathway-specific early laboratory trajectories and competing liver-directed transitions in HCC

## Scientific deliverable and falsifiable hypothesis

The deliverable is a newly fitted, locked competing-risk prognostic analysis in the local HCC snapshot. It must produce: a frozen cohort and exact procedure-family dictionaries; cohort, join, duplicate, invalid-time and endpoint audits; patient-level split assignments; a transparent baseline and early-summary comparator; a prespecified irregular latent-state alternative; cause-specific and cumulative-incidence estimates with uncertainty; locked test predictions and calibration; and a claim-to-output table.

The hypothesis is:

> Among adults with a first observed HCC-coded inpatient admission and no recorded liver-directed procedure during hours 0–48, the joint early trajectory of exact laboratory channels through hour 48 is differentially associated with the first subsequent recorded liver-directed pathway during hours 48–120—interventional embolization/TACE-family versus resection/ablation-family—beyond admission/pre-admission information and transparent first/last laboratory summaries.

The clinical importance is pathway selection and timing: an early signal that separates patients who subsequently enter an interventional pathway from those entering a resection/ablation pathway could motivate prospective multidisciplinary review and test whether physiologic change is useful for prioritizing diagnostic or treatment planning. The substantive advance over the incumbent is that “any liver-directed procedure” is decomposed into clinically interpretable first-event pathways, with the other pathway treated as a competing event. The endpoint remains a local recorded-care transition, not treatment need, urgency, progression, response, benefit, or a causal effect.

The strongest supported claim before the study is only feasibility: the snapshot contains dated encounters, HCC-coded diagnosis proxies, dated laboratory records and a procedure file with abundant exact strings for embolization/TACE and resection/ablation. Existing evidence and demonstrations motivate dated sequence/latent-state modelling but do not establish this HCC hypothesis. The unresolved claim is the prespecified differential association and whether an irregular coupled trajectory adds information beyond transparent summaries. The experiment is falsified by no differential association, no incremental held-out information, instability, or equivalent signal in a non-therapeutic negative-control endpoint.

## Population, landmark, outcomes and estimand

Use only configured participant buckets 0–79: fitting 0–59, selection 60–69, locked internal test 70–79. Do not claim access to or validate on buckets 80–99 or externally.

Read encounters and diagnoses, normalize only whitespace/encoding, and freeze the HCC lexical rule before modelling. An eligible encounter has age `年龄 >= 18`, parseable native `入院时间` and `出院时间`, `出院时间 >= 入院时间`, admission on/after 2011-01-01, discharge before 2026-01-01, and a diagnosis joined on the exact identity pair whose `诊断名称` matches the frozen rule (initial provisional audit used `肝细胞癌` or `肝癌`). Select the earliest eligible HCC-coded encounter per `患者主索引`, sorting by native admission time then `就诊号`. Report earlier HCC-coded rows, invalid/ongoing discharges, diagnosis multiplicity/types, duplicate keys and overlaps; this is a first observed HCC-coded admission, not a validated incident diagnosis.

The index cohort excludes any member of the frozen liver-directed dictionary with valid procedure `开始时间` in `0 <= start - 入院时间 < 48` hours. Missing/invalid procedure time is not evidence of absence and is reported separately. The prediction landmark is admission plus 48 hours.

Define a mutually exclusive first-event outcome over `48 <= procedure start - 入院时间 < 120` hours, requiring exact linkage on (`患者主索引`, `就诊号`) and valid native `开始时间`:

* cause 1: first interventional embolization/TACE-family procedure;
* cause 2: first resection/ablation-family procedure;
* cause 0: neither pathway in the window.

The primary estimands are cause-specific hazard/odds associations and 120-hour cumulative incidence for each cause, with the other cause censored only for cause-specific modelling and retained as a competing event for cumulative incidence. The first valid timestamp wins. If a same-time row contains both families, apply a frozen hierarchy (combined therapeutic record is cause “mixed/indeterminate”) and report it; do not arbitrarily assign a pathway. If mixed events exceed a prespecified 5% of first events or the dictionaries cannot be clinically coherent, the pathway-specific primary analysis is inconclusive and the original all-procedure endpoint may be reported only as a secondary descriptive sensitivity. A 48–168-hour window is secondary, as is a descriptive composite.

No procedure after discharge is eligible. Retain procedure end time and source only for data-quality audits. Do not interpret procedure timing as indication, rescue, scheduling, or necessity.

## Exact data bindings

All sources are ordinary files in HCC snapshot `[source checksum]`.

* **encounters**, schema `datasets/hcc/table-b743286cb1249287.json`, source `[internal dataset path]`. Required columns: `患者主索引`, `就诊号`, `年龄`, `性别`, `就诊时间`, `入院时间`, `出院时间`, `就诊科室`. The first two are the join key; admission/discharge define the cohort, landmark and censoring.
* **diagnoses**, schema `datasets/hcc/table-12710723c3df0c99.json`, source `[internal dataset path]`. Required `患者主索引`, `就诊号`, `诊断名称`, `诊断类型`; no diagnosis timestamp exists.
* **labs**, schema `datasets/hcc/table-38aad8c54471332f.json`, source `[internal dataset path]`. Required `患者主索引`, `就诊号`, `检验`, `定性结果`, `定量结果`, `标本类型`, `检验时间`. Parse numeric `定量结果` only; preserve qualitative result and specimen type; use native `检验时间`. Candidate exact assay channels are albumin `白蛋白`, total bilirubin `总胆红素`, creatinine `肌酐`, platelets `血小板`, and a coagulation/prothrombin assay only if an audit establishes stable exact semantics. There is no unit/reference-range column, so channels are never pooled and external cutoffs are prohibited.
* **procedures**, schema `datasets/hcc/table-d5eae16f8f8093d9.json`, source `[internal dataset path]`. Required `患者主索引`, `就诊号`, `手术`, `开始时间`, `结束时间`, `手术来源`. Freeze exact included strings and family assignment before outcome modelling; report all included strings, excluded near-matches, counts, multiplicity, same-time duplicates and mixed-family records.
* **clinical_documents**, schema `datasets/hcc/table-66afca58512c2fca.json`, source `[internal dataset path]`, is joinable on the same key but has no native time and duplicate admission-diagnosis columns. It is excluded from primary time-respecting prediction; the local lexical detector is not validated.
* **pathology**, schema `datasets/hcc/table-0a4ee86a446c605c.json`, source `[internal dataset path]`, has narrative payload but no native pathology timestamp. It is not a temporally valid confirmation endpoint.
* **examinations**, schema `datasets/hcc/table-fd016d2731b9d6c6.json`, source `[internal dataset path]`, has native `开始时间` but narrative findings are not validated stage/response labels and are excluded from the primary model.
* **medications**, schema `datasets/hcc/table-4f6ecaeb6e8f69c2.json`, source `[internal dataset path]`, has native start/end times and dose units but no validated indication; exclude from the primary predictor set.
* **orders**, schema `datasets/hcc/table-6b93dcf0ea823702.json`, source `[internal dataset path]`, has native times but no validated intent; exclude from primary prediction.
* **vitals**, schema `datasets/hcc/table-8436de9cba74b8ca.json`, and **transfers**, schema `datasets/hcc/table-320c20f732e71789.json`, are identifier-only payloads and add no physiologic/movement measurements. **front_page**, schema `datasets/hcc/table-38b3224239acc33f.json`, is also identifier-only.

Pre-admission features use only labs in [admission minus 90 days, admission) and prior encounter/procedure counts in that interval. Early labs use only native `检验时间` in [admission, admission plus 48 hours], including the exact landmark and excluding invalid times. No primary predictor may use post-landmark procedures, orders, medications, examinations, documents, pathology, discharge, or length of stay. Keep raw same-timestamp duplicates for audit, then use a frozen within-assay/time aggregation rule.

## Baseline and substantive alternative

B0 is a training-only standardized elastic-net logistic/cause-specific model with age, sex, admitting department family, calendar era, admission time-of-day, diagnosis-type indicators, pre-admission HCC/liver-disease proxies, prior counts, and per-exact-assay pre-admission nearest value, recency, count, missingness and slope. B1 adds first, last, difference, elapsed time, observation count, missingness and distinct timestamp count for each early exact assay. Both use the same cohort, competing-risk targets, buckets and outcome handling.

The selected substantive alternative is a low-dimensional continuous-time joint latent transition model. A hepatic-reserve state and renal-stress state evolve over 0–48 hours with assay-specific offsets/noise, patient random intercepts/slopes, shrinkage, irregular elapsed time, qualitative/missingness indicators and measurement density. A regularized cause-specific head predicts cause 1 versus cause 2 versus no event from state levels at 48h, recent slopes, coupled-state contrast and posterior uncertainty, retaining B0 covariates. Fit only on 0–59, select state/process/outcome regularization on 60–69, lock on 70–79. This alternative can reveal whether irregular timing, coupling and uncertainty distinguish changing from stable reserve when first/last summaries lose that information; it can also reveal that apparent physiology is only a measurement-intensity artifact.

A one-layer GRU/temporal-attention model over identical lab tokens is deferred because the central uncertainty is pathway-specific physiologic structure, not unrestricted predictive gain; revisit only if the latent model converges and locked residuals show reproducible nonlinear timing interactions. GPU is not required for the selected low-dimensional model.

## Evaluation, falsification and interpretation

Report cause-specific AUROC/PR-AUC, Brier score, calibration slope/intercept and time-specific cumulative-incidence calibration, with patient-level bootstrap or repeated split uncertainty. Compare B1 to B0 and latent model to B1 using paired bootstrap intervals, not a small performance threshold alone. Report pathway-specific coefficient/state contrasts and uncertainty, event counts, cause balance, missingness and measurement density.

Prespecified checks include department and calendar-era strata; exact-assay availability; observation-density adjustment; procedure-source and same-time duplicate sensitivity; 48–168h sensitivity; timestamp permutation of early labs within patient; shuffled patient labels; a negative-control endpoint based on a non-liver routine procedure/workflow string with the same window; and analyses restricted to admissions with no early order/procedure evidence when a valid order dictionary can be frozen. A claim of physiologic pathway signal is adverse if it disappears after density adjustment, is reproduced by timestamp permutation or the negative control, is driven by a single assay/department/era, or depends on procedure-name artifacts.

Support requires: a coherent dictionary with low mixed-event fraction; adequate events (target at least 100 for each primary cause after exclusions); a prespecified directionally coherent pathway contrast with uncertainty excluding a clinically negligible association as defined in the protocol; calibrated held-out improvement of B1 over B0 and/or latent model over B1; and survival of key falsification and strata checks. This supports a reproducible local prognostic association and prospective validation, not a procedure recommendation.

Adverse evidence is a null/opposite association, no incremental information, poor calibration, instability, or falsification-positive signal. Inconclusive evidence is inadequate cause counts, incoherent/mixed dictionaries, dominant invalid/missing procedure times, insufficient dated assay support, nonconvergence, severe overlap/duplicate ambiguity, or intervals too wide to distinguish relevant association from no association. An inconclusive result is a data limitation, not confirmation or refutation.

## Evidence limits and required next study

The available computation cannot establish validated HCC diagnosis, imaging stage, tumor burden, resectability, progression, treatment response, liver failure, AKI, mortality, transplant eligibility, procedure indication/urgency/benefit, clinician intent, scheduling, outside-hospital events, causality or clinical utility. Pathology and examination records cannot supply those claims because pathology lacks native timing and imaging labels are not adjudicated. Stronger conclusions require expert diagnosis/procedure adjudication, timestamped pathology and imaging review, units/reference ranges, intent/scheduling data, complete capture and external validation, followed by prospective operational or causal evaluation.

## Compute and records

Discovery measurements in the parent branch scanned the HCC encounter/diagnosis, procedure and transition cohorts with 4 CPUs/16 GiB in roughly 10 seconds per scan; these do not estimate full lab feature construction or fitting. The future solver envelope in `inputs.json` is 16 CPUs, 256 GiB RAM, up to 8 allocated A100 GPUs and 28,800 seconds. CPU is appropriate for the sparse baselines, exact-assay aggregation, competing-risk estimates and low-dimensional latent fit; full duration and repeated-fit memory remain unverified. If a deferred neural sensitivity is later justified, it must request an allocated GPU and use `cuda:0` inside the allocation.

Completion means the solver newly fits B0, B1 and the latent competing-risk model, freezes all dictionaries/cohort/splits, emits locked predictions and uncertainty, completes falsification/sensitivity outputs, and maps every conclusion to a computed artifact. Readiness or packaging checks alone cannot establish the hypothesis.
