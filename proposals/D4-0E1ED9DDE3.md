> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 63: outcome-blind incremental handgrip value for fixed-capacity cystatin-C testing

## Lead decision and relation to the assigned parent

This is a distinct successor to `[prior hypothesis]`, not a repair of its computation or interpretation. The assigned parent remains valid and its results are immutable: the frozen five-year AG1/G1 counts are 25 versus 23 (Delta 4.291845/1,000; one-sided lower limit -2.145923/1,000), and the independently computed nine-year counts are 60 versus 59 (Delta 2.145923/1,000; one-sided limits -8.583691 and 12.875536/1,000). Both horizons remain inconclusive. This successor cannot relabel, rescue, replace, or reinterpret those results.

The new clinical direction is whether handgrip adds useful information after UACR is already available when a service can offer cystatin C to only a fixed number of people. It is outcome-blind: allocation models are fitted only in the already locked baseline-development partition and then applied to the locked O1_hold partition. No inpatient outcome, death, follow-up completeness, or observed parent result determines eligibility, coefficients, rankings, or rosters.

## Evidence and unresolved question

The strongest evidence inspected supports that creatinine--cystatin C discordance is associated with adverse outcomes and may reclassify risk; it does not establish measured-GFR accuracy, a benefit from ordering cystatin C, or the incremental value of grip in a constrained testing policy. The current Europe PMC search record for Estrella et al., “Discordance in Creatinine- and Cystatin C-Based eGFR and Clinical Outcomes: A Meta-Analysis” (JAMA 2025, DOI 10.1001/jama.2025.17578), source ID `[source checksum]`, was inspected as an abstract/search result; the full paper was not acquired because the public acquisition endpoint returned HTTP 403. Its abstract supports an association literature, not this fixed-capacity policy question.

The prespecified hypothesis is:

> In the exact parent O1_hold population, with a fixed 466-person cystatin-C capacity, adding visit-1 handgrip to an otherwise identical UACR-based allocation rule increases the fixed-denominator yield of participants whose visit-1 race-free combined creatinine--cystatin C eGFR is below 60 despite creatinine eGFR being at least 60, by at least one participant per 466-person list, with a one-sided 95% lower limit strictly above zero.

The threshold is a resolution-aware operational margin (2.145923/1,000), not a validated clinical-utility threshold. Support would justify a prospective adjudicated testing-policy study; it would not establish CKD, measured filtration, or benefit.

## Population and model lock

Use exactly the parent definitions of O, O1, the visit-1 prior-code exclusion, the five-year and nine-year time conventions, and O1_hold. Do not change age, sex, BMI, grip, creatinine, eGFRcr, visit-date, race-free equation, missingness, hash split, or prior N17/N18 rules. O1_hold remains 2,334 canonical eids, and capacity remains n1=floor(0.20*2,334)=466.

Reuse the complete outcome-blind Episode-16 fitting protocol and its locked development/test/replication hash partition, transforms, ridge grid, one-SE rule, coefficients, and tie convention from the parent’s executable ancestry. Fit two new allocation scores in baseline development only:

- A: the parent routine baseline variables plus UACR, without grip.
- AG: the same variables plus grip.

Apply each locked score to every O1_hold participant, rank descending score, resolve ties using the frozen full SHA-256 tie digest and eid fallback, and take exactly the top 466 as A1 and AG1. These are new rosters for a new question; they do not alter the parent’s frozen G1/AG1 rosters or estimand. Any use of visit-1 or post-visit outcomes to fit, rank, refill, or tune A1/AG1 invalidates the experiment.

## Primary target, estimand, and time

For each O1_hold participant, use recorded visit-1 values only. Let R_i=1 when the frozen race-free creatinine eGFR is at least 60 and the frozen race-free combined creatinine--cystatin C eGFR is below 60; otherwise R_i=0. Use the exact 2021 equations and transformations in the parent’s complete Episode-16 specification, not a substitute equation or a post hoc threshold.

The primary fixed-denominator yields are:

- Y_R(A1)=1000*sum(R_i in A1)/466
- Y_R(AG1)=1000*sum(R_i in AG1)/466
- Delta_R=Y_R(AG1)-Y_R(A1)

Report the two numerators, yields, Delta_R, overlap/Jaccard, and the A1-only/AG1-only decomposition. Do not condition denominators on valid R, survivors, N18 events, or non-overlap. Also emit the parent’s immutable five-year and nine-year results exactly as inherited, but they are not components of Delta_R and cannot rescue it.

Use the parent’s 2,000-draw paired participant bootstrap over canonical-eid-sorted O1_hold, with fixed A1/AG1 memberships, shared multiplicities, PCG64DXSM, and the inherited seed convention and studentized/percentile fallback. Require at least 95% finite target draws, no zero-variance or membership/seed/decomposition failure, and at least 95% valid paired visit-1 creatinine/cystatin target labels in O1_hold before interpreting support or adversity. These gates are fixed before reading the new selected-list result.

Labels are mutually exclusive:

- supportive: all gates pass, Delta_R >= 2.145923/1,000, and the one-sided 95% lower limit is strictly above zero;
- adverse: all gates pass and the one-sided 95% upper limit is strictly below 2.145923/1,000;
- inconclusive: every other result, including sparse or invalid biomarker data, a boundary case, a wide interval, or failed computation.

Adverse means evidence against the prespecified material incremental yield; it does not mean grip harms patients, UACR-only testing is clinically optimal, or cystatin C has no value. Inconclusive is not equivalence or no difference.

## Exact data binding and availability

All source files are ordinary read-only CSVs with archive member `null). Every table is joined one-to-one on canonical `eid`; reject duplicate/missing keys and disagreement in overlapping fields.

- `population`, source `[internal dataset path]`, table `population`, schema `datasets/ukb/table-38565c9e35e7cb6c.json`, key `eid`; use `31-0.0` and `21022-0.0`.
- `assessment`, source `[internal dataset path]`, table `assessment`, schema `datasets/ukb/table-901ef6c7ddce2d51.json`, key `eid`; use parent-required `53-0.0`, `53-1.0`, `21003-1.0`, `21001-0.0/1.0`, `46-0.0/1.0`, `47-0.0/1.0), and all other locked Episode-16 eligibility/model fields.
- `biological_samples`, source `[internal dataset path]`, table `biological_samples`, schema `datasets/ukb/table-c6b666d905f3b02f.json`, key `eid`; use `30500-0.0/1.0`, `30505-0.0/1.0`, `30510-0.0/1.0` for the parent-defined UACR construction and `30700-0.0/1.0`, `30720-0.0/1.0` for creatinine/cystatin equations. The header contains `30515-0.0` but not `30515-1.0`; do not invent or use the absent visit-1 field.
- `health_outcomes`, source `[internal dataset path]`, table `health_outcomes`, schema `datasets/ukb/table-3cfae45e0905b0e3.json`, key `eid`; no field is used to form A1/AG1 or R_i. For the inherited parent audit only, retain paired `41270-0.i` with `41280-0.i`, i=0,...,258, and death `40000-0.0/1.0), using the parent’s exact t1/t5/t9 and same-day-death rules.

The UKB snapshot is `[source checksum]`; the full catalog is `[internal dataset path]` with [source checksum]. Catalog metadata declares `temporal_columns=[]`: instance 1 is not a specimen timestamp. The exact physical source headers were inspected and contain the required fields as stated.

HCC, MIMIC-IV including notes, and eICU remain directly accessible read-only but cannot join to UKB `eid`; they are not used in this UKB-specific experiment. No private rows or notes were sent to public search.

## Falsification and clinical limits

This hypothesis is falsified by an adverse label, not by a parent-inconclusive label. A supportive label establishes only incremental enrichment for an equation-defined baseline reclassification state in this fixed-capacity allocation exercise. It does not establish persistent or adjudicated CKD, measured-GFR accuracy, medication-dose correctness, nephrology referral benefit, prevention, safety, cost-effectiveness, fairness, transportability, or causal effects of testing. Those require repeated clinically timed biomarkers, measured GFR, outpatient and primary-care diagnoses, medications and downstream actions, complete follow-up/censoring, clinical adjudication, external validation, and a prospective implementation or randomized testing-strategy study.

Explicitly forbidden are subgroup or sex/age fishing; choosing a new horizon; changing O1_hold, n1, parent G1/AG1 rosters, or parent outcomes; fitting on O1_hold; refilling or reranking lists; changing the 60 threshold after seeing results; claiming equivalence, causal benefit, CKD truth, or workflow superiority; and using the known 25/23 or 60/59 direction to select a new endpoint or threshold.

## Why publish this successor rather than retain only the parent

The parent asks whether its two already-frozen allocation rules differ in later recorded inpatient N18 yield, and its correct result is unresolved at both five and nine years. That cannot answer the operational question of whether grip is worth adding when UACR is already available. This successor isolates that incremental component, uses an almost complete baseline biochemical target rather than a sparse administrative endpoint, and has a direct decision interpretation: supportive -> prospective testing-policy evaluation; adverse -> do not prioritize grip as an allocation feature; inconclusive -> retain the parent’s unresolved status and obtain better data. It is therefore a meaningful, pre-result advance while preserving the parent as a required immutable audit result.

A positive result still does not justify clinical adoption. The unavailable evidence is decisive: no specimen collection timestamps, measured GFR, repeated CKD confirmation, medication decisions, costs, harms, equity assessment, outpatient capture, or prospective intervention.
