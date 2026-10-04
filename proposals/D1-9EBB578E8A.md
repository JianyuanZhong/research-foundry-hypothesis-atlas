> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Persistent hyperlactatemia, perfusion trajectory, and the next crystalloid decision
Parent: `[prior hypothesis]`
Status: reference-complete experiment proposal. Only outcome-blind support diagnostics have run; no outcome contrast or treatment effect has been estimated.

## Opening and hypothesis

Lactate is a severity marker but not a specific perfusion readout: adrenergic production, impaired clearance, drugs, and sampling timing are alternatives [K2]. ANDROMEDA-SHOCK shows peripheral-perfusion- and lactate-targeted resuscitation are not interchangeable [K1]. CLASSIC found no significant 90-day mortality difference with restricted versus standard fluid in septic shock, bounding any simple “more is better” premise [K3]. None answers the next-bolus question in persistent hyperlactatemia.

Hypothesis: among ICU patients whose second available blood lactate remains >=2 mmol/L, the 24-hour risk difference under initiating >=500 mL additional isotonic crystalloid versus no additional bolus is more favorable in a worsening than an improving pre-decision measured-perfusion trajectory. The main rival is severity/clinician selection; observation intensity, prior treatment, and non-perfusion lactate biology are explicit alternatives. This can falsify an EHR phenotype, not prove fluid responsiveness or mechanism.

## Target trial

Use the first qualifying ICU stay per `subject_id` and first landmark therein. Admission age is `anchor_age + year(icustays.intime) - anchor_year`; require >=18. Require non-null ICU `outtime` and `intime+6h <= t0 < outtime`.

Two blood lactates (`labevents.itemid` 50813/52442/53154), each 2–30 mmol/L and >=2, must have `charttime` 2–12 h apart. `t0` is the later result's `storetime`; require `charttime <= storetime <= charttime+2h`, earlier `storetime<t0`, and every phenotype/confounder record to have event time and, where present, `storetime<t0`. Exclude NS/LR already active across t0.

The broad eligible cohort is the target-trial population. The primary phenotype estimand is in an observable subset with weight 30–250 kg, >=2 valid MAP values and >=1 urine event in each three-hour half, plus interpretable pressor history. Report selection flow and baseline differences. Missing domains are not coded stable; inverse observation weighting is sensitivity only.

Eligible fluid is NaCl 0.9% (`inputevents.itemid=225158`) or LR (225828), positive mL amount, status not Rewritten/Stopped. Because 225158 includes carriers, drips, and pushes, retain only rows whose four order-category fields identify IV-fluid/crystalloid bolus or continuous crystalloid; exclude drug pushes, medication carriers, and antibiotic-associated rows. Freeze retained category values and an outcome-blind sample audit.

Strategies in `[t0,t0+2h)`:

- bolus: initiate and cumulatively administer >=500 mL;
- no bolus: administer <=250 mL;
- 250–499 mL is compatible with neither once known.

Clone each record to both strategies at t0, censor at first incompatibility in 30-minute bins, and weight artificial censoring using history available before each bin. Follow-up begins at t0, retaining early deaths. Later fluid and post-initiation pressors/ventilation/RRT are downstream and not adjusted away.

## Phenotype, outcome, estimand

Compare `[t0-6h,t0-3h)` to `[t0-3h,t0)`. MAP improves/worsens if late-minus-early median is >=5/<=-5 mmHg. Norepinephrine-equivalent dose improves if mean falls >=0.05 mcg/kg/min or all pressors stop, and worsens if it rises >=0.05 or a pressor starts; zero in both halves is stable. Urine improves if late rate is >=0.5 mL/kg/h and rises >=0.2, and worsens if late rate is <0.5 and falls >=0.2. Improving requires >=2 improving and no worsening domains; worsening is symmetric. Stable/discordant records remain descriptive. Freeze thresholds and dose conversion before outcomes.

Primary `Y24` is death in `(t0,t0+24h]` or vasopressor infusion overlapping `[t0+23h,t0+25h]`. Alive ICU/hospital discharge before hour 23 without later overlap is event-free and separately reported; a competing-state sensitivity separates death, ongoing ICU pressor, alive ICU stay without pressor, and discharge. This measures failure to become alive and pressor-free, not responsiveness.

Estimate standardized `RD=risk(bolus)-risk(no bolus)` in worsening and improving phenotypes. Primary `Delta=RD_worsening-RD_improving`; negative is a more favorable bolus contrast in worsening. Secondary endpoints: hospital/28-day death; new invasive ventilation or RRT by 48 h among unsupported patients; and six-hour lactate change only among remeasured patients with a remeasurement model (never called “clearance”).

## Baseline and longitudinal alternative

Baseline: prespecified splined strategy and 30-minute censoring models plus a weighted doubly robust standardized logistic model containing strategy, phenotype, interaction, and baseline covariates. Inputs are demographics/context; 24-h lactate level/slope/lag/count; MAP, heart rate, urine, weight, pressor dose, crystalloid, ventilation/RRT; pH/base excess, creatinine, bilirubin, AST/ALT, albumin, hemoglobin, platelets, WBC, sodium, potassium; and counts, time since last value, distinct measurement hours, and store lag. No post-landmark diagnoses or notes.

Use subject-isolated `anchor_year_group`: development 2008–2016, validation 2017–2019, locked test 2020–2022. Raw shifted calendar year is not a real era. Primary stabilized-weight truncation is development 1st/99th percentiles; report untruncated and 2.5th/97.5th sensitivities. Use 2,000 subject bootstraps repeating fitting.

Before opening outcomes, every development propensity decile within phenotype needs >=20 records per strategy and probabilities 0.05–0.95; validation/test need >=200 per phenotype-strategy cell. After weighting require ESS>=100/cell, maximum truncated weight <=30, and key weighted SMDs <0.10. Failure is `inconclusive_positivity`; report no CATE outside support.

Alternative: on the identical cohort/strategies/outcome/estimand/split/weights, fit an outcome-blind masked switching state-space model to 12 half-hour pre-t0 bins. Inputs are MAP median/minimum, pressor mean/maximum, urine/kg, HR, prior fluid, lactate, pH/base excess, renal/hepatic labs, ventilation/RRT, and mask/count/time-since/store-lag channels. Fit to observed-data likelihood plus next-bin MAP/pressor/urine prediction; never expose outcome or post-t0 treatment. Compare 2/3/4 states and latent dimensions 4/8; require each state >=10% of validation landmarks. Align ten starts; >=8/10 need ARI>=0.70. Freeze, infer test posterior states, and interact posterior—not post hoc labels—with strategy.

This preserves timing, discordance, uncertainty, and intermittency lost by scalar thresholds. It is useful only if target-trial gates pass, held-out weighted log loss improves >=0.01, the interaction excludes zero across starts, and values+masks outperform masks/store lag alone. It remains an EHR state.

Falsifications: mask/count/store-lag-only; 100 within-person time permutations preserving masks and value multisets (observed gain/interaction must beat 95); prediction of a future unrelated treatment decision at 24–26 h among survivors; and D5W (220949) as specificity exposure. Comparable effects favor observation/treatment preference.

## Interpretation rules

Material interaction is five risk points.

- Supportive: gates pass; `upper95(Delta)<-0.05`, `upper95(RD_worsening)<0`, `lower95(RD_improving)>-0.02`, and weight/endpoint sensitivities agree. This supports heterogeneous historical strategy contrasts, not causal benefit.
- Adverse: gates pass and `lower95(Delta)>0`; or Delta is wholly within [-0.05,+0.05] while both stratum intervals exclude a five-point benefit.
- Inconclusive: category/timing, positivity, balance, stability, or null gates fail; ESS<100; intervals include material heterogeneity and none; or reasonable specifications conflict.

B cannot rescue failed support. A supportive/B null retains A; stable B supportive/A null is learned-state heterogeneity only. Precise adverse results from both abandon this direction; imprecision motivates revision.

## Exact source binding

Read-only MIMIC-IV 3.1 archive: `[internal dataset path]`, [source checksum].

- `mimic-iv-3.1/hosp/patients.csv.gz`: subject_id, gender, anchor_age, anchor_year, anchor_year_group, dod.
- `hosp/admissions.csv.gz`: subject_id, hadm_id, admittime, dischtime, deathtime, admission_type/location, discharge_location, insurance, race.
- `icu/icustays.csv.gz`: subject_id, hadm_id, stay_id, first/last_careunit, intime, outtime.
- `hosp/labevents.csv.gz`: labevent_id, subject_id, hadm_id, itemid, charttime, storetime, valuenum, valueuom; dictionary `hosp/d_labitems.csv.gz`.
- `icu/chartevents.csv.gz`: subject_id, hadm_id, stay_id, charttime, storetime, itemid, valuenum, valueuom, warning.
- `icu/inputevents.csv.gz`: subject_id, hadm_id, stay_id, starttime, endtime, storetime, itemid, amount/uom, rate/uom, four order-category fields, patientweight, statusdescription.
- `icu/outputevents.csv.gz`: subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valueuom.
- `icu/procedureevents.csv.gz`: subject_id, hadm_id, stay_id, starttime, endtime, storetime, itemid, value/uom, statusdescription.
- `icu/d_items.csv.gz`: itemid, label, abbreviation, linksto, category, unitname, param_type.

Join patients→admissions by subject_id, admissions→stays by subject_id+hadm_id, ICU events by subject_id+hadm_id+stay_id, and labs by subject_id+hadm_id plus ICU-interval containment. IDs: lactate 50813/52442/53154; MAP 220052/220181; HR 220045; NS/LR 225158/225828; norepinephrine 221906; epinephrine 221289/229617; vasopressin 222315; phenylephrine 221749/229630/229631/229632; dopamine 221662; ventilation 225792; RRT 225441/225802/225803/225809/225955; urine 226557–226565/226567/226627/226631, excluding mixed irrigant 226566/227489. Full lab IDs are frozen in `work/hyperlactate-methods.md`.

## Feasibility, deliverable, and limits

Completed permissive outcome-blind scan: 86,958 adult stays >=16 h; 15,662 repeated-lactate stays; 3,690 started >=500 mL within 2 h; 4,894 received 1–499 mL; 7,078 had no new start; 8,791 had fluid active at provisional t0. These predate strict availability/category/observability/positivity filters and prove gross support only.

Deliverable: newly fitted emulation and outcome-blind trajectory model yielding cohort flow, category audit, overlap/balance/ESS, stratum risks/RDs, Delta with uncertainty, nulls, and conclusion code. Estimated resources: extraction 1.5–2.5 h; baseline/bootstraps 2–3 h on 16 CPU/96 GiB; ten-start state-space/nulls 2–3 h on one A100/8 CPU/64 GiB. Full-run estimates are unmeasured.

Unavailable: clinician intent, indication, capillary refill, passive-leg-raise/echo response, congestion, bleeding, source control, and goals of care. Notes can support blinded adjudication, not recover counterfactual intent. A supportive result remains observational under consistency, timing, no interference, positivity, and measured exchangeability. A pragmatic trial with bedside perfusion/fluid-responsiveness data is needed for a treatment rule.

## Exactly three inspected works

[K1] Hernández G, Ospina-Tascón GA, Damiani LP, et al. *Effect of a Resuscitation Strategy Targeting Peripheral Perfusion Status vs Serum Lactate Levels on 28-Day Mortality Among Patients With Septic Shock: The ANDROMEDA-SHOCK Randomized Clinical Trial.* JAMA. 2019. doi:10.1001/jama.2019.0071. Full-text excerpt inspected.

[K2] Andersen LW, Mackenhauer J, Roberts JC, et al. *Etiology and therapeutic approach to elevated lactate levels.* Mayo Clin Proc. 2013. doi:10.1016/j.mayocp.2013.06.012. Full-text excerpt inspected.

[K3] Meyhoff TS, Hjortrup PB, Wetterslev J, et al. *Restriction of Intravenous Fluid in ICU Patients with Septic Shock.* N Engl J Med. 2022. doi:10.1056/NEJMoa2202707. Abstract-only inspection; publisher full text unavailable.
