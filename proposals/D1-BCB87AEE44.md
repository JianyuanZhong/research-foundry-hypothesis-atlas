> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Clinically interpretable trajectory instability before live ICU discharge

## Scientific deliverable and substantive evolution

The future Harbor solver must newly produce a reproducible first eligible live-ICU-discharge cohort, an ascertainable four-category 48-hour first-event outcome, a fixed trajectory-instability construct, and a fair comparison of terminal-state, order-blind history, and chronological history representations. Completion requires held-out predictions, uncertainty, observation-process sensitivities, competing-risk calibration, falsification tests, and an interpretation audit. A favorable result, task readiness, or a successful fit is not completion.

This is a substantive child of [prior hypothesis]. It retains the parent's 12-hour landmark, exact structured MIMIC-IV bindings, subject-level split, and matched aggregate-versus-sequence comparison. The material refinement is twofold. First, “instability” is no longer only a late abnormality burden: it is a prespecified, clinically readable combination of persistent abnormal burden, worsening versus recovery, and short-term fluctuation. Second, the primary outcome is an ascertainable competing-risk first-event estimand that reports ICU readmission and in-hospital death separately, while treating early hospital discharge as an observation-ending competing event rather than silently treating it as an observed zero-risk interval. This remains a prognostic study; it does not estimate whether discharge was appropriate or whether changing care would improve outcomes.

The actual scientific deliverable is newly fitted/estimated TIS component and phenotype associations, B0/B1 held-out competing-risk predictions, and a matched chronological GRU comparison. Completion outputs are the frozen cohort/label audit, feature manifest, model predictions, cause-specific cumulative-incidence calibration and Brier results, bootstrap intervals, observation-process and endpoint sensitivities, falsification outputs, and conclusion-to-output audit. No scientific outcome is claimed in this proposal.

## Unresolved question and evidence boundary

At the time a patient leaves the ICU alive, does a clinically meaningful trajectory of residual physiologic instability predict the distinct 48-hour risks of returning to the ICU versus dying in hospital, beyond the latest recorded state and admission/ICU context? Clinically, these outcomes motivate different review questions: readmission may signal inadequate ward transition or escalation, whereas death may reflect severe residual illness, treatment limitation, or another process. Separating them is important for interpreting a risk signal and for deciding what additional clinical review might be warranted.

The primary falsifiable hypothesis is:

> Among first eligible live ICU discharges with an ascertainable first-event label, adding the prespecified 12-hour trajectory-instability history to terminal state and admission/ICU context improves held-out probabilistic prediction and calibration of the 48-hour first-event competing-risk distribution, with reproducible positive associations for readmission-first and/or death-first cumulative incidence.

The primary competing-risk estimands are:
CIF_R(48|X) = P(T <= 48 hours, J = ICU readmission), and
CIF_D(48|X) = P(T <= 48 hours, J = timed in-hospital death),
where T is the first observed terminal event after ICU outtime and J is its type. Alive hospital discharge before 48 hours is an observation-ending competing event H; remaining hospitalized without readmission or death through 48 hours is N. Thus the modeled four-category outcome is J in {R,D,H,N}, and CIF_R and CIF_D are unconditional probabilities over the eligible index cohort, not a post-discharge treatment effect. The sum CIF_R + CIF_D is a descriptive adverse first-event probability, not net clinical benefit.

The primary incremental estimand is the paired held-out change in multiclass Brier score for the four first-event probabilities, Delta_Brier_history = Brier(B1) - Brier(B0), with negative values favorable. Report separate paired Brier/calibration differences for CIF_R and CIF_D, calibration intercept/slope or reliability tables, and outcome-free threshold operating characteristics for readmission and death risk. A supportive result means reproducible prognostic information for recorded outcomes. It does not show that delaying ICU transfer, increasing ward monitoring, changing treatment, or using a threshold would help.

The TIS estimand is descriptive and observational: report risk-standardized differences in CIF_R(48) and CIF_D(48) comparing prespecified TIS phenotypes, plus component-specific associations. It is not a causal effect of instability, and it is not a discharge-appropriateness score.

The strongest claim supported before analysis is only that this frozen snapshot contains ICU boundaries, admission death/discharge fields, and timestamped structured observations from which these labels and features can be constructed. It does not support a claim that instability caused either event, that either event was preventable, that death timing is complete for every record, or that post-ICU review/monitoring would change outcomes. The research-ambition demonstrations were inspected as method/rigor references; they are not evidence for this MIMIC question and are not reproduced.

## Population, index, and temporal boundaries

The source unit is an ICU stay linked to one hospital admission.

1. Read every icu/icustays row with non-null subject_id, hadm_id, stay_id, intime, outtime. Reject outtime <= intime, outtime < admittime, and rows without a matching admission.
2. Inner join hosp/admissions on (subject_id, hadm_id) and require non-null admittime and dischtime. Left join hosp/patients on subject_id for age, sex, and anchor-year-group context; never use dod.
3. Define an eligible live ICU discharge at t0 = outtime when outtime < dischtime and either deathtime is null or deathtime > outtime. Select the earliest eligible discharge per (subject_id, hadm_id), ordered by outtime. A secondary all-eligible analysis clusters by subject and hospitalization.
4. The primary analytic set requires at least four of twelve bins with at least two valid core numeric channels and a known, ascertainable first-event category. Retain a full flow table from all ICU rows through eligibility, coverage, and outcome ascertainment; unknown death timing is not silently counted as no event.
5. Use one deterministic approximately stratified 70/15/15 split by subject_id for training, validation, and test. No subject may occur in more than one partition. Because MIMIC timestamps are subject-specifically shifted, do not align calendar dates across subjects.

The feature window is exactly [t0 - 12 hours, t0], divided into twelve backward chronological bins [t0-12h,t0-11h), ..., [t0-1h,t0]. Use charttime for charted observations and starttime/endtime for intervals. storetime is never used for ordering, inclusion, or missingness. No clinical-time value after t0 is allowed, even if stored before it.

## Ascertainable competing-risk outcome

Search after t0 through t0+48 hours and no later than dischtime:

- R (readmission-first): the earliest later icu/icustays row with the same subject_id, hadm_id, a different stay_id, and intime > t0.
- D (death-first): hosp/admissions.deathtime > t0 and within 48 hours, occurring before any R event.
- H (alive hospital discharge): dischtime <= t0+48h before either R or D.
- N (no observed event): neither R nor D occurs by 48 hours and the patient remains hospitalized at 48 hours.

The first event is assigned by clinical timestamp. A same-time death is assigned D before R or H; a same-time ICU re-entry is assigned R before H. The solver must save event times, tie decisions, and the full R/D/H/N count table. A 48-hour composite is a secondary descriptive output R or D, never the primary estimand.

If hospital_expire_flag=1 but deathtime is null, the record cannot establish whether the death fell in the 48-hour window or whether another event preceded it. Mark it U and exclude it from the primary ascertainable analysis without imputation. Report U count, coverage, care-unit, and context distributions. Run prespecified bounds that place each U into timed death (when no earlier recorded readmission exists) versus no adverse first event; these are partial-identification bounds, not sensitivity-adjusted point estimates. If a deathtime is present, use its clinical time even when the flag is inconsistent and report the inconsistency audit.

Secondary outcomes are the same R/D/H/N construction at 7 days, readmission-first alone, death-first alone, the parent composite, and a sensitivity treating early alive discharge as administrative censoring with inverse-censoring weights only if diagnostics support positivity. The primary four-category construction makes the main 48-hour probabilities ascertainable without pretending that post-discharge same-admission events were observed.

## Exact MIMIC-IV data bindings and provenance

All source files are read-only. Cohorts, manifests, feature matrices, model states, predictions, bootstrap indices, and reports are workspace-derived files.

- Dataset guide: datasets/README.md; MIMIC guide: datasets/mimic/README.md.
- Snapshot: [source checksum].
- Read-only source ZIP: [internal dataset path], [source checksum] (see exact below).

The catalog is [internal dataset path], [source checksum].

Required source bindings:

| Role | Table and exact archive member | Required columns, key, and clinical time |
|---|---|---|
| Index and future ICU episodes | icu/icustays; mimic-iv-3.1/icu/icustays.csv.gz | subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los; join admissions on (subject_id,hadm_id); index at outtime; future R uses same admission, different stay, intime>t0. |
| Admission labels/context | hosp/admissions; mimic-iv-3.1/hosp/admissions.csv.gz | subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admission_location,discharge_location,hospital_expire_flag; admittime/dischtime/deathtime define eligibility/labels; discharge_location is prohibited from every model. |
| Demographic context | hosp/patients; mimic-iv-3.1/hosp/patients.csv.gz | subject_id,gender,anchor_age,anchor_year_group,dod; left join on subject_id; dod is prohibited. |
| Core ICU measurements | icu/chartevents; mimic-iv-3.1/icu/chartevents.csv.gz | subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valuenum,valueuom,warning; retain rows by stay_id and clinical charttime in the window. |
| ICU dictionary | icu/d_items; mimic-iv-3.1/icu/d_items.csv.gz | itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue; verify item meaning, link, and units. |
| Vasoactive/interval sensitivity | icu/inputevents; mimic-iv-3.1/icu/inputevents.csv.gz | subject_id,hadm_id,stay_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,statusdescription plus archive columns; clip usable intervals to window and reject missing/reversed timing. |
| Urine-output sensitivity | icu/outputevents; mimic-iv-3.1/icu/outputevents.csv.gz | subject_id,hadm_id,stay_id,charttime,storetime,itemid,value,valueuom; Foley itemid=226559; missing output is not zero. |
| Laboratory sensitivity | hosp/labevents; mimic-iv-3.1/hosp/labevents.csv.gz | labevent_id,subject_id,hadm_id,specimen_id,itemid,charttime,storetime,value,valuenum,valueuom,ref_range_lower,ref_range_upper,flag,priority,comments; join (subject_id,hadm_id) and use charttime<=t0. |
| Laboratory dictionary | hosp/d_labitems; mimic-iv-3.1/hosp/d_labitems.csv.gz | itemid,label,fluid,category; verify lactate 50813, creatinine 50912, bicarbonate 50882, hemoglobin 51222, platelets 51265, WBC 51300. |

The required archive members were checked present in the read-only ZIP. Local schema JSONs confirm these columns and temporal fields. Ordinary note files note/discharge, note/discharge_detail, note/radiology, and note/radiology_detail are available outside the ZIP but are excluded from every feature matrix; no text, discharge_location, dod, or post-outtime field enters a model. Images and raw waveforms are unavailable.

The audited item IDs are HR 220045; MAP 220052,220181,225312; RR 220210; SpO2 220277; temperature 223762; FiO2 223835; O2 flow 223834,227287; PEEP 220339,224700; vasoactive input IDs 221906,222315,221289,229617,221749,229630,229631,229632,221662,221653,221986; Foley 226559; and the six laboratory IDs above.

## Fixed trajectory-instability construct

Core channels are HR, MAP, RR, SpO2, temperature, FiO2, O2 flow, and PEEP. Use numeric valuenum and valueuom; reject fixed impossible ranges: HR 20–250 bpm, MAP 20–200 mmHg, RR 2–80/min, SpO2 50–100%, temperature 30–43 C, O2 flow 0–100 L/min, and PEEP 0–40 cmH2O. For FiO2 divide values above 1.5 by 100, then retain 0.21–1.00. Deduplicate an item within a bin and clinical timestamp by median. For MAP use source priority arterial 220052, non-invasive 220181, then ART 225312, with the median within the selected source.

A bin is valid when at least two core channels are observed. For each valid bin b, define q_b = abnormal_core_count_b / observed_core_count_b, using fixed indicators HR <50 or >120, MAP <65, RR <8 or >24, SpO2 <92, temperature <36 or >=38.5 C, FiO2 >0.40, O2 flow >=4 L/min, and PEEP >5 cmH2O. Store every numeric value, channel mask, abnormal flag, and observed-channel count. Do not impute an unobserved channel as normal.

For a patient with at least four valid bins, calculate in chronological order:

- P (persistent burden): mean q_b over valid bins.
- W (direction): mean q_b in the last three valid bins minus mean q_b in the first three valid bins, requiring at least six valid bins; negative values represent recovery.
- V (fluctuation): mean absolute change in q_b over consecutive valid bins, requiring at least three valid adjacent pairs.
- TIS_count: I(P>=0.50) + I(W>=0.25) + I(V>=0.25), with unavailable components reported missing rather than imputed.

The cut points are fixed from the clinical abnormal-fraction scale, not selected using outcomes. P captures persistent multi-channel burden; W distinguishes worsening from recovery; V captures instability even when the final value looks acceptable. Report components and the 0–3 phenotype separately; do not hide component missingness in the count. A secondary support descriptor adds vasoactive presence/overlap minutes from clipped inputevents, and optional urine/laboratory sensitivities, but these cannot replace the core TIS.

## Observation-process robustness

Observation is potentially informative: sicker patients may be measured more often, and a missing value is not physiologic normality. Therefore:

1. The primary cohort and TIS require the stated minimum coverage, and every model includes valid-bin count, per-bin observed-channel count, and channel masks. B0, B1, and the GRU use the same observation whitelist and do not use storetime.
2. Fit a training-only pooled observation model for each core channel/bin indicator using only pre-index context and earlier-bin masks/counts, never outcomes or same-bin values. Form stabilized inverse-observation weights, clip them to [0.25,4], and use them for an observation-adjusted TIS sensitivity and weighted cause-specific association. Report positivity, effective sample size, clipping fraction, and whether the adjustment was estimable. No outcome model chooses these weights.
3. Fit a mask-and-count-only model with the same split and four-category endpoint. If it matches the full model, a documentation/monitoring process rather than recoverable physiology is a plausible explanation. Repeat B0/B1 comparisons within prespecified low-, middle-, and high-coverage strata, with no outcome-derived strata.
4. As an extreme ascertainment check, repeat the main comparison in a stricter cohort with at least eight valid bins and at least three observed core channels per valid bin. Treat loss of positivity or severe event depletion as inconclusive, not as evidence of no association.

The observation-adjusted analysis is a robustness check, not a claim that missing-not-at-random physiology has been identified. A remaining mask-sensitive signal requires expert review of care-process confounding.

## Baseline, aggregate history, and chronological learned alternative

The transparent baseline B0 is penalized multinomial logistic regression for R/D/H/N, using only: anchor age, gender, anchor-year-group, first and last ICU care unit, ICU duration at t0, admission type and location, earlier ICU-stay count in the admission, valid-bin count, core-channel coverage, and the terminal-bin numeric values, masks, abnormal flags, and observed-channel count. No history-derived value other than coverage enters B0.

The order-blind aggregate history model B1 uses the identical context, terminal state, source whitelist, endpoint, subject split, preprocessing and fitting rules as B0, and adds P, W, V, TIS_count, per-channel 12-hour mean/median/minimum/maximum/SD/IQR, abnormal-bin fractions, valid-bin/missingness summaries, observation counts/masks, vasoactive presence/overlap minutes, and fixed first-versus-last summaries. It is a transparent penalized multinomial logistic model; its coefficients and predicted CIF_R/CIF_D are saved.

The substantive chronological alternative is a small masked GRU with the exact same context and exact same per-bin input fields used to derive B1: eight numeric channels, channel masks, fixed abnormal flags, observed-channel count, and clipped vasoactive presence/minutes. It outputs the same R/D/H/N softmax probabilities and uses the same training/validation/test subjects. Scaling, imputation constants, categorical encodings, hidden size (32 or 64), dropout, early stopping, and calibration are fit using training/validation only; use five fixed seeds and preserve states/predictions. The GRU can reveal persistence, abrupt worsening/recovery, and coupled order when patients have similar aggregate summaries. It is scientifically useful only if its held-out competing-risk probabilities are better calibrated and reproducibly better than B1; neural complexity or a tiny ranking gain is not a clinical advance.

The representation estimand is Delta_Brier_order = Brier(GRU)-Brier(B1) on untouched test patients. Shuffle bins 1–11 within each test patient while holding the terminal bin, all values, masks, context, and endpoint fixed; a chronology-dependent gain should attenuate. Shuffle all bins as a secondary check. A terminal-only descriptive model diagnoses whether the apparent sequence result is just the last state.

## Analysis, uncertainty, and falsification

Before fitting, freeze split, item allowlist, preprocessing, thresholds, model settings, and the four outcome definitions. Fit all transformations and models on training/validation only. Evaluate paired test predictions with the four-category multiclass Brier score, class-specific Brier scores for R and D, log loss, calibration of CIF_R and CIF_D, AUROC/AUPRC as secondary ranking summaries, and prespecified absolute-risk threshold tables. Thresholds are selected from training/validation and an absolute-risk grid, never test outcomes. Report cause-specific empirical cumulative incidence alongside model calibration.

Use 1,000 subject-level bootstrap replicates when within the declared execution cap, preserving all patients from a subject together; otherwise report the exact completed number and label intervals execution-limited. Bootstrap the paired B0/B1/GRU differences, CIF contrasts, TIS associations, calibration, and falsification effects. Five GRU seeds are not a substitute for patient-level uncertainty.

Supportive evidence requires a negative Delta_Brier_history with a 95% interval excluding zero, no clinically important deterioration in either R or D calibration, and directionally consistent results in the 7-day, coverage, and observation-adjusted analyses. For the clinically meaningful TIS claim, report component-specific and phenotype-specific CIF intervals; do not require an arbitrary universal effect-size cutoff, but call the result clinically small when absolute CIF differences are small even if statistically precise. Chronology support additionally requires negative Delta_Brier_order, interval exclusion of zero, and attenuation under preterminal shuffle.

Adverse evidence is no incremental history information, worse calibration, a signal restricted to masks/coverage or one care unit, disappearance after observation adjustment, a TIS association driven only by terminal values, or a chronology gain that survives order shuffling. These support the narrower conclusion that charting intensity, terminal state, or treatment selection accounts for the apparent signal.

Inconclusive evidence includes too few R or D events, many U labels, poor positivity for observation weights, malformed interval timing, inadequate TIS coverage, unstable calibration, discordant cause-specific and composite results, or failed item/unit validation. Inconclusive is neither confirmation nor refutation.

Label permutation within split, chronology shuffle, terminal-state-only, mask-only, and coverage-stratified falsifications must be reported. Export assertions that every feature clinical time is <=t0, no subject crosses partitions, no prohibited field enters either model, and event labels are constructed only from allowed post-t0 fields.

## Clinical limits and unavailable evidence

Computationally checkable claims are the source/member/column/item manifest, join and time rules, cohort and R/D/H/N/U flow, coverage and positivity diagnostics, feature construction, partition integrity, paired predictions, metrics, bootstrap intervals, and falsification effects. The verifier can check whether conclusions follow from these outputs.

Unavailable or non-identifiable claims include ICU-transfer appropriateness, clinician intent, treatment limitations/goals of care, bed/staffing pressure, ward surveillance, whether charted oxygen equals delivered physiology, whether instability was preventable, whether enhanced monitoring changes an outcome, net clinical benefit, and external validity. Raw waveforms, images, and validated clinician-adjudicated discharge-readiness labels are unavailable. Those claims require expert adjudication, an external cohort, and preferably prospective or interventional evaluation. No causal discharge claim is permitted.

## Method alternatives, compute, and deferred branches

The simple baseline is B0 because latest state plus context is transparent and directly tests incremental history information. B1 is the substantive order-blind aggregate alternative: it answers whether reproducible history summaries and the fixed TIS construct add information without depending on chronology. The GRU is retained because a true trajectory question requires testing persistence and ordering, not merely adding more summary variables. All three use the same endpoint, subject split, source whitelist, and held-out uncertainty; B1 and GRU use identical full-history inputs.

The configured discovery science limit is 7,200 seconds. The future solver planning envelope is 16 CPUs, 262,144 MiB, up to 8 GPUs, and 28,800 seconds. Schema and archive-member verification were measured; full extraction, event counts, model convergence, and bootstrap runtime were not measured. Aggregation and multinomial models are expected CPU-feasible. The GRU is a bounded tabular sequence fit and may also be CPU-feasible; an allocated A100-SXM4-80GB is an optional acceleration if solver profiling shows repeated seeds/bootstraps exceed the envelope. Ordinary shell CUDA visibility is not evidence that GPUs are absent, and GPU use carries no scientific merit bonus.

The following branches remain explicitly deferred: a causal effect of delaying ICU transfer or adding ward monitoring (requires a target-trial protocol, treatment/intent data and confounding review); a persistent-lactate-only hypothesis (selective testing and incomplete microcirculation/treatment context); diuretic, kidney-recovery, sedation, antimicrobial, transfusion, and asynchronous recovery questions (missing indication, adjudication, or treatment timing); and external validation (no second hospital cohort is configured). Revisit only with the missing clinical evidence or a prespecified external/prospective design.

## Demonstration disposition and provenance

references/research-ambition/README.md and methods-and-compute.md were read. The natural-history and Bayesian demonstrations support considering a bounded longitudinal sequence comparison and explicit uncertainty, but their populations and methods are not reproduced. The cancer main paper and complete STAR Methods remain unavailable; only its publisher metadata and supplement are available, so no unavailable text is claimed. The demonstrations do not establish this ICU hypothesis.

The parent audit verified the MIMIC schema bindings and item IDs. In this episode, the MIMIC guide, full catalog pointers, relevant local schema JSONs, the exact read-only ZIP archive members, and the parent proposal/support were inspected. No patient-level rows were sent to public search. No scientific model was fitted and no event result is claimed during discovery.
