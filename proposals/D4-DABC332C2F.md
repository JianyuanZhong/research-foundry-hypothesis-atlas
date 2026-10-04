# Episode 47: nonrescuing nine-year prognosis qualification of nested grip after FFM

## Decision, unresolved weakness, and one child hypothesis

A substantive child is justified. The assessed-valid parent [prior hypothesis] controls its exact O1_hold population, t1 boundary, baseline-only AFG fit, fixed AFG1 and AF1 rosters, 466-assay capacity, H1/D1 and observed-low-UACR estimands, paired uncertainty, margins, serial hierarchy, and supportive/adverse/inconclusive labels. This child never refits, reranks, refills, or changes those objects.

The clinically consequential weakness is that Episode 35 can support only contemporaneous, equation-defined allocation. AFG1 could outperform AF1 for visit-1 H1/D1 because grip tracks non-GFR creatinine determinants, yet its 31 substituted participants might have no greater subsequent recorded kidney-disease burden.

The single new hypothesis is:

> In the exact 2,334-person O1_hold population and at the same fixed 466-person capacity, does frozen AFG1 yield at least one more participant than frozen AF1 with a first recorded inpatient N18 code after t1 and before death within nine calendar years, with uncertainty excluding no enrichment?

At n1=466, one net event is 1000/466=2.145922746781116 per 1,000 selected. The primary endpoint is direct recorded N18 yield, not H1 multiplied by N18. H1-by-N18 and observed-low-UACR-by-N18 cross-tabs are attribution diagnostics only. This tests whether the nested grip increment has a later kidney-code anchor without making an underpowered claim that a rare later event must also satisfy a rare contemporaneous phenotype.

## Supported evidence, unresolved claim, and advance

The strongest evidence currently supports less than the hypothesis.

1. The parent outcome-blindly authenticates O1_hold=2,334, n1=466, all controlling model objects, AFG1 and AF1 rosters, 435 shared participants, and 31 swaps in each direction. This establishes deterministic computability and nontrivial reassignment, not outcome superiority.
2. Managed preflight [research job] read only frozen membership and source headers. It confirmed roster columns exactly eid,AFG1_selected,AF1_selected,A1_selected,AG1_selected; 2,334 rows; 466 selections per new list; 435 overlap; 31 swaps each way; and unique physical presence of 53-1.0, all 259 41270/41280 pairs, and both death dates. Output analysis/episode47_prognosis_header_preflight.json has [source checksum]. It read no cystatin, diagnosis, diagnosis-date, death-date, event, numerator, or yield value.
3. The inherited rank-blind all-O1_hold audit found 114 nine-year recorded N18 events, including 96 among participants with observed visit-1 UACR below 3.0 mg/mmol. It did not inspect AFG1/AF1-specific counts. This supports endpoint availability, not the policy contrast.
4. Lees et al. (JAMA Network Open 2022; DOI 10.1001/jamanetworkopen.2022.38300; PMCID PMC9597396) was acquired and inspected from Europe PMC full-text XML source [source checksum], retrieved-file [source checksum]. In UKB participants with albumin below 30 mg/g and eGFRcr at least 45, cystatin-based classification stratified cardiovascular and mortality risk over median 11.5 years; ten-year kidney failure probability was below 0.1%. This supports prognostic relevance of cystatin reclassification in low albuminuria, not this allocation rule, N18 definition, margin, or benefit.
5. The current Europe PMC core record for Estrella et al. (JAMA 2025; DOI 10.1001/jama.2025.17578; PMID 41202182; PMCID PMC12595547; source [source checksum]) and a focused PubMed page extraction were inspected. The abstract reports an individual-participant meta-analysis in which eGFRcys at least 30% below eGFRcr was associated with kidney failure with replacement therapy among outpatients (HR 1.29, 95% CI 1.13-1.47). Full-text acquisition returned HTTP 404; no article body, supplement, or detailed outcome adjudication is claimed as read. This supports general prognostic relevance of large negative discordance, not AFG1 versus AF1 or an inpatient N18 surrogate.

No visit-1 cystatin value, H1, D1, N18 code/date value, death date, selected-list numerator, yield, interval, or policy label was opened in designing this child. The unresolved claim remains falsifiable. The advance over Episode 35 is temporal clinical anchoring of the exact nested allocation contrast, not a new prediction model or causal strategy evaluation.

The research-ambition README was inspected. None of its demonstrations supplies topic evidence. The cancer main article and full STAR Methods remain unavailable and are not claimed as read.

## Frozen population, policies, capacity, and visit boundary

Incorporate the complete parent and support package unchanged. Canonical eid is a positive decimal string with no alternate representation. In compact form, O1 requires sex 31-0.0 in {0,1}; age 21003-1.0 from 40 through 69; strictly parseable t1=53-1.0; positive finite BMI 21001-1.0; at least one positive finite grip value 46-1.0/47-1.0; positive finite creatinine 30700-1.0; full-precision race-free 2021 eGFRcr1 in [60,90); and no position-paired inpatient N17 or N18 code/date on or before t1. A qualifying pre-t1 N17/N18 code with blank or invalid paired date retains the inherited exclusion/integrity rule.

O1_hold is O1 with int(SHA256("ukb-grip-cys-v3|"+eid),16) mod 100 >= 60. It is exactly the parent-authenticated 2,334 eids; O1 need not belong to baseline O. Capacity is floor(0.20*2334)=466.

AF1 is the frozen A+FFM list and AFG1 the frozen A+FFM+grip list. Their construction, transforms, coefficients, fallback rules, score precision, tie digest, and ordering are inherited and immutable. The controlling combined membership artifact is parents/[prior hypothesis]/support-4-episode35_AFG1_AF1_frozen_visit1_rosters.csv, [source checksum], with columns exactly eid,AFG1_selected,AF1_selected,A1_selected,AG1_selected. It has 2,334 rows; each selection column contains exactly 466 ones; AFG1 and AF1 overlap on 435 eids. The AFG manifest, ranked roster, and fitting script retain parent hashes [source checksum], [source checksum], and [source checksum]. AF1 and all upstream A1/AG1 artifacts remain authenticated by the parent package.

Missing events, deaths, cystatin, UACR, or chronology failures never change membership or denominator. Any artifact mismatch makes the child noncomputable/inconclusive and does not authorize regeneration.

## Nine-year endpoint and temporal rules

For participant i, t1_i is the strictly parsed date in 53-1.0. Define t9_i as t1 plus nine calendar years, mapping February 29 to February 28 when the terminal year is not a leap year. The inherited O1_hold t1 range is 2012-08-01 through 2013-06-07, so t9 ranges 2021-08-01 through 2022-06-07. The inherited audit found valid N18 pairs through 2022-10-31 and valid death dates through 2022-12-19. This establishes a common source-span window, not complete individual follow-up.

In the health_outcomes row for the same eid, pair 41270-0.j only with 41280-0.j for j=0,...,258. Trim and uppercase each code. A qualifying event begins with N18; N17 does not count. Strictly parse the paired date. Let T18_i be the earliest qualifying N18 date strictly after t1. Let Tdeath_i be the earliest strictly parsed date among 40000-0.0 and 40000-1.0; do not use 40001 or 40002 as death dates.

A nonblank unparseable date paired to N18, nonblank unparseable death date, death on/before t1, or code/date positional-integrity failure leaves the person and roster fixed but makes the prognosis layer inconclusive/noncomputable. Same-day death competes.

For chronology-valid i:

K18_9,i = 1{t1_i < T18_i <= t9_i and (Tdeath_i is blank or T18_i < Tdeath_i)}.

Otherwise K18_9=0. N18 on t1 is not incident; N18 exactly on t9 counts. Death before or on N18 remains in the denominator and makes K18_9=0. N17 neither counts nor censors. Blank arrays mean no recorded inpatient N18 in this source/window, not clinical absence of CKD.

No emigration, primary-care, outpatient, dialysis, transplant, or person-specific administrative censoring field is available. K18_9 is therefore a recorded fixed-window event indicator, not an unbiased clinical cumulative-incidence endpoint.

## Estimand, baseline, attribution, and uncertainty

For fixed policy p in {AFG1,AF1}:

Y_K(p)=1000*sum(i in S_p) K18_9,i/466

and

Delta_K=Y_K(AFG1)-Y_K(AF1).

AF1 is the prespecified baseline. Report each fixed-list numerator and yield, Delta_K, descriptive ratio when the AF1 numerator is nonzero, overlap/Jaccard, AFG-only and AF-only event counts, and:

Delta_K=(31/466)*1000*(mean_K_AFGonly-mean_K_AFonly).

Never divide the primary estimand by survivors, observed follow-up, reassigned slots, events, H1 positives, or low-UACR participants. Report Aalen-Johansen nine-year cumulative incidence with death as competing event only descriptively, explicitly noting unavailable censoring/emigration.

Cross-tab K18_9 by unchanged parent H1 and observed-UACR categories in each list and directional swap. Define J_H=H1*K18_9 and J_L=L1*K18_9; report fixed-denominator yields and differences only as descriptive attribution diagnostics. They receive no label and cannot rescue, reverse, mediate, or replace Delta_K or a parent result. For missing H1, use the parent's one-shared-latent-label sharp bounds for J_H; never assign policy-specific labels to a shared eid.

Use exactly the parent's 2,000 paired participant bootstrap draws over canonical-eid-sorted O1_hold. For zero-based b, seed NumPy Generator(PCG64DXSM(full_unsigned_big_endian_SHA256(UTF8("ukb-grip-visit1-bootstrap-v1|"+b)))); draw 2,334 row indices with replacement and convert to shared multiplicities. Keep memberships and denominator 466 fixed. Never refit, rerank, refill, condition on survival, or bootstrap policies independently.

F47_N18={Delta_K} is a separate single-component family. Report point estimate, bootstrap SE, two-sided 95% interval, and one-sided 95% lower and upper limits using the inherited studentized convention. If studentization fails, use the inherited componentwise percentile fallback and mark it. Fewer than 95% finite draws, nonfinite/nonpositive SE, seed mismatch, or identity failure is inconclusive.

Before supportive or adverse classification require exact source/header/descriptor/catalog hashes; canonical one-to-one joins; exact O1_hold, capacity, roster hashes/counts; no outcome-dependent selection; valid chronology; exact endpoint/swap identities; at least 15 K18_9 events in the list union; at least 4 in each list; and at least 5 across the symmetric difference. These inherited nine-year anti-vacuity gates are not a power guarantee. Gate failure is inconclusive, never adverse.

## Falsification and interpretation

nested_grip_after_FFM_N18_9_supportive requires every gate, point Delta_K >= +2/1,000, and one-sided 95% lower limit strictly >0. Support means only that fixed AFG1 has higher nine-year recorded inpatient N18 yield than AF1 at this quota. It does not establish that grip caused an event, that cystatin testing prevents one, or that N18 is an adjudicated incident CKD event.

nested_grip_after_FFM_N18_9_adverse requires every gate and one-sided 95% upper limit strictly <+2/1,000. It falsifies the prespecified material prognosis-enrichment claim. It does not prove AF1 superiority, equivalence, absence of biochemical grip information, or no value of cystatin C.

All other results are nested_grip_after_FFM_N18_9_inconclusive, including boundary equality, an interval spanning +2, sparse union/list/swap events, chronology/source failure, or degenerate uncertainty. A negative point estimate with a wide interval is inconclusive. Inconclusive is not equivalence.

Always emit every parent AG1:A1, Episode-33, and Episode-35 label unchanged and first. This child is strictly nonrescuing:

- If parent episode35_grip_beyond_FFM_and_albuminuria_supported and N18 supports, emit episode47_nested_grip_increment_biochemical_and_N18_supported.
- If that parent supports but N18 is adverse, emit episode47_nested_grip_increment_biochemical_supported_N18_adverse.
- If that parent supports but N18 is inconclusive, emit episode47_nested_grip_increment_biochemical_supported_N18_unresolved.
- Otherwise emit episode47_parent_hierarchy_not_supported_N18_nonrescuing with the exact upstream reason; N18 is descriptive in that branch.

Support advances the case only to prospective adjudicated testing. Adverse evidence weakens the claim that the biochemical gain has later kidney-code relevance. Inconclusive evidence leaves the anchor unresolved and does not erase a correctly supported parent biochemical result.

## Exact read-only source binding

All UKB sources are ordinary CSV files with archive member null, one row per canonical eid. Join horizontally one-to-one on eid; reject duplicates, missing O1_hold keys, and disagreements in overlapping loaded fields. Sources remain read-only; derived outputs remain in the workspace.

- population: [internal dataset path]; source [source checksum]; descriptor datasets/ukb/table-38565c9e35e7cb6c.json; descriptor-file [source checksum]; internal schema [source checksum]; key eid; required 31-0.0,21022-0.0.
- assessment: [internal dataset path]; source [source checksum]; descriptor datasets/ukb/table-901ef6c7ddce2d51.json; descriptor-file [source checksum]; internal schema [source checksum]; key eid; required 53-0.0,53-1.0,21003-1.0,21001-0.0,21001-1.0,46-0.0,47-0.0,46-1.0,47-1.0 and duplicate FFM audit 23101-0.0,23101-1.0.
- main: [internal dataset path]; source [source checksum]; descriptor datasets/ukb/table-e4a9e4d8baa71a9d.json; descriptor-file [source checksum]; internal schema [source checksum]; key eid; canonical FFM 23101-0.0,23101-1.0.
- biological_samples: [internal dataset path]; source [source checksum]; descriptor datasets/ukb/table-c6b666d905f3b02f.json; descriptor-file [source checksum]; internal schema [source checksum]; key eid; parent 30500/30505/30510/30700/30720 at instances 0 and 1; 30515-1.0 absent.
- health_outcomes: [internal dataset path]; source [source checksum]; descriptor datasets/ukb/table-3cfae45e0905b0e3.json; descriptor-file [source checksum]; internal schema [source checksum]; key eid; paired 41270-0.0...41270-0.258 with 41280-0.0...41280-0.258; deaths 40000-0.0,40000-1.0.

Full catalog: [internal dataset path], [source checksum]. UKB snapshot: [source checksum]. Descriptors declare temporal_columns=[]; encoded dates require explicit parsing and do not establish specimen/order/result chronology. The preflight physically verified every newly required field.

HCC, MIMIC-IV including notes, and eICU remain directly accessible read-only through datasets/{hcc,mimic,eicu}/README.md. They have no UKB eid linkage and are not mixed into this experiment. No private record or note was used in a public query.

## Compiler/verifier contract and nonidentifiability

The compiler authenticates and executes the complete parent first, freezes all rosters before any outcome access, then computes the child endpoint. Population, horizon, estimand, margin, uncertainty, event gate, or interpretation changes are scientific changes, not mechanical repairs.

Computationally checkable claims are source/catalog/descriptor/header hashes; exact field presence; canonical joins; O1_hold/t1 reconstruction; artifact hashes and roster counts; no cystatin/N18/death access before roster freeze; positional pairing; N18 prefix; t1/t9 boundaries; death precedence; fixed numerators/yields/swap identities/descriptive decompositions; paired seeds/draws; event gates; intervals; labels; and whether conclusions follow outputs.

Adversarial fixtures reject outcome-dependent refitting/ranking/refill; using AG1:A1 or AFG1:A1 instead of AFG1:AF1; changing n1; survivor, observed-follow-up, low-UACR, H1, event, or swap denominators; nonmatching code/date positions; counting N17; including N18 on t1 or after t9; letting same-day N18 beat death; using 40001/40002 as death dates; dropping deaths; independent policy bootstraps; ratio-only support; gate failure called adverse; parent rescue; or blank arrays called absence of clinical CKD.

Interpretation fixtures accept bounded supportive, adverse, and inconclusive conclusions and reject measured-GFR accuracy, incident/persistent CKD diagnosis, kidney-failure/KRT ascertainment, a grip-specific mechanism, causal benefit of cystatin ordering, prevented events, treatment actionability, complete capture, cost-effectiveness, safety, fairness, transportability, or routine adoption. Verification must not reward confirmation.

Automatic computation cannot identify specimen/order/result chronology; migration or individual loss to follow-up; outpatient/primary-care CKD; dialysis/transplant; measured GFR; repeat eGFR/UACR persistence; why grip changes rank; whether N18 is new, correct, or adjudicated; downstream actions; or patient benefit. Stronger claims require linked primary-care and KRT/censoring data, repeated clinically timed biomarkers, measured GFR, chart/nephrologist adjudication, workflow/action/cost/harms/equity review, external validation, and ultimately a prospective implementation or randomized testing-strategy study.
