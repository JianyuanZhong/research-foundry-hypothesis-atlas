> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Administration-confirmed susceptibility-triggered de-escalation in ICU patients

Parent: `[prior hypothesis]` (`[prior hypothesis]` lineage)
Dataset: MIMIC-IV 3.1, snapshot `[source checksum]`
Source archive: `[internal dataset path]` ([source checksum])

## Scientific question

After the first antimicrobial susceptibility report becomes available, clinicians may narrow broad empiric therapy if an active narrower agent exists. The parent proposal showed that this can be studied using a target-trial emulation anchored at the first **available** susceptibility result rather than a fixed ICU day. The strongest remaining measurement objection is that exposure based on orders or loosely defined antibiotic changes may not reflect what the patient actually received. If de-escalation is recorded when an order changes but the patient still receives the broad agent, or if continuation is recorded when the broad agent is merely delayed, then an apparent mortality association may be an administration artifact rather than a strategy effect.

The unresolved question is therefore:

**Among eligible ICU patients with a single named organism, a susceptible narrower systemic target, and broad empiric therapy active at the first susceptibility-availability time, is administration-confirmed narrowing of broad coverage within 24 hours associated with lower 30-day all-cause mortality than continued administration-confirmed broad coverage, after adjusting for pre-result severity and organism/treatment context?**

This is an associational target-trial estimand, not proof of causality.

## Clinical importance and advance over existing knowledge

- Existing MIMIC-IV evidence at a fixed day-4 landmark found antipseudomonal and anti-MRSA de-escalation not associated with higher mortality [K1]. That evidence is valuable but is anchored to elapsed time rather than the first susceptibility report and does not isolate actual medication receipt.
- Reviews emphasize that de-escalation definitions, eligibility, timing, and safety evidence remain fragmented [K2].
- Randomized biomarker-guided de-escalation can shorten antibiotic duration with similar short-term mortality, but does not model susceptibility and is not powered for mortality [K3].
- This proposal advances [K1] by anchoring at susceptibility availability, requiring an in-vitro susceptible narrower agent, and classifying exposure from **eMAR administration events** joined to order and route details. It tests whether the parent's average comparison survives a stricter administration-based exposure definition and whether effect estimates are stable across clinically plausible timing windows and order-only sensitivity definitions.

If administration-confirmed and order-based definitions agree, the mortality association is less likely to be a simple exposure misclassification artifact. If they diverge, the study will identify a concrete limitation in using order-based stewardship endpoints for mortality inference.

## Exact data bindings

All data are read from the MIMIC-IV 3.1 archive. Derived analyses and outputs are written under the workspace only; source files are never modified.

### Population and follow-up

- `icu/icustays` (`mimic-iv-3.1/icu/icustays.csv.gz`)
  - Keys: `subject_id`, `hadm_id`, `stay_id`.
  - Time fields: `intime`, `outtime`.
  - Additional fields: `first_careunit`, `last_careunit`, `los`.
- `hosp/admissions` (`mimic-iv-3.1/hosp/admissions.csv.gz`)
  - Keys: `subject_id`, `hadm_id`.
  - Time fields: `admittime`, `dischtime`, `deathtime`.
- `hosp/patients` (`mimic-iv-3.1/hosp/patients.csv.gz`)
  - Key: `subject_id`.
  - Age and outcome fields: `anchor_age`, `anchor_year`, `dod`.

One first qualifying ICU stay per `subject_id` is used. Adults are aged at least 18 years at ICU admission. Patients must be alive and hospitalized through the assignment time.

### Culture and susceptibility

- `hosp/microbiologyevents` (`mimic-iv-3.1/hosp/microbiologyevents.csv.gz`)
  - Keys: `microevent_id`, `subject_id`, `hadm_id`, `micro_specimen_id`.
  - Time fields: `chartdate`, `charttime`, `storetime`.
  - Qualifying fields: `spec_type_desc`, `org_name`, `ab_name`, `interpretation`, `isolate_num`, `quantity`.
  - Specimen types are limited to blood, respiratory, urine, or normally sterile fluid.

A qualifying culture is collected from ICU admission minus 24 hours through ICU day 7 and has a non-null named organism and categorical antimicrobial susceptibility. A specimen with more than one named organism is excluded to avoid ambiguous narrowing.

### Medication orders and administrations

- `hosp/emar` (`mimic-iv-3.1/hosp/emar.csv.gz`)
  - Keys: `subject_id`, `hadm_id`, `emar_id`, `emar_seq`, `poe_id`, `pharmacy_id`.
  - Time fields: `charttime`, `scheduletime`, `storetime`.
  - Exposure fields: `medication`, `event_txt`.
- `hosp/emar_detail` (`mimic-iv-3.1/hosp/emar_detail.csv.gz`)
  - Keys: `subject_id`, `emar_id`, `emar_seq`.
  - Administration fields: `administration_type`, `complete_dose_not_given`, `dose_due`, `dose_given`, `product_amount_given`, `route`, `infusion_complete`, `completion_interval`, `new_iv_bag_hung`, `continued_infusion_in_other_location`, `restart_interval`.
- `hosp/prescriptions` (`mimic-iv-3.1/hosp/prescriptions.csv.gz`)
  - Keys: `subject_id`, `hadm_id`, `pharmacy_id`, `poe_id`, `poe_seq`.
  - Time fields: `starttime`, `stoptime`.
  - Order fields: `drug`, `drug_type`, `formulary_drug_cd`, `gsn`, `ndc`, `dose_val_rx`, `dose_unit_rx`, `form_val_disp`, `form_unit_disp`, `doses_per_24_hrs`, `route`.

### Organ support, labs, and diagnoses

- `hosp/labevents` and `hosp/d_labitems`
  - Keys: `subject_id`, `hadm_id`, `itemid`.
  - Time field: `charttime`.
  - Fields: `valuenum`, `valueuom`, `itemid`, `label`.
- `icu/chartevents`, `icu/d_items`, `icu/inputevents`, `icu/outputevents`, `icu/procedureevents`
  - Keys: `subject_id`, `hadm_id`, `stay_id`, `itemid`.
  - Time fields: `charttime`, `starttime`, `storetime`, end-time fields where present.
- `hosp/diagnoses_icd`, `hosp/d_icd_diagnoses`, `hosp/procedures_icd`, `hosp/d_icd_procedures`
  - Keys: `subject_id`, `hadm_id`, `icd_code`, `icd_version`.
  - Used for chronic dialysis, severe immunosuppression, source-control procedures, and long-course infection exclusions.

## Time zero and exposure classification

Let `T0` be the first qualifying susceptibility `storetime`. If `storetime` is missing, `chartdate` at date resolution is a documented fallback. `T0` is operational report availability, not proof of clinician awareness.

The assignment window is `T0` to `T0+24h`. Patients who die, leave the ICU or hospital, enter comfort-only care, or have an unclassifiable exposure before `T0+24h` are excluded before assignment.

### Administration-confirmed active therapy

An antibiotic administration event is accepted only when all of the following are true:

1. The `hosp/emar.medication` name maps to a systemic antibiotic class in the versioned codebook.
2. `hosp/emar.event_txt` is an accepted administration category: `Administered`, `Delayed Administered`, `Administered in Other Location`, or `Administered Bolus from IV Drip`, case-insensitive. `Started`, `Delayed Started`, `Restarted`, `Confirmed`, and `Partial Administered` are accepted only when linked `hosp/emar_detail.administration_type`, `dose_given`, `product_amount_given`, or `new_iv_bag_hung` confirms dose receipt; otherwise they are ambiguous.
3. The linked `hosp/emar_detail.complete_dose_not_given` is not `Yes`.
4. The linked `hosp/emar_detail.route`, when available, is systemic. Topical, ophthalmic, inhaled, and lock preparations are excluded, as is oral nonabsorbed vancomycin. If the route is missing, the linked `hosp/prescriptions.route` is used; if both are missing or ambiguous, the event is excluded.
5. The event is joined to the correct patient and admission by `subject_id` and `hadm_id`, and to the correct event by `emar_id` and `emar_seq`.

A broad class is considered active at `T0` if:
- an accepted administration event for that class occurred before `T0`, or
- a linked `hosp/prescriptions` order for that class spans `T0`, and there is at least one accepted administration event for the same patient and medication before or within 24 hours after `T0`.

### De-escalation and continuation

Within the 24-hour window:

- **De-escalation** requires at least one broad class active at `T0` to stop or not be administered again after its last accepted pre-window or in-window administration, and a systemic in-vitro susceptible narrower agent to receive an accepted administration within 6 hours before or after that broad-class stop and remain active through the window or discharge.
- **Continuation** requires an accepted administration of the same broad class after `T0+6h` and no confirmed loss of all active systemic coverage against the cultured organism.
- Any patient not satisfying either rule is classified as **ambiguous** and excluded, with counts reported.

A linked prescription `stoptime` or an eMAR `Stopped` event can confirm a broad-agent stop only if no accepted administration of that class occurs afterward in the window. This distinguishes a true stop from a delayed dose.

### Measured eMAR feasibility diagnostic

A read-only full-table profile of `hosp/emar` found 42,808,593 rows, including 2,038,269 antibiotic-named rows. `charttime` and `storetime` were nonmissing for every matched antibiotic row. Major matched event categories included 1,787,585 `Administered`, 73,575 `Started`, 66,228 `Stopped`, 12,114 `Delayed Administered`, 5,629 `Administered in Other Location`, 5,132 `Hold Dose`, and 2,970 `Stopped in Other Location` events. The medication names also expose important non-systemic variants that must be excluded by route and product name, including oral liquid and ophthalmic vancomycin, vancomycin enema, heparin locks, topical metronidazole, ophthalmic/inhaled aminoglycosides, and desensitization or graded-challenge protocols. The complete counts are retained in `work/emar_antibiotic_profile.json`.

### Sensitivity definitions

- Order-only definition: use only `hosp/prescriptions.starttime`, `stoptime`, `drug`, and `route`.
- Administration-only definition: use only accepted eMAR events.
- Timing sensitivity: 12-hour and 48-hour assignment windows.
- Report exposure discordance, stop/restart rates, and the proportion of patients whose classification changes under each definition.

## Outcomes

Primary outcome: all-cause death within 30 days after `T0+24h`, using `hosp/patients.dod`. Date-boundary ties are conservatively assigned to death.

Secondary outcomes:
1. ICU-free and hospital-free days through day 14 and day 28.
2. Death-adjusted antibiotic-free days through day 14 and day 28.
3. KDIGO stage 2–3 creatinine-based AKI within 7 days among patients without chronic dialysis.
4. Recurrent or persistent positive culture with a resistant organism within 14 days, interpreted cautiously because follow-up cultures are selectively ordered.

## Analysis

### Baseline: overlap-weighted target-trial emulation

1. Define the eligible population and assignment groups before follow-up.
2. Estimate the propensity for administration-confirmed de-escalation using pre-`T0` variables only:
   - age, sex, admission type, ICU length of stay before `T0`;
   - first care unit, mechanical ventilation, vasopressor or renal-replacement support;
   - latest creatinine, bilirubin, platelets, lactate, and white-cell count;
   - pre-`T0` slopes over 24–48 hours;
   - organism, specimen type, susceptibility pattern, and antibiotic classes active at `T0`.
3. Apply overlap weights (`w=1-e` for de-escalation, `w=e` for continuation). Trim only prespecified propensity values outside `[0.01,0.99]`.
4. Report standardized mean differences before and after weighting.
5. Estimate the 30-day absolute risk difference and relative risk using weighted logistic regression with no post-baseline covariates.
6. Use patient-level nonparametric bootstrap with 2,000 replicates for 95% confidence intervals. Report cluster-robust standard errors as a sensitivity.

### Substantive alternative: dynamic-state model

A learned alternative tests whether the average comparison masks heterogeneity across evolving patient states.

- Inputs: only data available from ICU admission through `T0`, including SOFA-proxy components, time-delta summaries, antimicrobial classes, organism/susceptibility tokens, and demographics/support.
- Fitting target: a discrete-time 30-day mortality hazard model and an auxiliary 7-day organ-worsening calibration model, using gradient-boosted trees or a small regularized neural sequence model fixed before outcome analysis.
- Split: patient-level 70/15/15 train/calibration/test, stratified by exposure and outcome.
- Evaluation: test AUROC, Brier score, calibration intercept/slope, and overlap by decile; then cross-fitted AIPW estimates for the average effect and exposure-by-organ-state interaction.
- Scientific addition: the baseline can estimate an average contrast but cannot show whether benefit is concentrated in improving/stable patients or whether nonlinear trajectory adjustment changes the estimate.
- Limitation: even a well-calibrated model cannot adjust for unrecorded source control, clinician concern, or actual awareness of results.

A full marginal structural model is deferred unless more than 10% of patients switch treatment after assignment.

## Falsification and interpretation

Supportive:
- De-escalation has lower 30-day mortality with a confidence interval excluding zero, overlap and balance criteria pass, and administration/order discordance is low.
- Strongest claim: an association in this overlap population under the operational exposure definition. This can inform prospective stewardship study design, not a clinical recommendation.

Adverse:
- The point estimate favors continuation or the confidence interval excludes only no harm.
- Strongest claim: the susceptibility-triggered de-escalation strategy may be unsafe in this population and requires prospective evaluation.

Inconclusive:
- Confidence intervals include clinically important benefit and harm, overlap is poor, or exposure classification discordance exceeds 20%.
- Strongest claim: the data do not resolve the mortality question.

Falsification tests:
- If administration-confirmed and order-only definitions produce materially different exposure groups or effect estimates, the order-based exposure is not a valid substitute for receipt.
- A pre-`T0` negative-control outcome should not be associated with post-`T0` exposure.
- A clinically implausible narrowing unrelated to the cultured organism should not show the primary association.
- Excluding patients with source-control procedures should not fully explain the result.

Claims requiring additional evidence:
- actual clinician awareness of the susceptibility report;
- clinical appropriateness of a susceptible narrower agent given source, penetration, allergies, renal dosing, and toxicity;
- source-control adequacy and goals of care;
- external multicenter validation;
- prospective stewardship evaluation for a causal or practice-changing safety claim.

## Method-selection rationale

The overlap-weighted target-trial baseline is transparent, computationally stable, and directly estimates the average strategy contrast. The dynamic-state alternative adds scientific information about heterogeneity and nonlinear trajectory adjustment that the baseline loses. CPU is expected to suffice for the baseline. If the learned sequence model is used in the future solver, one A100 GPU is requested only if a measured CPU pilot exceeds the planning envelope. This is a planning choice, not a claim that GPU use improves scientific validity.

## Deliverables

- cohort flow diagram and codebook;
- exposure classification and administration/order discordance report;
- propensity overlap and balance diagnostics;
- primary 30-day mortality estimate with uncertainty;
- dynamic-state model performance and heterogeneity estimates;
- sensitivity analyses and falsification outputs;
- an interpretation file that states whether the result is supportive, adverse, or inconclusive.
