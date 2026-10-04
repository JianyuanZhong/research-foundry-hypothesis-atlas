# Observable report-to-summary chronology versus discordance despite adequate storage separation in pulmonary-nodule handoff

## Clinical decision and substantive advance

The prospective design choice is whether to test a trigger that accelerates radiology-to-discharge workflow, a reconciliation step that checks the discharge artifact against the final nodule recommendation, or both. The selected parent correctly showed why ordinary discharge-summary latency must be calibrated, but its `A` versus `C` decomposition cannot identify this choice: generic `note/discharge.storetime - dischtime` latency says nothing about how the recommendation and the summary were ordered relative to one another. Conversely, a discordant summary stored after a recommendation does not prove that its author had seen the recommendation, because MIMIC supplies no authoring, signing, UI-display, inbox, acknowledgement, or communication timestamp.

This child therefore tests a narrower, falsifiable mechanism hypothesis:

> Among a denominator frozen solely from adjudicated pre-discharge radiology evidence, is discharge-content discordance concentrated in summaries whose database storage precedes or closely follows storage of the operative recommendation, or does a clinically material discordance burden persist when the operative recommendation was stored at least 24 hours before both discharge and summary storage?

The first pattern is an **observable storage-chronology phenotype compatible with a report-to-summary workflow race**. The second is **content discordance despite adequate observable storage separation**, compatible with a reconciliation problem. Neither pattern establishes visibility, draft timing, signature, transmission, acknowledgement, communication, or causation. The design preserves the parent's institutional-latency controls but adds reciprocal report/addendum chronology, a fixed lead-time classification, all-opportunity joint burdens, and precision/overlap gates that permit four decision states: race-compatible only, reconciliation-compatible only, both, or unresolved.

The strongest existing evidence is only that the complete-source audit found large ordinary discharge-storage latency and ample radiology/chest-control volume, making the experiment feasible and generic-latency calibration necessary. The unresolved claim tested here is whether content discordance has a reproducible relationship to observable report-to-summary storage chronology. A successful result can prioritize what a prospective timestamp/UI study should measure; it cannot select an intervention as effective.

## Exact read-only MIMIC binding and provenance

Use MIMIC snapshot `[source checksum]`. All source data remain read-only; derived adjudication and analysis files are written only in the workspace.

1. Core archive `[internal dataset path]`, [source checksum]:
   * archive member `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`, columns `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admit_provider_id, admission_location, discharge_location, insurance, language, marital_status, race, edregtime, edouttime, hospital_expire_flag`; key `(subject_id,hadm_id)`; primary boundary `D=dischtime`; schema [source checksum].
   * `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`, key `subject_id`, columns `subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod`; used for adult status and interval-censored death only. Represented age 91 means 90+.
   * `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`, columns `subject_id, hadm_id, transfertime, prev_service, curr_service`; terminal service is the last `curr_service` at or before `D`, with ties resolved deterministically by source row order; schema [source checksum].
   * `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, columns `subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime`; schema [source checksum].
   * `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`, columns `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`; ICU indicator is any exact `(subject_id,hadm_id)` row; schema [source checksum].
   * `mimic-iv-3.1/hosp/diagnoses_icd.csv.gz` and `mimic-iv-3.1/hosp/d_icd_diagnoses.csv.gz`, joined on `(icd_code,icd_version)`, are descriptive covariates only and never establish incidental status, recommendation appropriateness, cancer, or eligibility.
2. `[internal dataset path]`, [source checksum], ordinary file/table `note/radiology`, columns `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`; identity `(subject_id,hadm_id,note_id)`, schema [source checksum].
3. `[internal dataset path]`, [source checksum], ordinary file/table `note/radiology_detail`, columns `note_id, subject_id, field_name, field_value, field_ordinal`; join `(subject_id,note_id)`, schema [source checksum]. Complete inspection shows the available fields are `exam_code`, `exam_name`, `cpt_code`, `parent_note_id`, and `addendum_note_id`; only the last two define report/addendum edges.
4. `[internal dataset path]`, [source checksum], ordinary file/table `note/discharge`, the same eight note columns and note schema hash as radiology; join `(subject_id,hadm_id)` to admissions and restrict `note_type == 'DS'`.
5. `[internal dataset path]`, [source checksum], ordinary file/table `note/discharge_detail`, columns `note_id, subject_id, field_name, field_value, field_ordinal`, join `(subject_id,note_id)`, schema [source checksum]. Complete inspection shows only `author`; it is not a section ontology, signature time, or communication field.

Dates are subject-specific deidentified shifts. Only within-subject/admission intervals are interpreted; no cross-subject calendar-era trend is permitted.

## Reused complete-source feasibility evidence, not study results

Reuse the selected parent's attached executable audit and JSON output without rerunning or reinterpreting its lexical proxy as clinical truth:

* `[internal dataset path]`
* `[internal dataset path]`

The audit streamed all rows, with no row sampling: 2,321,355 radiology rows, 6,046,121 radiology-detail rows, 331,794 `DS` rows, and 546,028 admissions. There was one `DS` row per discharge key in this snapshot and 17 missing DS storetimes. Among 331,715 linked DS rows, median `DS storetime-D` was 3.55 hours, p90 101.38 hours, and p95 202.02 hours. The retrieval-only pulmonary proxy yielded 3,764 reports; its report chart-to-store p95 was 14.0 hours. There were 894,757 chest/nonproxy reports with chart-to-store p95 15.32 hours. These values justify fixed 24-hour storage-separation and 7-day ascertainment horizons, but do not prove any report or summary was displayed, final, signed, read, transmitted, or communicated. The prior 3,861-versus-3,764 lexical-screen discrepancy remains an implementation-diff diagnostic; neither count defines `N`.

## Population and immutable all-opportunity denominator

The unit is the first eligible admission per subject. Apply the selected parent's population without modification:

* adult admission;
* radiology report linked exactly on nonmissing `(subject_id,hadm_id)` and with `admittime - 12 hours <= charttime <= D`;
* patient-specific, unconditional chest/thoracic CT recommendation at exactly 3, 6, or 12 calendar months for an incidental pulmonary nodule or indeterminate focal nodular pulmonary opacity;
* exclude in-hospital death, hospice/comfort-only transition, screening, established surveillance, cancer staging/oncologic surveillance, explicit no-follow-up, conditional/optional plans, and recommendations first introduced after `D`;
* do not infer smoking pack-years, Fleischner appropriateness, complete size/risk inputs, or malignancy.

Two independent radiology-trained reviewers, blinded to discharge text, DS `storetime`, later outcomes, and control labels, adjudicate eligibility, incidental status, action, exact interval, material addendum meaning, and timestamp uncertainty. Resolve disagreement by a third reviewer; report raw agreement and Gwet AC1 or kappa before resolution.

Freeze the full candidate cascade and final `N` before exposing discharge text, discharge `storetime`, later imaging/death, or any mechanism outcome. Freeze includes every screened row, linked chain, exclusion reason, late introduction/change, unresolved chain `U_R`, selected first admission, and hash of the adjudication file. Neither content availability nor chronology may change `N`. The all-opportunity denominator is used for every joint burden and primary state probability.

## Reciprocal report/addendum reconstruction and operative recommendation time

Construct a directed graph per subject from detail rows:

* parent `P` naming `A` through `field_name='addendum_note_id', field_value=A.note_id`; and
* addendum `A` naming `P` through `field_name='parent_note_id', field_value=P.note_id`.

An edge is valid only if both reciprocal rows exist, both note rows exist, `subject_id` agrees everywhere, both notes have the same nonmissing index `hadm_id`, and each referenced note ID is unique within subject. Preserve all `field_ordinal` values. One-way links, cross-subject links, cross-admission links, duplicate/conflicting parents, cycles, missing nodes, or required missing/conflicting times are `U_R`; they are never converted to an omission, a race, or adequate lead time.

Reviewers label, without seeing discharge information:

* `R_intro`: earliest chain component that introduces the eligible unconditional recommendation;
* `R_final`: latest chain component at or before `D` that materially determines the operative nodule/action/interval at discharge.

A nonmaterial correction does not reset `R_final`. A post-`D` first introduction is late and ineligible. A post-`D` material change that makes the at-discharge plan unknowable is a prespecified late-change/`U_R` exclusion rather than hindsight reassignment. Eligibility requires both `R_final.charttime <= D` and `R_final.storetime <= D`. The primary chronology uses `R_final.storetime`; `R_intro.storetime` is a locked sensitivity. `charttime` remains an observed chart label used for the eligibility boundary and lag diagnostics, not creation, draft, signature, availability, or communication time.

## Canonical discharge artifact and preserved all-`N` states

The snapshot has one `note_type='DS'` row per discharge key. This sole row is the canonical artifact; a future snapshot with multiplicity greater than one stops execution and requires a new prespecified version rule. Detail `author` neither changes the artifact nor supplies a time.

At `D`, retain exactly the parent's mutually exclusive exhaustive states over all `N`:

* `F`: DS stored by `D`, classifiable, and faithfully carries the patient-specific pulmonary finding, chest/thoracic CT action, and exact compatible interval/date;
* `C_O`: stored by `D`, classifiable, but no patient-specific actionable plan;
* `C_I`: stored by `D`, classifiable, but finding/action/timing is incomplete or discordant without a documented alternate resolution;
* `R`: stored by `D` with a documented alternate resolution such as refusal/preferences, goals-of-care decision, specialist takeover with a concrete alternative, or scheduled outside follow-up;
* `A`: known DS `storetime > D`; a storage-delay state only;
* `U_D`: missing DS storetime, absent/unreadable/contradictory linkage, or unclassifiable text.

A DS stored before `R_final.storetime` is a stale-storage chronology marker and is not blamed for omission. `A` remains `A` in the primary departure state even if its later text is faithful or discordant. Report the complete state vector, `p_A-p_C` with `C=C_O+C_I`, and simultaneous intervals/unknown bounds as inherited.

For the new mechanism module, classify the same sole DS text only if `storetime_DS <= H7 = D+168 hours`. Assign `F7`, `C_O7`, `C_I7`, or `R7` using the same blinded content rubric. Otherwise retain `A7`; missing/unclassifiable remains `U_D7`. This creates an exhaustive all-`N` transition table from the immutable `D` state to the `H7` state. It does not redefine the departure result or imply a clinically safe grace period.

## Observable storage chronology and fixed adequate-separation rule

For every frozen opportunity define, using only observed database timestamps:

* `t_R = R_final.storetime`;
* `t_I = R_intro.storetime` for sensitivity;
* `t_S = canonical DS.storetime`;
* `X = (D - t_R)` in hours, the recommendation-storage-to-discharge separation;
* `Y = (t_S - t_R)` in hours, the reciprocal recommendation-storage-to-summary-storage separation;
* `Z = (t_S - D)` in hours, ordinary DS storage lag;
* `L_RAD = R_final.storetime - R_final.charttime`, a report-label-to-storage diagnostic only.

Never rename `X` or `Y` visibility, notification, authoring, review, drafting, signing, or communication lead time. Negative or contradictory values are reported; missing required values produce unknown states, not imputation.

The primary adequate observable storage separation is fixed at `h=24 hours`, selected before discharge-content adjudication and longer than the p95 chart-to-store lag in both preexisting radiology proxy controls. It is an operational threshold, not a validated clinical standard. For DS artifacts stored by `H7`, assign exactly one chronology class:

1. `P` (predecessor/stale storage): `Y < 0`; the DS was stored before the operative recommendation component.
2. `T24` (tight or departure-proximate storage): `Y >= 0` and either `Y < 24` or `X < 24`.
3. `Q24` (adequately separated storage): `X >= 24` and `Y >= 24`.
4. `U_T`: missing/contradictory required timestamps or unresolved chain.

`W24 = P union T24` is the race-compatible chronology stratum. `Q24` is only “adequately separated in observed database storage.” It does not say the recommendation was visible before summary drafting. Report `P` and `T24` separately before any combined `W24` interpretation. Repeat locked sensitivity tables at `h=6,12,48 hours`, with `R_intro` replacing `R_final`, and at `H24=D+24 hours`; none may replace the primary 24-hour/7-day specification.

## Institutional latency and chronology controls

Retain the parent's controls and add a control that is reciprocal to the new chronology estimand. Labels and matching variables are frozen before nodule discharge content is opened.

1. **Ordinary discharge controls `O`:** every adult admission with a unique DS and nonmissing `D/t_S`, excluding all frozen index opportunities. Compute `Z`, and late-storage probabilities at `D`, `D+24h`, and `D+7d`.
2. **Chest-imaging controls `I`:** linked chest/CT radiology reports in `admittime-12h` through `D` that fail the frozen nodule-recommendation retrieval screen. They calibrate `L_RAD`, not clinical absence or visibility.
3. **Last-chest chronology controls `J`:** among `I`, retain reports with `charttime <= D` and `storetime <= D`. Select exactly one per admission: the report with latest `storetime`; ties use latest `charttime`, then lexicographically smallest `note_id`. Join that admission's sole DS and compute the same `X_J=D-storetime_J`, `Y_J=t_S-storetime_J`, and `P/T24/Q24` classes. Exclude any subject's frozen index admission and any report/addendum chain that entered the eligibility cascade. `J` quantifies how often generic inpatient chest reporting is stored close to discharge/summary storage; it has no content-propagation outcome.
4. **Matched/standardized controls `M`:** use the parent's pre-outcome strata: admission type, discharge location, ICU indicator, LOS bin (`0-1`, `>1-3`, `>3-7`, `>7` days), and terminal service family. Full-control standardization is primary; deterministic up-to-four exact matches per `N` admission are sensitivity. No outcome-driven covariate choice or coarsening is allowed.

For each boundary, retain the parent's `Delta_b = q_N(b)-q_O^std(b)`. Add `Gamma_W = Pr_N(W24)-Pr_J^std(W24)`, `Gamma_P`, and `Gamma_Q`. These are descriptive chronology contrasts. A large `W24` prevalence that is equally common in `J` indicates a generic institutional storage sequence, not a nodule-specific workflow. A nodule excess suggests specificity but still does not establish causation or visibility. The content mechanism conclusions below are never rescued by a favorable control contrast.

The existing radiology-process falsification remains: report `L_RAD` and `K_D=I(t_R<=D)` against chest controls. If nodule chronology is explained by generic report storage lag, label the mechanism unresolved. No `charttime`-only result may substitute for storage chronology.

## Primary estimands on the frozen denominator

Let `C7=C_O7 union C_I7`, and let `E7=F7 union C7 union R7` denote classifiable DS content by `H7`. First report the all-`N` joint table crossing `D` state, `H7` state, and `P/T24/Q24/U_T`. The primary decision quantities are:

### All-opportunity burdens

* `B_W = Pr(C7 and W24)`;
* `B_Q = Pr(C7 and Q24)`;
* `B_P = Pr(C7 and P)` and `B_T = Pr(C7 and T24)`;
* `B_U = Pr(A7 or U_D7 or U_T)`.

These preserve all opportunities and directly quantify how much of `N` has discordance in race-compatible versus adequately separated observed chronology.

### Conditional descriptive failure rates

* `theta_W = Pr(C7 | E7 and W24)`;
* `theta_Q = Pr(C7 | E7 and Q24)`;
* `theta_P` and `theta_T` analogously;
* `RACE = theta_W-theta_Q`.

`RACE` is an association across storage-order strata, not an effect of lead time. `R` stays in the classifiable denominator and is not silently counted as failure or success; also report the multinomial `F7/C_O7/C_I7/R7` distribution in each chronology class. Report crude estimates first. A predeclared standardization to the frozen `N` covariate distribution is secondary and cannot override the all-`N` burdens.

### Mechanism decision margins

The operationally important rate margin is 0.10 and all-opportunity burden margin is 0.05. They are design thresholds, not validated quality standards.

* **Race-compatible component passes** only if the simultaneous 95% lower confidence limit for `RACE` is greater than 0, its point estimate is at least 0.10, and the simultaneous lower limit for `B_W` is at least 0.05. `P` and `T24` must be shown separately; opposite-signed subtype estimates make the race subtype unresolved even if combined `W24` passes.
* **Reconciliation-compatible component passes** only if the simultaneous 95% lower limit for `theta_Q` is at least 0.10 and the simultaneous lower limit for `B_Q` is at least 0.05.
* A component is **precisely absent/adverse** only if its simultaneous upper limit is below its corresponding 0.10 rate/contrast margin or 0.05 burden margin. Merely failing to pass is inconclusive.

This yields four prespecified interpretations when all quality gates pass:

1. race-compatible only: race component passes and reconciliation component is precisely absent;
2. reconciliation-compatible only: reconciliation component passes and race component is precisely absent;
3. both: both components pass;
4. neither: both are precisely absent; redirect study design toward alternate resolution, downstream tracking, or unobserved processes.

Every other combination is inconclusive rather than assigned to the more favorable mechanism.

## Positivity, overlap, adjudication, and uncertainty gates

Mechanism labels are prohibited unless all relevant gates pass:

* final adjudicated `N >= 200`;
* `U_R <= 5%` of otherwise eligible chains, and `A7/U_D7/U_T <= 5%` of frozen `N`; report each separately;
* for every chronology stratum used in a passing claim, at least 50 all-`N` opportunities, at least 40 `E7` artifacts, at least 15 `C7`, and at least 15 non-`C7` classifiable artifacts; otherwise only burdens/bounds are reported;
* for `J` standardization, every exact target stratum with positive `N` mass must have a control observation or the unsupported mass is reported. Required retained target mass is at least 0.80, effective sample size at least 100 in both target and weighted control, maximum stabilized weight no greater than 10, and no single stratum contributes more than 20% of total weight. No post-outcome merging repairs failure;
* for standardized `W24` versus `Q24` content comparisons, retained common-support mass must be at least 0.80, each chronology ESS at least 50, maximum stabilized weight no greater than 10, and standardized estimates must not reverse direction from crude estimates by 0.10 or more;
* reviewer raw agreement at least 0.85 and AC1/kappa at least 0.70 for eligibility, material chronology component, and `F/C_O/C_I/R`; a lower value is inconclusive;
* simultaneous 95% interval width no greater than 0.20 for each rate/contrast used in a mechanism label and no greater than 0.10 for each all-`N` burden difference used in a label.

Use a subject-cluster bootstrap with at least 10,000 replicates and a fixed seed, resampling the first-index subject unit. Construct max-|t| simultaneous 95% intervals over the predeclared family `{B_W,B_Q,B_P,B_T,theta_W,theta_Q,theta_P,theta_T,RACE,Gamma_W,Gamma_P,Gamma_Q,Delta_D,Delta_24,Delta_7}`. If bootstrap regularity fails because of sparse/zero cells, use simultaneous exact/Newcombe bounds where defined and declare mechanism selection inconclusive.

Compute worst-case partial-identification bounds by assigning every `A7/U_D7/U_T` opportunity in turn to `C7-W24`, `C7-Q24`, nonfailure, and alternate resolution subject to observed timestamp constraints. A mechanism conclusion must remain on the same side of its decision margins under these bounds; otherwise it is inconclusive. Missing storetime is never imputed from charttime.

## Locked falsification and sensitivity checks

All are reported regardless of direction:

1. `h=6,12,24,48` threshold curve plus continuous restricted cubic-spline plot of `Pr(C7 | E7)` against `min(X,Y)`; only `h=24` drives the decision.
2. `R_final` primary versus `R_intro` sensitivity. A material reversal indicates addendum-timing ambiguity and blocks mechanism selection.
3. `H7` primary mechanism table versus `H24`; the departure `D` state remains unchanged. A conclusion present only after choosing a later horizon is inconclusive.
4. Exact admission linkage versus the locked `admittime` and `admittime-12h` retrieval windows; `N` is not refrozen for favorable results.
5. Full `O/J` standardization versus deterministic exact `M` controls. Absolute reversal at least 0.02 for storage contrasts or 0.10 for content contrasts blocks specificity claims.
6. Permute nodule/control labels within exact pre-index strata; calibrated chronology differences must disappear except Monte Carlo error. Content labels are never permuted across patients as a substitute for clinical adjudication.
7. Report negative `L_RAD`, `X`, `Y`, extreme values, missingness, and integer boundary counts at exactly 0, 6, 12, 24, 48, and 168 hours. Run strict `<` versus inclusive `<=` boundary sensitivity; primary definitions above prevail.
8. Keep `C_O` and `C_I` separate. A signal produced only by interval wording ambiguity, with no actionable omission, cannot be called a general reconciliation failure.
9. Compare original-report and material-addendum opportunities. Sparse or opposite effects block a shared mechanism claim.
10. Preserve the parent's chest-report, non-chest due-window imaging, acute/nodule-focused CT, and later-observation negative controls. They cannot establish adherence.

## Secondary same-system observation outcome, unchanged

For every frozen `N`, calculate the exact calendar-month due date from the adjudicated 3/6/12-month recommendation plus 42 days. From `D`, classify mutually exclusively: same-system timely chest CT/CTA before interval-certain death; death before window without prior CT; no timely CT/death but later MIMIC radiology/admission trace; no later trace; or indeterminate CT/death ordering. Use `deathtime` when available and otherwise interval-censor `patients.dod` to `[00:00, +1 day)`. Artifact-timed `max(D,t_S)` is sensitivity only. State 3 is not adherence and state 4 is not nonadherence. Do not condition the mechanism denominator on later trace. Orders, referrals, appointments, outside imaging, communication, malignancy, treatment, and benefit remain unavailable.

## Supportive, adverse, and inconclusive results

* **Supportive for an observable race-compatible pattern:** all gates pass; the race component passes; the signal is stable across reasonable thresholds and `R_intro/R_final`; report lag does not explain it. If `Gamma_W` is near zero, interpret it as a generic institutional report-to-summary chronology pattern; if positive and stable, as nodule-enriched chronology. Either remains storage chronology only. A race-only result prioritizes prospective capture of report finalization, UI publication, discharge-summary draft/open/save/sign events, inbox acknowledgement, and departure time before evaluating an early trigger.
* **Supportive for reconciliation despite adequate observed separation:** all gates pass and the reconciliation component passes in `Q24`, robust to unknown bounds and controls. This prioritizes prospective content reconciliation, but it still does not prove the author saw the report or that reconciliation would improve care.
* **Supportive for both:** both components pass. A future intervention should factorially or sequentially separate timing alerts from content reconciliation; MIMIC cannot choose their causal contribution.
* **Adverse for one mechanism:** its confidence/bound upper limits are below the locked margins while the other mechanism passes. This is evidence against prioritizing that mechanism in this storage-based phenotype, not evidence that the real-world process never occurs.
* **Adverse for both:** both are precisely below margins. Retain the all-`N` state vector and investigate documented alternate resolution, downstream tracking, cross-system capture, or another handoff artifact.
* **Inconclusive:** sparse chronology cells, insufficient `N/events`, poor reviewer agreement, excessive `U_R/U_D/A7`, poor control overlap/ESS, unstable reciprocal links, chart/store conflicts, threshold or `R_intro/R_final` reversal, control reversal, wide intervals, or partial-identification bounds crossing a margin. Do not select a mechanism and do not relabel absence of evidence as faithful handoff.

## What verification can and cannot establish

An automatic verifier can check file hashes, archive members, schemas, row counts, source filters, exact keys, one-DS-per-key invariant, reciprocal link construction, `R_intro/R_final` adjudication-file lock, freeze order for `N`, timestamp arithmetic, chronology partition exhaustiveness, all-`N` state totals, boundary inclusivity, control pseudo-index selection, matching/standardization variables, positivity/ESS/weight diagnostics, bootstrap seed/replicate count, simultaneous intervals, partial-identification assignments, falsification outputs, and that the reported conclusion matches the four-state decision logic. It must reject conclusions that call `storetime` visibility, draft, signature, finalization, acknowledgement, transmission, receipt, or communication.

Clinical reviewers are required to determine incidental status, recommendation appropriateness, material addendum meaning, interval fidelity, actionable omission, and alternate resolution. Prospective timestamp/UI/communication evidence is required to identify real report visibility, authoring sequence, signing, acknowledgement, clinician/patient communication, and intervention target. External linkage or another study is required for outside imaging, surveillance completion, malignancy, treatment, causal benefit, and safety. No causal, adherence, or patient-benefit conclusion follows from this MIMIC experiment.
