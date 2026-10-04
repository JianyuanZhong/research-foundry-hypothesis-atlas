# Target-specific interval semantics with observation-process calibration for departure-status validity

## Decision question and substantive repair

The inherited decision remains whether any exact MIMIC pulmonary-opportunity atom may be nominated only for a prospective within-site **silent** workflow validation of the inherited `AUTO`, `RECON`, `TIMING`, and `DEFER` routes. This child preserves the frozen first-eligible adult admission per subject, all-opportunity denominator, reciprocal pre-departure radiology reconstruction, canonical discharge (`note_type==DS`), unit-specific clock, exhaustive `Y,V,H,Z` states, exact support atoms, five strata, positive first- and second-order sampling probabilities, at-most-900 distinct admissions, all-unit worst-case routing, adverse-compatible inference, default-DEFER/no-rescue rules, and strict noncausal ceiling.

The parent [prior hypothesis] repairs an important departure-reference problem with two roster-disjoint readings and explicit firm, incomplete, tentative, completed, superseded, inactive, conflict, and unknown states. Its remaining limitation is that a target may be judged “grounded” and an interval “present” without testing whether the discharge action actually refers to the same radiology finding and whether its timing is semantically compatible with the source recommendation. Generic phrases such as “follow-up as clinically indicated,” copied text, a changed laterality or modality, and a changed interval can be lexically similar while representing different actions. A second limitation is observation-process ambiguity: `charttime` and `storetime` describe documentation and repository timing, not clinician viewing; missing or delayed artifacts do not show absence of care.

The substantive repair is a **presealed, target-specific semantic interval ledger coupled to an observation-opportunity ledger**. It tests the falsifiable claim that at least one inherited support-qualified `AUTO` or `RECON` atom remains admissible after every challenged recommendation is matched to a discharge action using independently preserved target/action fields and interval relations, and after every apparent absence or temporal conflict is separated into observed evidence, delayed storage, missingness, linkage ambiguity, administrative censoring, or unknown observation opportunity. This is not a longitudinal persistence endpoint and does not treat later same-system text as clinical truth. It directly tests whether the departure text denotes the same target and planned timing as the reciprocal source chain.

The strongest claim supported before this child is only that available pre-departure artifacts contain an apparently target-grounded future-directed textual action under the parent's reference ledger. This child tests whether that apparent match survives explicit semantic identity and interval compatibility rules and whether the observation process permits a valid adverse statement. It cannot establish that the action was appropriate, viewed, assigned, communicated, ordered, scheduled, executed, completed, beneficial, safe, or clinically live at departure.

## Immutable inherited population, chronology, and route contract

Use MIMIC snapshot `[source checksum]`, with all source files read-only. Preserve without reinterpretation:

* complete first eligible adult admission per subject and the all-opportunity denominator;
* reciprocal pre-`D` radiology report/addendum reconstruction, exact one canonical `note_type==DS` artifact per admission, and `D=dischtime`;
* unit clock `G_u=DS_store-R_store,u`, stale and post-departure distinctions, and exhaustive `Y,V,H,Z` states;
* pre-label atom `g=(possible-calendar class, terminal curr_service, workflow class)`, five strata, sentinel census, inherited sample-size formulas, and positive inclusion probabilities;
* every recommendation unit, no unit splitting or omission, no top-up, replacement, atom merging, post-label enrichment, or route-triggered verification;
* all-unit worst-case admission routing and inherited route precedence;
* at most 900 distinct admissions in the entire inherited design plus the fixed parent challenge workload; and
* adverse-compatible finite-population inference with exact finite-population inversion, joint admission clustering, 20,000 Rao-Wu replicates, one simultaneous 95% max-statistic family, and default `DEFER` for unresolved or unsupported cases.

`POE` and `POE_DETAIL` are prohibited from population construction, packets, labels, references, routes, and gates. The semantic and observation layers add no sampled admissions. They process every admission in the inherited actionability challenge, normally at most 300, and cannot create a new opportunity or alter `R_store,u`, `D`, the route, or the support atom.

## Exact source bindings

Bind the read-only core archive `[internal dataset path]`, [source checksum], including:

* `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`, schema `table-e8ec3e6e4c428559.json`, columns `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`, key `(subject_id,hadm_id)`, with `D=dischtime`;
* `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`, joined on `subject_id`, using only the inherited widened possible-calendar class and never treating shifted calendar years as exact real dates;
* `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`, columns `subject_id,hadm_id,transfertime,prev_service,curr_service`, joined on `(subject_id,hadm_id)`, with only `transfertime<D` rows contributing terminal service;
* `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, columns `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`, diagnostics only; and
* `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`, columns `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`, with admission-linked `intime<D` defining inherited ICU exposure only.

Bind `[internal dataset path]`, table `note/radiology`, schema `table-1ffcd77c4cbdaeda.json`, [source checksum], columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`, identity `(subject_id,note_id)`, admission join `(subject_id,hadm_id)`, and time fields `charttime,storetime`.

Bind `[internal dataset path]`, table `note/radiology_detail`, schema `table-2972dbfe5cb661c0.json`, [source checksum], columns `note_id,subject_id,field_name,field_value,field_ordinal`, joining only on `(subject_id,note_id)`, retaining all ordinals and reciprocal `parent_note_id`/`addendum_note_id` fields. It supplies document lineage/provenance only; it has no temporal columns and cannot create an opportunity.

Bind `[internal dataset path]`, table `note/discharge`, schema `table-69be322e2b58015b.json`, [source checksum], columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`, identity `(subject_id,note_id)`, exact `note_type==DS`, canonical admission key `(subject_id,hadm_id)`.

Bind `[internal dataset path]`, table `note/discharge_detail`, schema `table-18d43f38e33d1fd2.json`, [source checksum], columns `note_id,subject_id,field_name,field_value,field_ordinal`, joining `(subject_id,note_id)`. Detail fields are provenance only; `author` is not a responsibility ontology.

The available source profile records 546,028 admissions, 364,627 patients, 593,071 service rows, 94,458 ICU stays, 2,321,355 radiology rows (`RR=2,295,635`, `AR=25,720`), 6,046,121 radiology-detail rows, and 331,794 unique admission-linked DS rows, including 17 missing DS `storetime` values. These are computability checks, not clinical truth.

## Feasibility evidence and its limits

The executable bounded profile at `[internal dataset path]` and its output `source_target_interval_profile.json` read the first 100,000 physical discharge rows and first 300,000 physical radiology rows in gzip order. It did not construct the clinical population, use random sampling, export note text, or produce clinical labels. The discharge prefix had 100,000 nonmissing identifiers and timestamps except two missing `storetime` values; broad lexical indicators occurred in 67,768 target rows, 77,563 interval rows, 99,820 firm-marker rows, 75,756 tentative-marker rows, 67,391 completion-marker rows, and 47,003 replacement-marker rows. The radiology prefix had 147,256 nonmissing `hadm_id` values across 39,628 admission keys and 158,127 target-marker, 11,677 interval-marker, 42,377 firm-marker, 54,877 tentative-marker, 103,637 completion-marker, and 9,136 replacement-marker rows. These overlapping nonrandom regex counts establish that the required fields and broad threat signals are computationally observable; they are neither prevalence estimates nor evidence of completion, invalidity, persistence, or clinical importance.

## Presealed semantic target-and-interval ledger

All semantic features are computed after the inherited opportunity and recommendation-unit ledger is sealed, but before any route, atom, sampling weight, parent label, or release gate is joined to the new layer. The output contains hashed identifiers and structured codes, not source text. A frozen normalizer may change only Unicode form, case, whitespace, punctuation spacing, and de-identification placeholders. It must preserve measurements, anatomy, laterality, modality, comparison, action, interval, negation, and modal force.

For each frozen recommendation unit, derive a source fingerprint from its reciprocal radiology recommendation and a discharge-action fingerprint from every candidate target/action span in the canonical DS, including spans outside the apparent follow-up section. Each fingerprint has independently stored fields:

1. target anatomy and subsite;
2. laterality, when stated;
3. measurement and measurement qualifier, when stated;
4. modality or action type (for example, imaging modality, repeat study, surveillance, referral language);
5. comparison or lesion descriptor;
6. explicit action direction and negation;
7. interval value, unit, qualifiers (`approximately`, `at least`, `up to`, `within`), and whether the interval is relative to discharge, the report, or an unknown reference point; and
8. force (`FIRM`, `CONDITIONAL`, `OPTIONAL`, `INFORMATIONAL`, `NEGATED`, `UNKNOWN`).

A candidate DS span is eligible for matching only when it is target-specific under the frozen field rules. Exact sentence reuse, generic “follow-up,” a section heading, or subject/admission linkage alone is insufficient. The deterministic matcher emits one of the following mutually exclusive field-level relations for each source/DS pair:

* `EXACT`: all explicitly stated target/action fields agree and the interval relation is exact;
* `COMPATIBLE`: no explicit field conflicts, target identity is independently supported, and any interval difference falls within a prespecified clinically agnostic compatibility rule;
* `CONFLICT`: at least one explicitly stated anatomy, laterality, measurement, modality, action, negation, or interval relation conflicts;
* `UNKNOWN`: a required identity/timing field is missing, ambiguous, unparsable, or has no defensible reference point.

The compatibility rule is mathematical, not a clinical recommendation. For a source interval `[a,b]` and discharge interval `[c,d]` after conversion to a common unit, `EXACT` requires equal bounded values and equal qualifiers; `COMPATIBLE_RANGE` requires nonempty interval intersection with no contradictory qualifier or negation; `CONFLICT` is disjoint intervals or an explicit changed/superseding interval; and `UNKNOWN` applies to open-ended, calendar-relative, missing-unit, contradictory, or unanchored intervals unless the text explicitly supplies a valid common reference. No interval is judged clinically appropriate by this rule. “Within 3 months” versus “in 90 days” may be mathematically compatible only under a frozen unit-conversion tolerance declared before labels; it must otherwise remain `UNKNOWN`, not be silently rounded.

When multiple candidate DS spans exist, retain all pair relations and use the adverse-compatible set, not a favorable best match. A source unit has favorable semantic support only if every plausible target/action interpretation is `EXACT` or `COMPATIBLE` and at least one target-specific pair is present. Any `CONFLICT` or `UNKNOWN` interpretation remains possible and therefore blocks a release gate under worst-unit routing. A later span outside the apparent section is included; a section parser can locate it but cannot exclude it.

The ledger separately records source-to-DS exact-copy and token-LCS similarity, cross-subject recurrence, section coordinates, note lineage, and whether target-specific fields are independently preserved. Copy and recurrence are provenance covariates, never automatically adverse or favorable. A copied sentence with intact target and interval semantics can remain valid textually; a copied sentence with swapped target, incompatible modality/laterality, or unresolved interval is not target-grounded.

## Observation-process calibration ledger

The observation layer is a measurement audit, not an imputation model. It is generated deterministically for every fixed challenge admission and every frozen unit, with no future-note-positive selection. It retains separately:

* `charttime` (documented clinical-time field), `storetime` (repository storage-time field), and `D=dischtime`;
* whether each relevant row is admission-linked through `(subject_id,hadm_id)`, subject-only linked because `hadm_id` is missing, or unlinked;
* whether a row is available under the declared source snapshot, has missing times, has impossible ordering, or is an addendum/duplicate according to detail lineage;
* whether `charttime<D` and `storetime<D` (eligible pre-departure artifact), `charttime<D<storetime` (delayed index artifact), `D<charttime` and `D<storetime` (post-departure documentation), or temporally unresolved;
* whether the canonical DS `storetime` is missing, making the inherited unit clock unresolved; and
* whether the administrative source horizon, death, or missing linkage limits observation opportunity.

For a target/action candidate, define an observation-opportunity state before labels:

* `OBSERVED_PRE_D`: target/action evidence is present in an eligible pre-`D`, pre-storage artifact;
* `DELAYED_STORAGE`: charttime is pre-`D` but storetime is post-`D`; this cannot establish that the artifact was available at departure;
* `POST_D_DOCUMENTATION`: both relevant times are post-`D`; this is not evidence for the departure semantic match;
* `LINKAGE_UNKNOWN`: a same-subject row lacks `hadm_id` or target linkage is ambiguous;
* `CLOCK_UNKNOWN`: required time is missing or ordering is impossible;
* `ADMINISTRATIVELY_CENSORED`: the source horizon or death prevents a declared observation window; and
* `NO_OBSERVED_EVIDENCE`: no eligible artifact was observed, always distinguished from “no action,” “no care,” “completed,” or “failed.”

`OBSERVED_PRE_D` means only that the text is in the available artifact under the declared timestamp contract. It does not mean it was viewed or communicated. `DELAYED_STORAGE`, `LINKAGE_UNKNOWN`, `CLOCK_UNKNOWN`, censoring, and no observed evidence are adverse-compatible states for release bounds, but they are reported separately and never relabeled as a clinical failure. Repository storage is never treated as viewing.

The semantic ledger must be sealed before parent panel labels and routes are revealed. The observation ledger is joined only after the parent's R1/R2 compatible sets and all inherited route labels are sealed. No post-departure row may revise the original opportunity, `R_store,u`, `D`, unit identity, atom, route, or parent reference status. Same-admission post-`D` rows and later admissions are retained only as observation diagnostics; they are not persistence outcomes and cannot rescue a failed atom.

## Independent reference layer and workload

The parent's two roster-disjoint whole-admission reference readings remain unchanged and are not replaced by an algorithm. Every inherited challenged admission receives exactly those two readings, at most 600 total for at most 300 admissions. Panels retain the parent's assertion- and trajectory-centered views and exhaustive compatible departure statuses. The semantic and observation ledgers are presealed, route-concealed, and shown only as structured evidence after labels, never as expected answers. They do not prompt adaptive re-review.

The workload contract is explicit: one deterministic full-source computation for the fixed challenge roster; exactly two parent packets per challenged admission; no third reader, senior consensus, top-up, replacement, route-triggered packet, new unit, or post-label semantic search. All recommendation units remain in the denominator. Failure to render every unit, verify source hashes, preserve roster disjointness, or complete the declared scan is `SEMANTIC_OBSERVATION_INFEASIBLE`; all affected atoms default to `DEFER`.

## Estimands and exact adverse-compatible analysis

For every exact atom and inherited route, retain the parent's design-weighted unit- and worst-unit admission-level estimands and add:

1. mass of `EXACT`, `COMPATIBLE`, `CONFLICT`, and `UNKNOWN` semantic relations, separately by field (target, laterality, measurement, modality, action, interval, negation);
2. mass of interval relations `EXACT`, `COMPATIBLE_RANGE`, `CONFLICT`, and `UNKNOWN`;
3. target-specific versus generic-only DS action mass;
4. source-copy/recurrent provenance cross-tabulated with semantic compatibility, without treating recurrence as outcome evidence;
5. observation states `OBSERVED_PRE_D`, `DELAYED_STORAGE`, `POST_D_DOCUMENTATION`, `LINKAGE_UNKNOWN`, `CLOCK_UNKNOWN`, `ADMINISTRATIVELY_CENSORED`, and `NO_OBSERVED_EVIDENCE`; and
6. parent actionability/reference discordance and reference-state masses after semantic/observation restriction.

The primary estimand remains conditional on inclusion in the fixed inherited actionability challenge. A secondary lifted estimate uses the inherited admission and pair inclusion probabilities exactly as supplied; no new probability is invented for the deterministic ledger. Compute exact finite-population compatible-world lower and upper bounds and 20,000 Rao-Wu replicates with all units and labels from one admission kept as one joint cluster. The single simultaneous 95% family covers inherited and new semantic/observation estimands and controls.

Lower bounds count only jointly observed, target-specific `EXACT`/`COMPATIBLE` support with no conflicting interpretation. Upper adverse bounds assign every panel disagreement, plausible `CONFLICT` or `UNKNOWN`, missing time, delayed storage, ambiguous linkage, parser failure, missing DS storetime, source corruption, and nonresponse to the adverse-compatible state. The output also reports the observed category separately so conservative bounds are not misrepresented as observed clinical event rates. Kappa, majority vote, embedding similarity, latent-class models, favorable imputation, or an algorithmic score are diagnostics only and cannot change the bounds or routes.

## Release gates and falsification

All parent gates remain conjunctive and unchanged. In addition, an `AUTO` atom must satisfy, among its challenged candidate-route admissions:

* every adverse-compatible unit has parent status `R_FIRM_ACTIVE` and has at least one target-specific `EXACT` or `COMPATIBLE` source/DS match;
* no unit has an adverse-compatible target, action, negation, or interval `CONFLICT` or `UNKNOWN` state;
* simultaneous upper bound for semantic incompatibility is at most 0.05, and upper bound for interval `CONFLICT`/`UNKNOWN` is at most 0.02;
* observation-process missingness, delayed-storage, linkage-unknown, clock-unknown, administrative-censoring, and nonresponse upper bound is below 0.05 unless the relevant state is fully censused;
* parent copy, anchor, control, support, effective-sample-size, and workload gates pass; and
* the parent's worst-unit rule has no adverse-compatible unit that is tentative, completed, superseded, inactive, conflicting, or unknown.

A `RECON` atom must have every unit adverse-compatible with parent `R_FIRM_ACTIVE` or `R_FIRM_INCOMPLETE`, at least one target-specific `EXACT` or `COMPATIBLE` pair per unit, semantic incompatibility upper bound at most 0.10, interval `CONFLICT`/`UNKNOWN` upper bound at most 0.10, and observation-process adverse/missingness upper bound at most 0.10, together with every inherited gate. `R_FIRM_INCOMPLETE` can require reconciliation and never permits `AUTO`. `TIMING` cannot override a semantic conflict, observation uncertainty, or non-active parent status. All sparse, missing, unsupported, infeasible, or unresolved cases are `DEFER`.

The controls are inserted before any labels and are never used to rescue real cases:

1. exact copied text with preserved target, modality, and interval must remain semantically compatible but retain copy provenance;
2. target swap with otherwise identical wording must become `CONFLICT` or `UNKNOWN`, never compatible;
3. laterality swap, measurement perturbation, modality swap, and negation insertion must each change only the corresponding field relation;
4. exact interval equivalent after predeclared unit conversion must be `EXACT` or `COMPATIBLE_RANGE`, while disjoint intervals are `CONFLICT`;
5. missing interval unit, ambiguous reference point, or contradictory qualifier must be `UNKNOWN`, not rounded or favorable;
6. `charttime<D<storetime` must be `DELAYED_STORAGE`, not `OBSERVED_PRE_D` or post-departure care;
7. post-`D` documentation must not alter the sealed departure semantic ledger;
8. missing `hadm_id` must be `LINKAGE_UNKNOWN`, never silently dropped or linked by subject alone;
9. missing `charttime` or `storetime` must be `CLOCK_UNKNOWN`; and
10. adding or removing a generic “follow-up” phrase, section heading, punctuation, or formatting must not change a target-specific relation.

Route revelation before seals, using future or post-label evidence to define semantic fields, treating storage as viewing, omission of a unit, favorable assignment of unknown, POE use, source-text export, or any failed fixture invalidates the affected run.

## Interpretation

A supportive result requires all inherited gates, exact source/schema/key/time checks, complete semantic and observation ledgers, successful controls, positive inclusion probabilities, valid admission clustering, complete parent challenge workload, and at least one fully supported exact atom. It supports only that, in the available MIMIC artifacts, the discharge action is reproducibly target-specific and semantically compatible with the source recommendation under the frozen interval rule, while the observation-process audit does not leave adverse-compatible uncertainty above the release threshold. It permits nomination of a prospective within-site **silent** workflow study only.

An adverse result is an atom-specific semantic target/interval conflict, a parent reference state incompatible with activity, observation-process uncertainty crossing a gate, or a control/seal/workload failure. It excludes that atom from nomination but does not prove that care was inappropriate, delayed, omitted, harmful, or clinically unsuccessful. A high `NO_OBSERVED_EVIDENCE` or delayed-storage rate means limited observation, not completion, nonadherence, failure, or no need.

An inconclusive result includes missing or ambiguous target fields, unanchored intervals, missing times, delayed storage, unlinked rows, administrative or death censoring, missing DS storetime, sparse atom support, nonresponse, infeasible full-source scan, broken roster/seals, or compatible bounds that include both pass and fail worlds. It is not a pass and defaults to `DEFER`.

Computationally checkable claims are source/schema hashes, table and key uniqueness, exact canonical DS selection, `D`, reciprocal linkage, unit clocks, pre-`D` filtering, field-level semantic relations, interval arithmetic, observation-state assignment, complete-unit inclusion, roster/workload accounting, inclusion probabilities, compatible-world bounds, joint clustering, route precedence, and gate evaluation. MIMIC cannot establish actual viewing, responsibility, communication, ordering, referral, scheduling, execution, outside care, appropriateness, patient preference, malignancy, benefit, harm, live departure obligation, or causal utility. Expert adjudication and a separately approved prospective actual-calendar workflow study remain required before any live use, safety claim, benefit claim, or causal inference.
