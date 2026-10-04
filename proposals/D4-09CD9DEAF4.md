> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 67: baseline-eGFR qualification of the frozen AG1-versus-AF1 kidney allocation contrast

## Decision question and substantive advance

This is a substantive successor with parents `[prior hypothesis]` and `[prior hypothesis]`. The assessed-valid d44e allocation experiment and assessed-valid b7b9213 N18 endpoint experiment are inherited verbatim except for the new, prespecified baseline-eGFR qualification below. No fitted score, participant, capacity, time zero, endpoint, global denominator, bootstrap seed, parent label, or noncausal limit is changed.

The unresolved clinical question is:

> Does the fixed AG1-versus-AF1 enrichment of first recorded inpatient N18-before-death events persist in both clinically meaningful baseline kidney-function bands, eGFRcr1 60–<75 and 75–<90 mL/min/1.73m², in the same 466-assay allocation?

The distinction matters for implementation. A contrast confined to the lower part of the parent’s 60–<90 eligibility range would support a narrower referral hypothesis; a contrast that persists in both bands would make the strategy more relevant across adults with mildly reduced or near-preserved filtration. Either result informs a prospective testing-strategy study. It does not justify routine testing, because the endpoint is administrative, one-record equation-defined kidney status is not measured GFR, and the allocation is retrospective/noncausal.

The new claim is deliberately limited: AG1 is not claimed to cause more kidney detection, and subgroup membership is not a new eligibility criterion or a new selected roster. The experiment asks whether the already-frozen global allocation contrast has evidence of a positive fixed-denominator N18 enrichment in each baseline eGFR band.

## Evidence versus the hypothesis

The strongest supported claims are narrower than the hypothesis. Chen et al. (Kidney Medicine 2024, DOI `10.1016/j.xkme.2024.100796`, PMCID `PMC10986041`) was inspected from frozen full-text XML source `[source checksum]` with retrieved-file [source checksum]; it supports that observable characteristics can internally predict creatinine–cystatin eGFR discordance in UK Biobank, not this quota or allocation contrast. Lees et al. (JAMA Network Open 2022, DOI `10.1001/jamanetworkopen.2022.38300`, PMCID `PMC9597396`) was inspected from frozen XML source `[source checksum]`, [source checksum]; it supports prognostic relevance of cystatin-based reclassification, not grip-based testing benefit. Liu et al. (Clinical Kidney Journal 2025, DOI `10.1093/ckj/sfaf003`, PMCID `PMC11997436`) was inspected from frozen XML source `[source checksum]`, [source checksum]; its heterogeneous synthesis supports association of lower eGFRcys relative to eGFRcr with mortality/cardiovascular outcomes, while renal outcomes were insufficient for meta-analysis. None supports subgroup persistence, the fixed rosters, incident CKD, measured-GFR accuracy, causality, or benefit.

The three research-ambition demonstrations were not used as topic evidence. `references/research-ambition/README.md` was inspected. The cancer main article and full STAR Methods remain unavailable and are not claimed as read; no unavailable paper text or supplement is used here.

Outcome-blind private-data evidence supports only computability: d44/b7 authenticate O1=5,823, O1_hold=2,334, n1=466, AG1/AF1 overlap 435 and 31 directional swaps; inherited feasibility found 40 total five-year O1_hold N18-before-death events without opening policy yields. The outcome-blind subgroup audit specification is `analysis/subgroup_baseline_audit.py`; it is a compiler preflight, not a completed scientific result. It must scan all rows of the selected baseline columns in the exact read-only UKB sources, retain only authenticated O1_hold eids, and read no N18, death, H1/D1, score, rank, selected yield, or policy outcome. Its output must report subgroup counts and swap coverage as feasibility facts only. If either band fails the prespecified swap/coverage checks below, this proposed qualification is non-falsifiable and must be reported inconclusive rather than repaired by changing bands or pooling strata. A managed attempt was stopped before output and is not evidence of adequacy.

## Immutable parent population, time zero, fits and rosters

Reproduce and authenticate the entire b7/d44 package before opening outcomes.

* All joins use one canonical positive decimal `eid`, one row per source, and exact horizontal one-to-one joins. The inherited population is O1=5,823 and the hash-split holdout is O1_hold=2,334:
  `h = int(SHA256("ukb-grip-cys-v3|"+eid),16) mod 100 >= 60`.
* O1 requires recorded sex `31-0.0` in {0,1}; assessment-instance-1 age `21003-1.0` in [40,70); strictly parsed `53-1.0`; positive finite `21001-1.0`; positive finite serum creatinine `30700-1.0`; at least one positive finite `46-1.0` or `47-1.0`; full-precision 2021 race-free eGFRcr1 in [60,90); and no exactly position-paired inpatient N17/N18 code/date on or before t1. A malformed qualifying pre-index code/date is handled exactly by the inherited parent exclusion rule.
* Time zero is the strictly parsed assessment-instance-1 `53-1.0` date. Define `t5` as t1 plus five calendar years, mapping February 29 to February 28 when necessary. The source descriptors declare no temporal columns; specimen/order/result chronology is unavailable and must remain `specimen_time_verified=false` and `prospective_preassay_order_identifiable=false`.
* Development and all baseline-only fitting remain frozen: joined=502,370; O=134,118; development O=80,516; labeled L=80,470. A1 and AG1 are the inherited baseline-development fits; AF1 is the authenticated A+whole-body FFM fit from d44, using `23101-0.0/1.0`, development-only median 50.9 kg, winsor limits [35.4,83.90000000000002], population mean 53.549463460678616, population SD 11.185202961908633, inherited spline/UACR transforms, five-fold ridge selection, and no future or outcome information. Its exact script, coefficients, manifest and two-run reproducibility attestation are attached.
* The exact combined membership is `support-27-episode33_AF1_frozen_visit1_rosters.csv`, [source checksum], with columns `eid,AF1_selected,A1_selected,AG1_selected`. It must reproduce exactly 466 AG1, 466 AF1, 435 overlap, 31 AG1-only and 31 AF1-only. The inherited AG1/A1 file is `support-8-support-13-support-12-episode27_frozen_visit1_rosters.csv`, [source checksum]. No subgroup selection, within-band reranking, refitting, refill, outcome filtering or denominator change is permitted.

The parent biochemical H1/D1 hierarchy and d44 AF1 qualification must be computed and emitted unchanged before the b7 N18 endpoint and before this child label. A child result cannot rescue a failed parent hierarchy or alter any parent conclusion.

## Prespecified baseline-eGFR strata

The only new variable is a baseline subgroup label computed after the immutable O1_hold membership is authenticated and before any endpoint fields are read:

`G=low` iff 60 <= eGFRcr1 < 75; `G=high` iff 75 <= eGFRcr1 < 90.

Compute eGFRcr1 exactly as inherited, using age `21003-1.0`, sex `31-0.0` and creatinine `30700-1.0` in µmol/L converted by /88.4. For sex=0 use k=0.7, alpha=-0.241 and female multiplier 1.012; for sex=1 use k=0.9, alpha=-0.302 and multiplier 1.0:
`142*min(Scr/k,1)^alpha*max(Scr/k,1)^(-1.2)*0.9938^age*multiplier`.
Use binary64 values before comparison; no rounding or alternate equation is allowed. O1’s inherited full-precision [60,90) check and valid fields imply every eligible holdout member should fall in exactly one band. Values on 75 belong to high; 60 belongs to low; 90 is outside and is an integrity failure, not a third analytic stratum.

The audit must report, separately for low/high, holdout size, AF1/AG1/A1 counts, overlap, AG1-only and AF1-only counts, and exact eGFR missing/outside count. To keep the qualification falsifiable, each band must have at least 8 AG1-only and at least 8 AF1-only members, and at least 16 total symmetric-difference members; these are outcome-blind design feasibility gates. A failed gate is subgroup-sparsity inconclusive; do not merge bands, move cutpoints, use sex instead, or redefine the endpoint.

## Unchanged kidney endpoint and competing death

Use the canonical `health_outcomes` row for each O1_hold eid. For each j=0,...,258, trim and uppercase `41270-0.j`; pair only with its own `41280-0.j`. Let T18 be the earliest strictly parsed date for a code beginning exactly `N18`. N17 never satisfies or censors the primary endpoint. Let Tdeath be the earliest strictly parsed nonblank date among `40000-0.0` and `40000-1.0`; do not use 40001 or 40002.

`E18_i=1{t1_i < T18_i <= t5_i and (Tdeath_i absent or T18_i < Tdeath_i)}`.

Death on or before T18, including same-day death, prevents E18=1. N18 on t1 is pre-index; N18 after t5 is outside. Define the separate inherited competing-death state:
`C5_i=1{t1_i<Tdeath_i<=t5_i and no T18_i satisfies t1_i<T18_i<Tdeath_i}`.
Deaths after a prior qualifying N18 are reported separately. C5 is never added to E18 and cannot create kidney support.

Before endpoint computation, compare all 520 endpoint fields between canonical `health_outcomes` and duplicate-audit `main` for every O1_hold eid using identical trim/null/date normalization. Both physical headers contain `40000-0.0`, `40000-1.0`, and all 259 code/date pairs, but the inherited header audit read no rows. Canonical values remain `health_outcomes`; any row-level disagreement, nonblank malformed N18/date pair, nonblank unparseable death, death on/before t1, or inability to establish duplicate agreement is global integrity-inconclusive, never imputed.

## Fixed-denominator subgroup estimands

For p in {AG1,AF1} and g in {low,high}, let S_p be the immutable 466-person list and define:

`Y18_g(p)=1000*sum_{i in S_p} 1(G_i=g)E18_i/466`,
`Delta_g=Y18_g(AG1)-Y18_g(AF1)`.

The denominator is always 466, including for a subgroup. Do not divide by subgroup size, observed events, survivors, complete cases, or the number of swaps. Also report the inherited global `Y18(p)` and `Delta18=Delta_low+Delta_high`, each list/overlap/swap numerator and yield, and verify:
`Delta_g=(1000/466)*(sum_AGonly,g E18 - sum_AFonly,g E18)`;
`Delta18=Delta_low+Delta_high`.
Report the descriptive interaction `I=Delta_low-Delta_high` with its paired interval; it is not a new selection rule or a license to claim homogeneity.

The exact fixed-quota one-event resolution is `m=1000/466=2.145922746781116` events per 1,000 assay slots. The child’s persistence claim requires at least one net event in each stratum at this global denominator, not a validated utility or cost-effectiveness threshold.

## Paired inference and multiplicity

Retain the b7 global F66_N18 computation exactly: 2,000 participant-level paired bootstrap draws over canonical-eid-sorted O1_hold, PCG64DXSM seeded by the full unsigned big-endian SHA-256 of UTF-8(`"ukb-grip-visit1-bootstrap-v1|"+str(b)`), b zero-based, resampling 2,334 rows with replacement, fixed memberships and denominator, no refit. Its one-component global interval and gate remain unchanged.

For this child, the prespecified family is F67_sub={Delta_low, Delta_high, I}; it contains exactly these three components. In every draw use the same sampled multiplicity vector for both policies and both groups. Report point estimates, paired bootstrap SE (ddof=1), finite-draw counts, family order/hash, all seeds/namespace and the fallback reason if used. When all three component SEs are finite and positive and at least 95% of draws are finite, form simultaneous one-sided 95% max-t limits for the three components using the inherited NumPy-linear 95th-percentile convention. For lower limits, use the maximum standardized lower-tail deviation; for upper limits use the corresponding maximum upper-tail deviation. If that condition fails, use componentwise Bonferroni one-sided percentile limits with m=3 and tail .05/3, mark fallback, and make the qualification inconclusive if any component has fewer than 95% finite draws or zero variance. The interaction interval is reported for interpretation; all child support/adversity decisions use the simultaneous Delta_low and Delta_high limits.

The endpoint event gates are inherited globally and strengthened within each band: exact source/header/descriptor/catalog/roster identities; one-to-one joins and zero duplicate disagreement; exact t1/t5 chronology; at least 10 E18 events in global AG1 union AF1, at least 3 in each global policy list, at least 4 in the global symmetric difference; in each eGFR band at least 4 E18 events in its policy union, at least 1 in each policy list, and at least 2 in its symmetric difference; at least 95% finite bootstrap draws and positive finite uncertainty; all decomposition identities; and no outcome leakage. These are information gates, not power guarantees. Any failure is inconclusive, never adverse.

For C5, report global and band-stratified fixed-denominator yields and paired intervals descriptively under the same frozen chronology. Emit competing-death enrichment labels only as inherited prognostic diagnostics; a death signal cannot support the kidney endpoint or the subgroup qualification.

## Falsification and interpretation contract

The child label is determined before looking at prose conclusions:

* `eGFR_persistence_supportive`: all gates pass; both point estimates `Delta_low >= m` and `Delta_high >= m`; and both simultaneous one-sided lower limits are strictly >0. This is evidence that the fixed AG1 roster has at least one net recorded N18-before-death event at the global 466-slot resolution in each baseline eGFR band.
* `eGFR_persistence_adverse`: all gates pass and the simultaneous one-sided upper limit for either Delta_low or Delta_high is <=0. This rules out positive AG1 enrichment in at least one prespecified band; it does not prove AF1 superiority, equivalence, safety, or no clinical benefit.
* `eGFR_persistence_inconclusive`: every other result, including one positive band and one unresolved band, positive point estimates whose uncertainty includes zero, failure of sparse-band/eGFR/event/source/chronology/bootstrap gates, boundary equality, or fallback instability. Inconclusive is not no difference.

The final nonrescuing synthesis must preserve all upstream labels:

* emit `parent_n18_and_eGFR_persistence_supported` only if the inherited parent hierarchy supports, global b7 N18 is `n18_targeting_supportive`, and this child is supportive;
* emit `parent_n18_supported_eGFR_persistence_adverse` if the inherited parent hierarchy and global N18 support but the child is adverse;
* emit `parent_n18_supported_eGFR_persistence_inconclusive` if the inherited parent hierarchy and global N18 support but this child is inconclusive;
* otherwise emit `parent_or_global_n18_not_supported_eGFR_nonrescuing`, retaining the exact upstream adverse/inconclusive reason.

Support means only outcome-defined persistence in this UKB snapshot and merits prospective adjudicated evaluation. Adverse means at least one band does not show positive fixed-quota enrichment under the prespecified uncertainty rule. Inconclusive leaves persistence unresolved. No result establishes incident or persistent CKD, measured GFR, renal attribution of death, a grip mechanism, a causal testing effect, routine adoption, actionability, workflow feasibility, assay ordering, cost-effectiveness, safety, equity, transportability or patient benefit.

## Exact source bindings and availability

Catalog: `[internal dataset path]`, [source checksum]; UKB snapshot `[source checksum]`. Every source is an ordinary CSV (`archive_member=null`), identity key `eid`, descriptor `temporal_columns=[]`; sources are read-only.

| table | exact source path; source SHA-256 | descriptor; JSON SHA-256; internal schema SHA-256 | fields used |
|---|---|---|---|
| population | `[internal dataset path]`; `[source checksum]` | `datasets/ukb/table-38565c9e35e7cb6c.json`; `[source checksum]`; `[source checksum]` | `eid,31-0.0` |
| assessment | `[internal dataset path]`; `[source checksum]` | `datasets/ukb/table-901ef6c7ddce2d51.json`; `[source checksum]`; `[source checksum]` | `eid,53-0.0,53-1.0,21003-1.0,21001-0.0,21001-1.0,46-0.0,47-0.0,46-1.0,47-1.0,23101-0.0,23101-1.0` |
| main | `[internal dataset path]`; `[source checksum]` | `datasets/ukb/table-e4a9e4d8baa71a9d.json`; `[source checksum]`; `[source checksum]` | inherited `eid,23101-0.0,23101-1.0`; duplicate audit `eid,40000-0.0,40000-1.0,41270-0.0...41270-0.258,41280-0.0...41280-0.258` |
| biological_samples | `[internal dataset path]`; `[source checksum]` | `datasets/ukb/table-c6b666d905f3b02f.json`; `[source checksum]`; `[source checksum]` | subgroup/parent `eid,30700-1.0,30720-1.0,30500-1.0,30505-1.0,30510-1.0`; `30515-1.0` is absent and forbidden |
| health_outcomes | `[internal dataset path]`; `[source checksum]` | `datasets/ukb/table-3cfae45e0905b0e3.json`; `[source checksum]`; `[source checksum]` | endpoint `eid,40000-0.0,40000-1.0,41270-0.0...258,41280-0.0...258` |

The descriptor table names, exact columns and source hashes are verified against `datasets/README.md`, `datasets/ukb/README.md` and the full local catalog. The configured HCC (12 files), MIMIC-IV (5 files including notes), eICU (31 files), and UKB (8 files) remain directly accessible; HCC/MIMIC/eICU have no UKB `eid` linkage and are not mixed into this experiment. No private clinical row or note is sent to public search. All derived files and reports remain in the workspace.

## Compiler, verifier and adjudication boundary

The compiler must run: (1) parent artifact/header and outcome-blind subgroup authentication; (2) inherited d44 biochemical hierarchy and AF1 checks; (3) b7 global N18 endpoint with duplicate-source row audit; (4) this fixed-band calculation and F67 bootstrap. A proposed change to O1/O1_hold, t1/t5, eGFR cutpoints, estimand denominator, endpoint, bootstrap family, gates, or falsification logic is a new Lead child, not a compiler repair.

Required outputs include source/catalog/descriptor/schema/archive hashes; row and join counts; exact O/O1/O1_hold identities; parent fit and roster hashes; full baseline eGFR values or a private audit digest; band counts and swap counts; exact t1/t5 and code/date/death parsing counts; duplicate disagreements; E18/C5 states; global and per-band numerators, fixed-denominator yields, decompositions and interaction; all paired bootstrap seeds, component order, finite counts, SEs, simultaneous/fallback limits; gate states; parent/child labels; and a conclusion object whose claims cite output keys.

Falsification fixtures must include wrong sex coding/equation, eGFR=75 boundary misclassification, rounding before banding, moving a participant between bands after seeing outcomes, subgroup-denominator use, changed rosters or n=466, global-to-band decomposition failure, independently bootstrapped policies, sparse band, missing eGFR, N18/date position mismatch, N17 substitution, same-day death precedence error, death-on-t1, t5 boundary error, composite N18-or-death support, endpoint-source disagreement, outcome leakage, and unsupported claims of CKD persistence, measured GFR, causality, equivalence, safety, routine use, cost, equity or benefit.

Automatic verification can establish the encoded population, subgroup, roster, endpoint chronology, duplicate agreement, fixed-denominator arithmetic, paired resampling, gates, labels and whether prose follows computed outputs. It cannot establish complete event capture, emigration/censoring, clinically adjudicated or persistent CKD, measured GFR, specimen/order chronology, mechanism, actionability, workflow burden, harms, costs, fairness, transportability or patient benefit. Those require linked outpatient/kidney-replacement/censoring data, repeated clinically timed biomarkers, measured GFR, cause-specific mortality, chart/nephrologist adjudication, workflow/cost/equity review, external validation and a prospective implementation or randomized testing-strategy study.

## Direct artifact closure

The proposal directly packages the controlling proposals, executable scripts, manifests, authenticated rosters, evidence and reproducibility records from both parents; the subgroup audit script is included, while no unproduced audit result is claimed. The attached inherited artifact paths are:

- d44: `proposal.md`, `support-0-proposal.md`, `support-1-support-0-episode29_ffm_feasibility.md`, `support-2-proposal.md`, `support-3-support-0-proposal.md`, `support-4-support-1-support-0-support-0-episode16_complete.md`, `support-5-support-10-support-9-episode27_recompute_A1_roster.py`, `support-6-support-11-support-10-episode27_frozen_model_and_roster_manifest.json`, `support-7-support-12-support-11-episode27_A1_roster_ranked.csv`, `support-8-support-13-support-12-episode27_frozen_visit1_rosters.csv`, `support-9-support-14-support-13-episode27_parent_authentication.json`, `support-10-support-15-support-14-episode27_evidence.md`, `support-11-support-16-support-15-episode27_data_availability.md`, `support-12-support-17-episode29_low_uacr_feasibility.py`, `support-13-support-18-episode29_low_uacr_feasibility.json`, `support-14-support-2-support-1-support-1-episode17_complete.md`, `support-15-support-3-support-2-support-2-episode18_complete.md`, `support-16-support-4-support-3-support-3-episode19_complete.md`, `support-17-support-5-support-4-support-4-recompute_frozen_visit1_rosters.py`, `support-18-support-6-support-5-support-5-episode23_frozen_model_and_roster_manifest.json`, `support-19-support-7-support-6-support-6-episode23_G1_roster_ranked.csv`, `support-20-support-8-support-7-support-7-episode23_AG1_roster_ranked.csv`, `support-21-support-9-support-8-support-8-episode23_frozen_visit1_rosters.csv`, `support-22-episode33_ffm_coverage.py`, `support-23-episode33_ffm_coverage.json`, `support-24-episode33_fit_AF1.py`, `support-25-episode33_AF1_fit_and_roster_manifest.json`, `support-26-episode33_AF1_roster_ranked.csv`, `support-27-episode33_AF1_frozen_visit1_rosters.csv`, `support-28-episode33_evidence.md`, and `support-29-episode33_reproducibility.md`; b7: `proposal.md`, `support-0-episode66_evidence.md`, `support-1-episode66_header_audit.py`, and `support-2-episode66_header_audit.json`. The new outcome-blind audit script is `analysis/subgroup_baseline_audit.py`; its managed preflight attempt was stopped before output, so no audit result is claimed. The compiler must produce and verify its result. The parent row-level FFM extract remains a private regenerable workspace artifact and is not a source or clinical claim. No policy-specific outcome was opened while selecting this qualification.
