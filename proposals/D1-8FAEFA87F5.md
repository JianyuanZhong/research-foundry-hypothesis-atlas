> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Diuretic initiation in fluid-accumulating critically ill patients

## Scientific question and advance

The unresolved question is whether the timing of loop-diuretic initiation after ICU admission changes the risk of subsequent fluid overload or adverse outcomes among patients who are still fluid-accumulating and have adequate renal function. The clinically important decision is whether a clinician should consider early diuresis after fluid resuscitation, or reserve it for patients whose fluid status and organ function support it.

The strongest claim supported by available evidence is that loop-diuretic timing is an important, clinically consequential issue and that post-ICU fluid-accumulation risk is a plausible outcome to measure. The imported literature record for this seed is relevant documentation, not evidence that the MIMIC-IV comparison is identifiable. A recent MIMIC-IV study of sepsis patients found higher early diuretic initiation and mortality, but that study did not establish a causal effect of initiating diuretics and its timing definitions and confounding strategy are not automatically transferable. This proposal tests a narrower, falsifiable question: after a prespecified fluid-accumulation and stable-perfusion state, does early versus delayed initiation of a loop diuretic have an association with subsequent fluid overload, and does that association differ by a prespecified subgroup?

The substantive advance is to make the question testable in MIMIC-IV rather than leaving it as a treatment-timing hypothesis. It explicitly models time-varying confounding and competing ICU discharge/death, and it asks whether the observed association survives a negative-control test. The experiment does not claim that diuretic initiation causes fluid overload or that early initiation improves outcomes.

## Population, time origin, and estimand

The primary population is a MIMIC-IV ICU stay with at least 24 hours of ICU time, no recorded death before the index time, and no ICU transfer before the index time. The index time is the earliest time after ICU admission when the patient has:

- at least 12 hours of ICU time;
- at least three ICU chart-event timestamps, at least one of which is at least 12 hours after ICU admission;
- at least two non-missing, non-infinite ICU chart-event values in the perfusion window;
- at least one ICU input-event row in the fluid window; and
- no ICU transfer or death before the index time.

The perfusion window is ICU admission plus 12 through 48 hours. The fluid window is ICU admission plus 48 through 72 hours. The treatment window is ICU admission plus 72 through 96 hours. The outcome window is ICU admission plus 96 hours through ICU discharge or death, whichever occurs first.

A patient is eligible for a treatment assignment only if the treatment window contains at least one valid loop-diuretic administration record. A record is valid when its pharmacy row has medication equal to the exact MIMIC label Furosemide, Bumetanide, or Torsemide, and its proc_type is Unit Dose. The index is the earliest valid record whose starttime is in the treatment window. The exposure is early versus delayed: early if the index is at or before the 96-hour mark and delayed if it is after 96 hours. A patient is classified as delayed only if the earliest valid record is after 96 hours; patients without a valid record are not treated as a comparison group.

The primary estimand is the time-varying causal effect of early versus delayed diuretic initiation among patients who are eligible at 72 hours and remain eligible through the outcome window, conditional on a prespecified baseline and time-varying covariate model. The estimand is a target-trial estimand, not an unadjusted association. The primary outcome is cumulative time to first ICU discharge or death, with discharge as a competing event and death as the primary endpoint of interest. A secondary outcome is time to first documented ICU fluid overload, defined as a new ICU input-event row with itemid 220862 (colloids) or 226452 (oral/gastric intake) after the 96-hour mark, or an ICU output-event row with itemid 226560 (urine) showing a new positive value after 96 hours, subject to a sensitivity rule for repeated measurements. This outcome is a surrogate and may be incomplete.

## Exact data bindings

All source data are read-only from the MIMIC-IV 3.1 snapshot. The source archive is [internal dataset path] ([source checksum]). The relevant archive members, columns, joins, and time fields are:

- mimic-iv-3.1/hosp/admissions.csv.gz: subject_id, hadm_id, admittime, dischtime, deathtime, hospital_expire_flag. Join to ICU stays on subject_id, hadm_id.
- mimic-iv-3.1/icu/icustays.csv.gz: subject_id, hadm_id, stay_id, intime, outtime, last_careunit. Join to admissions and other ICU tables on subject_id, hadm_id.
- mimic-iv-3.1/hosp/pharmacy.csv.gz: subject_id, hadm_id, pharmacy_id, poe_id, starttime, stoptime, medication, proc_type, status, entertime, verifiedtime, route, infusion_type, duration. Join to admissions on subject_id, hadm_id; use starttime, stoptime, medication, proc_type, status for treatment assignment.
- mimic-iv-3.1/icu/inputevents.csv.gz: subject_id, hadm_id, stay_id, starttime, endtime, itemid, amount, amountuom, rate, rateuom, ordercategoryname, ordercategorydescription, totalamount, totalamountuom. Join to admissions and icustays on subject_id, hadm_id, stay_id; use starttime, endtime, itemid, amount, rate, ordercategoryname, ordercategorydescription for fluid input and treatment records.
- mimic-iv-3.1/icu/outputevents.csv.gz: subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valueuom. Join on subject_id, hadm_id, stay_id; use charttime, itemid, value, valueuom for urine output and fluid-accumulation outcomes.
- mimic-iv-3.1/icu/chartevents.csv.gz: subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valuenum, valueuom. Join on subject_id, hadm_id, stay_id; use charttime, itemid, value, valuenum, valueuom for perfusion, lactate, vital-sign and organ-support variables.
- mimic-iv-3.1/hosp/d_labitems.csv.gz: itemid, label, fluid, category. Join on itemid; use it to map 220862, 226452, 226560, and other relevant item IDs to labels and categories.
- mimic-iv-3.1/hosp/patients.csv.gz: subject_id, anchor_age, anchor_year, anchor_year_group, dod. Join on subject_id; use dod to establish death and avoid calendar-time leakage.

The catalog also confirms hosp/transfers has subject_id, hadm_id, transfer_id, eventtype, careunit, intime, outtime; use it to verify no transfer before the index. The note tables are not required for this structured analysis.

## Variables and phenotype

The baseline phenotype is defined using only data available before 72 hours. Fluid accumulation is a positive balance in the fluid window: the difference between summed valid input-event amounts and summed valid output-event amounts, with a minimum positive balance of 2,000 mL. Perfusion is defined as the mean of validated lactate, mean arterial pressure, and central venous pressure during the perfusion window, with a minimum of two valid measurements for each and no value below the prespecified clinical cutoff. Organ support is a binary flag for any recorded mechanical ventilation, renal replacement therapy, or vasopressor use in the perfusion window, using validated chartevents and inputevents item IDs. The primary analysis includes patients with adequate renal function, defined as at least one valid creatinine measurement in the perfusion window with valuenum at least 0.3 mg/dL and below 5.0 mg/dL. These cutoffs are prespecified and are not chosen after seeing the treatment effect.

Perfusion and fluid status are updated at 72-hour intervals during the outcome window. At each update, the model may use only data available before the update. A patient who develops a new ICU transfer, death, or an event that changes eligibility is censored or treated as a competing event according to the prespecified rule. The primary model is a time-varying Cox model or a target-trial inverse-probability-of-treatment-weighted marginal structural model, with a shared baseline and time-varying covariate process. The model includes age, sex, admission type, baseline creatinine, baseline lactate/MA/central venous pressure, baseline fluid balance, baseline organ-support status, baseline vasopressor use, baseline ICU length of stay, and all baseline laboratory and vital-sign covariates available before 72 hours. It also includes time-varying updates for fluid balance, lactate, MAP, central venous pressure, vasopressor use, and organ support.

## Baseline and substantive alternative

The baseline is a time-varying Cox model with robust standard errors and inverse-probability-of-treatment weights. It estimates the observed association between early and delayed diuretic initiation and the primary outcome while adjusting for the measured time-varying covariates. The alternative is a targeted learning model, a two-stage model in which the first stage fits a flexible longitudinal model for fluid balance and perfusion using only pre-treatment and time-varying covariates, and the second stage estimates the treatment effect using the predicted latent fluid/organ-status trajectory. The alternative can reveal whether the treatment effect is concentrated among patients whose evolving trajectory is close to a fluid-overload state, or whether it is driven by a small subgroup with stable perfusion. It can also test whether a nonlinear or trajectory-based explanation improves estimation beyond the baseline. The alternative is not selected for a small predictive gain; it is selected because it can distinguish a stable-perfusion subgroup effect from a general fluid-overload effect that the baseline may average away.

For both models, the future solver must fit the model on the full eligible cohort, report calibration, discrimination, decision-curve or clinically meaningful risk estimates, and uncertainty from bootstrap or exact inference. The primary result is the weighted risk difference or hazard ratio for early versus delayed initiation, with 95% confidence intervals and a sensitivity analysis without inverse-probability weights. The alternative’s improvement must be judged on whether its trajectory estimates change the clinical interpretation, not merely on a small AUC difference.

## Falsification and interpretation

A negative-control falsification is required. Using only data available before 72 hours, fit the same baseline and alternative models for a prespecified outcome that should not be affected by diuretic initiation, such as a new ICU transfer or death from a cause unrelated to fluid overload. The negative-control association should be small and stable; a large or clinically important association suggests residual confounding or measurement artifact and invalidates the primary causal interpretation. The negative-control outcome is not a substitute for the primary outcome.

Supportive evidence is a prespecified, clinically meaningful risk difference or hazard ratio for early versus delayed initiation among patients with adequate renal function, with a confidence interval excluding the null and a negative-control result that is not materially different from the primary result. It would support a cautious, population-stratified hypothesis that early initiation is associated with different fluid-overload trajectories, not that it causes fluid overload.

Adverse evidence is a null or reversed association, a confidence interval that includes no clinically meaningful effect, or a negative-control result that is large and stable. This would argue against a simple early-versus-delayed treatment interpretation and would require revisiting the phenotype, timing, confounding, or selection assumptions.

Inconclusive evidence is wide confidence intervals, poor event support, substantial time-varying confounding, poor model calibration, a failed negative-control test, or a result that changes materially under prespecified sensitivity analyses. It means the available data cannot resolve the question; it does not prove that early or delayed diuretics are safe or harmful.

## Required deliverable and limitations

The future solver must newly fit the baseline time-varying model, the alternative trajectory model, the weighted and unweighted estimands, the competing-risk analysis, and the negative-control analysis. Required outputs are the cohort and eligibility counts, item-ID mappings, time-varying covariate trajectories, treatment probabilities, weights, outcome tables, model convergence and calibration, uncertainty estimates, subgroup estimates, and a conclusion linked to these outputs. The solver must not report a causal effect if the negative-control or selection criteria fail.

The strongest claim this experiment can establish is an association or a target-trial estimand under explicit assumptions. It cannot establish a mechanism, prove that diuretic initiation causes fluid overload, establish safety, or establish that early initiation improves outcomes. Those claims require expert clinical adjudication of indication and treatment response, additional validated measurements of microcirculatory perfusion and fluid status, and an external validation cohort. The MIMIC-IV timestamps are subject-specific shifted timestamps; within-subject intervals are preserved but cross-subject calendar alignment is invalid. The study also cannot establish the full causal effect of delaying diuresis in all critically ill patients because treatment eligibility and selection are constrained by the available data.
