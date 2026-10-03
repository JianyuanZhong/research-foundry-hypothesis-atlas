# Corrected UKB cancer-type hypothesis with metabolic/liver restart audit

Status: proposed substantive child of `[prior hypothesis]`; no hypothesis test or full solver fit has been executed. This branch audits the expert-seed metabolic/liver restart and corrects an inherited source-binding error before preserving the CBC direction as the better-supported delivery hypothesis.

## Decision and scientific opening

The expert-seed metabolic/liver direction asks whether a low-ApoB/low-albumin, high-ALT/CRP phenotype identifies delayed hepatocellular carcinoma (HCC) or liver-family risk. It is clinically consequential because a persistent liver-risk pattern could motivate external validation of earlier liver assessment. But the relevant ambiguity is not just whether the markers predict HCC: it is whether any association is liver-family-specific and robust to the outcome source. The configured source has no symptoms, laboratory indication, alcohol history, viral-hepatitis adjudication, imaging, pathology, stage, treatment, or outpatient liver diagnoses.

The strongest evidence already supporting the mature CBC branch is that blood-count abnormalities can precede broadly defined cancer in UK primary care [K1], and an abstract-only retrospective CRC study reports longitudinal CBC trajectories up to 24 months before diagnosis while requiring prospective validation [K2]. The unresolved CBC claim is narrower and testable:

> Among UKB adults with a complete first CBC and no qualifying cancer at T0, is the prespecified platelet-high/haemoglobin-low contrast relatively more associated with later colorectal than haematologic cancer in the survivor-conditioned 2–5-year interval, and does that contrast remain compatible across registry and independently derived inpatient ascertainment proxies?

This is a descriptive, temporally ordered association. It is not causal, mechanistic, diagnostic-accuracy, screening, stage, treatment, or referral-threshold evidence. A learned model that ranks risk better would not by itself establish clinical utility; the inspected review [K3] specifically bounds predictive claims by limited calibration and external validation in the existing literature.

## Exact UKB binding and availability audit

Dataset snapshot: `ukb-completed-subset-20261002`; catalog [source checksum].

Use only the read-only Parquet source `[internal dataset path]`, [source checksum]. It is table `ukb671626.csv (Parquet)`, source ID `[UKB data file]`, 502,371 rows, unique key `eid`, namespace `ukb671626`. The original CSV lineage is not an analysis input.

Primary CBC fields are `53-0.0` (T0), `30000-0.0` WBC, `30020-0.0` haemoglobin, `30070-0.0` RDW, and `30080-0.0` platelets. Covariates are `31-0.0` sex, `21003-0.0` age, `21001-0.0` BMI, `20116-0.0` smoking, `30710-0.0` CRP and T0 calendar year. Registry outcomes pair same-index `40005-j.0` date with `40006-j.0` ICD-10 code for j=0,...,21. Death is `40000-0.0`. The inpatient sensitivity source is not a 259-element array in this frozen table: schema inspection found `41270-0.0` and `41280-0.0), while `41270-1.0` through `41270-258.0` and `41280-1.0` through `41280-258.0` are absent. The solver must therefore use exactly the single same-index inpatient pair, report this limitation, and never invent or silently substitute missing array members.

Measured bounded audit (job `[research job]` schema probe and `[research job]` selected-column scan) found 502,371 rows and 502,371 unique eids; all four T0 liver fields exist: `30640-0.0` ApoB (467,086 nonmissing), `30600-0.0` albumin (429,965), `30620-0.0` ALT (469,279), and `30710-0.0` CRP (468,446), with 426,822 complete four-marker rows and valid T0 dates. Registry date/code pairs had 152,596 valid paired rows over 119,269 eids; the single inpatient date/code pair had 445,001 valid paired rows over 445,001 eids. These are source audits, not fitted results.

## Metabolic/liver restart assessment

For a bounded liver check, define HCC as C22 and biliary cancer as C23–C24. Exclude valid registry-coded primary cancer on or before T0 (C00–C97 excluding C77–C79) from the complete four-marker cohort, then use the earliest post-T0 valid paired event. In the measured audit (`[research job]`), registry exclusion left 399,574 participants and yielded HCC first events of 50 in 0–2 years, 114 in 2–5 years and 164 in 0–5 years; the single inpatient-pair exclusion left 414,442 and yielded 32, 58 and 90. On the registry-eligible population, 228 people had a post-T0 HCC in both sources; only 20 had both source dates in 0–2 years and 40 in 2–5 years. The same audit found only 8 and 10 inpatient K70–K77 first events in those windows. These counts are availability diagnostics, not estimates of the liver hypothesis.

A liver baseline would be a standardized cause-specific competing-risk model for HCC, biliary cancer, other primary cancer and death using ApoB, albumin, ALT, CRP, age, sex, BMI, smoking and T0 year, with registry dates primary and the single inpatient pair sensitivity. A same-input nonlinear discrete-time multi-task model could test thresholds and interactions. However, a temporally held-out HCC comparison is likely to have fewer than 50 events, and source-overlap counts are below 50 in both planned windows. This makes source robustness and learned-model superiority scientifically inconclusive, not merely technically difficult. The liver branch is therefore deferred rather than promoted. Revisit only if a source with richer timed liver outcomes or expert adjudication becomes available; do not add the liver fields to the CBC hypothesis or join another namespace.

The mature CBC direction remains more informative because it can test CRC-versus-haematologic specificity with substantially larger relevant event support and a more direct observation-selection ambiguity. The correction from a nonexistent inpatient array to a single pair is consequential: it weakens source-bridge conclusions and must be carried into the CBC experiment.

## CBC population, temporal boundaries and estimand

Include unique eids with parseable T0 and complete instance-0 WBC, haemoglobin, RDW and platelets. Exclude any valid registry-coded qualifying cancer on or before T0. Do not require T1 or T2. Follow from T0 to the first CRC (C18–C20), haematologic cancer (C81–C96), other primary malignant cancer (C00–C97 excluding C77–C79 and the two target families), death, administrative censoring at 2022-12-31, or T0+2 years.

For the primary delayed analysis, retain participants alive and free of qualifying registry cancer at T0+2, enter at T0+2 and follow to the first event, censoring, or T0+5. Report events before T0+2 separately; this is a conditional delayed-risk estimand, not unconditional five-year risk. Repeat every analysis independently with the registry pair arrays and the single inpatient pair, never pooling source dates.

Standardize CBC variables using development-only means and scales. Fit separate cause-specific models and report the relative contrast
`D_s(w) = (beta_platelet,CRC,s,w - beta_Hb,CRC,s,w) - (beta_platelet,HEME,s,w - beta_Hb,HEME,s,w)`
for source s and window w. Positive D means a relative CRC-versus-haematologic association contrast; it does not identify a mechanism.

Use the parent’s fixed standardized profiles (platelets +1 SD/haemoglobin -1 SD versus platelets -1 SD/haemoglobin +1 SD, WBC and RDW at means) to report population-standardized cumulative incidence and the prespecified absolute-risk difference-in-differences A by cancer class and source. Keep the one-percentage-point boundary as a descriptive reporting boundary, never as a referral threshold.

## Falsification and interpretation

Derive each source independently with same-index date/code pairing, valid-date checks, duplicate-eid checks, code-family denominators, ties and impossible ordering. Report source-date displacement only for HCC/CRC/haematologic events with both sources; because the inpatient source has one diagnosis per eid, interpret overlap as ascertainment agreement, not gold-standard validation. If fewer than 50 same-class paired events are available in a window, source-robustness conclusions are inconclusive.

Stress-test the interpretation using 0–2 versus 2–5 timing, calendar-era strata from T0, fixed repeat-assessment gap strata, first-CBC repeat-observation strata, other-primary-cancer specificity, label permutation preserving dates/censoring, and weighted versus unweighted baseline-only repeat-observation analyses. Symptoms, indication, test ordering, iron studies, FIT, pathology, stage, treatment, healthcare use and outpatient capture remain unavailable; weighting cannot repair them.

Supportive results require a positive delayed D and A direction, specificity against other primary cancer, permutation collapse, no precise registry/single-inpatient reversal, and no confinement to the re-observed or near-diagnostic subset. This supports external validation only. Adverse results include precise reversal, source-sensitive boundary crossing, generic other-cancer similarity, disappearance after the two-year exclusion, or selection-sensitive changes; these weaken the stable cancer-type interpretation without refuting generic CBC-cancer association. Inconclusive results include fewer than 50 held-out haematologic events, fewer than 50 same-class source-overlap events, broad intervals, poor positivity, invalid pairs or nonconvergence. An imprecise null is not refutation.

## Equal-input method comparison and deliverable

The transparent baseline is separate cause-specific Cox models for CRC, haematologic cancer, other primary cancer and death with the same CBC and covariate inputs, plus Aalen–Johansen cumulative incidence and bootstrap uncertainty. The substantive alternative is a CPU gradient-boosted discrete-time multi-task competing-risk model with yearly intervals and separate type-specific hazards. It can reveal nonlinear Hb/platelet effects, interactions and time-varying hazards lost by additive Cox; it cannot reveal symptoms, indication, source correctness or mechanism.

Sort by T0 and use the earliest 70% for development and latest 30% for a locked temporal holdout, keeping eids intact. Fit transformations, tuning, weights and calibration in development only. Compare calibration intercept/slope, calibration plots, 2- and 5-year target-specific Brier/log scores, the fixed-profile A contrast and participant-bootstrap intervals; ranking metrics are secondary. If the final holdout has fewer than 50 haematologic events, type-specific learned superiority is inconclusive. A ranking gain without calibration or an improved fixed-profile A contrast is not a scientific advance.

The actual scientific deliverable is newly fitted source-specific cohort/event audits; D and A in both windows; source-date overlap/displacement; selection and era diagnostics; specificity/permutation controls; fitted Cox and learned outputs; temporal-holdout calibration and scores; bootstrap uncertainty; and a conclusion explicitly labelled supportive, adverse or inconclusive. Discovery audits above do not complete this deliverable.

Estimated future solver resources are 8–16 CPU cores, 32–64 GiB RAM and approximately 2–4 hours, within the configured 16-CPU/262,144-MiB/28,800-second envelope. GPU is not required for this tabular workload; the shared hardware guidance says an allocated A100 is available capacity, not a scientific requirement. This estimate is unmeasured for the full solver; the selected-column audit runtime was measured at roughly 13 seconds on 8 CPUs/64 GiB.

## Key references

[K1] supports broad primary-care CBC/cancer association but not this cancer-type or delayed UKB contrast. [K2] motivates a 24-month longitudinal boundary but is CRC-only and explicitly investigational. [K3] motivates calibration and temporal/external validation rather than ranking-only claims. All three were inspected as abstract/metadata excerpts only; no unavailable full text or supplement is claimed. The attached `key-references.json` and UTF-8 excerpts preserve the receipts.

## Alternatives and revisit rule

Selected: corrected CBC first-CBC competing-risk design with transparent Cox and same-input nonlinear alternative, because its event support and falsification structure can address timing, source capture and repeat-observation selection.

Deferred: ApoB/albumin/ALT/CRP liver-family direction, because the measured source contains the fields but has sparse HCC source overlap and only one inpatient diagnosis/date pair. Revisit with richer liver outcome capture, expert review or a new source.

Deferred: repeated metabolic change and pancreatic directions; inherited audits found zero pancreatic events in the planned repeat windows and only sparse inpatient pancreatic support. Do not rescue them by broadening outcomes.

Rejected: cross-namespace joins to `ukb672073`, treating codes without same-index dates as events, using absent inpatient indices, pooling registry and inpatient dates into a gold standard, or claiming causal/mechanistic/clinical-utility conclusions.

