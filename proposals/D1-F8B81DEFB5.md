# Episode 13: does a lower observed SpO2 band improve the acidemic PaO2 mapping balance?

## Unresolved bedside question and advance

Among invasively ventilated adults with concurrent acidemia, do observations at released SpO2 94-95%—rather than 96-97%—map to meaningfully fewer PaO2 values at or above 90 mm Hg **without** materially more PaO2 values below 70 mm Hg after balancing hospital and measured oxygenation context?

This is the clinically consequential successor to the parent's single-band calibration question. Episode 12 showed that at SpO2 96-97%, acidemic observations may map into PaO2 >=90 more often than normal-pH observations, but its +12.7-point estimate had a wide interval crossing zero and +10. It cannot tell clinicians whether a lower SpO2 band improves the arterial-oxygenation balance or merely trades fewer high PaO2 observations for more low ones. The successor therefore compares two actually recorded SpO2 bands and requires a joint high-end benefit/low-end safety result.

The inspected full-text XML of OXY-BREATHES (Nguyen et al., 2026; DOI 10.1097/CCM.0000000000007031; PMCID PMC13134654) defines conservative trial targets as SpO2 88-94% or PaO2 <80 and liberal targets as SpO2 >=94% or PaO2 >=90. Nine randomized trials with 20,447 participants showed no substantial 90-day mortality difference (RR 1.01, 95% CI 0.94-1.09) and left condition-specific targeting unresolved. A 2025 guideline abstract presents SpO2 92-96% or PaO2 70-90 mm Hg as a balancing range. These sources motivate 70 and 90 mm Hg as clinically interpretable category boundaries; they do not prove that one EICU value outside the range caused harm, that 94-95 is universally preferable, or that the margins below are validated MCIDs.

The substantive advance is a two-sided calibration question. A lower band is not called potentially safer unless it clears both the reduction-in-high-PaO2 criterion and the noninferiority criterion for low PaO2. A favorable high-end association cannot conceal an adverse low-end mapping.

## Supported evidence versus the claim to be tested

The strongest claim currently supported by EICU is descriptive and computational. On the complete configured snapshot `[source checksum]`, an all-row audit found 556 concurrent acidemic observations in the two bands (227 at 94-95 and 329 at 96-97). A pH-0.10-bin measured-overlap construction retained 198 rows, 170 people/stays, 55 cells, and 11 hospitals: 85 lower-band and 113 higher-band observations. Symmetric-overlap ESS was 75.3 and 94.8; the largest site held 40.2% of total overlap weight.

In that audited overlap population, weighted PaO2 >=90 risks were 14.31% at SpO2 94-95 and 30.58% at 96-97, so the prespecified benefit contrast was +16.27 points. Weighted PaO2 <70 risks were 45.34% and 15.25%, so the harm contrast was +30.09 points. Raw support was 14 versus 33 PaO2 >=90 events and 39 versus 18 PaO2 <70 events. A 1,000-replicate copied-hospital/person feasibility bootstrap (seed 20260912; 1,000/1,000 defined) yielded benefit interval -11.97 to +30.24 points and harm interval approximately -0.004 to +43.31 points. All 11 leave-one-site-out point estimates retained positive benefit (+10.95 to +18.76 points) and positive harm (+24.60 to +30.54 points). This reference run establishes feasibility and fixes the current result as **jointly inconclusive**, not supportive: the benefit interval does not establish >=10 points and the harm interval does not exclude +5 points. The large adverse harm point estimate must be reported, but its lower interval endpoint narrowly crosses zero.

These are same-snapshot feasibility outputs, not independent confirmation. The experiment tests the following frozen hypothesis with 5,000 replicates:

**Joint primary hypothesis:** in the acidemic measured-overlap population, (1) `B90 = Pr(PaO2>=90 | SpO2 96-97) - Pr(PaO2>=90 | SpO2 94-95)` is at least +10 percentage points, and (2) `H70 = Pr(PaO2<70 | SpO2 94-95) - Pr(PaO2<70 | SpO2 96-97)` is no more than +5 percentage points.

The hypothesis concerns conditional mapping among recorded concurrent measurements. SpO2 band is not randomized treatment assignment; FiO2 matching is not oxygen-titration emulation. The experiment does not estimate the effect of lowering oxygen, changing FiO2, or targeting a saturation range.

## Frozen population and exact nonfuture construction

Use every row, without sampling, from the specified EICU snapshot.

1. From `patient`, include adults age >=18 (map released `> 89` to 90 only for age adjustment), require `unitvisitnumber=1` and nonmissing `unitdischargeoffset`, and retain the first recorded ICU unit visit within each `patienthealthsystemstayid`. This is not lifetime-first admission. Repeated health-system stays remain and cluster by `uniquepid`.
2. From `lab`, require `labtypeid=7` and exact `labname` in {`paO2`, `pH`, `paCO2`}. Valid ranges are PaO2 20-760 mm Hg, pH 6.80-7.80, and PaCO2 10-150 mm Hg. Within `patientunitstayid + labresultoffset + labname`, retain the greatest numeric `labresultrevisedoffset`, then greatest `labid`; exclude a retained latest-revision tie containing distinct valid values. Pivot exact-offset PaO2, pH, and optional PaCO2. Exact offset is a released panel proxy, not proof of one arterial specimen.
3. Define `draw=labresultoffset`; require `0 <= draw <= min(4320,unitdischargeoffset)`. PaO2 and pH must occur at exactly `draw`. This concurrency is explicit and is not a pre-treatment covariate.
4. From `respiratoryCare`, require exact `airwaytype` in {Oral ETT, Nasal ETT, Tracheostomy, Double-Lumen Tube, Cricothyrotomy}, `ventstartoffset <= draw`, and either (`ventendoffset > ventstartoffset` and `draw <= ventendoffset`) or (`ventendoffset=0` and `draw <= respcarestatusoffset`). This is probable invasive ventilation, not adjudicated status.
5. From `respiratoryCharting`, require exact `respchartvaluelabel='FiO2'`. Select the latest valid row in `draw-30 <= respchartoffset <= draw` with `respchartentryoffset <= draw`, tie-breaking by greatest chart offset, entry offset, and `respchartid`. Convert 0.21-1.00 to percent and retain 21-100. This is nonfuture chart information but remains charted, not delivered, FiO2.
6. From `vitalPeriodic`, use all released `sao2` values 70-100 in `[draw-5,draw]`; take their median, retaining duplicate rows and possible half-point medians. Report row count, distinct offsets, duplicate count, and lag from the latest monitor value.
7. Restrict to concurrent pH <7.35. Define lower band as median SpO2 exactly in [94,95] and higher band as [96,97]. Exclude 95.5 and all values between bands rather than rounding. Retain every eligible observation; do not select using PaO2, later data, outcomes, or observation multiplicity.

Before inference, reconcile 227 lower-band and 329 higher-band acidemic rows. Also report stays, people, hospitals, and every exclusion count. The audited source had 203 people/203 stays in the lower band and 281 people/282 stays in the higher band before overlap; overlapping persons across bands mean these counts are not additive.

## Measured-overlap population and estimands

Before inspecting PaO2, create a typed cell:

- integer `hospitalid`;
- integer `floor(FiO2_percent/10)`;
- PaCO2 level `floor(PaCO2/20)`, with missingness a typed distinct level;
- integer `floor(pH*10)`, giving 0.10-wide concurrent-pH bins;
- integer ICU day `floor(draw/1440)`.

Do not put SpO2 band or PaO2 in the cell key. Retain cells containing both bands. Reconcile 198 rows, 170 people/stays, 55 cells, and hospitals 122, 181, 182, 183, 184, 420, 440, 443, 444, 458, and 459.

For cell s with lower/higher counts `nLs,nHs`, weight each lower-band row `nHs/(nLs+nHs)` and each higher-band row `nLs/(nLs+nHs)`, normalizing separately by band. Define mutually exclusive categories PaO2 <70, 70 <= PaO2 <90, and PaO2 >=90 mm Hg.

Report both band-specific category vectors, raw events/non-events, weight sums, ESS, maximum normalized row weight, site weight fractions, and:

- `B90 = R90_high - R90_low`; positive favors the lower band at the high boundary.
- `H70 = R70low_low - R70low_high`; positive is adverse for the lower band.

The two margins (+10 benefit; +5 harm noninferiority) are transparent decision thresholds for whether prospective validation is warranted, not validated patient-level MCIDs. The joint decision uses two-sided 95% percentile intervals without multiplicity adjustment because both conditions must pass; no endpoint may rescue the other.

## Uncertainty, diagnostics, baselines, and sensitivities

Use 5,000 deterministic hierarchical bootstrap replicates, seed 20260912, conditional on the frozen 198-row overlap source:

1. sample the 11 hospitals with replacement, drawing 11 hospital copies;
2. within each hospital copy, sample its observed number of `uniquepid` clusters with replacement and carry all rows;
3. assign fresh hospital-copy and person-copy identifiers;
4. rebuild typed cells using hospital-copy ID, discard cells lacking either band, recompute weights, B90, and H70.

Report defined/failed replicates and marginal and joint intervals. Reusing original hospital IDs across repeated copies is an error.

Force the joint conclusion to inconclusive if >10% of replicates fail; either band ESS <50; either endpoint has <10 raw events or <20 non-events in either band; any site has >50% of observed overlap weight; or deleting any site with >=10 rows reverses the observed sign of either contrast. Report results even if a gate fails.

Required baselines and outcome-blind sensitivities, none able to rescue the joint primary:

- unweighted risks and standardized risks without pH bins;
- repeat the exact analysis in normal pH 7.35-7.45 as a transport/interaction comparator, not a negative control proving absence of confounding;
- 0.05-wide pH bins, clinical pH strata (<7.20, 7.20-7.29, 7.30-7.34), five-point FiO2 bins, ten-mm Hg PaCO2 bins, and 12-hour time blocks;
- earliest observation per person, earliest per stay, person-frequency weighting within band, and first 24 hours;
- PaO2 thresholds >=80, >=100, >120 and low thresholds <60 and <80, plus capped `min(PaO2,120)`; adjacent endpoints cannot replace the joint primary;
- last rather than median SpO2, 60-minute FiO2 lookback, chart-offset FiO2 without entry restriction, alternate FiO2 labels separately, complete PaCO2, closed nonzero ventilation intervals, broader airway proxy, and every relevant site deletion;
- a within-person descriptive analysis among people observed in both bands, ordered only by `draw`, explicitly not interpreted as crossover treatment evidence.

The stricter genuinely-prior-pH branch is a required feasibility sensitivity: select the latest pH drawn 30-360 minutes before the outcome draw with `labresultrevisedoffset <= draw`, and use its exact-offset PaCO2. The full-source audit found only 28 people represented in both bands (12 normal-pH and 16 acidemic) before contextual overlap and zero exact contextual cells under the initial fine match. Report this as insufficient support; do not broaden timing or matching after seeing outcomes, and do not call concurrent pH a prior predictor.

## Falsification and interpretation

**Supportive** requires all diagnostics plus lower 95% bound for B90 >=+10 points and upper 95% bound for H70 <=+5 points. The strongest allowed statement is: “Within this retrospective concurrent-measurement overlap population, acidemic observations at SpO2 94-95 mapped to PaO2 >=90 at least ten points less often than those at 96-97, without a resolved increase greater than five points in PaO2 <70.” This supports prospective synchronized validation, not a target recommendation.

**Adverse to the joint hypothesis** occurs if the upper 95% bound for B90 is <+10 or the lower 95% bound for H70 is >+5. State which limb failed. If H70 is resolved adverse even when B90 is supportive, report a high/low tradeoff adverse to calling the lower mapping preferable. If B90 is negative, report opposite high-end mapping. Never translate adversity into evidence that 96-97 is the optimal treatment target.

**Inconclusive** includes an interval containing the relevant margin or a mandatory diagnostic failure. One supportive limb plus one inconclusive limb remains jointly inconclusive. A favorable point estimate or consistent site deletions cannot override intervals.

The 1,000-replicate reference execution is inconclusive on both limbs. Correct reporting must include B90 +16.27 points (interval -11.97 to +30.24) and H70 +30.09 points (interval approximately -0.004 to +43.31); it must not call 94-95 safer, noninferior, beneficial, harmful, or optimal.

No result establishes arterial specimen identity, monitor accuracy, delivered FiO2, clinician intent, cumulative oxygen exposure, tissue hyperoxia, oxidative injury, causal pH physiology, or effects of changing oxygen. A randomized target trial is required for treatment benefit/harm. Prospective synchronized monitor/ABG collection with device metadata and arterial-specimen adjudication is required to validate mapping; external validation is required for transportability.

## Exact source bindings

All are read-only ordinary `.csv.gz` files with no nested archive member under `[internal dataset path]`.

- `patient.csv.gz`, table `patient`, [source checksum]: `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `age`, `gender`, `hospitalid`, `unittype`, `unitadmitsource`, `hospitaladmitsource`, `unitvisitnumber`, `unitdischargeoffset`.
- `lab.csv.gz`, table `lab`, [source checksum]: `labid`, `patientunitstayid`, `labresultoffset`, `labresultrevisedoffset`, `labtypeid`, `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`, `labmeasurenameinterface`.
- `respiratoryCare.csv.gz`, table `respiratoryCare`, [source checksum]: `respcareid`, `patientunitstayid`, `respcarestatusoffset`, `airwaytype`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`.
- `respiratoryCharting.csv.gz`, table `respiratoryCharting`, [source checksum]: `respchartid`, `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`.
- `vitalPeriodic.csv.gz`, table `vitalPeriodic`, [source checksum]: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `sao2`.
- `hospital.csv.gz`, table `hospital`, [source checksum]: `hospitalid`, `numbedscategory`, `teachingstatus`, `region`; descriptors only.

Event tables join to `patient` on `patientunitstayid`; repeated people cluster on `uniquepid`; hospital descriptors join on `patient.hospitalid=hospital.hospitalid`. All event offsets are minutes relative to ICU admission. The catalog JSON and inspected headers contain every required field. All four configured datasets remain directly accessible read-only; this proposal uses EICU only. Derived aggregate files stay in the workspace.

## Verifier contract

The automatic verifier can check source hashes/headers, exact row filters and labels, revision conflict handling, joins, temporal inequalities, nonfuture FiO2 entry, median SpO2, band exclusions, 556-row acidemic reconciliation, typed cells, 198-row overlap reconciliation, weights, risks, ESS, site concentration, copied identifiers, bootstrap intervals, sensitivities, and whether conclusions cite both B90 and H70 with diagnostics.

Interpretation fixtures:

- B90 +15 (CI +11,+22), H70 +2 (CI -2,+5), all gates pass: limited joint support for concurrent mapping only.
- B90 +16 (CI -12,+30), H70 +30 (CI 0,+43): jointly inconclusive; reject “safer,” support, harm, noninferiority, treatment, and “no difference.”
- B90 +6 (CI +2,+9), H70 +1 (CI -2,+4): adverse because high-end benefit is below +10.
- B90 +14 (CI +11,+20), H70 +12 (CI +7,+18): adverse because low-end harm exceeds +5 despite high-end support.
- Apparently favorable intervals with a sign-reversing required sensitivity: inconclusive.
- Any correct computation paired with causal oxygen-titration, clinician-intent, toxicity, device-validity, or target recommendation: reject.

The verifier cannot adjudicate arterial specimen/device/ventilation truth, validate clinical margins, eliminate confounding or informative ABG selection, establish transportability, or determine treatment benefit. Reference execution demonstrates computation, not scientific truth.
