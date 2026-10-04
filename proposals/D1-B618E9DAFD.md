# Episode 15: does the apparent acidemic PaO2 60–89 gain survive a 70-mm Hg lower boundary?

## Unresolved question, clinical importance, and substantive advance

For invasively ventilated adults with concurrent acidemia, does released monitor SpO2 94–95%, rather than 96–97%, map at least 10 percentage points more often to observed PaO2 70–89 mm Hg while limiting the increase in observed PaO2 <70 to less than 10 points?

This is a concurrent three-category mapping question: PaO2 <70, 70–89, and >=90 mm Hg. It is not a safety, harm, benefit, target-assignment, or treatment-effect question. A PaO2 below 70 is called only “below the selected boundary,” not hypoxic injury. Likewise, PaO2 >=90 is an upper mapping category, not “hyperoxemia.”

The episode-14 parent used <60, 60–89, and >=90. Its strongest supported result was feasibility plus an uncertain +12.878-point 60–89 contrast; its <60 component had only 7 versus 5 raw events and a 95% interval from −10.724 to +12.525 points. Thus neither a bounded severe tail nor a target recommendation was supported. The important unresolved possibility was that the favorable 60–89 aggregate could be concentrated immediately above 60 rather than in a more defensible arterial range.

The 70-mm Hg boundary is externally anchored but not validated as an outcome. Hohmann et al. (Respiration 2025; DOI 10.1159/000549732; PMCID PMC12885501) suggest SaO2/SpO2 92–96% or PaO2 70–90 mm Hg in invasively ventilated patients. The exact frozen full-text XML was reacquired, but because passage targeting did not expose the complete body, this proposal does not claim that its full body or supplement was manually inspected. The inherited, inspected OXY-BREATHES review (Nguyen et al., Critical Care Medicine 2026; DOI 10.1097/CCM.0000000000007031; PMCID PMC13134654) found similar overall 90-day mortality across heterogeneous conservative and liberal strategies in nine RCTs/20,447 patients. The inherited, inspected Delgado study (Antioxidants 2026; DOI 10.3390/antiox15020235; PMCID PMC12938712) supports pH-dependent SpO2–PaO2 mapping plausibility. None identifies an acidemia-specific target or validates 70, 90, or the 10-point margins for clinical decisions. The 70 lower edge is the external anchor; exact PaO2 90 remains in the inherited upper category, so the analytic 70–89 interval is not claimed to reproduce the guideline range literally.

The boundary was selected because 70 is the lower edge of that contemporary guideline range and, in the frozen overlap cohort, it provides 37 versus 15 below-boundary observations—more than four times the parent’s 12 total <60 events. The feasibility screen also evaluated 60, 65, 75, and 80. Sixty and 65 remained sparse in the higher band (5 and 6 events); 75 and 80 had support but lack the same lower-edge interpretation and make the middle category increasingly narrow. These alternatives remain diagnostics and cannot rescue the primary. Because the same EICU snapshot informed this refinement and its reference estimate, episode 15 is hypothesis-generating; percentile intervals do not erase boundary-selection uncertainty. Independent validation must be prospectively frozen.

### Evidence-supported claim versus hypothesis tested

The strongest evidence presently supports: the exact 556-row EICU construction and 199-row measured-overlap analysis are computable; the parent’s favorable 60–89 point estimate is highly boundary-sensitive; and the guideline-anchored <70 category has substantially more observed support than <60.

The unresolved joint hypothesis tested is:

- (M_{70}=P(70\le PaO2<90\mid SpO2\ 94\text{–}95)-P(70\le PaO2<90\mid SpO2\ 96\text{–}97)\ge +0.10); and
- (L_{70}=P(PaO2<70\mid SpO2\ 94\text{–}95)-P(PaO2<70\mid SpO2\ 96\text{–}97)<+0.10).

Both components are required and neither can rescue the other. The common 10-point absolute margins make the desired middle-category gain material while disallowing a comparably large below-boundary increase. They are decision anchors, not MCIDs or validated utility thresholds. The estimand compares recorded observations in symmetric measured overlap; it does not compare assigned targets.

## Exact population and temporal construction

Use every row, without sampling, from EICU snapshot `[source checksum]`.

1. From `patient`, retain numeric age >=18, mapping released `> 89` to 90 only for adjustment; require `unitvisitnumber=1` and nonmissing `unitdischargeoffset`. Within `patienthealthsystemstayid`, retain the smallest `patientunitstayid` if duplicated. The source audit found 157,883 eligible rows and 157,883 distinct health-system stays, so this tie rule removes none. This is the first recorded ICU unit visit in a health-system stay, not lifetime-first admission.
2. From `lab`, require `labtypeid=7` and exact `labname` in {`paO2`, `pH`, `paCO2`}. Valid ranges are PaO2 20–760 mm Hg, pH 6.80–7.80, and PaCO2 10–150 mm Hg. Within `patientunitstayid + labresultoffset + labname`, retain greatest numeric `labresultrevisedoffset`, then greatest `labid`; exclude an analyte-time if rows tied at the retained revision contain distinct valid values. Pivot exact-offset PaO2+pH, with PaCO2 optional. Set `draw=labresultoffset`. Exact offset is a panel proxy, not proof of one arterial specimen.
3. Require `0 <= draw <= min(4320, unitdischargeoffset)`.
4. In `respiratoryCare`, require exact `airwaytype` in {`Oral ETT`, `Nasal ETT`, `Tracheostomy`, `Double-Lumen Tube`, `Cricothyrotomy`}, `ventstartoffset<=draw`, and either `ventendoffset>ventstartoffset` with `draw<=ventendoffset`, or `ventendoffset=0` with `draw<=respcarestatusoffset`. This is probable, unadjudicated invasive ventilation.
5. In `respiratoryCharting`, require exact `respchartvaluelabel='FiO2'`, `draw-30<=respchartoffset<=draw`, and `respchartentryoffset<=draw`. Parse numeric values, convert 0.21–1.00 to percent, and retain 21–100 before ranking. Choose greatest chart offset, entry offset, then `respchartid`. This ordering matches the audited code. Parse RFC CSV quoting (`quote='"', escape='"'`); strict full-source parsing must stop and report any malformed record rather than silently skipping it. This is charted, not delivered, FiO2.
6. In `vitalPeriodic`, retain every `sao2` 70–100 with `draw-5<=observationoffset<=draw`; take the median including duplicate offsets and half-point medians. Lower band is 94, 94.5, or 95; higher band is 96, 96.5, or 97. Exclude 95.5. These are released five-minute summaries, not waveform or arterial saturation.
7. Require pH<7.35 and one assigned band. Keep every eligible observation without selecting on PaO2, multiplicity, future fields, or hospital outcome counts.

Reconcile 556 observations: 227 lower and 329 higher, 440 stays, 439 people, 41 hospitals. SpO2 counts are 94:84, 94.5:12, 95:131, 96:163, 96.5:12, 97:154; report the inherited 12 acidemic observations at 95.5 excluded before inference.

## Outcome-blind overlap, variables, and estimands

Before using PaO2 categories, create a typed cell among the 556 rows from integer `hospitalid`; integer `floor(FiO2_percent/10)`; PaCO2 missing as a typed level or integer `floor(PaCO2/20)`; pH stratum <7.20, 7.20–7.29, or 7.30–7.349…; and integer `floor(draw/1440)` for ICU day 0, 1, or 2. Retain cells with at least one observation in each SpO2 band.

Reconcile 199 rows, 55 cells, 171 stays, 171 people, and 11 hospitals {122,181,182,183,184,420,440,443,444,458,459}: 85 lower and 114 higher observations. PaO2 and category event counts never define cells.

For cell s with nLs lower and nHs higher observations, assign lower rows (nHs/(nLs+nHs)) and higher rows (nLs/(nLs+nHs)), then normalize separately by band. Report weight sums, ESS, maximum normalized row weight, and original-hospital total-weight fractions.

Partition every PaO2 into exactly one of <70, 70–89.999…, or >=90. Report raw counts/noncounts, weighted risks summing to one by band, (L_{70}), (M_{70}), and (U_{90}=P(PaO2\ge90|lower)-P(PaO2\ge90|higher)). The compositional identity (L_{70}+M_{70}+U_{90}=0) must hold to numerical tolerance.

The minimum observed-support diagnostic is at least 15 category events and 30 non-events per band for each co-primary. It is a feasibility floor, not proof of adequate clinical power. The primary passes: <70 has 37/15 events and 48/99 non-events in lower/higher; 70–89 has 34/65 events and 51/49 non-events. Report these counts rather than hiding the higher-band boundary count of 15.

## Baselines, uncertainty, and diagnostics

Fixed baselines are unweighted three-category risks in all 556 eligible observations and symmetric overlap without pH strata. Secondary threshold partitions are <60/60–89/>=90, <65/65–89/>=90, <75/75–89/>=90, and <80/80–89/>=90. Split >=90 into 90–120 and >120, and report weighted quantiles, full range, and E[min(PaO2,120)]. None can replace a primary component or rename a category as safety/harm/benefit.

Use 5,000 deterministic hierarchical bootstrap replicates, seed 20260915, conditional on the frozen 199-row overlap source:

1. sample its 11 hospitals with replacement, taking 11 hospital copies;
2. within each copy sample that original hospital’s number of `uniquepid` clusters with replacement, carrying every row;
3. assign new hospital-copy and person-copy IDs;
4. rebuild cells using hospital-copy ID, drop copied cells lacking either band, recompute weights and all category risks.

Report defined/failed replicates and separate percentile two-sided 95% intervals. Pooling duplicate copies under original IDs is an error. Support requires <=10% failed replicates, ESS >=50 in each band, the raw-support floor, no original hospital >50% total weight, and no required sensitivity or deletion of a hospital with >=10 rows making (M_{70}\le0) or (L_{70}\ge+0.10). A failure cannot create support.

Mandatory outcome-blind rebuilt sensitivities are earliest row/person, earliest row/stay, first 24 hours, complete PaCO2, 12-hour time cells, five-point FiO2/ten-mm Hg PaCO2 cells, no pH cells, 0.10-pH cells, 0.05-pH cells, and each-site deletion. Extraction diagnostics inherited for compilation are last rather than median SpO2, 60-minute FiO2 lookback, chart-offset FiO2 without entry restriction, closed nonzero ventilation intervals, alternate FiO2 labels, and broader airway proxy; each must rebuild eligibility and overlap and report counts before estimates. Reference execution below covers the primary and the nine outcome-blind rebuilds, not these six extraction variants. Any discrepancy must be reported and cannot be silently folded into the primary.

## Full-source reference result

The audited full-source reconstruction exactly reproduced 556/199 rows and the parent’s weights. Weight sums are 42.4127 per band; ESS is 75.98 lower and 96.00 higher; the maximum normalized row weights are 2.021% and 1.886%; maximum original-site total-weight fraction is 39.73%.

Weighted three-category risks are:

- lower SpO2 94–95: 42.270% <70, 43.217% 70–89, 14.513% >=90;
- higher SpO2 96–97: 13.243% <70, 55.082% 70–89, 31.675% >=90.

Therefore (L_{70}=+29.027) points (95% interval +2.697 to +45.321), (M_{70}=-11.866) points (−35.168 to +6.859), and (U_{90}=-17.161) points (−31.536 to +12.200), with 5,000/5,000 defined replicates. The parent’s +12.878-point 60–89 estimate decomposes at the point-estimate level into +24.744 points for 60–69 and −11.866 points for 70–89.

All nine computed outcome-blind sensitivities kept (L_{70}) positive (+22.823 to +35.730) and (M_{70}) negative (−16.787 to −2.976). Every site deletion kept (L_{70}) positive (+24.598 to +30.566) and (M_{70}) negative (−13.819 to −10.251). These are same-snapshot robustness checks, not independent replication.

The valid reference interpretation is: **adverse to the +10-point 70–89 relocation component, with evidence of increased <70 mapping but unresolved magnitude relative to its +10-point cap; the joint hypothesis is falsified.** (M_{70})'s upper bound is below +10, although its interval crosses zero, so direction itself is not resolved by the bootstrap. (L_{70})'s interval is wholly above zero but crosses +10. This does not establish hypoxic injury, unsafe care, a causal target effect, or benefit of the higher band. The strongest advance is that the parent’s apparently favorable 60–89 relocation does not persist when the middle category begins at the clinically anchored 70 boundary.

## Falsification and result-linked conclusions

Support for the joint hypothesis requires (M_{70})'s lower bound >=+10, (L_{70})'s upper bound <+10, and all gates. The strongest allowed conclusion is limited to concurrent recorded category mapping and may justify prospective synchronized validation.

Adverse to material relocation means (M_{70})'s upper bound <+10. If its interval is wholly below zero, report opposite-direction middle-category mapping; if it crosses zero, report unresolved direction but adversity to +10. Adverse to the below-boundary cap means (L_{70})'s lower bound >=+10. If its interval is wholly above zero but crosses +10, report increased below-boundary mapping with unresolved material magnitude. Either adverse component falsifies the joint hypothesis.

Inconclusive includes either interval crossing its margin, a mandatory gate failure, or required sensitivity conflict, unless a component already meets its adverse rule and that adverse direction is robust. Support for one component with the other inconclusive leaves the joint claim inconclusive. A negative finding is valid and cannot be penalized by the verifier.

Verifier fixtures:

- M +15 (95% +11,+21), L +3 (−2,+8), all gates pass: limited support for the concurrent joint mapping only.
- M −12 (−35,+7), L +29 (+3,+45): adverse to +10 relocation; increased <70 mapping with cap magnitude unresolved; joint falsified. Reject “unsafe,” “harm,” and target advice.
- M +6 (+2,+9), L +2 (−1,+5): smaller positive middle mapping adverse to +10, not “no association.”
- M +14 (+11,+20), L +16 (+12,+22): relocation supported, below-boundary cap adverse, joint falsified.
- M +14 (+11,+20), L +6 (−2,+14): relocation supported, cap inconclusive, joint inconclusive.
- M −8 (−15,−2), L +15 (+11,+20): opposite middle mapping and adverse cap; do not translate to causal harm.
- Correct computation paired with a lower/higher SpO2 recommendation, causal FiO2 effect, tissue oxygenation, oxidative toxicity, ischemia, mortality benefit, device validity, or proof of safety must fail.
- Correct estimates with conclusions unsupported by their intervals/margins must fail; appropriate supportive, adverse, and inconclusive interpretations must pass.

## Exact source bindings and evidence limits

All sources are read-only ordinary `.csv.gz` files with no nested archive member under `[internal dataset path]`.

- `patient.csv.gz` / table `patient`, [source checksum]: `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `age`, `hospitalid`, `unitvisitnumber`, `unitdischargeoffset` (descriptive `gender`, `unittype`, `unitadmitsource` optional).
- `lab.csv.gz` / `lab`, [source checksum]: `labid`, `patientunitstayid`, `labresultoffset`, `labresultrevisedoffset`, `labtypeid`, `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`, `labmeasurenameinterface`.
- `respiratoryCare.csv.gz` / `respiratoryCare`, [source checksum]: `respcareid`, `patientunitstayid`, `respcarestatusoffset`, `airwaytype`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`.
- `respiratoryCharting.csv.gz` / `respiratoryCharting`, [source checksum]: `respchartid`, `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`.
- `vitalPeriodic.csv.gz` / `vitalPeriodic`, [source checksum]: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `sao2`.
- `hospital.csv.gz` / `hospital`, [source checksum]: `hospitalid`, `numbedscategory`, `teachingstatus`, `region`; descriptors only.

Event tables join to `patient` on `patientunitstayid`; repeated people cluster on `uniquepid`; `hospitalid` comes from `patient`. Event offsets are minutes from ICU admission. The complete catalog schemas and actual source headers contain every required field.

EICU lacks verified arterial specimen identity, arterial saturation, waveform synchronization/artifact, device make/calibration, delivered FiO2, temperature, 2,3-DPG, exact ventilation persistence, clinician target/intent, treatment timing, tissue oxygenation, injury outcomes tied to the measurement, and a missing-at-random ABG mechanism. Clinical adjudication is required for specimen and ventilation truth and implausible values. Prospective synchronized data are required to validate mapping; independent data are required to validate the selected boundary; an assigned-target trial with exposure duration, rescue criteria, and patient-centered outcomes is required for safety or benefit.

The verifier can check hashes/headers, exact labels/ranges, joins, revision ties, temporal inequalities, valid-before-ranking FiO2, median SpO2 and 95.5 exclusion, 556/199 counts, typed cells, weights, category identities, raw support, copied bootstrap IDs, intervals, diagnostics, sensitivities, and whether conclusions follow from computed outputs. It cannot adjudicate unavailable clinical facts, validate the margins or guideline boundary, remove confounding/selection, establish transportability, causality, safety, or benefit. Reference execution establishes computability and disciplined interpretation, not scientific truth.

All four configured datasets—HCC, MIMIC, EICU, and UKB—remain directly accessible read-only, including permitted rows and notes. This experiment uses EICU only; derived aggregate files remain in the workspace and no clinical record was sent to public search.
