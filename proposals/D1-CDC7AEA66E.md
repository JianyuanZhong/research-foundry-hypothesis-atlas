# Safety-net decision stress for fixed-capacity lactate-by-measured-perfusion prioritization

## Status, parent and scientific deliverable

This is a substantive child of the assigned valid observation-era successor `[prior hypothesis]`. It preserves that parent’s exact first eligible live ICU-exit cohort, one-hour availability buffer, 12-hour dual clinical/store-time window, lactate-by-measured-perfusion phenotype, R/D/S/N/U competing endpoint, legacy/bridge/contemporary observation-era transport, support gates, matched B1/Bdisc/Bmask comparison, M2 learned sensitivity, fixed-capacity queue evaluation, uncertainty, process falsifications and noncausal limits.

The new uncertainty is a policy stress rather than another era or care-unit subgroup:

> When an operational monitoring team must reserve half of a 10% review queue for the order-blind baseline’s highest-risk patients, does the lactate-by-measured-perfusion phenotype still rescue clinically important additional first R/D transitions using only the remaining capacity?

This asks whether the signal is a deployable adjunct to an existing triage safety net, not merely whether its unconstrained global ranking is better. It is distinct from the parent’s question of whether an era-blind model transports from L+B to C.

The future solver must newly fit the unchanged parent models and the parent’s L+B-to-C transport models, then construct the prespecified two-stage safety-net policy from frozen predictions. It must produce held-out historical and contemporary policy tables, paired uncertainty, rescue composition, process diagnostics, and a conclusion ledger—or a complete fixed-gate audit showing that the policy estimand is not estimable. No fitted clinical result is claimed in this proposal.

Completion is established by:

1. a source/schema/dictionary manifest and unchanged parent cohort-flow, live-exit, feature-coverage and endpoint audit;
2. a deterministic subject-level split and an era-blind L+B development manifest showing that no C outcome, policy queue or post-landmark field entered fitting;
3. the unchanged parent B1, Bdisc, Bmask and M2 predictions on the identical held-out L and C targets;
4. the new safety-net queues, exact queue sizes, baseline-reserved slots, phenotype-filled slots, overlap and rescue counts;
5. 24/48-hour competing-risk calibration and R/D/S/N/U outcome tables for global B1, global Bdisc, safety-net Bdisc, and random allocation;
6. paired subject-bootstrap intervals for safety-net gain, global-versus-safety-net attenuation, R/D-specific capture and rescue yield;
7. process-shift, overlap, permutation and feature-ablation falsifications; and
8. a conclusion ledger that links every claim to a computed output and labels clinical questions requiring adjudication or a prospective study.

A failed policy gate does not authorize changing the 50:50 reservation, queue workload, population, t0/tL, outcome, era cut, coverage rule or threshold.

## Unresolved question, evidence boundary and clinical importance

The expert seed `[starting question]` proposes that persistent hyperlactatemia may have different meanings when perfusion is improving versus worsening, while explicitly warning that repeated measurement is selective and these proxies cannot diagnose microcirculatory dysfunction. The parent operationalizes that hypothesis and tests observation-era robustness. Neither the seed nor the parent supplies a fitted result.

The strongest available evidence is feasibility and design evidence only:

- the configured MIMIC-IV 3.1 snapshot exposes ICU boundaries, admissions, repeated lactate and MAP observations, vasoactive intervals, organ laboratory values, transfers, and death/discharge fields;
- the local archive/header and dictionary audit verified the required members, schemas, selected item labels, links and units;
- the parent’s bounded join found 76,253 adult first eligible live exits before its strict feature gate across the five `anchor_year_group` values;
- local metadata records patient-specific timestamp shifts and invalid cross-subject raw-calendar alignment; `anchor_year_group` is therefore an observation-era proxy, not exact calendar transport.

This establishes neither the prevalence nor the predictive or clinical value of the phenotype. There is no result yet supporting an association, a queue gain, a transport claim, or a useful policy.

The clinical importance is operational. A monitoring service commonly has a pre-existing high-risk list and cannot review every patient. A phenotype that only helps when it can replace the baseline queue may be unusable where safety-net rules reserve capacity for conventional risk. Conversely, if it improves capture among patients outside the baseline reserve, it supports a prospective silent-mode test of an adjunctive workflow. The policy stress makes the unresolved signal clinically interpretable without claiming that review, monitoring, treatment, escalation or discharge changes outcomes.

## Falsifiable hypothesis and estimands

For each held-out target era (e\in\{L,C\}), let (N_e) be the strict-gated subjects with known first-transition labels, (K_e=\lceil0.10N_e\rceil), and (k_e=\lceil0.50K_e\rceil). Let (A=R\cup D) be first R/D transitions in ((t_0,t_0+48h]), with S competing. Scores are the predicted 48-hour R/D CIFs from models frozen before target outcomes are accessed.

- **Global baseline queue B1:** the top (K_e) by B1 score.
- **Global phenotype queue Bdisc:** the top (K_e) by Bdisc score.
- **Safety-net Bdisc policy (P_{SN}):** reserve the top (k_e) by B1 score; among subjects not reserved, fill the remaining (K_e-k_e) slots by descending Bdisc score. There is no duplicate selection. All ties use descending score then ((subject_id,hadm_id,stay_id)).
- **Random benchmark:** uniform deterministic-seed allocation of (K_e) subjects, repeated for the prespecified randomization uncertainty summary.

Define (mathrm{Cap}_{10,e}(Q)=K_e^{-1}\sum_{i\in Q}1(A_i=1)). Report event sensitivity, PPV/capture, false negatives, R capture, D capture, S counts, N counts and U counts. Also report the number and proportion of (P_{SN}\setminus B1) subjects with A, R and D events; these are the policy’s phenotype-enabled rescues.

The primary new estimands are:

[
\Delta_{SN,e}=\mathrm{Cap}_{10,e}(P_{SN})-\mathrm{Cap}_{10,e}(B1)
]

and

[
\Lambda_e=\mathrm{Cap}_{10,e}(P_{SN})-\mathrm{Cap}_{10,e}(Bdisc).
]

The primary hypothesis is that the safety-net adjunct retains clinically meaningful value in both the historical internal target and the contemporary transport target:

1. (Delta_{SN,L}\ge 0.03) and (Delta_{SN,C}\ge 0.03), with two-sided subject-bootstrap 95% intervals wholly above 0.03; and
2. (Lambda_L\ge-0.03) and (Lambda_C\ge-0.03), with intervals wholly above -0.03.

The 0.03 threshold means at least three additional known first R/D transitions per 100 reviewed under the safety-net policy; it is an operational effect threshold, not a claim about patient benefit. The -0.03 bound asks whether reserving half the queue sacrifices no more than three percentage points of global phenotype ranking. The parent’s G5/G10/G20 global queue criteria remain reportable and are not replaced.

A policy result can therefore be:

- supportive if both eras pass both criteria, with no material target calibration degradation and no comparable Bmask safety-net gain;
- adverse if either target’s safety-net gain is zero/negative, its lower interval is below 0.03, safety-net attenuation is below -0.03, R/D capture reverses, calibration degrades materially, or Bmask reproduces the rescue;
- inconclusive if either target gate fails, U exceeds the fixed limit, event support/overlap is inadequate, bootstrap is unstable, or intervals cannot distinguish the prespecified thresholds.

A positive result supports only an observed, fixed-capacity adjunctive ranking signal under an MIMIC observation-era proxy. It does not support causal benefit, clinical utility, net benefit, preventability, clinician intent, treatment response, microcirculatory diagnosis, or a recommendation to alter monitoring. The policy is retrospective and uses outcome labels only for evaluation.

## Population, live-exit timing and endpoint

Use adults in MIMIC-IV 3.1 at the first eligible ICU stay in each admission, selected before measurement coverage, phenotype, outcome, era, split or model calculation:

- Join `icu/icustays` to `hosp/admissions` on ((subject_id,hadm_id)), and to `hosp/patients` on `subject_id).
- Require `anchor_age >= 18), retaining MIMIC’s `anchor_age=91) representation.
- Within each `hadm_id`, sort by ((outtime,intime,stay_id)) and choose the first row with valid `intime < outtime), matching adult patient/admission, and at least 13 hours of ICU history.
- Require a known live exit at (t_0=outtime): nonmissing `deathtime > t_0), or null `deathtime` with `hospital_expire_flag=0). No later stay is substituted after a feature, endpoint or support failure.
- Set (t_L=t_0-1) hour. Use only observations with clinical time and store time no later than (t_L). The primary 12-hour feature window is ([t_0-13h,t_L]), split into ([t_L-12h,t_L-6h)) and ((t_L-6h,t_L]). This exact live-exit timing is unchanged by the safety-net policy.
- The 48-hour endpoint in ((t_0,t_0+48h]) is the first later ICU stay in the same admission (R), timed death (D), or alive discharge with `hospital_expire_flag=0) (S). N is known event-free follow-up. U is unresolved first-transition ascertainment. Ties are ordered D before R before S and all tied candidates are retained according to the parent’s rule. U is never assigned to N.

Use the parent’s prespecified observation eras from `hosp/patients.anchor_year_group): L = 2008–2013 labels, bridge B = 2014–2016, and C = 2017–2022 labels. The primary policy stress is evaluated in held-out L and C; B is descriptive. Develop on L+B and freeze before scoring C. The era variable is excluded from all model predictors in the transport fit.

## Exact read-only source bindings

Source catalog: `[internal dataset path]`, [source checksum].

Primary read-only archive: `[internal dataset path]`, 10,551,747,784 bytes, [source checksum]. Archive members are listed exactly below. The source remains read-only; derived manifests and results are written only to the workspace.

| role | local table metadata / archive member | join keys and time fields | required columns/items |
|---|---|---|---|
| index ICU and first/next stays | `datasets/mimic/table-7d5c8feb0fb0dbd4.json` / `mimic-iv-3.1/icu/icustays.csv.gz` | ((subject_id,hadm_id)), `stay_id`; `intime,outtime` | `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los` |
| admission, live/death/discharge endpoint | `datasets/mimic/table-e8ec3e6e4c428559.json` / `mimic-iv-3.1/hosp/admissions.csv.gz` | ((subject_id,hadm_id)); `admittime,dischtime,deathtime,edregtime,edouttime` | `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag` |
| patient and era | `datasets/mimic/table-9154f8c46cade9af.json` / `mimic-iv-3.1/hosp/patients.csv.gz` | `subject_id`; `anchor_year,dod` | `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod` |
| MAP | `datasets/mimic/table-8208609a785ea7e8.json` / `mimic-iv-3.1/icu/chartevents.csv.gz` | `stay_id); `charttime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; items 220052, 220181, 225312 |
| vasoactive intervals | `datasets/mimic/table-d193e854c19eb4ba.json` / `mimic-iv-3.1/icu/inputevents.csv.gz` | `stay_id); `starttime,endtime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,patientweight,totalamount,totalamountuom,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate`; pressor items 221906, 222315, 221289, 229617, 221749, 229630, 229631, 229632, 221662, 221653, 221986 |
| Foley process measure | `datasets/mimic/table-a7ad1c4cdcdbfe0a.json` / `mimic-iv-3.1/icu/outputevents.csv.gz` | `stay_id`; `charttime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valueuom`; item 226559 |
| lactate and organ labs | `datasets/mimic/table-bf701d962c63287c.json` / `mimic-iv-3.1/hosp/labevents.csv.gz` | ((subject_id,hadm_id)); `charttime,storetime` | `labevent_id,subject_id,hadm_id,specimen_id,itemid,order_provider_id,charttime,storetime,value,valuenum,valueuom,ref_range_lower,ref_range_upper,flag,priority,comments`; lactate 50813; organs 50861, 50878, 50885, 50912, 50882, 51222, 51265, 51300 |
| time-local transfer audit | `datasets/mimic/table-685b6b74d0d7c547.json` / `mimic-iv-3.1/hosp/transfers.csv.gz` | ((subject_id,hadm_id)); `intime,outtime` | `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime` |

Dictionary bindings are read-only and must be verified before extraction:

- `icu/d_items`, `mimic-iv-3.1/icu/d_items.csv.gz`, local metadata `datasets/mimic/table-d1023acc404fd1d4.json`, columns `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue`. The verified labels/units are MAP: 220052 “Arterial Blood Pressure mean”, 220181 “Non Invasive Blood Pressure mean”, 225312 “ART BP Mean”, all mmHg and linked to `chartevents); pressors: 221906 norepinephrine, 222315 vasopressin, 221289 epinephrine, 229617 epinephrine, 221749 phenylephrine, 229630/229631/229632 phenylephrine formulations, 221662 dopamine, 221653 dobutamine, 221986 milrinone, linked to `inputevents`; Foley 226559, mL, linked to `outputevents`.
- `hosp/d_labitems`, `mimic-iv-3.1/hosp/d_labitems.csv.gz`, local metadata `datasets/mimic/table-57ae65f0eb6cf1a6.json`, columns `itemid,label,fluid,category`. Lactate 50813 is “Lactate”, blood, Blood Gas. Organ items are ALT 50861, AST 50878, bilirubin 50885, creatinine 50912, bicarbonate 50882, hemoglobin 51222, platelet 51265 and WBC 51300; all blood laboratory dictionary entries.

The relevant table metadata files and full MIMIC README are part of the local evidence. The separate note files are available but excluded. MIMIC-CXR images, raw waveforms, measured microcirculation, measured GFR, fluid responsiveness, clinician intent, rescue completeness and external validation are unavailable.

## Feature construction and phenotype

Use the parent’s exact construction:

- Lactate P: both six-hour half medians of finite 50813 values are defined and at least 2.0 mmol/L. NL: both are defined and at least one is below 2.0.
- Perfusion I: late MAP minus early MAP >=5 mmHg and late unioned target-pressor minutes no greater than early minutes.
- Perfusion W: MAP change <=-5 mmHg and late unioned target-pressor minutes no less than early minutes.
- Other phenotype combinations are indeterminate and retained descriptively, not silently assigned.
- Coverage in each half requires at least one valid lactate, at least two valid MAP observations at distinct clinical timestamps, and one positive-duration pressor interval. Absence of a pressor row is not zero exposure.
- Collapse selected same-`(stay_id,charttime)` MAP duplicates by median; collapse exact-repeat pressor rows and union overlapping valid intervals. Require valid clinical intervals and `storetime<=t_L). Retain rejected/delayed/unit, duplicate/overlap, count, availability and chart-to-store-lag fields.

All parent B0/B1/Bmask/Bdisc/M2 variables are frozen. B1 is the simple order-blind baseline with the same 12 one-hour-bin summaries, organ/process fields and admission context but no phenotype interactions. Bdisc is the transparent phenotype alternative with frozen P/NL and I/W terms, early/late values, changes, interactions, organ values and availability indicators. Bmask retains context, missingness, counts, test presence and observation intensity while removing physiologic values. M2 is a small masked chronological GRU over the same 12 bins, masks, process indicators, context and frozen phenotype flags, predicting discrete-time competing R/D/S hazards. The learned model is a sensitivity alternative, not a required confirmation of biology.

## Split, fitting and policy evaluation

For the parent and transport fits, split subjects—not rows or stays—deterministically 70/15/15, stratified only by primary phenotype cell, endpoint label and original five-level `anchor_year_group`. Fit and preprocess on train; use historical validation only for model choice, regularization and early stopping. For transport, development is L+B and target C. Exclude `anchor_year_group` from all transport predictors. Freeze predictions before reading C outcomes or constructing any test policy table.

Evaluate the policy on the same untouched historical test and contemporary C target used by the parent. For each target, calculate (K=\lceil0.10N\rceil) and (k=\lceil0.50K\rceil) from target size before outcomes are inspected; predictions, not labels, determine membership. Use the exact tie-break rule above. Do not tune the 50:50 reservation, 10% workload, policy thresholds, era cut, phenotype cutoff or endpoint after seeing outcomes.

The policy estimand is not a treatment effect. It is a fixed-capacity ranking contrast under a hypothetical review allocation. Report all policies on identical subjects and identical label definitions. Repeat 5% and 20% global queues as parent sensitivities, but do not redefine the primary safety-net policy at those workloads. Report policy overlap, baseline-reserved event capture, phenotype-filled event capture, newly rescued R/D events and missed events.

Support gates for the new policy:

- Each primary L and C target has at least 90 strict known-label subjects, at least 10 known A events, (K\ge10), and U <=10% in the corresponding all-eligible audit.
- Each target has at least (K-k) subjects outside the reserved baseline set and at least 5 known A events outside that set; otherwise the rescue estimand is inconclusive.
- Each target has at least 10 subjects in the B1-reserved portion and at least 10 in the phenotype-filled portion after deduplication. If a deterministic small target cannot satisfy these, report descriptive values only.
- Parent cell gates and event gates are preserved for phenotype/era interaction claims: at least 40 subjects per primary cell, at least 10 known R/D events per cell, at least 8 test subjects and 3 known R/D events per test cell, U <=20%. These do not substitute for the policy gates.
- Report effective sample size/overlap and bootstrap failures. Poor overlap can make the policy interpretation inconclusive even if a point estimate is positive.

For each policy and target, calculate 24/48-hour cause-specific hazards and Aalen–Johansen CIFs with S competing, calibration intercept/slope, O:E and Brier score. A calibration slope outside [0.80,1.25] or absolute intercept >0.10 is material calibration degradation and blocks a calibrated risk-estimation claim, but does not alone erase a ranking result. Use subject-clustered bootstrap within fixed partitions, identical resamples for paired policies, and 95% intervals for (Delta_{SN,e}), (Lambda_e), R/D capture, PPV, rescue yield and policy overlap. Report favorable/adverse U bounds; never relabel U as N.

## Falsification and interpretation

Run all parent falsifications and add these policy-specific checks:

1. Recompute (P_{SN}) from Bmask rather than Bdisc. A similar Bmask rescue gain indicates documentation/measurement intensity, not a specific lactate-perfusion signal.
2. Permute outcomes within era and fixed split while preserving score and availability distributions. Safety-net gains should collapse toward the random benchmark.
3. Permute early/late bins and repeat exact policy construction. A persistent gain would weaken the trajectory/phenotype interpretation.
4. Use a negative-control safety-net policy that reserves half the queue for a process-intensity model, then compare Bdisc’s incremental rescue over that policy.
5. Repeat MAP-only, pressor-only, arterial-MAP-only, Foley-only and lactate threshold 4.0 variants; these are sensitivities, not alternate primary hypotheses.
6. Audit all ranking ties, queue counts, target membership, duplicate subject/stay exclusion, no same-subject split overlap, no clinical/store time after (t_L), and no outcome use in reserve/fill decisions.
7. Report process distributions by era and policy stratum: lactate/MAP/pressor availability, distinct MAP timestamps, positive pressor minutes, store-time lag, Foley charting, measurement counts, phenotype-cell occupancy, first/last careunit and transfer-careunit distributions. These describe the record process and are not confounder adjustment.
8. Recompute policy results at 5% and 20% global capacity only as predeclared sensitivity checks; the primary safety-net result remains 10% with 50% reserve.
9. Perform outcome-free q overlap diagnostics by target using baseline/context, care-unit context and 12-hour counts/masks/process intensity available at the control time; q is diagnostic, not causal correction.

The safety-net hypothesis is supported only when both target policy gates pass, (Delta_{SN,L}) and (Delta_{SN,C}) meet the 0.03 interval rule, (Lambda_L) and (Lambda_C) meet the -0.03 rule, calibration is not materially degraded, and Bmask/process controls do not reproduce the gain. It is adverse under the prespecified failures above. It is inconclusive under sparse target/cell support, U above limits, unresolved source units/joins, inadequate overlap, bootstrap instability or intervals too wide to distinguish the thresholds.

A supportive result means the phenotype appears to add observed first-transition capture as a safety-net adjunct under two MIMIC observation regimes. An adverse result means the global ranking result is not operationally robust when baseline triage is protected, or is likely process-driven if Bmask reproduces it. An inconclusive result means the configured records cannot resolve this policy uncertainty. None establishes patient benefit or justifies clinical deployment.

## Transparent baseline, learned alternative and method choice

B1 is required because it is the simplest order-blind comparator and defines the existing triage safety net. Bdisc is selected as the primary scientific alternative because its terms are auditable and make the phenotype’s incremental rescue and R/D components inspectable under the exact policy. M2 is a scientifically substantive learned alternative on the same inputs, target, split, outcomes and queue policy. It can reveal nonlinear, order-dependent coupled lactate/MAP/pressor trajectories that B1/Bdisc’s fixed summaries may lose; if its safety-net rescue differs, that is representation evidence, not mechanistic evidence.

A two-component diagonal-covariance trajectory mixture over the same training-only change vector is deferred unless a pre-outcome M2 implementation/stability audit fails or per-bin density is unusable. A full transformer is deferred because it adds capacity without a distinct clinical uncertainty and would make the policy interpretation less auditable. A fluid/treatment-effect model is deferred because the archive lacks clinician intent, fluid responsiveness, valid counterfactual treatment assignment and adequate time-varying confounding control. No deferred model can be selected based on target outcomes.

The method decision record contains the exact inputs, target, split, evaluation, baseline comparison and compute estimate:

- B1/Bdisc/Bmask: 12 one-hour-bin clinical/store-safe values, masks, process counts, organ labs, context and frozen phenotype fields as specified above; target is competing R/D/S hazards and 48-hour R/D CIF; subject-level historical train/validation/test and L+B-to-C transport; CPU tabular fits expected within the future solver envelope.
- M2: the same 12-bin tensor and target, small masked GRU, train only on historical L+B, same target-era queue and bootstrap/calibration evaluation; one allocated A100 is optional, using `cuda:0`, but CPU feasibility remains a valid fallback.
- Measured discovery resources: the bounded archive/header/dictionary and pre-gate eligibility audit ran in approximately seven seconds. Strict feature coverage, full event support, policy support, model stability, bootstrap time and GPU necessity remain unmeasured. The future solver planning envelope remains 16 CPUs, 262,144 MiB memory, up to 8 GPUs and 28,800 seconds; discovery limits are 7,200 science seconds with concurrency 2.
- Selection reason: Bdisc answers the auditable adjunct question; M2 tests whether fixed summaries lose clinically relevant order/nonlinearity; deferred alternatives do not answer a new decision uncertainty. Revisit the trajectory mixture only for the recorded pre-outcome M2 failure conditions. Revisit a treatment model only if new intent/responsiveness/counterfactual evidence becomes available.

## Availability, provenance and limits

I inspected `datasets/README.md`, `datasets/mimic/README.md`, the full configured MIMIC metadata, the exact relevant local table metadata files, `references/research-ambition/methods-and-compute.md`, `references/research-ambition/README.md`, `references/expert-seeds/README.md` and `references/expert-seeds/cards/mimic-04.md`. I read the local natural-history and Bayesian demonstration materials referenced by the research-ambition guide; they inform comparison of learned longitudinal and transparent alternatives but do not prescribe this question. The cancer demonstration’s main article and full STAR Methods remain unavailable; only the listed supplement/metadata availability is claimed. No demonstration is reproduced.

All source rows and notes remain read-only. MIMIC, eICU, UK Biobank and HCC source areas remain configured and directly accessible; this proposal uses only the MIMIC source because the assigned parent and exact endpoint are MIMIC-specific. Derived cohort manifests, predictions, bootstrap draws and policy tables belong in the workspace. No source row or private note is sent to public search.

The study can compute a retrospective policy ranking, observation-process diagnostics, competing-risk estimates, calibration and uncertainty. Clinical adjudication is still required for the meaning of rescue, the completeness of ICU return and death ascertainment, and whether review capacity corresponds to a feasible intervention. External validation or a prospective silent-mode study is required for transport beyond MIMIC and for any claim of clinical benefit.
