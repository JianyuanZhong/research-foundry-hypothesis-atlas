# Is hospital variation in strict post-rise renal-support documentation source-concordant?

## Scientific deliverable and substantive advance

The future solver must newly construct an auditable eICU six-hour first-rise cohort and a 30-minute post-rise event ledger, then fit two matched process models. The primary deliverable is the development-hospital 90th-minus-10th percentile spread in the standardized 48-hour cumulative incidence of a first strict, newly documented renal-support record after a recorded creatinine rise, among stays with no strict support record from ICU minute 0 through the rise.

This crossover preserves the clinically consequential endpoint of the top parent while making its validity dependent on cross-source evidence. Treatment records and intake/output flowsheets are not assumed to be independent or complete, and neither is a gold standard. A union result is called source-robust only if treatment-only and intake/output-only patterns, source ordering, and an auditable corroboration process support the same hospital-level signal. A union-only signal is explicitly classified as documentation/ascertainment heterogeneity or inconclusive—not as proof of a hospital difference in renal-care delivery.

Completion requires: frozen source dictionaries and raw-string audit; cohort flow and no-prior-support audit; one row-level event ledger; primary and source-specific standardized CIFs and spreads; first-source order and 60-minute corroboration outputs; nested surveillance/process decomposition; matched transparent and ordered-model estimates; 500 hospital-cluster bootstrap uncertainty; held-out-hospital transport; and all prespecified sensitivity and falsification results. Discovery has fitted none of these quantities and claims no clinical result.

## Evidence-supported claim and unresolved hypothesis

The inspected local evidence supports availability and timing semantics only. The frozen eICU snapshot contains ICU-relative MAP, laboratory, treatment, intake/output, patient-unit disposition, hospital, infusion, and admission-severity fields. The parent feasibility scan recorded renal/dialysis-related rows in the large treatment and intake/output sources, but those whole-source counts are not index-cohort event rates and do not establish prevalence, treatment receipt, renal replacement initiation, or hospital association.

The strongest supported claim is therefore:

> The snapshot can measure a first recorded creatinine rise and later high-specificity renal-support documentation through two differently captured source channels, with ICU-relative timing and competing unit exits, provided that source semantics and prior-support exclusions are audited.

The unresolved claim is:

> Among adult ICU-unit stays with a first recorded creatinine rise after the six-hour MAP landmark and no earlier strict support record, hospital variation in newly documented strict renal-support records remains materially heterogeneous after measured clinical-risk, early surveillance, source-capture, and competing-exit adjustment, and the direction is concordant across treatment and intake/output sources.

The primary hypothesis is frozen as follows. If at least 10 hospitals meet the prespecified support gate, the adjusted union spread H_E_surv is at least 5 percentage points, its two-sided hospital-cluster interval excludes zero, at least half of the estimable raw spread remains, both source-specific adjusted spreads are positive and directionally concordant on their supported-hospital intersection, their difference is within a 5-point equivalence band, and the qualitative result transports to held-out hospitals. The five-point margin is a study-scale comparability margin, not a treatment threshold.

A null adjusted spread, reversal between sources, source difference outside the equivalence band, corroboration that disappears under timing sensitivity, or loss of direction in held-out hospitals is adverse to source-concordance. Sparse source events, fewer than 10 supported hospitals, failed convergence, non-overlap, or failed transport make the result inconclusive rather than negative.

## Population and ICU-unit temporal boundary

Use eICU snapshot `[source checksum]`. The unit is one `patientunitstayid`; repeated ICU/unit stays remain separate. `uniquepid` is used only for a clustering sensitivity and for a connected-component split audit, never to concatenate stays.

Include a stay when all conditions hold:

1. `patient.age` is adult (parse `> 89` as 90 and retain an age-censored indicator);
2. there are at least two finite raw `vitalPeriodic.systemicmean` observations in minutes 0–360, each restricted to 20–200 mmHg;
3. a qualifying baseline creatinine is available at or before the first raw low MAP;
4. the first raw periodic `systemicmean < 65` occurs in minutes 0–360;
5. no qualifying baseline-plus-0.3-mg/dL creatinine rise occurs through minute 360; and
6. `patient.unitdischargeoffset > 360`.

The first qualifying rise must occur after minute 360. Let r be its raw `labresultoffset`, U=`unitdischargeoffset`, and E=min(r+2880,U). Source observations are eligible only when their primary event clock is after r and before U; an event exactly at r+2880 is eligible only when U>r+2880. If U<=r+2880, unit exit precedes an event at the same minute. The observation boundary is the ICU/unit stay: no substitution of hospital-discharge time, and transfer to another unit, floor, hospital, or location ends this index observation.

At U, `unitdischargestatus=Expired` is a recorded unit-death competing event and `Alive` is an alive unit exit. A missing/NULL status is unknown-status administrative censoring, never recoded as alive. `unitdischargelocation` is retained for audit; a missing-status/death-location sensitivity is descriptive. The analysis does not infer hospital mortality.

## First rise, baseline covariates, and no leakage

### Creatinine

From `lab`, retain case-folded `labname=creatinine`, finite numeric `labresult` in [0,60], and nonblank normalized `labmeasurenamesystem` and `labmeasurenameinterface` that both equal mg/dL. Exclude conflicting units, blank-unit rows, non-mg/dL rows, and invalid values; do not convert an unverified mmol/L row. A sensitivity permits one explicit mg/dL field when the other is blank. Deduplicate exact `labid`; at one stay and result offset, use the median of remaining valid rows and retain row counts.

The baseline is the earliest qualifying result in minutes 0–60, using the smallest `labresultoffset`, not the minimum value. The first rise is the earliest qualifying result after minute 360 at least 0.3 mg/dL above that baseline. The early-rise exclusion uses every qualifying result through minute 360, including results after the first low MAP. Same-`labid` revisions cannot create a distinct confirmation.

A secondary confirmation endpoint is the first distinct `labid` at least 360 minutes after r, with value at least baseline+0.3 mg/dL and within E. Its primary clock is `labresultoffset`; rerun with `labresultrevisedoffset` as a timing sensitivity. Confirmation is an observation process and is never substituted for the primary support endpoint.

### MAP and documented pressor context

The primary MAP ledger uses raw `vitalPeriodic` rows, deduplicated by `vitalperiodicid`, with `observationoffset` and `systemicmean`. First-low time uses the raw observation. Report minimum MAP, coverage, low-MAP runs, raw low minutes and a trapezoidal burden of max(65-MAP,0), bridging only gaps <=30 minutes; no-bridging is a sensitivity. `vitalAperiodic.noninvasivemean` with `observationoffset` is a separate sensitivity, never pooled with periodic MAP.

From `infusionDrug`, use the first raw `infusionoffset` in minutes 0–360 whose case-folded `drugname` matches a frozen list of norepinephrine, vasopressin, phenylephrine, dopamine, or epinephrine. Categorize it as pre-low/concurrent, prompt-after-low (through 30 minutes), delayed-after-low, or none. Retain `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, and `patientweight) only as audit/context. These are documented rows, not validated administration, start, dose, indication, intent, or complete exposure; no pressor effect is estimated.

All predictors, surveillance scores, source dictionaries, splits, and standardization distributions use information at or before r. No post-rise support, confirmation, competing exit, or outcome may enter a predictor or hospital score.

## Exact strict source definitions and primary corroboration rule

Freeze the dictionaries and print every retained and excluded observed string/label before fitting.

Treatment source T is a case-folded normalized `treatment.treatmentstring` match to explicit high-specificity renal-support terms: renal dialysis, hemodialysis, CVVHD, CVVH, CAVHD, peritoneal dialysis, SLED, hemofiltration, or an equivalent explicit renal modality string. Exclude catheter insertion/access surgery, line/flush language, generic renal terms, and ultrafiltration described only as fluid removal. Deduplicate exact `treatmentid`; the event clock is `treatmentoffset`. `activeupondischarge` is an audit field only and cannot establish initiation or receipt.

Intake/output source IO uses only the exact case-insensitive `intakeOutput.cellpath` or `celllabel` values `Dialysis (ml)|In`, `Dialysis (ml)|Out`, `CRRT Actual Pt Fluid Removed`, `CRRT Out`, `CRRT - UF removed`, `CRRT- UF removed`, or `Hemofiltration`, and requires a finite nonzero `cellvaluenumeric` or finite nonzero `dialysistotal`. An unlabeled `dialysistotal` row alone is not sufficient. `cellvaluetext` is audit context. Deduplicate exact `intakeoutputid`; the primary event clock is `intakeoutputoffset`, with `intakeoutputentryoffset` used only in a sensitivity. Later entry cannot backdate an event.

The primary endpoint is the first post-rise strict union event T OR IO within E, after removing every strict T/IO event from minute 0 through r. This is “newly documented support,” not new AKI, renal-replacement initiation, or treatment receipt. Prior-support stays are retained as a separate continuation/previously-observed-support analysis and are not silently pooled into the primary cohort. Fluid-removal-only terms are added only in a broad sensitivity.

The primary corroboration rule is an auditable process output, not a hidden gold-standard assumption: a union event is corroborated when the other source has its first eligible strict event in the same `patientunitstayid` within 60 minutes of the first source event, while remaining inside (r,E] and before U. The second source is not backdated. Store raw offsets, source IDs, source strings/labels, first-source direction (T-first, IO-first, or same-minute tie), and waiting time. Report the first union event and the first corroborated union event separately. Re-run corroboration at 30 and 120 minutes; also report union events that never corroborate. A same-minute T and IO event is a tie, not an ordered sequence.

Required source-specific sensitivities are treatment-only T, IO-only IO, union T+IO, corroborated-union at 30/60/120 minutes, conservative nonblank-valid-value rules, broad fluid-removal inclusion, and entry/revised-offset clocks. Generic urine, catheter, Foley, voided-amount, and occurrence labels remain an observation-process audit only; the catalog lacks a uniformly valid collection interval and denominator, so no KDIGO urine criterion or oliguria claim is made.

## Surveillance/process adjustment and estimands

Construct the primary risk set after the no-prior-support gate. Construct leave-one-stay-out hospital source-surveillance scores from all otherwise eligible first-rise reference stays before applying that gate, using only strict T and IO rows through each stay’s own r:

- S_T(h,-i): pre-rise T documentation proportion;
- S_IO(h,-i): pre-rise IO documentation proportion; and
- S_U(h,-i): pre-rise union documentation proportion.

Freeze dictionaries, denominators, numerators, empirical-logit shrinkage constant, and missing-score rule before fitting. Exclude stay i from its own hospital score. Report score numerators/denominators, overlap, zero/one hospitals, and unsupported hospitals. These scores represent observed documentation regimes, not patient need or causal adjustment.

At r, retain age/age-censored flag, gender, ethnicity, unit/hospital admission source, `unittype`, `unitstaytype`, baseline creatinine, first-rise value and delta, time since baseline/previous qualifying test, pre-rise creatinine-test count, MAP minimum/burden/coverage/runs/recovery, documented pressor category, and admission severity. Join hospital context `numbedscategory`, `teachingstatus`, and `region`; do not standardize by hospital identity. Admission severity is drawn from `apachePatientResult` (`acutephysiologyscore`, `apachescore`, `predictedicumortality`) and `apacheApsVar` only as admission/context (`dialysis`, `creatinine`, `meanbp`), never as a post-rise outcome.

For development hospital h, estimate q_E(h), the standardized 48-hour CIF of first strict union support after r, with recorded unit death and alive unit exit competing and unknown-status exit censored. Also estimate q_T(h), q_IO(h), corroborated-union CIF, support-before/after confirmation, confirmation, repeat-test opportunity, and the parent composite (confirmation OR strict support). Standardize to the development primary-risk-set distribution. Define H_X_raw and H_X_surv as the supported-hospital 90th-minus-10th percentile spreads for each X.

A hospital is supported for the primary union spread only with at least 50 primary risk-set stays and at least 10 union events; at least 10 such hospitals are required. Source-specific and corroboration claims use the intersection of hospitals meeting the same stay/event gate for the relevant source. Do not lower a gate to rescue concordance. If source events or the intersection are sparse, report descriptive results only.

## Matched transparent baseline

Fit regularized cause-specific pooled-logistic competing-risk models on identical 30-minute intervals, cohort, raw ledger, dictionaries, covariates, split, standardization distribution, exits, and bootstrap procedure. Parallel causes are T-only, IO-only, union support, corroborated union, distinct confirmation, repeat opportunity, recorded unit death, alive unit exit, and unknown-status censoring. Use prespecified elapsed-time linear/spline terms, common clinical slopes, source-specific hospital random intercepts, and one selected pre-rise source-surveillance score plus its prespecified source interaction.

Nested baseline fits are:

- B0: clinical covariates and elapsed time;
- B1: B0 plus hospital effects, yielding raw source/union spreads;
- B2: B1 plus patient-level pre-rise testing opportunity;
- B3: B2 plus the frozen leave-one-stay-out source score and interaction;
- B4: B3 without hospital-by-time slopes;
- B5: B3 using the standardized rather than local surveillance score.

Derive standardized CIFs, spreads, attenuation, source differences, corroboration, observed-versus-predicted curves, calibration, and Brier scores. This model is selected for transparent auditability, but its parallel causes lose source order, waiting time, and the mechanism by which repeat testing, source capture, or exits produce the observed spread.

## Substantive ordered-process alternative

Fit a piecewise-exponential ordered multi-state model on exactly the same 30-minute intervals, cohort, raw timestamps, covariates, split, support gates, standardization distribution, and 500-replicate uncertainty procedure.

Represent the ordered states and transitions:

- first rise -> repeat-test opportunity -> distinct confirmed rise;
- first rise -> T-only, IO-only, or same-time union support;
- T-first or IO-first support -> other-source corroboration within 60 minutes;
- every non-exit state -> recorded unit death or alive unit exit; and
- unknown-status unit exit -> censoring.

Keep first-rise-to-repeat, repeat-to-confirmation, post-rise-to-support, source-first direction, support-to-corroboration waiting time, and competing-exit timing distinct. Use transition-specific shrunken hospital effects and the same surveillance covariates. The alternative can show whether residual hospital variation is carried by testing opportunity, T capture, IO capture, corroboration failure, confirmation order, or exit selection—information the additive baseline loses. Agreement in adjusted union and source-specific spreads is robustness; disagreement is model uncertainty and must be reported, not selected away.

## Hospital-held-out transport and uncertainty

Assign hospitals to development (80%) and held-out transport (20%) before cohort summaries, score thresholds, missingness handling, fitting, or standardization using the frozen rule SHA256(`eicu-crosssource-v1|` + hospitalid), first eight hexadecimal digits modulo 10 < 8. Keep every `uniquepid` connected hospital component together; report any coverage loss. Use SHA256(`eicu-crosssource-v1-alt|` + hospitalid) as a prespecified split sensitivity. This study-defined split is not the catalog’s reserved participant partition and is not external validation.

Fit and standardize only in development hospitals. Apply frozen coefficients, dictionaries, score rules, cutpoints, gates, and support definitions to held-out hospitals; do not tune or recalibrate on held-out outcomes. Set unobserved held-out hospital effects to the prespecified population mean. Report held-out observed-versus-predicted CIFs for union/T/IO/corroboration/confirmation/repeat/death/alive exit, calibration, Brier score, event counts, overlap, timing and process discrepancies. Transport is inconclusive with fewer than 10 held-out hospitals, sparse events, inadequate overlap, extreme weights, failed convergence, or calibration failure.

Use 500 hospital-cluster bootstrap replicates for spreads, attenuation, source differences, corroboration, hospital-rank correlation, model differences and transport summaries. Add a `uniquepid`-clustered sensitivity. Preserve cohort, dictionary, ledger, score, fit and bootstrap checkpoints. Report missingness, effective sample size, supported hospitals, shrinkage, overlap and convergence.

## Falsification and interpretation

Falsification is prespecified at the level of the scientific claim:

- Source discordance: one source spread is null/reversed, the source-spread difference leaves [-5,+5] percentage points, source rank correlation is below 0.50, or the union is dominated by one source (>80% of events).
- Corroboration/process discordance: T-first versus IO-first ordering is unstable, or 60-minute corroboration materially changes at 30/120 minutes; union events rarely corroborate despite an apparently large spread.
- Surveillance falsification: adjustment eliminates the spread, source-score overlap fails, or the conclusion changes materially after adding patient-level testing opportunity.
- Temporal falsification: the qualitative result changes under revised-lab timing, 3-hour/12-hour confirmation gaps, no-bridging MAP, or alternative event-at-discharge handling.
- Measurement falsification: periodic versus aperiodic MAP, strict versus broad fluid-removal definitions, or NULL-status handling reverses direction.
- Transport falsification: development fit is not calibrated or process ordering fails in held-out hospitals.

Supportive evidence requires all of these: H_E_surv >=5 points with a two-sided hospital-cluster interval excluding zero and >=50% of H_E_raw remaining; positive same-direction H_T_surv and H_IO_surv on their supported intersection when estimable; the joint interval for H_T_surv-H_IO_surv contained in [-5,+5] and bootstrap median rank correlation >=0.50; no explanation by testing opportunity, one-source capture, corroboration failure, or recorded exit; and a qualitatively concordant held-out result.

Adverse evidence is a supported but null/reversed adjusted union spread, source discordance, large attenuation to below the margin after surveillance adjustment, unstable corroboration, or failed transport. This is evidence against robust cross-source hospital heterogeneity, not evidence that biological renal injury, treatment need, or care quality is absent.

Inconclusive evidence includes fewer than 10 supported hospitals, source/intersection event sparsity, fewer than 10 events in a required source analysis, unstable bootstrap, near-collinearity, non-overlap, extreme weights, semantic dictionary instability, failed convergence, dependence on NULL handling, or held-out failure. If the union is estimable but source validation is sparse, the report must say “adjusted union heterogeneity with source validation inconclusive.”

Computationally checkable claims include source and schema hashes, exact headers/dictionaries, joins, deduplication, unit checks, offsets, boundary rules, cohort flow, no-prior-support gate, pre-rise-only score audit, split integrity, ledger states, fitted parameters, CIFs, concordance, bootstrap intervals, calibration, transport and sensitivity reproducibility. Clinical adjudication or another study is required for biological AKI, renal replacement initiation, actual administration/receipt, dose/intent/indication, chronic dialysis before ICU, urine denominators, completeness of source absence, appropriateness of care, hospital quality, causal effects, treatment thresholds, and policy decisions.

## Exact source bindings, schemas, joins, times, and archive members

The full catalog is `[internal dataset path]`, [source checksum]. The local eICU guide reports 31 source files/tables. Every source below is a read-only gzip ordinary file with archive member `ordinary file`; there is no nested member to select. Snapshot SHA is `[source checksum]`.

- **patient** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-ab037c09d7df9a3c.json`, SHA `[source checksum]`; join `patientunitstayid`; fields `age`, `gender`, `ethnicity`, `hospitalid`, `unitadmitsource`, `hospitaladmitsource`, `unittype`, `unitstaytype`, `unitdischargeoffset`, `unitdischargestatus`, `unitdischargelocation`, `uniquepid`.
- **vitalPeriodic** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-a22c6d6981a32279.json`, SHA `[source checksum]`; join `patientunitstayid`; time `observationoffset`; MAP `systemicmean`; identity `vitalperiodicid`.
- **vitalAperiodic sensitivity** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-72ace5b89971196b.json`, SHA `[source checksum]`; join `patientunitstayid`; time `observationoffset`; MAP sensitivity `noninvasivemean`; identity `vitalaperiodicid`.
- **lab** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-79bdb33275339b1a.json`, SHA `[source checksum]`; join `patientunitstayid`; clocks `labresultoffset`, sensitivity `labresultrevisedoffset`; fields `labid`, `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`, `labmeasurenameinterface`.
- **treatment** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-5461361964176606.json`, SHA `[source checksum]`; join `patientunitstayid`; time `treatmentoffset`; fields `treatmentid`, `treatmentstring`, `activeupondischarge`.
- **intakeOutput** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-ebba5dc91b1d37e7.json`, SHA `[source checksum]`; join `patientunitstayid`; clocks `intakeoutputoffset`, `intakeoutputentryoffset`; fields `intakeoutputid`, `dialysistotal`, `cellpath`, `celllabel`, `cellvaluenumeric`, `cellvaluetext`.
- **infusionDrug** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-18e1a8caaa91eb44.json`, SHA `[source checksum]`; join `patientunitstayid`; time `infusionoffset`; fields `infusiondrugid`, `drugname`, `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, `patientweight`.
- **apacheApsVar** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-67711a86e012835e.json`, SHA `[source checksum]`; join `patientunitstayid`; admission/context fields `dialysis`, `creatinine`, `meanbp).
- **apachePatientResult** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-754bebf64d3d9909.json`, SHA `[source checksum]`; join `patientunitstayid`; admission fields `acutephysiologyscore`, `apachescore`, `predictedicumortality`; actual outcome fields are forbidden predictors.
- **hospital** — `[internal dataset path]`; source SHA `[source checksum]`; schema `datasets/eicu/table-811df7b2ef435e12.json`, SHA `[source checksum]`; join `hospitalid`; fields `numbedscategory`, `teachingstatus`, `region`.

The remaining 21 catalog tables remain accessible read-only but are not silently substituted for missing clinical adjudication, complete treatment administration/intent, validated urine intervals/denominators, or external outcomes. No archive member beyond the ordinary gzip file is applicable. The local headers were inspected for all named sources and agree with these bindings.

## Method choice, deferred alternatives, and resources

The transparent baseline is selected because the primary question is an auditable hospital spread with competing exits and source-specific decomposition; its coefficients, CIFs, attenuation and calibration can be inspected directly. The ordered multi-state alternative is selected because the substantive uncertainty is process order—testing, confirmation, support capture, corroboration, and exit—which a parallel baseline loses. Both methods use identical source rows, cohort, time grid, covariates, split, estimand, gates, standardization and bootstrap.

A learned longitudinal/sequence model is deferred, not banned. Its exact nonlinear contribution, event support, fitting time, calibration and GPU requirement are unverified. Revisit only if both prespecified models show reproducible shape-specific held-out miscalibration or omitted temporal structure in this same source-decomposed support estimand, source event support is adequate, and the learned model can retain the strict gate, no-leakage score, source order, calibration and uncertainty. If revisited, inputs are the same 30-minute source/event sequences; target is next-state hazard/CIF, with hospital-held-out split, calibration/Brier and clustered bootstrap, and a CPU/GPU profile before allocation. It is not selected now because a more complex predictor is not needed to resolve the current source-concordance uncertainty.

A urine/KDIGO branch is deferred until collection duration and a valid time-varying denominator are validated. A causal pressor branch is deferred because `infusionDrug` has timing/name and dose-like fields but not validated administration, indication, intent, or complete exposure. Biological-AKI and dialysis-initiation endpoints are deferred until clinician adjudication and external validation exist. These are evidence-bound deferrals, not blanket method restrictions.

Measured discovery work: the local source/header and schema inspection completed within seconds; parent read-only scans of large treatment/intakeOutput files took approximately 1–2 minutes each and were feasibility counts only. Unmeasured: full ledger construction, both fits, bootstrap, transport, convergence, and event support in the index cohort. The future solver planning envelope from `inputs.json` is 16 CPU, 262144 MiB memory, up to 8 allocated A100-SXM4 80-GB GPUs, and 28,800 seconds; `science_seconds=7200` is the separate discovery budget. CPU-first is appropriate for the two tabular models and 500 clustered bootstraps; no GPU is required unless a bounded profiling job changes that estimate. No discovery result is being presented as a fitted clinical finding.

## Evidence boundaries and references

I inspected `datasets/README.md`, the eICU guide and relevant source headers, `references/research-ambition/README.md`, and `references/research-ambition/methods-and-compute.md`. Those demonstrations establish standards for dated structured histories, process-aware alternatives and honest adaptation; they do not provide evidence for this renal hypothesis. The local README states that the cancer demonstration’s main article and full STAR Methods remain unavailable; neither is claimed as read. Public guidance and any future clinical interpretation cannot replace adjudication of actual AKI, support initiation, or care quality.
