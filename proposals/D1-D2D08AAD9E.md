> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Fixed offered-slot service yield for HCC documentary-M2 review: a pretest-fixed completed-case prefix benchmark

## Clinical question, evidence boundary, and substantive advance

The clinical question is whether interpretable information already present in routine preoperative CT/MRI report bodies can improve how a scarce multidisciplinary review service captures resected hepatocellular carcinoma (HCC) cases with high-grade microvascular invasion documented as M2. The action represented is allocation of documentary review. This study does not assign surgery, transplantation, neoadjuvant or adjuvant treatment, surveillance, or any other care.

The strongest claim supported before this experiment is limited. HCC snapshot [source checksum] contains patient/encounter-linked demographics, completed procedures with start/end fields, examination accessions with acquisition-like start times and eventual stored report text, untimed pathology narratives, and dated medication/order rows. It can support a retrospective, chronological benchmark inside a future-defined completed-resection cohort. It does not contain a preoperative referral or candidate roster, cancellations or noncompleters, planned-operation status, report authored/final/release/view time, immutable report version, pathology time/specimen/slide/block keys or sampling protocol, MDT slot releases, review completions, clinician actions, treatments caused by review, recurrence, survival, harm, cost, or benefit.

Current acquired evidence supports clinical importance, not the proposed result. Neves and Soares (2026; DOI 10.3390/cancers18132028; PMCID PMC13360217; acquired full-text XML source [source checksum]) reviewed 36 HCC early-recurrence AI studies: 35 were retrospective, only six reported external validation, calibration and decision-curve analysis were inconsistent, and most had high risk of bias. Fan et al. (2026; DOI 10.21037/jgo-2025-aw-944; acquired HTML source [source checksum]) reported documentary M2 in 106 of 621 resected HCC patients and only modest LDH discrimination (AUC 0.610 for MVI); the authors explicitly did not support changing surgical extent from LDH alone and requested incremental, external, and prospective validation. Neither source establishes report-semantic service yield, report availability at decision time, a real arrival roster, capacity, or patient benefit in this dataset. The research-ambition README was inspected as a rigor guide. The unavailable Cell main article and full STAR Methods were not read or used as evidence.

The unresolved claim tested here is that report semantics materially increase documentary-M2 captures per fixed pretest-offered service slot, relative both to the same fitted policy with semantics masked and to an independently fitted nonsemantic policy, across 2020 and 2021 and every claimed source/access state. The advance over the parent is an estimand repair: fixed offered-slot service yield is the sole primary effectiveness estimand. Equal-completed first-J results remain diagnostic only. An exact utilization/completion-set-composition decomposition explains arithmetic contributions without pretending that two adaptive policies encounter a common online opportunity set.

## Frozen scientific hypothesis

Let s index a complete coherent source state; y be test year 2020 or 2021; q be 0.05, 0.10, or 0.20; d be decision buffer 12, 24, 48, or 72 hours; h be an exact report-access cell; M be semantic policy S, same-fit semantic ablation S0, or independently fitted nonsemantic baseline B; and X be S0 or B.

For each state and historical year a in 2015–2019, count completed-case pseudo-roster members N_a(s) before parsing pathology grade or report semantics. Define:

N_ref = min over s and a in 2015–2019 of N_a(s)
K_q = floor(q N_ref)
J_q = ceil(0.90 K_q).

K_q and J_q are absolute integers frozen using only 2015–2019. The same values are used for every test year, access cell, policy, visibility realization, outcome state, and bootstrap replicate. They are workload benchmarks, not observed capacity. A q is infeasible if K_q < 50, J_q < 45, or any coherent test state has fewer than K_q pseudo-arrivals. The global N_ref >= 500 and K_0.05 >= 25 checks are retained, but do not override the stricter per-q K/J feasibility rule; a joint claim over all q therefore requires the strict rule for all q.

For one policy trace define n_M = sum_i A_i(M), z_M = sum_i A_i(M)Y_i, utilization U_M = n_M/K_q, completion-set M2 prevalence P_M = z_M/n_M, and fixed offered-slot service yield T_M = 100 z_M/K_q = 100 U_M P_M. P_M is undefined if n_M=0; any such cell is inconclusive and fails the J/utilization gates.

The two primary contrasts, in additional documentary-M2 captures per 100 offered slots, are:

D_K = T_S - T_S0, the incremental contribution of report semantics in the same fitted policy;
C_K = T_S - T_B, the total contrast against an independently fitted nonsemantic policy.

H1-service-yield: a nonempty report-access frontier exists such that, for every claimed frontier cell, q, test year, decision buffer, and coherent source state, the simultaneous 97.5% lower confidence limits for D_K and C_K both exceed 5 captures per 100 offered slots; the simultaneous lower limit for S relative to the state-matched retrospective top-K oracle exceeds 0.80; all policies complete at least J_q reviews and have U_M >= 0.90; and every evidence gate passes.

This is a universal, falsifiable completed-case pseudo-roster hypothesis. It is not a claim about a real referral stream, a common adaptive opportunity set, biological M2, workflow efficiency, changed treatment, or patient benefit.

## Exact utilization/completion-set-composition decomposition

For each primary comparison S versus X, X in {S0,B}, define:

V_U(S,X) = 50 (U_S - U_X)(P_S + P_X)
V_P(S,X) = 50 (P_S - P_X)(U_S + U_X).

Both are measured in documentary-M2 captures per 100 offered slots. V_U is the utilization contribution: the change in completion fraction valued at the average M2 prevalence of the two policy-specific completed sets. V_P is the completion-set-composition contribution, colloquially the case-selection contribution: the change in M2 prevalence among each policy's own completed cases, weighted by average utilization.

The identity is exact:

V_U + V_P
= 50[(U_S-U_X)(P_S+P_X) + (P_S-P_X)(U_S+U_X)]
= 100(U_S P_S - U_X P_X)
= T_S - T_X.

It is the order-invariant Shapley decomposition of the two-factor product 100UP: average the result of changing U first and P first. It therefore identifies exactly how much of the observed arithmetic yield difference is assigned to completion volume versus completed-set composition under that symmetric convention. It is invariant to policy labels, apart from the expected sign reversal when S and X are swapped.

It does not identify a causal mediated effect, a common risk set, a patient-for-patient substitution effect, or what either policy would have selected under the other's prior allocations. Each adaptive policy owns its threshold decisions, remaining-slot history, acceptance ordinals, completion time, and completed set. Those histories are generally policy-specific. The source cannot create a common online opportunity set after divergent actions, and the analysis will not condition one policy on another's actions. Overlap and discordant-selection counts may be reported descriptively, with no causal label.

For each decomposition component, a simultaneous interval wholly above zero supports a positive arithmetic contribution; one wholly below zero supports an offsetting contribution; and an interval spanning zero leaves that component unresolved. A service-yield result may be called composition-supported only if the V_P lower bound exceeds zero in every scope named by that label, utilization-supported only if the V_U lower bound exceeds zero, both-supported if both do, and unlocalized if total yield is supportive but neither component is uniformly signed. “Pure selection,” “prioritization effect,” and “utilization mediation” are prohibited. State-varying component signs must be reported as mixed.

## Secondary equal-completed diagnostic

For each policy, acceptance ordinal r_M(i) is defined only within that policy. Let A_i^J(M) = A_i(M) 1[r_M(i) <= J_q] and:

R_J(M) = (100/J_q) sum_i A_i^J(M)Y_i
D_J = R_J(S)-R_J(S0)
C_J = R_J(S)-R_J(B).

D_J and C_J compare the first J completions of each policy. They are secondary diagnostics and never gate H1-service-yield. The replay must report each policy's Jth-completion pseudo-time, pseudo-arrival position, released-slot count, used-slot count, and first-J member backpointers. Unless traces happen to coincide exactly, the first-J sets arise at policy-specific horizons and after policy-specific prior actions. Even exact equality of completion count does not establish equal opportunity. Favorable D_J/C_J may be described only as a difference between policy-specific first-J completion prefixes. Adverse or inconclusive D_J/C_J does not negate a supportive offered-slot yield, but it forbids language that the supported yield arose from better equal-workload prioritization.

## Population, coupled source states, and temporal boundaries

The person unit is Patient Master Index. Same-encounter joins use (Patient Master Index, Visit Number). Preserve raw row ordinal and multiplicity before exact deduplication. A state s jointly fixes patient membership, selected operative episode and clock, selected encounter and age, recorded prior treatment, pseudo-arrival order, examination-unit identity and clock, modality pattern, report-body visibility, pathology composite, and documentary-M2 outcome. Never mix a favorable clock from one state with report identity, eligibility, visibility, or outcome from another.

Two hepatobiliary surgeons and a surgical informatician must freeze a resection dictionary and reconcile Surgery Source values, including Anesthesia System and Medical Record Surgery, into operative-episode alternatives. A clinically linked anesthesia-system Start Time is exact only after validation. A midnight/date-like case-record time is an interval [date,date+24h). Missing, competing, same-day, and adjacent-day clocks remain explicit coupled states. Within each state, select the first eligible completed resection.

Membership requires age >=18 on the selected encounter; all-row same-encounter pathology explicitly supporting HCC; and no recorded prior HCC resection, transplant, TACE, ablation, radiotherapy, targeted therapy, or immunotherapy during [t_dec-365 days,t_dec), using state-matched procedures, medications, and orders. This is absence of recorded treatment, not biological treatment-naivety. Completion and postoperative pathology are future facts used to define a retrospective evaluation cohort. Patients outside it are not controls or negatives. The source cannot enumerate referrals, cancellations, non-HCC resections, or noncompleters.

Set t_dec = t_op-d, with d=24 hours designated and 12/48/72-hour locked sensitivities. Develop in 2015–2018; use 2019 only for tuning, calibration, threshold and policy selection; test 2020 and 2021 separately. Any patient with a possible later-period state is quarantined from every earlier fit. Use 2022 onward only for drift and ascertainment audit, never model or threshold revision.

Map a year to u=(t_dec-Jan 1)/(next Jan 1-Jan 1) and 366 fixed bins. From 2015–2019 pseudo-arrivals only, freeze monotonized cumulative release fraction F_ref(u), then L_q(u)=floor(K_q F_ref(u)) with L_q(1)=K_q. At pseudo-arrival i, policy M may allocate only if its own used count before i is below L_q(u_i), its frozen score meets its threshold, and that member has not previously been offered or recalled. Unused released capacity may be used by a later new arrival, but there is no patient queue, recall, replacement, or terminal backfill. The policy sees only the current member's admissible fields, scaled calendar time, its own cumulative released/used slots, and quantities frozen by 31 December 2019. It cannot read future arrivals, final test N, future ranks/outcomes, or another policy's trace. Interval clocks crossing an arrival or release boundary are enumerated. Exact-time ties use one pre-2019-frozen hash of Patient master index.

## Report unit, access, outcome, variables, and baselines

A nonblank source accession entity is (patient master index, encounter number, examination number), formed before time filtering, modality assignment, text parsing, or visibility masking. It is a source bundle, not a proven authored report. Retain every component row. If component modality labels conflict or valid component clocks differ by more than 24 hours, the outer state envelope contains both indivisible-accession and deterministic normalized-(examination, start-time calendar-date) partition interpretations, each with raw backpointers. No favorable identity interpretation may be selected. Blank examination-number rows stay in acquisition and population audits but their text is masked as identity-unknown.

A unit is temporally eligible only if every component clock places it within [t_dec-90 days,t_dec). The deterministic conservative choice uses the maximum component start; missing/conflicting clocks remain state alternatives. Select at most the latest eligible unit per modality, with frozen raw-ordinal/hash tie breaking. Two blinded abdominal radiologists map all component examination labels to CT, MRI, non-target, or unresolved. Concatenate examination findings and examination diagnosis in frozen raw order. Visibility exposes the whole selected source unit, never selected rows. Because no final/release/version field exists, “visible” means a hypothetical exposure of eventual stored text.

Compose every exact-deduplicated pathology row on the selected encounter from Pathology, Examination findings, and Examination diagnosis. A frozen position-aware parser sets Y=1 only for an anchored selected value M2 and Y=0 only for anchored M0/M1. Boilerplate, unanchored mentions, missing/uncertain grade, M0/M1/M2 conflict, uncertain specimen linkage, or inadequate documented sampling gives Y in {0,1}, not exclusion. Two Chinese-reading pathologists blinded to predictors adjudicate every test unknown/conflict and every parsed M2; a third resolves disagreement. The endpoint is documentary M2, not biological M2.

B includes only state-selected age, sex, CT/MRI/other acquisition indicators, eligible source-unit count, acquisition-to-decision recency, component count, report-identity ambiguity, and development-frequency Machine Model category. It excludes report text, pathology, diagnoses, labs, identifiers, year, and post-cutoff facts. S adds prespecified interpretable report semantics: maximum lesion diameter, lesion count, capsule, margin, arterial hyperenhancement, washout, peritumoral enhancement/hypointensity, satellite lesion, portal/hepatic-vein tumor thrombus, cirrhosis, and ascites, each encoded present/absent/uncertain/not-mentioned.

Fit S and B on 2015–2018 by patient-wise worst-state elastic-net logistic loss. For each M/q, select one constant calibrated-score threshold from {0,0.005,...,1} in 2019 to maximize documentary-M2 capture subject to U_M >=0.90 under the frozen release curve; break ties by fewer false reviews, then larger threshold. Freeze all preprocessing, coefficients, calibration, and thresholds before 2020. S0 is not refitted: it masks only semantic fields within S's exact fitted preprocessing, coefficients, calibration, threshold, and state machine. Under complete semantic masking S and S0 must be bitwise identical in features, scores, actions, traces, and outputs. B is independently fitted without report-body semantics.

Report first-come, frozen seeded lottery, none, age/sex-only, and state-matched retrospective top-K controls. The oracle is an unattainable retrospective ceiling, never an online comparator or primary policy.

## Report-access frontier and coherent uncertainty

Use exact access guarantees on a 0.05 grid: h_C for CT among C-pattern members, h_M for MRI among M-pattern members, h_A for at least one visible modality among CM members, and h_B <= h_A for both visible among CM members. O/C/M/CM patterns remain in all denominators. For singly visible CM members, modality choice, accession partitions, clocks, member/outcome states, chronological order, release counters, thresholds, and actions remain jointly coupled. The frontier is the coordinatewise-minimal set of cells satisfying H1-service-yield. It is a hypothetical exact-version access requirement, not observed availability. At the all-semantics-masked boundary S and S0 must collapse exactly, so D_K=V_U=V_P=D_J=0; any claimed positive semantic effect there is a computation failure.

## Analysis, uncertainty, and evidence gates

Use 2,000 patient-cluster bootstrap refits. Each replicate rebuilds coherent states, development fit, 2019 tuning/calibration/thresholds, access realizations, pseudo-policy traces, decompositions, first-J diagnostics, and endpoints. K, J, release bins, threshold grid, semantic dictionary, margins, and decision rules remain frozen. Preserve partial-identification extrema over complete coherent states inside each replicate; never combine table-wise or attribute-wise extrema.

Construct a max-centered 97.5% simultaneous confidence family over D_K, C_K, V_U and V_P for both comparisons, U and P differences, D_J, C_J, both years, all q values, four decision buffers, all evaluated access cells and identity states, attainability ratios, and prespecified null checks. The reported table must retain point estimate, simultaneous lower/upper limits, state attaining each extremum, event counts, n_M, z_M, U_M, P_M, and raw result-file locator. No selective access cell, state, year, q, or buffer may be omitted after results are seen.

Run 1,000 development/tuning semantic-block permutations stratified by year, modality pattern, source-unit cardinality, identity ambiguity, and formatting family, with full refits. The claimed S-versus-S0 cells must clear the predeclared simultaneous one-sided 0.025 null envelope; failure is inconclusive even if the bootstrap interval is favorable. Negative controls must preserve exact S/S0 identity when semantic blocks are entirely masked.

Required gates are: N_ref>=500; per-q K>=50 and J>=45; every coherent test state can offer K; at least 50 adjudicated M2 events per claimed year envelope; anchored grade >=85%; all test unknown/conflicts adjudicated; parser kappa >=0.90, M2 PPV >=0.98 and sensitivity >=0.95; modality agreement >=0.95 and unresolved <=1%; each claimed modality pattern >=100 members and 20 M2; semantic-feature PPV and sensitivity >=0.85; no required-feature/pattern shift >15 percentage points from 2019; all-report and no-report calibration slope 0.80–1.20 and intercept -0.10–0.10; every policy n_M>=J and worst-state U_M>=0.90; exact release/slot accounting; complete state/backpointer replay; optimizer/brute-force equality on N<=12 fixtures; coordinatewise monotone access limits; zero lab/diagnosis/forbidden lineage; all S/S0 masking identities; permutation gate; and <=2.5% failed bootstrap replicates.

Actual row counts, exact-deduplication counts, exclusions by reason, state multiplicity, unknown/adjudicated outcomes, access patterns, policy traces, and failed replicates must be written to derived ledgers. The prior bounded examination audit of 100,000 physical data rows found 92,118 nonblank accession groups, 4,064 multirow groups, 4,064 multilabel groups, 162 multistart groups, and no blank accession in that bounded sample. These are source-grain observations only, not cohort attrition or prevalence; compilation must scan the full source and report actual filters.

## Prespecified result zones and conclusions

Supportive for H1-service-yield requires every gate, a nonempty frontier, and simultaneous lower limits >5 for both D_K and C_K plus attainability lower limit >0.80 in every required year/q/buffer/state at every claimed cell. Equality to 5 or 0.80 is not supportive. The strongest permitted conclusion is: eventual stored CT/MRI report semantics materially improved documentary-M2 captures per fixed pretest-offered slot in this retrospective completed-resection pseudo-roster, robust to enumerated source and access uncertainty. Component language must follow the interval-based labels above.

Adverse for the universal hypothesis occurs if, with otherwise valid computation, any required D_K or C_K simultaneous upper limit is <=5, the access frontier is empty, or any attainability upper limit is <0.80. If an upper limit is <0, report evidence of lower service yield in that scope. Favorable D_J/C_J cannot rescue an adverse offered-slot result. If D_K is supportive but V_P is adverse or unresolved, report a utilization-led or unlocalized service-yield gain and explicitly state that better prioritization was not shown. If the oracle is favorable but the online prefix is adverse, say retrospective ranking did not survive chronological release.

Inconclusive includes any interval crossing its strict margin; any failed population, identity, adjudication, calibration, permutation, state, optimizer, utilization, event-count, or bootstrap gate; n_M<J; undefined P_M; incompatible year/q/buffer results; or an unverified conclusion/result link. Gate failure is not evidence against the biological idea. A result may be service-yield supportive while decomposition localization is inconclusive; report those two judgments separately.

Missing external roster, report-version, capacity, or action evidence never becomes a favorable or adverse HCC result. It always leaves real workflow performance and patient benefit untested. Stronger claims require: a representative timestamped preoperative roster including all considered patients, cancellations, non-HCC pathology and noncompleters; stable candidate/referral and exclusion times; exact report accession/version/authored/final/release/view timestamps and body hashes; actual slot release/completion times, reviewer roles/hours, queue/overflow rules; adjudicated pathology specimen/slide/block and sampling data; and prospectively captured actions, treatment, recurrence, survival, harms, cost and fairness. Transport requires prospective silent-mode validation; benefit requires expert review and ultimately a randomized or pragmatic impact study.

## Exact source bindings

All sources are ordinary read-only CSV files; archive member is null/ordinary file. The catalog snapshot and live headers were inspected. All joins use Patient master index and Encounter number unless explicitly stated.

- encounters — table encounters; [internal dataset path]; use Age, Sex, Encounter Time, Admission Time, Discharge Time. Direct identifiers Name, National ID Number, Mobile Phone Number, Medical Insurance/Encounter Card Number, and Inpatient Number are forbidden from predictors and exported ledgers.
- procedures — table procedures; [internal dataset path]; use Surgery, Start time, End time, Surgery source for completed episode, operative clock, year, and recorded prior procedures.
- examinations — table examinations; [internal dataset path]; source accession key extends the encounter join with Examination Number; use Examination, Examination Findings, Examination Diagnosis, Start Time, Machine Model for identity states, modality, eventual text, acquisition-like clock, and development-frequency device category. No authored/final/release/view/version field exists.
- pathology — table pathology; [internal dataset path]; use all same-encounter pathology, examination findings, examination diagnosis rows for the documentary endpoint; machine model is provenance only. No pathology time, accession/specimen, slide, block, or sampling field exists.
- medications — table medications; [internal dataset path]; use medication, medication type, start time, end time for recorded prior systemic treatment.
- orders — table orders; [internal dataset path](non-medication)_2062526727266216118.csv; use Non-medication Order, Order Entry Time, Start Time, End Time, Order Status for recorded local-treatment/radiotherapy proxies.
- diagnoses — table diagnoses; [internal dataset path]; untimed Diagnosis name and Diagnosis type are corroboration/audit only, never predictors or timed membership evidence.
- labs — table labs; [internal dataset path]; Test, Qualitative Result, Quantitative Result, Specimen Type, Test Time are aggregate availability audit only. Units, panel/accession, release and view fields are absent; predictor lineage must be zero.
- clinical_documents — table clinical_documents; [internal dataset path]; untimed narrative excluded.
- vitals — table vitals; [internal dataset path]; identifier-only, excluded.
- transfers — table transfers; [internal dataset path]; identifier-only, excluded.
- front_page — table front_page; [internal dataset path]; header/identifier-only, excluded.

The complete catalog is [internal dataset path], [source checksum]. MIMIC, eICU, and UKB remain directly accessible through datasets/mimic/README.md, datasets/eicu/README.md, and datasets/ukb/README.md. They are not pooled because none identifies this institutional completed-resection/report/pathology estimand. Source files remain read-only; all derived state, adjudication, trace, bootstrap, and conclusion ledgers belong in the workspace.

## Compiler and verifier contract

Compilation must preserve the completed-case pseudo-roster label, coupled state envelope, first eligible episode, all four decision buffers, patient quarantine, accession-first identity alternatives, whole-unit visibility, all-row documentary outcome, pre-2020 absolute K/J and release curve, prefix-only policy, no patient queue/recall/backfill, finite frozen threshold rule, exact S/S0/B definitions, D_K/C_K as sole primary contrasts, exact Shapley decomposition, first-J diagnostics as nonprimary, access frontier, simultaneous inference, gates, and clinical limits. Reintroducing test-year N into K, treating completed cases as referrals, making D_J/C_J primary, forcing a common policy opportunity set, changing a decomposition convention, splitting accessions without a state, pooling test years, changing margins, or claiming workflow/patient benefit is a scientific change requiring a Lead child.

The automatic verifier may establish source headers/hashes, joins, actual filters/attrition, source-state and raw-backpointer completeness, pre-2020 K/J provenance, temporal quarantine, no future-test-N reads, policy-local state transitions, release/slot accounting, n/z/U/P/T calculations, decomposition identities, first-J extraction and horizon reporting, accession states, S0 identity, bootstrap/permutation calculations, optimizer fixtures, and conclusion-to-zone linkage. It cannot establish true operative/referral identity, report visibility/version, Chinese semantics, pathology specimen linkage/sampling, biological M2, acceptable workload/margin, actual review action, treatment benefit, recurrence, survival, harms, costs, fairness, or transportability.

Required deterministic verifier fixtures:

1. Decomposition arithmetic: K=100, S(n=100,z=40), X(n=90,z=27) must give T difference 13, V_U=3.5, V_P=9.5, and exact sum 13.
2. Equal utilization: K=100, S(90,36), X(90,27) must give difference 9, V_U=0, V_P=9.
3. Equal composition: K=100, S(100,40), X(90,36) must give difference 4, V_U=4, V_P=0.
4. Offsetting components: K=100, S(90,45), X(100,40) must give difference 5, V_U=-4.5 and V_P=9.5. The total is not supportive at equality 5.
5. Undefined composition: n_X=0 must produce P_X/V_U/V_P as undefined, fail J/utilization, and force inconclusive—not impute zero prevalence.
6. Swap symmetry: swapping S/X negates total and both components exactly.
7. S0 identity: complete semantic masking must yield bitwise-equal S/S0 features, scores, actions, traces, n, z, T, first-J sets and zero D_K/V_U/V_P/D_J for every state.
8. First-J trap: K=100,J=90, S(n=90,z=30 with 30 positives in first 90), X(n=100,z=29 with 20 positives in first 90) gives D_J=100(30-20)/90 but D_K=1. A favorable first-J result must not produce support.
9. Offered-yield support with adverse first-J diagnostic: K=100,J=90, S(n=100,z=40 with 30 positives in first 90), X(n=90,z=32) gives D_K=8 and D_J=-200/90. If the simultaneous D_K lower bound exceeds 5 and gates pass, service yield may be supportive, but equal-workload prioritization language must be rejected.
10. Divergent histories: two synthetic chronological traces with different threshold acceptances and Jth-completion times must replay solely from each policy's own released/used counts. Any implementation that synchronizes, intersects, unions, or borrows another policy's available set must fail.
11. Release boundary and ties: enumerate interval clocks crossing release bins; use the frozen patient hash for exact ties; prohibit end-of-year filling, recall, and reads of final test N.
12. Coupled-state trap: a favorable operative clock from one state, report partition from another, and outcome from a third must never be combined.
13. Access monotonicity and null: all-semantic masking collapses S/S0; coordinatewise stronger access cannot violate the predeclared attainable-set monotonicity check; a positive semantic claim at the null boundary fails.
14. Zone boundaries: lower limit exactly 5 is not supportive; upper limit exactly 5 is adverse to the universal >5 hypothesis; an interval crossing 5 is inconclusive. Attainability uses the same strict handling at 0.80.
15. Conclusion discipline: reject a computationally correct supportive result labeled as real referral performance, causal prioritization, treatment benefit, or biological M2; accept the bounded completed-case service-yield statement. Accept properly worded adverse, mixed-component, and gate-failed/inconclusive interpretations without rewarding confirmation.
16. Provenance: every reported conclusion must point to a computed row containing scope, estimate, simultaneous interval, state extremum, counts, gate vector, source hashes, code version, and raw trace/result locator. Missing or mismatched links fail verification.

Reference execution demonstrates computational feasibility and linkage only. It neither validates clinical annotations nor establishes that a conclusion is true outside the explicitly computed documentary benchmark.
