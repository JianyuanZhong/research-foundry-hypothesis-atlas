> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Does a "disease-specific" plasma-protein signal survive adjustment for operative-treatment state? (UKB-Olink subset) — episode 18

Parent: [prior hypothesis] (episode 17, valid, mu 32.07, reference_delivery complete). Operation: evolve.
Status: **design + re-verified bindings; no association result is claimed in this episode.** Lineage: 12d74491 (ep17) <- cc21459667 (ep15) <- d96a1d29 (ep12) <- fd1b11ec (ep11) <- 5b53adfe (ep9) <- acb5dbc6 (ep8) <- c6bd99b3 (ep6) <- 8d03cc0a (ep3).

## Unresolved question and clinical importance
Plasma-proteomic screens nominate single circulating proteins (e.g. GDF15, CHI3L1, FABP1, IL-6/CRP family) as predictors/early-detection biomarkers of many diseases. The branch asks whether a robust cross-disease protein signal marks a **disease-specific process** (A) or a **shared systemic correlate** (B) [K2][K3]. Episodes 15 and 17 already eliminated chronological age/sex and disease co-occurrence/multimorbidity as rivals via case-case specificity. The strongest **uncovered** rival is now **treatment/intervention state**: many circulating proteins change with surgery/operative management, drugs and care intensity, so an apparently disease-preferential protein signal could be a *treatment/procedure correlate*. This distinction is consequential: it decides whether a candidate protein is a disease-biology target or only a marker of being under active operative treatment; circulating biomarker 'roles' (severity-associated vs predictive vs pharmacodynamic) are known to be conflated [K1].

## Verified bindings (inspected read-only 2026-10-13, this episode)
- Proteins: `[internal dataset path]` -> 53,014 rows; `n_eid` + 2,923 gene-symbol protein columns (NPX relative units). Binding `[UKB data file]` (sha256 922b2fea...); raw source `[UKB data file]` (olink.csv.gz, sha256 0834ab16...).
- Clinical: `[internal dataset path]` -> 502,250 rows; `n_eid`, `n_31_0_0` (sex), `n_21003_0_0` (age at recruitment), `s_41270_0_{0..258}` (ICD-10 codes), `s_41280_0_{0..258}` (first-inpatient diagnosis dates), **`s_41200_0_{0..55}` (OPCS operative-procedure codes; 446,464/502,250 non-null at index 0)**, `s_41210_0_{0..104}` (OPCS array). Binding `[UKB data file]` (sha256 79c23a5c...); raw source `[UKB data file]` (dta.csv.gz, sha256 f34a2b1b...).
- Join key: `n_eid`. olink n_eid (53,014 unique) INTERSECT dta n_eid = 53,014 (100%). No `n_eid` collisions.
- Temporal boundary: NONE. Direct check this episode: assessment-centre table `[UKB data file]` (key `eid`, holds `53-0.0` attendance date, `50-0.0` height) has **0 overlap** with olink/dta `n_eid` (olink ∩ assess = 0; dta ∩ assess = 0). Therefore no draw/birth/death date anchors the proteins -> strictly **cross-sectional / prevalent**; no incidence or washout claim.
- Namespaces NOT joined: `ukb671626*`, `ukb672073*` (disjoint from `n_eid`); `ukb483356f97e1e8132` etc. Data are read-only.

## Design (frozen estimand)
- Population: the 53,014 participants with Olink NPX AND dta rows (single `n_eid` namespace). Sex/age from `n_31_0_0`/`n_21003_0_0`.
- Outcomes: prevalent ICD-10 blocks from `s_41270_0_*` (3-char block granularity). Exclude symptom/history/administrative blocks (Z*, R*, V01-Y98 external causes kept only as a negative control). Documented exclusion list in `code_list.json`.
- New exposure/rival axis: OPCS codes from `s_41200_0_*` (+`s_41210_0_*`) summarised as (i) 3-char OPCS block flags and (ii) a procedure-count/intensity scalar. Define "procedure-associated disease blocks" as blocks whose cases are enriched for a specific OPCS block (documented, pre-specified list).
- Primary estimand: disease-preferential transfer gap `Delta_D = AUC(D vs unrelated disease set D')` on a **participant-level held-out half**, minus a co-occurrence-matched permutation null (permute D/D' labels within age-decile x sex x comorbidity-count strata). Report:
  - `Delta_D^raw` (no adjustment),
  - `Delta_D^casecase` (parent's diseased-only, age+sex+comorbidity adjusted),
  - `Delta_D^treat` = primary treatment contrast is **stratification by UNRELATED procedures only** (OPCS blocks not plausibly caused by the target disease D, via a pre-specified OPCS-block x disease-block exclusions list). A plain OPCS-*adjusted* estimate is reported only as a secondary, explicitly non-interpretable-as-null diagnostic (collider risk).
- Baseline vs learned alternative (same estimand): baseline = single 1-D shared-axis score (leave-one-protein-out first PC of the shared protein covariance); alternative = **elastic-net multi-protein** classifier fit on the discovery half. The learned alternative tests whether a *sparse, cross-validated protein combination* carries disease-preferential information the single shared axis loses (e.g. opposite-direction proteins cancelling in a 1-D score).
- Negative controls: (i) participants with no prevalent ICD-10; (ii) external-cause block V01-Y98 as an unrelated reference block; (iii) OPCS-present-without-target-disease check to confirm the procedure axis is not simply re-encoding disease.
- Split/provenance: fixed seed; `split_manifest.json` records assignment; axis fit only on the discovery half (leakage control).

## Falsification criteria
- **Supportive (A):** for >=1 pre-specified disease D, `Delta_D^treat` remains above the permutation null band after age+sex+comorbidity+OPCS adjustment.
- **Adverse (B):** `Delta_D^raw > 0` but `Delta_D^treat ~ null` -> the apparent specificity was operative-treatment state, not disease biology.
- **Inconclusive:** sparse co-diagnosis/OPCS strata, too few cases (<200), or unstable strata count; report as underpowered rather than as support.

## What each outcome would / would not establish
Supportive narrows but does not prove causality (still cross-sectional, prevalent, unmeasured covariates). Adverse would not disprove a disease-specific signal for *other* proteins/diseases. Neither establishes mechanism, incidence prediction, or clinical utility.


## Repair after blinded critique (episode 18 rev65)
The blinded reviewer preferred the parent (case-case comorbidity-matched) design and raised a valid objection: OPCS procedures are frequently *consequences* of the target disease, so adjusting for OPCS can induce collider/over-correction and make an adverse (null) result uninterpretable. Repair:
- The treatment rival is now tested by **stratification/contrast on UNRELATED procedures** (procedures whose OPCS block is not a plausible consequence of D, per a pre-specified OPCS-block x disease-block exclusions list). The disease-preferential gap is recomputed within the unrelated-procedure stratum and contrasted with the no-procedure stratum.
- Plain OPCS-*adjusted* `Delta_D` is demoted to a diagnostic only; a null there is NOT taken as evidence against disease specificity.
- Added control: an "OPCS-present-AND-unrelated-to-D" negative stratum; the adverse criterion now requires the *unrelated-procedure* contrast to collapse, which is not explainable by disease->procedure confounding.
All other bindings, controls, baseline-vs-elastic-net comparison and honest limits are unchanged. Key-reference claim mappings re-checked after this revision.

## Required solver outputs
`results.json` (per-D `Delta_D^raw/casecase/treat` + null bands + baseline-vs-elastic-net), `split_manifest.json`, `code_list.json` (ICD/OPCS inclusion + exclusions).

## Honest limits and missing evidence
Prevalent inpatient ICD-10 only (s_41270 under-ascertains); no draw/death/cancer date; comorbidity count = coarse severity proxy; procedure axis from inpatient OPCS under-ascertains outpatient/most primary-care treatment; unmeasured covariates (ethnicity, BMI, smoking, medication) absent from the joinable table; assessment-centre covariates unjoinable (disjoint namespace); ICD-10/OPCS block lists require clinical adjudication. No association result is claimed here.

## Three-demonstration dispositions (evidence-based, unchanged)
- Natural-history generative transformers (10.1038/s41586-025-09529-3): needs longitudinal trajectories + joined genetics namespace unavailable in this island -> parked (missing dependency).
- Longitudinal routine-data cancer detection (10.1016/j.cell.2026.07.009): main text unavailable (403/401) and needs longitudinal routine data -> parked.
- Bayesian longitudinal EHR+genetics (10.1038/s41586-026-10780-5): needs a joined longitudinal genetics namespace -> parked.
Expert seeds ukb-03..40 remain blocked by the disjoint identifier namespace; preserved as context.

## Method comparison record
Chosen: evolved cross-disease transfer design with a **new OPCS treatment-rival adjustment**, on the same estimand, baseline (1-D shared axis) vs **elastic-net** learned alternative. Not chosen (deferred): a pQTL/cis-MR target test using the island's `olink_rsid_map_*` and `ukb-e5-*` clump files — deferred because the island contains no individual-level genotype and no SNP->disease GWAS, so a causal MR estimand is not executable here (specific missing dependency documented). Revisit if genotype/GWAS inputs are admitted.

## Compact bibliography (key works)
- [K1] Lewandowska JA, Owczarczyk-Saczonek A, Nedoszytko B. Inflammatory Biomarkers for Assessing Treatment Response in Psoriasis: A Narrative Review. Int J Mol Sci 2026;27(16):7221. PMID 42653245. DOI 10.3390/ijms27167221. (abstract_only)
- [K2] Guan Y, Shen J, Li L, et al. A Circulating Proteomic Signature of Allostatic Load Is Associated with Multisystem Disease and Mortality. Proteomes 2026;14(3):47. PMID 42784208. DOI 10.3390/proteomes14030047. (abstract_only)
- [K3] Luo Y, Xiao YL, Chen JH, et al. Proteomics of aging: biomarkers for physiological systems and diseases. Front Aging 2026;7:1895104. PMID 42666595. DOI 10.3389/fragi.2026.1895104. (abstract_only)
