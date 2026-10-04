# Does leakage-safe intermediate hepatic history add prognostic information for a fixed early post-repeat-TACE directional panel transition after an explicit recorded-care-context stress test?

## Targeted repair and clinical question

This child freezes the parent’s repeat-TACE cohort, recorded-pathway ontology, strict numeric parser and duplicate rule, independent repeat-event selection, `B/P/H` clocks, common same-encounter post-repeat panel nearest +24 hours in `[12h,36h]`, primary outcome models, outcome-observation selection experiment, and noncausal evidence boundary. It changes neither the eligible event, outcome, post-panel selector, primary estimand, nor the parent’s outcome-model falsification machinery. It adds one read-only source and a prespecified **recorded-care-context sensitivity**, because albumin-down/bilirubin-up in this window could reflect albumin, blood products, fluids, diuresis, or peri-procedural observation context rather than hepatic injury.

The unresolved question is deliberately narrow:

> Among adults already selected for a recorded first repeat TACE, do two leakage-safe intermediate-to-current within-assay direction indicators (a) predict whether the fixed early post-event panel is observed after matching the intermediate measurement and encounter-opportunity process, (b) among episodes with that panel observed, improve out-of-fold prediction of a concordant albumin-down/total-bilirubin-up transition beyond remote-to-current direction, a compact decision-time core, and exactly matched intermediate-panel observation variables, and (c) is any measured prediction gain concentrated in episodes with high-specificity recorded albumin, blood-product, or diuretic starts before the selected panel?

The outcome is `Y=1` when albumin at the selected post panel is strictly lower than its contemporaneous pre-repeat value `P` and total bilirubin is strictly higher than its `P`; otherwise `Y=0`. Call this only a **concordant adverse-direction laboratory transition**. “Adverse-direction” describes the signs of two measurements; it is not an adjudicated deterioration, toxicity, decompensation, complication, or clinically important change. The new context audit does not cure this limitation: available rows are orders/records rather than verified administrations, and they lack validated delivered fluid volume, blood-product units, net balance, indication, and peri-procedural adjudication.

The clinical advance is therefore not a treatment recommendation. It is a falsifiable test of whether an archived, leakage-safe trajectory representation should remain a candidate prognostic feature when forecasting a fixed, event-aligned laboratory state, while distinguishing robustness to the small amount of high-specificity recorded supportive care from unresolvable contamination by routine fluid workflow and evolving peri-procedural physiology.

## Evidence already supported versus claim still untested

A complete-source feasibility audit inherited from the parent scanned every row in the five required cohort/outcome sources with no sampling. It reconstructed 319 systemic-record and 1,491 comparator pathway patients, then independently selected 159 and 526 first repeat-TACE events. Requiring both assays at `B` and both at `P`, before requiring the post-event outcome, produced 55 systemic-record and 187 comparator episodes. The locked common post panel was observed in 34/55 and 97/187, leaving 111 outcomes genuinely unmeasured. Prior common intermediate-panel observation was strongly associated with outcome observation: 32/37 versus 2/18 systemic episodes and 93/108 versus 4/79 comparator episodes. Outcome observation also varied sharply by event year. All 242 episodes were documented through +12 hours and 223 through +36 hours; no selected panel was after documented discharge, so short documented encounter duration does not explain the main selection pattern. Albumin and bilirubin intermediate-process clocks disagreed in one of 242 episodes, requiring assay-specific process variables in the observation-denominator experiment.

A new outcome-blind feasibility audit additionally scanned all 4,097,517 medication rows and all 16,730,319 non-drug-order rows and retained only exact composite-key links to the frozen event encounter. It did not inspect post-panel values, `Y`, predictor–`Y` associations, or model performance. The first broad lexical pass demonstrated why a naive adjustment is invalid: generic blood/plasma/cell strings selected coagulation and plasma laboratory orders plus G-CSF/thrombopoietin medications rather than transfusion, while crystalloid-name records occurred before 127/131 observed panels and mixed plain solutions with antibiotic/carrier products. Exact human-albumin names and plausible loop/aldosterone-diuretic names were sparse (preliminary start-record counts 3/131 and 5/131 before the selected panel). Therefore neither delivered fluid nor transfusion can be reconstructed from broad names, doses, or order times. The prespecified executable audit replaces broad blood strings with a high-specificity ontology, uses `开始时间` rather than the earlier of placement/start for primary clocks, separates fixed +12/+24/+36 clocks from the observed-only pre-panel clock, excludes explicitly void/cancelled non-drug orders, and relegates placement-only records to an order-process audit. Its corrected output must reproduce the frozen 242/131 denominators before any context-sensitive conclusion; the earlier broad audit is retained only as ontology-falsification evidence. These are ontology and availability findings, not evidence about the endpoint.

Within the 131 observed-outcome episodes, the directional outcome occurred in 23/34 systemic-record and 63/97 comparator episodes; all five inherited held-out folds contained both outcome classes. Both leakage-safe intermediate assays were available in 32/34 and 93/97 episodes. A narrower 0–24-hour construction was unusable (4/5 complete episodes), whereas the selected panel occurred at median 32.18 and 32.48 hours in the two arms. These are feasibility, denominator, timing, and observation-process facts, not evidence that intermediate values improve prediction of either outcome observation or `Y`.

The parent feasibility artifacts are frozen as [source checksum] (JSON) and `[source checksum]` (implementation). The parent’s complete-source, outcome-blind observation audit is attached as [source checksum] (JSON) and `[source checksum]` (implementation). This child additionally attaches the complete-source supportive-care/context audit and implementation; their published-file hashes provide the frozen provenance. No supportive-care association with outcome values and no outcome-model fitting was performed during design. The actual no-sampling filter is: all source rows -> frozen 319/1,491 pathways -> independently selected 159/526 repeat events -> both-`B`/both-`P` denominator 55/187 -> observed complete fixed-panel denominator 34/97. Execution must additionally report every intermediate observation and recorded-context gate rather than only the endpoints of this flow.

A 2025 retrospective HCC study (Chen et al., *Hong Kong Medical Journal*, DOI `10.12809/hkmj2311208`, full HTML inspected in the lineage) supports the broader clinical relevance of longitudinal albumin–bilirubin state around repeat TACE. It does not validate this 12–36-hour directional endpoint, establish its clinical importance, or answer whether an intermediate panel adds prediction after current state and observation intensity are known.

The untested primary claim is:

> The prespecified two-indicator intermediate-history representation reduces pooled cross-fitted Brier score by at least 0.02 compared with the observation-process-matched model in this 131-episode observed-panel denominator.

The outcome-model claim is supportive only if numeric history does not materially predict inclusion after the same measurement-process adjustment. The 0.02 margin is a locked design convention for a potentially useful forecasting increment, not a validated clinical-benefit threshold.

## Frozen population, pathway ontology, and event

Use HCC snapshot `[source checksum]`. Read every row; no sampling.

1. In `procedures`, qualify rows only when `手术` contains literal case-insensitive `TACE` or literal `化疗栓塞` and `开始时间` parses. Collapse qualifying rows to the deterministic earliest row per patient-calendar-day. For each patient select the earliest adjacent pair 14–180 calendar days apart; the second episode is TACE2 and its earliest exact `开始时间` is `tace2_time`.
2. At the latest encounter no later than exact TACE2, require numeric `年龄>=18`. Require `diagnoses.诊断名称` to contain literal `肝细胞癌` on or before TACE2 after linked-encounter time inheritance. Restrict TACE2 year to 2018–2024 and require a recorded institutional timestamp through TACE2 day +14.
3. Preserve the exact TACE2 days +1 through +14 systemic-record ontology: lenvatinib/仑伐替尼/乐伐替尼, sorafenib/索拉非尼, regorafenib/瑞戈非尼, donafenib/多纳非尼, apatinib/阿帕替尼, sintilimab/信迪利单抗, tislelizumab/替雷利珠单抗, camrelizumab/卡瑞利珠单抗, atezolizumab/阿替利珠单抗, pembrolizumab/帕博利珠单抗, nivolumab/纳武利尤单抗, and bevacizumab/贝伐珠单抗. Preserve the prior-record, placebo, bevacizumab-only, and generic `分子靶向治疗|抗肿瘤免疫治疗|免疫治疗|靶向治疗` ambiguity exclusions. A medication record is not verified administration.
4. Independently of laboratory availability, select within each frozen arm the first strict repeat-TACE patient-day on TACE2 days 15–90 inclusive. Its earliest valid `开始时间` is `event_time`; its `就诊号` is `event_encounter`.

Reproduce 319/1,491 pathways and 159/526 selected events before using laboratory availability. Any unexplained mismatch stops inference.

## Exact six-source bindings

All inputs are read-only ordinary CSVs with no archive member. Catalog SHA-256 is `[source checksum]`.

- `encounters`: `[internal dataset path]`, [source checksum], schema `datasets/hcc/table-b743286cb1249287.json`. Use `患者主索引`,`就诊号`,`年龄`,`性别`,`就诊时间`,`入院时间`,`出院时间`,`就诊科室`. Encounter chronology is `入院时间`, otherwise `就诊时间`; institutional observation uses the latest valid visit/admission/discharge timestamp.
- `diagnoses`: `[internal dataset path]`, [source checksum], schema `datasets/hcc/table-12710723c3df0c99.json`. Use `患者主索引`,`就诊号`,`诊断名称`,`诊断类型`; inherit time only from the composite-key-linked encounter.
- `procedures`: `[internal dataset path]`, [source checksum], schema `datasets/hcc/table-d5eae16f8f8093d9.json`. Use `患者主索引`,`就诊号`,`手术`,`开始时间`,`结束时间`,`手术来源`; only `开始时间` defines clocks.
- `medications`: `[internal dataset path]`, [source checksum], schema `datasets/hcc/table-4f6ecaeb6e8f69c2.json`. Use `患者主索引`,`就诊号`,`用药`,`开始时间`,`结束时间`,`单次用药计量`,`单次用药计量单位`,`频次`,`用药方式`,`药品类型`. Only `开始时间` defines a recorded-start clock; dose/route/end fields are audit-only and do not prove administration or delivered amount.
- `orders`: `[internal dataset path]`, [source checksum], schema `datasets/hcc/table-6b93dcf0ea823702.json`. Use `患者主索引`,`就诊号`,`医嘱(非药品)`,`开始时间`,`开立时间`,`结束时间`,`医嘱期限`,`医嘱状态`,`频次`. `开始时间` is the primary recorded-start clock. Exclude rows whose status contains literal `作废|取消|撤销|退费|已退|废止`. When start is missing, `开立时间` contributes only to a separately reported order-process sensitivity and is never treated as supportive-care exposure.
- `labs`: `[internal dataset path]`, [source checksum], schema `datasets/hcc/table-38aad8c54471332f.json`. Use `患者主索引`,`就诊号`,`检验`,`定量结果`,`定性结果`,`标本类型`,`检验时间`; exact assay labels are `白蛋白` and `总胆红素`.

Join encounter-linked rows only on (`患者主索引`,`就诊号`). A patient-only join may attach the already frozen patient-level event mapping to laboratory rows. Audit source row counts, duplicate/unmatched encounter keys, and any many-to-many multiplication before analysis. Never release identifiers or exact dates.

## Frozen parser, duplicate rule, B/P/H clocks, and outcome panel

Trim `定量结果`; accept only a signed decimal/scientific number with an optional leading `<`,`>`,`≤`, or `≥`. Reject commas and trailing text. The primary analysis uses valid, uncensored rows only. `标本类型` is not a unit. For rows sharing patient, encounter, exact assay label, and exact `检验时间`, retain the final source-order row only if parsed values and censor markers agree; otherwise reject the entire group.

Reproduce 28,159,928 laboratory rows, 476,846 exact target-assay rows, 476,820 valid uncensored numeric-time rows, seven duplicate groups, and zero discordant groups. A mismatch invokes the reconstruction branch.

For each assay separately:

- `B`: latest valid value on TACE2 calendar days -30 through -1.
- `P`: latest valid value in `event_encounter` during `[event_time-72h,event_time)`.
- `H_rows`: values with `time>=tace2_time`, `time<event_time-72h`, `time<P_time`, and encounter unequal to `event_encounter`. `N_H` counts distinct timestamps; `H_any=1[N_H>0]`; `L` is the latest value, with final source order breaking an exact-time tie; `R_hours=event_time-L_time`.

The analysis denominator requires both assays at `B`, both at `P`, and both assays at one common exact timestamp in `event_encounter` with elapsed time inclusively in `[12h,36h]`. Select the common timestamp closest to +24 hours; ties choose the earlier timestamp; within-timestamp duplicate resolution follows the frozen rule. Require both post values. Define `Y=1` only if `Y_albumin<P_albumin` and `Y_bilirubin>P_bilirubin`; equality on either assay is non-event. Do not alter the window, nominal time, tie rule, signs, or denominator after modeling.

Report the two marginal directions, equalities, the four joint direction cells, selected elapsed-time distribution, and native within-assay changes only as distributional audit values with no clinical threshold interpretation. The known marginal prevalence (bilirubin increase 30/34 and 91/97) means any supported joint-state prediction may be largely attributable to albumin direction; the conclusion must say so if component analyses show that pattern and must not imply a coordinated biological mechanism.

## Recorded supportive-care and encounter-context stress test

This is a sensitivity and interpretation gate, not a claim that downstream care is a baseline confounder. Post-event albumin, blood products, fluid workflow, and diuresis can respond to evolving physiology; putting them into `M_obs`/`M_hist` would change the forecasting estimand and could induce bias. Therefore leave the primary 131-episode models and `Delta_Brier` unchanged, and derive the following recorded-context variables only after freezing the panel selector.

Link medications and non-drug orders to the already selected event solely on (`患者主索引`,`event_encounter=就诊号`). A patient-only or time-only supportive-care join is prohibited. Scan all rows; report source, linked, valid-start, placement-only, explicitly invalid-status, and exact matched-label counts. For each observed-panel episode define, using records with `开始时间>=event_time` and strictly before `panel_time`:

- `C_albumin=1` for `用药` or `医嘱(非药品)` matching literal case-insensitive `人血白蛋白|human\s*albumin`;
- `C_blood=1` only for the high-specificity literal `悬浮红细胞|洗涤红细胞|浓缩红细胞|新鲜冰冻血浆|冰冻血浆|单采血小板|冷沉淀|全血|输血|血制品|成分血`;
- `C_diuretic=1` for `呋塞米|速尿|托拉塞米|螺内酯|氢氯噻嗪|吲达帕胺|布美他尼`;
- `C_direct=1[C_albumin or C_blood or C_diuretic]`.

These names identify recorded starts, not administration. Never expand `C_blood` to generic `血浆|红细胞|血小板|白细胞|粒细胞`: the outcome-blind audit showed those strings select laboratory tests and hematopoietic growth factors. Separately define `C_crystalloid_name` from `氯化钠|葡萄糖注射液|林格|勃脉力|醋酸钠林格|乳酸钠林格|复方电解质`, but use it only to demonstrate recorded workflow prevalence. It must not be called delivered fluid, assigned a volume, used for matching/exclusion, or used to infer dilution, because exact labels include carrier/antibiotic products and no validated administration or volume exists.

For all 242 both-`B`/both-`P` episodes, report each context record by fixed clocks `<+12h`, `<+24h`, and `<=+36h`, separately by arm and `O`. Do not use the selected panel as the +24-hour endpoint. For the 131 observed episodes additionally report the strictly-before-selected-panel counts and exact elapsed-time distributions. `开立时间` when `开始时间` is absent is a separately labeled order-process sensitivity only; it cannot set any `C_*` variable. Report how many otherwise matched rows are removed by the explicit invalid-status rule.

Use the primary out-of-fold predictions without refitting to compute

`Delta_Brier_no_direct = mean[(Y-p_obs)^2-(Y-p_hist)^2 | C_direct=0]`.

Also report the number and outcome-class counts with `C_direct=0/1`, each group’s paired mean contribution when both classes are present, and the maximum absolute contribution among `C_direct=1`. This paired-contribution restriction asks whether the prespecified gain is concentrated in episodes with an identifiable recorded start before the panel; it does not estimate an effect of supportive care and cannot remove unrecorded care. The stress test is computable only if the `C_direct=0` subset contains both outcome classes and at least one episode from every primary held-out fold. Otherwise label it context-inconclusive without changing the primary result.

A primary favorable result is **recorded-care-context-sensitive** if the stress test is computable and either `Delta_Brier_no_direct<=0` or `Delta_Brier-Delta_Brier_no_direct>=0.02`. It is **not detectably concentrated in high-specificity recorded care** only when `Delta_Brier_no_direct>0` and attenuation is `<0.02`; even then, do not claim freedom from fluid, transfusion, diuretic, hemodynamic, inflammatory, or peri-procedural contamination. The `0.02` attenuation threshold reuses the locked design-sized Brier increment; it is an interpretation gate, not a treatment-effect threshold.

Encounter context remains separate. From the composite-key-linked encounter define `pre_event_encounter_hours=max(0,event_time-(入院时间 else 就诊时间))`, `opportunity36=min(max(出院时间-event_time,0),36)/36`, and `documented_through_36h=1[出院时间-event_time>=36h]`. Missing or chronologically impossible values are reported, never silently imputed. Add `log(1+pre_event_encounter_hours/24)` and `opportunity36` to **both** `G_process` and `G_value`; neither enters `M_obs` or `M_hist`. Report `O` and context-record prevalence by arm, pre-event-duration quartile, and documented-through-36-hour status. These variables improve description/matching of the fixed-window observation process, but event-to-discharge time is downstream and cannot establish continuous observation, severity, or exchangeability.

## Parsimonious observation-matched primary models

The endpoint denominator is small (34/97; 86 events and 45 non-events), so replace the parent’s four added history-direction coefficients and broader timing core with one two-indicator increment and no tuning, interactions, arm-specific fits, feature selection, or nonlinear learners.

Use these remote-to-current direction indicators:

- `BP_alb_down = 1[P_albumin<B_albumin]`;
- `BP_bili_up = 1[P_bilirubin>B_bilirubin]`.

Use these two candidate intermediate-history indicators:

- `HP_alb_down = 1[H_any=1 and P_albumin<L_albumin]`;
- `HP_bili_up = 1[H_any=1 and P_bilirubin>L_bilirubin]`.

Equality and the opposite direction are the reference. When `H_any=0`, set both `HP` indicators, `logN`, and `logR` to zero. Define `logN=log(1+N_H)` and `logR=H_any*log(1+R_hours/24)`. The inherited audit found co-observed histories; execution must verify albumin/bilirubin equality of `H_any`, `N_H`, and `L_time` in all 131 denominator episodes. Any mismatch is computationally inconclusive; do not silently choose one assay’s clock.

The two nested models are:

`M_obs: Y ~ BP_alb_down + BP_bili_up + arm + age + sex + TACE2_to_repeat_days + P_old_lead_hours + H_any + logN + logR`

`M_hist: M_obs + HP_alb_down + HP_bili_up`

Here `P_old_lead_hours` is the larger of the two positive `event_time-P_time` values. Encode sex as two fixed indicators (`male`, `unknown/other`) with female as reference; if a category has no training observations, its coefficient is fixed to zero in both nested fits for that fold. Both models therefore receive identical current/remote directional state, compact core, pre-panel timing, and whether/how often/how recently the intermediate panel was observed. Only `M_hist` receives the two numeric-history-derived directions. Age is complete by cohort definition; no other imputation is allowed.

Assign five arm-balanced folds by SHA-256 sorting `hcc-repeat-tace-fixed-joint-24h-v1|患者主索引` within arm and rank modulo five. Preserve this primary partition. In each training fold, standardize only age, TACE2-to-repeat days, P-old lead, logN, and logR using training means and population standard deviations; do not scale binary variables. Fit both logistic models with an unpenalized intercept and the same fixed L2 slope penalty `lambda=1`, minimizing mean binomial log loss plus `0.5*sum(beta^2)`. Use deterministic Newton or LBFGS optimization, gradient tolerance `1e-8`, at most 10,000 iterations. No data-dependent penalty selection or fallback is permitted.

Require both classes in every training and held-out fold, finite positive training variance for every retained continuous feature, optimizer convergence, finite coefficients, finite probabilities, and nonzero held-out prediction variance. A zero-variance continuous feature is fixed to zero after centering in both models and recorded; more than one such feature in any fold makes the result model-fragile and inconclusive rather than prompting redesign.

The primary estimand is pooled paired out-of-fold

`Delta_Brier = Brier(M_obs) - Brier(M_hist)`.

Positive values favor the intermediate-history representation. Report both Brier scores, the training-prevalence-only null Brier, paired per-patient Brier contributions, log loss, prediction ranges/variances, and descriptive calibration intercept/slope. Report arm-stratified Brier values only as denominator descriptions; do not estimate an arm interaction or interpret arm differences as effects.

## Uncertainty and focused falsification

### 1. Full-refit conditional bootstrap

The parent’s fixed-prediction bootstrap understated uncertainty by treating fitted cross-validation models as fixed. Replace it with 1,000 full-refit stratified cluster bootstrap replicates using seed `20260911`. Resample patients with replacement within each nonempty primary-fold x arm x outcome cell, preserving each cell’s original size; duplicate copies remain in their original fold and enter training/scoring with integer multiplicity, so no patient can cross from train to test. In every replicate recompute multiplicity-weighted training means/SDs, refit both models in all folds, and recompute the multiplicity-weighted pooled `Delta_Brier`. Report the percentile 95% interval and the fraction `Delta_Brier<=0`. This interval includes fitting instability under resampling but remains conditional on the observed complete-panel cohort, the frozen partition, cell counts, modeling choices, and missing-outcome process; it is not population or clinical-utility uncertainty. Fewer than 950 estimable replicates is computationally inconclusive.

### 2. History-linkage destruction

Among `H_any=1`, jointly permute each patient’s paired `(L_albumin,L_bilirubin)` values across patients within arm and primary fold 500 times, while retaining that recipient’s `L_time`, `H_any`, `N_H`, `logR`, `B/P/Y`, covariates, and fold. Recompute only the two `HP` directions and refit the full cross-validation pipeline. This destroys patient-specific numeric history while exactly preserving the observation process and leakage clock. Support requires observed `Delta_Brier` to exceed the 95th percentile of permuted gains. Report the permutation distribution; do not call it a test of causality.

### 3. Partition stability

Repeat the complete point-estimate pipeline with four additional frozen salts ending `-v2` through `-v5`, using the same within-arm rank-modulo-five rule. A result is partition-sensitive if fewer than four of five total partition estimates are positive, or if their median is below 0.02 when the primary point estimate is at least 0.02. Bootstrap uncertainty remains attached only to the primary partition.

### 4. Influence

Using the primary out-of-fold paired contributions, delete one patient at a time without refitting and recompute `Delta_Brier`. Also report the largest absolute paired contribution. A favorable primary estimate is influence-sensitive if any deletion changes its sign or moves it by at least 0.02. This is a prediction-contribution diagnostic, not a replacement for the full-refit bootstrap.

### 5. Component attribution and timing specificity

Fit the identical two models separately for albumin decrease and bilirubin increase, secondary only. Do not substitute either component for the primary outcome. If the primary gain is favorable but only one component has positive gain, label the result component-attributed and name the component; this qualifies interpretation rather than erasing a correctly computed joint-endpoint result. In particular, do not describe a coordinated mechanism when nearly universal bilirubin increase contributes little predictive variation.

Repeat the locked construction at the inherited secondary window `(24h,48h]`, choosing the common timestamp nearest +36h (audit support 36/99), and rebuild its `P/H` variables against the same repeat event. This is a timing-specificity diagnostic, not a competing endpoint. If at least 75% of primary patients are retained and a favorable gain reverses sign, state that evidence is specific to the primary 12–36-hour panel. Never replace the primary with the secondary window. Do not run inferential alternatives at the infeasible 0–24-hour or 48–72-hour windows.

## Denominator and outcome-observation negative control

The primary `Y` estimand is explicitly conditional on the 131 episodes with complete required `B/P` panels and the fixed observed post panel. It does not target all 685 selected repeat events or even all 242 episodes with both `B` and `P`. Do not use inverse-probability weighting to manufacture unobserved event-aligned outcomes: the post-panel observation mechanism is not known to be missing at random, and a weighted selected sample cannot recover the 111 outcomes that were never measured.

Define the outcome-blind observation experiment before reading post-panel values. Its denominator is the 242 independently selected repeat-event episodes with both assays at `B` and both at `P`: 55 systemic-record and 187 comparator. Define `O=1` if and only if the valid uncensored common exact-timestamp post panel selected by the frozen `[12h,36h]`, nearest-+24-hour rule exists; otherwise `O=0`. Reproduce 34/55 and 97/187 observed outcomes. Report a no-sampling flow separately by arm from 159/526 selected events through both assays at `B`, both at `P`, assay-specific presence in the post window, common timestamp, valid uncensored selected panel, and assay-specific/shared intermediate history. Report Wilson 95% intervals for the arm-specific and pooled `O` rates. For `O=1` versus `O=0` in the 242 denominator, report missingness and distributions of arm, age, sex, event year, TACE2-to-repeat interval, P-panel timing, documented discharge opportunity, and each assay's intermediate availability/count/recency. Standardized differences are descriptive only.

Do not collapse the two assays' history process in this denominator. For assay `a`, define `H_any_a`, `logN_a=log(1+N_H,a)`, and `logR_a=H_any_a*log(1+R_hours,a/24)` from its own frozen `H_rows`. Define `HP_alb_down` and `HP_bili_up` by the same formulas used in the outcome experiment, but against the assay-specific `L`; set an assay's indicator and `logR` to zero only when that assay's `H_any=0`. Report all disagreements in `H_any`, `N_H`, or `L_time`; the audited count of one process mismatch in 242 must be reproduced but is not a failure because no assay is silently substituted for the other.

Fit the following outcome-observation negative control:

`G_process: O ~ BP_alb_down + BP_bili_up + arm + age + sex + event_year + TACE2_to_repeat_days + P_old_lead_hours + H_any_alb + logN_alb + logR_alb + H_any_bili + logN_bili + logR_bili + log_pre_event_encounter_days + opportunity36`

`G_value: G_process + HP_alb_down + HP_bili_up`

where `log_pre_event_encounter_days=log(1+pre_event_encounter_hours/24)` and `opportunity36=min(max(discharge_time-event_time,0),36)/36`. Both are identical context/process adjustments in the nested models, not numeric hepatic-history features. If either cannot be computed in any of the 242 episodes, report the missingness and run the parent-formula `G_process`/`G_value` models as the selection gate; label the encounter-augmented observation sensitivity context-inconclusive. Do not impute or discard episodes.

This contrast gives both models identical pre-event state, timing, assay-specific measurement-process information, and—when complete—encounter opportunity; only `G_value` receives numeric intermediate-history directions. Use five deterministic arm-and-`O`-balanced folds: within each arm x `O` cell, SHA-256 sort `hcc-repeat-tace-observation-v1|患者主索引` and assign rank modulo five. Use the same sex encoding, training-only standardization, fixed `lambda=1` logistic objective, optimizer requirements, and no-tuning rules as the `Y` models; additionally standardize numeric event year, `log_pre_event_encounter_days`, and `opportunity36` in training. Require both `O` classes in every training and held-out fold.

Define

`Delta_O = Brier(G_process) - Brier(G_value)`.

Report both pooled out-of-fold Brier scores, the training-prevalence null, log loss, prediction range/variance, and arm-stratified descriptive Brier scores. Run 500 outcome-blind linkage-destruction permutations with seed `20260912`: independently within assay, arm, and primary observation fold, permute `L` only among episodes with that assay's `H_any=1`, retaining each recipient's process variables, `B/P`, covariates, `O`, and fold; recompute the two `HP` indicators and refit both models. This preserves the one assay-process mismatch rather than forcing artificial paired histories.

The negative control **passes** only when `Delta_O<0.01` and observed `Delta_O` does not exceed the 95th percentile of its permutation distribution. It is **selection-entangled** if `Delta_O>=0.01` or exceeds that percentile. The 0.01 margin is a conservative locked diagnostic threshold, not a clinical threshold. A selection-entangled result does not prove that the `Y` gain is entirely artifactual, but it blocks an unqualified supportive prognostic conclusion because the same numeric feature helps select which outcome exists. A passed negative control does not establish missing at random, exchangeability, absence of selection bias, or recovery of missing outcomes.

The `M_obs` versus `M_hist` contrast addresses the complementary issue conditional on `O=1`: it prevents numeric intermediate history from being credited merely for whether, how often, or how recently clinicians measured the intermediate panel. Neither experiment repairs conditioning on repeat TACE, required `B/P`, or post-panel observation.

## Deterministic interpretation and falsification branches

Apply branches in this order.

1. **Reconstruction failure / negative feasibility.** Any source/hash/schema mismatch; unexplained failure to reproduce 319/1,491 pathways, 159/526 repeat events, parser/duplicate facts, 55/187 both-`B`/both-`P` denominator, 34/97 endpoint denominator, 23/63 events, 32/93 paired histories, one assay-process mismatch in the broader denominator, fold class support, or any key/clock/window violation. Stop; do not widen the window, alter the endpoint, or simplify filters to obtain a result.
2. **Computationally inconclusive.** Shared-history clocks disagree between assays among the 131 `Y` episodes; a required `Y` or `O` fold loses a class; required values are nonfinite; optimizer or prediction checks fail; more than one continuous feature is zero-variance in a fold; or fewer than 950 outcome-bootstrap replicates are estimable. Report feasibility only. The single expected assay-process mismatch among the 242 `O` episodes is handled by assay-specific variables and is not itself a failure. Missing/invalid encounter-opportunity variables or a non-estimable `C_direct=0` stress test make only their context sensitivity inconclusive: use the parent-formula observation gate and do not erase an otherwise computable primary result.
3. **Adverse predictive degradation.** Gates pass and the full-refit `Delta_Brier` 95% interval lies wholly below zero. Conclude only that adding these two history indicators worsened out-of-fold outcome prediction under the locked model; report `Delta_O` separately.
4. **Supportive prognostic evidence, context-qualified.** Gates pass; primary `Delta_Brier>=0.02`; the full-refit 95% interval lower bound is above zero; `M_hist` also beats the training-prevalence null Brier; observed gain exceeds the 95th outcome-linkage-permutation percentile; the result is neither partition- nor influence-sensitive; and the encounter-context-augmented outcome-observation negative control passes (`Delta_O<0.01` and not above its 95th permutation percentile). Conclude only that the prespecified intermediate-history directions add reproducible prognostic information for the fixed concordant directional transition in the selected observed-panel denominator without detectable numeric selection signal under the locked negative control. If the `C_direct=0` stress test is estimable and neither sensitivity condition is triggered, add “not detectably concentrated in high-specificity recorded albumin/blood-product/diuretic starts”; never call the endpoint hepatic deterioration or claim absence of unrecorded supportive-care contamination. If the stress test is context-inconclusive, say so. Add component-attributed and timing-specific qualifiers whenever triggered.
5. **Selection-entangled or recorded-care-context-sensitive favorable result.** If the outcome conditions for branch 4 otherwise pass but `Delta_O>=0.01` or exceeds its 95th observation-permutation percentile, report both gains and conclude that numeric intermediate history predicts outcome availability as well as the observed outcome, so the apparent outcome gain cannot be separated from observation selection with these data. Separately, if the primary gain otherwise passes but the estimable stress test has `Delta_Brier_no_direct<=0` or attenuation of at least 0.02, label it recorded-care-context-sensitive: the gain is concentrated in or materially altered by episodes with identifiable post-event supportive-care records. Neither condition proves that selection or care caused the result. Do not call the result unqualified supportive evidence, apply weighting, adjust for downstream care in the primary models, or infer that the measured signal exhausts peri-procedural contamination.
6. **Precise null for the design-sized outcome increment.** Gates pass, the outcome interval is not wholly below zero, and its upper bound is below +0.02. Rule out a 0.02 Brier improvement under this design and conditional uncertainty. Favor the smaller feature representation for this forecasting task only; do not recommend less clinical testing. Report the observation negative control independently.
7. **Small positive but below margin.** Outcome interval lower bound is above zero but point estimate is below 0.02, or the point estimate is at least 0.02 but partition/linkage/influence gates fail without adverse degradation. Report the measured increment and failed gate; do not claim the prespecified supportive result. If the observation negative control is selection-entangled, state that additionally.
8. **Inconclusive precision.** The outcome interval spans both zero and +0.02, or another locked ambiguity remains. State that the available 131 episodes cannot distinguish no outcome increment from the design-sized gain; report but do not use `Delta_O` to resolve that imprecision.

A precise null, adverse result, or inconclusive result is scientifically informative about this representation and endpoint. None licenses a monitoring-policy recommendation.

## Claim limits and verifier boundary

HCC lacks laboratory units/reference ranges/analyzer harmonization, analytical coefficient of variation, adjudicated hepatic decompensation or complications, Child–Pugh/MELD, tumour burden and radiographic response, TACE technical details/intent/success, verified albumin infusion/transfusion/fluid administration, fluid volume/rate, net balance, urine output, bleeding/infection, verified systemic-drug administration/adherence/dose, outside tests, complete follow-up, and reliable mortality. Recorded medication/order starts only partially describe peri-procedural workflow. The fixed early panel may reflect routine peri-procedural physiology, assay noise, supportive care, or patient selection. Conditioning on repeat TACE and on observed `B/P/post` panels can create selection/collider bias. Reusing `P` in predictors and outcome directions creates mathematical dependence that prediction validation cannot turn into pathophysiology.

A verifier can check source hashes and full scans, columns and composite joins, pathway/event reconstruction, parsing and duplicates, B/P/H/post clocks, the 55/187 and 34/97 denominator flow, assay-specific observation-process variables, encounter-opportunity variables, the literal supportive-care ontologies and exact-label/status/timestamp audits, fixed versus selected-panel context clocks, directional variables, both deterministic fold systems, training-only preprocessing, fixed-penalty fitting, paired `Delta_Brier`, `Delta_Brier_no_direct`, and `Delta_O`, full-refit outcome bootstrap, both linkage permutations, partition/influence/component/timing diagnostics, and branch precedence. It must reject conclusions that relabel crystalloid names as delivered fluid, placement as administration, absent records as absent care, or the context restriction as a causal effect. It cannot establish clinical deterioration, toxicity, causality, treatment benefit, utility, policy, missing-at-random assumptions, absence of selection bias after a passed negative control, absence of supportive-care contamination after a stable sensitivity, or transportability. Those claims require unit-validated assays, adjudicated outcomes and delivered supportive-care/exposure context, expert review, and an external or prospective study.

## What changed and what remains uncertain

Compared with `[prior hypothesis]`, this child (1) preserves the frozen population, exact `[12h,36h]` panel, `Y`, outcome prediction estimand, uncertainty, and separate 242-episode selection safeguards; (2) binds and completely scans the non-drug-order source in addition to medications and encounters; (3) demonstrates outcome-blind that broad blood/plasma and crystalloid string adjustment is clinically invalid, then freezes high-specificity albumin/blood-product/diuretic recorded-start definitions; (4) separates intended start from order placement, fixed +12/+24/+36 clocks from the observed-only pre-panel clock, and excludes explicitly void/cancelled non-drug orders; (5) adds a no-refit paired-contribution restriction that can label an otherwise favorable result recorded-care-context-sensitive without treating downstream care as a baseline confounder; and (6) adds admission-to-event and capped event-to-discharge opportunity symmetrically to both observation models while preserving the parent’s numeric-selection gate.

Uncertainty remains substantial because the denominator is selected and small, the outcome has no validated magnitude threshold, bilirubin increase is nearly ubiquitous, units and delivered supportive care are unavailable, crystalloid records are nonspecific, absence of a record is not absence of care, and all outcome-bearing model results remain uncomputed. The strongest possible result from this experiment remains context-qualified, noncausal prognostic information in the selected observed-panel cohort—not hepatic deterioration, treatment toxicity, or a care recommendation.
