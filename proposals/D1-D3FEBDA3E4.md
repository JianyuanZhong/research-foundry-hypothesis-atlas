> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Timing of loop-diuretic initiation in critically ill patients

## Scientific question and advance

The unresolved question is whether the timing of loop-diuretic initiation after ICU admission changes the risk of subsequent fluid overload, acute kidney injury, or death among patients with fluid accumulation and adequate renal function. This is a consequential decision question: clinicians must choose between early deresuscitation and deferring diuresis after fluid resuscitation.

The strongest claim supported by available evidence is that loop-diuretic timing is clinically important and that post-ICU fluid-accumulation risk is measurable. A recent MIMIC-IV study of sepsis patients found higher early-diuretic initiation and mortality, but that study did not establish a causal effect of initiating diuretics and its timing definitions and confounding strategy are not automatically transferable. This proposal tests a narrower, falsifiable question: among patients who remain fluid-accumulating and have no evidence of clinically important hypoperfusion at the decision point, does initiating a loop diuretic after a prespecified early window increase the risk of subsequent fluid overload, stage 3 AKI, or death compared with deferring diuresis?

The substantive advance over the imported seed is that the hypothesis is bound to exact MIMIC-IV archive members, tables, columns, joins, and time fields; it uses a target-trial estimand rather than a broad association; it separates a simple baseline from a substantive longitudinal alternative; and it prespecifies falsification, competing-risk, uncertainty, and interpretation rules.

## Population, temporal boundaries, and outcome

The primary cohort is adult ICU admissions with an ICU stay of at least 24 hours, a documented admission diagnosis of sepsis or septic shock, and at least 48 hours of ICU observation. A patient is eligible for the early strategy only if a loop diuretic is not started before 48 hours after ICU admission, the patient has no documented norepinephrine infusion or MAP <65 mmHg at the decision point, and at least 24 hours of fluid-accumulation information is available. The early strategy is initiation of any loop diuretic (furosemide, torsemide, or bumetanide) between 48 hours and 72 hours after ICU admission. The deferred strategy is no loop diuretic during that window. Patients who die before the window, have a documented hypotension episode, or have a clinically important indication for diuresis are excluded from the primary analysis.

The primary outcome is time to first of (a) fluid overload, defined as a positive 48-hour fluid balance or documented fluid overload; (b) stage 3 AKI, defined by a creatinine increase >0.3 mg/dL from baseline within 48 hours, a doubling of baseline creatinine, or urine output <0.5 mL/kg/h for more than 6 hours; or (c) death. The primary estimand is the standardized cumulative incidence of the first event by 28 days under the two strategies, with death treated as a competing event. Secondary outcomes are fluid overload and stage 3 AKI alone, and 28-day mortality. Baseline is the ICU admission; follow-up begins at the earliest eligible decision time. All variables are evaluated at or before the decision time, with no use of post-decision measurements for eligibility or covariates.

## Exact data bindings

All sources are read-only. The primary structured data are in `[internal dataset path]`, catalog [source checksum].

- `hosp/admissions` (archive member `mimic-iv-3.1/hosp/admissions.csv.gz`), joined to `icu/icustays` on `(subject_id, hadm_id)`; use `subject_id, hadm_id, intime, outtime, admission_type, hospital_expire_flag`.
- `icu/icustays` (archive member `mimic-iv-3.1/icu/icustays.csv.gz`), joined to admissions and all ICU events on `(subject_id, hadm_id, stay_id)`; use `first_careunit, last_careunit, intime, outtime, los`.
- `icu/chartevents` (archive member `mimic-iv-3.1/icu/chartevents.csv.gz`), joined on `(subject_id, hadm_id, stay_id)`; use `charttime, storetime, itemid, value, valuenum, valueuom`.
- `icu/d_items` (archive member `mimic-iv-3.1/icu/d_items.csv.gz`), joined on `itemid`; use `label, category, unitname` to identify norepinephrine, MAP, lactate, creatinine, urine output, and other prespecified variables.
- `hosp/emar` (archive member `mimic-iv-3.1/hosp/emar.csv.gz`), joined on `(subject_id, hadm_id)`; use `charttime, medication, event_txt, scheduletime, storetime` for diuretic administration and vasoactive medication.
- `hosp/ingredientevents` (archive member `mimic-iv-3.1/icu/ingredientevents.csv.gz`), joined on `(subject_id, hadm_id, stay_id)`; use `starttime, endtime, storetime, itemid, amount, amountuom, rate, rateuom` for fluid input/output and vasoactive administration.
- `icu/outputevents` (archive member `mimic-iv-3.1/icu/outputevents.csv.gz`), joined on `(subject_id, hadm_id, stay_id)`; use `charttime, storetime, itemid, value, valueuom` for urine output.
- `hosp/labevents` (archive member `mimic-iv-3.1/hosp/labevents.csv.gz`), joined on `(subject_id, hadm_id)`; use `charttime, storetime, itemid, value, valuenum, valueuom` for creatinine and other laboratory measurements.
- `hosp/d_labitems` (archive member `mimic-iv-3.1/hosp/d_labitems.csv.gz`), joined on `itemid`; use `label, fluid, category` to define creatinine, fluid balance, and urine-output item IDs.
- `hosp/diagnoses_icd` (archive member `mimic-iv-3.1/hosp/diagnoses_icd.csv.gz`), joined on `(subject_id, hadm_id)`; use `seq_num, icd_code, icd_version` for Sepsis-3 diagnosis.
- `hosp/transfers` (archive member `mimic-iv-3.1/hosp/transfers.csv.gz`), joined on `(subject_id, hadm_id)`; use `eventtype, careunit, intime, outtime` for ICU discharge and readmission.
- `hosp/patients` (ordinary file `[internal dataset path]` is not used; the relevant MIMIC-IV patient table is `hosp/patients` in the archive, archive member `mimic-iv-3.1/hosp/patients.csv.gz`), joined on `subject_id`; use `gender, anchor_age, anchor_year_group, dod` for demographics and death.

The exact source archive and catalog hashes are frozen. No source row is copied into a public artifact.

## Estimand and analysis

The primary analysis is a target-trial emulation with inverse-probability weighting (IPW) or g-formula to estimate the standardized 28-day cumulative incidence of the first fluid-overload/AKI/death event under early versus deferred initiation. The model includes baseline age, sex, admission type, Sepsis-3 diagnosis, ICU length of stay, admission SOFA components, 48-hour fluid balance, urine output, baseline creatinine, lactate, white blood cell count, platelets, sodium, comorbidities, and time-varying covariates measured before each decision. Confounding by indication is addressed with time-varying propensity weights, diagnostics for positivity and residual imbalance, and sensitivity analyses using a stabilized inverse-treatment-weighted model and a pre-specified landmark analysis. Death is a competing event, not silently censored.

The simple baseline is a logistic/competing-risk model using only measured baseline and pre-decision covariates, with no treatment interaction or trajectory. The substantive alternative is a longitudinal, time-varying representation of fluid balance, organ function, and treatment history: a regularized trajectory model or recurrent neural sequence model that updates risk at each decision time and can reveal whether recovery or deterioration trajectories, rather than a single snapshot, predict which patients respond differently to early diuresis. The target is the same standardized event-time outcome; the split is patient-level, with no patient appearing in both strategy groups and all model fitting and tuning on held-out data. The alternative is retained only if it improves prognostic discrimination or calibration and reveals a clinically interpretable trajectory signal; a small predictive gain alone is not a reason to select it.

Baseline comparison uses the simple model; the alternative is compared against the same baseline using held-out discrimination, calibration, and decision-curve metrics. The primary estimand is not a causal safety effect: treatment assignment is observational.

## Falsification and interpretation

Negative-control outcomes and variables are prespecified. Unexpectedly high early-diuretic rates in patients with severe hypotension, low urine output, or rising creatinine before diuresis would challenge the proposed fluid-accumulation phenotype. A positive association between early diuresis and death that persists after time-varying adjustment and competing-risk analysis would support the hypothesis under the stated assumptions. A null result would indicate that this MIMIC population does not support a clinically meaningful difference in these outcomes, or that the decision window, phenotype, or confounding strategy is invalid. An inconclusive result includes inadequate event support, poor positivity, unstable weights, or a trajectory alternative that does not improve over the baseline.

Supportive results would justify a targeted randomized trial of early versus deferred diuresis in a selected fluid-overloaded, normotensive population. They would not establish that early diuresis is safe or beneficial for every patient, nor would they establish microcirculatory or causal mechanisms. Adverse results would argue against routine early diuresis in this setting and identify the need for better phenotyping. Inconclusive results would require more observations, a different decision window, or expert adjudication.

Clinical adjudication is still required for the exact interpretation of fluid overload, organ failure, and indication for diuresis. The automatic verifier can check data provenance, joins, time validity, outcome coding, model fitting, uncertainty, and whether conclusions follow from computed outputs; it cannot establish clinical truth or mechanism.

## Compute and alternatives

The baseline and competing-risk estimand are CPU-feasible and can be run on 8–16 CPUs with 64–128 GiB RAM; no GPU is required. The longitudinal alternative may use one allocated A100 (80 GiB) for repeated fits, with a measured target of under one GPU-hour for training and about ten minutes for inference; these are estimates, not guarantees. The future solver envelope is 16 CPUs, 262,144 MiB, and 28,800 seconds; discovery work is separate.

The three demonstrations were considered. The natural-history transformer is not reproduced because the question is a decision estimand and the local snapshot lacks the required external validation; a bounded adaptation could revisit it if event support and temporal ordering are verified. The longitudinal Bayesian latent model is deferred because the observed ICU trajectory model is more directly identifiable and computationally adequate; it would be revisited if the longitudinal alternative fails to improve calibration or discrimination. The multimodal cancer transformer is not pursued because chest X-rays are unavailable and its main text/STAR Methods were not available; a lab-only adaptation would be a different question.

## References

The three key works below are inspected and attached. K1 is the imported MIMIC-IV diuretic-timing paper; K2 is a landmark systematic review of loop-diuretic trials in fluid-overloaded ICU patients; and K3 is a recent randomized trial that bounds the clinical interpretation of early diuresis.
