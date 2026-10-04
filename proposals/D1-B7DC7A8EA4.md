# Early post-TACE reserve decline as hidden vulnerability in apparently compensated HCC

## Scientific deliverable and clinical decision

The new scientific deliverable is a prespecified estimate of effect modification: among patients with HCC and a first recorded high-specificity TACE who have no previously recorded hepatic decompensation, does early post-TACE liver-reserve worsening predict a new recorded decompensation event during the subsequent 15–90 days, and is the marginal risk increment larger when baseline reserve appears preserved? The study is prognostic and observational. It does not estimate the causal effect of TACE, monitoring, or repeat treatment.

Completion requires: a flow/eligibility and ascertainment table; one row per patient-index; exact normalized procedure and outcome vocabularies; assay mapping and missingness tables; baseline and trajectory scores; fitted interaction estimates with patient-bootstrap 95% intervals; locked test predictions from the static baseline and temporal learned models; calibration intercept/slope, Brier score, AUROC, AUPRC and decision-curve tables; stratum-specific risk contrasts; and all prespecified sensitivity/falsification outputs. A schema audit or a fitted model without the interaction estimate is not completion.

The decision relevance is narrow: a patient can look compensated before TACE yet deteriorate shortly after it. If the decline signal is reproducible in this apparently preserved group, it would justify prospective evaluation of intensified observation and reconsideration of subsequent locoregional treatment. It would not establish a treatment threshold or that acting on the signal improves outcomes.

## Hypothesis and evidence boundary

Primary hypothesis: in the recorded-compensated cohort, greater worsening in the six-marker reserve trajectory from index to days 3–14 is associated with a larger increase in the probability of a new recorded hepatic-decompensation diagnosis during days 15–90 among patients with a higher baseline reserve score than among patients with a lower baseline reserve score. The interaction is prespecified as a positive marginal-risk interaction on the absolute-risk scale; a two-sided interval is reported. The biological rationale is that a new deterioration signal may reveal vulnerability that a relatively preserved pre-TACE record does not show, whereas patients already showing poor reserve may have less incremental information to gain.

The strongest claim supported before this experiment is only that the local snapshot contains repeated laboratory, encounter, diagnosis and procedure records that can support an observed-care prognostic analysis. It does not establish that TACE labels are a complete treatment registry, that decompensation labels are adjudicated, or that death and outpatient care are completely captured. The unresolved claim is incremental and heterogeneous prognostic information for recorded outcomes under leakage-safe timing. No causal, biological, deployment, treatment-benefit, tumor-response, survival, or clinical-threshold claim is allowed.

## Population, index and time

Use only HCC snapshot `[source checksum]`.

1. Resolve every procedure row to an encounter using (患者主索引, 就诊号), parse 手术开始时间, and discard unparseable times. The primary procedure vocabulary is 手术 equal to TACE case-insensitively, or an explicit hepatic-artery chemoembolization combination containing 肝动脉 or 经导管肝动脉 together with 栓塞 and 化疗. It includes the observed exact labels 肝动脉化疗栓塞, 经动脉造影化疗栓塞术（TACE）, and parenthesized catheter variants. Save normalized labels and counts. A sensitivity vocabulary adds 肝动脉栓塞术, 经导管肝动脉栓塞术 and equivalent labels, while flagging non-TACE embolization. Never infer TACE from medications or narrative text alone.

2. The index is the earliest qualifying primary TACE start per 患者主索引; exclude anyone with an earlier qualifying primary TACE in the procedure table. Require an HCC diagnosis on or before index: normalized 诊断名称 containing 肝细胞癌 or the prespecified 肝癌 term, excluding 疑似/待查 and mixed malignancy labels unless clinically reviewed. Link the diagnosis to encounters to obtain its time because diagnoses have no timestamp.

3. Define the recorded-compensated cohort as patients with no qualifying pre-index or index-time diagnosis of 腹水, 肝性脑病, 肝衰竭/急性肝衰竭/慢性肝衰竭, or 上消化道出血/消化道出血, after exact normalized matching and exclusion of uncertain labels. This is a record-based proxy, not clinical adjudication. Require a valid index encounter relationship and the complete baseline/early trajectory data for the primary complete-case interaction analysis. Report a prespecified broader cohort retaining baseline decompensation as a sensitivity/transportability analysis rather than silently mixing it with the primary estimand.

4. Baseline is [index−14 days, index]. Early trajectory is [index+3 days, index+14 days], so no post-procedure outcome-period information enters exposure construction. Use the nearest valid observation to each landmark per assay, tie-breaking deterministically by timestamp then source row order, and retain delays, counts and assay availability. A patient-level join is required because post-index labs may be on a later encounter.

5. Follow-up starts strictly after index+14. The primary outcome window is index+15 through index+90. A diagnosis event time is the linked encounter 就诊时间, falling back to 入院时间 only under a prespecified valid-time rule. Exclude labels present on or before index+14 at the patient level. Primary complete-window negatives require an encounter at or beyond index+90; otherwise exclude from the binary primary analysis and retain them in a censored time-to-recorded-event sensitivity analysis. This estimates recorded care, not disease-free survival.

## Variables and exact source bindings

Primary source files are ordinary read-only CSVs, no archive member:

- Encounters: `[internal dataset path]`, table `encounters` (`table-b743286cb1249287.json`). Use 患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室. Do not interpret 就诊科室 as hospital.
- Procedures: `[internal dataset path]`, table `procedures` (`table-d5eae16f8f8093d9.json`). Use 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源.
- Diagnoses: `[internal dataset path]`, table `diagnoses` (`table-12710723c3df0c99.json`). Use 患者主索引, 就诊号, 诊断名称, 诊断类型; timing comes only from linked encounters.
- Labs: `[internal dataset path]`, table `labs` (`table-38aad8c54471332f.json`). Use 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间.

The payload join key is (患者主索引, 就诊号). Lab alignment and diagnosis event timing additionally use patient ID and parsed time. Vitals, transfers and front_page are identifier-only and excluded as payload. Examinations (`table-fd016d2731b9d6c6.json`), clinical_documents (`table-66afca58512c2fca.json`), pathology (`table-0a4ee86a446c605c.json`), orders and medications are optional audits/sensitivities only.

Core laboratory assays are exact normalized names, not substring pools: 白蛋白; 总胆红素; 国际标准化比值 as primary coagulation measure, with 凝血酶原时间 as a replacement sensitivity; 血小板计数 or exact primary 血小板 label under an assay dictionary; 肌酐; and 钠. Acute-labelled variants such as 白蛋白（急）, 总胆红素（急）, 肌酐（急） and 钠（急） must be separately mapped only when the assay dictionary confirms equivalence. Reject ambiguous mappings, nonnumeric values and impossible sentinels. Preserve local assay units and do not pool across assays.

Create two direction-oriented, training-derived standardized scores from the six exact assays:

- Baseline reserve score: within each training split, standardize each baseline assay and orient albumin, platelets and sodium positively and bilirubin, INR and creatinine negatively; average available components only under a prespecified minimum-component rule. Higher means apparently better recorded baseline reserve.
- Early-worsening score: standardized early-minus-baseline changes with albumin, platelets and sodium decreases and bilirubin, INR and creatinine increases oriented positively; include assay delays and measurement counts as separate process variables, never as substitutes for missing values.

The primary interaction model uses early-worsening score, baseline reserve score, their product, age, sex, index department, prior HCC history, baseline component values, and baseline availability/recency. Estimate the interaction both on the log-odds scale and as model-based absolute-risk contrasts at prespecified baseline-reserve quartiles learned from training data. Quartile strata are descriptive; the continuous interaction is primary. Do not dichotomize a clinical “compensation” threshold from the test set.

## Outcomes and evidence limits

Primary outcome is the first new qualifying diagnosis in the index+15 to index+90 window among 腹水, 肝性脑病, 肝衰竭/急性肝衰竭/慢性肝衰竭, or 上消化道出血/消化道出血. Report each component separately. A secondary new inpatient encounter is utilization, not decompensation. Do not use death-diagnosis rows as a death endpoint.

As an ancillary robustness audit only, if counts permit, require a qualifying diagnosis plus same-encounter examination text in examinations (检查所见 or 检查诊断) containing the same decompensation concept, or a prespecified clinical_documents concordance flag. This is an unvalidated lexical proxy, not adjudication, and clinical_documents has no native timestamp; it must not replace the primary outcome. Pathology has no time and can only be a cohort-level sensitivity. The prior concordance child is deferred as a primary endpoint because its density and independent stability were not evidenced.

Unavailable evidence includes validated decompensation adjudication, decompensation grade, complete death/transplant capture, transplant-free survival, tumor stage, radiographic response, recurrence, treatment dose/intent, reliable hospital identity, and complete outpatient history. Expert chart review and external validation are needed before clinical deployment.

## Baseline, learned alternative and analysis

The simple baseline is regularized logistic regression for the primary complete-window binary outcome using only pre-index information: age, sex, department, prior HCC/decompensation history, baseline six-marker values, availability/recency and the continuous baseline reserve score. It does not use early labs, procedure-label text as an outcome proxy, or any future encounter.

The primary scientific model adds the early-worsening score and its prespecified interaction with baseline reserve. Compare it with the static baseline using patient-level locked-test Brier score, calibration intercept/slope, AUROC, AUPRC, decision-curve net benefit and risk contrasts, with patient-bootstrap 95% intervals. The estimand is the interaction and its absolute-risk interpretation, not a small AUROC gain.

The substantive learned alternative is patient-level temporal gradient-boosted trees over ordered observations in index−14 through index+14 for the six assays, retaining assay identity, value, time-from-index, baseline/early indicator, measurement count and missingness, plus age, sex, prior history and index context. Train/validation/test are patient-level 70/15/15 partitions stratified by outcome; use a later-index holdout if event counts permit. Fit and tune only on training/validation, calibrate on validation, and lock the test set. Permit at most 500 trees and 10 configurations. Summarize permutation/SHAP-style feature groups only as exploratory explanations; the interaction estimate comes from the prespecified regression model.

The learned alternative can reveal nonlinear thresholds, timing asymmetry and trajectories with the same endpoint that the composite score loses. It is deferred if the recorded event count, complete-case size or temporal density is inadequate, or if it improves prediction only through measurement-process shortcuts. A latent mixed-effects/GP trajectory model is also deferred because it adds missing-data and local-optimum assumptions without being necessary to test the interaction. A transformer/generative model is deferred because this question needs an interpretable heterogeneity estimate and no evidence yet shows that sequence capacity is necessary. This is a scientific deferral, not a blanket neural-network or GPU ban.

Use up to 4 CPUs and 16 GB RAM, stream the 2.2 GB laboratory file, and target 20–45 minutes extraction/fitting within the 7,200-second science limit. No GPU is needed. Preserve source/schema hashes, exact filters, row counts, split seed, software versions, cohort exclusions, model artifacts and derived results in the workspace; source files remain read-only.

## Sensitivity analyses and falsification

Prespecify: broad versus high-specificity TACE vocabulary; all-HCC versus recorded-compensated cohort; INR versus PT; primary exact assay mappings versus validated acute-labelled equivalents; complete-case versus missingness-indicator models; 30-day and 90-day horizons; 0–30 versus 15–90 outcome windows; exclusion of index-encounter labs from the early window; censored time-to-recorded-event analysis; each decompensation component; encounter-density adjustment; and the ancillary diagnosis-plus-examination/document concordance audit if sufficiently populated. The primary interaction and locked evaluation must not be reselected after seeing results.

Supportive results are a directionally positive early-worsening association, a bootstrap interval for the prespecified interaction excluding no interaction or a clinically negligible prespecified margin, and reproducible absolute-risk separation in the apparently preserved baseline stratum, with trajectory improvement in locked-test calibration/Brier or decision-curve net benefit over the static baseline. This supports incremental prediction of recorded decompensation in an observed-care cohort, not biological compensation failure or benefit from monitoring.

Adverse results are a null/reverse interaction, no incremental locked-test calibration/utility, or collapse after high-specificity TACE, patient-level splitting, outcome timing and ascertainment controls. This refutes the local hidden-vulnerability/incremental prediction claim and argues against using this signal as a monitoring trigger without another study; it does not show that post-TACE reserve biology is irrelevant.

Inconclusive results are too few complete compensated cases/events, wide intervals, missingness or follow-up imbalance, assay ambiguity, strong dependence on vocabulary or measurement density, failure to obtain ascertainment-complete negatives, or instability between continuous and descriptive-stratum estimates. This means the snapshot cannot resolve the claim.

Automatic verification can check source hashes, joins, one-row-per-patient indexing, TACE vocabulary, exact assay mappings, pre/post temporal exclusion, no-baseline-decompensation logic, outcome timing, censoring, patient splits, fitted artifacts, metric/interval computation and that conclusions match outputs. It cannot adjudicate clinical diagnoses, recover unrecorded deaths/outpatient events, establish causality, validate lexical concordance, establish tumor response, or prove clinical utility. Those require clinical review, missing modalities, external validation or a prospective intervention study.

## Demonstration and seed dispositions

The natural-history Delphi demonstration supports the idea of a bounded structured temporal-history adaptation, but its UK Biobank cohort and Danish external validation are unavailable; this proposal adapts the comparison to HCC labs and recorded outcomes. The cancer Oncoformer demonstration supports a lab-only longitudinal adaptation because the local HCC snapshot has no images and the main article/complete STAR Methods remain unavailable; no multimodal reproduction is claimed. ALADYNOULLI is not reproduced: genetics are unavailable and its latent assumptions are unnecessary for the present interpretable interaction question. The 30 imported expert seeds are UK Biobank, MIMIC-IV or eICU candidates, not HCC rows; no cross-dataset participant key exists, so none is used as a parent. Their native-dataset assessments and provenance remain preserved on the board.

## Alternatives not selected and revisit criteria

The static regularized baseline is retained because it estimates the same risk target and makes the baseline-reserve adjustment transparent. Temporal boosting is retained because it can test whether timing and nonlinear shape add information beyond the score. The prior diagnosis-plus-ancillary-record concordance endpoint is retained only as a conditional audit, not as the primary endpoint, unless its event density and stability are demonstrated. The latent mixed-effects/GP and transformer alternatives are deferred because they do not improve the core scientific estimand until event validity, measurement density and the interaction’s reproducibility are established. Revisit them only if a later audit shows adequate repeated trajectories and a scientific need to estimate patient-specific slopes or richer sequence states; revisit the concordance endpoint only with documented counts and independent chart review.
