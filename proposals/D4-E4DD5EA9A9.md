# Episode 77: temporal biological-validity qualification of the frozen AG1-versus-AF1 experiment

## Decision question and one new hypothesis

This is a direct child of assessed-valid `[prior hypothesis]`. The parent is the scientific authority and its complete executable/support package is controlling. This successor preserves, definition for definition, the parent’s O/O1/O1_hold populations, `t1=53-1.0`, hash split, development labels, A1/AG1/AF1 fits, immutable 466-person rosters, 435-person overlap, 31 directional swaps, H1/D1 estimands, low-UACR hierarchy, paired bootstrap, multiplicity, margins, gates, nonrescue rules, provenance, and all clinical limits. It does not open a new policy outcome.

The unresolved biological-validity question is whether the grip increment is a temporally coherent functional phenotype rather than a one-visit or mass-proxy selection artifact:

> In the exact frozen O1_hold=2,334 and equal-capacity AG1-versus-AF1 comparison, does AG1 select more participants with persistently low grip relative to whole-body impedance fat-free mass at both baseline and visit 1 than AF1?

The clinical importance is interpretive. AG1 was designed to add grip to routine variables, UACR and FFM. If its fixed roster enriches a two-visit relative-weakness phenotype, the grip increment has biological and temporal coherence that supports a prospective comparison of grip-based and FFM-based testing strategies. If the contrast disappears when relative weakness must repeat across visits, the biochemical allocation result is less credible as a stable functional signal. An inconclusive result leaves the biological interpretation open. None of these results establishes measured GFR, persistent CKD, causality, benefit, or routine deployment.

This is nonredundant with d44: d44 asks whether AG1 versus AF1 differs on equation-defined visit-1 biochemical targeting. Episode 77 asks whether the policy difference corresponds to a prespecified repeated biological phenotype. It is not a low-UACR subgroup, kidney-event endpoint, sex subgroup, record-density control, or persistence-coded N18 outcome.

## Evidence boundary

The strongest supported claims inherited from d44 are outcome-blind computability and authentication: O1_hold=2,334; n1=466; exact AG1/AF1 lists; 435 overlap and 31 swaps; baseline/visit-1 FFM field 23101 availability and duplicate-source agreement; and a deterministic, independently reproduced AF1 fit. D44’s public evidence supports interpreting 23101 as Tanita bioimpedance-derived whole-body FFM, not directly measured skeletal muscle, and grip as a functional measure that is not interchangeable with mass.

Those facts do not support the new claim. No AG1/AF1 policy-specific biochemical, N18, death, numerator, yield, or label is inspected here. The new claim will be supported only if the compiler computes the prespecified repeated relative-grip endpoint and its fixed-roster contrast with valid uncertainty and all gates.

The three demonstrations in `references/research-ambition/README.md` are ordinary references, not topic evidence. The cancer demonstration’s unavailable main article and full STAR Methods are not claimed as read. The configured HCC, MIMIC and eICU sources are not mixed into this UKB experiment.

## Frozen population, policies and time

Use d44’s exact definitions:

- canonical positive decimal `eid`;
- field `31-0.0` in {0,1};
- age `21003-1.0` in 40–69;
- strictly parsed assessment date `t1=53-1.0`;
- positive finite `21001-1.0`;
- at least one positive finite visit-1 grip value in `46-1.0` or `47-1.0`;
- positive finite `30700-1.0`;
- race-free 2021 eGFRcr1 in [60,90);
- no position-paired inpatient N17/N18 code/date on or before t1;
- `O1_hold=O1) when `int(SHA256("ukb-grip-cys-v3|"+eid),16) mod 100 >= 60).

Expected frozen identities are joined=502,370, O=134,118, development O=80,516, labeled L=80,470, O1=5,823, O1_hold=2,334, and `n1=floor(.20*2334)=466). Abort the child layer if any inherited identity, hash, roster, or source-binding check differs.

AG1 and AF1 are the parent’s immutable baseline-development policies. Reuse their exact membership files and hashes, not a reranking. AF1 is the A+UACR+FFM comparator; AG1 is the parent’s grip-augmented policy. The comparison remains fixed-denominator and policy-specific outcomes remain unopened until all pre-outcome checks pass.

Instance numbers are not specimen or order times. Preserve d44’s `specimen_time_verified=false` and `prospective_preassay_order_identifiable=false). “Baseline” and “visit 1” mean the UKB instance labels used by the parent, not verified assay chronology.

## New biological endpoint

For each eligible participant and instance v in {0,1}, define the maximum available handgrip:
`G_iv=max(46-v.0,47-v.0)), requiring a positive finite value. Define whole-body impedance FFM `F_iv=23101-v.0`, requiring a positive finite value. The canonical FFM source is d44’s `main` binding; the d44 outcome-blind audit must continue to verify exact agreement with the overlapping `assessment` columns before this layer runs.

Define the dimensionless relative-grip measure:
`R_iv=log(G_iv/F_iv)`.

Before reading any O1_hold policy result, calculate sex-specific development-only thresholds from the exact d44 development-O roster (80,516 participants), using no cystatin label, outcome, rank, roster, or holdout value:

1. Require both `R_i0` and `R_i1` and field `31-0.0` in each development-O participant used for thresholding.
2. Within each recorded-sex stratum, set `c_s` to the empirical 25th percentile of `R_iv` pooled over v=0 and v=1, using the parent’s explicit NumPy binary64 linear-quantile convention. The threshold source population and both instance values are frozen before holdout policy outcomes.
3. For an O1_hold participant with both valid instance ratios, define `P_i=1) iff `R_i0<=c_sex` and `R_i1<=c_sex`. Otherwise P is missing. This is a repeated low-relative-grip phenotype, not sarcopenia, measured muscle, frailty, or persistent disease.

The pooled two-instance threshold makes the endpoint a stability qualification rather than a threshold tuned to one visit. As descriptive diagnostics, report baseline-low and visit-1-low status and the within-person change `R_i1-R_i0`; neither can rescue or replace P. Do not inspect or use H1, D1, UACR outcome labels, N18, death, policy-specific yield, or any post-index endpoint while deriving `c_s` or P.

## Estimand, uncertainty and falsification

For p in {AG1,AF1}, with the immutable denominator 466:
`Y_P(p)=1000*sum_{i in S_p}P_i/466`,
`Q_P=Y_P(AG1)-Y_P(AF1)`.

Report both policy numerators, observed-label counts, missing-label counts, overlap/Jaccard, AG1-only and AF1-only numerators, and the 31-person directional-swap decomposition. With shared missing P values, verify:
`Q_P=(31/466)*1000*(mean_P(AG1-only)-mean_P(AF1-only)))
whenever both swap means are defined. Report sharp lower and upper Q_P bounds by assigning one shared latent P_i to each missing participant; shared members cannot receive different labels under the two policies.

The sole new multiplicity family is `F77={Q_P}`. Use exactly d44’s 2,000 participant-level paired bootstrap over canonical-eid-sorted O1_hold, its PCG64DXSM SHA-256 seed construction, shared participant multiplicities, fixed rosters, fixed denominator, and no refitting/reranking. For support use the sharp-lower Q_P series; for adversity use the sharp-upper series. Report finite-draw count, SE, quantiles, one-sided 95% limit, fallback reason if the inherited finite/positive-variance condition requires it, and the family order/hash.

Use d44’s one-event planning margin `m=1000/466=2.145922746781116` per 1,000 as the predeclared minimum detectable roster-exchange resolution. This is a planning resolution, not a validated clinical utility or harm threshold.

Require all inherited gates plus:

- development thresholds are reproducible bitwise from the exact development-O roster and sex field;
- both instance ratio source fields and units are present, positive/finite, and source agreement/column uniqueness pass;
- at least 95% of O1_hold P labels are observed;
- at least 20 observed P labels in each AG1/AF1 list;
- at least 4 observed P labels across the 62-person directional swap;
- finite positive bootstrap uncertainty with at least 95% finite draws;
- exact shared-missingness bounds and swap identities pass.

A failed gate is inconclusive, never adverse. The endpoint is designed to be likely resolvable because P is a common repeated phenotype defined over the full 2,334-person holdout, rather than a sparse clinical event; nevertheless, the compiler must report actual counts and may not assume feasibility.

Emit exactly one child label:

- `grip_FFM_temporal_supportive`: all gates pass; sharp lower Q_P >= +m; and the simultaneous one-sided lower limit is strictly > +m.
- `grip_FFM_temporal_adverse`: all gates pass; sharp upper Q_P <= 0; and the simultaneous one-sided upper limit is <= 0. This rules out the prespecified repeated relative-weakness enrichment, not AF1 superiority or equivalence.
- `grip_FFM_temporal_inconclusive`: every other result, including missingness/gate failure, noncomputability, equality or uncertainty crossing a boundary, or a favorable point estimate without conservative support.

A supportive or adverse child label does not alter d44’s parent AG1:A1 biochemical or observed-low-UACR labels. The parent labels must be emitted unchanged first. If the parent is adverse or inconclusive, append `parent_not_supported_temporal_nonrescuing`; a favorable Episode-77 phenotype cannot rescue it. If the parent is supportive and Episode 77 is supportive, append `episode77_biologically_temporally_coherent`; if the parent is supportive and Episode 77 is adverse, append `episode77_grip_increment_not_temporally_coherent`; otherwise append `episode77_temporal_qualification_unresolved`.

## Exact source bindings and read-only rules

Use catalog `[internal dataset path]`, [source checksum], UKB snapshot `[source checksum]`. All files are ordinary CSVs with archive member null and one row per canonical eid; joins are horizontal one-to-one and must reject duplicate/missing keys.

| table | exact read-only source | descriptor / JSON hash / internal schema hash | fields used by Episode 77 |
|---|---|---|---|
| population | `[internal dataset path]`; [source checksum] | `datasets/ukb/table-38565c9e35e7cb6c.json`; `[source checksum]`; `[source checksum]` | `eid,31-0.0`; parent `21022-0.0` |
| assessment | `[internal dataset path]`; [source checksum] | `datasets/ukb/table-901ef6c7ddce2d51.json`; `[source checksum]`; `[source checksum]` | `eid,53-1.0,21003-1.0,21001-1.0,46-0.0,47-0.0,46-1.0,47-1.0,23101-0.0,23101-1.0` |
| main | `[internal dataset path]`; [source checksum] | `datasets/ukb/table-e4a9e4d8baa71a9d.json`; `[source checksum]`; `[source checksum]` | `eid,23101-0.0,23101-1.0`; parent covariates/outcomes only when inherited parent runs |
| biological_samples | `[internal dataset path]`; [source checksum] | `datasets/ukb/table-c6b666d905f3b02f.json`; `[source checksum]`; `[source checksum]` | parent `30700-1.0`; no new Episode-77 biomarker |
| health_outcomes | `[internal dataset path]`; [source checksum] | `datasets/ukb/table-3cfae45e0905b0e3.json`; `[source checksum]`; `[source checksum]` | no new Episode-77 field; inherited parent source remains sealed until parent outcome stage |

The descriptors declare `temporal_columns=[]`; no archive member or timestamp is available. Derived scripts/results stay in the workspace and source files remain read-only. The outcome-blind preflight script is `analysis/episode77_bio_audit.py`; it must be rerun by the compiler against the current catalog and must not be treated as a scientific result if its source or output hash differs.

## Verification and limits

Computationally checkable claims are exact source/header/descriptor/catalog hashes; one-to-one joins; parent population, split, transforms and rosters; development threshold reconstruction; ratio parsing; missing labels and bounds; fixed-denominator yields; swap identities; paired seeds/draws; gate states; and output-linked interpretation.

Adversarial fixtures must reject: using visit-1 values to define development thresholds; thresholding on O1_hold or policy membership; using cystatin, H1, D1, UACR outcome, N18, death or any selected-list endpoint to define P; treating FFM as direct muscle; treating two instances as verified elapsed-time persistence; changing the 25th-percentile rule; complete-case denominators; independent missing values for shared participants; reranking or refilling AG1/AF1; or interpreting a supportive label as measured-GFR accuracy, persistent CKD, sarcopenia, causality, benefit, cost, fairness, safety, transportability or routine use.

The phenotype is a repeated recorded-measurement qualification, not clinical adjudication. Stronger conclusions require repeated clinically timed grip/FFM measurements, device and protocol metadata, hydration/effort assessment, measured muscle or measured GFR where relevant, adjudicated CKD/frailty outcomes, external validation, and a prospective testing-strategy study. Automatic verification cannot establish that the two UKB instances represent a fixed elapsed interval, that FFM measures skeletal muscle, or that either policy improves patient outcomes.

## Direct-parent package closure

The sole scientific parent is `[prior hypothesis]`. Stage its complete direct-parent proposal and every attached executable/support artifact under their content-addressed paths, unchanged and without origin-path or global-cache substitution. Episode 77 adds only `analysis/episode77_bio_audit.py` and its derived result; it does not copy, edit, or regenerate d44’s parent artifacts. Any missing or hash-mismatched inherited artifact makes the inherited policy layer noncomputable and the Episode-77 result inconclusive, not a reason to alter the design.

## Remaining uncertainty

The actual policy-specific P numerators, Q_P, confidence limits, and child label are intentionally unopened. Feasibility of the repeated phenotype and the effect size across only 31 directional swaps remain empirical. A favorable computed contrast would support temporal biological coherence of this allocation comparison only; an adverse result would falsify that qualification; an inconclusive result would require better-timed repeated measurements or another study.
