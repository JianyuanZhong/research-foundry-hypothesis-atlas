> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Do "disease-specific" plasma-protein signals survive a shared systemic/ageing axis, when the axis cannot be circular? (UKB-Olink, episode 4)

Parent: [prior hypothesis] (episode 3, valid, mu 31.0). Operation: evolve.
Status: design + data bindings verified against source files this episode; **no association results claimed**.
This episode's substantive advance is a verified reproducibility/integrity correction of the parent's temporal
binding, plus a fix to a circularity flaw in the parent's shared-axis construction.

## Verified bindings (probed this episode, source-level)
- Olink protein table `[UKB data file]` (from `olink.csv.gz`): 53,014 rows, key `n_eid`,
  2,923 gene-symbol protein columns. Original `olink.csv.gz` header = `n_eid` + 2,923 protein names,
  2,924 fields, **no date column**.
- Diagnosis-outcome table `[UKB data file]` (from `dta.csv.gz`): 502,250 rows. Only three
  non-array columns: `n_eid`, `n_31_0_0` (sex), `n_21003_0_0` (age at recruitment). ICD10/date arrays
  `s_41200_0_*` … `s_41283_0_*`, including `s_41270_0_*` (259 ICD10 code columns) and `s_41280_0_*`
  (259 first-diagnosis **date** columns). **No `53-0.0` draw date.**
- Join: Olink `n_eid` ∩ `dta n_eid` = 53,014 (full containment). Verified.
- Covariate/draw-date table `[UKB data file]` (ukb672073 Assessment_Center): 502,370 rows,
  key `eid`, with `53-0.0` (draw date), `21001-0.0` (BMI), `20116-0.0` (smoking), `21000-0.0` (ethnicity),
  `1558-0.0` (alcohol).

### Correction that invalidates the parent's temporal design
`dta n_eid` and the ukb672073 tables' `eid` are **disjoint identifier namespaces** (sample values
`1000019…` vs `1000014…`; pairwise intersection over ~502k × ~502k rows = **0**, and likewise for
`[UKB data file]`). The two groups are each ~502k rows, so they cannot both be the ~502k UKB
participants; they are distinct codings. `catalog.json` contains **no documented crosswalk** between them.
Consequences, verified:
1. The parent's blood-draw anchor `53-0.0` **cannot be joined to the Olink subset** — its claim that the
   draw date joins on `n_eid = eid` is false.
2. The parent's "missing covariates" (BMI/smoking/ethnicity) are not missing from the release; they exist
   in the *other* namespace and are therefore **not joinable** without a crosswalk.
3. Therefore the washout-restricted "incident after draw" contrast, and the reverse-causation rival the
   parent claimed to have resolved, are **not computable from the bound sources as written.**

## Unresolved question and clinical importance
Plasma-proteomic screens report single proteins (GDF15, IL-6/CRP family) as strong predictors of one
incident disease. It is unresolved whether such associations mark a **disease-specific preclinical
process** (A) or a **shared systemic sickness/inflammation/ageing axis** elevated before many diagnoses,
partly via reverse causation (B). This decides whether a circulating protein is a plausible
disease-specific early-detection target or only a generic risk/severity correlate. [K1] shows plasma
protein patterns encode many health states at once; [K2] shows broad shared age structure across 2,925
plasma proteins; [K3] defines the UKB-PPP platform/scale.

## Remaining, executable core (reduced claim)
What is computable in the Olink-compatible namespace: protein–outcome association breadth across many
ICD10 disease blocks, and the attenuation of that breadth after removing a shared axis — tested with the
circularity and age-rival fixes below. The temporal (reverse-causation) contrast is **out of scope** here
and is declared as required additional evidence.

## Design: baseline vs substantive alternative (same question)
- Baseline (B0): per-protein logistic/Cox association with each incident-disease block, adjusted for
  age+sex, BH-FDR across proteins. Produces a set of nominal protein–disease pairs ("specificity" hits).
- Circularity-free learned alternative (B1): estimate a low-rank **shared axis** across proteins by PCA,
  but compute each protein's attenuation using the shared axis estimated **leave-one-protein-out** (LOO),
  so the tested protein cannot define the axis it is tested against. The per-protein baseline cannot do
  this; it can only condition on a single pre-computed PCA score, which reintroduces the circularity.
- Discriminating rival (B2): the strongest non-mechanistic rival is that the "shared axis" is largely
  **chronological/nonlinear age**, not a sickness axis. Test: refit B0/B1 with a **natural-spline age term
  (4 df)** instead of linear age. If shared-axis attenuation disappears once age is flexible, the axis is
  age per se.
- Positive/negative control fixtures (bounded): a pre-specified positive control (a protein–outcome pair
  with well-established association, e.g. GDF15–diabetes block) must be detected; a negative control
  (age/sex-shuffled outcomes, or a randomly permuted protein) must not survive FDR.

## Split, estimand, uncertainty
- Derive the shared axis on one fold / with out-of-fold scores; evaluate associations on held-out
  participants (no leakage). Report bootstrap CIs and multiplicity control.
- Primary estimand: fraction of nominal (B0-significant) protein–disease pairs that (i) attenuate below
  threshold, (ii) lose significance, (iii) persist, after LOO shared-axis adjustment, with and without the
  flexible age term.

## Falsification criteria
- H_shared: after LOO-axis adjustment, most nominal pairs attenuate substantially (>50%) or lose
  significance, and this persists under the flexible-age model.
- H_specific: attenuation is small (<20%) and a majority of pairs persist at FDR control.
- Age-rival (B2): if attenuation is large under linear age but vanishes under age-splines, the shared
  axis is chronological age, not a sickness axis.
- Pre-specified supportive, adverse, and inconclusive (wide CIs / low event counts per block) outcomes.
  An imprecise null does not refute specificity.

## What would NOT be established
Association persistence is not mechanism; attenuation is not proof of reverse causation. The temporal
contrast, incidence vs prevalence adjudication, and any clinical-utility claim require (a) a documented
participant crosswalk to a blood-draw date (or an Olink-namespace draw date), (b) outpatient/GP
ascertainment (the arrays used are HES-style registrations and under-ascertain), and (c) external
replication and expert clinical adjudication. These are declared gaps, not assumed.

## Approximate budget
53k × 2,923 matrix ops → CPU-feasible; LOO PCA is O((p) × SVD) and is the dominant cost; fits are small.
No GPU required for the core fit; a bounded GPU slot is only relevant for large repeated bootstrap refits.

## Alternatives not chosen (preserved)
The parent's washout/incident-only design is parked, not deleted: it becomes executable if a documented
crosswalk or an Olink-namespace draw date is obtained. If a draw date becomes available, the temporal
contrast should be reinstated as the primary estimand.

## Key references
[K1] Williams et al. 2019, Nat Med, doi:10.1038/s41591-019-0665-2 (abstract inspected).
[K2] Lehallier et al. 2019, Nat Med, doi:10.1038/s41591-019-0495-2 (abstract inspected).
[K3] Sun et al. 2023, Nature, doi:10.1038/s41586-023-06563-x (metadata/abstract inspected; UKB-PPP platform).
