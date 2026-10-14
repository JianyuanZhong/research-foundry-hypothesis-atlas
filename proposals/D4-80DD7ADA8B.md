> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional hypothesis: body-fat distribution separates metabolic from functional/fall risk trajectories

## Status and scientific deliverable

This is a provisional, data-bound research hypothesis, not an observed result. The deliverable is a newly fitted, held-out comparison of a simple total-adiposity baseline with a prespecified body-composition model that tests whether visceral fat and posterior-thigh muscle fat infiltration (MFI) identify distinct subsequent metabolic and functional/fall trajectories. Completion requires cohort and overlap counts, a temporally ordered event table, fitted estimates with uncertainty, calibration/discrimination or trajectory summaries, and a conclusion classified as supportive, adverse, or inconclusive. No association or clinical conclusion has been computed in this episode.

## Unresolved question and clinical importance

At similar total body fat, does higher visceral fat predict subsequent metabolic disease more specifically, while higher posterior-thigh MFI predicts subsequent functional decline or falls more specifically? This matters because separating these phenotypes could justify targeted body-composition assessment rather than treating adiposity as one generic risk factor. A positive result would support distinct risk pathways; a negative result would argue against separating these phenotypes for clinical risk stratification.

The substantive advance is a temporally ordered test of divergent downstream trajectories, rather than another generic prediction of a composite health score. The leading claim is that fat distribution contains clinically distinct information beyond total adiposity. The strongest rival is that apparent divergence is explained by current severity, age/sex, measurement timing, selection into MRI, or observation practices. The proposed comparison is observational and cannot establish mechanism or treatment benefit.

## Grounding and evidence boundary

The inspected evidence supports only that myosteatosis/MFI is associated with metabolic and functional outcomes [K1], that IMAT/MFI spans metabolic, cardiovascular and oncologic settings but remains heterogeneous across imaging and disease contexts [K2], and that UKB abdominal MRI phenotypes including visceral fat improve internal prediction of incident T2D [K3]. These works do not establish the proposed divergence, causality, or clinical utility. The prior UKB-17-derived branch supplies the data opening, not a result. No association has been computed here, and no clinical adjudication or unavailable evidence is being implied.

## Exact data and computable experiment (to be verified before execution)

Use only the UK Biobank namespace and documented joins. The exact read-only Parquet views are `datasets/population_multiomics/table-6fc0a334db7f533b.json` (source `[UKB data file]`, 502,370 rows, `eid`, UKB namespace) for `53-2.0`, `21085-2.0`, `23355-2.0`, `23356-2.0`, `23099-2.0`, `46-2.0/3.0`, `47-2.0/3.0`, and `2296-2.0/3.0`; `table-03f57283ab9ae48b.json` (source `[UKB data file]`, 502,370 rows, `eid`) for `41270-0.*` diagnosis codes and `41280-0.*` dates; and `table-674bd55f4152a860.json` (source `[UKB data file]`, 502,370 rows, `eid`) for `31-0.0` sex, `34-0.0` birth year, and `21022-0.0` ethnicity. Join only on `eid` within this namespace. The catalog source hashes are `[source checksum]`, `[source checksum]`, and `[source checksum]`. A bounded managed diagnostic found 36,320 complete second-assessment MRI/total-fat participants; 4,557 had any third-assessment grip and 4,564 had third-assessment falls. These are feasibility counts, not hypothesis results.

Population: participants with baseline body-composition measurements, valid total adiposity, visceral fat and posterior-thigh MFI, and a defined baseline index date. Exclude participants lacking the required baseline measurements or with non-identifiable temporal ordering. Preserve source-specific identifiers and do not join across incompatible namespaces.

Temporal boundaries: define time zero at the second assessment (`53-2.0`); exclude prevalent metabolic disease using diagnosis arrays available before or at baseline and baseline functional limitation/falls where feasible; use a prespecified one-year lag for metabolic outcomes with no-lag and longer-lag sensitivities. Functional outcomes use later repeated measurements at instance 3. Functional decline and falls must be measured after baseline. If dates or event ascertainment are unavailable, the relevant endpoint is deferred rather than inferred.

Outcomes: (1) incident metabolic disease using the verified diagnosis fields, with baseline disease excluded; (2) incident falls; and (3) change in functional measures where repeated measurements exist. The primary scientific contrast is whether visceral fat and MFI have distinct outcome-specific associations after adjustment for total adiposity and prespecified covariates.

Baseline model: a simple adjusted model using total adiposity plus age, sex, ethnicity, and measurement timing. Alternative substantive model: a prespecified composition model adding visceral fat and posterior-thigh MFI, with outcome-specific interaction or mediation-style descriptive contrasts only if the estimand is justified. Compare held-out calibration/discrimination and, more importantly, the direction and uncertainty of the visceral-versus-MFI outcome-specific contrasts. The alternative can reveal whether fat distribution carries information lost by total adiposity alone; it does not prove mechanism.

A learned sequence/trajectory model is deferred unless repeated functional measurements and temporal support are verified. It could reveal nonlinear or time-varying recovery/decline patterns, but would add complexity without resolving the primary distribution question if the baseline and composition model are not first estimable. Revisit it only with adequate repeated measures, missingness diagnostics, and a held-out temporal split.

## Falsification and interpretation

Supportive: visceral fat and MFI show prespecified, outcome-specific associations of sufficient magnitude with uncertainty excluding the null, after total-adiposity adjustment, with stable direction in held-out or sensitivity analyses. This would support distinct descriptive risk phenotypes, not causality.

Adverse: the composition model adds no stable outcome-specific information, effects reverse, or associations are explained by baseline severity/timing/selection diagnostics. This would weaken the divergence claim.

Inconclusive: insufficient overlap, sparse events, missing dates, wide uncertainty, or unstable calibration. This would motivate a larger or differently ascertained study, not a positive interpretation.

A positive result would not establish that changing visceral fat or MFI improves outcomes. Causal, mechanistic, and treatment claims require longitudinal intervention or stronger design, clinical adjudication, and additional covariates not guaranteed by these files.

## Missing evidence and next checks

The exact catalog bindings and schema checks above are verified; row-level overlap and event counts remain feasibility diagnostics, not results. The three inspected key works and frozen receipts are attached. The future solver must recompute exact code-specific and post-lag counts, model estimates, uncertainty, calibration, and classify the result as supportive, adverse, or inconclusive.
