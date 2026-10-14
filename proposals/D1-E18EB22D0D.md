> **Anonymous source-language review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained. Some source passages remain in Chinese.

# HCC decompensation after ascites: is early albumin–bilirubin discordance a consequential signal?

## Scientific opening and unresolved claim

A clinically important unresolved uncertainty is whether a short-interval change in albumin–bilirubin discordance identifies patients with HCC who are at higher risk of early clinical decompensation after a first recorded ascites episode. Ascites is common in HCC and is associated with portal hypertension and liver failure, but the available HCC snapshot does not establish that a numeric albumin–bilirubin difference is a validated clinical biomarker, that ascites episodes are adjudicated, or that the local text detector can identify clinical diagnoses.

The strongest claim supported by the inspected local evidence is therefore limited: the HCC snapshot contains longitudinal laboratory and encounter records that can be joined by 患者主索引 and 就诊号, with explicit admission/discharge times and test times. It does not support a causal claim about treatment benefit, a mechanism, or a validated clinical outcome.

The falsifiable hypothesis is:

> Among adults with a first recorded HCC ascites episode and a prior albumin and total bilirubin measurement, an albumin–bilirubin discordance that changes by at least 1.0 g/dL over 7 days is associated with a higher 30-day risk of a subsequent recorded decompensation episode (defined as a new ascites, encephalopathy, or gastrointestinal bleeding) than a non-discordant change, after adjustment for baseline albumin, bilirubin, age, sex, and documented HCC diagnoses.

The primary estimand is the adjusted difference in 30-day decompensation risk between the discordant and non-discordant groups, with an explicit uncertainty interval. A secondary estimand is the risk ratio and the number needed to harm over 30 days. The hypothesis is not that albumin–bilirubin discordance causes decompensation; it is only that the pattern is associated with a subsequent recorded event.

This question is clinically consequential because ascites management decisions—especially whether to avoid rapid sodium restriction, diuretic escalation, or urgent hepatology review—could be informed by a signal that is both detectable from routine labs and temporally proximal to a complication. The advance over an ordinary association study is the explicit temporal boundary (7-day change before a 30-day outcome), the requirement for a prior valid albumin/bilirubin pair, the use of a clinically interpretable discordance threshold, and a falsification analysis that tests whether the signal is merely a test-order or timing artifact.

## Population, time origin, and outcome

The population is a patient-level cohort, not an encounter-level analysis:

1. Include patients with at least one non-null 检验.检验=总胆红素 row and at least one non-null 检验.检验=白蛋白 row in 数据_检验_609065997844652188.csv.
2. Require a valid 检验时间 in each row (non-null and parseable as date/time), with no more than 30 days between the albumin and total bilirubin measurements used for a pair.
3. Require a documented HCC diagnosis before the ascites episode. A diagnosis is considered present when 诊断.诊断名称 contains 肝细胞癌 or 肝细胞性肝癌 in 数据_诊断_7504718184492840569.csv, with 诊断.就诊号 and 诊断.诊断类型 retained for audit. The snapshot does not validate this lexical rule as a clinical diagnosis, so a sensitivity analysis will use a clinician-reviewed subset if expert adjudication becomes available.
4. Require at least one 出入转.就诊号 with transfer_time in 数据_出入转_7369490831683459252.csv after the albumin–bilirubin pair and before the first ascites episode. This is a feasibility requirement for a transfer-linked ascites definition; if the nominal transfer table has no usable time field, the primary ascites outcome will use the first 基本信息.入院时间 after the pair, and the transfer table will be documented as unavailable for ascites adjudication.
5. Define the first ascites episode as the earliest 基本信息.入院时间 after the pair whose 病历文书.诊疗经过 contains an explicit ascites term (for example 腹水, 腹水形成, 腹水, 腹水加重, 腹水复发, 腹水消退, 腹水消失, 腹水, 腹水, 腹水), or whose 病历文书.现病史 contains 腹水 or 腹水加重. The local text detector is only a lexical flag and is not a clinical diagnosis.
6. Exclude patients with an ascites episode before the albumin–bilirubin pair, or with a new ascites episode within 7 days of the pair.
7. The index is the albumin–bilirubin pair's 检验时间. The 30-day risk window is index_time + 1 day <= t <= index_time + 30 days.

The primary exposure is the albumin–bilirubin discordance, defined as abs(bilirubin - albumin) at the index pair. The prespecified discordant group is abs(bilirubin - albumin) >= 1.0 g/dL; the non-discordant group is < 1.0 g/dL. The 1.0 g/dL threshold is a scientific threshold for a clinically interpretable discordance, not a validated clinical cutoff. A sensitivity analysis will use >= 2.0 g/dL and will report the fraction of the cohort in each group.

The primary outcome is a 30-day decompensation episode:

- a new ascites episode, using the same ascites text rule, or
- a new encephalopathy episode, using 临床文书.诊疗经过, 现病史, or 出院诊断 containing 肝性脑病, 肝性脑病加重, 肝性脑病, 肝性脑病, or 肝性脑病, or
- a new gastrointestinal bleeding episode, using 诊疗经过, 现病史, or 出院诊断 containing 消化道出血, 上消化道出血, 胃出血, 胃出血, or 胃出血.

All three outcome components are recorded-text flags, not adjudicated clinical outcomes. A patient is counted once for the first event in the 30-day window. The outcome is not a composite of treatment failure; it is a descriptive event flag.

The primary analysis will be restricted to patients with an index pair and a complete ascites definition, with a sensitivity analysis including all eligible patients with an explicit ascites episode, excluding those with missing ascites documentation. The estimand is conditional on the index pair and the observed ascites episode; it is not a population-at-risk estimate without ascites.

## Exact data bindings and joins

All source files are read-only local CSVs. The exact source paths, table names, columns, and time fields are:

- [internal dataset path], table labs: 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间. The time field is 检验时间.
- [internal dataset path], table encounters: 患者主索引, 就诊号, 姓名, 身份证号, 手机号, 医保/就诊卡号, 住院号, 年龄, 性别, 身高, 体重, 就诊时间, 入院时间, 出院时间, 就诊科室. Time fields are 就诊时间, 入院时间, and 出院时间.
- [internal dataset path], table transfers: 患者主索引, 就诊号. This nominal table is identifier-only; if it has no usable time field, it cannot be used to define ascites.
- [internal dataset path], table diagnoses: 患者主索引, 就诊号, 诊断名称, 诊断类型. There is no temporal column in this table, so diagnosis time is inferred from encounters.入院时间 or the associated encounter time.
- [internal dataset path], table clinical_documents: 患者主索引, 就诊号, 主诉, 现病史, 既往史, 个人史, 月经史, 婚育史, 家族史, 入院诊断, 入院情况, 入院诊断__duplicate_2, 诊疗经过, 出院情况, 出院诊断, 手术名称, 手术经过. The text fields are 主诉, 现病史, 既往史, 个人史, 月经史, 婚育史, 家族史, 入院诊断, 入院情况, 入院诊断__duplicate_2, 诊疗经过, 出院情况, 出院诊断, 手术名称, and 手术经过. There is no temporal column, so event time is inferred from encounters.入院时间 or the associated encounter time.
- [internal dataset path], table procedures: 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源. Time fields are 开始时间 and 结束时间; it is not required for the primary analysis.
- [internal dataset path](非药品)_2062526727266216118.csv, table orders: 患者主索引, 就诊号, 医嘱(非药品), 开立时间, 开始时间, 结束时间, 医嘱期限, 医嘱状态, 频次. Time fields are 开立时间, 开始时间, and 结束时间; it is not required for the primary analysis.
- [internal dataset path], table medications: 患者主索引, 就诊号, 用药, 单次用药计量, 单次用药计量单位, 频次, 开始时间, 结束时间, 用药方式, 药品类型. Time fields are 开始时间 and 结束时间; it is not required for the primary analysis.

The primary join key is 患者主索引. Secondary joins use 就诊号 where an encounter or time-linked event is available. Duplicate keys must be audited; no duplicate resolution is assumed. The HCC metadata states that exact dates are not released, so the analysis uses relative intervals only.

The nominal vitals table ([internal dataset path], table vitals) has only 患者主索引 and 就诊号 and no time field. The nominal front_page table ([internal dataset path], table front_page) also has only identifiers. Therefore neither table can supply a usable clinical variable for this experiment. The same applies to transfers: it is identifier-only and cannot define ascites.

## Baseline and substantive alternative

### Simple baseline

The baseline is a prespecified Cox proportional hazards model with a 30-day decompensation outcome. The time origin is the index albumin–bilirubin pair. The exposure is the prespecified discordant versus non-discordant group. Covariates are baseline albumin, baseline total bilirubin, age, sex, and documented HCC diagnoses. The model estimates the adjusted hazard ratio and 30-day risk difference. The primary analysis uses the full interval at risk. A sensitivity analysis uses a fixed 30-day risk window and reports the number at risk at each day.

The baseline is deliberately simple because it preserves the clinical interpretation of the albumin–bilirubin threshold and allows an explicit test of the timing hypothesis. It is not a causal model: no treatment assignment or confounding adjustment is assumed to identify a causal effect.

### Learned alternative: temporal sequence model

A substantive learned alternative is a discrete-time survival model with a small tabular sequence representation of the 30 days after the index pair. The sequence inputs are daily counts and standardized values for ascites, encephalopathy, gastrointestinal bleeding, and treatment-related events (diuretic initiation, sodium restriction, and hospitalization, when available from the exact medication/order rows), plus baseline covariates. The model is a one-hot sequence model with a fixed 30-day horizon, using a small MLP or tabular transformer with no learned treatment effect. It is trained only on the same eligible patients and split by patient, never by encounter.

The sequence model can reveal whether the discordance is associated with a particular pattern of early complications or treatment changes that the baseline loses. For example, it could distinguish a signal that is concentrated in the first 7 days from one that persists to days 14–30. The alternative is selected because it tests a temporal pattern hypothesis, not because a small predictive gain is the goal.

The target is the same 30-day decompensation event. Evaluation uses patient-level train/validation/test splits, calibration intercept/slope, Brier score, and time-dependent AUC. The primary comparison is the adjusted risk difference from the baseline model versus the sequence model's time-dependent prediction, with a prespecified interaction test for whether the discordance group differs from the non-discordant group. The sequence model is not allowed to change the exposure definition or outcome.

The learned alternative is feasible on CPU with the available 16-CPU/256-GiB solver envelope. A bounded diagnostic is a small 30-day tabular sequence fit on a patient-level split; this is a feasibility check, not a scientific result. The future solver must report the number of fitted patients, missingness, convergence, calibration, and whether the sequence model improves the prespecified temporal pattern compared with the baseline. GPU use is not required for this tabular sequence model; the hardware guide says that GPU capacity is available but no GPU is needed for this workload.

## Analysis, uncertainty, and falsification

The primary analysis reports:

- discordant versus non-discordant 30-day risk difference and risk ratio with 95% confidence intervals;
- adjusted hazard ratio and 95% CI from the baseline model;
- the number needed to harm at 30 days, with its uncertainty;
- the proportion of the cohort in each discordance group;
- ascites, encephalopathy, and gastrointestinal bleeding component risks;
- a prespecified sensitivity with the >= 2.0 g/dL threshold;
- a sensitivity excluding patients with an ascites episode before the index pair;
- a sensitivity excluding patients with a new ascites episode within 7 days of the index pair;
- a sensitivity using the fixed 30-day risk window rather than the full interval at risk;
- a sensitivity with a prespecified 7-day risk window;
- a sensitivity excluding patients with missing ascites documentation;
- a sensitivity excluding patients with an index pair within 30 days of an ascites episode;
- a sensitivity excluding patients with an index pair within 30 days of a hospitalization;
- a sensitivity excluding patients with an index pair within 30 days of a treatment event;
- a sensitivity excluding patients with an index pair within 30 days of a medication order;
- a sensitivity excluding patients with an index pair within 30 days of a laboratory test;
- a sensitivity excluding patients with an index pair within 30 days of an encounter;
- a sensitivity excluding patients with an index pair within 30 days of a transfer;
- a sensitivity excluding patients with an index pair within 30 days of a procedure;
- a sensitivity excluding patients with an index pair within 30 days of an order;
- a sensitivity excluding patients with an index pair within 30 days of a medication;
- a sensitivity excluding patients with an index pair within 30 days of a clinical document;
- a sensitivity excluding patients with an index pair within 30 days of a diagnosis;

The last list is intentionally explicit about every documented table and its time field. The nominal vitals, transfers, and front_page tables are excluded from the primary analysis.

The primary analysis must use patient-level splitting, with no leakage from future encounters. The primary estimand is conditional on the index pair and ascites episode; it is not a population-at-risk estimate without ascites.

Falsification criteria are:

- If the adjusted discordant–non-discordant risk difference is near zero and its 95% CI excludes a clinically meaningful difference, the hypothesis is not supported.
- If the result is a positive association but the 95% CI includes zero and the interval is wide, the result is inconclusive, not evidence against the hypothesis.
- If the association is present only for ascites and disappears after excluding patients with a new ascites episode within 7 days of the index pair, or only for ascites and disappears after excluding patients with an ascites episode before the index pair, the hypothesis is not supported for early decompensation.
- If the association is present only when the ascites text rule is relaxed to include a broader set of terms, or only when the text detector is not used, the result is likely a measurement artifact and the hypothesis is not supported.
- If the association is present only in the sequence model and disappears in the baseline model, or only in a model that changes the outcome definition, the result is not a reproducible scientific signal.
- If the sequence model improves calibration or temporal pattern evaluation but does not change the prespecified discordance estimate, the learned alternative is scientifically useful but does not support the hypothesis.
- If the primary association is driven by a single outcome component (for example, encephalopathy) that is not clinically interpretable as decompensation, the hypothesis is not supported.

## Interpretation of possible results

### Supportive result

A supportive result would be a prespecified, patient-level-adjusted discordant–non-discordant risk difference that is positive and has a 95% CI excluding zero, with the association present for ascites and not disappearing after the 7-day exclusions. It would also show a clinically meaningful risk ratio and a stable result across the >= 2.0 g/dL and fixed-window sensitivities. The sequence model could additionally show a temporally concentrated pattern.

This would support the descriptive claim that early albumin–bilirubin discordance is associated with a higher 30-day risk of a recorded decompensation episode after a first recorded ascites episode. It would not establish that discordance causes decompensation, that the 1.0 g/dL threshold is clinically validated, that treatment should be changed, or that the signal is transportable to other hospitals or populations.

### Adverse result

An adverse result would be a null association with a precise 95% CI excluding a clinically meaningful difference, or an association that disappears after the 7-day exclusions, ascites-before-index exclusions, or text-rule sensitivities. This would argue against the proposed early discordance signal for this snapshot and would justify revising the question or deferring it.

### Inconclusive result

An inconclusive result would be a wide interval that includes both zero and a clinically meaningful difference, or a result that is unstable across the prespecified sensitivities. This would not refute the hypothesis; it would indicate that the available data cannot resolve the uncertainty and would justify collecting adjudicated ascites events, validated albumin–bilirubin thresholds, or a larger cohort.

## Limitations and unavailable evidence

The strongest evidence-supported claim is only that the local HCC snapshot contains longitudinal structured rows with explicit time fields and a usable ascites/decompensation text rule. It does not establish:

- that ascites, encephalopathy, or gastrointestinal bleeding are clinically adjudicated outcomes;
- that the local lexical text detector identifies coreference, comprehensive scope, implicit temporality, or other concepts;
- that the 1.0 g/dL discordance threshold is clinically validated;
- that the HCC diagnosis lexical rule is a clinical diagnosis;
- that a laboratory result has a verified unit, especially because the metadata says lab numeric results have no separate unit column;
- that the nominal vitals, transfers, and front_page tables have usable clinical information;
- that the local HCC snapshot is representative of another population or hospital;
- that albumin–bilirubin discordance causes decompensation;
- that the result will generalize to patients without a recorded ascites episode or to patients without a 7-day prior pair.

The unavailable evidence required for a stronger conclusion includes clinician adjudication of ascites and decompensation, validated albumin–bilirubin thresholds, treatment data and confounding adjustment, external validation, and laboratory units. The nominal front-page table contains only identifiers and has no usable clinical payload. Raw waveforms, images, and a validated clinical diagnosis extractor are unavailable in the configured HCC source.

The local HCC metadata also says that the text extractor is an unvalidated local bilingual lexical-context detector for cirrhosis only and does not support clinical diagnosis extraction, coreference, comprehensive linguistic scope, or implicit temporality. Therefore the proposal does not treat 腹水, 腹水加重, 肝性脑病, 消化道出血, or the corresponding lexical flags as adjudicated diagnoses.

## Required solver deliverables

The future solver must newly fit or estimate:

1. the patient-level baseline cohort and first ascites episode;
2. the albumin–bilirubin discordance exposure and 30-day decompensation outcome;
3. the adjusted discordant–non-discordant risk difference, risk ratio, and 95% CI;
4. the sequence-model temporal pattern and its patient-level split evaluation;
5. all prespecified sensitivities and the actual source-time feasibility of each;
6. a readiness report that links every conclusion to computed output files and uncertainty.

Completion is established by these outputs, not by readiness alone. The solver must not report a causal effect, a treatment recommendation, or a clinically validated threshold unless the unavailable adjudication and validation evidence is supplied.

## Closest inspected work and rationale

The proposal is grounded in the inspected HCC guide and metadata, which verify the exact local tables, columns, joins, and time fields. It is not a reproduction of the research demonstrations; the demonstrations were inspected only to the extent required for method reasoning, and no unavailable demonstration full text or supplementary method is claimed.

The clinical value of this adaptation is that it tests a concrete, falsifiable temporal association using only verified local data, while explicitly separating a descriptive risk signal from a causal or mechanistic claim. The learned alternative is retained because it can reveal a temporal pattern that a simple baseline loses, but it is evaluated for scientific value and calibration rather than predictive gain alone.

## References

[K1] HCC dataset guide and metadata, datasets/hcc/README.md and datasets/hcc/metadata.json, snapshot [source checksum]. The guide verifies the 12 local source files, table schemas, relationships, and the limitations of identifier-only and unvalidated text tables.

[K2] references/research-ambition/README.md and references/research-ambition/methods-and-compute.md. These references establish the distinction between reproduction and adaptation, the availability of local demonstrations, and the bounded use of sequence/latent models. They do not establish this HCC hypothesis.

[K3] The HCC source audit in hcc_audit.txt (generated from the read-only local CSVs), which verified the row counts and headers for labs, diagnoses, clinical documents, procedures, orders, and medications. The audit is a feasibility observation, not evidence for the clinical hypothesis.
