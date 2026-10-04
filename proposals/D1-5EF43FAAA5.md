> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Candidate: Is pH-conditioned hidden hyperoxemia reproducible across EICU hospitals?

## Unresolved question, clinical importance, and advance

A fixed peripheral oxygen-saturation target assumes that a given SpO2 implies a sufficiently similar arterial oxygen tension across patients and hospitals. A large 2026 single-center study found that SpO2 96–97% was generally associated with physiologic PaO2, but acidemia and FiO2 shifted that relationship. The unresolved claim is whether acidemia identifies a clinically large and reproducible hidden-hyperoxemia subgroup at this apparently acceptable saturation in heterogeneous US ICUs.

**Primary falsifiable hypothesis:** among qualifying invasive-ventilation blood-gas observations during the first 72 ICU hours with preceding monitor SpO2 96–97%, concurrent acidemia (pH <7.35), versus pH 7.35–7.45, has a case-mix-standardized probability of PaO2 >120 mm Hg at least 10 percentage points higher. Support also requires a positive standardized contrast in at least 70% of prespecified adequately sized hospitals.

This is a physiologic measurement-transportability study. It can determine whether an SpO2-only target has an important blind spot and whether a prospective protocol using recent pH is warranted. It does **not** test oxygen toxicity, tissue hyperoxia, benefit from lowering oxygen, or a deployable pH-trigger rule: concurrent pH comes from the same blood-gas panel as PaO2. The earlier candidate blurred that distinction, used a catalog-listed patient column absent from the source header, treated respiratory-care zero end-times as ordinary interval ends, required five hospitals with at least 100 target observations when none existed, and combined hospital fixed effects with unseen-hospital validation. This child repairs each defect and extends the observation window from 24 to 72 hours based on feasibility, without weakening the inherited +10-point clinical threshold.

## Strongest supported evidence versus claim tested

Delgado et al. (Antioxidants 2026; DOI 10.3390/antiox15020235) was acquired and its full Europe PMC XML was inspected (source `[source checksum]`, [source checksum]). It supports a same-time, single-tertiary-center association in 21,406 adults and 717,064 paired measurements: SpO2 >=98% frequently indicated PaO2 hyperoxemia; 96–97% was generally physiologic; acidemia and higher FiO2 modified the relation. It does not establish EICU transportability or a +10-point contrast.

Diop and Mounier (Medical Gas Research 2026; DOI 10.4103/mgr.MEDGASRES-D-25-00028) was acquired and its full XML inspected (source `[source checksum]`, [source checksum]). It supports the limitation that PaO2 is not tissue oxygen exposure and that oxygen-target evidence is unsettled.

Parr et al. (J Gen Intern Med 2024; DOI 10.1007/s11606-024-08852-1) was acquired and its full XML inspected (source `[source checksum]`, [source checksum]). Its meta-analysis supports racial/ethnic disparities in *occult hypoxemia*, not hidden hyperoxemia, and motivates checking oximetry calibration heterogeneity. EICU ethnicity is not skin pigmentation and cannot adjudicate device bias.

Thus the strongest existing claim is a single-center concurrent association plus known oximetry heterogeneity. The experiment tests a clinically large, multi-hospital concurrent association. A temporally deployable recent-pH rule remains a separate question.

## Population, index observations, and temporal boundaries

1. Read `patient.csv.gz`. Keep age >=18, mapping `> 89` to 90 only for modeling and reporting it separately. Select `unitvisitnumber=1` within each `patienthealthsystemstayid`; actual profiling found no duplicate visit-1 rows. Do not claim first lifetime admission. Retain repeated health-system encounters and cluster them by `uniquepid`.
2. Candidate index times are `labresultoffset` in [0,4320] minutes. Require same-`patientunitstayid + labresultoffset` rows with `labtypeid=7`, `labname='paO2'`, `labmeasurenamesystem='mm Hg'`, PaO2 20–760, and `labname='pH'`, pH 6.80–7.80. Accept repeated identical values once; if either analyte has more than one distinct in-range value at that key, exclude the panel in the primary analysis. A latest-revision rule using maximum `labresultrevisedoffset`, then `labid`, is sensitivity-only. Pair unambiguous same-offset `paCO2` 10–150 when available. Same offset and type 7 are panel proxies, not specimen identity.
3. Require a single `respiratoryCare` row with exact `airwaytype` in Oral ETT, Nasal ETT, Tracheostomy, Double-Lumen Tube, or Cricothyrotomy; `ventstartoffset <= index`; and either (a) `ventendoffset > ventstartoffset` and `ventendoffset >= index`, or (b) `ventendoffset=0` and `respcarestatusoffset >= index`. This is a conservative computable interpretation of the zero sentinel, not clinically adjudicated ventilation truth. Do not use APACHE ventilation flags for temporal eligibility.
4. From `respiratoryCharting`, select the last row with exact label `FiO2` and `respchartoffset` in [index-30,index], tie-breaking by greatest `respchartentryoffset` then `respchartid`. Convert values <=1 to percent and retain 21–100. Alternate labels `FIO2 (%)` and `Set Fraction of Inspired Oxygen (FIO2)` are sensitivity-only. Report `respchartentryoffset-index`; repeat after requiring entry offset <=index.
5. From `vitalPeriodic`, take the median valid `sao2` 70–100 for `observationoffset` in [index-5,index]. These are released five-minute monitor summaries, not raw waveform or one-minute observations.
6. After all pairing, retain the earliest observation in each stay-specific six-hour block, maximum 12 per stay. No outcome-based sampling. Report every attrition step, observation/stay/person counts, and hospital distributions.

The primary analysis is restricted to median SpO2 96–97 inclusive. Alkalemia is secondary. There is no survival landmark because the outcome is contemporaneous measurement, not prognosis.

## Variables, estimand, outcomes, and baselines

Primary exposure is acidemia versus normal pH. Primary outcome is observed PaO2 >120 mm Hg. Secondary outcomes are PaO2 >150, continuous PaO2, and PaO2 <60 as a safety description. These are arterial blood-gas states, not tissue oxygenation or injury.

The primary estimand is the marginal standardized risk difference for acidemia versus normal pH among observed eligible SpO2 96–97 panels, standardized over their measured FiO2, SpO2, PaCO2, age, sex, and six-hour-block distribution. It is associational, not a causal effect of pH.

Prespecified models are:

- B0: intercept plus SpO2 (96–97) only.
- B1: B0 plus FiO2 per 10%, PaCO2 per 10 mm Hg with a missing indicator, age per decade, sex, and six-hour block.
- B2: B1 plus acidemia and acidemia×FiO2.

Do not add hospital indicators to a model claimed to transport to an unseen hospital. Unit type, admission source, ethnicity, PEEP, APACHE fields, and a FiO2 spline are prespecified sensitivities, not data-driven primary additions.

## Analysis and transportability

Tabulate raw outcome prevalence by integer/median SpO2, pH category, FiO2 band, hospital, and patient denominator. Fit B0–B2 with marginal logistic GEE clustered by `uniquepid`. Derive the B2 standardized risk difference by setting pH category to acidemic and normal for every primary-cohort row and averaging predicted risks. Obtain the primary 95% interval from 1,000 hospital-level bootstrap resamples, refitting the person-clustered model within each sample; report failed fits and declare the bootstrap unreliable if >10% fail.

Internal-external validation uses the nine feasibility-defined hospitals having >=30 SpO2 96–97 observations, >=5 acidemic, and >=10 normal-pH observations. For each, train the fixed, site-agnostic B1/B2 specification on all other hospitals and evaluate the held-out hospital. Report held-out calibration-in-the-large, slope, Brier score, log loss, standardized acidemia contrast, and B2-minus-B1 metrics. Small hospitals contribute to training and the overall estimate but not the sign-consistency denominator. Pool hospital-specific contrasts with random effects and report tau-squared, I-squared, and a 95% prediction interval. The adequate-site rule is based only on exposure counts, not outcomes.

Assess selection from monitor/FiO2 availability by modeling complete pairing among otherwise eligible invasive panels using only pre-index patient, hospital, time-block, and observed respiratory variables. Repeat the primary contrast with stabilized inverse-observation weights truncated at the 1st/99th percentiles. Also repeat with one observation per stay, first 24 hours, entry-time-available FiO2, latest-revision panels, FiO2 lookback 60 minutes, alternate labels, PaO2 >150, complete PaCO2, and hospital leave-one-out deletion. Ethnicity-stratified calibration is descriptive only; ethnicity must not be described as skin pigmentation or genetic biology.

## Frozen feasibility evidence

Read-only full-source audits are frozen in `analysis/hidden_hyperoxemia_audit.json` and `analysis/hidden_hyperoxemia_72h.json`. The actual `patient.csv.gz` header lacks catalog-listed `unitadmitoffset`; it contains `unitvisitnumber`, and profiling found 166,355 health-system stays, 27,635 multi-unit stays, and no duplicate visit-1 rows.

The first-day audit found 132,235 unambiguous same-offset PaO2/pH panels, 206 discordant duplicate panels, and only 514 final exact-FiO2 SpO2 96–97 observations; zero hospitals reached the inherited >=100 threshold. This makes the parent’s promised first-day transportability test structurally inconclusive.

The repaired 72-hour, same-row invasive-episode audit found 6,339 fully paired block-deduplicated observations in 3,298 stays/3,196 persons across 69 hospitals. The primary band contained 911 observations in 730 stays across 46 hospitals: 350 acidemic and 424 normal-pH. Three hospitals had >=100 band observations, five >=50, and nine met the frozen balanced >=30 gate. Preliminary raw rates (11.4% acidemic, 7.1% normal) are feasibility/QC, not adjusted evidence and do not satisfy the +10-point hypothesis. Only 257 band observations had a prior pH 30–360 minutes earlier, so no deployable recent-pH model is promoted.

## Falsification and interpretation

**Supportive:** B2’s standardized acidemia risk difference is >=+10 points, its two-sided 95% CI excludes 0, at least 70% of adequate held-out hospitals have a positive standardized contrast, and no single-hospital deletion reverses the direction. B2 must not worsen pooled held-out Brier score by >0.005 or calibration slope outside 0.8–1.2 versus B1. This supports a reproducible concurrent physiologic blind spot and a prospective recent-pH protocol study only.

**Adverse to the stated hypothesis:** the upper 95% confidence bound is below +10 points (which rejects the prespecified clinically large magnitude even if a smaller positive association remains), a majority of adequate hospitals have nonpositive contrasts, or the overall contrast is <=0 with a CI excluding 0. Report a smaller positive association as such; do not call it “no relationship.” This would favor the simpler SpO2/FiO2 interpretation over pH-conditioned targeting.

**Inconclusive:** the interval spans both 0 and +10; fewer than five hospitals meet the frozen balance gate after exact reconstruction; the hospital prediction interval includes both <=0 and >=+10; <20% of otherwise eligible invasive panels retain both FiO2 and SpO2; >10% bootstrap fits fail; or the direction reverses under entry-time-available FiO2, observation weighting, or leave-one-hospital deletion. Inconclusive is not supportive.

## Exact EICU bindings

Snapshot `[source checksum]`. All sources are ordinary read-only gzip CSV files, archive member none, under `[internal dataset path]`.

- `patient.csv.gz`, table `patient`: `patientunitstayid`, `patienthealthsystemstayid`, `uniquepid`, `age`, `gender`, `ethnicity`, `hospitalid`, `wardid`, `unittype`, `unitadmitsource`, `unitvisitnumber`, `admissionweight`, `unitdischargeoffset`. The actual header does **not** contain `unitadmitoffset`.
- `lab.csv.gz`, table `lab`: `labid`, `patientunitstayid`, `labresultoffset`, `labresultrevisedoffset`, `labtypeid`, `labname`, `labresult`, `labresulttext`, `labmeasurenamesystem`, `labmeasurenameinterface`.
- `respiratoryCare.csv.gz`, table `respiratoryCare`: `respcareid`, `patientunitstayid`, `respcarestatusoffset`, `currenthistoryseqnum`, `airwaytype`, `ventstartoffset`, `ventendoffset`, `priorventstartoffset`, `priorventendoffset`.
- `respiratoryCharting.csv.gz`, table `respiratoryCharting`: `respchartid`, `patientunitstayid`, `respchartoffset`, `respchartentryoffset`, `respchartvaluelabel`, `respchartvalue`.
- `vitalPeriodic.csv.gz`, table `vitalPeriodic`: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `sao2`.
- `hospital.csv.gz`, table `hospital`: `hospitalid`, `numbedscategory`, `teachingstatus`, `region`, joined from patient for descriptive site summaries.
- `apacheApsVar.csv.gz`, table `apacheApsVar`: `patientunitstayid`, `vent`, `intubated`, `pao2`, `fio2`, `ph`; QC/sensitivity only because these lack event timestamps.

## Verification boundary and stronger claims

The automatic verifier can check headers against source, exact joins and time inequalities, exclusion of future chart offsets, FiO2 conversion/labels, duplicate-panel rules, six-hour selection, attrition, model formulas, absence of hospital indicators in unseen-site models, hospital resampling, standardized contrasts/CIs, held-out metrics, and deterministic classification under the supportive/adverse/inconclusive rules. Required verifier fixtures must include: correct computation paired with an unsupported claim of oxygen toxicity or treatment benefit (reject); a supportive numeric result with a properly limited conclusion (accept); an upper CI below +10 interpreted as rejection of the clinically large hypothesis (accept); and wide/heterogeneous results interpreted as inconclusive (accept).

Automatic checks cannot establish arterial specimen identity, that zero-ended respiratory-care records truly mean ongoing ventilation until status time, that `sao2` is artifact-free or comparably calibrated across devices/hospitals, that charted FiO2 equals delivered FiO2, or that pH/PaO2-dependent selection is ignorable. These require clinical informatics adjudication and device/specimen metadata unavailable here. A temporally deployable pH rule needs substantially more paired prior-pH data and external prospective validation. Changing oxygen targets or claiming benefit requires expert review and a randomized protocol with hypoxemia, organ injury, and patient-centered outcomes.
