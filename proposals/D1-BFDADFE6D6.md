# Target-independent first-qualifying-stay audit of eICU ventilator care-plan transportability

## Scientific question and hypothesis

The inherited 540-row result establishes hospital-dependent use of the two exact care-plan labels, but its denominator was selected after examining those labels. The unresolved, falsifiable question is whether that adverse conditional transportability signal persists when adult ICU stays are selected from pre-landmark clinical and respiratory evidence, with first qualifying stay per `uniquepid` frozen before either target label is read. The primary hypothesis is that target-label receipt and the evaluation/no-trial mix remain materially hospital-dependent even under this target-independent denominator; a competing result would be that the prior signal was an artifact of target-conditioned stay selection.

The strongest supported claim before this audit was narrower: within the inherited target-labelled, target-conditioned cohort, label mix was hospital-dependent and unstable under leave-one-hospital-out diagnostics. This audit does not convert a care-plan label into an actual SBT, extubation, bedside action, durable liberation, quality measure, causal effect, clinical benefit, or external transportability claim.

## Population, temporal ordering, and estimand

Use the eICU 2.0 snapshot `[source checksum]` (catalog [source checksum]). Consider landmarks 1,440, 2,880, 4,320, 5,760, and 7,200 minutes after ICU admission. Include adults (`age >=18`; eICU `> 89` is mapped to 90) whose ICU stay extends beyond each landmark. At every landmark, use only offsets `< L` to establish eligibility and first-stay selection. After the selected stay/person-landmark cohort is frozen, classify care-plan receipt in `[L,L+360]`.

The primary denominator is documentation receipt among target-independent, pre-landmark eligible first qualifying ICU stays. The primary stay survival requirement is `unitdischargeoffset > L`; the complete-target-window sensitivity requires `unitdischargeoffset > L+360`. Selection is at person level: among qualifying stays, sort by `uniquepid`, `unitvisitnumber`, and `patientunitstayid`, retain the first stay, and retain every qualifying landmark in that stay. No `carePlanGeneral` target label is used to establish invasive ventilation or to select the first stay.

## Independent ventilation and strict eligibility definition

Independent invasive-ventilation evidence is the latest nonmissing pre-landmark `respiratoryCare.airwaytype`, restricted to the explicit values `Oral ETT`, `Nasal ETT`, `Tracheostomy`, `Double-Lumen Tube`, or `Cricothyrotomy`. `No Artificial Airway`, missing airway values, and `Other` do not qualify the primary explicit-airway definition. In addition, require a valid FiO2 and PEEP/CPAP in `[L-360,L)`.

Apply the inherited strict physiology before `L`: latest normalized FiO2 `<=0.50`, latest PEEP/CPAP `<=8`, at least two valid SpO2 observations in `[L-120,L)` with median `>=88` and `<100`, latest respiratory rate 8 through 35, and at least one MAP observation with median `>=65` (combining `vitalPeriodic.systemicmean` and `vitalAperiodic.noninvasivemean`). Normalize FiO2 values 21–100 to fractions and retain 0.21–1.0. Exclude any pre-landmark EOL discussion and any `Spontaneous - adequate` care-plan record in `[L-1440,L)`. The executable does not impose vasopressor non-escalation because no validated active interval is available.

## Receipt categories and analyses

After cohort freezing, inspect `carePlanGeneral` records in the Ventilation group and classify each person-landmark into four mutually exclusive states. The earliest exact target in the window gives `daily_evaluation` or `no_daily_trial`; absent either target but with another Ventilation-group value gives `other_ventilation_label`; with no Ventilation-group record gives `no_target_label`. Same-offset contradictory exact targets are retained as other and counted separately. These categories represent documentation receipt, not observed care.

Report the complete filter flow, overall and landmark-specific category counts, full-window sensitivity, hospital and hospital-landmark coverage, hospitals without target receipt, target-receipt probabilities and Jeffreys-corrected odds, conditional evaluation mix, hospital and landmark eta-squared, and positivity/common support. A receipt inverse-probability weighting calculation is only a missing-at-random sensitivity over observed hospital-landmark cells; it cannot infer the latent evaluation/no-trial category for `no_target_label` rows.

## Exact source bindings

- `patient.csv.gz`, table `patient`: `patientunitstayid`, `uniquepid`, `hospitalid`, `age`, `unitvisitnumber`, `unitdischargeoffset`, `unitdischargestatus`, `unitdischargelocation`; join and person/stay selection by `patientunitstayid`, ordering by `uniquepid`, `unitvisitnumber`, `patientunitstayid`.
- `respiratoryCare.csv.gz`, table `respiratoryCare`: `patientunitstayid`, `respcarestatusoffset`, `airwaytype`; latest pre-`L` explicit airway.
- `respiratoryCharting.csv.gz`, table `respiratoryCharting`: `patientunitstayid`, `respchartoffset`, `respchartvaluelabel`, `respchartvalue`; FiO2 and PEEP/CPAP in `[L-360,L)`.
- `vitalPeriodic.csv.gz`, table `vitalPeriodic`: `patientunitstayid`, `observationoffset`, `sao2`, `respiration`, `systemicmean`; SpO2, respiratory rate, and systemic MAP in `[L-120,L)`.
- `vitalAperiodic.csv.gz`, table `vitalAperiodic`: `patientunitstayid`, `observationoffset`, `noninvasivemean`; additional MAP in `[L-120,L)`.
- `carePlanEOL.csv.gz`, table `carePlanEOL`: `patientunitstayid`, `cpleoldiscussionoffset`; pre-landmark EOL exclusion.
- `carePlanGeneral.csv.gz`, table `carePlanGeneral`: `patientunitstayid`, `cplitemoffset`, `cplgroup`, `cplitemvalue`; prior spontaneous exclusion only after independent clinical screening, and target classification only after cohort selection. All joins use `patientunitstayid`; all temporal comparisons use the listed minute offsets.

## Computed results

The executable completed successfully as resource-managed job `[research job]` in 288.82 seconds. Submitted executable SHA-256 is `[source checksum]`. Output hashes are:

- rows CSV `[source checksum]`
- hospital CSV `[source checksum]`
- hospital-landmark CSV `[source checksum]`
- results JSON `[source checksum]`

Filter flow was 132,495 potential adult stay-landmarks, 21,948 with explicit invasive airway, 13,421 with recent FiO2 and PEEP, 4,326 passing strict physiology before exclusions, 4,058 after EOL/spontaneous exclusions, 2,188 qualifying stays, 2,024 qualifying people, and 3,722 selected first-stay person-landmarks.

The target-independent denominator contained 3,722 rows from 2,024 stays/persons and 77 hospitals: 78 daily-evaluation, 30 no-daily-trial, 213 other-ventilation-label, and 3,401 no-target-label rows. Target receipt was 108/3,722 (2.902%); the conditional evaluation mix among received exact targets was 78/108 (72.222%). In the complete-window sensitivity, 3,671 rows had 78 evaluation, 29 no-trial, 204 other, and 3,360 no-target, with receipt 107/3,671 (2.915%) and evaluation mix 72.897%. There were no target conflicts.

Receipt by landmark was 27/894 (3.020%), 33/892 (3.700%), 21/731 (2.873%), 14/654 (2.141%), and 13/551 (2.359%) for landmarks 1,440 through 7,200, respectively. The receipt odds ratios versus 1,440 were 1.000, 1.230, 0.955, 0.714, and 0.791, with the reported 95% intervals all compatible with substantial uncertainty.

Only 18/77 hospitals had any target receipt, 59/77 had none, and 5/77 had both exact targets. Only one hospital had at least ten rows under each exact target; 46 had at least ten denominator rows. Among hospitals with at least ten denominator rows, Jeffreys-corrected receipt odds ranged from 0.00348 to 0.20548 (median 0.02564). Hospital eta-squared was 0.05692 for receipt and 0.09824 for the conditional evaluation/no-trial mix; landmark eta-squared was 0.00107 and 0.04533, respectively.

The pre-specified common-support rule—hospital-landmark cells with at least five target rows and both exact labels—left 5 cells, 1 hospital, 980 denominator rows (26.33%), and 73 target rows. The directly denominator-weighted evaluation mix in this restricted support was 0.68415. The IPW sensitivity gave hospital and landmark eta-squared values of 0.12169 and 0.03669, but is not identification of unlabelled states.

## Positive control and lineage reconciliation

The independently written executable exactly reconstructed the inherited 540-row positive control on `sid`, `uniquepid`, `hospitalid`, `landmark`, `strategy`, and `decision_offset`: 540/540 rows, 443/443 stays, 74/74 hospitals, zero missing keys, and zero extra keys. The inherited frozen cohort hash is `[source checksum]`.

Of the 108 target-labelled rows in the new denominator, all 108 intersected the frozen 540 and no new target row was absent from it. Conversely, 432 frozen rows were absent from the new denominator: 421 lacked the explicit-airway plus recent-FiO2/PEEP candidate under the independent definition, and 11 were displaced by a different first qualifying stay per `uniquepid`. Thus exact lineage identity passes, while the target-independent denominator is demonstrably a different and much broader documented-airway population.

## Interpretation and falsification criteria

These results support the computational claim that the inherited 540 can be reproduced and that receipt and conditional label mix can be measured after a target-independent first-stay selection under the stated explicit-airway definition. They are adverse to a well-powered hospital-transportable label-use interpretation: receipt is sparse, 59 hospitals have no target receipt, only one hospital has ten or more rows under each target, and common support covers only 26.33% of denominator rows. The conditional-mix hospital heterogeneity is smaller than in the inherited target-conditioned analysis but cannot be treated as a stable transportability estimate because support is extremely limited and label receipt is likely informative.

The prior conditional adverse finding therefore does not simply disappear under denominator correction, but its population-level conditional interpretation becomes non-identifiable for most denominator rows. Receipt weighting cannot recover an unobserved target state for 3,401 no-target rows. A supportive result would require exact identity, substantial receipt across hospitals, adequate both-label common support, stable conditional contrasts under denominator-aware analyses, and reproducible results under reasonable bounded airway-lookback definitions. An adverse result is a falsification of broad label-use transportability under this operational definition, not proof that bedside evaluation practices differ or that clinical benefit differs. An inconclusive result would follow from failed source identity, inadequate receipt/support, or sensitivity-dependent airway ascertainment.

Important remaining uncertainty is airway-state persistence: the primary executable uses the latest nonmissing airway status at any pre-landmark offset, without a maximum lookback, while requiring recent FiO2 and PEEP. Bounded airway-lookback and active-interval analyses using `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, and `priorventendoffset` are needed before treating the operational denominator as definitive. Clinical adjudication and workflow metadata are required for actual SBT/extubation semantics, bedside action, and causal or quality claims.

## Reproducibility artifacts

- Executable: `[internal dataset path]`
- Results: `[internal dataset path]`
- Row-level output: `[internal dataset path]`
- Hospital output: `[internal dataset path]`
- Hospital-landmark output: `[internal dataset path]`
- Assigned parent positive-control cohort: `[internal dataset path]`

No public publication or private-file exposure is intended. Source files remain read-only.
