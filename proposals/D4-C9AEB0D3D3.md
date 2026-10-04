# Episode 28 specificity qualification: kidney-code enrichment versus general inpatient coding

## Parent and unresolved clinical question

This is a substantive child of assessed-valid `[prior hypothesis]`. That candidate's complete executable specification and authenticated artifacts remain controlling. The child changes no O1_hold population, visit-1 time zero, development fit, coefficients, AG1/A1/G1 scores, rank/tie rule, n1=466 lists, biochemical H1/D1 hierarchy, observed-low-UACR definition, nine-year N18 endpoint, missing-label bounds, bootstrap construction, or evidence limits.

The unresolved question after the parent repair is interpretive but clinically important: if adding grip to UACR changes which cystatin-C slots find low-albuminuria participants later coded with inpatient N18, is that signal specific enough to be kidney-relevant, or is it largely a marker of general frailty, illness burden, or differential hospital contact? The parent appropriately does not claim kidney specificity. This child makes one necessary-condition challenge to that interpretation computable.

The new hypothesis is:

> On the exact frozen O1_hold population and exact n1=466 AG1 and A1 lists, AG1 will not have a materially greater nine-year yield of any subsequent non-genitourinary inpatient ICD-10 diagnosis than A1; the one-sided 95% upper confidence bound for the fixed-denominator difference will be below +10 events per 1,000 slots. This negative-control qualification is considered only alongside the inherited low-UACR N18 result and cannot rescue it.

The +10/1,000 threshold is an explicitly provisional operating margin (about five people in a 466-person list), not a validated equivalence or patient-utility threshold. A non-material nonrenal contrast is necessary but not sufficient evidence for kidney specificity: it cannot rule out coding, ascertainment, or residual frailty explanations.

## Evidence boundary and substantive advance

The inherited evidence supports that cystatin-C/creatinine discordance is predictable in UK Biobank and that combined filtration estimates can improve risk classification in some cohorts; it does not support the AG1-versus-A1 fixed-capacity policy, a grip increment after UACR, measured GFR, persistent CKD, or clinical benefit. The relevant full-text evidence in the controlling parent is Chen et al. (Kidney Medicine 2024, DOI 10.1016/j.xkme.2024.100796, PMCID PMC10986041) and Lees et al. (JAMA Network Open 2022, DOI 10.1001/jamanetworkopen.2022.38300, PMCID PMC9597396). I rely on the parent’s frozen full-text acquisitions and do not infer anything from unavailable paper text. Current public literature likewise supports biomarker prognostic association while leaving prospective management benefit, implementation, and cost unresolved.

The strongest computational evidence before this child remains outcome-blind feasibility: the parent read all 502,370 joined source rows and reproduced O=134,118, O1=5,823, O1_hold=2,334, and the two exact n1=466 lists; AG1 and A1 overlap on 427 people, with 39 directional swaps. No selected H1, D1, N18, death, or policy-yield result was opened. Thus no evidence yet supports or refutes either the inherited hypothesis or this negative-control hypothesis.

The advance is not a prediction-score improvement. It tests whether the parent’s most clinically tempting interpretation—kidney-specific discovery among low-UACR participants—survives a prespecified generic inpatient-coding challenge on the same people, same lists, same denominator, and same chronology. A positive N18 contrast accompanied by a large nonrenal contrast should be interpreted as broad prognostic/healthcare-contact enrichment, not as evidence that cystatin targeting discovers occult kidney disease.

## Population, exposure, time, and outcomes

Use the parent’s exact O1_hold=2,334: valid population sex `31-0.0`, visit-1 age `21003-1.0` 40–69, visit-1 date `53-1.0`, positive BMI `21001-1.0`, positive maximum grip `46-1.0` or `47-1.0`, positive creatinine `30700-1.0`, race-free 2021 eGFRcr1 in [60,90), and no valid position-paired inpatient N17/N18 before or on t1; original development is excluded by the inherited hash lock `h>=60`. Preserve the parent’s exact treatment of codes with missing or invalid paired dates. The two frozen exposures are S_AG1 and S_A1, each exactly 466 eids, and membership never depends on follow-up codes, death, UACR outcome, or this endpoint.

Time zero is t1=`assessment.53-1.0`. Set t9 to t1 plus nine calendar years using the parent leap-day rule. Use the health-outcomes arrays `41270-0.0` through `41270-0.258` and paired dates `41280-0.0` through `41280-0.258`. A valid event is a parseable ICD-10 diagnosis code paired to its same-position parseable date. Define the new participant-level endpoint NR9=1 if at least one paired code-date lies in (t1,t9] and strictly before the parent’s earliest valid death from `40000-0.0`/`40000-1.0`; same-day death is not an event because the event must be strictly before death. If no death is recorded, use the parent’s meaning: no recorded death in this source, not proof of survival.

For the negative-control event, retain only ICD-10-looking codes whose first character is not N (case-normalized); this excludes the entire N00–N99 genitourinary chapter, including N17/N18, rather than attempting to classify individual diagnoses clinically. Do not call this an admission count: the available arrays are diagnosis-code/date pairs without encounter identifiers. NR9 is therefore “any subsequent non-genitourinary diagnosis code in the inpatient-linked outcome arrays,” not a validated hospitalization or disease diagnosis.

The inherited K18_9 endpoint remains exactly the parent’s paired N18 code/date event, strictly before death in (t1,t9]. Report it unchanged and do not replace it with NR9. Also report, descriptively and non-confirmatorily, pre-t1 non-genitourinary code prevalence and the four-cell NR9/K18_9 table. These checks can reveal baseline imbalance or overlap but cannot be used to reselect lists or adjust the primary endpoint.

## Estimands and analysis

For p in {AG1,A1}, with fixed denominator 466:

`Y_NR9(p)=1000 * sum(i in S_p) NR9_i / 466`

and `Delta_NR9=Y_NR9(AG1)-Y_NR9(A1)`. Report numerators, yields, AG-only/A1-only events, list overlap/Jaccard, and the exact symmetric-difference identity. Do not divide by observed UACR, survivors, N18 cases, or valid codes; do not count repeated codes more than once per participant.

Run the exact parent participant-level paired bootstrap: canonical-eid-sorted O1_hold, 2,000 shared multiplicity draws, PCG64DXSM, seed string `SHA256("ukb-grip-visit1-bootstrap-v1|" + b)`, b=0,...,1999. Memberships, denominators, coefficients, and ranks are fixed; no refit, rerank, refill, or post-outcome tuning. Report point estimate, bootstrap SE, two-sided 95% interval, one-sided 95% upper/lower limits, finite-draw fraction, and the parent’s prescribed studentized/percentile fallback. The child’s new confirmatory component is Delta_NR9; the inherited primary and secondary families, results, and rescue prohibitions remain controlling. If the verifier requires one joint family, append Delta_NR9 once after the parent’s frozen family in a deterministic manifest order, never duplicate inherited components.

Before interpretation require exact list sizes/hashes and successful joins; at least 40 NR9 events in the union, at least 10 in each list, and at least 10 in the symmetric difference; no unresolved two-field death conflict; valid paired-code chronology; and at least 95% finite bootstrap draws. These are anti-vacuity feasibility gates, not power guarantees. An aggregate all-row preflight may inspect only NR9 feasibility and code/date parsing before opening selected yields.

Classify the new qualification as follows:

- `nonrenal_control_supported`: all gates pass and the one-sided upper 95% bound for Delta_NR9 is < +10/1,000.
- `nonrenal_control_adverse`: all gates pass and the one-sided lower 95% bound is > +10/1,000. This weakens a kidney-specific interpretation but does not prove harm, causality, or a generic mechanism.
- `nonrenal_control_inconclusive`: otherwise, including sparse events, a bound touching the margin, parsing conflict, zero variance, or computation failure; this is not equivalence.

The conjunction `low_UACR_N18_signal_with_specificity_qualification` may be reported only if the inherited parent low-UACR result is supportive and the new control is supportive. If the parent is supportive but the control is adverse, report `low_UACR_N18_signal_with_generic-coding-concern`; if the control is inconclusive, report `low_UACR_N18_signal_specificity_unresolved`. A control result never rescues failed H1/D1, the parent N18 endpoint, or the parent’s missing-label gates. No result may be described as kidney-specific benefit, CKD diagnosis, safe testing, causal effect, or clinical utility.

## Falsification and verifier contract

The design is falsified or downgraded if any membership flag, list hash, denominator, pair position, date boundary, death precedence, code-prefix rule, bootstrap seed, or uncertainty calculation differs from the declaration. A pre-t1 code contrast cannot be relabeled as follow-up evidence. A large NR9 contrast is an adverse interpretive result even if the N18 contrast is favorable; a null NR9 contrast cannot be used to claim specificity without clinical adjudication. Permuting the NR9 labels within O1_hold while preserving list membership is a negative-control computation check; it must not be used to choose the margin or endpoint. The verifier must accept correct supportive, adverse, and inconclusive interpretations and reject claims of equivalence, causal safety, measured GFR, persistent/adjudicated CKD, mechanism, prevention, cost-effectiveness, fairness, transportability, or patient benefit.

## Exact source bindings and availability

All source files are ordinary read-only CSVs; archive member is null/ordinary file. Join once on canonical `eid`, one-to-one, and reject duplicate/missing keys or disagreement in overlapping fields.

- `population`: `[internal dataset path]`, [source checksum]; table `population`, schema `datasets/ukb/table-38565c9e35e7cb6c.json`, schema [source checksum]; key `eid`; use `31-0.0`.
- `assessment`: `[internal dataset path]`, [source checksum]; table `assessment`, schema `datasets/ukb/table-901ef6c7ddce2d51.json`, schema [source checksum]; key `eid`; use `53-1.0,21003-1.0,21001-1.0,46-1.0,47-1.0`.
- `biological_samples`: `[internal dataset path]`, [source checksum]; table `biological_samples`, schema `datasets/ukb/table-c6b666d905f3b02f.json`, schema [source checksum]; key `eid`; use `30500-1.0,30505-1.0,30510-1.0,30700-1.0,30720-1.0`; `30515-1.0` is absent and must not be invented.
- `health_outcomes`: `[internal dataset path]`, [source checksum]; table `health_outcomes`, schema `datasets/ukb/table-3cfae45e0905b0e3.json`, schema [source checksum]; key `eid`; use `41270-0.0...41270-0.258`, `41280-0.0...41280-0.258`, and `40000-0.0,40000-1.0`.

The UKB snapshot is `[source checksum]`; full catalog is `[internal dataset path]`, [source checksum]. All four schemas declare `temporal_columns=[]`; encoded dates are parsed explicitly. HCC, MIMIC-IV (including notes), and eICU remain directly accessible but cannot join to UKB `eid` and are not used for this UKB island.

## What the computation cannot establish

This Harbor experiment can check source/header/schema hashes, one-to-one joins, exact parent population/list identity, code/date pairing, N00–N99 exclusion, t1/t9/death chronology, fixed-denominator yields, bootstrap uncertainty, anti-vacuity gates, and interpretation/output consistency. It cannot establish that an array entry is a true encounter, that an N18 or non-N code is clinically correct, that absence of a death or code means absence of disease, that UACR preceded a real clinical decision, that the lists cause testing, or that testing changes management or patient outcomes.

Stronger conclusions require repeated clinically timed UACR/eGFR and measured GFR, complete censoring/emigration and kidney-replacement capture, outpatient/primary-care linkage, encounter-level identifiers, chart/nephrologist adjudication, order/result timestamps, treatment/action and medication data, workflow burden/harms/costs, external validation, and a prospective implementation or randomized testing-strategy study.
