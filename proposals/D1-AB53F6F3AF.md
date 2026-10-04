# A governance-weight utility frontier for route-concealed pulmonary-opportunity routing

## Targeted repair and decision question

This child combines `[prior hypothesis]` and `[prior hypothesis]`. It preserves their frozen first-eligible, all-opportunity MIMIC population; reciprocal pre-departure radiology report/addendum chain; one exact canonical `DS`; unit-specific storage chronology; exhaustive `Y/V/H/Z` states; split-view and independent holistic adjudication; exact pre-label support atoms; all-unit worst-case admission routing and precedence; route-independent probability sampling; at most 900 distinct sampled admissions; adverse finite-population inference; no pooled, neighboring-atom, consensus, shrinkage, or latent-class rescue; default `DEFER`; and strict noncausal ceiling.

The remaining consequential weakness is decision governance. The parents can estimate reproducibility, actionability, supersession, contamination, and burden, but their fixed numerical release margins do not establish that `AUTO`, `RECON`, `TIMING`, or universal `DEFER` is the preferable next-study policy. A 5% contamination limit, 90% agreement requirement, or a single net-benefit threshold is an operational choice, not a clinically authoritative utility. Conversely, deleting thresholds without a decision analysis leaves universal `DEFER` implicitly privileged even when it may discard many supported textual opportunities.

The unresolved, falsifiable question is therefore: **after all inherited measurement and integrity safeguards, which exact support-atom/derived-route actions are dominated, robustly optimal, potentially optimal, or unresolved across a preregistered transparent set of governance loss weights?** The primary hypothesis is not that one route is best. It is that the data will eliminate at least one action by simultaneous robust dominance in at least one support-qualified atom-route cell, while any action proposed for a prospective silent bridge will remain optimal for every weight vector in a stakeholder-elicited set and every loss vector in the simultaneous design-based uncertainty set. Failure to obtain such a stable region is an informative `DEFER`, not evidence that no clinically useful policy exists.

Available MIMIC evidence can support only stored-text quantities: route-specific target-linked actionability, explicit/possible supersession, adverse-compatible text-defined unsafe rerouting, textual missed-opportunity proxies, and counts of review tasks plus retrospective packet-reading time. It cannot supply stakeholder utilities or establish appropriateness, actual visibility, responsibility, execution, safety, harm, benefit, or causal effects.

## Exact immutable data bindings

Use MIMIC snapshot `[source checksum]`. Sources are read-only; manifests, hashes, samples, packets, labels, replicate vectors, and frontier outputs are workspace derivatives.

Core source `[internal dataset path]`, [source checksum]:

* member `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`, schema [source checksum], columns `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`; key `(subject_id,hadm_id)`, frozen departure proxy `D=dischtime`;
* member `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`, schema [source checksum], columns `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; join `subject_id`, using only the inherited widened possible-calendar class, never shifted years as actual dates;
* member `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`, schema [source checksum], columns `subject_id,hadm_id,transfertime,prev_service,curr_service`; join `(subject_id,hadm_id)`, restrict `transfertime<D`, retain the inherited exact terminal-service rule;
* member `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, schema [source checksum], columns `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; diagnostics only;
* member `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`, schema [source checksum], columns `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; join `(subject_id,hadm_id)`, with admission-linked `intime<D` defining inherited ICU workflow exposure.

Note sources:

* `[internal dataset path]`, [source checksum], table `note/radiology`, schema [source checksum], columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`; admission join `(subject_id,hadm_id)`, note key `(subject_id,note_id)`;
* `[internal dataset path]`, [source checksum], table `note/radiology_detail`, schema [source checksum], columns `note_id,subject_id,field_name,field_value,field_ordinal`; join only `(subject_id,note_id)`, retain every ordinal and reciprocal `parent_note_id`/`addendum_note_id` rows;
* `[internal dataset path]`, [source checksum], table `note/discharge`, the same eight note columns and schema hash; exact `note_type=='DS'`, inherited sole canonical `(subject_id,hadm_id)` artifact;
* `[internal dataset path]`, [source checksum], table `note/discharge_detail`, schema [source checksum], columns `note_id,subject_id,field_name,field_value,field_ordinal`; join only `(subject_id,note_id)`.

`hosp/poe` and `hosp/poe_detail` remain prohibited from population construction, packets, labels, routes, atoms, estimands, utility components, and gates. The inherited source-profile counts—546,028 admissions, 364,627 patients, 593,071 service rows, 94,458 ICU stays, 2,321,355 radiology rows, 6,046,121 radiology-detail rows, 331,794 unique-admission `DS` rows, and 17 missing `DS storetime` values—remain feasibility checks, not clinical findings.

## Frozen population, chronology, support, and review workload

Construct the complete inherited `N_A`: one first eligible adult admission per subject, ordered by `admittime,hadm_id`; exact admission-linked candidate radiology in `[admittime-12h,D]`; reciprocal subject/admission-consistent pre-`D` report/addendum links; and the inherited pulmonary-nodule/focal-opacity, unconditional patient-specific 3/6/12-month thoracic-CT eligibility and exclusions. Preserve exactly the canonical artifact, every recommendation unit, `R_store,u`, `DS_store`, `G_u=DS_store-R_store,u`, the identity `D-R_store,u=(D-DS_store)+G_u`, all `Y/V/H/Z` states, unit matching, stale/post-`D` rules, split panels, holistic panels, compatible sets, and admission precedence. One adverse or unresolved unit controls the admission.

Preserve the outcome-blind atom `g=(widened possible-calendar class, exact terminal pre-D curr_service, workflow class)` and the inherited support atlas. Rare, residual, unknown, and novel signatures are never certified by pooling or similarity and prospectively map to `DEFER`.

Preserve the inherited five sampling strata and formula totals, sentinel census, positive first- and second-order inclusion probabilities, and `NO_SELECTION` if the master draw would exceed 900 distinct admissions. The actionability/supersession challenge remains nested in that master draw with `m=min(300,n)` and adds no admission. For executable compilation, use the prior assessed-valid total `ACTSUP-v2` allocation: census if `n<=300`; otherwise give each occupied atom one case if singleton and two if nonsingleton, distribute residual slots proportionally by deterministic largest remainder when the bases fit, and use a global 300-admission SRS fallback when they do not. Hash tie-breaking and within-cell order use `ACTSUP-v2`, `subject_id`, and `hadm_id`. Record phase-1 and conditional phase-2 `pi_i,pi_ij` separately and combine both phases in replication. An absent cell or route is unsupported, never topped up.

Retain route-concealed, roster-disjoint `ACT-A1`, independently rendered `ACT-A2`, supersession `ACT-S1`, and independent `ACT-H3` whole-admission readings, append-only seals, exhaustive actionability categories `A1_ACTIVE_PORTABLE` through `A6_UNKNOWN`, supersession categories `S0_NONE` through `S4_UNKNOWN`, locked controls, and route derivation only after every seal. The closed added ledger is four whole-admission readings and six linked control-pair assignments per challenged admission; at `m=300`, 1,200 whole-admission readings plus 1,800 linked control-pair assignments/3,600 card exposures, but still no more than 900 distinct admissions overall. This utility analysis reuses those labels and creates **zero** extra clinical readings. Record actual open-to-seal minutes, units, spans, and roster type; do not convert retrospective adjudication time into live-workflow time.

## Decision cells, candidate actions, and observable quantities

After all inherited labels are sealed, define decision cell `h=(g,r)`, where `g` is an exact final support atom and `r` is the inherited robust admission route before the added actionability/supersession layer. This does not redefine an atom or permit outcome-based regrouping. Candidate final actions are the finite conservative set allowed by the inherited route table:

* from `AUTO`: retain `AUTO`, downgrade to `RECON`, or `DEFER`;
* from `RECON`: retain `RECON` or `DEFER`;
* from `TIMING`: retain `TIMING` or `DEFER`;
* from `DEFER`: `DEFER` only.

No action may be more permissive than the inherited route. `TIMING` is not silently converted to `AUTO`; unsupported actions are absent, not assigned favorable zero loss. A global policy is a vector choosing one allowed action for every occupied `h`. Universal `DEFER`, the unchanged inherited policy, `AUTO`-to-`RECON`, and every atomwise conservative descendant are included. Because losses add over admissions, atomwise frontiers are primary; a deterministic dynamic program or mixed-integer linear program enumerates global nondominated policies without brute-force materialization.

For every `(h,a)`, report design-weighted admission totals, rates per 100 frozen opportunities, numerator/denominator totals, and adverse-compatible simultaneous intervals for:

1. **route-specific actionability `Q_ACT(h,a)`**: the fraction whose complete unit-compatible set satisfies the locked textual state required by action `a`—portable active and unsuperseded for `AUTO`; active but requiring resolution of recipient, timing, responsibility, plan, or conflict for `RECON`; active with inherited opportunity-clock limitation for `TIMING`. For `DEFER`, report rather than reward the active-unsuperseded mass it declines.
2. **supersession `Q_SUP(h,a)`**: the fraction exposed to an active route while any compatible unit is `S1`–`S4`, replacement, competing plan, or unknown. Explicit replacement dominates. Jointly supported `S0_NONE` contributes zero; disagreement and missingness contribute to the adverse upper endpoint.
3. **unsafe contamination `Q_UNSAFE(h,a)`**: the fraction for which any sealed compatible assignment requires a more conservative action than `a`, including an unresolved minority unit, route-changing actionability state, supersession, boundary/redaction failure, or required missing label. This remains text-defined contamination, not patient harm.
4. **missed opportunity `Q_MISS(h,a)`**: the fraction with jointly supported active, target-linked, unsuperseded text whose action is not retained for the silent bridge by `a`. Unknowns yield lower/upper compatible bounds. `TIMING` is counted as preserved only when its locked clock state and an explicit silent timing-queue task are both defined; otherwise it is adverse-compatible missed opportunity. This is missed *textual study opportunity*, not missed beneficial care.
5. **review demand `Q_WORK(h,a)`**: mandatory silent-workflow review assignments per 100 admissions under the frozen action contract—zero for `AUTO` and `DEFER`, one admission-level reconciliation assignment for `RECON`, and one timing-queue assignment for `TIMING`. Also report distinct unit tasks and retrospective packet minutes separately. These are computable workload-volume proxies; live clinician minutes and opportunity cost require prospective observation.

The five primary loss coordinates are `L=(1-Q_ACT, Q_SUP, Q_UNSAFE, Q_MISS, Q_WORK/100)`, each on the transparent scale of one affected admission or one mandatory review assignment per admission. Overlap is intentional: supersession is one mechanism of unsafe contamination, not an independent biological event. Preserve every admission's joint five-vector through all replicates; never multiply marginal probabilities or assume independent errors. Publish the raw quantities before any weighted loss.

## Preregistered loss-weight simplex and stakeholder boundary

Before labels, preregister the full normalized nonnegative simplex

`W0={lambda in R^5: lambda_k>=0, sum_k lambda_k=1}`,

where one coordinate expresses the governance exchange rate for one admission-level actionability mismatch, supersession exposure, unsafe text contamination, missed textual opportunity, or mandatory review assignment. Analyze the entire simplex, including vertices and boundaries; do not choose an equal-weight point, a single willingness-to-review threshold, a minimum region volume, or a contamination cutoff as the primary decision.

Governance may additionally provide a closed convex stakeholder set `W*` before route results are revealed, represented only by auditable linear inequalities and its elicitation provenance. Clinician, patient, safety, operational, and equity stakeholders may disagree; retain the convex hull or separately named sets rather than averaging them into a hidden point. If no independently elicited `W*` exists, the computable result is the full `W0` frontier and universal dominance only. Retrospective MIMIC may not manufacture weights. Any later `W*` is prospective governance evidence and cannot be described as learned from MIMIC.

For weight `lambda`, estimated loss is `D_h(a,lambda)=lambda^T L_h(a)`. Also report unnormalized component counts so a stakeholder can rescale a workload task differently without rerunning adjudication. Named legacy margins (for example 0.05, 0.90, 0.02, and 30/10 counts) remain visible as historical operational sensitivity overlays, not clinical utility truths and not a mechanism for rescuing an unsupported cell.

## Dominance, uncertainty, and fail-closed rules

Use inherited Horvitz–Thompson totals/Hájek ratios, exact finite-population inversion where mathematically applicable, and at least 20,000 two-phase Rao–Wu replicates. Keep all units, panels, compatible assignments, and five loss coordinates for an admission together. Use one simultaneous 95% max-statistic family covering inherited integrity/reproducibility quantities, every supported `(h,a)` loss contrast, atomwise and global-policy frontiers, and workload outputs. Optimize unknown/disagreement assignments jointly, not coordinate by coordinate when their shared compatible sets constrain them.

For each cell:

* `a` is **point-Pareto dominated** if another allowed action has no larger point estimate in every loss coordinate and a smaller estimate in at least one.
* `a` is **robustly dominated** if the simultaneous joint confidence set implies the same componentwise relation for all compatible finite-population loss vectors. This can safely eliminate `a` without selecting its competitor.
* The nominal optimal region is the exact polyhedron `R0(a)={lambda in W: lambda^T[L(a)-L(b)]<=0 for every b}`.
* The **robust-optimal region** `R-(a)` contains weights for which `a` has no larger weighted loss than every competitor for every loss vector in the simultaneous joint uncertainty set.
* The **potentially optimal region** `R+(a)` contains weights for which at least one loss vector in that set makes `a` optimal. The shell `R+(a)\R-(a)` is decision uncertainty, not evidence for either action.

Compute regions by linear programming over the simplex and the replicate/compatible-set support function; output vertices, half-space inequalities, adjacency, and simplex volume only as a descriptive geometric summary. Validate low-dimensional faces by exhaustive grid checks, but a grid never defines the answer. For global policies, use column generation/MILP and verify all returned policies by direct loss recomputation.

The precision gate is decision-based, not a new numerical width cutoff. A retrospective policy may be proposed for a prospective silent bridge only when: (i) every selected cell is pre-label support-qualified and all inherited source, chronology, seal, roster, control, positivity, all-unit, and estimability safeguards pass; (ii) every required loss vector and joint simultaneous set is defined; (iii) there is a preregistered stakeholder set `W*`; and (iv) the same policy is optimal for **every** `lambda in W*` and **every** compatible loss vector in the simultaneous set. Equivalently, `W*` must be wholly contained in that policy's robust-optimal region. If different policies win within `W*`, regions overlap only potentially, a denominator is zero, a bound is too wide, an atom is absent, or no `W*` exists, decision selection fails closed to `DEFER`. No arbitrary minimum simplex volume is imposed.

For `AUTO`, retain the stronger inherited safeguard: any observed adverse-compatible unresolved, superseded, conflicting, or nonportable unit blocks `AUTO` in that cell regardless of weighted utility. Controls remain zero-tolerance protocol integrity checks; passing controls cannot offset real-case loss. Pooled performance, neighboring atoms, macro-services, sentinel-only results, complete-case analysis, imputation, shrinkage, latent-class estimates, favorable consensus, or a high utility in another atom cannot rescue a failing or unsupported cell.

## Baselines, falsification, and verification

Apply the identical sample and labels to universal `DEFER`, unchanged inherited routing, every single-route conservative downgrade, point-estimate utility choice, equal-weight choice (diagnostic only), each legacy threshold screen, and pooled/macro/shrunken analyses. None may override the robust-region rule.

Mandatory fixtures include:

1. one policy with lower unsafe contamination but higher missed opportunity, producing a nontrivial simplex boundary rather than a single winner;
2. a componentwise dominated policy that is eliminated throughout `W0`;
3. correlated supersession/unsafe labels whose joint replicate frontier differs from an independence calculation;
4. point-optimal but not robustly optimal `AUTO`, which must `DEFER`;
5. two stakeholder weight polytopes selecting different policies, proving MIMIC did not determine utilities;
6. a `W*` crossing a decision boundary, which must yield no selection without a volume threshold;
7. an unsupported atom, zero route denominator, high-weight missing panel, and global-fallback absent cell, each widening/undefining regions and mapping to `DEFER`;
8. an observed superseded or unresolved minority unit that blocks `AUTO` even when some weights favor it;
9. pooled-safe/domain-unsafe and shrinkage-rescue traps;
10. universal `DEFER` winning when missed-opportunity weight is low and losing when it is high, without either result being called clinically authoritative;
11. exact reconstruction of master/challenge draws, phase probabilities, workload ledger, route seals, and all-unit precedence; and
12. claim checks rejecting appropriateness, actual safety, execution, benefit, causal, exact-calendar, forward-transport, or external-site language.

The verifier can check hashes, members, columns, joins, chronology, reciprocal links, population/sample membership, inclusion probabilities, packet/roster/seal integrity, compatible-set routing, workload counts, loss vectors, survey estimates, joint replicates, LP/MILP frontiers, dominance statements, `W*` containment, and whether conclusions follow. It cannot verify stakeholder legitimacy, clinical utility, service ownership, appropriateness, actual visibility, execution, harm, benefit, or causality.

## Interpretation and prospective bridge

A **supportive retrospective result** is not “AUTO is best.” It is an exact report that specified actions are robustly dominated and, only if an independently preregistered `W*` exists, that one conservative policy is decision-stable across all stakeholder weights and simultaneous loss uncertainty for an explicit allow-list. This supports only a separately approved within-site prospective silent bridge; all other signatures remain `DEFER`.

An **adverse result** is a well-supported region showing that an action is dominated or cannot be optimal for the declared stakeholder set, excess actionability mismatch/supersession/unsafe contamination, an `AUTO` blocking unit, or a protocol-control failure. It excludes that action/cell under this study but does not prove clinical harm.

An **inconclusive result** includes sparse or absent cells/routes, undefined ratios, broad overlapping robust/potential regions, missing `W*`, incomplete reviews, broken seals, invalid two-phase inference, or stakeholder sets spanning different winners. It maps to `DEFER`; it is not evidence that universal deferral benefits patients.

The required prospective actual-calendar silent bridge must observe report finalization/addenda, availability and viewing, discharge draft/version/edit/sign/transmission, physical departure, responsible team, target-linked orders/referrals and scheduling, timing-queue execution, outside plans, preferences, correction/dismissal, actual clinician minutes, and outcomes. It must re-estimate execution contamination, missed opportunities, and live workload without exposing silent routes to clinicians. Stakeholders must then revisit `W*` using prospective burden and safety evidence. Only a later governed comparative study could test whether any live policy improves follow-up or patient outcomes. Retrospective MIMIC text alone cannot establish those claims.

## Substantive advance and remaining uncertainty

This child converts arbitrary-threshold nomination into a falsifiable, source-bound decision frontier while adding no admissions or review layer. It shows exactly where each route or atom is dominated, potentially optimal, robustly optimal, or unsupported; retains correlated measurement uncertainty at the admission level; and makes selection contingent on transparent stakeholder tradeoffs rather than a hidden universal cutoff. It also imports the prior episode's total nested allocation and closed workload ledger so the actionability experiment is executable without route-enriched top-ups.

Uncertainty remains substantial. The loss coordinates concern stored textual routing and review demand, not harm or benefit. Their overlap is reported rather than assumed independent. `curr_service` and ICU exposure are workflow proxies, shifted dates do not establish real calendar transport, packet minutes are not live clinician time, and adjudicators can share error despite inherited challenges. Stakeholder weights and prospective execution evidence are unavailable in MIMIC. Therefore a frontier may honestly eliminate policies but still select none.
