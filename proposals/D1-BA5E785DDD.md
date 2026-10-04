> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Does laboratory surveillance add a monitoring signal after physiologic state is measured?

Status: Episode-18 substantive child of `[prior hypothesis]`. This is an observational prognostic, transportability, and measurement-process study. It is not a causal test-ordering study, a hospital-quality ranking, a treatment-effect study, or evidence that an alert improves survival.

## Real weakness repaired and clinical question

The parent establishes a supported six-hour landmark, a recorded-death competing-risk outcome, whole-hospital transport, alert-burden diagnostics, state-matched process permutation, site descriptors, and outcome-free within-hospital percentile normalization. A remaining scientific weakness is that its baseline state is almost entirely the same laboratory panel whose observation process is being tested. A laboratory count can therefore appear to be a patient-level monitoring signal because the baseline omitted physiologic instability that prompted both vital monitoring and laboratory measurement.

This child preserves the parent’s primary strict raw-process comparison, but adds a prespecified physiologic-state challenge:

> After adjustment for pre-landmark vital physiology and laboratory state, does patient-level laboratory observation timing/intensity still improve zero-shot held-out-hospital calibration and a prespecified enhanced-laboratory-monitoring review decision for recorded ICU death by 1,800 minutes?

The process signal will be interpreted narrowly. Persistence after physiologic adjustment, state-risk-matched permutation, and outcome-free target-hospital normalization supports a patient-linked surveillance association beyond the measured state. Disappearance after physiologic adjustment supports the simpler explanation that the earlier process increment was residual severity or general monitoring intensity. Persistence only in raw absolute counts, or a gain matched by vital-observation intensity or site descriptors, supports workflow dependence. None of these patterns identifies clinician intent or a causal benefit from ordering tests.

The strongest claim supported before this study is only that the frozen eICU snapshot contains enough first-stay, revision-timed laboratory, hospital, and recorded-disposition structure to test a transportable association. The unresolved claim is the state-adjusted patient-level interpretation above. No fitted result is asserted.

## Scientific deliverable

The future solver must newly produce:

1. A frozen first-stay cohort, outcome-blind laboratory codebook, vital-field codebook, revision audit, and five whole-hospital folds.
2. The parent’s legacy B0/B1 analysis, so the original lab-only increment remains auditable.
3. A physiologic-state baseline Bv and matched state-plus-lab-process model BvP, with vital coverage, missingness, and support reported before outcome interpretation.
4. A matched vital-observation-process diagnostic, BvV, and the relative-process version BvP-rel using only outcome-free target-hospital calibration data.
5. Held-out hospital predictions for recorded-death and alive-discharge competing risks; paired calibration, integrated competing-risk Brier, and uncertainty.
6. Reclassification and hypothetical net benefit at q in {0.01, 0.02, 0.05, 0.10}, including the number of episodes whose monitoring-review status changes when lab process is added to Bv.
7. State-matched process permutations, vital-process comparisons, common-panel and strict-revision sensitivities, and an interpretation trace linking every claim to computed outputs.
8. If support and convergence pass, a temporal learner using the same state/process inputs and folds, with ablations for temporal order, lab process, and vital process.

Completion is a fitted, uncertainty-bearing state-adjustment and transport experiment with its falsification outputs. Confirmation of the hypothesis is not the completion criterion.

## Population, landmark, and outcome

Use eICU snapshot `[source checksum].`

Include the first adult ICU stay per person:

- patient.age >= 18, recoding values >89 to 90;
- numeric patient.unitdischargeoffset >360;
- smallest valid numeric patient.unitvisitnumber within patient.uniquepid, breaking ties by patientunitstayid;
- only stays reaching minute 360.

The predictor window is ICU-relative [0,360] minutes. No result, revision, vital observation, or derived feature with a relevant time after minute 360 enters a primary predictor. The outcome window is (360,1800] minutes.

The primary event is patient.unitdischargestatus normalized exactly to Expired with patient.unitdischargeoffset in (360,1800]. Alive ICU discharge before 1,800 is a competing event. An ICU stay present at 1,800 without recorded death is administratively censored at the horizon. Death after alive ICU discharge, hospital mortality, and latent or unrecorded death are outside the estimand.

For the secondary monitoring-review decision diagnostic, recorded death by 1,800 is the label-relative event and alive discharge before 1,800 is a non-event in the net-benefit formula. This does not replace the competing-risk estimand and is not a clinical utility estimate.

## Exact eICU bindings

All source files are read-only. Each is an ordinary `.csv.gz` file with archive member “ordinary file”; no nested archive member is selected. The source directory is:

`[internal dataset path]`

The complete catalog is `datasets/eicu/README.md` and `datasets/eicu/metadata.json`.

- **patient table / patient.csv.gz**, schema `datasets/eicu/table-ab037c09d7df9a3c.json`, [source checksum]. Join key patientunitstayid; first-stay key uniquepid; hospital key hospitalid. Use age, unitvisitnumber, unitdischargeoffset, unitdischargestatus, hospitaladmitoffset, hospitaladmitsource, admissionweight, gender, ethnicity, and unitstaytype. Offsets are ICU-relative minutes; hospitaladmitoffset is context only.

- **lab table / lab.csv.gz**, schema `datasets/eicu/table-79bdb33275339b1a.json`, [source checksum]. Join lab.patientunitstayid = patient.patientunitstayid. Required fields are labid, labresultoffset, labtypeid, labname, labresult, labresulttext, labmeasurenamesystem, labmeasurenameinterface, and labresultrevisedoffset. Keep a numeric result only if labresultoffset is in [0,360], labresult parses numeric, and labresultrevisedoffset <=360 or is null under a frozen, reported null-revision convention. Preserve unresolved units/interfaces in the audit and exclude them from numeric state features unless an outcome-blind codebook resolves them. The candidate analyte panel remains potassium, sodium, hemoglobin, hematocrit, glucose, creatinine, BUN, calcium, WBC, platelets, bicarbonate, FiO2, PaO2, PaCO2, pH, anion gap, HCO3, oxygen saturation, magnesium, and base excess, subject to the strict audit.

- **hospital table / hospital.csv.gz**, schema `datasets/eicu/table-811df7b2ef435e12.json`, [source checksum]. Join patient.hospitalid = hospital.hospitalid. Fields hospitalid, numbedscategory, teachingstatus, and region are descriptive workflow diagnostics only; hospitalid is prohibited as a primary predictor.

- **vitalPeriodic table / vitalPeriodic.csv.gz**, schema `datasets/eicu/table-a22c6d6981a32279.json`, [source checksum]. Join vitalPeriodic.patientunitstayid = patient.patientunitstayid. Use only rows with observationoffset in [0,360]. Available columns are vitalperiodicid, observationoffset, temperature, sao2, heartrate, respiration, cvp, etco2, systemicsystolic, systemicdiastolic, systemicmean, pasystolic, padiastolic, pamean, st1, st2, st3, and icp. The catalog records this as a five-minute summary of generally one-minute monitor averages, not a raw waveform.

- **vitalAperiodic table / vitalAperiodic.csv.gz**, schema `datasets/eicu/table-72ace5b89971196b.json`, [source checksum]. Join vitalAperiodic.patientunitstayid = patient.patientunitstayid. Use only rows with observationoffset in [0,360]. Available columns are vitalaperiodicid, observationoffset, noninvasivesystolic, noninvasivediastolic, noninvasivemean, paop, cardiacoutput, cardiacinput, svr, svri, pvr, and pvri.

The raw headers and catalog schemas were inspected. A bounded full-file vital coverage audit was attempted but exceeded the 120-second discovery limit and produced no output; early vital row counts and support are therefore unverified. The future solver must measure them, and Bv/BvP/BvV are unsupported if the prespecified coverage gates fail.

apacheApsVar is available at `apacheApsVar.csv.gz`, table schema `datasets/eicu/table-67711a86e012835e.json`, but is excluded from the primary state challenge because it has no time column and its aggregation window cannot be proven to be known by minute 360. apachePatientResult is excluded because actual mortality fields leak outcomes. No other table is required for the primary experiment.

## Feature blocks and estimands

Freeze codebooks and coverage decisions before using outcome labels.

**Legacy lab comparison.** B0 is the parent’s transparent elastic-net pooled discrete-time cause-specific logistic model with hourly rows from 360 through 1,800, two heads (recorded death and alive discharge), demographics/admission context, lab state summaries, clinical value flags, and one lab availability indicator per retained analyte. B1 adds the parent’s lab process block: counts, distinct times, first/last result, recency, spans, inter-result gaps, revision-known indicators, stable interface/system indicators, and aggregate laboratory intensity. The paired held-out B1-minus-B0 result is retained as the legacy primary transport estimate.

**Physiology-adjusted challenge.** Bv adds to B0 only pre-landmark vital state: for prespecified supported vital fields, first/last/min/max, slope when at least two observations exist, threshold/instability flags, and a field-level availability mask. It includes no vital counts, recency, inter-observation gaps, interface/site descriptors, or outcomes. Continuous transformations, clipping, imputation, and value mappings are learned in the development hospitals. BvP adds exactly B1’s lab process block to Bv; no new post-landmark information is introduced. The primary successor estimand is the paired held-out BvP-minus-Bv difference.

**General workflow diagnostic.** BvV adds only vital observation-process features (row count, distinct observation times, first/last observation, recency to minute 360, observation span, and modality availability) to Bv. It is not a deployment competitor. If BvV performs like BvP, a general monitoring-intensity fingerprint is a stronger explanation. Interface and hospital descriptors remain separate diagnostics.

**Relative process.** BvP-rel replaces continuous lab-process variables with empirical within-target-hospital percentiles learned from a prespecified outcome-free 10% calibration subset of eligible target episodes; target outcomes, discharge status, and post-landmark fields are never used. The remaining target episodes are scored. Require at least 50 calibration candidates and 20 evaluation episodes per target hospital. This is unsupervised site adaptation, not strict zero-shot transport.

**Learned alternative.** T-v is a one-layer GRU or temporal convolution over six one-hour bins in [0,360]. It uses exactly the BvP channels: lab and vital state values and masks, lab process and vital-process channels, and the stable interface/revision indicators that survive the outcome-blind support audit. It has recorded-death and alive-discharge heads, the same cohort, target, horizon, hospital folds, and support gates. A next-bin-observation auxiliary head may describe measurement dynamics but its output cannot enter death prediction. T-v is informative only if it improves held-out-hospital calibration/Brier or prespecified decision outputs beyond BvP; AUROC alone is insufficient.

The transparent Bv/BvP pair is primary because it provides an interpretable test of whether lab process adds information after measured physiology. T-v is retained because temporal order, persistence, and co-movement may reveal information lost by summaries. The alternative is scientifically substantive, not a complexity bonus.

## Splits and uncertainty

Use five grouped outer folds holding out approximately 20% of hospitals once. Stratify by eligible episode and event counts where feasible; keep all episodes from a uniquepid together. Development hospitals are split approximately 75%/25% for fitting/validation. No held-out outcome, target-hospital outcome summary, post-landmark field, or held-out-fold preprocessing decision may influence fitting, codebook, imputation, hyperparameters, early stopping, percentile calibration, or thresholds.

Report macro-hospital paired differences as primary and patient-weighted results secondarily. Use hospital-clustered bootstrap or a hierarchical interval with at least 1,000 resamples if feasible. Report per-hospital calibration-in-the-large and slope, competing-risk integrated Brier, cumulative incidence, alert burden, recorded-death capture, PPV, and uncertainty. Apply simultaneous 95% intervals over the four thresholds and prespecified risk strata.

Define baseline-risk strata from out-of-fold Bv risk: <0.01, 0.01 to <0.05, and >=0.05. A decision cell is supported only with at least 200 stays, 30 recorded deaths overall, and at least 10 stays in at least 80% of contributing hospitals. Unsupported cells are not evidence against the hypothesis.

## Monitoring-review decision and falsification

At each fixed q in {0.01, 0.02, 0.05, 0.10}, define a hypothetical recommendation for enhanced laboratory-surveillance review when predicted recorded-death risk by 1,800 minutes is at least q. Report alerts per 100 stays, death capture, PPV, and:

100 * [TP/N - FP/N * q/(1-q)].

Also report how often BvP changes the review recommendation relative to Bv, the risk of changed-up and changed-down episodes, and whether the change is stable across held-out hospitals and Bv-risk strata. This is a label-relative prioritization diagnostic, not a recommendation to order a test and not a net clinical benefit estimate.

Falsifications are frozen before outcome analysis:

1. **Physiology sufficiency challenge.** Compare B1-minus-B0 with BvP-minus-Bv. A collapse of the process increment after vital state adjustment is adverse to the claim that lab observation history adds patient-level information beyond measured state. It does not prove that testing is irrelevant.
2. **State-matched process permutation.** Within each held-out hospital and Bv-risk stratum, permute complete lab-process vectors across episodes, keeping state, outcomes, and hospital fixed. Attenuation toward Bv is required for a patient-linked interpretation. Persistence signals residual state/site structure, leakage, or a flawed null.
3. **Vital-process placebo.** Compare lab-process and vital-process increments under the same folds and outcomes. A comparable vital-process gain means the signal may be general workflow intensity rather than a laboratory-specific patient process.
4. **Workflow descriptors and relative scale.** Fit hospital-descriptor-only diagnostics using numbedscategory, teachingstatus, and region. Compare BvP with BvP-rel. Raw-only improvement or a descriptor/vital-process match supports workflow dependence; persistence after outcome-free normalization narrows the claim to relative surveillance position, not a causal effect.
5. **Lab block ablations.** Remove counts/intensity, timing/recency, revision, and interface/system blocks separately. Gains confined to interface/site coding are workflow evidence. Repeat with a common analyte panel and after excluding all null-revision rows.
6. **Leakage sentinels.** Prohibit post-360 lab/vital rows, apachePatientResult actual outcomes, hospital outcome summaries, and any target-hospital outcome calibration. A deliberately post-landmark feature may be used only as a pipeline sentinel and never as a scientific result.
7. **Support and calibration gates.** Require the parent event/hospital gates, plus sufficient nonmissing vital support for every retained Bv field, positive state/process overlap, finite competing-risk metrics, and convergence. If coverage is inadequate, report the legacy lab-only result separately and label the physiology-adjusted question inconclusive.

## Interpretation

Supportive evidence requires a favorable, uncertainty-supported BvP-minus-Bv held-out macro-hospital calibration/Brier or supported decision-cell result; changed monitoring-review decisions at a prespecified threshold; attenuation under state-matched lab-process permutation; no comparable vital-process or hospital-descriptor-only gain; and no reversal under common-panel or strict-revision sensitivity. Persistence in BvP-rel supports only a narrower relative-surveillance interpretation. These findings would justify prospective measurement of test indication and response, not a claim that more testing improves outcomes.

Adverse evidence is a reproducible null or worsening after vital adjustment, a calibration harm at supported thresholds, a process-permutation failure, reversal under revision/common-panel handling, or a comparable vital-process/site-descriptor signal. This weakens or refutes the proposed laboratory-specific patient-level interpretation in this snapshot.

Inconclusive evidence includes failed vital coverage, insufficient events or hospitals, no common support, unsupported relative-process target hospitals, unstable temporal fitting, or intervals spanning clinically meaningful ranges. Do not replace an inconclusive result with the legacy model’s favorable result.

## Evidence limits and deferred alternatives

The recorded-death label is discharge status, not adjudicated cause or complete mortality. VitalPeriodic is a summarized monitoring stream, not raw waveform. Lab rows do not establish orders, clinician concern, indication, collection quality, or treatment response. The release lacks a complete test-order table, reliable administration semantics, alert response, patient preferences, post-discharge mortality, external hospitals, validated narrative text, and a causal intervention assignment. Residual confounding by staffing, unit type, illness severity, and undocumented workflow remains.

A supportive computation cannot establish that clinicians should increase or decrease testing, that an enhanced-monitoring review improves survival, or that a threshold is safe. Those require expert adjudication of the physiologic state and test indication, external validation in new hospitals, and a prospective impact or randomized study.

Deferred branches are: a causal test-ordering model (no complete orders/indications), treatment-effect or policy learning (no assigned intervention and response), full waveform modeling (no raw waveform), NLP (public narrative limitations), apacheApsVar state (no landmark-safe time), and reproduction of the demonstration papers (missing cohorts/modalities and unavailable supplementary methods). A larger multimodal model is not selected because it would add complexity without resolving the state-versus-workflow question.

## Compute plan and method record

Measured: snapshot/catalog provenance, raw headers, schema columns/hashes, parent’s outcome-blind lab support counts, and the bounded attempt to audit vital coverage (timed out without output). Unverified: vital coverage, full extraction runtime, Bv/BvP/BvV support, convergence, and all outcome metrics.

Streaming extraction and B0/B1/Bv/BvP/BvV should use 4–8 CPUs and 16–32 GiB RAM, with an estimated 1–4 hours; this is a future-solver estimate. T-v may fit CPU; if repeated outer folds or convergence make CPU time excessive, request one allocated NVIDIA A100-SXM4-80GB with 4 CPUs and 32 GiB host memory, explicitly move model and tensors to cuda:0. Ordinary shell CUDA absence is not evidence of unavailable hardware. GPU use is optional and not scientifically rewarded. Discovery and solver budgets remain separate; no proposer or solver weight training is authorized.

The actual study output must be the frozen data/codebook and fold manifest, paired state-adjusted and legacy predictions, decision/reclassification tables, uncertainty, falsifications, and interpretation trace. No fitted result is claimed here.
