> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Residual instability before ICU-to-ward transfer: trajectory-state discordance test

Status: proposed substantive child of `[prior hypothesis]`. No outcome model has been fit and no discordance hypothesis result is claimed. This child preserves the frozen 49,157-transfer cohort, `t0`, final-24-hour strict decision-time inputs, raw 48-hour endpoint, adjudicated first-transition extension, pooled and temporal transport analyses, opening sequence, and exact source bindings. It adds a pre-specified test of whether recent direction changes risk and fixed-capacity ranking specifically when endpoint state and direction disagree.

## Scientific opening, evidence boundary, and advance

The parent tests average incremental trajectory information and its temporal/workflow transport. That average can be positive while being clinically uninformative: T1 might only amplify risk among transfers already concerning at the endpoint. The unresolved and more consequential question is whether history changes the ranking of apparently reassuring patients who are worsening, and apparently concerning patients who are improving.

The inspected evidence supports only bounded premises. A longitudinal MIMIC-IV/external-hospital model outperformed SWIFT for seven-day ICU readmission/death but explicitly left operational factors, DNR status, and distinct composite components unresolved [K1]. A systematic review found advantages for longitudinal models but wide variation in populations, windows, and outcomes [K2]. EHR timing and frequency encode healthcare process as well as patient state [K3]. The exact parent audit supports cohort and temporal feasibility; a new bounded support probe reproduced 49,157 transfers/2,607 adverse events and found adequate paired/current measurements in 46,935 transfers/2,277 events. Neither literature nor audit establishes trajectory gain, discordance-specific risk, physiology, safe transfer, or monitoring benefit.

**Frozen claims retained.** The pooled primary remains paired test-set `Brier(S0)-Brier(T1)` on the raw three-state outcome. The temporal parent still asks whether T1 and adjudicated R+D gain survive frozen early-fit/middle-calibration/late-test transport. This child cannot rescue an adverse parent result.

**New falsifiable hypothesis.** Conditional on endpoint-state risk at `t0`, recent measured-value worsening raises and recent improvement lowers 48-hour R+D risk; the resulting T1-versus-S0 risk shift and fixed-quota re-ranking are largest when endpoint state and direction oppose one another. This interaction must survive locked temporal transport, endpoint sensitivities, and value/process controls.

**Leading claim and strongest rival.** The leading bounded claim is that recent measured-value history contains residual prognostic information not represented by the current endpoint state. The rival is that apparent discordance is endpoint severity measured imperfectly, regression to the mean, irregular charting/store lag, clinician-triggered observation/treatment, treatment limitation, destination/service selection, or transfer-selection/opportunity artifact. Value-specific, temporally transported interaction evidence is compatible with residual patient-state information; it still does not identify physiology or mechanism.

**Clinical decision.** At `t0`, a ward/rapid-response team with fixed review capacity ranks transfers for review over 24/48 hours. The consequential outputs are patients entering or leaving the top 2%, 5%, and 10% R+D worklists when direction is added, plus observed R+D capture among those swaps. These are prioritization outputs, not proof that review, delayed transfer, or ICU retention is beneficial.

## Frozen population, time, endpoints, and analyses

Retain the parent exactly:

- first eligible adult ICU-to-frozen-general-ward transfer per hospitalization after ICU LOS at least 24 hours; `t0=icu/icustays.outtime`, exact successor `hosp/transfers.intime=t0`;
- frozen 17 destination values and step-down sensitivity;
- inputs only in `[t0-24h,t0)`; chart rows require both `charttime<t0` and `storetime<t0`; interval events require overlap and `storetime<t0`;
- parent S0/T1/O1, M0/M1 and L2 definitions, plausibility limits, item mappings, process strata, pooled seed-20260923 subject split, 2,000 subject-cluster bootstraps;
- raw adverse outcome: same-admission later ICU `intime` or `admissions.deathtime` in `(t0,t0+48h]`; raw live discharge/no-event classes unchanged; 2,607 adverse composites;
- adjudicated W→R, W→D, valid W→L and W first-transition analysis, administrative-discordance flag, 33 unresolved records, and all endpoint sensitivities;
- uncertainty-aware approximate-era roles, subject isolation, early development, middle validation, locked 2017–2019 test and separately opened 2020–2022 stress test;
- all destination, density, store-lag, O1, clock, service, endpoint, calibration and opening-order audits.

The new discordance test is additional. No subgroup is removed from the population and middle/undefined direction rows remain in the continuous primary interaction.

## Endpoint state, recent direction, and discordance—defined before test outcomes

### Endpoint-state severity C

Fit `E0`, a ridge multinomial endpoint model, under the same split/era protocol as S0. It contains S0 static context and measured endpoint state: age, sex, admission type, source/last ICU, destination, latest service, ICU LOS, prior ICU count, transfer clock, final valid HR/SBP/MAP/RR/SpO2/temperature/oxygen flow/FiO2/device value with four-hour freshness, final GCS components, ventilation, vasopressor, and code-status state. It excludes counts, distinct hours, recency except the endpoint freshness flag, missing-bin fractions, store lags, caregiver counts, persistence, runs, transitions, volatility, slopes, early-late differences, and worst historical values. Training medians and explicit missing flags remain because absent endpoint state must not be fabricated.

For each transfer, `C=logit(p_E0(R+D))`, using out-of-fold training predictions, frozen validation prediction, and untouched evaluation prediction. This avoids defining severity from outcomes or from T1.

### Recent measured-value direction G

Use six fixed two-hour bins in `[t0-12h,t0)`. For each parent domain—HR, BP, RR, SpO2, temperature, oxygen support—define an abnormality margin from the parent's fixed clinical normal bounds; positive is worse. Divide each margin by its development-set IQR. BP uses the worse standardized SBP/MAP margin. Oxygen uses the maximum of standardized FiO2, flow, and frozen device-ordinal margins; missing oxygen remains unknown.

For domain `j`, `G_j = median(margin)` in `[t0-6h,t0)` minus the median in `[t0-12h,t0-6h)`. Require at least two observed bins per half. Define `G=mean(G_j)` across at least four eligible domains. Positive means worsening; negative means improvement. All IQRs and the exact oxygen dictionary freeze in development without outcomes. Report channel directions and cancellation; no last-observation-carried-backward values are allowed.

This recent-direction definition is prospective and independent of the 48-hour outcome. It avoids deriving direction as `T1-S0`, which would make the explanatory variable model-dependent.

### Continuous primary interaction and communicative cells

The primary discordance estimand uses all rows with defined G: tensor-product restricted cubic splines for `C`, `G`, and their interaction, knots fixed at development 10th/50th/90th percentiles. Report standardized contrasts at the development 30th and 70th percentiles:

`I = [risk(C30,G70)-risk(C30,G30)] - [risk(C70,G70)-risk(C70,G30)]`.

Also report direction contrasts separately at `C30` and `C70`. This tests effect modification without arbitrary clinical subgroup cutoffs.

For worklist communication, freeze development-only distributional cells:

- reassuring/worsening: `C<=q30(C), G>=q70(G)`;
- concerning/improving: `C>=q70(C), G<=q30(G)`;
- reassuring/improving and concerning/worsening are concordant extremes;
- all other rows remain in the continuous analysis.

Quantiles are selected for symmetric state/direction boundaries, not outcome rates. Absolute parent abnormality cells are descriptive only. The support probe found reassuring+worsening 830/47 and concerning+improving 72/13 under literal absolute cutoffs, so those sparse extremes cannot be a symmetric primary claim and thresholds must not be altered to rescue them.

## Prefit support gates

Before any discordance outcome fit, freeze `C/G` transforms and thresholds from development, then publish counts with outcomes still sealed for the evaluation sets.

- direction coverage must be at least 70% in every evaluation era;
- pooled untouched test: each distributional discordant cell requires >=500 transfers and >=50 R+D events for a named-cell claim;
- combined 2017–2022 locked late-era union: each requires >=500 and >=50 events;
- each late era: >=300 and >=30 events; failure makes that era's cell interpretation inconclusive while retaining the continuous interaction;
- supported destination/density cell claims require >=500 transfers and >=50 events;
- if either pooled discordant cell fails, the experiment may report continuous effect modification but cannot claim both clinical discordance patterns;
- if G coverage is <70%, both continuous and categorical discordance claims are infeasible; report measurement failure rather than impute direction.

The support diagnostic is not a result: it used worst abnormal bins and a conservative oxygen regex. It only establishes that exact extraction is plausible.

## Baseline and scientifically substantive learned alternative

### D1: simple prespecified discordance model

Fit `E0`, then `D1=E0 + spline(G) + C×G` and the frozen cell indicators as a ridge multinomial model on the raw three-state target. Repeat a matched first-transition `DM1` using the parent six-hour adjudicated R+D/L model. Preprocessing and penalties use training/development; selection and calibration use validation/middle era only.

D1 reveals the sign and scale of recent direction at matched endpoint state and provides transparent cell-level risk shifts. It loses nonlinear order, cross-domain lag and opposing organ patterns.

### L2-D: matched learned value/process sequence alternative

Fit the parent's two-stream causal TCN on the same twelve two-hour final-24-hour bins, static E0 inputs, raw target, splits, temporal roles, five seeds, validation early stopping and temperature scaling:

- value stream: standardized observed/forward-filled values, no masks or gaps;
- process stream: masks, deltas, counts, strict decision-time store lag and caregiver counts, no measured values;
- static stream: E0 context;
- two causal convolution layers, kernel 3, dilations 1/2, 32 or 64 channels, dropout 0 or 0.2, Adam 1e-3 or 3e-4.

Mandatory heads are full, value+static, process+static, static-only. Mandatory falsifications are order permutation with final bin fixed and patient-value-sequence permutation within destination, E0 risk decile and development density quintile. For every head output, compute risk shift relative to E0 over continuous C/G and the frozen cells.

L2-D can detect nonlinear late relapse, cross-channel interactions and patterns hidden when G averages opposing domains. Select it only if calibrated, stable across seeds, and it beats D1 in both locked late eras while measured values—not process alone—account for the gain. Otherwise prefer D1. A latent/domain-adversarial alternative is deferred because no independent physiology, staffing, policy, or transfer-intent label can identify what its representation removed; revisit with an external site or observed policy change.

## Estimands, outputs, uncertainty, and falsification

Retain every parent pooled and temporal output. Add:

1. pooled and era-specific likelihood-ratio/deviance improvement for D1 over E0, paired Brier/log-loss differences, calibration, AUROC/AUPRC;
2. continuous interaction `I`, direction contrasts at C30/C70, and bootstrap confidence bands over a predeclared 5×5 C/G grid;
3. D1 versus E0 and L2-D versus E0 risk-shift distributions by cell;
4. at q=2%, 5%, 10%, worklist entrants/exits, R+D capture/PPV/sensitivity, net events gained per 1,000 reviewed, and Jaccard;
5. adjudicated R+D first-transition IBS and component R/D/L contrasts;
6. full/value/process/static heads and permutation contrasts;
7. all support, measurement cancellation, destination, density, store lag, O1 quintile, code-status, endpoint-adjudication and temporal outputs.

Use paired 2,000-replicate subject-cluster bootstraps. Cross-era contrasts resample subjects independently within era. Validation estimates are optimistic. The 2017–2019 result is frozen before 2020–2022 is opened. No p-value alone establishes materiality.

**Supportive bounded result:** parent pooled and transport gates pass; D1 improves raw Brier with a positive paired interval in pooled test and both late eras; the C30 worsening contrast is larger than the C70 contrast with the interaction interval excluding zero in the predeclared direction; at least one pooled supported discordant cell gains >=5 observed R+D events per 1,000 reviewed at a fixed quota without losing net capture overall; adjudicated R+D direction is concordant; full/value L2-D evidence is not reproduced by process-only or permutations. Claim only residual measured-value information and useful re-ranking.

**Adverse:** the interaction is opposite with interval excluding zero, D1 worsens Brier/IBS, re-ranking loses >=5 events/1,000 reviewed, endpoint sensitivities reverse direction, or value evidence disappears while process-only reproduces the shift. This rejects the specified discordance-based prioritization claim, not all longitudinal physiology.

**Endpoint sufficiency:** D1's pooled and both late-era 95% upper bounds exclude a 0.002 Brier gain and 2 extra R+D captures per 1,000 at every quota; continuous interaction bands exclude the prespecified material contrast. Prefer E0/S0.

**Simple adequacy:** D1 is supportive while L2-D's upper bound excludes an additional 0.002 Brier gain and 2 events/1,000 in both late eras. Prefer D1.

**Inconclusive:** intervals include material benefit and harm, G coverage/support gates fail, seeds are unstable, late-era calibration fails, endpoint sensitivities disagree, or one named cell is unsupported. An imprecise null is not falsification; unsupported literal threshold cells remain descriptive.

None of these outputs establishes mechanism, plannedness, safe transfer, preventability, or intervention benefit.

## Exact MIMIC-IV 3.1 data contract

Read-only archive: `[internal dataset path]`, [source checksum].

Physical members, catalog schemas and source headers were checked:

- `hosp/patients` / `mimic-iv-3.1/hosp/patients.csv.gz`: `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod`; subject join and era interval;
- `icu/icustays` / `mimic-iv-3.1/icu/icustays.csv.gz`: `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los`; `outtime=t0`, later `intime` is R;
- `hosp/transfers` / `mimic-iv-3.1/hosp/transfers.csv.gz`: `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime`; exact successor/destination;
- `hosp/admissions` / `mimic-iv-3.1/hosp/admissions.csv.gz`: `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,discharge_location,hospital_expire_flag`; target and endpoint gate;
- `hosp/services` / `mimic-iv-3.1/hosp/services.csv.gz`: `subject_id,hadm_id,transfertime,prev_service,curr_service`; latest `transfertime<=t0`;
- `icu/chartevents` / `mimic-iv-3.1/icu/chartevents.csv.gz`: `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning`; stay/item joins and strict availability;
- `icu/d_items` / `mimic-iv-3.1/icu/d_items.csv.gz`: `itemid,label,abbreviation,linksto,category,unitname,param_type`; fail on mapping mismatch;
- `icu/inputevents` / `mimic-iv-3.1/icu/inputevents.csv.gz`: identifiers, `starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,statusdescription`;
- `icu/procedureevents` / `mimic-iv-3.1/icu/procedureevents.csv.gz`: identifiers, `starttime,endtime,storetime,itemid,statusdescription`.

Frozen item IDs: HR 220045; SBP 220050/220179; MAP 220052/220181; RR 220210; SpO2 220277; temperature 223761/223762; O2 flow 223834; FiO2 223835; O2 device 226732; GCS 220739/223900/223901; code status 223758; ventilation 225792; vasopressors 221289/229617, 221662, 221749/229630/229631/229632, 221906, 222315.

Endpoint adjudication only: `[internal dataset path]` with `note_id,subject_id,hadm_id,note_type,note_seq,charttime,storetime,text`. Notes never enter predictors or automatic labels.

## Actual deliverable, compute, and verification boundary

The future solver must newly fit E0, D1/DM1, the retained parent models, and L2-D; mere feature extraction is incomplete. Required outputs:

- parent cohort, split, temporal-role, endpoint, process/workflow, model and opening manifests;
- `direction_features.parquet`, `direction_coverage.json`, `discordance_thresholds.json`, `discordance_support.json`;
- `discordance_predictions.parquet`, `discordance_grid.csv`, `interaction_metrics.json`;
- `worklist_swaps.parquet`, `quota_swap_metrics.json`, `transition_discordance_metrics.json`;
- `l2d_ablations.json`, seed/checkpoint/permutation manifests;
- `interpretation_axes.json` linking every conclusion to estimates, intervals and paths, and result-linked `conclusion.md`.

Measured discovery computation: exact support probe, 8 CPUs/64 GiB/no GPU, 759 seconds; no predictor fit. Estimated future budget: extraction 8 CPUs/64 GiB 2–4 h; ridge/event fits and bootstrap 8–16 CPUs/64–128 GiB 2–4 h; five-seed TCN one allocated A100 plus 8 CPUs/64 GiB 3–6 h; 5–8 h wall time with overlap. Estimates are unverified but fit the 16-CPU, 262,144-MiB, 8-GPU, 28,800-second planning envelope.

Automatically checkable: source hashes/headers, joins, cohort, times, leakage, G/C construction, support gates, fitting/splits, opening order, metrics, uncertainty and rule-consistent conclusions. Clinical adjudication is required for transfer intent, plannedness, device semantics, clinician concern, goals of care and apparent treatment response. Bed occupancy, staffing, ward monitoring, rapid-response availability, preventability, post-transfer actions, capacity cost/harms and external-site evidence are unavailable. External transport requires another institution; clinical benefit requires prospective or quasi-experimental evaluation.

## Exactly three rechecked key references

[K1] Heo Y, Kim M, Han SS, et al. *AI-Driven Predictions of Readmission and Mortality for Improved Discharge Decisions in Critical Care: A Retrospective Study.* Diagnostics. 2026;16(6):874. doi:10.3390/diagnostics16060874.

[K2] Ruppert MM, Loftus TJ, Small C, et al. *Predictive Modeling for Readmission to Intensive Care: A Systematic Review.* Crit Care Explor. 2023;5(1):e0848. doi:10.1097/CCE.0000000000000848.

[K3] Agniel D, Kohane IS, Weber GM. *Biases in electronic health record data due to processes within the healthcare system: retrospective observational study.* BMJ. 2018;361:k1479. doi:10.1136/bmj.k1479.

K1 bounds operational/component interpretation, K2 bounds longitudinal-model generalization, and K3 directly motivates the measurement-process rival. None establishes discordance, temporal transport, physiology or benefit. Attached excerpts and receipts are reused byte-for-byte; no new inspection is implied.
