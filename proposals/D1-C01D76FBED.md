> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

eICU provenance-checked denominator reconstruction: what can and cannot be learned about target-label receipt

Status and substantive advance

This proposal is a substantive child of assessed-valid [prior hypothesis] and [prior hypothesis]. It executes the requested provenance audit rather than treating the denominator proposal as merely prospective. It preserves the inherited 540 target-labelled person-landmarks, the five landmarks L={1440,2880,4320,5760,7200} minutes after ICU admission, the literal labels "Ventilated - with daily extubation evaluation" and "Ventilated - with no daily extubation trial", the first-target decision time D in [L,L+360], and all inherited negative endpoint and chart-proxy findings.

The clinical advance is a falsifiable separation of two questions that had previously been conflated. First, can an identity-checked extension retain eligible landmark rows with neither target label? Yes, within the inherited 443 selected ICU stays. Second, does that establish a denominator for all otherwise eligible ventilated eICU stays? No. The inherited builder first creates rows only after target receipt and then selects each person's first qualifying stay among those target-labelled rows. Removing target receipt before first-stay selection changes the population rule. The all-stay denominator therefore remains unresolved and requires Lead approval for a changed population/estimand; it is not a mechanical provenance repair.

Evidence boundary and hypothesis

The supported claim is that an exact anchored extension can quantify target-label coverage inside the inherited selected-stay frame, while the full target-independent population is not identified by the inherited construction. The executed anchored result is not evidence of target-label prevalence among all ventilated patients and cannot prove that labels are hospital-specific conventions.

The falsifiable research hypothesis for Lead approval is: among a newly defined, target-independent first-qualifying-stay population, target-label receipt and the conditional evaluation/no-trial mix will differ materially by landmark and hospital even after retaining zero-record states and separating documentation absence from clinical absence. The competing hypothesis is that those differences attenuate after target-independent selection and prespecified documentation-coverage standardization. This proposal does not claim either outcome for the unconstructed all-stay population.

Inherited findings preserved without re-estimation

Durable liberation remains unascertainable under the locked endpoint algorithm: independent signals were 13/309 versus 4/231 overall, 1/130 versus 0/173 in overlap hospitals, and strict 48-hour observation among union events was approximately one half. No durable-liberation association, discharge bridge, or causal model is estimated.

The inherited 12-hour chart-proxy analysis remains unchanged. The primary setting association was inverse but dominated by peak-pressure charting; peak-only events were 87.2% of evaluation and 83.3% of no-trial composite events in overlap hospitals. The no-peak result was sparse and site/leave-one-out unstable, sedation-rate results were imprecise and hospital-dependent, the primary contrast reversed at 120 hours, and pre-D/post-minus-pre patterns were adverse and site-reversing. These are chart proxies only. Nothing here establishes actual SBT delivery, daily evaluation, extubation, ventilator action, sedation interruption, quality, causality, or benefit.

Exact frozen population and positive control

Frozen artifact: [internal dataset path], [source checksum].

The inherited executable builder is [internal dataset path], [source checksum]. Its executable logic was followed exactly, including PEEP <=8 (not <8), FiO2 normalization of 21-100 to 0.21-1.00, latest pre-L respiratoryCare airwaytype plus FiO2/PEEP evidence, strict physiologic windows, pre-L EOL, and prior 24-hour "Spontaneous - adequate" exclusion.

The reconstruction tested exact row identity on sid, uniquepid, hospitalid, landmark, strategy, and decision_offset. It reproduced 540/540 rows, 443/443 stays, 74/74 hospitals, 309 evaluation and 231 no-trial rows, all five landmark counts (129,147,111,77,76), with zero missing keys and zero extra keys and exact D equality. This is a computational pass, not clinical validation.

Anchored denominator definition and results

The anchor is exactly the 443 ICU stays selected by the inherited target-conditioned first-qualifying-stay rule. Within those stays, each landmark is retained when adult, unitdischargeoffset>L, strict inherited pre-L physiology passes, inherited invasive evidence is present, no pre-L EOL discussion occurs, no "Spontaneous - adequate" marker occurs in [L-1440,L), and no contradictory same-offset first target is present. Target receipt is not required. The primary target-window classification is performed in [L,L+360]: evaluation, no_trial, other_ventilation_value, or no_ventilation_record. Missing target receipt is never coded as no-trial.

Primary anchored result: 1,044 eligible stay-landmarks, 443 stays/persons, 74 hospitals; 309 evaluation, 231 no-trial, 540 either target, 504 neither target, 14 other ventilation values, and 490 with no ventilation-group record in the target window. Target-label coverage is 540/1044 = 51.724%; conditional evaluation mix is 309/540 = 57.222%.

Landmark-specific n, target receipt, neither-target rows, coverage, and conditional evaluation mix are respectively: L=1440, 216, 129, 87, 59.72%, 53.49%; L=2880, 255, 147, 108, 57.65%, 61.90%; L=4320, 219, 111, 108, 50.68%, 60.36%; L=5760, 188, 77, 111, 40.96%, 58.44%; and L=7200, 166, 76, 90, 45.78%, 48.68%.

A full-window sensitivity requiring unitdischargeoffset>L+360 yielded 1,039 rows, 442 stays/persons, 539 target rows and 500 neither-target rows; coverage was 51.877% and conditional evaluation mix 57.328%. Four neither-target rows had only partial target-window observation, and one frozen no-trial row also failed this sensitivity. This sensitivity cannot replace the inherited positive-control population.

The anchored frame is selection-conditioned. All 74 hospitals necessarily entered through at least one target-labelled eligible landmark; therefore zero hospitals have no target rows, and hospital target-receipt variation cannot be interpreted as population prevalence. In this frame, hospital eta-squared is 0.0753 for target receipt and 0.3544 for the conditional evaluation/no-trial mix. Coverage quantiles across hospitals are 0%, 25th=37.74%, median=50%, 75th=75%, maximum=100%; 16 hospitals have all anchored rows target-labelled. There are 18 hospitals with at least 10 denominator rows but only 7 with at least 10 target rows. These diagnostics are descriptive and do not solve target-independent selection.

Exact source and time binding

The source snapshot is eICU 2.0 [source checksum]; catalog [source checksum]. Each is a read-only gzip CSV with archive member convention ordinary file under [internal dataset path] 2.0 data/.

patient.csv.gz (patientunitstayid, uniquepid, hospitalid, age, unitvisitnumber, unitdischargeoffset, unitdischargestatus, unitdischargelocation) supplies adult, stay, hospital, first-stay, and discharge fields. carePlanGeneral.csv.gz (patientunitstayid, cplitemoffset, cplgroup, cplitemvalue) supplies target labels, D, ventilation states, and target-window classification. carePlanEOL.csv.gz (patientunitstayid, cpleoldiscussionoffset) supplies the pre-L EOL exclusion. respiratoryCharting.csv.gz (patientunitstayid, respchartoffset, respchartvaluelabel, respchartvalue) supplies FiO2, PEEP, and RT Vent On/Off evidence. respiratoryCare.csv.gz (patientunitstayid, respcarestatusoffset, airwaytype) supplies latest pre-L airway evidence. vitalPeriodic.csv.gz (patientunitstayid, observationoffset, sao2, respiration, systemicmean) and vitalAperiodic.csv.gz (patientunitstayid, observationoffset, noninvasivemean) supply strict physiologic windows. All joins are through patientunitstayid; event times are the named offset fields and all offsets are relative to ICU admission.

The full scans retained no sampled source rows: patient 200,859; carePlanGeneral 3,115,018; respiratoryCharting 20,168,176; respiratoryCare 865,381; vitalPeriodic 146,671,642; vitalAperiodic 25,075,074; carePlanEOL 1,433. Source hashes are patient [source checksum]; carePlanGeneral [source checksum]; carePlanEOL [source checksum]; respiratoryCharting [source checksum]; respiratoryCare [source checksum]; vitalPeriodic [source checksum]; vitalAperiodic [source checksum].

Provenance decision and next experiment

The minimal exact raw-source reconstruction is sufficient for an identity-preserving anchored extension, and that extension was executed. It is not sufficient to claim an all-ventilated-stay denominator under the inherited estimand. A direct target-independent first-stay selection must be specified and approved as a new population rule, then rerun from the same read-only sources. It must retain every eligible landmark, left-join source-specific coverage summaries so zero-record rows remain, and report age unknowns, exclusions, target classes, and complete observation separately. Any target-independent reconstruction must first pass the same 540-row identity control; failure stops denominator-aware inference.

For the approved follow-up, estimate target-label rates among all eligible rows, target coverage, other-value and no-record states, conditional label mix, and source-specific pre-L documentation coverage at [L-720,L). Standardize only over prespecified common-support hospital/coverage/landmark cells. Use hospital descriptors only descriptively. Never interpret note, provider, nursing, or care-plan presence as bedside action. Keep the inherited D, (D,D+720] chart-proxy definitions, peak-only decomposition, pre-D diagnostic, landmark contrasts, and leave-one-hospital-out analyses unchanged in the target-labelled subset.

Supportive result: exact identity passes, full target-independent denominator is complete with zero-record rows, coverage/common support is broad, and hospital dispersion attenuates without rescuing the inherited proxy instability. Adverse result: target assignment remains concentrated by hospital/landmark/coverage or proxy mappings remain unstable; this strengthens the warning against unqualified pooling. Inconclusive result: identity or full-source coverage fails, or sparse cells prevent standardization. No branch proves semantics, documentation convention, actual care, quality, causality, or benefit.

Computational verification can check hashes, row identity, counts, labels, D, joins, windows, classifications, denominators, and linkage of conclusions to outputs. Clinical adjudication, local workflow/template metadata, device semantics, standardized units, validated SBT/extubation/reintubation outcomes, and external replication are required for stronger claims.

Reproducibility artifacts

Executable: [internal dataset path], [source checksum].

Anchored rows: [internal dataset path], [source checksum].

Results JSON before the resource-managed rerun: [internal dataset path], [source checksum]. The final JSON hash must be recomputed after the declared job completes; the hash is not a scientific result.

The inherited endpoint and action artifacts remain available at their frozen support paths and are not regenerated: endpoint rows [internal dataset path] and action rows [internal dataset path]
