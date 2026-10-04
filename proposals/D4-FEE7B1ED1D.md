> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 29: observed-low-UACR biochemical complementarity of incremental grip

## Controlling parent and one substantive addition

This is a child of assessed-valid `[prior hypothesis]`. Its complete proposal and all attached Episode-16/17/18/19/23/27 executable specifications, model constants, transforms, penalties, coefficients, exact O1_hold membership, exact n1=466 A1/AG1/G1 rosters, hashes, temporal rules, outcomes, missing-label bounds, paired bootstrap, hierarchy, falsification rules, and evidence limits are attached and controlling. This child changes no population, eligibility criterion, time zero, model, fit, score, selected participant, capacity, primary H1/D1 estimand, N18 endpoint, parent family, parent label, or conclusion.

It adds one nonrescuing biochemical complementarity challenge on the exact frozen AG1 and A1 lists:

> Among the exact 2,334-person O1_hold population and fixed 466-assay capacity, does allowing grip in the baseline-trained AG1 rule materially increase visit-1 combined-eGFR<60 yield over the separately trained A1 rule specifically among participants with an actually observed visit-1 UACR below 3.0 mg/mmol?

The parent establishes the primary add-grip question, but its total H1 result could in principle be driven by participants with already elevated albuminuria or by the score fallback among participants without a usable urine result. That would still be an equation-defined allocation result, but it would be weaker evidence that grip helps find otherwise less visible kidney-filtration discordance. This child asks whether the biochemical increment itself—not only the sparse downstream N18 endpoint—extends to the observed-low-UACR group. It does not reselect within that group and does not change the 466-slot denominator.

## Evidence-supported claim, unresolved claim, and advance

Chen et al. (Kidney Medicine 2024; DOI `10.1016/j.xkme.2024.100796`; PMCID `PMC10986041`) was inspected from the frozen full-text Europe PMC XML source `[source checksum]`, retrieved-source [source checksum]. It studied 468,969 UKB participants, reported that observable characteristics predict creatinine-cystatin eGFR differences, and internally validated an enriched model with AUC 0.75. It supports plausibility and internal predictability, not AG1:A1 fixed-capacity superiority, low-UACR complementarity, measured-GFR accuracy, or benefit.

Lees et al. (JAMA Network Open 2022; DOI `10.1001/jamanetworkopen.2022.38300`; PMCID `PMC9597396`) was inspected from frozen full-text XML source `[source checksum]`, [source checksum]. In 428,402 UKB participants selected with urine albumin below 30 mg/g, cystatin-based classification stratified cardiovascular and mortality risk over median 11.5 years; kidney failure was rare. It supports the clinical relevance of cystatin reclassification when albuminuria is low, not the present UACR threshold, grip rule, quota, or causal testing benefit.

The strongest data claim already supported is outcome-blind feasibility. A managed all-row reconstruction previously established O1_hold=2,334 and only three unavailable H1 labels. This episode's managed audit `[research job]` read only the `eid` column of the authenticated all-O1_hold artifact—never any selection flag, score, rank, or selected yield—and physically projected the required source columns. It found 2,208 usable observed UACR1 values, 2,100 below 3.0 mg/mmol, 108 at or above 3.0, 126 unavailable, zero urine-integrity failures, 41 aggregate H1 cases, and the decomposition 35 observed-low-UACR, 5 observed-high-UACR, and 1 UACR-unavailable H1. This establishes computability and aggregate event availability only. It neither supports nor refutes AG1 versus A1.

The unresolved claim is the policy-specific fixed-denominator contrast below. Its advance is to distinguish a grip increment that finds low-albuminuria equation-defined reclassification from one confined to an already visible urine signal or unavailable-urine fallback.

## Frozen population, temporal boundary, exposures, and primary parent estimand

All parent definitions remain exact. O1_hold contains the authenticated 2,334 canonical `eid` values satisfying the frozen instance-1 eligibility and original-development exclusion. Time zero remains the parseable assessment date `t1=53-1.0`; the catalog's empty temporal metadata does not prove specimen or result chronology. Capacity remains `n1=floor(0.20*2334)=466`.

A1 and AG1 were separately fit only in the baseline development set to baseline H, then applied without refitting at instance 1. A1 includes the standard frozen covariates and observed/fallback UACR; AG1 adds the one frozen grip column. The exact authenticated rosters remain fixed. No H1, D1, observed-low-UACR endpoint, N18, death, or other post-selection value may refit, rerank, refill, exclude, or alter a denominator.

The parent H1 and D1 definitions, F27_H/F27_D families, sharp shared-person missing-label bounds, support/adverse/inconclusive rules, h/sex checks, and all upstream parent gates remain primary and unchanged. This child cannot rescue any parent failure.

## New observed-UACR strata and endpoints

Using only raw visit-1 urine fields, define usable observed UACR1 exactly as the parent does:

- urine creatinine `30510-1.0` is positive and finite; and
- either urine albumin `30500-1.0` is positive finite numeric with blank trimmed flag `30505-1.0`, or albumin is blank and the trimmed flag is exactly `<6.7`, in which case assign 3.35 mg/L solely for the ratio calculation;
- compute `UACR1=1000*albumin/urine_creatinine` mg/mmol under the frozen source units;
- numeric albumin plus a nonblank flag is an integrity failure;
- `30515-1.0` is physically absent and must never be invented.

Define `L1=1` only for usable observed UACR1 strictly below 3.0 mg/mmol; `A23_1=1` for usable UACR1 at or above 3.0, including exactly 3.0; and `U1=1` when UACR1 is unavailable. The development-median fallback remains inside the frozen A1/AG1 score but can never create `L1=1`. These are one-snapshot categories, not persistent albuminuria diagnoses.

Define `H_L=H1*L1`, `H_A23=H1*A23_1`, and `H_U=H1*U1`. For each fixed list p in {AG1,A1}:

`Y_L(p)=1000*sum(i in S_p) H_L_i/466`,
`Delta_L=Y_L(AG1)-Y_L(A1)`,
and `R_L=Y_L(AG1)/Y_L(A1)` only when the comparator numerator is nonzero.

Report fixed-list numerators, yields, `Delta_L`, `R_L`, observed-label counts, selected L1/A23_1/U1 counts, overlap/Jaccard, AG-only and A-only H_L counts, directional-swap yield, and the same quantities descriptively for H_A23 and H_U. Verify participant-, list-, point-, sharp-bound-, and bootstrap-draw identities `H1=H_L+H_A23+H_U` and `Delta_H=Delta_L+Delta_A23+Delta_U`. Never divide by selected L1 participants, usable urine results, observed H labels, survivors, or events.

For missing H1, preserve one shared latent binary label per eid. H_L is unknown only when H1 is missing and L1=1; use coefficient `c_i=I(i in AG1)-I(i in A1)` with exact lower/upper contributions `min(0,c_i)` and `max(0,c_i)`. H_A23 and H_U use the analogous known stratum indicators. A shared participant cannot receive different missing labels across lists or strata. More than 1% H1 missingness, any stratum/decomposition failure, or any source/roster mismatch makes this layer inconclusive/noncomputable.

## Paired analysis, multiplicity, and falsification

Use the exact parent 2,000 participant-level paired bootstrap draws over canonical-eid-sorted O1_hold, the exact PCG64DXSM seeds from the full unsigned big-endian SHA-256 of UTF8(`"ukb-grip-visit1-bootstrap-v1|"+b`) for b=0,...,1999, shared multiplicities, fixed memberships, and denominator 466. Never refit or rerank in a draw.

The new `F29_H_complementarity` family contains exactly four components in this order: parent `Delta_H`, parent `log(R_H)`, `Delta_L`, `log(R_L)`. Recompute simultaneous inference for all four; do not reuse the smaller F27_H limits for a compound Episode-29 claim. Use the parent's studentized max-t one-sided 95% limits and two-sided intervals. If any SE is nonfinite/nonpositive or fewer than 95% of ratio replicates are finite, use the parent's fixed componentwise Bonferroni percentile fallback for all four and mark it; any component with fewer than 95% finite draws remains inconclusive. F27_H and its parent label remain reported unchanged. F27_D remains separate; the Episode-29 claim is an intersection-union conjunction, not an either/or rescue.

Before supportive or adverse low-UACR interpretation require exact rosters and n=466; at least 40 observed H labels in each list and 20 in each directional swap as in the parent; at least 10 observed H_L cases in the AG1 union A1; at least 4 in each list; at least 3 across the symmetric difference; U1 no more than 10% in each list; zero selected urine-integrity failures; at least 95% finite ratio draws; nonzero variance; and all source/join/hash/decomposition/bootstrap checks. These minima are outcome-blind anti-vacuity gates, not a power guarantee. Failure is inconclusive, never adverse.

`visit1_grip_increment_low_UACR_supportive` requires every information gate; the unchanged parent grip-increment biochemical label supportive; adverse sharp `Delta_L>=+2/1,000`; adverse sharp `R_L>=1.10`; F29 simultaneous lower `Delta_L>+2` and lower `R_L>1.10`; and adverse sharp AG-only minus A-only H_L swap yield >0.

`visit1_grip_increment_low_UACR_adverse` requires adequate computation/information and at least one of: simultaneous upper `Delta_L<+2`; finite feasible/simultaneous `R_L` upper <1.10; or favorable sharp low-UACR swap upper <=0. This is adverse to the complementarity claim, not proof that A1 improves health or that cystatin lacks value.

Every other result is `visit1_grip_increment_low_UACR_inconclusive`, including a limit touching/crossing a margin, sparse H_L events/swaps, feasible zero denominator, excessive urine/H missingness, zero variance, or integrity failure. Inconclusive is not equivalence.

Emit the parent `visit1_grip_increment_supportive|adverse|inconclusive` unchanged. Emit `episode29_complementary_grip_increment_supported` only when every parent/upstream required gate and the new low-UACR label support. If the parent supports but low-UACR is adverse, emit `total_increment_supported_low_UACR_adverse`: the total equation-defined result remains reportable, but evidence argues against the prespecified complementary-discovery claim. If the parent supports and low-UACR is inconclusive, emit `total_increment_supported_low_UACR_unresolved`. A favorable H_L result cannot rescue any adverse/inconclusive parent gate. H_A23, H_U, D1, or N18 cannot rescue H_L failure.

## Exact source binding

All sources are read-only ordinary CSVs with archive member `null`, one row per canonical `eid`, and horizontal one-to-one joins. Reject duplicate/missing keys and disagreement in overlapping loaded fields. Derived files remain in the workspace.

- `population`: `[internal dataset path]`, [source checksum]; table `population`; schema `datasets/ukb/table-38565c9e35e7cb6c.json`, schema [source checksum]; key `eid`; required `31-0.0,21022-0.0`.
- `assessment`: `[internal dataset path]`, [source checksum]; table `assessment`; schema `datasets/ukb/table-901ef6c7ddce2d51.json`, schema [source checksum]; key `eid`; required `53-0.0,53-1.0,21003-1.0,21001-0.0,21001-1.0,46-0.0,47-0.0,46-1.0,47-1.0`.
- `biological_samples`: `[internal dataset path]`, [source checksum]; table `biological_samples`; schema `datasets/ukb/table-c6b666d905f3b02f.json`, schema [source checksum]; key `eid`; required `30500/30505/30510/30700/30720` at instances 0 and 1. The audit physically projected `30500-1.0,30505-1.0,30510-1.0,30700-1.0,30720-1.0`.
- `health_outcomes`: `[internal dataset path]`, [source checksum]; table `health_outcomes`; schema `datasets/ukb/table-3cfae45e0905b0e3.json`, schema [source checksum]; key `eid`; inherited paired `41270-0.0...41270-0.258`/`41280-0.0...41280-0.258` and deaths `40000-0.0,40000-1.0`.

Snapshot is `[source checksum]`; full catalog is `[internal dataset path]`, [source checksum]. The four schemas declare `temporal_columns=[]`; only encoded dates explicitly parsed by the parent provide boundaries. HCC, MIMIC-IV including notes, and eICU remain directly accessible read-only but cannot join to UKB `eid` and are not used. No private row or note was sent to public search.

## Verifier contract, result meanings, and stronger evidence required

The verifier can recompute source/header/schema hashes; one-to-one joins; exact O1_hold and roster identities; UACR parsing and strict observed strata; H endpoints and decomposition; fixed-denominator yields; shared missing-label bounds; paired seeds/draws; four-component multiplicity; anti-vacuity gates; labels; and whether conclusions follow outputs.

Fixtures must reject: using the score fallback to define L1; treating `<6.7` as measured 6.7; inventing `30515-1.0`; classifying exactly 3.0 as low; reselecting within L1; changing n=466; dividing by selected-low or observed-label counts; independent policy bootstraps; different labels for a shared missing eid; omitting parent components from F29; allowing low-UACR support to rescue a parent failure; calling sparse or margin-crossing results adverse/equivalent; or attaching measured-GFR, persistent-CKD, mechanism, action, cost, fairness, prevention, or benefit claims to correct computation.

A supportive result means only that the frozen AG1 list has a multiplicity-controlled material increase in one-record equation-defined H1 yield over A1 at equal capacity and that this increment is also present among participants with observed snapshot UACR<3. It would justify a prospective adjudicated comparison focused on complementary detection. An adverse result is useful evidence against that complementary-increment claim. An inconclusive result leaves it unresolved.

No automatic computation can establish specimen/order/result chronology, persistent low UACR or reduced GFR, measured GFR truth, sarcopenic mechanism, complete kidney-event capture, causal actionability, workflow feasibility, costs, harms, equity, transportability, or patient benefit. Those require repeated clinically timed urine and serum measures, measured GFR, complete outpatient/kidney-replacement and censoring data, chart/nephrologist adjudication, order/result and action/medication records, local workflow/cost/harms/equity review, external validation, and a prospective implementation or randomized testing-strategy study with patient-centered outcomes.
