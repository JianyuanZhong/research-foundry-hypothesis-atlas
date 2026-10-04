> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Proposal: schedule-robust component trajectories after a recorded TACE-like index

## Episode, parent, and actual scientific deliverable

This Episode-23 child evolves assessed-valid parent
\`[prior hypothesis]\`. It preserves the parent’s exact HCC
read-only source bindings, encounter-constrained first recorded TACE-like index,
day-45 risk set, component-resolved AFP/albumin/total-bilirubin trajectory,
strict-versus-broad pathway ontology, coding/capture controls, patient-temporal
split, clustered uncertainty, and evidence limits.

The remaining clinically consequential ambiguity is observation timing. The
parent’s last pre-index and first post-index measurements (post-index days 7–45)
are valid, reproducible recorded-care variables, but a day-8 measurement and a
day-44 measurement can represent different clinical opportunities. A patient
with frequent assays can contribute a different apparent change category from a
patient with one late assay. Measurement timing, number of tests, department,
and local contact may therefore explain an apparent trajectory/pathway
association even after missingness indicators are included. This child makes
that ambiguity a falsifiable estimand rather than an informal limitation.

The future solver must newly construct the same leakage-safe cohort and
procedure episodes, freeze the same assay and endpoint vocabularies, fit a
transparent observation-schedule baseline and a trajectory-augmented baseline,
estimate schedule-standardized component-profile contrasts and incremental
locked-test CIF/log-score outputs, and fit or explicitly defer a joint
irregular-time latent model. It must produce patient-clustered uncertainty,
overlap and calibration diagnostics, timestamp-permutation and placebo
falsifications, and an interpretation manifest. Discovery has not fitted these
models and claims no result.

## Strongest supported claim, unresolved claim, and clinical importance

The strongest claim supported by the available evidence is structural: dated
local procedure, encounter, and laboratory rows can be joined by
\`(patient master index, encounter number)\`; the procedure source contains many liver-related and
compound labels; and the laboratory source contains exact-name AFP, albumin,
and total-bilirubin rows with timestamps. A bounded full procedure audit found
338,040 rows and 7,781 labels, including 33,332 standalone hepatic-angiography
records; the selected laboratory-name screen found 190,022 AFP, 238,293
albumin, and 238,553 total-bilirubin rows, with 54,961 qualitative/empty
results. These are data-availability observations, not clinical findings.

The unresolved claim is whether a favorable recorded component pattern after an
eligible first recorded TACE-like episode has a reproducible, directionally
lower association with a later *strict recorded TACE-containing pathway* than a
discordant pattern, after standardizing over the opportunity and timing to
observe those components. This is a prognostic association with a local
recorded-care endpoint, not a response, treatment-intent, benefit, or causal
claim.

This matters because a surveillance or escalation signal that is actually a
test-scheduling/capture signal could mislead retrospective pathway studies and
future clinical workflow design. Separating the two is a substantive advance
over reporting a small predictive gain: it asks whether the component pattern
adds pathway-specific information beyond the process that generated the
measurements, while retaining diagnostic and non-liver recording controls.

## Falsifiable hypothesis

Let the favorable profile be \(A_F\): AFP decreases, albumin is
non-worsening, and total bilirubin is non-worsening. Let \(A_D\) be AFP
decrease with worsening of albumin or total bilirubin. “Decrease” and
“worsening” retain the parent’s assay-specific, training-only robust scaling
and uncertainty categories; they are not clinical response or liver-reserve
labels.

Primary hypothesis, tested at 320 days after the day-45 landmark: within the
common-support paired-observed target and after schedule/capture
standardization, \(A_F\) has a lower cumulative incidence of
\`TACE_strict\` than \(A_D\), with an absolute contrast of at least 0.03 in
the hypothesized direction. The contrast is also estimated in the full-index
population with availability states retained. A two-sided component
interaction test is reported in addition to this directional margin because
recorded TACE may reflect planned repeated care as well as escalation.

The repaired estimand is explicitly noncausal. For endpoint \(k\), time \(t\),
profile \(a\), baseline/capture covariates \(Z\), and schedule vector \(S\),
the paired-observed schedule-standardized contrast is

\[
\Delta_k(t;a,a') =
 E_{(Z,S)\sim P_{\mathrm{overlap}}}
 [\widehat F_k(t\mid Z,S,A=a) -
  \widehat F_k(t\mid Z,S,A=a')],
\]

where \(P_{\mathrm{overlap}}\) is the empirical distribution of observed
\((Z,S)\) among profile groups satisfying frozen positivity/overlap rules.
This is model-based predictive standardization of recorded outcomes, not a
treatment intervention and not confounding removal. The full-index estimand
retains all patients in the day-45 risk set and reports availability/missingness
states rather than imputing a clinical value.

The companion incremental estimand is

\[
\Psi_k(t)=
 E_{\mathrm{test}}[
 \widehat F^{B_{\mathrm{time+traj}}}_k(t\mid Z,S,A)
 -\widehat F^{B_{\mathrm{time}}}_k(t\mid Z,S)],
\]

evaluated on the same locked patients. \(B_{\mathrm{time}}\) contains
pre-index history and the measurement schedule but no laboratory values;
\(B_{\mathrm{time+traj}}\) adds the parent’s component categories, delays and
missingness. \(\Psi\) quantifies what the trajectory adds beyond observation
opportunity. It is not evidence that changing a laboratory value would change
care.

The hypothesis is falsified if the strict contrast is null or reversed after
schedule standardization and coding/capture adjustment, if
\(B_{\mathrm{time}}\) reproduces the apparent interaction without laboratory
values, if the association is equally strong for diagnostic-only or non-liver
recording, if timestamp permutation preserves it, if it is concentrated in
ambiguous bundles or one assay variant, or if it fails under the parent’s
encounter-only episode sensitivity. A null/adverse result concerns the
recorded-pathway hypothesis only; it does not show absent biological response.

## Exact data bindings, population, and time rules

The dataset guide \`datasets/README.md\`, HCC guide \`datasets/hcc/README.md\`,
HCC catalog metadata \`datasets/hcc/metadata.json\`, and the complete local
catalog identify the HCC snapshot
\`[source checksum]\`.
All listed HCC sources are ordinary files, not archive members. Source files
remain read-only. Every child table is aggregated by
\`(Patient Master Index, Encounter Number)\` before any join; no many-to-many join is permitted.

1. Procedures: read
   \`[internal dataset path]`,
   table \`procedures\`, schema \`datasets/hcc/table-d5eae16f8f8093d9.json\`.
   The verified header is
   \`patient master index, encounter number, surgery, start time, end time, surgery source\`.
   Retain raw name, source, both timestamps, matched terms, and episode ID.
   Form the primary episode within patient and encounter using the parent’s
   24-hour temporal grouping; retain encounter-only grouping as sensitivity.
   Untimed rows cannot define a dated index or outcome and are counted in the
   vocabulary audit.

2. Index ontology and anchor: the first eligible timed episode whose raw
   \`Surgery\` is literal \`TACE\), contains \`transarterial chemoembolization\`, or contains both
   \`Hepatic Artery\` and \`Embolization\` is the candidate index. Exact ties remain tied.
   Hepatic angiography alone cannot define the therapeutic index. Require a
   corresponding encounter record. Let \(t_0\) be the earliest start timestamp
   among tied index rows. Relative-time rules use hours from \(t_0\), with
   day-45 information ending at \(45*24\) hours; timestamps exactly on a
   boundary follow the stated inclusive interval.

3. Encounters: read
   \`[internal dataset path]`,
   table \`encounters\`, schema \`datasets/hcc/table-b743286cb1249287.json\),
   joined on \`patient master index, encounter number\`. The verified header includes
   \`Patient master index, encounter number, name, national ID number, mobile phone number, health insurance/encounter card number, inpatient number,
   age, sex, height, weight, visit time, admission time, discharge time, visit department\`.
   Require age >=18 and nonmissing sex. Use \`Visit Time\` as the local
   temporal anchor for diagnosis ascertainment; department, admission/
   discharge, and contact intervals are covariates, not adjudication.

4. Diagnosis ascertainment: read
   \`[internal dataset path]`,
   table \`diagnoses\`, schema \`datasets/hcc/table-12710723c3df0c99.json\`,
   joined on \`Patient Master Index, Encounter Number\`. The verified header is
   \`patient master index, visit number, diagnosis name, diagnosis type\`. Require
   \`Diagnosis Name\` containing \`hepatocellular carcinoma\` on an encounter dated from 180 days
   before through 7 days after the index encounter. Diagnoses has no time
   column: encounter time is only a dated diagnosis proxy, never onset,
   order, or clinical adjudication.

5. Require \(t_0\) on or before 2025-01-01 for a nominal 365-day local horizon.
   Follow from 46*24 through 365*24 hours after \(t_0\). Record maximum local
   follow-up and administrative local-observation end. Neither is death,
   survival, cure, or outside-care cessation.

6. Define the primary day-45 risk set by excluding any primary-ontology
   liver-directed therapeutic episode after index through 45*24 hours. Report
   excluded early therapeutic episodes separately. Diagnostic-only contacts
   remain eligible. This preserves the parent’s landmark and avoids conditioning
   the later endpoint on an early recorded therapeutic transition.

## Outcomes and strict-versus-broad ontology

Create the first mutually exclusive timed recorded states from day 46 through
day 365. Administrative loss of local observation is reported separately as an
observation/censoring state, not as death.

- \`TACE_strict\` (primary): timed episode containing literal \`TACE\), or a
  frozen training-only list of arterial chemoembolization/embolization labels
  that are not angiography-only and have no unresolved mixed-only
  interpretation. Vocabulary, exclusions, and ambiguous labels are locked
  before evaluation.
- \`Liver_therapeutic_broad\` (secondary): the parent broad liver-directed
  therapeutic ontology, including TACE, ablation, resection, transplant and
  other frozen therapeutic families, never angiography alone.
- \`Liver_diagnostic\`: hepatic angiography, liver imaging/procedure work-up,
  or diagnostic-only liver contact under a frozen lexical screen.
- \`Mixed_ambiguous\`: compound or unresolved strings not safely classifiable
  as strict therapy.
- \`Nonliver_procedure\`: first timed procedure outside the liver-directed
  therapeutic/diagnostic ontology, as a capture control.
- \`No recorded transition\` or administrative end of local observation.

The endpoint ladder is prespecified and scientific, not endpoint shopping.
Unclassified labels remain ambiguous; \`surgery source\` cannot be used to infer
intent. Diagnostic procedures are not therapeutic outcomes.

## Component exposure and the repaired schedule vector

Read
\`[internal dataset path]`, table
\`labs\`, schema \`datasets/hcc/table-38aad8c54471332f.json\`, joined on
\`patient master index, visit number\`. The verified header is
\`patient master index, visit number, test, qualitative result, quantitative result, specimen type, test time\`.
There is no units column.

Freeze the assay vocabulary using fitting data only. Primary numeric candidates
remain exact serum \`alpha-fetoprotein\` (AFP), serum \`albumin\`, and serum
\`total bilirubin\`. Exclude \`alpha-fetoprotein isoforms\`, \`prealbumin\`,
\`glycated albumin\`, urine/body-fluid albumin, direct/indirect bilirubin, and
generic substitutes. Treat \`albumin (urgent)\` and \`total bilirubin (urgent)\` as
separate variants unless a training audit demonstrates defensible
within-assay linkage; never pool raw values across labels. Preserve exact
name and specimen type.

For each index and exact assay, preserve the parent’s exposure construction:
the last eligible numeric pre-index value strictly before \(t_0\), and the
first eligible numeric post-index value satisfying
\(7*24 \le t-t_0 \le 45*24\) hours. Parse only numeric
\`Quantitative Result\`; qualitative/inequality observations stay nonnumeric. Retain
pre/post timestamps, delays, counts, qualitative/inequality flags, assay
name, specimen type, and missingness. Estimate robust scale and category
tolerances from fitting data only. AFP is decrease/non-decrease/uncertain/
unavailable; albumin and bilirubin are non-worsening/worsening/uncertain/
unavailable with frozen standardized directions. No clinical units, ALBI,
MELD, INR, hepatic-reserve, or threshold claim is permitted.

The new schedule vector \(S\), available only through day 45, contains for
each component: exact pre-gap \(t_0-t_{\rm pre}\), exact post-delay
\(t_{\rm post}-t_0\), number of numeric and total assay rows in the post
window, number of encounters carrying that assay, and missing/qualitative/
inequality flags. For transparent strata, post-delay is binned exactly as
[7,14], (14,30], (30,45] days and pre-gap as (0,30], (30,90],
(90,180], >180 days; absent values have a separate unavailable level. Counts
remain numeric. The bins, sparse-cell rule, and common-support thresholds
are learned on fitting data and frozen. No schedule variable uses any
post-day-45 field.

Retain both parent estimands: (a) full-index, with availability indicators,
and (b) paired-observed, restricted to supported component pairs. The repaired
paired analysis additionally restricts to common support in \((Z,S)\), reports
the number removed and the exact overlap rule, and estimates \(\Delta\) above.
No observation weighting is called causal adjustment; if used, it is
training-only predictive standardization with frozen truncation and effective
sample-size/positivity diagnostics.

## Matched baseline and substantive alternative

All methods use the identical cohort, \(t_0\), day-45 risk set, information
boundary, endpoint ladder, temporal split, uncertainty procedure, and locked
test. The comparison tests whether component trajectory information adds
pathway-specific evidence beyond measurement opportunity.

- \(B_0\): regularized discrete-time cause-specific hazards for each recorded
  state using age, sex, index year/department, pre-index diagnosis/procedure
  counts, and prior local contact.
- \(B_{\rm time}\) (new transparent baseline): \(B_0\) plus testing/contact
  intensity, assay availability, exact and binned component delays, assay
  counts, examination/order opportunity, procedure-source mix,
  episode/coding density, and ambiguous-label indicators, but no laboratory
  values or component changes. This is the schedule-only comparator.
- \(B_{\rm time+traj}\): \(B_{\rm time}\) plus the parent’s separate AFP,
  albumin, and bilirubin standardized changes, delays, missingness and
  uncertainty levels.
- \(B_{\rm int}\) (primary transparent test): \(B_{\rm time+traj}\) plus the
  prespecified AFP-by-albumin-by-bilirubin interaction and profile contrasts,
  reporting strict, broad, diagnostic, ambiguous, and non-liver outcomes.
- \(M_{\rm joint}\) (substantive alternative): an irregular-time, multi-output
  state-space model with separate latent AFP, albumin, and total-bilirubin
  states; assay- and specimen-specific observation models; numeric,
  qualitative/inequality and missingness indicators; the exact measurement
  times; a contact/measurement intensity component; and competing transition
  hazards for the same endpoint states. Fit only through day 45. It must
  output latent-state/profile \(\Delta\), full-index availability contrasts,
  CIF, log score, calibration, posterior/cluster uncertainty, convergence,
  overlap, and sensitivity to its observation model.

The transparent baseline shows whether values add information beyond when and
how often they were measured. \(M_{\rm joint}\) can reveal asynchronous,
nonlinear, noisy component evolution and distinguish a latent trajectory from
a first-post measurement artifact; the categorized baseline necessarily loses
that information. The alternative is scientifically substantive because it
tests the measurement-generating process, not because it is more complex or
uses a GPU.

The generic transformer/large sequence model is deferred: the question’s
limiting dependencies are validated assay units, treatment intent, imaging/
response adjudication, death, outside-care linkage, and endpoint semantics,
not representation capacity. A mechanistic ALBI/MELD or reserve model is also
deferred because this design has no validated units and intentionally does not
claim INR or hepatic reserve. Full multimodal cancer-model reproduction is
not possible: HCC has no image files, and the demonstration bundle states that
the cancer main paper and complete STAR Methods were unavailable; only its
accessible supplement was inspected. Revisit these alternatives if those
dependencies become available.

## Split, uncertainty, and falsification plan

Use 2010–2022 for fitting, 2023 for tuning, and 2024 through the cutoff as
locked test when event support permits; otherwise use a deterministic
patient-hash split declared before fitting. No patient crosses splits. Freeze
the assay/procedure vocabulary, episode rules, time bins, robust tolerances,
sparse-cell/overlap rule, endpoint ladder, model tuning, standardization rule,
and bootstrap count before locked evaluation.

Report cause-specific hazards, CIF at 30, 90, and 320 post-landmark days,
absolute \(\Delta\) and \(\Psi\), interaction estimates, calibration, overlap,
log score, and patient-clustered bootstrap or equivalent intervals. Never
row-bootstrap.

The following falsifications are mandatory:

1. Schedule-only: compare \(B_{\rm time}\) with \(B_{\rm int}\). If the
   favorable/discordant contrast and strict-pathway performance are already
   present in \(B_{\rm time}\), the trajectory-specific hypothesis fails.
2. Timestamp permutation: within patient and exact assay variant, use a frozen
   seed to permute eligible post-index value-to-time assignments while
   retaining the value multiset, counts, specimen type and outcome. Rebuild
   first-post phenotypes and \(S\) without changing the endpoint. Repeat in
   fitting/tuning and use a fixed prespecified number of locked permutations.
   Preservation of the original strict contrast supports timing/capture
   artifact; attenuation supports temporal alignment but does not establish
   biology.
3. Specificity: repeat the same estimand for \`Liver_diagnostic\`,
   \`Nonliver_procedure\`, and \`Mixed_ambiguous\`. A similarly large pattern
   across controls is adverse.
4. Placebo: apply the frozen component-window construction to a pre-index
   pseudo-landmark with no post-index outcome leakage, using the parent’s
   pre-index placebo rule. A comparable placebo signal is adverse.
5. Semantic/episode sensitivity: repeat with encounter-only episodes and
   report strict-versus-broad results, assay-variant results, missingness
   states, and ambiguous-label concentration.

Supportive computation requires all of: a favorable strict \(\Delta(320)\)
whose patient-level interval is directionally below zero and excludes the
-0.03 margin in the prespecified direction; nontrivial \(\Psi\) beyond
\(B_{\rm time}\); adequate common support and calibration; persistence in the
full-index availability-aware analysis and after capture controls; weaker
diagnostic/non-liver/placebo and permuted signals; compatible broad-endpoint
direction; and a converged \(M_{\rm joint}\) with compatible profile
contrasts. This supports a robust association with a local recorded pathway
only.

Adverse computation is a null/reversal after schedule standardization,
\(B_{\rm time}\) reproducing the result, similar diagnostic/non-liver/placebo
or timestamp-permuted signals, ambiguous-bundle or single-variant
concentration, episode instability, poor overlap/calibration, or
\(M_{\rm joint}\) nonconvergence/observation-model sensitivity. This favors
measurement, coding, or capture explanations.

Inconclusive computation includes sparse strict events, insufficient paired
support, unstable assay vocabulary, positivity failure, inadequate follow-up,
temporal-split failure, intervals crossing the margin, inability to separate
diagnostic from therapeutic records, or materially incompatible baseline and
joint-model estimates. Null/adverse/inconclusive findings do not establish
absence of biological response.

## Computationally checkable versus clinically unavailable claims

The verifier can check read-only paths and schema IDs, exact headers, two-key
aggregation, episode and boundary rules, no leakage, fitting-only vocabulary
and bins, schedule construction, endpoint exclusivity, CIF/competing-risk
calculations, timestamp permutations, patient-level splits, predictions,
uncertainty, calibration, overlap, and the mapping from every interpretation
statement to an output.

It cannot adjudicate treatment indication, intent, technical completion,
radiologic or pathological response, viable tumor, liver failure, death,
mortality, survival, appropriateness, benefit, utility, care outside this
institution, or external validity. Diagnoses are not timed onset labels.
Labs have no separate units column. Images, validated assay harmonization,
outside-care linkage, death ascertainment, and external validation are
unavailable. Those claims require expert adjudication, linked clinical
outcomes, prospective or external data, or another study.

## Resource budget and required deliverable

Discovery used no model fitting and no GPU. The only measured feasibility
operation in this episode was a read-only header audit of the four files
(completed in under one second); it does not measure model runtime. The
future solver planning envelope is up to 16 CPUs, 262,144 MiB memory, and
28,800 seconds. CPU tabular fitting is expected to fit that envelope but is
unmeasured. \(M_{\rm joint}\) convergence, memory, and runtime are unverified.
An allocated A100-SXM4 80-GB GPU is available in the deployment, but GPU
benefit is unverified and no GPU is required for the transparent analysis;
any GPU probe must be separately allocated through \`job_submit\`, use
\`cuda:0\`, and remain within the approved solver envelope. No discovery
estimate is a promise of full-study completion.

At minimum produce
\`analysis_manifest.json\`, \`index_manifest.csv\`, \`landmark_manifest.csv\`,
\`split_manifest.csv\`, \`procedure_vocabulary_audit.csv\`,
\`procedure_episode_manifest_primary.csv\`,
\`procedure_episode_manifest_24h_sensitivity.csv\`,
\`pathway_specificity_manifest.csv\`, \`lab_vocabulary_audit.csv\`,
\`component_trajectory_manifest.csv\`, \`component_state_manifest.csv\`,
\`observation_schedule_manifest.csv\`, \`observation_state.csv\`,
\`predictions.parquet\`, \`metrics.json\`, \`bootstrap_intervals.json\`,
\`pathway_cif.json\`, \`pathway_calibration.json\`,
\`capture_decomposition.json\`, \`schedule_overlap.json\`,
\`weight_diagnostics.json\`, \`model_parameters.json\`,
\`mstate_checkpoints_or_deferral.json\`, \`timestamp_permutation.json\`,
\`negative_control.json\`, \`interpretation.json\`, and \`limitations.csv\`.

\`interpretation.json\` must map every supportive, adverse, or inconclusive
statement to a computed estimate, interval, model, endpoint, schedule rule,
and frozen criterion. It must prohibit response, intent, causality, survival,
mortality, benefit, utility, and external-validity language. Sources remain
read-only; all manifests and derived analyses are workspace artifacts.
