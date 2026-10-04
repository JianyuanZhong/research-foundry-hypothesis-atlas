> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 24 process-conditioned assay-content child

Status: design only. No cohort count, fitted result, event rate, parameter, effect estimate, or clinical conclusion is claimed.

Parent: `[prior hypothesis]`. This child preserves the parent's HCC first dated literal-code TACE population, [t0+43,t0+181) first-event estimand, O0/O1/O2/O3/O4 endpoint hierarchy, capture-adequate `O_planproxy_cap` and `unknown_provenance` rules, R42/R28 arms, patient-held-out temporal split, elastic-net baseline, compact GRU alternative, uncertainty, falsification, O4/provenance controls, and unavailable-clinical-evidence limits. The substantive repair is a process-conditioned assay-content contrast.

## Scientific opening and clinical importance

The strongest claim supported by the inherited evidence is narrow: in a selected HCC record cohort with a first dated TACE code and day-42 observation, a pre-index-to-day-42 assay trajectory may predict a later operational TACE record better than a day-42 snapshot. Longitudinal record prediction can contain useful temporal structure but also learned data-collection bias [K1]; explicit longitudinal selection modeling can adjust observation/analysis processes without adjudicating codes [K2]; and recorded time, biological time, decision time, missingness, and care process must be separated [K3]. The local endpoint repair further requires administratively valid procedure closure plus same-visit downstream activity and never treats unsupported post-source absence as planned care.

The unresolved interpretation boundary is more specific: does assay-result content add information after conditioning on the opportunity and documentation process that produced the assay rows, or does a numeric trajectory merely mark who was repeatedly seen, tested, ordered, examined, medicated, and documented? Stable severity/person profile is a second rival. The question matters because a residual content signal would justify a blinded assay/intent/imaging validation study, whereas an opportunity-only signal would redirect effort toward capture and workflow adjudication. This is a descriptive/predictive record question, not a causal or mechanistic claim.

## Hypothesis and estimands

Primary hypothesis:

> Among the inherited eligible patients, the day-42 assay-result content increment over a pre-specified stable-profile plus observation/workflow model remains positive for the later closed-coherent O4 record, and is larger than the corresponding increment for a capture-adequate pre-opened-order/no-strict-coherence process pattern.

Define all feature blocks before test scoring:

- (W_0): baseline demographic/encounter and pre-index stable profile, without any post-index assay result;
- (W_{
m opp}): (W_0) plus assay opportunity and care/documentation process features available by t0+42, but with all lab result fields masked;
- (W_{
m content}): (W_{
m opp}) plus assay-result content and within-person change features through t0+42;
- (W_{
m snap}): inherited day-42 snapshot block plus (W_{
m opp});
- (W_{
m traj}): inherited pre-index-to-day-42 trajectory block plus (W_{
m opp}).

For each method, endpoint, and weighting arm, report patient-level held-out loss contrasts:

- (D_{
m opp}=L(W_0)-L(W_{
m opp})), the opportunity/workflow increment;
- (D_{
m content|opp}=L(W_{
m opp})-L(W_{
m content})), the assay-result-content increment conditional on process;
- (D_{
m traj|opp}=L(W_{
m snap})-L(W_{
m traj})), the inherited trajectory-vs-snapshot contrast after process conditioning.

Positive values mean lower loss for the second model. The new claim requires (D_{
m content|opp}), not merely (D_{
m opp}), and requires the same pattern for O4 and not for `O_planproxy_cap`. The process block is a comparator, not a sufficient-statistic claim: residual confounding, care-intensity selection, and measurement error remain possible. Cross-fitting/residualization does not establish causality.

As a timing-safe secondary diagnostic, within each development fold fit the process-only discrete-time hazard (q_{W_{
m opp}}) using only rows through t0+42, form cross-fitted risk residuals on development patients, and evaluate the pre-specified content score against those residuals without fitting on the held-out test set. This is reported only as a concordant decomposition check; the primary estimand remains paired held-out loss. No post-tp feature, later procedure row, O4 flag, closure field, or downstream provenance row enters a predictor.

## Population, time, joins, and endpoint hierarchy

Use the first row in `procedures` with Unicode-normalized, trimmed, case-folded `Surgery == TACE`, nonmissing `Patient master index`, `Encounter number`, and parseable `Start time`; call its start t0. Keep the inherited deterministic duplicate/alias audit, malformed-date exclusions, early-repeat exclusions, and all-source observation requirement through t0+42 for R42. Preserve the R28 pre-day-42 arm. Group only by `Patient master index`; visit joins are exactly (`Patient master index`, `Encounter number`). Never join on names, ID cards, phones, insurance cards, file order, or an incompatible namespace.

The later first-event window is [t0+43,t0+181), with the inherited 14-day grid [43,57), [57,71), ..., [169,181). O0 is the first later unique literal TACE. O1 adds the frozen semantic hepatic-arterial procedure rule and valid same-patient/same-visit timed examination or order corroboration. O2 adds same-visit medication corroboration. O3 adds qualifying examination/order/medication activity on the exact visit key at u in (tp,tp+72h], with nonblank/non-cancelled order status. O4 is O3 plus the same procedure row's parseable te=`end time` satisfying 0 <= te-tp <= 72h. Missing, negative, or over-72h closure is closure_unknown, not a negative event. O3 remains visible to quantify O3/O4 discordance.

Preserve the inherited process-control rules: `post-window capture-adequate` is evidenced only by a valid encounter discharge at least tp+72h or a timed non-procedure row in examinations/orders/medications/labs during (tp,tp+72h]; `O_planproxy_cap` requires a same-visit order opened in [tp-7d,tp), capture adequacy, no O4, and no qualifying O3 post-activity; otherwise unsupported absence is `unknown_provenance`. Overlap with O4 is retained and excluded from the process-control class. These are record classes, never intent, completion, response, or benefit labels.

## Exact source bindings

Use HCC snapshot `[source checksum]`; all members are ordinary files and no archive member is required. The parent’s full 12-file binding-template remains unchanged. The new contrast uses these exact read-only members:

| table | source path and SHA-256 | required fields and use |
|---|---|---|
| procedures | `[internal dataset path]`; `[source checksum]` | `Patient Master Index`, `Encounter Number`, `Surgery`, `Start Time`, `End Time`, `Surgery Source`; t0, O0-O4, tp/te and endpoint audit |
| encounters | `[internal dataset path]`; `[source checksum]` | `Patient Master Index`, `Encounter Number`, `Encounter Time`, `Admission Time`, `Discharge Time`, `Encounter Department`; W0/Wopp encounter timing, observation, discharge capture |
| labs | `[internal dataset path]`; `[source checksum]` | `patient master index`, `encounter number`, `test`, `qualitative result`, `quantitative result`, `specimen type`, `test time`; result content and opportunity; Wopp may use only `test`, `specimen type`, time and counts |
| orders | `[internal dataset path]`; `[source checksum]` | `Patient master index`, `Encounter number`, `Non-medication order`, `Order time`, `Start time`, `End time`, `Order status`, `Frequency`; process/opportunity and O1/O3 audit |
| examinations | `[internal dataset path]`; `[source checksum]` | `Patient master index`, `Encounter number`, `Examination`, `Examination findings`, `Examination diagnosis`, `Start time`, `Examination number`; process timing/O1/O3 audit; findings/diagnosis are not response labels |
| medications | `[internal dataset path]`; `[source checksum]` | `patient master index`, `encounter number`, `medication`, `single-dose medication amount`, `single-dose medication amount unit`, `frequency`, `start time`, `end time`, `medication method`, `drug type`; process timing/O2/O3; no indication inferred |

For Wopp, mask `qualitative results` and `quantitative results` entirely, including missingness indicators derived from those fields. It may retain lab test name, sample type, valid timestamp, counts, inter-test intervals, and assay-opportunity indicators. It may retain non-result encounter/order/examination/medication names only as pre-specified token/count or timing features; no text-derived clinical response or outcome label is created. For Wcontent, fit assay-specific robust scaling/token dictionaries and imputation within development folds only; numeric units are unavailable, so do not pool unlike assays or interpret values clinically.

The other exact inherited source members remain bound but coverage-only unless used by the parent audit: vitals `[internal dataset path]` SHA `[source checksum]`; transfers `[internal dataset path]` SHA `[source checksum]`; clinical_documents `[internal dataset path]` SHA `[source checksum]`; front_page `[internal dataset path]` SHA `[source checksum]`; pathology `[internal dataset path]` SHA `[source checksum]`; diagnoses `[internal dataset path]` SHA `[source checksum]`. No archive member or alternate patient namespace is introduced.

## Baseline and substantive alternative

The transparent baseline is a pooled-logistic discrete-time hazard with intercept/risk-bin indicators and W0/Wopp blocks, fit separately for O0, O1, O2, O3, O4, and O_planproxy_cap. It uses alpha 0.5 elastic net; lambda, parsing, assay tokenization, scaling, imputation, and R42 selection weights are fit only in grouped development folds. It makes the new decomposition auditable and exposes which process block carries signal.

The learned alternative is the inherited compact two-stream GRU: eight assay labels with numeric/qualitative/inequality content, sample type, relative time, inter-event time, and opportunity tag from t0-365 through t0+42, with M0/workflow covariates at the hazard head; one layer, hidden 32, dropout .10, head 32/16, Adam 1e-3, weight decay 1e-4, max 50 epochs, eight-epoch early stopping, seeds 17/29/41. Train matched W0, Wopp, Wcontent, Wsnap, and Wtraj variants with identical targets, masks, R42/R28 weights, splits, and reporting. The GRU is scientifically useful because nonlinear combinations and irregular ordering could reveal content patterns lost by summaries; it is not a complexity bonus. If only the process block helps, the learned model does not rescue the assay interpretation.

Defer transformers, narrative NLP, mechanistic response models, and causal intent models: the available HCC source lacks validated intent/response labels, images, image reports, assay units/reference ranges, outside-care capture, and expert adjudication. Revisit them only if O4 support and process-conditioned content support survive.

## Split, uncertainty, and falsification

Sort by t0; earliest 80% of patients are development and latest 20% are untouched test, with no patient in both. Use five grouped development folds for all preprocessing, nuisance fitting, imputation, hyperparameters, early stopping, and seed choice. Process residuals are cross-fitted; test outcomes never tune the decomposition.

Report patient-level paired log loss, Brier, integrated Brier, calibration, risk-bin counts, paired availability, and secondary discrimination. Use 1,000 patient-level paired bootstrap resamples of the untouched test set with one max-|t| simultaneous 95% family over O0-O4/O_planproxy_cap, all W0/Wopp/Wcontent contrasts, snapshot/trajectory contrasts, ordinary/R42/R28, and fixed falsifiers. Report ESS/weight tails, O3/O4 overlap, closure-invalid and capture-unknown reasons, and process feature availability by split/time bin.

Freeze these falsifiers: (1) retain assay timestamps/opportunity but remove result content; (2) permute result content within patient while preserving assay names, timestamps, missingness, and opportunity; (3) retain result content but permute timestamps/opportunity within patient; (4) restrict assay content to t0-35 and compare with t0-42; (5) compare R28/R42; (6) compare O3/O4 and O4/`O_planproxy_cap`; (7) report content increments in a workflow-only/time-only model. The within-patient content permutation is a negative control for numeric content, not proof of exchangeability.

Decision rule:

- **Supportive:** in both elastic-net and GRU, ordinary and R42-weighted analyses, O4 has a positive simultaneous lower 95% bound for (D_{
m content|opp}), the direction persists in R28/late-row controls, and (D_{
m planproxy|opp}) has an upper simultaneous bound <= 0. The content increment must exceed the pre-specified process-only increment in the paired decomposition, with adequate O4 support, capture audit, ESS, and test availability. This supports residual record information beyond measured opportunity/workflow, not biology or causality.
- **Adverse:** (D_{
m content|opp}) is null/negative while (D_{
m opp}) is positive; the content increment disappears at O4, is reproduced by timestamp/opportunity permutation or within-patient content permutation, appears for `O_planproxy_cap`, or survives only one method/weighting arm. This redirects the study to workflow/capture or endpoint adjudication.
- **Inconclusive:** O4 or process-control support, ESS, paired availability, closure validity, or capture adequacy is insufficient; simultaneous intervals are wide; nuisance fits fail; or elastic-net and GRU disagree. Do not alter feature masks, window rules, process tokens, endpoints, or seeds after test scoring.

A supportive result establishes only an incremental association with a narrower operational record after measured process conditioning. It cannot establish assay biology, severity-independent prognosis, TACE intent/completion, radiographic response, recurrence, survival, treatment benefit, mechanism, or transport. A clinically consequential conclusion requires expert adjudication of intent/procedure completion and imaging response, units/reference ranges and assay validation, outside-care capture, and patient-important outcomes.

## Deliverables and completion gates

The future solver must newly produce:

- `endpoint_provenance_audit.csv`, `capture_adequacy_audit.csv`, and `endpoint_class_counts.csv` with O0-O4, O_planproxy_cap, unknown reasons, closure and capture fields;
- `process_feature_audit.csv` documenting each W0/Wopp/Wcontent field, time bound, result masking, availability, and fold;
- `heldout_predictions_losses.csv` for every method/block/endpoint/weighting, with patient-level losses;
- `process_conditioned_contrasts.csv`, `content_opportunity_falsification.csv`, `trajectory_gru_sensitivity.csv`, `trajectory_support_freeze.json`, `trajectory_decision_gate.json`, and `claim_output_map.md`.

Completion requires deterministic endpoint/provenance and process-feature audits; matched held-out elastic-net and GRU predictions; cross-fitted nuisance/residual diagnostics; simultaneous uncertainty; fixed falsifications; R42/R28 and ESS gates; and an output-linked supportive/adverse/inconclusive decision. This proposal has no fitted result.

Estimated future workload: materialization/audits and elastic-net approximately 4 CPUs/16 GiB for 1-3 hours; 1,000-bootstrap and permutation outputs approximately 4 CPUs/16 GiB for 1-3 additional hours; compact GRU three seeds approximately 4 CPUs/16 GiB and one allocated A100 for 2-5 hours. These are unmeasured planning estimates, separate from discovery. If GPU is used, request one GPU and explicitly use `cuda:0`; ordinary shell CUDA visibility is not a feasibility test. The solver envelope remains 16 CPUs, 262,144 MiB, up to eight GPUs, and 28,800 seconds.

## What changed, alternatives, and revisit rule

Changed from the parent: a cross-fitted, values-blinded Wopp comparator is now a primary estimand rather than a descriptive covariate audit. It uses exact assay-name/timestamp opportunity and non-lab care-routing fields, masks both numeric and qualitative lab result content, and tests whether adding result content improves O4 but not the capture-adequate process-control class. A timing-safe cross-fitted nuisance residual is a secondary check. This directly distinguishes residual content information from measured workflow opportunity while preserving O4, R42/R28, patient-held-out evaluation, uncertainty, and falsification.

The stable-profile decomposition of [prior hypothesis] remains a supported alternative, not ancestry: it is useful for persistent severity/person heterogeneity but does not on its own make assay opportunity values-blind. The inherited elastic-net is retained for transparent decomposition; the GRU is retained because irregular nonlinear assay combinations could carry information summaries lose. Deferred models are not rejected by complexity or GPU policy; they lack validated local targets/modalities. Revisit a richer model only if the process-conditioned O4 content contrast is supportive and the missing clinical dependencies are supplied. If process-only and content increments are indistinguishable, abandon assay interpretation and seek intent/imaging/response adjudication or better longitudinal capture rather than adding complexity.

## Compact bibliography

Exactly three distinct inspected works are attached as UTF-8 excerpts with the unchanged frozen receipts in `key-references.json`.

[K1] Shmatko A, Jung AW, Gaurav K, Brunak S, Mortensen LH, Birney E, Fitzgerald T, Gerstung M. Learning the natural history of human disease with generative transformers. Nature. 2025. DOI: 10.1038/s41586-025-09529-3.

[K2] Urbut SM, Ding Y, Nakao T, Koyama S, Misra A, Jiang X, Harish A, Gaffney L, Hornsby WE, Smoller JW, Gusev A, Natarajan P, Parmigiani G. A Bayesian framework for longitudinal EHR and genetic discovery. Nature. 2026. DOI: 10.1038/s41586-026-10780-5.

[K3] Liu Y, Liu Y, Zhao Y, Luo Y, Hao X. From static snapshots to longitudinal trajectories: artificial intelligence in women's reproductive and ovarian health. Frontiers in Endocrinology. 2026. DOI: 10.3389/fendo.2026.1893963.
