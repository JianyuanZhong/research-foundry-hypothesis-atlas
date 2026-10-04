> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# CBC cancer-type ordering boundary after delayed entry

Status: planned Harbor experiment; no model, event estimate, cohort count, or hypothesis result has been executed in this branch. This is an independent substantive alternative to parent [prior hypothesis]. It retains the inherited UKB CBC cancer-type question but changes the primary deliverable from a coefficient contrast to a calibrated, absolute risk-ordering boundary.

## Scientific opening and clinical importance

The strongest inspected evidence supports a narrower claim than a clinical CBC rule. Sala et al. report that serial CBC trajectories can precede and stratify metastatic versus non-metastatic CRC in a retrospective CRC-only cohort [K1]. Hampton et al. find that cancer-risk models often lack calibration and external validation, even when discrimination appears good [K2]. Brands et al. show that triage performance depends strongly on symptomatic context and that adding FIT can materially change referral evidence [K3]. Together they motivate a dated CBC signal, but they do not establish that a UKB assessment-centre CBC trajectory can order future CRC versus hematologic cancer, nor that it can support a referral decision.

The unresolved question is:

> Among adults with complete CBC measurements at two verified UKB assessment instances, does a prespecified trajectory create a reproducible absolute-risk boundary in which the later 5-year cumulative incidence of registry-coded CRC exceeds that of hematologic cancer, after a two-year delayed-entry stress test and comparison with other primary cancers?

This is clinically consequential because CRC and hematologic malignancy lead to different confirmatory pathways. The proposed boundary is a research ordering boundary, not a diagnostic cutoff or referral recommendation: it asks whether the observed data can reliably rank the two cancer families at all. The experiment cannot determine whether a person should be referred because symptoms, test indication, FIT, iron studies, pathology, stage and clinical harms/benefits are unavailable.

The substantive advance over the parent is an absolute, profile-standardized decision boundary with explicit calibration and boundary stability. A relative CBC coefficient can be statistically nonzero yet too small, poorly calibrated or unstable to change which pathway has higher expected risk. The new deliverable asks whether a fixed CRC-like profile and a fixed hematologic-like profile fall on opposite sides of a clinically interpretable risk-ordering boundary, and whether that ordering survives the near-diagnosis and ascertainment tests. It therefore addresses a different scientific uncertainty, not a small predictive gain.

## Hypothesis, rival explanations and claims

Primary hypothesis H1: in the delayed-entry risk set, a fixed CRC-like CBC trajectory will have a higher 5-year CRC cumulative incidence and lower 5-year hematologic cumulative incidence than a fixed hematologic-like trajectory, with a standardized CRC-minus-hematologic absolute risk contrast of at least 0.5 percentage points for each profile and a 95% interval excluding zero for the sign of the ordering. The boundary is defined by

    B_5(x) = CIF_CRC,5y(x) - CIF_HEME,5y(x)

and the research pathway-ordering rule is CRC-side when B_5(x) >= +0.005 and hematologic-side when B_5(x) <= -0.005. Values between these boundaries are an indeterminate zone. The 0.005 quantity is a prespecified design threshold on the absolute-risk scale, not a clinical referral threshold.

The profiles are fixed before any outcome analysis, using development-partition CBC standardization:

- CRC-like: Delta-Hb = -0.75 SD, Delta-RDW = +0.75 SD, Delta-platelets = +0.75 SD, Delta-WBC = 0 SD.
- Hematologic-like: Delta-Hb = -0.75 SD, Delta-RDW = 0 SD, Delta-platelets = -0.75 SD, Delta-WBC = +0.75 SD.
- Reference: all four deltas = 0 SD.

These are standardized descriptive profile interventions in the fitted model, not claims that changing a patient’s CBC causes risk to change. For every profile, standardize over the observed covariate distribution in the held-out set; do not report only a hand-picked participant.

The strongest rival is occult disease proximity and ascertainment: the profile is a marker of cancer already developing near the CBC or of intensified testing, not a durable site-specific signal. It predicts a larger boundary in the 0–2-year window, attenuation after delayed entry, and calendar-era or outcome-source instability.

A second rival is generic cancer burden or inflammation: the same CBC pattern reflects systemic illness, infection, nutrition, chronic disease or health-care contact. It predicts similar profile ordering for other primary C00–C97 cancers, weak CRC-versus-hematologic specificity, and attenuation after CRP adjustment or repeat-attendance weighting.

A third rival is repeat-attendance and measurement selection: complete instance-1 CBC selects survivors who return to a research assessment, with different intervals, calendar eras and assay conditions. It predicts imbalance in repeat completion, dependence on the assessment interval, and changes under inverse-probability weighting. Weighting is a measured-selection stress test, not a causal repair.

Evidence already supports only the existence of a plausible prediagnostic CBC signal and the need for calibration and context-specific validation [K1–K3]. It does not support H1, a mechanism such as occult gastrointestinal bleeding or marrow disease, or a clinical action. The precise unresolved claim is the delayed, absolute CRC-versus-hematologic ordering boundary defined above.

## Exact verified data binding

All primary analyses use one table, one namespace and no joins.

- Catalog table: `datasets/ukb/table-5d49a6760e7ffdbd.json`, named `ukb671626.csv (Parquet)`.
- Read-only source: `[internal dataset path]`.
- Parquet source ID: `[UKB data file]`; [source checksum]; 502,371 rows and 502,371 unique `eid` in the catalog.
- Original lineage: `[internal dataset path]`, source ID `[UKB data file]`, [source checksum]; catalog archive member is an ordinary file.
- Join key: `eid`, restricted to identifier namespace `ukb671626`. Do not join it to `ukb672073`, dta or olink. The catalog confirms that the separate assessment-center, biological-sample and genomics tables have different namespaces; no crosswalk is verified for this study.

Required inputs, all columns of `ukb671626`:

- Dates: `53-0.0`, `53-1.0` (Date of attending assessment centre). Define t1 from `53-1.0`; require `53-1.0 > 53-0.0`. The solver must recompute the maximum nonmissing registry cancer date and report it; the inherited audit observed 2022-06-01 but this proposal does not treat that observation as an assumed constant.
- CBC: `30000-0.0/1.0` WBC, `30020-0.0/1.0` haemoglobin, `30070-0.0/1.0` RDW, and `30080-0.0/1.0` platelets. Only instances 0 and 1 are required for the primary design. Values are strings in the Parquet view and must be explicitly cast; missing primary CBC values are not imputed.
- Prespecified covariates: `31-0.0` sex, `34-0.0` year of birth, `21001-0.0/1.0` BMI, `20116-0.0/1.0` smoking status, and `30710-0.0/1.0` CRP. Age at t1 is calculated from `34-0.0` and `53-1.0`. The assessment interval is `53-1.0 - 53-0.0`. No center field is used.
- Primary registry outcome: paired arrays `40006-0.0` through `40006-21.0` (Type of cancer: ICD10) and `40005-0.0` through `40005-21.0` (Date of cancer diagnosis). Pair code and date only by the same array index.
- Primary competing death: `40000-0.0` and `40000-1.0` (Date of death); use the earliest valid date relevant to follow-up.
- Sensitivity outcome: paired `41270-0.0` through `41270-258.0` (Diagnoses - ICD10) and `41280-0.0` through `41280-258.0` (Date of first in-patient diagnosis - ICD10). These are a predeclared sensitivity, not a replacement for the registry.
- Administrative end: recompute from the frozen source as the maximum nonmissing primary cancer-registry date, report the checksum and do not extend follow-up from a later source.

Normalize codes only by trimming, uppercasing and removing punctuation for prefix matching, while preserving original strings for audit. CRC is C18–C20, including subcodes. Hematologic cancer is C81–C96, including subcodes. Other primary malignant neoplasms are C00–C97 excluding those target families and excluding secondary C77–C79 from target assignment. Do not infer cancer stage, morphology or histology from these codes.

## Population and temporal boundaries

Include participants with valid `eid`, nonmissing castable CBC at instances 0 and 1, valid dates with t1 after t0, and no registry-coded C00–C97 cancer on or before t1. Record a flow table and compare included repeat attendees with all instance-0 CBC-complete participants. This is not a disease-free cohort: registry absence cannot exclude occult cancer.

Define the primary delayed-entry analysis as follows:

1. Landmark at t1 = `53-1.0`.
2. Exclude participants with any target cancer, other primary cancer or death in (t1, t1 + 730 days]. Participants surviving this interval enter at e = t1 + 730 days.
3. Follow from e to the earliest of CRC, hematologic cancer, other primary cancer, death or recomputed administrative end. The primary horizon is 5 years after e; report shorter horizons if event support requires it.
4. A same-day CRC/hematologic pair is a tie. Report it separately and exclude it from the mutually exclusive primary boundary; a sensitivity assigns it to the first array entry. A same-day target and death is handled by a fixed date-order rule stated in the analysis log.
5. The near-diagnosis sensitivity starts at t1 and uses the first 0–730 days. It is deliberately not pooled with the delayed analysis. An additional 2–5-year interval after t1 is equivalent to the delayed-entry primary when no event occurs in the gap.
6. Other cancer and death are competing events for cumulative incidence. For cause-specific hazards they leave the target risk set at their event date; this is descriptive competing-risk analysis, not a causal estimand.

A participant-level deterministic split is created after eligibility and outcome derivation but before any standardization, imputation or fitting. Use the earliest 70% of t1 dates for development and the latest 30% for held-out testing; retain whole participants. If the late-calendar test has inadequate 5-year follow-up, report the limitation and use a participant-hash held-out secondary check, never silently change the primary split. The administrative end and event counts must be shown for each split.

## Analysis and actual deliverable

The actual scientific deliverable is newly fitted evidence, not a model package alone. Completion requires:

- a locked flow/missingness/interval/event table and paired code-date audit;
- a split manifest and development-only standardization constants;
- fitted baseline and learned models on matched inputs;
- `B_5` estimates for the CRC-like, hematologic-like and reference profiles, with participant bootstrap 95% intervals;
- target-specific 2- and 5-year cumulative incidence, calibration intercept/slope/plots, Brier or log scores, and boundary occupancy;
- near-diagnosis versus delayed-entry estimates, other-cancer comparator, registry/inpatient sensitivity, and repeat-attendance weighting results;
- conclusions that cite the computed outputs and classify the result supportive, adverse or inconclusive.

### Transparent baseline

Fit separate cause-specific Cox models for CRC, hematologic cancer and other primary cancer/death using:

- the four instance-0 CBC standardized levels;
- the four within-person changes (instance 1 minus instance 0), each standardized using development quantities;
- age at t1, sex, BMI at instance 0, smoking at instance 0, baseline CRP, assessment interval and t1 calendar year.

Do not include instance-1 CBC levels in this linear baseline when the corresponding instance-0 level and change are present: instance 1 is algebraically determined by baseline plus change. This avoids the identifiability problem in the parent while preserving current-state information through the two independent components. Use fixed linear terms for the prespecified profiles and their cause interactions; use age and interval splines only if specified before fitting. Report cause-specific hazard ratios only as secondary descriptive outputs. Obtain profile-specific cumulative incidence with an Aalen–Johansen-compatible g-computation/standardization over held-out covariates. Use robust participant-level uncertainty and a predeclared penalization rule if separation occurs.

The baseline is not merely a comparator. It tests whether an auditable linear profile and absolute competing-risk calculation are sufficient to cross the pathway-ordering boundary. It loses threshold effects and interactions, such as a haemoglobin decline that matters only when RDW and platelets move together.

### Learned alternative

Fit a CPU gradient-boosted discrete-time multi-task competing-risk model to exactly the same participants, split, covariate information and outcomes. Inputs are the same instance-0 CBC levels, four changes, age, sex, BMI, smoking, CRP, interval and t1 year; it receives no cancer dates or post-landmark values. Expand each participant into one-year intervals from e through five years or first event. The class target is CRC, hematologic cancer, other cancer/death or no event conditional on being event-free at interval start. Use modest HistGradientBoosting or an equivalent fixed implementation, with hyperparameters selected only in rolling development folds.

The learned model is informative because it can reveal a nonlinear boundary that the baseline averages away: for example, whether the same haemoglobin fall changes pathway ordering only above a platelet/RDW combination, or whether the ordering is time-local rather than constant. Its primary comparison is not AUC. Evaluate whether its standardized `B_5` boundary is calibrated and reproduced in the held-out data, and whether it adds a stable, clinically interpretable profile separation beyond the transparent baseline. Report target-specific 2-/5-year Brier/log scores, calibration slope/intercept, time-dependent AUC secondarily, and participant-bootstrap intervals. A small predictive improvement without a stable, calibrated boundary is not a scientific advance.

For the learned model, generate held-out profile predictions by replacing only the four change components with the three prespecified profile vectors while holding the observed covariate distribution fixed. Label these as model-standardized profiles, not patient counterfactuals. Use development-only preprocessing. Compare baseline and learned boundary direction and magnitude; if they disagree materially, classify the scientific result as inconclusive unless one has a prespecified calibration failure.

## Selection, ascertainment and falsification checks

Run these checks once under the locked plan:

- Repeat-attendance model: among instance-0 CBC-complete participants, predict complete instance-1 CBC using only age, sex, BMI, smoking, baseline CBC, CRP, t0 year and observed interval eligibility. Use stabilized inverse-probability weights with a fixed truncation rule. Compare unweighted and weighted boundary estimates; this diagnoses measured selection and is not a causal correction.
- Proximity: report 0–2-year and delayed 2–5-year boundary estimates separately. A boundary that exists only before delayed entry supports proximity/ascertainment rather than durable biology.
- Generic burden: estimate the same profile-specific absolute contrast for other primary cancers versus the target families. A similar boundary for other cancers weakens site specificity.
- Source concordance: repeat event derivation with inpatient arrays 41270/41280, preserving the registry as primary. A material reversal is adverse to a registry-robust claim.
- Calendar stability: repeat estimates by prespecified t1 calendar-era strata and test interaction with era. A change across eras is a warning about ascertainment or coding environment, not evidence of biology.
- Measurement and negative controls: report interval distribution, implausible dates and registry code/date alignment. Permute cancer-family labels among target events in development only; the boundary should collapse toward zero. Reverse the change-vector signs as a diagnostic, not as a new search.
- Sparse-event rule: if the held-out hematologic count is fewer than 50, or if the boundary interval spans both the null and the 0.005 design threshold, do not call the result adverse or supportive solely from a point estimate.

Supportive results require all of: (i) the two profiles have the prespecified opposite-sided standardized delayed-entry boundary with the required 0.005 margin and uncertainty; (ii) the direction is retained in the held-out set and in at least one calendar-era/source sensitivity; (iii) target-specific calibration is acceptable under a prespecified tolerance; and (iv) the difference is not reproduced similarly for other primary cancer and is not confined to 0–2 years. This would support a reproducible descriptive CRC-versus-hematologic ordering signal worth external validation. It would not establish mechanism, diagnosis, referral, benefit, or causality.

Adverse results are a precise reversal of the prespecified ordering, a precise delayed null after a near-diagnosis-only signal, or a boundary that is reproduced for other cancers but not for CRC versus hematologic cancer. That would falsify the stated site-specific boundary and favor proximity, generic burden or ascertainment explanations. It would not prove that CBCs have no cancer association.

Inconclusive results include sparse delayed hematologic events, wide intervals, poor calibration, model disagreement, unstable era/source results, or a temporal holdout with inadequate follow-up. An imprecise null is not a refutation. Continue only with a clinically richer or larger cohort, not with outcome-guided profile thresholds or repeated threshold searches.

## Missing evidence and limits of inference

The source lacks symptoms, test ordering and indication, primary-care contacts, ferritin, iron/transferrin saturation, reticulocytes, FIT, infection timing, medications, transfusion, pathology, stage, morphology, flow cytometry, cytogenetics, molecular subtype, treatment and systematic external validation. The assessment-centre repeat is not routine clinical monitoring and may select healthier returners. Registry and inpatient codes are ascertainment fields, not adjudicated incident phenotypes.

Computationally checkable claims are source binding, same-namespace joins, cohort flow, code/date pairing, temporal windows, competing-risk estimates, profile standardization, calibration, boundary stability, uncertainty and whether conclusions follow from outputs. Clinical adjudication is required to decide whether a trajectory reflects occult blood loss, marrow disease or another mechanism. External validation in symptomatic and asymptomatic clinical populations is required for transportability. A prospective decision-impact study with symptoms, indications, test harms and downstream outcomes is required before any referral or surveillance change. No automatic verifier can establish those claims.

## Method comparison, resources and selection record

The selected transparent method is the primary scientific baseline because it directly estimates an auditable absolute competing-risk boundary and avoids the parent’s algebraic dependence among baseline, current and change CBC values. The learned alternative is retained because nonlinear interaction and threshold information may be scientifically important for pathway ordering, not because it may improve AUC slightly. Both use exactly matched inputs, split, horizons, outcomes and uncertainty.

A simple static threshold model was not selected as the main alternative: it discards within-person change and cannot test whether a boundary is stable after delayed entry. A neural sequence/latent-GP model was deferred because the verified table has only two broadly complete CBC instances for this design, and extra capacity cannot recover missing clinical indication. A model using olink, genetics or `ukb672073` fields was rejected because the verified identifier namespaces and required crosswalk are absent; this is a data-validity decision, not a blanket objection to multimodal or neural methods. A decision-curve/net-benefit analysis was also deferred: harms, referral alternatives, symptoms, indication and treatment consequences are unavailable, so it would manufacture clinical utility. It should be revisited only with those data.

Measured discovery facts inherited from the verified branch are the Parquet schema and selected-column audits; no new cohort scan or model fit was executed here. Future solver estimates are unverified: 8–16 CPU cores, 32–64 GiB RAM, approximately 2–4 hours for cohort construction, two model families, held-out predictions and 200–500 participant bootstrap replicates. CPU is appropriate for the tabular Cox/boosted design; no GPU is requested. The configured hardware includes A100 GPUs, but allocation is not a scientific requirement for this experiment.

## Three inspected key works

[K1] Sala et al. supports the prediagnostic CBC-trajectory opening but is a retrospective, CRC-only cohort and does not establish cancer-type ordering or implementation.

[K2] Hampton et al. supports calibration, validation and appropriate-population safeguards; it does not validate this UKB CBC boundary.

[K3] Brands et al. supports the importance of symptomatic context and bounds any clinical triage interpretation; it does not establish a CBC or hematologic decision rule.

Compact bibliography:

- [K1] Sala RJ, Ery J, Cuesta-Peredo D, Muedra V, Rodilla V. “Haematological pre-staging of colorectal cancer: Longitudinal trends identify high-risk metastatic phenotypes 24 months prior to diagnosis.” Translational Oncology. 2026;72:102954. DOI 10.1016/j.tranon.2026.102954. PMCID PMC13449478. Full-text XML inspected.
- [K2] Hampton JS, Kenny RPW, Rees CJ, Hamilton W, Eastaugh C, Richmond C, Sharp L, COLOFIT Research Team. “The performance of FIT-based and other risk prediction models for colorectal neoplasia in symptomatic patients: a systematic review.” EClinicalMedicine. 2023;64:102204. DOI 10.1016/j.eclinm.2023.102204. PMCID PMC10541467. Full-text XML inspected.
- [K3] Brands HJ, Van Dijk B, Brohet RM, van Westreenen HL, de Groot JWB, Moons LMG, de Vos Tot Nederveen Cappel WH. “Possible Value of Faecal Immunochemical Test (FIT) When Added in Symptomatic Patients Referred for Colonoscopy: A Systematic Review.” Cancers (Basel). 2023;15(7):2011. DOI 10.3390/cancers15072011. PMCID PMC10093340. Full-text XML inspected.

The attached evidence files are selected UTF-8 excerpts from the inspected frozen XML sources, not claims that the excerpts replace the full papers.
