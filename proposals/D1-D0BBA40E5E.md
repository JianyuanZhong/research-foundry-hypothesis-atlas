# Episode 19: falsification and stopping result for the late acidemic SpO2 mortality hypothesis

## Resolution, clinical importance, and advance

The unresolved claim inherited from Episode 18 was whether, among invasively ventilated adults with an eligible acidemic SpO2/PaO2 pair strictly after ICU hour 24 and by hour 72, recorded SpO2 94–95% rather than 96–97% identifies an absolute hospital-mortality risk at least 10 percentage points higher after standardization for first-day APACHE-IVa predicted hospital mortality, hospital, charted FiO2, PaCO2, pH, and index time.

This is a noncausal prognostic comparison of recorded phenotypes. It is not an effect of assigning an oxygen target, changing FiO2, obtaining an ABG, treating acidemia, or spending time in either saturation band.

The strongest evidence before this experiment supported feasibility and a measurement association only. The lineage reproducibly yielded 556 eligible observations, 440 earliest-stay indices, and 156 exact-cell overlap stays; lower and higher SpO2 bands mapped differently to concurrent PaO2 categories. Episode 18 then audited 164 post-24-hour indices, 158 APACHE-covered indices, and a 126-person, nine-hospital measured-overlap cohort. Its weighted mortality point diagnostic was −16.75 points, but no inferential interval existed, so it supported no mortality conclusion.

The experiment tests the locked hypothesis

[
Delta=P_w(D=1mid L=1)-P_w(D=1mid L=0)ge 0.10,
]

where (L=1) denotes recorded SpO2 94–95%, (L=0) denotes 96–97%, and (D) is future hospital death. The +10-point margin is a predeclared material prognostic anchor, not a validated MCID or treatment-effect margin.

The substantive advance is a completed falsification. The exact 5,000-copy hierarchical bootstrap gave (Delta=-0.16755), 95% percentile interval −0.52913 to +0.02370, with 5,000/5,000 replicates defined. Because the upper bound is below +0.10, the material prognostic-harm hypothesis is adverse/falsified. Because the interval includes zero, the direction remains unresolved: this is not evidence that lower oxygenation is protective. The correct decision is to stop promoting or refining this same EICU phenotype as a ≥10-point mortality-risk trigger. A new mortality claim would require external, synchronized prospective data, not another threshold search in this selected snapshot.

## Population and temporal lock

Use all rows, without sampling, from EICU snapshot `[source checksum]`.

1. From `patient`, include adults age >=18 (`age='> 89'` becomes 90 only for eligibility), `unitvisitnumber=1`, and nonmissing `unitdischargeoffset`. If duplicated `patienthealthsystemstayid` values occur, retain the smallest `patientunitstayid`; the full-source audit found none among eligible unit-visit-1 rows.
2. In `lab`, require `labtypeid=7` and exact `labname` in {`paO2`, `pH`, `paCO2`}. Valid ranges are PaO2 20–760 mm Hg, pH 6.80–7.80, and PaCO2 10–150 mm Hg. At `patientunitstayid + labresultoffset + labname`, retain greatest numeric `labresultrevisedoffset`, then greatest `labid`; exclude an analyte-time if distinct valid values remain tied at the retained revision. Pivot exact-offset PaO2+pH+PaCO2. Exact offset is a panel proxy, not verified common arterial specimen.
3. Set `draw=labresultoffset` and require `1440 < draw <= min(4320, unitdischargeoffset)`. This makes first-day APACHE inputs pre-index but cannot establish when the released prediction row was available clinically.
4. Require probable invasive ventilation at draw from `respiratoryCare`: exact `airwaytype` in {`Oral ETT`, `Nasal ETT`, `Tracheostomy`, `Double-Lumen Tube`, `Cricothyrotomy`}; `ventstartoffset<=draw`; and either a positive interval with `draw<=ventendoffset`, or `ventendoffset=0` with `draw<=respcarestatusoffset`.
5. From `respiratoryCharting`, require exact `respchartvaluelabel='FiO2'`, `draw-30<=respchartoffset<=draw`, and `respchartentryoffset<=draw`. Convert 0.21–1.00 to percent, retain 21–100, and choose greatest `respchartoffset`, then `respchartentryoffset`, then `respchartid`. Parse RFC CSV quoting strictly and stop on malformed records.
6. In `vitalPeriodic`, retain all `sao2` 70–100 in `draw-5<=observationoffset<=draw` and take their median including duplicate offsets. Lower band is 94, 94.5, or 95; higher is 96, 96.5, or 97; exclude 95.5. Require pH<7.35 and complete valid PaCO2.
7. Select the smallest qualifying post-24-hour draw within each `patientunitstayid` before inspecting APACHE, outcome, PaO2 category, or care limitation. Earlier eligible pairs do not disqualify the primary index.
8. Join one and only one `apachePatientResult` row on `patientunitstayid` with `apacheversion='IVa'` and numeric `predictedhospitalmortality` in [0,1]. Stop on duplicate/conflicting valid IVa rows. Never use `actualhospitalmortality`, `actualicumortality`, actual LOS, or actual ventilation fields.
9. Define death only from `patient.hospitaldischargestatus='Expired'` and survival only from exact `Alive`; require `hospitaldischargeoffset>draw`.
10. Before outcome modeling, retain only hospitals with at least one index patient in each SpO2 band. This outcome-blind gate yields 126 unique people in nine hospitals: 45 lower-band patients (13 deaths) and 81 higher-band patients (37 deaths).

The target is late, ABG-selected, acidemic, invasively ventilated, APACHE-scoreable patients in hospitals showing both recorded bands. It excludes one-band hospitals and is not transportable by assumption.

## Estimator, uncertainty, and computed baselines

Fit an unpenalized logistic exposure model without death or PaO2:

[
operatorname{logit}P(L=1mid X)=alpha+gamma_h+
eta_1operatorname{logit}(operatorname{clip}(r_{APACHE},.005,.995))+
eta_2 FiO2+eta_3 PaCO2+eta_4 pH+eta_5 draw .
]

Standardize continuous terms with the primary-cohort population SD and use (H-1) hospital indicators. Assign overlap weight (1-e_i) to lower-band and (e_i) to higher-band patients, normalize within band, and estimate lower-minus-higher hospital-death risk difference. This is measured-overlap standardization, not a causal propensity-score effect.

For uncertainty, use seed 20260918 and 5,000 replicates. Sample the nine original hospitals with replacement and create distinct hospital-copy IDs. Within each copied hospital and band, sample `uniquepid` clusters with replacement, preserve the original cluster count, create person-copy IDs, re-standardize, refit with copy indicators, and recompute the RD. Report defined failures and the 2.5th/97.5th percentiles.

The primary model converged in 64 iterations. Risks were 29.96% lower-band and 46.72% higher-band; RD −16.75 points. Previously audited diagnostics remain: ESS 43.49/75.34, no propensity outside .05–.95, maximum site weight 39.19%, and maximum absolute clinical/site SMD approximately (2.3	imes10^{-8}/1.65	imes10^{-7}). The independent rerun reproduced the propensity range 0.09675–0.66440 and produced 5,000/5,000 defined bootstrap values.

Outcome baselines were also adverse-looking: before APACHE restriction, raw mortality was 31.67% lower versus 39.42% higher (RD −7.76 points; n=164); among 158 APACHE-covered patients it was 32.20% versus 41.41% (RD −9.21). Broader ridge-overlap diagnostics at C=.1, 1, and 10 were −8.59, −9.60, and −13.67 points. All nine leave-one-hospital-out primary refits remained negative, ranging from −23.38 to −10.40 points. These checks strengthen the stopping interpretation but do not prove an opposite biological effect.

## Treatment-limitation sensitivity

A prespecified interpretive sensitivity uses `carePlanGeneral`, never the outcome, and flags any row with `cplgroup='Care Limitation'`, `cplitemoffset<=draw`, and exact `cplitemvalue` in {`Do not resuscitate`, `No CPR`, `No intubation`, `Comfort measures only`, `No cardioversion`, `No vasopressors/inotropes`, `No augmentation of care`, `No blood products`, `No blood draws`}. Twelve primary patients were flagged, six in each band. Excluding them and reapplying same-hospital band overlap left 111 patients in eight hospitals and RD −15.37 points.

This is only a recorded-documentation exclusion. Absence of a flag is not adjudicated unrestricted goals, and sparse `carePlanEOL` coverage cannot repair missing goals-of-care data. Post-index limitation records must not be adjusted for because they may be consequences of deterioration or prognosis.

## Falsification and interpretation rules

- Supportive: lower 95% bound >=+0.10 and all feasibility/balance gates pass. Conclude only material noncausal prognostic enrichment in this overlap population.
- Adverse: upper 95% bound <+0.10. The ≥10-point hypothesis is falsified. If the interval crosses zero, direction remains unresolved; if wholly below zero, report an opposite observed association without protection/benefit language.
- Inconclusive: interval includes +0.10, >10% bootstrap failures, or model/overlap failure without robust adverse evidence.
- The observed result is adverse: −16.75 points (−52.91,+2.37). It cannot support “no association,” equivalence, protection, benefit, safety, a lower target, or reduced ABG use.

## Exact source bindings

All are read-only ordinary `.csv.gz` files with no nested archive member under `[internal dataset path]`.

- `patient.csv.gz` / `patient`, [source checksum]: `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `age`, `hospitalid`, `unitvisitnumber`, `unitdischargeoffset`, `unitdischargestatus`, `hospitaldischargeoffset`, `hospitaldischargestatus`.
- `lab.csv.gz` / `lab`, [source checksum]: `labid`, `patientunitstayid`, `labresultoffset`, `labresultrevisedoffset`, `labtypeid`, `labname`, `labresult`.
- `respiratoryCare.csv.gz` / `respiratoryCare`, [source checksum]: `respcareid`, `patientunitstayid`, `respcarestatusoffset`, `airwaytype`, `ventstartoffset`, `ventendoffset`.
- `respiratoryCharting.csv.gz` / `respiratoryCharting`, [source checksum]: `respchartid`, `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respchartvaluelabel`, `respchartvalue`.
- `vitalPeriodic.csv.gz` / `vitalPeriodic`, [source checksum]: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `sao2`.
- `apachePatientResult.csv.gz` / `apachePatientResult`, [source checksum]: `apachepatientresultsid`, `patientunitstayid`, `apacheversion`, `acutephysiologyscore`, `apachescore`, `predictedhospitalmortality`.
- `carePlanGeneral.csv.gz` / `carePlanGeneral`, [source checksum]: `cplgeneralid`, `patientunitstayid`, `activeupondischarge`, `cplitemoffset`, `cplgroup`, `cplitemvalue`.

Event tables join on `patientunitstayid`; repeat-person uncertainty uses `uniquepid`; site uses `hospitalid`; offsets are ICU-relative minutes.

## Evidence, missing data, and verifier boundary

The inspected Ding and Chen full-text XML (Critical Care 2025; DOI `10.1186/s13054-025-05754-4`; PMCID `PMC12587580`; frozen source `[source checksum]`) supports that SF/PF discordance can differ in prognostic discrimination, but its 582 MIMIC-IV ARDS patients, first <24-hour pair, and 28-day outcome do not answer this acidemic EICU question; its supplementary methods were not inspected here. The inspected OXY-BREATHES full-text XML (Nguyen et al., Critical Care Medicine 2026; DOI `10.1097/CCM.0000000000007031`; PMCID `PMC13134654`; frozen source `[source checksum]`) reports nine RCTs/20,447 patients and pooled 90-day mortality RR 1.01 (0.94–1.09); heterogeneous strategies and subgroups forbid translating this phenotype association into a target effect. The research-ambition README and availability limits were inspected; no demonstration paper was used as substantive evidence.

EICU lacks verified arterial specimen identity, co-oximetry, waveform/artifact flags, device calibration, delivered FiO2, oxygen-target intent/duration, complete goals-of-care adjudication, exact/cause of death, and post-discharge mortality. APACHE has no result timestamp and may be selected or miscalibrated. Landmark survival, ABG ordering, and one-band-hospital exclusion remain selection mechanisms.

The verifier can check hashes/headers, exact filters/joins/times, 556/440/156 and 164/158/126 reconciliations, forbidden-column non-use, exposure model, weights, bootstrap copy IDs, interval, care-limitation timing, leave-site-out values, and result-linked interpretation. It cannot prove clinical truth, specimen/ventilation validity, complete goals of care, causal effects, equivalence, safety, target choice, device validity, utility, or transportability.

Fixtures: RD +15 (+11,+21) with all gates passes only the stated prognostic support; +6 (+2,+9) is adverse to +10 but smaller positive association; −3 (−12,+6) is adverse with unresolved direction; −12 (−20,−4) is opposite observed association without protection; +12 (−3,+24) is inconclusive. Any causal, safety, target, device, routine-ABG, or equivalence conclusion must fail even when computation is correct.

All four configured datasets remain directly accessible read-only. This experiment uses EICU only; derived aggregates remain in the workspace, and no clinical row, note, identifier, or private aggregate was sent to public search.
