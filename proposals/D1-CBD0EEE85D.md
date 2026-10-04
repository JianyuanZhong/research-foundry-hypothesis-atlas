> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Finite-corpus HCC documentary-M2 experiment with a computable ridge/elastic-net grid

## 1. Focused child repair and preserved scientific target

This child is a normative, focused repair of assessed-valid parent `[prior hypothesis]`. Every parent rule remains controlling except its definition and certification of the elastic-net regularization grid, which this proposal replaces in Section 6.

The parent requires, for every `alpha in {0,.25,.5,.75,1}`, a finite `lambda_max` at which every penalized coefficient is exactly zero. That condition is generally impossible when `alpha=0` (pure ridge). At a zero slope vector the derivative of the L2 penalty is zero, so a nonzero loss gradient cannot be cancelled by any finite ridge penalty. Requiring a zero-slope KKT certificate for pure ridge would therefore force an otherwise valid experiment to be inconclusive for a mathematical reason unrelated to the HCC data or hypothesis.

The repair retains pure ridge, the four positive-L1 elastic-net families, one locked robust model per information set, independent `R` and `G` tuning, and all exact solver gates. It defines a certified zero-slope anchor only where one exists (`alpha>0`) and uses that anchor to define a finite prespecified ridge grid without claiming that ridge reaches an exact all-zero model. This changes no population, time boundary, feature, outcome, capacity, contrast, state envelope, finite-corpus inference rule, or clinical interpretation.

## 2. Clinical question, evidence boundary, and advance

### Strongest claim supported before the experiment

The configured HCC snapshot contains patient- and encounter-linkable procedure, examination, medication, non-drug order, and pathology rows. Procedure rows contain source labels and start/end fields; examination rows contain an accession-like identifier, acquisition-like start, machine label, and eventual narrative findings/diagnosis; pathology contains untimed same-encounter narratives. Those fields are sufficient to construct a source-defined first-resection frame, chronology-safe finite alternatives, eventual-report concept features, and an encounter-documentary M2 outcome if the prespecified expert and completeness gates pass.

They do not show that a listed operation was completed, that duplicate or adjacent procedure rows are one operation, that pathology belongs to the selected resection specimen, or that documentary M2 is biological high-grade microvascular invasion under an adequate sampling standard. The snapshot contains no pathology time, specimen/accession/slide/block identifier, sampling record, source images, report author/final/release/version/view time, review roster/action, recurrence, survival, treatment response, harm, cost, equity outcome, or clinical benefit.

The frozen full-text Europe PMC XML for Feng, Qu, and Han's 2026 systematic review was inspected (J Med Internet Res 2026;28:e82000; DOI `10.2196/82000`; PMCID `PMC12954728`; frozen source `[source checksum]`, [source checksum]). It reports 52 studies and 19,531 patients, lower SROC under independent external than internal validation (0.85 versus 0.90), heterogeneity, scarce independent validation, and a need for prospective multicenter evaluation. This motivates strict temporal evaluation and restrained claims; it does not validate this report-semantic construct, this M2 abstraction, or any treatment effect.

The research-ambition README was inspected. It says the natural-history and Bayesian demonstrations have frozen article/supplement files, whereas the Cell cancer demonstration has metadata and a supplement but not the main article or full STAR Methods. No unavailable article text is claimed as inspected or used to dictate this design.

### Unresolved falsifiable hypothesis

Among adults in the finite-ledger first eligible source-documented HCC resection frame, with same-encounter documentary HCC pathology and no recorded qualifying HCC treatment during the preceding 365 days, does one locked model using adjudicated meanings in eventual stored preoperative CT/MRI report text capture more encounter-documentary M2 cases at exactly the same fixed top-K capacity than both:

1. an independently optimized nested comparator with identical nonsemantic acquisition and documentation-surface information; and
2. the same fitted full model after complete semantic masking,

by strictly more than 5 captures per 100 positions in every admissible outer-envelope state world, separately in 2020 and 2021?

The substantive advance is robust retrospective evidence that stored-report meaning contributes to ranking composition beyond documentation surface and that the fitted score actually depends on that meaning. It is not evidence that reports were available in real time, a diagnostic claim about biological M2, a deployment result, or proof of clinical benefit.

## 3. Frozen population, clocks, and finite ambiguity ledger

For offset `d`, include at most one row per patient in a state only if all conditions hold:

- age is at least 18 in the selected encounter;
- the episode is the patient's earliest eligible source-documented procedure under a frozen hepatobiliary-surgery dictionary;
- blinded pathology adjudication finds at least one same-encounter pathology composite explicitly supporting HCC;
- no recorded prior HCC resection, transplant, TACE, ablation, radiotherapy, targeted therapy, or immunotherapy occurs in `[c_d-365d,c_d)`.

The primary offset is `d=24` hours and `c_d=t_op-d`; `d in {12,48,72}` are locked sensitivities. The report acquisition window is `[c_d-90d,c_d)`. The cutoff is analytical and is not a report-release, clinician-view, referral, or decision time.

Two hepatobiliary surgeons, with third-review resolution, classify every procedure/order/medication label touched by the rules before outcomes are opened. Raw and normalized labels, source table/column, counts, decisions, unresolved alternatives, reviewers, versions, and hashes are retained. “No recorded prior treatment” is not biological treatment-naivety.

Exact-deduplicate procedure rows over their six fields while retaining source ordinal/backpointer. Form same-patient, same-encounter, same-calendar-day provisional episodes. Preserve defensible adjacent-day, source-conflict, duration, multiple-date, and clock alternatives unless a signed clinical rule or source operation identifier resolves them. Non-midnight anesthesia-system times may be point clocks only after source validation; date-only or unvalidated midnight values are intervals `[date,date+24h)`. Partition clock intervals at every examination-window, prior-treatment-window, and calendar-role boundary so predicates are constant within a cell.

For each patient emit a relational, not Cartesian, finite set `S_i+` of outer states. Each state binds one episode and clock cell to encounter age, year/role, prior-treatment status, eligible whole examination units, `Z,S,X`, encounter-specific pathology, outcome completion, membership, and raw provenance. A state never borrows an examination, pathology, outcome, or treatment status from another episode. Nonmembership is a state, not `Y=0`.

The frozen high-sensitivity ambiguity ledger includes every exact-deduplicated row that can alter procedure candidacy/linkage, age, clock, year, treatment history, examination identity/modality/window, report body, HCC pathology, M2 completion, or denominator. Each branch must terminate as an emitted `S_i+` state, a machine-checkable deterministic impossibility, or an adjudication-only exclusion retained in `S_i+` but omitted from secondary `S_i*`. Primary fits, K feasibility, and test extrema use `S+`; `S*` is adjudication-conditional only. No state cap, beam search, random state sample, approximate favorable search, or time-limit incumbent can support or falsify the primary hypothesis.

Chronology-safe superframes remain:

- `U_T`: any patient with any eligible 2020 or 2021 state; excluded from all fitting/tuning in every alternative state;
- among the remainder, `U_V`: any patient with any eligible 2019 state;
- among the remainder, `U_D`: any patient with any eligible 2015-2018 state.

A test world chooses one state per `U_T` patient. A patient ambiguous between 2020 and 2021 can belong only to the year selected by that same state. The annual targets are separate and never pool or compensate. Data from 2022 onward are audit-only.

## 4. Examination units, documentary outcome, and exact information sets

A nonblank whole examination unit is `(patient master index, encounter number, examination number)`, retaining all exact-deduplicated component rows and immutable boundaries. Blank `examination number` is identity-unknown and cannot provide primary semantics. Conflicting modality, components more than 24 hours apart, and possible merged identity remain alternatives. A unit is eligible only if every retained component acquisition interval is wholly compatible with `[c_d-90d,c_d)`. Select at most the latest whole CT and latest whole MRI by latest admissible component start, raw ordinal, then frozen patient hash. Concatenate complete-unit `examination findings` and `examination diagnosis` in raw component order; phrase selection is forbidden.

Two blinded abdominal radiologists, with a third resolver, classify modality and annotate maximum lesion diameter, lesion count, capsule, margin, arterial hyperenhancement, washout, peritumoral enhancement/hypointensity, satellite lesion, portal/hepatic-vein tumor thrombus, cirrhosis, and ascites. Each is `present/absent/uncertain/not-mentioned/source-text-unavailable`. These are meanings in stored text, not image or biological findings.

For every possible index encounter, exact-deduplicate all six-field pathology rows and concatenate all `Pathology`, `Examination Findings`, and `Examination Diagnosis` with raw row/field boundaries. Two blinded Chinese-reading pathologists and a third resolver apply the frozen rubric:

- `Y={1}`: M2 is explicitly anchored to microvascular invasion or an HCC MVI grade;
- `Y={0}`: anchored M0/M1 excludes M2 in the relevant context;
- `Y={0,1}`: missing, unanchored, boilerplate, contradictory, attribution-uncertain, or inadequate.

Unknown is completed only inside the coupled state world and never imputed negative. Require at least 85% anchored adjudicated grade and at least 50 lower-envelope M2 events in each test year. These gates do not establish specimen linkage, sampling adequacy, or biological M2.

`Z` contains age, sex, CT/MRI/other indicators, eligible-unit count, acquisition-to-cutoff recency, component count, identity/accession ambiguity, source-text-unavailable, and development-grouped `Machine Model`; identifiers never enter.

`S` contains only modality-specific documentation surface: untrimmed Unicode code-point length; nonblank findings/diagnosis indicators; digit, punctuation, whitespace, Han, and other-character proportions; component count; blank/conflicting accession; and separator count. It contains no token, n-gram, semantic flag, hand-picked phrase, pathology, laboratory, diagnosis, or clinical-document content.

`X` contains only the modality-specific adjudicated concepts and explicit uncertain/not-mentioned/unavailable levels. Shared `Z,S` preprocessing and column order are byte-identical in `R` and `G`. One patient-balanced, outcome-blind preprocessing map is computed over all eligible outer development states, with each patient total weight one, and is frozen for all worlds.

## 5. Models and unchanged robust objective

Use additive logistic regression with an unpenalized intercept and elastic-net penalty

`P_alpha(beta)=alpha*||beta||_1 + (1-alpha)/2*||beta||_2^2`.

No interactions, splines, unrestricted text, test-derived features, or test refits are allowed.

- `B(Z)`: acquisition-only diagnostic baseline;
- `R(Z,S)`: independently optimized reduced comparator;
- `G(Z,S,X)`: full model;
- `Gmask`: no fit or recalibration; apply fitted `G` after replacing every `X` level, including uncertain and not-mentioned, with its training-defined source-text-unavailable level while leaving `Z,S` unchanged.

For model `M`, hyperparameter `h=(alpha,lambda)`, and development world `w`, retain the parent's normalized robust objective:

`beta_hat_M(h)=argmin_beta [max_{w:n_D(w)>0} L_M(beta,w)+lambda*P_alpha(beta)]`.

Outcome completions stay coupled to source states. Exact Dinkelbach separation solves the worst normalized finite world, and a convex epigraph cutting-plane master adds worlds until omitted-world violation is at most `1e-8`, primal-dual gap at most `1e-8`, and two canonical separations add no world. Store cuts, active worlds, residuals, objective, KKT/primal-dual certificates, hashes, solver versions, and seeds. Approximate separation is nonconfirmatory.

## 6. Normative repair: finite regularization grids that are mathematically certifiable

This section supersedes the parent's generic claim that every alpha has a finite all-zero `lambda_max`.

For each `M in {B,R,G}`, using its fixed outer-development preprocessing and normalized minimax loss, define `A_M` as the smallest nonnegative L1 penalty coefficient for which a zero slope vector is globally optimal with `alpha=1`; the unpenalized intercept is optimized. Find `A_M` by deterministic doubling to a feasible upper bracket followed by certified monotone bisection to relative tolerance `1e-8`. Certification must include:

- an attained finite robust intercept solution;
- active worst-world cuts or an exact separator;
- a convex combination/subgradient of active worst-world losses;
- zero intercept subgradient; and
- slope KKT inequalities `|g_j| <= A_M` for every penalized column.

If no finite intercept optimum or certificate exists, model fitting is inconclusive.

If `A_M>0`, use exactly these prespecified families:

- for each `alpha in {.25,.5,.75,1}`, `lambda_hi(M,alpha)=A_M/alpha` and 100 log-spaced values from `lambda_hi` to `10^-4*lambda_hi`; the highest value must have a stored exact zero-slope KKT certificate because its effective L1 coefficient is `A_M`;
- for `alpha=0`, use 100 log-spaced finite ridge values from `A_M` to `10^-4*A_M`. No exact zero-slope claim or zero-slope gate is made for ridge. Every fitted ridge solution still requires the same robust master/separation and KKT/primal-dual certificates as every other candidate.

If `A_M=0`, zero slopes already minimize the unpenalized convex robust loss. Collapse duplicate candidates for every alpha to one canonical `lambda=1` zero-slope fit per alpha after a stored global KKT certificate; do not attempt a log grid with zero endpoints.

The serialized grid, `A_M`, brackets, bisection trace, effective L1 coefficients, duplicate map, and every fit certificate are frozen before 2019 evaluation. Independently choose `R` and `G` hyperparameters on the complete 2019 superframe by maximum sharp worst-state fixed-K documentary capture, with the parent's tie order, using no 2020/2021 outcomes. `B` is similarly locked for diagnostics. Descriptive calibration cannot alter ranking.

A mandatory adversarial fixture is `x=(-1,1), y=(0,1)` with an optimized intercept. At zero slope the logistic-loss gradient is nonzero, while the ridge derivative is zero; the verifier must show that no finite `alpha=0` value satisfies the old zero-slope KKT rule, that `A_M` is finite for lasso, and that the repaired ridge grid fits and certifies without asserting an all-zero endpoint. This fixture directly distinguishes a correct repair from silently dropping ridge or preserving the impossible gate.

## 7. Preserved fixed-K estimand and exact finite-corpus analysis

Before test outcomes or semantic annotations are consulted, compute the sharp minimum eligible count `N_a(w,d)` for each year `a=2015,...,2019`, offset `d in {12,24,48,72}`, and outer world `w`. Freeze

`N_ref=min_{a,d,w} N_a(w,d)`,
`K_rho=floor(rho*N_ref)` for `rho in {.05,.10,.20}`.

The confirmatory capacity is `rho=.10`. Require `N_ref>=500`, `K_.10>=50`, and at least `K_.10` eligible patients in every admissible 2020 and 2021 world. The .05/.20 capacities are sensitivities and cannot rescue the primary. This is an analytic fixed capacity, not evidence that K is operationally acceptable; acceptability requires a real review service and prospective capacity data.

In each world rank by locked score, frozen SHA-256 patient tie key, and raw episode backpointer, selecting exactly K whole patients. For model `M` and year `a`:

`T_M(a,w)=100/K * sum_{i in TopK_M(a,w)} Y_i(s_i)`.

The co-primary contrasts are:

- `Delta_nested=T_G-T_R`;
- `Delta_mask=T_G-T_Gmask`.

`Delta_surface=T_R-T_B` is diagnostic and cannot veto or supply semantic support. For each contrast and each year 2020/2021 compute certified attained outer-envelope extrema `[delta^-,delta^+]=[min_w Delta,max_w Delta]` with the same state shared by both arms. Store witness-world hashes, both top-K sets, arithmetic traces, and zero unresolved integer gap (reported numerical gap at most `1e-8`). Raw and exact lossless-quotient representations must replay identically; synthetic fixtures through 12 patients and real shards through 20 patients must match exhaustive enumeration. Timeout, omitted state, invalid quotient, or uncertified optimum makes the affected primary family inconclusive.

The target is the complete frozen accessible HCC corpus under declared source rules. The extrema are attained ambiguity bounds, not confidence intervals. No primary bootstrap, standard error, significance test, patient-sampling law, or generalization is permitted. Resampling/permutation may be assumption-indexed diagnostics only and cannot alter a label.

## 8. Falsification and mutually exclusive interpretation

After every mandatory gate passes, for coordinate `e=(year,contrast)`:

- supportive if `delta^-_e>5`: every admissible outer world exceeds the margin;
- heterogeneous if `delta^-_e<=5<delta^+_e`: attained worlds lie on both sides;
- all-world-adverse if `delta^+_e<=5`: even the best world does not exceed the strict margin.

Equality to 5 is adverse. Any `delta^-<=5` falsifies the universal conjunction. Global labels are exactly:

1. **Universal-supportive** only if all four coordinates are supportive.
2. **Decisive-threshold-heterogeneity** if at least one coordinate/world exceeds 5 and at least one coordinate/world fails it.
3. **Universal-adverse-without-positive-coordinate** if every `delta^+<=5`.
4. **Inconclusive** if any mandatory source, adjudication, event, state-completeness, preprocessing, grid, fit, quotient/replay, top-K, or exact-solver gate fails.

A supportive result permits only this claim: in this frozen retrospective eventual-report corpus, the locked full score exceeded both semantic controls by more than 5 documentary-M2 captures per 100 fixed positions in every declared outer state, separately in 2020 and 2021. It does not establish statistical significance, future performance, biological M2, report availability, actionability, or benefit.

A heterogeneous or all-world-adverse result falsifies the strict universal margin as specified, but does not prove report meaning is useless, that smaller effects are absent, or that biological MVI cannot be predicted. Inconclusive means the exact question was not validly instantiated or computed; it is not an adverse scientific result.

## 9. Exact HCC source bindings and availability

Controlling catalog: `[internal dataset path]`, [source checksum]. HCC snapshot: `[source checksum]`. All HCC members are ordinary read-only CSV files (catalog member `null`; no archive member).

- `encounters`: `[internal dataset path]`. Exact join `patient master index,encounter number`; `age,sex` supply Z; `encounter time,admission time,discharge time` are audits.
- `procedures`: `[internal dataset path]`. Keys plus `surgery,start time,end time,surgery source` define episode/clock and prior-treatment evidence.
- `examinations`: `[internal dataset path]`. Keys plus `Examination Number` define units; `Examination` modality; `Examination Findings,Examination Diagnosis` S/X; `Start Time` acquisition; `Machine Model` Z.
- `pathology`: `[internal dataset path]`. Keys plus `Pathology,Findings,Diagnostic impression` define HCC frame/Y; `Machine model` provenance. It has no time, specimen, or pathology-accession column.
- `medications`: `[internal dataset path]`. Keys plus `medication, medication type, start time, end time` supply prior systemic-treatment evidence.
- `orders`: `[internal dataset path]`. Keys plus `non-drug orders,order time,start time,end time,order status` supply prior local/radiotherapy evidence.
- `diagnoses`: `[internal dataset path]`; `diagnosis name, diagnosis type` are untimed corroboration only.
- `labs`: `[internal dataset path]`; `Test,Qualitative Result,Quantitative Result,Specimen Type,Test Time` are lineage audit only and never predictors.
- `clinical_documents`: `[internal dataset path]`; keys/narratives are audited but excluded because there is no document time/version; duplicate raw `Admission diagnosis` maps to catalog `Admission diagnosis__duplicate_2`.
- `vitals`: `[internal dataset path]`; `patient master index, encounter number` only.
- `transfers`: `[internal dataset path]`; `patient master index,encounter number` only.
- `front_page`: `[internal dataset path]`; identifier header only.

Same-encounter joins are exact on `(patient master index,encounter number)`; examination grouping adds `examination number`; treatment lookback is patient-wide on `patient master index` followed by interval logic. Direct identifiers, untimed diagnoses/documents, post-cutoff examinations, identifier-only tables, and labs are forbidden predictors. Raw ordinals and backpointers survive every derivation.

The catalog schemas and live UTF-8-sig headers were rechecked for the six payload tables above. The parent's aggregate availability audit remains descriptive only: 105,044 encounter rows/43,815 patients, 338,040 procedure rows/43,062 patients, 419,996 examination rows/42,206 patients, and 46,395 pathology rows/28,184 patients; 419,821 examination rows had a narrative field, 419,924 had nonblank `Examination Number`, and all 46,395 pathology rows had an outcome-source narrative field. These are not eligible cohort or M2-event counts.

MIMIC, eICU, and UKB remain directly readable and unmodified. MIMIC is the archive `[internal dataset path]` with members including `mimic-iv-3.1/hosp/admissions.csv.gz` and `note/radiology.csv.gz`; eICU has 31 ordinary files under `[internal dataset path]`, including `patient.csv.gz,diagnosis.csv.gz,note.csv.gz`; UKB has eight ordinary CSVs under `[internal dataset path]`, including `ukb672073.csv` and assessment/outcome/genomics/follow-up tables. They are not pooled because there is no patient crosswalk and they do not instantiate this HCC resection/eventual-report/untimed-pathology estimand. Their exclusion is scientific, not an access restriction.

## 10. Required outputs and verifier boundary

Publish the canonical raw and quotient state ledgers, provenance, dictionary/rubric/adjudication hashes, filter counts, superframes, denominator ranges, `N_ref`, K, event gates, preprocessing hashes, `A_M` and regularization-grid manifests, robust-fit certificates, eight primary endpoints and witnesses, top-K hashes, arithmetic traces, coordinate/year labels, and one global label.

The verifier can check source hashes/headers, joins, deduplication, breakpoints, chronology quarantine, state-DAG reachability, quotient/replay, feature lineage, shared `Z,S`, no-refit masking, the repaired alpha/lambda construction, KKT logic, independent model tuning, fixed K, exact extrema, threshold arithmetic, and conclusion-to-output linkage. It must include the pure-ridge fixture in Section 6, exact equality at 5, supportive, heterogeneous, all-world-adverse, and failed-gate outcomes. It must accept correct adverse and inconclusive reports rather than reward confirmation.

It must reject a numerically correct report that calls ambiguity extrema confidence intervals, claims significance/generalization, treats eventual reports as timely, treats documentary M2 as specimen-linked biology, treats K as acceptable clinical workload, recommends action, or claims benefit. Automatic verification cannot establish clinical dictionary completeness, expert qualifications or adjudication correctness, Chinese meaning, operation completion, pathology specimen linkage/sampling, report finalization/release/view, workload acceptability, future performance, clinician response, treatment effect, benefit, fairness, or transportability.

A future clinical study needs validated operation clocks and completion, report-version/finalization/release/view logs linked to selected accessions, specimen-linked pathology and sampling review, a real consecutive candidate stream, prospectively justified K and staffing, silent-mode clinician workflow, subgroup monitoring, and external temporal/site evaluation. Recurrence, survival, treatment effect, harms, costs, and benefit require additional outcomes and an appropriate controlled design.
