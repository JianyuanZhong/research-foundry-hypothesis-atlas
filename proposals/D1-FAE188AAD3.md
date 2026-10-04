> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Observed creatinine/Foley recovery discordance at 72 hours — episode 8 executable successor

## Decision, unresolved claim and scientific deliverable

This proposal preserves the selected clinical question and repairs the repeated support-audit bottleneck. It is a new, noncausal MIMIC-IV prognostic analysis, not a reproduction of the expert seed or the cited paper.

The unresolved hypothesis is:

> Among adults in a first valid ICU stay who are alive and still in that ICU at 72 hours, have an observed early creatinine rise and documented early Foley oliguria, and have apparent creatinine recovery by 72 hours, those without recovery of densely observed Foley-recorded urine output have higher subsequent same-admission in-hospital mortality than those whose Foley-recorded output also recovers.

The clinical importance is that a falling creatinine can be interpreted as reassurance even when recorded urine output remains low. A reproducible observed association would motivate prospective validation of a discordant-recovery alert using cystatin C, measured GFR, muscle/volume assessment and complete urine capture. It would not show that low Foley output is true low GFR, that creatinine recovery causes harm, or that treatment should change.

The actual deliverable is newly fitted/estimated outputs, not a result envelope:

1. provenance.json, cohort_flow.csv, item_support.csv, and phenotype_outcomes.csv, including raw/valid/duplicate/storage-time counts and every support gate;
2. one frozen row per hospitalization's earliest valid ICU stay, with exact phenotype components and observability flags;
3. the primary discordant-versus-concordant post-landmark death risk difference and risk ratio with subject-clustered bootstrap 95% intervals, plus a prespecified standardized covariate-adjusted associational contrast;
4. first-event summaries for post-landmark RRT and later same-admission ICU readmission;
5. two newly fitted models on the same support-defined prediction population and subject-held-out split: a transparent ridge-logistic baseline and a six-hour nonlinear temporal model, with a urine/output ablation;
6. held-out discrimination, Brier score, calibration intercept/slope and grouped feature-family uncertainty;
7. source, threshold, density, storage-time, creatinine-source, early-RRT and timing-permutation falsifications, followed by an output-linked supportive, adverse or inconclusive classification.

No cohort count, event count, effect estimate or model metric is asserted here. The episode-7 parent records that the previous broad row-level audit ([research job]) was canceled after 912.3 seconds without an output. This successor changes the computation plan; it does not convert that cancellation into evidence.

## Evidence versus tested claim

The inspected local paper is Haines et al., “Comparison of Cystatin C and Creatinine in the Assessment of Measured Kidney Function during Critical Illness,” CJASN 2023, DOI 10.2215/CJN.0000000000000203, locally available at references/expert-seeds/papers/kidney-function/article.readable.txt and article.pdf. Its reported study enrolled 38 mechanically ventilated patients, measured creatinine, cystatin C, iohexol clearance and rectus-femoris muscle, and found creatinine-based kidney estimates could overestimate measured function during prolonged critical illness. That is evidence for a biologically plausible creatinine measurement concern in a selected study; it does not establish the prevalence, prognosis, completeness or mechanism of a Foley/creatinine discordance phenotype in MIMIC-IV.

The expert card references/expert-seeds/cards/mimic-03.md is explicitly an untested hypothesis and warns that measured kidney function is unavailable. The present experiment tests only an association between an observed chart phenotype and later observed outcome. Its strongest computable claim is a conditional prognostic association in the measured population. True GFR, muscle loss, volume status, catheter intent, KDIGO AKI and treatment effects require other data or clinical adjudication.

## Source, archive and exact bindings

Use the read-only source identified in datasets/mimic/README.md and datasets/mimic/metadata.json:

- path: [internal dataset path];
- snapshot: [source checksum];
- archive [source checksum];
- catalog [source checksum].

The executable must verify member names and catalog schema hashes before any measurement scan. It must not extract or modify the source archive. It must stream all rows in the required members (no row sampling), retain only whitelist item IDs and eligible keys, and write all manifests, filtered rows, features, fits and predictions to the workspace.

Required members, table IDs, columns and joins are:

- mimic-iv-3.1/icu/icustays.csv.gz, icu/icustays, schema datasets/mimic/table-7d5c8feb0fb0dbd4.json: subject_id, hadm_id, stay_id, first_careunit, last_careunit, intime, outtime, los.
- mimic-iv-3.1/hosp/admissions.csv.gz, hosp/admissions, schema table-e8ec3e6e4c428559.json: subject_id, hadm_id, admittime, dischtime, deathtime, admission_type, admission_location, discharge_location, insurance, language, marital_status, race, hospital_expire_flag.
- mimic-iv-3.1/hosp/patients.csv.gz, hosp/patients, schema table-9154f8c46cade9af.json: subject_id, gender, anchor_age.
- mimic-iv-3.1/icu/d_items.csv.gz, icu/d_items, schema table-d1023acc404fd1d4.json: itemid, label, linksto, category, unitname, param_type; used to verify item identity, table linkage and units.
- mimic-iv-3.1/hosp/d_labitems.csv.gz, hosp/d_labitems, schema table-57ae65f0eb6cf1a6.json: itemid, label, fluid, category; used to verify laboratory item identity.
- mimic-iv-3.1/hosp/labevents.csv.gz, hosp/labevents, schema table-bf701d962c63287c.json: labevent_id, subject_id, hadm_id, specimen_id, itemid, charttime, storetime, value, valuenum, valueuom; filter item IDs 50912 and 52546.
- mimic-iv-3.1/icu/chartevents.csv.gz, icu/chartevents, schema table-8208609a785ea7e8.json: subject_id, hadm_id, stay_id, charttime, storetime, itemid, value, valuenum, valueuom; filter item IDs 220615, 226512, 224639, 220181, 220045, 220210, 220277, 50813, 52442 and 53154.
- mimic-iv-3.1/icu/outputevents.csv.gz, icu/outputevents, schema table-a7ad1c4cdcdbfe0a.json: subject_id, hadm_id, stay_id, caregiver_id, charttime, storetime, itemid, value, valueuom; filter Foley item 226559.
- mimic-iv-3.1/icu/procedureevents.csv.gz, icu/procedureevents, schema table-f6493e8403a0abe7.json: subject_id, hadm_id, stay_id, caregiver_id, starttime, endtime, storetime, itemid, value, valueuom; filter RRT 225441, 225802, 225803, 225805, 225809, 225955 and ventilation 225792, 225794.

The dictionary audit must confirm the observed labels before fitting: 220615 is “Creatinine (serum)” linked to chartevents; 50912 and 52546 are “Creatinine” in hosp/d_labitems; 226559 is “Foley” linked to outputevents with unit mL; 226512 and 224639 are admission/daily weight with unit kg; and each vital/lactate/procedure item has the declared link and label. A missing member, unexpected schema, mismatched item label/link, or incompatible unit is a reproducibility failure and stops the scientific fit.

Join icustays to admissions on (subject_id, hadm_id) and to patients on subject_id, checking one-to-one expectations and rejecting cross-subject hadm_id matches. Join ICU measurements, output and procedures on stay_id while verifying matching (subject_id, hadm_id). Join hospital labs on (subject_id, hadm_id) and retain only records whose charttime lies within the selected ICU interval. diagnoses_icd and d_icd_diagnoses are available in the catalog but are not required inputs: omitting the retrospective CKD/ESRD proxy removes a nonessential scan and avoids presenting discharge-coded diagnoses as onset-timed covariates.

## Executable support-audit design

The support audit is a census, not a sampled probe.

Stage 0, bounded preflight (about 5 minutes): read the catalog JSON and all listed schema JSONs; verify archive hash if not already present in the run manifest; use zipinfo to verify the required members; read the two dictionaries and verify the exact item map. Emit a failed manifest rather than silently remapping.

Stage 1, small-table cohort construction (about 10 minutes): stream icustays, admissions and patients; parse only declared columns; sort stays within each (subject_id, hadm_id) by (intime, stay_id) and retain the earliest valid stay. Construct eligible identifiers and the exact interval [intime, outtime), without reading measurement files.

Stage 2, one sequential pass per required measurement member (the bounded repair): use a compiled streaming CSV reader or equivalent buffered reader over the ZIP member’s gzip stream. Test key membership before timestamp parsing and item membership before value conversion. For each retained row, store only the declared clinical fields and a source-row signature in a compact workspace file. Do not load a full 2.6–3.5 GB member into a dataframe. The three measurement members needed for the primary phenotype are labevents, chartevents and outputevents; procedureevents is a small separate pass for secondary RRT/ventilation flags. This avoids the parent’s full-row materialization bottleneck while still examining every source row that could affect the eligible population. Set hard per-member watchdogs and emit a checkpoint after each completed member; a timeout is inconclusive, never a reason to change the phenotype.

Stage 3, deterministic reduction: use clinical charttime for inclusion and relative windows; use starttime for procedures. For primary as-observed support, retain a measurement only when nonmissing storetime <= t0; report charttime-only and missing/late-storetime rows separately. Use strict half-open windows relative to intime: W0 [0,24h), W1 [24,48h), W2 [48,72h). Exact duplicate removal is performed before aggregation using all available measured identity/value/time fields while excluding caregiver/order/provider identifiers that represent recording provenance; duplicate counts and the signature rule are retained. At a shared clinical timestamp, use the prespecified median of valid creatinine values after exact duplicates, retain ICU-lab source indicators and a same-time disagreement flag, and never convert incompatible units or text values.

The audit must emit, for every flow gate, denominator, excluded count and reason: valid first ICU, adult, 72-hour ICU support, discharge/outcome support, primary storage-available creatinine support, Foley support, weight support, dense W0/W2 coverage, early observed oliguria, creatinine-rise/recovery cells, discordant/concordant cells, and death/RRT/readmission observability. It must also emit raw/valid/duplicate/late-storage counts by item and source, missingness and density distributions, and all phenotype cells—not only the two primary cells.

This plan uses no random row sampling. It makes the support audit finishable within the 7,200-second science budget by reducing the cohort before the large scans, doing one buffered pass per relevant member, filtering by item/key before expensive parsing, and persisting a compact checkpoint after each pass. A declared run may use at most 2 CPUs and 8 GiB RAM; the proposed census and fits are CPU-only and no GPU is required. If an implementation cannot meet the watchdog, it must report the completed stages and classify the scientific result inconclusive rather than substitute a smaller question.

## Population, landmark and phenotype

Unit: one row per hospitalization’s earliest valid ICU stay. Require:

- anchor_age >= 18;
- nonmissing valid intime < outtime;
- t0 = intime + 72 hours strictly before outtime;
- nonmissing dischtime > t0;
- no deathtime <= t0.

This conditions on being alive and remaining in the index ICU at the fixed landmark. Multiple hospitalizations may contribute rows, but all rows for a subject stay in one split and all bootstrap resamples cluster by subject_id. Deidentified timestamps preserve within-subject intervals; no cross-subject calendar comparison is made.

Creatinine: retain positive numeric values with audited valueuom compatible with mg/dL from item IDs 50912, 52546 and 220615. Require at least one primary-storage-available value in each window. Define C0=min(W0), C1=max(W1), Cpeak=max(W0 union W1), and Clate=min(W2). An observed early rise is C1 >= C0 + 0.3 mg/dL OR C1/C0 >= 1.5; apparent creatinine recovery is Clate <= Cpeak - 0.3 mg/dL OR Clate/Cpeak <= 0.75. Preserve the continuous values and both rule components. These are observed screens, not KDIGO AKI.

Foley output: retain nonnegative numeric values for item 226559 with audited mL unit. Remove exact duplicates, bin by relative chart hour, and sum recorded values per hour. Require in both W0 and W2 at least 18 distinct observed chart hours, first-to-last observed-hour span at least 20 hours, and maximum gap between observed hours no more than 4 hours. Divide recorded volume by the full 24-hour window and the W0 positive weight, not by observed hours. Require W0 recorded output <0.5 mL/kg/hour (early observed oliguria). W2 recovery is >=0.5 mL/kg/hour; W2 non-recovery is <0.5. A zero is observed zero; an absent hour is missing. Dense observation is an auditability gate, not proof of complete Foley capture.

Weight: use positive W0 item 226512, otherwise 224639, requiring charttime in W0 and storetime <= t0; if both are eligible at the same time, item 226512 has priority. Record weight source, timing and late/missing alternatives. Weight is used for primary normalization and is not evidence of stable volume status.

Primary groups, restricted to early rise + apparent creatinine recovery + weight support + dense W0/W2 Foley support + early observed oliguria, are:

- discordant: creatinine recovered and W2 Foley output did not recover;
- concordant: creatinine recovered and W2 Foley output recovered.

The audit also reports the four rise/recovery cells, lower-density support, no-early-oliguria, missing/late-weight and charttime-only versions. No creatinine-only fallback or alternate phenotype is authorized if paired support fails.

## Outcomes and estimands

Primary outcome: all-cause in-hospital death with t0 < deathtime <= dischtime. deathtime determines event timing; hospital_expire_flag is a consistency check. Report missing and impossible date fields and flag/deathtime discrepancies. If outcome fields cannot be reconciled, stop interpretation.

Primary estimand: within the support-defined survivor population, the observed difference and ratio in probability of death before discharge between discordant and concordant groups. Report unadjusted risks, risk difference and risk ratio with subject-clustered percentile bootstrap 95% intervals. Then report a prespecified standardized associational contrast from a ridge logistic model containing the group indicator and only pre-48-hour covariates: age, sex, first-careunit/admission context, W0 weight, C0/C1/rise severity, W0 Foley amount/coverage, and pre-48 summaries/counts/missingness for MAP, HR, RR, SpO2 and lactate. Do not adjust for W2 Foley, W2 density, Clate, post-t0 treatment or any outcome-derived variable. This standardization is descriptive adjustment, not a causal estimand.

Secondary descriptive outcomes: new RRT is the first qualifying procedureevents.starttime > t0 and < dischtime among item IDs 225441, 225802, 225803, 225805, 225809 and 225955; a procedure that began before t0 is not “new”. Later same-admission ICU readmission is a later ICU row for the same (subject_id, hadm_id) with later.intime > index.outtime and < dischtime. Report death, RRT and readmission as first observed events where timing is available, with discharge as censoring; report death-or-RRT and length of stay descriptively. These do not replace the primary mortality estimand.

## Matched baseline and substantive learned alternative

The method comparison asks a separate but linked scientific question: does the temporal pattern and observed urine-output channel add prognostic information beyond a transparent creatinine-centered risk summary? It is not used to rescue a null primary phenotype association.

Prediction population is frozen before group labeling: all primary-support stays with outcome observability, including both eventual phenotype groups. Target is post-t0 in-hospital death. Use one deterministic subject-level split: hash subject_id || “renal-discordance-episode8” with SHA-256; first 60 hash values for training, next 20 for validation, final 20 for locked test. All admissions of a subject share a partition. Select preprocessing and hyperparameters using training/validation only; read the test set once.

Baseline: ridge logistic regression, with one-hot categorical encoding and standardized continuous features, using age, sex, first-careunit/admission context, W0 weight, C0/C1/Cpeak/Clate and pre-48 physiology summaries, measurement counts and missingness. It excludes Foley values, Foley density, weight-normalized urine, and all other urine/fluid channels. It is transparent and tests whether observed output provides incremental information beyond the creatinine-centered summary. Fix a small prespecified lambda grid and select only by validation Brier score.

Alternative: CPU histogram gradient-boosted trees on six-hour bins over [0,72h), with identical rows, target, split and outcome. Features are last/mean/min/max, within-bin slope when defined, count and missingness for creatinine, Foley mL/hour, weight-normalized Foley mL/kg/hour, MAP, HR, RR, SpO2 and lactate, plus ventilation flags from procedure items 225792/225794 and pre-landmark RRT flags. The full alternative includes urine trajectory/density; the ablation removes Foley amount, normalized output and output-density features while retaining other features. This alternative can reveal persistence, timing, threshold nonlinearity and interactions that terminal creatinine summaries lose. Density-only features are separately evaluated as a process model.

A six-hour tree is selected over a sequence transformer, latent GP or mechanistic fluid-balance model for a scientific reason and a feasibility reason: the substantive uncertainty is whether temporal output information adds beyond creatinine, and this representation tests it with inspectable feature-family ablations. A mechanistic fluid model would require complete intake/output, volume status, catheter intent and treatment indication, none of which is available. A transformer/GP would add assumptions and resource cost without resolving that missing adjudication. Revisit those alternatives only if the support audit shows adequate events and the tree’s residual temporal structure is clinically motivated and materially unresolved. No method is preferred because of GPU use or complexity.

For each model report test AUROC, AUPRC, Brier score, calibration intercept/slope and 95% subject-cluster bootstrap intervals, plus grouped feature-family permutation or ablation summaries. Require at least 20 deaths and 20 non-deaths in both training and locked test and estimable calibration; otherwise the model comparison is inconclusive. A small score improvement alone is not a clinically meaningful success. The substantive result is whether urine/output features improve calibrated risk information consistently and whether that improvement survives the density/process controls.

## Falsification, uncertainty and decision rules

Prespecified checks are:

- repeat the phenotype with 18-hour coverage and with the primary denser gate; stratify by observed-hour density and maximum gap;
- primary storage-available versus charttime-only support;
- ICU-chart-only, hospital-lab-only and combined creatinine sources;
- absolute-only, relative-only and combined creatinine thresholds; 0.5 threshold sensitivity; unweighted mL/hour sensitivity;
- W0 weight versus latest eligible weight by t0;
- exclude any pre-t0 RRT;
- compare full, urine/output-ablated and density-only models;
- permute Foley timestamps within each stay while preserving values, counts and windows; and permute labels within prespecified support/creatinine strata as an implementation negative control.

Supportive classification requires: both primary cells meet the predeclared minimum of 50 stays and 10 deaths per cell; the adjusted and unadjusted mortality contrast is higher in discordant stays with a 95% interval excluding the null; direction is retained across dense/storage/source/threshold checks; density-only and timestamp-permutation checks do not explain the finding; and the matched temporal model shows reproducible, calibrated urine/output information beyond the baseline. This supports only a conditional observed prognostic signal.

Adverse classification is a precise null or reversal under adequately supported primary analysis, especially if it persists under dense storage-available support, or attenuation explained by source/coverage/process controls. A temporal model improvement without the prespecified discordant-versus-concordant mortality signal is adverse for the renal-discordance hypothesis, not a rescue.

Inconclusive classification applies to inadequate paired support or events, irreconcilable outcomes, differential observability not separable from phenotype, leakage, failed permutation implementation, unstable bootstrap/calibration, or failure of the declared resource/watchdog limits. Gates and thresholds cannot be relaxed after results are seen. A failed support gate is a feasibility result, not evidence that the hypothesis is false.

The verifier can check source hashes/member/schema/item bindings, join and time logic, de-duplication, flow counts, phenotype construction, model inputs/split/fits, uncertainty and whether each conclusion is linked to a reported output. It cannot adjudicate complete Foley capture, true GFR, muscle loss, volume status, catheter intent, treatment indication, causality, bedside utility, external validity or clinical actionability. Those require additional clinical data, expert review, prospective validation or another cohort.

## Provenance, limitations and branch decisions

This is an adaptation of the MIMIC expert seed mimic-03, not a reproduction. The seed’s core idea is retained; numerical cutoffs, support gates and model specifications are this proposal’s falsifiable design. Haines et al. provide related physiological evidence, not validation of this cohort or phenotype.

Unavailable or unadjudicated evidence includes cystatin C, measured GFR/iohexol clearance, serial muscle mass, volume status, complete urine capture, catheter placement/recording intent, reliable total intake, KDIGO adjudication, treatment indication, bedside utility and external validation. MIMIC notes, radiology text, images and waveforms are not needed for this structured experiment; images and raw waveforms are unavailable in the configured core snapshot. The other configured datasets remain directly accessible and read-only, but are not pooled into this MIMIC estimand.

The three research demonstrations were treated as methodological context only: Delphi supports the idea that dated trajectories can answer a different information question than snapshots, but UKB/Danish validation data are absent; ALADYNOULLI’s genetics-dependent analysis is not reproduced and a latent EHR model is deferred; Oncoformer’s full image/EHR experiment cannot be reproduced because images and complete main methods are unavailable, and its lab-only precedent does not replace the renal design. None establishes the present hypothesis.

The actual scientific selection is therefore: one newly estimated paired-support mortality association plus one newly fitted transparent-versus-temporal information comparison. The evidence that would justify revisiting the deferred branches is adequate event/support counts, clinically reviewed labels or an external cohort, and a residual uncertainty that the selected CPU tree demonstrably cannot represent.
