# Outcome-blind identifiability audit of the all-hour eICU excess-FiO2 crossover

## Status and scientific decision

This is a substantive child of `[prior hypothesis]`. It preserves the parent's target population, hour-24 phenotype landmark, hour-24–36 all-hour exposure, hour-36 outcome origin, seven-day competing-risk estimand, and 3 percentage-point interaction target. It reports a completed outcome-blind measurement experiment, not a mortality result.

The audit gives an adverse answer to the assigned feasibility question: under a transparent source-error plus logical-missingness model, the 12-hour excess-FiO2 burden is not identified precisely enough to resolve the prespecified interaction in the full fixed population. Therefore the mortality branch is deferred. Failure itself is the scientific result: eICU's chart streams can characterize oxygen-record observability and disagreement, but cannot presently support a pulmonary-specific mortality interpretation without unverifiable tightening assumptions and clinician adjudication.

## Evidence-supported claim, unresolved claim, and clinical importance

ICU-ROX established that an oxygen-target strategy can alter exposure without significantly changing ventilator-free days in a broad ventilated population [K1]. A mechanistic review supports biological plausibility for hyperoxia–mechanical-stress synergy while emphasizing inconsistent clinical mortality evidence [K2]. LUNG SAFE showed incomplete and severity-dependent clinician recognition of ARDS [K3]. Thus, the strongest external-evidence claim remains: oxygen exposure is modifiable; biological interaction with mechanical stress is plausible; and pulmonary labels are imperfect. None of the three works validates eICU FiO2, the eICU pulmonary proxy, or a mortality interaction.

The unresolved biological hypothesis remains the parent's:

**Among adult first ICU stays alive and in ICU at hour 36, with PaO2 80–120 mm Hg paired to FiO2 during hours 18–24, the pre-hour-24 acute-pulmonary-injury proxy modifies the association between mean all-hour excess FiO2 during hours 24–36 and seven-day post-hour-36 in-hospital death by a clinically consequential 3 absolute risk points per +0.10 excess FiO2.**

This child first tests the necessary measurement hypothesis:

**Before outcomes are used, respiratory-chart/lab FiO2 and bounded carry-forward identify each stratum's 12-hour mean excess-FiO2 burden with median width <=0.10 and 75th-percentile width <=0.15; an ordered latent model calibrated by masked-chart prediction must meet the same gate in both strata and cannot override failure of the transparent envelope.**

Answering this gate prevents a clinically seductive but unresolvable mortality association from consuming the evidence. Passing would justify phenotype adjudication and the mortality experiment. Failure redirects work to device/chart validation rather than oxygen-treatment inference.

## Fixed population, clocks, variables, and eventual outcome

The fixed design is unchanged. Index `patient.patientunitstayid`. Select age >=18, then the first ICU stay per `patienthealthsystemstayid` by valid lowest `unitvisitnumber`, then require `unitdischargeoffset>2160`. Exclude impossible chronology, burns, ECMO before minute 1440, and exact comfort-measures-only before minute 1440. The diagnostic implemented age, first-stay ordering, hour-36 presence, burn/ECMO/comfort exclusions; it found 90,296 adult first stays through hour 36 and 85,428 after these exclusions.

Anchor: last valid `lab.labname='paO2'` of 80–120 at minutes 1080–1440, paired to nearest valid FiO2 within +/-60 minutes, ties preceding then earlier. Respiratory-chart and lab FiO2 are admissible. `respiratoryCare.setapneafio2` is not: its field meaning is apnea FiO2 and its paired median absolute disagreement with respiratory charting was 0.50; it remains a negative/source-failure control.

Phenotype is frozen at minute 1440. P0 injury requires a diagnosis/admission term for ARDS/acute respiratory distress, pneumonia, aspiration, pulmonary oedema, or acute respiratory failure plus anchor P/F <=300. Primary comparator has no term. Term with P/F>300 is discordant validation, not primary analysis. The corrected audit found 3,235 anchored stays: 1,348 injury, 1,693 no-term, and 194 discordant.

Exposure is all 12 bins in [1440,2160). The target burden is
`B_i=(1/12) sum_t max(F_it-0.40,0)`.
No same-hour oxygenation selects an hour or stay. If the measurement gate eventually passes, outcome origin is minute 2160 and outcome is seven-day in-hospital death through minute 12,240 with live discharge competing and administrative censoring at day seven. No outcome or discharge status was read by this diagnostic.

## Exact data bindings

Read-only eICU snapshot: `[source checksum]`. Files are ordinary gzip CSVs, no archive members, under `[internal dataset path]`. All clinical tables join on `patientunitstayid`; `hospital` joins on `hospitalid`; never join measurements on `uniquepid`.

- `patient.csv.gz`, table `patient`, catalog `datasets/eicu/table-ab037c09d7df9a3c.json`: `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `unitvisitnumber`, `hospitalid`, `age`, demographic/admission fields, `unitdischargeoffset/status`, and eventual `hospitaldischargeoffset/status`.
- `lab.csv.gz`, table `lab`, `table-79bdb33275339b1a.json`: `patientunitstayid`, event `labresultoffset`, revision `labresultrevisedoffset`, `labname`, `labresult`, `labresulttext`, measurement-system/interface. Required labels are `paO2` and `FiO2`; later analysis also uses PaCO2, pH, O2 Sat, PEEP, lactate, renal/hepatic/haematologic labs.
- `respiratoryCharting.csv.gz`, table `respiratoryCharting`, `table-339bf06c7eef27e0.json`: `patientunitstayid`, event `respchartoffset`, entry `respchartentryoffset`, `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`. FiO2 labels contain FiO2/fraction of inspired oxygen; pressure, PEEP, tidal-volume, rate, saturation and device fields support later ordering.
- `respiratoryCare.csv.gz`, table `respiratoryCare`, `table-75bd08623beb504f.json`: `respcarestatusoffset`, `ventstartoffset`, `ventendoffset`, `airwaytype`, `setapneafio2`. The last field is excluded as an exposure source and retained only for the source-failure control.
- `diagnosis.csv.gz`, table `diagnosis`, `table-5d5ab99e8c359037.json`: `diagnosisoffset`, `diagnosisstring`, `icd9code`, priority/status.
- `admissionDx.csv.gz`, table `admissionDx`, `table-2e48e1043e7eaa89.json`: entry clock `admitdxenteredoffset`, `admitdxpath/name/text`.
- `carePlanGeneral.csv.gz`, table `carePlanGeneral`, `table-33b82ae7a5609587.json`: `cplitemoffset/group/value` for exact comfort-only exclusion.
- `treatment.csv.gz`, table `treatment`, `table-5461361964176606.json`: `treatmentoffset/string` for burn/ECMO flags.

The eventual outcome/adjustment tables from the parent remain available: `hospital`, `vitalPeriodic`, `note`, `physicalExam`, `apacheApsVar`, `apachePatientResult`, `apachePredVar`, `infusionDrug`, `carePlanEOL`, and `pastHistory`, with the same keys/clocks. They were not needed for this outcome-blind diagnostic. All four configured dataset trees remain directly accessible read-only; derived files are under `work/identifiability-gate/`.

## Transparent partial-identification baseline: completed M0 diagnostic

FiO2 normalization accepted 0.21–1.00 directly and 21–100 after division by 100. Within each hour, the median respiratory-chart value was primary. If absent, the most recent prior respiratory-chart value was carried forward only to a bin whose start was <=120 minutes later; future values were never carried backward. A same-bin lab FiO2 could supply a validation-source value when respiratory charting was unavailable. All other hours retained the logical excess interval [0,0.60].

Among the 1,348 injury stays, 5,325 of 16,176 hours (32.9%) were directly charted, 3,619 (22.4%) were supported by <=120-minute carry-forward, 402 (2.5%) by lab only, and 6,830 (42.2%) remained unsupported. Among 1,693 no-term stays, counts were 5,752/20,316 (28.3%), 3,563 (17.5%), 556 (2.7%), and 10,445 (51.4%). Median supported hours were 8 versus 6. Carry age had median 49 and 90th percentile 104 minutes.

Respiratory-chart/lab pairs within 30 minutes numbered 2,522. Median absolute difference was 0, 75th percentile 0, and 90th percentile 0.10. This is agreement, not accuracy against delivered FiO2. A conservative +/-0.10 source interval was propagated. Apnea-FiO2 produced 532 pairs with median difference 0.50 and was excluded.

The resulting transparent burden-width median/p75 was 0.283/0.517 in injury and 0.367/0.567 in no-term. Only 11.7% and 15.6% respectively had width <=0.10. Both prespecified stratum gates fail by large margins. Logical missingness, not sampling uncertainty, dominates.

## Ordered latent alternative: completed bounded comparison

The scientifically substantive alternative used the identical stays, 12 hours, respiratory-chart and lab measurements, source clocks, and no outcomes. It was a finite-state hidden Markov model over FiO2 0.21–1.00 in 0.01 steps. An empirical persistence transition kernel was fitted from consecutive observed hourly respiratory-chart medians. Source-specific emissions used respiratory-chart/lab pair residuals. It was tested by masking one directly charted hour in each stay with at least three direct hours (n=1,481) and predicting it from ordered surrounding observations.

The transparent last-observation/lab baseline was available for 1,022 masked hours and had MAE 0.0155. The latent model covered all masked hours, MAE 0.0172, and its nominal 90% intervals covered 90.7%; injury and comparator MAEs were 0.0157 and 0.0187. Thus the latent model adds broad coverage and uncertainty through ordering, but no precision improvement over simple carry-forward where the baseline is available.

Latent burden widths had median/p75 0.0567/0.1288 in injury, passing that stratum, but 0.0617/0.5608 in no-term, failing the p75 gate. The huge comparator tail corresponds to stays with little chart information; masked re-entry performance does not validate extrapolation to never-charted hours. Per the frozen hierarchy, latent assumptions cannot override the transparent M0 failure.

This comparison is substantive: M0 preserves honest ignorance but loses temporal persistence; the latent alternative uses persistence to recover charted states and quantifies when that information is insufficient. It shows that model complexity cannot solve structural absence in the comparator stratum.

## Gate interpretation and falsification

The measurement hypothesis is **adverse**, not merely statistically inconclusive:

- transparent median and p75 widths exceed 0.10/0.15 in both strata;
- the ordered alternative fails the comparator p75 gate;
- apnea-FiO2 is not a valid substitute;
- phenotype accuracy remains unmeasured without clinicians.

Consequently, the 3-point mortality interaction is not tested. It would be invalid to compute a mortality coefficient and call its wide or narrow conventional confidence interval biological evidence. The parent's proposed “maximum error-only risk interaction <1.5 points” cannot itself be evaluated outcome-blind: it requires outcomes plus explicit assumptions linking exposure/phenotype errors to risk. This child corrects that gate. The computable outcome-blind prerequisite is exposure identification at a +0.10 burden scale; it fails.

Supportive measurement result would have required both M0 stratum median widths <=0.10 and p75 <=0.15, adequate lab/respiratory agreement across >=20 hospitals, and an ordered model with calibrated held-out coverage that stayed inside M0. That would permit clinician phenotype review, then outcome modeling.

Adverse is the observed result: structural missingness makes M0 too broad and the latent alternative cannot pass both strata. This defers the biological/mortality branch and prioritizes device/chart validation. It does **not** refute oxygen toxicity or the 3-point interaction.

Inconclusive would mean estimates near thresholds, insufficient pairs/hospitals, failed masking calibration, or implementation uncertainty. Those do not describe the magnitude of the transparent failure here, although the exact anchor/cohort count differs from an inherited pilot because this audit applies first-stay ordering before the hour-36 criterion and excludes apnea-FiO2. The solver must publish a row-level flow reconciliation before any revival; no population change is authorized.

## Clinician adjudication and missing evidence

Two ICU clinicians plus adjudication remain essential to estimate whether pre-hour-24 eICU evidence supports acute parenchymal injury, hydrostatic-only disease, support class, and evidence timing. Review must be blinded to hospital, P0, exposure, post-hour-24 data, and outcome. It can validate consistency with available eICU evidence, not Berlin ARDS.

No automatic computation can recover bilateral imaging, exclude hydrostatic oedema uniformly, verify delivered airway FiO2, infer clinician intent, or establish oxidative injury. A future mortality study requires external device/chart validation or a design whose exposure is actually observed; causal oxygen-target recommendations require prospective evidence.

## Solver deliverables and resources

The next solver should deliver the completed measurement study, not a mortality estimate:

1. a row-level cohort-flow reconciliation against the inherited pilot, without changing the fixed rules;
2. a 12-hour source/age/entry-delay panel and hospital/stratum coverage matrix;
3. respiratory-chart/lab pair calibration by source age, support, stratum, and held-out hospital;
4. transparent logical and empirical-source burden intervals with the frozen gates;
5. the ordered latent model with hospital-held-out contiguous-block masking, calibration/coverage, and comparison to carry-forward;
6. the blinded clinician-review sampling frame and, if actual review is available, weighted confusion estimates;
7. a gate-concordant conclusion: measurement-only adverse unless all prerequisites pass.

Measured compute: final diagnostic used 8 CPUs, 64 GiB requested, 188 seconds; no GPU. Full hospital-bootstrap measurement fitting is estimated at 2–4 hours on 16 CPUs/128 GiB. A GPU is unnecessary for this finite-state model. Only if measurement and clinician gates later pass should the parent’s outcome model (16 CPUs, then at most one A100 for the ordered sequential alternative, within 8 hours) be reopened.

## Alternatives not chosen and revisit conditions

A complete-case or >=6-hour cohort was rejected because it changes the all-hour population through observation selection. Missing=0.21 and unlimited carry-forward were rejected. Same-hour oxygen adequacy conditioning remains rejected as post-treatment selection. A learned gradient-boosting re-entry model in existing support had worse error than carry-forward and optimistic missing-hour widths; this motivated the calibrated ordered model but does not justify imputation. A generic mortality RNN remains scientifically irrelevant.

Revisit the mortality branch only after an external delivered-FiO2 validation sample, dense device export, or a frozen redesign approved as a scientific child establishes both-stratum burden precision and clinician phenotype validity. A narrower high-coverage estimand could be proposed separately, but it is not this fixed all-hour target.

## Compact bibliography

[K1] ICU-ROX Investigators and ANZICS Clinical Trials Group; Mackle D, Bellomo R, Bailey M, et al. *Conservative Oxygen Therapy during Mechanical Ventilation in the ICU.* N Engl J Med. 2020;382:989–998. doi:10.1056/NEJMoa1903297. Abstract-level record inspected.

[K2] Nadeau EE, Schwingshackl A, Sturgill JL, Waters CM. *Bench evidence, bedside uncertainty: hyperoxia, mechanical ventilation and lung injury.* Eur Respir Rev. 2026;35:260058. doi:10.1183/16000617.0058-2026. Version-of-record XML passages inspected.

[K3] Bellani G, Laffey JG, Pham T, et al.; LUNG SAFE Investigators and ESICM Trials Group. *Epidemiology, Patterns of Care, and Mortality for Patients With Acute Respiratory Distress Syndrome in Intensive Care Units in 50 Countries.* JAMA. 2016;315:788–800. doi:10.1001/jama.2016.0291. Published abstract/metadata inspected; supplement not inspected.
