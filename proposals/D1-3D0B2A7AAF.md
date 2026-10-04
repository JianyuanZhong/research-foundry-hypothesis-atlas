# A fixed-workload minimax domain envelope for the sealed pulmonary-nodule routing audit

## Decision bottleneck and targeted repair

The clinical decision is unchanged from the assessed parent: in the frozen first-eligible, all-opportunity MIMIC population, do the admission-level `AUTO`, `RECON`, `TIMING`, and `DEFER` routes have sufficiently reproducible, text-defined behavior to justify only a prospective silent validation? Every recommendation unit remains enumerated, and one unsafe or uncertain minority unit still controls the whole admission. This is not a test of guideline correctness, actual clinician awareness, safety, follow-up completion, or benefit.

The parent materially repaired incorporation and differential-verification bias through split recommendation/context/departure-plan views, sealed component labels, locked all-compatible route derivation, and independent all-route audit of every probability-sampled admission. Its most consequential remaining threat is pooling: a large, easier workflow can dominate a favorable finite-population estimate while a smaller observable workflow or coarse era band has unsafe `AUTO` contamination, misses uncertainty, or requires unworkable review time.

This child preserves the parent's population, chronology, canonical artifact, exhaustive states, unit clocks, sampling strata, full sentinel census, fixed sample-size formulas and 900-admission ceiling, split views, independent all-route audit, worst-unit routing, estimands, finite-population logic, and noncausal ceiling. It changes only the outcome-blind sampling allocation and confirmatory analysis. Unlike `[prior hypothesis]`, it does not rely on many marginal target constraints or an artificial leave-one-domain-out release for a route that is never fitted. It instead freezes a deliberately small crossed era-by-workflow partition and uses a guaranteed-feasible integer allocation that (i) gives every occupied cell positive inclusion probability, (ii) dedicates a deterministic coverage floor using no more than half of each inherited stratum's fixed sample, and (iii) minimizes the largest survey weight with the remaining slots. Safety nomination is based on an absolute worst-domain envelope, not on failure to detect pairwise drift. Sparse cells are never rescued by pooling, shrinkage, or a nonsignificant interaction; they make unrestricted nomination inconclusive and can only be prospectively defaulted to `DEFER`.

## Evidence-supported claim, unresolved claim, and hypothesis

### Strongest claim currently supported

The configured snapshot contains the exact fields needed to construct pre-label domains and execute the inherited audit. A source-wide read of the core archive (not the pulmonary-eligible population) found 546,028 admissions, 593,071 service rows, 335 admissions without a service row at or before discharge, no terminal-time ties under the source-wide rule, 85,136 admissions with a pre-departure ICU row, and shifted admission years from 2105 through 2214. Terminal service codes include `MED, CMED, NMED, SURG, CSURG, NSURG, PSURG, TSURG, VSURG, ORTHO, TRAUM, GU, GYN, ENT, EYE, DENT, OBS, PSYCH, OMED, NBB`. The note profile inherited from the parent found 2,321,355 radiology rows (`RR=2,295,635`, `AR=25,720`), 6,046,121 radiology-detail rows, 331,794 `DS` rows with unique `(subject_id,hadm_id)` keys, 17 missing discharge `storetime` values, and 25,735 rows each carrying `parent_note_id` and `addendum_note_id`. These are feasibility facts, not evidence of pulmonary eligibility, route prevalence, route purity, calendar transport, workflow ownership, or safety.

### Unresolved claim

After the full protocol is frozen without labels from real records, do the parent's pooled route-purity, capture, reproducibility, and workload conclusions remain within their governance margins in each observable era-by-workflow cell in which a route would be allowed, or does pooling conceal a cell-specific failure?

### Falsifiable hypothesis

For the same frozen `N_A`, every cell proposed for prospective route use will simultaneously satisfy the parent's adverse-compatible route gates. In particular, each `AUTO`-allowlisted cell will have a simultaneous one-sided upper bound `C_AUTO,c < 0.05`, `D_MIX,c < 0.10`, and `leak_AUTO,c < 0.02`, a lower confirmation bound at least 0.90 and AC1 at least 0.70, no independently confirmed unsafe minority unit compatible with `AUTO`, and approved workload. Each claimed `RECON`, `TIMING`, or `DEFER` cell will meet the inherited capture and confirmation margins. A pooled pass with any adequately measured cell failure is adverse. A cell with insufficient denominator/events/ESS or a wide bound is inconclusive and cannot be allowlisted. Failure to reject heterogeneity is never evidence of transport.

The only supportive decision is an explicit within-MIMIC workflow/era allowlist for prospective silent validation. All cells not on that list must prospectively default to `DEFER`. No result supports exact calendar trends, external-site transport, retrospective automation, or patient benefit.

## Exact source provenance and bindings

Use snapshot `[source checksum]`. Sources are read-only. Derived manifests, seeds, hashes, pseudonyms, review labels, replicate weights, and results are written only in the workspace. Clinical text is never sent to a public service.

### Core archive

Source `[internal dataset path]`, [source checksum].

1. Member `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`, schema [source checksum]; columns `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag`. Key `(subject_id,hadm_id)`. The inherited departure proxy is `D=dischtime`.
2. Member `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`, schema [source checksum]; columns `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`. Join `subject_id`. Adult age remains `anchor_age + year(admittime) - anchor_year >=18`, retaining the documented representation above age 89. Only `anchor_year_group`, `anchor_year`, and the within-subject shifted-year offset enter the coarse era construction below.
3. Member `mimic-iv-3.1/hosp/services.csv.gz`, table `hosp/services`, schema [source checksum]; columns `subject_id,hadm_id,transfertime,prev_service,curr_service`. Join exactly `(subject_id,hadm_id)`. Rows after `D` cannot define departure workflow.
4. Member `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`, schema [source checksum]; columns `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`. Join `(subject_id,hadm_id)`; a row with nonmissing `intime<=D` supplies the pre-departure ICU indicator.
5. Member `mimic-iv-3.1/hosp/transfers.csv.gz`, table `hosp/transfers`, schema [source checksum]; columns `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`. It is descriptive only and cannot repair an unknown service or ICU state.
6. The inherited optional POE appendix uses members `mimic-iv-3.1/hosp/poe.csv.gz` and `mimic-iv-3.1/hosp/poe_detail.csv.gz`, schemas `[source checksum]` and `[source checksum]`. POE remains prohibited from every primary packet, route, domain, estimand, and gate.

### Notes

1. `[internal dataset path]`, [source checksum], table `note/radiology`, schema [source checksum]; columns `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`. Admission join `(subject_id,hadm_id)`; note identity `(subject_id,note_id)`.
2. `[internal dataset path]`, [source checksum], table `note/radiology_detail`, schema [source checksum]; columns `note_id,subject_id,field_name,field_value,field_ordinal`. Join `(subject_id,note_id)` and retain all ordinals and reciprocal-link fields.
3. `[internal dataset path]`, [source checksum], table `note/discharge`, the same eight-column schema/hash as radiology. Restrict exactly to `note_type=="DS"`; canonical key `(subject_id,hadm_id)`.
4. `[internal dataset path]`, [source checksum], table `note/discharge_detail`, schema [source checksum]; columns `note_id,subject_id,field_name,field_value,field_ordinal`. Join only `(subject_id,note_id)`. The observed `author` field is not a validated section ontology.

The core is locally identified as MIMIC-IV 3.1 and notes as 2.1. Subject-specific date shifts preserve within-subject intervals but invalidate cross-subject analysis of raw shifted calendar years or seasons.

## Frozen inherited population and chronology

Before any unredacted pulmonary discharge-plan text, sampling domain, route, or audit label is seen, stream all radiology and radiology-detail rows. Freeze hashes for extraction code, the high-recall lexical/exam dictionary, all included and excluded note IDs, and the retrieval-negative audit seed.

The inherited candidate frame remains every exact admission-linked report with `charttime in [admittime-12h,D]` meeting any locked pulmonary/nodule/opacity, follow-up/recommendation, 3/6/12-month calendar, thoracic CT, or exam-code/name rule. Candidate rules cannot use unredacted pulmonary discharge-plan content and cannot be tuned to route labels.

Two independent eligibility physicians receive only reciprocal radiology chains, permitted admission/death/disposition fields, and context with all pulmonary target/action/timing/recipient/order/preference spans redacted by a separate operator. They never see domains, strata, discharge `storetime`, routes, or outcomes. Each seals an atomic eligibility record with source spans. Disagreement remains `U_R`; a third opinion cannot erase it.

`N_A` remains exactly one first eligible admission per subject, sorted by `admittime` then `hadm_id`, satisfying all inherited criteria: adult; exact admission-linked report; incidental pulmonary nodule or indeterminate focal nodular opacity; patient-specific unconditional chest/thoracic CT at exactly 3, 6, or 12 calendar months. Preserve exclusions for screening, established surveillance, staging/oncologic surveillance, conditional/optional plans, explicit no follow-up, in-hospital death, locked hospice/comfort-only transition, and recommendations first introduced after `D`. Never infer size, smoking, malignancy risk, life expectancy, appropriateness, or missing context. Later eligibility concern is retained as `U_R`, not used to redefine `N_A`.

Report/addendum chains require subject- and admission-consistent reciprocal links: the `AR` parent relation and corresponding `RR` addendum relation must agree. Operative components need `charttime<=D` and `storetime<=D`; missing nodes, one-way/contradictory links, conflicting times, or unresolved text remain `U_R`. The retrieval-negative probability audit remains inherited, including subject-cluster handling if several negatives arise from one subject; any confirmed miss or simultaneous upper bound indicating more than 5% denominator undercoverage blocks all routes.

For each `N_A` admission require exactly one canonical `DS`. Duplicate keys stop the run. Missing artifact/text/linkage/`storetime`, unreadability, or contradiction remains unknown; `charttime` never substitutes for `storetime`.

Preserve exhaustive departure state `Y={F,C_O,C_I,R,A,U_D}`, availability state `V={V_D,V_24,V_72,V_168,V_late,V_U}`, lag state `H={H_stale,H_0_6,H_6_24,H_24_72,H_72plus,H_U}`, eventual state `Z={F_text,C_O_text,C_I_text,R_text,U_text}`, and all zero/unknown `J_A=count(V,H,Z)/N_A` cells. Later faithful text cannot change departure state `A`.

For every operative recommendation unit `u`, retain `R_store,u`, `DS_store`, and `G_u=DS_store-R_store,u` in hours, checking row-wise

`D-R_store,u = (D-DS_store) + G_u`.

Only unit-specific `G_u` controls opportunity. Every active unresolved unit needs resolved `G_u>=24h` for content routing. Under-24-hour, unknown-clock, stale, or post-departure artifacts cannot become content failures.

A unit remains the smallest operative tuple `(target cluster, action/modality, due interval/date, polarity)`. Co-mentioned targets sharing an action/window form one unit; differing actions/windows form separate units; reciprocal restatements are deduplicated; material addenda revise rather than duplicate. Unresolved coreference/splitting is `U_BOUNDARY`. Units are nested observations, never sampled, independently weighted, or treated as inferential subjects.

## Inherited sealed split-view audit and worst-unit routing

Preserve without relaxation:

* the two independent index lanes and two independent audit lanes for recommendation (`R`), redacted context (`K`), and unredacted radiology-to-departure-plan atoms (`S`);
* separate eligibility, redaction, packet-construction, index, audit, safety, and code roles;
* role-specific pseudonyms, access logs, packet hashes, canaries, append-only atomic labels, no cross-role discussion, and release only after all labels or explicit nonresponse records are sealed;
* no real `N_A` record for training, rehearsal, threshold setting, prompt/rule tuning, code debugging, or redaction repair; synthetic clinician-written fixtures only;
* fresh de-novo `R-A/K-A/S-A` review and a complete pre-`D` minority-unit safety audit for every selected admission regardless of apparent route;
* locked matching by compatible normalized tuples and source offsets, with every one-to-many/many-to-one/conflicting match becoming `U_BOUNDARY`; and
* all prespecified lane pairings, off-diagonal combinations, minimum/maximum inventories, safety findings, nonresponse, redaction breaches, and unknowns retained in the compatible route set.

Unit states remain `U_RESOLVED`, `U_OPEN`, `U_TIMING`, `U_CLOSED`, and `U_DEFER`. Admission precedence remains:

1. any `U_DEFER` gives `A_DEFER`;
2. otherwise any `U_TIMING` gives `A_TIMING`;
3. all units resolved/closed gives `A_NOACTION`;
4. `A_AUTO` requires every open unit to be a wholly omitted `S_0` unit with ample clock, every other unit reproducibly resolved/closed, and no boundary, redaction, context, or cross-unit conflict; and
5. any incomplete, conflicting, interaction-dependent, or mixed admission gives `A_RECON`; `A_MIXED` is nested in `RECON` when pure omission coexists with a reconciliation unit.

A robust route is a singleton only if every compatible assignment yields the same route. Otherwise decision-facing routing is `A_DEFER`. One unsafe minority unit always dominates; duplicating safe units cannot change route or admission weight.

## Outcome-blind domains frozen before sampling

Construct and hash domains after `N_A`, reciprocal chains, canonical artifacts, and deterministic clocks are frozen, but before sampling or human route-component labels. Domains are hidden from reviewers and cannot affect packet content. Missingness is explicit rather than deleted.

### Coarse possible-calendar era

Parse `anchor_year_group` as inclusive real-year interval `[a_i,b_i]`. Let `q_i=year(admittime)-anchor_year`. Because exact real anchor year and month/day alignment are unavailable, define the conservative possible admission-year interval

`C_i=[a_i+q_i-1, b_i+q_i+1]`.

The one-year widening prevents year-boundary assumptions from creating false precision. Assign exactly one:

* `E_EARLY` if `upper(C_i)<=2013`;
* `E_LATE` if `lower(C_i)>=2017`;
* `E_BRIDGE` otherwise, including intervals crossing either boundary; or
* `E_UNKNOWN` for missing/malformed/contradictory fields.

Raw `year(admittime)` can only supply the within-subject offset `q_i`; it cannot itself define an era, trend, season, or cross-subject chronology. These are possible-calendar bands, not recovered dates. `E_EARLY` and `E_LATE` are separated conservatively; `E_BRIDGE` and `E_UNKNOWN` remain fully represented.

### Workflow state

Order service rows with exact `(subject_id,hadm_id)`, nonmissing `transfertime`, and `transfertime<=D` by `transfertime`. If the latest timestamp has one distinct nonmissing `curr_service`, that is the terminal service. A same-time tie with different codes, missing code/time, no pre-departure row, unseen code, contradictory linkage, or parser failure is unknown. Row order cannot break a timestamp tie.

Freeze service families before outcomes:

* medical: `{MED,CMED,NMED}`;
* procedural: `{SURG,CSURG,NSURG,PSURG,TSURG,VSURG,ORTHO,TRAUM,GU,GYN,ENT,EYE,DENT}`;
* observation/behavioral/other: `{OBS,PSYCH,OMED,NBB}`; and
* unknown: all missing, tied, unseen, or contradictory states.

Define the four mutually exclusive workflow domains `W_MED`, `W_PROC`, `W_OTHER`, and `W_UNKNOWN` from those service families. This grouping is operational, not a validated taxonomy of clinical ownership. Publish exact `curr_service` counts within every workflow domain.

Define ICU exposure separately as `ICU_YES` if any exact admission-linked `icu/icustays` row has nonmissing `intime<=D`; `ICU_NO` if no such row exists and there is no contradictory admission-linked ICU timestamp; and `ICU_UNKNOWN` for contradictory linkage/time. ICU is a mandatory marginal transport domain rather than another crossed dimension: this preserves an ICU masking check without fragmenting the fixed sample into clinically unresolvable cells.

The primary crossed partition is `c=(E,W)`, at most 16 cells including unknowns and only nine known early/bridge/late-by-medical/procedural/other cells. Every `N_A` admission belongs to exactly one crossed cell. Publish `N_c` and the complete cross-tabulation with inherited sampling strata and ICU domain before labels are unsealed. No cell is removed for inconvenience or size. Secondary, simultaneously adjusted diagnostics retain exact service code, number of pre-`D` service rows (`0,1,2+`), any service change, ICU careunit, `admission_type`, and `admission_location`; they cannot rescue a crossed-cell or ICU-marginal failure and cannot be regrouped after labels.

## Fixed-workload positive-probability allocation

Retain the parent's five hierarchical, outcome-blind strata exactly:

1. certainty `S_SENTINEL`: reciprocal-chain defect; missing/contradictory time; missing/unreadable canonical artifact; parser failure; `U_BOUNDARY` signal; possible multiplicity; different actions/windows; negation/conditionality conflict; target-linked decision/non-pursuit/definitive treatment; or discordant pulmonary-plan spans in `DS`;
2. `S_TIMECLOCK`: no sentinel, but any deterministic unit has `G_u<24h`, unknown `G_u`, `DS_store>D`, or stale chronology;
3. `S_ZERO`: no sentinel, all clocks ample, no deterministic target-linked pulmonary plan span in `DS`;
4. `S_PARTIAL`: no sentinel, all clocks ample, target text but missing/discordant action, timing, responsibility, polarity, or linkage; and
5. `S_COMPLETE`: no sentinel, all clocks ample, deterministic target/action/timing/responsibility or replacement-plan elements present.

These are sampling strata, never routes, and remain hidden from reviewers. Census all sentinels. In `S_ZERO`, retain the larger of 300 or the finite-population sample size for worst-case 0.5 and ±4 percentage-point 95% precision, capped at `N_h`. In every other noncensus stratum retain the larger of 120 or the analogous ±7-point size, capped at `N_h`:

`n_h=ceil[N_h*1.96^2*0.25/{e_h^2*(N_h-1)+1.96^2*0.25}]`.

The mandatory census plus fixed formula samples must not exceed 900. If it does, obtain resources before labels or declare feasibility failed. Never reduce a sample, omit sentinels, top up after seeing events, stop early, or replace a difficult admission.

### Guaranteed-feasible crossed-cell allocation

For each noncensus `h`, let `C_h` be its occupied era-by-workflow crossed cells, `K_h=|C_h|`, and `N_hc` their frozen sizes. If `n_h=N_h`, census the stratum. Otherwise the inherited lower bound (`n_h>=120`) and at most 16 cells guarantee `n_h>=K_h`.

Reserve deterministic coverage

`b_hc=min[N_hc, max(1, floor(n_h/(2*K_h)))]`.

Because `sum_c b_hc<=K_h*floor(n_h/(2*K_h))<=n_h/2` (and the `min[N_hc,...]` operation can only reduce that sum), the floor is always feasible and uses no more than half the fixed allocation while guaranteeing at least one selection from every occupied cell. Allocate all remaining slots by exact integer optimization:

1. `sum_c n_hc=n_h` and `b_hc<=n_hc<=N_hc`;
2. minimize `M_h=max_c(N_hc/n_hc)` (the largest noncertainty base weight);
3. among ties, minimize `sum_c N_hc^2*(1-n_hc/N_hc)/n_hc`; and
4. among remaining ties, use lexicographic `(h,E,W)` order.

Freeze solver/version, objective values, allocation, and a brute-force or independently implemented verification certificate before labels. This allocation is genuinely fixed-workload: it neither creates extra reviews nor relies on possibly infeasible marginal quotas. It also gives every occupied cell positive probability and explicitly controls the largest design weight.

Draw SRS without replacement independently within every `(h,c)` using a seed derived from the sealed protocol hash. Freeze ordered selected IDs and an explicit no-replacement list. For admission `i` in `(h,c)`, `pi_i=1` in certainty/census cells and otherwise `pi_i=n_hc/N_hc>0`; `w_i=1/pi_i`. Within a sampled noncensus cell,

`pi_ij=n_hc(n_hc-1)/[N_hc(N_hc-1)]`,

and across independently sampled cells `pi_ij=pi_i*pi_j`. Cells of size no greater than their coverage floor are censused; any remaining noncensus cell with fewer than two sampled observations is unsupported for variance-based claims and uses only conservative exact bounds.

All selected admissions receive every inherited index component, audit component, redaction audit, and minority-unit safety audit. Reviewer assignment is block-randomized across crossed cells and component roles before packets, while cell identities remain concealed. No reassignment based on speed, disagreement, route, or interim result is allowed.

## Preserved estimands and domain envelope

The inference population remains all frozen `N_A`; the admission is the sampling/analysis unit and also one per subject. Preserve pooled route burdens

`T_r=sum_i I(R_i=r)`, `B_r=100*T_r/N_A`,

for `AUTO,RECON,TIMING,DEFER,NOACTION,MIXED`, with `MIXED` nested in `RECON`. Estimate totals by Horvitz-Thompson and ratios by ratios of HT totals.

Preserve the parent's route reproducibility metrics: weighted raw agreement, category-specific positive agreement, Gwet AC1, kappa, both directional confirmations, index-to-audit confirmation, and adverse route-crossing probabilities. Consensus cannot satisfy a gate.

Preserve `C_AUTO`. Let `d_i=1` if either initial index lane calls `AUTO`. Let `x_i=1` when `d_i=1` and the other index lane, any audit-compatible route, or the safety auditor supports `RECON/TIMING/DEFER`; when a required audit label is missing; or when boundary, redaction, clock, context, or other unknown evidence can resolve adversely to non-`AUTO`. Then

`C_AUTO=sum_i x_i/sum_i d_i`,

estimated by the Hájek ratio `sum_s w_i x_i/sum_s w_i d_i`, with numerator and denominator HT totals always reported. This is independent text-defined route contamination, not clinical safety.

Also preserve `D_MIX`, newly found additional/unsafe-unit rate, deterministic-one-unit-to-multiple-unit error rate, `Se_RECON`, `PPV_RECON`, `PPV_TIMING`, `Se_DEFER`, `leak_AUTO`, all `Y/V/H/Z/J_A` cells, and workload (packets, components, units, minutes, physician-hours, nonresponse, and hours per 100 `N_A`).

For every endpoint calculate the same quantity within each era margin, workflow margin, ICU margin, and occupied era-by-workflow crossed cell. For a crossed-cell total,

`T_yc_hat=sum_{i in s} w_i I(C_i=c)y_i`.

Conditional risks are ratios of corresponding HT totals. Report numerator/denominator totals, cell burden, sampling fractions, maximum normalized weight, and route-denominator ESS. Calculate cell-minus-complement contrasts as descriptive heterogeneity measures, but nomination depends on absolute cell gates. A nonsignificant contrast cannot establish equivalence.

### Domain allowlist and no pooled rescue

A route is prospectively allowlisted only for crossed cells that satisfy all source/seal gates, have the required route support, and pass that route's adverse simultaneous bounds; the corresponding ICU margin must also pass or be support-eligible and route-inactive. A pooled pass cannot override a crossed-cell or ICU-marginal failure. A crossed cell or ICU domain that is sparse, unsupported, unknown, or imprecise is assigned prospective `DEFER`; it is never inferred safe from another margin, neighboring cell, model, or complement.

Unrestricted within-site nomination requires every occupied known cell to be either (i) allowlisted for the route or (ii) demonstrably route-inactive, defined prospectively as a simultaneous upper bound below 1 route-positive admission per 100 `N_c`, with the route forced to `DEFER` there. `E_UNKNOWN` or `W_UNKNOWN` upper burden above 2% blocks unrestricted nomination. A restricted silent study may proceed only with the frozen allowlist encoded before prospective accrual; every nonallowlisted cell defaults to `DEFER`.

## Finite-population inference, nonresponse, rare events, and multiplicity

Treat `(h,c)` as survey strata. For scalar `y`, use

`V_hat(T_y_hat)=sum_{h,c} N_hc^2*(1-n_hc/N_hc)*s_y,hc^2/n_hc`,

with zero contribution from census cells. For ratio `R`, use Taylor linearization `z_i=y_i-R_hat*d_i` and divide the analogous total variance by `T_d_hat^2`. Never report a ratio with zero estimated denominator.

Generate at least 20,000 Rao-Wu rescaled bootstrap replicates independently within each noncensus `(h,c)`; certainty admissions remain fixed. Every unit/view/label/nonresponse state for an admission travels together. The same replicate drives pooled, marginal-domain, crossed-cell, workload, support, and heterogeneity outputs.

The single primary multiplicity family contains all inherited pooled gates and all route-specific gates in every occupied era, workflow, ICU, and era-by-workflow crossed domain. Use a bootstrap max statistic for regular endpoints. For rare/zero events, invert the exact stratified finite-population distribution: hypergeometric inversion for unconditional binary totals and multivariate-hypergeometric enumeration of `{unsafe AUTO,safe AUTO,non-AUTO}` for `C_AUTO`. Apply closed testing from pooled route to era/workflow margins to crossed cells when valid; a child cell can pass only if every ancestor intersection null is rejected in the safe direction. For endpoints not covered by a valid closed-test relation, use Holm-adjusted one-sided tests or Bonferroni-adjusted exact bounds over the frozen family. Report the widest valid bound among exact inversion, max-statistic bootstrap, and adverse partial identification. Never drop a sparse domain to improve multiplicity.

No selected admission is replaced. Nonresponse includes unreadable packet, reviewer withdrawal, late/schema-invalid label, access failure, missing component, missing safety audit, or broken seal. Base weights do not change. Complete-case deletion, response weighting, model imputation, consensus imputation, and missing-at-random assumptions are prohibited for primary inference.

For each estimand, every incomplete admission contributes all states compatible with source facts. Optimize lower/upper endpoints subject to mutually exclusive exhaustive routes; use linear-fractional optimization for ratios inside each replicate. An index `AUTO` with missing audit evidence is unsafe for the upper `C_AUTO` bound. Missing/unknown domain fields contribute to `UNKNOWN` and to every compatible adverse unrestricted endpoint, never to a favorable known cell. Unknown clocks cannot be assigned ample favorably. Redaction breach, unit-boundary ambiguity, cross-route disagreement, and safety-auditor concern are adverse. Complete-response estimates are diagnostics only.

Report Kish ESS overall, by cell, and for every ratio denominator; maximum weight and normalized share; stratum/cell response; certainty-case share; and reviewer allocation. The first-eligible rule requires unique `subject_id`; any duplicate after freezing stops the run rather than invoking a cluster-robust repair. A secondary reviewer-cluster bootstrap diagnoses roster effects but cannot make adverse design bounds favorable.

## Fixed gates

Governance must approve all margins and an absolute physician-hour budget before any real route label is released. Defaults remain operational silent-validation margins, not acceptable harm rates: `tau_AUTO=0.05`, confirmation `rho=0.90`, AC1 `0.70`, `sigma_RECON=0.95`, `pi_RECON=0.80`, `pi_TIMING=0.95`, and `sigma_DEFER=0.95`.

Every pooled or domain claim first requires stable source/schema/code hashes; reproducible `N_A`; retrieval-audit pass; no duplicate canonical `DS`; `U_R<=5%`; `U_D<=5%`; intact role/access separation and seals; redaction pass; at least 200 `N_A`; at least 60 inherited `E_A`; overall design ESS at least 150; `max(w_i)/sum(w_i)<=0.10`; and simultaneous all-`N_A` burden half-width no greater than 5 per 100.

A primary domain (era margin, workflow margin, ICU margin, or crossed cell) is support-eligible for a route only if it has at least 40 sampled admissions total, at least 10 from non-sentinel cells, normalized maximum weight no greater than 0.10, domain ESS at least 30, and the following route denominators:

* `AUTO`: at least 20 sampled candidate-`AUTO` admissions and route-denominator ESS at least 30;
* `RECON`: at least 20 index `RECON` and 20 audit unsafe-content admissions, each denominator ESS at least 30;
* `TIMING`: at least 20 index `TIMING`, denominator ESS at least 30;
* `DEFER`: at least 20 independent-audit uncertain-reference admissions, denominator ESS at least 30.

These domain thresholds are lower than inherited pooled thresholds because workload is fixed, but multiplicity-adjusted precision still controls the decision: each required one-sided bound must have width no greater than 0.05 for probabilities other than contamination bounds, whose upper confidence limit must directly meet the margin. Event/ESS failure is inconclusive, not favorable. Pooled thresholds remain exactly the parent's: 30 route-positive/reference-positive events as applicable and route-denominator ESS 80 or 100.

For every allowlisted cell:

* `AUTO`: lower confirmation/raw-agreement `>=0.90`; lower AC1 `>=0.70`; upper `C_AUTO<0.05`; upper `D_MIX<0.10`; upper `leak_AUTO<0.02`; no safety-auditor-confirmed unresolved minority unit compatible with `AUTO`; lower `B_AUTO>0`; and upper physician-hours per 100 admissions below the preapproved absolute budget.
* `RECON`: lower confirmation `>=0.90`; lower `Se_RECON>=0.95`; lower `PPV_RECON>=0.80`; upper leakage of unsafe-content references to `AUTO<=0.02`; lower `B_RECON>0`; approved workload.
* `TIMING`: lower confirmation `>=0.90`; lower `PPV_TIMING>=0.95`; zero observed use of index-only `G` when another active unit has `G_u<24h`; lower `B_TIMING>0`; approved workload.
* `DEFER`: lower confirmation `>=0.90`; lower `Se_DEFER>=0.95`; no adverse-compatible unknown routed `AUTO`; approved workload.

Apply corresponding inherited pooled gates before any cell allowlist. Routes pass separately. A reconciliation-only silent study remains possible when its own pooled and domain gates pass while `AUTO` fails. Missing governance approval, broken seals, prohibited adaptation, unsupported required cells, or excessive unknown-domain burden yields `NO_SELECTION` for unrestricted use.

## Baselines

Use the identical population, sample, domains, weights, audit labels, uncertainty, and multiplicity for:

1. the parent's pooled-only analysis, the principal comparator;
2. marginal-majority route assignment;
3. deterministic sampling-stratum routing;
4. recommendation-unit majority routing, expected to miss a minority unsafe unit;
5. service-family-majority and era-majority routing;
6. a domain-blind analysis reporting only pooled endpoints;
7. favorable consensus, complete-case unweighted, and incorporated-reference analyses, all prohibited from nomination; and
8. a sentinel-only safety analysis, which must fail a planted non-sentinel domain-specific contamination scenario.

The methodological advance is successful only if synthetic finite populations demonstrate that this design blocks nomination when a pooled analysis passes but one crossed cell violates a margin, while retaining nominal finite-population coverage under unequal fractions.

## Falsification and adversarial verification

1. Recompute source/schema hashes, full row counts, canonical keys, reciprocal links, `N_A`, first-eligible selection, clocks, domains, crossed cells, allocations, `pi_i`, `pi_ij`, ordered sample, and zero replacements from sealed inputs.
2. Recheck `D-R_store,u=(D-DS_store)+G_u`; changing an index clock cannot rescue another active under-24-hour unit.
3. Era trap: identical shifted years with different `anchor_year_group` must map through the conservative possible-calendar interval; a band crossing a cutoff must be `E_BRIDGE`; malformed data must be `E_UNKNOWN`.
4. Raw-year trap: any direct split/trend/season using shifted `admittime` year fails the temporal claim.
5. Workflow trap: a service row after `D` cannot alter a domain; a same-time distinct terminal-code tie, missing service, unseen code, or contradictory ICU time must become unknown.
6. Allocation certificate: an independent implementation must reproduce `b_hc`, minimax `M_h`, tie-break objective, `n_hc`, seeds, and selected IDs. Route labels or row processing order cannot alter them.
7. Fixed-workload trap: no outcome-dependent top-up, replacement, cell merge, adaptive stopping, or extra review beyond the inherited selected admissions is permitted.
8. Positivity trap: every occupied `(h,c)` must have `pi_i>0`; deliberately place unsafe admissions in the smallest non-sentinel cell and verify they remain represented with correct weights and exact bounds.
9. Domain-masking trap: plant unsafe `AUTO` events in one crossed cell at a rate above 0.05 while pooled `C_AUTO` remains below 0.05. Pooled-only analysis may pass; the allowlist/unrestricted claim must fail or be inconclusive.
10. Sparse-cell trap: zero observed unsafe events in a noncensus cell must produce a positive simultaneous upper bound. Neighboring cells, margins, or pooled data cannot shrink it into a pass.
11. Workload-masking trap: keep pooled hours below budget but double one cell's review time. That cell cannot be allowlisted.
12. Unknown-domain trap: concentrate unsafe, high-weight admissions in `E_UNKNOWN/W_UNKNOWN`; complete known cells may pass, but unrestricted nomination must fail.
13. Reviewer-balance trap: assign slower or systematically discordant synthetic reviewers disproportionately to one cell; balance diagnostics and reviewer bootstrap must expose it, with no post-label reassignment.
14. Exact-code trap: concentrate failures in one exact service code within a family. Exact-code simultaneous diagnostics must retain the signal; post-label regrouping is forbidden. A primary crossed cell still fails if its bound fails.
15. Multiplicity trap: nominal intervals may pass while the max-statistic/Holm/exact family fails; only simultaneous bounds can nominate.
16. Nonresponse trap: concentrate missing audit labels among high-weight candidate-`AUTO` admissions. Complete-case purity may pass, but adverse partial-identification bounds must block the cell.
17. Packet leakage and canary traps: post-`D`, route, stratum, domain, clock-category, POE, target-plan, and other-role-label canaries must be detected; shared pseudonyms/filenames/timestamps enabling cross-view linkage fail masking.
18. Seal trap: mutate one submitted atomic label and require hash failure; route code cannot run before all due labels/nonresponse records are sealed.
19. Incorporation and differential-verification traps: index labels cannot resolve audit ambiguity, and every sampled apparent route receives identical audit components and safety review.
20. Unit matching/minority traps: one-to-many matching gives `U_BOUNDARY`; nine pure omissions plus one conflict gives `A_MIXED` within `A_RECON`; duplicating safe units changes neither route nor weight.
21. Unequal-fraction/pairwise trap: compare HT/Hájek variance and pairwise probabilities against exhaustive repeated sampling in small synthetic finite populations; unweighted analysis must fail when fractions differ.
22. Threshold perturbation: show `G_u>=12h` and `>=72h` sensitivity without changing `N_A`; nomination requires no adverse route reversal at 72h.
23. POE nonleakage: adding/removing the optional appendix cannot change any primary state, domain, route, burden, or gate.
24. Claim checker rejects exact-calendar, external-site, guideline-appropriateness, clinician-failure, actual-viewing, deployment-safety, causal-benefit, completion, or outcome claims.

The verifier can mechanically check sources, joins, time rules, packet access, seals, domain construction, fixed allocation, sampling probabilities, route code, survey estimators, exact/bootstrap bounds, multiplicity, gates, and whether conclusions match outputs. It cannot establish clinical truth, service ownership, exact dates, external transport, utility margins, appropriateness, actual viewing, safety, or benefit.

## Interpretation

**Supportive for a domain-restricted prospective silent validation** requires the unchanged pooled route to pass and every explicitly allowlisted crossed cell to meet source, seal, support, precision, contamination/capture, and workload gates under simultaneous adverse bounds. All nonallowlisted cells must be hard-coded to `DEFER`. This supports only observation of the frozen process in the same site's specified workflow/possible-era proxy cells.

**Supportive for unrestricted within-site silent validation** additionally requires every occupied known cell either to pass the route gate or to have a simultaneous route-burden upper bound below 1 per 100 while defaulting to `DEFER`, plus sufficiently small unknown-domain burden. It still does not support external or future temporal transport.

**Adverse** means adequately precise evidence that any cell exceeds unsafe `AUTO` contamination/leakage, misses unsafe or uncertain references, fails route confirmation, hides a minority unsafe unit, or exceeds its workload budget. Such a result falsifies transport to that cell even if pooled performance is favorable. A `RECON`-only allowlist may still be useful when `AUTO` is adverse.

**Inconclusive** includes retrieval undercoverage; broken separation/seals; mandatory workload above 900; unapproved budget; excessive `U_R/U_D` or unknown domains; sparse cell/route events; low ESS; wide simultaneous bounds; selected nonresponse; unstable matching; or any post-label design change. Inconclusive cells are not allowlisted and cannot borrow from complements. Sparse `AUTO` is described by its upper burden bound, not declared absent.

## Required next evidence and evidence ceiling

A favorable result freezes the extractor, first-eligible population, reciprocal chains, canonical `DS`, unit schema, clock logic, domain mapping, sampling/allocation code, split packets, redaction, matching, routes, audit manual, margins, and allowlist for a prospective silent study of consecutive adult discharges. New data must contain actual calendar time, immutable report finalization/addenda, report availability/viewing, discharge draft/version/edit/sign/transmission, physical departure, all recommendation units, responsibility, orders/referrals/scheduling, outside-plan attestation, preferences/competing risks, final transmitted artifact, and enough route-positive cases in each claimed workflow. A second hospital applying the frozen protocol is required for external-site transport.

Clinical appropriateness, actionability, intervention safety, utility, follow-up completion, and benefit require independent expert adjudication and a later governed route-stratified trial. MIMIC cannot establish them.

## Substantive advance and remaining uncertainty

The parent prevented a route from validating itself. This child prevents a large pooled workflow from validating a route on behalf of a smaller unsafe or unworkable crossed domain, while preserving the fixed workload. Its bounded partition makes positivity feasible by construction; its coverage-plus-minimax integer allocation has exact inclusion probabilities and controls worst weights without route-based top-ups; and its absolute worst-domain allowlist avoids the weak inference that a nonsignificant interaction proves stability. Unsupported cells default to `DEFER` rather than being smoothed toward the pooled mean.

Important uncertainty remains. `anchor_year_group` supplies only a widened possible-calendar band, not exact time. Terminal service and ICU exposure are workflow proxies, not ownership or responsibility. Some crossed cells or route denominators may remain too sparse under 900 reviews, making unrestricted nomination honestly inconclusive. Independent experts can share correlated error; the audit is independent text interpretation, not truth. The canonical `DS` and storage clocks incompletely represent the transmitted artifact and opportunity to act. Retrieval may miss semantic opportunities. Thus even a complete pass advances evidence only from pooled retrospective reproducibility to fixed-workload, domain-stressed retrospective reproducibility and can nominate only prospective silent validation.
