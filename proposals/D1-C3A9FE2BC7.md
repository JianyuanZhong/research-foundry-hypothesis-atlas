> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Concordant recorded-care pathways after a first observed HCC-coded admission

## Decision, hypothesis and substantive advance

This is a targeted child of `[prior hypothesis]`. The incumbent asks whether a strictly pre-admission local-care and assay trajectory adds calibrated information about a recorded procedure transition. Its remaining scientific limitation is endpoint meaning: a procedure row is not demonstrably a treatment, and a broad procedure vocabulary can be clinically heterogeneous. The repair makes the primary semantic question a time-linked documentation concordance question while retaining the incumbent's all-admission, semantics-independent procedure endpoint as a prespecified sensitivity.

The future solver must newly fit and lock an admission-anchored sequential competing-state analysis and produce predictions for every eligible admission. The actual scientific deliverable is a calibrated estimate of the complete terminal documentation-state vector, a paired comparison of transparent history summaries with an irregular learned history model, and a prospective dictionary/pairing audit that determines whether the concordance endpoint is interpretable.

The falsifiable hypothesis is:

> Among all eligible adults at their first observed HCC-coded inpatient admission, does documented pre-admission local-care and assay history add calibrated held-out information beyond admission context plus the first 12 hours of current-admission assay history for distinguishing a concordant pathway-family order followed by a same-family procedure from procedure-only, order-only, other procedure, discharge, unresolved timing and no transition during hours 24–72?

The clinical decision relevance is deliberately bounded. If concordance is frequent, temporally stable and predictable, it may identify admissions whose record streams support coordinated pathway review; if discordance is common, it identifies a documentation/coordination gap that warrants chart review before any automated decision support. This does not select embolization, resection or ablation, and no result can be called treatment intent, receipt, completion, appropriateness, benefit or clinical utility.

The strongest available evidence supports only that this HCC snapshot contains encounter/discharge times, native assay times, procedure rows with names and native start/end fields, and non-drug orders with opening/start/end/status/frequency fields. Direct header and sample inspection confirmed these fields. A bounded full-file audit found 338,040 procedure rows, 322,166 nonempty procedure starts, 183,354 midnight starts, 16,730,319 order rows and 519,237 order rows matching broad pathway tokens. These are source-feasibility counts, not endpoint prevalences or study results. Broad order tokens include diagnostic tests and routine care, so they cannot be used as a clinical label without a frozen reviewable dictionary. The snapshot has no validated HCC confirmation, diagnosis time, laboratory units/reference ranges, indication, scheduling, consent, treatment administration/completion, response, toxicity, mortality or outside-care capture.

## Population and temporal design

Use HCC snapshot `[source checksum]`, catalog [source checksum], with every source read-only. Normalize Unicode and whitespace only in keys and diagnosis text. Join `diagnoses` to `encounters` on exactly (`patient master index`, `visit number`). Freeze and print the HCC cohort rule before locked evaluation: normalized `hepatocellular carcinoma` or case-insensitive `hepatocellular carcinoma` in `diagnosis name`; report all matched strings, `diagnosis type`, duplicate keys and unmatched joins. This is a record-coded cohort, not pathology-confirmed active HCC.

Include age >=18, parseable native `admission time` and `discharge time`, nonnegative stay, admission in [2011-01-01, 2026-01-01), and discharge before 2026-01-01. Select the earliest eligible encounter for each `patient master index`, ordered by native admission time then `encounter number`; do not replace an invalid earliest encounter with a later record. Set t0 to `admission time`. Exclude direct identifiers `name`, `ID number`, `mobile phone number`, `medical insurance/encounter card number`, and `inpatient number` from predictors. Every eligible admission remains in the primary estimand, including early discharge, early procedure and unresolved-time cases.

Use half-open elapsed-time intervals:

- prior history: [(t0-730 days), t0), only rows with valid native time strictly less than t0;
- current assay history: [t0, t0+12 hours), never [12,24);
- early documentary-state window: [t0, t0+24 hours);
- later pathway window: [t0+24 hours, t0+72 hours).

The 12-hour gap prevents a laboratory at or after hour 12 from being used to predict an overlapping early state or a coarse-time later event. Audit boundary ties, midnight starts, invalid/ongoing times, before-admission and after-discharge rows, and rows linked to the anchor encounter that have a pre-anchor native timestamp. Unparseable times are never absence; they contribute to unresolved-state counts and sensitivity bounds.

## Exhaustive all-admission endpoint

The primary outcome is a terminal documentation state, not a clinical treatment state. Construct the early state for every eligible admission from procedure/order records:

- E_PROC: valid procedure start in [0,24) before discharge;
- E_ORDER: qualifying pathway-family order opened in [0,24), when no earlier valid E_PROC;
- E_UPROC: unresolved procedure timing that could alter the early ordering;
- E_UORDER: unresolved qualifying order timing that could alter the early ordering;
- E_DISCH: discharge at or before 24 hours before any established earlier event;
- R24: none of the preceding states established.

Use a prespecified precedence table for same-time events, with a conservative primary rule and procedure-wins/order-wins sensitivities. No early laboratory feature predicts this early state; all four model versions use the same early-state model.

Among R24, define the first later state in [24,72) using the same encounter key:

- C_E, C_S, C_A, C_M: a first valid family procedure with a same-family qualifying order opened no later than the procedure start and within a frozen 48-hour lookback;
- P_E, P_S, P_A, P_M: a first valid family procedure without such a preceding same-family order;
- Q_E, Q_S, Q_A, Q_M: a qualifying family order with no same-family procedure before discharge or hour 72;
- O: a first valid procedure matching no family;
- D: discharge before an established qualifying order/procedure;
- U: unresolved procedure/order timing that could change the state;
- N72: no established state through hour 72.

A later order never retroactively changes a prior procedure-only state. A valid non-family procedure preceding a family episode remains O. Multiple same-time family matches remain M. A Q state is an order-documentation endpoint at the window boundary, not evidence of non-receipt. The primary all-admission estimand is the mean terminal probability vector over every eligible admission, obtained by the early-state probability multiplied by the conditional R24 later-state distribution and retaining all early states. Report the R24-conditional distribution only secondarily.

The parent’s semantics-independent endpoint is a mandatory sensitivity: procedure-only P0/D0/U0/R24 followed by P1/D1/U1/N72, using procedure presence and native `start time` only. It must not be replaced by the concordance endpoint. If concordance is sparse or dictionary coherence fails, the parent endpoint remains computable but the clinical pathway interpretation is inconclusive.

## Prospective semantic dictionary and endpoint adjudication boundary

In buckets 0–59, with choices fixed before reading locked labels, build a clinician-reviewable dictionary from exact `surgery` and `orders (non-drug)` strings. Candidate families are:

- E (embolization/interventional): explicit TACE/TAE/embolization/chemoembolization language plus hepatic/liver/hepatic artery context;
- S (resection/transplant): hepatic/liver context plus resection/transplant/resection/transplant;
- A (ablation): hepatic/liver/tumor/lesion context plus ablation/radiofrequency/microwave/cryotherapy/ablat;
- M: more than one family matches;
- X: therapeutic-looking but unassignable or mixed;
- O: valid procedure matching none.

The final dictionary must print normalization, positive and exclusion terms, exact strings, counts and adjudication status. Exclude diagnostic tests, routine nursing, imaging-only and administrative/cancellation language from a single-family order match; do not use `Order Status`, `Order Duration` or `Frequency` to infer intent or execution. Orders use `Order Entry Time` as the primary documentation time; `Start Time` and `End Time` are audit/sensitivity fields. Procedures use `Start Time`; `End Time` and `Surgical Source` are audit fields.

A qualifying concordance requires the same normalized (`patient master index`, `visit number`), same family, order `order opening time` <= procedure `start time`, both valid, order-to-procedure gap in [0,48] hours, and procedure start before discharge and within the later window. This is a reproducible record linkage state. It does not prove a plan, intent, administration or completion. A clinician-blinded review of a stratified sample of exact family strings and C/P/Q cases is required before describing the endpoint as clinically meaningful; absent such review, report only a lexical/documentation result and mark the semantic mechanism analysis inconclusive.

## Information sets, alternatives and split

Use one patient-level split for all models: SHA-256 of normalized `patient master index` under catalog policy, modulo 100; buckets 0–59 fit, 60–69 preprocessing/hyperparameter/regularization selection, 70–79 locked evaluation, and 80–99 inaccessible and not external validation. All rows for a patient follow the same bucket. Freeze cohort, dictionary, pairing, state precedence, assay inclusion, transformations, dimensions, hyperparameters and calibration before test labels are used.

A (transparent baseline) uses age, sex, admitting department, calendar era, admission time-of-day, pre-admission encounter count, prior assay-specific nearest/count/recency/missingness summaries, and current early process-free context. It predicts the full terminal vector with a sequential multinomial cause-specific model. It excludes current [0,12) assay values, procedure/order text, medications, documents, pathology and post-boundary data.

L adds current [0,12) assay-specific history using `laboratory_test`, `qualitative_result`, `quantitative_result`, `specimen_type`, and `test_time`: first/last values, within-assay change, elapsed time, count, missingness/density and slope only with two distinct native times. Numeric and qualitative results remain assay-specific because there is no unit column.

H adds the prior 730-day transparent summary using encounter timing, assay-specific lab counts/first-last/change/recency/slope, generic procedure occurrence counts/recency/gaps, and order/medication documentation-process counts/recency/missingness. It uses no order/procedure names for the primary prediction. All transformations are fit-only; “no observation” indicators are explicit.

S is the substantive learned alternative using exactly H’s prior-window rows, event source/type, native relative time and permitted assay/process payloads. It is a low-dimensional continuous-time latent state-space model with assay-specific offsets/noise, irregular-time decay, observation masks and a coupled head for the same early/later terminal vector. It may reveal nonlinear level/change coupling, order-sensitive recency and posterior uncertainty lost by H’s summaries. A process-only S variant is mandatory; if it matches S, the result is documentation intensity rather than physiology. S is not rejected because it is neural or GPU-capable. It is retained because irregular sampling is the scientific uncertainty; a CPU fit is first, with one allocated A100 only if a bounded probe shows material need.

The actual primary comparison is H versus L: does prior local history add information beyond admission context and the first 12 hours of current labs? S versus H is secondary and tests whether representation of irregular history adds information beyond transparent summaries. All versions predict the same exhaustive endpoint on the same split and output.

## Evaluation, proper scores and uncertainty

Evaluate locked predictions for every eligible admission using multiclass log loss, multiclass Brier score, calibration intercept/slope or reliability curves, observed-versus-predicted probability for every early/later/terminal state, and paired H-minus-L and S-minus-H contrasts. Report marginal P1 and concordance probabilities as secondary risk-scale summaries, never as clinical utility or treatment probabilities. Use at least 500 patient-clustered paired bootstrap resamples (1,000 preferred), preserving all admissions per patient; locked-prediction bootstrap is primary and refit bootstrap is sensitivity. Report history-availability strata, effective state support, missing-time fractions, and exact partition counts.

Supportive primary evidence requires coherent source/key/time audits; positive H-minus-L proper-score improvement with a 95% interval excluding zero and no material calibration deterioration; attenuation under time/value/history permutations; and no full explanation by process-only variables. Concordance-specific support additionally requires enough C/P/Q support, stable strict/broad dictionary results, stable 24/48/72-hour pairing sensitivities, and clinician review indicating that the strings represent the intended documentary pathway. S is supportive only if it adds calibrated improvement over H beyond uncertainty, is stable across seeds and timing sensitivities, and is not reproduced by process-only inputs.

Adverse evidence is no H-minus-L improvement, worse calibration, a gain explained by testing/recording intensity, persistence after cross-patient history shuffling or label permutation, or a concordance gain that disappears in the procedure-only sensitivity. Such results reject the incremental-history or concordance interpretation but do not prove physiology is clinically irrelevant. Inconclusive evidence includes dominant U states, sparse C/P/Q cells, poor exact-string coherence, wide intervals, severe left truncation, order/procedure key mismatch, dictionary instability, or absent clinical review. Do not relabel inconclusive results as support.

Falsifications are frozen before locked evaluation: within-patient assay/source time shuffle; within-assay value shuffle; cross-patient history shuffle within partitions; reverse temporal order; process-only history model; observation count/density/missingness ablation; label permutation within era/department; forbidden-window sentinel using [12,24) data; procedure/order duplicate and midnight/tie/missing-time bounds; order-time sensitivity; dictionary perturbation and family/string leave-outs; pairing-window sensitivity; status-stratified order audit; and the parent procedure-only endpoint. Persistence after label/history permutation indicates leakage or artifact. Persistence after assay permutations, or full reproduction by process variables, falsifies a physiology interpretation.

## Exact read-only bindings and complete catalog audit

All HCC files are ordinary CSVs; archive member is “ordinary file” for every file. Every clinical row is joined by normalized (`Patient Master Index`, `Encounter Number`) and duplicate, multiplicity and unmatched-key audits are mandatory.

Primary tables:

- `encounters`, schema `datasets/hcc/table-b743286cb1249287.json`, source `[internal dataset path]`: `Patient master index`, `Encounter number`, `Age`, `Sex`, `Encounter time`, `Admission time`, `Discharge time`, `Department`.
- `diagnoses`, schema `datasets/hcc/table-12710723c3df0c99.json`, source `[internal dataset path]`: `Patient Master Index`, `Encounter Number`, `Diagnosis Name`, `Diagnosis Type`; no native diagnosis time.
- `labs`, schema `datasets/hcc/table-38aad8c54471332f.json`, source `[internal dataset path]`: keys, `test`, `qualitative result`, `quantitative result`, `specimen type`, `test time`.
- `procedures`, schema `datasets/hcc/table-d5eae16f8f8093d9.json`, source `[internal dataset path]`: keys, `Surgery`, `Start Time`, `End Time`, `Surgery Source`.
- `orders`, schema `datasets/hcc/table-6b93dcf0ea823702.json`, source `[internal dataset path]`: keys, `Non-drug medical order`, `Order time`, `Start time`, `End time`, `Order duration`, `Order status`, `Frequency`.
- `medications`, schema `datasets/hcc/table-4f6ecaeb6e8f69c2.json`, source `[internal dataset path]`: keys, `Medication`, `Single-dose medication amount`, `Single-dose medication amount unit`, `Frequency`, `Start time`, `End time`, `Administration route`, `Drug type`; process audit only, no treatment interpretation.
- `examinations`, schema `datasets/hcc/table-fd016d2731b9d6c6.json`, source `[internal dataset path]`: keys, `Examination`, `Examination Findings`, `Examination Diagnosis`, `Start Time`, `Machine Model`, `Examination Number`; secondary audit only.
- `clinical_documents`, schema `datasets/hcc/table-66afca58512c2fca.json`, source `[internal dataset path]`: keys, narrative columns including `Admission Diagnosis`, `Admission Status`, `Diagnostic and Treatment Course`, `Discharge Status`, `Discharge Diagnosis`, `Surgery Name`, `Surgical Procedure`; no native time and duplicate `Admission Diagnosis` column.
- `pathology`, schema `datasets/hcc/table-0a4ee86a446c605c.json`, source `[internal dataset path]`: keys, `Pathology`, `Examination Findings`, `Examination Diagnosis`, `Machine Model`; no native time.
- `vitals`, schema `datasets/hcc/table-8436de9cba74b8ca.json`, source `[internal dataset path]`: keys only; no payload/time.
- `transfers`, schema `datasets/hcc/table-320c20f732e71789.json`, source `[internal dataset path]`: keys only; no payload/time.
- `front_page`, schema `datasets/hcc/table-38b3224239acc33f.json`, source `[internal dataset path]`: keys only; no payload/time.

The complete 12-file HCC catalog must be audited and retained as read-only even when tables are secondary. The other configured datasets (MIMIC, eICU and UKB) remain directly accessible through their catalog bindings, rows and notes and are not silently substituted or used as HCC evidence; this is an HCC-only proposal. No archive member is used for HCC. Sources are never overwritten and derived matrices/audits belong in the workspace.

## Compute, evidence limits and revisit record

Discovery measurements are limited to the header/sample inspection and bounded streaming audit above. No solver fit or locked result has been run. Future solver planning uses at most 16 CPUs, 262,144 MiB memory, 28,800 seconds, and up to 8 allocated GPUs; this is a planning envelope, not a measured runtime. Use chunked scans for the 2.21-GB labs, 2.19-GB orders, 491-MB medications and 1.14-GB examinations. B0/L/H aggregation is CPU-first. S first receives one CPU implementation; request one A100 from `ehr-campaign-gpu:20260908` only after a bounded probe demonstrates material need, explicitly using `cuda:0`. Expected S/bootstrap times are unverified.

The null history increment is meaningful completion. Computably checkable outputs are source/key/time audit, frozen cohort and dictionary, endpoint row provenance, locked predictions, proper scores, calibration, bootstrap intervals, partition/support counts, process-only and permutation falsifications, and sensitivity results. Clinical adjudication is still necessary for HCC confirmation, diagnosis timing, tumor burden/stage/resectability, indication, intent, recommendation, scheduling, consent, administration, completion, response, complications, mortality, outside care, and pathway-string meaning. Prospective chart review and external validation are required before deployment.

The demonstrations were used as method context only. The local natural-history material supports dated history modelling but its UKB/Danish setting is unavailable; the Bayesian material supports an irregular latent adaptation but its genetics are unavailable; the cancer README states that the main article and full STAR Methods are unavailable, and no HCC images exist. No reproduction is claimed. The expert seed library has no HCC problem; its UKB/MIMIC/eICU cards are not HCC evidence or parents.

Alternatives not chosen are retained explicitly: the incumbent history-summary/state-space design remains the primary comparison; the parent procedure-only endpoint remains a sensitivity; text/image models are deferred because HCC text lacks native document time and images are unavailable; causal treatment-effect analysis is deferred because indication, receipt, confounding control and adjudicated outcomes are missing; a larger GRU/transformer is deferred unless S has stable residual timing signal and sufficient event support. These are evidence-bound deferrals, not neural-network or GPU prohibitions.

Revisit concordance only if the frozen source audit shows adequate C/P/Q support, clinician-blinded string review confirms coherent meaning, and dictionary/pairing sensitivities are stable. If those conditions fail, report the dictionary-independent parent endpoint and its calibrated history increment, mark the semantic endpoint inconclusive, and do not promote it to a clinical pathway claim.
