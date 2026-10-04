> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB metabolic change after established single-domain disease and route to a second domain

## Episode-11 child and scientific deliverable

This child preserves the leading parents' verified two-panel UK Biobank question but repairs temporal attribution. In the parent, the single existing cardiometabolic domain could first appear between panels 0 and 1. A measured change over that interval could therefore be partly downstream of the first diagnosis and could proxy unmodeled disease duration. The primary estimand is now restricted to people with exactly one domain already present at panel 0 and still exactly one domain at panel 1; duration since that domain's first coded date is included in both models. Participants whose first domain appears only between panels are retained only for a labeled secondary analysis.

The future solver must newly construct and freeze the source/header audit, paired outcome phenotype and codebook, stable-single-domain cohort, panel-gap and disease-duration variables, event flow, repeat-panel selection model, matched route-specific models, locked predictions, uncertainty, falsification and sensitivity outputs. Completion is a complete computed comparison and a conclusion classified as supportive, adverse or inconclusive. Readiness, a successful fit, a positive coefficient or a better fit alone is not completion.

## Unresolved question and hypothesis

Available evidence supports that baseline metabolic indices are associated with later cardiometabolic multimorbidity and that multistate models can describe progression. The recent Europe PMC search also returned 2026 UKB studies of baseline insulin-resistance/atherogenic indices and transitions to cardiometabolic multimorbidity. Those studies do not establish whether an observed dated change between two valid UKB biomarker panels adds information beyond the latest level after an existing disease is already established, nor whether it identifies which second domain is most likely.

Primary hypothesis:

> Among UKB participants aged 40–69 with exactly one coded domain—diabetes, cardiovascular disease, or chronic kidney disease—already present by biomarker panel 0 and no second domain through panel 1, annualized worsening in HbA1c, triglycerides and/or HDL predicts the first transition to a second domain after a one-year washout, beyond panel-1 levels, existing-domain identity, age, sex, disease duration and prespecified covariates. The incremental signal may be route-specific (for example, diabetes-to-CVD versus CVD-to-CKD), but should not be reproduced for acute appendicitis.

This is a prognostic association and internal-prediction hypothesis, not a causal effect of changing a biomarker, evidence that monitoring improves outcomes, a treatment recommendation, or a chart-adjudicated onset claim.

## Exact data binding and source audit

UKB snapshot: `[source checksum]`. All sources are ordinary read-only CSVs; there are no archive members. The catalog specifies one-to-one horizontal joins on `eid`, with overlapping fields audited for agreement.

| table | exact source path | catalog schema | join key | fields |
|---|---|---|---|---|
| `main` | `[internal dataset path]` | `datasets/ukb/table-e4a9e4d8baa71a9d.json` | `eid` | dates `53-0.0`, `53-1.0`; HbA1c `30750-0.0/1.0`; HDL `30760-0.0/1.0`; triglycerides `30870-0.0/1.0`; creatinine `30700-0.0/1.0`; cystatin-C `30720-0.0/1.0` |
| `assessment` | `[internal dataset path]` | `datasets/ukb/table-901ef6c7ddce2d51.json` | `eid` | dates `53-0.0/1.0`; BMI `21001-0.0/1.0`; systolic BP `4080-0.0/1.0`; diastolic BP `4079-0.0/1.0`; smoking `20116-0.0/1.0`; center `54-0.0/1.0` |
| `health_outcomes` | `[internal dataset path]` | `datasets/ukb/table-3cfae45e0905b0e3.json` | `eid` | ICD-10 diagnosis fields `41270-0.0`–`41270-0.258` paired by position with dates `41280-0.0`–`41280-0.258`; ICD-9 fields `41271-0.0`–`41271-0.46` paired with `41281-0.0`–`41281-0.46`; death `40000-0.0/1.0` |
| `population` | `[internal dataset path]` | `datasets/ukb/table-38565c9e35e7cb6c.json` | `eid` | sex `31-0.0`; recruitment age `21022-0.0` |

Source hashes are main `[source checksum]`, assessment `[source checksum]`, health outcomes `[source checksum]`, and population `[source checksum]`. The complete catalog reports 30,799, 18,159, 4,896 and 34 columns respectively; required fields above are present. A fresh bounded read of the first 1,000 ordered rows found 32 valid main date pairs, 31–32 nonmissing repeat assays per core marker, and 1,000 unique `eid` values per table. This is an availability probe, not a cohort estimate.

## Phenotype and temporal construction

Freeze before model fitting a codebook with normalized case/whitespace and explicit prefixes:

- diabetes: ICD-10 E10–E14; ICD-9 250;
- cardiovascular disease: ICD-10 I20–I25, I50, I60–I69; ICD-9 410–414, 428, 430–438;
- chronic kidney disease: ICD-10 N18/N19; ICD-9 585;
- negative control: acute appendicitis, ICD-10 K35; ICD-9 540.

Scan every suffix in both diagnosis/date arrays. Pair code and date only at the same suffix; require a valid parsed date. A domain's first event is the minimum valid paired date, not the first array position. Code-only/date-only mismatches are audited and create no event. These are first coded occurrences, not confirmed clinical onset.

For the primary stable cohort, require age 40–69 inclusive, valid sex, valid dates d0<d1 with a 365–3,650 day gap, finite core markers at both main instances, and agreement of main and assessment date fields at 53-0/1 after normalization. At d0 there must be exactly one domain and its first coded date must be on or before d0. At d1 there must still be exactly one domain, the same existing domain, and no death. Thus the change interval is not allowed to straddle acquisition of the existing domain or a second domain. Define disease duration at d1 as (d1 - first-domain-date)/365.25; report its distribution and require it in both models. Exclude a second-domain event or death in (d1, d1+365 days] from the primary risk set. Follow strictly after d1+365 days to the first second-domain event, death, administrative end, or five years. Death is absorbing; a same-day event/death tie treats death as primary, with reverse handling as sensitivity.

For marker j, compute annualized change `g_j=(x_j1-x_j0)/((d1-d0)/365.25)`; reverse HDL so worsening is positive. Standardize using fit-partition means/SDs only. No unavailable biomarker instances 2/3 are invented. The secondary interval-onset analysis allows one domain at d1 whose first date lies in (d0,d1], but reports it separately and does not pool it into the primary estimand. Sensitivities vary washout (0, 2, 5 years), gap (182–5,475 days), stable-domain definition and death ties.

## Matched baseline and substantive alternative

Both models use the same stable primary cohort, route-specific state space, disease-duration variable, covariates, split, censoring, competing-death convention and locked evaluation.

M0 is an interpretable cause-specific Cox baseline for each existing-domain → new-domain route and death. Inputs are panel-1 HbA1c `30750-1.0`, TG `30870-1.0`, HDL `30760-1.0`, existing domain, disease duration, age, sex, latest valid BMI/BP/smoking/center and panel gap. Use fit-frozen splines and participant-level uncertainty. A secondary extension adds latest creatinine/cystatin-C.

M1 has the identical route/death hazards, population and preprocessing and adds the three dated changes. It may include change-by-existing-domain interactions only under a fit-partition rule and adequate route support. M1 therefore tests whether the earlier dated panel contains incremental information after the current level and established-domain duration, rather than rewarding a different state space. Route-specific cumulative incidence is primary; aggregate “any second domain” risk is derived only after fitting routes.

A compact two-panel recurrent/temporal-attention model was considered with exactly the same inputs, target, split, metrics and bootstrap uncertainty. It could reveal nonlinear combinations and route interactions, but two observations carry little sequence structure and extra capacity cannot resolve repeat-testing indication, regression to the mean or coded-phenotype uncertainty. It is deferred pending at least three verified dated assay panels or a bounded preregistered diagnostic showing stable locked value beyond M1. This is a scientific adequacy decision, not a neural-network or GPU ban. The four-instance slope/mixed-effects branch is rejected because the local main header has no assay instances 2/3. The selected M1 is CPU-first; the future solver envelope is at most 16 CPUs, 262,144 MiB RAM and 28,800 seconds, currently unmeasured for full fitting/bootstrap. No GPU is required; any future learned branch must use an allocated GPU job and report its measured resource use separately.

## Split, uncertainty and decision analysis

Hash participants, never rows, using the catalog namespace `ehr-hypothesis-discovery-v1`, dataset and `eid` with SHA-256 modulo 100: buckets 0–59 fit, 60–69 model/threshold decisions, 70–79 locked test, and 80–99 reserved and unread. Freeze preprocessing, model choices, selection weights and thresholds before the locked test.

Report route coefficients and 95% intervals, five-year competing-risk cumulative incidence, integrated/time-dependent Brier score, calibration intercept/slope/error, discrimination, restricted mean event-free survival and paired 200-resample participant-bootstrap intervals for M1−M0. Preserve seeds, indices, convergence warnings and route event support.

Use “refer for additional metabolic/cardiovascular/kidney risk review” only as a hypothetical action. Evaluate fixed 5%, 10% and 20% five-year-risk operating points, with alerts, sensitivity, specificity, PPV, number needed to review, calibration and decision-curve net benefit. These are not validated clinical cutoffs. Clinical utility requires an expert-approved review action, burden/costs and external validation.

## Falsification and interpretation

Supportive evidence requires: a prespecified worsening-direction joint change association after latest levels, disease duration and gap; route estimates compatible with the proposed heterogeneity where supported; locked-test improvement in Brier/calibration or 10% net benefit without material subgroup harm; persistence across washout, gap, selection-weighting, missingness and competing-death sensitivities; no comparable appendicitis association; and no signal under within-state, sex or gap-bin change permutations. Any interval-onset versus stable-cohort difference is supportive only if event support and uncertainty permit it; otherwise it is inconclusive.

Adverse evidence is a null/reverse joint change association, loss after duration adjustment, worse locked performance/calibration/net benefit, a comparable appendicitis signal, or a permutation signal. This falsifies the incremental prognostic claim in the selected cohort, not biological harmlessness or all possible causal effects.

Inconclusive evidence includes too few stable repeat panels or second-domain events, date/code mismatch, inadequate repeat-availability positivity, poor route support, severe subgroup calibration failure, or intervals spanning meaningful benefit and no benefit. A computed threshold result without a specified clinical action is inconclusive for policy value.

Computationally checkable claims are source hashes/headers, joins, field rules, code/date pairing, first-event dates, stable-cohort flow, duration and gap distributions, split integrity, fitted models, uncertainty, predictions, calibration, Brier, decision curves, permutations and sensitivities. Confirmed disease onset, treatment effects, repeat-testing indication, medication/adherence effects, external validity, transport to non-repeat-tested people and clinical utility require adjudication, additional data or another study.

## Context and retained alternatives

The three demonstrations were read as context. Delphi supports the general value of ordered dated histories, but this is not a reproduction and no Danish validation is claimed. ALADYNOULLI's genetic analysis is not reproduced because the selected question has no verified genetic design requirement; M1 is a bounded EHR transition adaptation, not that method. The Oncoformer supplement was inspected for modality-ablation context, while the main article and complete STAR Methods remain unavailable and raw images are absent; no multimodal claim is made.

The adopted expert seed is UKB seed 09, “metabolic deterioration and multimorbidity,” materially revised to stable single-domain disease at both biomarker panels and duration-adjusted route progression. UKB seeds 01 (infection), 02 (organ aging/proteomics), 03 (discordant kidney estimates/AKI), 04 (fat distribution/imaging), 05 (sleep/accelerometry), 06 (post-infection cardiovascular risk/proteomics), 07 (CHIP sequencing), 08 (reserve/cancer) and 10 (genetic risk/protective factors) remain deferred because exact local modalities, staging, exposure timing or validation dependencies are unavailable or unverified; none is disproven. HCC, MIMIC and eICU remain directly accessible read-only through their catalogued source files and distinct schemas, but are not validation cohorts for this UKB design and cannot be silently joined to UKB.

This candidate is a substantive child of `[prior hypothesis]` and `[prior hypothesis]`. The change is not cosmetic: it separates biomarker change after established disease from change surrounding first-domain acquisition and adjusts the route comparison for disease duration.
