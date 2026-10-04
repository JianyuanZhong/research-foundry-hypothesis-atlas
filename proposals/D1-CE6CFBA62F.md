> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 20 restart: does persistent hyperlactatemia matter after pressure recovery?

## Unresolved question, clinical importance, and advance

When mean arterial pressure (MAP) has recovered soon after norepinephrine is recorded, should failure of lactate to clear still identify a materially higher-risk patient, or is it mainly a nonspecific correlate of baseline illness and site-specific testing practice?

**Primary falsifiable hypothesis:** among the defined EICU early-norepinephrine, hyperlactatemic, eight-hour landmark population with sustained recorded MAP recovery, failure to achieve 20% lactate clearance is associated with at least a **+10 percentage-point** higher baseline-standardized probability of hospital death than achieving at least 20% clearance.

This is a prognostic physiology hypothesis, not an effect of lactate-guided treatment, norepinephrine, fluids, MAP targeting, or any intervention. The clinical decision it can inform is whether a prospective study of mandatory serial perfusion reassessment after apparent pressure recovery is justified. A reliably large contrast would support that next study; exclusion of +10 points would argue against treating this EICU-defined lactate trajectory alone as a major escalation trigger.

This is a justified no-parent restart. The highest-ranked prior EICU lineage has completed its late oxygenation prognostic test, excluded its locked +10-point harm margin, and explicitly stopped further same-snapshot threshold and model refinement. The present question uses a different population, physiology, timing, outcome construction, and decision.

## Existing evidence, supported claim, and unresolved claim

The strongest external evidence supports only the broad proposition that lactate trajectory can convey prognostic information and must be interpreted in clinical context. The full-text 2021 Surviving Sepsis Campaign guideline (Evans et al., DOI 10.1007/s00134-021-06506-y; frozen XML source `e5686418...`, SHA-256 `6a55ec3b...`) recommends using lactate reduction during resuscitation in patients with elevated lactate, but grades this as weak/low-quality and cautions that lactate is not a direct tissue-perfusion measure. A recent full-text single-center study of 574 ED patients with sepsis or septic shock (Diab et al., 2025, DOI 10.3389/fmed.2025.1679297; source `8280f85c...`, SHA-256 `e3bf0e2e...`) defined positive clearance as >10% between first and second measurements; its adjusted association with in-hospital mortality was borderline (OR 0.66, 95% CI 0.42–1.04). It did not isolate patients whose MAP had already recovered after early norepinephrine or provide multicenter EICU transport evidence. The inspected full-text 2026 conceptual review (Hernandez et al., DOI 10.1186/s13054-026-06201-8; source `b8f07487...`, SHA-256 `f769b35b...`) argues that isolated hemodynamic or metabolic targets have not yielded reproducible benefit and motivates short-cycle multi-physiology reassessment; it does not establish this hypothesis.

Complete-source feasibility—not outcome inference—is currently supported in EICU snapshot `[source checksum]`. No rows were sampled. The audit found 359 patients with the required serial lactate, MAP response, and baseline vital data across 63 hospitals. The locked outcome-blind hospital gate retained 189 patients in ten hospitals: 91 clearance patients (38 deaths; crude 41.8%) and 98 nonclearance patients (48 deaths; crude 49.0%). Baseline lactate and vital differences and site selection make this crude +7.2-point contrast noninferential. It neither supports nor falsifies the primary +10-point standardized claim.

The substantive advance is therefore not “lactate predicts mortality.” It is a strict temporal and physiological challenge: whether a lactate trajectory still marks a clinically material mortality contrast **after recorded MAP recovery**, within hospitals that observed both trajectories, using only information available by an eight-hour landmark and preserving clinician-selected testing as an explicit target-population limitation.

## Exact population and temporal boundaries

All offsets are integer minutes relative to ICU admission.

1. Read all source rows. Adults have numeric `age>=18`; released `age='> 89'` is mapped to 90.
2. In each ICU stay, define (T0) as the minimum `infusionDrug.infusionoffset` from 0 through 1440 inclusive for a case-insensitive `drugname` containing `norepinephrine` or `levophed`. Dose and rate fields do not define eligibility because their units and completeness vary.
3. Among all qualifying stays for a `uniquepid`, retain the one with the smallest (T0), breaking ties by `patientunitstayid`. This is the earliest qualifying norepinephrine-recorded stay per person, not necessarily the person's first ICU stay.
4. Require `unitdischargeoffset>=T0+480` and `hospitaldischargeoffset>=T0+480`, so every patient is alive and still in the ICU at the fixed eight-hour landmark. Require exact `hospitaldischargestatus` Alive or Expired. Exact death time is unavailable; hospital death is binary and necessarily occurs after the landmark under this construction.
5. Baseline lactate is the valid `labname='lactate'` value 0.2–30 mmol/L with the latest `labresultoffset` in ([T0-360,T0]); require `labresultrevisedoffset<=T0+60` and baseline lactate >=2. If the latest collection time has conflicting distinct valid values after retaining the latest revision, exclude the patient.
6. Follow-up lactate is the valid value whose collection offset is nearest (T0+360) within ([T0+120,T0+480]), tie-breaking toward the earlier collection and then smallest `labid); require `labresultrevisedoffset<=T0+480`. Apply the same latest-revision/conflict rule. Thus all exposure information is available by landmark.
7. Recorded MAP recovery requires at least six valid `vitalPeriodic.systemicmean` values from 20–180 mm Hg in ([T0+60,T0+120]), with at least 80% of them >=65. Duplicate offset rows are reduced to their median before counting.
8. Baseline vital adjustment requires at least three offsets in ([T0-60,T0]) at which MAP 20–180 and heart rate 20–250 are both valid. The median MAP and heart rate over unique offsets are frozen covariates.
9. Before outcomes are read, retain hospitals with at least five exposed and five comparator patients. The audit identified ten such hospitals. If reconstruction produces fewer than eight hospitals, fewer than 50 patients or 20 deaths in either group, classify the experiment inconclusive rather than weakening the gate.

The target is consequently patients who survived to eight hours, had early recorded norepinephrine, clinician-selected serial lactates, measurable baseline vitals, documented pressure recovery, and membership in an overlap hospital. It is not all shock, all sepsis, or all norepinephrine use.

## Variables, estimand, and baselines

Exposure (X=1) is lactate nonclearance:
[
(B-F)/B < 0.20,
]
where (B) and (F) are baseline and follow-up lactate. (X=0) is clearance >=20%. Negative clearance (a rise) belongs to nonclearance. The primary outcome (D) is exact `hospitaldischargestatus='Expired'`.

The primary estimand is the overlap-population standardized risk difference
[
\Delta=P_w(D=1\mid X=1)-P_w(D=1\mid X=0).
]
It is a baseline-standardized prognostic association, not a causal propensity estimand.

Fit one prespecified ridge logistic exposure model with `X` as outcome and these pre-exposure predictors: age (90 for `> 89`), sex indicators including missing, baseline lactate, median baseline MAP, median baseline heart rate, (T0), and fixed indicators for the retained hospitals. Continuous terms are winsorized at pooled 1st/99th percentiles and standardized with pooled population means and SDs. Use scikit-learn `LogisticRegression(C=1, penalty='l2', solver='lbfgs', max_iter=10000)`; no outcome enters this model. Assign (1-e_i) to nonclearance and (e_i) to clearance, then normalize weights to mean one within each exposure group. Estimate each weighted mortality risk and their difference.

Required baselines are:

- the crude risk difference in the same 189-person target;
- a hospital-only overlap model;
- the full baseline model above;
- a continuous secondary association using percentage clearance, winsorized at -100% and +100%, in a ridge logistic hospital-mortality model with the same covariates.

The full model is primary. Baselines diagnose whether apparent information is explained by hospital or measured starting physiology; they cannot rescue a failed primary.

## Uncertainty, diagnostics, and falsification

Run 5,000 hierarchical bootstrap replicates with seed 20260920. Sample the ten hospitals with replacement and assign hospital-copy identifiers. Within every copied hospital and exposure group, sample `uniquepid` clusters with replacement to the original cell size, assign person-copy identifiers, recompute preprocessing, refit the exposure model, and re-estimate risks and (Delta). Use the percentile 2.5th and 97.5th percentiles. A replicate that loses an outcome class, does not converge, or yields a nonfinite estimand fails; do not substitute another model.

Report group counts, deaths, hospitals, crude and standardized risks/RDs, risk ratio, propensity range, group effective sample sizes, maximum normalized weight, maximum hospital weight fraction, weighted standardized mean differences for every model term, all 5,000 bootstrap results, and leave-one-hospital-out RDs.

Required primary gates are: both group ESS >=40; no propensity outside 0.02–0.98; maximum normalized person weight <=5%; maximum absolute weighted SMD <=0.10; maximum hospital weight fraction <=35%; bootstrap failure <=5%; and at least eight of ten leave-one-hospital-out estimates finite. Failure of any gate makes the result inconclusive.

Classification is locked:

- **Supportive:** lower 95% bound for (Delta) >=+0.10, every gate passes, and at least 80% of leave-one-hospital-out point estimates are positive. This supports only a material noncausal prognostic contrast and a prospective reassessment study.
- **Adverse to materiality:** upper 95% bound <+0.10 with all computational gates passing. Report any smaller positive, null, or negative association exactly; do not call it “no association.”
- **Opposite association:** upper 95% bound <0 with all gates passing. This is adverse to the hypothesis but does not imply that nonclearance is protective.
- **Inconclusive:** the interval contains +0.10, any gate fails, or required computation is not defined.

Prespecified robustness checks are descriptive unless their own intervals are reported: 10% and 30% clearance cutoffs; nearest follow-up in 120–360 and 240–480 minute windows; MAP recovery as median MAP >=65; inclusion of all 359 complete patients with ridge hospital indicators but no hospital cell gate; exclusion of baseline lactate >10; earliest globally observed ICU stay per person; and exclusion of rows with recorded non-full therapy before landmark from `carePlanGeneral`. None changes the primary classification.

## Meaning of possible results and stronger claims

A supportive result would show that, among this selected and measured EICU phenotype, MAP recovery does not erase a large mortality gradient associated with persistent lactate. It would justify externally validating a mandatory serial-assessment trigger with synchronized drug administration, fluid, capillary-refill, urine-output, and organ-perfusion data. It would not show that additional fluids, more vasopressor, inotropy, or lactate normalization improves outcome.

An adverse result would show that this exact trajectory does not carry the prespecified +10-point adjusted contrast in the overlap target. It would argue against advancing this EICU definition as a major escalation trigger, while preserving any smaller association. An opposite result would more strongly reject the hypothesized direction but would likely indicate selection or residual-confounding mechanisms needing clinical review.

An inconclusive result would mean this snapshot cannot distinguish material from smaller prognostic separation. It must not trigger cutoff, window, or subgroup mining. A larger independently collected cohort is required.

A treatment-effect conclusion requires a randomized or credible target-trial design with time-stamped administered therapies, treatment intent, dynamic confounding control, and expert protocol review. Clinical utility requires a prospective impact study. Generalization to sepsis requires adjudicated infection and organ dysfunction. Mechanistic tissue hypoperfusion requires perfusion measurements absent here.

## Exact source bindings and provenance

All inputs are read-only ordinary `.csv.gz` files with no nested archive member under
`[internal dataset path]`.

- `patient.csv.gz` / table `patient`, [source checksum]: `patientunitstayid`, `uniquepid`, `age`, `gender`, `hospitalid`, `unitdischargeoffset`, `hospitaldischargeoffset`, `hospitaldischargestatus`.
- `infusionDrug.csv.gz` / `infusionDrug`, [source checksum]: `infusiondrugid`, `patientunitstayid`, `infusionoffset`, `drugname`; `drugrate`, `infusionrate`, `drugamount`, `volumeoffluid`, and `patientweight` are audited but unused.
- `lab.csv.gz` / `lab`, [source checksum]: `labid`, `patientunitstayid`, `labname`, `labresult`, `labresultoffset`, `labresultrevisedoffset`, `labmeasurenamesystem`, `labmeasurenameinterface`.
- `vitalPeriodic.csv.gz` / `vitalPeriodic`, [source checksum]: `vitalperiodicid`, `patientunitstayid`, `observationoffset`, `systemicmean`, `heartrate`.
- `carePlanGeneral.csv.gz` / `carePlanGeneral`, [source checksum], sensitivity only: `cplgeneralid`, `patientunitstayid`, `cplitemoffset`, `cplgroup`, `cplitemvalue`; `activeupondischarge` is forbidden because it can encode future state.

Event tables join to patient on `patientunitstayid`; person selection/resampling uses `uniquepid`; site uses `hospitalid`. EICU metadata confirms that `vitalPeriodic` contains five-minute medians of generally one-minute monitor averages, not raw waveform. The feasibility script and JSON are `analysis/norepi_lactate_feasibility.py` and `analysis/norepi_lactate_feasibility.json`; the script's initial aggregate audit did not implement the final duplicate/conflict rules, which the inferential compiler must enforce and reconcile rather than silently inherit.

## Unavailable evidence, adjudication, and verifier contract

EICU cannot establish that the first infusion row is true drug initiation or administration, distinguish continued outside-hospital norepinephrine, verify dose units or target intent, adjudicate arterial versus venous lactate, determine why or exactly when a specimen was drawn, recover capillary refill, skin mottling, mental status, delivered fluid boluses, complete urine output, source control, cardiac output, liver clearance, seizure or beta-agonist contributions, or determine exact death time/cause. Serial-lactate inclusion and the eight-hour survivor requirement create selection. “MAP recovery” is recorded central/arterial monitor summary, not adjudicated organ perfusion. Absence of a care-plan limitation is not proof of full treatment. These require clinical adjudication or new data.

The verifier can check source hashes and headers, no source writes, complete scanning, drug-name matching, (T0), one-person selection, landmark inequalities, lab collection/revision logic, duplicate/conflict handling, MAP and baseline-vital windows, outcome-blind hospital gate, counts and reconciliation, forbidden-column non-use, model matrix, weights, bootstrap copy IDs/seed/count, diagnostics, intervals, and classification logic. It cannot prove drug administration, specimen type, monitor validity, perfusion, clinical rationale, causal exchangeability, sepsis, treatment benefit, transportability, or utility.

A correct supportive synthetic result must pass only the stated prognostic interpretation. A correct RD +6 points (95% +2,+9) is adverse to +10 while supporting a smaller association. RD -3 (-12,+6) is adverse to +10 with unresolved direction. RD -12 (-20,-4) is opposite, not protective. RD +12 (-3,+24), any failed gate, or undefined bootstrap is inconclusive. Correct computation paired with recommendations for fluids/vasopressors, claims of treatment benefit or harm, tissue hypoperfusion, sepsis-wide generalization, or clinical deployment must fail verification.

All four configured HCC, MIMIC, EICU, and UKB datasets remain directly available read-only, including permitted rows and notes. This proposal uses EICU only; derived aggregate files stay in the workspace, and no private row, identifier, text, or note was sent to public search.
