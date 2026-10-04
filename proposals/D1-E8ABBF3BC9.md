# A nested two-phase probability validation of actionability and supersession with all-unit fail-closed routing

## Decision question and targeted advance

The decision is whether any exactly supported MIMIC pulmonary-opportunity atom warrants a **prospective within-site silent measurement/workflow bridge**. The bridge would measure, without firing an alert or changing care, whether a future implementation could distinguish a still-active portable recommendation from one requiring clinician choice or one explicitly completed, stopped, or replaced. MIMIC-only evidence can never nominate `AUTO` or `RECON` for operational deployment, and it cannot establish clinical truth, appropriateness, safety, benefit, responsibility, or causality.

The assigned parent is scientifically mature but requires four independent clinical readings for every recommendation unit in every selected admission: two actionability (`C`) and two supersession (`S`) readings. That admission-complete design may consume the entire <=900-admission budget in physician time before it can answer its narrower retrospective question. This successor makes one targeted change only: it replaces the four-reading census of the selected audit with a **predeclared nested two-phase probability validation**.

* Phase 1 reviews every unit in every selected admission once for actionability and once for supersession (`C1` and `S1`). Thus every selected unit and every selected admission still receives an actual route-bearing review; no admission is dropped, and one adverse or unknown unit still controls its admission.
* Phase 2 independently re-reviews every unit in a probability-selected subset of phase-1 admissions (`C2` and `S2`). The phase-2 draw is fixed from the pre-label frame, atom, stratum, and unit-load cell; it is never triggered by a phase-1 label, apparent route, disagreement, or ease of packet construction.
* Phase-1 labels are the complete all-unit screening route. Phase-2 labels can only worsen or invalidate that route, never rescue it. The finite-population phase-2 validation estimates and bounds the population of possible missed adverse states, while the complete integer shared-error frontier remains an explicit sensitivity analysis rather than an agreement-as-truth claim.

This reduces the maximum real-case clinical reading burden from `4*sum(U_i)` to `2*sum(U_i)+2*sum_{i in phase2}(U_i)`, with a prespecified phase-2 rate of at least 25% and a census in small cells. It therefore lowers expected burden while retaining positive known inclusion probabilities, design-based finite-population inference, all-unit worst-case routing, exact support atoms, measurement-integrity controls, correlated-error sensitivity, and fail-closed defaults. The price is deliberate: phase-1-only admissions have no individually confirmed duplicate reading. They are not silently treated as confirmed; phase-2 noncoverage is represented in adverse bounds and can block nomination.

## Evidence boundary and unresolved claim

The strongest available claim is a feasibility claim. The configured snapshot contains the admission, patient, service, ICU, radiology, radiology-detail, discharge, and discharge-detail artifacts needed to construct the inherited retrospective opportunity, chronology, support atoms, and route packets. It does not contain a reliable physical-departure artifact, viewing or acknowledgement logs, sign/transmit history, named responsibility, outside plans, target-linked orders/referrals/scheduling, completed follow-up imaging, patient preference, safety outcomes, or intervention receipt. The note guides also warn that MIMIC timestamps are deidentified and cross-subject calendar alignment is invalid. These facts do not support actionability or clinical benefit.

The untested claim is narrower and falsifiable: among exact support-qualified atoms, can route-concealed clinicians apply the frozen actionability/supersession ontology reproducibly enough that the inherited text route is not contradicted by an observed or design-bounded adverse state, even after accounting for phase-2 noncoverage and arbitrary shared clinical error? The attainable MIMIC decision is only whether to launch a prospective silent bridge to measure actual workflow and clinical adjudication. A retrospective pass is not a deployment recommendation.

### Falsifiable hypothesis

At least one support-qualified atom will satisfy all of the following under the frozen two-phase protocol:

1. complete source, join, chronology, unitization, sealing, and machine-mapping fixtures have zero errors;
2. every selected admission receives valid phase-1 `C1` and `S1` review for every inherited unit, with all-unit precedence preserved;
3. the phase-2 probability validation has known positive first- and second-order inclusion probabilities, no response or packet leakage failure, and provides simultaneous finite-population bounds for duplicate instability, phase-1-to-phase-2 route worsening, adverse-compatible states, and workload;
4. locked decisive synthetic controls distinguish ontology transitions from semantic-invariance flips, and route realization does not add instability beyond the calibrated nuisance floor;
5. the complete adverse-compatible contamination curve has a positive breakdown count for any candidate route, and no registered external bound on shared clinical error is exceeded; and
6. after all inherited, measurement, support, workload, and correlated-error gates, the atom is at most eligible for a prospective **silent** bridge.

The hypothesis is falsified for an atom by any observed phase-1 or phase-2 candidate-`AUTO` unit compatible with choice, explicit completion/stop/replacement, or unknown; any phase-2 route worsening beyond the registered adverse gate; positive route-realization excess instability; decisive controls indistinguishable from nuisance; a zero shared-error breakdown count; a failed source/seal/workload condition; or an adverse finite-population upper bound that does not meet the predeclared bridge criterion. Sparse or imprecise phase-2 validation, missing external actual-workflow evidence, missing utility governance, or an infeasible packet plan is **inconclusive and fail closed**, not a pass and not a `RECON` rescue.

## Exact source bindings and permitted evidence

Use the frozen MIMIC snapshot `[source checksum]` and retain source files read-only. The core archive is `[internal dataset path]`, [source checksum]. Use these archive members and catalog schemas.

* `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`, columns `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`; join key `(subject_id,hadm_id)`, departure proxy `dischtime`.
* `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`, columns `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; join on `subject_id`. Adult age and widened possible-calendar class use the inherited definitions only.
* `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`, columns `subject_id,hadm_id,transfertime,prev_service,curr_service`; join `(subject_id,hadm_id)`. Only nonmissing `transfertime < dischtime` can define terminal service or workflow atom.
* `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, columns `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; diagnostic only, never responsibility or supersession evidence.
* `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`, columns `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; join `(subject_id,hadm_id)` and use `intime < dischtime` for inherited ICU exposure.
* `[internal dataset path]` is not the correct absolute path in this workspace; the exact source is `[internal dataset path]`, [source checksum], table `note/radiology`, columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; join `(subject_id,hadm_id)`, identity `(subject_id,note_id)`.
* `[internal dataset path]`, [source checksum], table `note/radiology_detail`, columns `note_id,subject_id,field_name,field_value,field_ordinal`; join only `(subject_id,note_id)`, retain every ordinal and reciprocal `parent_note_id`/`addendum_note_id` relation.
* `[internal dataset path]`, [source checksum], table `note/discharge`, exactly `note_type == "DS"`, canonical key `(subject_id,hadm_id)`, same eight note columns.
* `[internal dataset path]`, [source checksum], table `note/discharge_detail`, columns `note_id,subject_id,field_name,field_value,field_ordinal`; join `(subject_id,note_id)`. `author` is not an ontology, responsibility, or supersession signal.

The exact local catalog and guide are `[internal dataset path]` and `[internal dataset path]`. The parent ontology is copied byte-for-byte from `[internal dataset path]`, [source checksum]; no real labels may be viewed before its hash and acceptance are recorded.

`hosp/poe`, `hosp/poe_detail`, diagnoses, procedures, medications, billing, and all post-`D` records are prohibited from eligibility, primary packets, clinical states, routes, atoms, estimands, calibration, and gates. Do not send any clinical note or private row to public search.

## Frozen inherited frame, chronology, and route

Import the parent’s population and do not reinterpret it. Stream the complete radiology and discharge sources; freeze retrieval and the retrieval-negative audit before unredacted route work. Define `N_A` as one first-eligible admission per subject, sorted by `admittime,hadm_id`, satisfying the adult, incidental pulmonary-nodule or indeterminate focal-nodular-opacity, and patient-specific unconditional chest/thoracic CT at exactly 3, 6, or 12 calendar-month opportunity rules. Retain every inherited exclusion: screening/surveillance/staging, conditional or optional recommendations, explicit no-follow-up, in-hospital death, hospice/comfort, and post-`D` evidence. Do not infer risk, appropriateness, life expectancy, or absent context.

Retain only subject/admission-consistent reciprocal pre-`D` report/addendum chains. Every operative component must have `charttime <= D` and `storetime <= D`; missing, one-way, contradictory, or mistimed chains are `U_R`. Require exactly one canonical `DS`; duplicate canonical keys halt the run; missing or unreadable text/linkage/storetime is unknown, and `charttime` cannot substitute for `storetime`.

Preserve every inherited departure state `Y={F,C_O,C_I,R,A,U_D}`, availability state `V={V_D,V_24,V_72,V_168,V_late,V_U}`, lag state `H={H_stale,H_0_6,H_6_24,H_24_72,H_72plus,H_U}`, eventual state `Z={F_text,C_O_text,C_I_text,R_text,U_text}`, and `J_A` cell. For each unit retain `R_store,u`, `DS_store`, `G_u=DS_store-R_store,u`, and verify `D-R_store,u=(D-DS_store)+G_u`; only unit-specific `G_u` defines opportunity, and every content-routed active unresolved unit requires known `G_u >= 24h`.

A unit is exactly `(target_cluster, action/modality, due_interval_or_date, polarity)`. Deduplicate reciprocal restatements, treat material addenda as revisions, and map unresolved splitting/coreference to `U_BOUNDARY`. Units are nested inside admissions and are never sampled or weighted independently. Preserve all sealed `R-I/K-I/S-I`, `R-A/K-A/S-A`, H1/H2/H3, redaction, minority-unit, roster, packet, access, and route-concealment firewalls.

Use exact atom `g=(E, exact terminal curr_service, W)`. Define `E` by the inherited possible-calendar interval `C_i=[a_i+q_i-1,b_i+q_i+1]`, with `E_EARLY` if the upper endpoint is `<=2013`, `E_LATE` if the lower endpoint is `>=2017`, `E_BRIDGE` otherwise, and `E_UNKNOWN` on defects. Terminal service is the unique nonmissing `curr_service` at greatest valid `transfertime < D`; ties, absence, and contradiction become `SERVICE_UNKNOWN`. Retain `W_SIMPLE` for one valid service row with no transition and no pre-`D` ICU, `W_COMPLEX` for a distinct service transition or pre-`D` ICU, `W_INTERMEDIATE` for multiple rows without transition or ICU, and `W_UNKNOWN` for defects.

Build the pre-label support atlas from frame counts only. Initial atoms require known components and `N_g >= max(30,0.02*N_A)`, preserve within-stratum occupied-cell minima, and use deterministic smallest-atom removal to a residual until the inherited fixed sample is feasible. No merge, return, borrowing, neighboring-atom rescue, or post-label pruning is permitted.

## Phase-1 and phase-2 population and sampling

The source frame is the complete inherited `N_A` admissions, not a responder or route-selected subset. Preserve the five outcome-blind strata and precedence: sentinel census; `S_ZERO` is the larger of 300 or the finite-population worst-case 95% +/-4-point formula; each other noncensus stratum is the larger of 120 or the +/-7-point formula, capped at `N_h`; sentinel plus formula totals must be <=900 distinct admissions or the run is `NO_SELECTION`.

### Phase 1: census within the frozen admission audit sample

Use deterministic maximin allocation and SRS without replacement within each inherited stratum. Record ordered IDs, `n_h`, `N_h`, and first-order `pi1_i`; compute exact `pi1_ij` for every pair. There is no replacement, top-up, adaptive restriction, or phase-1 label-dependent selection. Every phase-1 admission receives one `C1` and one `S1` reading for every inherited unit, including all units in sentinel-census admissions.

### Phase 2: fixed nested validation sample

Before packet construction, partition the phase-1 sample by the cross-product

`c = (inherited stratum h, exact support atom g, unit-load bin b)`.

The unit-load bin is frozen from the deterministic phase-1 unit inventory and is `b=0` for `U_i=1`, `b=1` for `2<=U_i<=3`, `b=2` for `4<=U_i<=7`, and `b=3` for `U_i>=8`; it is a workload-control variable, not a clinical feature. Let `m_c` be the number of phase-1 admissions in cell `c`. Draw phase 2 by SRS without replacement within every cell, independently of every phase-1 label and outcome. The exact conditional phase-2 inclusion probability is

`q_c = 1                       if m_c <= 12`
`q_c = 1/4                     if m_c > 12`.

Thus `pi2_i = pi1_i*q_c` for an admission in cell `c`; for two distinct admissions `i,j`, `pi2_ij = pi1_ij*q_c^2` when they share a cell and `pi1_ij*q_c*q_c'` otherwise, with the obvious census convention when a cell is fully included. Record the realized draw seed, ordered IDs, `m_c`, selected count, `q_c`, `pi2_i`, and exact `pi2_ij` before any phase-2 packet is opened. If a cell is not represented in phase 1 it cannot be invented or repaired. Phase-2 selection failure, altered probabilities, or any label-conditioned resampling is `NO_SELECTION`.

For each phase-2 admission, every unit receives a second actionability reading `C2` and a second supersession reading `S2`, from roster-disjoint reviewers and newly ordered, independently sealed packets. Phase-2 review is all-unit within the selected admission; never sample individual units, easy units, candidate routes, or responders. The expected real-reading burden is at most three readings per unit in cells with `m_c>12` and four in census cells; no workload accounting treats phase-1-only records as having duplicate labels.

### Workload feasibility

Before real labels, operations governance hashes an absolute physician-hour budget `B_H`, per-reviewer weekly caps, qualifications, roster-disjoint availability, assignments, deadline, and the phase-2 cell-selection algorithm. A synthetic final-packet rehearsal records active time by phase and packet type. Use the maximum observed rehearsal time for each type, not a favorable mean. Let `P_t` count phase-1, phase-2, calibration, redaction, audit, and seal packets. Require

`H_plan = 1.15 * (sum_t P_t*max_time_t + fixed_meeting_and_audit_hours) / 60 <= B_H`.

Every selected admission must have sufficient slots for its complete phase-1 review; every phase-2 selected admission must have both duplicate readers for every unit. Fixed controls and a 15% reserve cannot be purchased by reducing phase-1 coverage. If the plan fails, return `NO_SELECTION`; do not preferentially review simple admissions or remove high-unit-load cells. Report observed hours and simultaneous finite-population upper workload bounds by atom, phase, and route.

## Route-blinded clinical readings and locked mapping

Use the byte-frozen `pulmonary_actionability_supersession_v1` ontology. The phase-1 actionability reviewer labels each unit `C_PORTABLE_ACTIVE`, `C_CHOICE_ACTIVE`, `C_EXPLICIT_COMPLETE`, `C_EXPLICIT_STOP`, `C_UNDETERMINED`, or `C_PACKET_INVALID`, with quoted spans and a missing-facts checklist. The phase-1 supersession reviewer independently enumerates target linkage, action/modality, timing, polarity, status, and `S_EXACT_REPLACEMENT`, `S_EXACT_COMPLETION`, `S_EXACT_STOP`, `S_MODIFY_OR_COEXIST`, `S_RESTATEMENT`, `S_NONE_OBSERVED`, or `S_UNKNOWN`, with exact quoted evidence. They see no inherited labels, routes, atoms, strata, sampling weights, phase-2 status, or outcomes.

`C-P` contains the reciprocal pre-`D` radiology chain, permitted admission/death/disposition context, relative chronology, and canonical DS context after independent redaction of target/action/timing/recipient/responsibility/replacement/completion/conflict spans. `S-P` contains only the reciprocal recommendation and every pre-`D` target-linked DS statement with local context and relative order. The two packet views remain sealed and roster-disjoint. No author/service field, omission, paraphrase, intuition, or consensus establishes supersession.

For phase 1, apply the locked Cartesian product to the two individual labels `(C1,S1)`, packet validity, redaction audit, and inherited boundary states. Let `K1_U` result from any unknown/invalid/boundary state or active-versus-no-action conflict; let `K1_N` result from any compatible explicit completion/stop/exact replacement; let `K1_R` result from wholly active compatible sets containing material choice or modification/coexistence; and let `K1_P` require the singleton portable-active/none-or-restatement state. For phase 2, apply the identical mapping to all four individual labels and all quality states, producing `K2`.

The all-unit screening route is derived only by locked code, never by a reviewer vote. For every admission, preserve the parent precedence: any `U_DEFER` gives `A_DEFER`; otherwise any `U_TIMING` gives `A_TIMING`; all resolved/closed gives `A_NOACTION`; `A_AUTO` requires every unit to be wholly omitted with ample unit-specific clocks and no uncertainty/conflict; incomplete, conflicting, or mixed states give `A_RECON`. Any non-singleton robust route is `DEFER`.

The new phase rule is monotone and fail closed.

* Every unit in every phase-1 admission receives a `K1` and participates in the all-unit route. A `K1_U`, `K1_N`, or `K1_R` blocks `AUTO`; a singleton `K1_P` is only a screening-compatible portable unit.
* In phase-2 admissions, replace each `K1` by the Cartesian-compatible `K2` set. A phase-2 `K2_U`, `K2_N`, or `K2_R` can only remove a candidate route or change it to `RECON`/`DEFER`; it can never convert a phase-1 failure into a pass. Any duplicate disagreement is retained as a compatible set, not consensus-resolved.
* A phase-1-only unit has no fabricated `K2`. Its missing duplicate is a phase-2 noncoverage state in the validation estimand. It is not called validated, and no individual phase-1-only record may be claimed clinically safe.
* All `K_N` remains descriptively no-action but operationally `DEFER`; `RECON` is not a rescue queue for phase-2 absence, unknowns, or packet defects.

This is how the design preserves all-unit worst-case routing while acknowledging that a probability validation cannot provide a second clinical reading for every admission. The primary route is a complete, conservative route for every selected unit; duplicate evidence is used only through prespecified adverse population bounds and sensitivity curves.

## Calibration, negative controls, and measurement integrity

Before real packets, an independent methods unit creates and hashes the parent’s 48 matched synthetic/semisynthetic pairs for each task: six ontology contrast families, four independently worded surface forms, and two concealed orders per contrast. Every reviewer receives a balanced 24-pair qualification set, and the remaining pairs are interspersed as ongoing controls. No text is copied from a real selected admission. The fixtures cover portable versus material choice; active versus exact completion; active versus explicit stop; missing decisive evidence; exact replacement versus coexistence; completion versus restatement; exact target linkage versus unrelated plan; route-realization invariance; semantic paraphrase; nuisance; and non-target invariance.

The phase-2 duplicate panel receives independently ordered control packets, including route-swap and nuisance/non-target transformations. Controls are selected and assigned before real labels, and missing control responses are errors. Require zero implementation errors in schema, Cartesian mapping, all-unit precedence, phase probabilities, packet generation, and expected control transitions. Within task, use one common max-statistic simultaneous 95% family and require the lower confidence bound for correct decisive transition to exceed the upper bound for semantic-invariance flips. Require the upper bound for route-realization flips to be no larger than the upper bound for matched nuisance/semantic flips. Report each decisive rate, invariance rate, pair difference, reviewer effect, phase effect, and exact interval without replacing them with kappa or an arbitrary clinical threshold.

Phase-2 duplicate instability is an observable measurement property, not a clinical gold standard. Estimate disagreement and route-worsening under the nested design with design weights. A route-worsening event includes any phase-1 candidate `AUTO` unit/admission becoming `RECON`, `TIMING`, or `DEFER`, or any phase-1 non-adverse unit becoming `K_N`, `K_U`, or `K_R`. For phase-1-only admissions, the unobserved duplicate outcome is not assumed benign; the finite-population upper bound integrates the phase-2 validation design and assigns missing/nonresponse/packet defects adversely. A phase-2 duplicate can expose a shared codebook or interpretation problem only if it differs; agreement still cannot identify shared clinical error.

Required controls include route anchoring, semantic paraphrase invariance, decisive completion/decline, exact replacement versus coexistence, unrelated-plan non-supersession, one adverse minority unit among safe units, high-weight missingness, pooled-safe/atom-unsafe masking, unsupported signatures, noncensus zero events, phase-2 probability monotonicity, workload overload, roster overlap, phase-before-seal access, and a claim checker rejecting clinical-truth, safety, benefit, responsibility, and causal conclusions. Any control or seal failure is adverse or `NO_SELECTION`, never repaired by excluding the offending record.

## Finite-population estimands and correlated-error sensitivity

The primary estimand is the finite-population proportion and count, within each exact support atom and inherited stratum, of selected admissions whose all-unit phase-1 screening route is compatible with each inherited route, and whose phase-2 duplicate state would worsen that route. Estimate these with the known nested inclusion probabilities, retaining the admission as the sampling unit and all units, views, labels, controls, packet states, and workload as a cluster. Use Horvitz–Thompson totals, Hájek ratios where requested, finite-population Taylor variance, exact hypergeometric or multivariate-hypergeometric inversion for sparse cells, and at least 20,000 Rao–Wu rescaled bootstrap replicates within each noncensus design cell. Use one max-statistic simultaneous 95% family over inherited gates, atom gates, phase-2 instability, route worsening, precision, workload, calibration contrasts, and registered bridge-policy endpoints. Census records remain fixed. Report both numerator and denominator; zero events retain a positive upper bound.

For a route-compatible phase-1 atom, let `W_g` be the complete finite-population compatible set of possible phase-2 adverse counts obtained by the design-based interval for phase-2 route worsening, including phase-1 noncoverage and nonresponse under the registered adverse rule. Do not impute or use complete cases. Let `m=0,...,N_g` be the number of atom admissions whose true clinical decision need may lie outside every observed compatible set because all retrospective clinical readings share an error. Solve the inherited adverse finite-population program for every integer `m`, retaining all units of each admission, and report simultaneous lower/upper curves for candidate-`AUTO` adverse compatibility, no-action/supersession compatibility, candidate-`RECON` active-choice compatibility, capture, route worsening, and workload. Define the breakdown count `m*_{gr}` as the smallest integer at which route statement `r` ceases to hold; report `m*/N_g` with uncertainty.

Neither phase-1/phase-2 agreement, duplicate disagreement, H1/H2/H3, latent-class models, nor synthetic controls identifies clinical shared error. An external `M_g` may condition a silent-bridge nomination only if independently registered before labels and based on an independent, probability-ascertained target population with actual-calendar workflow evidence that can reveal errors shared by all retrospective panels, plus a simultaneous upper bound after transport uncertainty. With no qualifying external source currently available, set policy `M_g=N_g`; all clinical-actionability nominations remain `DEFER` even if the retrospective compatible route looks favorable. This is an identification limitation, not an estimate of harm.

## Baselines and required comparisons

Run, without using any baseline to change the locked route:

1. inherited text-only routing;
2. phase-1 single-pair routing versus the phase-2 duplicate-adjudicated subset;
3. H1/H2/H3 agreement and majority/favorable consensus;
4. route-revealed review;
5. one shared ontology task instead of separate C/S tasks;
6. pooled, unweighted, complete-case, and shrunken analyses;
7. `m=0`, the complete `m=0..N_g` contamination curve, and unrestricted `m=N_g`;
8. an exact phase-2 census-cell subset versus the 1/4 cells; and
9. any latent-class diagnostic, with every identifying assumption displayed.

These are diagnostics or falsification controls only. None can nominate an operational route, rescue an unsupported atom, or replace the nested design. The key feasibility comparison is physician hours and interval width against the parent’s four-reading census, reported without choosing the design after seeing labels.

## Predeclared outcomes and interpretation

### Supportive outcome

At least one atom passes source, ontology, chronology, unit, seal, calibration, support, phase-probability, workload, and simultaneous precision gates; no observed all-unit adverse unit is hidden by a phase-2 duplicate; the phase-2 design-based upper bound for route worsening is below the independently registered bridge criterion; and the atom’s complete integer contamination frontier has a positive breakdown count at every externally defensible shared-error bound. This supports only the narrow statement that a specific MIMIC text route and route-concealed measurement process are sufficiently reproducible and feasibly auditable to justify consideration of a prospective **silent** measurement/workflow bridge. Because no qualifying external actual-workflow bound or utility governance exists in the current evidence, the default output remains `DEFER`, not a deployment or route nomination.

### Adverse outcome

Any observed adverse-compatible phase-1 or phase-2 unit, a phase-2 duplicate that worsens a candidate route, an adverse upper bound exceeding the bridge criterion, a zero breakdown count, decisive-control failure, route anchoring, leakage, roster/seal violation, missing high-weight labels, unsupported atom, or workload overload excludes the atom or stops the run. A single adverse unit controls its admission; a safe majority, pooled estimate, consensus, favorable complete-case result, or phase-1-only status cannot rescue it.

### Inconclusive outcome

No supported atom fits the <=900-admission design; phase-2 cells are too sparse for simultaneous precision; effective sample size is low; packet or control response is incomplete; workload certificate fails; probabilities or seals are not auditable; external shared-error evidence or independently registered bridge utility is absent; or confidence regions span both decisions. Inconclusive means that the retrospective evidence cannot decide whether a silent bridge is warranted. It does not imply safety, actionability, transport, or operational readiness and forces `DEFER/NO_SELECTION`.

## Verifier scope and claim ceiling

A verifier can check the source and ontology hashes; archive-member and table bindings; row counts and joins; first-eligible population; pre-`D` chronology; canonical DS; unit inventory; atom and stratum membership; sample IDs; phase-1 and phase-2 probabilities and second-order probabilities; no label-conditioned selection; packet fields and redaction; roster and access logs; all-unit precedence; monotonic phase-2 mapping; controls and expected transitions; workload arithmetic; HT/Hájek/finite-population intervals; bootstrap count; contamination-curve feasibility and monotonicity; and whether reported supportive, adverse, or inconclusive text is entailed by computed outputs. It must reject any conclusion that calls a route clinically true, safe, appropriate, beneficial, causal, responsible, or deployable.

The verifier cannot establish whether a quoted clinical span is actually correct, whether an external shared-error bound is credible, whether stakeholder utility governance is legitimate, whether a recommendation was visible at departure, whether a clinician or patient understood it, whether a future bridge would be useful, or whether care would improve. Those require independent clinical adjudication, actual-calendar workflow data, governance review, and ultimately a separately governed comparative study with safety monitoring, receipt/correction measurement, workload, follow-up, unnecessary imaging, patient-reported effects, diagnostic outcomes, and causal estimands.

## Exact feasibility advance and remaining uncertainty

The advance is not a smaller arbitrary reviewer sample and not an average-agreement shortcut. It is a nested, probability-ascertained validation in which every sampled admission and unit still receives a complete route-bearing first review, while a prelabel probability subset receives the costly independent duplicate needed to estimate and bound measurement instability. It preserves exact atoms, all-unit adverse precedence, finite-population estimands, and a complete unidentified-shared-error frontier. It explicitly exposes the price of reducing burden: duplicate evidence is incomplete for phase-1-only records and therefore enters adverse bounds rather than being assumed absent. If those bounds are too wide, the result is honestly inconclusive. The only attainable MIMIC decision is whether a prospective silent bridge merits approval; `AUTO`/`RECON` deployment and claims of clinical truth remain outside the experiment.
