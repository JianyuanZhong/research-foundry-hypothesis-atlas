# Direct all-offered comparison of intention-to-obtain-UACR-first versus immediate UACR-free cystatin-C allocation

## Clinical decision, evidence boundary, and advance

A health service can assay cystatin C in exactly 20% of adults aged 40–69 whose baseline 2021 race-free creatinine eGFR (eGFRcr) is 60–89 mL/min/1.73 m². The consequential unresolved decision is whether to (1) attempt UACR in every eligible adult, wait until a usable result or a protocol-defined failure, use a frozen fallback after failure, and allocate cystatin C with the all-O AG score; or (2) allocate cystatin C immediately to all-O candidates with the UACR-free G score. Both strategies receive the identical absolute cystatin capacity. They do not receive equal total resources.

The strongest evidence already supported is narrower. Chen et al. (Kidney Medicine 2024; DOI 10.1016/j.xkme.2024.100796; PMCID PMC10986041; frozen Europe PMC full-text XML source [source checksum], inspected for this proposal) studied 468,969 UK Biobank participants, developed clinical and enriched models in 375,175, internally validated them in 93,794, and reported validation AUC 0.75 for the enriched model. This supports association and internal predictability of large creatinine–cystatin eGFR differences from demographic, clinical, laboratory and lifestyle characteristics. It does not establish a fixed-capacity testing strategy, incremental grip value, a UACR-first workflow, measured-GFR accuracy, chronicity, treatment benefit, cost-effectiveness, or external transportability.

The unresolved claim tested here is that the intention-to-obtain-UACR-first strategy analog identifies materially more prespecified biochemical targets per 1,000 cystatin assays than immediate UACR-free allocation, in both untouched locks, while retaining everyone offered UACR in the denominator and candidate pool. The substantive advance over the direct-workflow parent is removal of its per-protocol mismatch: the primary UACR-first selected set is the all-O AG set, including O\V through the frozen median fallback, rather than the AG_V set restricted to snapshot-usable UACR. The mature executable parent's population, recruitment time zero, outcomes, score definitions, v3 splits, exact O-based 20% capacity, inference, internal comparator gates and evidence limits are unchanged. V remains a secondary usable-result analysis only.

This is a retrospective strategy analog, not an emulation of observed UKB ordering. “Intention-to-obtain” is an imposed hypothetical protocol assignment: it does not mean UKB participants were offered testing, that UACR was available before cystatin allocation, or that future collection would succeed. The experiment compares biochemical allocation under two deterministic information strategies; it does not estimate causal benefit.

## Primary falsifiable hypothesis

For each locked partition p (test and replication), let n_p=floor(0.20×|O_p|). Let ITO_AG_p be the top n_p all-O participants under frozen AG after applying observed snapshot UACR where usable and the frozen primary fallback otherwise. Let IM_G_p be the top n_p all-O participants under frozen UACR-free G.

Primary biochemical support requires, in both locks and under the adverse joint missing-label assignment:

- Δ_H(ITO_AG:IM_G) ≥2 additional H targets per 1,000 cystatin assays;
- H-yield ratio ITO_AG/IM_G ≥1.10;
- simultaneous lower limits above 0 for the difference and above 1 for the ratio;
- positive target yield in the equal-size ITO_AG-only versus IM_G-only swap sets;
- positive Δ_D in each lock and a pooled simultaneous lower limit above 0.

If the frozen N18 information thresholds pass, primary prognostic support additionally requires pooled adverse-bound Δ_H18(ITO_AG:IM_G) ≥1/1,000 with simultaneous lower limit above 0. Every applicable all-O W0 and W1_ITO internal gate, missingness, calibration, placebo, sex, UACR-variant, leakage, integrity and replication gate below remains mandatory. The V analysis is not a primary gate and cannot rescue or overturn the all-O direct result merely because it differs.

## Exact sources and availability

All sources are read-only ordinary CSV files (member=null) in UKB snapshot [source checksum]. Join one row per eid by one-to-one horizontal joins; reject duplicate/missing eids and disagreement in overlapping loaded columns. Full catalog: [internal dataset path], [source checksum].

- population: [internal dataset path]; schema datasets/ukb/table-38565c9e35e7cb6c.json; [source checksum]; columns eid, sex 31-0.0, age 21022-0.0.
- assessment: [internal dataset path]; schema datasets/ukb/table-901ef6c7ddce2d51.json; [source checksum]; eid, recruitment 53-0.0, repeat date 53-1.0, grip 46-0.0, 47-0.0 and repeats 46-1.0, 47-1.0, BMI 21001-0.0, pace 924-0.0, health 2178-0.0; stress fields 2443-0.0, 4080-0.0, 4080-0.1, 6153-0.0…6153-0.3, 6177-0.0…6177-0.2.
- biological_samples: [internal dataset path]; schema datasets/ukb/table-c6b666d905f3b02f.json; [source checksum]; eid, urine albumin 30500-0.0, albumin flag 30505-0.0, urine creatinine 30510-0.0, urine-creatinine flag 30515-0.0, serum creatinine 30700-0.0, cystatin C 30720-0.0, repeats 30700-1.0, 30720-1.0, stress HbA1c 30750-0.0.
- health_outcomes: [internal dataset path]; schema datasets/ukb/table-3cfae45e0905b0e3.json; [source checksum]; eid, inpatient codes 41270-0.0…41270-0.258 paired position-for-position with dates 41280-0.0…41280-0.258, deaths 40000-0.0, 40000-1.0.

The four schemas and physical headers were inspected in this episode: 34, 18,159, 1,775 and 4,896 unique columns, respectively; every named boundary field is present; each schema has temporal_columns=[]; and the biological header contains no column name containing date, time, order, collect or result. No source data row was sampled or filtered in this episode and no H, D, K18, death or policy yield was opened. The parents' inherited read-only feasibility result (O=134,118, V=130,257, 97.12%) is provenance, not a newly inspected outcome or a prospective success estimate. HCC, MIMIC and eICU remain directly accessible but have no UKB eid linkage and are not joined. All derived files belong in the workspace.

## Population O, locks, and snapshot usability V

Parse dates strictly as calendar dates. canonical_decimal_eid is the unsigned base-10 integer representation with no leading zeros; zero and any noninteger representation are invalid. Female is 31-0.0=0, male =1; other values are invalid.

O contains one row per eid meeting all of: age 40–69 inclusive; valid sex and 53-0.0; finite positive BMI and serum creatinine; at least one finite positive baseline grip; full-precision 2021 race-free eGFRcr in [60,90); and no exactly paired inpatient N17* or N18* code on or before recruitment. For i=0,…,258, trim and uppercase 41270-0.i only and pair only with 41280-0.i. Exclude and report anyone with an N17*/N18* code but blank/unparseable paired date. Recorded absence is not clinical absence. O does not require cystatin, UACR, pace, health or outcome.

Let Scr=30700-0.0/88.4 mg/dL. In binary64 without rounding:

eGFRcr = 142 × min(Scr/k,1)^α × max(Scr/k,1)^−1.200 × 0.9938^age × 1.012 if female,

with (k,α)=(0.7,−0.241) female and (0.9,−0.302) male. Freeze fixtures for both sexes, Scr/k below/at/above 1, and the 60/90 boundaries. The bitwise value defines O, enters B and orders T.

Before any locked label is read, set h=int(SHA256(UTF8("ukb-grip-cys-v3|"+canonical_decimal_eid)).hexdigest(),16) mod 100: development h<60, test 60≤h<80, replication h≥80. Assert no overlap.

V is the fixed subset of O with positive finite urine creatinine c=30510-0.0 and either positive finite numeric urine albumin a=30500-0.0, or blank albumin with trimmed 30505-0.0 exactly <6.7. Numeric-plus-nonblank-flag is an integrity failure. Primary censored a=3.35 mg/L. UACR=1000a/c mg/mmol. Missing/nonpositive c, missing albumin without that exact flag, another albumin flag or nonfinite ratio is outside V. Audit 30515-0.0 but never use it as albumin flag. V is invariant across sensitivities.

For each p, n_p=floor(.20×|O_p|). Every all-O policy selects n_p from O_p; every V policy selects the same n_p from V_p. Require |V_p|≥n_p and |V_p|/|O_p|≥.95; never use 20% of V.

## Labels, outcomes, and temporal boundaries

L is O with finite positive baseline cystatin C Scys=30720-0.0. For L:

eGFRcr-cys = 135 × min(Scr/k,1)^α × max(Scr/k,1)^−0.544 × min(Scys/0.8,1)^−0.323 × max(Scys/0.8,1)^−0.778 × 0.9961^age × 0.963 if female,

with (k,α)=(0.7,−0.219) female and (0.9,−0.144) male. H=1 iff eGFRcr-cys<60.

eGFRcys = 133 × min(Scys/0.8,1)^−0.499 × max(Scys/0.8,1)^−1.328 × 0.996^age × 0.932 if female.

D=1 iff eGFRcys/eGFRcr≤0.70; eGFRcys−eGFRcr<−15 is sensitivity only.

For each O participant, T18 is the earliest valid exactly paired N18* date in (recruitment, recruitment+10 calendar years]. Death is the earliest valid 40000-0.0 or 40000-1.0. K18=1 only when T18 exists and death is absent or strictly later; death on or before T18 competes, with same-day death preceding N18. Define T17/K17 analogously and Kany from the earlier eligible T17/T18; N17 neither satisfies nor censors K18. Report duplicate/invalid pairs, N17 before N18, and death without earlier K18. K17 and Kany are diagnostic only. Missing outpatient events, emigration and individual censor dates prevent complete-follow-up claims.

H is equation-based one-time biochemical reclassification, D a marker-discordance phenotype, and K18 an unadjudicated inpatient-code outcome. None is measured GFR, persistent CKD, mechanism or benefit.

## Exact predictors and scores

All quantiles use NumPy method="linear" (R type 7), SDs use ddof=0, and transform constants come from development O without H. Zero SD, nonunique spline boundary or nonfinite transform makes the affected branch noncomputable.

For continuous x, use development-O knots ξ1…ξ4 at 5%,35%,65%,95%; u_j(x)=max(x−ξ_j,0)^3; and for j=1,2:

r_j(x)=[u_j(x)−((ξ4−ξ_j)/(ξ4−ξ3))u_3(x)+((ξ3−ξ_j)/(ξ4−ξ3))u_4(x)]/(ξ4−ξ1)^2.

For age, BMI and eGFRcr, B contains x,r1,r2, each standardized by its development-O mean/SD. B is exactly an unpenalized intercept, raw sex 0/1 and these nine columns.

Raw grip R is the maximum finite positive 46-0.0/47-0.0, winsorized at development-O 0.5%/99.5%, then standardized to Z_R. G=B+Z_R exactly once: no residualization, spline, interaction, sex-specific scale, side, handedness or missingness column.

W=B plus pace burden 924-0.0 mapped 1→2, 2→1, 3→0; all else to its development-O valid mean, then standardized. Q=B plus health 2178-0.0 retaining 1–4; all else to its development-O valid mean, then standardized. No global negative-code rule.

For A, m_A is the median usable development-O UACR. Completed UACR is observed for V and m_A otherwise. Apply log1p, winsorize at 1%/99% of development-O usable log1p(UACR), then standardize using completed-and-winsorized development O to Z_A. A=B+Z_A; AG=A+Z_R. No UACR missing indicator, category, spline, interaction, future value, cystatin or locked statistic. This completed value is the frozen fallback for every O\V participant in the primary all-O strategy analog; no participant is dropped.

Before unlocking, freeze six UACR stress variants: censored a in {0,3.35,6.7} mg/L crossed with unavailable UACR imputed to the development-O 1st or 99th percentile of usable UACR. Repeat log1p/winsorization/standardization and refit A/AG in development. Variants never rescue primary failure.

Nonrescuing C=A plus diabetes 2443-0.0, mean positive 4080-0.0/4080-0.1 and sex-appropriate medication code 2 in the listed arrays, using development medians/modes plus explicit missing indicators; CG=C+Z_R. A second descriptive version adds positive 30750-0.0 with development median/missing indicator.

## Exact fitting, tuning, F selection, and ties

Fit models for H only on development L; never use D, K18, death or postbaseline fields. CV fold f=int(SHA256(UTF8("ukb-grip-cys-cv-v3|"+canonical_decimal_eid)).hexdigest(),16) mod 5. Ridge grid λ={10^(−6+0.5j):j=0,…,20}. Minimize mean training binomial negative log likelihood +(λ/2) times squared coefficients except intercept, binary64 deterministic L-BFGS, zero initialization, 20,000 iterations maximum, gradient infinity tolerance 1e−9 and objective tolerance 1e−12. Report nonconvergence and make that policy noncomputable.

For each model, calculate five validation-fold mean log losses. λ_min minimizes their unweighted mean; ties at 12 decimals choose larger λ. SE is sample SD of the five means/sqrt(5). Choose the largest λ with mean ≤mean(λ_min)+SE(λ_min), then refit all development L.

For W and Q separately, use chosen λ to refit four folds and rank the held-out development-L fold; select floor(.20×|L_fold|), calculate H/1,000, and average five fold yields unweighted. F is the higher mean-yield policy; equality at 12 decimals chooses W. Freeze all column names/order, constants, λ, coefficients, F, versions and hashes before accessing lock labels.

Every fitted policy ranks descending H probability. T ranks ascending full-precision eGFRcr. Break ties by ascending full 256-bit SHA256 of UTF8("ukb-grip-cys-tie-v3|"+canonical_decimal_eid), then eid only for a digest collision. Record cutoffs, ties and selected-eid hashes. B,G,W,Q,F,T,A,AG rank all O_p. A_V,AG_V,G_V,B_V,T_V apply unchanged scores to V_p at n_p, with no refit.

## Information states, protocol, fallback, and resource vector

Let τ_alloc be list commitment, t_collect urine collection and t_result usable result release. “Prior” requires t_collect≤t_result≤τ_alloc; “post” requires t_result>τ_alloc; otherwise timing is unknown. Never infer chronology from instance 0, recruitment date, same-row storage or nonmissingness.

The mandatory audit emits timing_fields_present=false, assignable_prior_count=0, assignable_post_count=0, timing_unknown_count=|V_p|, timing_unknown_fraction=1 and observed_preassay_estimand_evaluable=false. Zero assigned rows means unclassifiable, not postallocation.

The hypothetical W1_ITO protocol offers/attempts UACR once for every O_p participant before allocating cystatin, waits for a usable released result or a prospectively prespecified operational failure declaration, uses the result when usable, applies the frozen median fallback after declared failure, and ranks every O_p with AG to select n_p. UKB lacks the timestamps and attempt/failure records needed to instantiate a wait deadline; the retrospective computation therefore uses V as snapshot usability and O\V as the fallback stratum. It evaluates this fixed mapping, not future collection success or delay.

W0_IM allocates immediately with G over all O_p and makes no UACR attempt for allocation. The primary direct contrast is ITO_AG=AG_p versus IM_G=G_p. Both contain n_p and both candidate pools are O_p.

W1_PP is secondary: AG_V:A_V and G_V:A_V among snapshot-usable V at unchanged n_p, without refit. It is conditional usable-result evidence, not all-offered, immediate, prior, or a replacement for ITO_AG. Wobs historical preassay remains nonevaluable and contains no numeric estimate.

For U_p=O_p\V_p, report before outcomes:

R_ITO(p)=(eligible=|O_p|, imposed_uacr_attempts=|O_p|, snapshot_uacr_usable=|V_p|, snapshot_uacr_unusable=|U_p|, cystatin_capacity=n_p, cystatin_selected=n_p, selected_from_U=|ITO_AG_p∩U_p|);

R_IM(p)=(eligible=|O_p|, imposed_uacr_attempts=0, cystatin_capacity=n_p, cystatin_selected=n_p).

The attempts are imposed by the hypothetical protocol, not observed UKB actions. Snapshot usable/unusable counts are not successful/failed future collections. selected_from_U documents fallback behavior. Equality of n_p establishes only identical cystatin capacity, never equal cost, turnaround, burden, feasibility or total resources.

## Estimands, missing labels, inference, and multiplicity

For fixed S with denominator n_p: Y_H=1000ΣI(i∈S)H_i/n_p; Y_D analogously; Y_H18=1000ΣI(i∈S)H_iK18_i/n_p. Report selected and observed-label counts, yields, ratios, overlap, Jaccard and challenger-only minus comparator-only decompositions. Never change the denominator to observed labels.

For missing H/D, a single-policy contribution ranges 0–1. For contrast S:C use c_i=I(S)−I(C): joint lower adds Σ_missing min(0,c_i), upper adds Σ_missing max(0,c_i); for H×K18 use c_iK18_i. Shared participants use one common unknown value. Compute exact ratio extrema over the same assignments; feasible zero comparator numerator makes the ratio and branch inconclusive. More than 1% of O lacking valid cystatin makes every performance claim inconclusive.

Use 2,000 paired bootstraps without refitting, with fixed transforms, membership, n_p and V. Sort O_p by canonical eid. For partition and zero-based draw b, initialize NumPy Generator(PCG64DXSM(full unsigned big-endian SHA256(UTF8("ukb-grip-bootstrap-v3|"+partition+"|"+b)))) and draw |O_p| integer indices with replacement; use multiplicities and retain n_p. Pooled draws resample each lock independently using its seed, sum numerators/denominators, and never pool first.

The simultaneous F_H family contains, in both locks, differences G:B,G:F,G:T,AG:A,G:A,AG_V:A_V,G_V:A_V, and the primary AG:G; plus log ratios G:B,G:T,AG:A,AG_V:A_V,AG:G: 26 statistics. F_D contains pooled stratified differences G:F,G:T,AG:A,G:A,AG_V:A_V,AG:G: 6. F_18 contains pooled G:B,G:F,G:T,AG:A,G:A,AG_V:A_V,G_V:A_V,AG:G: 8. This expansion is mandatory; the new direct claim may not use intervals from the smaller parent family.

For component j estimate bootstrap SE s_j. If every s_j is finite/positive and ≥95% ratio replicates finite, use t_bj=(θ_bj−θ_j)/s_j; q_.95 is NumPy-linear 95th percentile of draw-wise max_j|t_bj|; two-sided interval θ_j±q_.95s_j, exponentiating log ratios. One-sided lower uses the 95th percentile of max_j[(θ_j−θ_bj)/s_j]. If studentization fails, use componentwise Bonferroni percentiles with two-sided tail .025/m or one-sided .05/m, mark fallback, and make components with <95% finite replicates inconclusive.

Freeze 500 G placebos per lock by permuting Z_R within sex×pace×health strata, merging cells <20 first across health within sex/pace then same-sex, with frozen maps. Draw d uses PCG64DXSM from full big-endian SHA256("ukb-grip-placebo-v1|partition|d"), lexical strata and ascending eid. Hold B, G coefficient, transforms and penalty fixed; rerank/select n_p. Actual G:B must strictly exceed the 97.5th percentile in each lock; p=(1+#placebo≥actual)/501.

Report calibration among observed L: prevalence, sensitivity, PPV, selected-count calibration, Brier, unpenalized intercept/slope on frozen score logit and fixed-capacity decision curves. For direct support, finite G and AG slopes must each be [0.8,1.2] in both locks. Separation/nonconvergence is inconclusive; finite out-of-range is adverse stability. Report AG in V separately.

Freeze sex-specific contrasts. Sex instability exists if AG:G or any required internal superiority contrast is ≤0 for the same sex in both locks while overall gates pass; this makes clinical interpretation inconclusive. Selection imbalance and grip×sex are descriptive and require equity review.

Any all-O AG:G H or D sign reversal in a frozen UACR variant, V changing across variants, snapshot UACR unavailability >5% in either lock, or hand-definition/sex/frailty/lock instability is inconclusive. Sensitivities and C/CG cannot rescue.

N18 support requires ≥100 observed-label H×K18 events in the union of relevant primary selections across locks, ≥20 in every pooled directional swap set used for a claim (including both AG:G directions), and ≥30 in a lock for a positive lock-specific statement. Missing H cannot satisfy counts. Failure means chronic-kidney consequence unresolved, not adverse. Report Aalen–Johansen N18 cumulative incidence with competing death; Cox/Fine–Gray, K17, Kany and death-without-prior-K18 are descriptive.

When those counts pass, preserved W0 N18 support requires adverse-bound pooled Δ_H18(G:B)≥1/1,000 with simultaneous lower >0 and G:F/G:T noninferiority lower limits >−1/1,000. Preserved W1_ITO support requires adverse-bound pooled Δ_H18(AG:A)≥1/1,000 with lower >0 and G:A lower >−1/1,000. Secondary W1_PP applies the same +1 and −1 gates to AG_V:A_V and G_V:A_V. The primary direct gate is adverse-bound pooled Δ_H18(AG:G)≥1/1,000 with lower >0. A sufficiently informed superiority result is adverse if its upper interval is below +1 or wholly ≤0; noninferiority is adverse if its upper interval is ≤−1; boundary-crossing intervals are inconclusive. N17/composites cannot rescue.

## Preserved internal falsification gates and exact result classes

W0 internal biochemical support requires in both locks under adverse bounds: G:B,G:F,G:T Δ_H≥2/1,000; ratios G:B≥1.25 and G:T≥1.10; required simultaneous limits >0/>1; positive G-only directional swaps versus F/T; placebo pass; positive D versus F/T in each lock and pooled lower limits >0; G calibration pass; no sex flag or integrity failure.

W1_ITO internal support requires all-O AG:A Δ_H≥2/1,000, ratio≥1.10, simultaneous limits >0/>1, positive directional H swap and D in each lock with pooled lower >0; G:A H and D noninferiority under adverse bounds and one-sided simultaneous lower limits >−1/1,000; all six variants concordant; AG calibration pass; no sex flag. This is all-O and uses fallback.

W1_PP retains identical AG_V:A_V superiority and G_V:A_V noninferiority gates at O-based n_p, plus V preflight, variants and calibration, but is explicitly secondary. Its result is reported and can reveal candidate-pool or fallback sensitivity; it neither defines nor rescues the direct all-offered decision.

A superiority/materiality gate supports only if its adverse joint difference bound reaches m, simultaneous lower difference >0, and required point/adverse-bound ratio reaches target with simultaneous lower ratio >1. It is adverse with adequate precision if the simultaneous upper difference is below m, feasible/simultaneous ratio upper is below target, or required directional swap ≤0; otherwise inconclusive. Noninferiority supports when adverse-bound and simultaneous lower are >−1; it is adverse when favorable joint upper or simultaneous upper ≤−1; otherwise inconclusive. D follows zero or −1 margins. Undefined computation, excessive missingness, variant reversal, sex instability, lock disagreement, feasible zero denominator or sparse events is inconclusive, not adverse.

Emit the primary direct label:

- cross_workflow_all_O_supportive_chronic_supported: AG:G direct biochemical gates, W0 and W1_ITO internal gates, all stability/integrity gates, and sufficient N18 gates all support.
- cross_workflow_all_O_supportive_chronic_unresolved: all required biochemical gates support, while N18 is sparse or a nonadverse interval crosses its boundary.
- cross_workflow_all_O_adverse: at least one adequately precise direct, W0/W1_ITO internal biochemical, or sufficiently powered N18 gate is adverse; identify the exact gate. A negative finding is useful evidence against the failed allocation claim.
- cross_workflow_all_O_inconclusive: no adverse gate is established but support fails from uncertainty, lock disagreement, missingness, instability, sparse swaps/events, integrity or noncomputability.

Also emit branch labels for direct AG:G, W0, W1_ITO and secondary W1_PP, each supportive/adverse/inconclusive, plus observed_preassay_not_identifiable. PP support with all-O direct failure never establishes UACR-first value; PP failure with all-O direct support suggests fallback/candidate-pool heterogeneity and limits interpretation but does not mechanically reverse the prespecified all-offered estimate. Wobs is always evaluable=false, reason=required_timestamps_absent, with no numeric policy estimate.

No development result, pooled point alone, sensitivity, C/CG, N17, Kany, V-only result or longer follow-up rescues a failed primary gate.

## Supportive, adverse, inconclusive meanings and stronger evidence needed

A supportive result means only that, in both internal UKB locks under the frozen snapshot/fallback mapping and equal cystatin counts, AG selected more equation-defined H/D targets than G by the prespecified margins, with N18-coded enrichment only if its gates pass. It justifies prospective comparison of these strategies; it does not show a preferred workflow, lower cost, better care or true CKD.

An adverse result means adequately precise evidence against at least one prespecified allocation claim. AG:G below materiality argues against adding the UACR-first mapping for cystatin assay yield in this population; failure of G's internal comparators questions the immediate strategy; failure of W1_ITO internal gates questions the UACR-first score. It does not prove the other workflow improves outcomes.

An inconclusive result means the data cannot distinguish the strategies at the frozen margins because of uncertainty, disagreement, missing labels, sparse events/swaps, instability or failed computation. It is not equivalence and cannot be repaired by V-only or sensitivity evidence.

The exact additional data needed to test actual collection success and implementation are participant-level UACR offer/order, collection, result release, invalid/failure reason, retry, protocol deadline and cystatin list/order timestamps. Persistent albuminuria/reduced filtration requires repeated measurements; kidney truth requires measured GFR and clinical adjudication; complete prognosis requires outpatient events, emigration/censoring and chart review; workflow choice requires turnaround, workload, monetary cost, burden, downstream action, harms and utility; transportability requires external validation; benefit requires a prospective implementation or randomized testing-strategy study with patient-centered outcomes.

## Verification contract and limits

The result must contain source/hash/header and join audits; O/L/V/U exclusions and counts; timing audit; transform/fold/grid/fit hashes; coefficients and F identity; selected-eid hashes, counts and ties; the two resource vectors and selected_from_U; all yields, exact joint bounds, ratios, swaps, bootstrap seeds/fallbacks/families; calibration, placebo, sex, variants and N18 sufficiency; branch/global labels; and machine-generated reasons.

Adversarial fixtures must reject: wrong creatinine/UACR units; confusion of 30505 and 30515; treating <6.7 as measured 6.7; changing O/V/n; using 20% of V; dropping O\V from ITO_AG; replacing AG with AG_V in the direct contrast; failing to use/report fallback; calling O\V a prospective failure rate; counting |V| rather than |O| imposed attempts; refitting in V/locks; score-column/grid/fold/tie/seed changes; outcome leakage; marginal instead of joint bounds; independently bootstrapped policies; omission of AG:G from multiplicity; mispaired code/date arrays; N17 censoring N18; same-day death after N18; instance 0 labeled prior; numeric Wobs; equal cystatin called equal cost; and correct arithmetic attached to claims of sarcopenia, CKD diagnosis, cost-effectiveness, workflow superiority, prevention or benefit.

The automatic verifier can establish source identity, header/timestamp absence, joins, equations, O/L/V/U, deterministic models/rankings, fallback use, equal cystatin count, imposed attempt accounting, bounds, resampling, multiplicity, gates and whether submitted conclusions follow outputs. It cannot establish actual protocol adherence, future UACR success/failure, chronology, turnaround, clinical feasibility, persistent/adjudicated CKD, measured GFR, complete events, mechanism, fairness, action, costs, harms, transportability or benefit. Those require the additional evidence and expert review above.

## Frozen change for Lead approval

Relative to [prior hypothesis], no population, time zero, capacity, score, outcome, model fit, comparator, margin, missingness method, bootstrap, placebo or evidence boundary changes. Relative to [prior hypothesis], the primary direct UACR-first set changes substantively from AG_V on V to AG on all O with the frozen fallback; attempts remain |O| and cystatin count remains n_p. AG:G is added to the simultaneous H, D and H×K18 families (26, 6 and 8 components). V becomes a secondary usable-result diagnostic and cannot stand in for the all-offered decision. This is the intended scientific repair, not a compiler default.
