# Residual instability before ICU-to-ward transfer: coupling-resolved trajectory-state discordance

Status: proposed substantive child of `[prior hypothesis]`. No outcome model has been fit and no trajectory-discordance result is claimed. This child preserves the parent's frozen 49,157-transfer population, `t0`, outcomes, pooled subject split, approximate-era roles and opening order, exact source bindings, parent S0/T1 and M0/M1 analyses, endpoint state `C`, raw direction `G`, and the primary endpoint-state-by-direction question. It adds the smallest controls needed to decide whether the apparent interaction is more than mathematical coupling, regression to the mean, or treatment/measurement dynamics.

## Unresolved question and substantive advance

The strongest evidence currently supports only three premises. Longitudinal ICU-discharge models can outperform a snapshot score, but operational factors, treatment limitation and the components of a readmission/death composite remain unresolved [K1]. Across ICU-readmission studies, longitudinal predictors can improve performance, but populations, windows and outcomes vary and risk of bias is common [K2]. Observation timing and frequency can be more predictive than recorded values because EHR trajectories reflect healthcare processes [K3]. The parent's exact audits establish a 49,157-transfer cohort with 2,607 raw 48-hour ICU-return/death events, approximate-era support, and 46,935 transfers/2,277 events with a bounded paired/current measurement definition. They do not establish a trajectory effect.

The unresolved claim is: among transfers with the same measured endpoint state at `t0`, does an unusually worsening versus improving recent measured-value history change calibrated 48-hour ICU-return/death risk and fixed-capacity ranking, particularly when state and direction disagree?

The parent's raw `G` subtracts an earlier six-hour summary from a later six-hour summary, while `C` uses final values drawn largely from that later period. Even if a patient's latent state is constant, noisy endpoint values mechanically induce an apparent opposing prior direction: a high late value tends to follow a lower earlier value and vice versa. Treatment changes and clinician-triggered measurement can produce the same pattern. Adjustment for `C` does not by itself remove this coupling.

The substantive advance is therefore not another model. It is a falsifiable attribution gate:

1. residualize raw direction against endpoint levels and recorded treatment/measurement context without using the R+D label in the residual fit; the frozen cross-fitted E0 risk score remains an outcome-trained conditioning summary;
2. test a temporally disjoint direction ending four hours before the endpoint window;
3. compare the observed interaction with a within-patient, endpoint-fixed value-order null that preserves every patient's value multiset, final value, missingness schedule and process/treatment sequence but destroys pre-final temporal order.

A donor-history null was considered and rejected: another patient's earlier values would not preserve the recipient's latent severity, so observed-minus-donor differences could still be simple measurement-error correction. A positive parent interaction that fails the endpoint-fixed within-patient controls is not evidence of residual patient-state history. A signal that survives them supports only temporally ordered measured-value information beyond endpoint and recorded process context; it still does not establish physiology, treatment response, preventability, or benefit from altered transfer or monitoring.

Clinical relevance remains the frozen decision: at `t0`, a ward or rapid-response team with fixed review capacity ranks transfers for review over 24/48 hours. The decisive outputs remain who enters or leaves the top 2%, 5% and 10% worklists and how many observed R+D events are captured. They do not prove that acting on the list improves outcomes.

## Frozen design

Retain the parent exactly:

- first eligible adult ICU-to-frozen-general-ward transfer per hospitalization after ICU LOS at least 24 hours; `t0=icu/icustays.outtime` and exact successor `hosp/transfers.intime=t0`;
- all 17 frozen ward destinations and step-down sensitivity;
- predictors only in `[t0-24h,t0)`; chart rows require `charttime<t0` and `storetime<t0`; interval events require overlap and `storetime<t0`;
- pooled seed-20260923 subject split, 2,000 subject-cluster bootstrap replicates, and subject-isolated uncertainty-aware approximate-era development, middle calibration, locked 2017–2019 test, then separately opened 2020–2022 stress test;
- raw three-state outcome with same-admission later ICU `intime` or `admissions.deathtime` in `(t0,t0+48h]`; raw live-discharge/no-event classes and 2,607 R+D events;
- adjudicated W→R, W→D, valid W→L first-transition extension, administrative-discordance flag, 33 unresolved records, six-hour M0/M1 fitting and all endpoint sensitivities;
- parent S0/T1/O1, E0, D1/DM1 and two-stream L2-D definitions, item dictionaries, plausibility limits, calibration, destination/density/store-lag/process strata, and opening sequence;
- `C=logit(p_E0(R+D))` from outcome-cross-fitted training, frozen validation, and untouched evaluation predictions;
- raw `G`: mean standardized abnormality-margin change across at least four of HR, BP, RR, SpO2, temperature and oxygen support, comparing `[t0-12h,t0-6h)` with `[t0-6h,t0)`, with at least two observed two-hour bins per half;
- primary continuous tensor-spline `C×G` interaction, development 30/70 contrasts and support-gated communication cells. No outcome-responsive threshold or subgroup change is allowed.

The child cannot rescue an adverse S0/T1 result, an adverse raw D1 result, failed direction coverage, unsupported cells, endpoint disagreement, or failed temporal transport.

## Coupling-resolved estimands

### 1. Outcome-blind conditional residual direction G-perp

For each row with defined raw `G`, construct `Z` only from information available before `t0`:

- the six domain-specific endpoint abnormality margins used by E0, their freshness/missing flags and `C`;
- destination, latest service, ICU source, transfer clock and ICU LOS;
- per-half observed-bin counts, distinct observed hours, median/max store lag and caregiver count;
- frozen ventilation, vasopressor and oxygen device/FiO2/flow transition flags in `[t0-12h,t0)`, including start, stop, escalation, de-escalation and no recorded change.

Fit `m(Z)=E(G|Z)` without exposing R+D labels to this nuisance regression. Because `Z` includes the frozen cross-fitted E0 score `C`, this is not globally outcome-free; it is an outcome-blind direction residual conditional on the already-prespecified endpoint-risk summary. Compare a ridge additive model with a depth-3 histogram gradient-boosted regressor; choose by subject-grouped development cross-validation RMSE, not by R+D association. Use out-of-fold nuisance predictions for development and one frozen development fit for every later set. Define

`G_perp = (G - m_hat(Z)) / SD_development(G - m_hat(Z))`.

Positive `G_perp` means worsening more than expected among transfers with the same measured endpoint, observation pattern and recorded support dynamics. Report residual correlation and calibration against every `Z` block. The orthogonalization gate passes only if, in validation and each evaluation era, absolute standardized linear slope of `G_perp` on the nuisance prediction is <0.05, absolute Spearman correlation of `G_perp` with `C` is <0.05, and no endpoint/process block explains more than 1% additional residual variance. Failure is an inconclusive nuisance-model result, not evidence against the clinical hypothesis.

Fit `D1-perp = E0 + spline(G_perp) + C×G_perp` with the same multinomial target, ridge protocol and calibration as D1. Report the same interaction contrast, grid, cells and quota swaps, using `G_perp` development 30/70 cut points. These cells are sensitivity labels; the parent's raw-G cells remain the named clinical communication cells.

### 2. Temporally disjoint direction G-pre

Using the same two-hour bins and abnormality functions, define per-domain

`G_pre,j = median([t0-8h,t0-4h)) - median([t0-12h,t0-8h))`.

Require both two-hour bins in each four-hour half and at least four eligible domains; average as for `G`. Endpoint values for the matched check are restricted to `[t0-4h,t0)`, so no chart row contributes to both `G_pre` and endpoint state. The half-open boundary assigns a record at exactly `t0-4h` to the endpoint window. Fit `D1-pre = E0-4 + spline(G_pre) + C-4×G_pre`, where E0-4 is the same E0 specification but only endpoint values observed in the final four hours; no population, landmark, outcome or split changes.

This is a timing-disjoint corroboration, not a replacement primary. Absence of a G-pre effect alone is inconclusive because a true final-four-hour change could be clinically relevant. Concordant G-pre evidence makes shared-row coupling implausible.

### 3. Coupling-preserving endpoint-fixed value-order null

Within each patient/domain's six two-hour bins in `[t0-12h,t0)`, freeze the final observed bin and its value. For each of 200 predeclared seeds, randomly permute the remaining observed abnormality-margin bin summaries only among that same patient's remaining observed bin positions. Missing positions, observation counts, chart/store times, caregiver identities, all process/treatment sequences, the final value, `C`, outcome, split and era role remain unchanged. Values never cross patients or domains. Recompute `G_perm` with the same eligibility rule; because values move only among already observed positions, coverage and missingness are identical.

This null preserves latent patient level as represented by the complete 12-hour bin-summary multiset, repeated-measure reliability, endpoint sharing, the algebraic late-minus-early construction, observation intensity and recorded treatment context. It destroys only whether the patient's pre-final values occurred in their observed order. Refit D1 with the parent's frozen hyperparameter-selection protocol inside each permuted training set and evaluate on the corresponding permutation of each evaluation set. Produce null distributions for the C×G interaction, Brier gain and quota capture. The prespecified attribution contrasts are observed minus median-null, with subject-cluster bootstrap intervals; permutation tail areas are secondary and never sufficient alone.

A secondary exact time-reversal control reverses the five nonfinal bin positions rather than randomizing them. A genuine ordered worsening pattern should materially attenuate or oppose the observed interaction, whereas an endpoint-coupling effect should persist. If fewer than 70% of G-eligible rows have at least three movable nonfinal observed bins across four domains, the order attribution is inconclusive; it must not be replaced by cross-patient borrowing.

## Treatment and measurement interpretation

The residualization and endpoint-fixed order controls address recorded treatment/measurement dynamics, but conditioning on treatment can remove genuine response information and cannot identify a biological mechanism. Therefore report, without changing the primary cohort:

- no-recorded-support-change sensitivity: no ventilation, vasopressor, oxygen-device, FiO2 or flow start/stop/escalation/de-escalation in `[t0-12h,t0)`;
- observation-stable sensitivity: every eligible domain has the same number of observed two-hour bins in both halves and median store-lag change is within the development IQR;
- active-treatment and observation-change strata separately;
- parent O1, process-only L2-D head, value-only head and endpoint-fixed order ablations.

Persistence in the quiet/observation-stable rows argues against abrupt recorded treatment or charting changes. Confinement to active-treatment rows supports only a treatment-associated predictive pattern. It cannot show whether treatment caused improvement, whether a clinician anticipated deterioration, or whether transfer was safe.

## Transparent baseline and learned alternative at matched specificity

The transparent scientific baseline is D1-perp, alongside frozen E0 and raw D1. It estimates the direction and size of unusual recent change at a matched endpoint and exposes the exact C×direction contrast. The additive nuisance model is preferred if it satisfies orthogonality; the boosted nuisance model is used only if it materially reduces held-out RMSE and passes the same balance gates. The nuisance model is not judged by outcome prediction.

The substantive learned alternative remains L2-D: the parent's two-stream causal TCN over the same 12 two-hour bins, static E0 context, five seeds, validation early stopping and temperature scaling. It can reveal nonlinear late relapse, cross-domain lag and opposing organ patterns that scalar `G_perp` loses. Apply the same within-patient endpoint-fixed value permutations to the value stream while retaining each patient's final bin, missingness and entire process stream; also retain the frozen full, value+static, process+static and static-only heads.

Select L2-D over D1-perp only if it is calibrated and seed-stable, beats D1-perp in both locked late eras, and its full/value gain and discordance shift exceed both process-only and endpoint-fixed order nulls. Otherwise prefer D1-perp. A latent-state or domain-adversarial model remains deferred: without an independent physiologic sensor, policy environment or transfer-intent label it cannot identify what was removed. Revisit it only with an external site or observed policy change.

Approximate future resources remain within the configured 16 CPUs, 262,144 MiB, 8 GPUs and 28,800 seconds: outcome-blind conditional nuisance fits, 200 ridge permutation refits and bootstraps add an estimated 8–16 CPUs/64–128 GiB for 1–2 hours; existing extraction/ridge/event work remains 2–4 hours; five-seed TCN work remains one allocated A100 plus 8 CPUs/64 GiB for 3–6 hours. These are unverified planning estimates. The inherited 759-second CPU support probe is measured; no new fit or GPU probe was needed for this design revision.

## Outputs, uncertainty and decision rules

Retain every parent output. Add:

- `orthogonalization_manifest.json`, nuisance cross-validation and balance tables;
- `direction_features.parquet` with raw G, G-perp and G-pre;
- `prewindow_coverage.json` and overlap assertion proving no row feeds both G-pre and E0-4 endpoint state;
- `order_permutation_manifest.json`, movable-bin coverage, seeds and 200 null metric files;
- `coupling_contrasts.json` for observed-minus-permutation interaction, Brier and quota capture;
- quiet/active-treatment and observation-stable/change sensitivity tables;
- L2-D endpoint-fixed order ablations;
- updated `interpretation_axes.json` and result-linked `conclusion.md`.

Use paired 2,000-replicate subject-cluster bootstraps. Cross-era comparisons resample independently by era. Freeze all nuisance choices, order-permutation seeds and G-perp/G-pre cut points in development; lock 2017–2019 before opening 2020–2022.

A **coupling-resolved supportive result** requires the frozen parent support conditions plus all of the following:

1. raw D1 is supportive under the parent's Brier, interaction, worklist, endpoint and transport rules;
2. D1-perp interaction has the same prespecified sign, with a 95% interval excluding zero in pooled test and both locked late eras, and adjudicated R+D is concordant;
3. observed-minus-median-order-null interaction and Brier gain have positive paired 95% intervals, and observed fixed-quota capture exceeds the order null by at least 2 R+D events per 1,000 reviewed at one parent-supported quota without worsening overall capture; the time-reversal interaction is opposite in sign or materially attenuated;
4. either G-pre is directionally concordant with an interval excluding zero in the pooled test, or the raw and G-perp signals persist in the no-support-change and observation-stable sensitivities;
5. L2-D value/full evidence, if claimed, is not reproduced by its process-only or endpoint-fixed permuted histories.

This supports residual measured-value history and consequential re-ranking beyond measured endpoint/coupling context. It does not establish physiology or benefit.

A **coupling/mean-reversion adverse result** occurs if raw D1 appears supportive but the endpoint-fixed order null reproduces it: the 95% upper bound for observed-minus-null Brier gain is <0.002, the interaction difference includes or favors zero, the time-reversal interaction does not reverse or attenuate, and the upper bound for quota-capture advantage is <2 events per 1,000 at every quota. If D1-perp is also null with an upper bound excluding the parent's material interaction/capture thresholds, interpret the raw interaction as adequately explained by unordered repeated values plus endpoint coupling under this design. Do not rescue it with L2-D.

A **treatment/measurement-dynamics adverse result** occurs if the signal is absent or reversed in both quiet and observation-stable sensitivities while process-only or active-treatment patterns reproduce the observed re-ranking. Claim a treatment/documentation-associated predictor only; reject residual-instability attribution.

An **endpoint-sufficiency result** retains the parent's rule: pooled and both late-era upper bounds exclude 0.002 Brier gain and 2 additional captures per 1,000 at every quota. Prefer E0/S0.

The result is **inconclusive** if G-perp balance or movable-bin gates fail, G-pre coverage is <70% in an evaluation era, intervals include material benefit and harm, raw and orthogonalized directions disagree without a valid null explanation, one late era fails calibration/support, endpoint sensitivities disagree, or learned seeds are unstable. G-pre null alone is not refutation. No subgroup, window or permutation rule may be changed after opening outcomes.

## Exact MIMIC-IV 3.1 bindings

Read-only archive: `[internal dataset path]`, [source checksum].

Catalog schemas were rechecked for the new controls; the parent's frozen physical-header verification is retained:

- `icu/chartevents` / `mimic-iv-3.1/icu/chartevents.csv.gz`: `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; joins on `stay_id` and `itemid`; bins use `charttime`, availability also requires `storetime<t0`;
- `icu/d_items` / `mimic-iv-3.1/icu/d_items.csv.gz`: `itemid,label,abbreviation,linksto,category,unitname,param_type`; fail on mapping mismatch;
- `icu/inputevents` / `mimic-iv-3.1/icu/inputevents.csv.gz`: identifiers plus `starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,statusdescription`; treatment-transition context uses overlap with the frozen window and `storetime<t0`;
- `icu/procedureevents` / `mimic-iv-3.1/icu/procedureevents.csv.gz`: identifiers plus `starttime,endtime,storetime,itemid,statusdescription`;
- `icu/icustays` / `mimic-iv-3.1/icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; `outtime=t0`, later same-admission `intime` defines R;
- `hosp/transfers` / `mimic-iv-3.1/hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; exact successor and destination;
- `hosp/admissions` / `mimic-iv-3.1/hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`; outcome, D, valid L and endpoint gate;
- `hosp/services` / `mimic-iv-3.1/hosp/services.csv.gz`: `subject_id,hadm_id,transfertime,prev_service,curr_service`; latest `transfertime<=t0`;
- `hosp/patients` / `mimic-iv-3.1/hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; subject join and approximate-era interval.

Frozen item IDs remain: HR 220045; SBP 220050/220179; MAP 220052/220181; RR 220210; SpO2 220277; temperature 223761/223762; oxygen flow 223834; FiO2 223835; oxygen device 226732; GCS 220739/223900/223901; code status 223758; ventilation 225792; vasopressors 221289/229617, 221662, 221749/229630/229631/229632, 221906, 222315.

Endpoint adjudication only uses `[internal dataset path]` with `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`. Notes never enter predictors, residualization, order permutations or automatic labels.

## Verification and limits

Computationally checkable claims are source hashes/headers, joins, cohort and times, strict availability, nonoverlap of G-pre and endpoint windows, outcome-blind conditional nuisance fitting, subject/split isolation, residual balance, within-patient/domain endpoint-fixed permutations, refits, opening order, metrics, bootstraps and conclusion-rule linkage.

Automatic verification cannot establish latent physiology, clinician intent, plannedness, treatment response, device semantics, goals of care, bed pressure, staffing, ward monitoring, preventability, actionability, harms or intervention benefit. Expert review is required for clinical meaning of support changes and selected records. External transport requires another institution. Monitoring or transfer benefit requires a prospective or quasi-experimental study with workload, uptake and harms.

## Exactly three inspected key references

[K1] Heo Y, Kim M, Han SS, et al. *AI-Driven Predictions of Readmission and Mortality for Improved Discharge Decisions in Critical Care: A Retrospective Study.* Diagnostics. 2026;16(6):874. doi:10.3390/diagnostics16060874.

[K2] Ruppert MM, Loftus TJ, Small C, et al. *Predictive Modeling for Readmission to Intensive Care: A Systematic Review.* Crit Care Explor. 2023;5(1):e0848. doi:10.1097/CCE.0000000000000848.

[K3] Agniel D, Kohane IS, Weber GM. *Biases in electronic health record data due to processes within the healthcare system: retrospective observational study.* BMJ. 2018;361:k1479. doi:10.1136/bmj.k1479.

The attached excerpts were re-inspected and their inherited hashes verified. K1 establishes relevance while bounding operational/DNR/composite interpretation; K2 bounds longitudinal-model generalization; K3 directly motivates the healthcare-process rival. None establishes the proposed coupling-resolved interaction, transport, mechanism or benefit.
