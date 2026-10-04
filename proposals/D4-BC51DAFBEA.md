> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Field-certified UKB repeat kidney-status prioritization with a fail-closed audit branch

## Lineage and substantive repair

This proposal is a substantive child of assessed-valid `[prior hypothesis]` and `[prior hypothesis]`. It preserves the Lead's exact scientific estimand: among participants with a complete first exported qualifying repeat assessment, test whether baseline cystatin-C/creatinine discordance improves prioritization of low creatinine-equation kidney status at that next observed repeat beyond sex, baseline age, and baseline creatinine-equation eGFR. It remains a baseline-only, schedule-marginal prioritization experiment, not a fixed-horizon risk analysis and not a causal test of ordering a laboratory test.

The substantive repair is an evidence-gated state machine that resolves a tension in the parents. A strict assay/date certificate is necessary before raw UKB values can be interpreted or equations applied, but a certificate failure should not make the implementation unauditable or silently turn a technical failure into a biological null. This child therefore makes `STOP_FIELD_UNCERTIFIED` the deterministic scientific status whenever any required field semantic is uncertified, while permitting a separate, deterministic `COMPUTATIONAL_AUDIT_ONLY` execution over headers, hashes, schemas, synthetic fixtures, and aggregate raw availability/malformedness diagnostics. The audit branch can establish whether the implementation is ready to run; it cannot compute biomarker-derived eGFR, define the scientific cohort, fit outcome models, or report a biological result. Certificate failure has precedence over every audit pass.

A second substantive repair is the age/date binding. Field `21003` is the age-at-assessment field used for age in the equation and score (`21003-0.0` baseline and `21003-1.0` repeat). Field `21022-0.0` is age at recruitment, present in `population`, and is retained as a separately certified provenance and consistency-audit field; it must never be substituted for `21003-0.0`, used as a repeat age, or used to infer elapsed time. Field `53` supplies assessment dates (`53-0.0` and `53-1.0`) and is the sole source of the schedule interval. Instance index is not elapsed time, and the repeat is not claimed to be the first chronological laboratory measurement.

## Evidence-supported and untested claims

The available local catalog supports the existence of the requested columns, one-to-one `eid` relationships, the field-instance.array representation, and the fact that these schema artifacts have no temporal columns. It does not locally certify the renal analyte labels, specimen/matrix, assay/platform, units, field-specific missing codes, Gregorian date semantics, or whether instance 1 is the first chronological clinical laboratory test. The local metadata explicitly provides only the frozen public metadata for field 31 and field 21022. Equation provenance is available from the cited CKD-EPI publications, but it does not validate UKB assay semantics or establish measured GFR.

Thus, before certification, no claim about the observed cohort counts or discordance is a scientific result. After certification and a passing computation, the strongest permitted claim is incremental discrimination/prioritization of an equation-derived repeat status under the observed UKB assessment schedule among complete repeat attenders. Even a supportive result cannot establish CKD chronicity, measured GFR accuracy, kidney failure, benefit or harm from ordering testing, clinical utility, cost-effectiveness, or transportability.

## Immutable source and exact table bindings

Use only UKB snapshot `[source checksum]`, catalog `[internal dataset path]` ([source checksum]). All sources are ordinary read-only CSV files; there are no archive members.

* `population`: `[internal dataset path]`, file [source checksum], schema `[internal dataset path]`, schema-artifact [source checksum]; use `eid`, `31-0.0`, and `21022-0.0`.
* `assessment`: `[internal dataset path]`, file [source checksum], schema `[internal dataset path]`, schema-artifact [source checksum]; use `eid`, `53-0.0`, `53-1.0`, `21003-0.0`, and `21003-1.0`.
* `biological_samples`: `[internal dataset path]`, file [source checksum], schema `[internal dataset path]`, schema-artifact [source checksum]; use `eid`, `30700-0.0`, `30700-1.0`, `30720-0.0`, and `30720-1.0`.

Join only these three tables, horizontally on `eid`, with one-to-one uniqueness assertions for each input and the joined result. Before retaining a field, verify all overlapping columns agree exactly, treating two certified missing values as agreement. Do not read fields from `main`, `additional_exposures`, `health_outcomes`, `online_followup`, or `genomics` for the primary experiment. Record input row counts, duplicate-key counts, unmatched-key counts, overlap disagreements, source hashes, schema hashes, and selected-column header hashes.

## Required field certificate and equation manifest

The declared input `field_certificate.json` must have one record for each of the following exact field-instance.array columns: `31-0.0`, `21003-0.0`, `21003-1.0`, `21022-0.0`, `53-0.0`, `53-1.0`, `30700-0.0`, `30700-1.0`, `30720-0.0`, and `30720-1.0`. Each record must contain field ID, table, instance, array index, semantic label, specimen/matrix, unit, assay/platform or measurement method, date representation where applicable, valid domain, field-specific missing codes, source URL, source version/retrieval date, and source hash. The certificate must explicitly distinguish `21003` age at assessment from `21022` age at recruitment and must establish that 53-0 and 53-1 are comparable assessment dates. It must also establish whether 30700 and 30720 at instances 0 and 1 are comparable analytes, specimens, assays, and units; otherwise a frozen conversion/harmonization record is required.

A certificate is `CERTIFIED` only if every item is backed by a frozen local artifact or a versioned, hash-pinned declared implementation artifact. A web search result or an unversioned recollection is not certification. The current local metadata is insufficient for the renal units/assays/missing codes and exact date/instance semantics; therefore, absent a new qualifying certificate, the actual scientific run must stop.

Use an equation manifest rather than an untracked formula string. The manifest freezes the canonical formulas, constants, sex convention, age units, and citations:

* 2021 race-free CKD-EPI creatinine equation, Inker et al., DOI `10.1056/NEJMoa2102953`, PMID `34554658`, PMCID `PMC8822996`:
  `eGFRcr = 142 * min(Scr/k,1)^a * max(Scr/k,1)^(-1.200) * 0.9938^Age * 1.012^F`, with `F=1` female, `F=0` male, `(k,a)=(0.7,-0.241)` female and `(0.9,-0.302)` male.
* 2012 cystatin-C-only CKD-EPI equation, Inker et al., DOI `10.1056/NEJMoa1114248`, PMID `22762315`, PMCID `PMC4398023`:
  `eGFRcys = 133 * min(Scys/0.8,1)^(-0.499) * max(Scys/0.8,1)^(-1.328) * 0.996^Age * 0.932^F`.

The manifest must record the frozen public citation identifiers and a hash of each canonical formula string. It must not be used until the field certificate establishes units. Following certification only, convert 30700 creatinine from certified micromoles/L by `Scr_mg_dL = raw_30700 / 88.4`; retain raw and converted values. Require certified cystatin-C mg/L or a certified conversion. Age is `21003-0.0` for baseline and `21003-1.0` for repeat. `21022-0.0` is not an age fallback. Define `Z=log(eGFRcys_0/eGFRcr_0)` and primary `Ycr=I(eGFRcr_1<60)`; `Ycys=I(eGFRcys_1<60)` is secondary. These labels are equation-derived statuses, not measured GFR, CKD, chronicity, or patient-important outcomes.

## Deterministic status state machine: stop versus audit fallback

Execute the following in the stated order and write one machine-readable status record.

1. `SCHEMA_READY`: verify source hashes, schema-artifact hashes, exact required columns, `eid` uniqueness, and one-to-one join integrity without interpreting participant values.
2. Validate the certificate and equation manifest. For any missing/invalid certificate item, set `field_status=STOP_FIELD_UNCERTIFIED` and record the exact deficiency IDs.
3. If `field_status=STOP_FIELD_UNCERTIFIED`, optionally execute `audit_mode=COMPUTATIONAL_AUDIT_ONLY`. This mode is deterministic and may perform only: header/schema/path/hash/key tests; synthetic in-memory fixtures for every certified-missing, negative-uninterpreted, malformed-date, interval-boundary, unit-conversion, equation, spline-dimension, fold, tie, quota, bootstrap, and arithmetic-identity test; and aggregate raw lexical availability diagnostics (counts of empty/nonempty/non-numeric tokens per required column) without mapping tokens to analytes or computing a participant biomarker/eGFR/outcome/cohort.
4. The audit must not parse real participant dates into elapsed time, recode a real negative value, convert a real laboratory value, calculate a real eGFR or Z, select real participants, fit a model, bootstrap, permute, or report inherited anchor counts as scientific output. Synthetic fixtures must contain no real `eid` and must be retained separately from the source data.
5. Final status precedence is deterministic: `STOP_FIELD_UNCERTIFIED` (with optional `COMPUTATIONAL_AUDIT_PASS` or `COMPUTATIONAL_AUDIT_FAIL` as a subordinate diagnostic) whenever certification fails; `FAIL_COMPUTATIONAL_AUDIT` if certification passes but any audit or implementation invariant fails; `READY_FOR_SCIENTIFIC_EXECUTION` only if both certificate and audit pass. A computational-audit pass never upgrades an uncertified field to certified. No biological support, adversity, or null finding may be reported in either stop/audit state.
6. If a nonmissing real date is syntactically unparseable after certification, return `FAIL_UNCERTIFIED_DATE` rather than treating it as missing. If a real token is outside the certified domain or missing-code set, return `FAIL_UNCERTIFIED_VALUE`. These are not biological adverse findings.

This makes a missing certificate actionable rather than a predetermined scientific negative: the implementation can be audited and repaired now, while field interpretation awaits expert/versioned evidence.

## Population, time boundary, missingness, and attendance selection

Only after `READY_FOR_SCIENTIFIC_EXECUTION`, parse field-specific missing codes exactly as certified. Do not globally recode negative values. Report raw-empty, certified-missing-code, nonnumeric, out-of-domain, and malformed-date counts separately for every required field and every sequential mask. A nonmissing malformed date is never silently converted to missing.

Define the primary sequence:

* `J`: one-to-one join of the three tables.
* `B`: valid certified sex `31-0.0`, assessment age `21003-0.0`, baseline date `53-0.0`, baseline 30700 and 30720; finite positive age and laboratory values and valid sex. `21022-0.0` is retained for the audit, but does not fill or replace `21003-0.0`.
* `R_date`: within B, valid repeat date `53-1.0` and strict `date1 > date0`; elapsed years is exact calendar-day difference divided by `365.25`, inclusive `[2,8]`.
* `R_complete`: within `R_date`, valid finite positive repeat age `21003-1.0`, 30700, and 30720.
* `S_A`: within `R_complete`, baseline `eGFRcr_0 >= 60`.

The expected diagnostic anchors from prior implementations are `J=502,370`, `B=468,887`, `R_complete=16,546`, `S_A=16,372`, and 309 primary events, with approximate elapsed range 2.1081451061–6.1136208077. They are not forced. Any discrepancy is reported by field-specific mask reason and sent to review; it cannot be repaired by changing a field or date rule after seeing the result. The repeat is specifically exported instance 1, the first available qualifying exported repeat in this design, not the first chronological clinical test.

For attendance/missingness selection, preserve the primary complete-attender estimand but avoid the parents' degenerate missingness model. Define a separate descriptive selection frame `B_att` before lab completeness: valid certified `31-0.0`, `21003-0.0`, and `53-0.0`, with baseline laboratory tokens retained as either certified valid values, certified missing, or an explicit failure category. Define `A=1` when the participant has a valid later date in the `[2,8]` interval and complete valid baseline and repeat 30700/30720 and repeat 21003 measurements; otherwise `A=0`. Do not use outcome or repeat values to define predictors of A.

Fit a five-fold cross-fitted attendance model in `B_att` using only baseline sex, age, raw baseline creatinine and cystatin C where valid, and field-specific baseline missingness indicators; training-fold medians are used only for the observation model, and missing indicators remain explicit. No eGFR equation is required for this model, and no repeat/date-after-baseline variable is a predictor. Report A prevalence, field-specific missingness, calibration, clipped inverse-probability weights `w=P(A=1)/clip(p,0.05,0.95)` normalized to mean one among A=1, effective sample size, and positivity failures. These weights are a selection sensitivity and cannot identify outcomes for non-attenders or rescue primary failure. The primary outcome models remain restricted to `S_A`, so the scientific estimand and 9/10 dimensions are unchanged.

Separately report the certified `21022-0.0 - 21003-0.0` discrepancy distribution as a provenance/quality diagnostic only. Do not exclude, impute, or redefine participants based on that discrepancy unless a field certificate explicitly requires it.

## Fixed baseline-only models and dimensions

For every participant in `S_A`, use only baseline sex `F`, baseline age `21003-0.0`, baseline eGFRcr, and optionally baseline discordance Z. M0 is `[F, rcs4(age), rcs4(eGFRcr)]`; M1 appends standardized Z. The explicit `rcs4` basis has four columns: clip to fixed bounds, let `k1=lower`, `k2=lower+(upper-lower)/3`, `k3=lower+2*(upper-lower)/3`, `k4=upper`, define `d_j(t)=max(t-k_j,0)^3/(k4-k_j)` for j=1,2,3, and return `[u, d1(u)-d3(u), d2(u)-d3(u), d3(u)]`. Use age bounds `[40,80]` and eGFRcr bounds `[60,120]`; center and population-scale all continuous basis columns and standardize F and Z with training-fold moments, replacing a zero SD by 1.

Hard assertions are M0 = `1+4+4=9` non-intercept columns and M1 = `9+1=10`; any other dimension is `FAIL_MODEL_SPEC`. Use float64 logistic regression `penalty='l2', C=1.0, solver='lbfgs', fit_intercept=True, class_weight=None, max_iter=1000, tol=1e-10, random_state=0`; convergence warnings, nonfinite probabilities, and `n_iter_ >= 1000` fail execution. The feature allowlist must prove that 21022, both dates, elapsed time, repeat labs, A, Y, and attendance weights are absent from score construction.

Use ten deterministic outcome-stratified five-fold repeats with seeds `104729,104759,104773,104779,104789,104801,104827,104831,104849,104851`. Stable-sort by `(label,eid)`, assign round-robin fold IDs 0–4 within each label, and reuse the exact rule under permutations. Produce paired OOF predictions for identical S_A participants, one prediction per participant, repeat, and model.

## Estimands, uncertainty, falsification, and interpretation

For q=`0.01,...,0.20`, select top `ceil(q*n)` paired OOF risks with stable descending risk and ascending numeric `eid` ties. Report capture, selected event fraction, PPV, and `DeltaC(q)`. At thresholds `{0.001,0.0025,0.005,0.0075,0.010,0.015,0.020,0.030,0.040,0.050,0.075,0.100,0.150,0.200}`, report `NB=TP/N-FP/N*p_t/(1-p_t)`, DeltaNB, treat-all, and treat-none. These are mathematical, assumption-indexed policy summaries, not clinical net benefit.

Use 4,000 paired participant bootstrap draws with seed `520241`, recomputing frozen OOF capacity and threshold summaries; provide separate two-sided simultaneous 98% max-|T| bands for capacity, DeltaNB, calibration, and supported strata. A zero/nonfinite studentizing SD is a declared failure. Use 200 outcome-label permutations with seed `520242`, permuting within baseline eGFRcr strata `[60,75)` and `>=75`, reconstructing labels/folds and refitting both models. Also run a predictor-null permutation of Z within baseline eGFRcr deciles and sex, a reversed-label sentinel, and an elapsed-time leakage sentinel. None is a clinical policy claim.

At 10% and 5% capacity, allocate quotas by floor plus largest remainder, ties by fold index, then rank stably by descending probability and ascending numeric eid. Report exact selected N, events, overlap, Jaccard, entrants/leavers, and identities. Timing bands `[2,4)`, `[4,6)`, `[6,8]` are descriptive decompositions of the already globally selected 10% set; never rerank within bands. Require N >= 1,000 and 20 events for directional timing claims, and require exact summation to pooled DeltaC.

Support requires certified fields, exact source/join integrity, 9/10 dimensions, complete arithmetic, no material calibration deterioration, a contiguous predeclared 5–15% positive simultaneous DeltaC band, repeat/stratum stability, favorable outcome-null comparison, and no comparable predictor-null, reversed-label, or leakage gain. Adverse evidence is a reproducibly negative incremental curve, calibration harm, null-compatible gain, leakage gain, or failed/incomplete computation after certification. Inconclusive evidence includes STOP_FIELD_UNCERTIFIED, audit-only status, intervals crossing zero, isolated gains, unstable strata, or poor attendance positivity. A stop/audit result is never a biological negative. Even a supportive result remains limited to schedule-marginal equation-derived status prioritization; measured GFR, CKD chronicity, treatment benefit, utility, and transportability require adjudicated persistent CKD, measured GFR, observed decisions and harms, clinical review, and external/prospective validation.

All participant rows, eids, predictions, folds, actions, selections, weights, and resampling arrays remain private. Publish only aggregate diagnostics and the hashes/status records needed for audit.
