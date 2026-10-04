> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Can pulmonary-phenotype and oxygen-recording error create or erase the post-adequacy hyperoxia interaction?

## Status, opening, and fixed scientific question

This is a substantive measurement-validity child of `[prior hypothesis]`, not an executed clinical result. It preserves the parent's population, hour-24 phenotype/adequacy landmark, hour-24–36 inspired-oxygen window, hour-36 outcome origin, seven-day in-hospital death outcome, live-discharge competing event, and pulmonary-stratum interaction estimand. It changes the order of inference: phenotype and exposure measurement must first be shown sufficiently accurate and sufficiently nondifferential for a clinically consequential interaction to be distinguishable from ascertainment.

A broad randomized ICU trial established that changing oxygen targets changes oxygen exposure without showing a ventilator-free-day benefit [K1]. Mechanistic evidence distinguishes inspired hyperoxia from arterial hyperoxemia and supports an oxygen–mechanical-stress interaction in experimental systems, but clinical mortality evidence remains inconsistent [K2]. LUNG SAFE showed that even prospectively collected Berlin-definition components and clinician recognition diverge, with recognition increasing from 51.3% in mild to 78.5% in severe ARDS [K3]. Those works support the clinical opening, not the proposed result.

The strongest currently supported claim is limited: oxygen exposure can be changed; high inspired oxygen and arterial hyperoxemia are not interchangeable; and pulmonary-injury recognition is severity-dependent even in a prospective study with imaging and PEEP data. The parent audit further establishes that eICU contains enough PaO2, FiO2, saturation, ventilator, diagnosis, and hospital data to attempt the experiment. It does **not** establish that the eICU pulmonary proxy is acute lung injury, that unrecorded FiO2 is low, or that the observed proxy-by-FiO2 interaction represents pulmonary oxygen toxicity.

The unresolved hypothesis is unchanged:

**Among adults alive and still in the ICU at hour 36 who had PaO2 80–120 mm Hg paired with valid FiO2 during hours 18–24, greater sustained FiO2 above 0.40 during oxygen-adequate hours 24–36 is associated with a larger subsequent seven-day in-hospital death cumulative incidence in a pre-hour-24 acute-pulmonary-injury proxy than in ICU states without a documented acute pulmonary diagnosis.**

The primary estimand remains the difference between those strata in the standardized seven-day death risk difference per 0.10 increase in time-weighted excess FiO2, with live hospital discharge competing. It is a conditional observational contrast among 36-hour survivors. It is not the total causal effect of oxygen initiation, and no adjustment for physiologic changes occurring after hour 24 will be described as recovering that total effect.

The new measurement hypothesis is:

**After blinded phenotype review and source-concordance analysis, the simultaneous upper bound on an interaction produced solely by differential pulmonary-label and FiO2 ascertainment is less than 1.5 absolute percentage points of seven-day death risk per 0.10 excess FiO2 (half the prespecified clinically consequential 3-point interaction), and this remains true across hospital documentation strata.**

This hypothesis is tested before any toxicity interpretation. Failure is an informative measurement result and ends the pulmonary-toxicity branch.

## Clinical advance and competing explanations

The clinical decision is whether a future oxygen-titration trial should enrich or stratify by pre-exposure pulmonary injury. The parent could produce a positive interaction even if sicker patients receive more oxygen and more measurements. This child addresses a distinct failure: the "injury" group may be enriched for hospitals or patients that document respiratory failure, obtain ABGs, and chart ventilator FiO2 frequently, while the comparison group may contain undocumented injury and sparse oxygen records. Differential misclassification can amplify, attenuate, reverse, or manufacture effect modification.

The leading scientific explanation remains delayed oxygen–mechanical-stress injury after adequate oxygenation. Its strongest measurement rival predicts that:

- proxy positivity follows diagnosis-entry intensity, ventilation support, ABG use, and hospital charting style;
- recorded excess-FiO2 burden rises with respiratory-charting density even at similar saturation;
- proxy-positive and proxy-negative patients exchange strata under blinded review nonrandomly by severity or site; and
- the interaction shrinks, reverses, or becomes nonidentified when joint phenotype/exposure error is propagated.

A toxicity-compatible observation is therefore not merely an adjusted positive interaction. It requires a measurement gate pass, a delayed exposure pattern not present before escalation, agreement between transparent bounds and an admissible latent model, and stability across hospital/source restrictions. A severity-compatible pattern begins at or before FiO2 escalation and follows pressure, shock, or hypoxemia. A documentation-compatible pattern tracks source density or disappears after source-balanced analysis. None identifies oxidative tissue injury.

## Population and immutable clocks

Use one index `patientunitstayid`: adult age >=18 (map `age='> 89'` to 90 for adjustment only), first ICU stay (`unitvisitnumber=1`) per `patienthealthsystemstayid`, and `unitdischargeoffset>=2160`. Exclude comfort-measures-only/end-of-life plans entered by minute 1440, burns, extracorporeal support where identifiable, impossible offsets, and unresolved duplicate/revised rows.

- Baseline: minute 0 through 1440.
- Adequacy anchor: minutes 1080–1440. Select the last PaO2 80–120 mm Hg paired with valid FiO2 within ±60 minutes; among equal-distance FiO2 values prefer a preceding value, then the earlier record.
- Phenotype cutoff: clinical event/entry time <=1440 only.
- Exposure: minute 1440 inclusive through 2160 exclusive.
- Outcome time zero: minute 2160.
- Follow-up: through minute 12240, hospital death, or live hospital discharge, whichever comes first.

Everyone must be alive and observed at hour 36. Exposure duration never determines the landmark. These safeguards remove exposure-defined immortal time but do not solve treatment selection within hours 24–36.

## Frozen computable phenotype and exposure

### Pulmonary strata

Version P0 is frozen before outcomes are opened. The positive proxy requires both:

1. a `diagnosis` or `admissionDx` acute term entered by minute 1440: ARDS/acute respiratory distress, pneumonia, aspiration, pulmonary edema, or acute respiratory failure; and
2. anchor PaO2/FiO2 <=300.

The comparison stratum has no such acute pulmonary term by minute 1440, regardless of P/F. A pulmonary term with P/F >300 is a discordant validation group, not a primary comparator. COPD/asthma alone is insufficient. Term-family indicators are retained separately; collapsing them does not imply one biology. The proxy is not Berlin ARDS because eICU lacks uniform bilateral-imaging adjudication, complete PEEP confirmation, and reliable exclusion of hydrostatic edema.

Hospital documentation is evidence about the observation process, not truth. Pre-hour-24 `note`, `physicalExam`, `treatment`, and ventilation-support rows are **corroboration features and review-packet content only**; they do not silently expand P0. Outcome-blind Phase I review may motivate one documented P1 revision. P1 must then be frozen before Phase II and outcome analysis.

### Oxygen exposure

Normalize FiO2 values recorded as 0.21–1.00 or 21–100%. Respiratory-charting FiO2 is the primary longitudinal setting; lab FiO2 and `respiratoryCare.setapneafio2` are independent agreement channels, not automatically interchangeable observations. Build 12 hourly bins. Within source and bin use the median. Multiple sources within 30 minutes form a concordance pair; do not average discordant sources before reporting error.

An hour is oxygen-adequate when median SaO2/SpO2 >=94%; PaO2 >=80 within ±60 minutes may establish adequacy when saturation is absent. SpO2 <92% or PaO2 <60 marks hypoxemia and excludes that hour from excess while contributing a separate severity flag. SpO2 never quantifies arterial hyperoxemia.

For adequate hour (t), (X_t=(FiO2_t-0.40)_+). The primary exposure is the time-weighted mean across all 12 hours; unobserved hours remain missing and are integrated or bounded, never coded as room air or no excess. Require at least six observed FiO2 hours and six adequate-status hours for the complete-record analysis. Display categories (not the estimand) are sustained FiO2 >0.40 in >=75% versus <=25% of observed adequate hours. Threshold sensitivities are 0.30, 0.50, and 0.60.

## Measurement-first experiment

### Phase 0: outcome-blind census

Before reading mortality, publish by stratum, hospital, and source:

- P0 flow, term-family overlap, diagnosis-versus-admission-source overlap, P/F distribution, and discordant group;
- hourly FiO2, SpO2/SaO2, ABG, PEEP, plateau-pressure, tidal-volume, respiratory-support, note, and physical-exam coverage;
- invalid-value, duplicate, source-disagreement, event-to-entry/revision delay, and time-since-last-observation distributions;
- cross-source FiO2 agreement within 30 minutes: median absolute difference, 90th percentile, Bland–Altman summaries, and probability of disagreement >0.05;
- hospital distributions of label prevalence and coverage, without selecting hospitals by outcomes.

The bounded audit for this child is feasibility evidence, not a result. In 1,869 first-visit adult hour-36 survivors with the fixed adequate anchor, it found 804 P0 injury, 965 no-term, and 100 discordant stays. Injury versus no-term groups had >=6 FiO2 hours in 420/804 (52.2%) versus 454/965 (47.0%); >=6 saturation hours in 773/804 (96.1%) versus 937/965 (97.1%); exposure-window ABGs in 410/804 (51.0%) versus 531/965 (55.0%); and any ventilation corroboration in 777/804 (96.6%) versus 924/965 (95.8%). Among 47 hospitals with >=10 anchored cases, pulmonary-label prevalence ranged 0.17–0.94, >=6-hour FiO2 coverage 0–1.00, and exposure-window ABG prevalence 0.06–0.74. Thus oxygen and phenotype observability are materially site-dependent even though saturation is dense.

### Phase I and II phenotype validation

Create relative-time review packets from minute 0–1440 containing deidentified diagnosis/admission paths and times, anchor ABG/FiO2/P/F, respiratory-support trajectory, PEEP, available structured note fields, physical-exam respiratory fields, and treatment evidence. Remove `hospitalid`, outcome, post-hour-24 data, P0 label, and FiO2-excess summary. Review targets are:

1. **available-record-supported acute pulmonary injury at hour 24**: definite, probable, absent, or indeterminate;
2. support class: invasive ventilation, noninvasive positive pressure, other oxygen support, or indeterminate;
3. likely hydrostatic-only explanation, mixed/uncertain, or nonhydrostatic-compatible;
4. timing interval and whether evidence is adequate for clinical classification.

This is not retrospective diagnosis of true ARDS; source images and full source charts are unavailable.

Phase I uses 160 packets (80 P0 positive, 80 P0 negative), balanced over P/F bands, ventilation support, hospital label/FiO2-coverage quartiles, and source signatures. Two ICU clinicians independently review all packets; a third resolves after initial labels are locked. One P0-to-P1 rule revision is allowed using Phase I only.

Phase II uses a new probability sample of 600 packets: 300 P1 positive and 300 P1 negative, stratified by the same factors and with exact inclusion probabilities. At most one packet per `uniquepid`. Two clinicians independently review 30%, all indeterminate/disagreements, and all source-poor sentinels; one reviews the remainder; a third arbitrates disagreements. Report weighted confusion tables, effective sample sizes, PPV, sensitivity, specificity, NPV, indeterminate fractions, kappa, and simultaneous intervals overall and by documentation quartile, ventilation class, P/F band, and hospital random-effect distribution.

If ICU clinicians or the 600-packet review are unavailable, the study can deliver Phase 0 and source-based exposure validation, but must stop before a pulmonary-injury-specific biological interpretation.

### M0: transparent validation and error-bound baseline

M0 uses design-weighted Phase II confusion tables plus empirical FiO2 source disagreement. It propagates joint uncertainty in pulmonary status (P), observed exposure (	ilde X), and missing hourly FiO2 to the same competing-risk interaction estimand.

For each of 2,000 hospital-cluster bootstrap draws:

1. sample stratum/source-specific phenotype sensitivity and specificity from simultaneous confidence sets, treating indeterminate reviews first as false and then as true;
2. sample FiO2 error from paired-source empirical residuals separately by source, support class, P0 status, and hospital coverage quartile;
3. bound each missing hour between zero excess and the nearest observed support-compatible FiO2, capped at 1.0; a multiple-imputation sensitivity uses the predeclared observation model;
4. recompute the P-by-X interaction under all vertices of the conservative error set; and
5. simulate the interaction when true mortality risk depends on baseline severity and true pulmonary status but **not** on excess FiO2.

M0's primary output is the 95% simultaneous interval for the maximum absolute spurious interaction and the identification interval for the observed interaction. It is auditable and makes every error assumption visible. It loses ordering, borrows no information across sparse source combinations, and cannot distinguish a latent respiratory change from a change in observation intensity.

### M1: clinician-anchored latent respiratory/measurement state

M1 uses exactly the same cohort, hourly inputs, folds, endpoint, and adjudication sample. Fit an outcome-blind hierarchical state-space model on training hospitals:

- latent hourly respiratory state (R_t) emits PaO2, SpO2/SaO2, PaCO2/pH, PEEP, plateau/peak pressure, tidal volume, respiratory rate, hemodynamics, and support state;
- latent inspired-oxygen setting (F_t) emits respiratory-charting FiO2, lab FiO2, and respiratory-care FiO2 with source- and hospital-specific error;
- a separate observation process predicts whether each ABG, FiO2, saturation, ventilator setting, diagnosis, note, and physical-exam field is recorded, using only past observed state and hospital documentation effects;
- pre-hour-24 latent pulmonary state is anchored by Phase II clinician labels and emits term families, P/F, support, and structured documentation;
- accumulated lagged oxygen–mechanical burden (sum (F_t-0.40)_+	imes) standardized PEEP/plateau burden is evaluated only after measurement calibration.

Only after frozen outcome-blind posterior predictive checks pass is the competing-risk death/discharge head fitted. Integrate over posterior pulmonary class and missing (F_t) rather than imputing one label or setting. The model may be Bayesian state-space or a structured variational recurrent implementation. Hospital has hierarchical treatment and observation effects; it cannot receive an unrestricted hospital-to-outcome shortcut.

M1 adds source reliability, temporal ordering, uncertainty in pulmonary class and FiO2, and separation of physiologic versus observation transitions that M0 aggregates away. It is scientifically admissible only if held-hospital calibration passes for clinician labels, FiO2 source pairs, observation hazards, next-hour PaO2/SpO2, and support state, and its error-only interaction lies inside M0's conservative bounds. It cannot rescue a failed M0 gate or turn model assumptions into truth.

## Hard measurement gate

Outcome modeling may be computed for audit, but no result may be described as pulmonary-toxicity effect modification unless all conditions pass:

1. Phase II weighted P1 PPV and sensitivity are each >=0.80 with simultaneous lower 95% bounds >=0.70; indeterminate <=15% overall and <=25% in every documentation quartile.
2. Absolute PPV or sensitivity differences across hospital documentation quartiles and ventilation classes have simultaneous upper bounds <=0.15. At least 30 hospitals contribute reviewed or hierarchically estimable cases in both primary strata.
3. Among paired FiO2 sources, median absolute difference <=0.05, 90th percentile <=0.10, and stratum/documentation-quartile difference in disagreement probability <=0.10. At least 150 paired observations exist per primary stratum and 20 hospitals contribute pairs.
4. Both strata retain >=150 complete-record stays and >=40 seven-day deaths; generalized-propensity effective sample size >=100 per stratum and overlap is >=5% in every prespecified propensity decile.
5. Under M0, the simultaneous 95% upper bound on the maximum error-only interaction is <1.5 risk points per 0.10 excess FiO2. M1 must pass all calibration checks and remain within M0 bounds.
6. No single source family or five hospitals account for >50% of weighted exposure information or determine the interaction direction; event-time versus entry/revision-time and high-coverage-site analyses agree in direction.

A failed phenotype gate yields a proxy-measurement result. A failed FiO2 gate yields an exposure-measurement result. Failed overlap/events yields an inconclusive clinical contrast. Thresholds are not relaxed after outcomes are viewed.

## Outcome analysis without unsupported causal adjustment

The primary transparent outcome model is a cause-specific discrete-time death/discharge model with restricted cubic spline for measured excess FiO2, P1 pulmonary probability/stratum, their interaction, and covariates fixed by minute 1440: age, sex, ethnicity, admission source/type, unit type, hospital region/size/teaching status, APACHE IV severity/predicted mortality, anchor PaO2/FiO2/P/F, baseline pH/PaCO2/lactate/renal/hepatic/hematologic measures, baseline vasopressor and respiratory support, pre-hour-24 PEEP/pressure/tidal-volume summaries, chronic disease, sepsis/trauma/postoperative/neurologic indicators, and treatment limits. Standardize seven-day Aalen–Johansen risks with hospital-cluster bootstrap uncertainty.

Variables measured during hours 24–36—hypoxemia, pressure, shock, ventilation changes, ABG ordering, and observation counts—are not placed into the primary model as if ordinary baseline confounders. They may be:

- included in a clearly labeled descriptive residual/direct-contrast sensitivity whose estimand differs from the primary contrast;
- modeled sequentially in M1 under explicit treatment-confounder feedback assumptions; or
- used for lag, negative-control, and measurement diagnostics.

Attenuation after conditioning on these variables does not prove mediation; persistence does not prove toxicity. The M1 bounded regime that caps FiO2 at 0.40 only during modeled adequate hours is reported as model-based g-computation under sequential exchangeability, consistency, positivity, and measurement-model assumptions—not an identified trial effect.

Five folds are grouped by `hospitalid`; `uniquepid` never crosses folds. M0, M1, and outcome models use identical folds and inputs. Evaluate calibration, Brier score, integrated calibration index, observation-hazard calibration, clinician-label calibration, next-hour physiology error, source agreement, overlap/ESS, interaction estimate, and error-only interaction. Model selection is not based on AUROC or a small predictive gain.

## Exact eICU bindings

All source files are read-only ordinary gzip CSVs (archive member: none) under `[internal dataset path]`, snapshot `[source checksum]`. Catalog schemas are under `datasets/eicu/`. Derived data stay in `work/evolution-measurement/`.

- `patient.csv.gz` / `patient` / catalog `table-ab037c09d7df9a3c.json`: `patientunitstayid` join key; `patienthealthsystemstayid`, `uniquepid`, `unitvisitnumber`, `hospitalid`; demographics/admission fields; `unitdischargeoffset/status/location`, `hospitaldischargeoffset/status/location`. Offsets are ICU-relative minutes.
- `lab.csv.gz` / `lab` / `table-79bdb33275339b1a.json`: `patientunitstayid`; event `labresultoffset`; revision `labresultrevisedoffset`; `labname`, `labresult`, `labresulttext`, measurement-system/interface fields. Required labels include `paO2`, `paCO2`, `pH`, `FiO2`, `O2 Sat (%)`, `PEEP`, lactate and baseline labs.
- `respiratoryCharting.csv.gz` / `respiratoryCharting` / `table-339bf06c7eef27e0.json`: `patientunitstayid`; event `respchartoffset`; entry `respchartentryoffset`; `respcharttypecat`, `respchartvaluelabel`, `respchartvalue`. Required labels include FiO2 variants, SaO2, PEEP/CPAP, plateau/peak pressure, tidal volumes, ventilator/respiratory rates, O2 device/delivery, and RT Vent On/Off.
- `vitalPeriodic.csv.gz` / `vitalPeriodic` / `table-a22c6d6981a32279.json`: `patientunitstayid`, `observationoffset`, `sao2`, `heartrate`, `respiration`, `systemicmean`, other pressures.
- `respiratoryCare.csv.gz` / `respiratoryCare` / `table-75bd08623beb504f.json`: `patientunitstayid`; `respcarestatusoffset`, current/prior vent start/end offsets, `airwaytype`, `setapneafio2`, limits for support corroboration. Zero/sentinel offsets are not events without corroboration.
- `diagnosis.csv.gz` / `diagnosis` / `table-5d5ab99e8c359037.json`: `patientunitstayid`, `diagnosisoffset`, `diagnosisstring`, `icd9code`, priority/status.
- `admissionDx.csv.gz` / `admissionDx` / `table-2e48e1043e7eaa89.json`: `patientunitstayid`, entry clock `admitdxenteredoffset`, path/name/text.
- `note.csv.gz` / `note` / `table-86a431bb16ad4fc7.json`: `patientunitstayid`, event `noteoffset`, entry `noteenteredoffset`, `notetype`, `notepath`, `notevalue`, `notetext`. These are structured note fields and not a dependable complete narrative chart.
- `physicalExam.csv.gz` / `physicalExam` / `table-e618699abb8e55de.json`: `patientunitstayid`, `physicalexamoffset`, path/value/text for corroboration only.
- `treatment.csv.gz` / `treatment` / `table-5461361964176606.json`: `patientunitstayid`, `treatmentoffset`, `treatmentstring`, status for respiratory-support and treatment-limitation corroboration.
- `apacheApsVar.csv.gz` / `apacheApsVar` / `table-67711a86e012835e.json`: `patientunitstayid`, `intubated`, `vent`, admission physiology, PaO2/FiO2. Untimed summaries are baseline only.
- `apachePatientResult.csv.gz` / `apachePatientResult` / `table-754bebf64d3d9909.json`: APACHE score/version and predicted mortality/LOS. Actual mortality/LOS/ventilator days are outcomes/audits, never predictors or timestamps.
- `apachePredVar.csv.gz` / `apachePredVar` / `table-b1f86cc4a8d9f2a2.json`: day-one ventilation, P/F, comorbidity and admission fields; baseline agreement only.
- `infusionDrug.csv.gz` / `infusionDrug` / `table-18e1a8caaa91eb44.json`: `patientunitstayid`, `infusionoffset`, drug/rate fields for vasopressor indicators with unknown-unit flags.
- `carePlanGeneral.csv.gz` / `carePlanGeneral` / `table-33b82ae7a5609587.json` and `carePlanEOL.csv.gz` / `carePlanEOL` / `table-4a60395475cf75e7.json`: item/discussion/save offsets and status for treatment-limit exclusion.
- `hospital.csv.gz` / `hospital` / `table-811df7b2ef435e12.json`: join `patient.hospitalid=hospital.hospitalid`; bed category, teaching status, region.

All clinical streams join on `patientunitstayid`; do not join measurements on `uniquepid`. Preserve event and entry/revision clocks separately. Source bytes stay read-only.

## Falsification and interpretation

**Supportive for a trial-enrichment rationale:** the measurement gate passes; both M0 and admissible M1 estimate a positive pulmonary interaction with 95% interval excluding zero; the lower bound remains above the error-only envelope and includes a clinically consequential magnitude near or above 3 points per 0.10 excess; delayed rather than pre-escalation patterns predominate; and hospital/source/high-coverage checks retain direction. This supports prospective phenotype validation and trial stratification, not oxygen toxicity as a cause.

**Adverse:** the error-only envelope can reproduce the interaction; P1 sensitivity/PPV is poor or differential; the no-term group contains substantial adjudication-supported injury; FiO2 discordance or missingness is stratum/site-dependent; a precise corrected interaction excludes +3 points; association is equal/larger in other ICU states; it begins before escalation; or pressure/severity explains the temporal pattern. This argues against interpreting the parent contrast as pulmonary-specific oxygen harm and may argue against the proposed enrichment rule.

**Inconclusive:** measurement intervals are wide; review is unavailable; indeterminacy or overlap gates fail; fewer than 40 deaths per stratum; M0 and calibrated M1 disagree; or results depend on a few hospitals. An imprecise null does not refute toxicity.

Negative controls are fixed: hour-24–36 burden must not predict a deterioration indicator defined wholly in hours 12–18 after baseline adjustment; documentation-entry delay and LPM-O2, conditional on recorded FiO2, must not reproduce the interaction; shifting diagnosis cutoff from event to entry clock must not create it. Term-family removal, strict ARDS-term-only, P/F 200/300, invasive-support-only, high-coverage hospitals, lab-versus-respiratory FiO2, and source-downsampling are reported jointly and never promoted after favorable results.

Computationally checkable claims include cohort flow, clocks, source mappings, range rules, coverage, source concordance, review sampling/weights, confusion tables, error propagation, calibration, overlap, standardized risks, uncertainty, and whether conclusions obey gates. Automatic verification cannot determine true acute lung injury, bilateral opacity, hydrostatic contribution, clinician oxygen intent, FiO2 delivered at the airway, or oxidative tissue injury. Those require clinician adjudication, source imaging/full charts, device validation, or a prospective study.

## Deliverable, resources, and alternatives

The future solver must newly produce: frozen P0/P1 rules; outcome-blind coverage/concordance census; review sampling frame and packets; adjudication import and M0 bounds; identical hospital folds; an outcome-blind M1 checkpoint and calibration report; primary competing-risk interaction with uncertainty; error-only simulation; falsification matrix; and a conclusion classified supportive, adverse, or inconclusive. Completion is not a positive hypothesis result.

Measured discovery work: the child audit scanned the required structured sources on 8 CPU threads in approximately 62 seconds after bounded script repair. Future estimates are unverified: extraction/packets 1–2 hours on 8–16 CPUs and 64–128 GiB; M0 plus 2,000 cluster bootstraps 2–4 hours on 16 CPUs; M1 1–3 hours per fold on one allocated A100-80GB with 8 CPUs/64 GiB, or a slower CPU Bayesian implementation. Human review, not GPU capacity, is the main dependency. These fit the configured 16-CPU, 8-GPU, 262-GiB, 8-hour planning envelope only for computation; adjudication time is external.

Alternatives retained: a diagnosis-only subgroup was rejected as the primary phenotype because it magnifies documentation dependence; a P/F-only phenotype was rejected because it cannot distinguish acute pulmonary injury from other hypoxemia; treating SpO2 100% as hyperoxemia was rejected [K2]; complete-case analysis remains a sensitivity because selection on dense charting can itself induce the interaction; capture-recapture without clinician anchors was deferred because sources are dependent; and a hospital-preference instrument remains implausible. M0 is primary for auditability. M1 is retained because source reliability, ordering, and latent respiratory versus observation state directly address information M0 loses—not because it is learned or GPU-eligible. Revisit a Berlin-ARDS-specific claim only with images/reports, PEEP and timing adjudication, and cardiac-failure assessment.

## Compact bibliography

[K1] ICU-ROX Investigators and ANZICS Clinical Trials Group; Mackle D, Bellomo R, Bailey M, et al. *Conservative Oxygen Therapy during Mechanical Ventilation in the ICU.* N Engl J Med. 2020;382:989–998. doi:10.1056/NEJMoa1903297. Abstract inspected.

[K2] Nadeau EE, Schwingshackl A, Sturgill JL, Waters CM. *Bench evidence, bedside uncertainty: hyperoxia, mechanical ventilation and lung injury.* Eur Respir Rev. 2026;35:260058. doi:10.1183/16000617.0058-2026. Version-of-record XML sections inspected.

[K3] Bellani G, Laffey JG, Pham T, et al.; LUNG SAFE Investigators and ESICM Trials Group. *Epidemiology, Patterns of Care, and Mortality for Patients With Acute Respiratory Distress Syndrome in Intensive Care Units in 50 Countries.* JAMA. 2016;315:788–800. doi:10.1001/jama.2016.0291. Version-of-record PDF abstract and relevant Methods inspected; supplement not inspected.
