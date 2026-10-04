# Observation-gated emulation of earlier versus later postoperative adjuvant TACE after HCC resection with microvascular invasion

## Decision question and substantive advance

For adults with resected hepatocellular carcinoma (HCC) and pathology evidence of microvascular invasion (MVI) who actually receive postoperative adjuvant transarterial chemoembolization (TACE) within 84 days, does initiating the first TACE on postoperative days 1–42 rather than days 43–84 lower adjudicated intrahepatic recurrence by postoperative day 365?

This child preserves the clinically consequential, active-comparator timing question from `[prior hypothesis]`, but repairs its most consequential weakness: the proposed primary composite mixed recurrence-coded diagnoses with subsequent liver-directed procedures. Full-source feasibility shows that repeat procedures are common and may be planned serial TACE, while recurrence-specific diagnoses and liver imaging are sparse. The parent could therefore estimate institutional treatment and surveillance processes rather than recurrence.

The repair is substantive, not a sensitivity analysis:

1. Subsequent TACE, ablation, or resection is removed from the primary recurrence endpoint.
2. A qualifying liver-imaging report and blinded clinical adjudication are mandatory for primary outcome ascertainment.
3. Imaging observation is a separate process outcome and explicit feasibility gate, not evidence of being recurrence-free.
4. Patients without qualifying follow-up imaging are not automatically classified as recurrence-free. The timing effect is declared non-estimable from this source if observation and event gates fail.
5. Treatment and MVI dictionaries must pass blinded validation gates before effect estimation.

This is an adjudication- and observability-gated target-trial feasibility study with a conditional comparative-effect analysis. Its clinically useful result may be negative: demonstrating that this institutional EHR cannot identify the timing effect without misleading outcome substitution would prevent an unsupported treatment recommendation and define the registry fields needed for a definitive study.

## Evidence-supported claim, unresolved claim, and data required

### Strongest claim currently supported

The available source files can identify dated resection and explicit chemotherapy-embolization procedure records, pathology text containing HCC/MVI terms, encounters, and some dated imaging reports. Full scans (no sampling) found 25,465 patients with a first observed resection; among an unvalidated lexical adult HCC/MVI cohort without recorded liver-directed treatment in the preceding 180 days, 388 had first strict TACE on days 1–42 and 143 on days 43–84. Timing is strongly concentrated around the proposed boundary (median day 37; 75th percentile day 43).

The same scan shows why the parent endpoint is not presently valid. Under a pragmatic day-84 observability filter and exclusion of pre-landmark recurrence signals, only 78 earlier and 28 later recipients remained. Only 24/78 and 11/28 had a qualifying liver-imaging record on days 85–365. Strict recurrence language appeared in examination reports for 12/78 and 6/28, whereas recurrence-specific diagnoses appeared for only 2/78 and 0/28. Repeat liver-directed procedures occurred in 50/78 and 19/28 within 180 days after first TACE. These are aggregate feasibility findings, not comparative clinical outcomes, because the phenotype, imaging endpoint, treatment indication, confounding control, and recurrence adjudication have not been validated.

A separate full-file laboratory feasibility analysis found paired same-assay bilirubin and INR around TACE in only 23 earlier and 11 later recipients. An exploratory biochemical-injury endpoint is therefore not a superior substitute, and the exploratory albumin dictionary was contaminated by prealbumin/electrophoresis labels.

### Unresolved hypothesis to test

Among otherwise eligible day-84 survivors who received first postoperative adjuvant TACE by day 84, earlier initiation (days 1–42) reduces the day-84-to-day-365 cumulative incidence of clinically adjudicated intrahepatic HCC recurrence compared with later initiation (days 43–84).

The null is no difference in day-365 recurrence risk. A clinically meaningful benchmark is an absolute risk difference of at least 10 percentage points; this is an interpretation threshold, not a powered noninferiority margin.

### Exact evidence required

The effect question requires:

- confirmed curative-intent HCC resection and no gross residual disease at baseline;
- confirmed MVI status and, ideally, MVI grade;
- confirmation that the first post-resection embolization was adjuvant chemotherapy embolization rather than treatment of known residual/recurrent disease, bland embolization, radioembolization, hemorrhage control, or a diagnostic angiogram;
- treatment date relative to resection;
- pre-TACE imaging/clinical evidence that recurrence was absent through treatment assignment and through the day-84 landmark;
- standardized longitudinal CT/MRI or other accepted liver imaging through day 365, including outside-institution studies;
- blinded adjudication of the first recurrence date and location;
- baseline tumor burden, resection margin, macrovascular invasion, liver reserve, postoperative recovery/complications, and treatment-indication variables that influence timing;
- survival, competing death, and loss-to-follow-up information.

The HCC source supplies only part of this evidence. Missing outside imaging, a dependable death endpoint, structured margin/MVI grade, explicit treatment indication, and complete postoperative complication data prevent an unconditional causal recurrence-effect claim.

## Target trial and computable Harbor experiment

### Population and index

Use the earliest observed qualifying liver resection for each participant as index day 0. Include participants who:

1. are age 18 years or older at the index encounter;
2. have an index procedure name consistent with liver resection (`肝.*切除`, `半肝切除`, `肝叶切除`, or `肝段切除`) and not merely cholecystectomy, transplant, biopsy, radiofrequency ablation, or microwave ablation;
3. have pathology linked to the same `患者主索引` and `就诊号` with HCC and affirmative MVI evidence after phenotype validation;
4. have no recorded institutional TACE, liver ablation, or liver transplant during days −180 through −1;
5. have first post-index strict TACE during days 1–84;
6. have no adjudicated residual/recurrent tumor before or on day 84;
7. are known through clinical review to be alive at day 84 and to have received TACE for an adjuvant rather than therapeutic indication.

Day 84 is the common time zero for outcome analysis. This avoids assigning pre-treatment person-time to either timing strategy, but changes the estimand to the selected population alive, recurrence-free, and treated by day 84. It does not estimate the effect of treatment versus no treatment or the effect in patients who die, recur, or never receive TACE before day 84.

Because no dependable death endpoint exists in the source, criterion 7 cannot be established automatically. Encounter presence after day 84 is not a valid surrogate for survival. Clinical review or linked vital status is essential before final effect estimation.

### Exposure strategies

Primary exposure uses the first qualifying postoperative procedure `开始时间`:

- earlier TACE: day 1 through day 42 inclusive;
- later TACE: day 43 through day 84 inclusive.

Strict qualifying TACE requires explicit `TACE` or co-occurring chemotherapy and embolization wording (`化疗...栓塞` or `栓塞...化疗`) in `手术`. Generic hepatic artery embolization is not primary. The broad parent expression is prohibited because source auditing found broad-only splenic and bronchial embolization, angiography/infusion combinations, bland hepatic embolization, and radioisotope combinations. Generic hepatic-artery embolization is evaluated only after blinded procedure-dictionary review and, if accepted, as a sensitivity analysis.

The boundary is prespecified from the parent question, but timing density must be plotted in aggregate and analyzed continuously as a secondary noncausal dose-timing description because feasibility data show heaping around day 42. Results that appear only under the dichotomy and not under nearby cutoffs (35/49 and 28/56 days) are fragile.

### Primary estimand

Conditional on all validation and observation gates passing, estimate the per-protocol intention-to-initiate contrast among eligible day-84 survivors treated by day 84:

- 365-day risk difference and risk ratio for first adjudicated intrahepatic recurrence from day 85 through day 365, comparing earlier with later first TACE.

A secondary estimand is the restricted mean recurrence-free time difference over days 85–365. With no validated competing-death data, it may be reported only after linkage/adjudication of death; otherwise recurrence-free survival is not computable as a clinical endpoint.

### Primary outcome: adjudicated imaging-anchored recurrence

A candidate event must have a dated qualifying liver examination on days 85–365 and report text in `检查所见` or `检查诊断` indicating a new or recurrent lesion after resection (for example, liver/operative-bed text near `复发`, `新发病灶`, or `新发结节`). A blinded panel of two clinicians independently reviews the longitudinal record, including the examination name, findings, diagnosis, relevant pre-landmark and prior surveillance reports, pathology, diagnoses, treatment-course notes, and subsequent management. Disagreement is resolved by a third adjudicator.

Adjudicators are masked to the earlier/later category and receive relative day intervals rather than exposure labels. They classify:

- definite recurrence;
- probable recurrence;
- no recurrence;
- indeterminate;
- residual disease already present by day 84;
- insufficient imaging evidence.

Primary events are definite recurrence; definite plus probable is sensitivity analysis. The event date is the earliest imaging date supporting the adjudicated recurrence. Indeterminate cases are not silently classified as no recurrence.

Subsequent TACE, ablation, resection, transplant, or a recurrence diagnosis is corroborating evidence only and never sufficient for the primary event. This prevents planned serial TACE and treatment preference from becoming the outcome.

### Co-primary process endpoint and observation target

Compute separately by timing group:

- probability of at least one technically qualifying liver CT/MRI report during days 85–365;
- probability of imaging in prespecified surveillance windows, days 85–180 and 181–365;
- number of qualifying liver studies and all encounters per 100 observed days;
- time from day 84 to first qualifying study;
- proportions with only ultrasound/other imaging, outside-imaging references without an available report, or no ascertainable imaging;
- reasons for missing follow-up from manual review when available.

No-imaging participants have unknown recurrence status, not recurrence-free status. The primary recurrence effect is estimated only under the prespecified gates below, using the target population plus observation models; a complete-case estimate among imaged participants is explicitly labeled selection-prone and cannot be the headline result.

### Secondary outcomes

1. Definite-or-probable adjudicated recurrence by day 365.
2. Extrahepatic or any-site adjudicated recurrence if observable.
3. Repeat TACE and any repeat liver-directed procedure after first TACE, reported as treatment-process outcomes, not recurrence.
4. Hospital encounter within 14 days after first TACE and same-assay changes in bilirubin, INR, ALT, albumin, and creatinine, only after an exact-label assay dictionary is validated. Units are unavailable, so values cannot be pooled across assay labels; the contaminated albumin mapping in the exploratory script is not reusable as-is.
5. Documented post-TACE complication signals, exploratory and adjudication-required.

### Baseline variables and timing-confounding controls

All automatic baseline covariates must precede first TACE; variables affected by timing cannot be treated as ordinary baseline confounders. Extract, where observable:

- age, sex, weight, and index year;
- exact index resection wording and surgical source;
- pathology text features: tumor count/size, grade/differentiation, capsule, satellite lesions, macrovascular/portal-vein invasion, margin language, cirrhosis, MVI wording/grade;
- diagnosis and clinical-document text for HBV/HCV, cirrhosis, portal hypertension, diabetes, and comorbidity;
- index length of stay and discharge-to-TACE interval;
- preoperative and immediate postoperative exact-label AFP, bilirubin, INR, albumin, ALT/AST, creatinine, platelets, and other liver-reserve measures when available;
- postoperative complications, readmission, infection, bleeding, bile leak, ascites, and liver failure signals before treatment;
- pre-TACE imaging and laboratory testing intensity;
- calendar period and clinical department.

Timing confounding is particularly serious: delayed treatment may reflect slower recovery, complications, impaired liver reserve, scheduling, pathology turnaround, or concern for residual disease. Pathology has no independent sign-out timestamp, clinical documents have no native timestamp, and the source does not reliably encode planned treatment indication. Therefore, automatic covariate adjustment alone cannot establish exchangeability.

### Analysis

#### Stage A: validation and estimability gates

Before treatment-effect modeling:

1. Draw a reproducible stratified random audit sample from all machine-positive and machine-negative index records and procedure classes, with a fixed seed. The audit must include at least 100 HCC/MVI phenotype records (positive, local-negation, broad-only, and negative strata), all distinct frequent TACE-name classes plus all exposed broad-only cases, and all candidate recurrence events plus at least 50 candidate-negative imaging reports if counts permit.
2. Have two blinded clinical reviewers establish reference classifications. Report sensitivity, specificity, positive predictive value, negative predictive value, and Cohen's kappa with exact/binomial uncertainty.
3. Reconcile the parent’s 2,323 lexical MVI-positive count with the new local-negation rule’s 2,935 before freezing the phenotype. Neither is clinical truth. The primary MVI phenotype must achieve PPV at least 0.90 and kappa at least 0.80, or the experiment stops at phenotype-feasibility results.
4. The strict TACE/adjuvant-indication phenotype must achieve PPV at least 0.95 and kappa at least 0.80. Otherwise no timing-effect estimate is presented.
5. Recurrence adjudication must achieve kappa at least 0.80; disagreement and indeterminate fractions are reported.
6. Report group sizes after every filter, event counts, imaging coverage, missing covariates, and excluded pre-landmark disease.

#### Stage B: confounding and observation diagnostics

Estimate the propensity for earlier versus later TACE using a parsimonious prespecified model because the later group is small; consider penalized logistic regression without outcome-guided variable selection. Report propensity distributions, overlap, stabilized weights, effective sample size (ESS), maximum weight, and standardized mean differences (SMDs). Truncate weights at the 1st/99th percentiles only as a sensitivity analysis, not to conceal nonoverlap.

Separately estimate the probability of qualifying imaging in each surveillance window using only information available before that window. Use inverse-probability-of-observation weights for the adjudicated outcome analysis if positivity is plausible. Report covariate balance both for treatment weights and combined treatment-observation weights. Multiple imputation may address partially observed baseline covariates under stated missing-at-random assumptions; it cannot manufacture unobserved recurrence outcomes or death.

Primary adjusted inference uses doubly robust standardization or weighted outcome regression for day-365 risks with participant-level bootstrap confidence intervals. Given anticipated small samples/events, do not rely on asymptotic p-values. Provide unadjusted risks only as descriptive quantities. If sparse-event separation occurs, use penalized models for diagnostics but do not interpret model convergence as estimability.

#### Stage C: sensitivity analyses

- definite versus definite-or-probable recurrence;
- strict TACE only versus validated inclusion of selected hepatic embolization names;
- alternative timing boundaries at 35/49 and 28/56 days;
- restriction to patients with imaging in both surveillance windows;
- complete-case imaged analysis, clearly labeled selection-prone;
- inverse-probability-of-observation assumptions under progressive selection-bias tipping analyses: vary the unobserved recurrence odds among non-imaged participants by group and determine when the conclusion reverses;
- E-value or quantitative unmeasured-confounding analysis for any apparently protective estimate, while noting it cannot capture indication miscoding or unobserved residual disease;
- exclude patients with repeat TACE within 42 days after first TACE to probe serial planned treatment, without reclassifying repeat TACE as recurrence;
- calendar-period restriction and flexible adjustment for index year.

### Negative controls and falsification

1. **Pre-exposure outcome falsification:** candidate recurrence language dated before first TACE, including days 1–84, must not appear less often in the earlier group after adjustment. An association implies residual disease/indication differences or temporal leakage.
2. **Pre-exposure observation falsification:** pre-TACE imaging and laboratory encounter intensity should balance after weighting. Persistent differences indicate surveillance/recovery confounding.
3. **Non-liver observation control:** where identifiable, compare non-liver examination/encounter intensity after day 84. A timing association similar to that for liver imaging suggests general care-utilization selection.
4. **Planned-treatment diagnostic:** a strong group difference in repeat TACE within 42 days after the first session, especially without adjudicated recurrence, falsifies use of repeat procedures as disease outcomes and may reveal strategy differences beyond initiation timing.
5. **Calendar-placebo analysis:** within strata where workflow changed but biological timing should not, strong discontinuities at the 42-day cutoff or effect reversal under nearby cutoffs make the dichotomous result non-robust.

These controls can expose bias but cannot prove its absence.

## Prespecified estimability and falsification criteria

Do not issue a comparative recurrence-effect conclusion if any of the following occurs:

- phenotype or procedure PPV/kappa gates fail;
- adjuvant indication or day-84 recurrence-free status cannot be adjudicated;
- fewer than 20 total definite recurrence events or fewer than 5 in either timing group;
- fewer than 60% of either group has a qualifying liver CT/MRI report through day 365, or the adjusted absolute difference in imaging observation exceeds 10 percentage points;
- treatment PS overlap fails (for example, more than 10% outside common support), weighted ESS is below 50 overall or below 15 in either group, any post-weight SMD exceeds 0.10 for a major confounder, or extreme weights dominate;
- combined observation weights violate positivity or reduce ESS below those thresholds;
- pre-exposure falsification outcomes remain materially associated with timing;
- the direction of effect reverses across reasonable endpoint adjudication definitions or observation-bias tipping values near the empirical range.

Thresholds are safeguards against false precision, not guarantees of causal validity. The feasibility scan already suggests the 60% imaging gate will fail without recovering outside studies or additional report classes: observed qualifying imaging was 31% (24/78) versus 39% (11/28). Thus the most likely valid result from the current frozen extract is “comparative recurrence effect not estimable,” unless manual review identifies substantially more valid imaging.

## Interpretation

### Supportive result

A supportive result requires all gates to pass, adequate overlap and event counts, balanced observation, null falsification controls, and an adjusted earlier-minus-later recurrence risk difference below zero with uncertainty excluding no difference; an absolute reduction of at least 10 percentage points would be clinically notable. The strongest defensible claim would be that earlier initiation is associated with lower one-year adjudicated intrahepatic recurrence among selected day-84 survivors who received adjuvant TACE by day 84 under the measured and modeled assumptions. It would not prove that TACE itself is beneficial, that 42 days is biologically optimal, or that practice should change.

### Adverse result

If all gates pass and earlier treatment yields higher adjudicated recurrence, materially more post-TACE hepatic injury, or both, the result argues against assuming that earlier initiation is superior in this selected population and motivates scrutiny of postoperative recovery and selection. It does not establish harm from early TACE without stronger confounding control and complete death/toxicity ascertainment.

### Null but precise result

If all gates pass and confidence intervals exclude a clinically meaningful 10-percentage-point benefit or harm, the study supports no large one-year recurrence difference between these timing windows in the selected institutional population. It cannot establish equivalence outside the prespecified margin or among untreated/early-failure patients.

### Inconclusive or non-estimable result

Failure of imaging coverage, adjudication, event, overlap, observation-weight, or falsification gates means the timing effect is non-estimable from this extract. That is not evidence of no effect. Report the exact failed gate and the data needed: linked outside imaging, standardized surveillance, treatment-indication documentation, death linkage, or a prospective/multicenter registry.

## Exact source bindings and provenance

Snapshot provenance is the HCC snapshot recorded in `datasets/hcc/metadata.json` (`[source checksum]`). Source files remain read-only; derived relative intervals and aggregate outputs belong in the workspace. Never release direct identifiers or exact dates.

Join across tables by `患者主索引`; join encounter-specific records by `患者主索引` plus `就诊号`.

1. **Procedures**
   - Source: `[internal dataset path]`
   - Catalog: `datasets/hcc/table-d5eae16f8f8093d9.json`
   - Columns: `患者主索引`, `就诊号`, `手术`, `开始时间`, `结束时间`, `手术来源`.
   - Uses: index resection, first strict TACE, prior treatment, repeat-treatment process outcomes. Derive only within-participant days relative to index/TACE.

2. **Pathology**
   - Source: `[internal dataset path]`
   - Catalog: `datasets/hcc/table-0a4ee86a446c605c.json`
   - Columns: `患者主索引`, `就诊号`, `病理`, `检查所见`, `检查诊断`, `机器型号`.
   - Uses: lexical HCC/MVI candidate phenotype and manual adjudication. There is no independent pathology sign-out time; do not infer treatment eligibility date from this table.

3. **Encounters/basic information**
   - Source: `[internal dataset path]`
   - Catalog: `datasets/hcc/table-b743286cb1249287.json`
   - Columns: `患者主索引`, `就诊号`, `年龄`, `性别`, `身高`, `体重`, `就诊时间`, `入院时间`, `出院时间`, `就诊科室`.
   - Uses: age/sex, encounter timing, department, index stay, observation-process measures. Encounter after day 84 does not establish survival or disease-free status. Direct identifiers in this table are prohibited from outputs.

4. **Examinations**
   - Source: `[internal dataset path]`
   - Catalog: `datasets/hcc/table-fd016d2731b9d6c6.json`
   - Columns: `患者主索引`, `就诊号`, `检查`, `检查所见`, `检查诊断`, `开始时间`, `机器型号`, `检查号`.
   - Uses: qualifying liver-imaging denominator, candidate recurrence reports, and adjudicated event date. Text extraction is unvalidated; no recurrence is assigned without review.

5. **Diagnoses**
   - Source: `[internal dataset path]`
   - Catalog: `datasets/hcc/table-12710723c3df0c99.json`
   - Columns: `患者主索引`, `就诊号`, `诊断名称`, `诊断类型`.
   - Uses: corroboration, baseline conditions, negative controls. No diagnosis-level timestamp exists; inherit encounter time only and label that limitation.

6. **Laboratory tests**
   - Source: `[internal dataset path]`
   - Catalog: `datasets/hcc/table-38aad8c54471332f.json`
   - Columns: `患者主索引`, `就诊号`, `检验`, `定性结果`, `定量结果`, `标本类型`, `检验时间`.
   - Uses: exact-assay baseline covariates and exploratory post-TACE safety. There is no separate unit column; do not pool different assay labels or assume common units.

7. **Clinical documents**
   - Source and archive member as bound in `datasets/hcc/metadata.json` and `datasets/hcc/table-66afca58512c2fca.json` (clinical-document table).
   - Columns include `患者主索引`, `就诊号`, narrative admission/history/diagnosis/treatment-course/discharge/operation fields, and `入院诊断__duplicate_2`.
   - Uses: manual adjudication of indication, postoperative recovery, complications, residual disease, and recurrence corroboration. Documents lack a native document timestamp; inherit encounter context and never treat text as independently dated.

8. **Orders and medications**
   - Catalogs: `datasets/hcc/table-6b93dcf0ea823702.json` and `datasets/hcc/table-4f6ecaeb6e8f69c2.json`, with exact source paths/archive members bound in `datasets/hcc/metadata.json`.
   - Orders columns: `患者主索引`, `就诊号`, `医嘱(非药品)`, `开立时间`, `开始时间`, `结束时间`, `医嘱期限`, `医嘱状态`, `频次`.
   - Medication columns: `患者主索引`, `就诊号`, `用药`, `单次用药计量`, `单次用药计量单位`, `频次`, `开始时间`, `结束时间`, `用药方式`, `药品类型`.
   - Uses: corroborating adjuvant intent, chemotherapy exposure, and complications; not sufficient alone to define TACE.

Vitals, transfers, and front-page sources are identifier-only in this snapshot and add no clinical variables. Imaging pixels, dependable death data, and complete external follow-up are unavailable.

## Computable outputs and verification boundary

An executable implementation can verify:

- source hashes/snapshot and full-file scans;
- deterministic cohort flow, relative-day calculations, and treatment dictionary classes;
- random audit sampling seed and stratum counts;
- group sizes, imaging coverage, event counts, treatment/observation weights, balance, ESS, missingness, and falsification-control estimates;
- adjudication labels once supplied as a governed input;
- adjusted estimates, bootstrap intervals, sensitivity analyses, and whether prespecified gates passed;
- that narrative conclusions match the gate status and computed direction/uncertainty.

An automatic verifier cannot determine curative/adjuvant intent, survival at day 84, true MVI, true recurrence, imaging adequacy, residual disease, causal exchangeability, clinical meaningfulness, or generalizability. Those require clinical adjudication, outside-data linkage, expert review, or another study. Reference execution establishes computational feasibility only, not scientific truth.

## Existing feasibility provenance

The repair is supported by full scans with no row sampling:

- `[internal dataset path]`
- `[internal dataset path]` ([source checksum]; job `[research job]`)
- `[internal dataset path]`
- `[internal dataset path]` ([source checksum]; job `[research job]`)

The scripts are feasibility evidence, not final analysis code. Known quarantined issues are the MVI rule discrepancy, broad TACE contamination, and exploratory albumin-label contamination.

## Relation to existing knowledge and ambition references

Current literature supports the importance of MVI and continued uncertainty around postoperative adjuvant TACE selection and effect; it does not establish that days 1–42 are superior to days 43–84. A 2026 multicenter analysis specifically showed that conventional analyses of adjuvant TACE can change after landmark and time-dependent analyses, reinforcing the need to define treatment timing and immortal-time handling; its abstract does not validate this source’s recurrence proxy or timing boundary (Zhang et al., *Surgical Endoscopy*, DOI `10.1007/s00464-026-12838-x`). A recent review likewise characterizes patient selection and benefit as unresolved and calls for prospective validation (Chen et al., DOI `10.2147/JHC.S601849`). These references were identified through current Europe PMC records; unavailable full text is not claimed as inspected.

The locally available research-ambition demonstrations were used methodologically, not as HCC evidence. The inspected cancer supplement emphasizes missingness-process shortcuts, validation, calibration, and prospective evaluation; the main Cell article and STAR Methods were unavailable and are not claimed as read. The inspected natural-history article material emphasizes explicit event time, representation of observation gaps, external validation, and bias assessment. This child applies those lessons by separating recurrence from the healthcare observation process and by refusing an effect conclusion when observation cannot support it.

## What remains uncertain

Even after this repair, a valid causal timing estimate may remain impossible because treatment timing reflects postoperative recovery and indication, the day-84 estimand excludes early deaths/recurrences, exact pathology timing is absent, outside imaging and death are missing, and the later group is small. The design makes these limitations testable and reportable rather than concealing them inside a broad utilization endpoint. A definitive clinical recommendation would require a prospective multicenter registry or randomized timing trial with standardized pre-TACE disease assessment, liver-reserve criteria, surveillance imaging, recurrence adjudication, toxicity, and vital status.
