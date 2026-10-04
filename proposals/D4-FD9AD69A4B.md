# Certified baseline-only decision experiment for UKB renal-marker discordance

## Lineage, unresolved question, and substantive advance

This is a targeted successor combining the decision-focused design of assessed-valid `[prior hypothesis]` with the two-lane field/equation certification of assessed-valid `[prior hypothesis]` and the exact current-workspace schema, certificate, equation, and model contracts repaired in `[prior hypothesis]`. It retains the same population, timing boundary, outcome family, and evidence limits. The prior executed elapsed-time experiment found a small, localized held-out loss signal but did not establish useful fixed-capacity concentration; that result is prior evidence, not a result of this proposal. This proposal is substantively distinct because every deployable predictor is available at baseline and the primary test is decision value, not another elapsed-time-conditioned loss test.

The unresolved, falsifiable question is:

> Among UKB participants with a certified baseline creatinine/cystatin-C panel, baseline equation-derived creatinine eGFR at least 60, and a complete exported instance-1 assessment occurring 2–8 years after baseline, does adding continuous baseline cystatin-C/creatinine eGFR discordance to a baseline creatinine-only score improve out-of-fold prioritization of the low creatinine-equation eGFR status observed at that repeat, at a prespecified 2% action threshold and a fixed 10% monitoring capacity?

The action represented is prioritization of a repeat kidney-marker assessment. The target is **not** a fixed-horizon risk, onset, cumulative incidence, persistent CKD, measured GFR, kidney failure, treatment benefit, cost-effectiveness, or causal utility. A supportive result would justify only external prospective validation of a baseline-input prioritization rule with observed decisions and clinically adjudicated outcomes. An adverse result would be a stop signal for adding this discordance to this particular schedule-marginal prioritization rule. A certification or technical failure is not adverse biology.

The clinically relevant advance is to test whether a previously observed probabilistic signal changes a concrete, baseline-computable action under two explicit operating points. The 2% threshold is an auditable hypothetical exchange rate, and 10% capacity is an auditable fixed-slot policy; neither is asserted to be a validated clinical utility or patient-specific treatment threshold.

## Evidence already supported, and limits on the new claim

Prior same-snapshot work supports only that baseline cystatin-C information can be associated with or modestly change prediction of the observed repeat creatinine-eGFR state in a selected complete repeat-attender sample. An executed elapsed-conditioned analysis did not establish the inherited 10% concentration target. Those facts motivate, but do not answer, the new baseline-only decision question. The present experiment must not report a loss improvement as a decision result, and it must not describe the observed repeat status as CKD or a renal event.

The exported files do not by themselves certify the semantic label, units, specimen or matrix, assay/platform comparability, field-specific missing tokens, exact date meaning, or whether instance 1 is a person's first clinical repeat. Field and cross-instance certification is therefore a prerequisite for a scientific classification. A field certificate is not created by inspecting value magnitudes or by assuming that familiar UKB field numbers have their expected meanings.

## Frozen data, exact paths, tables, joins, and provenance

Use only UKB snapshot `[source checksum]` and catalog `[internal dataset path]` with catalog [source checksum].

All three inputs are ordinary CSV files; there are no archive members. Open them read-only:

| table | exact source and SHA-256 | exact current schema JSON, schema-file SHA-256, internal `schema_sha256` | required columns |
|---|---|---|---|
| `population` | `[internal dataset path]`; `[source checksum]` | `[internal dataset path]`; file `[source checksum]`; internal `[source checksum]` | `eid`, `31-0.0` |
| `assessment` | `[internal dataset path]`; `[source checksum]` | `[internal dataset path]`; file `[source checksum]`; internal `[source checksum]` | `eid`, `53-0.0`, `53-1.0`, `21003-0.0`, `21003-1.0` |
| `biological_samples` | `[internal dataset path]`; `[source checksum]` | `[internal dataset path]`; file `[source checksum]`; internal `[source checksum]` | `eid`, `30700-0.0`, `30700-1.0`, `30720-0.0`, `30720-1.0` |

The executor must verify each literal path, source hash, schema file hash, table ID, internal schema hash, and snapshot/catalog identifiers before reading payload values. It must read headers and record, privately, ordered required columns, duplicate or absent columns, source row count, `eid` uniqueness, finite numeric identity checks, and overlap checks. Join the three projections horizontally on `eid`, one-to-one, with no row multiplication; every overlapping column must agree exactly. Do not open the other five UKB tables. The source metadata specify `eid` as the identity key and one-to-one horizontal relationships; they do not supply renal field semantics.

The expected inherited diagnostics are: 502,370 unique joined rows; 468,887 rows in baseline-valid `B`; 16,546 qualifying complete repeat rows; 16,372 selected `S_A` rows; and 309 primary low-status labels. The expected selected binary cells `(Y=0/1 by baseline discordance D=0/1)` are `(15,769,255,294,54)` in the inherited construction, with observed elapsed range 2.1081451061–6.1136208077 years and minimum baseline eGFRcr 60.0659423121. These are diagnostic anchors, not forced constants. If an anchor differs, preserve actual counts and stop the scientific classification pending reconciliation; never delete rows to force an anchor.

## Evidence certificate and fail-closed state machine

The compiler must look for an immutable, separately supplied `field_certificate.json` and `equation_certificate.json`; neither is assumed to exist merely because this proposal names the contract. Certificate bytes are canonical UTF-8 JSON with recursively sorted object keys, preserved array order, no insignificant whitespace, and no self-reported digest field included in the digest input. Recompute SHA-256 over canonical bytes and compare with the supplied sidecar/invocation digest. A certificate is evidence, not an operator prose declaration.

The field certificate must have exactly these required field-instance identifiers and no others in `required_fields`:

```text
31-0.0, 21003-0.0, 21003-1.0, 53-0.0, 53-1.0,
30700-0.0, 30700-1.0, 30720-0.0, 30720-1.0
```

For each identifier, its single evidence record must bind the exact table ID, source ID and source hash, schema path and both schema hashes, field/instance/array identity, data type, semantic label, valid domain, exhaustive exact raw missing-token list, unit, specimen/matrix, assay/platform or measurement method, and applicable sex/age/date/analyte concepts. Each evidence item must retain evidence class, directness, source URL or local artifact, version, retrieval date, artifact hash, and claim text. An `ASSUMED`, `MISSING`, or `CONFLICT` item cannot authorize scientific execution. No global negative-code interpretation is allowed. Any raw token not in the certificate's exact missing set is nonmissing; if it cannot parse as the declared type, the run fails rather than silently treating it as missing.

The certificate must separately establish all of the following: (1) instance 1 is an exported repeat record but not evidence of the first chronological clinical test; (2) baseline and repeat date values have compatible exact semantics; (3) creatinine values at instances 0 and 1 have compatible analyte, matrix, unit, and assay/method semantics or a certificate-authorized conversion; and (4) cystatin-C values at instances 0 and 1 have the same. A conflict is a stop, not an invitation to choose the convenient interpretation. External field evidence may establish these facts, but the verifier checks its presence, hashes, and consistency rather than clinically adjudicating its truth.

The equation certificate must bind the exact formula text, constants, input units, sex coding, source artifact and hash, implementation hash, and float64 numerical test vectors. It must not be used as evidence that UKB assays have the claimed units or analyte identity.

Use this monotone state machine:

```text
SOURCE_INTEGRITY_FAIL
  -> STRUCTURAL_READY
  -> FIELD_CERTIFICATE_MISSING | FIELD_CERTIFICATE_INVALID
     | FIELD_CERTIFICATE_INCOMPLETE | FIELD_CERTIFICATE_CONFLICT
  -> NEUTRAL_QA_PASS | NEUTRAL_QA_FAIL
  -> CERTIFIED_READY
  -> CERTIFIED_ANALYSIS_COMPLETE | CERTIFIED_ANALYSIS_FAIL
```

Before `CERTIFIED_READY`, output only source/schema hashes, exact headers, aggregate row/key/join integrity, synthetic parser/equation/basis/fold/quota/arithmetic tests, and certificate status. Do not output eids, participant-level distributions, biomarker values, value-attached field interpretations, dates, elapsed-time distributions, eGFR values, cohort masks, outcomes, predictions, folds, weights, selections, or metrics. If a complete assumption manifest is supplied instead of verified evidence, a private fallback may run the identical pipeline under each independently named bundle after raw-token and formula tests, but every output must be labeled `ASSUMPTION_CONDITIONED_UNVERIFIED`; no supportive, adverse, biological, or policy conclusion is permitted, and bundles may never be selected for favorability. With no certificate or manifest, remain structural-only. Certification failure is never a negative biological finding.

## Scientific population and schedule-marginal estimand

Only in `CERTIFIED_READY`, apply masks in this fixed order after the one-to-one join. Use only certificate-listed missing tokens, finite numeric parsing, and positive finite laboratory and age values. Sex is `31-0.0`; code 0 is female and code 1 male only because this coding is locally approved in `datasets/ukb/metadata.json` (metadata source hash `[source checksum]`). Use `21003`, not `21022`, for active visit age; `21022-0.0` is not silently substituted.

1. `B`: valid baseline sex, age `21003-0.0`, date `53-0.0`, creatinine `30700-0.0`, and cystatin C `30720-0.0`.
2. `R_date`: from `B`, valid repeat date `53-1.0`, strictly later than `53-0.0`, with unrounded elapsed years `delta_days/365.25` in the inclusive interval `[2,8]`.
3. `R_complete`: from `R_date`, valid positive finite repeat age `21003-1.0`, creatinine `30700-1.0`, and cystatin C `30720-1.0`.
4. `S_A`: from `R_complete`, baseline equation-derived creatinine eGFR `eGFRcr_0 >= 60`.

Call instance 1 the **first available qualifying exported instance-1 observation**, never the first clinical repeat. The repeat date and elapsed interval are used only for eligibility, descriptive schedule audits, and selection-flow accounting. The repeat date, elapsed time, repeat age, repeat analytes, repeat attendance, and outcome are forbidden from every deployable score design matrix, preprocessing fit, ranking, threshold, recalibration, tie-break, and capacity selection.

The primary outcome is the observed one-visit state `Ycr = I(eGFRcr_1 < 60)`, with no rounding before comparison. Secondary descriptive outcomes, computed without changing `S_A`, are `Ycys = I(eGFRcys_1 < 60)`, `Yboth = Ycr AND Ycys`, and the four-level repeat state `(neither, creatinine-only, cystatin-only, both)`. These labels are equation-derived marker states at one observed repeat; they are not CKD, chronicity, persistent low filtration, measured GFR, or an onset time.

The primary estimand is the paired out-of-fold contrast in threshold decision value and fixed-capacity observed event yield for `Ycr`, averaged over the ten deterministic repeats and over the observed repeat-time distribution in `S_A`. Equivalently, it is performance for low creatinine-equation eGFR status at the next observed exported repeat among selected complete repeat attenders whose repeat lies 2–8 years after baseline. It is not a 2-, 4-, or 8-year risk and not a policy effect. Complete repeat cystatin-C is retained solely to preserve the inherited selected-cohort evidence boundary; dropping it would be a new scientific population, not a compiler repair.

If any requested interpretation uses four-year risk, cumulative incidence, interval-censored onset, benefit from earlier testing, action-dependent visit timing, or outcome ascertainment among people who do not attend, return `STOP_UNIDENTIFIED_FIXED_HORIZON` without scientific fitting. Resolving that claim requires common-horizon or validated longitudinal onset outcomes collected independently of the action, with follow-up/censoring coverage for baseline-eligible nonattenders.

## Equations and exact implementation contract

After certified unit evidence, convert creatinine to mg/dL only by the certificate-authorized conversion. For the UKB unit declared as micromoles/L, the conversion is `Scr = raw_30700 / 88.4`; retain the raw token and converted value privately. Cystatin C must be certified in mg/L or have a certificate-authorized conversion. Let `F=1` denote female and `F=0` male, and use float64 natural powers.

Primary 2021 CKD-EPI creatinine equation:

```text
k = 0.7 if F=1 else 0.9
alpha = -0.241 if F=1 else -0.302
eGFRcr = 142 * min(Scr/k,1)^alpha * max(Scr/k,1)^(-1.200)
          * 0.9938^Age * (1.012 if F=1 else 1)
```

Use the race-free 2021 CKD-EPI cystatin-C-only equation for the discordance feature and secondary outcome:

```text
eGFRcys = 133 * min(Scys/0.8,1)^(-0.323)
           * max(Scys/0.8,1)^(-0.778)
           * 0.9961^Age * (0.932 if F=1 else 1)
```

The optional combined equation is not a predictor or primary endpoint; if reported, it is descriptive only and must be separately labeled:

```text
eGFRcr_cys = 135 * min(Scr/k,1)^alpha * max(Scr/k,1)^(-0.544)
              * min(Scys/0.8,1)^(-0.323) * max(Scys/0.8,1)^(-0.778)
              * 0.9961^Age * (0.963 if F=1 else 1)
```

The baseline incremental feature is `Z = log(eGFRcys_0 / eGFRcr_0)`. No thresholded cystatin feature replaces `Z` in the primary model. The equation certificate must cite the public equation sources (2021 creatinine/cystatin formulation, Inker et al., DOI `10.1056/NEJMoa2102953`, PMID `34554658`, PMCID `PMC8822996`; formula provenance does not certify the UKB fields) and include these corrected float64 test vectors with absolute and relative tolerance `1e-10`:

```text
creatinine: (Scr,Age,F)=(0.9,50,0) -> 104.0490129932253
             (0.7,60,1) -> 98.94831465668567
             (1.2,70,0) -> 65.0565950204461
cystatin:   (Scys,Age,F)=(0.8,50,0) -> 109.39529553827676
             (0.7,60,1) -> 102.37062578462721
             (1.0,70,0) -> 85.04748156103189
combined:   (Scr,Scys,Age,F)=(0.9,0.8,50,0) -> 111.04033757644632
             (0.7,0.7,60,1) -> 107.36626871737116
             (1.2,1.0,70,0) -> 73.82048812375221
```

The vectors are implementation checks, not observed-data assertions. A mismatch stops the bundle. In particular, do not use the incompatible cystatin vectors from an earlier draft; those values do not evaluate from the equation frozen here.

For each continuous input `x`, use one canonical four-column fixed restricted-cubic basis. Set fixed bounds `a,b` to `[40,80]` for age and `[60,120]` for baseline eGFRcr; clip x to `[a,b]` before basis evaluation. Define `k1=a`, `k2=a+(b-a)/3`, `k3=a+2(b-a)/3`, `k4=b`, and for `j=1,2,3`:

```text
d_j(x) = max(x-k_j,0)^3 / (k4-k_j)
B(x) = [ x, d_1(x)-d_3(x), d_2(x)-d_3(x), d_3(x) ]
```

This is the complete basis; do not add another raw age or raw eGFR column. In each training fold, center and population-scale each of the four columns using training rows only; a zero training standard deviation is replaced by 1 exactly as a declared convention. Standardize `F` and `Z` likewise using training rows only, with zero standard deviation replaced by 1. The ordered non-intercept design columns are exactly `[F, B(age_0)[0:4], B(eGFRcr_0)[0:4]]` for `M0-B` (9 columns) and the same plus `Z` for `Mc-B` (10 columns). Persist these names and assert dimensions `M0=9`, `Mc=10`; any other dimension is `FAIL_MODEL_SPEC`.

Fit float64 `sklearn.linear_model.LogisticRegression(penalty='l2', C=1.0, solver='lbfgs', fit_intercept=True, class_weight=None, max_iter=2000, tol=1e-10, random_state=0)`. No tuning or class weighting is permitted. A fold with absent outcome class, nonconvergence, warning indicating nonconvergence, nonfinite coefficient/prediction, or incomplete one-prediction-per-person coverage is `CERTIFIED_ANALYSIS_FAIL`.

## Repeated cross-fitting, thresholds, and capacity

Use exactly ten participant-level, outcome-stratified five-fold repeats with seeds:

```text
104729, 104759, 104773, 104779, 104789,
104801, 104827, 104831, 104849, 104851
```

For each seed, stable-sort rows within outcome by ascending numeric `eid` and assign round-robin fold labels. The same assignment is reconstructed after every label or predictor permutation. `eid` is an administrative tie-break and remains private. Fit all preprocessing and models on training folds only, then generate paired held-out probabilities `p0` and `pc` for every member of `S_A` in every repeat.

For threshold `p_t`, define `A_m(p_t)=I(p_m >= p_t)`, `TP_m=sum(A_m Ycr)`, `FP_m=sum(A_m(1-Ycr))`, and

```text
NB_m(p_t) = TP_m/n - FP_m/n * p_t/(1-p_t)
DeltaNB(p_t) = NB_c(p_t)-NB_0(p_t).
```

Compute the primary threshold contrast at `p_t=0.02`, average the ten repeat-specific contrasts, and report it as net true-positive equivalents per participant and per 1,000. Prespecified secondary thresholds are 0.01 and 0.05; the complete descriptive grid is `{0.001,0.0025,0.005,0.0075,0.010,0.015,0.020,0.030,0.040,0.050,0.075,0.100,0.150,0.200}`. Report treat-none `NB=0` and treat-all `TP=n_events, FP=n-n_events` curves. The 2% exchange rate (one true positive versus 49 false-positive actions) is an explicit operating assumption, not validated utility.

For the co-primary capacity estimand, in each held-out fold allocate exactly the fold quota resulting from floor-plus-largest-remainder allocation of `K10=1,637` total slots across the five fold sizes; assign remaining slots to folds with largest fractional remainders, breaking ties by ascending fold ID. Within each fold, rank held-out probabilities descending, breaking exact ties by ascending numeric `eid`, and select exactly its quota. The selected sets across folds therefore total exactly 1,637 per repeat. Define `E10_m=sum(selected_m Ycr)` and `DeltaE10=mean_repeat(E10_c-E10_0)`, in observed labels per 1,637 slots. The secondary `K5=819` policy uses the same quota/tie algorithm and is descriptive unless the 10% gate passes. Report selected event fraction, event capture, overlap/Jaccard, entrants, leavers, and outcomes entering minus leaving; no selected set or individual action may be published.

Do not rerank within timing bands. Timing bands `[2,4)`, `[4,5)`, `[5,8]` are descriptive audits of schedule heterogeneity. They do not define horizons and cannot change the pooled estimand. Every band requires at least 500 participants and 20 events before directional description; otherwise mark `TEMPORAL_ROBUSTNESS_UNASSESSABLE`.

## Calibration, selection, uncertainty, and artifact checks

Using each person's mean of the ten held-out probabilities, report calibration-in-the-large, logistic calibration intercept and slope, and observed-minus-predicted risk for each model. Before a threshold-policy classification, `Mc-B` must have absolute intercept at most 0.10, slope in `[0.90,1.10]`, and absolute observed-minus-predicted risk at most 0.002; pooled 2% actions must include at least 100 actions and 20 observed positives for each model. These are operational adequacy gates, not safety guarantees. Failure yields `THRESHOLD_POLICY_UNCERTIFIED`; capacity and loss diagnostics may still be reported, but no threshold-policy conclusion is allowed.

Report the complete selection flow: joined, `B`, valid date, 2–8-year date, complete repeat age/analytes, `S_A`, and primary outcome availability. Compare baseline characteristics and field-specific missingness between `B` attendees and nonattendees descriptively. A predeclared sensitivity may fit a five-fold baseline-only attendance model using only sex, age, baseline eGFRcr/eGFRcys and baseline missingness indicators, with training-fold medians, propensity clipping `[0.05,0.95]`, declared weight clipping and normalization, and effective sample size. It may recompute descriptive contrasts in `S_A`; it is not an identification strategy for nonattender outcomes, not a primary gate, and cannot turn the selected-attender result into population prognosis. No future repeat variable enters that attendance model.

Use 4,000 paired participant bootstrap draws with seed `520243`. Resample participants, carrying outcomes, ten paired predictions, threshold actions and capacity selections together; do not refit models or regenerate folds. The primary intervals are two-sided 98% percentile intervals for mean `DeltaNB(0.02)` and mean `DeltaE10`. Report a separate two-sided 98% max-|T| family for secondary thresholds, `DeltaE5`, supported timing-band contrasts, and the two baseline-eGFR stratum contributions. The bootstrap is conditional on frozen cohort, fits, folds and attendance selection and omits model-refitting, cohort-selection and attendance uncertainty. Zero or nonfinite studentizing variance is a declared analysis failure.

Artifact falsification is mandatory and must use the same paired folds and full pipeline. (i) Permute `Z` within baseline-eGFRcr strata `[60,75)` versus `>=75`, sex, attendance status, and timing band, preserving the empirical feature distribution. (ii) Run 200 outcome-label permutations with seed `520242`, within baseline-eGFRcr strata and reconstructing folds each time. (iii) Run a reverse-label sentinel and a private elapsed-time leakage sentinel. A repeat-stable gain in a predictor-null, reverse-label, or leakage sentinel invalidates the corresponding scientific interpretation. A technical assay replicate or batch-control claim cannot be made because no such evidence is available in the configured export unless a certificate supplies it.

For interpretation only, report explanatory loss diagnostics and the 10% decomposition by baseline eGFRcr `[60,75)` versus `>=75`; the contributions must sum exactly to the pooled `DeltaE10`. Compare baseline-only loss with the prior elapsed-conditioned values only as a nonrandomized same-snapshot diagnostic. These diagnostics cannot satisfy or rescue a decision gate and do not retest the prior failed incremental-information claim as a primary endpoint.

## Prespecified gates and result meanings

All scientific labels require `CERTIFIED_ANALYSIS_COMPLETE`, source/schema/join integrity, exact model dimensions, complete predictions, complete uncertainty arithmetic, and completed falsification controls. A calibration or pooled-support failure blocks threshold classification even if capacity is computable.

**Supportive joint decision signal** requires all of the following:

* primary mean `DeltaNB(0.02) >= 0.001`, positive in at least 8 of 10 repeats, and its two-sided 98% lower bound above 0;
* `Mc-B` has positive net benefit at 2% versus both treat-none and treat-all;
* primary mean `DeltaE10 >= 5`, positive in at least 8 of 10 repeats, and its two-sided 98% lower bound above 0;
* calibration and pooled 2% support gates pass;
* no material M1 calibration deterioration, predictor-null/reverse-label/leakage replication, unexplained anchor mismatch, or adverse supported timing band; and
* the result is not reversed by the predeclared selection-weighting sensitivity in a way that invalidates the direction.

This supports only reproducible baseline-input decision information for the observed exported repeat status in selected complete repeat attenders and motivates external validation. It does not establish that ordering a test helps, that patients benefit, or that the assay/equations measure true GFR.

**Threshold-specific but not capacity-compatible** means the 2% threshold gate passes but the 10% capacity gate fails. It supports, at most, a result under the stated hypothetical exchange rate and not a fixed-capacity monitoring program. **Capacity-specific but threshold-uncertified** means the capacity gate passes while calibration or the threshold gate fails; it supports rank concentration only and forbids probability-threshold deployment.

**Adverse to the worthwhile incremental policy** requires both primary practical floors to be ruled out: the 98% upper bound for `DeltaNB(0.02)` is below `0.001` and the 98% upper bound for `DeltaE10` is below `5`. If either upper bound is below zero and at least 8 of 10 repeats are directionally adverse, label that axis directionally adverse. This is evidence against worthwhile incremental value for this prespecified observed-schedule policy, not evidence against cystatin-C biology or every clinical use. A null-compatible point estimate, a failed calibration gate, a certificate failure, or an incomplete control is not adverse biology.

**Inconclusive** applies when practical floors are neither passed nor ruled out, the co-primary axes disagree without a named mixed pattern, timing bands are underpowered, attendance positivity is poor, controls are incomplete, or computation fails. `STOP_UNIDENTIFIED_FIXED_HORIZON`, `STOP_FIELD_UNCERTIFIED`, `FAIL_SCHEMA_BINDING`, `FAIL_MODEL_SPEC`, and `CERTIFIED_ANALYSIS_FAIL` are stopping/technical states, never scientific adverse findings. Non-significance is not equivalence.

The hypothesis is falsified as a worthwhile **joint** baseline policy only when both practical upper-bound criteria are met under certified execution. A loss improvement alone, a point estimate below a floor, or a secondary outcome result cannot support or falsify the joint claim.

## Verification boundary, unavailable evidence, and privacy

A verifier can mechanically check literal source/schema paths and hashes, snapshot and catalog identifiers, headers, row/key/join integrity, certificate structure and digest, missing-token handling, date parsing, sequential masks, equation vectors, unit conversions permitted by the certificate, four-column basis, 9/10 dimensions, training-only preprocessing, fold reconstruction, baseline-only feature lineage, convergence, prediction coverage, threshold/capacity allocation and tie arithmetic, calibration/support rules, bootstrap/permutation arithmetic, decomposition identities, falsification completion, and conclusion-to-gate consistency.

A verifier cannot establish that external field evidence is clinically truthful, that exported values are assay-comparable, that the analytes measure GFR, that a one-visit status is CKD or chronic, that repeat attenders represent nonattenders, that a threshold has acceptable patient-level harms, or that testing changes outcomes. Those claims require expert assay review, technical replicates or external laboratory linkage, adjudicated longitudinal CKD/measured-GFR outcomes, observed decisions and resource/harm data, and prospective external validation. The configured UKB metadata explicitly notes that narrative text, raw imaging, waveforms and sequence variants are unavailable or unsupported; no such modality may be implied.

Keep sources read-only. Never publish `eid`, raw rows, biomarker values, dates, elapsed times, predictions, fold membership, actions, selected sets, attendance weights, bootstrap arrays, or projected participant records. Publish only aggregate diagnostics, status, hashes, equations, and gate-linked conclusions. Candidate support consists of this proposal and future aggregate code/results/audit artifacts only.
