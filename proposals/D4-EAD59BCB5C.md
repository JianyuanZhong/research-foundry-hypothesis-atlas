> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Resource-credit frontier: can UACR-first preserve target yield with fewer cystatin assays?

## Episode-15 controlling extension

This is a substantive child of [prior hypothesis]. The complete Episode-14 parent remains controlling except where this section explicitly adds cross-capacity comparisons. There is no change to O, V, recruitment time zero, the 2021 race-free equations, H, D, K18, the v3 60/20/20 participant locks, B/G/W/Q/F/T/A/AG predictors or fitting, development-only transforms and tuning, tie order, UACR censoring or median fallback, the seven equal-capacity selections, the 20% internal gates, bootstrap/placebo seeds, joint missing-label logic, source bindings, or evidence limits. No locked outcome is opened.

## Clinical question, supported evidence, and stronger unresolved hypothesis

The selected parent asks whether all-offered UACR-first AG has higher equation-defined target yield than immediate UACR-free G when both receive the same cystatin-C capacity at seven hypothetical operating points. That is an important but incomplete service question. UACR-first imposes one urine test attempt for every eligible adult. Equal cystatin counts therefore do not show whether the additional urine-screen resource is compensated by enough targeting gain.

The strongest claim supported before this experiment is limited. Chen et al. (Kidney Medicine 2024; DOI 10.1016/j.xkme.2024.100796; PMCID PMC10986041; frozen Europe PMC full-text XML source [source checksum], inspected) supports internal prediction of creatinine–cystatin eGFR differences in UK Biobank, not a resource-constrained testing policy. The Ovid abstract page for Awdishu et al. (JASN 2026; DOI 10.1681/ASN.0000001201; frozen source [source checksum], [source checksum], inspected) states that in-house availability is a barrier to cystatin-C adoption. It contains no service cost, turnaround, or assay-exchange estimate; no unavailable full paper is claimed read.

The parent's audited feasibility establishes only that frozen nested AG and G rankings can be truncated at the prespecified capacities. The unresolved, falsifiable Episode-15 hypothesis is stronger: across a prespecified planning band, AG can surrender five cystatin assays per 100 eligible adults and still identify a greater absolute number of H targets than G, with concordant D evidence, in both locked partitions. A separate ten-per-100 stress analysis estimates whether a larger sacrifice may be tolerated but cannot rescue failure of the five-point claim.

A supportive result would establish an internally replicated *capacity credit* under hypothetical fungible resource accounting. It would not estimate the price of UACR, show that one UACR attempt actually consumes 0.05 of a cystatin assay, prove equal total cost, identify an optimal budget, establish historical timing or future collection success, diagnose CKD, or show clinical benefit.

## Prespecified resource-exchange scenarios

Retain the parent's capacity set C={0.05,0.10,0.15,0.20,0.25,0.30,0.40}. For each partition p, let N_p=|O_p| and preserve n_pc=floor(c N_p), S_AG(p,c), and S_G(p,c) exactly.

Define a dimensionless hypothetical exchange rate rho as the cystatin-capacity fraction surrendered after imposing one UACR attempt on every member of O. If an immediate strategy has a total assay-equivalent allowance b N_p, the scenario gives G b N_p cystatin slots and AG (b-rho)N_p cystatin slots after N_p UACR attempts. This is an accounting scenario only. UKB has no costs, staff time, analyzer occupancy, turnaround, failed-collection workflow, or fungibility data.

Freeze:
- P_05={(0.10,0.05),(0.15,0.10),(0.20,0.15),(0.25,0.20),(0.30,0.25)}.
- P_10={(0.15,0.05),(0.20,0.10),(0.25,0.15),(0.30,0.20),(0.40,0.30)}.

Each tuple is (b,a): compare S_AG(p,a) against S_G(p,b). P_05 represents rho=0.05 and P_10 rho=0.10. The primary planning pairs are P_05 with b in {0.15,0.20,0.25,0.30}; (0.10,0.05) is a low-budget edge. P_10 is a prespecified secondary stress analysis. Never add 0.35, interpolate between grid points, optimize rho, choose a favorable pair after seeing outcomes, or refit/recalibrate any model. Assert that every selected-eid hash equals the corresponding Episode-14 set hash.

The scenario ledger is:
R_AG(p,b,rho)=(eligible=N_p, imposed_uacr_attempts=N_p, snapshot_uacr_usable=|V_p|, snapshot_uacr_unusable=|O_p\V_p|, accounting_total=b N_p, accounting_uacr_credit=rho N_p, cystatin_capacity=n_p,b-rho, cystatin_selected=n_p,b-rho, selected_from_U=|S_AG(p,b-rho)∩(O_p\V_p)|);
R_G(p,b)=(eligible=N_p, imposed_uacr_attempts=0, accounting_total=b N_p, cystatin_capacity=n_pb, cystatin_selected=n_pb).

Report integer assay counts and noninteger accounting totals separately; floor only the cystatin selections through inherited n_pc. These vectors do not assert observed orders or costs.

## Absolute population-yield estimands

Different cystatin counts make the parent's per-1,000-assay yield unsuitable for this question. For E in {H,D,H18}, define absolute target count per 1,000 eligible:
Z_E(S,p,c)=1000 sum_{i in S} E_i / N_p,
where H18 means H_i K18_i. For each (b,a) report
Psi_E(p;b,a)=Z_E(S_AG(p,a),p,a)-Z_E(S_G(p,b),p,b).

Always use N_p, including participants with missing labels, as denominator. Also report raw target counts, selected counts, observed-label counts, overlap, AG-only and G-only counts, and the identities
Psi_E=1000[sum_{AG-only}E_i-sum_{G-only}E_i]/N_p
and
Psi_E=a Y_E(AG,a)-b Y_E(G,b) up to the exact floor correction, which must be computed explicitly rather than ignored. Do not normalize by n_pa, n_pb, observed labels, overlap, or swap counts.

For each b report the prespecified pointwise capacity-credit status at rho=0,0.05,0.10 where defined. The largest supported rho may be reported only as an interval-censored descriptive summary on this grid and only if all lower tested rho values at that b also support. A nonmonotone pattern is reported as nonmonotone and cannot be summarized by a threshold.

## Missing labels and inference

For a cross-capacity contrast define q_i=I[i in S_AG(p,a)]-I[i in S_G(p,b)]. Apply the inherited shared-person sharp assignment: the lower numerator adds sum_missing min(0,q_i), the upper adds sum_missing max(0,q_i); for H18 use q_i K18_i. One person's unknown label is common across policies and capacities. More than 1% of O without valid cystatin keeps every performance claim inconclusive. Do not impute, drop, or use selected-label denominators.

Reuse the parent's 2,000 paired bootstrap draws exactly. Within a draw, use the same O_p multiplicities for all policies and capacities, fixed memberships, fixed N_p and n_pc, and no refitting. Pooled D/H18 resamples each lock independently and sums numerators over summed eligible denominators.

Preserve the parent's complete 50/12/14 simultaneous families as subsets. Add all ten P_05/P_10 cross-capacity contrasts:
- F_H_credit: 50 parent components plus Psi_H in both locks for ten pairs =70.
- F_D_credit: 12 parent components plus pooled stratified Psi_D for ten pairs =22.
- F_18_credit: 14 parent components plus pooled stratified Psi_H18 for ten pairs =24.

Use the inherited max-|t| studentization, one-sided max-t lower limits, finite-replicate rules, and Bonferroni fallback. Report exact family order and component hash. Primary conclusions use adverse sharp point bounds together with simultaneous intervals. Pairwise intervals outside these families cannot support a claim.

## Supportive, adverse, and inconclusive rules

First emit the complete inherited equal-capacity frontier label unchanged. Emit credit_05_{b} for all five P_05 pairs and credit_10_{b} for all five P_10 pairs, plus one Episode-15 global label.

A primary P_05 planning pair supports biochemical credit only if, in both test and replication:
1. the adverse-bound Psi_H is strictly positive and its familywise one-sided lower limit is >0;
2. lock-specific adverse-bound Psi_D is >0 and the pooled F_D_credit lower limit is >0;
3. all selected hashes/counts, missingness, variants, nesting, calibration, sex, placebo, leakage, and integrity checks inherited from the parent pass; and
4. every inherited equal-capacity gate required for capacity_frontier support passes.

The low-budget (0.10,0.05) edge must satisfy the same directional H and D criteria but is not used to claim performance below 5%. All four planning pairs plus the edge are required for the global five-point claim. P_10 is secondary: label each pair supportive only under the analogous criteria, adverse under the rules below, otherwise inconclusive. P_10 cannot rescue P_05 or the inherited frontier.

A pair is adverse for H if, with adequate computation, either lock's simultaneous upper limit is <=0 or its sharp upper bound is <=0. It is adverse for D if the pooled simultaneous upper is <=0 or either lock has a sharp upper <=0. This falsifies the claimed capacity credit at that named budget; it does not prove immediate G is cheaper or clinically superior. A positive point estimate whose lower limit crosses zero is inconclusive, not supportive. Lock disagreement, nonmonotonicity, missingness, UACR-variant sign reversal, sex instability, sparse swaps, integrity failure, or noncomputability is inconclusive unless a favorable sharp upper already establishes adverse.

Emit exactly one:
- resource_credit_supportive_chronic_supported: inherited capacity frontier is biochemically supportive; all five P_05 pairs support H and D; every required N18 count gate passes; and pooled adverse-bound Psi_H18 plus its F_18_credit lower limit are >0 for all four planning pairs.
- resource_credit_supportive_chronic_unresolved: inherited biochemical frontier and all five P_05 H/D pairs support, but N18 is sparse or nonadversely uncertain, with no adequately informed adverse N18 pair.
- resource_credit_adverse: an inherited required gate or at least one adequately precise P_05 H/D pair is adverse. Name b,a,lock/pooled endpoint, estimate, sharp bound, simultaneous interval, and reason.
- resource_credit_inconclusive: no adverse gate is established but full support fails through uncertainty, disagreement, missingness, instability, nonmonotonicity, integrity failure, or noncomputability.

N18 observed-event minima remain the parent's: at least 100 observed H×K18 events in the pooled union relevant to a claim, at least 20 in each pooled directional difference set, and at least 30 in a lock for a lock-specific positive statement. Missing H cannot satisfy counts. Sparse N18 means chronic consequence unresolved, never biochemical adversity. K17/Kany, survival models, tranches, P_10, and longer follow-up cannot rescue.

## Exact data bindings and audit

All inputs are read-only ordinary CSVs (archive member null) in UKB snapshot [source checksum]. Full catalog: [internal dataset path], [source checksum]. Join one row per eid by one-to-one horizontal joins; reject duplicate/missing eid or disagreement in overlapping loaded fields.

- population table, [internal dataset path], schema datasets/ukb/table-38565c9e35e7cb6c.json, [source checksum]: eid, sex 31-0.0, age 21022-0.0.
- assessment table, [internal dataset path], schema datasets/ukb/table-901ef6c7ddce2d51.json, [source checksum]: eid, recruitment 53-0.0, repeat date 53-1.0, grips 46-0.0/47-0.0 and 46-1.0/47-1.0, BMI 21001-0.0, pace 924-0.0, health 2178-0.0, stress fields 2443-0.0, 4080-0.0/4080-0.1, 6153-0.0…6153-0.3, 6177-0.0…6177-0.2.
- biological_samples table, [internal dataset path], schema datasets/ukb/table-c6b666d905f3b02f.json, [source checksum]: eid, urine albumin 30500-0.0, albumin flag 30505-0.0, urine creatinine 30510-0.0, urine-creatinine flag 30515-0.0, serum creatinine 30700-0.0, cystatin C 30720-0.0, repeats 30700-1.0/30720-1.0, stress HbA1c 30750-0.0.
- health_outcomes table, [internal dataset path], schema datasets/ukb/table-3cfae45e0905b0e3.json, [source checksum]: eid, codes 41270-0.0…41270-0.258 paired positionally with dates 41280-0.0…41280-0.258, and deaths 40000-0.0/40000-1.0.

This Lead inspected the full catalog metadata, all four schemas, and physical headers. The headers have 34, 18,159, 1,775, and 4,896 unique columns with every named field present and no duplicate header. Every schema has temporal_columns=[]; the biological header contains no name with date, time, order, collect, or result. No row was sampled or filtered, and no H, D, K18, death, score, selection, or yield was opened. Inherited O=134,118 and V=130,257 (97.12%) are provenance, not a new result or a prospective completion rate. HCC, MIMIC and eICU remain available read-only but have no UKB eid linkage and are not joined.

## Interpretation boundary and stronger evidence needed

Support means only that frozen AG found more one-time equation-defined H targets per eligible person than frozen G despite five fewer cystatin slots per 100 eligible people, at the prespecified internal UKB grid points, with D concordance and optionally N18-coded enrichment. Adverse means the five-point resource-credit claim failed at a named operating point; it does not establish G's cost-effectiveness or patient benefit. Inconclusive is not equivalence.

Applying rho to a real service requires local, prospective measurement of UACR orders, successful collections, invalids/retries, result-release and cystatin-order timestamps, analyzer and staff capacity, marginal and fixed costs, turnaround, burden, and whether resources are fungible. Persistent CKD requires repeated clinically timed measurements; kidney truth requires measured GFR and expert adjudication; complete prognosis requires outpatient events and censoring. Choosing a workflow needs downstream actions, harms, utility, equity review and external validation. Patient benefit requires a prospective implementation or randomized testing-strategy study.

## Compiler and verifier contract

In addition to every inherited output, emit for each p and pair: N_p; b,a,rho; n_pb/n_pa; selected hashes; ledgers; raw/observed/missing H,D,H18 counts; Z and Psi point estimates; sharp bounds; simultaneous intervals; overlap/directional-set counts; floor-correction identity; family order/hash; finite-draw fraction; fallback; pair label and machine-readable reason. Emit the inherited frontier label before the Episode-15 label.

The automatic verifier can check source identity, headers, joins, frozen rankings/selections, pair grid, counts, per-eligible denominators, ledgers as scenario arithmetic, bounds, resampling, multiplicity, integrity gates, result labels, and whether conclusions follow outputs. It cannot verify rho as a real exchange rate, observed workflow timing, future UACR completion, cost, feasibility, persistent/adjudicated CKD, measured GFR, complete event capture, fairness, action, transportability, or benefit.

Adversarial fixtures must reject: same-capacity substituted for cross-capacity comparison; b/a reversed; 20% of V; refitting; added 35% interpolation; post hoc rho; selected or observed-label denominator; per-assay yield treated as per-eligible yield; omitted floor correction; independent policy bootstraps; marginal rather than shared-person bounds; omitted credit components from multiplicity; calling rho observed cost or efficiency; calling imposed attempts observed; and correct arithmetic attached to claims of workflow superiority, diagnosis, prevention, cost-effectiveness, or benefit.
