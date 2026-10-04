# Final discharge-boundary experiment for incidental pulmonary-nodule recommendations

## Decision problem and substantive advance

An incidental pulmonary-nodule recommendation can fail to reach outpatient care through at least two distinct, actionable transition mechanisms: the canonical discharge artifact may not be observed as stored at the actual discharge boundary, or a canonical artifact observed by discharge may fail to preserve the patient-specific action and exact interval. These mechanisms nominate different prospective interventions. At the same time, MIMIC note `storetime` is an administrative availability marker, not proof of EHR visibility, signature, transmission, patient receipt, or actual physical departure; therefore it is unsafe to convert a delayed `storetime` directly into a clinical handoff failure.

This experiment resolves that tension by separating two questions rather than forcing them into one label:

1. **Primary clinically meaningful process question:** when a canonical discharge artifact is strictly observable by discharge and the recommendation was available before that artifact, was the adjudicated 3/6/12-month CT recommendation faithfully propagated?
2. **Co-primary operational decomposition:** over every established eligible recommendation opportunity, what fraction has no canonical artifact observed stored by discharge versus an artifact observed by discharge with failed recommendation content?

The first preserves content fidelity as the primary handoff outcome. The second keeps delayed/absent canonical artifacts in the unconditional opportunity set and can nominate a workflow target only after an external timestamp-validity gate. The design also retains an observation-aware downstream same-system CT outcome as secondary evidence; it never calls an absent MIMIC CT nonadherence or failed care.

### What is already supported

Published observational evidence supports a communication problem and the feasibility of tracking, not a causal benefit of discharge wording. Kwan et al. reported that 35/65 patients with explicit pulmonary-nodule follow-up suggestions lacked imaging in the recommended interval and found an association between discharge-summary mention and timely imaging (J Hosp Med 2019; PMID 30794133; PMCID PMC6625441). A tracking-program report observed follow-up imaging in 34/67 post-implementation versus 16/52 pre-implementation patients (J Digit Imaging 2023; PMCID PMC10287591). A systematic review found tracking systems promising but heterogeneous, with serious or critical risk of bias in most nonrandomized evidence (Chest 2025; PMID 40081655; PMCID PMC12264345). These public sources were inspected by the parent work as recorded there; they motivate measurement and prospective testing but do not establish recommendation appropriateness, communication, adherence, cancer benefit, or causality.

Complete-source parent audits establish computational feasibility only. They scanned all 2,321,355 radiology rows and found 1,291 broad lexical candidate reports, 1,241 with CT metadata, and 1,194 first candidate subjects. Among first candidates, 285 had a canonical discharge artifact stored by discharge, 770 by 24 hours, and 1,022 by seven days. In the prior +24-hour proxy cohort, counts were 403 faithful, 188 omitted, and 52 incomplete/discordant, with 3/6/12-month proxy strata of 234/135/274. These are not adjudicated clinical counts.

A complete 331,794-row discharge audit found exactly one `DS` row per discharge-note admission key and only 17 missing `storetime`. After joining to core admissions, 86,609 were stored by discharge, 147,800 at >0 to 24 hours, 76,977 at >24 hours to seven days, and 20,329 after seven days; 62 discharge keys lacked a matching core admission. Every linked delayed artifact in the 0–24-hour and 24-hour–7-day bands had `charttime <= dischtime`. Thus delayed `storetime` is common, but may reflect finalization/export or timestamp semantics rather than true clinical nonavailability.

## Falsifiable hypotheses and estimands

The unit is the first adjudicated eligible recommendation admission per subject, chosen without using discharge content or future outcomes.

### Primary content-fidelity hypothesis

Let `D0` be the subset with a resolvable pre-discharge report state, a qualifying recommendation first stored by `dischtime` and no later than the canonical discharge artifact, and a canonical artifact with known `storetime <= dischtime`. Define faithful propagation as an affirmed patient-specific pulmonary nodule, chest/thoracic CT action, and the same exact 3/6/12-month interval or an unambiguously equivalent due date.

Estimate

`p_F0 = P(faithful propagation | D0)`.

The prespecified operational quality hypothesis is that fidelity is below 80%. It is supported only if the upper two-sided 95% confidence limit for `p_F0` is below 0.80. The 80% value is an operational quality target, not an evidence-derived clinical standard. Omission, incomplete/discordant content, and explicit alternate resolution are reported separately; alternate resolution is not silently called success or failure.

### Co-primary all-opportunity mechanism decomposition

Let `N` include every first established eligible recommendation with a resolvable report/addendum state and qualifying recommendation-bearing state stored by `dischtime`, regardless of discharge-artifact timing. Partition `N` at the strict discharge boundary into:

- `A`: no canonical artifact observed stored by discharge, meaning the sole `DS` row has `storetime > dischtime`; this label is deliberately **observed storetime delay**, not proven clinical nonavailability;
- `C`: canonical artifact has known `storetime <= dischtime` and its content is omitted or incomplete/discordant;
- `F`: artifact is stored by discharge and faithfully propagates the recommendation;
- `R`: artifact is stored by discharge and documents an explicit alternate resolution;
- `U_D`: missing/unknown artifact time, absent or contradictory admission link, absent canonical text, or unreadable text.

These states are mutually exclusive and exhaustive over `N`. Report omission and incomplete/discordant components within `C`. An artifact stored before the first recommendation-bearing state cannot enter `D0`; in the all-opportunity decomposition it is a **stale-artifact sequencing subtype** of `C`, reported separately without implying that the writer had seen later information.

Estimate `p_A`, `p_C`, and the paired contrast `Delta = p_A - p_C = mean(A-C)` on the common denominator `N`. The directional operational hypothesis is `Delta > 0.05`. Nominate an artifact-finalization/availability intervention ahead of content insertion only if the simultaneous 95% lower confidence bound exceeds +0.05, all data/reliability/precision gates pass, unresolved-state bounds do not reverse the conclusion, and an independent site timestamp crosswalk validates that MIMIC-delayed artifacts were genuinely unavailable at departure. Nominate content insertion first only if the simultaneous 95% upper bound is below -0.05. Otherwise choose neither from point estimates; a bundled or 2-by-2 factorial prospective pilot is warranted. Report margins 0 and 0.10 as sensitivities. The five-point margin is an operational decision rule, not a patient-valued clinical threshold.

The primary content question remains reportable even if `storetime` fails as a visibility proxy, because it is explicitly conditional on strict observable artifact timing. The operational interpretation of `A` is falsified if local timestamp validation shows those artifacts were final and visible at departure.

### Secondary observation-aware hypothesis

Among all subjects with adjudicated content state `F` or omission and a canonical artifact known by `dischtime + 24 hours`, faithful propagation is associated with a higher all-eligible risk of a MIMIC-observed recommendation-timed chest CT than omission after prespecified baseline standardization. The null standardized risk difference is zero. This is a secondary same-system association, not adherence, care-loop closure, or causal benefit, and it cannot determine the primary workflow nomination.

## Exact snapshot and data bindings

Use MIMIC snapshot `[source checksum]` (core v3.1 and local note v2.1). Subject-specific date shifts preserve within-subject intervals but prohibit cross-subject calendar-era and interrupted-time-series claims.

### Radiology report/addendum state and imaging outcomes

1. `[internal dataset path]`, [source checksum], table `note/radiology`, columns `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`. Join to admissions on `(subject_id, hadm_id)`. Base `charttime` anchors examination timing and calendar-month due dates; `storetime` defines observable report-state availability. Full `text` supports candidate retrieval and blinded adjudication. Later rows supply same-system imaging outcomes and observation traces.
2. `[internal dataset path]`, [source checksum], table `note/radiology_detail`, columns `note_id, subject_id, field_name, field_value, field_ordinal`. Join on `(subject_id, note_id)` and retain all ordinals. `exam_name`, `exam_code`, and `cpt_code` classify index and outcome coverage. Reconstruct addendum links using both `parent_note_id` and `addendum_note_id`, never file order.

The complete audit found 25,735 unique reciprocal directed edges: 25,600 present, chronological, same-subject and same-admission `RR -> AR` pairs; 129 edges with both referenced nodes absent; three missing parents; and three missing addenda. For every candidate base `RR`, construct the connected component. At cutoff `t`, report state contains only the base and linked nodes with nonmissing `storetime <= t`. A cross-subject/admission edge, contradictory direction, missing required node, missing availability time, or nondeterministic cycle is unresolved report state `U_R`. Tabulate `U_R` in the unconditional screen cascade and report worst-case eligibility bounds; never recode it as failure. Addenda after discharge cannot redefine primary eligibility or content, but adjudicators separately tabulate whether they introduce, reinforce, negate, or change the interval.

### Canonical discharge artifact

3. `[internal dataset path]`, [source checksum], table `note/discharge`, columns `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`. Join on `(subject_id, hadm_id)`. The complete audit found 331,794 `DS` rows for 331,794 distinct discharge-note admission keys, so the sole `DS` row is the canonical artifact; there is no draft/version selection. `storetime` supplies strict observable timing, `charttime` only diagnoses timestamp discordance, and full `text` is authoritative for content. Never use `charttime` to back-impute availability.
4. `[internal dataset path]`, [source checksum], table `note/discharge_detail`, columns `note_id, subject_id, field_name, field_value, field_ordinal`. Join on `(subject_id, note_id)`. All 331,794 audited rows contain only `field_name=author` and masked `field_value=___`; this file provides neither author identity nor section structure. No heading or section-position hypothesis is allowed.

### Admission boundaries, death, and baseline descriptors

Read the following archive members from `[internal dataset path]`, [source checksum]:

- `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`: `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admit_provider_id, admission_location, discharge_location, insurance, language, marital_status, race, edregtime, edouttime, hospital_expire_flag`; join `(subject_id, hadm_id)`. `dischtime` is the sole confirmatory discharge boundary.
- `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`: `subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod`; join `subject_id`. Age is `anchor_age + year(admittime) - anchor_year`; represented age 91 means 90+.
- `mimic-iv-3.1/hosp/diagnoses_icd.csv.gz`, table `hosp/diagnoses_icd`: `subject_id, hadm_id, seq_num, icd_code, icd_version`, joined to `mimic-iv-3.1/hosp/d_icd_diagnoses.csv.gz`, table `hosp/d_icd_diagnoses`: `icd_code, icd_version, long_title`, on `(icd_code, icd_version)`. Freeze and title-audit lists for active/previous cancer, COPD/emphysema, immunosuppression, and tobacco-code availability before adjudicated outcomes are opened; absent tobacco coding is unknown, not nonsmoking.
- `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`: `subject_id, hadm_id, transfertime, prev_service, curr_service`; select the last `curr_service` at or before discharge.
- `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`: `subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime`; derive transition count and final care unit using records through discharge only.
- `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`: `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`; ICU exposure is a severity/transition descriptor, not a causal exposure.

## Population and exact temporal rules

Scan every radiology row; there is no row sampling. Lexical rules are high-sensitivity retrieval only, and every candidate is independently adjudicated.

Include:

- age at admission >=18;
- base CT linked to the admission by `(subject_id, hadm_id)` with `admittime - 12 hours <= charttime <= dischtime`;
- chest CT, CTPA/CTA, or abdominal CT including lung bases, classified from all detail fields with blinded text adjudication for ambiguous coverage;
- incidental pulmonary/lung nodule or indeterminate focal nodular pulmonary opacity; and
- affirmed, patient-specific, unconditional recommendation for chest/thoracic CT at exactly 3, 6, or 12 calendar months, present in a resolvable report state whose recommendation-bearing node has nonmissing `storetime <= dischtime`.

Exclude:

- scheduled lung-cancer screening or index imaging explicitly for nodule surveillance;
- lung-cancer staging/oncologic surveillance, known actively managed primary pulmonary malignancy, or a nonpulmonary nodule;
- conditional/optional recommendations dependent on unavailable risk, and explicit no-follow-up recommendations;
- hospice/comfort-only transition, in-hospital death, or recorded death by the relevant discharge-artifact ascertainment time;
- pre-boundary CT explicitly superseding or satisfying the recommendation; and
- unresolved report state from confirmatory denominators.

Do not require that the nodule is new, Fleischner-eligible, or guideline-concordant because morphology, longitudinal stability, smoking pack-years, and full clinical context are incomplete. Abstract size, type, multiplicity, new/changed/stable/unknown, and prior same-system imaging when stated.

Select the first eligible opportunity per subject by base `charttime`, then base `storetime`, then `note_id`, without discharge state or future outcome information. Repeat eligibility with a zero-hour admission boundary and an ED-window rule using `edregtime`/`edouttime`. Repeat key descriptive analyses among subjects with at least two years of prior same-system radiology trace.

Publish the complete cascade: all radiology rows; lexical candidates; CT metadata-confirmed candidates; adjudication disposition; `U_R`; established eligible `N`; recommendation available by discharge; discharge row/link/timing status; `A/C/F/R/U_D`; and entry into `D0` and the +24-hour downstream cohort. Provide interval and coverage counts before inference. Proxy audits calibrate workload only and never replace the adjudicated cascade.

## Blinded adjudication and content states

1. Two radiology-trained reviewers, blinded to discharge text and future outcomes, independently decide eligibility and abstract index coverage, incidental status, recommendation action, exact interval, certainty/conditionality, nodule size/type/multiplicity/newness, and the effect of each pre-discharge addendum.
2. Two transition reviewers, blinded to report text, exact recommendation, recommendation/discharge chronology, and future outcomes, independently review the sole canonical discharge text and abstract patient-specific nodule content, chest/thoracic CT action, interval or due date, responsible clinician/service if stated, and explicit alternate resolution.
3. Outcome reviewers, blinded to propagation state, classify later CT coverage and whether it is nodule-focused or acute/symptom-driven.
4. Lock both abstraction domains, then match fields algorithmically. Consensus or a third reviewer resolves every disagreement before analysis.

The mutually exclusive content states at a cutoff are:

- **faithful:** affirmed patient-specific pulmonary nodule, chest/thoracic CT, and the same exact 3/6/12-month interval or unambiguously equivalent calendar due date;
- **incomplete/discordant:** nodule without action, CT without usable timing, or a different action/interval without explicit alternate resolution;
- **omission:** no active patient-specific actionable nodule follow-up content;
- **explicit alternate resolution:** documented refusal/preference, goals-of-care choice, specialist takeover with a concrete alternative, already scheduled outside-system follow-up, or a documented clinical decision superseding CT.

Negated, historical, or family-history mentions, generic “follow up with PCP,” copied guideline boilerplate, and copied report prose without an active patient-specific plan are not faithful. Alternate resolution records documentation only; reviewers do not judge its correctness.

Report raw agreement, Gwet's AC1 with subject-bootstrap 95% intervals, and kappa for eligibility, exact interval, and four-state content. Confirmatory inference requires complete consensus resolution, raw agreement >=0.80, and AC1 >=0.70 in each domain. If a gate fails, revise the codebook and independently re-adjudicate affected records once; persistent failure restricts conclusions to reviewer-specific bounds. The automated screen must have sensitivity >=0.95 with lower 95% Wilson bound >=0.90. Automated content labels may not supply analysis outcomes unless relevant state-specific PPV is >=0.90 with lower bound >=0.80.

## Analyses and feasibility gates

### Primary content fidelity

In `D0`, report exact counts and simultaneous multinomial 95% intervals for faithful, incomplete/discordant, omitted, and alternate resolution. Report an exact binomial 95% interval for `p_F0`. Confirmatory threshold inference requires at least 200 members of `D0`; otherwise report descriptive exact bounds only. The below-80% hypothesis is supported only when the upper confidence bound is below 0.80. An interval crossing 0.80 is inconclusive, not evidence of adequate or inadequate quality.

As a planned secondary content estimand, repeat fidelity among canonical artifacts first observed by `dischtime + 24 hours`, while requiring the recommendation-bearing state to precede that artifact. This quantifies eventual canonical content without substituting +24 hours for the actual discharge boundary.

### All-opportunity paired decomposition

Report counts and risks for `A`, omission, incomplete/discordant, their union `C`, `F`, `R`, and `U_D`, all over `N`. Calculate `Delta` from paired indicators. Use 9,999 subject-level nonparametric bootstrap replicates with a fixed published seed. Construct a two-sided family-wise 95% max-|t| simultaneous interval across `p_A`, `p_C`, and `Delta`; if studentization fails or a component is zero, use a prespecified nonstudentized max-deviation bootstrap and report simultaneous multinomial score intervals as a check.

A dominance claim requires:

- `N >= 200`;
- at least 20 events in each of `A` and `C`;
- complete adjudication and screen gates;
- `U_D <=5%` of `N`; otherwise assign all unresolved cases first to `A` and then to `C` and require the conclusion to survive the resulting partial-identification range;
- simultaneous interval width for `Delta <=0.10` (half-width <=0.05); and
- the decision to remain unchanged under plausible `U_R` eligibility bounds.

Even if these pass, artifact-intervention language additionally requires the external timestamp-validity gate. Without that gate, the strongest claim is only that MIMIC does not record the artifact as stored by discharge.

Stratify paired risks descriptively by 3/6/12-month interval, chest/CTA versus lung-base coverage, artifact-before-versus-after-recommendation chronology, medical versus surgical final service, ICU exposure, care-transition count, and discharge destination. Before adjudication, feasibility is assessed from the full proxy audit. After adjudication, require >=40 subjects and >=10 events for any stratum-specific confidence interval; otherwise combine only clinically prespecified coverage categories or report counts without effect estimates. No data-dependent subgroup determines the primary decision.

### Exact delayed-artifact transitions

Reconstruct states at `dischtime`, `dischtime + 24 hours`, and `dischtime + 7 days` with immutable content from the sole artifact and exact `storetime` cutoffs. Publish individual-state transition matrices plus distributions of `charttime - dischtime`, `storetime - dischtime`, and `storetime - charttime`.

- An `A` case can transition to faithful, omitted, incomplete/discordant, alternate resolution, or remain not observed by the later cutoff.
- Later content is never treated as having existed before its `storetime`.
- Delayed artifacts that eventually contain failed content remain `A` in the strict decomposition to avoid double counting, but their eventual content is reported.
- Later radiology addenda are tabulated separately and cannot alter discharge eligibility.

A large `A` risk with rapid transition to faithful and `charttime <= dischtime` is compatible with export/signing latency or timestamp semantics; it is not evidence that clinicians or patients lacked instructions.

### Observation-aware downstream outcome

For the secondary cohort, time zero is `max(dischtime, discharge.storetime)`; no event at or before time zero is an outcome. Due date is base index `charttime +` adjudicated 3, 6, or 12 **calendar months**, using calendar arithmetic rather than 30-day approximations. Primary event is the first MIMIC chest CT/CTA with `charttime` in `[due - 42 days, due + 42 days]` and after time zero. Report +/-30-day and +/-90-day sensitivities. Blinded reviewers classify nodule-focused versus acute/symptom-driven CT. Also report any chest CT through `due+42` and CT occurring only during a later acute admission.

Assign one joint observation state by precedence:

1. MIMIC-observed recommendation-timed CT before recorded death;
2. recorded death before window end with no earlier timed CT, using `deathtime` or `dod <= due+42`;
3. no timed CT/death but a later MIMIC radiology event or admission after `due+42`;
4. no subsequent trace/unknown capture.

The all-eligible risk of state 1 is the secondary estimand. Restriction to state 3 is descriptive only because observability is post-exposure and may be a collider. Model continued trace as an outcome. Inverse-probability-of-observation results are sensitivity analyses under an explicitly unverifiable missing-at-random assumption, never replacements for the all-eligible estimate.

Contrast faithful versus omitted only; retain incomplete/discordant and alternate resolution descriptively. Report crude risk difference and ratio, exact interval-specific estimates, then overlap-weighted and regression-standardized risk difference/ratio only if all gates pass. Freeze before outcomes: interval, CT coverage, nodule size/type/newness, prior-year same-system chest CT and admission counts, age category, sex, cancer-history category excluding active staging, COPD/emphysema, ICU exposure, medical/surgical final service, length of stay, discharge destination, language, and insurance; repeat without language/insurance. Never include future addenda or post-exposure observation variables.

Adjusted inference requires >=50 faithful and >=50 omitted, >=15 timed CT events in each arm, >=90% of each arm in the prespecified propensity range 0.05–0.95 and empirical common-support intersection, overlap-weighted effective sample size >=40 per arm, no zero-exposure interval-by-coverage stratum of >=10, weighted absolute standardized mean difference <0.10 for every key covariate, and no separation or influential-weight pathology. If any gate fails, stop at crude and exact/parsimoniously stratified estimates and call adjustment inconclusive. Bootstrap intervals and limit degrees of freedom to available events. No result is causal because diligence, patient preference, outpatient relationships, orders/referrals, direct notification, and outside-system care are unmeasured.

The existing proxy evidence is deliberately preserved as a negative feasibility finding: continued same-system trace was 253/403 (62.8%) in proxy-faithful versus 99/188 (52.7%) in proxy-omitted subjects; among trace-positive subjects, timed CT was 44/253 (17.4%) versus 16/99 (16.2%), and any chest CT was 77/253 (30.4%) versus 30/99 (30.3%). In all proxy-gated subjects, timed CT was 49/403 (12.2%) versus 17/188 (9.0%). This provides no compelling crude evidence of improved surveillance and warns against observed-only conditioning.

## Falsification and stopping rules

1. **Timestamp-validity gate:** before an artifact-finalization intervention is recommended, a prospective site audit must crosswalk MIMIC `storetime`, authoring/signature/finalization time, UI visibility, patient-release/transmission time, and actual departure. If purportedly delayed artifacts were already final and visible at departure, the workflow-availability interpretation is falsified; the MIMIC finding then nominates timestamp/data-pipeline validation, not a clinical intervention.
2. **Strict versus eventual content:** compare `D0` with +24-hour and +7-day transition states. If most delayed artifacts rapidly become faithful, do not describe their strict delay as a content failure. If delayed artifacts remain absent or eventually have failed content, report coexistence but do not double count.
3. **Chronology challenge:** split available-artifact content states by artifact `storetime` before versus after first recommendation-bearing `storetime`. Failure concentrated in stale artifacts supports an update/reconciliation trigger rather than generic author education.
4. **Alternate-resolution challenge:** if most nonfaithful available artifacts contain documented alternate resolution, the data do not support automated content insertion.
5. **Unresolved bounds:** if assignments of `U_D` or plausible eligible `U_R` cases reverse either the 80% fidelity interpretation or `Delta` decision, that result is inconclusive.
6. **Boundary sensitivity:** repeat with zero-hour and ED-window eligibility. A reversed mechanism decision indicates boundary-dependent retrieval, not a stable workflow target.
7. **Temporal placebo:** chest CT in an 84-day window centered on `index charttime - recommendation interval`, before discharge content could act. A same-direction standardized association at least as large as the surveillance association indicates baseline utilization/team selection, extraction error, or residual confounding.
8. **Generic-utilization control:** recommendation-window non-chest radiology. A comparable association indicates general same-system engagement rather than nodule-specific action.
9. **Differential observation:** continued same-system trace after window end is an outcome. A large content association warns that capture differs by arm.
10. **Mechanism specificity:** nodule-focused timed CT must be at least as directionally supportive as any chest CT. A result driven by acute/non-nodule CT does not support a recommendation-handoff mechanism.
11. **Retired heading branch:** only six prior proxy-gated cases had a dedicated recommendation heading, and discharge detail has no section fields. No heading mechanism may be revived.

A downstream result is not supportive if placebo or generic-utilization differences are at least as large in the same direction, acute CT drives the estimate, observation differs materially, or accuracy/event/positivity gates fail.

## Interpretation matrix

### Primary content result

- **Supportive of a content gap:** the upper 95% bound for `p_F0` is <0.80, a material fraction is omission/incomplete rather than alternate resolution, and all agreement/sample/unresolved gates pass. This establishes an observable report-to-canonical-discharge content gap among strictly timed artifacts and justifies prospective testing of interval-specific reconciliation. It does not establish recommendation appropriateness, patient receipt, or benefit.
- **Adverse to a content-target hypothesis:** faithful propagation is >=0.90 with lower bound >0.80, or apparent failures are predominantly alternate resolutions. Content insertion is unlikely to be the principal observable discharge bottleneck.
- **Inconclusive:** confidence interval crosses 0.80, `D0<200`, unresolved bounds reverse the result, or agreement fails. Report only the cascade and descriptive dispositions.

### Mechanism selection

- **Observed delay statistically dominates and timestamp validity passes:** simultaneous lower bound for `Delta > +0.05`, gates/bounds pass, and a site crosswalk confirms genuine nonavailability. First test a discharge-time canonical-artifact finalization/availability check, while measuring true visibility/transmission. Do not claim patients lacked all instructions or that finalization improves outcomes.
- **Observed delay statistically dominates but timestamp validity fails or is unavailable:** conclude only that MIMIC `storetime` records delay. Validate the data pipeline; do not nominate a clinical availability intervention.
- **Content statistically dominates:** simultaneous upper bound for `Delta < -0.05`, content is not mostly alternate resolution, and gates pass. First test structured report-to-discharge action/interval reconciliation, including a stale-artifact update trigger.
- **Neither dominates or precision/bounds fail:** obtain more adjudication/mechanism data or test a bundled/2-by-2 factorial workflow. Never select from point estimates.
- **Both components low and precise:** these discharge-EHR mechanisms are unlikely to be the main bottleneck; prospective tracking, scheduling, patient communication, or cross-system exchange may be more consequential.

### Secondary outcome

- **Supportive association:** adjusted faithful-minus-omitted all-eligible risk difference for preferably nodule-focused timed CT is >0 with interval excluding zero; all gates pass; observation imbalance does not explain it; and negative controls are smaller/nonsupportive. This motivates a randomized or stepped-wedge workflow study, not a causal conclusion.
- **Adverse:** an adequately precise risk difference is <=0, or association exists only for acute/non-nodule CT. Documentation alone may be ineffective or accompany low-value imaging.
- **Inconclusive:** interval spans -0.10 to +0.10, arm/event/overlap/accuracy gates fail, observation differs materially, or controls are positive. The upstream process results remain independently reportable.

## Verification boundary and additional evidence required

An automatic verifier can check source hashes, archive members, schemas, joins, reciprocal chain reconstruction, exact `storetime` cutoffs, one-artifact-per-admission logic, first-subject selection, calendar-month arithmetic, mutually exclusive state assignment, common denominators, delayed-state transition matrices, agreement/screen/sample/event/overlap/precision gates, partial-identification bounds, confidence intervals, negative controls, and whether conclusions follow from computed outputs.

Clinical experts must establish incidental status, unconditionality, exact interval, addendum meaning, CT coverage, faithful propagation, discordance, alternate resolution, and nodule-focused outcome classification. Neither code nor MIMIC can establish guideline appropriateness, true pathology, complete smoking exposure, what clinicians or patients saw, discussion or receipt, order/referral/appointment completion, outside imaging, actual departure, undocumented preferences, cancer outcomes, radiation harm, survival benefit, or intervention causality. Stronger claims require a local timestamp/visibility audit, linked outpatient and outside-system data, expert review, and a prospective randomized, factorial, or stepped-wedge study.
