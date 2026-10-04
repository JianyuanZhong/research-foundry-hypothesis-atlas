# Context robustness of lactate-by-perfusion prioritization at the first eligible live ICU exit

## Status and actual scientific deliverable

This is a substantive successor to assigned valid parent `[prior hypothesis]`. It develops imported MIMIC expert seed `[starting question]` (`[prior hypothesis]`), “Residual instability before ICU discharge.” The seed is an untested hypothesis, not evidence. The parent’s first eligible live-exit selection, one-hour buffer, 12-hour dual clinical/recording-time feature window, persistent-lactate-by-measured-perfusion phenotype, competing R/D/S/N/U endpoint, support/coverage rules, fixed 5/10/20% queues, uncertainty and noncausal boundaries remain unchanged.

The actual new deliverable is a prespecified context-heterogeneity test:

> Among adults at the first eligible live ICU exit with complete parent coverage and adequate observation of the final six hours, does the parent’s phenotype add the same fixed-capacity held-out capture of the first 48-hour record-defined ICU return or timed in-hospital death in exits with versus without residual oxygen/vital-sign instability?

The primary estimand is the difference in within-context incremental 10%-queue capture:
`Psi10 = [Cap10(Bdisc|residual-instability)-Cap10(B1|residual-instability)] - [Cap10(Bdisc|stable)-Cap10(B1|stable)]`.
A 95% interval wholly outside the prespecified null region [-0.05,+0.05] with `|Psi10| >= 0.05` is a clinically meaningful context shift. The 5% and 20% within-context queues are fixed sensitivities. Bctx tests whether explicitly modeling the context adds value beyond the unchanged parent Bdisc; M2 tests whether ordered fluctuation adds information beyond transparent summaries. The future Harbor solver must newly fit the models, produce held-out predictions, competing-risk CIFs, queue tables, uncertainty, and audits—or a complete prespecified non-estimability report. No fitted result is claimed.

## Evidence, unresolved claim and clinical importance

The strongest available evidence is design-level: the local MIMIC-IV 3.1 snapshot contains ICU boundaries, repeated lactate/vital/oxygen observations, vasoactive and support-process records, admission death/discharge fields and transfer intervals. The inspected dictionaries identify the item meanings and links below. This establishes data availability and field semantics, not prevalence, proxy validity, event support, queue value, clinical appropriateness or benefit.

The imported seed asserts that residual high oxygen requirements or fluctuating vital signs before ICU discharge may identify patients who return to the ICU or die. The parent asserts an untested lactate-by-measured-perfusion interaction and fixed-capacity queue gain. The unresolved claim here is narrower: the parent’s incremental retrospective prioritization gain differs across a clinically meaningful, prespecified residual-instability context, and is not merely a documentation-intensity artifact.

This matters because a transition-review service has finite capacity. A stable gain across contexts would strengthen the parent’s internal robustness; a gain confined to residual instability would identify the population for prospective silent-mode evaluation; disappearance of the gain would limit promotion of a pooled phenotype. None of these results estimates a treatment, discharge-delay, oxygen, fluid or review effect. A positive result requires clinical adjudication, prospective silent-mode validation and an external hospital study before care use.

## Population and temporal validity

Use only MIMIC-IV for the primary experiment. The HCC, eICU and UK Biobank datasets remain directly available read-only, including rows and notes, but are not mixed into this population.

For each `hadm_id`, sort `icu/icustays` by `(outtime,intime,stay_id)` and select the first row meeting all parent rules: finite `intime<outtime`; valid adult `hosp/patients` join with `anchor_age >=18`; valid `hosp/admissions` join; known live exit at `t0=outtime` (either `deathtime` is null and `hospital_expire_flag=0`, or `deathtime>t0`); and `t0-intime >=13 hours`. Selection occurs before feature construction, coverage, context, endpoints, fitting or outcomes. Never substitute a later ICU stay after failure.

Set `tL=t0-1 hour`. Parent features use exactly `[t0-13h,t0-1h]=[tL-12h,tL]`, with early `[tL-12h,tL-6h)` and late `[tL-6h,tL]`. Point records require valid `charttime<=tL` and `storetime<=tL`; intervals require finite `starttime<endtime`, clinical overlap and `storetime<=tL`. A charted-before-but-stored-after record is delayed and excluded. No post-`tL` clinical event, `outtime`, `last_careunit`, discharge/death field, `dod`, note or future row is a feature. `outtime` is only the index boundary.

The parent phenotype and endpoint are copied exactly: persistent lactate P uses item 50813 medians >=2.0 mmol/L in both six-hour halves; NL is both defined with at least one below 2.0; improving perfusion I requires late-minus-early MAP >=5 mmHg and no greater late target-pressor duration; worsening W requires MAP <=-5 and no smaller late target-pressor duration; other cases are indeterminate. The endpoint window is `(t0,t0+48h]): R is the first later same-admission ICU stay, new target-pressor interval, or new verified support-procedure interval; D is timed in-hospital death; S is an earlier alive hospital discharge; N is known event-free follow-up; U is unresolved ascertainment. Ties use D before R before S, are recorded, and are not overwritten. S competes with R/D; U is never imputed into N. Report favorable/adverse U bounds exactly as in the parent.

## New residual-instability context

Define `W6=[t0-7h,t0-1h]=[tL-6h,tL]` in six one-hour bins, left-closed/right-open except the final bin closed at `tL`. Context status is determined before labels, fitting, queue ranking and test inspection.

Use core numeric channels HR, MAP, RR and SpO2; oxygen/support channels FiO2, O2 flow, additional-cannula flow, PEEP, and active invasive/non-invasive ventilation procedures. A bin is core-observed only with at least two accepted dual-time core numeric channels. Require at least four of six bins to be core-observed and at least two of the final three bins to have accepted oxygen/support evidence (FiO2, either flow, PEEP, or a verified procedure interval). Otherwise assign context-observation indeterminate; retain it in the all-candidate flow and process diagnostics, but do not call it stable.

Abnormality uses fixed operational rules: HR <50 or >120 bpm; MAP <65 mmHg; RR <8 or >24 insp/min; SpO2 <92%; FiO2 >=0.40 after converting values >1.5 from percent to fraction; O2 flow >=4 L/min; PEEP >5 cmH2O; or active invasive/non-invasive ventilation. Temperature is a prespecified secondary channel (30–43 C after Fahrenheit conversion) and does not define the primary context. A core-bin abnormal fraction is the proportion of observed core channels abnormal; oxygen/support abnormality is retained separately. No missing oxygen row is coded as room air or no support.

Residual-instability status requires the core/oxygen observation rules above and is present if any of: (a) at least two of the final three bins have an abnormal core fraction >=0.50; (b) mean abnormal core fraction across observed bins >=0.50; or (c) an invasive/non-invasive ventilation or target-pressor interval overlaps either final two bins. Stable status requires the same observation rules, no primary abnormality in the final three bins, no mean abnormal fraction >=0.50, and no such ventilation/pressor overlap in the final two bins. All remaining cases are context-observation indeterminate, including conflicting or invalid timing. The only context sensitivity changes (a) to at least one of the final three bins; it cannot replace the primary rule. This is a record-defined context, not an adjudicated oxygen requirement, physiologic stability or discharge readiness state.

## Exact source bindings

The full catalog is read-only at `[internal dataset path]`, [source checksum]. The structured MIMIC source is read-only at `[internal dataset path]`, 10,551,747,784 bytes, [source checksum]; snapshot `[source checksum]`.

| purpose | catalog table / exact archive member | join key | time fields | required columns |
|---|---|---|---|---|
| index/exits | `icu/icustays` / `mimic-iv-3.1/icu/icustays.csv.gz` | `subject_id,hadm_id,stay_id` | `intime,outtime` | `subject_id,hadm_id,stay_id,first_careunit,last_careunit,intime,outtime,los` |
| eligibility/death/discharge | `hosp/admissions` / `mimic-iv-3.1/hosp/admissions.csv.gz` | `subject_id,hadm_id` | `admittime,dischtime,deathtime,edregtime,edouttime` | `subject_id,hadm_id,admittime,dischtime,deathtime,admission_type,admit_provider_id,admission_location,discharge_location,insurance,language,marital_status,race,edregtime,edouttime,hospital_expire_flag` |
| demographics | `hosp/patients` / `mimic-iv-3.1/hosp/patients.csv.gz` | `subject_id` | `dod` prohibited as feature | `subject_id,gender,anchor_age,anchor_year,anchor_year_group,dod` |
| vitals/oxygen | `icu/chartevents` / `mimic-iv-3.1/icu/chartevents.csv.gz` | `stay_id` | `charttime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valuenum,valueuom,warning` |
| vasoactive intervals | `icu/inputevents` / `mimic-iv-3.1/icu/inputevents.csv.gz` | `stay_id` | `starttime,endtime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,amount,amountuom,rate,rateuom,orderid,linkorderid,ordercategoryname,secondaryordercategoryname,ordercomponenttypedescription,ordercategorydescription,patientweight,totalamount,totalamountuom,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate` |
| support intervals | `icu/procedureevents` / `mimic-iv-3.1/icu/procedureevents.csv.gz` | `stay_id` | `starttime,endtime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,starttime,endtime,storetime,itemid,value,valueuom,location,locationcategory,orderid,linkorderid,ordercategoryname,ordercategorydescription,patientweight,isopenbag,continueinnextdept,statusdescription,originalamount,originalrate` |
| Foley process sensitivity | `icu/outputevents` / `mimic-iv-3.1/icu/outputevents.csv.gz` | `stay_id` | `charttime,storetime` | `subject_id,hadm_id,stay_id,caregiver_id,charttime,storetime,itemid,value,valueuom` |
| lactate/organ features | `hosp/labevents` / `mimic-iv-3.1/hosp/labevents.csv.gz` | `subject_id,hadm_id` | `charttime,storetime` | `labevent_id,subject_id,hadm_id,specimen_id,itemid,order_provider_id,charttime,storetime,value,valuenum,valueuom,ref_range_lower,ref_range_upper,flag,priority,comments` |
| transfer audit | `hosp/transfers` / `mimic-iv-3.1/hosp/transfers.csv.gz` | `subject_id,hadm_id` | `intime,outtime` | `subject_id,hadm_id,transfer_id,eventtype,careunit,intime,outtime` |
| dictionaries | `icu/d_items`, `hosp/d_labitems` / respective `mimic-iv-3.1/icu/d_items.csv.gz`, `mimic-iv-3.1/hosp/d_labitems.csv.gz` | `itemid` | none | ICU: `itemid,label,abbreviation,linksto,category,unitname,param_type,lownormalvalue,highnormalvalue`; lab: `itemid,label,fluid,category` |

Verified ICU dictionary items are HR 220045; MAP 220052/220181/225312; RR 220210; SpO2 220277; temperature 223761/223762; O2 flow 223834 and 227287; FiO2 223835; PEEP 220339/224700; Foley 226559; target vasoactives 221906, 222315, 221289, 229617, 221749, 229630, 229631, 229632, 221662, 221653 and 221986; and support procedures 224385, 225792, 225794, 225441, 225802, 225803, 225805, 225809 and 225955. Verified lab items are lactate 50813; ALT 50861; AST 50878; bilirubin 50885; creatinine 50912; bicarbonate 50882; hemoglobin 51222; platelets 51265; WBC 51300. Dictionary links and units must be rerun as a solver readiness check.

For point values use finite `valuenum`, `valueuom), and fixed ranges HR 20–250, MAP 20–200, RR 2–80, SpO2 50–100, temperature 30–43 C, O2 flow 0–100 L/min, PEEP 0–40 cmH2O. Convert Fahrenheit to Celsius; convert FiO2 >1.5 by 100, then retain 0.21–1.00. Collapse selected MAP items within `(stay_id,charttime)` by median and record source counts. For intervals require valid clinical times, `storetime<=tL`, exact-duplicate collapse on available identity fields and clipped union duration. Never turn absence of pressor/procedure/oxygen rows into zero support without a process flag. The parent’s lactate/MAP/pressor and organ cleaning remains unchanged.

## Estimands and gates

Use the parent’s held-out predictions from unchanged B1 and Bdisc. For context z in {stable, residual-instability}, `Q_w(M,z)` is exactly `ceil(w*n_z,test)` subjects within z, ranked by predicted 48-hour CIF for A=R/D, with deterministic descending score then `subject_id,hadm_id,stay_id` ties. `Cap_w(M,z)` is the proportion of known A events among the queue; report also event sensitivity (# A events captured / # A events in that context), PPV, false negatives and R/D-specific capture. `G_w(z)=Cap_w(Bdisc,z)-Cap_w(B1,z)`; `Psi_w=G_w(residual-instability)-G_w(stable)`. The primary is `Psi10); report `Psi5`, `Psi20), pooled parent gains, and random-allocation benchmarks. The fixed queue remains a retrospective benchmark, not an intervention policy.

B1 and Bdisc are not changed from the parent. The new context-aware transparent model Bctx adds the frozen context indicator, continuous final-six-hour abnormal burden, final-three-bin persistence and pre-specified context-by-parent-phenotype interactions. The context is not used to refit B1/Bdisc by subgroup. A context-specific gain is not evidence for biology if it is reproduced by process-only features.

Before fitting, require parent G_cov/G_sup and: at least 40 stable and 40 residual-instability subjects, at least 10 known A events in each complete gated context, at least 8 subjects and 3 known A events in each held-out test context, and U <=20% per context. The global 10% queue gate remains at least 90 pooled test subjects, 10 known A events, queue size at least 10 and U <=10%. Context-observation-indeterminate cases are not reassigned. If any gate fails, the affected estimand is inconclusive.

## Matched baseline and substantive learned alternative

All models use the same selected exits, endpoint, subject-level 70/15/15 split, test set, dual-time convention, competing-risk target, calibration and bootstrap.

- B1: unchanged parent transparent order-blind longitudinal-history cause-specific model.
- Bdisc: unchanged parent phenotype-augmented transparent model; its within-context gain over B1 is the primary robustness quantity.
- Bctx: Bdisc plus residual-instability burden and frozen context interactions; it asks whether explicitly modeling the context adds incremental fixed-capacity capture beyond the parent.
- M2: a small masked one-layer GRU (hidden size 32, fixed regularization) over the same 12 one-hour bins, with raw cleaned parent channels, oxygen/vital/support channels, missingness masks, observation counts, parent phenotype flags and context flags. It predicts the same R/D/S hazards and is evaluated on exactly the same test subjects and queues. It can reveal ordered fluctuation or nonlinear coupling lost by transparent summaries; it cannot establish microcirculatory dysfunction, true oxygen need or treatment benefit.

A two-state mechanistic instability score based on consecutive abnormal bins is retained as a deferred alternative pending ICU expert review of thresholds and discharge-readiness semantics. A full transformer is deferred because capacity alone adds no clinical question and stability/compute are unverified. Causal oxygen, discharge or treatment-effect modeling is deferred because MIMIC lacks clinician intent, valid counterfactual assignment, complete treatment-limitation context, fluid responsiveness and a validated discharge-readiness label. B1 isolates the parent phenotype increment, Bctx tests the chosen heterogeneity, and M2 tests the distinct information content of order/persistence/nonlinearity.

## Analysis, uncertainty and falsification

Fit three cause-specific discrete-time hazards and compute Aalen–Johansen CIFs at 24 and 48 hours. Standardize the unchanged parent theta_RD/theta_R/theta_D contrasts to the held-out parent cells. Report calibration intercept/slope, observed/expected ratio, Brier score, AUROC/AUPRC as secondary metrics, all fixed queue tables, random benchmarks and paired contrasts B1/Bdisc/Bctx/M2. Use identical subject-bootstrap resamples preserving the split, context strata and admission clustering within subject. Preprocessing, imputation, scaling, calibration, regularization and early stopping use training/validation only.

Required audits/falsifications:

- source SHA, archive members, catalog schemas, joins, dictionary labels/linksto/units and item IDs;
- first-exit and first-transition selection, D/R/S tie order, U logic and U bounds;
- row-level feature provenance with clinical time, store time, unit/value reason, duplicate and interval handling;
- no clinical or recording time >tL and no terminal/discharge/death/outcome field in features;
- MAP source collapsing, support interval duplicate/union checks, and missingness versus zero;
- parent-versus-child model source whitelist audit;
- dual-time versus chart-time-only matrices;
- early/late permutation preserving counts/availability and outcome permutation within partitions;
- Bmask removing physiologic values while retaining context, counts, masks and observation intensity;
- process-intensity model and outcomes by observation density;
- context results by first/transfer care unit and anchor-year group, without cross-subject calendar alignment;
- fixed context threshold, lactate 4.0, MAP-only, pressor-only, no-procedure, 24-hour, four/eight-bin and complete-ascertainment sensitivities;
- R and D capture separately, S boundary capture separately, deterministic queue arithmetic;
- outcome-free selected-exit versus eligible one-hour-record selection model q with common support and ESS diagnostics, never treated as causal correction.

Support requires parent gates, both context gates, `|Psi10|>=0.05` with a 95% interval wholly outside [-0.05,+0.05], no material Bdisc calibration degradation, coherent 5/20% direction, and no Bmask/process-only or timing falsification. A positive Psi means greater phenotype capture gain in residual instability; a negative Psi means attenuation. Adverse evidence includes no Bdisc gain in either context, `Psi10` inside the meaningful null, reversed R/D components, Bmask equivalence, outcome-permutation resistance, or timing instability. Inconclusive evidence includes failed source/unit joins, high context-indeterminate fraction, insufficient events, U/overlap failure or intervals too wide. Bctx or M2 gain alone is representation evidence, not proof of physiology.

## Claim boundaries, compute and provenance

Computationally checkable claims are source/schema/member hashes, dictionary links/units, joins, temporal filters, context construction, feature provenance, split integrity, labels/ties, model predictions, CIFs, queue arithmetic, calibration, uncertainty, process controls and falsifications. Clinical adjudication or another study is required for microcirculatory dysfunction, lactate etiology, true oxygen requirement, discharge appropriateness, preventability, clinician intent, treatment response, utility, harms, causal policy and external transportability. Notes exist locally but are excluded because timing/content can encode disposition and note links have documented limitations; MIMIC-CXR images and raw waveforms are unavailable.

Discovery inspected `datasets/README.md`, the MIMIC README/catalog and relevant table JSONs, `inputs.json`, the hardware skill, the expert-seed README and MIMIC-10 card, the parent and support note, and the three research-ambition demonstration/method summaries. A CPU source scan over the 3.4-GB compressed chart-events member was submitted as `[research job]`; it was still running at proposal time and supplies no prevalence or runtime evidence. Archive/schema/dictionary facts are measured; context prevalence, event support, U, overlap/ESS, model stability, bootstrap runtime and GPU necessity are unverified.

The future solver envelope is 16 CPUs, 262,144 MiB memory, up to 8 GPUs and 28,800 seconds, concurrency 2. B1/Bdisc/Bctx are expected to fit on CPU after one archive pass; this is an estimate. M2 is a small sequence model; one explicitly allocated A100 may accelerate repeated fits/bootstrap, but CPU remains valid if it fits. If GPU is used, request `gpus=1`, move model/tensors to `cuda:0`, and report image/import dependencies. Ordinary shell CUDA visibility cannot establish GPU absence. No task-specific fit or result is claimed.

The completion output is newly fitted held-out B1/Bdisc/Bctx/M2 competing-risk predictions, CIFs, the unchanged parent theta contrasts, `Psi5/Psi10/Psi20`, exact queue PPV/sensitivity/false-negative/R/D tables, context and feature manifests, uncertainty, process/selection/timing falsifications and a conclusion ledger—or a complete fixed-gate audit. All derived files remain in the workspace; source archives, notes and rows remain read-only.
