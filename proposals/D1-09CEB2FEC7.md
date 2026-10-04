> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Bundle-valid modality-pattern access requirements for documentary-M2 review

## Unresolved clinical question and substantive advance

The consequential but bounded question is whether, 24 hours before an adult patient's first eligible HCC resection, semantics in routine CT/MRI reports can add clinically material value to a laboratory-independent flag for multidisciplinary review of pathology-documented high-grade microvascular invasion (M2). The flag is not a recommendation for resection extent, transplant, systemic or locoregional treatment, adjuvant therapy, or surveillance.

**Strongest claim supported now.** Direct catalog, schema, header, and aggregate source inspection establishes that this HCC snapshot contains operation starts, examination acquisition starts, eventual CT/MRI report bodies, and untimed same-encounter pathology text. It does not contain report authored/final/release/view times or version history, pathology times or specimen identifiers, raw images/slides, sampling protocols, recurrence, survival, clinician response, treatment benefit, harms, or costs. The laboratory table has one ambiguous `Test time` and no collection, result-entry, finalization, release/view, accession/panel, or unit field, so all laboratory fields and process derivatives have zero primary lineage. These are source facts, not evidence that any model works or that eventual report text was available at the decision time.

The full XML of Li et al. (2025; DOI `10.1111/jcmm.70746`, PMCID `PMC12309289`, frozen source `[source checksum]`, [source checksum]) supports that MVI is pathology-defined, prognostically relevant, and unavailable directly for preoperative decisions, while prediction and management evidence remains limited. The full HTML of Huang et al. (2026; DOI `10.3389/fonc.2026.1821034`, frozen source `[source checksum]`, [source checksum]) reports a binary-MVI CT-margin/AFP model in 487 development and 256 external-validation patients (AUC 0.740/0.781), with complete-data eligibility, blinded raw-image review, and defined pathology sampling. Neither source validates M2 extraction from this snapshot, routine report semantics, report visibility, or treatment benefit.

**Unresolved computable hypothesis P.** In the locked 2020–2021 whole target frame, when all selected nonempty stored CT/MRI bundles are exposed, the fitted semantic strategy S will exceed (i) the same fitted pipeline with only semantic fields ablated, S0, and (ii) an independently optimized structured/basic-report baseline B, by a net-benefit margin greater than 0.01 at threshold 0.30 with simultaneous uncertainty, positive lower bounds from 0.25 through 0.35, superiority to flag-all/flag-none, and a passed semantic-null control.

**Unresolved transport hypothesis T.** If P is supported, there is an upward-closed set of minimum report-access guarantees `H` across patients with CT-only, MRI-only, and dual stored-report patterns such that the worst-case S-S0 and S-B net-benefit lower bounds still exceed 0.01. T asks whether value is access-robust or depends consequentially on one modality. It does not assert that those guarantees were met.

**Unidentified decision-time claim D.** Exact semantic value at `t_dec` is not identified here. D can be supported conditionally only by a separate source-system audit proving that the exact report version used by extraction was final/released and preferably viewable before `t_dec`, under the same bundle and pattern units, with conservative simultaneous lower confidence bounds that fall inside H.

This advances the selected bundle-valid design by replacing a pooled patient-any requirement, which can conceal CT/MRI dependence, with exact bundle-valid pattern requirements. It also repairs the prior pattern proposal by retaining patients with no nonempty stored report as a fixed contribution to the whole-frame denominator and by requiring an exclusive, adjudicated modality assignment before a multirow bundle enters a pattern stratum.

## Direct source audit and bundle construction

Snapshot: `[source checksum]`.

A full aggregate scan of all 419,996 examination rows found 393,468 nonblank keys on `(Patient master index,Encounter number,Examination number,Start time)`, 16,099 multirow keys (maximum 12 rows), 16,086 keys with multiple normalized `Examination` labels, and 72 blank-`Examination number` rows. A broad lexical diagnostic found no CT/MR-conflicted key but recovered no MRI from `Examination` labels alone; it is not a clinical dictionary or cohort prevalence estimate. The inherited broad 2015–2021 audit found component multiplicities through 10 and 5,038 frame patients without a selected nonempty report. These diagnostics establish source grain and motivate the fixed no-report stratum; final execution must emit its own frozen-dictionary attrition.

1. Deduplicate exact examination rows on all eight columns.
2. With nonblank `examination number`, bundle all rows sharing `(patient master index,encounter number,examination number,start time)` before modality filtering or text extraction. Never split component rows into visibility units.
3. Two blinded abdominal radiologists freeze a development-only map using all normalized bundle `examination` values and `machine model`, assigning exactly one of CT, MRI, non-target, or unresolved/conflicted. A bundle cannot be copied into both CT and MRI. Unresolved/conflicted bundles remain in audit counts and acquisition diagnostics but cannot provide primary report-body features or establish a pattern claim. Require >=0.95 agreement and <=1% unresolved among candidate target bundles for pattern support; otherwise T is inconclusive.
4. Blank-ID rows are logged but are not primary semantic bundles. A singleton sensitivity is descriptive and cannot support report-level availability.
5. For each modality select at most the latest eligible bundle in `[t_dec-90 days,t_dec)`, tie-breaking by valid `Start Time`, normalized nonempty `Examination Number`, then normalized bundle label. Concatenate all component `Findings` and `Diagnostic Impression` fields in deterministic source order before extraction. Expose or mask the entire bundle.
6. Let `E_ij=1` only when selected bundle j has a nonempty eventual body. Empty bundles remain acquisition facts but have no exposed-content state.

Report counts, exact duplicates, blank IDs, invalid clocks, component multiplicity, modality assignments/disagreements, selected/discarded bundles, ties, empty text, and final pattern counts by year before reading test outcomes.

## Population and temporal boundaries

The unit is one patient (`Patient Master Index`) and one first eligible index resection.

- In `procedures`, select the earliest valid `start time` whose normalized exact `surgery` is in a clinically reviewed dictionary of partial, segmental, hemihepatic, or liver-tumor resections. Exclude transplant, biopsy/puncture, ablation-only, gallbladder-only, metastatic-organ surgery, and explicit repeat/recurrence procedures. Break exact-time ties by `encounter number` and normalized `surgery`; output every raw value/frequency and exclusion.
- Require age >=18 from a uniquely resolved same-encounter `encounters` row and same-encounter pathology text explicitly identifying HCC. This is a retrospectively resected, pathology-confirmed frame, not preoperative diagnostic certainty, curative intent, resectability, or biological treatment-naivety.
- Define `t_dec=procedures.Start Time-24 hours`. No content at or after it predicts. Repeat fixed 12-, 48-, and 72-hour buffers as sensitivities.
- Exclude recorded prior HCC resection, transplant, TACE, ablation, radiotherapy, targeted therapy, or immunotherapy in `[t_dec-365 days,t_dec)` from reviewed `procedures`, `medications`, and `orders` dictionaries using valid source clocks. Analyze recorded prior treatment separately.
- Use 2015–2018 for development, 2019 only for penalty selection and recalibration, and untouched 2020–2021 for primary test. Exclude 2013–2014. Use 2022–snapshot end only for template/extraction/ascertainment drift audits; make no current performance claim.
- Retain every target-frame patient, including those with no selected nonempty report and uncertain MVI grade. Freeze all dictionaries, parser rules, bundle/modality rules, features, preprocessing, robust loss, solver, thresholds, bootstrap family, pattern grid, and gates before test outcomes are accessed.

## Documentary outcome and adjudication

`Y=1` only when a frozen position-aware parser plus blinded adjudication assign explicit M2 to the index resection pathology. `Y=0` for explicit M0/M1. Let `V=1` denote a trustworthy assignment. Missing grade, binary-positive ungraded MVI, conflict, uncertain specimen linkage, or inadequate documented sampling is `V=0` with `Y in {0,1}`; never exclude or impute it.

Only the immediate selected value after a frozen anchor such as `MVI risk grade indication[:：]`, stopping before definitions, history, or another specimen section, or a reviewed synonymous selected-value construction may assign grade. Unanchored M2 and boilerplate cannot. Two independent parser implementations must agree. Two qualified Chinese-reading pathologists blinded to predictors and scores review every parsed M2, every conflict, every locked-test V=0, and at least 150 sampled M0 plus 150 M1 stratified by year/template; a third resolves disagreement. Require class PPV >=0.98, sensitivity >=0.95, kappa >=0.90, and parser disagreement <=5%.

Raw slides, specimen IDs, block counts, vessel distances, and sampling protocols are absent. The outcome is documentary M2, not latent biological M2.

## States, models, and baselines

After bundle selection, define stored-text pattern `g_i`:

- `O`: no selected nonempty bundle;
- `C`: CT only;
- `M`: MRI only;
- `CM`: one CT and one MRI nonempty bundle.

For C/M there are unavailable/exposed states; for CM there are none, CT-only, MRI-only, and both. O has one fixed state. A visible bit exposes the entire eventual stored body; zero masks every body-derived size, count, thrombus, formatting, and semantic field while preserving acquisition modality/time/count and a development-frequency machine category. Every compared score uses the identical state and CT-then-MRI bit order. No independence, random visibility, or missing-at-random assumption is allowed.

Fit interpretable elastic-net logistic models with the inherited patient-wise worst-state convex loss over both `Y_i` and report states in 2015–2018, and use the same rule for 2019 tuning/nonnegative-slope recalibration, every bootstrap, and every matched-null refit. Equal-state, all-report, and no-report fits are diagnostics only.

- `B`: age, sex, acquisition indicators, development-frequency machine category, and—only when a body is exposed—frozen maximum lesion diameter, lesion-count category, and explicit macrovascular tumor thrombus with unknown indicators.
- `S=B+C_R`, where `C_R` is a frozen present/absent/unknown block for capsule complete/interrupted/absent, irregular/non-smooth margin, satellite/peritumoral lesion or enhancement, arterial hyperenhancement, washout, and peritumoral hypointensity.
- `S0` is never refit. Use S's exact coefficients, intercept, preprocessing, penalty choice, and recalibration, replacing only `C_R` by its state-zero vector. Require bitwise-equal S and S0 scores whenever no semantic bundle is exposed.
- `W` and `A=W+C_R` remain secondary nested workflow/provenance diagnostics. Unrestricted text is a ceiling only.

Labs, diagnoses, pathology, procedures, identifiers, year, and post-cutoff content cannot enter predictors. Prove zero lab and forbidden lineage.

Two blinded radiologists adjudicate extracted report features by year, modality, and stored pattern. Require size agreement within 5 mm or 10% in >=90%, count agreement >=90% and kappa >=0.80, and PPV/sensitivity >=0.85 for every binary feature in every claimed modality stratum.

## Estimands and exact pattern frontier

At threshold `p`, `w=p/(1-p)`, `I_Mi(r,p)=1[score_Mi(r)>=p]`, and for contrast `j=(M1,M0)`:

`d_ij(y,r,p)=[y-w(1-y)] [I_M1i(r,p)-I_M0i(r,p)]`.

Primary contrasts are `D=(S,S0)` and `C=(S,B)`; defaults are `F_all=(S,flag-all)` and `F_none=(S,flag-none)`. Every value is divided by whole target-frame N. For V=0, minimize/maximize over both labels; for V=1 use adjudicated Y.

First compute the all-stored-content intervals with every E=1 bundle exposed. P requires one-sided 97.5% simultaneous lower limits for D and C above `m=0.01` at p=.30, both defaults exceeded by .01, D/C point lower bounds positive at `p in {.25,.275,.30,.325,.35}`, and the null/calibration gates below.

For pattern transport, set `N_g=|{i:g_i=g}|` and `k_g=ceil(h_g N_g)` for `g in {C,M,CM}` and `h_g in {0,.05,...,1}`. O has no access coordinate and contributes its fixed unavailable cost to every whole-N bound. Within CM, “exposed” means CT-only, MRI-only, or both; the adversary may choose any of those states.

Fold outcome uncertainty into state costs `ell_ij(r,p)=min_y d_ij(y,r,p)` and `u_ij(r,p)=max_y d_ij(y,r,p)`. For a lower stratum bound define `l_i0=ell_i(all-unavailable)` and `l_i1=min_{r:any exposed} ell_i(r)`. Start from `min(l_i0,l_i1)`; if fewer than k_g patients are thereby exposed (ties count exposed), force the required additional patients using the smallest sorted positive differences `l_i1-l_i0`. For the upper bound use `u_i0`, `u_i1=max_{r:any exposed}u_i(r)`, start from their maxima, and force extra exposure with the smallest losses. Add the fixed O contribution and the three disjoint stratum sums, then divide by N.

This sorted binary-cost algorithm is exact. It must equal exhaustive enumeration for every fixture with total N<=12, include dual CT-only/MRI-only/both states and O, and machine-check coordinatewise monotonicity. A seeded implementation already matched 4,520 lower/upper endpoint checks across 100 random small instances.

Define support set H as pattern grid points whose simultaneous lower limits for D, C, F_all, and F_none exceed their frozen margins and whose D/C point lower bounds are positive across all thresholds. H must be upward closed; report its Pareto-minimal antichain, not a cherry-picked point. `N_g=0` makes that modality-specific claim unavailable rather than deleting patients. A claimed stratum requires N_g>=100 and >=20 adjudicated M2 events. Retain the pooled patient-any frontier as a secondary conservative benchmark.

## External clock/version audit

A conditional D claim requires a representative source-system audit from the same workflow/era that applies the identical target population, `t_dec`, bundle key, modality map, latest-bundle rule, and stored-pattern definitions. For every selected nonempty bundle it must retrieve final/release time and preferably clinician-view time plus an immutable version identifier or content hash proving that the exact text used by feature extraction existed by `t_dec`. Acquisition/order time or later nonempty text is insufficient.

Report simultaneously, within C, M, and CM, the patient fraction with at least one exact selected bundle visible by `t_dec`; in CM also report CT-only, MRI-only, and both-visible fractions. Account for patient clustering, calendar/workflow strata, missing logs, and repeated examinations. Round simultaneous one-sided 97.5% lower confidence bounds down to the 0.05 grid. A conditional decision-time statement is allowed only if that conservative vector lies in H. A 97.5% simultaneous model family plus a separate 97.5% simultaneous audit family gives joint noncoverage <=5% by Bonferroni; joint resampling may replace this. Audit absence, nonrepresentativeness, missing version identity, or use of a different unit makes D inconclusive.

## Inference, gates, and falsification

Use 2,000 patient bootstraps within calendar period, rebuilding bundles, states, preprocessing, robust fits, recalibration, every contrast, all pattern points, and all thresholds. A frozen max-absolute-centered-deviation procedure supplies the 97.5% simultaneous model family over all lower/upper endpoints. More than 2.5% failed refits invalidates support.

Use 1,000 development/tuning-only semantic-null repetitions that permute the complete `C_R` bundle block within frozen year, modality/pattern, state cardinality, and formatting family, followed by full robust refit and S0 reconstruction. All-store D at .30 must exceed the frozen 97.5th null percentile. Label permutation must behave as null and post-cutoff injection must trigger leakage controls.

Global gates: test N>=1,000; >=75 adjudicated V=1 M2; V=1>=85%; every test V=0 reviewed; all parser/radiologist/modality thresholds pass; nonempty text in >=80% of selected candidate target bundles; size/count jointly extractable in >=70%; no required-feature or pattern-frequency shift from 2019 to either test year >15 percentage points; exact fit/frontier convergence; complete simultaneous inference; shared states; and zero forbidden/lab lineage. Report AUROC, AUPRC, Brier, calibration intercept/slope, sensitivity, specificity, PPV, and NPV among V=1 in all/no-report diagnostics. A global strategy claim additionally requires slope .80–1.20, intercept -.10–.10, sensitivity >=.70 and PPV >=.50 at .30 in both diagnostics. These thresholds require later stakeholder acceptance and do not themselves prove useful workload.

- **Supportive P:** every gate passes and all stored-content simultaneous margin, threshold, default, and null requirements pass. Conclude only that stored routine report semantics made materially favorable action changes within fixed S and complete S exceeded B in this historical documentary-M2 frame under maximal stored content.
- **Supportive T, audit absent:** P passes and H is nonempty. Conclude only that specified CT/MRI pattern access guarantees would suffice under adversarial visibility and outcome assignment. Decision-time value remains inconclusive.
- **Conditional D:** the version/clock audit passes and its conservative vector lies in H under the joint error rule. Conclude conditional historical transport to that audited workflow, not deployment benefit or treatment utility.
- **Adverse P:** with all gates passed, the simultaneous upper limit for D is <=.01, C/default requirements fail with intervals wholly below margin, or the semantic-null gate fails. All stored content cannot rescue the tested strategy.
- **Adverse T:** P passes but H is empty. The tested “at least one visible within each pattern” guarantee is insufficient. A stronger dual-bundle guarantee is a new estimand, not permission to reinterpret this result.
- **Mixed:** D supports but C does not means semantic fields change actions within S but S does not beat optimized B; C supports but D does not means refitting/shared features, not runtime semantics, may explain value. Do not recommend S.
- **Inconclusive:** any source, adjudication, event, sparsity, shift, solver, bootstrap, calibration, or version-audit gate fails, or intervals cross a decision boundary. Positive AUC, point estimates, isolated pattern points, unrestricted text, complete-case outcomes, or eventual-text-as-visible analyses cannot rescue it.

No computation can establish Chinese semantic correctness, reviewer credentials, pathology linkage/sampling or biological M2, actual report visibility without logs, threshold/workload acceptability, clinician action, external validity, treatment effects, recurrence, survival, harms, costs, or patient benefit. These require expert adjudication, stakeholder review, source-system evidence, prospective validation, or another study.

## Exact read-only source bindings

All are ordinary CSVs, archive member none; same-encounter joins use `(patient master index,encounter number)` after exact-row deduplication and report multiplicity. Longitudinal history joins by `patient master index` plus valid clocks.

- `encounters`: `[internal dataset path]`; keys; `Age,Sex`; `Encounter Time,Admission Time,Discharge Time`.
- `procedures`: `[internal dataset path]`; keys; `Surgery, surgery source, start time, end time` for index, `t_dec`, ties, and prior treatment.
- `examinations`: `[internal dataset path]`; keys; `examination,examination findings,examination diagnosis,start time,machine model,examination number` for bundle/modality, acquisition lock, bodies, states, and provenance. It has no report/version clock.
- `pathology`: `[internal dataset path]`; keys; `Pathology,Examination findings,Examination diagnosis,Machine model` for HCC frame, Y/V, conflict/linkage review, and dedup audit. It has no time/specimen/slide/sampling fields.
- `medications`: `[internal dataset path]`; keys; `Medication, medication type, start time, end time` for prior systemic-treatment exclusion only.
- `orders`: `[internal dataset path]`; keys; `non-drug orders,order time,start time,end time,order status` for prior local/radiotherapy exclusion only.
- `diagnoses`: `[internal dataset path]`; keys; `Diagnosis Name,Diagnosis Type` for untimed HCC corroboration only, never prediction.
- `labs`: `[internal dataset path]`; keys; `Tests, Qualitative Result, Quantitative Result, Specimen Type, Test Time` for segregated diagnostics only; zero primary lineage.

Untimed diagnoses/documents, direct identifiers, post-cutoff content, nominal identifier-only vitals/transfers/front page, and all lab derivatives are excluded from predictors. MIMIC, eICU, and UKB remain directly accessible via configured read-only sources but do not identify this institutional documentary-M2 estimand and are not pooled.

## Compiler and verifier contract

The compiler must preserve the population, clocks/windows, calendar split, documentary Y/V whole denominator, bundle-first exclusive modality assignment, O/C/M/CM patterns, whole-bundle states, robust fit, zero lab lineage, fitted S/non-refitted S0, D/C/default contrasts, all-store P, exact sorted pattern frontier with fixed O contribution, simultaneous inference, external version-audit gate, and result zones. Changing a population, estimand, outcome, pattern unit, margin, or falsification rule requires a scientific child.

The verifier can check hashes/headers, attrition, joins, clocks, bundle aggregation, exclusive modality states, O contribution, masks/bit order, zero forbidden lineage, robust objective, S=S0 at semantic zero, Y/V enumeration, net-benefit arithmetic, sorted-versus-brute-force fixtures, monotonicity/Pareto antichain, bootstrap/null families, audit-presence/version fields, and conclusion linkage. Required fixtures include multirow and ambiguous bundles, blank IDs, empty text/O, dual four-state patients, V=0, refitted S0, row-wise masking, fabricated report time, eventual-equals-visible, equal-state fitting, complete-case Y, pointwise-as-simultaneous, cherry-picked pattern/threshold, favorable AUC with adverse net benefit, supportive P without audit, conditional D, CT-dependent/MRI-dependent mixed patterns, sparse strata, and numerically correct outputs paired with treatment/survival/biological-M2 claims.

Reference execution establishes arithmetic feasibility and whether submitted conclusions follow from outputs. It cannot establish clinical semantics, adjudicator qualifications, report-log truth/representativeness, pathology sampling, biological M2, acceptable workload, clinician behavior, treatment benefit, or patient outcomes.
