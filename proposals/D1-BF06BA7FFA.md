> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 22 evolution: an earlier competing-observation check for the HCC assay-change question

Status: independent substantive child of [prior hypothesis]. Design only. No cohort count, fitted parameter, effect estimate, prevalence, clinical adjudication, or clinical conclusion is claimed.

## Change and scientific opening

The inherited question is retained: after separating a stable pre-index assay/recording profile from a patient's later assay change, does within-person change add held-out information about a later locally recorded TACE record? The strongest evidence-supported claim is only predictive and record-level: a day-42 assay trajectory may add information beyond a matched observation clock and stable profile in the first exact-code TACE population. O0-O4 are operational record outcomes, not adjudicated intent, completion, response, progression, survival, benefit, or utility.

The remaining rival is stronger than ordinary measured-severity confounding. The day-42 eligible cohort is selected by records that occur after the index procedure. A patient may remain observable because of planned follow-up, non-TACE care, impending retreatment, transfer within the captured system, or documentation intensity; a patient with outside care or sparse records may appear to have “lost observation.” If this process also determines which assay is repeated, a day-42 within-person increment can be a marker of observation or care routing rather than a durable patient signal. The inherited R42 weight and R28 arm are useful, but they do not separately quantify the earlier composition check or distinguish non-TACE operational care from observation loss.

The targeted repair is the smallest additional check that can change the next decision:

1. Freeze an earlier landmark at L14 = t0 + 14 days, before the later TACE risk window begins.
2. Audit the transition from L14 through L42 as mutually exclusive operational states: non-TACE care/monitoring, observation ending before day 42, early repeat-TACE, or reaching day 42 without either, with unknown/invalid timing retained rather than forced.
3. Use the L14 information to estimate a descriptive, fold-frozen transport weight for the R42 day-42 feature set, while reporting the joint competing-state probabilities and support.
4. Test the same stable-profile versus within-person-change increment at L14 and L42, and repeat the L42 contrast after excluding the final seven days.

This is a selection and ascertainment study, not a causal correction. [K1] supports a learned TACE-adjacent prediction alternative but uses a selected imaging cohort with different endpoints; [K2] bounds treatment response as an imaging/necrosis-aware construct; [K3] shows why documented outcomes and missingness must be bounded rather than treated as treatment effects. The proposed advance is to test whether the HCC assay increment survives an earlier, explicit competing-observation audit on the available longitudinal records.

## Hypothesis and estimands

Primary hypothesis:

> In the inherited first-index TACE population that is operationally observable through day 14 and has no early repeat TACE, the baseline-supported within-person assay-change block through day 42 improves untouched-test prediction of the later operational O0 record beyond the same clock and stable pre-index assay profile; the increment remains after descriptive standardization for the L14-to-L42 observation process, is not reproduced by a process-only block, and has a directionally concordant pre-day-42 L14 analogue.

Leading explanation: a within-person change in recorded assay content contains information beyond stable patient/recording profile.

Strongest rivals and their predictions:
- future-observation selection: the increment shrinks or vanishes after R42 transport weights; non-TACE-care and loss states are unequally distributed and predict feature availability;
- late care-routing/documentation: the increment disappears when content in (t0+35,t0+42] is removed or is matched by process-only timing/availability;
- stable-profile explanation: stable profile absorbs the apparent signal and Delta42 adds little;
- measurement artifact: within-patient value or assay-label permutations preserve the apparent increment.

For endpoint j, define held-out patient-level loss Lw(M,j) for model/input block M, using ordinary weights or the predeclared observation weights:

- A_clock = M0 + B0 + P_obs + P_care + C42, with no assay-result value.
- A_stable = A_clock + P_stable.
- A_change42 = A_stable + Delta42.
- A_snap42 = A_stable + S42.
- A_change14 = M0 + B0 + P_obs + P_care + C14 + P_stable + Delta14.
- A_snap14 = the same L14 block with S14 instead of Delta14.

P_stable is built only from valid, assay-specific labs in Hpre=[t0-365 days,t0): last content, robust repeated-value summary where valid, qualitative reference token, and content-availability indicators. Delta42 is computed only from same-label/same-sample-type labs in (t0,t0+42], relative to the pre-index reference; no absent baseline is replaced by zero. Numeric units/reference ranges are not available, so values are never pooled across assays. Delta14 uses only (t0,t0+14]. C14/C42 contain event presence, label/channel, relative time, inter-event time, opportunity, missingness and source-family counts, but no qualitative or quantitative result.

The within-person estimands are:

- Gwithin,42,j = Lw(A_stable,j) - Lw(A_change42,j)
- Gsnapshot,42,j = Lw(A_stable,j) - Lw(A_snap42,j)
- Gwithin,14,j = Lw(A_stable-at-14,j) - Lw(A_change14,j)

The primary new estimand is Gwithin,42,O0 under the observation-standardized weights. O1-O4 are boundary/robustness endpoints; O_planproxy_cap is a process-control endpoint if its inherited support permits it. A positive value means lower held-out loss for the added recorded block, not clinical utility.

### Earlier competing-observation estimand

Let P0 be all eligible index patients and P14={i in P0: obs_end_i >= t0+14 days and required timing is valid}. The P0-to-P14 attrition is reported; P14 is the primary pre-outcome analysis population because it has a defined earlier observation check. Let E be the inherited early-repeat-TACE exclusion for 0 < tp-t0 < 43 days. Among P14 with E=0, define the mutually exclusive operational state Z over (t0+14,t0+42]:

- Z=N: the earliest qualifying non-TACE operational care/monitoring signal is in the interval. It is any valid-time row from encounters, examinations, non-cancelled orders, medications, labs, or a non-TACE procedures row, with its channel and time retained. This is a record-process state, not treatment receipt or clinical deterioration.
- Z=L: no Z=N signal occurs and the all-source observation end is before t0+42 days.
- Z=R: no Z=N signal occurs and obs_end >= t0+42 days.
- Z=U: invalid/insufficient source time prevents distinction; U is reported, not imputed to L.
- E is separately reported before the competing-state analysis; no early TACE is silently treated as non-TACE care.

The first qualifying signal has precedence over later observation status. Thus N, L and R are competing operational states, and U is an explicit support/missingness state. The exact source channel, first time, and reason for U are output.

Fit within each development fold a multinomial model for Z using only information available by L14: M0, B0, pre-index P_obs/P_care, C14 and the L14 availability masks. Do not use day-42 assay values, later endpoint evidence, or any post-L14 outcome label. Report qN, qL, qR, qU, event calibration and proper loss for Z. The joint observation estimand is the vector Pr(Z=k | P14,E=0), k in {N,L,R,U}; the R42-selection component is qR and is not a clinical risk.

For day-42 assay models evaluated among R42=1, use a fold-frozen stabilized descriptive transport weight:

w_i = π0(X0_i) / πR(X0_i,H14_i),

where πR=P(R=1 | X0,H14) from the multinomial model and π0=P(R=1 | X0) is the numerator model. Normalize weights within fold, freeze truncation only from development-fold support, and report unweighted and weighted results, weight tails, overlap and effective sample size. This reweights the observed-through-day-42 records toward the P14 baseline distribution conditional on measured H14 information; it is not an inverse-probability causal effect estimate and cannot repair outside-care or unmeasured clinical selection.

The solver must also report the direct empirical/modeled N versus L versus R composition before weighting. If U or early TACE is material, the selected-cohort result is not presented as transport to P0.

## Population, timing and endpoint rules

Use the first row in procedures with Unicode-normalized, trimmed, case-folded Surgery equal to TACE, nonmissing Patient Master Index and Encounter Number, and parseable Start Time; call its start t0. Collapse exact duplicate patient/start records only under a deterministic audit. Group patients only by Patient Master Index. Every visit-level join is exactly (Patient Master Index, Encounter Number). No names, identity-card numbers, phones, insurance cards, hospital numbers, file order, or cross-dataset identifiers are allowed.

The index feature history is [t0-365,t0). L14 is [t0,t0+14], with the endpoint at t0+14 included only for the earlier snapshot/trajectory; L42 is [t0,t0+42]. No row after t0+42 is a predictor. The later risk window is [t0+43,t0+181), with fixed bins [43,57), [57,71), [71,85), [85,99), [99,113), [113,127), [127,141), [141,155), [155,169), [169,181). Follow-up ends at first qualifying event, inherited obs_end, or day 181; [43,90] and [91,181) are fixed sensitivities.

Retain the inherited operational hierarchy:
- O0: first later unique literal-code TACE in the risk window.
- O1: O0 plus the frozen semantic hepatic-arterial procedure predicate, valid procedure time, same-patient/same-visit timed examination or order corroboration.
- O2: O1 plus the frozen same-visit medication corroboration.
- O3: O2 plus a qualifying examination, order or medication row on the exact visit key with valid event/start time strictly after tp and no later than tp+72 hours; orders require nonblank Order Status and exclude normalized cancellation tokens Cancelled, Voided, Revoked and Discontinued.
- O4: O3 plus parseable same-row end time te with 0 <= te-tp <=72 hours. Missing, malformed, negative or longer closure is closure_unknown, not a negative clinical event.
- capture-adequate: inherited indicator based on encounter discharge >= tp+72 hours or a valid-time non-procedure row in (tp,tp+72 hours]; this is not proof of complete capture.
- O_planproxy_cap: inherited pre-opened-order process control, retaining O4 overlap, unknown_provenance, O3-only, closure_unknown and capture_unknown flags.

Post-tp corroboration and closure fields are endpoint audits only. They never enter predictors, selection models or censoring. No absence of a downstream row is evidence of intent. Early literal-code TACE rows before day 43 are excluded from the later risk set and reported as E.

## Exact HCC source bindings

Frozen HCC snapshot: [source checksum]. Catalog: [internal dataset path]; catalog [source checksum]. The parent binding audit identified 12 ordinary CSV files and no archive members. Sources are read-only.

| table | exact source path and SHA-256 | required columns, time and role |
|---|---|---|
| procedures | [internal dataset path]; [source checksum] | Patient master index, encounter number, surgery, start time, end time, surgery source; t0, early TACE, O0-O4, non-TACE procedure signal |
| encounters | [internal dataset path]; [source checksum] | Patient Master Index, Encounter Number, Age, Sex, Encounter Time, Admission Time, Discharge Time, Clinical Department; joins, M0, obs_end and N/L/R timing |
| examinations | [internal dataset path]; [source checksum] | Patient master index, visit number, examination, examination findings, examination diagnosis, start time, examination number; O1/O3 corroboration, operational N, timing audit; narrative is not a validated response label |
| orders | [internal dataset path](non-medication)_2062526727266216118.csv; [source checksum] | Patient master index, Encounter number, Non-medication order, Order time, Start time, End time, Order status, Frequency; O1/O3, pre-open audit, operational N and cancellation/time audit |
| medications | [internal dataset path]; [source checksum] | patient master index, encounter number, medication, single-dose medication amount, single-dose medication amount unit, frequency, start time, end time, route of administration, medication type; O2/O3, operational N and capture clock |
| labs | [internal dataset path]; [source checksum] | Patient Master Index, Encounter Number, Test, Qualitative Result, Quantitative Result, Specimen Type, Test Time; B0, S14/S42, Delta14/Delta42, assay opportunity and operational N |
| diagnoses | [internal dataset path]; [source checksum] | Patient Master Index, Encounter Number, Diagnosis Name, Diagnosis Type; matched-visit context only, no validated event time |
| pathology | [internal dataset path]; [source checksum] | patient master index, encounter number, pathology, examination findings, examination diagnosis, diagnosis; context/review only, no validated event time |
| clinical_documents | [internal dataset path]; [source checksum] | Patient Master Index, Encounter Number and narrative fields; coverage/context audit only, no validated event-time predictor |
| vitals | [internal dataset path]; [source checksum] | Patient Master Index, Encounter Number; identifier/catalog audit only, no validated time/content |
| transfers | [internal dataset path]; [source checksum] | Patient Master Index, Encounter Number; identifier/catalog audit only, no cross-table time/content |
| front_page | [internal dataset path]; [source checksum] | Patient master index, Encounter number; identifier/catalog audit only, no predictor |

All required joins are on the documented patient or composite visit keys. The experiment uses only validated event times from procedures, encounters, examinations, orders, medications and labs. It does not infer dates from diagnoses, pathology, documents, vitals, transfers or front-page rows. HCC lacks reliable death status, outside-care capture, imaging/raw images, assay units/reference ranges, validated narrative temporality, technical TACE dose/intent, treatment response/progression, toxicity, survival, utility and patient-important outcomes. Clinical adjudication or a prospective/imaging-linked study is required for those claims.

## Comparable methods and alternatives

Both methods use the identical P14/E-free patients, input blocks, Z-derived weights, O0-O4 labels, risk grid, right-censoring, temporal split, uncertainty family and held-out test predictions. Neither uses Z, O0-O4, post-tp corroboration, closure, or obs_end beyond t0+42 as an outcome predictor.

Transparent baseline: pooled logistic discrete-time hazard with intercept and risk-bin indicators and elastic-net alpha=0.5. Fit A_clock, A_stable, A_change42, A_snap42 and the L14 A_change14/A_snap14 analogues. Fit parsers, qualitative token dictionaries, assay-specific scalers, imputation, P_stable/Delta construction, selection models, weight truncation, regularization and early stopping only within grouped development folds. The baseline is scientifically adequate because each information block, competing state, and weight can be audited and its loss difference directly answers the nested question.

Matched learned alternative: a compact time-aware two-stream GRU over the same allowed event stream from t0-365 through t0+42. One stream receives process/time/availability information C14/C42; the assay stream receives the same eight assay labels, qualitative/numeric/inequality-preserving content, sample type, relative time, time since prior event and baseline-available masks. Separate ablations fit clock, clock+stable, clock+stable+Delta14, clock+stable+Delta42 and snapshot versions. One GRU layer, hidden size 32, dropout 0.10, 32/16 hazard head, Adam 1e-3, weight decay 1e-4, maximum 50 epochs, early stopping after eight non-improving epochs, seeds 17/29/41. The learned model can reveal nonlinear ordered patterns, irregular timing and recovery-then-worsening combinations that pooled elastic-net summaries lose. It cannot reveal units, imaging, intent, outside care or mechanism.

Primary selection uses CPU: approximately 1-4 hours on 4 CPUs/16 GiB for materialization, multinomial observation models, elastic-net fits, paired bootstrap and fixed permutations. GRU sensitivity is approximately 2-6 hours on 4 CPUs/16 GiB; if materially helpful, request one allocated A100 with resources gpus=1 and explicitly use cuda:0 inside the managed job. These are planning estimates, not measured runtimes. This discovery episode has a 9,000 science-second and two-GPU-slot limit; the future solver envelope is separate: 16 CPUs, 262144 MiB, up to 8 GPUs and 28800 seconds. Ordinary shell CUDA visibility is not a hardware test.

Deferred alternatives: transformer, narrative NLP, latent causal/intent model, image/radiomics model and mechanistic liver-response model. They require missing timed expert labels, validated narrative temporality, assay units, images or adjudicated response/outcomes. A larger model is not chosen for a small predictive gain; revisit only if a substantive observation-state or assay-change question cannot be represented by the matched GRU.

## Split, uncertainty and falsification

Sort P0 by t0; assign earliest 80% to development and latest 20% to one untouched test, with no patient in both. Use five grouped development folds. All endpoint, parser, feature, observation-state, weight and model choices are frozen before test scoring. Use 1,000 patient-level paired bootstrap resamples of the untouched test set and one max-|t| simultaneous 95% family across O0-O4, O_planproxy_cap, Gwithin/Gsnapshot at L14/L42, ordinary/weighted arms, Z states and fixed falsifiers. Report paired log loss, Brier/integrated Brier, calibration, discrimination secondarily, event/risk-set counts, P0-to-P14 attrition, E/U counts, qN/qL/qR/qU, weight tails, overlap, ESS and paired availability.

Frozen falsifiers:

1. R42 transport: compare ordinary versus weighted Gwithin,42. If the increment disappears under adequate overlap, observation selection is favored; if positivity or ESS fails, the weighted estimand is INCONCLUSIVE.
2. Earlier pre-outcome check: compare Gwithin,14 and Gwithin,42 with the same [43,181) outcome. A day-42-only increment with no supported L14 analogue is late-landmark-dependent, not evidence of a durable within-person trajectory.
3. Competing-state composition: report qN, qL, qR and qU by Delta42 availability and by assay. A high N or L state concentrated among patients with Delta42, or a large U state, narrows interpretation to workflow/ascertainment and may make transport INCONCLUSIVE.
4. Late-window removal: remove all lab/process rows in (t0+35,t0+42] and refit identically. Erasure is adverse to a durable trajectory interpretation and compatible with review/scheduling lead time.
5. Process-only rival: compare A_clock without result values, A_stable, A_change42 and A_snap42. If process-only matches the change increment within the frozen uncertainty/resolution rule, retain only workflow-associated prediction.
6. Within-patient content permutation: preserve assay labels, times, and availability but permute content within patient/assay and development-frozen timing strata; separately permute assay labels. A matched increment is adverse to content-specific interpretation.
7. Endpoint boundary: repeat O0 with O1-O4, closure/capture unknowns visible, and the fixed [43,90]/[91,181) horizon sensitivity. Agreement across operational definitions supports record robustness only.
8. Negative control: fit the same input blocks to O_planproxy_cap where support allows. Similar increments in a workflow process control are adverse to a TACE-specific interpretation.

Supportive requires: adequate P14 and R42 support; positive simultaneous lower bounds for Gwithin,42,O0 and its weighted counterpart; no adverse L14, late-window, process-only or permutation control; stable direction in the GRU; and no endpoint-boundary contradiction. It supports a recorded within-person assay-change increment that transports descriptively across measured observation states. It does not support response, intent, mechanism, benefit or a causal effect.

Adverse means stable profile absorbs the increment, weighted results erase it, the L14 check is absent/adverse, late content explains it, process/timestamp permutation matches it, or the process-only control is equally informative. Retain a narrower snapshot or workflow result only if its own uncertainty and support pass; do not conclude that assays lack clinical value.

Inconclusive means inadequate event/paired availability, P14/R42 positivity failure, unstable weights, high U, wide uncertainty, or method disagreement. Freeze the direction, report the missing evidence, and seek an independently scheduled/imaging-linked cohort rather than changing windows or subgroups.

## Actual scientific deliverable

The future solver must newly fit and output: trajectory_definition.json; r14_r42_competing_observation_audit.csv; endpoint_event_audit.csv; trajectory_availability_audit.csv; competing_observation_multistate.csv; trajectory_support_freeze.json; heldout_predictions_losses.csv with all nested models and ordinary/weighted arms; selection_robust_contrasts.csv; trajectory_falsification.csv; trajectory_gru_sensitivity.csv when feasible; trajectory_decision_gate.json; and claim_output_map.md. Completion requires computed held-out predictions/losses, frozen source and split provenance, state/overlap/ESS checks, uncertainty, and a conclusion explicitly mapped to those outputs. Readiness or a planned fit is not a result.

## Key references

Exactly three distinct inspected works are attached as K1-dai2025-inspected-excerpt.txt, K2-tsurusaki2024-inspected-excerpt.txt, K3-minh2026-inspected-excerpt.txt, with receipts and byte hashes in key-references.json. K1 supports the learned-method comparison but bounds its selected imaging cohort; K2 bounds response interpretation; K3 supports explicit missingness and ascertainment auditing. No unavailable supplement, raw imaging, or clinical adjudication is claimed.
