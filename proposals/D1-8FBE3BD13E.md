> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Episode 25: renal-reserve effect modification of post-shock loop initiation

**Parent:** `[prior hypothesis]`

## Unresolved question and substantive advance

The parent asks whether a qualifying ICU-input-system recorded furosemide/bumetanide delivery during the 24 hours after the first broad hour-48 post-shock opportunity improves a durable respiratory-recovery endpoint. That is clinically consequential, but an average effect is not yet a bedside rule: clinicians need to know whether the same fluid-removal decision is more useful in a patient with substantial accumulation and preserved renal reserve, and more dangerous or ineffective in a patient with renal vulnerability.

The strongest supported claim from current evidence is narrower: conservative-fluid or deresuscitation strategies can change recorded fluid balance, while patient-centered benefit, renal safety, timing, and the clinically appropriate target population remain unresolved. The available MIMIC fields can test an observational, recorded-strategy version of the treatment-effect heterogeneity question; they cannot establish that the loop was given by every route, that the patient was clinically ready, or that an estimated contrast is causal.

**Hypothesis.** Among adults who reach the parent's first eligible broad hour-48 opportunity and have at least 100 mL/kg cumulative delivered fluid balance at the decision time, the risk difference for definite recorded respiratory recovery by day 28 (DRR28) from initiating a qualifying recorded loop delivery rather than avoiding that recorded event is greater in the renal-reserve stratum than in the renal-vulnerable stratum by at least 5 percentage points. The prespecified directional clinical pattern is a DRR28 risk difference >+5 percentage points in the renal-reserve stratum, with no positive DRR28 effect in the renal-vulnerable stratum and no more than +5 percentage points excess observed RRT7 or +3 percentage points excess recorded death/hospice/acute discharge in either stratum. If the interaction is absent, reversed, or not identifiable, the proposed patient-selection rule is falsified or inconclusive; the average parent hypothesis is not thereby proven or disproven.

Define renal vulnerability without using post-`t0` information: latest decision-available blood creatinine at or before `t0` is >=2.0 mg/dL **or** delivered urine output in the preceding 6 hours is <=0.50 mL/kg/hour (while retaining the parent's >0.10 mL/kg/hour eligibility floor). Renal reserve is the complementary category. The high-congestion analysis is primary for the heterogeneity question; the parent's full positive-balance population remains a prespecified secondary effect estimate. The 100 mL/kg threshold and creatinine/urine thresholds are fixed before outcome inspection. No alternative cut-point search or machine-learned subgroup discovery is permitted.

This is a substantive advance over the parent because it tests a decision-relevant benefit–harm tradeoff and identifies whether a broad “deresuscitate after shock” result would be clinically misapplied to renal-vulnerable patients. It does not turn a subgroup association into a treatment recommendation.

## Population, time zero, exposure and partition

Use the read-only MIMIC-IV 3.1 snapshot:

- source archive: `[internal dataset path]`
- archive [source checksum]
- catalog [source checksum]
- snapshot: `[source checksum]`

Apply the configured discovery partition before inspecting eligibility:
`SHA256(ASCII("ehr-hypothesis-discovery-v1") + NUL + ASCII("mimic") + NUL + ASCII(canonical base-10 subject_id)) mod 100`; retain buckets 0–79 only. Never inspect 80–99 and do not call them validation. Emit subject ID, digest, bucket, partition and checksum. Split folds, bootstrap samples and both treatment clones by subject.

For each subject select only the earliest broad ICU stay ordered by (`icustays.intime`, `stay_id`) with nonmissing `intime/outtime` and `intime <= t0 < outtime`, where `t0 = intime + 48 hours). Require the masked retrospective Boolean crossing of invasive ventilation from `icu/procedureevents` item 225792: valid keys, nonmissing `starttime,endtime,storetime`, `starttime < endtime`, `starttime <= t0 < endtime`, and final status in {FinishedRunning, Stopped}; Paused is sensitivity only. Use no future end time, duration, later status update or store lag as a covariate, eligibility gate beyond crossing, exposure or outcome. A failed first opportunity never reopens on a later stay; report repeated-opportunity and later-only-qualifier audits.

Retain the parent's adult and post-shock gates: `admissions.admittime < t0 < dischtime`, valid deterministic terminal resolution and `hospital_expire_flag`, age >=18 from `anchor_age + year(admittime) - anchor_year`, positive delivered balance >=+50 mL/kg from ICU `intime` through `t0`, valid decision-time weight 30–300 kg, no qualifying vasopressor delivered in `(t0-6h,t0]`, median MAP >=65 in `(t0-3h,t0]`, urine output >0.10 mL/kg/hour in `(t0-6h,t0]`, latest decision-available potassium >=3.0 mmol/L in `(t0-12h,t0]`, no active ECMO or delivered RRT at `t0`, and no qualifying loop in `(t0-12h,t0]`. Every measurement is selected by clinical/chart time with `storetime <= t0`, except the masked ventilation Boolean. A missing creatinine or an unclassifiable urine window is not silently assigned to renal reserve: it is excluded from the primary modifier analysis, retained in an observability audit, and included in a missingness sensitivity with an explicitly inconclusive interpretation.

The high-congestion effect-modification cohort then requires balance >=100 mL/kg at `t0). Report the 50–<100 mL/kg cohort as a prespecified lower-congestion transportability/interaction sensitivity, not as a replacement threshold.

Qualifying exposure remains a recorded strategy, never a claim of actual all-route treatment or IV administration: `icu/inputevents.itemid in {221794,228340,229639}`, dictionary-verified furosemide/bumetanide, matching (`subject_id,hadm_id,stay_id`), `t0 < starttime <= G=t0+24h`, `starttime < endtime`, `starttime < icustays.outtime`, nonmissing start/end/store, `starttime <= endtime`, final status in {FinishedRunning, ChangeDose/Rate, Stopped}, and positive mg amount or positive mg/hour rate for a positive duration. Unknown units, orders, canceled/not-started, nonpositive and unresolved-key rows are not exposure. Paused is sensitivity. There is no route field in `inputevents`.

Clone each eligible person to initiate-versus-avoid at `t0). Let `T` be the parent's deterministic admissions-only terminal resolver and `E=icustays.outtime`; `D=min(G,T,E)). Apply the same transition order and tie sensitivities as the parent: T/E first closes both clones while retaining outcomes; a qualifying delivery satisfies A and censors B; unresolved candidate rows censor both; G completes B and censors unsatisfied A. ICU exit and terminal events are competing closures, not censoring. eMAR is a coverage/contamination diagnostic only; absence never proves avoidance.

## Exact source bindings

Required archive members, tables, joins and fields are:

- `mimic-iv-3.1/hosp/patients.csv.gz`, `hosp/patients`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`.
- `mimic-iv-3.1/hosp/admissions.csv.gz`, `hosp/admissions`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`.
- `mimic-iv-3.1/icu/icustays.csv.gz`, `icu/icustays`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime`.
- `mimic-iv-3.1/icu/inputevents.csv.gz`, `icu/inputevents`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,patientweight,statusdescription,totalamount,totalamountuom`.
- `mimic-iv-3.1/icu/procedureevents.csv.gz`, `icu/procedureevents`: `subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,statusdescription,continueinnextdept,orderid,linkorderid`.
- `mimic-iv-3.1/icu/d_items.csv.gz`, `icu/d_items`: `itemid,label,abbreviation,linksto,category,unitname`; confirm loop, ventilation, dialysis, MAP, vasopressor, output and weight semantics from this dictionary.
- `mimic-iv-3.1/icu/chartevents.csv.gz`, `icu/chartevents`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; use decision-time weights (226512, 224639, and pounds item 226531 only after unit confirmation), MAP and respiratory covariates.
- `mimic-iv-3.1/icu/outputevents.csv.gz`, `icu/outputevents`: `subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valueuom`; use dictionary-confirmed Output/Drains items for urine and balance, exclude GU irrigant, require no >6-hour urine/output gap, and retain item/unit ledger.
- `mimic-iv-3.1/hosp/labevents.csv.gz`, `hosp/labevents`: `labevent_id,subject_id,hadm_id,itemid,charttime,storetime,valuenum,valueuom,flag`; use blood creatinine (primary item 50912, dictionary-confirmed; sensitivity to other dictionary-confirmed blood-creatinine items) and potassium, with clinical time/store cutoff.
- `mimic-iv-3.1/hosp/d_labitems.csv.gz`, `hosp/d_labitems`: `itemid,label,fluid,category`; require label/fluid/category confirmation for creatinine and potassium.
- `mimic-iv-3.1/hosp/emar.csv.gz` and `hosp/emar_detail.csv.gz`: join `(subject_id,emar_id,emar_seq)`, retain `parent_field_ordinal`, and report any/detail-joined/positive administration, route missingness, lag and contamination. These sources are not used to define avoidance.
- `mimic-iv-3.1/hosp/procedures_icd.csv.gz` and `hosp/d_icd_procedures.csv.gz`: join `(subject_id,hadm_id)` and `(icd_code,icd_version)`; use dated delivered dialysis codes ICD-9 {3995,5498} and ICD-10 {5A1D00Z,5A1D60Z,5A1D70Z,5A1D80Z,5A1D90Z} for RRT7 sensitivity with chartdate interval bracketing.

Join patients to admissions on `subject_id`; ICU stays to admissions on `(subject_id,hadm_id)`; ICU events on `(subject_id,hadm_id,stay_id)`; dictionaries on `itemid`; hospital procedures on `(subject_id,hadm_id)`; eMAR detail as above. Assert unique admissions/stays, subject agreement, key uniqueness and compatible event/stay times; report violations without repairing them.

Use the parent's unit-safe ledger: positive delivered input amounts in mL (or L×1000), positive mL/hour rates accrued only through the boundary, statuses {FinishedRunning, ChangeDose/Rate, Stopped, Paused, Bolus}, deduplicate only overlapping order/linkorder segments; positive dictionary-confirmed mL output excluding GU irrigant; weight in kg with unit-confirmed pound conversion. Report every actual filter and window in a run manifest.

## Estimands and analysis

The primary estimand is the difference-in-differences of DRR28 risk differences between renal reserve and renal vulnerability within the high-congestion cohort:
`[RD_A-B(DRR28 | high congestion, reserve) - RD_A-B(DRR28 | high congestion, vulnerable)]`.
Also report both stratum-specific RDs and the parent’s overall overlap-population RD. DRR28 is the parent's partially identified conjunctive endpoint: accepted extubation by t0+5d, no later accepted invasive ventilation through t0+7d with continuous linked observation, no recorded index-hospital death or exact hospice/acute discharge by t0+28d, and live index-hospital discharge by day 28 to a non-hospice, non-acute destination. Definite successes are 1, definite failures are 0, and observation gaps/early nonterminal ICU exit are [0,1]. Report sharp lower/upper risks and `DeltaL=pA_L-pB_U`, `DeltaU=pA_U-pB_L`; do not use absent `patients.dod` as survival.

Fit one prespecified overlap model using only decision-available pre-`t0` variables, including the modifier components, demographics, era/admission/service/unit/transfers, prior diagnoses/loops, weight, fluid/urine/creatinine/MAP/pressor/respiratory trajectories, sedation, crystalloid/albumin and missingness. Use common overlap `e0(X0) in [0.10,0.90]` and common tilt `e0(1-e0)`, cross-fitted by subject. Estimate arm-specific pooled-logistic artificial-censoring hazards with lagged decision-available histories, stabilized baseline-only numerators, 1st/99th percentile truncation and >=500 subject bootstraps rerunning folds, overlap, bounds and models. Report crude, overlap-only, overlap-plus-censor and stochastic observed-odds multiplier estimates (0.5/0.75/1/1.33/2), calibration, balance, weight tails and ESS. No flexible subgroup search, post-treatment covariate, future eMAR, discharge destination or outcome may define strata or weights.

The primary supportive gate requires the one-sided 95% lower bound for the interaction RD to exceed +0.05, the reserve-stratum DRR28 lower bound to exceed +0.05, the vulnerable-stratum DRR28 upper bound to be <=0.00, and conservative upper effects for observed RRT7 and recorded death/hospice/acute discharge to remain below +5 and +3 percentage points in both strata. A vulnerable-stratum harm signal instead enters the adverse branch below; a vulnerable-stratum interval that is neither nonpositive nor clearly harmful is inconclusive. Because the subgroup is observational and partially identified, even a supportive branch is a design result, not a treatment recommendation.

Secondary outcomes are parent ANHATD28, recorded live discharge with in-hospital death competing, ALDL7, RTHD28, true day-28 mortality bounds, observed RRT7, dose/latency and eMAR contamination, and all outcomes stratified by the fixed modifier. RRT7 includes exact ICU procedure IDs {225441,225802,225803,225805,225809,225955} in (t0,t0+7d] and dated hospital dialysis codes above; death/discharge is not renal safety.

## Falsification and interpretation

Supportive means the prespecified interaction and reserve-stratum benefit gates pass, both stratum ESS >=75, each stratum has >=100 compatible decisions and >=50 qualifying A deliveries and B completions, overlap/weight/calibration/balance and endpoint-bound arithmetic pass, no adverse observed-terminal or RRT7 gate fails, the result is stable to Paused, treatment-first ties, 6/12-hour grace, alternative blood-creatinine item, lower-congestion stratum and contemporaneous-store sensitivities, and there is no material differential eMAR contamination, late exposure confirmation or source/key contradiction. This supports only a hypothesis-generating renal-reserve selection signal for a recorded strategy.

Adverse means the vulnerable stratum has a lower-bound excess recorded death/hospice/acute-discharge effect >=+3 percentage points, lower-bound excess observed RRT7 >=+5 points, or DRR28 upper bound <=-5 points; or the interaction is reversed with the predeclared adverse margin. These are recorded harms, not proof of loop toxicity.

Margin-falsified means the interaction upper one-sided limit is <=+5 points, or the reserve-stratum DRR28 upper limit is <=+5 points. This rejects the clinically meaningful heterogeneity/benefit margin, not all possible effect modification.

Inconclusive includes wide DRR28 bounds, modifier missingness preventing classification, any stratum below feasibility thresholds, ESS <75, poor positivity, >25% E-first closures, >1% ambiguity/contradiction, >5% B eMAR contamination, >1% late confirmation, material sensitivity reversal, failed negative controls, or unreconciled clone/bound arithmetic. A narrow null interaction is scientifically informative against this selection rule; it must not be labeled “no treatment effect” outside the tested population and recorded strategy.

Required negative controls are a pre-`t0` outcome-free trajectory/time placebo, a falsification exposure window before `t0`, and tests that the renal modifier does not predict impossible pre-baseline outcomes after adjustment. No result may be promoted if these show material residual time or measurement bias.

## What the computation cannot establish

The verifier can check archive/catalog hashes, headers and dictionary links; namespaced partition; first-opportunity and repeated-opportunity audits; source-symmetric exposure; balance/weight/renal modifier construction; unit, clock, transition, competing-closure, overlap, ESS, bootstrap, bound and branch arithmetic; and whether conclusions match computed outputs.

It cannot establish route-complete treatment or true non-use, bedside congestion, readiness, intent, true renal reserve, unrecorded urine, complete eMAR capture, functional recovery, post-discharge survival, exchangeability, causal benefit/harm, safety, transportability or a treatment recommendation. Those require clinical chart adjudication, validated medication and respiratory-state capture, external/post-discharge linkage, expert review and preferably a randomized or prospective strategy trial. No conclusion may call DRR28 functional recovery or an observational subgroup contrast causal.

## Required outputs

Emit the partition proof; first-opportunity and later-only audits; sequential attrition; ventilation masked/strict-store audit; balance/urine/weight/creatinine item-unit and missingness ledger; modifier-stratum counts and overlap; eMAR/detail coverage; loop latency/ambiguity; T/E/clone/hour states; calibration/balance/weights/ESS; stratum and interaction DRR28 bounds with >=500 bootstraps; secondary outcomes and date brackets; negative-control and sensitivity grids; and a final supportive, adverse, margin-falsified, inconclusive or infeasible branch with every claim linked to computed output.
