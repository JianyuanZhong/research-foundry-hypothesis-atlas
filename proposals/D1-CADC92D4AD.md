# All-randomized validation with a three-state strategy-failure estimand

## Decision and substantive repair

This is a targeted child of `[prior hypothesis]`. The future clinical decision is whether a locked EHR endpoint can be used in a later randomized comparison of a norepinephrine-first (NE-first) versus vasopressin-first (VP-first) discontinuation strategy without changing the randomized risk difference (RD) enough to alter a clinically consequential noninferiority decision. This validation study does not compare the drugs and cannot estimate treatment benefit.

The parent correctly removed post-randomization selected-adherer analysis from the primary denominator and retained every randomized patient. Its remaining weakness is interpretability: a single binary failure can still make implementation failure (the assigned cessation was never successfully delivered), post-implementation rescue (cessation was delivered but support was subsequently restarted), and label error look like the same clinical event. A high binary failure rate may therefore be a workflow problem rather than a rescue problem; a small EHR/reference discordance does not show that the strategy was implemented well; and a large discordance does not identify whether the implementation or rescue component was mismeasured.

The repair is a **pre-randomization, clinically ratified three-state estimand** reported for every randomized first patient, with an explicitly separate measurement estimand:

* `S0`: assigned strategy successfully implemented and no qualifying rescue during the locked rescue window;
* `S1`: assigned strategy successfully implemented, followed by intent-qualified rescue of the first-stopped agent during that window; and
* `S2`: implementation failure or structural non-applicability before a successful assigned cessation, including nonassigned-first/simultaneous stop, crossover/override, death before implementation, and alive ICU exit before the implementation deadline.

`S2` is not called a rescue, and `S1` is not allowed to absorb implementation failure. Death and ICU exit are retained in the all-randomized strategy outcome, but are reported as mutually exclusive structural subtypes of `S2`, not treated as evidence of pump rescue. If governance rejects treating any subtype as a strategy failure, the protocol must stop as unratified rather than silently recode it.

The confirmatory clinical claim is deliberately narrower than an efficacy claim:

> In a new, fully verified, all-randomized endpoint-validation cohort using the locked population, clocks, and configuration strata, the EHR reconstruction reproduces the reference three-state disposition well enough that its induced binary strategy-failure RD distortion is strictly below 0.025 simultaneously over the prespecified clinically ratified event-rate/effect region, while state-specific implementation and post-implementation rescue discordance are separately bounded and reported.

Here the binary utility endpoint is fixed before data: `Y=1` for `S1` or `S2` (any clinically unfavorable strategy disposition) and `Y=0` for `S0`. This preserves the parent's exact RD-distortion target and sample-size rule. The three-state table explains what that binary result means; it does not replace the locked primary gate or create a new causal estimand.

## What is supported, what is untested, and what MIMIC can do

The strongest supported MIMIC claim is retrospective and noncausal. In 6,040 MAP-eligible repeated landmarks, NE-first and VP-first actions were uncommon (211, 3.49%, and 167, 2.76%, respectively), both below the frozen 5% positivity gate; the 5,638 no-action landmarks are not controls. The observed stopped-drug frame was small and nonexchangeable (84 NE-first and 53 VP-first episodes; 49 and 24 determinate composite failures). Among 136 determinate episodes, 73 failed, 59 included a charted stopped-agent restart, and 36 were restart-only; MCS status was unknown in all 137 episodes. Restart labels were sensitive to reconstruction rules, and prognostic enrichment was negligible/adverse. These findings motivate validation but cannot establish pump delivery, clinician intent, causal strategy performance, or the truth of any MIMIC label.

The untested claim is not that NE-first or VP-first is better. It is whether the locked EHR representation can distinguish `S2` implementation failure from `S1` post-implementation rescue and `S0`, and whether any remaining measurement error can materially distort a future randomized RD. MIMIC has no randomization, reliable pump-native delivery truth, adjudicated intent, dependable MCS absence, or validated cross-clock linkage; no retrospective result may be presented as those facts.

## Prospective population, timing, and immutable labels

Use a new, consecutively enrolled endpoint-validation cohort of eligible ICU patients, randomized 1:1 to a **validation-only assigned strategy** NE-first or VP-first. Randomization is for indexing the measurement target and must not be used to infer efficacy. The eligibility rule, first eligible patient unit, and exclusions are frozen before the operational pilot and before confirmation. Recurrent qualifying episodes are retained only as a prespecified clustered secondary analysis and never replace the first-patient confirmatory unit.

For each randomized patient, escrow the following clocks before unblinding any reference result:

1. `t0`: randomization and first eligible dual-vasopressor landmark;
2. `t_impl`: the first assigned-agent cessation time, or the fixed implementation deadline;
3. `t_rescue_end`: the fixed six-hour window after a successfully verified assigned cessation; and
4. `t_obs_end`: ICU exit, death, or the fixed maximum observation time.

The assigned strategy is implemented only when the pump-native/device-linked feed and the prespecified clinician-intent record jointly show that the assigned first stop occurred in the allowed implementation window, with no simultaneous stop, nonassigned-first stop, or crossover before the locked implementation decision. If implementation is not established, assign `S2` and a subtype (`nonimplementation`, `crossover/override`, `simultaneous`, `death-before-implementation`, `alive-ICU-exit-before-implementation`, or `unresolved`). Do not infer implementation from a medication order, a charted phrase, or a single EHR event.

For implemented patients, reference adjudicators determine whether the stopped agent was actually resumed for hemodynamic support in the six-hour rescue window. The reference requires pump-native delivery evidence plus clinician-intent adjudication and records rescue timing, agent identity, dose/rate continuity, and competing terminal events. Rescue after death or exit is structurally impossible and remains `S2` if implementation had not occurred, not `S1`. A later restart after the window is not a qualifying rescue but is retained in an exploratory timing table.

The EHR algorithm receives only the locked EHR interface fields and applies a fixed deterministic reconstruction. It must produce the same mutually exclusive `S0/S1/S2` state and the same `S2` subtype from the available order, administration, chart, and time data. The EHR state is never edited to agree with the reference. Blinded reference adjudication is completed without access to the EHR state; EHR programmers are blinded to reference labels.

## Estimands that separate the mechanisms

Let `Z` be randomized assignment, `R` the reference state in `{S0,S1,S2}`, and `E` the EHR state. Let `N_z` include every patient assigned to arm `z`, including patients with no cessation, death, ICU exit, crossover, and unresolved records.

The locked primary measurement estimand is the arm-specific binary RD distortion

`B = [(Pr(E in {S1,S2}|Z=1) - Pr(E in {S1,S2}|Z=0)) - (Pr(R in {S1,S2}|Z=1) - Pr(R in {S1,S2}|Z=0))]`.

With `FP_z = count(E in {S1,S2}, R=S0)` and `FN_z = count(E=S0, R in {S1,S2})`, the exact identity is

`B = (FP_1/N_1 - FN_1/N_1) - (FP_0/N_0 - FN_0/N_0)`.

The confirmatory gate remains a simultaneous two-sided 95% upper bound on `|B|` strictly less than 0.025, using the parent's exact randomized-arm risk-difference distortion construction, Bonferroni allocation, and joint aggregate 3x3 indeterminate completion. The 1,200-patient operational pilot is independent, accuracy-blinded, excluded from confirmation, and cannot change the 5,920-patient fixed confirmation, endpoint definitions, region, or gate. The exact assurance rule remains 2,960 per arm (5,920 total), with the adjacent 2,959 total failing the prespecified strict rule under the stated Se/Sp planning conditions; this is planning assurance, not a guarantee of prevalence, determinacy, or feasibility.

The three-state decomposition is co-primary for interpretation but not a second unplanned pass/fail gate. Report, for each arm and jointly:

* `p_impl = Pr(R=S0 or S1 | Z=z)` and `p_implfail = Pr(R=S2 | Z=z)`, with `S2` subtype counts;
* `p_rescue = Pr(R=S1 | Z=z)` among all randomized patients, and the conditional descriptive quantity `Pr(R=S1 | R in {S0,S1}, Z=z)` only as a post-implementation description, never as an ITT effect;
* the full reference and EHR 3x3 state confusion matrix, including state-specific false-positive and false-negative contrasts; and
* arm differences in each state, with exact simultaneous confidence sets and a statement that they describe assigned-strategy performance in this validation cohort, not causal treatment effects.

The all-randomized state vector is clinically interpretable: the reference RD in `S2` answers whether assigned strategies differ in failure to reach an implemented cessation; the reference RD in `S1` answers whether they differ in post-implementation rescue frequency on the all-randomized scale; and the binary RD is their prespecified utility aggregation. The conditional rescue proportion is descriptive because successful implementation is post-randomization. No principal-stratum causal rescue claim is made.

To prevent cancellation from hiding a dangerous component, require a separate descriptive alarm (not a relaxed primary gate): any state-specific arm-by-state discordance contrast whose exact simultaneous 95% interval exceeds 0.05 triggers adverse review and blocks a supportive endpoint-validation interpretation, even if the signed binary `B` happens to cancel. This component alarm is fixed prospectively and is not used to manufacture a favorable result. If governance wants a different clinical tolerance, it must be ratified before lock.

## Missingness, indeterminacy, and inference

Every randomized patient remains in every denominator. A reference or EHR state that cannot be assigned with the required timing is `U` and is not dropped. The primary binary outcome and the three-state table use the exact joint 3x3 aggregate completion optimization inherited from the parent: for each arm, enumerate feasible integer allocations of reference/EHR unknown counts over `{S0,S1,S2}` subject to observed margins and fixed adjudication rules; optimize the affine numerator of `B` over all arms jointly and over the fixed clinically ratified effect/event-rate region. Use person-level enumeration only as a small-table oracle (at most eight unknown labels), never as the production algorithm. The verifier must test that unknowns cannot be reclassified as absent, that row totals equal `N_z`, and that implementation-failure unknowns cannot enter the rescue cell without reference evidence of successful cessation.

Use exact Clopper–Pearson/binomial tail constants and the locked Bonferroni allocation for the arm-specific discordance components. Report the identified set when missingness prevents the strict gate. A narrow interval obtained only because unresolved records were excluded is invalid. The primary gate is adverse if the upper bound reaches 0.025; it is inconclusive if accrual, adjudication reliability, indeterminate completion, or configuration transport prevents the prespecified analysis.

## Verification and transport

The reference protocol requires dual blinded adjudication of implementation, rescue intent, timing, agent identity, and structural death/exit states; adjudication agreement, unresolved fraction, and pump-feed linkage are reported by arm and configuration. A protocol-identical interface/configuration audit is required for every intended deployment. Prespecified gates include representation and concentration, sufficient events in each `S0/S1/S2` cell, no material arm imbalance in indeterminate rates, adjudication agreement, and leave-one-configuration-out distortion. A supportive result applies only to the locked population, interfaces, clocks, and composite; it does not validate another hospital, another clock, a different rescue definition, or a later efficacy endpoint.

Required adversarial verifier cases include: perfect agreement but high `S2` implementation failure; perfect implementation with EHR-only rescue false positives; true `S1` rescue hidden by an order with no pump delivery; death before stop; alive ICU exit before deadline; simultaneous stop; crossover followed by restart; EHR/reference state cancellation in the binary composite; and a favorable binary estimate driven by dropping unresolved patients. The verifier must distinguish computationally checkable identities and confidence envelopes from clinical judgments about whether `S2` should count as failure, whether rescue intent is valid, and whether the endpoint is useful.

## Exact available source bindings and retrospective audit

The retrospective feasibility/audit is read-only and uses the current MIMIC-IV 3.1 snapshot. Source files and hashes are fixed by `[internal dataset path]` and catalog [source checksum].

* `baidu_downloads/eicu_mimic/mimic数据库/mimic-iv-3.1.zip`, archive `mimic-iv-3.1/icu/inputevents.csv.gz`: `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,patientweight,totalamount,totalamountuom,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate`; schema `table-d193e854c19eb4ba.json`, hash `[source checksum]`.
* The corresponding `mimic-iv-3.1/icu/chartevents.csv.gz`, `d_items.csv.gz`, `datetimeevents.csv.gz`, `procedureevents.csv.gz`, and `icustays.csv.gz` members, described respectively by `table-8208609a785ea7e8.json`, `table-d1023acc404fd1d4.json`, `table-b88dd677d1c84a2d.json`, `table-f6493e8403a0abe7.json`, and `table-7d5c8feb0fb0dbd4.json`, provide the locked retrospective item dictionaries, charted observations, event times, procedures, and ICU boundaries. Joins use `stay_id`/`hadm_id`/`subject_id` as available; event times are the table's `starttime`, `endtime`, `charttime`, `storetime`, or `charttime` fields exactly as documented in each JSON, with no invented cross-clock equivalence. The source archive is never modified.
* `mimic-iv-3.1/hosp/admissions.csv.gz` and `patients.csv.gz`, described by `table-e8ec3e6e4c428559.json` and `table-9154f8c46cade9af.json`, supply admission/discharge and deidentified patient linkage; joins are `hadm_id` and `subject_id`, and `admittime`, `dischtime`, `deathtime`, and `dod` are used only for the frozen eligibility and structural-boundary audit.

The MIMIC audit must scan all eligible rows in these members, retain the parent’s exact MAP landmark and medication-item mapping, and output counts for eligibility, action arms, repeated landmarks, first stops, restarts, clock ambiguity, MCS unknownness, and implementation/rescue subtypes only as **observational transaction diagnostics**. It cannot label any row as pump-delivered truth or clinician intent. The prospective validation additionally requires data absent from MIMIC: device/pump-native delivery linkage, clinician intent adjudication, synchronized clocks, reliable MCS state, and governance ratification of the three-state clinical utility.

## Interpretation and falsification

Supportive results require all of the following: the strict simultaneous upper bound for `|B|` is below 0.025; component discordance alarms do not trigger; the full state matrix and indeterminate envelope are reported; adjudication and linkage gates pass; and configuration leave-out remains within the locked limit. This would support measurement validity of the locked endpoint for represented configurations, while separately describing implementation and rescue rates. It would not support a preferred vasopressor, safety, causal strategy benefit, or noninferiority in a treatment trial.

Adverse results include a bound at or above 0.025, a component alarm, differential missingness/discordance, poor adjudication or pump linkage, or instability under configuration leave-out. These falsify the endpoint-validity claim for the proposed use or expose a specific implementation/measurement failure; they do not prove that either strategy is clinically inferior.

Inconclusive results include failure to accrue 5,920 new randomized patients within the fixed window, excessive unresolved states, unavailable synchronized pump/intent evidence, or failure of clinical governance to ratify the state utility. Inconclusive is not success and does not justify post hoc denominator restriction, relaxed gates, or inference from MIMIC.

What remains for another study is a randomized efficacy/safety trial with the validated endpoint and explicit treatment estimand, clinical adjudication of appropriateness and harm, and broader multisite transport. The present proposal's advance is a clinically interpretable separation of implementation performance, post-implementation rescue, and endpoint measurement error without sacrificing the all-randomized denominator or the exact RD-distortion guarantee.
