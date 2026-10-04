# Loss-weight frontier and robust policy dominance for pulmonary-opportunity routing

## Decision question and targeted repair

The frozen decision remains whether any exact MIMIC pulmonary-opportunity atom can be nominated for a prospective **within-site silent validation** of the inherited admission routes `AUTO`, `RECON`, `TIMING`, and `DEFER`. This proposal does not authorize an alert, copied recommendation, order, referral, or patient-facing action. It is a retrospective audit of text-defined reproducibility and observable action structure.

The two parents repair major threats that could make a route appear reliable when it is not: a complete first-eligible all-opportunity denominator; reciprocal pre-departure chronology; a single canonical discharge artifact; exhaustive recommendation-unit states; route-independent, split evidence views; all-unit worst-admission routing; support-qualified possible-calendar/service/workflow atoms; roster-disjoint holistic challenge; independently written codebooks; explicit actionability and supersession panels; route-invariant and route-decisive controls; positive-probability sampling; adverse-compatible finite-population inference; and a strict noncausal ceiling. The remaining governance weakness is different. Even after those measurements, numerical release margins such as an upper contamination bound of 0.05, an actionability bound of 0.10, or an absolute review budget do not identify a clinically authoritative preference among `AUTO`, `RECON`, `TIMING`, and `DEFER`. They are operational screens, not values elicited from patients, clinicians, service leaders, or safety governance.

This child therefore adds a fully computable **loss-vector, loss-weight-frontier, and dominance analysis** without inventing a single utility threshold. It estimates several observable burdens for every atom-policy pair, carries all unresolved labels adversely through compatible sets and simultaneous finite-population intervals, and evaluates a preregistered transparent simplex of nonnegative governance weights. A policy may be called robustly dominant only under a definition that is true across the stated weight region and uncertainty set. A policy that is optimal only for some weights is reported as potentially optimal, not selected as clinically preferable. If no policy is robustly dominant, the correct result is an explicit frontier and a request for stakeholder weight elicitation or a prospective comparison, not an arbitrary winner.

## Supported evidence, unresolved claim, and falsifiable hypotheses

Available MIMIC evidence supports that a linked, first-eligible admission frame can be constructed from admission, patient, service, ICU, radiology, radiology-detail, discharge, and discharge-detail artifacts; that within-subject intervals can be calculated; that recommendation units and target-linked textual action structure can be independently measured; and that route-specific observable burdens can be estimated under a known finite-population design. It does not establish that a stored artifact was visible at physical departure, that a service code identifies responsibility, that an expert label is clinically correct, that an action was communicated or executed, that an omitted action harmed a patient, or that any policy improves outcomes.

The unresolved claim is narrower and consequential: **conditional on inherited validity and support gates, does any candidate routing policy have a defensible loss profile over a transparent range of governance priorities, or are policy preferences weight-sensitive, uncertainty-sensitive, or dominated by a safer lower-burden policy?**

The primary falsifiable hypotheses are:

* **H1 (dominance):** at least one support-qualified atom-policy pair is robustly non-dominated, and at least one candidate is robustly dominant over every alternative policy in a prespecified governance-weight region and simultaneous uncertainty set. Failure to find such a pair is not evidence that `DEFER` is clinically best; it is a no-dominance result.
* **H2 (frontier stability):** at least one policy remains potentially optimal over a nonzero connected region of the full weight simplex after adverse-compatible uncertainty is propagated. A policy that is optimal only at an isolated grid point, or whose region disappears under the uncertainty set, fails this stability hypothesis.
* **H3 (actionable separation):** the non-dominated frontier contains at least one pair whose loss difference is simultaneously estimable with the prespecified precision gate; otherwise the decision remains inconclusive and requires stakeholder elicitation or prospective data.
* **Falsification:** a claimed robust dominance or stable region is falsified if any admissible governance weight or any admissible joint label assignment reverses the comparison; if simultaneous intervals overlap the stated sign in a way allowed by the definition; if a route-invariant control changes; if a route-decisive control violates the locked transition; if an atom lacks support/positivity; or if any inherited seal, chronology, sampling, workload, or POE prohibition is violated.

The hypotheses concern observable decision burdens and governance sensitivity, not clinical benefit. Agreement is a measurement result, never a gold standard.

## Immutable inherited population, chronology, routes, and safeguards

Preserve both parent designs exactly. Do not change the population, opportunity definition, route table, route precedence, atom definition, sample sizes, random seeds, or admission budget.

Use dataset snapshot `[source checksum]`, with all source files read-only. The core source is `[internal dataset path]`, [source checksum], with archive members:

* `mimic-iv-3.1/hosp/admissions.csv.gz`
* `mimic-iv-3.1/hosp/patients.csv.gz`
* `mimic-iv-3.1/hosp/services.csv.gz`
* `mimic-iv-3.1/hosp/transfers.csv.gz`
* `mimic-iv-3.1/icu/icustays.csv.gz`

Bind `hosp/admissions` columns `(subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag)`, with key `(subject_id,hadm_id)` and `D=dischtime`. Bind `hosp/patients(subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod)`, joined on `subject_id`; use only the inherited widened possible-calendar class and never treat deidentified shifted years as real calendar dates. Bind `hosp/services(subject_id,hadm_id,transfertime,prev_service,curr_service)`, joined on `(subject_id,hadm_id)` and restricted to `transfertime<D`. Bind `hosp/transfers(subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime)` only for the inherited diagnostic workflow descriptors. Bind `icu/icustays(subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los)`, with admission-linked `intime<D` defining ICU workflow exposure.

Bind `[internal dataset path]`, [source checksum], table `note/radiology`, columns `(note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text)`, joined on `(subject_id,hadm_id)` and identified by `(subject_id,note_id)`. Bind `[internal dataset path]`, [source checksum], table `note/radiology_detail`, columns `(note_id,subject_id,field_name,field_value,field_ordinal)`, joined only on `(subject_id,note_id)`, retaining every ordinal and reciprocal `parent_note_id`/`addendum_note_id`. Bind `[internal dataset path]`, [source checksum], table `note/discharge`, columns `(note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text)`, restricted to exact `note_type==DS` and one canonical `(subject_id,hadm_id)` artifact under the parent rule. Bind `[internal dataset path]`, [source checksum], table `note/discharge_detail`, columns `(note_id,subject_id,field_name,field_value,field_ordinal)`. POE and `poe_detail` are prohibited from every packet, label, route, atom, estimand, loss, and gate.

Retain the parent’s complete first eligible admission per subject, adult rule, all-opportunity denominator, reciprocal pre-departure radiology report/addendum chain, canonical `DS`, unit-specific `G_u=DS_store-R_store,u` clocks, stale/post-discharge exclusions, exhaustive `Y,V,H,Z` states, all-unit worst-case admission routing, and exact `AUTO/RECON/TIMING/DEFER` precedence. One unsafe or unresolved recommendation unit controls its admission. Preserve the pre-label support atlas and atom `g=(possible-calendar class, terminal curr_service, workflow class)`, including unknown and residual atoms. Preserve the five outcome-blind sampling strata, sentinel census, positive first- and second-order inclusion probabilities, adverse finite-population inference, roster-disjoint A1/A2/S1/H3 panels, independent codebooks, route-concealed packets, append-only seals, all locked controls, fixed total of at most 900 distinct admissions, and default `DEFER` for unsupported/rare/novel/unknown signatures.

The inherited source profile counts (546,028 admissions; 364,627 patients; 593,071 service rows; 94,458 ICU stays; 2,321,355 radiology rows; 6,046,121 radiology-detail rows; 331,794 DS rows; 17 missing DS `storetime` values) remain feasibility checks only. Recompute and verify them rather than silently relying on copied counts.

## Fixed actionability challenge and workload

Retain the inherited master draw exactly. Let `M` be its distinct admissions, `n=|M|<=900`, and `m=min(300,n)`. Nested actionability challenge selection uses the already frozen protocol seed `ACTSUP-v1`; it is determined before packets or labels and is never enriched by route, disagreement, or outcome. To make the inherited instruction total without changing its sample size or target atoms:

1. If `n<=300`, set `C=M`.
2. If `n>300`, let `N_g` be the master count in each occupied pre-label atom, set coverage base `b_g=1` for `N_g=1` and `b_g=2` for `N_g>=2`, and let `B=sum_g b_g`.
3. If `B<=300`, allocate the residual `R=300-B` over capacities `c_g=N_g-b_g`: set `q_g=R*c_g/sum_h c_h`, take `floor(q_g)`, and award remaining slots by descending fractional remainder, breaking exact ties by ascending SHA-256 of `ACTSUP-v1 || canonical_atom_string(g)`. Then draw `m_g=b_g+a_g` admissions without replacement within each atom by ascending SHA-256 of `ACTSUP-v1 || subject_id || hadm_id`.
4. If `B>300`, use the prespecified global fallback: draw one SRS without replacement of 300 admissions from all `M` by the same admission hash ordering. Do not merge or prioritize atoms. An unrepresented atom is unsupported and remains `DEFER`; do not top up.

Record phase-1 inherited probabilities separately from conditional phase-2 probabilities. In census mode, `pi2_i=1` and `pi2_ij=1`. In covered mode, `pi2_i=m_g/N_g`; for distinct admissions in the same atom, `pi2_ij=m_g(m_g-1)/(N_g(N_g-1))`, and across atoms `pi2_ij=pi2_i*pi2_j`. In fallback mode, `pi2_i=300/n` and `pi2_ij=300*299/(n*(n-1))`. Use sequential two-phase weights and replicate both phases; do not describe a conditional phase-2 probability as an unconditional marginal. No additional admissions, replacement sampling, atom merging, route-triggered verification, or adaptive allocation is allowed.

Retain exactly four core whole-admission readings per challenged admission: A1, A2, S1, and H3, each covering every recommendation unit. Retain exactly six linked control-pair assignments per challenged admission: A1 and A2 route-invariant pairs, A1 and A2 route-decisive pairs, one S1 target-linked/non-target pair, and one H3 mask/insert pair. Thus the added ledger is `4m` whole-admission readings plus `6m` linked control-pair assignments (`12m` card exposures), adding zero distinct admissions. No disagreement re-read or extra reviewer is permitted. Record packet-time and physician-hour totals by atom and policy. Staffing shortfall or an incomplete ledger yields missing adverse-compatible labels and an inconclusive/default-`DEFER` result; it never changes the master sample, challenge sample, or weights. Workload is a feasibility/governance quantity, never a clinical harm threshold.

## Route-concealed actionability and supersession measurements

Generate A1, A2, S1, and H3 packets from sealed raw extracts before any labels or route joins. Packets contain only permitted pre-`D` radiology chains, permitted admission/death/disposition fields, canonical DS and permitted DS detail, timestamps, and explicit missingness. They contain no route, atom, stratum, weight, outcome, post-`D` text, POE, component label, or another reviewer’s output. A1 and A2 use disjoint rosters, independent ordering, separate pseudonyms, and independently written codebooks. S1 uses a disjoint roster. H3 is sealed only after A1/A2/S1 and is another measurement system, not an oracle.

Use the inherited exhaustive actionability categories exactly: `A1_ACTIVE_PORTABLE`, `A2_ACTIVE_RECONCILE`, `A3_SUPERSEDED_EXPLICIT`, `A4_RESOLVED_OR_INACTIVE`, `A5_NO_TARGETED_ACTION`, and `A6_UNKNOWN`. Use the inherited supersession categories exactly: `S0_NONE`, `S1_EXPLICIT_REPLACEMENT`, `S2_EXPLICIT_ALTERNATIVE_INCOMPLETE`, `S3_COMPETING_CONTRADICTORY_PLANS`, and `S4_UNKNOWN`. Duplicate restatements are one recommendation unit; distinct target/action/timing units remain distinct. Uncertainty remains a compatible set. A3 dominates other actionability categories, S3/S4 are adverse, and any unresolved minority unit controls the admission.

The inherited route compatibility table remains the only route derivation mechanism. No reviewer votes a route. An actionability result can block an atom or map it to `RECON`/`DEFER`; it cannot create a favorable route, override all-unit worst-case routing, or rescue a failing atom.

## Policy set and estimand

The policy comparison is predeclared and finite. For every support-qualified atom `g`, evaluate these policies on the same frozen opportunity units and admissions:

1. `P_AUTO`: propagate only if the inherited route and every adverse-compatible actionability/supersession output permit `AUTO`; otherwise `DEFER`.
2. `P_RECON`: send every inherited route-eligible unit to clinician reconciliation, including actionability states needing reconciliation; unresolved or unsupported cases remain `DEFER` under inherited precedence.
3. `P_TIMING`: use the inherited timing-specific route only when its exact timing state, opportunity clock, and actionability/supersession constraints permit it; otherwise `RECON` then `DEFER` as locked.
4. `P_DEFER`: no automated propagation; all eligible units are referred to manual review only through the predeclared safe reconciliation lane, and units without an explicit active target-linked action remain deferred. This is an operational comparator, not an assertion of clinical safety.

These are policy labels for a silent validation nomination analysis, not treatment assignments. No policy changes the observed MIMIC text or historical care. The primary estimand is the finite-population, design-weighted vector of observable policy burdens per eligible opportunity and per admission, stratified by atom, route, and all-unit worst-case admission status. Report both unit-level and admission-level values, with the admission-level value controlling nomination.

Let `a` index recommendation units in the frozen all-opportunity population, `i` index admissions, `g(a)` be its pre-label atom, and `p` be a policy. Let `d_{a,p}` be the policy’s action state (`AUTO`, `RECON`, `TIMING`, or `DEFER`) after the locked compatibility table and policy mapping. Let `Y^A_a` be the adverse-compatible actionability state measured by A1/A2/S1/H3, and let `Y^S_a` be supersession. For every unresolved pattern, compute a compatible set rather than selecting a favorable value.

## Observable loss vector

The loss vector is designed to separate burdens that imply different governance concerns. It deliberately does not call any component clinical harm or benefit.

### 1. Unsafe-contamination burden `L_U`

For a policy action that would propagate or nominate automation (`AUTO` or `TIMING`), mark a unit adverse if any admissible sealed panel output is `A2_ACTIVE_RECONCILE`, `A3_SUPERSEDED_EXPLICIT`, `A4_RESOLVED_OR_INACTIVE`, `A5_NO_TARGETED_ACTION`, or `A6_UNKNOWN`; if supersession is `S1`–`S4`; if a route-invariant control flips; or if the all-unit compatibility set contains an adverse competing route. For `RECON`, mark an adverse contamination when a purported active/reconciliation packet is not target-linked, is explicitly superseded, or is unresolved in a way that makes the stated reconciliation action unsupported. For `DEFER`, report contamination as zero only for the narrow *automated-propagation* component and separately retain an `unknown-deferred` component; no policy receives a blanket safety credit from absence of automation.

The primary `L_U` is the design-weighted proportion of policy-actionable units/admissions with an adverse-compatible text state. The lower endpoint uses only jointly observed adverse support; the upper endpoint assigns every unresolved or disagreement pattern adversely. This is textual contamination, not patient harm.

### 2. Missed-opportunity burden `L_M`

A missed opportunity is a unit with an independently measured, target-linked `A1_ACTIVE_PORTABLE` and `S0_NONE`, with no adverse-compatible contradiction, that the policy leaves in `RECON` or `DEFER` rather than the action state it could operationally propagate. A unit whose actionability is `A2_ACTIVE_RECONCILE`, superseded, resolved, informational, or unknown is not counted as an observed missed opportunity; it contributes to uncertainty or another component. This prevents defining “missed” by mere route disagreement. Report both the lower jointly supported and upper adverse-compatible missed-opportunity burden, because unresolved labels can be either a true missed opportunity or an unsafe action.

`L_M` is an observable addressable textual-opportunity burden, not prevented clinical benefit. MIMIC has no counterfactual outcome to show that propagation would help.

### 3. Supersession burden `L_S`

For every policy that would propagate or nominate a propagated route, count target-linked `S1_EXPLICIT_REPLACEMENT`, `S2_EXPLICIT_ALTERNATIVE_INCOMPLETE`, `S3_COMPETING_CONTRADICTORY_PLANS`, or `S4_UNKNOWN` as a policy supersession/plan-conflict burden. `S1` and `S3` remain distinct in the report. For `RECON` and `DEFER`, report the prevalence of such cases as unresolved review demand rather than zero, so the policy cannot hide the burden by changing the denominator. The primary loss component is the weighted fraction of opportunities requiring a decision different from unqualified propagation.

### 4. Review-workload burden `L_W`

Calculate actual packet readings and physician minutes per 1,000 eligible opportunities under each policy’s locked review pathway. Include duplicate/independent actionability readings, supersession readings, holistic challenge readings, controls, and any manual reconciliation review required by the policy. Use the same predeclared workload ledger for all policies. Report admissions and units separately, plus upper simultaneous workload intervals where sampling permits. `L_W` measures resource use, not clinician inconvenience as a clinical outcome and not an assumed monetary value.

### 5. Residual-uncertainty burden `L_Q`

Retain an explicit uncertainty component for unknown, missing, contradictory, control-infeasible, and unsupported states that prevent a policy from being safely classified. `L_Q` is not silently folded into either safety or missed opportunity. It is the weighted mass of opportunities for which the policy’s action state cannot be determined under the locked compatible-set rules. Policies that defer uncertainty may have higher workload but lower automated contamination; policies that automate it may have lower workload but higher adverse-compatible contamination. This component makes that tradeoff visible.

The primary decision vector is `(L_U,L_M,L_S,L_W,L_Q)`. A four-component sensitivity report omitting `L_Q` is permitted only as a labeled secondary analysis; it may not certify a policy or suppress the five-component frontier. All components are reported in common transparent units: proportions per 1,000 eligible opportunities for `U/M/S/Q`, and standardized physician-hours per 1,000 eligible opportunities for `W`, with the conversion constant and raw minutes also published. Standardization is dimensional bookkeeping, not a clinical value claim.

## Loss construction and denominator discipline

All losses use the frozen all-opportunity denominator `N_A` for population summaries. A policy-specific actionable denominator is reported only as a secondary descriptive quantity and may not replace `N_A`. For admission-level safety, any adverse-compatible unit marks the entire admission adverse under the inherited worst-unit rule. For workload, use the policy’s actual eligible review pathway and report both per-opportunity and per-admission totals.

Estimate each component using the inherited design weights and finite-population Horvitz–Thompson or Hájek form exactly as prespecified by the parent. Do not use unweighted complete cases. Retain first- and second-order inclusion probabilities. For each sampled admission, retain all unit labels together in every replicate. The primary uncertainty set is generated by the parent’s exact finite-population inversion for binary components and 20,000 Rao-Wu replicates, with one max-statistic simultaneous 95% family across inherited gates, atoms, routes, all five loss components, pairwise loss differences, controls, workload, and frontier endpoints. Every replicate preserves admission clustering, all-unit worst-case routing, and compatible-set adverse assignments.

For each atom-policy pair produce:

* point estimate and simultaneous lower/upper interval for each `L_k`;
* lower/upper interval for every pairwise difference `L_k(p)-L_k(q)`;
* effective sample size, event count, missingness, challenge coverage, and positive inclusion checks;
* atom and admission estimates, with route-specific estimates where defined;
* raw physician minutes, packet readings, and standardized workload;
* the complete compatible-set reason codes contributing to each adverse upper endpoint; and
* a machine-readable ledger linking every reported number to source rows, sealed labels, sampling weights, and replicate identifiers.

No imputation, favorable consensus, latent-class point estimate, shrinkage, macro-service pooling, neighboring-atom rescue, or negative-control performance may narrow the primary intervals.

## Governance-weight simplex and transparent frontier

### Weight domain

No clinically authoritative weight vector is assumed. Define the governance weight as
`w=(w_U,w_M,w_S,w_W,w_Q)` with each component nonnegative and `sum(w)=1`. The **full simplex** is the primary domain; its vertices and edges must be retained rather than excluded because a stakeholder may legitimately assign near-zero value to a particular burden. To make computation finite and reproducible, evaluate the deterministic lattice
`W_20={w: w_k=j_k/20, j_k in {0,...,20}, sum(j_k)=20}`. This is the complete five-part composition lattice, with exactly `C(24,4)=10,626` weights; the implementation must compute and assert this count rather than rely on the earlier erroneous “1,064?” shorthand. Retain the five vertices and every pairwise edge continuously by analytic linear minimization. The lattice is a display and audit fixture, not the certification mechanism.

Because a coarse lattice can miss a thin region, compute exact polyhedral regions analytically from the estimated loss vectors: policy `p` is pointwise optimal at weight `w` when `w·L_p <= w·L_q` for every `q`. Intersect these half-spaces with the simplex using deterministic linear programming. The grid is not a substitute for the polyhedral calculation. Report each policy’s region volume relative to the simplex, vertices/facets, and connected components. Use exact rational weights for the lattice and a fixed LP tolerance recorded in the manifest.

### Utility/loss score

For a weight vector `w`, define
`R(p,w)=w_U L_U(p)+w_M L_M(p)+w_S L_S(p)+w_W L_W(p)+w_Q L_Q(p)`.
Lower is better. This is a governance sensitivity score, not expected patient utility and not a clinical net benefit. Report `R` only with its component units, normalization constants, and uncertainty set; never call it benefit, harm, safety, or cost-effectiveness.

### Point frontier and dominance

Using point estimates only for visualization, define `p` as pointwise dominated by `q` if `L_k(q)<=L_k(p)` for all five components and `<` for at least one. Report the component-wise Pareto frontier separately from the weight-optimal frontier. A policy can be Pareto non-dominated but never optimal under the simplex, or optimal only in a narrow region; these distinctions must be explicit.

A policy is **robustly dominated** by `q` only if the joint uncertainty set proves `L_k(q)<=L_k(p)` for every component and every admissible shared-label realization, with strict improvement in at least one component for every admissible realization or a separately stated strict robust margin. Component-wise sufficient screening uses simultaneous upper bounds for `L_k(q)-L_k(p)`, but failure of that screen is not evidence of non-dominance: solve the exact joint constrained LP over the recorded replicate/compatible-label set. In particular, do not claim dominance from marginal interval endpoints assembled from incompatible realizations.

The primary release analysis uses a joint uncertainty set `C` formed by the simultaneous 95% compatible-compatible intervals and the observed-label compatibility constraints, not independent marginal interval combinations when those combinations are impossible. Let `C_p` denote the admissible loss vectors for policy `p`, retaining the covariance/replicate relationships and adverse-compatible label assignments. Define:

* **Robust dominance:** `p` robustly dominates `q` only if for every `w` in the full simplex and every joint `(l_p,l_q)` in `C_p×C_q` consistent with the shared labels, `w·l_p <= w·l_q`, with strict inequality for at least one admissible weight and uncertainty point. Equivalently for the componentwise sufficient screen, every upper bound for `L_k(p)-L_k(q)` is nonpositive and at least one component has a strictly negative simultaneous upper bound; if the sufficient screen is not met, solve the exact constrained LP and do not infer dominance.
* **Robustly optimal:** `p` is robustly optimal over region `A` only if for every `w` in `A` and every admissible joint uncertainty realization, `w·l_p <= w·l_q` for all alternatives `q`. This is intentionally stringent and may yield no policy.
* **Potentially optimal:** `p` is potentially optimal at `w` if at least one admissible joint uncertainty realization makes it a minimizer. The set of such weights is an optimistic diagnostic and cannot nominate a policy alone.
* **Weight-robustly potentially optimal:** `p` is retained on the decision frontier if its potentially optimal region has nonzero volume under the full simplex and its point estimate and adverse upper/lower profiles satisfy all inherited validity gates. A region with only measure-zero ties is reported as a tie, not stable support.
* **Indeterminate:** if uncertainty permits each of two policies to win on the same nontrivial weight region, report the region as unresolved. Do not resolve by selecting the midpoint, favorable panel, or a single threshold.

In addition to full-simplex analysis, report a preregistered **safety-priority sub-simplex** `A_safe={w: w_U>=0.40}` only as a governance sensitivity, not as a universal clinical value. The 0.40 boundary is a declared analytic slice chosen to show how safety-priority preferences alter the frontier; it is not a harm threshold and cannot select a policy without stakeholder endorsement. Also report `A_equal={w_k=0.20}` as a descriptive reference point, never as an authoritative default.

### Robustness and precision gates

The following are protocol gates on interpretability, not clinical utility thresholds:

1. Every claimed atom must pass all inherited support, control, seal, chronology, route, sample, event, ESS, missingness, and workload feasibility gates. Those gates are unchanged and remain necessary.
2. A frontier claim must be based on the full five-component vector and simultaneous joint uncertainty. A policy cannot be declared dominant because it wins after dropping `L_Q`, pooling atoms, or treating unresolved labels favorably.
3. For any pair called robustly ordered over a region, the simultaneous 95% upper bound of its weighted loss difference must be nonpositive throughout that region. If the interval includes both signs anywhere in the region, the order is indeterminate there.
4. A “stable” potentially optimal region must have positive polyhedral volume and must persist under the adverse-compatible endpoint analysis and the leave-one-panel-out measurement sensitivity (A1/A2/H3), without changing any labels or definitions. A zero-volume or grid-only region is not stable.
5. Precision must be reported, not hidden: give maximum simultaneous half-width for each component, maximum half-width of pairwise weighted differences over each reported region, minimum effective sample size, and number of admissible challenge events. If a component or pairwise difference is too wide to establish its reported sign, label it unresolved and fail closed to `DEFER` for nomination. The exact numerical reporting tolerances are computational precision specifications approved before labels; they are not claims about acceptable clinical risk.
6. A policy may be nominated for prospective silent validation only when it is either robustly optimal over the stakeholder-endorsed weight region supplied independently of these results, or the frontier report shows no dominance but stakeholders explicitly choose the candidate policy and accept the unresolved tradeoff. In the absence of such elicitation, the retrospective result can nominate at most the set of non-dominated candidates for governance review, never a single policy.

The inherited parent release margins remain unchanged as hard operational screens. Passing them does not imply a policy is utility-optimal; failing them blocks that atom regardless of a favorable weighted score. Conversely, a policy can pass every operational screen yet have no robustly dominant status.

## Stakeholder-weight separation and prospective bridge

MIMIC contains no stakeholder utility weights, patient preferences, clinician time valuation, safety tolerance, resource opportunity cost, or validated mapping from textual contamination to harm. Therefore, weights must not be estimated from historical actions, outcomes, note frequency, reviewer preference, or the same labels used to construct losses. A later governance process may elicit weights independently using a documented panel, patient/public input where appropriate, and explicit definitions of how review time, missed textual opportunities, supersession conflicts, uncertainty, and automation error are valued. That elicitation is outside this retrospective run.

The prospective bridge must use actual calendar time and actual workflow observation. Before live use, it should record whether the recommendation was viewed, edited, signed, transmitted, assigned to a responsible team, reconciled, ordered, referred, scheduled, superseded, and followed up; capture patient preference and outside plans; measure actual physician time; and predeclare patient-centered and process outcomes. A prospective silent validation can test transport and execution of the exact observable signature. A later governed interventional study is required for safety, benefit, causal effect, or clinical utility.

## Baselines and falsification fixtures

Run the same frozen data and labels against:

* each of `P_AUTO`, `P_RECON`, `P_TIMING`, and `P_DEFER`;
* the inherited parent-only route decision without actionability labels;
* a majority-consensus diagnostic and a favorable-consensus diagnostic, neither eligible for nomination;
* each single-panel leave-one-out diagnostic;
* pooled and macro-service analyses, explicitly prohibited as rescue;
* a latent-class sensitivity, if computed, labeled diagnostic only and unable to narrow primary intervals; and
* a zero-review and full-review accounting baseline, using only the declared workload ledger.

Mandatory fixtures are fully computable and must fail validation if they do not behave as specified:

1. **Shared-wrong labels:** make all panels agree on a planted wrong active plan. Agreement can be high, but adverse-compatible `L_U` and `L_Q` must not narrow merely because of agreement; no automation policy may become robustly dominant from consensus.
2. **Pooled-safe/atom-unsafe:** make one support atom unsafe while the pooled population appears safe. The unsafe atom must be blocked and cannot be rescued by pooled weights or a neighboring atom.
3. **Weight reversal:** create synthetic loss vectors in which `P_AUTO` wins when workload weight is high and `P_RECON` wins when contamination weight is high. The frontier must show both regions and must not select a default winner.
4. **Dominance:** create a synthetic policy with no greater loss in every component and lower loss in one. The implementation must identify robust dominance when simultaneous intervals permit it, and withhold it when an interval crosses zero.
5. **Uncertainty reversal:** widen one high-weight component through missing labels. A previously stable region must shrink or become indeterminate; no favorable complete-case substitution is allowed.
6. **Route-invariant perturbation:** formatting, section order, author-like tokens, and non-target wording must preserve unit inventory and route; any flip falsifies the affected run.
7. **Route-decisive perturbation:** a one-field timing or explicit-replacement change may change route only according to the locked compatibility table.
8. **Unsupported atom:** a novel/unknown service-workflow signature must remain `DEFER` and cannot receive a weighted utility advantage from missingness.
9. **Duplicate/restatement precedence:** duplicate restatements remain one unit, while distinct target/action/timing units remain distinct; one adverse minority unit controls the admission.
10. **Simplex implementation:** weights sum exactly to one; vertex, edge, lattice, LP, volume, and tie outputs agree; adding a display grid does not alter certification.

Any route-before-seal execution, packet leakage, roster overlap, codebook reuse, post-label control creation, prohibited POE use, favorable unknown assignment, negative-control rescue, adaptive sample change, incorrect archive member, source/hash mismatch, invalid join, or fabricated calendar alignment invalidates the run.

## Analysis algorithm and executable outputs

The compiler must implement the following deterministic sequence in an ordinary Python/SQL job, with source reads only from the exact paths above and all derived files in the workspace.

1. Verify the snapshot identifier, all five archive members and four note-file hashes, table schema hashes, source row counts, key uniqueness rules, reciprocal links, and MIMIC timestamp conventions. Extract only the bound columns.
2. Build the parent’s complete first-eligible, adult, all-opportunity admission frame; reconstruct the reciprocal radiology chain and canonical `DS`; calculate `D`, `G_u`, `Y,V,H,Z`, stale/post-`D` exclusions, terminal service, ICU workflow class, and possible-calendar class exactly as inherited.
3. Construct the five outcome-blind strata and final atom `g` before any label or challenge packet. Reproduce fixed random draws and inclusion probabilities; halt with `NO_SELECTION` when inherited sample/workload feasibility fails.
4. Generate sealed route-concealed A1/A2/S1/H3 packets and all controls before labels. Verify packet hashes, independent codebook hashes, roster disjointness, randomized order, and append-only seal order.
5. Obtain labels, preserve compatible sets, derive inherited routes only after all component seals, and run all inherited and actionability gates. Do not calculate policy losses or choose weights using labels before their preregistered seal state.
6. For each sampled admission, compute the policy action state for every `P_*`, all unit-level adverse/missed/supersession/unknown indicators, review pathway, packet count, and physician minutes. Apply all-unit worst-case routing to create admission-level indicators.
7. Estimate the five-component loss vectors with design weights, exact finite-population binary intervals, 20,000 Rao-Wu replicates, and one max-statistic simultaneous family. Retain shared admission labels in every replicate.
8. Build `W_20`, the continuous simplex half-space systems, and uncertainty-constrained LPs. Enumerate point Pareto frontier, grid minimizers, exact potential-optimal regions, robust dominance, robust-optimal regions, region volumes, ties, pairwise weighted intervals, and precision diagnostics. Assert `sum(w)==1` in exact rational arithmetic for lattice weights.
9. Apply fail-closed logic: an unsupported or failing atom is `DEFER`; a policy with no precision-qualified ordering is `INDETERMINATE`; no single policy is chosen without independently elicited weights; no MIMIC result is translated to safety, utility, benefit, or causal effect.
10. Emit immutable manifests and machine-readable outputs, including `source_manifest.json`, `population_frame.parquet`, `sampling_manifest.json`, `packet_manifest.json`, `label_compatibility.parquet`, `policy_loss_vectors.parquet`, `loss_intervals.parquet`, `frontier_lattice.parquet`, `frontier_regions.json`, `dominance_matrix.parquet`, `precision_gates.json`, `falsification_results.json`, and `interpretation.md`. Every row must retain atom, policy, admission/unit scope, source key, time rule, label version, weight, and replicate provenance. These are computational outputs, not scientific entities.

A minimal load-bearing score function is:

```python
def governance_loss(loss_vector, weights):
    keys = ("unsafe", "missed", "supersession", "workload", "uncertainty")
    if set(loss_vector) != set(keys) or set(weights) != set(keys):
        raise ValueError("incomplete five-component loss vector")
    if any(v < 0 for v in weights.values()) or sum(weights.values()) != 1:
        raise ValueError("weights must lie on the simplex")
    return sum(weights[k] * loss_vector[k] for k in keys)
```

The exact implementation may use rational arithmetic for weight construction and a fixed LP solver for regions, but must not substitute an unrecorded utility model or optimize a threshold after seeing results.

## Interpretation of supportive, adverse, and inconclusive outcomes

**Supportive:** An atom passes every inherited and actionability validity gate; the policy loss vector is fully specified; controls behave as locked; the adverse-compatible simultaneous intervals are sufficiently precise for the reported frontier; and either (a) one policy is robustly optimal over an independently endorsed governance-weight region, or (b) a transparent non-dominated frontier is returned for independent stakeholder selection. Support supports only nomination of the exact atom-policy mapping for prospective within-site silent validation. It does not establish that the policy is clinically preferable, safe, beneficial, or causal.

**Adverse:** An atom has a route-invariant control flip, route-decisive violation, unsupported or unresolved actionability, adverse-compatible contamination beyond an inherited operational screen, nonpositive support, broken seal, or an atom-level policy whose claimed dominance is reversed by an admissible weight or label assignment. Block the affected atom/policy. An adverse textual loss profile does not prove patient harm; it shows that the proposed nomination cannot be justified by the stated evidence and governance assumptions.

**Inconclusive:** Sparse events, challenge infeasibility, nonresponse, wide joint intervals, precision failure, no robust dominance, weight-sensitive frontier without independent stakeholder weights, unsupported atoms, workload infeasibility, or inability to establish a positive-volume stable region. Inconclusive is not evidence that `DEFER`, `AUTO`, `RECON`, or `TIMING` is safe or preferable. The proper output may be a frontier and a request for elicitation or a prospective study, with no single-policy nomination.

## Evidence ceiling and unavailable evidence

MIMIC cannot establish actual viewing, finalization or signature semantics, physical departure visibility, communication, responsibility, patient preference, outside plans, order/referral execution, scheduling, actual review time in workflow, appropriateness, follow-up completion, malignancy, harm, utility, benefit, causal effects, or forward/external transport. The source uses deidentified subject-specific shifted timestamps; within-subject intervals are usable, while cross-subject calendar alignment is not. Radiology images, raw waveforms, actual UI exposure, and real-time workflow traces are unavailable in the configured sources. Service, transfer, ICU, discharge, and storage fields are proxies, not ownership or execution truth. The actionability and loss labels measure observable text structure and adjudicator behavior under a sealed protocol, not clinical truth.

The strongest defensible conclusion from a successful run is therefore: for specified support-qualified MIMIC observable signatures, under specified measurement systems and a specified finite-population design, the stated policy burdens and their governance-weight frontier are computable and may justify a prospective silent-validation nomination or independent stakeholder review. Stronger claims about safety, utility, patient benefit, implementation, or clinical policy require independent weight elicitation, expert governance, actual-calendar prospective workflow evidence, and ultimately an appropriately designed interventional or outcomes study.
