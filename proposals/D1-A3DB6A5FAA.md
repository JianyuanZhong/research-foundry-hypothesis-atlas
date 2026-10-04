> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 82 child: separate rank transport from calibration transport

## Audit and advance

The selected Episode-82 proposal asks whether a model trained in one outcome-blind repeat-lactate measurement-practice stratum transports to the other. Its fixed-capacity queue estimand is useful, but its hard target calibration-in-the-large gate can make a baseline-risk shift look like rank-transport failure. Ranking determines the queue; calibration does not. Passing calibration also does not validate the practice proxy or clinical workflow.

This child preserves the exact audited cohort, clocks, source files, joins, revision/conflict rules, four models, seven capacities, copied-hospital uncertainty, noncausal limits and +3-per-100 materiality threshold. Its substantive repair is a two-axis decision contract:

- H-rank (primary): the numeric repeat-lactate model adds the material worst-capacity D7 queue increment when trained in the opposite practice stratum.
- H-cal (secondary): the un-recalibrated source-trained probabilities are compatible with target absolute risk.

A positive H-rank with a calibration warning supports only portable prognostic ordering, not deployment of the probability scale. Calibration cannot veto or rescue H-rank.

## Evidence and limits

The parent’s inspected full-text Baysan et al. (2022, DOI 10.1097/CCE.0000000000000750, PMCID PMC9444407) supports incremental association of 24-hour lactate in a selected measured cohort, not observation-process adjustment or cross-practice transport. The inspected Sisk et al. review (2020, DOI 10.1093/jamia/ocaa242, PMCID PMC7810439) motivates informative observation patterns but does not establish that EICU availability is attention, staffing or capacity. The research-ambition README was inspected; the cancer demonstration’s main paper and STAR Methods are unavailable and are not cited as inspected evidence.

The complete-source feasibility audit supports only computability: 2,302 people, 30 hospitals, 1,163 eligible repeats, 607 D7 events and 779 eventual deaths. Outcome-blind median strata are low: 15 hospitals/1,011 people/229 events/782 non-events; high: 15/1,291/378/913. These counts do not test transport. The strongest possible claim is a source-stratum score changing the observed D7 composition of equal-size target-hospital queues. It cannot establish ordering, assay/specimen validity, result release or viewing, review, workload/capacity, preventability, patient benefit, causality, fairness, safety or external transportability.

## Population, source bindings and clocks

Use the complete read-only EICU snapshot [source checksum]; chunking is not sampling. Dataset catalog: datasets/README.md, [source checksum]. EICU guide: datasets/eicu/README.md. Each gzip below is an ordinary file.

1. baidu_downloads/eicu_mimic/eicu_database/EICU 2.0 data/patient.csv.gz; SHA [source checksum]; table patient, schema datasets/eicu/table-ab037c09d7df9a3c.json. Columns: patientunitstayid, patienthealthsystemstayid, uniquepid, gender, age, hospitalid, hospitaldischargeoffset, hospitaldischargestatus.
2. baidu_downloads/eicu_mimic/eicu database/EICU 2.0 data/infusionDrug.csv.gz; SHA [source checksum]; table infusionDrug, schema datasets/eicu/table-18e1a8caaa91eb44.json. Columns: infusiondrugid, patientunitstayid, infusionoffset, drugname.
3. baidu_downloads/eicu_mimic/eicu database/EICU 2.0 data/lab.csv.gz; SHA [source checksum]; table lab, schema datasets/eicu/table-79bdb33275339b1a.json. Columns: labid, patientunitstayid, labresultoffset, labname, labresult, labmeasurenamesystem, labresultrevisedoffset.
4. baidu_downloads/eicu_mimic/eicu database/EICU 2.0 data/vitalPeriodic.csv.gz; SHA [source checksum]; table vitalPeriodic, schema datasets/eicu/table-a22c6d6981a32279.json. Columns: vitalperiodicid, patientunitstayid, observationoffset, heartrate, respiration, sao2.
5. baidu_downloads/eicu_mimic/eicu database/EICU 2.0 data/hospital.csv.gz; SHA [source checksum]; table hospital, schema datasets/eicu/table-811df7b2ef435e12.json. Columns: hospitalid, numbedscategory, teachingstatus, region; descriptive only.

Resolve paths and hashes from the catalog and fail on mismatch. Join by patientunitstayid; choose one stay per uniquepid using smallest (t0, patientunitstayid); group by hospitalid. Offsets are ICU-admission minutes. Map only literal age >89 to 90; retain age >=18. Define t0 as the smallest infusionoffset in [0,1440] where case-folded drugname contains norepinephrine or levophed. Require Alive/Expired and hospitaldischargeoffset >= L24=t0+1440.

Use exact Episode-82 lactate rules: lactate in mmol/L, finite [0.2,30]; baseline collection [t0-360,t0], revision <=t0+60; repeat collection [t0+720,L24], revision <=L24; greatest eligible revision; differing final-revision ties invalid; identical ties smallest labid; latest eligible B collection; F nearest t0+1080, then earlier, then smallest labid; require B>=2. F_available marks eligible F and F is its numeric value. No post-L24 predictor. Retain hospitals with >=30 eligible people before outcomes. H7=t0+11520. D7=1 only for Expired with hospitaldischargeoffset<=H7; all others, including later Expired discharges, are D7=0. Dinf=1 for Expired. No censoring weights. The audit must reproduce 2,302 people/30 hospitals/1,163 repeats/607 D7 events/1,695 non-events/779 Dinf events.

## Variables and locked analysis

Use the inherited exact literal-name/unit/finite-range/revision/conflict/tie dictionary for 16 non-lactate streams: potassium, sodium, chloride, BUN, glucose, creatinine, bicarbonate, calcium, Hgb, platelets, WBC, albumin, total bilirubin, paO2, paCO2 and pH. Any ambiguity is not computable.

R_state is age and square, sex indicators, t0/1440 and square, baseline lag, ln(B) and square, and latest valid L24 values plus age and missing indicators for those 16 streams. R_attention adds over [t0+720,L24] log(1+marker-time pairs) for 13 routine streams, log(1+blood-gas marker-time pairs), log(1+distinct labresultoffset), observed-stream fraction, recency and no-row indicator. R_process adds F_available, repeat age and repeat-age-missing. R_full adds ln(F) and ln(F)^2 using training-fold imputation and retains availability indicators. The only inferential contrast is R_full versus R_process; the other contrasts are descriptive. F_available and surveillance are recorded process proxies, F is a recorded numeric value, and scores are prognostic rankings—not orders, visible results, actions or treatments.

Compute each hospital’s complete eligible-population F_available proportion before outcome fitting. Low is below the hospital median and high is at/above it; ties stay high. For low->high and high->low, train on all source-stratum hospitals and score only target-stratum hospitals. Source hospitals alone determine 1st/99th percentile winsorization, mean/SD, imputation and fitting. Fit unweighted intercept logistic regression, L2 C=1, lbfgs, max_iter=10,000, tol=1e-8, seed 20260973, no class weights. Rank raw linear predictors within target hospital, ties by ascending patientunitstayid. Target outcomes never affect preprocessing, fitting, strata, capacities or scores.

For C={0.05,0.075,0.10,0.125,0.15,0.175,0.20}, k_h(c)=ceil(c n_h), with top-k queues Q_full and Q_process and K_b(c)=sum_h k_h(c). Define Delta7(a->b,c)=[sum_h(D7 in Q_full,h(c)-D7 in Q_process,h(c))]/K_b(c); tau7(a->b)=min_c Delta7(a->b,c); pooled tau7 is the minimum of both directed taus. Report per-hospital and macro-hospital values, capture, false positives, unflagged events, overlap, additions/removals, ties and denominators. Apply identical queues to Dinf for tauInf, a no-tradeoff guard. Zero substitutions set fixed-slot Delta to zero and yield undefined.

## Uncertainty and calibration diagnostic

Use 2,000 copied-hospital refits, sampling hospitals independently with replacement within source and target strata and preserving direction. A copied target hospital is never scored by a model trained on itself or its source-stratum copy. Repeat source-only preprocessing, fits, scores, all capacities, minima and decompositions. Save joint tuples; require at least 1,900 finite replicates for every required functional; use two-sided percentile 95% intervals.

R_process is the primary baseline because it contains the same availability, repeat age, missingness and process/surveillance information. R_attention and R_state are secondary and cannot rescue a failed primary result. AUC, model complexity and small predictive improvement do not replace the queue estimand.

For each direction and R_process/R_full, compute source-trained p=expit(raw linear predictor) on target labels without recalibration. Report Brier, calibration slope and CITL = mean_target(D7)-mean_target(p). Require finite predictions, both target outcome classes and estimable slope/intercept. Calibration-compatible means abs(CITL)<=0.05 for both models in both target strata/directions; otherwise flag calibration-incompatible. Report bootstrap intervals. This is a target-label diagnostic, not source-independent evidence and not a rank gate; no target outcome enters fitting or transformation.

## Deterministic falsification states

The margin is 0.03 deaths per slot = 3 per 100 equal slots; it is operational, not validated utility or preventability. Apply in order:

1. Not computable: source/hash/header/schema mismatch; changed flow counts, clocks, rules, features or capacities; missing target outcome support; leakage; nonconvergence/nonfinite fit; queue/algebra failure; missing artifacts; or fewer than 1,900 finite replicates.
2. Opposite adverse: any directed capacity has upper 95% Delta7 <0.
3. Asymmetric transfer adverse: one directed tau7 upper bound <0.03 while the reverse directed tau7 lower bound >=0.03.
4. Below-materiality adverse: both directed tau7 upper bounds <0.03.
5. Eventual-death tradeoff adverse: rank conditions clear but pooled tauInf upper bound <0.
6. Supportive rank transport, calibration-compatible: both directed tau7 lower bounds >=0.03; pooled tauInf lower bound >=0; no capacity upper Delta7 <0; positive tau7 in >=70% of represented hospital deletions in each direction; and calibration-compatible.
7. Supportive rank transport with calibration warning: all rank conditions in state 6 pass but any calibration-compatible condition fails. This supports ordering only and neither proves H-cal nor invalidates H-rank.
8. Inconclusive: all other computable patterns, including intervals crossing thresholds, deletion instability without a contradictory bound, or favorable mixed-stratum sensitivity with failed directed transport.

Calibration cannot turn adverse/inconclusive rank results supportive, and its failure alone cannot make rank support adverse. State 1 applies if target outcome support needed for the queue/calibration audit is absent. The mixed-stratum leave-one-hospital-out analysis and the two other model contrasts remain non-rescuing diagnostics.

## Interpretation, verification and unavailable evidence

Support means only source-defined modeled D7 re-ranking under this EICU reconstruction, across every tested capacity and both practice directions, with the stated guards. A calibration-compatible label means source-trained probabilities also match target prevalence within the fixed CITL tolerance; a warning means target labels would be needed before using probabilities. Adverse falsifies the locked materiality/portability claim, not all lactate prognostic value. Inconclusive is not equivalence.

Compilation must emit source/hash/header/schema and flow manifests; clock and feature-origin audits; outcome-blind strata/folds; person scores/probabilities; every directional queue; Brier/CITL/slope; bootstrap tuples; deletion table; queue algebra; and conclusion-to-output mapping. Verification can check exact filtering/revision/ties, no sampling, source-only preprocessing, no leakage, directed exclusion, cardinality, bootstrap, calibration arithmetic, interval/state ordering and rejection of unsupported claims. It cannot establish true norepinephrine administration/indication, specimen or device validity, order/release/viewing, staffing/capacity, clinician action, preventability, utility, fairness, safety, causal effects, external transportability or patient benefit. These require laboratory/workflow adjudication, stakeholder utility work, independent temporal/site validation and an impact study or trial.

The read-only HCC snapshot is [source checksum]; MIMIC is [source checksum] (including ZIP members); UKB is [source checksum]. All four configured datasets remain directly accessible read-only; the other three are not pooled or treated as external validation because no validated cross-dataset key/harmonization exists. Derived analyses remain in the workspace and no source rows/notes are published.
