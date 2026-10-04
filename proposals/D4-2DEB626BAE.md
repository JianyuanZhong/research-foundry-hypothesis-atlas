# Baseline cystatin-C/creatinine discordance and repeat biomarker status: a fail-closed actionability-boundary successor

## Lineage and substantive change

This is a substantive child of assessed-valid `[prior hypothesis]` for the Lead goal. The parent asks whether baseline cystatin-C/creatinine discordance improves baseline-only prioritization of a repeat creatinine-equation biomarker status among participants with certified baseline eGFRcr at least 60 and an observed complete first repeat assessment. This child keeps that estimand and all of its certificate, race-free equation, timing, leakage, null, privacy, and noncausal safeguards.

The targeted repair is an explicit, data-bound actionability determination. I inspected the current UKB catalog, metadata, and the four relevant schema files. The available export does contain a `health_outcomes` table and an `online_followup` table, so a superficially attractive extension would be to relate baseline discordance to a later clinical event or a subsequent care action. That extension is not identifiable under the current evidence boundary. The current UKB metadata says that per-field labels, units, and missing-value meanings are absent, that field-instance.array is not elapsed time, and that no verified narrative or clinical diagnosis extraction is available. The current schema metadata declares no temporal columns for either `health_outcomes` or `online_followup`. Consequently, a field ID in either table cannot, by itself, establish an event identity, ascertainment date, incident-versus-prevalent status, censoring time, treatment/action occurrence, or clinical adjudication.

The substantive advance is therefore not a fabricated endpoint analysis. It is a prespecified endpoint-admissibility gate that tests whether the four-table export can support a decision-relevant extension, while preserving the narrower repeat-biomarker-status experiment when it cannot. This prevents a positive protocol-ranking result from being misrepresented as testing benefit, CKD progression, kidney failure, or improved patient outcomes.

## Evidence-supported and untested claims

Evidence supported by the supplied materials and parent protocol is limited to the following. The export has participant-keyed structured tables with an `eid` identity, baseline and repeat biomarker columns used by the parent, and separate health-outcome and online-follow-up tables. The parent can, conditional on an authoritative field certificate, evaluate incremental prediction of observed repeat biomarker-derived statuses. The 2021 CKD-EPI equations are a prespecified computational protocol, not evidence that local field units or assay semantics are certified.

The following claims remain untested and are not licensed by this child: that discordance predicts adjudicated CKD, chronic eGFR decline, kidney failure, hospitalization, mortality, treatment initiation, repeat-testing decisions, patient benefit, harms, cost-effectiveness, or utility. Neither a field-instance name nor a nonmissing value establishes any of those claims.

## Immutable data boundary and exact current bindings

Use only UKB rectangular export snapshot `[source checksum]` and catalog `[internal dataset path]`, catalog [source checksum]. All source files are read-only ordinary files; archive member is `ordinary file` for every table below.

The four-table audit and parent computation bind these exact files and schemas.

| logical table | exact schema JSON | read-only source | source SHA-256 | schema SHA-256 | key / required fields |
|---|---|---|---|---|---|
| `biological_samples` | `[internal dataset path]` | `[internal dataset path]` | `[source checksum]` | `[source checksum]` | `eid`, `30700-0.0`, `30700-1.0`, `30720-0.0`, `30720-1.0` |
| `assessment` | `[internal dataset path]` | `[internal dataset path]` | `[source checksum]` | `[source checksum]` | `eid`, `53-0.0`, `53-1.0`, `21003-0.0`, `21003-1.0` |
| `population` | `[internal dataset path]` | `[internal dataset path]` | `[source checksum]` | `[source checksum]` | `eid`, `31-0.0` |
| `health_outcomes` | `[internal dataset path]` | `[internal dataset path]` | `[source checksum]` | `[source checksum]` | `eid`; no outcome field is admissible until individually certified |

For the endpoint-admissibility audit only, the following fifth available table may be inspected, but it cannot be used to assert a care action or a dated clinical endpoint without certification: `online_followup`, schema `[internal dataset path]`, source `[internal dataset path]`, source [source checksum], schema [source checksum], ordinary-file archive member. Its schema has 5,467 columns and declares no temporal columns; this is a structural fact, not a statement that no follow-up information exists.

Horizontally join the parent tables and any audit table one-to-one on `eid`; assert non-null unique keys and agreement of overlapping columns. Never publish participant rows, eids, notes, or field-level values.

## Endpoint-admissibility gate and why no extension is currently identifiable

Before looking at endpoint values, inspect only schema metadata and the participant-independent certificate. A candidate endpoint can enter an outcome analysis only if an authoritative certificate supplies all of the following for the exact field-instance(s): field identity and clinical meaning; coding and missing codes; units where relevant; ascertainment source; event-versus-status semantics; date or interval semantics; incident/prevalent definition; linkage coverage; censoring and end-of-observation rules; and an independently reproducible provenance/checksum. For a care-action endpoint, the certificate must additionally establish that the field records an actual clinical decision or order, rather than intention, attendance, self-report, or an administrative proxy.

The existing approved metadata certifies only field 21022 age at recruitment and field 31 sex/coding. It does not certify the health-outcome or online-follow-up fields, nor the parent biomarker fields and assessment-date semantics. The metadata explicitly records `time: Field-instance.array; instance index is not elapsed time; exact dates remain server-only`, and `coding_metadata: missing locally except frozen public field21022 and field31/coding9 below`. The schema files for `health_outcomes` and `online_followup` have empty `temporal_columns`. Therefore no exact health outcome, subsequent action, or follow-up horizon can be named from these files without inventing metadata. The certificate gate must stop with `NEUTRAL_STOP_NO_FIELD_CERTIFICATE` (or the more specific existing technical-stop state when applicable), before any endpoint count, hazard, risk, event-free curve, or endpoint model is generated.

This is not a negative biological finding. It is a technical/evidence-boundary finding: the available evidence does not identify the endpoint estimand. Adding a health-outcome table to the join without field certification would create false precision, not clinical actionability.

## Preserved parent experiment

If and only if the parent certificate contract passes, retain the parent population and schedule-marginal estimand exactly.

1. Join `biological_samples`, `assessment`, and `population` on `eid` after source/schema/hash gates.
2. Construct baseline-valid `B` using certified sex `31-0.0`, baseline date `53-0.0`, age under the certificate's predeclared rule, and baseline `30700-0.0` and `30720-0.0` with field-specific missing-code handling and positive finite checks.
3. Require `53-1.0 > 53-0.0`, with `2 <= (date1-date0)/(365.25 days) <= 8`, then complete positive finite repeat biomarkers `30700-1.0` and `30720-1.0`.
4. Restrict to baseline `eGFRcr_0 >= 60`; this remains conditional on observed complete first-repeat attendance and is not a fixed-horizon risk population.
5. Compare baseline-only M0 (sex, certified age, baseline eGFRcr with inherited fixed natural-cubic-spline bases) with M1 (M0 plus training-fold-standardized baseline `Z=log(eGFRcys_0/eGFRcr_0)`) using the parent's paired outcome-stratified five-fold cross-fitting, ten fixed repeats, fixed L2 logistic regression, paired Brier primary contrast, capacity grid, bootstrap, leakage sentinel, label/predictor/reversed-label nulls, timing bands, selection sensitivity, and repeat-stability requirements.

The parent primary outcome remains `Ycr=I(eGFRcr_1<60)` at the observed repeat interval. Secondary outcomes remain repeat cystatin-C and combined-equation statuses and the four-level pair. These are biomarker-derived statuses, not CKD, chronicity, measured GFR, kidney failure, clinical events, or treatment indications.

## Prespecified interpretation and decision states

* **Supportive:** only if all technical gates pass and M1 improves the predeclared repeat-biomarker protocol-ranking estimand over the parent’s capacity region with uncertainty, null, interval, selection, and repeat-stability safeguards. This supports conditional ranking for repeat biomarker assessment in the selected observed-attender cohort only. It does not support testing benefit or any clinical outcome claim.
* **Adverse:** technical gates pass and M1 reproducibly worsens the repeat-status ranking/calibration estimand. This argues against adding discordance for that narrow prioritization protocol, not against cystatin C clinically.
* **Inconclusive:** technical gates pass but uncertainty crosses the null, results are materially interval/equation/repeat heterogeneous, or isolated capacity points drive the result. No action or threshold recommendation follows.
* **Neutral technical stop:** missing or contradictory certificate, unresolved unit/assay/instance/date semantics, source/schema failure, failed equation tests, failed null completion, or endpoint-admissibility failure. This is neither support for nor evidence against a biological hypothesis.

A health-outcome or care-action extension may be proposed as a later child only after a participant-independent authoritative certificate resolves the exact field identity, coding, dates, coverage, incident definition, and clinical adjudication. Even then, a prognostic association would not estimate the effect of ordering a test; testing benefit would require observed decisions, downstream care, harms, costs, and an appropriate causal design.

## Falsification and verification additions

The compiler must run a static endpoint audit that fails closed if any health-outcomes or online-follow-up field is included without a complete certificate record. It must verify that the parent feature audit excludes all health-outcome, follow-up, repeat attendance, repeat date, interval, completeness, and future variables. It must reject any code that interprets an instance number as elapsed time or a nonmissing administrative field as a clinical event.

The verifier can check exact current paths and hashes, the four-table `eid` join, schema-declared absence of temporal columns, certificate presence and digest, endpoint-field admissibility logic, parent timing and feature restrictions, and state-specific output permissions. It cannot determine the clinical meaning of an uncertified field, establish CKD or chronicity, adjudicate an event, estimate testing benefit, or establish transportability. The currently defensible pre-certificate output remains `NEUTRAL_STOP_NO_FIELD_CERTIFICATE`, with no participant outcome or biomarker result permitted.

## What changed and what remains uncertain

Changed: the proposal now binds `health_outcomes` exactly as a fourth-table structural audit, identifies `online_followup` as an additional non-admissible audit source with exact current bindings, and adds an explicit certificate-based endpoint gate. It explains why a decision-relevant endpoint extension is not identifiable from the present four-table evidence boundary rather than silently treating the health-outcome export as a clinical endpoint. It also explicitly separates technical neutral stop from adverse or inconclusive biological results.

Unchanged: the parent’s baseline-only biomarker-status hypothesis, exact observed 2–8-year repeat schedule, certificate requirement, race-free equations, complete-repeat selection boundary, cross-fitting, bootstrap/null controls, privacy rules, and noncausal interpretation limits.

Remaining uncertainty: authoritative field semantics, assay comparability, exact assessment-date meaning, endpoint ascertainment and linkage coverage, and clinical adjudication are unavailable in the current evidence. No conclusion about clinical outcomes or benefit is therefore identifiable in this child.
