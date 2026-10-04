> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Final locked repair: HCC laboratory trajectories after first strict repeat TACE

## Scope and immutable inherited design

This child makes only the Lead-requested inferential repair to `[prior hypothesis]`. It does not rerun an outcome model, inspect outcome direction, or change any population, event, window, assay, pathway, or selector. Every inherited construction and evidence limit remains normative unless an inferential rule is explicitly replaced below.

The frozen complete-source, value-blinded audit remains:

- HCC snapshot `[source checksum]`, with no sampling.
- Frozen post-TACE2 pathway cohort: 319 systemic and 1,491 comparator patients.
- First strict repeat TACE on TACE2 calendar days 15–90: 159 systemic and 526 comparator events; event-day quartiles 43/55/69 and 44/55/69, respectively.
- Primary assay-specific complete triplets: albumin 40/118 and total bilirubin 41/119 (systemic/comparator).
- Strict common-timestamp joint triplets: 40/118. Assay-specific timing therefore adds no albumin triplets and only one per arm for bilirubin; it does not solve sparse interaction support.
- No laboratory value, sign, effect estimate, or outcome-model result was used to choose the population, event, window, or selector.

The question remains noncausal: in the selected repeat-event cohort with observed assays, is the pre-repeat assay trajectory associated with the post-repeat assay level beyond baseline, and, only exploratorily, does that slope differ by pathway arm? The study cannot establish treatment benefit, treatment response, mechanism, procedural success, or effects of verified drug administration.

## Frozen source bindings and selectors

Read-only sources and ordinary-file table bindings are unchanged:

- `HCC/data_Basic Information_2500296761891079109.csv`, `encounters`: `Patient Master Index`, `Encounter Number`, `Age`, `Sex`, `Encounter Time`, `Admission Time`, `Discharge Time`, `Encounter Department`; composite join (`Patient Master Index`,`Encounter Number`).
- `HCC/data_diagnoses_7504718184492840569.csv`, `diagnoses`: `Patient master index`, `Encounter number`, `Diagnosis name`, `Diagnosis type`; composite encounter join, with diagnosis time inherited from the encounter because no native diagnosis time exists.
- `HCC/data_surgery_8024330590283626027.csv`, `procedures`: `patient master index`, `visit number`, `procedure`, `start time`, `end time`, `procedure source`; `start time` is the procedure clock.
- `HCC/data_medication_5693407050835159466.csv`, `medications`: `patient master index`, `encounter number`, `medication`, `start time`; medication records are orders/records, not verified administrations.
- `HCC/data_lab_test_609065997844652188.csv`, `labs`: `patient master index`, `encounter number`, `test`, `quantitative result`, `qualitative result`, `specimen type`, `test time`; exact assay labels are `albumin` and `total bilirubin`. Numeric parsing remains a signed decimal/scientific number with optional leading `<`, `>`, `≤`, or `≥`, retaining the numeric component and inequality flag. There is no unit field, so assays are never pooled on their raw scales and no unit-dependent clinical threshold is inferred.

Strict TACE matching, earliest adjacent 14–180-day pair selection, adult/HCC/2018–2024/day-14 observation criteria, prior-systemic exclusions, inherited exact systemic-medication ontology and ambiguity exclusions, and first strict day-15–90 repeat-event selection are unchanged from the parent. The inherited pathway includes lenvatinib, sorafenib, regorafenib, donafenib, apatinib, sintilimab, tislelizumab, camrelizumab, atezolizumab, pembrolizumab, nivolumab, bevacizumab and their frozen Chinese-name strings, with the inherited bevacizumab-only and generic-procedure ambiguity exclusions. No later pair or event may be substituted.

For assay `a`, selectors remain exactly:

- `B_a`: latest valid numeric value on TACE2 calendar days −30 through −1.
- `P_a`: latest valid numeric value in the selected repeat-event encounter in `[event time−72 h,event time)`.
- `Y_a`: valid numeric value in that encounter in `(event time,event time+72 h]` nearest nominal event+24 h; a distance tie selects the earlier timestamp.
- `D_a=P_a−B_a`.

The seven locked alternative selectors remain: latest-pre 24 h; latest-pre 48 h; latest-pre 168 h; first-pre 72 h with nearest +24 h post; first-pre 72 h with nearest +48 h post; first-pre 72 h with first eligible post; and latest-pre 72 h with post on calendar days +1–3. Their audited triplets are respectively albumin 27/86, 33/110, 40/127, 40/118, 40/118, 40/118, 42/123 and bilirubin 27/87, 34/111, 41/128, 41/119, 41/119, 41/119, 42/124. None may replace the primary selector based on results.

## Primary pooled trajectory model and separately gated exploratory interaction

For each assay separately, the primary complete-triplet model is

```text
Y_a = beta0 + betaB B_a + betaD D_a + betaA A + gamma'Z + epsilon,
```

where `A=1` is systemic and `A=0` comparator and `Z` is the unchanged pre-TACE2 demographic, encounter-history, disease/observation-proxy, calendar-era, and selection covariate set inherited from the parent. Use HC3 robust standard errors. `betaD` is one pooled, arm-adjusted trajectory slope. It is the primary estimand. It is not a comparator/reference-arm slope, and no reference-arm trajectory is the primary claim.

Only as a separately gated exploratory extension, add

```text
betaDA (D_a × A).
```

In that extension, `betaDA` is the systemic-minus-comparator trajectory-slope contrast. The comparator slope is `betaD` and the systemic slope is `betaD+betaDA`, but those are exploratory arm-specific quantities. The interaction may always be emitted as a descriptive estimate with its interval; it may be called supported pathway modification only if every gate below passes. A failed gate cannot be repaired by changing a window, assay, covariate set, weight truncation, or event definition.

The unchanged five-fold cross-fitted propensity/selection and assay-observation models use only eligible pre-outcome variables and the folds frozen before outcome inspection. The inherited overlap/selection weights are calculated without outcome-dependent tuning. Diagnostic rules below apply to the final product weight. No observation is deleted, clipped, or trimmed in the primary weighted fit; trimming/winsorization, if shown, is sensitivity analysis only.

## Locked numeric gates

All inequalities include their boundary. Compute weights and diagnostics separately by assay. Let normalized final weights have mean 1 within each assay analysis; let `ESS(S)=(sum_{i in S} w_i)^2/sum_{i in S}w_i^2`.

### 1. ESS

A weighted primary trajectory result is inferentially reportable only if:

- systemic-arm ESS is at least **30.0**, and
- combined-arm ESS is at least **120.0**.

The exploratory interaction must satisfy the same two thresholds in each assay. These correspond to retaining at least 75% of the raw systemic albumin support and approximately 75% of the raw combined support; they are feasibility gates, not declarations that 30 systemic equivalents guarantee adequate power. If either threshold fails, weighted coefficients remain descriptive and the result is inconclusive for robust association or pathway modification.

### 2. Propensity support and balance

Apply these rules to every cross-fitted arm-overlap, repeat-event-selection, and assay-stage observation probability used in the final product weight:

- at least **95%** of relevant observations must have a predicted probability in `[0.05,0.95]`;
- **no** predicted probability may be below `0.01` or above `0.99`;
- after final weighting, every prespecified covariate must have absolute standardized mean difference `≤0.10` for systemic versus comparator balance;
- for each selection/observation model, every prespecified covariate must also have absolute standardized mean difference `≤0.10` between the weighted observed subset and its specified target risk set; and
- every continuous-covariate weighted variance ratio must lie in `[0.50,2.00]` whenever both comparison variances are nonzero. A zero variance is acceptable only when both groups have the same zero variance; otherwise the balance gate fails.

Standardized mean differences and variance ratios are computed from covariates, never outcomes. Any failure blocks a robust weighted or interaction claim but does not erase the unweighted descriptive result.

### 3. Weight instability

Using mean-one normalized final product weights, all must hold:

- coefficient of variation `SD(w)/mean(w) ≤1.50`;
- maximum weight `≤10.0`;
- the largest **5%** of weights (using `ceil(0.05n)` observations) carry `≤25%` of total weight; and
- no single observation carries `>5%` of total weight.

No threshold is optimized against an outcome. Failure makes the weighted estimate unstable/inconclusive; an outcome-blind 1st/99th-percentile winsorized refit may be reported only as sensitivity and cannot convert a failed primary gate into a passed one.

### 4. Influence

Apply the following separately to `betaD` in the primary model and `betaDA` in the exploratory model, using the corresponding weighted fit and `n` complete triplets:

- no more than **2** observations may have absolute DFBETA greater than `2/sqrt(n)` for the target coefficient;
- no more than **2** observations may have Cook's distance greater than `4/n`;
- across all one-observation-deleted refits, the target coefficient must retain its sign and its largest absolute change from the full estimate must be `≤0.50` times the full-fit HC3 standard error; and
- delete the union of DFBETA-flagged and Cook-flagged observations (maximum four distinct observations). The refitted coefficient must retain its sign, and its absolute change must be `≤0.50` full-fit HC3 standard errors.

If the full estimate is exactly zero, sign stability fails by definition and no supportive claim is allowed. Failure of any influence rule makes that coefficient descriptive/inconclusive.

### 5. Direction and magnitude stability

For a target coefficient `theta` (`betaD` or, only after other interaction gates pass, `betaDA`), define the unit-invariant standardized effect

```text
theta_std = theta × SD(D_a) / SD(Y_a),
```

using unweighted SDs in that selector's complete-triplet sample. Zero SD makes that selector non-estimable.

The primary weighted and unweighted estimates must have the same nonzero sign, and their standardized magnitudes must have a ratio in `[0.50,2.00]` (smaller absolute magnitude divided by larger absolute magnitude equivalently at least 0.50).

Among the seven locked alternative selectors, at least **6** must be estimable. If `m` are estimable, at least `ceil(0.75m)` must both (i) have the same sign as the primary weighted estimate and (ii) have absolute standardized magnitude between `0.50` and `2.00` times the primary absolute standardized magnitude. Thus six estimable variants require five stable variants; seven require six. The rule is applied without choosing variants by their results.

The inherited pre-event negative-control interval is evaluated with the same model. A supportive event-linked interpretation additionally requires the negative-control 95% CI to include zero and its absolute standardized effect to be **<50%** of the primary absolute standardized effect. Otherwise timing specificity is falsified and the result is adverse or inconclusive, not robust event-linked evidence.

### 6. Deterministic albumin/bilirubin corroboration for exploratory arm modification

There is no raw-scale cross-assay pooling. A pathway-modification statement is permitted only when **both** albumin and total bilirubin separately pass every ESS, propensity, balance, weight, influence, and selector-stability gate above and all of the following hold:

1. albumin and bilirubin `betaDA` estimates have the same nonzero sign;
2. both two-sided HC3 tests remain significant at family-wise `alpha=0.05` after Holm correction across the two assays;
3. both assay-specific 95% confidence intervals exclude zero; and
4. the ratio of the smaller to the larger absolute standardized `betaDA` is at least **0.50**.

If either assay fails, signs disagree, Holm significance fails, or the standardized magnitude ratio is below 0.50, there is no corroborated pathway modification. Report both estimates and diagnose the failure as adverse when well-powered and contradictory, or inconclusive when precision/support gates fail. A positive result in one assay alone cannot be promoted as pathway modification.

## Locked conclusion rules

For each assay, support for the primary vulnerability-marker association requires: nonzero `betaD` with a two-sided 95% HC3 interval excluding zero; all weighted ESS/support/balance/weight and influence gates passing; weighted/unweighted and selector direction/magnitude stability passing; and the negative-control rule passing. This supports only a reproducible baseline-adjusted association in the selected observed-repeat cohort.

A null 95% interval narrow enough to exclude the prespecified clinically relevant standardized magnitude, with all gates passing, is evidence against that magnitude in this cohort. Because no unit-based clinical threshold is available, the compiler must report the standardized interval and must not invent a clinical cutoff. A wide interval or any failed support/ESS gate is inconclusive, not evidence of no biology. Sign reversal, material attenuation outside the locked magnitude bounds, negative-control failure, or dominance by a few observations is adverse to robustness.

The exploratory interaction is never substituted for the pooled primary model. Only the deterministic two-assay rule permits a corroborated pathway-modification statement. Regardless of results, causal, benefit, response, mechanism, administration, survival, or technical-success claims remain prohibited.

## Provenance and remaining uncertainty

The unchanged value-blinded complete-source audit code is `[internal dataset path]`. Its aggregate output is `[internal dataset path]`, [source checksum], from managed job `[research job]`. It contains aggregate counts only.

No outcome model has been run. It remains unknown whether either pooled trajectory association exists, whether its magnitude is clinically meaningful, or whether arm modification is stable. Missing laboratory units, unverified medication administration/adherence/dose, post-TACE2 event and observation selection, absent tumor/cirrhosis/procedure adjudication, and unavailable out-of-hospital events prevent stronger interpretation. Expert record/imaging review and a prospective or target-trial design with verified exposure, units, repeated untreated comparators, clinically meaningful outcomes, and adjudication would be required for causal or clinical-benefit claims.
