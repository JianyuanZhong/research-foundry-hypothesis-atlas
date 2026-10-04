# Episode 68: non-rescuing H1-to-N18 clinical-validity qualification of the frozen AG1-versus-AF1 experiment

## Decision and unchanged parent design

This is a scientific child of assessed-valid [prior hypothesis], with assessed-valid [prior hypothesis] retained as the executable AF1 parent. It adds one prespecified joint clinical-validity endpoint. It does not change O, O1, O1_hold, the development split, time zero, predictors, transformations, A1/AG1/AF1 fitting, coefficients, ranked rosters, n1=466 quota, parent H1/D1 hierarchy, existing five-year N18 endpoint, competing-death definition, parent bootstrap draws, parent multiplicity families, source bindings, or evidence limits.

The clinical decision is whether the UACR-plus-grip AG1 rule merits prospective testing as a selective cystatin-C strategy after routine covariates, UACR and whole-body bioimpedance FFM are available. The existing N18 endpoint asks whether AG1's fixed 466-person list has more later recorded inpatient N18 events than the otherwise matched AF1 list. That endpoint can still be nonspecific: an N18 difference might arise from frailty, health-care contact, or other features of the list rather than from the intended cystatin-defined reclassification target.

The added qualification asks:

> At the same fixed 466-assay capacity, is any AG1-versus-AF1 enrichment of five-year first recorded inpatient N18-before-death events concentrated in participants who are actual equation-defined visit-1 H1 reclassification targets?

The primary new object is the joint person-level endpoint J18_i = H1_i times E18_i on the unchanged fixed rosters, not an analysis that drops people without H1 or compares only the selected H1 subsets.

A supportive joint result can qualify the existing N18 signal as more specifically aligned with the intended H1 target. It cannot rescue an unsupported AG1:A1 biochemical hierarchy, the existing N18 endpoint, or any upstream low-UACR result. An adverse or inconclusive joint result is scientifically informative: it says that the recorded N18 signal is not shown to be concentrated in the equation-defined target, or that available data are too sparse to decide.

## Evidence already supported and unresolved claim

The strongest available evidence supports plausibility and computability, not AG1 superiority or clinical validity. The inspected full texts of Chen et al. (Kidney Medicine 2024; PMCID PMC10986041), Lees et al. (JAMA Network Open 2022; PMCID PMC9597396), and Liu et al. (Clinical Kidney Journal 2025; PMCID PMC11997436) support, respectively, common internally predictable creatinine-cystatin discordance, prognostic relevance of cystatin-based reclassification in relevant UK Biobank analyses, and an association literature in which lower eGFRcys relative to eGFRcr is clinically consequential. They do not establish this fixed-capacity AG1-versus-AF1 contrast, measured-GFR accuracy, incident or persistent CKD, a grip-specific mechanism, or benefit from selective testing.

Outcome-blind private audits inherited by the parents support O1=5,823, O1_hold=2,334, n1=466, exact frozen AG1/AF1 membership, 435-person overlap and 31 directional swaps. They support availability of the required equation fields and 259 same-position inpatient code/date pairs, and an all-holdout feasibility count of 40 five-year N18-before-death events. They do not support or refute any selected-list H1, J18, N18, death, or AG1-versus-AF1 result. During this design turn I inspected the dataset guide, cataloged schemas and parent artifacts; I did not read sealed policy-specific outcomes or compute a policy yield.

The unresolved claim is narrower and falsifiable: among the fixed-capacity lists, AG1 will have a material excess of people who both meet H1 at visit 1 and subsequently have E18, beyond the one-event-per-466-slot resolution, while preserving the existing N18 endpoint and upstream hierarchy. A positive result would be a downstream target-validity qualification, not evidence of causal benefit. A negative result would weaken the interpretation that a biochemical AG1 signal has a clinically relevant kidney-record correlate in the intended target.

## Frozen population, exposure assignment and chronology

The compiler must first reproduce the complete b7/d44 design. The canonical key is positive decimal eid; all tables are one-to-one horizontally joined on canonical eid. O1 requires:

- 31-0.0 in {0,1};
- 21003-1.0 age 40 through 69;
- strictly parsed 53-1.0 visit-1 date t1_i;
- positive finite BMI 21001-1.0;
- at least one positive finite grip value in 46-1.0/47-1.0;
- positive finite serum creatinine 30700-1.0;
- full-precision 2021 race-free eGFRcr1 in [60,90);
- no exactly position-paired inpatient N17 or N18 code/date on or before t1_i.

O1_hold is exactly O1 with int(SHA256("ukb-grip-cys-v3|" + eid),16) mod 100 >= 60.

The frozen identities are O1=5,823, O1_hold=2,334 and n1=floor(0.20*2334)=466. AG1 and AF1 each contain exactly 466 eids, overlap in 435, and have 31 directional swaps. The canonical membership artifacts remain:

- support-27-episode33_AF1_frozen_visit1_rosters.csv, [source checksum], with eid,AF1_selected,A1_selected,AG1_selected;
- inherited support-8-support-13-support-12-episode27_frozen_visit1_rosters.csv, [source checksum], with the O1_hold/A1/AG1 membership identity.

No H1, D1, N18, death or joint endpoint may refit, rerank, refill, exclude, alter capacity, select the five-year horizon, or change any inherited gate.

For each person, define t5_i as t1_i plus five calendar years, mapping February 29 to February 28 when the terminal year is not leap. Retain the parent's chronology exactly:

- trim and uppercase 41270-0.j and pair it only with 41280-0.j, for j=0,...,258;
- T18_i is the earliest strictly parsed date whose same-position code begins exactly N18;
- N17 is not an N18 event and does not censor it;
- Tdeath_i is the earliest strictly parsed nonblank date among 40000-0.0 and 40000-1.0;
- E18_i=1 iff t1_i<T18_i<=t5_i and either death is absent or T18_i<Tdeath_i;
- death on or before N18, including same-day death, prevents E18=1;
- an N18 on t1 is pre-index and an N18 after t5 is outside the endpoint.

The existing parent competing-death state C5, its label and its inference remain unchanged. Death never creates an E18 or J18 event. Nonblank N18 codes without valid paired dates, nonblank unparseable death dates, death on or before t1, duplicate-source disagreement, or any inherited chronology-integrity failure makes the endpoint layer noncomputable/inconclusive; these states are not imputed as nonevents.

## Exact H1 and joint endpoint

Use the parent's positive finite visit-1 cystatin 30720-1.0, inherited sex, age and creatinine, and the race-free 2021 equations. With serum creatinine Scr=30700-1.0/88.4 mg/dL:

eGFRcr-cys1 = 135*min(Scr/k,1)^alpha*max(Scr/k,1)^(-0.544)*min(Scys/0.8,1)^(-0.323)*max(Scys/0.8,1)^(-0.778)*0.9961^age*(0.963 if female else 1),

where (k,alpha)=(0.7,-0.219) for female and (0.9,-0.144) for male.

The unchanged parent definition is H1_i=1 iff eGFRcr-cys1<60. Invalid, nonpositive or nonfinite visit-1 cystatin makes H1 missing. It never changes O1_hold membership, either roster, the denominator, a score or a rank. H1 is a one-record equation-defined phenotype, not measured GFR, incident CKD, persistent CKD, sarcopenia or a diagnosis.

For chronology-valid participants define the new joint endpoint:

J18_i=1 iff H1_i=1 and E18_i=1.

The partial-label rule is exact and conservative:

- observed H1=1 and E18=1 gives J18=1;
- observed H1=0 gives J18=0 regardless of E18;
- E18=0 gives J18=0 regardless of H1, including missing H1;
- missing H1 with E18=1 gives an unknown J18, not zero.

Thus missingness can affect the joint contrast only in people with a valid qualifying N18-before-death event. Use one shared latent H1 value for a missing person wherever that person appears in AG1 and AF1; never assign separate missing labels by policy. This preserves the parent shared-person missing-label logic.

A conditional fraction among observed H1 targets may be reported descriptively as sum(J18) / sum(H1) within each list, with a missing-H1 range when appropriate. It must not be the policy estimand, a support criterion, or a rescue. Conditioning on post-assignment H1 counts would make the selected H1 subset and its missingness part of the exposure definition and could create a misleading contrast.

## Joint estimands and shared missingness bounds

For p in {AG1, AF1}, with immutable S_p and denominator 466, define under any completion of missing H1:

Y_J(p)=1000*sum(i in S_p) J18_i/466.

The new contrast is Delta_J=Y_J(AG1)-Y_J(AF1).

Let c_i=I(i in S_AG1)-I(i in S_AF1), which is -1, 0 or +1. Let N_J_obs be the observed joint contrast numerator. For missing-H1 participants with E18=1, exact sharp bounds are:

N_J_lower = N_J_obs + sum(min(0,c_i)),
N_J_upper = N_J_obs + sum(max(0,c_i)),

with sums only over missing-H1 participants having E18=1. Missing-H1 participants with E18=0 contribute zero to both bounds; shared roster members cannot contribute different latent values to AG1 and AF1. Divide both bounds by 466 and multiply by 1000 to obtain Delta_J_lower and Delta_J_upper. Report list-specific observed J numerators, H1 counts, missing-H1 counts, the bounds, overlap/Jaccard, AG-only and AF-only J counts, and the exact 31-swap identity whenever swap means are defined.

The new planning margin is the inherited resolution-aware one-event margin m_J=1000/466=2.145922746781116 joint recorded H1-to-N18 events per 1,000 assay slots. It is not a validated clinical utility, cost, or patient-benefit threshold. Never divide by H1 counts, observed joint events, survivors, complete cases, or directional swaps for the primary estimand.

## Inference and multiplicity

The existing E18/N18 result remains exactly the b7 F66_N18 one-component analysis: its point estimate, studentized paired 2,000-draw interval, margin, gates, competing-death diagnostic and label are not recalculated under a different family.

For J18 use the same canonical-eid-sorted O1_hold resampling, same 2,000 shared participant-multiplicity draws, PCG64DXSM construction and inherited seed namespace ukb-grip-visit1-bootstrap-v1| plus zero-based draw index. Do not refit or bootstrap AG1 and AF1 independently. In each draw recompute E18, the shared missing-H1 sharp lower/upper joint contrasts, Delta_J lower/upper and swap/decomposition identities with the fixed denominator 466.

Add a distinct one-component family F68_J18={Delta_J}. It uses the parent's studentized one-sided 95% lower limit for the conservative lower-bound series and one-sided upper limit for the conservative upper-bound series; use the parent's marked percentile fallback only when the inherited studentization condition fails. Because F68_J18 has exactly one prespecified component, it requires no new max-t dimension and does not retroactively widen or narrow F33_AF or F66_N18. Report seed namespace, draw count, family order/hash, finite-draw count, SE, two-sided interval, one-sided limits and fallback reason. The final qualification is a conjunction of already-frozen parent/N18 decisions with this prespecified J18 decision, not an exploratory selection among downstream endpoints.

## Feasibility gates and exact result taxonomy

All inherited source, join, roster, chronology, N18, parent H1/D1, AF1, bootstrap and no-leakage gates remain mandatory. Add these J18-specific anti-vacuity gates before supportive or adverse interpretation:

1. at least 5 observed J18 events in S_AG1 union S_AF1;
2. at least 2 observed J18 events in each list;
3. at least 2 observed J18 events across S_AG1 symmetric_difference S_AF1, because overlap events cancel from Delta_J;
4. less than 1% missing H1 labels in O1_hold, with identical missingness by policy for shared eids;
5. at least 95% finite paired bootstrap draws and positive finite variance for required lower and upper series;
6. all exact joint-bound, swap, roster and decomposition identities pass.

These are anti-vacuity gates, not a power claim. No outcome-blind aggregate currently establishes the H1-by-N18 intersection count, so the 40 all-holdout E18 feasibility count must not be presented as J18 feasibility. If any J18 gate fails, label the qualification inconclusive rather than changing the endpoint, pooling H1-missing cases, substituting ten-year events, or lowering the threshold after outcomes are opened.

The standalone J18 label is:

- h1_to_n18_joint_supportive only if all inherited and J18 gates pass, the conservative lower-bound point Delta_J_lower is at least m_J, and its one-sided 95% lower limit is strictly greater than 0;
- h1_to_n18_joint_adverse only if all inherited and J18 gates pass and the conservative upper-bound one-sided 95% upper limit is strictly below m_J;
- h1_to_n18_joint_inconclusive_unresolved otherwise, including sparse joint events, missingness or integrity failure, degenerate resampling, boundary equality, a lower limit that does not exclude zero when the point reaches the margin, or an upper limit that still includes the margin.

The support rule mirrors the existing E18 resolution rule: a lower-bound point must reach one net whole event per 466 slots, while uncertainty must exclude no positive joint contrast. The adverse rule is evidence against the prespecified material joint-enrichment claim, not evidence that AF1 is superior, equivalent, safer, cheaper or beneficial.

For interpretation, emit all inherited labels first and never rewrite them. Then emit the existing E18 label and new J18 label. Emit a final nonrescuing synthesis:

- ag1_clinical_validity_qualified only if unchanged upstream AG1:A1/H1-D1 hierarchy is supported, E18 is n18_targeting_supportive, J18 is h1_to_n18_joint_supportive, and no inherited competing-death concern exists;
- ag1_clinical_validity_qualified_with_competing_death_concern under the same support conditions when the death diagnostic is competing_death_AG1_enriched; this requires clinical adjudication and is not unqualified support;
- ag1_n18_supported_but_h1_link_unresolved when upstream hierarchy and E18 are supportive but J18 is inconclusive;
- ag1_n18_supported_but_h1_link_adverse when upstream hierarchy and E18 are supportive but J18 is adverse;
- ag1_joint_signal_nonrescuing when J18 is supportive but E18 or the upstream hierarchy is adverse, inconclusive or not supported; preserve the exact earlier failure;
- ag1_clinical_validity_inconclusive when required upstream decisions are unresolved and J18 does not establish a separate adverse result.

A J18 adverse result must not relabel an E18 supportive result as AF1 superiority or equivalence. A J18 supportive result must not rescue an E18 adverse/inconclusive result, failed H1/D1 hierarchy, or failed low-UACR parent. This is a qualification layer, not a replacement endpoint.

## Exact source bindings and availability

Use the same read-only UKB snapshot and catalog as both parents:

- snapshot [source checksum];
- full catalog [internal dataset path], [source checksum];
- every source is a read-only ordinary CSV with archive member null (not an archive), every table has key eid and temporal_columns=[].

| table | exact source path and source SHA-256 | descriptor and internal schema | fields used |
|---|---|---|---|
| population | [internal dataset path]; [source checksum] | datasets/ukb/table-38565c9e35e7cb6c.json; schema [source checksum] | eid, 31-0.0, 21022-0.0 |
| assessment | [internal dataset path]; [source checksum] | datasets/ukb/table-901ef6c7ddce2d51.json; schema [source checksum] | eid, 53-0.0, 53-1.0, 21003-1.0, 21001-0.0/1.0, 46/47-0.0/1.0, 23101-0.0/1.0 |
| main | [internal dataset path]; [source checksum] | datasets/ukb/table-e4a9e4d8baa71a9d.json; schema [source checksum] | eid, AF1 23101-0.0/1.0; duplicate audit 40000-0.0/1.0 and all 41270-0.j/41280-0.j |
| biological_samples | [internal dataset path]; [source checksum] | datasets/ukb/table-c6b666d905f3b02f.json; schema [source checksum] | eid, 30500/30505/30510/30700/30720 at 0.0 and 1.0; 30515-1.0 absent and forbidden |
| health_outcomes | [internal dataset path]; [source checksum] | datasets/ukb/table-3cfae45e0905b0e3.json; schema [source checksum] | eid, all 259 41270/41280 pairs, 40000-0.0, 40000-1.0 |

Descriptor JSON file hashes authenticated by the parents are: population [source checksum], assessment [source checksum], main [source checksum], biological_samples [source checksum], and health_outcomes [source checksum].

The main and health_outcomes sources physically contain the 520 endpoint fields, but the prior header-only audit read no participant rows. At execution, compare all 520 fields for every O1_hold eid using identical trim/null/date normalization; report raw disagreements and use health_outcomes as canonical only if duplicate agreement passes. A duplicate disagreement makes the endpoint layer inconclusive. The endpoint sources have no archive members or temporal-column metadata that can establish specimen/order/result chronology.

HCC, MIMIC-IV including notes, and eICU remain directly available read-only but have no UKB eid linkage and are not joined. No private rows or clinical notes are sent to public search.

## Pitfalls, falsification criteria and required outputs

The child is noncomputable/inconclusive if any catalog, snapshot, source, descriptor, schema, archive-member, header, key, parent-artifact or roster identity fails; joins are not one-to-one; duplicate endpoint fields disagree; code/date positions are mismatched; a pre-index N17/N18 exclusion is violated; an N18 on t1 or after t5 is counted; same-day death is treated as after N18; N17 is substituted; missing H1 is treated as observed H1=0 for the joint contrast; H1 is redefined using a different equation or threshold; the denominator is changed; a conditional H1-target denominator replaces 466; any outcome leaks into fitting/ranking/capacity; or a favorable result is selected after looking at outcomes.

Required outputs include all inherited provenance, population, model, roster, AF1 and hierarchy hashes; row/key/join/exclusion/date counts; exact t1/t5 construction and date spans; duplicate-source disagreements; H1 observed/missing counts and equation audit; E18, C5 and J18 states for every O1_hold row; observed and sharp-bound list/overlap/swap numerators, fixed-denominator yields and optional descriptive target-conditional fractions; bootstrap seeds/draws/family/fallbacks; inherited labels, J18 label, final synthesis and machine-linked reasons.

## Verifier contract and interpretation limits

The verifier must test correct J18 computation as well as unsupported conclusions. Fixtures must cover correct joint support, correct joint adversity, sparse/boundary/missingness-failing inconclusiveness, E18 support plus J18 adverse or inconclusive, J18 support with E18 or upstream failure, missing H1 with E18=0 versus E18=1, one shared latent label for a person in both rosters, and all chronology, denominator, roster, N17 and leakage errors.

Correct arithmetic paired with claims of measured-GFR accuracy, persistent/adjudicated CKD, H1-mediated mechanism, causal testing benefit, routine adoption, safety, cost-effectiveness, fairness, transportability or patient benefit must be rejected. An N18-or-death composite, conditional-H1 denominator, mispaired code/date, t1/t5 error, same-day death reversal, changed roster, changed n1 or outcome leakage must also be rejected.

Computationally checkable claims are source and artifact identity, canonical joins, frozen population and rosters, equations, H1 missingness, code/date chronology as encoded, first N18-before-death, joint bounds, fixed-denominator arithmetic, paired draws, family membership, gates, labels and whether prose follows computed output. Automatic verification cannot establish complete outcome capture, censoring/emigration, true incident or persistent CKD, clinical validity of an inpatient N18 code, measured GFR, specimen chronology, actual assay ordering, H1-mediated mechanism, downstream action, workflow burden, cost, safety, equity, transportability or patient benefit.

Those stronger conclusions require outpatient/primary-care/kidney-replacement/cause-specific-mortality and censoring linkage; repeated clinically timed cystatin, creatinine and UACR; measured GFR; order/result/action records; nephrologist or chart adjudication; external validation; workflow, cost, harm and equity review; and ultimately a prospective implementation or randomized testing-strategy study.

This child is sound only as a nonrescuing downstream qualification. A favorable J18 result would nominate a more specific prospective clinical-validity study; it would not establish that AG1 improves patient outcomes.
