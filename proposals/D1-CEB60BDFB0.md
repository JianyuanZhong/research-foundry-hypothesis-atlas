# Early post-TACE reserve worsening and concordant recorded hepatic decompensation

## Scientific deliverable and clinical decision

The deliverable is a newly fitted, locked prognostic comparison that estimates whether early post-TACE change in liver-reserve markers adds reproducible information about a subsequent recorded hepatic-decompensation event, while testing whether the finding survives a more specific concordant-record outcome. Completion requires a cohort-flow/ascertainment table; one index row per patient with exposure, HCC history, windows, follow-up and censoring fields; a prespecified outcome dictionary and source-concordance table; fitted baseline and temporal-model artifacts; locked test predictions; calibration intercept/slope, Brier, AUROC, AUPRC, decision-curve net benefit, coefficient/feature summaries and patient-bootstrap intervals; and broad-vocabulary, high-specificity-vocabulary, concordant-outcome, PT/INR and censoring sensitivity outputs. A schema audit alone is not completion.

The decision relevance is narrow: after TACE, should a patient with acceptable pre-procedure reserve but early laboratory worsening receive intensified observation and multidisciplinary reconsideration before another locoregional treatment? This is prognosis among treated patients, not the causal effect of TACE, monitoring, repeat treatment, or a threshold policy.

## Existing evidence and unresolved hypothesis

The local snapshot establishes HCC-coded activity, many recorded TACE procedures, repeated laboratory observations, and ancillary examination/document records. It does not establish a complete TACE registry, expert-adjudicated decompensation, reliable death capture, complete outpatient care, tumor stage/response, or treatment appropriateness. The three demonstrations motivate (but do not prove) structured temporal histories, bounded learned longitudinal representations, and multimodal adaptation; their unavailable UKB/Danish, genetic, image, and full-method dependencies are not claimed as inspected or reproduced.

Strongest supported claim: the snapshot can support an observational estimate of incremental prediction for recorded post-TACE decompensation, if procedure/diagnosis timing and ascertainment are handled as specified. Unresolved claim: among patients with a first recorded high-specificity TACE, does worsening reserve in days 3–14 predict a new recorded decompensation in days 15–90 beyond pre-TACE reserve/history, and is the direction/utility stable when the event additionally requires concordant evidence in an examination or clinical document?

Primary hypothesis: the prespecified worsening direction of albumin, platelets and sodium decline, or bilirubin, INR/PT and creatinine rise, during index+3 through index+14 is associated with higher 15–90-day risk of a new broad recorded-decompensation composite and improves locked-test calibration/decision utility beyond the static baseline.

Specificity hypothesis: the association and incremental utility are not artifacts of diagnosis coding alone; they persist in a secondary high-specificity concordant-record endpoint requiring a qualifying diagnosis and a positive, temporally linked examination or clinical-document corroboration. This is a falsifiable robustness claim, not a claim that the rule is clinical adjudication.

## Population, exposure and time

Use only HCC snapshot [source checksum].

1. Resolve every procedure row in [internal dataset path] to [internal dataset path] by (患者主索引, 就诊号). Parse 开始时间; discard unparseable times and retain exact normalized procedure vocabulary/counts. Primary exposure is case-insensitive TACE or an explicit hepatic-artery chemoembolization combination: a hepatic-artery term (肝动脉 or 经导管肝动脉) plus embolization/chemo terms such as 栓塞 and 化疗. Sensitivity exposure adds observed catheter/arterial embolization variants but flags non-TACE embolizations separately; never infer exposure from medication or narrative alone.

2. Index is the earliest qualifying primary TACE start for each 患者主索引; exclude anyone with an earlier qualifying TACE in the available procedure record. Require an HCC diagnosis on or before index from [internal dataset path], using normalized 肝细胞癌 or prespecified 肝癌 terms while excluding 疑似/待查 and non-HCC mixed-malignancy labels unless clinically reviewed. Diagnosis timing comes only from its linked encounter’s 就诊时间, falling back to valid 入院时间 if prespecified; diagnosis rows themselves have no time. A pathology-linked pre-index corroboration of malignancy may be reported as a sensitivity cohort definition using [internal dataset path], but pathology has no time field and cannot be required for the primary cohort.

3. Use encounter fields 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室 from [internal dataset path] Require valid index encounter/time linkage. Unit is patient, not procedure row.

4. Resolve [internal dataset path] by (患者主索引, 就诊号) and then align by patient ID and parsed 检验时间, because post-index labs can occur in subsequent encounters. Baseline window is [index−14 days,index]; post window is [index+3,index+14]. For each assay and landmark use nearest valid observation with deterministic timestamp/source-row tie-break and save delays. Core exact normalized assays are albumin 白蛋白, total bilirubin 总胆红素, INR 国际标准化比值 or PT 凝血酶原时间, platelets 血小板, creatinine 肌酐, sodium 钠. Do not pool ambiguous assays or units; numeric parsing and impossible-sentinel rejection are mandatory. INR is primary, PT replacement sensitivity. Primary complete-case analysis requires all six components in both windows; report component-specific and missingness-indicator cohorts.

5. Follow-up starts strictly after index+14. A broad primary event is the first new qualifying diagnosis from index+15 through index+90: 腹水, 肝性脑病, 肝衰竭/急性肝衰竭/慢性肝衰竭, or 上消化道出血/消化道出血. Link timing through encounters; exclude any same component present at patient level on or before index+14. An inpatient encounter indicator is secondary utilization, never the decompensation endpoint. Require an encounter at or beyond index+90 for ascertainment-complete binary negatives; otherwise exclude from the primary complete-window analysis and include in right-censored time-to-recorded-event sensitivity.

## Concordant-record specificity endpoint

For each broad positive diagnosis encounter, define a source-specific corroboration flag using only outcome-window records linked to the same (患者主索引, 就诊号):

- ascites: examination 检查所见/检查诊断 or clinical-document fields contain a prespecified positive term such as 腹水/腹腔积液;
- encephalopathy: corresponding fields contain 肝性脑病;
- liver failure: contain 肝衰竭;
- gastrointestinal bleeding: contain 消化道出血, with any prespecified positive clinical terms recorded separately.

Normalize HTML/whitespace, preserve raw source-row counts, and apply a fixed negation/history/uncertainty rule before counting a positive. Do not use the outcome diagnosis itself as corroboration. Examination timing uses 开始时间. Documents lack their own event time, so only linked encounter time is allowed. Pathology has no timestamp and is used only as a HCC-cohort sensitivity source, not as acute decompensation corroboration. Report each component and the overall concordant composite separately, plus three strictness levels (diagnosis alone; diagnosis plus same-encounter ancillary positive; diagnosis plus two-source ancillary positives if counts permit). If the concordant endpoint is sparse, lexically unstable, or differentially documented, it remains a feasibility/sensitivity result and cannot replace the broad primary outcome.

The HCC metadata states that the local lexical detector is unvalidated and supports only limited cirrhosis axes, not comprehensive diagnosis extraction. Therefore this endpoint is an algorithmic source-concordance proxy requiring blinded chart review before clinical interpretation. No result can establish true decompensation, grade, or biological mechanism.

## Baseline, alternative, estimand and analysis

Static baseline: regularized logistic regression for each locked outcome using age, sex, index department, pre-index HCC/decompensation history, baseline lab values, assay availability/recency, and no post-index or future outcome-encoding variable.

Temporal alternative: patient-level gradient-boosted trees over ordered six-assay observations from index−14 through index+14, retaining assay identity, value, time-from-index, baseline/post indicator, measurement count, missingness, and direction-oriented deltas. Do not include outcome-window examination, documents, diagnoses, pathology or medications as features. Fit/tune on patient-level 70/15/15 train/validation/test partitions stratified by outcome; add a later-index temporal holdout if event counts permit. Calibrate only on validation and lock the test. At most 500 trees and 10 tuning configurations. Up to 4 CPUs and 16 GB RAM; stream the 2.2 GB lab file; target 20–45 minutes extraction/fitting. No GPU is scientifically needed.

The primary estimand is the incremental prognostic value of early reserve trajectory conditional on pre-index reserve/history, quantified by optimism-corrected test Brier/calibration improvement and decision-curve net benefit, with association estimates per training-set IQR and worsening quartiles. AUROC/AUPRC are secondary discrimination summaries. Use patient-level bootstrap intervals for all metrics, associations and calibration. Compare against static baseline on identical patients, outcome and split. The temporal model is retained because it can reveal nonlinear thresholds, interactions and timing/shape information that a single delta loses; it is not selected for complexity.

Sensitivity analyses: 30- versus 90-day horizons; broad versus high-specificity TACE vocabularies; index-encounter labs excluded from post window; PT replacing INR; 0–30 versus 15–90 outcomes; broad versus concordant outcome; component endpoints; complete-case versus missingness indicators; pathology-supported HCC cohort; and censored time-to-recorded-event analysis. Preserve split seed, source/schema hashes, exact vocabulary, row counts, filters and exclusions.

## Falsification and interpretation

Supportive: worsening has the prespecified direction; its interval excludes no association in the locked primary test; and trajectory improves test calibration/Brier or net benefit over baseline, with broadly stable direction under high-specificity exposure and concordant-outcome sensitivity. This supports incremental prediction of recorded or concordant-record outcomes in this snapshot.

Adverse: reverse association; no incremental locked-test calibration/utility; or collapse after high-specificity TACE, timing, ascertainment and source-concordance controls. This refutes the local incremental claim and argues against using these changes as a monitoring trigger without another study. It does not prove reserve biology is irrelevant.

Inconclusive: inadequate complete cases/events; wide intervals; missing follow-up; assay ambiguity; strong dependence on lexical vocabulary, documentation density, or diagnosis coding; failure of the concordant endpoint to achieve stable ascertainment; or no valid negatives. This means the snapshot cannot resolve the claim.

Automatic verification can check source paths, columns, joins, one-row-per-patient indexing, timestamps, vocabulary, incident-label logic, ancillary-source timing, leakage-free features, censoring, splits, metrics, intervals and conclusion-to-output consistency. It cannot establish clinical diagnosis validity, chart adjudication, death capture, complete outpatient history, tumor stage/response, causal effects, treatment appropriateness, or benefit from altered monitoring. Those require blinded clinician review, richer longitudinal capture, or an external/target-trial study.

## Exact bindings and unavailable evidence

Primary files are:
- encounters: [internal dataset path]
- procedures: [internal dataset path]
- diagnoses: [internal dataset path]
- labs: [internal dataset path]
- examinations: [internal dataset path]
- clinical documents: [internal dataset path]
- pathology sensitivity: [internal dataset path]

All are ordinary read-only CSVs, with no archive member. Orders (data_医嘱(非药品)_2062526727266216118.csv) and medications (data_用药_5693407050835159466.csv) remain available for audit but are excluded from the primary model because indication/adherence and exact clinical timing semantics are not validated. Vitals, transfers and front_page contain only identifiers. No images, waveforms, validated death endpoint, decompensation grade, tumor stage/response, transplant outcome, complete outpatient history, reliable hospital identifier, or external validation cohort is available.

The seed audit, demonstration dispositions, exact streaming counts, method comparison, resource budget and deferred alternatives are recorded in work/episode-4-hcc-ancillary-audit.md. The central advance over the prior parent is not a more complex predictor: it tests whether the reserve signal survives a prespecified ancillary-source concordance check, separating a potentially clinically meaningful prognostic pattern from a diagnosis-coding artifact while honestly preserving the broad recorded-outcome result.
