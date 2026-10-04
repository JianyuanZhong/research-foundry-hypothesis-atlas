> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Proposal: capture- and episode-history-standardized directional concordance after a first local TACE-like episode

## Episode, parent, and substantive repair

This is a substantive Episode-30 child of assessed-valid parent \`[prior hypothesis]\`. The parent’s endpoint repair is retained: a strict timed procedure episode corroborated by a same-encounter TACE-like non-drug order, with procedure-only and ambiguous records retained as competing recorded states. The parent’s all-index early-transition design, L=14/L=45 boundaries, observation-loss state, component-resolved AFP/albumin/total-bilirubin profile, patient-temporal split, uncertainty, and noncausal recorded-care boundary are also retained.

The next ambiguity is not solved by adding another generic capture covariate. Three facts need to be tested as part of the estimand and measurement logic:

1. The first local strict TACE-like episode makes prior *local strict TACE* history structurally empty by construction. A claim about prior TACE history would therefore be false. Only prior timed broad/ambiguous liver-directed episodes and the amount of observable local history can be used, with an explicit history-unobserved stratum.
2. The parent’s procedure-plus-order endpoint allows an order entered after the procedure to corroborate it. Such a record may be retrospective documentation or an automatically generated workflow artifact. Orders contain \`Order Entry Time\`, \`Start Time\`, \`End Time\`, and \`Order Status\`, so the direction of the order/procedure timestamps can be tested.
3. Pre-index capture adjustment and an absorbing observation-loss state do not by themselves show whether the profile contrast is stable under a common local-observation regime. The solver must estimate a distinct capture-standardized recorded-care contrast, while retaining the all-index contrast as the main population target.

The repair therefore changes both the estimand and the falsification hierarchy:

- retain the parent’s bidirectional same-encounter C2 as \`C2_bi\`;
- add a stricter directional tier \`C2_pre\`, requiring a valid TACE-like order entered before the procedure and an order start time within the parent’s concordance window;
- label orders entered only after the procedure as \`C2_post\` (retrospective-only concordance), not as positive evidence for \`C2_pre\`;
- estimate profile contrasts within explicit local-history strata and under a prespecified capture-standardized observation regime;
- require the directional tier, capture transport check, and history strata to agree before describing a robust recorded-care pathway association.

This is a measurement and transportability repair, not a causal treatment analysis. An order still does not prove intent, completion, technical success, or clinical response.

## Strongest supported claim, unresolved claim, and hypothesis

The strongest supported claim is operational only. The frozen HCC snapshot contains dated procedure, encounter, order, examination, and laboratory rows that can be joined by \`(patient master index, encounter number)\`. It contains no adjudicated treatment completion, radiologic response, mortality, outside-care record, or row-level time in clinical documents/pathology. The exploratory all-row audit found 338,040 procedure rows, 322,166 valid procedure start times, 16,730,319 order rows with valid order-entry dates, 419,996 examination rows (419,714 valid start times), 28,159,928 laboratory rows (28,158,196 valid times), and encounter dates from 2010-07-27 through 2026-01-01. These establish measurable local records, not their clinical meaning. A separate exploratory token screen found repeated strict-token procedure rows in many patients; because the exact parent vocabulary and episode aggregation are frozen only in the solver, these counts are audit evidence, not endpoint definitions.

The unresolved question is:

> After preserving all early recorded transitions and explicitly accounting for local observation opportunity and observable prior episode history, does a favorable early AFP/albumin/total-bilirubin profile predict a later procedure-plus-order record when the order is entered prospectively before the procedure, or is the apparent association confined to retrospectively entered orders, local-care intensity, or particular prior-history strata?

Primary noncausal hypothesis:

> In the all-index HCC population, a favorable profile (AFP decrease with non-worsening albumin and total bilirubin) will have a lower 320-day cumulative incidence of \`C2_pre\` than a discordant profile after standardization to the pooled distribution of observable prior episode history and local observation opportunity. The directional contrast will remain practically meaningful at both L=14 and L=45, while \`C2_post\` and unrelated recorded-care controls will be weaker.

Use the parent’s 3 percentage-point absolute contrast and test-set 95% interval excluding zero as a design margin, not as an expected result. The scientific deliverable is valuable if it falsifies the interpretation; no supportive result is presumed.

Clinical importance: if a profile association survives a prospective timing check, history stratification, and capture standardization, it is a more credible target for prospective reassessment studies. If it exists only in retrospective-order records or high-contact strata, the appropriate advance is to prevent researchers from treating a workflow/capture association as evidence of a disease-specific monitoring pathway. Neither result establishes what clinicians should do for an individual patient.

## Population, index, and temporal boundaries

Use one first-index episode per patient.

1. Aggregate procedure rows into 24-hour within-patient/within-encounter episodes using \`surgery start time\`; preserve all member rows, labels, source values, valid-time flags, and source-row identifiers. The candidate index is the earliest valid timed episode containing the training-frozen strict screen: literal \`TACE\`, \`arterial chemoembolization\`, or both \`hepatic artery\` and \`embolization\`. Hepatic angiography alone is not the index. Missing/invalid procedure times remain in an audit and cannot define t0.
2. Require age >=18 and nonmissing sex from the linked encounter, and a linked diagnosis with \`Diagnosis Name\` containing \`hepatocellular carcinoma\` on an encounter with \`Encounter Time\` in [t0-180 days, t0+7 days]. Diagnosis has no native timestamp; linked encounter time is an ascertainment proxy, not onset.
3. Require t0 <= 2025-01-01. Do not use the later source maximum as a clinical follow-up guarantee.
4. Retain every eligible first-index patient: early procedures, incomplete paired labs, no post-index record, and observation loss all remain in the all-index manifest. Early states are not excluded from the primary population.
5. Preserve the parent’s day-45 continuity cohort (no primary-ontology liver-directed therapeutic episode in (t0,t0+45]) only as a parent-comparison sensitivity. The primary analysis keeps early events as absorbing states.
6. Define L=14 and L=45 exactly as the parent: last eligible pre-index observation and first numeric value in days 7-14 or 7-45 for each of AFP `alpha-fetoprotein`, albumin `albumin`, and total bilirubin `total bilirubin`. Freeze assay-name rules, qualitative/inequality handling, profile thresholds, and common-support rules on training only. There is no laboratory unit column, so do not call the profile ALBI/MELD or pool undocumented units.

All predictors stop at L. The primary post-boundary window is (L, 365 days after t0], with cumulative-incidence reports at 30, 90, and 320 days after t0 where defined. The all-index multi-state analysis models first transitions from t0 through day 45, including therapeutic, diagnostic/technical, non-liver, and observation-loss states. \`C2_pre\` and \`C2_bi\` after L are not retrospectively used as predictors.

## Explicit local episode history and capture regime

### Observable prior episode history

Because t0 is the first *local strict* TACE-like episode, prior local strict TACE history is not an estimable modifier. Do not report “no previous TACE” as a clinical fact. Define a training-frozen broad/ambiguous liver-directed procedure vocabulary, excluding the strict index vocabulary, and aggregate its timed rows into the same 24-hour patient/encounter episodes.

For the 365 days before t0, define:

- H0: at least one encounter with valid \`encounter time\` in [t0-365,t0), no timed broad/ambiguous liver-directed episode;
- H1: at least one such encounter and at least one timed broad/ambiguous liver-directed episode;
- HU: no valid local encounter in the lookback, or insufficient valid procedure time to classify the lookback.

H1 is prior *locally recorded broad/ambiguous liver-directed care*, not prior treatment completion. HU explicitly represents a history that is unobservable locally; it must not be merged into H0. Also report the exact count, days-since-last episode, number of prior procedure rows, and lookback coverage days. Generic pre-index procedure, encounter, order, examination, medication, and laboratory burden remain covariates, but H0/H1/HU is a prespecified effect-modifier/transportability output, not just another feature.

### Local observation opportunity

Define a non-endpoint local contact as a valid timestamp in any of:

- \`encounters.Encounter time\`;
- \`labs.test time\` for any laboratory row;
- \`examinations.Start Time\` for any examination row;
- \`medications.start time\`;
- \`orders.Order Time\` or \`orders.Start Time\` for an order whose name does not pass any C2/order endpoint vocabulary.

Do not count procedures, strict TACE-like orders, C2-contributing orders, or the outcome itself as a contact for its own observation weight. This avoids making the endpoint observable by definition. For every patient, report pre-index contact count, distinct contact days, time since last contact, modality-specific availability, and whether any contact is present in the prior 365 days.

For the dynamic capture sensitivity, a patient is locally observable at post-L day d if a non-endpoint contact occurred in (d-90,d]. If no such contact occurs, censor the observation-weighted analysis at d; do not call this death, discharge, or clinical absence. The all-index analysis instead records first local observation loss as an absorbing recorded state using this exact 90-day rule and keeps that state in the CIF vector.

The new capture-standardized estimand is a predictive standardization, not a counterfactual intervention:

\`Delta_cap,k^L(h) = sum_gq w*_gq [CIF_k(h | favorable, g, q, common-contact regime) - CIF_k(h | discordant, g, q, common-contact regime)]\`.

Here g is H0/H1/HU, q is a prespecified training-derived capture stratum (low/middle/high pre-index contact opportunity, with a separate HU/insufficient-history label), and w* is the pooled eligible-test distribution after positivity trimming. The common-contact regime is implemented by stabilized inverse probabilities of remaining locally observable at each post-L interval, estimated without endpoint-contributing records. This is a sensitivity estimand about recorded-care ascertainment under a common observed-contact distribution; it is not the risk under treatment or a claim about unobserved outside care.

The retained all-index estimand is:

\`Delta_full,k^L(h) = P(first recorded state k by h | favorable, L, history/capture) - P(first recorded state k by h | discordant, L, history/capture)\`

with the same pre-index standardization as the parent and explicit early/observation-loss states. Report \`Delta_full,C2_pre\`, \`Delta_full,C2_bi\`, \`Delta_full,C2_post\`, C1, C0, diagnostic/technical, non-liver, and observation loss. Report \`Delta_cap\` only if overlap and weight diagnostics pass. H-stratum contrasts \`Delta_{k,g}^L\` and the profile-by-H interaction are mandatory; a marginal result cannot be called stable if it reverses across H0/H1/HU.

## Outcome measurement ontology

Construct mutually exclusive first post-boundary states, with the parent’s hierarchy retained.

- C2_bi: strict timed procedure episode plus a TACE-like non-drug order linked by patient and encounter keys, with the order’s \`Order time\` or \`Start time\` in [-24,+24] hours of the earliest procedure time. This is the parent-compatible bidirectional concordance tier.
- C2_pre (new primary measurement tier): C2_bi with valid `orders.Order Time` in [-24,0] hours relative to the earliest procedure time, and, when `Start Time` is present, `Start Time` in [-24,+24] hours. If `Order Time` or the required time is invalid, it cannot be C2_pre. This says only that a relevant order was entered before the recorded procedure; it does not establish intent or completion.
- C2_post (new falsification comparator): a strict procedure with a same-encounter TACE-like order satisfying C2_bi but whose valid \`Order Time\` is >0 and <=24 hours after the procedure, with no qualifying pre-procedure order. C2_post is retrospective-only concordance. If both pre and post orders exist, classify as C2_pre and retain both timestamps in the audit.
- C1: strict procedure-only episode not meeting C2_bi.
- C0: timed broad/ambiguous/mixed liver-directed episode that is not C1/C2.
- diagnostic/technical-only, non-liver, and administrative observation-loss states remain competing states.

All order matches are same patient/same encounter in the primary definition. Cross-encounter matches and ±6/±24/±72-hour windows are sensitivities. Preserve \`order status\` exactly; report exact-status and canceled/terminal-status sensitivities without inventing a universal status dictionary. Never use an order supplying a C2 endpoint as a predictor or plan covariate for that endpoint. A secondary examination-workflow tier may use \`examinations.examination\` and \`start time\` in the preceding 30 days; \`examination findings\` and \`examination diagnosis\` are narrative sensitivity evidence only, not imaging adjudication.

## Exact HCC data bindings and availability

Frozen snapshot: \`[source checksum]\`. Every HCC source is an ordinary file (no archive member); sources are read-only. Aggregate each child table before joining to \`encounters\` on exactly (\`patient master index\`, \`visit number\`) to prevent many-to-many expansion.

- \`encounters\`, schema \`datasets/hcc/table-b743286cb1249287.json\`, source \`[internal dataset path]\`: required \`patient master index\`, \`visit number\`, \`age\`, \`sex\`, \`visit time\`, \`admission time\`, \`discharge time\`, \`visit department\`. \`visit time\` anchors eligibility, history visibility, local contact, and index linkage; admission/discharge/department are recorded covariates only.
- \`procedures\`, schema \`datasets/hcc/table-d5eae16f8f8093d9.json\`, source \`[internal dataset path]`: required \`Patient Master Index\`, \`Encounter Number\`, \`Surgery\`, \`Start Time\`, \`End Time\`, \`Surgery Source\`. \`Start Time\` anchors episodes and all outcome timing; \`End Time\` and \`Surgery Source\` are sensitivities/audit fields.
- \`diagnoses\`, schema \`datasets/hcc/table-12710723c3df0c99.json\`, source \`[internal dataset path]`: required \`Patient Master Index\`, \`Encounter Number\`, \`Diagnosis Name\`, \`Diagnosis Type\`; no native time, so linked encounter time is only ascertainment.
- \`labs\`, schema \`datasets/hcc/table-38aad8c54471332f.json\`, source \`[internal dataset path]`: required \`Patient Master Index\`, \`Encounter Number\`, \`Test\`, \`Qualitative Result\`, \`Quantitative Result\`, \`Specimen Type\`, \`Test Time\`. Use exact training-frozen assay names \`Alpha-fetoprotein\`, \`Albumin\`, \`Total Bilirubin\`; retain numeric/qualitative/inequality/specimen/time/count/missingness.
- \`orders\`, schema \`datasets/hcc/table-6b93dcf0ea823702.json\`, source \`[internal dataset path]`: required \`Patient Master Index\`, \`Visit Number\`, \`Non-drug Medical Order\`, \`Order Time\`, \`Start Time\`, \`End Time\`, \`Order Duration\`, \`Order Status\`, \`Frequency\`. \`Order Time\` supplies the new direction check; \`Start Time\` supplies concordance; \`End Time\`, duration, frequency, and status are measurement sensitivities.
- \`examinations\`, schema \`datasets/hcc/table-fd016d2731b9d6c6.json\`, source \`[internal dataset path]`: required \`patient master index\`, \`encounter number\`, \`examination\`, \`examination findings\`, \`examination diagnosis\`, \`start time\`, \`machine model\`, \`examination number\`. Primary workflow contact uses \`examination\`/\`start time\`; narrative fields are sensitivity-only.
- \`medications\`, schema \`datasets/hcc/table-4f6ecaeb6e8f69c2.json\`, source \`[internal dataset path]`: required \`Patient Master Index\`, \`Encounter Number\`, \`Medication\`, \`Single Dose\`, \`Single Dose Unit\`, \`Frequency\`, \`Start Time\`, \`End Time\`, \`Administration Route\`, \`Drug Type\`. \`Start Time\` is an optional capture contact; medication is never used to infer TACE intent/completion.
- \`clinical_documents\`, schema \`datasets/hcc/table-66afca58512c2fca.json\`, source \`[internal dataset path]\`: identifier keys and \`medical history\`, \`clinical course\`, \`surgery name\`, \`operative course\` among narrative fields, but no usable row-level time. Use only descriptive coding/history sensitivity; it cannot define H0/H1, C2, or timed outcomes.
- \`pathology\`, schema \`datasets/hcc/table-0a4ee86a446c605c.json\`, source \`[internal dataset path]`: identifier keys plus \`Pathology\`, \`Examination findings\`, \`Examination diagnosis\`, \`Machine model\`; no time. Descriptive only, not an outcome or prior-history timestamp.
- \`vitals\`, schema \`datasets/hcc/table-8436de9cba74b8ca.json\`, source \`[internal dataset path]`, and \`transfers\`, schema \`datasets/hcc/table-320c20f732e71789.json\`, source \`[internal dataset path]`: identifier-only with no usable payload or time; do not represent them as contact measurements.
- \`front_page\`, schema \`datasets/hcc/table-38b3224239acc33f.json\`, source \`[internal dataset path]`: identifier-only and 30 bytes in the catalog; no usable payload.

The complete catalog is \`[internal dataset path]`; the HCC guide is \`datasets/hcc/README.md\`. All HCC members are ordinary files. The catalog’s reserved participant buckets are inaccessible and are not external validation.

## Analysis and split

Use 2010-2022 for fitting, 2023 for tuning, and 2024-2025-01-01 for locked testing where support permits; otherwise declare the deterministic participant-hash split before fitting. No participant crosses splits. Fit strict/broad vocabularies, assay rules, thresholds, H strata, capture cut points, weights, overlap trimming, and status mappings on training only.

### Simple baseline B_cap-history

Fit regularized discrete-time cause-specific hazards for mutually exclusive first states, with an Aalen-Johansen/CIF reconstruction. Use the same all-index patients, L boundary, outcome tiers, splits, standardization, capture rule, and patient-level bootstrap for every model.

B0 contains age, sex, index encounter time/department, diagnosis ascertainment, and prior local procedure/encounter history. B1 adds explicit H0/H1/HU and exact lookback coverage. B2 adds pre-index modality-specific capture opportunity and dynamic observation-loss weights. B3 adds the L-specific component profile, delays, counts, qualitative/inequality indicators, and missingness. The required scientific contrasts are B2 versus B3, and the profile contrast within H strata under B3. Fit separate endpoint parameterizations for C2_pre, C2_bi, C2_post, C1, C0, and controls; do not pool endpoint-contributing orders into capture features.

Report coefficients, cause-specific hazards, CIFs, standardized absolute risk differences and stable risk ratios, Brier score, dynamic log score, calibration, overlap, effective sample size, weight distribution, and patient-clustered bootstrap or an equivalent patient-level resampling interval.

### Substantive alternative M_joint-history-capture

Fit an irregular-time hidden semi-Markov multi-source model to the same split. A latent recorded-care episode state has source-specific emissions for strict/broad procedure rows, order direction (pre/post), examination workflow, and observation-contact intensity; transition hazards depend on the same L-specific profile and H0/H1/HU history. The model must explicitly allow source-specific false-positive/sensitivity parameters and missingness/capture kernels, with weakly informative priors or penalization. Fit to the observed source streams, not a fabricated clinical gold standard.

The alternative reveals graded source disagreement, order-direction dependence, repeated episode structure, and uncertainty in the latent recorded-care state that B3 loses when it deterministically tiers each episode. It is scientifically useful only if it converges, passes posterior/predictive checks, improves held-out source log score/Brier/calibration over B3, and yields profile contrasts stable under prior sensitivity. A latent state is still not clinical response, and a better held-out source score does not prove treatment completion.

Both models must produce locked test predictions for every endpoint tier, H stratum, capture regime, and L; source-level concordance audits; CIF contrasts; calibration/log-score metrics; weight/overlap diagnostics; bootstrap intervals; and an interpretation file linking every statement to a computed output.

CPU is the default. The discovery metadata scan over the five dated streams used 2 CPUs and 8,192 MiB and completed in 104.0 seconds; this is measured preprocessing evidence, not a full-model runtime. No solver model was fitted in discovery. The future solver planning envelope is at most 16 CPUs, 262,144 MiB, and 28,800 seconds; baseline and latent-fit runtimes remain unverified. GPU is not required. If a solver requests an A100 for a matrix-intensive latent fit, it must use the allocated \`cuda:0\`, report that allocation, and preserve a CPU fallback/deferral; GPU use has no scientific merit bonus.

## Falsification and interpretation

Required checks:

1. **All-index and parent continuity:** reproduce the parent’s early-transition vector and day-45 procedure-only continuity contrast. Any discrepancy is a construction failure, not evidence for C2_pre.
2. **Directional measurement check:** compare C2_pre, C2_bi, and C2_post. A contrast present only in C2_post is adverse to interpreting concordance as prospectively corroborated recorded care. C2_pre sparsity or missing \`Order Time\` is inconclusive, not a null.
3. **Capture specificity:** compare full-index and \`Delta_cap\`; compare B2 capture-only with B3 profile-plus-capture. A large attenuation after capture standardization, or similar profile contrasts for local-contact/observation-loss outcomes, supports a workflow/capture explanation.
4. **History transport:** report \`Delta_{k,H0}\`, \`Delta_{k,H1}\`, and \`Delta_{k,HU}\`, interaction and overlap. Strong marginal association driven by HU or one narrow H stratum is not stable transport across local episode histories.
5. **Source and time sensitivity:** same-encounter versus cross-encounter; ±6/24/72-hour windows; exact order-status and terminal/canceled sensitivities; order-entry lag bins; and a permutation of order times within patient preserving names, encounters, and source counts. A similar signal after permutation is adverse.
6. **Negative recorded endpoints:** apply the same profile/capture procedure to diagnostic/technical and non-liver states. Similar contrasts weaken disease-specific pathway interpretation.
7. **Profile-time placebo:** permute eligible assay timestamps within patient or use pre-index placebo windows, preserving assay/specimen and measurement counts. Preserved effects favor temporal/capture artifact.
8. **Selection and observation:** retain all early states through day 45; compare L=14/L=45, weighted/unweighted capture analyses, complete paired values, and qualitative/inequality-as-missing versions. Never report a day-45-only result as the all-index result.
9. **Latent-model integrity:** require convergence, posterior predictive checks, held-out source metrics, and prior-sensitivity intervals. Nonconvergence, prior domination, or no improvement is inconclusive and cannot be repaired by preferring the latent model.

Supportive evidence requires: parent continuity; sufficient C2_pre cells and valid \`order time\`; directionally compatible C2_pre contrasts at L=14 and L=45; practical contrast meeting the 3-point design margin with an interval excluding zero; persistence after capture standardization and across H0/H1 (with HU reported); weaker C2_post, negative-endpoint, and permutation contrasts; overlap/calibration; and a converged M_joint-history-capture with prior-stable contrasts. This supports only a robust association with a prospective-direction, locally recorded evidence tier and motivates external adjudication.

Adverse evidence includes: C2_pre null/reversal with C2_post or C1 persisting; attenuation under capture weighting; concentration in HU/high-contact or one history stratum; similar non-liver/observation-loss/placebo contrasts; order-window/status instability; poor overlap/calibration; or latent-model source/capture instability. These favor documentation, local workflow, history selection, or measurement explanations.

Inconclusive evidence includes: sparse or absent C2_pre, invalid order-entry dates, no common support, extreme weights, insufficient follow-up, temporal split failure, lexical instability, model nonconvergence/prior domination, or intervals crossing the design margin. It does not establish absence of response, progression, benefit, or clinical utility.

The verifier can check source paths, schema IDs, ordinary-file declarations, headers, two-key aggregation, episode construction, time direction, leakage exclusion, H strata, capture weights, splits, CIFs, predictions, calibration, permutations, and conclusion-to-output links. It cannot adjudicate order intent, treatment completion, technical success, radiologic/pathologic response, recurrence/progression, liver failure, death, survival, benefit, appropriateness, utility, outside care, or external validity. Those require expert chart/radiology/pathology review, units and validated assays where needed, linked mortality/outside-care data, and prospective or external validation.

## Required solver artifacts

- \`index_episode_manifest.csv\`
- \`trajectory_manifest_L14_L45.csv\`
- \`early_transition_manifest.csv\`
- \`outcome_evidence_manifest.csv\`
- \`source_concordance_audit.csv\` (including order-entry direction and lag)
- \`episode_history_capture_manifest.csv\`
- \`observation_process.json\`
- \`transition_cif.json\`
- \`history_capture_contrasts.json\`
- \`predictions.parquet\`
- \`metrics.json\`
- \`calibration.json\`
- \`bootstrap_intervals.json\`
- \`overlap_and_weights.json\`
- \`multisource_parameters.json\`
- \`mstate_checkpoints_or_deferral.json\`
- \`negative_control_and_permutation.json\`
- \`interpretation.json\`
- \`limitations.csv\`

\`interpretation.json\` must map every conclusion to estimate, interval, model, L boundary, endpoint tier/state, H stratum/capture regime, split, and frozen criterion, and prohibit wording implying intent, completion, response, progression, causality, mortality, survival, benefit, utility, or external validity.

## Alternatives not selected and revisit triggers

A transformer over clinical text is deferred because \`clinical_documents\` has no row-level time and no validated outcome labels. ALBI/MELD is deferred because lab units and INR are unavailable. Images/multimodal learning is deferred because HCC image files are absent. Causal treatment-policy and survival analyses are deferred because intent, assignment, completion, mortality, and outside-care ascertainment are unavailable. A generic neural model is deferred because it would add complexity without testing order-direction, capture, or episode-history uncertainty. These branches should be revisited only with validated timestamps/labels, lab units and INR, images, or adjudicated outcomes.

The parent should otherwise stand: the child does not replace the parent’s C2_bi and all-index estimand; it makes the next falsifiable measurement distinction—prospective versus retrospective order corroboration—and formally elevates history/capture transport from covariate adjustment to an explicit estimand and interpretation gate.
