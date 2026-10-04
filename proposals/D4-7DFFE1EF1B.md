> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Threshold-nearest challenge to raw-grip cystatin C allocation: Episode-6 actionability repair

## Status of this child

This child incorporates [prior hypothesis] unchanged except for the additions and replacements stated here. In particular, it preserves the audited pre-assay population O; baseline and ten-year chronology; v3 60/20/20 participant locks; development-only preprocessing; B, G, W, Q and frozen F model definitions; exact 20% assay counts; frailty-conditioned permutations; joint missing-label bounds; H, D, K and competing-death definitions; paired inference; event-sufficiency rules; sex-instability flag; source bindings; and verifier limits. The scientific repair is to promote the previously descriptive lowest-eGFRcr reference into a mandatory operational comparator T and to make passing T necessary for a clinically actionable positive result. T does not replace B or F: B and F remain the capacity-matched attribution controls.

## Unresolved question, prior evidence, and clinical importance

The strongest evidence available before this experiment is that creatinine and cystatin C have different non-GFR determinants, combined creatinine-cystatin eGFR can be useful when precision is required, and participant characteristics can internally predict creatinine-cystatin discordance. Chen et al. (PMCID PMC10986041; DOI 10.1016/j.xkme.2024.100796), whose full-text XML was inspected, developed and internally validated UKB discordance models but did not test a fixed assay budget or compare a grip policy with simply testing people nearest the eGFRcr 60 boundary. The inspected ERBP commentary on KDIGO 2024 (PMCID PMC11792658; DOI 10.1093/ndt/gfae209) describes creatinine eGFR as the first approach and combined creatinine-cystatin eGFR when more precision is needed, while emphasizing access, cost and turnaround barriers and that a single value cannot diagnose CKD. It does not establish whom a capacity-limited service should assay.

The parent can beat fitted B and equal-one-scalar F yet still be operationally dominated by a transparent policy requiring no grip measurement or fitted model: assay those with the lowest baseline eGFRcr within the eligible 60–89 range. That is a consequential comparator-validity gap. If G cannot beat this threshold-nearest policy for biochemical reclassification, a service has no evidence from this study that collecting and deploying grip improves use of the same cystatin budget. If it does beat T reproducibly while retaining kidney-event yield, the result supports a prospective implementation comparison of a grip-augmented policy against a credible simple alternative.

The strongest supported claim remains biological and operational plausibility. The unresolved claim tested here is:

> In the inherited pre-assay UKB population and separately in both locked partitions, a 20% policy G whose model is the shared clinical baseline B plus exactly one globally standardized raw maximum-grip scalar will identify at least 2 more combined-equation low-filtration reclassifications per 1,000 assays, with a yield ratio at least 1.10, than an exact-budget threshold-nearest policy T that assays the 20% with lowest baseline eGFRcr. G will also retain clinically noninferior subsequent kidney-event-enriched reclassification yield relative to T. These gates are additional to, and cannot substitute for, all inherited G:B, G:F, placebo, discordance, calibration, missingness, sex-stability and event gates.

This hypothesis is falsifiable. It tests incremental allocation value beyond proximity to the decision threshold. It does not test that grip measures muscle mass, that grip or muscle causes marker discordance, that H is measured GFR or persistent CKD, that T is current guideline care, that either policy is cost-effective, or that testing changes treatment or outcomes.

## Frozen population, time zero, labels, and exact data required

Construct one row per `eid` by one-to-one horizontal joins. O is unchanged: age 40–69 at recruitment; sex code 0 or 1; valid baseline assessment date; positive baseline creatinine and BMI; at least one finite positive baseline left/right grip; 2021 race-free eGFRcr in [60,90); and no position-matched inpatient N17* or N18* diagnosis dated on or before baseline. A relevant prior code with missing/invalid paired date remains unresolved and excluded. O does not require cystatin C, walking pace, overall health, or any future field.

Time zero is assessment date `53-0.0`. Baseline creatinine is `30700-0.0` mg/L divided by 88.4 to mg/dL. With female defined by sex `31-0.0=0`, compute 2021 eGFRcr at full floating-point precision as

`142 × min(Scr/k,1)^alpha × max(Scr/k,1)^-1.200 × 0.9938^age × 1.012(if female)`,

where k=0.7 and alpha=-0.241 for female, k=0.9 and alpha=-0.302 for male. Formula and unit fixtures at both sex and Scr/k boundaries remain mandatory. No rounded displayed eGFR may be used for O or T ranking.

L is O with valid positive baseline cystatin C `30720-0.0`. H=1 when the inherited 2021 race-free combined equation gives eGFRcr-cys <60:

`135 × min(Scr/k,1)^alpha × max(Scr/k,1)^-0.544 × min(Scys/0.8,1)^-0.323 × max(Scys/0.8,1)^-0.778 × 0.9961^age × 0.963(if female)`,

with k=0.7/0.9 and alpha=-0.219/-0.144 for female/male. D=1 when inherited 2012 eGFRcys / 2021 eGFRcr <=0.70; absolute discordance below -15 remains sensitivity only.

K is the first exactly position-matched inpatient `41270-0.i` N17*/N18* code with valid paired `41280-0.i` date in (time zero, time zero+10 years]. Prior exclusion uses those same index pairs on or before time zero. Death is the earliest valid `40000-0.0` or `40000-1.0`; same-day death precedes K. Repeat-measure sensitivity still uses actual `53-1.0`, `30700-1.0`, and `30720-1.0` 90 days to 6 years after baseline and cannot rescue allocation failure.

## Inherited policies and new operational comparator

B remains ridge logistic H prediction using the identical intercept and restricted-cubic-spline basis for age, sex, BMI and eGFRcr. G remains B plus exactly one column: development-O globally 0.5th/99.5th percentile winsorized (NumPy `method="linear"`, R type 7), mean-centered and population-SD standardized raw maximum of positive finite `46-0.0` and `47-0.0`. There is no primary residualization, sex-specific transformation, interaction, spline, handedness term or missing indicator. W and Q remain B plus exactly one standardized walking-pace or overall-health scalar, and F remains the development-frozen better of W/Q by five-fold out-of-fold exact-20% H yield, tie to W. All inherited model fitting, common folds, penalty grid, one-standard-error rule, lock discipline and placebo policies remain unchanged.

Define T without fitting or development selection. Within each locked partition, rank every member of O by ascending full-precision baseline 2021 eGFRcr and select exactly

`n = floor(0.20 × |O_partition|)`.

Break exact eGFRcr ties by ascending `SHA256(utf8("ukb-grip-cys-tie-v3|" + canonical_decimal_eid))`, exactly as inherited for other policies. T uses only age `21022-0.0`, sex `31-0.0`, baseline creatinine `30700-0.0`, and the frozen equation/unit conversion already required for O. It uses no cystatin value, H, D, K, death, post-baseline value, model coefficient, development outcome, or rounded eGFR. Freeze the equation implementation, numerical dtype/library versions, full-precision ranking values and tie rule before any locked cystatin or outcome is opened. Record T’s selected eids, cutoff eGFRcr, number tied at the cutoff, and deterministic tie resolution.

T is capacity-matched in assays, not in model dimension. That asymmetry is intentional: T represents the cheaper operational decision rule G must outperform, while B/F answer whether grip adds participant-specific information under matched prediction designs.

## Added estimands, uncertainty, and decision gates

For any policy S retain

`Y_H(S)=1000 sum(S×H)/n`, `Y_D(S)=1000 sum(S×D)/n`, `Y_HK(S)=1000 sum(S×H×K)/n`, and `Y_DK(S)=1000 sum(S×D×K)/n`.

Add, separately in each locked partition:

- `Delta_H(G:T)=Y_H(G)-Y_H(T)`;
- `R_H(G:T)=Y_H(G)/Y_H(T)`;
- exact G-only gains minus T-only losses, overlap count and Jaccard index.

A T actionability pass requires, under the adverse joint missing-label bound in each locked partition, `Delta_H(G:T) >=2` per 1,000 assays, `R_H(G:T) >=1.10`, the simultaneous two-sided 95% paired interval for the difference above 0, and the simultaneous ratio interval above 1. A feasible zero T denominator makes the ratio undefined and the result inconclusive, never supportive. Positive aggregate yield with nonpositive H yield in G\T versus T\G is adverse.

Extend the inherited max-|t| simultaneous bootstrap family to the three locked-partition H differences G:B, G:F and G:T and the two prespecified ratios G:B and G:T. Use 2,000 paired participant resamples within partition; models and T are not refit. Retain the inherited percentile fallback if studentization fails and report its trigger. This stricter family replaces the parent’s two-comparator H family; no unadjusted T interval can trigger support.

For biochemical attribution, retain the inherited placebo gate and pooled partition-stratified `Delta_D(G:F)>0` interval. Add a descriptive-but-required direction check that `Delta_D(G:T)>0` in both partitions and its pooled partition-stratified paired 95% interval is above 0. Failure is adverse to the claim that grip finds marker discordance beyond mere threshold proximity; D remains a marker phenotype, not mechanism.

For decision relevance, if event sufficiency passes, require the inherited `Delta_HK(G:B)>=1` per 1,000 with pooled interval above 0 and inherited G:F noninferiority. Add G:T noninferiority: the one-sided 95% lower bound for pooled `Delta_HK(G:T)` must exceed -1 per 1,000 assays. Claim event superiority to T only if the two-sided pooled interval exceeds 0. Event enrichment is not benefit caused by testing.

Extend event sufficiency to the union G∪B∪F∪T: at least 100 H×K events across both locked partitions, at least 20 separately in each pooled comparator-specific swap set G\B, B\G, G\F, F\G, G\T and T\G, and at least 30 in a partition for any positive partition-specific event statement. If any relevant T condition fails, T event relevance is inconclusive and “fully supportive” is unavailable; biochemical conclusions may still be classified separately.

## Missing labels, diagnostics, and falsification

Every policy, including T, ranks all O and uses n—not observed-label count—as denominator. Extend all inherited sharp participant-level joint bounds for H, D, H×K and D×K to G:T. A selected missing cystatin label contributes 0/1 to H or D lower/upper bounds and can contribute 1 to H×K or D×K upper bounds only if K=1. Shared participants use one common unknown assignment; subtracting marginal bounds is invalid. More than 1% missing valid cystatin in O still makes every allocation conclusion inconclusive.

Report for T and G\T/T\G the same age, sex, BMI, eGFRcr, raw grip, Z_R, pace, health, label availability, H/D/H×K/D×K yields, sex-specific selection/yields, and ten-year death-without-prior-K diagnostics required for B/F. Retain calibration, decision curves, hand-definition, budget, lag, sex, frailty-stratum and repeat sensitivities; none can rescue a failed T primary gate. A result confined to one partition or sex, inside placebo distributions, driven by missing-label bounds, or reversed across hand definitions remains unstable/adverse as inherited.

New mandatory computational checks are:

1. T selects exactly n in each locked partition from all O, with no cystatin-completeness filtering.
2. T’s ordering is identical to ascending unrounded frozen eGFRcr plus the exact v3 tie hash; ranking rounded eGFR or creatinine directly must fail.
3. T has no fitted parameters and no access to development H or locked H/D/K.
4. The same eGFRcr values used for O inclusion and B are used bit-for-bit for T.
5. T is included in joint bounds, paired resampling, swap decomposition, event sufficiency and result classification.
6. Fixtures include G passing B/F but failing T (must not be fully or biochemically supportive), G beating T on H but losing the event noninferiority margin (adverse if sufficiently powered), a sparse T swap set (event-inconclusive), and a fully supportive result passing all inherited and T gates.
7. Correct computations followed by claims that T is guideline care, H is CKD, grip is muscle mass, or testing prevents events must be rejected.

## Result meanings

- **Fully supportive:** every inherited G:B, G:F, placebo, D, calibration, missing-bound, sex-stability and event gate passes; both locked partitions also pass T’s difference and ratio H gates under adverse bounds; pooled D superiority to T passes with concordant signs; event sufficiency passes; G beats B and is noninferior to both F and T for H×K. This supports a prospective comparison of selective-testing policies, not adoption.
- **Biochemical allocation supportive, clinical consequence unresolved:** all inherited biochemical gates and all T H/D gates pass, but any H×K sufficiency rule fails or event intervals cross their margins. The defensible claim is limited to replicated biochemical allocation efficiency over B, F and threshold-nearest T.
- **Operationally adverse:** G passes B and/or F but fails either T H materiality/ratio/interval gate. The transparent T policy is then preferred on available evidence; the study does not justify grip-based allocation. Also adverse are inherited failure conditions, nonpositive G\T-versus-T\G yield, pooled D failure versus T, or sufficiently powered H×K inferiority to T.
- **Inconclusive:** T intervals cross thresholds, partitions disagree, T’s denominator can be zero, >1% of O lacks cystatin, adverse joint bounds fail, T event swap sets are sparse, chronology or code/date pairing is unresolved, pre-unlock rules are violated, or inherited instability conditions occur.

Negative findings are clinically useful: they can show that proximity to eGFRcr 60 captures the available reclassification yield without collecting grip.

## Exact source bindings and availability limits

All inputs remain read-only ordinary CSVs in snapshot `[source checksum]`; archive member is null; join key is `eid`; joins are one-to-one horizontal.

- **population** — `[internal dataset path]`; schema `datasets/ukb/table-38565c9e35e7cb6c.json`; `eid`, sex `31-0.0`, age `21022-0.0`.
- **assessment** — `[internal dataset path]`; schema `datasets/ukb/table-901ef6c7ddce2d51.json`; `eid`, dates `53-0.0/53-1.0`, grip `46-0.0/47-0.0` and repeats `46-1.0/47-1.0`, BMI `21001-0.0`, pace `924-0.0`, health `2178-0.0`.
- **biological_samples** — `[internal dataset path]`; schema `datasets/ukb/table-c6b666d905f3b02f.json`; `eid`, creatinine `30700-0.0`, cystatin C `30720-0.0`, repeats `30700-1.0/30720-1.0`.
- **health_outcomes** — `[internal dataset path]`; schema `datasets/ukb/table-3cfae45e0905b0e3.json`; `eid`, every exact `41270-0.0…41270-0.258` code paired to `41280-0.0…41280-0.258` date at the same index, death `40000-0.0/40000-1.0`.

The complete catalog and hashes are in `datasets/ukb/README.md` and `metadata.json`. This episode physically inspected headers only and sampled zero clinical rows; the parent’s recorded 2,000-row coding sanity audit remains inherited, not repeated.

Unavailable evidence remains explicit: measured GFR; serial confirmation sufficient to diagnose CKD; validated outpatient kidney history; urine albumin data incorporated into this decision; prescriptions, doses, clinical actions and treatment eligibility; assay and downstream costs; harms/anxiety from reclassification; chart adjudication; complete emigration/hospital follow-up; direct body composition for this design; and an external transport cohort. Thus the strongest computable claim is comparative allocation/enrichment in this UKB snapshot. Cost-effectiveness, clinical adoption, fairness, mechanism, diagnostic accuracy against measured GFR, and patient benefit require clinical/equity review, external validation, action/cost data, adjudication, and ultimately a prospective implementation or randomized testing-strategy study.

## Verifier boundary and substantive advance

An automatic verifier can check source hashes/headers, joins, O, chronology, equations, locks, frozen models, one-column G, exact budgets, T ordering/ties, leakage, bounds, paired intervals, swaps, event sufficiency and whether the reported classification follows computed outputs. It cannot establish clinical truth, guideline status, measured GFR, CKD, fairness, mechanism, actionability after a result, cost-effectiveness or benefit.

The substantive advance is narrow but consequential: the parent established clean one-scalar attribution against B/F; this child asks whether that gain survives the simplest clinically interpretable allocation rule already computable from the creatinine eGFR that defines eligibility. A grip policy that fails T is now explicitly rejected even if statistically impressive against fitted controls. A policy that passes T earns only the stronger claim that it merits prospective comparison under the same assay budget.
