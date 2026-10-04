> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Asynchronous renal/respiratory recovery as a context shift for lactate-by-perfusion monitoring

## Status and scientific deliverable

This is a substantive successor of assessed-valid `[prior hypothesis]`. It preserves that candidate's leakage-safe first adult live ICU-exit cohort, one-hour availability buffer, dual clinical/store-time feature rule, persistent-lactate-by-measured-perfusion phenotype, late hepatic burden and paired bilirubin/ALT/AST trajectory, 48-hour competing R/D/S/N/U endpoint, L+B-to-C transport freeze, fixed 10% review queue with a 50% transparent safety-net reserve, uncertainty, process falsifications and noncausal boundaries.

No cohort count, prevalence, fitted estimate, calibration result, or clinical conclusion is claimed. The new scientific deliverable is a prespecified organ-trajectory interaction:

> Among patients with adequate observed renal and respiratory coverage at a live ICU exit, does the lactate-by-measured-perfusion risk contrast and its incremental fixed-capacity review-queue capture differ when renal and respiratory trajectories are asynchronous (one improving while the other is not) versus concordant?

The future Harbor solver must newly produce:

1. an all-eligible flow, the inherited parent coverage flow, and an organ-trajectory coverage flow with row-level clinical-time/recording-time provenance and deterministic exclusion reasons;
2. the inherited lactate/perfusion and hepatic phenotypes, plus an observed renal state, observed respiratory state, and prespecified asynchronous state;
3. standardized 48-hour competing-risk CIFs and R/D decompositions for the lactate/perfusion contrast within the organ states, with a predeclared interaction estimand and subject-level uncertainty;
4. held-out fixed-capacity capture comparing the inherited hepatic/trajectory model with the new organ-interaction model at exactly a 10% review queue, half reserved for the transparent incumbent, with 5% and 20% workload sensitivities;
5. matched transparent Bdisc/Bhep/Basync/Bmask models and a same-input chronological M2 sensitivity, all frozen on one subject-level split;
6. coverage, unit, availability, selection-overlap, process-only, chronology-shuffle and phenotype-permutation audits; and
7. a conclusion ledger assigning supportive, adverse or inconclusive status from the gates and prespecified effect criteria.

The organ labels are observed EHR trajectories, not claims of kidney recovery, lung recovery, perfusion recovery, or mechanism. The primary question is prognostic/ranking heterogeneity under a documented ICU-exit observation process, not a treatment effect, discharge-policy effect, or proof that an alert improves outcomes.

## Evidence, unresolved claim and clinical importance

The strongest available evidence is design and availability evidence. The local MIMIC-IV schema contains the required keys and time fields, and the ICU dictionary directly verifies creatinine, MAP, O2 flow, FiO2, ventilator-mode, airway-pressure and Foley item definitions. The expert asynchronous-organ-recovery seed proposes that persistent organ impairment after circulatory stabilization may precede renewed deterioration, but it is explicitly untested and supplies no cutoff, event support or fitted result. The inherited candidate supplies no fitted result either. Thus current evidence supports only that this can be made into a bounded observed-data experiment; it does not support the hypothesis.

The parent asks whether persistent lactate has different observed near-term risk according to measured perfusion and whether a late record-defined hepatic burden/trajectory changes that signal. A single cross-sectional organ flag can obscure a clinically important discordance: renal markers may appear to improve while respiratory support remains high, or respiratory support may fall while renal output/creatinine remains abnormal. If this discordance identifies a subgroup in which improving measured perfusion is not reassuring, a future monitoring protocol might need to display joint organ trajectory rather than one lactate or SOFA snapshot. If it does not, the additional complexity would not be justified.

The primary falsifiable hypothesis is:

> Within the parent’s supported live-exit cohort, the absolute 48-hour R/D risk contrast between persistent lactate with improving measured perfusion and the matched nonpersistent-lactate comparison is less reassuring in the asynchronous organ state than in concordant-improving or concordant-nonimproving states; correspondingly, adding the organ state should increase held-out R/D capture in the fixed safety-net queue.

Let (I) denote improving measured perfusion, (P) persistent lactate, (H+) late hepatic burden, (G) the inherited paired biochemical trajectory, and (A_o) the new asynchronous state. The primary new risk interaction is:

`Theta_async = [CIF_RD(P,I,H+,G,A_o=asynchronous) - CIF_RD(NL,I,H+,G,A_o=asynchronous)] - [CIF_RD(P,I,H+,G,A_o=concordant) - CIF_RD(NL,I,H+,G,A_o=concordant)]`.

The primary comparison pools concordant improving and concordant nonimproving states only if both pass the pre-fit support gate; the solver must also report the two component contrasts. The directional hypothesis is `Theta_async > 0`: persistent lactate with improving measured perfusion is less reassuring when renal and respiratory trajectories disagree. A prespecified clinically meaningful interaction region is an absolute 0.05 48-hour R/D CIF difference. The primary policy estimand is the difference in held-out R/D capture of the organ-interaction model versus the inherited hepatic model in each organ state under a fixed 10% queue with 50% of slots reserved for the transparent incumbent; a 0.03 absolute gain is the meaningful policy threshold.

Supportive evidence requires the direction and at least 0.05 interaction criterion in both legacy and contemporary target eras, adequate overlap and event support, a concordant R/D decomposition, a positive fixed-queue increment meeting its 0.03 criterion, and attenuation under process-only and permutation controls. Adverse evidence is a reproducible null inside the prespecified interaction region, reversal, deterioration in calibrated risk or queue capture, a similar effect in the physiology-masked model, or persistence after organ-state permutation/chronology shuffling. Inconclusive evidence includes failed coverage or event gates, sparse asynchronous cells, high unresolved follow-up, poor overlap, unit ambiguity, unstable bootstrap, or disagreement between target eras. A supportive result motivates a prospective silent-mode study; it does not establish benefit, preventability or causal physiology.

## Population and temporal boundaries

Use the inherited parent cohort without changing its target:

- Join `icu/icustays` to `hosp/admissions` on `(subject_id,hadm_id)`, and to `hosp/patients` on `subject_id`.
- Retain adults with `anchor_age >= 18`; preserve the MIMIC `anchor_age=91` representation.
- Select one first valid ICU stay per admission, deterministically sorted by `(outtime,intime,stay_id)`, requiring nonmissing identifiers, `intime < outtime`, and at least 13 hours of ICU history.
- Set `t0=outtime` and `tL=t0-1 hour`. Retain a known live exit only when `deathtime > t0`, or `deathtime` is null with `hospital_expire_flag=0`. Contradictory or missing survival fields are unresolved, not survival.
- Extract features only from `[t0-13h,tL]`, with early `[tL-12h,tL-6h)` and late `[tL-6h,tL]`. A charted row requires `charttime <= tL) and `storetime <= tL). An interval row requires finite `starttime < endtime), `storetime <= tL), and clinical overlap with the window. Chart-before/store-after rows are excluded from the primary analysis and retained in a chart-time-only sensitivity.
- Ascertain the first transition in `(t0,t0+48h]`: R is a later ICU stay in the same admission, D is timed in-hospital death, S is alive hospital discharge with `hospital_expire_flag=0), N is known event-free follow-up, and U is unresolved. Preserve deterministic first-transition and tie ordering; never convert U into N.

Use historical L (2008–2013) and contemporary C (2017–2022) as primary target eras, with B (2014–2016) descriptive. Fit thresholds and models on L+B and freeze them before scoring C. Use a subject-level 70/15/15 train/validation/test split stratified only by original era group, parent phenotype cell, organ state and endpoint label; all admissions of one subject remain in one partition.

The inherited late hepatic burden H and paired biochemical trajectory G remain primary context variables exactly as in the parent. The solver must not replace the parent's G definitions after seeing outcomes. The new organ state is defined before outcome reading, and subjects failing its support gate remain in all-eligible and parent flows but are not silently forced into a comparison cell.

## Parent phenotype retained

Persistent lactate P requires both six-hour half medians of labevents item 50813 to be defined and at least 2.0 mmol/L; NL requires both defined and at least one below 2.0. A fixed 4.0 mmol/L threshold is a secondary sensitivity.

Improving perfusion I requires late-minus-early median MAP >=5 mmHg and late target-pressor unioned minutes no greater than early minutes. W requires MAP change <=-5 mmHg and late target-pressor minutes no less than early minutes. Other combinations are indeterminate. Each half requires at least one valid lactate, at least two MAP observations at distinct clinical times, and one positive-duration target-pressor interval. Missing pressor ascertainment is not zero exposure.

MAP uses ICU chartevents item IDs 220052, 220181 and 225312, accepted units audited as mmHg. Target pressors use inputevents item IDs 221906, 222315, 221289, 229617, 221749, 229630, 229631, 229632, 221662, 221653 and 221986. Use interval `starttime/endtime` for duration and `storetime` for availability; do not pool rate and amount into a dose.

The inherited hepatic burden uses labevents 50885 (total bilirubin), 50861 (ALT), and 50878 (AST), with thresholds fit on finite training values and frozen before validation/test/outcomes. The inherited G trajectory requires paired early/late markers and uses the parent’s marker-specific symmetric change rules. It is named a recorded biochemical trajectory, not liver recovery.

## New observed renal/respiratory trajectory state

The state is deliberately conservative and record-defined. No imputation, last-observation carry-forward, reference-range substitution or outcome-dependent thresholding is allowed. Thresholds below are fixed design cutoffs, not clinical claims; unit acceptance and row support are audited before fitting.

### Renal state Rg

Use labevents creatinine item 50912 and ICU outputevents Foley item 226559.

A half has creatinine coverage when it contains at least two finite numeric 50912 values at distinct `charttime` values, each with `charttime/storetime <= tL), and an accepted canonical unit. A half has Foley coverage when it has at least one positive-duration output observation per 6-hour half after summing only clinically distinct rows; the output rate is volume divided by observed half duration, with no interpolation across unmeasured time. Rows must have finite `charttime`, `storetime <= tL`, finite nonnegative `value`, and `valueuom=mL` after the frozen unit audit.

Renal-improving requires both halves covered and either (a) late creatinine median is at least 0.3 mg/dL and at least 15% below early median while late urine-output rate is not lower than early rate by more than 10%, or (b) late urine-output rate is at least 20% higher while late creatinine is not higher than early by more than 0.3 mg/dL and 15%. Renal-nonimproving is the symmetric non-improving category among covered halves: it includes stable, mixed and worsening patterns not satisfying renal-improving. If both indicators are contradictory or missing, label renal-indeterminate. The solver must report creatinine-only and output-only sensitivities; they cannot replace the composite primary state. This is suspected observed renal trajectory, not measured GFR or kidney recovery. Dialysis status is not inferred unless an additional dictionary-verified procedure/input audit is explicitly reported.

### Respiratory state Qg

Use ICU chartevents items 223834 (O2 Flow), 223835 (Inspired O2 Fraction), and, as a support-context sensitivity, 223848/223849 (ventilator type/mode). Dictionary-confirmed airway pressure items 224695, 224696 and 224697 may be included only in a declared sensitivity and never treated as oxygenation.

A half has primary respiratory coverage when it has at least two finite numeric O2 Flow and two finite numeric FiO2 observations at distinct clinical times, with accepted units (O2 Flow L/min; FiO2 fraction or percent normalized only when the observed unit is unambiguous), and recording time no later than tL. A half's respiratory burden is the standardized mean of within-half robust ranks of O2 flow and FiO2; the primary raw summaries remain separately reported. O2 flow and FiO2 are not conflated, and missing FiO2 is not zero.

Respiratory-improving requires both halves covered and both late medians no greater than their early medians, with at least one relative reduction of 20% and no marker worsening by more than its fixed 20% rule. Respiratory-nonimproving includes stable, mixed or worsening covered patterns not satisfying respiratory-improving. Respiratory-indeterminate means either half lacks primary coverage. Ventilator-mode text is a context sensitivity only; no mode text is converted into invasive ventilation without expert-reviewed mapping.

### Asynchrony cell A_o

Among subjects with both renal and respiratory states observed:

- Concordant-improving: Rg=improving and Qg=improving.
- Concordant-nonimproving: Rg=nonimproving and Qg=nonimproving.
- Asynchronous: exactly one of Rg and Qg is improving and the other is nonimproving.
- Other/indeterminate: any renal or respiratory indeterminate state.

The primary contrast pools the two concordant states only when both have the required support and reports them separately. Asynchronous is not called organ failure, recovery, discordance of biology, or treatment response. The new primary support gate is endpoint-independent and frozen before model fitting: at least 40 subjects and 10 known R/D events in every primary P/NL × I × H+ × G × A_o cell in each target era; at least 8 test subjects and 3 R/D events per evaluated cell; U <=10% overall and <=20% per cell; positive overlap/ESS for the queue comparison; and the inherited parent/H/G gates. If the gate fails, report `Theta_async=not estimable` and do not merge states or relax thresholds after outcomes.

## Estimands, competing risks and queue

For each supported organ cell, report standardized 48-hour CIFs for R, D and S, composite A=R-or-D, N/U accounting, and the inherited H/G contrasts. The primary new estimand is `Theta_async` above. Report the R-specific and D-specific decomposition, the asynchronous-versus-concordant-improving and asynchronous-versus-concordant-nonimproving contrasts, W perfusion sensitivity, H0/H+ sensitivity, G-stratified sensitivity, and 6/12/48-hour profiles where support permits.

Use cause-specific risk models or a directly standardized competing-risk estimator with prespecified covariates; no post-t0 information may enter. Report absolute risks and risk differences, not only discrimination. Use 95% subject bootstrap intervals preserving all admissions of each subject, with a fixed replicate count and seed declared before execution. Report effective sample size, overlap, bootstrap failures and whether intervals are conditional-prediction or full-refit intervals.

For held-out subjects, rank frozen predicted 48-hour A risk with deterministic score/subject-ID tie-breaking. Select exactly the top 10%. In the primary safety-net comparison, reserve 50% of the queue for the transparent inherited Bhep score and fill the remaining 50% with Basync scores after excluding reserved subjects. Report overlap, A/R/D capture, PPV, random benchmark and paired subject-bootstrap intervals overall and by A_o when supported. Report 5% and 20% queue sensitivities secondarily. This is an allocation operating characteristic, not patient benefit.

The queue result is supportive only if the organ-interaction model's incremental capture is at least 0.03 in the prespecified direction with uncertainty excluding zero in both L and C, while the parent and organ support gates pass. Era disagreement makes the transport claim inconclusive even if pooled results are positive.

## Matched models and method choice

All models use the same eligible subjects, source whitelist, endpoint, time boundary, split, test set and queue.

- **B1:** order-blind transparent aggregate competing-risk baseline: fixed 12 one-hour bins of available lactate/MAP/pressor, renal/respiratory/hepatic values, admission/demographic context, missingness, counts and availability lag.
- **Bhep:** the inherited transparent hepatic model adding P-by-perfusion, H and G terms but no new A_o interaction.
- **Basync:** transparent extension of Bhep adding Rg, Qg, A_o, P×I×A_o, and prespecified R/D/S cause-specific effects. This is the primary scientific model because its new estimand is auditable.
- **Bmask:** retains measurement counts, missingness, store lag, availability and care-process indicators but removes physiologic values and organ-state values. A similar interaction here suggests testing intensity or workflow rather than physiology.
- **M2:** a small masked chronological GRU over the identical 12 one-hour bins and raw whitelist: lactate, hepatic markers, creatinine, Foley output rate, O2 flow, FiO2, MAP, pressor exposure, context, values, masks, counts and timing/process channels. Hidden size 32 or 64, five fixed seeds, early stopping and dropout selected only on training/validation. M2 can reveal whether within-half ordering and nonlinear renal/respiratory coupling add information lost by the half-median state; it cannot by itself establish mechanism.

The transparent baseline is scientifically adequate: Bhep isolates incremental value over the inherited question, and Basync tests the exact new organ-state interaction. M2 is substantive rather than cosmetic because it retains temporal order and joint timing discarded by fixed early/late summaries. M2 is deferred if the leakage-safe tensor cannot be constructed, the new state gate fails, chronology shuffles are not reproducible, or the alternative adds no distinct information. A full transformer is deferred because the accessible demonstrations establish learned sequence modeling but do not make a full transformer necessary here; added capacity would not repair selective testing, absent measured GFR or absent expert adjudication.

The demonstrations are treated as methodological inspiration, not reproduction targets. The natural-history Delphi paper and methods summary provide verified evidence that structured dated histories can be learned and that a bounded disease-sequence adaptation is possible; M2 is the data-bound adaptation. The Bayesian ALADYNOULLI paper supports a possible longitudinal latent-trajectory sensitivity, but its genetic inputs are not required/verified here and a latent model would not add a distinct clinical estimand beyond M2, so it is deferred. The cancer Oncoformer main paper and complete STAR Methods are unavailable; its supplement supports multimodal learning/ablation context, but MIMIC-CXR images are unavailable locally, so no image claim or reproduction is made. The organ-aging demonstration concerns proteomics not available in this MIMIC source, so it is not pursued.

## Falsification and process controls

1. Verify every item label, unit and link in `icu/d_items` and `hosp/d_labitems`; report accepted/rejected units, finite/impossible values, duplicates and item-specific coverage.
2. Produce all-eligible, parent-coverage, hepatic-trajectory and organ-state flows before reading outcomes into model code. Audit joins, first-stay selection, live-exit survival flags, one-hour buffer, half boundaries, subject split, threshold fitting and no-post-tL access.
3. Fit Bmask with testing density, number of renal/respiratory observations, store lag, care-unit/process fields and availability flags. If Bmask reproduces the interaction, downgrade the physiologic interpretation.
4. Permute A_o across subjects within fixed era/partition/H/G/parent-cell strata, refit, and require the interaction and queue increment to collapse toward the permutation benchmark.
5. Shuffle early/late order while preserving values, counts and masks; a surviving result weakens the trajectory interpretation. Chronology-shuffle M2 is a separate negative control.
6. Repeat with creatinine-only, output-only, O2/FiO2-only, no-ventilator-context, arterial-only/non-invasive-only MAP, and chart-time-only availability. These are sensitivities, not replacements.
7. Test fixed 4.0 lactate threshold, paired-marker thresholds, continuous burden, and alternate 6-hour/12-hour windows, with no outcome-driven selection.
8. Audit urine-output duration, Foley availability, duplicate collapse, FiO2 percent/fraction conversion, impossible values, rate/amount separation and whether respiratory documentation is selectively denser in high-risk patients.
9. Report care-unit, era, age/sex and measurement-intensity strata only with frozen support. Do not call them causal effect modifiers.
10. The verifier must check both computation and inference: a numerically correct positive interaction with unsupported conclusions is a failure, as is a negative/inconclusive result reported as hypothesis confirmation.

## Interpretation limits and unavailable evidence

A supportive result establishes only reproducible observed prognostic/ranking heterogeneity between a record-defined asynchronous organ state and concordant states at this MIMIC live-exit landmark. It may justify a prospectively adjudicated silent-mode study that measures treatment intent, fluid balance quality, true renal function, oxygenation, ventilator settings, liver etiology/synthetic function and actionable deterioration.

It does not establish renal or respiratory recovery, microcirculatory status, hepatic lactate clearance, causal organ interaction, fluid/pressor/ventilator treatment effect, discharge appropriateness, monitoring benefit, preventability, net benefit or external transportability. Measured GFR, reliable fluid responsiveness, arterial oxygenation/waveforms, adjudicated organ failure, treatment limitation intent, post-discharge events, and external validation are not available in the configured evidence. Expert review is required for clinical meaning of trajectory cutoffs, endpoint actionability, unit/ventilator mapping and whether a 10% queue is operationally plausible.

## Exact read-only source bindings

Catalog: `[internal dataset path]`, [source checksum].

Primary source: `[internal dataset path]`, 10,551,747,784 bytes, [source checksum]. Source is read-only.

Required archive members and table bindings:

- `mimic-iv-3.1/icu/icustays.csv.gz` (`icu/icustays`): `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; join, first-stay selection and t0.
- `mimic-iv-3.1/hosp/admissions.csv.gz` (`hosp/admissions`): `subject_id,hadm_id,admittime,dischtime,deathtime,hospital_expire_flag`; joins and R/D/S/U.
- `mimic-iv-3.1/hosp/patients.csv.gz` (`hosp/patients`): `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; adult and era fields.
- `mimic-iv-3.1/hosp/labevents.csv.gz` (`hosp/labevents`): `labevent_id,subject_id,hadm_id,specimen_id,itemid,charttime,storetime,value,valuenum,valueuom,ref_range_lower,ref_range_upper,flag,priority,comments`; lactate 50813, creatinine 50912, bilirubin 50885, ALT 50861, AST 50878, optional INR 51237/PT 51274. Use `labevent_id` for provenance and `charttime/storetime` for clinical/availability time.
- `mimic-iv-3.1/hosp/d_labitems.csv.gz` (`hosp/d_labitems`): `itemid,label,fluid,category`; laboratory dictionary/unit audit.
- `mimic-iv-3.1/icu/chartevents.csv.gz` (`icu/chartevents`): `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; MAP 220052/220181/225312, O2 flow 223834, FiO2 223835, ventilator context 223848/223849, optional pressures 224695/224696/224697.
- `mimic-iv-3.1/icu/d_items.csv.gz` (`icu/d_items`): `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue`; ICU item dictionary and unit audit.
- `mimic-iv-3.1/icu/inputevents.csv.gz` (`icu/inputevents`): `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,patientweight,totalamount,totalamountuom,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate`; target pressor intervals and availability.
- `mimic-iv-3.1/icu/outputevents.csv.gz` (`icu/outputevents`): `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valueuom`; Foley item 226559 and urine-output timing.
- `mimic-iv-3.1/hosp/transfers.csv.gz` (`hosp/transfers`): `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; pre-landmark care-context audit only.
- `mimic-iv-3.1/icu/procedureevents.csv.gz` is catalogued but not required for primary predictors; no procedure-derived ventilation is assumed.
- Note files `note/discharge.csv.gz`, `note/discharge_detail.csv.gz`, `note/radiology.csv.gz`, and `note/radiology_detail.csv.gz` are available but excluded from the primary whitelist; no text adjudication is claimed. MIMIC-CXR images and raw waveforms are unavailable.

Required joins are `icu/icustays -> hosp/admissions` on `subject_id,hadm_id`, `icu/icustays -> hosp/patients` on `subject_id`, ICU event rows additionally on `stay_id), and lab rows on `subject_id,hadm_id). Do not join on free text or patient names.

## Compute, method budget and measured versus unverified estimates

The inherited discovery scan over selected labevent IDs reached its 600-second limit without an output; the direct archive dictionary/schema audit is verified, while row-level prevalence, paired support, event counts, unit distribution, model convergence and bootstrap runtime remain unmeasured. This proposal does not pretend the failed scan demonstrates absence.

B1/Bhep/Basync/Bmask should be CPU-feasible with 8–16 CPUs and 32–128 GiB, with under 30 minutes for fitting expected but unverified. Subject bootstrap is separately budgeted. M2 is a bounded sensitivity at 4 CPUs and 16–32 GiB, either CPU or one allocated A100, with five seeds and up to two hours expected but unverified. If a GPU is used, request `gpus=1`, use `cuda:0` inside the allocation, and explicitly move model/tensors; ordinary shell CUDA absence is not evidence. Full solver planning must stay within 16 CPUs, 262144 MiB, up to 8 GPUs and 28800 seconds. No proposer/solver weight training is authorized.

The actual scientific choice is Basync as the primary interpretable model plus M2 as a deferred/secondary sequence sensitivity. The alternative is retained because it tests within-half ordering and nonlinear joint timing that Basync intentionally discards. It must be deferred if support or leakage checks fail, not replaced by an easier question.

## Completion and evidence record

The study is complete only when the solver supplies the frozen source/provenance and gate reports; matched held-out predictions; CIF, interaction, R/D, queue and calibration tables with uncertainty; all falsification outputs; model and process comparisons; and a conclusion ledger that distinguishes supportive, adverse and inconclusive results. Readiness or compilation can validate packaging and bounded probes but cannot establish the hypothesis.

No fitted result is supplied here. A failed support gate is a valid not-estimable scientific result and is not permission to change population, timing, estimand or cutoffs after seeing outcomes.
