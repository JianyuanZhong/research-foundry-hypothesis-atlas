> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.


# Resource-aligned repair for the fixed-capacity UKB cystatin-C allocation experiment

## Decision, evidence boundary, and unresolved hypothesis

A service with capacity to order cystatin C for exactly 20% of adults with baseline creatinine eGFR (eGFRcr) 60–89 mL/min/1.73 m² must distinguish two decisions:

1. immediately allocate cystatin C without a urine result; or
2. first obtain and wait for a usable UACR, then allocate cystatin C.

The selected parent correctly repaired the chronology problem: UK Biobank's nonmissing instance-0 UACR establishes calculability, not that UACR was available before an unrecorded cystatin-allocation decision. This child addresses the strongest remaining decision gap: the two workflows have the same cystatin-C capacity but not the same upstream resource use or operational target population.

The strongest supported claims remain feasibility and timing non-identifiability. In the inherited audit, O has 134,118 eligible participants and censor-aware instance-0 UACR is usable for 130,257 (97.12%); coverage is 97.18% in test and 97.14% in replication. The biological-samples schema has the required urine, creatinine and cystatin fields but no temporal columns; the physical header has 1,775 unique fields and no collection, result, order, release, date or timestamp field. The full catalog records the UKB convention that field instance/array indices are not elapsed time. These facts do not establish a clinical workflow sequence.

The inherited evidence from Chen et al. (Kidney Medicine 2024; DOI 10.1016/j.xkme.2024.100796; PMCID PMC10986041; frozen full-text XML inspected by the parent) supports associations with creatinine–cystatin eGFR differences and an internally validated enriched model with AUC about 0.75. It does not establish fixed-capacity policy value, UACR chronology, measured-GFR validity, persistent albuminuria, clinical benefit, cost, or equitable access.

The unchanged performance hypothesis is:

> In each locked partition, conditional on a protocolized UACR-first workflow that attempts UACR for every O participant and waits for a usable result, AG_V will identify at least 2 additional combined-equation eGFR<60 reclassifications per 1,000 cystatin assays versus A_V, with yield ratio at least 1.10 and positive marker-discordance yield; G_V will be noninferior to A_V at -1 reclassification per 1,000. If inherited N18 event sufficiency passes, AG_V will add at least 1 reclassification followed by first 10-year inpatient N18 per 1,000 and G_V will be noninferior at -1 per 1,000. The result must replicate and all inherited all-O, B/F/T, placebo, missingness, calibration, sex-stability, UACR-robustness, N18 and integrity gates must pass.

The immediate no-UACR arm remains the inherited all-O comparison of G against B/F/T at the same absolute cystatin capacity. No result from V may be relabeled as an immediate pre-UACR estimate.

## Substantive repair: separate cystatin capacity from total pathway resources

The parent’s exact capacity constraint is preserved:

\[
n_p=\lfloor 0.20 |O_p|\rfloor.
\]

That is a cystatin-assay capacity, not a complete equal-resource constraint. A UACR-first workflow requires an upstream urine work-up and waits for a usable result; the immediate workflow does not. UKB has no price, staff-time, turnaround, patient-burden, refusal, or access fields, so a scalar cost or utility cannot be invented.

Define, in each partition p:

- \(O_p\): the unchanged eligible population.
- \(V_p\): the unchanged subset with a computable censor-aware instance-0 UACR and positive urine creatinine.
- \(M_p=O_p\setminus V_p\): eligible participants without a usable UACR under the frozen rule.
- \(n_p=\lfloor0.20|O_p|\rfloor\): the unchanged exact cystatin capacity.

The experiment must report a resource vector, not a fabricated combined cost:

| Workflow | UACR work-up attempts | Cystatin assays | UACR failure/absence |
|---|---:|---:|---:|
| W1 protocolized UACR-first | \(|O_p|\) | \(n_p\) | \(|M_p|\) |
| W0 immediate no-UACR | 0 | \(n_p\) | not applicable |

For W1, “attempts” is a protocol quantity: the primary emulation specifies exactly one upstream UACR work-up for every O participant before cystatin allocation. It is not inferred from a stored UACR value and is not a claim that UKB recorded such a protocol. In this retrospective experiment, the vector is a counterfactual resource specification; M means result unavailable or unusable in the snapshot, not a documented failed clinical collection. Repeat attempts are outside the fixed protocol and would increase UACR resource use above |O_p|. If a real service would repeat failed tests or offer UACR only to a subset, that is a different estimand requiring a prespecified eligibility and fallback rule.

The primary W1 policy is now operationally explicit: rank only \(V_p\) by the frozen A_V or AG_V score and select exactly \(n_p\); \(M_p\) receives no cystatin allocation under this primary policy. This is a deliberate “usable-result required” policy, not silent exclusion. Report \(|M_p|\), \( |V_p|/|O_p|\), and whether \(|V_p|\ge n_p\). A later study may add a fallback for \(M_p\), but no fallback may be invented from this snapshot.

W0 ranks all \(O_p\) by the frozen UACR-free G, B, F and T scores and selects exactly \(n_p\). It has no UACR work-up. G_V remains inadmissible as an immediate policy estimate because V membership depends on a usable urine result.

This repair does not claim that UACR work-up and cystatin assays consume comparable units, and it does not impose an arbitrary sum such as \(|O_p|+n_p\). It makes the extra W1 resource visible while preserving the fixed cystatin capacity.

## Frozen design made explicit

Construct one row per eid by one-to-one horizontal joins. O contains participants aged 40–69 at recruitment; sex coded 0 or 1; valid baseline assessment date 53-0.0; positive baseline serum creatinine 30700-0.0 and BMI 21001-0.0; at least one finite positive baseline left/right grip value 46-0.0 or 47-0.0; full-precision 2021 race-free eGFRcr in [60,90); and no position-matched inpatient N17* or N18* diagnosis dated on or before baseline. Exclude and count separately any participant with an N17/N18 code whose paired date is missing or unparsable. O does not require cystatin C, UACR, a future assessment or an observed outcome.

Time zero remains 53-0.0. Convert creatinine from µmol/L to mg/dL by dividing by 88.4. With female defined by 31-0.0=0, compute:

\[
eGFRcr=142\times\min(Scr/k,1)^\alpha\times\max(Scr/k,1)^{-1.200}\times0.9938^{age}\times1.012_{female},
\]

where k=0.7 and alpha=-0.241 for female, and k=0.9 and alpha=-0.302 for male. Never use rounded displayed eGFR.

For positive cystatin C Scys=30720-0.0, H=1 when the 2021 combined equation is below 60:

\[
eGFRcr\text{-}cys=135\times\min(Scr/k,1)^\alpha\times\max(Scr/k,1)^{-0.544}\times\min(Scys/0.8,1)^{-0.323}\times\max(Scys/0.8,1)^{-0.778}\times0.9961^{age}\times0.963_{female},
\]

with k=0.7/0.9 and alpha=-0.219/-0.144 for female/male. D=1 when the 2012 eGFRcys divided by 2021 eGFRcr is at most 0.70, where

\[
eGFRcys=133\times\min(Scys/0.8,1)^{-0.499}\times\max(Scys/0.8,1)^{-1.328}\times0.996^{age}\times0.932_{female}.
\]

H is a one-time biochemical threshold crossing and D is marker discordance; neither is measured GFR or an adjudicated diagnosis.

Partition with h=int(SHA256(utf8("ukb-grip-cys-v3|" + canonical_decimal_eid)).hexdigest(),16)%100: development h<60, untouched test 60<=h<80, untouched replication h>=80. Freeze every transform, score, variant and threshold before opening locked cystatin or outcome labels.

V is the subset of O with either finite positive urine albumin 30500-0.0 plus finite positive urine creatinine 30510-0.0, or blank albumin with albumin flag 30505-0.0 trimmed exactly to <6.7 plus finite positive urine creatinine. Numeric UACR is 1000a/c mg/mmol; primary left-censored a=3.35 mg/L. A numeric/flag contradiction is an integrity failure. Field 30515-0.0 is the urine-creatinine result flag and is never parsed as albumin. Missing/nonpositive urine creatinine, missing albumin without exact <6.7, another flag or a nonfinite ratio is M, not V.

K18 is the earliest valid position-matched inpatient N18* code/date from 41270-0.i and 41280-0.i, i=0,...,258, strictly after time zero and on or before time zero plus 10 years. Death is the earliest valid 40000-0.0 or 40000-1.0; death before or on the K18 date competes, with same-day death preceding K18. N17 does not censor N18. Missing outpatient diagnoses, emigration and individual linkage censor dates prevent interpreting no event as complete follow-up.

## Estimands and denominators

For a selected set S in partition p, retain the existing assay-yield estimands:

\[
Y_H(S)=1000\frac{\sum_{i\in S}H_i}{n_p},\quad
Y_D(S)=1000\frac{\sum_{i\in S}D_i}{n_p},\quad
Y_{H18}(S)=1000\frac{\sum_{i\in S}H_iK18_i}{n_p}.
\]

These are cystatin-assay yields. Report the inherited paired contrasts:

- AG_V − A_V and its feasible ratio for incremental value after usable UACR;
- G_V − A_V for substitution within the usable-UACR stratum;
- all-O G − B/F/T for the immediate no-UACR policy;
- exact selected counts, overlap/Jaccard and directional swap decompositions.

Add two resource/selection audits without replacing the primary estimands:

1. UACR coverage:
   \[
   C_{U,p}=1000|V_p|/|O_p|,
   \qquad F_{U,p}=|M_p|/|O_p|.
   \]

2. Eligible-population allocation throughput:
   \[
   T_H(S)=1000\frac{\sum_{i\in S}H_i}{|O_p|},
   \quad
   T_D(S)=1000\frac{\sum_{i\in S}D_i}{|O_p|},
   \quad
   T_{H18}(S)=1000\frac{\sum_{i\in S}H_iK18_i}{|O_p|}.
   \]

The throughput audit reflects both exact cystatin capacity and the fact that W1 does not allocate cystatin to \(M_p\); it is not a treatment effect or a cost-effectiveness estimate. Since \(n_p\) is the same absolute cystatin capacity across arms, it cannot be used to claim that W1 and W0 have equal total burden. Do not divide W1 primary outcomes by \(|V_p|\), do not divide W0 outcomes by \(|O_p|\) while calling that a matched assay-yield contrast, and do not compare a V-restricted yield directly with an all-O yield as if the candidate populations were identical.

The workflow labels must therefore be:

- W1_conditional_uacr_first: conditional assay performance on V, with resource vector \((|O_p|,n_p)\);
- W0_immediate_no_uacr: all-O UACR-free performance, with resource vector \((0,n_p)\);
- Wobs_observed_preassay: nonevaluable, because collection/result/allocation timestamps are absent.

## Timing audit and unavailable chronology

Define an observed-pre-assay label only if participant-level urine collection time, usable UACR result-release time, intended cystatin-order/allocation time, and availability times for every other policy input are present. The UKB snapshot supplies none of these.

The required audit must deterministically report:

- timing_fields_present=false;
- assignable_prior_count=0;
- assignable_post_count=0;
- timing_unknown_count=|V_p|;
- timing_unknown_fraction=1.0;
- observed_preassay_estimand_evaluable=false;
- reason=required_timestamps_absent.

The zero assignable count means no participant can be classified from the source, not that no urine was collected before a decision. Do not use instance 0, horizontal colocation, nonmissing UACR, recruitment date 53-0.0, cystatin availability, or a later N18 diagnosis as chronology proxies.

## Supportive, adverse and inconclusive results

A supportive W1 result requires every inherited gate, including both locked V partitions meeting the AG_V materiality/ratio/swap and D criteria, G_V noninferiority, all-O gates, robustness and sufficiently observed N18 gates. It supports only conditional performance of the specified UACR-first pathway. The report must also display its upstream vector and C_U; a positive assay yield cannot erase the additional UACR work-up or its 2.88% inherited unusable-result stratum.

A supportive W0 result requires the unchanged inherited all-O G:B/G:F/G:T gates and is labeled immediate_no_uacr_supportive. It supports prospective evaluation of a UACR-free allocation policy, not benefit from testing or real-time availability of every input.

If W1 and W0 are both supportive, the strongest conclusion is that both fixed-cystatin-capacity strategies merit prospective head-to-head evaluation with measured turnaround, refusal, staff time, patient burden, cost, equity and clinical actions. The UKB experiment does not select a winner because it does not identify a utility function that trades \((|O_p|,n_p)\) against \((0,n_p)\).

A W1 adverse result remains adverse when precision is adequate and a locked AG_V materiality/ratio/swap, G_V noninferiority, or sufficiently observed N18 gate fails. It falsifies conditional value of the UACR-first policy despite its extra upstream resource. A W0 adverse result remains an inherited all-O failure. A favorable W1 throughput cannot rescue an adverse W1 assay-yield gate, and a favorable W0 result cannot be used to claim UACR-first efficiency.

The result is performance-inconclusive under the inherited rules when intervals cross margins, locks disagree, V coverage/capacity fails, labels or swaps are sparse, N18 is insufficient, a feasible ratio denominator can be zero, a UACR variant reverses sign, or a join/date/calibration/integrity check fails. Missing resource prices or missing chronology are reported as evidence limitations, not as adverse policy performance.

## Exact data bindings and availability

All source files are read-only ordinary CSVs with archive member null in snapshot [source checksum]. Join one-to-one horizontally on eid; overlapping fields must agree.

- Population: [internal dataset path]; table population; schema datasets/ukb/table-38565c9e35e7cb6c.json; eid, sex 31-0.0, age 21022-0.0.
- Assessment: [internal dataset path]; table assessment; schema datasets/ukb/table-901ef6c7ddce2d51.json; recruitment date 53-0.0, grip 46-0.0/47-0.0, BMI 21001-0.0, and all inherited policy/stress fields.
- Biological samples: [internal dataset path]; table biological_samples; schema datasets/ukb/table-c6b666d905f3b02f.json; eid, urine albumin 30500-0.0, albumin result flag 30505-0.0, urine creatinine 30510-0.0, urine-creatinine flag 30515-0.0, serum creatinine 30700-0.0, cystatin C 30720-0.0, HbA1c 30750-0.0. Its catalog temporal_columns is empty; the physical header has 1,775 unique columns and no timing-like field.
- Health outcomes: [internal dataset path]; table health_outcomes; schema datasets/ukb/table-3cfae45e0905b0e3.json; paired inpatient diagnosis/date arrays 41270-0.0…41270-0.258 and 41280-0.0…41280-0.258, death dates 40000-0.0/40000-1.0.

The complete catalog is [internal dataset path], [source checksum]. The catalog’s UKB metadata says exact dates are server-only, field-instance.array indices are not elapsed time, and the source has no verified narrative, imaging, waveform or sequence-variant modalities.

## Verification contract

The executable output must retain the three parent workflow blocks and add resource_vector_audit and eligible_population_throughput:

- verify exact O and V membership, |M_p|=|O_p|-|V_p|, coverage, exact n_p, and selected counts;
- verify W1 reports (|O_p|,n_p), W0 reports (0,n_p), and no scalar combined resource cost is invented;
- verify W1 assay yields use denominator n_p, W0 all-O policies use denominator n_p, and throughput uses denominator |O_p|;
- verify no W1 estimate is divided by |V_p|, no W0 estimate is mislabeled as a V estimate, and no cross-workflow efficiency claim is emitted;
- verify no G_V estimate is called immediate pre-UACR;
- verify no UACR timing is inferred from instance 0, same-row storage, nonmissingness, recruitment date, cystatin availability or future outcomes;
- verify exact frozen scores, no refitting, no capacity shrinkage, locked outcomes, uncertainty, gates and result labels;
- include fixtures with different V coverage, all-O and V denominators, an adverse conditional W1 result, an adverse W0 result, supportive and inconclusive intervals, and correct arithmetic paired with unsupported efficiency, benefit, chronology, persistence, CKD, measured-GFR or equity claims.

The automatic verifier can establish source/header availability, joins, O/V/M membership, resource counts specified by the protocol, denominators, budgets, scores, outcomes, uncertainty, gates and workflow labels. It cannot establish actual UACR work-up burden, turnaround, refusal, cost, patient harm, clinical action, persistent/adjudicated CKD, measured GFR, benefit, equity or external transport. Those require timestamps, service-operation data, repeat measurements, clinical review and a prospective implementation or randomized testing-strategy study.

## Substantive advance and remaining uncertainty

The prior timing repair correctly prevented a result-defined V pool from masquerading as an observed pre-assay state. This child adds the remaining computable fairness guard: it makes explicit that W1 and W0 share only the cystatin-C capacity, while W1 also requires a full-O UACR work-up and excludes \(M_p\) from cystatin allocation. The added vector and O-denominator throughput report make selection and upstream resource use visible without pretending that UKB contains costs or chronology.

The experiment can now falsify conditional UACR-first assay value, immediate no-UACR assay value, or both, while preserving the exact frozen population, temporal endpoints, capacity, development locks, outcomes and evidence limits. It still cannot decide which workflow should be deployed. That stronger decision requires timed prospective workflow data, resource/utility measurement, repeat UACR and kidney-function measurements, clinical adjudication, equity review and a prospective implementation or randomized strategy study.
