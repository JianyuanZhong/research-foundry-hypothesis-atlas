# Executable two-phase actionability audit with fixed atom allocation and a closed workload ledger

## Targeted repair and unchanged scientific question

This child preserves the frozen design of `[prior hypothesis]`. The population remains the first eligible adult admission per subject in the complete all-opportunity pulmonary frame; the reciprocal pre-departure radiology report/addendum chain, one canonical exact-`DS` discharge artifact, unit-specific storage chronology, exhaustive `Y/V/H/Z` states, final support atoms, split evidence views, independent holistic challenge, all-unit worst-case admission routing and precedence, support-atlas/no-rescue logic, finite-population inference, and strict noncausal evidence ceiling are unchanged. The inherited master probability sample still contains at most 900 distinct admissions. No control clone, packet rendering, reviewer assignment, or repeat reading creates another sampled admission.

The decision remains whether an exact support-qualified MIMIC atom-route signature may be nominated only for a prospective within-site silent validation. MIMIC can show whether stored text reproducibly contains an explicit target-linked action and whether stored text contains an explicit target-linked superseding plan. It cannot establish clinical appropriateness, actual viewing, physical departure visibility, responsibility, communication, order/referral execution, scheduling, safety, benefit, or causality.

The strongest evidence available before this experiment is that the frozen admission frame, reciprocal chronology, canonical discharge artifact, service/ICU workflow proxies, recommendation units, and final support atoms are computable from the bound MIMIC snapshot. The unresolved and falsifiable claim is that at least one otherwise releasable atom-route signature remains within the inherited adverse contamination margin after route-concealed active-action and supersession measurements are applied to every recommendation unit. A pass supports only nomination for prospective silent validation. A failure blocks the affected atom; it does not prove harm or clinical inappropriateness.

This successor repairs five compilation weaknesses without changing that question: it replaces the ambiguous largest-remainder challenge instruction with a total algorithm and a prespecified universally feasible fallback; separates pre-label atom allocation from post-seal route support; records phase-specific first- and second-order inclusion probabilities; defines exactly what a whole-admission reading and a control reading are; and removes newly introduced numerical agreement, case-count, control-error, missingness, and hour thresholds from nomination. The inherited sample size of 300 is retained honestly as a resource/governance cap, not presented as a clinical or precision threshold.

## Immutable data bindings

Use snapshot `[source checksum]`, with source data read-only and all manifests, samples, packets, labels, and results written in the workspace.

The structured source is `[internal dataset path]`, [source checksum]:

* archive member `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`, schema [source checksum], columns `subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admit_provider_id, admission_location, discharge_location, insurance, language, marital_status, race, edregtime, edouttime, hospital_expire_flag`; key `(subject_id,hadm_id)` and frozen departure proxy `D=dischtime`;
* member `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`, schema [source checksum], columns `subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod`; join on `subject_id`, using only the inherited widened possible-calendar class and never treating shifted years as actual dates;
* member `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`, schema [source checksum], columns `subject_id, hadm_id, transfertime, prev_service, curr_service`; join on `(subject_id,hadm_id)`, use only rows with `transfertime<D`, and derive terminal `curr_service` exactly as inherited;
* member `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, schema [source checksum], columns `subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime`; diagnostics only under the inherited rules;
* member `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`, schema [source checksum], columns `subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los`; join on `(subject_id,hadm_id)` and use admission-linked `intime<D` for the inherited ICU workflow class.

The note sources are ordinary compressed files:

* `[internal dataset path]`, [source checksum], table `note/radiology`, schema [source checksum], columns `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`, admission join `(subject_id,hadm_id)`, note key `(subject_id,note_id)`;
* `[internal dataset path]`, [source checksum], table `note/radiology_detail`, schema [source checksum], columns `note_id, subject_id, field_name, field_value, field_ordinal`, joined only on `(subject_id,note_id)`, retaining every ordinal and reciprocal `parent_note_id`/`addendum_note_id` field row;
* `[internal dataset path]`, [source checksum], table `note/discharge`, schema [source checksum], columns `note_id, subject_id, hadm_id, note_type, note_seq, charttime, storetime, text`; select exact `note_type=='DS'` and the inherited sole canonical `(subject_id,hadm_id)` artifact;
* `[internal dataset path]`, [source checksum], table `note/discharge_detail`, schema [source checksum], columns `note_id, subject_id, field_name, field_value, field_ordinal`, joined on `(subject_id,note_id)`.

POE and `poe_detail` remain prohibited from the frame, packets, labels, controls, routes, atoms, estimands, and gates.

## Master draw and exact 300-admission nested allocation

Let `M` be the already frozen inherited master draw after sentinel handling and the five inherited outcome-blind sampling strata. Its realized distinct-admission count is `n=|M|<=900`; preserve the inherited stratum sample-size formulas, seeds, sampling probabilities, route-independent review, and `NO_SELECTION` rule if those formulas would exceed 900. Do not redraw `M` for this child.

Before generating packets or exposing any admission to any reviewer, construct each admission's inherited final atom

`g=(widened possible-calendar class, terminal pre-D curr_service including UNKNOWN, inherited workflow class including UNKNOWN)`.

Let `N_g` be the number of master admissions in occupied atom `g`, let `m=min(300,n)`, and freeze protocol seed `ACTSUP-v2`. The nested actionability sample `C` is selected once as follows.

1. If `n<=300`, take a census: `C=M`, `m=n`.
2. If `n>300`, calculate the coverage base `b_g=1` when `N_g=1` and `b_g=2` when `N_g>=2`; let `B=sum_g b_g`.
3. **Covered stratified mode:** if `B<=300`, set residual capacity `c_g=N_g-b_g` and `R=300-B`. If `sum_g c_g=0`, necessarily `R=0`. Otherwise calculate `q_g=R*c_g/sum_h c_h`, set `a_g=floor(q_g)`, and award the remaining `R-sum_g a_g` slots to atoms in descending fractional remainder `q_g-floor(q_g)`. Break exact ties by ascending SHA-256 of `ACTSUP-v2 || canonical_atom_string(g)`. Set `m_g=b_g+a_g`, verify `sum_g m_g=300` and `b_g<=m_g<=N_g`, then draw an SRS without replacement of `m_g` admissions within every atom using ascending SHA-256 of `ACTSUP-v2 || subject_id || hadm_id` as the frozen random ordering.
4. **Global fallback mode:** if `B>300`, do not merge atoms, choose atoms, or declare the entire audit infeasible. Draw one SRS without replacement of 300 admissions from all of `M`, ordered by ascending SHA-256 of `ACTSUP-v2 || subject_id || hadm_id`. This fallback is determined solely by the sealed pre-label frame. It gives every admission and every admission pair positive challenge probability, while honestly relinquishing guaranteed atom coverage. An atom absent from `C` is unsupported and remains `DEFER`; no top-up is allowed.

This algorithm is total for every `1<=n<=900`. It never uses a route because routes are unavailable until all inherited and added component labels are sealed. Consequently, no compiler may promise a route-specific count. The realized atom counts and later realized route counts are outcomes of the probability design, not quotas.

For every master admission, store `phase2_mode`, `N_g`, `m_g` where applicable, the hash priority, selection flag, and conditional first-order probability:

* census: `pi2_i=1`;
* covered stratified mode: `pi2_i=m_g/N_g`;
* global fallback: `pi2_i=300/n`.

For every pair needed by variance or verification, store or deterministically regenerate the conditional second-order probability:

* census: `pi2_ij=1`;
* covered mode, same atom with `N_g>=2`: `pi2_ij=m_g(m_g-1)/(N_g(N_g-1))`; different atoms: `pi2_ij=pi2_i*pi2_j`;
* global fallback: `pi2_ij=300*299/(n*(n-1))`.

The coverage base ensures `pi2_ij>0` for every extant within-atom pair in covered mode; singleton atoms contain no within-atom pair. Record the inherited phase-1 `pi1_i` and `pi1_ij` separately. Use sequential two-phase analysis weights `1/(pi1_i*pi2_i)` and the inherited cluster/stratum identifiers. Do not misleadingly call the realized product an unconditional marginal probability when `pi2` depends on the realized master frame. Design replication must reproduce the inherited phase-1 replicate factors and, inside each replicate, the applicable phase-2 census/stratified-SRS/global-SRS factor. The existing 20,000-replicate max-statistic family remains frozen; all labels for an admission travel together.

## Route support after sealing, without route-enriched sampling

Pre-label atom support remains exactly the inherited support atlas. Post-seal atom-route support is a separate estimability condition and cannot be manufactured by sampling on a derived route. For every final atom `g` and route `r`, publish the master route count, challenged route count, phase-specific weights, weighted route denominator, effective sample size as a diagnostic, and simultaneous interval endpoints.

An atom-route can proceed to its inherited release test only if all of the following computability statements are true: the atom was support-qualified before labels; at least one challenged admission contributes positive weight to the adverse-compatible route denominator; the denominator and every required worst-unit numerator are defined; the simultaneous adverse-compatible interval can be computed; all required packets and controls have determinate ledger states; and the resulting upper endpoint lies on the passing side of the already inherited route-specific contamination margin. There is no new `30 admissions`, `10 challenged admissions`, or other case-count gate. A zero challenged route count, zero denominator, undefined ratio, nonpositive denominator lower endpoint, or interval too wide to decide is `INCONCLUSIVE -> DEFER`, never evidence of purity. No pooled route, adjacent atom, macro-service group, sentinel result, imputation, shrinkage, favorable consensus, or latent-class estimate can provide route support.

## Packet manifest, readings, and roster constraints

For each challenged admission, the packet generator enumerates every inherited recommendation unit once and writes one admission manifest containing the ordered unit IDs, source note IDs, source spans, allowed timestamps, hashes, explicit missingness tokens, and the canonical `DS` ID. Distinct target/action/timing units remain distinct; duplicate restatements remain one unit under the inherited unitization rule. Every human reading covers the whole manifest and must return one row for every unit, including `UNKNOWN/INDETERMINATE`; a reading is not complete merely because one salient unit was labeled.

The four core views remain frozen, but their names are made collision-safe:

* `ACT-A1`: the route-concealed active-action view with the permitted reciprocal pre-`D` radiology chain, permitted admission/death/disposition context, canonical `DS`, and permitted discharge detail. It records target, requested action, timing, recipient, responsibility language, polarity, departure-artifact status, and a compatible set over the inherited exhaustive actionability categories.
* `ACT-A2`: independently rendered and independently ordered from the same allowed raw evidence, using independently written `CB-A2`. It never displays `ACT-A1` fields or any inherited component label.
* `ACT-S1`: a separately rendered supersession view retaining recommendation wording and target-linked plan spans but displaying no route, stratum, atom, weight, or A1/A2 output. It returns a compatible set over `S0_NONE`, `S1_EXPLICIT_REPLACEMENT`, `S2_EXPLICIT_ALTERNATIVE_INCOMPLETE`, `S3_COMPETING_CONTRADICTORY_PLANS`, and `S4_UNKNOWN`.
* `ACT-H3`: after A1, A2, and S1 append-only seals exist, a fourth mutually disjoint roster independently reads a whole-admission raw-evidence rendering and records its own support/contradiction/indeterminate fields. It is not shown the sealed A1/A2/S1 assertions; locked code compares the independent fields only after the H3 seal. H3 is a measurement system, not an oracle.

All four added rosters are mutually disjoint and disjoint from every inherited development, split-view, and holistic roster. Freeze roster IDs, assignments, packet generator version, source-span manifest hashes, codebook hashes, queue order, and seal dependency graph before the first opening. Reviewers see no route, atom, sampling stratum, inclusion probability, expected control answer, post-`D` text, POE content, clinical outcome, or other panel output. Administrative replacement is permitted only before the original assignee opens the packet and must be recorded in a pre-opening append-only amendment; after opening, no replacement or consensus reading is allowed. Missing output remains missing and enters compatible sets adversely.

The inherited actionability and supersession categories, dominance of explicit supersession, locked compatibility table, and route precedence are unchanged. Added labels may only leave the inherited route unchanged or make it more conservative. No reviewer votes on a route.

## Closed workload ledger

A **whole-admission packet reading** is one assignment of one core view for one challenged admission to one reviewer, including review and labeling of every recommendation unit in that admission. Reopening by the same assigned reviewer during the permitted session does not add a reading; assignment to another reviewer does. Unit count, page count, and note count do not multiply the reading count, but are recorded as burden covariates.

There are exactly four planned core readings per challenged admission: one each for `ACT-A1`, `ACT-A2`, `ACT-S1`, and `ACT-H3`. Therefore the added core workload is exactly `4m`, which is 1,200 whole-admission readings when `m=300`, not 900. The parent's 900-reading phrase omitted the separate S1 reading and is superseded by this ledger. This correction changes no sampled admission, packet evidence, roster firewall, or scientific estimand.

Each challenged admission also generates exactly six linked control-pair assignments:

1. one formatting/section-order/nuisance-token invariance pair for the A1 assignee;
2. the independently rendered equivalent invariance pair for the A2 assignee;
3. one one-field route-decisive replacement-or-timing pair for the A1 assignee, with replacement versus timing selected by the frozen hash;
4. the independently rendered equivalent decisive pair for the A2 assignee;
5. one target-linked-plan versus wording/provenance-matched non-target-plan pair for the S1 assignee;
6. one masked/inserted recommendation-or-plan compatibility-transition pair for the H3 assignee, with recommendation versus plan selected by the frozen hash.

A **control-pair assignment** consists of two standalone redacted cards placed at independently hashed positions in that reviewer's queue; the reviewer is not told they form a pair or which card is modified. Thus the added control workload is exactly `6m` linked pair assignments and `12m` card exposures: at `m=300`, 1,800 control-pair assignments and 3,600 individual card exposures. These are not whole-admission readings and may not be reported as such. Each pair is derived only from its own challenged admission, so controls add zero distinct admissions. Automated packet construction, hashing, and schema QA are machine tasks, not reviewer readings.

The complete added ledger is therefore `4m` whole-admission readings plus `6m` linked control-pair assignments (`12m` card exposures), in addition to the immutable inherited parent workload. The compiler must output both the inherited ledger and this added ledger, their sum by reviewer roster, and the union of distinct `hadm_id`; the latter must equal `n<=900`. Record elapsed open-to-seal minutes, number of source spans, number of units, and physician versus nonphysician roster hours, but those measurements are feasibility outputs rather than nomination thresholds. There is no ungrounded 95th-percentile hour budget. A protocol cannot create extra readings to repair disagreement, missingness, or failed controls. If staffing cannot complete the frozen ledger, affected labels are missing and the corresponding atom-route is inconclusive or adverse under the locked bounds.

## Auditable governance rule and controls

The numerical additions in the parent—minimum 30/10 counts, agreement `>=0.90`, added route-discordance values `0.05/0.10`, control-error values `0.02/0.05`, missingness `0.05`, and a 95th-percentile hour threshold—have no external clinical justification in MIMIC. This child does not reinterpret them as safety thresholds. They may be displayed in a clearly labeled operational-screening sensitivity table so prior work remains auditable, but they cannot nominate or rescue an atom.

Nomination instead uses a closed rule tied to the frozen routing decision:

1. Locked code forms every unit's adverse-compatible actionability/supersession set from A1, A2, S1, and H3, then applies the inherited Cartesian-product route table and precedence.
2. For each admission, the most conservative compatible unit controls. Define `B=1` when any compatible added-label assignment would move the inherited route to a more conservative route, or when a required route decision is indeterminate; otherwise `B=0`.
3. Estimate the atom-route adverse mass of `B`, together with inherited contamination and workload endpoints, using the two-phase weights and the inherited simultaneous 95% max-statistic family. Unknown, disagreement, missing packet, and unresolved unit states enter the adverse endpoint. Agreement and kappa are descriptive only.
4. The atom-route is eligible only if every inherited support/reproducibility/contamination gate still passes and the simultaneous upper endpoint for added-label adverse re-routing passes the same inherited route-specific contamination margin. This reuses the frozen decision margin rather than inventing a second actionability margin. The inherited stronger rule remains: an `AUTO` atom with any observed adverse-compatible unresolved or superseded unit is blocked regardless of its weighted interval.
5. All other signatures, including absent challenge atoms, route-unsupported atoms, novel/unknown atoms, and any atom with an undefined endpoint, default to `DEFER`.

Controls are deterministic protocol falsification fixtures, not estimates of clinical performance. Before review, locked code records the exact allowed compatibility-set transition for every card pair. Formatting/nuisance pairs must preserve unit inventory and compatibility set; decisive pairs must exhibit only the transition listed by the inherited table; target-linked versus non-target plans must differ only in target linkage; mask/insert pairs must exhibit their frozen transition. A rendering diff outside the allowed token/span map invalidates the packet-generator version before review. After review, any missing control card or any response outside its frozen allowed transition blocks the corresponding panel-codebook-atom from nomination. There is no tolerated error percentage and no averaging across atoms. This strict rule is a governance screen for execution integrity, not evidence that a human interpretation is clinically correct. Passing controls cannot rescue a real-case adverse result.

Append-only seals must prove the order: raw extraction and reciprocal links; master frame and atoms; nested sample and probabilities; packet and control manifests; codebooks/rosters/queues; A1/A2/S1 labels; H3 labels; locked joins and route derivation; analysis. Route derivation before all seals, packet leakage, roster collision, post-label control creation, favorable unknown assignment, unlogged extra reading, or prohibited POE use invalidates the affected run.

## Estimands, analysis, and verification

Retain every inherited unit- and admission-level estimand, `C_AUTO`, `D_MIX`, route discordance, capture, workload, worst-unit routing, exact finite-population calculations, and 20,000 Rao-Wu/max-statistic simultaneous family. Add, by final atom and route, design-weighted totals and ratios for each actionability category, each supersession category, adverse-compatible re-routing `B`, explicit replacement, unknown/missingness, control validity, packet burden, and reading time. Publish numerator and denominator totals rather than percentages alone.

For nested endpoints, combine inherited phase-1 replicate factors with the correct phase-2 stratified-SRS or global-SRS replicate factors; keep all units and all four panel outputs for an admission together. Compare implementation against direct Sen-Yates-Grundy variance calculations using the recorded phase-2 first- and second-order probabilities on small fixtures. Exact finite-population inversion remains where inherited and mathematically applicable; do not label a bootstrap interval exact. If the simultaneous procedure cannot represent both phases, return `INCONCLUSIVE` rather than substituting an independence model.

Mandatory synthetic verification fixtures are: `n<300` census; exactly `n=300`; covered mode with fractional-remainder ties; singleton atoms; `B=300`; `B=301` invoking global fallback; an atom absent under global fallback; zero challenged cases for a post-seal route; same-atom and cross-atom probability checks; hashes reproduced under row permutation; all-unit admission precedence; duplicate-restatement versus distinct-unit behavior; shared-wrong A1/A2 labels not narrowed by agreement; one high-weight missing packet widening the adverse bound; a superseded AUTO unit blocking its atom; every one of the six control-pair types; a roster collision; route derivation before seal; and an extra reviewer assignment. Verification must assert `|M|<=900`, `C subseteq M`, `|C|=m`, no duplicated `hadm_id`, exact workload equations, and zero control admissions outside `M`.

Computationally checkable claims are source/schema hashes and columns, joins, chronology fields, reciprocal links, canonical `DS`, frame/sample membership, atom construction, seeds and hashes, first- and second-order phase probabilities, packet manifests, roster disjointness, seal order, exhaustive labels, locked route mapping, weights, workload counts, controls, intervals, and whether each stated atom passes the frozen rule. Clinical appropriateness, actual viewing, finalization/signature semantics, workflow execution, communication, responsibility, preferences, outside plans, safety, benefit, causality, and temporal or external transport are not computationally adjudicable from MIMIC.

## Supportive, adverse, and inconclusive interpretation

A supportive result is an exact allow-list of support-qualified atom-route signatures for which the inherited gates, deterministic control checks, two-phase adverse-compatible actionability bound, and all-unit precedence pass. It supports only a separately approved prospective actual-calendar silent validation of those signatures. It does not authorize a live route or clinical action.

An adverse result occurs when a supported atom's upper bound crosses the inherited decision margin, an observed unresolved/superseded unit blocks AUTO, a deterministic control transition fails, or a more conservative route is required. It blocks that atom under this protocol but does not establish patient harm or that the superseding plan was clinically correct.

An inconclusive result includes absent atom or route support, zero or unstable denominator, wide simultaneous bounds, global-fallback undercoverage, incomplete packets, unavailable staffing, broken seals, invalid variance implementation, or any other condition that prevents the frozen rule from being computed. Inconclusive always maps to `DEFER`; it is not evidence of safety. No adaptation, top-up, threshold relaxation, neighboring-atom borrowing, or favorable consensus is permitted.

Any stronger conclusion requires a prospective actual-calendar study with direct logs of note availability, signatures/finalization, viewing, edits, transmission, responsible team, target-linked orders/referrals, scheduling, outside plans, patient preferences, follow-up, outcomes, and predefined safety/utility governance, followed by expert review. MIMIC alone cannot supply those data.
