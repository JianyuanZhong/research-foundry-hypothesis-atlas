> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 77 successor: a landmark-correct, uncensored seven-day queue with an eventual-death no-tradeoff guard

## Clinical decision, unresolved claim, and advance

At the end of the locked 24-hour reassessment window, a hospital can generate only a fixed number of silent review assignments. The decision studied here is whether optional repeat-lactate information that is already available by that landmark should be retained as a candidate prioritization signal for a prospective silent queue, beyond an otherwise identical model that represents late non-lactate surveillance. The modeled action is immediate allocation of the top 10% of eligible people within each hospital to review; the data contain neither the review nor any response to it.

The parent answers this question against eventual hospital-discharge death, which is complete but temporally unbounded. That endpoint cannot say whether any incremental queue yield is concentrated soon enough after the L24 assessment to define a clinically coherent review window. The prior seven-day successor tried to solve this by excluding everyone discharged after a horizon and also set “seven days after L24” to `t0+10080`, which is only six days after L24. This successor repairs the single substantive limitation—an unbounded decision horizon—without changing or subsetting the audited cohort. It uses the correct landmark-relative horizon, treats alive discharge as an observed competing state, retains people still hospitalized at H7 as observed D7 non-events, and requires that a near-term gain not trade away eventual-death capture in the same queue.

The falsifiable hypothesis is:

> In the frozen all-baseline/L24 EICU population, D7-targeted hospital-held-out `R_full` top-10%-within-hospital queues will capture at least 3 additional in-hospital deaths occurring within seven days after L24 per 100 fixed review slots compared with equal-capacity `R_attention` queues: the pooled `Delta7_slot` 95% lower bound will be at least +0.03, the corresponding lower bounds will be nonnegative in both frozen repeat-availability strata and in the equal-hospital macro estimand, the inherited deletion and 20%-capacity stresses will pass, and the same D7-fitted queue substitutions will have a nonnegative 95% lower bound for eventual hospital-discharge death capture.

The +0.03 margin and 10% capacity are inherited operational anchors, not stakeholder-elicited utilities. The seven-day horizon is a frozen prognostic horizon, not an asserted treatment-effect window. Support would justify independent prospective silent validation of this specific prioritization policy; it would not justify ordering a lactate, activating a clinical alert, or claiming preventable mortality.

## Existing evidence versus the claim under test

The strongest available evidence supports only the premise that late lactate and observation processes may carry prognostic information. I directly inspected the frozen full-text XML for Baysan et al. (2022; DOI `10.1097/CCE.0000000000000750`; PMCID `PMC9444407`; source ID `[source checksum]`; [source checksum]). It reports 4,440 critically ill adults with sepsis, 2,347 in-hospital deaths, a recalibrated APACHE IV C-statistic of 0.62 (95% CI 0.60–0.63), and 0.64 (0.62–0.66) after adding 24-hour lactate. That supports modest incremental prognostic information in a lactate-measured cohort; it does not establish optional-result value, surveillance-matched specificity, seven-day queue value, multicenter portability, ordering benefit, or patient benefit.

I also directly inspected the frozen full-text XML for Sisk et al. (2021; DOI `10.1093/jamia/ocaa242`; PMCID `PMC7810439`; source ID `[source checksum]`; [source checksum]). It defines informative presence/observation and reports that 24 of 36 reviewed articles used missing indicators or summary measures. This supports explicitly representing the observation process; it does not show that the locked surveillance summaries measure attention or remove confounding.

Thus the evidence-supported claim is only that lactate values and observation patterns can be prognostic. The unresolved claim tested here is whether optional lactate adds material, internally portable, near-term fixed-slot prioritization value after surveillance matching, without an eventual-death capture tradeoff. No published evidence inspected here establishes that exact claim or validates seven days as a treatment window. The horizon is justified below by clinical interpretability and an outcome-count-only feasibility audit, not by outcome-model performance. The three papers in `references/research-ambition/README.md` were treated as ambition demonstrations, not topic or method authorities; no claim is made that the unavailable cancer main article or full STAR Methods was inspected.

## Frozen population, t0/L24 clocks, and lactate resolution

Use every required source row; there is no person sampling. Chunking is memory management only. Record chunk sizes, coercions, exclusions, invalidated timestamps, collapsed duplicates, and flow counts. Keep all source files read-only and all person-level derivatives private in the workspace.

1. From `patient`, trim age strings, map only the exact literal `> 89` to 90, numerically coerce all other values without capping, and retain age >=18. Required fields are `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `gender`, `age`, `hospitalid`, `hospitaldischargeoffset`, and `hospitaldischargestatus`.
2. Among adult stays, identify `infusionDrug` rows whose case-folded `drugname` contains `norepinephrine` or `levophed` and whose `infusionoffset` is in the closed interval [0,1440] minutes. For each ICU stay, define `t0` as the earliest qualifying offset. This is a recorded infusion row, not adjudicated administration, indication, dose, or true drug start.
3. Per `uniquepid`, retain the lexicographically smallest `(t0, patientunitstayid)` pair. Define `L24=t0+1440`.
4. Require `hospitaldischargestatus` exactly `Alive` or `Expired` and finite `hospitaldischargeoffset>=L24`. Define `Dinf=1` for `Expired`, otherwise 0. This is the unchanged eventual hospital-discharge outcome and population boundary.
5. Baseline `B` is a `lab` row with trimmed/case-folded `labname=lactate`, trimmed/case-folded `labmeasurenamesystem=mmol/L`, finite `labresult` in [0.2,30], collection `labresultoffset` in [t0-360,t0], and `labresultrevisedoffset<=t0+60`. At each collection offset, keep the greatest eligible revision; invalidate a final-revision tie containing different numeric values and collapse identical final-revision ties to the smallest `labid`. Select the latest valid collection, breaking a remaining tie by smallest `labid`, and require `B>=2`.
6. Optional repeat `F` uses exactly the same analyte, unit, range, revision, conflict, and duplicate rules, with collection in [t0+720,L24] and revision by L24. Select the valid collection nearest `t0+1080`, then the earlier collection offset, then the smallest `labid`. Retain absence as `F_available=0`; revisions after L24 are unavailable.
7. Build this complete baseline/L24 population before any outcome modeling. Retain hospitals with at least 30 people and freeze that hospital set. Preserve the parent gates: at least 30 hospitals, 1,000 people, 200 eventual deaths, 200 eventual survivors, maximum hospital share <=15%, and both eventual outcome classes in at least 80% of hospitals.
8. Before outcome modeling, compute each retained hospital’s F availability in the complete population. Hospitals at or above the median are high availability; those below it are low availability. Freeze labels, and make bootstrap copies inherit their original hospital’s label. This is outcome-blind process stratification, not causal moderation.

The inherited and independently reproduced flow is 13,023 adult one-person early-pressor stays meeting the L24 discharge boundary, 3,117 with valid B>=2 before the hospital-size gate, and 2,302 people in 30 frozen hospitals after the gate: 779 eventual deaths and 1,523 eventual survivors. The inherited F count is 1,163. The F-measured subset must never replace the complete primary cohort.

## Landmark-correct outcome and feasibility audit

Set `H7=L24+10080=t0+11520` minutes. Define

`D7 = 1[hospitaldischargestatus == "Expired" and hospitaldischargeoffset <= H7]`.

Every one of the 2,302 frozen cohort members remains in fitting, queue construction, and evaluation:

- `Expired` with discharge offset <=H7 is death by H7.
- `Alive` with discharge offset <=H7 is observed alive discharge by H7, a competing event and D7=0.
- Any status-valid person with discharge offset >H7 is known from the source-relative clock not to have an in-hospital death by H7 and is D7=0, regardless of later discharge status. Such people are event-free and still hospitalized at H7; they are not “seven-day survivors” in a post-discharge or all-cause sense.
- Equality at H7 is included. No one is excluded for a discharge after H7, no inverse-censoring weight is used, and no post-L24 field enters a predictor.

This is seven-day in-hospital cumulative death incidence in the locked L24 risk set. It does not capture death after alive discharge, and `hospitaldischargeoffset` is an administrative discharge/death proxy rather than an adjudicated death timestamp.

A complete-source, outcome-count-only audit (`[research job]`; output [source checksum]) reproduced the parent flow before comparing horizons. At 3, 7, 14, and 28 days after L24 it found 436, 607, 706, and 767 deaths, respectively, capturing 56.0%, 77.9%, 90.6%, and 98.5% of the 779 eventual deaths. At H7 there are 1,695 D7 non-events: 611 alive discharges by H7 and 1,084 still hospitalized without death at H7, of whom 172 later die before hospital discharge. All 30 hospitals have both D7 classes; the minimum is 7 D7 events per hospital; maximum hospital share remains 7.34%. Seven days is frozen as a compromise: unlike three days it includes more than three quarters of eventual deaths while retaining a near-term review interpretation; unlike fourteen or twenty-eight days it does not move the primary window farther from L24. These are feasibility and endpoint-composition observations, not evidence that a review changes care.

Require at least 200 D7 events, 200 D7 non-events, both D7 classes in at least 80% of the already frozen hospitals, and both classes in every outer-fold training set. These are computability checks only; they do not remove people or redefine hospitals. The exact snapshot should reproduce 607/1,695. A discrepancy requires a documented mechanical source-version explanation and renewed gate review, never horizon shopping.

## Frozen predictors and four models

Fit the same four unweighted L2 logistic models, now to D7. Hospital ID, discharge fields, Dinf, diagnoses, treatments, F/B clearance, post-L24 information, outcome-derived features, and post hoc interactions or feature selection are forbidden.

`R_state` contains:

- age and age squared; Female and Male indicators, with Other/Unknown as reference;
- `t0/1440` and its square;
- baseline collection lag `(t0-B_offset)/360`;
- `ln(B)` and its square;
- for each locked non-lactate laboratory stream, its latest valid value in [t0,L24], age `(L24-offset)/1440`, and missing indicator; and
- for heart rate, respiration, and SpO2, the last, median, minimum, maximum, resolved-timestamp count, and no-valid-observation indicator in [L24-360,L24].

The exact trimmed/case-folded laboratory name | unit | hard range streams are: potassium | mmol/L | [1,10]; sodium | mmol/L | [100,180]; chloride | mmol/L | [50,150]; BUN | mg/dL | [1,300]; glucose | mg/dL | [20,1000]; creatinine | mg/dL | [0.1,20]; bicarbonate | mmol/L | [2,60]; calcium | mg/dL | [2,20]; Hgb | g/dL | [2,25]; platelets x 1000 | K/mcL | [1,2000]; WBC x 1000 | K/mcL | [0.1,500]; albumin | g/dL | [0.5,8]; total bilirubin | mg/dL | [0.1,50]; paO2 | mm Hg | [20,700]; paCO2 | mm Hg | [10,200]; pH | blank/missing unit | [6.5,8.0]. At each stream/collection offset require a finite in-range value revised by L24, retain the greatest eligible revision, invalidate differing final-revision ties, collapse identical ties to the smallest `labid`, and select the latest resolved timestamp for state.

For `vitalPeriodic`, use `observationoffset`; accept heart rate 20–250/min, respiration 2–80/min, and `sao2` 40–100%. Resolve each stream separately at each timestamp: differing valid values invalidate that stream/timestamp; identical ties collapse to the smallest `vitalperiodicid`. Counts are resolved timestamps, not export rows. These are five-minute summaries without order, entry, validation, display, or view timestamps.

`R_attention = R_state` plus six summaries from valid resolved non-lactate rows in [t0+720,L24], all revised by L24: `ln(1+routine marker-time pairs)` for the first 13 streams through total bilirubin; `ln(1+blood-gas marker-time pairs)` for paO2, paCO2, and pH; `ln(1+distinct labresultoffsets)` over all 16 streams; observed-stream fraction out of 16; recency `(L24-latest offset)/720`; and a no-qualifying-row indicator, with recency missing and training-imputed when none. Apply exactly the state unit/range/revision/conflict rules. These are surveillance proxies, not verified orders, concern, workload, or viewing.

`R_process = R_attention` plus `F_available`, F age `(L24-F_offset)/720` when available, and a missing-age indicator. `R_full = R_process` plus `ln(F)` and its square. Impute missing continuous F terms using training-fold preprocessing while retaining availability explicitly.

## Fixed-capacity estimands and paired algebra

Use leave-one-hospital-out D7 predictions. For each frozen hospital h with its unchanged complete-cohort size `n_h`, set `k_h=ceil(0.10*n_h)`. Rank each model’s held-out raw linear predictors within hospital; the top k_h form `Q_m,h`, breaking exact score ties by ascending `patientunitstayid`. Let `K=sum_h k_h`.

For outcome `o in {7, inf}`, let `D_i^7=D7_i`, `D_i^inf=Dinf_i`, `S_m,h^o=sum(D_i^o, i in Q_m,h)`, and `P_m,h^o=S_m,h^o/k_h`. The queues are learned for D7; Dinf only evaluates the same assignments.

The primary pooled workload estimand is

`Delta7_slot = [sum_h S_full,h^7 - sum_h S_attention,h^7] / K`.

Report `100*Delta7_slot` as additional seven-day in-hospital deaths captured per 100 fixed review slots. The materiality margin is +0.03. Prespecified portability estimands are `Delta7_macro=mean_h(P_full,h^7-P_attention,h^7)` and pooled `Delta7_slot` separately within the frozen low- and high-F-availability hospital strata.

The no-tradeoff guard is

`Deltainf_samequeue = [sum_h S_full,h^inf - sum_h S_attention,h^inf] / K`.

It evaluates eventual discharge deaths in exactly the D7-fitted, D7-ranked queues. It is not the parent’s eventual-outcome-trained policy, and must not be described as such.

For the shared queue substitutions define `A_h=Q_full,h\Q_attention,h`, `R_h=Q_attention,h\Q_full,h`, `s_h=|A_h|=|R_h|`, `M=sum_h s_h`, and `rho_swap=M/K`. For each outcome define `G_o=sum_h[sum_{i in A_h}D_i^o-sum_{i in R_h}D_i^o]` and, if M>0, `Psi_o=G_o/M`. Equal quotas require, separately for D7 and Dinf,

`Delta_o = G_o/K = rho_swap*Psi_o`, with `|Delta_o|<=rho_swap`.

Save and verify both identities. If M=0, both G values and both Delta values must be zero and both yields are undefined. Report M, K, rho, both G values, addition/removal event proportions for both outcomes, hospitals with substitutions, and the distribution of `s_h/k_h`. Never use either yield to rescue or veto its fixed-slot contrast, and never report yield without M/K. Costs of changed assignments and benefits of review are unavailable.

Required secondary analyses, all labeled exploratory or descriptive, are D7 slot contrasts `R_full-R_state` and `R_process-R_attention`; D7 capture fraction `C_m=sum_h S_m,h^7/sum_i D7_i`; conditional measured-population `R_full-R_process` after refitting both only among F-measured people with new within-hospital 10% quotas; queue overlap, additions/removals, D7 true/false positives, sensitivity, unflagged deaths, exact score ties, and switch fractions by hospital; the three-state H7 composition (death, alive discharge, still hospitalized event-free) in every queue and among additions/removals; and all slot/decomposition quantities at 20% capacity with `ceil(0.20*n_h)`. None can rescue the 10% primary.

## Hospital-held-out fitting

For each outer hospital and each of the four models, exclude that hospital completely. In the remaining hospitals only, winsorize continuous predictors at training 1st/99th percentiles, standardize using the training mean and population SD, then mean-impute missing continuous values to zero after scaling; do not scale binary indicators. Fit logistic regression with intercept, L2 penalty, `C=1`, `lbfgs`, `max_iter=10000`, `tol=1e-8`, no class weighting, and seed 20260973. Score only the excluded hospital using its training constants. No feature may be dropped. No finite training values, zero post-winsorization variance, nonconvergence, or nonfinite prediction makes the required model noncomputable.

Use raw linear predictors for ranking. Probabilities are descriptive only for AUROC, Brier score, log loss, and calibration plots; do not call them clinically calibrated or use threshold decision curves. Save feature order, fold constants, convergence, deterministic state, and one score and queue indicator per person/model.

## Copied-hospital uncertainty and stability

Use 2,000 copied-hospital refit bootstrap replicates with seed 20260973. Sample original hospitals with replacement. Copies contribute copied evaluation rows and training weight, but all copies of one original hospital remain one exclusion group: no prediction for an original hospital may be trained on any copy of it. Repeat preprocessing, four D7 fits, predictions, unchanged within-copy quotas, primary pooled/macro/stratum estimands, the same-queue eventual guard, paired decompositions, and the 20% analysis.

Within every replicate save the joint tuple `(K,M,rho,G7,Delta7,Psi7,Ginf,Deltainf,Psiinf)`; enforce both identities when M>0 and zero-G/zero-Delta/missing-yield rules when M=0. Use percentile 95% intervals. Require at least 1,900 finite replicates for pooled Delta7, Delta7_macro, both D7 stratum contrasts, and Deltainf_samequeue. Report a yield interval only if at least 1,900 replicates have M>0; otherwise label it `yield denominator-fragile`, report the zero-substitution fraction, and do not impute or continuity-correct yield. Yield fragility alone does not make fixed-slot contrasts noncomputable.

For fixed-design leave-one-original-hospital deletion, delete one evaluation hospital from already held-out predictions without refitting and recompute pooled, macro, stratum, same-queue eventual, and swap quantities. Support requires Delta7>0 in at least 80% of finite pooled deletions, at least 70% in each availability stratum, and at least 70% of macro deletions. Report eventual-guard deletion signs descriptively and whether any hospital dominates slots, D7 deaths, eventual deaths, G7, Ginf, or M.

## Ordered result states and action interpretation

Apply the first matching state. Neither swap yield changes the state.

1. **Not computable.** Source/header/hash mismatch; undocumented failure to reproduce the frozen flow or horizon audit; a missing key/clock; incorrect one-person, unit, range, window, revision, conflict, duplicate, H7, competing-state, or D7 rule; any H7-based exclusion; a failed population/outcome gate; hospital leakage; altered features; incomplete predictions/quotas; nonfinite/nonconverged required fits; or fewer than 1,900 finite bootstrap replicates for a required fixed-slot contrast. Do not substitute a person-random split, measured-only primary, different horizon, survival-status recoding, or post-L24 predictor.
2. **Supportive for near-term fixed-slot prognostic value without observed eventual-capture tradeoff.** Pooled Delta7 lower 95% bound >=+0.03; low- and high-availability Delta7 lower bounds >=0; Delta7_macro lower bound >=0; deletion proportions meet 80%/70%/70%; 20%-capacity pooled Delta7 upper bound >=0; and Deltainf_samequeue lower bound >=0. This supports only that the locked optional-lactate queue captures at least three additional source-defined seven-day in-hospital deaths per 100 equal slots, with no detected loss of eventual-death capture, in this snapshot. The next action is independent prospective silent validation with verified result visibility and measured queue workflow—not test ordering or live deployment.
3. **Adverse: opposite near-term direction.** Pooled Delta7 upper bound <0, or both availability-stratum upper bounds <0. The locked optional-lactate queue worsens near-term death capture for this estimand; do not advance this policy.
4. **Adverse: near-term gain trades away eventual capture.** Pooled Delta7 lower bound >=+0.03 but Deltainf_samequeue upper bound <0. The D7-targeted substitutions enrich early deaths while losing eventual deaths at equal capacity; the joint hypothesis is falsified.
5. **Adverse: surveillance-explained materiality.** The naive `R_full-R_state` D7 contrast has lower bound >=+0.03 but primary `R_full-R_attention` upper bound <+0.03. Materiality does not survive the surveillance-matched comparator; this does not prove surveillance caused the naive association.
6. **Adverse: below materiality.** Primary Delta7 upper bound <+0.03. This rejects the locked three-per-100 near-term claim while allowing a smaller association.
7. **Adverse: internally nonportable.** Pooled Delta7 lower bound >=+0.03, but either availability stratum or Delta7_macro has upper bound <0, or the 20%-capacity pooled upper bound <0. A pooled gain is directionally contradicted in a prespecified site/process or capacity stress.
8. **Inconclusive.** Every other computable pattern, including an interval crossing +0.03; pooled materiality with macro/stratum intervals crossing zero; a Deltainf_samequeue interval crossing zero; failed deletion stability without an adverse interval; or favorable point estimates lacking required bounds. Inconclusive cannot support deployment and cannot be rescued by another horizon, swap yield, three-state composition, or a secondary model.

Attach only the parent’s descriptive mechanism labels: `numeric component supported` if the conditional measured-population numeric contrast lower bound >0; `process-dominant pattern` if the process point estimate is at least the full-primary point estimate or the numeric upper bound <=0; otherwise `numeric/process unresolved`. They are noncausal and do not alter the ordered state.

## Exact sources, schemas, joins, clocks, and archive members

The inspected full catalog is `[internal dataset path]`, [source checksum]. It exposes all configured HCC (12 sources), MIMIC (5), EICU (31), and UKB (8) sources read-only. They remain directly accessible, including permitted rows and notes. This experiment uses only EICU because no validated cross-dataset person key or harmonized early-pressor, revision-aware lactate availability, L24 clock, and seven-day in-hospital outcome definition exists. The EICU snapshot is `[source checksum]`; its catalog convention states that offsets are minutes relative to ICU admission.

The four required sources are gzip CSV streams, not multi-member archives; each schema records `member=null` (guide: ordinary file). I directly inspected every live CSV header and the linked schema:

- **patient** — `datasets/eicu/table-ab037c09d7df9a3c.json`, schema [source checksum]; source `[internal dataset path]`, source [source checksum]. Required columns: `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `gender`, `age`, `hospitalid`, `hospitaldischargeoffset`, `hospitaldischargestatus`. `hospitaldischargeoffset` supplies the L24 population boundary, H7 competing-state classification, and eventual outcome.
- **infusionDrug** — `datasets/eicu/table-18e1a8caaa91eb44.json`, schema [source checksum]; source `[internal dataset path]`, source [source checksum]. Required columns: `infusiondrugid`, `patientunitstayid`, `infusionoffset`, `drugname`; `infusionoffset` defines t0.
- **lab** — `datasets/eicu/table-79bdb33275339b1a.json`, schema [source checksum]; source `[internal dataset path]`, source [source checksum]. Required columns: `labid`, `patientunitstayid`, `labresultoffset`, `labname`, `labresult`, `labmeasurenamesystem`, `labresultrevisedoffset`; collection clock `labresultoffset`, revision/availability proxy `labresultrevisedoffset`.
- **vitalPeriodic** — `datasets/eicu/table-a22c6d6981a32279.json`, schema [source checksum]; source `[internal dataset path]`, source [source checksum]. Required columns: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `sao2`, `heartrate`, `respiration`; clock `observationoffset`.

Join `infusionDrug`, `lab`, and `vitalPeriodic` to `patient` on `patientunitstayid`. Use `uniquepid` only for one-person selection. Use `hospitalid` only for the frozen gate, folds, quotas, availability strata, copied-hospital exclusion groups, and deletion diagnostics; it is never a predictor. `patienthealthsystemstayid` is retained for audit only and is not substituted for the specified person or stay keys.

## Evidence limits, required future data, and verifier boundary

Structured EICU data can compute source-relative eligibility, H7 and its three administrative states, D7/Dinf, four D7 risk scores, equal-capacity queues, substitutions, fixed-slot contrasts, and internal uncertainty. It cannot establish why lactate was ordered, specimen type or quality, actual infusion delivery or indication, result release/display/view time, whether a reviewer saw or acted on a queue, clinician concern, workload, treatment response, post-discharge death, exact clinical death time, cause or preventability of death, patient harm, switching cost, fairness, causal benefit, or external transport. Calendar period is unavailable for temporal transport testing.

Clinical informatics review must adjudicate whether `labresultrevisedoffset<=L24` is a defensible availability proxy and whether discharge offset/status represent the intended endpoint. Clinical review of records would be required to judge actionability and preventability. A prospective silent study needs order, specimen, verified release/display/view, queue generation and review timestamps, review action, treatment, workload, competing discharge, post-discharge vital status, and patient-centered outcome times. Stakeholders must set review capacity and utilities. Only after silent external validation should an impact study—preferably randomized if the policy changes care—test safety or patient benefit.

Harbor must retain private row-level eligibility, feature, score, queue, substitution, and three-state files and publish only permitted aggregates plus source/header/hash manifests, exact flow/filter logs, revision/conflict audits, horizon composition, feature/fold manifests, convergence, queue cells, bootstrap tuples, intervals, deletions, and a structured conclusion linked to computed fields.

The automatic verifier can recompute source hashes/headers, population, clocks, revision and tie handling, H7, D7/Dinf, feature blocks, LOHO fits, quotas, queues, both outcome-specific G/Delta/Psi identities, copied-hospital intervals, deletion proportions, and the first matching result state. It must reject H7=`t0+10080`, exclusion of post-H7 discharges, calling all D7=0 people survivors, outcome leakage, unequal queues, a `2M` denominator, sign/algebra errors, yield without M/K, and correct numbers paired with unsupported causal or action claims. Fixtures must include valid supportive, opposite, horizon-tradeoff, surveillance-explained, below-margin, internally nonportable, inconclusive-eventual-guard, zero-swap, denominator-fragile-yield, and noncomputable cases. It cannot automatically establish clinical visibility, endpoint validity, actionability, preventability, utility, fairness, safety, causality, or transportability.
