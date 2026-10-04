> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 95 successor: one label-free deployment margin for a fixed-capacity L24 mortality-review queue

## Decision and unresolved question

At the L24 landmark, a receiving ICU may have a fixed number of mortality-review slots but no local outcome labels with which to fit a model. The decision is whether to deploy a score trained in the opposite EICU repeat-lactate practice stratum to fill exactly 10% of each receiving hospital's eligible queue. This is a ranking decision, not an intervention decision and not permission to display a calibrated probability.

The strongest evidence available to this lineage is narrower than that deployment claim. Baysan et al. (2022, DOI 10.1097/CCE.0000000000000750, PMCID PMC9444407) studied 24-hour lactate in selected critically ill patients with sepsis and reported a modest change in discrimination when it was added to an APACHE-IV-based prediction model (recalibrated C-statistic 0.62 to 0.64); that does not establish fixed-capacity queue yield, practice transport, or benefit. Sisk et al. (2021, DOI 10.1093/jamia/ocaa242, PMCID PMC7810439) reviews informative presence/observation and supports representing measurement processes in prediction, but does not establish that a repeat-lactate value transports between these hospitals. The three research-ambition demonstrations were inspected as demonstrations of rigor, not as evidence that this EICU question is true. The cancer demonstration's main article and full STAR Methods remain unavailable in the supplied references; no claim about them is used here.

The unresolved claim is therefore:

> In the audited EICU cohort, can a source-practice, source-label-only score containing the optional repeat lactate fill a fixed 10% hospital queue with D7 mortality yield that is both materially above the otherwise identical process-aware score and not materially below the best available held-out-local-label benchmark, in both cross-practice directions?

The substantive advance is a deployable boundary: one predeclared queue size, one scalar decision estimand, a label-free portable score, and an explicit local-label benchmark. It separates queue ranking from calibration, capacity choice, and eventual in-hospital death.

## Single primary hypothesis and estimand

Let the frozen practice strata be Low and High, defined below. For direction d in {Low-to-High, High-to-Low}, let T_d be the 15 target hospitals and S_d the opposite 15 source hospitals. For target hospital h, let n_h be its eligible cohort size and

[
k_h = \lceil 0.10 n_h \rceil, qquad K_d=\sum_{h\in T_d} k_h.
]

At the sole primary capacity, rank target patients within hospital by the raw score (descending), with ascending patientunitstayid as the only tie-breaker. Define:

- Q^P_{d,h}: the portable R_full queue, fit only on S_d;
- Q^0_{d,h}: the source-only R_process queue;
- Q^L_{d,h}: the R_full queue from a model fit on T_d excluding h, using target-stratum labels, scored only on h.

For x in {P,0,L}, define the D7 queue yield

[
Y^x_d = \frac{\sum_{h\in T_d}\sum_{i\in Q^x_{d,h}} D7_i}{K_d}.
]

The single primary estimand is the worst-direction deployment margin

[
M_{D7}=\min_{d}\left[
Y^P_d - \max\{Y^0_d+0.03,\;Y^L_d-0.02\}
\right].
]

Thus the portable queue must clear both reference requirements in the weaker direction: at least 0.03 D7 deaths per occupied slot above R_process and no more than 0.02 below the held-out local-label R_full benchmark. The margins are operational design margins for this experiment, not estimates of preventable deaths, clinical utility, or guideline thresholds. The component yields and contrasts are emitted so that the reason for any decision is visible, but they do not become additional primary estimands.

Primary hypothesis: M_D7 >= 0. The null/deployment failure is M_D7 < 0. The primary state is based only on this scalar, its joint copied-hospital interval, and prespecified computability/stability gates.

Capacity is fixed at c=0.10 before analysis and is not selected from the results. Capacities {0.05, 0.075, 0.125, 0.15, 0.175, 0.20} are stress diagnostics only; they cannot change the primary state or rescue it. Hospital-specific ceil arithmetic is mandatory, so the experiment does not silently replace a real fixed-capacity queue with a pooled patient fraction.

## Deterministic result states

Run the full finite/computability and stability checks below.

- **Supportive D7 deployment-boundary result:** all provenance and cohort audits pass; at least 1,900 of 2,000 joint copied-hospital replicates are finite; deletion stability passes; and the two-sided percentile interval's lower endpoint for M_D7 is >= 0.
- **Adverse D7 deployment-boundary result:** all required computation is valid and the interval's upper endpoint for M_D7 is < 0. This means the portable queue fails at least one required reference margin in the worst direction under this data-defined experiment.
- **Inconclusive D7 result:** valid computation exists but the interval crosses zero, fewer than 1,900 joint replicates are finite, deletion instability occurs, required support is inadequate, or any other prespecified gate prevents a determinate supportive/adverse classification.

No point estimate, single direction, stress capacity, calibration result, or Dinf result can create a supportive state. If the primary interval crosses zero, report the component intervals and direction-specific diagnostics but classify the primary result as inconclusive, even if one direction appears favorable.

The eventual-horizon analysis is secondary and has an explicit, non-rescuing margin:

For each direction, compute the Dinf portable-versus-held-out-local contrast
\(T^{inf}_d=Y^{P,inf}_d-Y^{L,inf}_d\), and define the reported worst-direction \(T^{inf}=\min_d T^{inf}_d\). Use the prespecified noninferiority margin -0.02 deaths per occupied slot. Label **eventual-horizon warning** if the upper endpoint of the joint interval for \(T^{inf}\) is < -0.02; label **eventual-horizon compatible** if its lower endpoint is >= -0.02; otherwise label **eventual-horizon inconclusive**. This analysis never changes the D7 state, and “compatible” does not establish eventual-mortality transport, safety, or clinical benefit.

This makes D7 the sole deployment outcome and gives the secondary Dinf interpretation a deterministic verifier rule.

## Population, clocks, outcomes, and exact source bindings

Use EICU snapshot `[source checksum]`. All five inputs are read-only gzip files with archive member “ordinary file.” Fail closed on a snapshot, path, source hash, header, schema hash, key, or member mismatch.

1. **patient table**: source `[internal dataset path]`; [source checksum]; schema `datasets/eicu/table-ab037c09d7df9a3c.json`; schema [source checksum]. Required columns: `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `gender`, `age`, `hospitalid`, `hospitaldischargeoffset`, `hospitaldischargestatus`.
2. **infusionDrug table**: source `[internal dataset path]`; [source checksum]; schema `datasets/eicu/table-18e1a8caaa91eb44.json`; schema [source checksum]. Required columns: `infusiondrugid`, `patientunitstayid`, `infusionoffset`, `drugname`.
3. **lab table**: source `[internal dataset path]`; [source checksum]; schema `datasets/eicu/table-79bdb33275339b1a.json`; schema [source checksum]. Required columns: `labid`, `patientunitstayid`, `labresultoffset`, `labname`, `labresult`, `labmeasurenamesystem`, `labresultrevisedoffset`.
4. **vitalPeriodic table**: source `[internal dataset path]`; [source checksum]; schema `datasets/eicu/table-a22c6d6981a32279.json`; schema [source checksum]. Required columns: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `heartrate`, `respiration`, `sao2`.
5. **hospital table**: source `[internal dataset path]`; [source checksum]; schema `datasets/eicu/table-811df7b2ef435e12.json`; schema [source checksum]. Required columns: `hospitalid`, `numbedscategory`, `teachingstatus`, `region`. Hospital descriptors are descriptive only and never predictors.

Join each clinical table to patient on `patientunitstayid`. Use `uniquepid` only to retain the lexicographically smallest pair (t0, patientunitstayid) per person; `patienthealthsystemstayid` is audit-only. Use `hospitalid` for practice strata, source/target folds, queues, hospital deletion, and copied-hospital bootstrap. The catalog confirms these relationships and that all offsets are minutes relative to ICU admission. No additional configured dataset is silently substituted; the HCC, MIMIC, and UKB sources remain accessible but are out of scope for this EICU experiment.

Construct t0 as the smallest finite `infusionoffset` in [0,1440] for a case-folded `drugname` containing “norepinephrine” or “levophed.” Let L24=t0+1440 and H7=t0+11520. Trim age, map only literal >89 to 90, coerce other ages, and retain age>=18. Retain exact `hospitaldischargestatus` values Alive or Expired and `hospitaldischargeoffset>=L24`.

Construct baseline B from case-folded `labname` lactate, unit mmol/L, finite `labresult` in [0.2,30], collection in [t0-360,t0], and `labresultrevisedoffset<=t0+60]. At each collection retain the greatest eligible revision; invalidate differing final-revision numeric values; collapse identical final ties to the smallest `labid`; select the latest valid collection, then smallest `labid`; require B>=2.

Construct optional repeat F using the identical analyte, unit, range, revision, conflict, and tie rules in [t0+720,L24], with revision deadline L24. Select the collection nearest t0+1080, then earlier, then smallest `labid`. Retain people without F with F_available=0. Apply hospital n>=30 after complete construction. Freeze Low strictly below and High at or above repeat proportion median `0.5029411764705882`, computed from the complete constructed cohort before outcomes. Set D7=1 only for Expired with `hospitaldischargeoffset<=H7`; Alive and later Expired are D7=0. Set Dinf=1 for Expired. Do not use post-L24 predictors or censoring weights.

The expected reconstruction gates, inherited from the audited parent and to be independently rechecked, are 2,302 people in 30 hospitals; 1,163 F_available=1; D7 607/1,695; Dinf 779/1,523; Low 15 hospitals/1,011 people/380 repeats/229 D7 events; High 15 hospitals/1,291 people/783 repeats/378 D7 events. These are audit values, not hypothesis results.

## Frozen predictors and source-only fitting

Use inherited R_state, R_attention, R_process, and R_full byte-for-byte. R_state contains age and square, sex indicators, t0/1440 and square, baseline lag, ln(B) and square, and latest valid L24 values plus age and missingness indicators for potassium, sodium, chloride, BUN, glucose, creatinine, bicarbonate, calcium, Hgb, platelets, WBC, albumin, total bilirubin, PaO2, PaCO2 and pH. Resolve analytes with the inherited valid ranges, units, revision deadlines, final-revision conflict invalidation, and smallest-id ties.

Resolve `vitalPeriodic` `heartrate` [20,250], `respiration` [2,80], and `sao2` [40,100] per `observationoffset`; differing valid duplicate values invalidate a timestamp and identical values retain the smallest `vitalperiodicid`. Summarize each over [L24-360,L24] by last, median, minimum, maximum, valid timestamp count, and no-valid-observation.

R_attention is the inherited non-lactate surveillance representation over [t0+720,L24]: log(1+marker-time pairs) for 13 routine streams, log(1+blood-gas marker-time pairs), log(1+distinct labresultoffsets), observed-stream fraction, recency, and no-row indicators. R_process adds F_available, repeat age, and repeat-age-missingness. R_full adds ln(F) and its square with source-fold imputation while retaining availability indicators. No hospital descriptor, narrative note, D7, Dinf, target label, or post-L24 field enters a score.

For each direction, fit R_process and R_full using only source-stratum hospitals S_d. Use source-only 1st/99th percentile winsorization, means/SDs, imputation, and unweighted L2 logistic regression (C=1, lbfgs, max_iter=10000, tol=1e-8, seed 20260973, no class weights). Nonfinite input, zero variance, nonconvergence, or nonfinite score is not-computable. The local reference uses exactly this pipeline trained on target-stratum hospitals other than the scored target hospital; its labels are quarantined from every portable fit, transform, source/target stratum definition, queue, and model choice. The held-out local reference is a historical label-availability benchmark, not a deployable score in the proposed no-label setting.

R_state and R_attention are descriptive source-only baselines (yield, capture, overlap, and substitution) and cannot replace R_process in the primary envelope. Within-hospital random selection is also reported as a capacity sanity baseline, along with all-patient D7 prevalence. None is allowed to change the primary estimand or state.

## Probability-use diagnostic, kept separate

Report—but do not include in M_D7—a source-only offset calibration screen for R_full. In each direction estimate delta_A by bisection on [-20,20], tolerance 1e-12, solving

[
\sum_i[D7_i-\operatorname{expit}(\eta_i+\delta_A)]-\delta_A=0
]

on source-hospital-held-out predictions. Apply p_tr=expit(eta_tr+delta_A) to targets. Fit p_loc from the held-out-local pipeline only for the historical benchmark. Within direction and F_available status, and threshold z(p)=1[p>=0.10] including equality, emit n, D7 events, observed event rate, mean prediction, and E=mean(D7-p). q_tr is the maximum absolute E across four target cells; q_loc is analogously defined; G=q_tr-q_loc. Report calibration as acceptable only if upper 95% q_tr<=0.05, upper 95% G<=0.02, and each portable/local cell has at least 30 original patients. Calibration-supportive does not authorize probability display, and calibration-adverse does not alter the queue state. The source offset and all portable calibration preprocessing use source labels only.

## Uncertainty, deletion stability, and exact arithmetic

Use 2,000 copied-hospital refit replicates with seed 20260973. Sample source and target hospitals independently with replacement within their frozen strata, preserving original hospital IDs. Refit source preprocessing, R_process/R_full, source-held-out offset, portable scores, local scores, all c=0.10 queues, D7 yields, M_D7, calibration cells, and Dinf jointly. A duplicated target hospital must be excluded from the local model by original hospital identity even when another copy is present. Require at least 1,900 finite joint replicates; retain every failure reason. Use the two-sided 2.5th and 97.5th percentiles of the joint M_D7 replicates. Never bootstrap directions, capacities, or calibration cells independently.

For each original hospital, leave out that hospital and recompute the entire relevant pipeline while keeping the frozen Low/High strata unchanged. A directional component is unstable if its result state (support/adverse/inconclusive relative to its own margin interval) changes. If more than 30% of valid original-hospital deletions change either directional component state, classify the primary result inconclusive. Emit all deletion estimates and states.

The queue checker must verify for every h exactly k_h=ceil(0.10 n_h) rows, no duplicate patientunitstayid, only eligible patients, descending raw linear predictor, ascending patientunitstayid ties, and K_d equal to the sum of hospital queue sizes. Recompute Y^P_d, Y^0_d, Y^L_d and M_D7 from emitted patient-level rows. Random, R_state, R_attention, and stress-capacity queues are diagnostics and do not substitute for the primary queues.

## Required outputs and falsification

Emit:

- source/snapshot/path/size/hash/header/schema/member manifest;
- row flow, de-duplication, cohort and 30-hospital audit;
- person-level t0, L24, H7, B, F, F_available, stratum, hospital and outcome records;
- feature-origin and preprocessing map, fold maps, source/local exclusion records;
- portable, process, state, attention and local raw scores/probabilities;
- every primary queue row, score tie, k_h, K_d, and queue algebra;
- D7 component yields, M_D7 bootstrap tuples and failures;
- calibration cells and roots;
- Dinf secondary tuples and horizon tag;
- deletion results and a conclusion-to-output map.

Falsification is strongest when the portable queue fails despite a valid source-only fit, or when R_full does not exceed R_process by the +0.03 margin. A transport failure against R_local falsifies the no-local-label deployment boundary even if lactate appears predictive within source data. A favorable point estimate with a crossed copied-hospital interval, unstable deletions, or failed audit is inconclusive. A favorable D7 result with an adverse Dinf tag falsifies any attempted eventual-outcome generalization but does not falsify the narrower D7 queue statement. Intercept-only score shifts that change queue membership must be exposed by the queue and bootstrap artifacts, not hidden by calibration.

Not-computable precedes interpretation for any provenance or audit mismatch; altered cohort, clocks, revision/conflict/tie rules, predictors, folds, capacities, thresholds, or outcomes; leakage; wrong local exclusion; nonfinite fit/root/score; queue/cardinality/algebra error; missing artifact; inadequate cell support; or fewer than 1,900 finite joint replicates.

## Interpretation and clinical evidence limits

A supportive result means only that, in this fixed retrospective EICU construction, source-practice R_full ranked a 10%-per-hospital queue with D7 event yield meeting the two operational reference margins in both directions. It does not show that repeat lactate causes better outcomes, that review changes care, that any death was preventable, or that a hospital should allocate staff based on this result. An adverse result is useful evidence against this exact label-free deployment boundary, not evidence that lactate has no prognostic information. An inconclusive result requires more data or a better-powered design.

The experiment cannot establish true norepinephrine administration or indication; specimen collection, assay validity, result release/viewing, or repeat-lactate clinical availability; staffing and actual review capacity; clinical action, preventability, utility, safety, fairness, or subgroup acceptability; causal treatment effects or patient benefit; external or temporal transport; or eventual mortality outside the source-defined in-hospital discharge record. EICU `vitalPeriodic` is a five-minute summary rather than a raw waveform, and public narrative note sections are removed; retained structured note fields are not used. Clinical adjudication of medication and specimen workflows, synchronized workflow/capacity data, stakeholder-defined utility and fairness review, independent temporal/external validation, and an impact or randomized study are required for those stronger conclusions. Reference execution, if performed, establishes computational feasibility only.
