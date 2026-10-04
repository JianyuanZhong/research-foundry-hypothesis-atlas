> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

TITLE
Cross-hospital and cross-landmark semantic invariance audit of the two exact eICU ventilation care-plan labels

STATUS AND SUBSTANTIVE CHILD CHANGE
This is a substantive child of assessed-valid `[prior hypothesis]` and `[prior hypothesis]`. It preserves both completed results rather than retrying either blocked endpoint. The first parent established that the durable-liberation proxy is not independently validated: independent liberation markers were rare and strict 48-hour observation was incomplete, with large dependence on unobservable discharge bridging. The second completed the fixed `(D,D+720]` chart-association and found no reproducible positive label-to-documented-de-escalation signal: the setting contrast was inverse and peak-pressure dependent, while sedation-rate results were imprecise and hospital-dependent. This child changes the unresolved question from whether there is a single overall association to whether the labels have stable operational meaning across hospitals and landmark decision times.

CLINICAL IMPORTANCE AND EVIDENCE BOUNDARY
Structured care-plan labels are often reused as multicenter quality-measurement phenotypes or decision-support inputs. If the exact same string denotes materially different documentation workflows or management states by hospital or by time since ICU admission, pooling it as one phenotype can create misleading dashboards, transportability failures, and unsafe CDS assumptions. Conversely, a stable relationship to independently charted short-horizon trajectories would justify prospective semantic validation, not clinical deployment.

The strongest claims already supported are narrow and dataset-specific. In this eICU snapshot, the exact labels and fixed decision times can be reconstructed reproducibly; durable liberation cannot be defensibly ascertained; and the completed 12-hour association does not show a general positive label-to-action signal. The unresolved claim tested here is:

> In the frozen 540-person-landmark cohort, do `Ventilated - with daily extubation evaluation` and `Ventilated - with no daily extubation trial` retain a common operational meaning across hospitals and landmark times, as judged by their prevalence, independent chart observability, and relationship to prespecified documented ventilator-setting and infusion-rate trajectories?

The hypothesis is semantic/operational invariance, not treatment efficacy: after applying the same rules, label-specific outcome distributions and label contrasts will be sufficiently similar across hospitals and landmarks that a pooled descriptive phenotype is defensible. The adverse alternative is site- or landmark-specific convention: prevalence, marker ascertainment, component composition, or contrast direction differs enough that a pooled label is not a stable operational construct.

No result may be interpreted as actual SBT delivery, extubation, durable liberation, physiologic readiness, appropriateness, bedside action, causal effect, or patient benefit. A charted numeric change is only a documented proxy. True semantic equivalence requires clinical adjudication and, ideally, prospective bedside/device observations.

FROZEN POPULATION, EXPOSURE, AND TIME DESIGN
Use the exact parent artifact `eicu_strict_cohort.csv`, [source checksum], containing 540 person-landmarks from 443 unique ICU stays/persons: 309 evaluation and 231 no-trial rows. Retain all eligible landmarks in the first qualifying ICU stay per `uniquepid`; do not select one landmark per person and do not add post-D exclusions. Landmarks are L = 1440, 2880, 4320, 5760, and 7200 minutes after ICU admission. The exposure is the first exact `carePlanGeneral.cplitemvalue` in `[L,L+360]` equal to one of the following strings, with D equal to its `carePlanGeneral.cplitemoffset`:

- `Ventilated - with daily extubation evaluation`
- `Ventilated - with no daily extubation trial`

Preserve contradictory same-time exclusion, adult restriction, invasive pre-landmark evidence, no pre-landmark EOL discussion, no prior 24-hour `Spontaneous - adequate`, strict pre-landmark physiology screen, and first qualifying ICU stay rule exactly as in the frozen artifact. Verify one row per `(patientunitstayid, landmark, strategy)` and `D == decision_offset`; any mismatch is a computational failure, not a reason to silently repair the cohort.

PRIMARY TRANSPORTABILITY POPULATION AND SECONDARY POPULATIONS
The primary comparison is restricted before outcome analysis to hospitals 248, 252, and 420, the only hospitals with at least 10 rows under each exact label in the frozen cohort. Their evaluation/no-trial counts are 18/52, 53/96, and 59/25, respectively (303 rows total). This is a limited overlap set, not evidence of generalization to all eICU hospitals. Report all 540 rows as a prespecified secondary descriptive transportability analysis, with hospitals lacking both labels retained for prevalence/availability description but not interpreted as within-hospital contrasts.

Cross-landmark strata are L = 1440, 2880, 4320, 5760, and 7200 separately. Do not merge landmark strata while hiding time-specific missingness. Because repeated landmarks occur within `uniquepid`, use person-clustered uncertainty for descriptive intervals and report the number of distinct persons. Do not use three hospital clusters as if they support population-level hospital inference.

OPERATIONAL MEASURES OF SEMANTIC/OPERATIONAL MEANING
For every hospital-by-label and landmark-by-label cell, report the denominator, label prevalence among eligible target-label observations, number of rows with each outcome available, event rate among available rows, and missingness/availability. The following outcomes are frozen from the completed 12-hour analysis and must not be redefined after seeing stratified results.

1. Ventilator-setting de-escalation. From `respiratoryCharting`, pair a numeric component value strictly before D with a numeric value in `(D,D+720]`. A reduction is FiO2 >= 5 percentage points, PEEP/PEEP-CPAP >= 1, pressure support >= 1, set ventilator rate >= 1, or peak inspiratory pressure >= 1 in the documented units. The primary composite is any paired qualifying reduction. Report component-specific rates and the prespecified no-peak-pressure composite separately; missing paired values are unavailable, never no change.

2. Same-drug sedation/analgesic infusion-rate de-escalation. From `infusionDrug`, match names containing the locked set propofol, fentanyl, midazolam, dexmedetomidine, lorazepam, ketamine, or morphine. Require a numeric same-exact-drug-name rate in `(D-1440,D)` and `(D,D+720]`; reduction is >=10% of baseline or >=0.01 documented rate units. This is conditional on rate documentation and is not a sedation interruption.

3. Available process-field documentation. Report the already-defined `respiratoryCharting` process-field availability only as an ascertainment descriptor, never as proof that a bedside process occurred.

4. Durable-liberation fields. Do not re-estimate the failed durable endpoint. If included for completeness, report the frozen parent’s care-plan-only, independent-first, and union counts and failed coverage/independent-marker gates without calling them semantic validation outcomes.

The primary semantic-invariance object is the vector of label-specific documented-outcome distributions and missingness, not a causal risk ratio. A label contrast is secondary and descriptive. Also report whether the setting composite is dominated by peak pressure within each cell; component dominance itself is a semantic warning signal.

EXACT SOURCE BINDINGS, JOINS, AND TEMPORAL RULES
Snapshot: eICU 2.0 `[source checksum]`; catalog [source checksum]. Sources are read-only ordinary gzip CSV files under `[internal dataset path]`; archive member is `ordinary file`.

- `patient.csv.gz`, table `patient`: join on `patientunitstayid`; use `uniquepid`, `hospitalid`, `unitvisitnumber`, `unitdischargeoffset`, `unitdischargestatus`, and `unitdischargelocation` for cohort verification, hospital grouping, and truncation description. Schema is `[internal dataset path]`.
- `hospital.csv.gz`, table `hospital`: join `hospitalid` to report `numbedscategory`, `teachingstatus`, and `region` only as descriptive site descriptors; do not adjust away hospital or claim these fields establish semantic equivalence. Schema `[internal dataset path]` (the dataset-local equivalent is also available).
- `carePlanGeneral.csv.gz`, table `carePlanGeneral`: use `patientunitstayid`, `cplitemoffset`, `cplgroup`, and `cplitemvalue` for exact labels, D, prior spontaneous exclusion, and descriptive post-D care-plan marker availability. Schema `[internal dataset path]`.
- `respiratoryCharting.csv.gz`, table `respiratoryCharting`: use `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respchartvaluelabel`, and `respchartvalue`; apply strict offset windows above and use the same numeric parsing/component mapping as the completed analysis. Schema `[internal dataset path]`.
- `infusionDrug.csv.gz`, table `infusionDrug`: use `patientunitstayid`, `infusionoffset`, `drugname`, `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, and `patientweight`; use `infusionoffset` for all windows. Schema `[internal dataset path]`.
- `respiratoryCare.csv.gz`, table `respiratoryCare`: use `patientunitstayid`, `respcarestatusoffset`, `airwaytype`, ventilator setting/alarm fields, `ventstartoffset`, and `ventendoffset` only for the frozen pre-landmark invasive screen, recurrence audit, and documentation coverage; `ventendoffset` alone is never liberation evidence. Schema `[internal dataset path]`.
- `treatment.csv.gz`, table `treatment`: use `patientunitstayid`, `treatmentoffset`, and `treatmentstring` only for the frozen independent marker/recurrence audit; exact ETT-removal strings do not establish true extubation. Schema `[internal dataset path]`.

For all joins, retain only cohort `patientunitstayid` keys; never join on deidentified patient names or text. Use `respchartoffset` (not entry time) for clinical ordering, with `respchartentryoffset` retained for a timing diagnostic if available. Use half-open/closed windows exactly: pre-D `offset < D`; post-D `D < offset <= D+720`; pre-D trajectory `(D-1440,D-720]` versus `(D-720,D]`. Do not use post-D outcomes in cohort construction or covariate adjustment.

ANALYSIS PLAN
First reproduce and hash-check the 540-row cohort and the completed 12-hour action artifact. Then perform a full-source, no-row-sampling scan of the bound tables, recording source row counts, SHA-256 values, target-label counts, and derived artifact hashes. Construct a long table by hospital, landmark, label, outcome, and component with denominators, available counts, events, rates, and missingness.

For each outcome and each label, quantify heterogeneity of event rates and ascertainment across hospitals and landmarks. Use exact binomial or Wilson intervals for cells and person-clustered bootstrap intervals for pooled descriptive contrasts where feasible. Fit only descriptive interaction models if cell counts permit: linear-probability models for documented event indicators with label, hospital, landmark, and label-by-hospital and label-by-landmark interactions, using pre-D variables only for optional sensitivity adjustment. Report interaction estimates and uncertainty; no causal interpretation and no hospital-level random-effects generalization with only three overlap hospitals. If sparse cells make interactions unstable, report cell tables and leave-one-hospital-out contrasts rather than force a model.

Primary invariance summaries are prespecified before inspecting stratified outputs:
(a) absolute range of label-specific event rates across overlap hospitals and landmarks;
(b) range of label availability rates;
(c) fraction of overlap hospitals and landmark strata with the same direction of evaluation-minus-no-trial contrast;
(d) peak-pressure share of setting-composite events by cell;
(e) leave-one-hospital-out pooled contrast range.
These are descriptive diagnostics, not universal clinical thresholds.

FROZEN FALSIFICATION GATES AND INTERPRETATION
Supportive pattern (operational invariance) requires all of the following in the primary overlap analysis: balanced outcome availability (absolute label difference <=10 percentage points for the setting outcome and report, but do not silently pass, any larger sedation difference); no hospital or landmark stratum with a sign reversal for the primary setting contrast unless its interval is wholly uninformative; setting direction remains materially similar after removing peak pressure; peak-pressure share does not account for nearly all events in only one label/site pattern; and leave-one-hospital-out contrasts remain directionally compatible with the pooled descriptive result. Even if this pattern occurs, it supports only a candidate common documentation phenotype requiring prospective validation.

Adverse/non-invariance evidence is any prespecified major failure: opposite label-contrast directions across overlap hospitals or landmarks with informative cell counts; a large availability difference or site-specific missingness that can explain the contrast; materially altered or reversed setting contrast after removing peak pressure; nearly all events concentrated in one component, hospital, or landmark; or leave-one-hospital-out reversal. This would support treating the strings as site/time-specific documentation conventions unsuitable for pooled quality measurement or CDS without local calibration.

Inconclusive evidence occurs when fewer than three overlap hospitals or fewer than two adequately populated landmark strata remain, when event or availability cells are too sparse for informative intervals, or when source semantics/numeric units cannot be verified. Inconclusive does not support either invariance or non-invariance. The prior durable-liberation failure remains adverse for that endpoint regardless of this audit, and the completed 12-hour result remains adverse/inconclusive rather than a positive operational validation.

EXPECTED EVIDENCE AND CURRENT RESULTS
Existing full-source artifacts already show limited overlap (only hospitals 248, 252, and 420 meet the minimum 10-per-label rule), balanced setting ascertainment in those hospitals, an inverse setting contrast in all three hospitals, peak-pressure dependence, and sedation-rate heterogeneity with hospital-specific reversals. These findings motivate the child and predict an adverse or inconclusive semantic-invariance result; they are not replaced by the proposed stratified audit and must be reported as prior evidence. No new positive claim is made without computing the frozen strata and leave-one-hospital-out summaries.

REQUIRED CLINICAL ADJUDICATION AND ADDITIONAL DATA
The available tables cannot determine whether labels represented an actual standardized protocol, an SBT, bedside readiness, a delivered ventilator change, a true extubation, or a clinically appropriate decision. Peak inspiratory pressure semantics, ventilator-setting units, infusion-rate units, and local documentation workflows need site-level clinical review. A meaningful validation study would require prospective clinician adjudication of label intent and SBT/ventilator actions, device/waveform data, standardized setting and drug units, explicit sedation interruption records, true extubation/reintubation outcomes including after ICU discharge, and a broader multicenter sample with within-hospital overlap.

COMPUTATIONALLY CHECKABLE CLAIMS
A verifier can check snapshot/source hashes, full-scan row counts, cohort hash and 540 rows, exact strings, all joins and D equality, landmark and offset windows, component thresholds, missing-as-unavailable handling, hospital/landmark cell tables, interaction and leave-one-hospital-out calculations, gate flags, and whether the narrative follows supportive, adverse, or inconclusive outputs. It cannot establish clinical semantic equivalence, bedside delivery, SBT performance, appropriateness, true extubation, causal benefit, or safety; those require adjudication or another study.

SUPPORTING ARTIFACTS
The frozen cohort is support `[source checksum]`. The completed durable audit JSON is `[source checksum]` with code `[source checksum]`. The completed 12-hour joined rows are `[source checksum]`, results are `[source checksum]`, and code is `[source checksum]`. The current workspace source scan records exact source headers, hashes, and a full 3,115,018-row carePlanGeneral scan at `[internal dataset path]`.
