# A multiphase, futility-curtailed holistic audit under the fixed pulmonary-nodule workload

## Decision question and targeted repair

The frozen decision is whether any admission-level `AUTO`, `RECON`, `TIMING`, or `DEFER` route in the first-eligible MIMIC pulmonary-opportunity population is sufficiently reproducible, with sufficiently low text-defined adverse cross-route contamination, to nominate only a prospective **silent** within-site validation. It is not a decision to deploy a route, and it is not a test of guideline appropriateness, clinician performance, follow-up completion, harm, or benefit.

Parent `[prior hypothesis]` usefully challenges correlated text error with two independently written holistic codebooks, a roster-disjoint senior assertion review, and perturbation controls. Its blanket layering is inefficient: applying H1, H2, H3, and four transformed controls to essentially every challenge admission consumes many readings while stringent atom-level simultaneous bounds may already be mathematically incapable of passing. The parent also allocates only a fixed challenge fraction and then asks sparse atom-specific gates to carry the decision.

This targeted child preserves the inherited population, chronology, canonical discharge artifact, exhaustive states, split-view seals, route-independent all-route audit, every-unit worst-case routing, pre-label support atlas, domain-specific no-rescue rules, adverse finite-population inference, default `DEFER`, and the `<=900` distinct-admission ceiling. It replaces blanket challenge review with a **registered three-phase probability design**, a smaller two-control assay, and **failure-only curtailment**. H3 effort is concentrated in disagreement classes without ever showing H3 the earlier labels and without treating consensus as truth. All phase probabilities remain known and positive; no favorable early stopping, top-up, replacement, or reuse of saved effort is allowed.

## Evidence already supported, unresolved claim, and hypothesis

The configured sources support the computable facts that admission-linked radiology text, reciprocal addendum metadata, one canonical discharge-summary row per observed discharge key, service histories, ICU exposure, and storage-time proxies can be joined. Complete profiling inherited from the parent found 546,028 admissions, 364,627 patients, 593,071 service rows, 94,458 ICU stays, 2,321,355 radiology rows (`RR=2,295,635`, `AR=25,720`), 6,046,121 radiology-detail rows, and 331,794 `DS` rows with 331,794 unique `(subject_id,hadm_id)` keys, no duplicate keys, and 17 missing `DS.storetime` values. These are feasibility facts, not clinical truth.

The unresolved claim is whether an explicit support-qualified workflow atom that passes the inherited component audit also passes an independently worded whole-admission challenge when the challenge is estimated by valid multiphase sampling rather than exhaustive duplicate review. The falsifiable hypothesis is:

> At least one pre-label challenge-claimable atom, and every atom placed on a route allow-list, will satisfy all inherited gates plus the same adverse holistic disagreement, assertion-support, control-invariance, route-sensitivity, missingness, and workload margins under simultaneous finite-population bounds. Any atom that cannot still pass under the most favorable completion of its unopened scheduled reviews will be curtailed and excluded.

Agreement is only reproducibility evidence. Even unanimous H1/H2/H3 labels cannot identify arbitrary common-mode clinical error. The strongest possible supportive conclusion is therefore nomination of exact observable signatures for prospective silent validation, with all unlisted, rare, unknown, residual, novel, curtailed, or inadequately verified signatures forced to `DEFER`.

## Exact MIMIC sources, tables, joins, and times

Use read-only snapshot `[source checksum]`.

### Core archive

Source `[internal dataset path]`, [source checksum]:

* member `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`, schema [source checksum]; columns `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`; key `(subject_id,hadm_id)`, with frozen departure proxy `D=dischtime`;
* member `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`, schema [source checksum]; columns `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`, joined on `subject_id`; adult age is the inherited `anchor_age + year(admittime) - anchor_year >=18`, and `anchor_year_group` is used only for the inherited widened possible-calendar class;
* member `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`, schema [source checksum]; columns `subject_id,hadm_id,transfertime,prev_service,curr_service`, joined on `(subject_id,hadm_id)`; only nonmissing `transfertime<D` can define the terminal service and service path;
* member `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, schema [source checksum]; columns `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`, used only for diagnostic workflow partitions and never to repair a route or service label; and
* member `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`, schema [source checksum]; columns `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`, joined on `(subject_id,hadm_id)`, with a valid admission-linked `intime<D` defining pre-departure ICU exposure.

Members `mimic-iv-3.1/hosp/poe.csv.gz` and `mimic-iv-3.1/hosp/poe_detail.csv.gz` remain prohibited from primary packets, labels, domains, routes, estimands, and gates.

### Notes

* `[internal dataset path]`, [source checksum], table `note/radiology`, schema [source checksum]; columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; join to admissions on `(subject_id,hadm_id)` and identify notes by `(subject_id,note_id)`;
* `[internal dataset path]`, [source checksum], table `note/radiology_detail`, schema [source checksum]; columns `note_id,subject_id,field_name,field_value,field_ordinal`, joined only on `(subject_id,note_id)`, retaining every ordinal and reciprocal `parent_note_id`/`addendum_note_id` relation;
* `[internal dataset path]`, [source checksum], table `note/discharge`, the same eight note columns and schema hash, restricted exactly to `note_type=="DS"`, with canonical key `(subject_id,hadm_id)`; and
* `[internal dataset path]`, [source checksum], table `note/discharge_detail`, schema [source checksum]; columns `note_id,subject_id,field_name,field_value,field_ordinal`, joined only on `(subject_id,note_id)`. Retain `author` as observed metadata, never as a section or responsibility ontology.

Raw shifted dates are not cross-subject real dates. `curr_service` and ICU exposure are workflow proxies, not validated ownership.

## Frozen population, artifacts, states, and routes

Reproduce the parent's complete high-recall retrieval and retrieval-negative audit. Candidate reports are exact admission-linked radiology rows with `charttime` in `[admittime-12h,D]` and an inherited pulmonary/nodule/opacity, recommendation, interval, thoracic-CT, or exam-code/name trigger. Two roster-disjoint eligibility physicians see only the reciprocal radiology chain, permitted admission/death/disposition fields, and independently redacted context. Disagreement remains `U_R`; consensus cannot erase it.

The finite population `N_A` remains the first eligible admission per `subject_id`, sorted by `admittime` then `hadm_id`: adult; incidental pulmonary nodule or indeterminate focal nodular opacity; patient-specific unconditional chest/thoracic CT at exactly 3, 6, or 12 calendar months. Preserve exclusions for screening, established or oncologic surveillance/staging, conditional or optional plans, explicit no follow-up, in-hospital death, locked hospice/comfort-only transition, and recommendations first introduced after `D`. Do not infer size, smoking, malignancy risk, life expectancy, or appropriateness.

A usable report/addendum chain requires admission- and subject-consistent reciprocal `AR` parent and `RR` addendum links. Every operative node needs `charttime<=D` and `storetime<=D`; missing, one-way, contradictory, unresolved, or mistimed chains remain `U_R`. Require exactly one canonical `DS`; missing text/linkage/`storetime`, unreadability, contradiction, or duplicate canonical key is unknown or stops the run exactly as inherited. `charttime` never substitutes for `storetime`.

Preserve departure `Y={F,C_O,C_I,R,A,U_D}`, availability `V={V_D,V_24,V_72,V_168,V_late,V_U}`, lag `H={H_stale,H_0_6,H_6_24,H_24_72,H_72plus,H_U}`, eventual `Z={F_text,C_O_text,C_I_text,R_text,U_text}`, and every zero/unknown joint cell. For every operative unit `u`, retain `R_store,u`, `DS_store`, `G_u=DS_store-R_store,u`, and verify `D-R_store,u=(D-DS_store)+G_u`. Only unit-specific `G_u` governs opportunity; every active unresolved unit must have known `G_u>=24h` before a content route is possible.

The recommendation unit remains the smallest operative `(target cluster, action/modality, due interval/date, polarity)` tuple. Reciprocal restatements are deduplicated, material addenda revise rather than duplicate, and unresolved splitting/coreference is `U_BOUNDARY`. Units are nested and are never sampled or weighted. Preserve sealed roster-disjoint `R-I/K-I/S-I` index and `R-A/K-A/S-A` audit views, two immutable lanes, de-novo all-route review, independent redaction and senior minority-unit audits for every sampled admission, packet/access hashes, and route-after-seal execution.

Locked cross-products retain all compatible states and apply the inherited precedence: any `U_DEFER` gives `A_DEFER`; otherwise any `U_TIMING` gives `A_TIMING`; all resolved/closed gives `A_NOACTION`; `A_AUTO` requires every open unit wholly omitted with ample unit clock and no boundary/redaction/cross-unit conflict; all incomplete, conflicting, interaction-dependent, or mixed cases give `A_RECON`, with `A_MIXED` nested in `RECON`. A non-singleton robust route set is decision-faced as `DEFER`, and one adverse minority unit controls the admission.

## Frozen support atlas and challenge-claimability screen

Preserve the parent's atom exactly as `g=(E, exact terminal curr_service, W)`. `E` is derived from the widened possible admission-year interval using `anchor_year_group` and shifted-year offset and is one of `E_EARLY,E_LATE,E_BRIDGE,E_UNKNOWN`. `W` is exactly `W_SIMPLE,W_INTERMEDIATE,W_COMPLEX,W_UNKNOWN` from valid pre-`D` service transitions and ICU exposure. Tied terminal services, absent/malformed chronology, and unknown components remain unknown. No exact service code is regrouped after labels.

Preserve the parent's initial support threshold `N_g>=max(30,0.02*N_A)`, deterministic pruning into `RESIDUAL_h`, within-stratum maximin allocation, positive `pi_i` and `pi_ij`, and fixed five outcome-blind phase-1 strata `S_SENTINEL,S_TIMECLOCK,S_ZERO,S_PARTIAL,S_COMPLETE`. Preserve its sample sizes: sentinel census; `S_ZERO` the larger of 300 or the finite-population worst-case 95% +/-4-point formula; each other noncensus stratum the larger of 120 or the +/-7-point formula, capped at `N_h`. Their sum must be `<=900`, otherwise `NO_SELECTION`. Every selected admission receives all inherited component, redaction, and minority-unit audits.

Before any real label is opened, add a **challenge-claimability screen** without changing the parent atlas. For each parent-atlas atom, compute whether any allocation under the fixed phase-2 and phase-3 capacities below could pass the prespecified simultaneous gates even under zero adverse events, complete response, and all admissions route-positive. Use exact finite-population inversion with the predeclared max-statistic critical value. If an atom cannot pass even in that best case, label it `CHALLENGE_UNDERPOWERED` before labels. It remains represented in phase-1 and residual safety summaries but cannot enter any route allow-list and prospectively defaults to `DEFER`. This is non-support, not an adverse clinical finding. Publish the best-case bound and binding capacity constraint; do not change thresholds, merge atoms, or borrow information to make an atom claimable.

## Three-phase probability verification

### Phase 1: inherited audit, at most 900 distinct admissions

Run the inherited probability sample and all inherited reviews unchanged. Let its inclusion probability be `pi_i`. Route, atom, outcome, reviewer response, and workload labels are unavailable when later packet manifests and initial allocations are sealed.

### Phase 2: paired independent holistic challenge

Select at most `K2=360` of the phase-1 admissions for holistic review; if phase 1 contains fewer than 360, census it. Use stratified SRS without replacement in the crossed phase-1 design cells `(h,g)` plus `RESIDUAL_h`. Allocation is frozen before labels:

1. give every occupied cell positive inclusion and at least two records when possible;
2. among challenge-claimable atoms, maximize lexicographically the minimum planned phase-2 count per atom, then minimum count over possible-calendar, exact-service, and workflow margins;
3. allocate remaining positions toward population-proportional allocation while minimizing the largest projected normalized final weight; and
4. break ties lexicographically by `(h,E,service,W)`.

If `K2` cannot give every occupied cell positive inclusion, or cannot give a candidate atom at least two records in every occupied phase-1 cell, that atom is `CHALLENGE_UNDERPOWERED`; no cell is dropped. Let the known conditional probability be `q_i=n2_hg/n1_hg`, so phase-2 inclusion is `pi_i*q_i>0`. Freeze the integer program, solution, seed, order, IDs, `q_i`, and pairwise probabilities. No route-, label-, disagreement-, response-, or workload-based phase-2 top-up is permitted.

Each phase-2 admission is independently packetized twice from the sealed raw extract. H1 and H2 have disjoint rosters, pseudonyms, packet orders, and no communication. `CB-H1` and `CB-H2` are separately authored, differently ordered, differently exemplified codebooks with no shared real training cases; both are hashed before packet generation. Packets contain the reciprocal pre-`D` radiology chain, permitted admission/death/disposition fields, canonical `DS` and permitted detail metadata, and explicit missing/time metadata, but no component labels, route, stratum, atom, weight, POE, post-`D` text, or outcome. Both record de-novo unit inventory and atomic target/action/timing/recipient/responsibility/polarity/replacement/conflict evidence. Routes are derived only by locked code after both append-only labels seal; neither reviewer votes on a route.

### Phase 3: disagreement-stratified senior verification

After H1/H2 and inherited component labels are append-only sealed, but before any outcome summary is computed, classify every completed phase-2 admission using only direction-free disagreement indicators:

* `C0`: H1 and H2 have identical unit inventory and singleton route set and agree with the inherited robust route set;
* `C12`: H1 and H2 disagree in unit inventory, atomic assertion, or compatible route set;
* `CP`: H1/H2 agree with each other but their route set differs from or is more favorable than any inherited compatible route; and
* `CU`: packet/label nonresponse, corruption, or an unknown preventing classification.

No class distinguishes favorable from adverse route direction, and classes are hidden from H3. Select at most `K3=120` phase-2 admissions by stratified SRS without replacement within `(g,C)` plus residual. Give every occupied cell positive probability and at least two if noncensus and feasible; then maximize coverage of `C12`, `CP`, and `CU` subject to retaining positive `C0` probability and minimizing maximum final weight. If minima exceed 120, affected atoms are challenge-underpowered; do not collapse atoms or disagreement classes. Let `r_i=n3_gC/n2_gC`, with final inclusion `pi_i*q_i*r_i>0`. Selection depends on sealed disagreement class but never route direction or H3 result, and its probability is exactly recorded.

H3 is roster-disjoint from all earlier roles and receives the same unmarked whole-admission packet in independently randomized order. H3 sees no H1/H2 or component output, class, route, domain, or weight. It labels whether each route-defining textual assertion is `supported`, `contradicted`, or `indeterminate`, independently enumerates units, and provides atomic evidence. H3 is another measurement system, not a truth oracle and not a consensus adjudicator. H1, H2, H3, and parent labels all remain in the compatible-set analysis.

A planned nonsampled admission is not treated as missing; it is represented by its known sampling probability. Failure to obtain a scheduled label, packet corruption, access failure, or withdrawal is adverse-compatible. For H1/H2 quantities use weights `1/(pi_i*q_i)`; for H3 quantities use `1/(pi_i*q_i*r_i)`. No complete-case substitution is allowed.

## Smaller, probability-sampled codebook assay

The parent's four transformed pairs partly duplicate one another and test internal behavior rather than clinical correctness. Replace them with two locked controls on at most `KC=80` phase-2 admissions selected before H1/H2 labels by positive-probability stratified SRS across claimable atoms and residual:

1. one **route-invariant pair** that changes only formatting, section order, or signature-like nuisance tokens while preserving every route-relevant span; no unit or route change is allowed; and
2. one **single-field decisive pair** that changes exactly one unambiguous atomic field, such as explicit replacement or an ample versus under-24-hour clock statement, with the exact compatible-route transition frozen in the transformation manifest.

Transform only parser-unambiguous cases; parser-infeasibility is recorded and adverse for the assay missingness gate. H1 and H2 see randomized pair order without transformation identity. Controls never alter real-case labels or estimands and cannot rescue a real-case failure. Use inclusion `pi_i*q_i*c_i` and design-based bounds. There is no omission/addition or separate nuisance pair beyond these two, reducing transformed reads while retaining a direct invariance and sensitivity test.

## Prespecified failure-only curtailment

Freeze a random review order and inspect gates only after blocks of 20 completed paired H1/H2 admissions within an atom and after blocks of 10 H3 admissions within an atom. At each boundary, enumerate **all** compatible assignments for every scheduled but unopened label, nonresponse state, H3 result, and control result. Include the frozen finite-population weighting and simultaneous-bound procedure.

Stop further challenge review for atom `g` only if **no possible completion, including the most favorable one, can satisfy every challenge gate**. Mark it `CHALLENGE_FAIL_FUTILITY`; retain all observed labels and report which gate made passage impossible. Saved packets and physician-hours are not reassigned, substituted, or used to enlarge another atom. There is no early declaration of success: every atom still capable of passing receives its full scheduled H1/H2, H3, and control sample. A global stop is allowed only when every remaining atom is mathematically incapable of passing or a seal/source failure invalidates the run.

This rule cannot preferentially retain a favorable atom by stopping after good results. A stopped atom is permanently excluded. For inherited phase-1 outcomes, ordinary finite-population inference remains unchanged. For an incompletely challenged stopped atom, report the observed plus best/worst completion identified set; do not claim a design-unbiased challenge point estimate. The adverse certification endpoint uses the worst compatible completion, while the impossibility proof establishes that even the best completion failed.

## Estimands and finite-population inference

Preserve every inherited phase-1 total, burden, chronology state, confirmation measure, `C_AUTO`, `D_MIX`, `Se_RECON`, `PPV_RECON`, `PPV_TIMING`, `Se_DEFER`, `leak_AUTO`, additional-unit rate, one-to-multiple error, and workload estimand. The inferential unit is the admission. Preserve the parent's adverse `AUTO` definition: `d_i=1` if either initial index lane calls `AUTO`; `x_i=1` if any other index lane, audit-compatible route, minority-unit finding, missing audit, redaction/boundary failure, timing limitation, or adverse unknown permits `RECON`, `TIMING`, or `DEFER`; estimate `C_AUTO=sum x_i/sum d_i` as a Hájek ratio of HT totals, always reporting numerator and denominator.

For each atom and route, add:

* H1/H2 unit-inventory and route-set disagreement;
* parent-versus-H1/H2 adverse route discordance;
* H3 contradiction/indeterminacy of any route-defining assertion;
* adverse compatible route discordance across all available parent/H1/H2/H3 outputs;
* route-invariant flip and single-field decisive-violation rates;
* scheduled-label nonresponse/corruption and assay infeasibility; and
* physician minutes, packets, and transformed presentations per 100 atom admissions.

Use multiphase Horvitz-Thompson totals and Hájek ratios with the probabilities above. Variance must include phase-1, phase-2, and phase-3 sampling. Implement either the exact nested finite-population variance decomposition or at least 20,000 nested Rao-Wu rescaled replicates: resample within phase-1 `(h,g)` cells, then reproduce phase-2 sampling within each replicate, then reproduce phase-3 `(g,C)` selection while keeping every admission's units, labels, response, and time together. Census stages contribute zero sampling variance. Validate against exact enumeration in small finite populations.

For binary totals use exact stratified hypergeometric inversion; for ratios such as discordance among candidate-route admissions use multivariate-hypergeometric enumeration of `{adverse candidate,nonadverse candidate,noncandidate}` where feasible. Report the widest valid endpoint from exact inversion, nested bootstrap, and adverse compatible-set optimization. A single max-statistic simultaneous 95% family covers inherited route gates, all claimable atoms, H1/H2 disagreement, H3 contradiction/indeterminacy, controls, missingness, minimax endpoints, and workload. Zero observed events in a noncensus phase has a positive upper bound. Planned nonsampling is weighted; scheduled nonresponse and semantic unknowns are adverse. Latent-class models, favorable consensus, hierarchical shrinkage, regression, and model imputation are diagnostics only and cannot narrow a gate.

## Gates, no-rescue logic, and falsification

Governance must approve thresholds and the absolute physician-hour/packet budget before labels. Preserve all inherited source, retrieval-negative, population, chronology, canonical-artifact, seal/access, event-count, ESS, precision, route, workload, and atlas gates, including `tau_AUTO=0.05`, confirmation `>=0.90`, AC1 `>=0.70`, `Se_RECON>=0.95`, `PPV_RECON>=0.80`, `PPV_TIMING>=0.95`, `Se_DEFER>=0.95`, `D_MIX<=0.10`, and `leak_AUTO<=0.02` where applicable.

For challenge certification, retain the parent's margins but estimate them by the registered phases:

* simultaneous lower H1/H2/H3 assertion-support compatibility `>=0.90`;
* simultaneous upper parent-versus-holistic adverse route discordance `<=0.05` for `AUTO`, `<=0.10` for `RECON`, `<=0.05` for `TIMING`, and `<=0.10` for `DEFER`;
* simultaneous upper route-invariant flip rate `<=0.02` and decisive-control violation rate `<=0.05`;
* no adverse-compatible holistic result leaves an `AUTO` admission compatible with `RECON`, `TIMING`, or `DEFER` under the inherited worst-unit rule;
* scheduled challenge nonresponse/corruption plus control infeasibility upper bound `<0.05`; and
* atom-specific upper physician-hours and packet-time below the preapproved absolute budget.

A claimable atom also needs positive lower route burden, required inherited route-event counts, route-denominator ESS `>=50`, at least 10 non-sentinel route-positive challenge admissions, and normalized maximum final weight `<=0.10`. If staged sampling makes an endpoint too wide, the result is inconclusive/unsupported, not a pass.

No failing or underpowered atom can be rescued by pooled performance, another atom, a service macro-group, era adjacency, residual records, sentinel performance, consensus, H3 agreement, a control pass, imputation, regression, latent classes, shrinkage, or reallocating saved reviews. Unsupported/rare/unknown/residual/novel prospective signatures map to `DEFER`. One failing supported atom blocks unrestricted nomination but does not invalidate a separately passing allow-listed atom unless an inherited global gate fails.

Mandatory computational falsification fixtures are:

1. **multiphase coverage:** enumerate small unequal finite populations and verify HT totals, nested variance, and interval coverage using `pi*q*r`; an analysis using only `pi` must fail;
2. **disagreement enrichment:** oversample `C12/CP` heavily while keeping all `r>0`; weighted estimates must recover the finite-population H3 rate, while unweighted estimates must be detectably wrong;
3. **direction leakage:** swapping favorable and adverse route names while preserving disagreement indicators must leave the phase-3 sample unchanged;
4. **favorable-stop trap:** an atom with early perfect labels cannot stop or certify before its full schedule;
5. **futility trap:** an atom with enough adverse labels that even favorable completion cannot pass must stop, remain excluded, and donate no reviews to another atom;
6. **underpowered best case:** an atom whose zero-event simultaneous upper bound exceeds a margin must be marked challenge-underpowered before labels;
7. **domain masking:** pooled challenge performance may pass while one supported atom fails; that atom cannot be rescued;
8. **unknown/nonresponse:** missing scheduled high-weight labels widen adverse bounds; planned nonsampled records are weighted rather than called missing;
9. **shared-wrong fixture:** unanimous planted wrong labels may pass agreement but cannot be described as clinical truth and cannot narrow the prespecified common-mode-error sensitivity envelope;
10. **control fixtures:** formatting-only change cannot alter route, while one-field replacement/timing change can alter only the locked route-table field;
11. **worst-unit fixture:** one adverse unit among many safe units controls the admission; duplicated restatements alter neither route nor weight; and
12. **novel-signature fixture:** an unseen service/workflow signature maps to `DEFER` and cannot be nearest-neighbor matched.

Roster overlap, shared H1/H2 codebook text or examples, H3 visibility of earlier labels/classes/routes, route-before-seal computation, post-label phase-2 allocation, phase-3 selection using disagreement direction, saved-work reallocation, replacement, favorable unknown assignment, or complete-case certification invalidates the affected analysis.

## Supportive, adverse, and inconclusive interpretations

**Supportive:** all inherited global gates pass; at least one pre-label challenge-claimable atom completes its full schedule and independently passes every simultaneous route, holistic, control, missingness, ESS/weight, worst-unit, and workload gate; every atom in the stated allow-list passes; and minimax endpoints over that allow-list pass. This supports only a prospective silent test of the frozen route process for those exact observable MIMIC signatures, with all others forced to `DEFER`.

**Adverse:** an adequately supported atom crosses a contamination, discordance, contradiction/indeterminacy, control, minority-unit, or workload margin, or reaches the failure-only stopping boundary. It is excluded even if pooled results and panel agreement look favorable. This is evidence against nominating that text-routing signature under the prespecified operational standard, not evidence of patient harm or clinician error.

**Inconclusive:** no atom is challenge-claimable under best-case precision; a staged cell lacks positive/estimable support; route events or ESS are sparse; simultaneous bounds remain too wide; challenge nonresponse or corruption is excessive; the fixed budget is infeasible; controls cannot be generated; seals fail; or H3 cannot be completed. Underpowered and inconclusive atoms still default to `DEFER`; neither is evidence of safety, failure, or transport.

The design is falsified if a stopped, underpowered, unsupported, unknown, or failing atom enters an allow-list; if weighted multiphase estimates do not recover known synthetic finite populations; if phase-3 selection changes with route direction; if a favorable early sequence can certify; or if pooled/consensus/model results rescue an atom-specific adverse bound.

## Evidence ceiling and prospective requirements

The verifier can check hashes, headers, joins, chronology, reciprocal links, canonical keys, unit clocks, atlas construction, phase allocations, positive first- and second-order probabilities, packet/codebook/roster seals, review order, stopping proofs, nested estimators, simultaneous bounds, no-rescue mapping, and whether reported conclusions follow from computed outputs. It cannot establish clinical truth, service ownership, actual note viewing, draft/final/signature semantics, physical-departure visibility, communication, responsibility, order/referral execution, scheduling, outside care, patient preference, malignancy, appropriateness, follow-up completion, harm, utility, causal benefit, or external/forward-calendar transport.

A retrospective pass therefore requires a separately approved prospective silent bridge with actual dates and observed report availability/viewing, discharge draft/version/edit/sign/transmission, physical departure, responsibility, orders/referrals/scheduling, outside-plan and preference/competing-risk evidence, and final transmitted artifacts. Novel signatures remain `DEFER`. Only a later governed trial with clinical adjudication and workflow/outcome data could test live safety, utility, or benefit.

## Substantive advance

This child turns a blanket, increasingly layered challenge into an auditable resource allocation problem. The fixed 360 paired holistic, 120 senior, and 80 two-control samples preserve known positive verification probabilities and atom-specific adverse inference, while disagreement-stratified H3 sampling spends senior effort where measurement systems diverge without revealing those divergences to H3. The pre-label best-case precision screen prevents impossible atoms from consuming scarce review, and failure-only curtailment saves work only after certification has become mathematically impossible; it never converts early favorable labels into success and never reallocates saved effort. The tradeoff is explicit: fewer readings may widen bounds and yield more `DEFER` or `NO_SELECTION`, but cannot manufacture a favorable conclusion.
