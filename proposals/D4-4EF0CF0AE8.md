> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Observed-UACR deployment test of grip-augmented cystatin-C allocation

## Decision, evidence boundary, and Episode-9 judgment

The consequential decision is how to spend a fixed cystatin-C assay capacity in adults whose baseline creatinine-based eGFR is 60–89 mL/min/1.73 m². The selected lineage already asks whether raw grip improves a fixed-budget policy and whether it beats a transparent threshold-nearest rule. Its remaining validity gap is deployment semantics: the leader’s all-O UACR model imputes unavailable UACR for score construction, although a clinician cannot condition a decision on a urine result that is not observed.

I independently reviewed the full UKB catalog, the exact source schemas and physical headers, the two assessed-valid parents, and the inherited feasibility audit. No available dataset supports a more consequential fully computable alternative. UKB has no measured GFR, adjudicated or persistent CKD, validated outpatient history, prescription/action data, assay or downstream costs, complete individual follow-up, or external validation cohort. Repeat assessment and repeat creatinine/cystatin fields are too sparse for a population-wide longitudinal gate. The genomics export is phenotype/derived metadata, not a sequence or variant bundle. Diabetes, blood pressure, medication, and HbA1c fields can stress-test confounding by common risk information, but cannot identify whether allocation changes treatment or patient outcomes.

The strongest available claim remains feasibility, not clinical benefit: the inherited O has 134,118 participants, and a baseline UACR record judged usable under the prespecified assay rule is available for 130,257 (97.12%); the locked-test and locked-replication coverage is 97.18% and 97.14%. No locked cystatin label, H, D, K18, or policy yield is established by that audit.

The unresolved hypothesis is:

> In each locked partition, among the same participants with an observed usable baseline UACR record, adding the inherited single raw-grip scalar to the inherited UACR-conditioned policy (AG_V versus A_V) will yield at least 2 additional combined-equation eGFR<60 reclassifications per 1,000 cystatin assays, with yield ratio at least 1.10 and positive D contrast. The inherited grip-only policy (G_V) will be noninferior to A_V at −1 reclassification per 1,000. If the prespecified N18 event-sufficiency gate passes, AG_V will yield at least 1 additional baseline-H reclassification followed by a 10-year inpatient N18 event per 1,000 assays and G_V will be noninferior to A_V for that endpoint.

AG_V:A_V isolates whether grip adds allocation information after an actually observed usable UACR record. G_V:A_V separately tests whether grip-only allocation can substitute for UACR on the same observed-UACR candidate pool. This is a comparative allocation hypothesis, not a claim of measured-GFR validity, persistent albuminuria, CKD diagnosis, treatment benefit, mechanism, cost equivalence, or transportability.

## Frozen inheritance

Parent precedence is explicit:

- [prior hypothesis] supplies the UACR-conditioned A/AG decision, censoring and UACR robustness variants, routine-risk stress policies, and exact source audit.
- [prior hypothesis] supplies the availability-aware observed-UACR restriction, common candidate pool, frozen-score reuse, unchanged absolute assay capacity, and deployment-specific interpretation.

Retain [prior hypothesis] exactly for:

- O, eligibility, time zero, the 2021 race-free creatinine and combined equations, H/D/K18 definitions, N17/N18 date handling, death competition, and all source/date integrity rules;
- SHA256 v3 development/test/replication locks (60/20/20);
- development-only fitting, tuning, transformations, missing-label bounds, paired bootstrap and multiplicity;
- B/G/W/Q/F/T, the one-column raw-grip restriction, placebos, calibration, sex-stability, exact yield and falsification gates;
- exact 20% denominators, N18 sufficiency, adverse/inconclusive branches, and noncausal limits.

The child adds only an availability-restricted deployment arm. It does not change O, time zero, equations, any inherited all-O policy membership, any locked outcome label, any existing estimand, or assay capacity. The all-O analyses remain reported adjacent to the added arm; an all-O pass is never reported as an observed-UACR pass.

## Population and temporal boundaries

Construct one row per eid by horizontal one-to-one joins. O is exactly:

- age 40–69 at recruitment, sex coded 0/1, valid baseline assessment date 53-0.0;
- positive baseline creatinine 30700-0.0 and BMI 21001-0.0;
- at least one finite positive baseline left/right grip value 46-0.0 or 47-0.0;
- full-precision 2021 race-free eGFRcr in [60,90);
- no position-matched inpatient N17* or N18* diagnosis on or before baseline.

Any N17/N18 code with a missing or invalid paired date is excluded before O and reported. No cystatin, H, D, K18, death, future field, or outcome is used to define O. Time zero is 53-0.0. The assessment instance index is not treated as elapsed time.

Compute creatinine eGFRcr at full precision after converting 30700-0.0 from µmol/L to mg/dL by division by 88.4:

`142 × min(Scr/k,1)^alpha × max(Scr/k,1)^−1.200 × 0.9938^age × 1.012(if female)`

with female 31-0.0=0: k=0.7, alpha=−0.241; male: k=0.9, alpha=−0.302. Use the inherited formula fixtures and never rounded displayed eGFR.

L is O with finite positive baseline cystatin C 30720-0.0. H=1 when the inherited 2021 creatinine-cystatin combined eGFR is <60:

`135 × min(Scr/k,1)^alpha × max(Scr/k,1)^−0.544 × min(Scys/0.8,1)^−0.323 × max(Scys/0.8,1)^−0.778 × 0.9961^age × 0.963(if female)`

with k=0.7/0.9 and alpha=−0.219/−0.144. D=1 when the inherited 2012 eGFRcys / 2021 eGFRcr ≤0.70, using:

`133 × min(Scys/0.8,1)^−0.499 × max(Scys/0.8,1)^−1.328 × 0.996^age × 0.932(if female)`.

H is a one-time laboratory threshold crossing and D is marker discordance; neither is true GFR.

For K18, pair 41270-0.i only with 41280-0.i at the same i, i=0,…,258. Normalize codes only by trimming whitespace and uppercasing. K18=1 if the earliest valid paired inpatient N18* date lies in (53-0.0, 53-0.0+10 years]. Death is the earliest valid 40000-0.0 or 40000-1.0; it competes and precedes same-day K18. N17 does not censor N18. H18=H×K18. K17 and Kany are diagnostics only and cannot rescue an N18 conclusion.

## UACR and observed-pool semantics

Use baseline instance-0 fields from biological_samples:

- positive numeric 30500-0.0 is urine microalbumin in mg/L;
- blank 30500-0.0 with trimmed 30505-0.0 exactly `<6.7`, plus positive 30510-0.0 urine creatinine in µmol/L, is an observed left-censored low-result record;
- 30515-0.0 is the urine-creatinine result flag and is never parsed as the albumin flag.

For positive numeric albumin, compute `UACR = 1000 × albumin / urine_creatinine` mg/mmol. For an observed `<6.7` albumin result, the primary policy uses the inherited deterministic 3.35 mg/L midpoint convention. This is a coding of an observed assay censoring interval, not a missing-value fill and not a claim that 3.35 was measured. A numeric-plus-albumin-flag contradiction, missing/nonpositive urine creatinine, missing albumin without the exact flag, another flag, or a nonfinite ratio is unavailable and counted as an integrity failure.

Define V, the deployment candidate pool, before opening any cystatin label or health outcome, as O participants with either positive numeric albumin plus positive urine creatinine or the exact observed `<6.7` albumin flag plus positive urine creatinine. No participant enters V because an unavailable UACR was imputed. Report V_obs coverage and a numeric-albumin-only descriptive stratum; the primary V includes the observed censored low-result category because it is a usable clinical result, while all censoring uncertainty is exposed by frozen variants.

Freeze before opening locks six variants: albumin censoring value 0, 3.35, or 6.7 mg/L crossed with unavailable-UACR development 1st- or 99th-percentile transform imputation. The 3.35/development-median specification is primary. The extreme variants are LOD/missingness stress tests, cannot rescue a primary failure, and cannot change V membership. Since V contains no unavailable UACR, no missing-UACR imputation is applied to a V participant at deployment; the variants test only the inherited frozen score/censoring convention. UACR unavailability above 5% in either lock is inconclusive.

## Frozen policies, scores, and absolute assay capacity

Use the inherited lock hash:

`h = int(SHA256(utf8("ukb-grip-cys-v3|" + canonical_decimal_eid)).hexdigest(),16) % 100`.

Development is h<60, locked test 60≤h<80, and locked replication h≥80. The inherited tie hash is used exactly wherever scores tie.

A is the inherited development-fitted ridge-logistic H policy B plus exactly the primary transformed UACR scalar Z_A. Form Z_A in development O from log1p(UACR), development-O 1st/99th winsorization, development-O mean/SD standardization, and inherited development median imputation for unavailable values before applying the frozen transform. AG is bit-for-bit A plus exactly the inherited development-frozen standardized raw maximum-grip scalar Z_R. G is the inherited grip-only policy, bit-for-bit B plus only Z_R. No additional feature, missing indicator, interaction, future value, cystatin, H, K18, death, or locked statistic enters these primary scores.

C is the inherited non-rescuing routine-risk stress policy A plus known 0/1 diabetes 2443-0.0, mean valid positive automated systolic readings 4080-0.0/0.1, and the sex-specific antihypertensive indicator (code 2 in 6153-0.0…0.3 for female or 6177-0.0…0.2 for male). CG is C plus exactly Z_R. A further HbA1c 30750-0.0 stress variant is descriptive. Development medians/modes and missing indicators for these stress policies are frozen in development only; they cannot rescue the primary result.

All A, AG, G and stress-policy scores are fit/tuned and transformed only in development O under the inherited procedure, then frozen. The primary added arm reuses the frozen all-O scores without refitting, recalibration, re-imputation, or rank shrinkage in V. Thus AG_V, A_V, and G_V are not new fitted policies.

For each partition p, set the exact absolute inherited budget:
`n_p = floor(0.20 × |O_p|)`.
Select exactly n_p from V_p by ranking the already frozen all-O score for that policy and applying the inherited tie hash. The budget is 16,103 in development, 5,395 in locked test, and 5,325 in locked replication, because it remains 20% of O, not 20% of V. Preflight verifies |V_p|≥n_p; failure makes the added V arm inconclusive but does not alter the inherited all-O arm. A_V, AG_V and G_V rank the same V_p pool and therefore have common candidate-pool denominators and equal assay capacity.

The six UACR variants reuse the same O, locks, n_p and V membership. Their frozen score ranks are sensitivity outputs only; they cannot replace the primary score or change the population.

## Estimands, analysis, and uncertainty

For any selected S in V_p:

- `Y_H^V(S)=1000×sum(H_i)/n_p`;
- `Y_D^V(S)=1000×sum(D_i)/n_p`;
- `Y_H18^V(S)=1000×sum(H_i×K18_i)/n_p`.

Report the unchanged inherited all-O yields and contrasts first, then the V-arm yields. For AG_V:A_V and G_V:A_V report paired differences and ratios, exact feasible ratio extrema, overlap/Jaccard, selected counts, and the H/D/H18 yields of AG_V\A_V versus A_V\AG_V and G_V\A_V versus A_V\G_V. Report V coverage, integrity counts, V-versus-O characteristics, and policy selection by sex.

Use the inherited 2,000 participant-paired, no-refit bootstrap within each lock and max-|t| adjustment over the added V H, ratio, D and H18 family together with the inherited family. The paired resampling preserves the common V candidate pool and shared participants. For missing H, use participant-level joint lower/upper bounds with one common unknown H assignment; never subtract marginal missing-label bounds. Apply the inherited >1% missing-cystatin inconclusive rule, label counts, standard errors, interval endpoints, exact n, and death handling.

Before any lock is opened, freeze all transformations, score files, UACR variants, policy definitions, date parsing, event rules, and verifier checks. No locked outcome label is used for model fitting, tuning, V membership, imputation, or ranking.

## Gates and falsification

In each lock, the primary AG_V:A_V test requires:

- adverse joint-bound Δ_H≥2 per 1,000;
- feasible yield ratio≥1.10;
- simultaneous 95% intervals strictly above 0 for Δ_H and above 1 for the ratio;
- positive H yield in AG_V\A_V relative to A_V\AG_V.

G_V:A_V requires a one-sided simultaneous 95% lower bound above −1 per 1,000. G_V may be called superior only if its two-sided interval is above 0. AG_V:A_V must have positive Δ_D in each lock and a pooled partition-stratified paired 95% interval above 0. All inherited G/B/F/T, placebo, calibration, sex-stability, missingness, and lock gates remain mandatory.

For the grip-beyond-UACR claim, Δ_H(AG_V:A_V)>0 and Δ_D(AG_V:A_V)>0 must retain their sign in every one of the six frozen UACR variants in both locks. Variants need not meet the primary materiality or ratio thresholds; a sign reversal is inconclusive. C/CG/HbA1c results are reported as non-rescuing stress analyses.

N18 is supportive only if each pooled AG_V\A_V and A_V\AG_V swap set has at least 20 observed-label H×K18 events, and each pooled G_V\A_V and A_V\G_V set also has at least 20. If sufficient, require Δ_H18(AG_V:A_V)≥1 per 1,000 with a pooled two-sided 95% interval above 0, and a one-sided lower bound for Δ_H18(G_V:A_V) above −1 per 1,000. Positive N17, K17, or Kany cannot rescue N18.

Falsify the actionable incremental claim if either lock has nonpositive AG_V:A_V H contrast, failure of the 2/1,000 bound, failure of the 1.10 ratio, a crossed simultaneous interval, nonpositive swap-set yield, or failure of D. Falsify substitution if G_V:A_V is below −1 per 1,000 with its one-sided bound. No all-O result, routine-risk stress result, or UACR sensitivity can rescue a failed primary gate.

## Interpretation

Fully supportive requires all inherited gates, both-lock primary AG_V:A_V H/ratio/D gates, G_V:A_V biochemical noninferiority, UACR-variant sign robustness, and—if event-sufficient—the N18 gates. It supports a prospective comparison of availability-aware cystatin allocation strategies.

Supportive AG_V but adverse G_V means grip is a complement to observed UACR, not a substitute. Supportive G_V but null AG_V means grip-only allocation may be a lower-burden substitute candidate on this observed-UACR pool, but it says nothing about people without UACR. If A_V matches or beats AG_V with adequate precision, raw grip adds no decision-relevant information beyond observed UACR under this design. If the parent all-O AG:A passes but AG_V:A_V fails, the parent’s apparent grip increment is imputation-dependent and the observed-UACR deployment claim is adverse.

Adverse means a prespecified biochemical gate fails with adequate information, including a reproducible negative result; such a result favors the competing policy within this UKB frame and does not prove no benefit in another population. Inconclusive means V_p<n_p, >5% UACR unavailability in a lock, integrity/chronology/join failure, leakage, >1% missing cystatin, sparse N18 or swap events, zero feasible ratio denominator, partition disagreement, crossed intervals, calibration or sex instability, or sign reversal across a frozen UACR variant. Biochemical support with N18 insufficiency is biochemical-only, not chronic-kidney consequence support.

## Exact UKB bindings

Snapshot is `[source checksum]`. All used sources are ordinary read-only CSVs with no archive member; the horizontal join key is `eid`, one-to-one, with overlapping-field agreement required by the catalog.

- population / table `population`: `[internal dataset path]`; schema `datasets/ukb/table-38565c9e35e7cb6c.json`; required `eid`, `31-0.0`, `21022-0.0`.
- assessment / table `assessment`: `[internal dataset path]`; schema `datasets/ukb/table-901ef6c7ddce2d51.json`; required `eid`, `53-0.0`, `53-1.0` (sensitivity only), `46-0.0`, `47-0.0`, `21001-0.0`, `924-0.0`, `2178-0.0`, `2443-0.0`, `4079-0.0/0.1`, `4080-0.0/0.1`, `6153-0.0…0.3`, and `6177-0.0…0.2`.
- biological_samples / table `biological_samples`: `[internal dataset path]`; schema `datasets/ukb/table-c6b666d905f3b02f.json`; required `eid`, `30500-0.0`, `30505-0.0`, `30510-0.0`, `30515-0.0`, `30700-0.0`, `30720-0.0`, and stress `30750-0.0`; repeat `30700-1.0/30720-1.0` is non-rescuing sensitivity only.
- health_outcomes / table `health_outcomes`: `[internal dataset path]`; schema `datasets/ukb/table-3cfae45e0905b0e3.json`; required `eid`, `40000-0.0`, `40000-1.0`, `41270-0.0…41270-0.258`, and paired `41280-0.0…41280-0.258`.

The full UKB catalog also includes main, additional_exposures, genomics, and online_followup ordinary files; they were inspected for availability but are not required by this locked design. No archive member is used. Source file sizes and SHA-256 identities are fixed in `datasets/ukb/README.md` and `datasets/ukb/metadata.json`; the relevant source hashes are preserved there and must be checked by the compiler/verifier.

## Falsification fixtures and verifier boundary

Fixtures must catch: parsing 30515 as albumin; admitting an imputed/unavailable UACR into V; treating 6.7 as an observed numeric albumin; changing V across variants; using 20% of V rather than n_p=floor(0.20|O_p|); unequal A_V/AG_V/G_V pools or budgets; refitting or re-imputing in V; opening locked labels before freezing; using cystatin, H, D, K18, death, future assessments, or outcomes for V or scores; rounded-eGFR ordering; changed tie hashes; marginal rather than joint missing-H bounds; N17 censoring N18; same-day death ordering; and calling an all-O pass, C/CG stress pass, or biochemical support an observed-UACR, CKD, mechanism, cost, guideline, or benefit claim.

The verifier can check source identity and headers, one-to-one eid joins, O and time zero, indexed code/date pairing, UACR V membership, observed-censoring semantics, frozen-score reuse, lock separation, exact absolute n, leakage, H/D/K18 arithmetic, missing-label bounds, bootstrap intervals, event sufficiency, gates, and whether the final narrative is linked to computed outputs. It cannot establish that the urine result was available before a real clinical decision, that one censored baseline sample represents persistent albuminuria, that combined eGFR equals measured GFR, that N18 is adjudicated CKD, that grip measures muscle mass, that costs/harms are acceptable, that care changes, that equity is adequate, or that patient outcomes improve. Those claims require specimen workflow/timestamps, repeat urine testing, measured GFR, clinical adjudication, outpatient/action and economic data, equity review, external validation, and prospective implementation or randomized testing-strategy evidence.

## Substantive advance

This Episode-9 synthesis makes the leader’s clinically relevant comparison deployment-valid without changing its scientific target. It tests incremental grip value after a usable UACR and substitution by grip-only allocation on one common observed-UACR pool, reuses development-frozen all-O scores, and retains the exact inherited absolute assay budget. The result will distinguish a real observed-UACR decision signal from an artifact of imputing unavailable urine values while keeping negative and inconclusive findings scientifically interpretable.
