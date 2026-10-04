> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Nested two-phase probability validation of pulmonary actionability, with admission-level fail-closed routing

## Purpose and substantive repair

This is a targeted child of `[prior hypothesis]`. It retains the parent's inherited population, chronology, ontology, source restrictions, atom definition, outcome-blind sampling frame, finite-population inference, measurement-integrity controls, contamination frontier, and noncausal ceiling. The repair replaces the admission-complete four-reading burden for every selected admission with a prespecified nested two-phase design.

The central design flaw being repaired is not simply workload. A naive two-phase design would verify only screen-positive or apparently safe admissions, allow reviewers to see the screen result, sample units rather than admissions, and then treat verified labels as truth. That produces verification bias, undercounts correlated within-admission failures, makes atom-level precision illusory, and can support a conclusion about `AUTO` or `RECON` that the MIMIC evidence cannot establish. This protocol prevents those failures by making the phase-2 sampling probability known and positive in every phase-1 result cell, concealing phase-1 labels from phase-2 clinicians, retaining all units of a selected admission, and treating the phase-2 panel as a fallible measurement rather than a gold standard.

The attainable decision is consequently narrowed and made executable: whether the frozen MIMIC measurement system has enough internally bounded evidence to justify a separately governed **prospective silent measurement/workflow bridge**. No MIMIC result nominates a live `AUTO` or `RECON` route, proves clinical truth, establishes actual workflow visibility, or demonstrates benefit.

## Supported evidence and unresolved claim

The available evidence supports feasibility of a retrospective audit, not actionability. The frozen MIMIC snapshot contains admission-linked timestamps and text in the exact files bound below. The catalog records 546,028 `hosp/admissions` rows, 364,627 `hosp/patients` rows, 593,071 `hosp/services` rows, 94,458 `icu/icustays` rows, 2,321,355 radiology rows, 6,046,121 radiology-detail rows, and 331,794 unique discharge rows; 17 discharge rows lack `storetime`. These facts establish computability and known defects only. They do not establish that a recommendation was visible at departure, that an accountable clinician received it, that a plan was appropriate, or that it was completed or superseded.

The unresolved, falsifiable question is:

> In the frozen first-eligible pulmonary-opportunity population, does a low-cost blinded phase-1 actionability screen agree with an independently route-concealed phase-2 measurement often enough, and with sufficiently bounded adverse compatibility under finite-population and shared-error sensitivity analysis, to justify launching a prospective silent bridge that measures actual workflow before any operational routing is considered?

The primary hypothesis is deliberately about measurement and study readiness, not clinical truth. At least one exact support atom must pass the inherited retrieval, chronology, support, calibration, and workload gates; phase-2 weighted estimates must be computable with positive inclusion probabilities in every phase-1 result cell; phase-1/phase-2 discrepancies must not be concentrated in an unverified result class after design weighting; all observed phase-2 admissions must satisfy all-unit adverse precedence; and the atom must remain informative over the complete admission-level contamination curve. A positive result supports only proceeding to a separately approved silent bridge. It does not support an operational route.

A screen-positive-only verification design, a design with zero phase-2 probability for screen-negative or apparently safe cases, phase-2 access to phase-1 labels, unit-level sampling, or a claim that the phase-2 panel is truth is a prespecified falsification of the design rather than a negative clinical result.

## Exact read-only MIMIC bindings

Use snapshot `[source checksum]`. All source files remain read-only. Derived frame manifests, source row numbers, packet hashes, pseudonyms, access logs, phase-1 and phase-2 labels, inclusion probabilities, replicate weights, and outputs are written only in the workspace.

The core archive is `[internal dataset path]`, [source checksum]. Use these archive members and exact columns.

* `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`; key `(subject_id,hadm_id)`, with `D=dischtime`.
* `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; join on `subject_id` for the inherited adult and widened calendar-class rules.
* `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`: `subject_id,hadm_id,transfertime,prev_service,curr_service`; join on `(subject_id,hadm_id)`. Only nonmissing `transfertime<D` can define terminal service.
* `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; pre-`D` `intime` defines the inherited ICU exposure proxy.
* Ordinary file `[internal dataset path]`, table `note/radiology`, [source checksum]: `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; identity `(subject_id,note_id)`, admission join `(subject_id,hadm_id)`.
* Ordinary file `[internal dataset path]`, table `note/radiology_detail`, [source checksum]: `note_id,subject_id,field_name,field_value,field_ordinal`; join only `(subject_id,note_id)`. Retain all ordinals and reciprocal `parent_note_id`/`addendum_note_id` fields.
* Ordinary file `[internal dataset path]`, table `note/discharge`, [source checksum]: the same eight note columns; require exactly `note_type=="DS"` and canonical `(subject_id,hadm_id)`.
* Ordinary file `[internal dataset path]`, table `note/discharge_detail`, [source checksum]: `note_id,subject_id,field_name,field_value,field_ordinal`; join `(subject_id,note_id)`.

The catalog schemas confirm that the four structured tables have the stated temporal columns and keys, and that both narrative note tables have `charttime`, `storetime`, and `text`. `hosp/transfers` may be retained for diagnostic reporting only; it is never evidence of responsibility or supersession. `poe`, `poe_detail`, diagnoses, procedures, medication, billing, and post-`D` records are excluded from eligibility, packets, states, routes, atoms, estimands, calibration, and gates.

## Frozen inherited frame

The compiler must import the parent's frame without reinterpretation.

1. Stream complete radiology and freeze the inherited high-recall pulmonary/exam retrieval and retrieval-negative probability audit before unredacted route work. Candidate reports are admission-linked, have `charttime` in `[admittime-12h,D]`, and meet the inherited triggers.
2. `N_A` is one first-eligible admission per subject, ordered by `admittime,hadm_id`, requiring adult age, an incidental pulmonary nodule or indeterminate focal nodular opacity, and a patient-specific unconditional chest/thoracic CT at exactly 3, 6, or 12 calendar months. Retain every inherited exclusion for screening/surveillance/staging, conditional or optional follow-up, explicit no-follow-up, in-hospital death, hospice/comfort, and post-`D` evidence. Do not infer appropriateness, risk, life expectancy, or missing context.
3. Keep only subject/admission-consistent reciprocal pre-`D` radiology report/addendum chains. Every operative component must have `charttime<=D` and `storetime<=D`; missing, one-way, contradictory, or mistimed chains are `U_R`. A retrieval miss or simultaneous upper denominator undercoverage above 5% blocks every route.
4. Require exactly one canonical `DS`, with `note_type=="DS"`; duplicate keys stop the run. Missing/unreadable text, linkage, or `storetime` is unknown, and `charttime` never substitutes for `storetime`.
5. Preserve all inherited departure, availability, lag, eventual, and `J_A` states. For every recommendation unit retain `R_store,u`, `DS_store`, `G_u=DS_store-R_store,u`, and verify `D-R_store,u=(D-DS_store)+G_u`. Only unit-specific `G_u` determines opportunity, and content-routed active unresolved units require known `G_u>=24h`.
6. A unit is the smallest `(target_cluster, action_modality, due_interval_or_date, polarity)` tuple. Deduplicate reciprocal restatements, treat material addenda as revisions, and map unresolved splitting or coreference to `U_BOUNDARY`. Units are nested under an admission and are never independently sampled or weighted.
7. Preserve the parent's sealed inherited views, roster and packet firewalls, access/seal ordering, independent codebooks, route concealment, and adverse cross-products. No phase-1 or phase-2 reviewer sees inherited labels, routes, atoms, strata, weights, post-`D` text, or outcomes.
8. Preserve admission precedence: any `U_DEFER` gives `A_DEFER`; otherwise any `U_TIMING` gives `A_TIMING`; all resolved/closed gives `A_NOACTION`; `A_AUTO` requires every open unit wholly omitted with ample clocks and no uncertainty/conflict; incomplete, conflicting, or mixed states give `A_RECON`. A non-singleton robust route is `DEFER`; one adverse unit controls the admission.
9. Preserve exact atom `g=(E, exact terminal curr_service, W)`. Use `C_i=[a_i+q_i-1,b_i+q_i+1]`, `E_EARLY` when its upper endpoint is `<=2013`, `E_LATE` when its lower endpoint is `>=2017`, `E_BRIDGE` otherwise, and `E_UNKNOWN` for defects. Terminal service is the unique nonmissing `curr_service` at greatest valid `transfertime<D`; ties, absence, or contradiction give `SERVICE_UNKNOWN`. Preserve `W_SIMPLE`, `W_COMPLEX`, `W_INTERMEDIATE`, and `W_UNKNOWN` exactly as inherited.
10. Construct the support atlas from frame counts only. Initial atoms require known components and `N_g>=max(30,0.02*N_A)`, with inherited occupied-cell minima and deterministic smallest-atom removal to residual until the fixed design is feasible. No post-label merging, borrowing, return, neighboring-atom rescue, shrinkage, or neighboring-service rescue.

## Two-phase design

### Phase 1: inexpensive index screen on all phase-1 admissions

The inherited five outcome-blind strata, sentinel census, finite-population formulas, maximin allocation, SRS without replacement, positive first-phase probabilities `pi1_i`, ordered IDs, and no replacement/top-up remain fixed. Every selected phase-1 admission receives the same inexpensive index screen over **all** of its units. The screen is one trained actionability/supersession abstraction team operating under the same route-concealed source restrictions, or an equivalently frozen deterministic software screen if governance approves it before labels. The screen is not a clinical reference standard and cannot nominate a route.

For each admission, the screen records only a prespecified coarse class `Q_i`, after applying all units and admission precedence:

* `Q_AUTO_SCREEN`: all indexed units appear wholly omitted with ample clocks and no index uncertainty or conflict;
* `Q_RECON_SCREEN`: at least one indexed active unit appears to require choice/modification or the inherited route is mixed;
* `Q_ADVERSE_SCREEN`: any indexed unit is compatible with explicit completion, stop, exact replacement, or another adverse-compatible state;
* `Q_UNKNOWN_SCREEN`: missing packet, invalidity, unresolved boundary, nonresponse, or any other non-allow-listed result.

The screen must process every unit in the admission. It may not stop after finding a favorable unit or review only the unit that triggered the inherited route. `Q_i` is used only to define a phase-2 sampling cell and an index-versus-verification comparison; it is never treated as truth. A screen nonresponse is `Q_UNKNOWN_SCREEN`, not exclusion.

Before any phase-1 labels are read, freeze the phase-2 cell list, fixed target counts `n_{2,h,q}`, maximum packet times, the workload budget, and the assignment algorithm. Every possible `(inherited stratum h, Q_i=q)` cell has a positive target count or an explicit census rule. Empty cells are recorded, not silently removed.

### Phase 2: independent admission-level verification

Within every observed `(h,Q=q)` cell, select admissions by a fresh SRS without replacement of fixed target size

`n_{2,hq}=min(N_{1,hq}, r_{hq})`,

where the nonnegative integers `r_{hq}` are frozen before any phase-1 labels and chosen by a deterministic maximin allocation subject to the registered total physician-hour budget and the inherited atom/stratum precision requirements. The protocol must register the resulting `r_{hq}` values, not merely an intention to oversample adverse cases. Thus

`pi2_i = min(1, r_{h_iq_i}/N_{1,h_iq_i}) > 0`

for every phase-1 admission in every nonempty cell, and the total inclusion probability is

`pi_i = pi1_i*pi2_i`.

If a cell is smaller than its target, it is a census; there is no replacement or adaptive top-up. If a registered budget cannot accommodate the fixed targets after the prelabel unit inventory and maximum packet-time rehearsal, the run is `NO_SELECTION`; the analyst may not reduce the adverse or unknown cells after seeing labels.

Phase-2 packet construction is performed by a separate sealed-data operator. Phase-2 clinicians receive the same complete all-unit admission packet, with route concealment, independent redaction, reciprocal chain, allowed context, relative chronology, and canonical DS context as applicable, but **never receive `Q_i`, any phase-1 label, the phase-1 sampling cell, inherited route, atom, stratum, weight, or phase-1 response**. They are roster-disjoint from phase-1 screeners and extraction/route analysts. The phase-2 actionability and supersession panels use the byte-frozen `pulmonary_actionability_supersession_v1` ontology and independently write their labels, quoted spans, missing-facts checklists, packet validity, and redaction audits.

Every phase-2 admission receives every phase-2 review for every inherited unit: two independent actionability readings and two separately rostered supersession readings. There is no unit sampling, no within-admission selective verification, no consensus replacement of individual labels, and no stopping after a safe or adverse unit. The Cartesian compatibility mapping remains exactly the parent mapping: `K_U` for invalid/unknown/boundary or active-versus-no-action conflict; `K_N` for any compatible completion/stop/exact replacement; `K_R` for active choice/modification; and `K_P` only for a singleton portable-active plus none/restatement configuration. Any `K_U`, `K_N`, or `K_R` blocks `AUTO`; mixed `K_P/K_R` can at most support descriptive `RECON`; all `K_N` remains operationally `DEFER`.

### Why this is not verification-biased

The phase-2 panel is independent of the phase-1 screen in both information and personnel. The phase-2 sample is not restricted to screen positives, apparent `AUTO`, or apparent safe cases. Every phase-1 result class has a known nonzero `pi2_i`; screen-positive oversampling is allowed only through the frozen `r_{hq}` values and is fully represented in the design weights. Phase-2 response, packet quality, and missing labels cannot alter inclusion probabilities or trigger selective resampling.

The protocol reports phase-2 coverage and missingness by every `(h,Q,atom)` cell. A cell with zero phase-2 observations, zero effective sample size, or nonpositive inclusion probability is not interpreted through complete cases or imputation; its atom is inconclusive and maps to `DEFER`. Agreement with the screen is estimated after inverse-probability weighting, not by comparing the verified subset as though it were a random sample of the target population.

The phase-1 screen result is frozen before phase-2 selection, but it is not a post-treatment clinical outcome. Conditional sampling on it is valid for design-based estimation only because `pi2_i` is known for each admission and every result class remains represented. The phase-2 clinicians' concealment prevents anchoring and incorporation bias. The phase-2 panel remains fallible; it is a second measurement, not a gold standard.

## Admission-cluster estimands and atom-level precision

The sampling unit is always the admission. Let `U_i` be the complete inherited unit inventory for admission `i`, let `R_i` be its phase-1 screen class, and let `V_i` be a phase-2 admission-level vector containing the full Cartesian compatible-set result, any-unit adverse indicators, route comparison, packet validity, response status, control error, and active reading hours. No unit receives an independent probability or weight.

For any atom `g` and admission-level quantity `y_i`, estimate the finite-population total and mean with the two-phase Horvitz–Thompson and Hájek estimators

`T_g(y)=sum_{i in S2,g} y_i/(pi1_i*pi2_i)`

and

`P_g(y)=T_g(y)/T_g(1)`.

The primary vectors include at least: `I(any K_U or K_N or K_R)`, `I(candidate-AUTO-compatible)`, `I(candidate-RECON-compatible)`, `I(any phase-2 packet/control failure)`, `I(Q_i != phase-2 compatible class)`, and the number of units. Report weighted totals, denominators, atom-specific effective sample size, maximum weight, design effect, and simultaneous finite-population confidence bounds. A phase-2 admission with 20 units contributes one admission-level outcome and retains all 20 units in the adverse calculation; it is not 20 independent observations.

Use the exact stratified two-phase variance calculation with first-phase and conditional second-phase without-replacement covariance, or a design-valid Rao–Wu rescaled bootstrap that resamples admissions within every first-phase stratum and every conditional `(h,Q)` cell while preserving all nested units, labels, controls, weights, and atom membership. The bootstrap must not resample units independently, treat phase-2 labels as fixed truth, or collapse phase-1 cells. Retain at least 20,000 replicates where the parent requires them and use one max-statistic simultaneous 95% family over inherited gates, atom-level compatible outcomes, phase-1/phase-2 discrepancy, calibration contrasts, workload, and registered-policy endpoints.

Atom precision is checked separately; pooled safety or agreement cannot rescue a deficient atom. Before labels, calculate the attainable worst-case interval width from `N_g`, the frozen `r_{hq}`, the first-phase allocation, and maximum weights. An atom whose phase-2 allocation cannot meet the inherited precision requirement or whose realized effective sample size, upper weight, or simultaneous interval is inadequate is `INCONCLUSIVE`, not merged with a neighboring atom. The atom retains its exact `E`, terminal service, and `W`; residual, unknown, and novel signatures remain `DEFER`.

## Shared error and adverse routing

No amount of phase-1/phase-2 agreement identifies clinical truth. Both teams may share an incorrect ontology, missing context, or a systematic interpretation of the same MIMIC artifacts. Preserve the parent's complete integer contamination frontier at the **admission** level. For each atom, for every `m=0,...,N_g`, allow up to `m` complete admissions to have an unobserved true decision need outside every observed phase-2 compatible set. Reassign all units of a contaminated admission together, prioritize high-weight admissions in the adverse program, and report bounds for candidate-AUTO adverse compatibility, candidate-RECON adverse compatibility, no-action/supersession compatibility, capture, and workload.

The phase-1 screen cannot reduce the contamination allowance. Synthetic controls establish software/ontology responsiveness only; phase-1/phase-2 disagreement estimates measurement discordance, not shared clinical error. `m=0` is a descriptive optimistic baseline, not a safety assumption. Without a pre-label independent actual-workflow source capable of exposing errors shared by both MIMIC panels, the policy frontier uses `m=N_g` for any claim that would nominate a route. This generally prevents a retrospective AUTO/RECON nomination by design, while still allowing an explicit result that the MIMIC system is or is not ready for a prospective bridge.

For each observed phase-2 admission, all compatible states are retained. A single adverse minority unit blocks the admission-level candidate route. A phase-1 apparent safe admission that is not phase-2 verified is **unverified**, not safe and not routed. A phase-2 failure, nonresponse, leaked packet, unknown, or boundary defect is adverse for route eligibility and included in the weighted missingness/quality outcome. There is no default assignment of unverified admissions to `RECON`; unverified means `DEFER` at the individual level.

## Measurement-integrity controls and workload certificate

The parent's byte-frozen ontology and calibration fixtures remain required. Before real labels, independently verify schema, Cartesian compatibility mapping, all-unit precedence, phase-1 class mapping, two-phase inclusion-probability arithmetic, cell-size and census rules, and nested bootstrap fixtures with zero implementation errors. Use the matched decisive-versus-invariance confidence contrast and route-realization flip comparison already registered by the parent. A missing control response is an error.

The four-reading cost is incurred only for phase-2 admissions. Phase-1 maximum active time for each unit/packet type and phase-2 maximum active time are measured in a synthetic-only rehearsal. Before labels register the fixed `r_{hq}`, absolute physician-hour budget, reviewer weekly caps, roster-disjoint assignments, control burden, redaction/audit burden, reserve, and deadline. Compute the worst-case planned burden using the fixed phase-2 cell targets, all phase-1 unit inventories, every control packet, and the prespecified reserve. Phase-1 processing is complete for every phase-1 admission; phase-2 processing is complete for every unit of every selected phase-2 admission. If the certificate fails, the run is `NO_SELECTION`; do not drop apparently difficult admissions, limit verification to one unit, or top up only favorable cells.

The phase-2 sample may be enriched for `Q_ADVERSE_SCREEN` or `Q_UNKNOWN_SCREEN` to learn where the screen fails, but enrichment never changes the finite-population estimand. A separate descriptive case-enrichment table is permitted only if it is clearly labeled nonrepresentative and cannot be used for a route gate. All primary estimates use `pi1_i*pi2_i`.

## Baselines and falsification fixtures

Required comparisons include the inherited text-only route; the phase-1 screen; the independently concealed phase-2 panel; phase-1/phase-2 weighted and unweighted comparisons; phase-2 route-revealed versus route-concealed controls; H1/H2/H3 agreement; favorable consensus; a unit-level analysis shown only as an invalid sensitivity demonstration; pooled versus atom-specific results; `m=0` and `m=N_g`; and complete-case, imputed, shrunken, or latent-class analyses displayed as non-gating diagnostics. None may nominate a route.

Executable fixtures must include: phase-2 selection with positive probability in every phase-1 result class; screen-positive-only selection rejected; leaked `Q_i` in a phase-2 packet rejected; phase-1 nonresponse retained as `Q_UNKNOWN_SCREEN`; all-unit adverse minority propagation; two admissions with different unit counts showing admission-cluster rather than unit weighting; high-weight phase-2 missingness; zero phase-2 cell; atom-safe/pooled-unsafe and pooled-safe/atom-unsafe masking; fixed-target census behavior; no replacement/top-up; first- and second-phase probability arithmetic; conditional finite-population variance; contamination-curve monotonicity; workload overload; roster overlap; route access before seals; and a claim checker that rejects “clinical truth,” “safety,” “benefit,” “responsibility,” and operational `AUTO`/`RECON` conclusions from MIMIC-only output.

## Interpretation and conclusion contract

### Supportive result

A supportive result requires all inherited gates, exact source lineage, successful calibration and seal checks, positive phase-2 inclusion probability in every nonempty phase-1 cell, complete all-unit phase-2 review, valid cluster-weighted estimands, adequate atom precision, no uncontained adverse-compatible admission pattern, and an informative contamination frontier. It supports this narrow conclusion only:

> In the frozen MIMIC source and prespecified two-phase measurement design, the index screen and independently route-concealed verification measurement provide bounded evidence sufficient to design/launch a prospective silent measurement/workflow bridge for the exact atom, subject to fresh governance.

It never supports a live alert, automatic recommendation, reconciliation instruction, clinical safety, clinical truth, benefit, or transport to another institution. If the external actual-workflow/shared-error bound and independent utility governance are absent, the prospective mapper remains `DEFER` despite a favorable internal measurement result.

### Adverse result

An observed phase-2 adverse-compatible unit, phase-1/phase-2 discrepancy concentrated after weighting, route anchoring, failed decisive controls, missing/invalid packets, a zero or weak phase-2 cell, atom-level imprecision, workload overload, or a zero/insufficient contamination breakdown excludes that atom from bridge readiness. A phase-1 apparently safe result cannot offset a phase-2 adverse result, and pooled safety cannot offset atom-level failure.

### Inconclusive result

An unavailable phase-2 cell, nonpositive probability, high unverified leverage, excessive interval width, unresolved packet defects, absent external shared-error evidence, absent independent utility registration, or an incomplete workload certificate is inconclusive and fail-closed. It maps to `DEFER` and never defaults to `RECON`. The design should report why the evidence was insufficient rather than recoding uncertainty as no action.

## Evidence ceiling and required next study

MIMIC lacks actual report delivery/view/acknowledgement, discharge sign/transmit history, physical departure workflow, named responsibility, outside-system plans, target-linked orders/referrals/scheduling, completed imaging, duplicate imaging, radiation/contrast burden, patient preference, downstream cascades, diagnostic outcomes, workload displacement, and causal outcomes. `storetime`, `services`, and ICU exposure are proxies, not those events.

A stronger claim requires a prospective consecutive-admission silent bridge with immutable actual-calendar logs for report finalization/addenda, delivery/view/acknowledgement, discharge versions/sign/transmission, physical departure, named responsibility, target-linked replacement rationale, orders/referrals/scheduling, outside-plan attestation, patient preference/competing-risk context, and follow-up. Route-blinded adjudication must preserve the admission-level all-unit rules. Only a later governed comparative study can evaluate live safety, utility, unnecessary imaging, patient-reported effects, diagnostic outcomes, workload, or causal benefit.

## What changed and remaining tradeoffs

Compared with the parent, this child changes only the clinical-validation layer and its conclusion contract. It replaces four clinical readings for every phase-1 admission with one all-unit phase-1 index screen plus four all-unit readings for a fixed nested phase-2 admission sample. It adds explicit positive-probability verification in every screen-result cell, phase-2 information and roster concealment, admission-cluster estimands and variance, fixed conditional targets, and an individual-versus-population DEFER rule. It retains the parent's adverse Cartesian ontology and integer shared-error frontier rather than pretending that a smaller panel is truth.

The tradeoff is wider uncertainty and less direct individual-level coverage: unverified phase-1 admissions cannot be declared safe or routed, and a screen that fails in a rare result cell may make the entire atom inconclusive. The design also remains potentially infeasible for atoms with many units, because phase-2 coverage is admission-complete by construction. That burden is deliberate: reducing it by sampling units would invalidate the all-unit adverse estimand. The benefit is a feasible, transparent path to learn whether a prospective silent bridge is warranted without verification bias, false precision from clustered units, shared-error overclaim, or a conclusion that MIMIC cannot support.
