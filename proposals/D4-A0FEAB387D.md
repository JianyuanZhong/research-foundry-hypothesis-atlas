# Fixed-combined-eGFR profiles and commensurable broad first-code falsification

Status: prospective substantive child of [prior hypothesis]. No P−/P0 association has been estimated. This child preserves the parent's age-40–69 population, fixed-combined-eGFR profiles, day-30 origin, common N17/N18-free risk set, 10-year competing-transition estimand D, profile-support and matching gates, censoring hard gate, uncertainty, and clinical limits. The change is confined to the strongest remaining interpretation threat: broad post-index first-code outcomes are redesigned so depletion of unseen codes, competing death, and different family risk subsets cannot masquerade as renal specificity.

## Opening, evidence, unresolved claim, and advance

The strongest inspected evidence supports only these bounded claims. Large eGFRcys-minus-eGFRcr differences are common in UK Biobank and have kidney and non-GFR predictors [K1]. In SPRINT, this difference tracked frailty and broad adverse outcomes, and the combined equation could lose prognostic information [K2]. Administrative AKI coding can be insensitive and subgroup-dependent relative to serum-creatinine KDIGO AKI [K3]. In the attached parent audit, recorded N17-first and N18-first also had different coding contexts: same-day principal-family confirmation was 12.0% versus 1.39%, and median nonrenal first-code counts in the prior 365 days were 3 versus 0. These are observed ascertainment differences; they do not establish a P−/P0 association or its cause.

Unresolved hypothesis: among supported UKB adults aged 40–69 in the common day-30 N17/N18-free state, P− (2021 combined eGFR G=90 and eGFRcys−eGFRcr=−15), versus P0 (G=90 and delta=0), has a larger adjusted 10-year relative-risk contrast for first recorded inpatient N17 than for first recorded inpatient N18, and that excess is greater than a commensurable contrast for generalized new nonrenal code emission after measured pre-index history is represented.

Let theta17=log RR10(N17-first; P−/P0), theta18=log RR10(N18-first; P−/P0), and D=theta17−theta18. D remains primary. The broad comparison's main contrast is thetaK=log RR10(reaching a profile-blinded K-th new nonrenal three-character code before death; P−/P0), standardized over exactly the primary renal cohort; QK=theta17−thetaK. The experiment distinguishes:

- renal-selective recorded transition information: theta17 and D are positive, while QK shows N17 is stronger than an adequately powered, incidence-commensurate broad first-code burden;
- generalized morbidity/first-code opportunity: measured baseline history explains D, or P− predicts the broad burden at least as strongly as N17 under both threshold and depletion-process analyses.

This is descriptive prognostic discrimination, not a causal effect of discordance. Neither adjustment nor QK identifies true GFR, renal reserve, biological AKI/CKD, contact opportunity, coding behavior, or mechanism. The clinical advance is a decision rule for whether external record-level AKI validation is worth pursuing or whether the signal should instead be treated as generalized morbidity/ascertainment.

## Exact UKB binding and verified availability

Use read-only snapshot [source checksum]. All four sources are ordinary CSVs, not archive members, joined one-to-one on eid; overlapping fields must agree.

- population table `population`, catalog `datasets/ukb/table-38565c9e35e7cb6c.json`, source `[internal dataset path]`: eid, sex `31-0.0`, age `21022-0.0`, possible linkage-loss date `191-0.0`. Direct header inspection confirmed these fields. Do not use 191 until provider semantics are frozen.
- assessment table `assessment`, catalog `datasets/ukb/table-901ef6c7ddce2d51.json`, source `[internal dataset path]`: index `53-0.0`, centre `54-0.0`, grips `46-0.0` and `47-0.0`, waist `48-0.0`, BMI `21001-0.0`, ethnicity `21000-0.0`, smoking `20116-0.0`, diabetes `2443-0.0`, SBP `4080-0.0/.1`, DBP `4079-0.0/.1`.
- biological_samples table `biological_samples`, catalog `datasets/ukb/table-c6b666d905f3b02f.json`, source `[internal dataset path]`: creatinine `30700-0.0`, cystatin C `30720-0.0`, CRP `30710-0.0`, urine albumin `30500-0.0`, urine creatinine `30510-0.0`, glucose `30740-0.0`, HbA1c `30750-0.0`.
- health_outcomes table `health_outcomes`, catalog `datasets/ukb/table-3cfae45e0905b0e3.json`, source `[internal dataset path]`: 259 all-position code columns `41270-0.0`…`41270-0.258` paired by array index with first inpatient diagnosis dates `41280-0.0`…`41280-0.258`; 80 principal codes `41202-0.0`…`41202-0.79` paired with `41262-0.0`…`41262-0.79`; death dates `40000-0.0/1.0`; lifetime HESIN row count `41259-0.0` for audit only and prohibited from models.

Catalog metadata records no semantic temporal columns even though the named UKB fields contain dates; provider field metadata must verify their meaning. Direct headers confirm 259 all-position and 80 principal code/date pairs. The inherited full audit found 84 all-position and 35 principal codes without paired dates, and no dates without codes; exclude unpaired values from all dated constructions and report them. Normalize codes to uppercase alphanumeric. For broad outcomes, map only values matching `^[A-Z][0-9]{2}` after normalization to the first three characters. Freeze and emit the resulting code universe before any profile association is inspected.

The source has summary first appearances, not HESIN/HESIN_DIAG rows, encounter/admission IDs, repeated diagnosis dates, testing, provider/nation, or outpatient renal measurements. Thus it can test renal selectivity versus measured history and generalized *first-code discovery*, not utilization, clinical onset, or complete coding opportunity.

## Preserved population, profiles, clocks, and primary estimand

Use baseline instance 0; age 40–69; valid sex/index; positive creatinine/cystatin C after unit verification; at least one grip; and race-free 2021 eGFRcr >=60. Risk starts S=index+30 days. Exclude N17 on/before S and pre-S N18.5/N18.6/Z49/Z94.0/Z99.2/T86.1; the common state additionally excludes every N18* on/before S. A renal clinician must approve this operational failure/replacement set.

Compute race-free 2021 CKD-EPI eGFRcr, 2012 CKD-EPI eGFRcys, race-free 2021 combined eGFR G, and delta=eGFRcys−eGFRcr. Generate participant-age/sex-specific raw P− and P0 profiles by inversion. Preserve windows P−: 85<=G<=95 and −18<=delta<=−12; P0: 85<=G<=95 and −3<=delta<=3. Require >=100 observations/window in every sex×five-year-age stratum, both targets within every observed-stratum convex hull, and the inherited local raw-assay nearest-neighbour gate. Repeat unchanged after diagnosis restriction and corrected calendar eligibility.

Preserve 1:1 matching without replacement, exact sex/five-year-age/assessment-year, |G_i−G_j|<=1.5, and 0.2 pooled-SD propensity-logit caliper using inherited baseline covariates, centre, continuous age, G, and the scalar history block below. Reject if either group loses >50%, <1,000 pairs remain, or any prespecified covariate/G/history |SMD|>0.10. Repeat matching inside participant bootstraps. The inherited outcome-blind audit passed all 24 hull checks and found 10,893 pairs, 54.9%/90.9% retention, and maximum |SMD| 0.0352; these are feasibility facts, not outcome results.

Through S+10 calendar years classify N17-first, N18-first, same-day N17/N18 tie, death-first, death/renal same-day tie, or event-free/censored. Preserve tie assignment/exclusion sensitivities. Eligibility is S+10 calendar years<=verified administrative end C. Observed maximum dates do not prove completeness. Without export-linked provider documentation for participant-applicable C, set censoring_status=unverified and all clinical inference is inconclusive.

## Baseline history: common representation, not a post-index adjustment

All history features are frozen strictly before index. Primary window is [index−5 calendar years,index); sensitivities are [index−2,index) and [index−10,index−5). From valid non-N17/N18 41270/41280 pairs construct:

1. log1p distinct three-character first appearances over five years;
2. log1p counts in [−5,−2) and [−2,0);
3. represented ICD-10 chapters;
4. days since latest nonrenal first appearance with a none indicator;
5. proportion exactly code/date matched to 41202/41262 principal pairs with a none indicator;
6. assessment year;
7. baseline unseen-slot counts U_i(S) for the all-nonrenal universe and each frozen family.

Use prespecified restricted splines for counts, recency, and U. Report history start coverage because first appearances become appreciable only around 1995. Missing history is not proof of health.

Before post-index fitting, compare P−/P0 windows on every scalar feature and on learned history scores using SMDs and matched-pair differences. Also report a profile-blinded retrospective count of new nonrenal groups in [index−5,index), but do not compare its risk ratio to QK: survival to recruitment and unequal historical observation make it a selection diagnostic, not a commensurable outcome or causal negative control. Strong baseline-history imbalance supports stable morbidity/selection as a rival; favorable balance cannot exclude unmeasured contact.

No post-index count, code state, 41259 value, principal confirmation, or future event enters a renal adjustment or matching model.

## Transparent renal baseline

Fit inherited cause-specific Cox transition models and standardized CIFs for N17, N18, death, and ties with splined G/delta, prespecified G×delta, inherited clinical covariates, and the scalar history block. Report CIF, RD, RR, theta17, theta18, D, joint covariance, and >=500 participant-bootstrap replicates; <90% successful replicates is inconclusive. Preserve matched Aalen–Johansen corroboration and principal-position directional sensitivity. A cause-specific/CIF directional conflict attributable to death is inconclusive for selectivity, not evidence to censor death.

## Commensurable broad first-code baseline

Define V as all valid normalized three-character non-N17/N18 codes present anywhere in 41270 in this frozen snapshot, constructed without marker values or profile labels. For participant i, Seen_i(S) contains V codes whose paired first date is <=S and U_i(S)=|V\Seen_i(S)|. A post-S discovery occurs at the paired date of a code in V\Seen_i(S). Multiple codes on one day are distinct discoveries but one event time for threshold crossing. Codes without dates never enter Seen, U, or outcomes.

Randomly freeze a participant-level 70/15/15 train/validation/test split before P−/P0 associations, stratified only by sex and aggregate renal transition class, seed 20260924. In the 70% training split and blinded to marker/profile values, choose K* from {1,3,5,10,15,20,30} to minimize the absolute difference between the pooled 10-year Aalen–Johansen risk of reaching the K-th discovery before death and the pooled mean of N17-first and N18-first risks. Tie-break toward smaller K. Freeze K*; no reselection in bootstrap, validation, test, matching, or after associations.

B_K is first passage to K* newly recorded nonrenal three-character codes after S. Death before K* is a competing event; administrative end censors. Participants with U_i(S)<K* remain in the identical primary population with structural zero B_K risk, and their proportion is reported by profile. Commensurability requires >=95% of each profile window to have U>=K*, >=200 B_K events per window, and held-out pooled B_K CIF between one-half and twice the pooled mean renal CIF. If no candidate K passes, broad threshold evidence is inconclusive; do not invent a new set, subset, or horizon.

Fit B_K with the identical Cox/CIF specification, same cohort, S, 10-year horizon, death/tie rules, covariate/history representation, profile standardization distribution, bootstrap resamples, and matched pairs. Report thetaK and QK=theta17−thetaK with joint bootstrap covariance. This aligns population, first-passage form, marginal incidence, follow-up, competing death, and effect scale. It does not make N17 and B_K biologically exchangeable.

Prespecified families are J09–J18 acute respiratory infection, S00–T14 injury/poisoning, H60–H95 ear/mastoid, and L00–L99 skin. For family j define V_j, U_ij(S), and first post-S discovery among V_j\Seen_i(S). Keep every primary participant; U_ij=0 gives structural zero. Standardize CIFs over the full primary population and report theta_j and Q_j. Family-free-at-S estimates are sensitivity-only, explicitly use different risk subsets, and cannot support or refute QK. Freeze families and code universe before profile association; never replace a sparse or adverse family.

## Substantive learned/mechanistic alternative

The threshold baseline loses code composition, all discoveries after K*, and whether apparent burden reflects fewer remaining slots or a higher per-slot discovery process. Fit one alternative at matched specificity:

1. Learn outcome-blind baseline phenotypes from [index−5,index): sparse participant × (three-character code × recency bin [5,2), [2,0.5), [0.5,0) years × all-position/principal-confirmed channel) NMF. Training-frequency threshold is 50. Fit ranks 8,16,32 and seeds 20260924–20260926 in training only; select by validation Poisson deviance plus matched-component cosine stability >=0.80. Freeze loadings and list top codes before naming components.
2. On yearly intervals 1–10, model C_im, the number of first discoveries while alive, as an overdispersed binomial process with trials U_im (unseen slots at interval start), complementary-log-log time baseline, G/delta surface, the same clinical covariates, scalar history, and NMF scores. Update U_i,m+1=U_im−C_im; this post-index state is an outcome-process denominator only and never enters renal models.
3. Fit death as an absorbing interval transition with the same baseline inputs and a shared participant frailty with discovery intensity. Jointly simulate standardized 10-year trajectories under P− and P0, preserving each participant's baseline U/history. Report the per-slot discovery intensity ratio, expected fraction of baseline unseen slots discovered before death, probability of reaching frozen K*, and death CIF.
4. Evaluate untouched-test count calibration by year, death calibration slope/intercept, negative-binomial/binomial deviance, B_K Brier/calibration, and stability across seeds. Compare scalar-only, scalar+NMF, and scalar+NMF+shared-frailty models. The alternative is retained only if held-out calibration is acceptable, B_K Brier is not worse than the transparent baseline, and profile contrasts are seed-stable.

This alternative can reveal a shared morbidity/coding-history phenotype and separate baseline opportunity U from discovery intensity, which the K-th first-passage baseline loses. It cannot turn first-code discovery into healthcare utilization or identify a biological mechanism. A transformer is deferred because each code has only one date and ordering beyond first appearance is unavailable; revisit only if the NMF/depletion model fails held-out reconstruction/calibration and a preregistered sequence model improves those targets, not merely renal AUC. A latent true-GFR model remains deferred without measured GFR or validated repeated-marker errors.

Approximate future-solver budget: sparse parsing/checkpointing 1–2 hours, Cox/matching/bootstrap 2–4 hours, NMF and yearly joint model 1–3 hours; <=16 CPUs, <=262,144 MiB, <=8 hours. The parent's measured outcome audit used 8 CPUs for 953 seconds with <2 GiB observed RSS; its unvectorized control audit timed out at 1,800 seconds. CPU-first is appropriate. One allocated A100 may be used only if profiling shows NMF/joint bootstrap is dominant; GPU availability is verified infrastructure, not scientific merit or a runtime guarantee.

## Rule-linked interpretation

All rules require verified units/code semantics/C, support and matching gates, K commensurability, model convergence, held-out calibration, joint uncertainty, and no material tie/principal reversal.

Supportive for *recorded N17 selectivity robust to measured baseline history and broader first-code opportunity* requires all of:

- theta17 lower 95% bound >0 and D lower bound >0 in the scalar model;
- matched D agrees in direction and the principal-position sensitivity does not reverse;
- QK lower bound >0 in the transparent model;
- scalar+NMF renal D remains positive and the calibrated depletion model's B_K contrast agrees with thetaK/QK;
- results are not driven by U<K structural zeros, and cause-specific/CIF conclusions are not reversed by differential death.

Family results are contextual. Remote-family nulls support specificity only when their Q intervals exclude equality in the N17-favoring direction; “not significant” never counts. Even this supportive pattern justifies external encounter/laboratory-validated AKI study, not clinical use.

Adverse to renal selectivity / supportive of generalized morbidity or first-code opportunity if any prespecified, adequately precise pattern occurs:

- D upper bound <=0 after scalar or stable NMF baseline history;
- thetaK lower bound >0 and QK upper bound <=0 in both threshold and calibrated depletion analyses;
- a stable NMF component associated with P− predicts N17, B_K, and multiple families similarly, with Q intervals excluding an N17 advantage;
- death-adjusted CIF and cause-specific results show the apparent N17 excess is explained by differential competing death.

Adverse to acute selectivity but compatible with chronic/shared renal information: theta18>0 with D upper bound <=0, or theta17 and theta18 are similar with adequate precision. Adverse to both profile claims: both renal theta upper bounds <=0.

Inconclusive includes unverified export completeness; no K satisfying the frozen commensurability gate; >5% structural ineligibility; sparse profile-window events; QK crossing zero with clinically material alternatives; inadequate NMF stability or held-out calibration; <90% bootstrap convergence; support/matching failure; death/CIF/cause-specific discordance; principal/tie reversal; or methods disagreeing without adjudication. An imprecise null does not refute the hypothesis. Do not rescue a result by changing K, families, profiles, windows, population, horizon, rank, or exclusions.

Stronger conclusions require more data. Biological AKI/CKD and coding sensitivity require record-level admissions, serial creatinine/cystatin C/albuminuria, tests and clinician adjudication. Complete observation opportunity requires provider/nation/contact data and export provenance. True filtration requires measured GFR or validated measurement-error data. Transportability needs external validation; benefit from marker-guided care needs a prospective decision-impact or intervention study.

## Solver deliverable and verifier boundaries

A future solver must newly construct and fit: exact cohort/support rerun; code/date pairing and release audit; frozen code universe; baseline Seen/U/history matrices; profile-blinded K selection; transparent renal/B_K/family models; matched/principal/tie analyses; NMF and depletion/death alternative; joint bootstrap; and a rule-consistent conclusion.

Required outputs:

- `run-manifest.json`, `censoring-provenance.json`, `field-audit.json`, `cohort-flow.csv`
- `profile-support.json`, `matched-balance.csv`, `events-by-definition.json`
- `code-universe.csv`, `baseline-history-audit.json`, `k-selection.json`, `commensurability-audit.json`
- `cox-results.json`, `broad-threshold-results.json`, `family-results.json`
- `nmf-history-results.json`, `depletion-model-results.json`, `transition-contrasts.json`
- `conclusion.json`, `report.md`

The verifier can check source hashes/headers, joins, pair indices, timestamps, code universe, no post-index renal covariates, split isolation, profile-blinded K selection, common population/clock/death handling, structural-zero accounting, support/matching/calibration/convergence gates, bootstrap QK/D intervals, and consistency of conclusion.json with computed rules. It must accept correct supportive, adverse, and inconclusive interpretations and reject unsupported favorable claims. It cannot establish export completeness, validate AKI/CKD, infer unmeasured contact/testing, adjudicate mechanism, or establish clinical benefit.

## Exactly three inspected works

[K1] Chen DC et al. *Cystatin C- and Creatinine-based Estimated GFR Differences: Prevalence and Predictors in the UK Biobank.* Kidney Medicine. 2024;6:100796. doi:10.1016/j.xkme.2024.100796. Relevant full-text XML excerpt inspected.

[K2] Potok OA et al. *The Difference Between Cystatin C- and Creatinine-Based Estimated GFR and Associations With Frailty and Adverse Outcomes: A Cohort Analysis of SPRINT.* American Journal of Kidney Diseases. 2020;76:765–774. doi:10.1053/j.ajkd.2020.05.017. Relevant PMC full-text excerpt inspected.

[K3] Zhang J et al. *Validation of Administrative Coding and Clinical Notes for Hospital-Acquired Acute Kidney Injury in Adults.* AMIA Annual Symposium Proceedings. 2021:1234–1243. PMID:35308921; PMCID:PMC8861756. Relevant full-text sections inspected; US single-system performance estimates are not transported to UKB.
