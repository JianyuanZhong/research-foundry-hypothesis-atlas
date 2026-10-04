# Separate strategy performance, endpoint measurement, and implementation in an all-randomized vasopressor validation trial

## Decision question and targeted repair

The future clinical decision remains whether a norepinephrine-first (NE-first) versus vasopressin-first (VP-first) discontinuation strategy can be compared using a locked EHR endpoint without clinically important distortion of the randomized risk difference (RD). The selected parent correctly retained every randomized patient, but its single binary “strategy-failure” label combined three different phenomena:

1. whether the assigned strategy was implemented, crossed over, or pre-empted by death/ICU exit;
2. whether a successfully stopped drug required intent-qualified pump rescue; and
3. whether the EHR measured those facts correctly.

A high event rate caused by poor implementation is not measurement error, and good EHR recognition of nonimplementation cannot validate measurement of rescue. Conversely, a clinically unfavorable strategy can still have a validly measured endpoint. This successor therefore preserves randomization but separates three estimand layers:

* **all-randomized strategy-level outcome:** the reference and EHR versions of the same clinical composite, both defined for every randomized first patient;
* **all-randomized measurement validation:** paired reference-versus-EHR discordance, with every patient carried through immutable implementation and post-cessation disposition states; and
* **implementation/adherence diagnostics:** actual execution under assignment, explicitly interpreted as strategy performance rather than endpoint accuracy.

The narrower, falsifiable confirmatory claim is:

> In a new, fully verified randomized cohort using the locked endpoint and configurations, the simultaneous 95% upper confidence bound on absolute EHR-versus-reference distortion of the all-randomized VP-first minus NE-first strategy-failure RD is strictly below 0.025.

Unlike the parent’s sensitivity/specificity extrapolation over a hypothetical prevalence region, the primary analysis estimates distortion directly from paired all-randomized false-positive and false-negative probabilities. This removes neither patients nor implementation outcomes. It removes the unnecessary division by outcome prevalence and reduces the conservative fixed confirmation target from 12,532 to **5,920 randomized first patients (2,960 per arm)** under the same strict 0.025 distortion gate and an explicitly narrower planning alternative. A separate 1,200-patient randomized pilot prevents a large launch when accrual, implementation, adjudication, linkage, or error rates are unacceptable. Pilot patients never enter confirmatory accuracy calculations.

The strongest existing evidence remains negative and retrospective: MIMIC establishes computability, sparsity, restart dominance, and transaction-rule instability, but not pump delivery, intent, randomized effects, reliable MCS absence, or prospective interface validity. The experiment tests endpoint measurement, not which strategy is beneficial. A supportive result cannot establish efficacy, safety, equipoise, noninferiority, or clinical acceptability of treating implementation deviations, death, or alive ICU exit as specified below.

## Frozen MIMIC evidence and evidence boundary

All inherited findings are frozen. Among 6,040 MAP-eligible MIMIC landmarks, observed actions were 211 NE-first (3.49%) and 167 VP-first (2.76%), both below the prespecified 5% positivity gate; the 5,638 no-action landmarks are not controls. The observed-stop cohort contains 84 NE-first and 53 VP-first episodes, with 49 and 24 determinate failures. The arms are neither randomized nor exchangeable. Among 73 failures in 136 determinate episodes, 59 include a charted stopped-agent restart and 36 are restart-only. MCS status is unknown in all 137 episodes. Compact temporal models had negligible Brier improvement (about 0.000174 for M1 over M0 and 0.000111 for M2 over M1, both below 0.01) and adverse later transport; no model or subgroup advances.

The complete audit used all 137 inherited episodes and every input row retained after declared stay/item/time filters. It reproduced all boundaries and 59 raw restarts. Five symmetric transaction reconstructions invalidated 0, 1, 13, 16, or 23 stop indices. The inherited chain-plus-dose rule invalidated 13/137 stop indices and 13/59 restart indices (10 NE-first, 3 VP-first), all at `Paused` boundaries. These are reconstruction-instability findings, not evidence of false pump delivery or clinical rescue. No source rows are resampled in this successor.

MIMIC cannot supply randomization, protocol intent, physical pump delivery, a cross-system clock map, adjudicated rescue intent, or reliable negative MCS status. It therefore cannot compute the prospective reference endpoint and cannot answer the confirmatory hypothesis. Its role is to freeze adverse feasibility evidence and bind the EHR-side reconstruction.

## Population, trial clock, and randomization

The prospective program includes at least 12 hospitals, at least two adult ICUs per hospital where available, and at least two pump–EHR interface families. Contracted expansion to as many as 24 hospitals is permitted before confirmation, but adding a site or changing a configuration after confirmatory first-patient enrollment creates a separately versioned configuration and cannot silently pool incompatible records. A configuration is the tuple of site, ICU, pump vendor/model/software major version, integration engine, EHR medication module/build, drug-library version, and clock-map method/version.

Each configuration first completes a 50-episode technical run-in. At least 95% must have unique patient–pump–channel–drug linkage, complete pump export from two hours before candidate assignment through endpoint closure, and an escrowed clock map; at least 90% must have contemporaneous material suitable for blinded intent adjudication. One repeat run-in using 50 wholly new episodes is allowed after repair. A second failure excludes that configuration from pilot and confirmation. Run-in episodes are not randomized and are excluded from all trial estimands.

Eligibility is locked before assignment and cannot depend on later implementation, actual first-stopped drug, capture, rescue, adherence, or outcome:

1. age at least 18, alive in an adult ICU;
2. linked pump-delivered NE and VP concurrently for at least six continuous hours;
3. at the start of the final 30 minutes before randomization, NE greater than 0 and no more than 0.20 mcg/kg/min and VP greater than 0 and no more than 0.04 U/min, with neither increased during those 30 minutes;
4. no pump-delivered epinephrine, phenylephrine, or dopamine in the preceding two hours;
5. at least three valid MAPs spanning at least three of four preceding 30-minute bins, including the final bin; median MAP at least 65 and minimum at least 55 mmHg; and
6. before assignment, the treating team documents that either protocolized first-stop strategy is clinically permissible.

The first eligible randomization per person is the only primary unit. `tr` is immutable randomization time. Assignment is 1:1 in configuration-stratified permuted blocks: `Z=0` NE-first, `Z=1` VP-first. Actual first-stopped drug `A` is post-randomization and never replaces `Z` in a primary table.

The assigned drug should be stopped within 120 minutes. A reference qualifying cessation `t0_R` is the first pump-native delivered-rate timestamp in `[tr,tr+120 min]` at which the assigned drug falls below 0.005 mcg/kg/min for NE or 0.005 U/min for VP and remains below threshold continuously for five minutes while the comparator remains above its threshold. Programmed rate without linked delivery is insufficient. A nonassigned-drug cessation first is crossover. Both crossings within five minutes are simultaneous. A later assigned cessation does not erase crossover or simultaneous implementation failure.

The post-cessation horizon is `(t0_R,min[t0_R+6 h,death,ICU exit]]`. Before cessation, implementation is observed through `min[tr+120 min,death,ICU exit]`. Each source has a prospectively escrowed affine clock map recording offset, drift, time zone, daylight-saving rule, fitting rows, residuals, and version. The ambiguity band is the run-in 99th percentile absolute residual, capped at 60 seconds; a configuration requiring a wider band fails qualification. Events whose mapped uncertainty crosses an ordering or endpoint boundary are indeterminate, never rounded toward agreement.

## Immutable state system for every randomized patient

A binary composite alone is insufficient. Every randomized patient receives one reference implementation state `I_R`, one EHR implementation state `I_E`, one reference post-cessation state `O_R`, and one EHR post-cessation state `O_E`. These variables are never overwritten. Structural non-applicability is an explicit value, not missingness.

### Implementation state at 120 minutes

`I_R` and `I_E` each take exactly one value:

* `AQ`: assigned-drug qualifying cessation by 120 minutes;
* `XO`: nonassigned drug qualifies first while assigned drug remains on;
* `SIM`: both drugs qualify within five minutes;
* `NI_OVERRIDE`: documented clinician override/aborted protocol without qualifying cessation;
* `NI_NO_STOP`: no qualifying cessation and no documented override while alive and still in ICU at 120 minutes;
* `EXIT_PRE`: alive ICU exit before qualifying cessation;
* `DEATH_PRE`: death before qualifying cessation or before the implementation boundary;
* `IND_I`: linkage, export, clock, boundary, or other capture uncertainty can change the state.

Reference states use linked delivered pump rates, trial implementation records, vital status, and the mapped clock. EHR states use only the locked EHR intervals, EHR-visible assignment/override records, and EHR death/ICU feeds. `NI_OVERRIDE` is distinguishable from `NI_NO_STOP` only if the corresponding source contains a prospectively required, timestamped reason code; otherwise it is `NI_NO_STOP` or `IND_I` according to completeness, never inferred from free text after outcome review.

### Post-cessation state

For every patient with `I= AQ` in the corresponding source, `O_R` or `O_E` takes exactly one value:

* `RESCUE`: assigned drug returns to threshold for at least five continuous minutes before closure; for `O_R`, two blinded adjudicators must classify the resumption as deliberately treating or seeking to prevent worsening hypotension/impaired perfusion;
* `DEATH_POST`: death before six-hour closure and before any earlier adjudicated rescue;
* `NO_EVENT_6H`: six complete hours with no rescue or death;
* `EXIT_POST_OFF`: alive ICU exit before six hours, complete capture through exit, and assigned drug still off;
* `IND_O`: linkage, export, clock, intent, vital-status, or boundary uncertainty can change the state.

For all patients whose corresponding implementation state is not `AQ`, the post-cessation state is exactly `SNA` (structurally not at risk under this endpoint). `SNA` is analytically retained. It is neither success nor missingness. If rescue precedes death, both source events are retained, `O=RESCUE` is the first endpoint state, and death is a mandatory subsequent-event field. If death precedes rescue, `O=DEATH_POST`. This temporal rule avoids the parent’s priority label masking one event with another.

### All-randomized strategy-level composite

The panel-ratified reference endpoint is

`Y_R=1` for `I_R in {XO,SIM,NI_OVERRIDE,NI_NO_STOP,EXIT_PRE,DEATH_PRE}` or `I_R=AQ` with `O_R in {RESCUE,DEATH_POST}`.

`Y_R=0` for `I_R=AQ` with `O_R in {NO_EVENT_6H,EXIT_POST_OFF}`.

`Y_R=?` if `I_R=IND_I` or `I_R=AQ,O_R=IND_O`.

`Y_E` is the identical mapping from `(I_E,O_E)`. Alive ICU exit after successful cessation remains a competing success only for this ratified six-hour-or-ICU-exit endpoint; alive exit before implementation remains strategy nonimplementation. A future trial seeking six clock hours regardless of location needs post-ICU medication truth and new validation.

For each arm, `p_z=P(Y_R=1|Z=z)` and `q_z=P(Y_E=1|Z=z)`. The **strategy-level clinical estimand** is `Delta_R=p_1-p_0`. It contains implementation, competing events, death, and rescue by design. It is reported with an exact/randomization-compatible confidence interval but the validation program is not powered or authorized to conclude benefit or noninferiority. `Delta_E=q_1-q_0` is the same strategy estimand measured by the EHR endpoint.

## Primary measurement estimand: direct paired RD distortion

For determinate paired labels in arm `z`, define all-randomized joint error probabilities

* `f_z=P(Y_E=1,Y_R=0|Z=z)` (false-positive probability per randomized patient), and
* `g_z=P(Y_E=0,Y_R=1|Z=z)` (false-negative probability per randomized patient).

These are not one minus specificity and one minus sensitivity; their denominator is every randomized patient. The arm-level endpoint-rate bias is exactly

`d_z=q_z-p_z=f_z-g_z`,

and randomized RD distortion is exactly

`b=(Delta_E-Delta_R)=d_1-d_0=f_1-g_1-f_0+g_0`.

This identity is the key repair. The incidence of nonimplementation, crossover, death, exit, and rescue contributes to `Delta_R`, but only EHR/reference discordance contributes to `b`. Thus poor adherence cannot masquerade as measurement error, and accurate recognition of abundant nonimplementation cannot conceal rescue errors because component tables remain mandatory.

Construct two-sided Clopper–Pearson intervals for each of `f_0,g_0,f_1,g_1`, each with `alpha=0.0125`. By Bonferroni, the four-interval Cartesian product has simultaneous coverage at least 95%. Since `b` is linear, its exact conservative confidence limits are

`b_L=L(f_1)-U(g_1)-U(f_0)+L(g_0)` and

`b_U=U(f_1)-L(g_1)-L(f_0)+U(g_0)`.

Let `B_U=max(|b_L|,|b_U|)`. The primary gate is strict: `B_U<0.025`; equality fails. This is an observed randomized-cohort measurement guarantee and does not extrapolate over the parent’s hypothetical prevalence/effect region `Omega`. That narrower scope is deliberate. Transport to a later trial requires the same endpoint, population, implementation protocol, clock rules, and a configuration mixture satisfying the prespecified transport gates. Conditional sensitivity/specificity and the parent’s `Omega` analysis remain secondary stress tests only and cannot rescue a direct-distortion failure.

### Indeterminate pairs and exact partial identification

Every patient enters an arm-specific 3 by 3 table with `Y_E,Y_R in {0,1,?}`. Unknown labels are allocated jointly over aggregate counts, never metric by metric and never by person-level `2^m` enumeration. For each feasible completion, compute `f_z=FP_z/N_z` and `g_z=FN_z/N_z`, the four exact intervals, and `B_U`; the primary result is the largest `B_U` over all joint completions. The parent’s aggregate 3 by 3 bounded-knapsack/branch-and-bound engine and its small-table oracle are retained, but the objective is now the linear all-denominator discordance expression above. A timeout is inconclusive.

Because unknown rows can be adversarial, no separate 5% rule can make a failing bound pass. Indeterminacy above 2% overall, above 3% in an arm-by-configuration cell with at least 50 patients, or differing by more than 2 percentage points between arms is additionally operationally adverse even if the exact completion bound happens to pass. Missing EHR negatives or treating loss of capture as no event invalidates computation.

## Component measurement validation and implementation diagnostics

The binary bound is primary, but it cannot stand alone.

### Measurement components, defined for all randomized patients

Report complete `I_E x I_R` and `(I_E,O_E) x (I_R,O_R)` tables by `Z` and configuration. Patients without reference `AQ` retain `O_R=SNA`; they are not dropped. Prespecified component metrics are:

1. exact multinomial agreement and one-versus-rest sensitivity/false-positive probability for each implementation state;
2. among the immutable reference state `I_R=AQ`, rescue-state sensitivity and false-positive probability, explicitly labeled a post-randomization component diagnostic rather than ITT;
3. death and ICU-exit timestamp/state agreement over every randomized patient;
4. rescue timing error and one-to-one pump/EHR event matching among applicable episodes; and
5. the contribution of each state-pair cell to `f_z`, `g_z`, `d_z`, and `b`.

A global `B_U` pass with cancellation between implementation and rescue is adverse if any common component (at least 100 reference events per arm) has sensitivity below 0.80, if any state contributes an absolute arm-differential error above 0.010, or if removing one component changes the sign of estimated `b` and that component has more than 20 discordances. These safeguards prevent abundant, easily recognized nonimplementation from obscuring poor rescue measurement.

### Implementation/adherence diagnostics, not measurement accuracy

Using reference states only, report by assignment: `AQ`, crossover, simultaneous cessation, override, no stop, pre-implementation death/exit, time to first attempt, actual first-stopped drug, protocol deviation reason, rescue, post-cessation death/exit, and six-hour success. Report the all-randomized assigned-strategy implementation RD and component RDs with confidence intervals. These describe delivery of the strategy and competing outcomes. They do not enter an accuracy denominator, do not redefine `Z`, and cannot be described as EHR measurement failure unless `I_E/O_E` disagrees with `I_R/O_R`.

A reference assigned-cessation rate below 60% in either arm, crossover/simultaneous rate above 15%, arm difference in assigned cessation above 10 percentage points, or safety-board concern is adverse for executing or interpreting the strategy but does not by itself falsify measurement validity. Conversely, excellent adherence cannot rescue `B_U>=0.025`.

## Staged feasibility and immutable confirmation

### Stage 1: independent randomized pilot

After technical run-in, enroll **1,200 consecutive first randomized patients, 600 per assignment arm**, over at most 12 months. All are fully pump-linked and adjudicated under the final state definitions. Pilot patients are excluded from confirmatory accuracy, treatment, and transport estimands. The pilot may end the program but cannot generate a validation claim.

Before unblinding pilot error tables, sites must show:

* at least 100 randomized patients/month over the final three pilot months across contracted confirmation sites, with a one-sided 95% Poisson lower bound of at least 85/month;
* at least 12 active hospitals and two interface families, no hospital contributing above 15%;
* at least 98% complete linkage/export/clock/vital-status records in each arm;
* at least 95% determinate reference and EHR state pairs in each arm;
* adjudicator raw agreement at least 85% and at least one of Gwet AC1 or kappa at least 0.70; and
* no safety/equipoise stop by the independent board.

After operational review is frozen, an independent pilot statistician releases the paired error tables. Confirmation does not launch if the conservative pilot aggregate-completion `B_U` is at least 0.060, if any arm has a one-sided 95% upper bound above 0.025 for either all-denominator false-positive or false-negative probability, if component cancellation is adverse, or if strategy implementation makes the endpoint clinically uninterpretable. These are futility/safety rules, not validation. Selection on the independent pilot cannot make a new confirmatory confidence set anti-conservative because no pilot patient is reused; nevertheless the final claim is explicitly conditional on the locked confirmation configurations and is not a combined pilot-plus-confirmation claim.

The blinded pilot statistician may recommend only “stop” or “proceed unchanged.” Pilot results cannot change `N`, the 0.025 gate, endpoint definitions, thresholds, time windows, analysis, or configuration pooling. Any such change requires a new protocol and new run-in/pilot.

### Stage 2: fixed confirmation

Confirmation enrolls exactly **5,920 new first randomized patients, 2,960 per arm**, with one common start and database lock, or closes unsuccessfully at 48 months. There is no denominator-, event-, adherence-, component-, arm-, or accuracy-dependent stopping, no sample-size re-estimation, and no post-lock extension. Failure to complete is inconclusive.

The executed no-simulation design calculation fixes a planning alternative of all-denominator false-positive and false-negative probability 0.005 in each arm. For candidate arm size `n`, exact binomial lower/upper count envelopes use tail 0.0125 for each of the four error probabilities. Two count-tail events per error probability give eight events and a Bonferroni assurance lower bound of 0.90. The count endpoints are converted to the same two-sided Clopper–Pearson intervals used at analysis, and the linear worst-case bound for `b` is evaluated. The smallest integer with strict `B_U<0.025` is `n=2,960`: its error-count envelope is 7–24 per type, and the worst confidence envelope is `[-0.0249929186,0.0249929186]`. At `n=2,959`, the bound is 0.0250013417 and fails. The planning alternative is not an acceptance threshold or a promise of feasibility.

At 5,920 patients over 48 months, confirmation needs 123.3 patients/month. The pilot launch criterion of a lower accrual bound of 85/month alone is not sufficient; before confirmation, signed site contracts must project at least 130/month and the final three observed months must average at least 100/month. The discrepancy is explicit: even a scientifically promising pilot is operationally inconclusive if contracted expansion cannot make the fixed target plausible. This replaces the parent’s untested 12,532-patient launch with a falsifiable stage gate while preserving an outcome-independent confirmatory lock.

## EHR reconstruction and reference adjudication

The EHR algorithm is frozen before pilot enrollment. For NE, local mappings to MIMIC item 221906 retain mcg/kg/min or divide mcg/min by a contemporaneous valid weight of 30–300 kg; rates above 5 mcg/kg/min are rejected. For VP, mappings to item 222315 retain U/min or divide U/hour by 60; rates above 0.2 U/min are rejected. Positive intervals require `endtime>starttime`. Primary intervals cannot be repaired with `statusdescription`, transaction chain, `storetime`, caregiver, open-bag, transfer, programmed-rate, or order fields. Those remain diagnostics.

Two independent critical-care/pharmacy adjudicators review pump/monitor traces, workflow events, cointerventions, and timestamped intent evidence, but not `Y_E`, EHR/reference error tables, assignment-specific accuracy, or each other’s labels. A third blinded adjudicator resolves disagreement. Technical/procedural pause, bag/syringe replacement, channel exchange, transfer continuation, mistaken-stop correction, reconciliation, and documentation fragmentation without interrupted delivery are not rescue. If intent cannot be determined, `O_R=IND_O`.

Secondary event matching is one-to-one maximum-cardinality/minimum-total-absolute-lag matching within person, episode, drug, and window at locked ±10 minutes, with ties resolved by earlier pump time, earlier mapped EHR time, then immutable row ID. Matching cannot alter the immutable states or primary labels.

## Prospective data contract

All files are immutable and row-hashed; text remains private and is never used in public searches.

* `configuration.csv`: `site_id,icu_id,configuration_id,family_id,pump_vendor,pump_model,pump_software_major,integration_engine,ehr_module_build,drug_library_version,clock_map_version,valid_from,valid_to`.
* `screening.csv`: `person_id,encounter_id,icu_stay_id,candidate_id,screen_time,screen_order,age,adult_icu,dual_drug_start,ne_rate,vp_rate,rate_units,weight,weight_time,other_pressor_2h,map_bin_count,map_median,map_min,clinical_permissibility_time,eligible,exclusion_reason,configuration_id`.
* `randomization.csv`: `person_id,trial_patient_id,randomization_id,Z,assigned_stop_drug,randomization_time,block_id,configuration_id,eligibility_lock_hash,phase,first_patient_flag`.
* `strategy_order.csv`: `person_id,randomization_id,order_time,assignment_ack_time,planned_stop_drug,implementation_deadline,override_time,override_reason_code,protocol_attempt_time,protocol_deviation_code,clinician_id_hash`.
* `pump_rate.csv`: `person_id,randomization_id,pump_id,channel_id,drug_library_id,drug,concentration,weight,weight_time,source_time,delivered_rate,programmed_rate,rate_unit,linkage_status,export_gap,immutable_row_id`.
* `pump_event.csv`: `person_id,randomization_id,source_time,event_type,pump_id,channel_id,drug,bag_syringe_id,alarm_code,workflow_code,immutable_row_id`.
* `monitor_map.csv`: `person_id,randomization_id,source_time,map_value,map_source,quality_flag,immutable_row_id`.
* `ehr_interval.csv`: `person_id,randomization_id,drug,starttime,endtime,storetime,rate,rateuom,patientweight,statusdescription,orderid,linkorderid,caregiver_id,isopenbag,continueinnextdept,immutable_row_id`.
* `clock_map.csv`: `configuration_id,source_system,clock_map_version,fit_start,fit_end,offset,drift,time_zone,dst_rule,residual_p99,residual_distribution_hash`.
* `intent_evidence.csv`: `person_id,randomization_id,evidence_time,evidence_source,evidence_text_or_code,source_row_id`; protected text is not released.
* `adjudication.csv`: `person_id,randomization_id,adjudicator_id,round,rescue_intent_label,reason_code,label_time,third_resolution`.
* `boundary.csv`: `person_id,randomization_id,icu_exit_time,death_time,capture_complete_to,mcs_device_type,mcs_state,mcs_support_setting,mcs_source_time`.
* `state.csv`: exactly one row per randomized primary unit with `person_id,randomization_id,Z,I_R,I_E,O_R,O_E,Y_R,Y_E,t0_R,t0_E,first_endpoint_time_R,first_endpoint_time_E,subsequent_death,actual_first_stopped_drug,adherent,indeterminate_reason,closure_reason,phase,configuration_id,row_hash`.
* Derived locked outputs: `state_transition_tables.csv`, `analysis_3x3.csv`, `joint_completion_witness.csv`, `direct_error_intervals.csv`, `distortion_witness.csv`, `implementation_diagnostics.csv`, `component_error_contributions.csv`, `transport_leaveout.csv`, and `sample_size_lock.json`.

Invariants are: one primary row per person; every randomized row has one `I_R,I_E,O_R,O_E`; `O=SNA` iff the corresponding `I` is not `AQ`; every EHR-positive, negative, and indeterminate patient receives reference verification; pilot and confirmation identifiers do not overlap; and no row is deleted after randomization.

## Current MIMIC bindings

The read-only source is `[internal dataset path]`, [source checksum]; configured snapshot `[source checksum]`.

* `mimic-iv-3.1/icu/inputevents.csv.gz`, table `icu/inputevents`; schema `[internal dataset path]`, schema [source checksum]. Join `subject_id,hadm_id,stay_id`; times `starttime,endtime,storetime`; required columns `caregiver_id,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,patientweight,totalamount,totalamountuom,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate`. NE item 221906; VP item 222315.
* `mimic-iv-3.1/icu/chartevents.csv.gz`, table `icu/chartevents`; schema `[internal dataset path]`, schema [source checksum]. Join by `stay_id` with `subject_id,hadm_id` consistency; times `charttime,storetime`; columns `caregiver_id,itemid,value,valuenum,valueuom,warning`. MAP items 220052 arterial and 220181 non-invasive; retain 20–200 mmHg, reject warning, prefer arterial at identical time.
* Positive-only MCS audit: `mimic-iv-3.1/icu/d_items.csv.gz`, table `icu/d_items`, schema `[internal dataset path]`, columns `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue`; `mimic-iv-3.1/icu/datetimeevents.csv.gz`, table `icu/datetimeevents`, schema `[internal dataset path]`, keys `subject_id,hadm_id,stay_id`, times `charttime,storetime`, columns `caregiver_id,itemid,value,valueuom,warning`; and `mimic-iv-3.1/icu/procedureevents.csv.gz`, table `icu/procedureevents`, schema `[internal dataset path]`, keys `subject_id,hadm_id,stay_id`, times `starttime,endtime,storetime`, columns `caregiver_id,itemid,value,valueuom,location,locationcategory,orderid,linkorderid,ordercategoryname,ordercategorydescription,patientweight,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate`. A non-positive MCS audit remains unknown, not absent.
* ICU boundaries: `mimic-iv-3.1/icu/icustays.csv.gz`, table `icu/icustays`; schema `[internal dataset path]`, schema [source checksum]; keys `subject_id,hadm_id,stay_id`; fields/times `first_careunit,last_careunit,intime,outtime,los`.
* Death/hospital boundaries: `mimic-iv-3.1/hosp/admissions.csv.gz`, table `hosp/admissions`; schema `[internal dataset path]`, schema [source checksum]; keys `subject_id,hadm_id`; fields/times `admittime,dischtime,deathtime,hospital_expire_flag`.
* Age: `mimic-iv-3.1/hosp/patients.csv.gz`, table `hosp/patients`; schema `[internal dataset path]`, schema [source checksum]; key `subject_id`; fields `gender,anchor_age,anchor_year,anchor_year_group,dod`.

The frozen source audit remains at `[internal dataset path]` (source-audit hash `[source checksum]`, cohort hash `[source checksum]`); executable cache `[internal dataset path]`.

## Recurrence and configuration transport

Later eligible episodes are captured under identical rules but cannot enlarge the primary denominator. A recurrent opportunity requires a new six-hour dual-drug baseline and begins at least 24 hours after the preceding `t0` or randomization when no `t0` exists. It retains the original assignment unless a separately approved re-randomization occurs before a new eligibility lock. Recurrent state tables, direct distortion, and implementation diagnostics use patient-cluster bootstrap stratified by assignment/configuration and diagnostic marginal GEE. They cannot rescue a first-patient failure.

No hospital, configuration, or family may provide more than 20% of either arm. At least eight hospitals and both interface families must each contribute at least 100 patients per arm. Report exact site/configuration/family state tables, hierarchical multinomial summaries, prediction intervals, and leave-one-hospital/family-out direct aggregate-completion bounds. Every leave-out mixture must retain `B_U<0.025`. A configuration with at least 500 patients per arm must have `B_U<0.05`; sparse configurations are inconclusive. A material assignment-by-configuration interaction or adjusted state-error range above 0.10 is adverse. Support applies only to enumerated locked configurations.

## Verifier requirements and adversarial cases

The verifier must reproduce pre-randomization eligibility, one primary unit per person, block balance, retention under `Z`, immutable implementation and outcome states, structural `SNA`, independent reference/EHR clocks, complete positive/negative verification, 3 by 3 counts, exact joint completions, four Clopper–Pearson intervals, direct bias limits, component contributions, pilot exclusion, the 2,960 adjacent-integer design result, common confirmation lock, recurrence separation, and transport gates.

Required adversarial cases include:

1. identical EHR/reference measurement within each state but high nonimplementation or death: measurement can pass while strategy performance is adverse; do not call implementation a measurement failure;
2. excellent implementation but arm-differential EHR discordance giving `B_U>=0.025`: endpoint validation fails;
3. pooled composite agreement passes because implementation false positives cancel rescue false negatives: component cancellation gate fails;
4. selecting only reference `AQ` patients produces favorable rescue accuracy: retain it only as a component diagnostic, never the all-randomized primary;
5. crossover followed by assigned cessation: `I=XO` remains immutable;
6. simultaneous cessation reconstructed as a single-drug stop: count the state and binary discordance;
7. rescue followed by death and death followed by rescue: apply first-endpoint timing while retaining subsequent death;
8. alive exit before versus after `t0`, exact 120-minute/five-minute/six-hour boundaries, spanning intervals, duplicate rows, and mapped-clock ambiguity;
9. separate best-case imputations for each metric pass but one joint aggregate completion fails: report the joint failure and witness;
10. pilot rows reused, `N` changed after error review, arm-specific closeout, denominator-triggered extension, or confirmation stopped on accuracy: invalidate the confirmatory claim;
11. high sensitivity/specificity over a selected reference status but direct all-randomized distortion fails: fail;
12. pilot futility stop or accrual failure described as endpoint invalidity: correct conclusion is adverse pilot evidence or operationally inconclusive, not confirmation;
13. correct adverse/inconclusive results described as validation, treatment benefit, safety, or noninferiority: reject the conclusion.

A computational verifier can establish row accounting, state assignments under frozen inputs, exact bounds, design arithmetic, and whether conclusions follow from outputs. It cannot ratify the composite, infer intent without clinical adjudication, prove physical delivery from linkage alone, establish MCS absence, approve randomization, judge safety/equipoise, or establish causal treatment benefit.

## Supportive, adverse, and inconclusive interpretation

**Supportive:** all 5,920 new confirmation patients complete; worst-case joint completion gives `B_U<0.025`; state/component cancellation, indeterminacy, adjudication, clock, recurrence, concentration, and every leave-out gate pass. This supports only that the locked EHR composite measures the reference all-randomized RD with less than 0.025 worst-case distortion in the enrolled configuration mixture. For a later trial using the identical estimand and measurement system, an EHR confidence bound must still be widened by the validated distortion bound. Validation alone does not establish noninferiority.

**Adverse:** completed confirmation has `B_U>=0.025`, clinically important arm-differential state error, cancellation hiding poor rescue measurement, or harmful configuration heterogeneity. This falsifies the narrow validation claim even if implementation was excellent or the EHR treatment contrast was favorable. Separately, poor implementation, crossover, competing deaths/exits, or safety findings are adverse for the strategy design, not evidence of measurement failure unless paired labels disagree.

**Inconclusive:** governance does not ratify the composite/margin; randomization is impermissible; pilot accrual or contracted expansion cannot support 5,920 within 48 months; technical, linkage, clock, adjudication, determinacy, or exact-computation requirements fail; the fixed sample does not complete; or a later trial changes the population, strategy, endpoint, handling of death/exit, clock, configuration mixture, or estimand. Inconclusive never supports validity, safety, benefit, or noninferiority.

The substantive advance is a cleaner clinical interpretation and a smaller but still demanding experiment: strategy implementation and competing events remain in the all-randomized clinical estimand, yet only paired EHR/reference discordance is called measurement error. Immutable state variables preserve every randomized patient and expose where errors arise. The direct paired identity retains an exact 0.025 RD-distortion guarantee without outcome-dependent confirmation, while the independent pilot makes operational infeasibility and an unpromising endpoint discoverable before committing to the 5,920-patient confirmatory cohort.
