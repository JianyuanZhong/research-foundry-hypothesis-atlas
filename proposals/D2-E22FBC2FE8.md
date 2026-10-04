> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# A benefit-axis identifiability gate for context-selective MerTK perturbation

Status: substantive evolution of `[prior hypothesis]`; planned Harbor experiment only. No molecular screening, model fitting, or scientific result has been executed in this episode.

## Scientific opening, supported claim, and unresolved claim

The inspected evidence supports a bounded biological prior: MerTK-positive/TREM2-high or LYVE1-positive synovial macrophage states are associated with rheumatoid-arthritis remission and can induce synovial-fibroblast repair [K1]. A distinct HBEGF-positive inflammatory macrophage state can promote fibroblast invasiveness through tissue cross-talk [K2]. Fibroblast inflammatory programs are heterogeneous and niche-linked [K3]. These observations motivate target prioritization, but they do not show that inhibiting MerTK selectively harms the resolution-like context, nor that the same context carries a measurable clinical benefit in the configured assays.

The parent made the harm estimand explicit: in E-MTAB-8873, exact MerTK-inhibitor exposure might increase an FLS inflammatory harm program more in the unambiguous MerTK/CD206-positive than in the negative coculture. Its consequential limitation is that this is harm-only. A target can have a selective harm signal without a demonstrated benefit axis, and the available remission/resistant atlas might be mistaken for an external validation if incompatible units are forced together.

The smallest scientifically meaningful evolution is therefore not to add an arbitrary net-benefit score. It is to add a prespecified benefit-axis identifiability gate:

> Exact MerTK-inhibitor exposure has a larger FLS inflammatory harm effect in the eligible Mpos than Mneg coculture, but a MerTK-specific benefit-versus-harm prioritization is supportable only if an independently fitted remission-versus-resistant macrophage state axis is reproducible under donor holdout, has a verified target annotation, and can be linked to the measured Mpos/Mneg context without cross-assay donor or unit substitution.

The executable primary hypothesis is the narrowed harm claim. The benefit clause is a falsifiable gate and a required decision condition, not an established conclusion. With the currently frozen files, the benefit gate is expected to be blocked by feature namespace and context incompatibility; that is a planned identifiability outcome, not a screening result.

Clinical importance: deciding whether to preserve or activate MerTK-like resolution states requires evidence that perturbation harm is context-selective and that the selected context is clinically relevant. A supportive harm result alone justifies orthogonal target-engagement and functional experiments; it does not justify a patient-selection rule, treatment, direct mechanism, or clinical benefit claim. A benefit gate that remains blocked prevents over-prioritizing a target on a one-sided expression endpoint.

## Data bindings, source lineage, and temporal boundaries

The immutable catalog is `[internal dataset path]`, catalog [source checksum]; snapshot `core-molecular-20261003`. The prepared matrices are derived views with lineage recorded in the catalog; they are not additional biological replicates. All joins below are source-local. No identifier is joined between assays.

### E-MTAB-8873: primary FLS harm population

Prepared inputs:

- Counts: `[internal dataset path]`, [source checksum]. Schema is `feature` plus 33 sample-ID columns and 445 measured transcript rows. Required features are `IL6|NM_000600.4|Reference_end`, `MMP1|NM_002421.3|Reference_end`, `MMP3|NM_002422.4|Reference_end`, `MMP14|NM_004995.3|Reference_end`, with `MERTK|NM_006343.2|Reference_end`, `MRC1|NM_002438.3|Reference_end`, `TREM2|NM_018965.3|Reference_end`, `SPP1|NM_000582.2|Reference_end`, `IL1B|NM_000576.2|Reference_end`, `MMP12|NM_002426.5|Reference_end`, and `MMP13|NM_002427.3|Reference_end` retained as prespecified contrasts.
- Design: `[internal dataset path]`, [source checksum]. Schema fields are `sample_id`, `donor_id`, `donor_status`, `other_donor_id`, `age`, `sex`, `tissue`, `cell_type`, `condition`, `treatment`, `source_metadata`, and `cells`. Join only `design.sample_id = counts.feature-header sample ID).
- Registry: `[internal dataset path]`, [source checksum]). The exact entry says 33 samples, 445 features, no verified single donors, targeted assay, pseudobulk FLS/coculture, and ordinary donor t-tests disabled.

Primary rows are restricted to `tissue=synovial membrane`, `cell_type=type B synovial cell`, co-culture, exact inhibitor or untreated exposure, and unambiguous single-context labels. The exact four-cell comparison is:

- `R1_SA256A_FLS_SA259A_Mneg_Inhibitor`, donor membership `SA256A, SA259A`, treatment `macrophages pre-treated with MerTK inhibitor`, cells 432.
- `R1_SA256A_FLS_SA259A_Mneg`, the same membership, treatment `none`, cells 491.
- `R1_SA256A_FLS_SA259A_Mpos_Inhibitor`, the same membership, treatment `macrophages pre-treated with MerTK inhibitor`, cells 283.
- `R1_SA256A_FLS_SA259A_Mpos`, the same membership, treatment `none`, cells 368.

The R1 `SA260R` Mpos inhibitor row is `donor_id=SA256A`, while its untreated counterpart is `SA256A | SA256A, SA260R` with a metadata conflict; both are sensitivity-only. The R2/R5 `Mpos_preInhibitor` rows are a separate tier and are never silently substituted for exact inhibitor rows. Mixed `1Mpos/3Mneg` and `3Mpos/1Mneg` rows are composition controls, not clean context labels. FLS-only rows and LPS rows are controls. There is no machine-readable time field; the temporal boundary is the single recorded assay condition, so no longitudinal, transition, or dose/time claim is allowed.

Source lineage read and retained in the catalog includes `E-MTAB-8873/E-MTAB-8873.sdrf.txt`, [source checksum], and the relevant RSEC members: `R1_SA256A_FLS_SA259A_Mneg_Inhibitor_RSEC_MolsPerCell.txt.gz` (`[source checksum]`), `R1_SA256A_FLS_SA259A_Mpos_Inhibitor_RSEC_MolsPerCell.txt.gz` (`[source checksum]`), `R1_SA256A_FLS_SA259A_Mneg_RSEC_MolsPerCell.txt.gz` (`[source checksum]`), and `R1_SA256A_FLS_SA259A_Mpos_RSEC_MolsPerCell.txt.gz` (`[source checksum]`). The FLS-only, LPS, mixed, metadata-conflicted, and preInhibitor members are retained as controls/sensitivity lineage, not added observations.

### E-MTAB-8316: source-local paired perturbation check

- Counts: `[internal dataset path]`, [source checksum]; schema is `feature` plus 12 sample IDs and 58,302 Ensembl rows.
- Design: `[internal dataset path]`, [source checksum]; fields are `sample_id`, `donor_id`, `other_donor_id`, `donor_status`, `condition`, `treatment`, `source_metadata`, `tissue`, `cell_type`, `age`, `sex`, and `unit_definition`.
- Exact source-local pairs are MK11/MK12, MK15/MK16, MK19/MK20, MK23/MK24, MK3/MK4, and MK7/MK8, each `none` versus `UNC106238`. The verified FLS donor clusters are SA114, SA051, SA104, and SA049; monocyte donors 1533, 1534, 1601, 1602, 1462, and 1463 are nested. The biological unit is the FLS donor cluster with nested monocyte donor, not 12 independent donors. There is no Mpos/Mneg context field and no time field.
- Source lineage is `E-MTAB-8316/MK_readcountMatrix.txt.gz` (`[source checksum]`) and `E-MTAB-8316/E-MTAB-8316.sdrf.txt` (`[source checksum]`).

Define only the source-specific paired response `d_{f,m,g}=log2CPM(UNC106238)-log2CPM(none)`, averaged within FLS cluster after preserving nested monocyte structure. It is not the primary FLS harm score, not a common endpoint, and never a cross-source donor join. The registry gate requires protocol/compound identity, paired-unit confirmation, a named frozen Ensembl-to-gene map for gene-level target claims, and readout compatibility. Current prepared inputs pass pairing/nesting but fail the configured feature-map and Mpos/Mneg-context requirements. The planned result is therefore a compatibility report or blocked status, not an external validation.

### E-MTAB-8322: benefit-axis feasibility population

- Counts: `[internal dataset path]`, [source checksum]; schema is `feature` plus 27 sample IDs and 33,694 Ensembl IDs. The inspected header begins `feature,HC0547,HC0572,HC0701,HC0732,NaiveSA131,...,RemSA132,...,ResistantSA144,...`; no configured feature map is present.
- Design: `[internal dataset path]`, [source checksum]; fields are `sample_id`, `donor_id`, `donor_status`, `other_donor_id`, `age`, `sex`, `tissue`, `cell_type`, `condition`, `treatment`, `source_name`, and `cells`. Join only by sample ID to the counts header.
- The macrophage-only cross-sectional labels are 7 remission rows (`RemSA132, RemSA160, RemSA161, RemSA174, SA159, SA168, SA225`) and 6 resistant rows (`ResistantSA144, ResistantSA145, ResistantSA151, ResistantSA166, SA222, SA227`). Healthy controls, naive RA, and undifferentiated arthritis are not part of the primary remission-versus-resistant fit. `SA149P` and `UPASA149` have `possible_related_or_repeated_donor_exclude_inference` and are excluded. The biological unit is verified donor-level macrophage pseudobulk; this is not a whole-tissue or longitudinal transition dataset.
- Source lineage is `E-MTAB-8322/E-MTAB-8322.sdrf.txt` (`[source checksum]`) plus per-donor matrix/barcode members. Relevant remission matrices are `RemSA132.matrix.mtx` (`[source checksum]`), `RemSA160.matrix.mtx` (`[source checksum]`), `RemSA161.matrix.mtx` (`[source checksum]`), `RemSA174.matrix.mtx` (`[source checksum]`), `SA159.matrix.mtx` (`[source checksum]`), `SA168.matrix.mtx` (`[source checksum]`), and `SA225.matrix.mtx` (`[source checksum]`). Resistant matrices are `ResistantSA144.matrix.mtx` (`[source checksum]`), `ResistantSA145.matrix.mtx` (`[source checksum]`), `ResistantSA151.matrix.mtx` (`[source checksum]`), `ResistantSA166.matrix.mtx` (`[source checksum]`), `SA222.matrix.mtx` (`[source checksum]`), and `SA227.matrix.mtx` (`[source checksum]`). The shared genes files are `*.genes.tsv` [source checksum]; barcodes are source-specific and retained by the catalog.

The atlas can test whether a remission-versus-resistant expression axis is reproducible, but it cannot currently establish that the axis is MerTK-positive, align it to the 8873 Mpos/Mneg labels, or supply a clinical benefit endpoint. A named annotation map and a measured context bridge are explicit dependencies.

### GSE95588: artifact and timing-context comparator, not validation

Two prepared matrices are available:

- `[internal dataset path]`, [source checksum], with design `GSE95588_coculture_htseq_counts.design.json`, [source checksum]; schema is `feature` plus 8 columns `m_r1,mf_r1,mt_r1,mtf_r1,m_r2,mf_r2,mt_r2,mtf_r2), 23,710 source feature rows.
- `[internal dataset path]`, [source checksum], with design `GSE95588_d1d2d3d4_counts.design.json`, [source checksum]; schema is `feature` plus 70 columns including P1-P4 M/MT/MTF and drug-labelled variants, 23,710 source feature rows.
- The feature-map members are `GSE95588_coculture_htseq_counts.txt.gz.feature-map.json` [source checksum] and `GSE95588_d1d2d3d4_counts.txt.gz.feature-map.json` [source checksum]. GSM metadata is `GSE95588.gsm-metadata.json`, [source checksum].

The registry design marks every prepared row `donor_status=unresolved` and `donor_id=null`; its exact mapping note says column labels alone do not verify donor identity. The source lineage is `GSE95588/GSE95588_coculture_htseq_counts.txt.gz` (`[source checksum]`), `GSE95588/GSE95588_d1d2d3d4_counts.txt.gz` (`[source checksum]`), `samples.soft` (`[source checksum]`), and `series.soft` (`[source checksum]`). The registry also states that the coculture r1/r2 material includes earlier GSE57723 data and cannot be counted as independent validation of that study. The source metadata describes one-day TNF exposure, but there is no verified donor/time field in the prepared design; no longitudinal inference is permitted.

GSE95588 is used only for descriptive concordance and negative-control planning after a GSM/donor gate. It cannot repair the 8873 rank deficiency, demonstrate MerTK perturbation, or serve as independent validation. Duplicate/date-like feature labels must be resolved by the frozen feature maps; no guessed correction or row merging is allowed.

## Estimands and identifiability gates

Normalize each source separately to log2(CPM+1), preserving feature IDs and never imputing absent genes.

Primary harm outcome is
`H_s = mean(z(IL6), z(MMP1), z(MMP3), z(MMP14))`,
where z parameters are frozen from eligible unambiguous untreated exact-context co-culture rows. The primary estimand is
`Delta_H = [E(H | exact inhibitor,Mpos)-E(H | untreated,Mpos)] - [E(H | exact inhibitor,Mneg)-E(H | untreated,Mneg)]`.
Report each component, plus MERTK/MRC1/TREM2/SPP1 and IL1B/MMP12/MMP13 contrasts. This is a descriptive/associational perturbation interaction under a pseudobulk assay, not a clinical or causal treatment effect.

Before fitting, emit `harm_gate.json` with: row counts for each treatment/context cell; exact counterpart availability; donor-membership incidence matrix rank; whether any cell requires mixed, preInhibitor, metadata-conflicted, or random-split rows; and model estimability. The gate fails if it relies on ambiguous mixed rows, preInhibitor rows, the conflicted SA260R untreated row, random row split, or independent-donor assumptions. With the verified design, only one same-membership R1 pair supplies all four exact cells, so a population-level interaction is not automatically identified. Rank failure or a non-estimable interaction returns inconclusive, never a zero.

The secondary atlas estimand is a source-local remission-versus-resistant state contrast, not a target effect:
`B_f = mean(log2CPM_f | verified remission donors) - mean(log2CPM_f | verified resistant donors)`,
with uncertainty clustered at donor and with the two related/unresolved SA149 rows excluded. B is a state-association axis, not a treatment benefit or transition effect. The benefit gate requires: (a) the Ensembl feature map is present and frozen; (b) target genes and a prespecified resolution module are actually measured; (c) a donor-holdout model/contrast is stable; and (d) an explicit bridge to the 8873 Mpos/Mneg context is available. Current files fail (a) and (d), so the full benefit-versus-harm estimand is not identified.

For 8316, estimate source-local paired d-vectors only after compound/protocol and feature-map checks. For GSE95588, produce a mapping/feature-quality report and descriptive contrasts only unless donor and GSM identity are independently verified. Neither source is pooled with 8873 or 8322.

## Baseline and substantive alternative

Both alternatives use the same prepared inputs, frozen row filters, normalization, biological-unit definitions, donor/cluster holdouts, and prespecified outcomes.

Simple baseline:

1. On 8873, calculate the paired four-cell `Delta_H` and component contrasts with an incidence-matrix paired-score model. Use membership-cluster bootstrap only when at least two admissible clusters exist; otherwise report the exact contrast, rank, and an honest non-population uncertainty status. Use leave-one-round and leave-one-membership sensitivity only as applicable. This baseline is transparent and auditable, but loses correlated marker structure.
2. On 8322, estimate feature-wise `B_f` and a nearest-centroid remission-versus-resistant score after a training-only variance filter, only if the annotation/measurement gate passes. Fit target is the remission versus resistant label; hold out one verified donor at a time and report held-out balanced accuracy/log loss, donor-bootstrap intervals, and sign stability. This is a feasibility state axis, not a benefit outcome.
3. On 8316, report paired within-cluster d-vectors and on GSE95588 report only gated descriptive contrasts. No donor t-tests, pooled coefficients, or cross-source donor matches.

Substantive alternative:

- On 8873, fit a cross-classified multivariate partial-pooling model to IL6/MMP1/MMP3/MMP14 with shared harm factor, feature-specific treatment/context/interaction effects, and FLS/macrophage membership effects represented by an incidence matrix. Retain target/context marker features as contrasts. The fitted target remains `Delta_H`; the alternative asks whether the harm signal is a coherent multivariate program and whether uncertainty widens when membership dependence is respected.
- On 8322, if the feature-map and measurement gates pass, fit a sparse multivariate remission-versus-resistant model (elastic-net logistic or a low-rank factor model selected before fitting) to the same Ensembl matrix. Target is the same remission/resistant label, not drug response. Use leave-one-verified-donor-out validation, donor-cluster bootstrap, held-out log loss/AUROC/balanced accuracy, feature-sign stability, and calibration. The alternative can reveal a correlated state program that nearest-centroid scoring loses; it cannot establish a MerTK mechanism without annotation and context bridge.
- On 8316, a multivariate paired response is secondary and source-local only after the same protocol/feature gates. GSE95588 is not used to rescue a result with unresolved donor mapping.

The alternative is scientifically useful because it tests whether a putative harm or remission state is a coherent biological program rather than a single marker or one row. It is deferred automatically when the relevant gate fails; complexity cannot repair missing units, labels, or features. A neural predictor is not selected: predictive gain would not identify a MerTK interaction or clinical benefit. Revisit a hierarchical cross-assay model only after a named common feature map, same endpoint, verified context, intervention identity, and compatible biological units are obtained.

Approximate future solver resources: CPU only, 4-8 cores and <16 GiB RAM for 8873; 8-16 cores and 16-64 GiB RAM for repeated sparse/low-rank fits on 27 x 33,694 atlas data; approximately minutes for the baseline and 10-60 minutes for donor-held-out alternatives, unmeasured in this episode. GPU is deferred because the limiting issue is identifiability, not matrix scale. This is a planning estimate, not an executed benchmark. The configured planning envelope is 16 CPUs, 8 GPUs, 262,144 MiB and 28,800 seconds; no GPU or screening job is required here.

## Controls, falsification, and interpretation

Controls are fixed before fitting:

- FLS-only untreated/inhibitor rows test whether an apparent signal is a direct FLS or capture effect rather than macrophage-context interaction.
- LPS-pretreated Mpos/Mneg rows test whether generic macrophage activation reproduces the context pattern.
- Mixed-cell-composition rows test composition sensitivity but never define a clean context.
- Exact versus preInhibitor and R1/R2/R5 round/tier comparisons are sensitivity analyses, not pooled replication.
- MERTK/MRC1/TREM2/SPP1 and IL1B/MMP12/MMP13 components test coherence and competing inflammatory programs.
- 8316 paired none/UNC106238 and GSE95588 drug/TNF labels are source-local perturbation or timing comparators only; they are not MerTK validation.

Freeze a material harm threshold of 0.5 SD of H before fitting. A harm-supportive result requires positive `Delta_H` above that threshold with uncertainty supporting the threshold, coherent components, stable admissible mapping/round sensitivities, and no matching selective pattern in LPS or FLS-only controls. It supports follow-up with balanced donor pairs, orthogonal MerTK protein/phospho-readouts, genetic perturbation, viability, efferocytosis, secreted mediators, and direct FLS invasion/matrix-degradation assays. It does not establish direct target engagement or clinical benefit.

A full target-prioritization-supportive result additionally requires a non-blocked benefit gate: a reproducible donor-held-out remission-versus-resistant atlas axis, verified annotation including the target, and a separately obtained context bridge. Even then, it supports a next experiment, not a net clinical benefit estimate. Under the current files, the honest expected status is harm result plus benefit-gate blocked/inconclusive.

Adverse evidence includes a nonpositive harm interaction, Mneg harm at least as large as Mpos harm, generic LPS/FLS-only mimicry, instability driven by one membership, or discordance after a valid source-local 8316 gate. This weakens the selective-harm rationale and favors generic inflammation, composition, assay, timing, or off-target explanations. A weak or non-reproducible atlas state axis is adverse to the *benefit* claim but does not refute the harm interaction.

Inconclusive evidence includes rank/overlap failure, dependence on mixed/preInhibitor/conflicted rows, uncertainty spanning zero or the material threshold, unresolved donor/GSM mapping, missing Ensembl annotation, absent Mpos/Mneg bridge, or a cross-source estimand that must be invented. Inconclusive means obtain balanced matched Mpos/Mneg donor pairs with dose, exposure time, viability, target engagement, efferocytosis, secreted mediators, and FLS functional endpoints; it is not evidence for or against a drug.

Harbor can check source-local joins, required feature presence, exact row filters, incidence rank, held-out split integrity, paired contrasts, uncertainty calculations, gate status, and rule-consistent conclusion links. It cannot establish clinical benefit, direct molecular mechanism, spatial localization, viability, therapeutic window, or independent biological validity; these require expert adjudication, missing measurements, orthogonal experiments, or another study.

## Scientific deliverable

Newly fitted or computed outputs must include:

- `analysis_manifest.json`: catalog and input hashes, source-local filters, exact included/excluded rows, and temporal boundaries.
- `harm_gate.json`: cell counts, incidence matrix/rank, estimability, and reasons for any failure.
- `effects.csv`: `Delta_H`, component effects, marker contrasts, and uncertainty status.
- `controls.csv` and `sensitivity.csv`: FLS-only, LPS, mixed-composition, tier, round, and membership checks.
- `atlas_benefit_gate.json`, `atlas_effects.csv`, and `atlas_holdout.csv`: remission/resistant state contrast, map/measurement status, donor-holdout metrics, and explicit blocked status where required.
- `source_compatibility.json`: 8316 and GSE95588 protocol, feature, donor, context, and pooling decisions.
- `method_comparison.json`: baseline versus multivariate alternative, targets, splits, uncertainty, resource timing, and fit/defer reason.
- `results.json`: every conclusion linked to computed output rows and tagged supportive, adverse, or inconclusive.

Completion is not a readiness report. It requires the primary harm estimand or a formal non-identifiability report, the benefit-axis gate result, controls/sensitivities, method comparison, and conclusions that preserve uncertainty. No result is claimed in this proposal.

## Evidence limits and alternatives not selected

Unavailable or inadequate evidence remains explicit: no clinical outcomes, remission transition data, dose-response, exposure-time field in the prepared assays, viability, protein/phospho-MerTK, efferocytosis, secreted mediators, spatial localization, direct FLS invasion/matrix-degradation readout, verified common annotation across all assays, or balanced independent Mpos/Mneg FLS-macrophage cohort.

The atlas extension is retained as a bounded feasibility branch because remission/resistant donor labels are present and can test whether a state axis is reproducible. It is not promoted to a benefit claim because the required feature map and context bridge are absent. GSE95588 is retained as an artifact/timing comparator because its feature maps and rich treatment labels may inform controls, but it is not selected as validation because donor identities are unresolved and coculture r1/r2 includes GSE57723 material. A pooled hierarchical cross-assay model is deferred because the endpoints, feature namespaces, contexts, and units differ. A neural model is deferred because no added information would distinguish mechanism from assay structure at this sample size. Evidence that would justify revisiting these decisions is a frozen Ensembl-to-gene map, verified target/intervention identity, balanced matched contexts, donor/GSM mapping, and orthogonal protein/functional data.

## Key inspected works

[K1] establishes a remission-associated MerTK-positive macrophage state and fibroblast repair association; it does not establish the interaction or benefit axis tested here.

[K2] supplies a consequential inflammatory macrophage–fibroblast rival; it does not establish MerTK specificity or equivalence of the configured assay units.

[K3] bounds the FLS harm endpoint as heterogeneous and niche-linked; it does not validate the targeted score, atlas bridge, or clinical benefit.

Exactly three distinct inspected works are attached as UTF-8 excerpts in `evidence-K1-alivernini-2020.txt`, `evidence-K2-kuo-2019.txt`, and `evidence-K3-korsunsky-2022.txt`. They are reused unchanged from the parent’s inspected evidence; no inaccessible full text or supplementary method is claimed.
