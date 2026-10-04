# Episode 79 successor: is numeric repeat-lactate value useful across a fixed capacity curve?

## Unresolved clinical question and substantive advance

At a fixed 24-hour reassessment after an early recorded norepinephrine/Levophed entry, does the numeric value of a repeat lactate improve modeled ranking of near-term in-hospital death after the repeat-observation process and contemporaneous non-lactate surveillance have already been represented?

The selected parent isolates this numeric-information contrast with one 10% review capacity. That is useful, but a result at one quota can be sensitive to how many people a hypothetical reviewer can inspect. This successor preserves the parent’s audited all-baseline/L24 population, exact lactate-resolution rules, D7 and eventual-death clocks, hospital-held-out fitting, paired queues, and noncausal interpretation. It changes only the primary capacity question: four fixed capacities are prespecified, and the primary result is one equal-weight capacity-curve summary rather than a decision anchored to a single quota.

Primary falsifiable hypothesis (H-curve): in the frozen all-baseline/L24 EICU population, adding the numeric repeat-lactate value to the process-adjusted model produces at least 3 additional D7 in-hospital deaths per 100 fixed review slots on average over the prespecified 5%, 10%, 15%, and 20% within-hospital capacities.

This is a modeled ranking claim, not a claim that review occurred, that a death was preventable, or that any capacity is preferred by a stakeholder. The 3-per-100 threshold is an inherited operational materiality anchor, not an elicited utility or benefit threshold. The single primary estimand is:

S7 = (1/4) sum over p in {0.05, 0.10, 0.15, 0.20} of (100 times Delta7,p),

where each Delta7,p is the paired D7 death-capture difference between R_full and R_process, divided by the number of slots at that capacity. S7 has units of additional D7 deaths per 100 slots, averaged equally over the four locked capacity choices. The 10% result is not primary; it is one prespecified curve ordinate.

A supportive result means that numeric value has material average incremental ranking value across this locked capacity range, subject to the gates below. It does not establish workflow, order indication, result turnaround, visibility, review effect, causal treatment effect, patient benefit, safety, cost-effectiveness, or external transportability. Prospective silent validation and workflow/clinical adjudication would still be required.

## Evidence boundary and claim under test

The strongest available evidence supports only that lactate measurements and their observation process can be prognostic. The inherited source audit cites inspected full-text evidence from Baysan et al. (2022, DOI 10.1097/CCE.0000000000000750; PMCID PMC9444407), which reported a modest recalibrated APACHE IV discrimination change after adding 24-hour lactate in 4,440 critically ill adults with sepsis (C-statistic 0.62 to 0.64). That does not establish incremental fixed-slot ranking value after informative repeat availability, repeat age, non-lactate surveillance, seven-day in-hospital outcome definition, or hospital-held-out evaluation. The inherited audit also cites Sisk et al. (2021, DOI 10.1093/jamia/ocaa242; PMCID PMC7810439) for the general rationale that observation/missingness can be informative; it does not validate these EICU variables as orders, attention, workload, or result viewing.

The unresolved claim is narrower: after R_process represents whether a repeat lactate is available and how old it is, and after the common models represent baseline/L24 state and non-lactate surveillance, does adding the numeric repeat value produce a material, internally portable ranking increment over a prespecified capacity curve?

The three materials in references/research-ambition/README.md are ambition demonstrations, not lactate evidence. The available natural-history and Bayesian article text was inspected only for general longitudinal-EHR/research context. The cancer main article and full STAR Methods remain unavailable as explicitly stated in that README; only its available supplement/metadata may be inspected, and no cancer-paper claim is used here.

## Dataset scope, provenance, and exact source bindings

Use the complete EICU source snapshot [source checksum], with no person sampling. Chunking is permitted only for memory management. Sources are read-only; all resolved rows, features, predictions, queue flags, bootstrap tuples, audits, and reports are workspace derivatives.

The five source files used are ordinary gzip-compressed CSV files; the archive member is the ordinary file itself:

- patient table, schema datasets/eicu/table-ab037c09d7df9a3c.json, source [internal dataset path] 库/EICU 2.0数据/patient.csv.gz, [source checksum]. Required columns: patientunitstayid, patienthealthsystemstayid, uniquepid, gender, age, hospitalid, hospitaldischargeoffset, hospitaldischargestatus.
- infusionDrug table, schema datasets/eicu/table-18e1a8caaa91eb44.json, source [internal dataset path] 库/EICU 2.0数据/infusionDrug.csv.gz, [source checksum]. Required columns: infusiondrugid, patientunitstayid, infusionoffset, drugname.
- lab table, schema datasets/eicu/table-79bdb33275339b1a.json, source [internal dataset path] 库/EICU 2.0数据/lab.csv.gz, [source checksum]. Required columns: labid, patientunitstayid, labresultoffset, labname, labresult, labmeasurenamesystem, labresultrevisedoffset.
- vitalPeriodic table, schema datasets/eicu/table-a22c6d6981a32279.json, source [internal dataset path] 库/EICU 2.0数据/vitalPeriodic.csv.gz, [source checksum]. Required columns: vitalperiodicid, patientunitstayid, observationoffset, heartrate, respiration, sao2.
- hospital table, schema datasets/eicu/table-811df7b2ef435e12.json, source [internal dataset path] 库/EICU 2.0数据/hospital.csv.gz, [source checksum]. Required columns: hospitalid, numbedscategory, teachingstatus, region. It is an audit/description lookup only; no hospital-level predictor enters models.

The catalog and EICU metadata bind all longitudinal joins to patientunitstayid; independent-person selection is by uniquepid, not ICU-stay row. Exact paths, archive/member descriptions, full schemas, relationship map, snapshot identifier, and source hashes are in datasets/README.md, datasets/eicu/README.md, datasets/eicu/metadata.json, and the five linked table JSON files.

MIMIC, HCC, and UKB remain directly configured and accessible under their read-only catalog entries, but are not silently substituted or joined: no supplied crosswalk links their identities/times to EICU uniquepid, patientunitstayid, or hospitalid, and this question is explicitly an EICU hospital-held-out test. The compilation audit must record that these three configured datasets were not used. No source rows or clinical notes are sent to public queries.

## Cohort construction and clocks

Apply the parent’s rules exactly; this is not a population change.

1. In patient, trim age strings; map only the exact literal > 89 to 90; numerically coerce other ages without capping; retain age >=18.
2. In infusionDrug, case-fold drugname, retain rows containing norepinephrine or levophed and infusionoffset in closed [0,1440]. For each patientunitstayid, t0 is the smallest qualifying offset. This is a recorded infusion row, not adjudicated administration, dose, indication, or true drug start.
3. For each uniquepid, retain the lexicographically smallest (t0, patientunitstayid) pair. Define L24=t0+1440 minutes.
4. Require hospitaldischargestatus exactly Alive or Expired and finite hospitaldischargeoffset >= L24. Define Dinf=1 exactly when status is Expired; otherwise Dinf=0.
5. Resolve baseline lactate B from lab: case-folded labname=lactate, case-folded labmeasurenamesystem=mmol/L, finite labresult in [0.2,30], collection labresultoffset in [t0-360,t0], and labresultrevisedoffset <= t0+60. At each collection offset retain greatest eligible revision; invalidate a final-revision tie with different numeric values; collapse identical final-revision ties to smallest labid; select latest valid collection, then smallest labid. Require B>=2.
6. Resolve optional repeat lactate F from the same lab columns and validity rules, with collection in [t0+720,L24] and revision by L24. Choose the valid collection nearest t0+1080, then earlier collection offset, then smallest labid. Retain absence as F_available=0; post-L24 revisions cannot enter.
7. Construct the complete baseline/L24 population before outcome modeling. Retain hospitals with at least 30 people and freeze the hospital set. Require at least 30 hospitals, 1,000 people, >=200 eventual deaths, >=200 eventual survivors, maximum hospital share <=15%, and both eventual classes in >=80% of hospitals.
8. Reproduce inherited feasibility counts before fitting: 2,302 people in 30 hospitals, 779 eventual deaths, 1,523 eventual survivors, and 1,163 valid repeat lactates. Any discrepancy requires a source-version explanation and renewed gate review; it cannot be repaired by changing the horizon or filters.
9. Label each retained hospital high- or low-availability using the median of its F availability in the complete population, fixed before outcome fitting and inherited by bootstrap copies. This is outcome-blind process stratification, not a causal effect modifier.

Set H7=L24+10080=t0+11520 minutes. D7=1 iff hospitaldischargestatus=="Expired" and hospitaldischargeoffset <= H7; otherwise D7=0. Equality at H7 is included. Retain every eligible person; do not exclude later discharges or use inverse-censoring weights. An Alive discharge by H7 is an observed alive discharge and competing state. A valid discharge after H7 is a D7 non-event, regardless of later status. The inherited audit reports 607 D7 events and 1,695 non-events, including 611 alive discharges by H7 and 1,084 still hospitalized without death; all 30 hospitals have both D7 classes. Reproduce these counts.

This is a seven-day in-hospital cumulative-death endpoint in the L24 risk set. hospitaldischargeoffset is an administrative discharge/death proxy, not an adjudicated death timestamp; death after an alive discharge is not captured by D7.

## Predictors and process-adjusted contrast

Use the parent’s four unweighted L2 logistic models, fitted to D7, without changing feature identity.

R_state includes age and age-squared; sex indicators with Other/Unknown reference; t0/1440 and square; baseline collection lag; ln(B) and square; latest valid L24 non-lactate laboratory values, ages, and missing indicators; and last/median/minimum/maximum/resolved-timestamp count/no-valid-observation summaries for heart rate, respiration, and SpO2 over [L24-360,L24].

The 16 non-lactate streams are potassium (mmol/L [1,10]), sodium (mmol/L [100,180]), chloride (mmol/L [50,150]), BUN (mg/dL [1,300]), glucose (mg/dL [20,1000]), creatinine (mg/dL [0.1,20]), bicarbonate (mmol/L [2,60]), calcium (mg/dL [2,20]), Hgb (g/dL [2,25]), platelets (K/mcL [1,2000]), WBC (K/mcL [0.1,500]), albumin (g/dL [0.5,8]), total bilirubin (mg/dL [0.1,50]), paO2 (mm Hg [20,700]), paCO2 (mm Hg [10,200]), and pH (blank/missing unit [6.5,8.0]). Use greatest revision, final-tie conflict, smallest-labid, latest-resolved-timestamp, and revision-by-L24 rules.

R_attention adds the six parent summaries over [t0+720,L24]: log(1+routine marker-time pairs) for the first 13 streams; log(1+blood-gas marker-time pairs) for paO2, paCO2, pH; log(1+distinct labresultoffsets across all 16 streams); observed-stream fraction; recency from L24 to latest qualifying row divided by 720; and no-qualifying-row indicator. These are surveillance proxies only, not verified orders, concern, workload, or viewing.

R_process adds F_available, repeat age (L24-F_offset)/720 when present, and missing-age indicator. R_full adds ln(F) and ln(F)^2 to R_process; missing continuous F terms are training-fold-imputed while availability remains explicit.

The primary contrast is strictly R_full versus R_process. R_full-R_attention remains secondary process-plus-value, and R_process-R_attention remains secondary process-component decomposition. Neither can replace or rescue H-curve. Do not use an outcome-trained queue, repeat-measured-only primary cohort, Dinf-trained models, post-L24 predictors, or probability thresholds as the primary analysis.

## Hospital-held-out fitting and capacity-curve estimands

For each outer hospital h, exclude h completely from training. Fit each model on all other hospitals using only D7. Within each training fold, winsorize continuous predictors at training 1st/99th percentiles, standardize with training mean and population SD, and mean-impute missing continuous values to zero after scaling; do not scale binary indicators. Fit logistic regression with intercept, L2 penalty, C=1, lbfgs, max_iter=10000, tol=1e-8, no class weights, seed 20260973, and no feature dropping. Any nonfinite training value, zero post-winsorization variance, nonconvergence, or nonfinite held-out score makes that model noncomputable. Rank raw held-out linear predictors; probabilities are descriptive only.

Let P={0.05,0.10,0.15,0.20}. For each h and p, preserve unchanged complete-cohort hospital size n_h and set k_h,p=ceil(p*n_h). For each p, let Q_full,h,p and Q_process,h,p be top-k queues from paired held-out R_full and R_process scores, breaking exact ties by ascending patientunitstayid. Let K_p=sum_h k_h,p.

For o in {7,inf}, define Delta_o,p = [sum_h sum over Q_full,h,p of D^o minus sum_h sum over Q_process,h,p of D^o] / K_p.

The primary summary is only S7=mean_p(100 times Delta_7,p). The same-queue eventual-death guard is S_inf=mean_p(100 times Delta_inf,p), computed from D7-fitted queues and never from Dinf-trained models. It guards against an apparent D7 gain that reverses eventual in-hospital death capture; it is not a causal or utility estimand.

Also report the four capacity-specific Delta values, K_p, additions/removals, queue overlap, exact ties, and switch composition. Define A_h,p=Q_full,h,p minus Q_process,h,p, R_h,p=Q_process,h,p minus Q_full,h,p, M_p=sum_h |A_h,p|, and rho_p=M_p/K_p. For o in {7,inf}, G_o,p=sum over A of D^o minus sum over R of D^o, so Delta_o,p=G_o,p/K_p=rho_p times (G_o,p/M_p) when M_p>0 and |Delta_o,p|<=rho_p. If M_p=0, set G and Delta to zero and mark yield undefined. Never use a yield without its M/K denominator.

Report the equal-hospital macro counterpart at each p and as the same equal-weight summary: S7_macro=mean_p(mean_h[100 times (P_full,h,p^7-P_process,h,p^7)]). Report pooled and macro summaries overall and by frozen low-/high-availability strata.

## Uncertainty and prespecified falsification

Use 2,000 copied-hospital refit bootstrap replicates, seed 20260973. Sample original hospitals with replacement; copies contribute evaluation rows and training weight, but all copies of one original hospital remain one exclusion group. In every replicate, repeat preprocessing, all four D7 fits, all four capacity quotas, paired queues, S7, S_inf, per-capacity deltas, availability strata, pooled/macro summaries, and the 20% ordinate. Save one machine-readable tuple per replicate containing K_p, M_p, rho_p, G7,p, Delta7,p, S7, Ginf,p, Deltainf,p, S_inf for all p, and enforce decomposition algebra. Use percentile 95% intervals. Require at least 1,900 finite replicates for pooled S7, macro S7, both availability-stratum S7 summaries, and S_inf; report a capacity-specific interval only when at least 1,900 finite replicates exist.

Use fixed-design hospital deletions (each one omitted once) to report S7, its four ordinates, macro S7, and availability-stratum summaries. The deletion table is a stability check, not a replacement estimand.

Apply these ordered states:

1. Not computable: source/header/hash mismatch; unresolved schema/key; failure to reproduce the 2,302/30 cohort and 607/1,695 D7 audit without documented source-version explanation; missing outcome class; any required model noncomputable; fewer than 1,900 finite bootstrap replicates for a required summary; missing capacity ordinate; algebra violation; or missing reproducibility artifact.
2. Supportive curve-average numeric increment: pooled S7 lower bound >=3.0; all four pooled capacity-specific upper bounds >=0 (no locked capacity shows evidence of an adverse numeric increment); low/high-availability and macro S7 lower bounds >=0; pooled S_inf lower bound >=0; S7 positive in >=80% of finite hospital deletions, >=70% of each availability-stratum deletion set, and >=70% of macro deletions.
3. Adverse opposite-direction curve average: pooled S7 upper bound <0, or both availability-stratum S7 upper bounds <0.
4. Adverse horizon tradeoff: pooled S7 lower bound >=3.0 but pooled S_inf upper bound <0.
5. Adverse capacity fragility: pooled S7 lower bound >=3.0 but at least one locked capacity-specific upper bound <0. The average is favorable while the curve contains evidence of an adverse ordinate; it cannot be called robust across the locked range.
6. Adverse below materiality: pooled S7 upper bound <3.0. This rejects the locked three-per-100 average-materiality claim while allowing a smaller association.
7. Adverse internally nonportable: pooled S7 lower bound >=3.0 but a required macro or availability-stratum S7 upper bound <0.
8. Inconclusive: every other computable pattern, including an interval crossing 3.0, a summary interval crossing zero where a sign gate is required, an eventual-death interval crossing zero, insufficient deletion evidence without an adverse interval, or favorable point estimates lacking required bounds. No point estimate or secondary ordinate can rescue this state.
9. Not clinically adjudicable from EICU: regardless of computational state, no conclusion about true norepinephrine administration, lactate order/specimen validity, turnaround, visibility, review, workload, actionability, preventability, safety, preference, utility, causal effect, patient benefit, or external transportability is permitted.

When multiple adverse states could apply, apply the first matching state. A supportive state concerns only the locked modeled curve-average ranking contrast. Capacity-specific results must be shown alongside it so a positive mean is not misrepresented as uniformly positive at every capacity.

## Required audit, verification, and interpretation contract

Compilation must produce a source manifest with paths, archive-member status, hashes, headers, dtypes/coercions, invalid timestamps, exclusion counts, duplicate/conflict collapses, and every cohort flow count; resolved B/F lactate and feature-origin audits; outer-fold membership, preprocessing constants, convergence, held-out scores, outcomes, and deterministic queue flags for every p; per-capacity paired queue K/M/rho/G/Delta tables; pooled/macro/stratum S7 and S_inf tables; curve table/plot; deletion table; and bootstrap tuples.

Every numerical conclusion must name its output column and percentile interval, record the ordered state, and separate computed ranking evidence from clinical limitations. Automatic verification may check hashes/headers, exact filters, joins, clocks, revision/tie rules, cohort counts, hospital freezing, feature identity, no post-L24 predictor, complete hospital exclusion, deterministic ties, all queue cardinalities, bootstrap finiteness, algebra, intervals, ordered states, and rejection of invalid substitutions. Fixtures must reject replacing R_process with R_attention, changing to repeat-measured patients, using Dinf-trained queues, future data, changing capacities after outcome inspection, selecting a capacity after results, or calling the average a workflow utility.

Verification can establish computational correctness and whether reported conclusions follow the locked results. It cannot establish specimen validity, order intent, turnaround, visibility, clinician review, preventability, benefit, harm, cost, preference, causality, or transportability. Those require clinical/laboratory/workflow adjudication, stakeholder utility work, external validation, and a prospective silent or impact study. EICU metadata states that narrative portions were removed, vitalPeriodic is a five-minute summary rather than raw waveform, and all times are ICU-relative.
