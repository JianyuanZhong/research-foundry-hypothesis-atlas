> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Context-dependent fibroblast response to macrophage conditioning

## Seed and question
Develops expert seed D2-T1 (`[prior hypothesis]`). The unresolved question is whether a fibroblast transcript response to a defined intervention is context-dependent on the macrophage phenotype present in the coculture, rather than being a uniform fibroblast response.

## Clinical importance
Fibroblasts are a major target of fibrotic disease, but their pathogenic program may be induced, amplified or restrained by macrophage signals. A target that is responsive only in a particular macrophage context could be a more selective intervention point than a target whose expression merely differs between disease and control. Resolving this question can prioritize candidates for perturbation and reduce false prioritization from a global expression contrast.

## Evidence and closest work
The available data include E-MTAB-8316 (four FLS donor clusters, six nested monocyte donors, twelve condition samples) and GSE95588 (coculture HT-Seq counts, including r1/r2 derived from earlier GSE57723 and therefore not independent validation). E-MTAB-8316 has an explicit FLS/monocyte context design; GSE95588 can be used for exploratory expression and donor-aware checks only after resolving duplicate/date-like gene labels and verified column-to-GSM/donor mapping.

The closest inspected works are:
- [K1] Froom ZSCS, Callaghan NI, Davenport Huyer L. (2025). Cellular crosstalk in fibrosis: Insights into macrophage and fibroblast dynamics. J Biol Chem, 301(6):110203. DOI: 10.1016/j.jbc.2025.110203.
- [K2] Liu T, Liu Y, Liu Y, Wen D, Sun J, Zhang Y, Gao Y, Zheng D. (2026). Extracellular vesicles in wound healing and scar formation: molecular regulation of macrophages, fibroblasts, and their crosstalk. Front Cell Dev Biol, 14:1917543. DOI: 10.3389/fcell.2026.1917543.
- [K3] Qiang P, Han L, Lv R, Dong Z, Ma T, Wang X, Xu Q. (2026). Macrophage-Fibroblast Crosstalk in Kidney Injury: A Narrative Review. Int J Mol Sci, 27(18):8173. DOI: 10.3390/ijms27188173.

No claim is made here that any of the three demonstration papers was read for this molecular question; their disposition is below.

## Hypothesis
In macrophage-conditioned fibroblast cocultures, the intervention-associated change in a candidate fibroblast target is larger (or opposite in direction) when fibroblasts are exposed to a pro-fibrotic macrophage state than when exposed to a non-pro-fibrotic/protective macrophage state, after accounting for donor and condition structure.

This is a hypothesis, not an observed result. The available expression data can test an association/context interaction; they cannot establish direct target causality or drug specificity.

## Design
1. Reconcile E-MTAB-8316 sample metadata with the protocol: identify FLS samples, monocyte donors, condition labels, repeated measurements and any vehicle/unstimulated controls.
2. Average repeated context measurements within each donor/condition before paired exploratory inference. Preserve donor dependence; do not treat twelve condition samples as twelve independent donors.
3. Define the macrophage context factor from verified condition labels (e.g., pro-fibrotic versus non-pro-fibrotic/protective), not from an inferred cell-state score unless the score is validated against the protocol.
4. For each candidate gene, estimate the intervention-by-macrophage-context interaction in a donor-aware model. A simple baseline is a paired donor-aware contrast of intervention versus control within each macrophage context, with context as a fixed effect. A substantive alternative is a donor-aware linear mixed model with donor random effects and context/intervention interaction; this can reveal whether the interaction is stable across donors rather than driven by one donor.
5. Use GSE95588 only as an exploratory expression screen after feature-map resolution. Do not call r1/r2 independent validation of GSE57723.
6. Falsification: no context-specific interaction after donor-aware adjustment, or the interaction is confined to one donor/condition and disappears under permutation of context labels. Supportive: a reproducible direction and magnitude difference across donors. Adverse: the intervention response is uniform across macrophage contexts, or the apparent context effect is explained by donor, treatment or composition.

## Competing explanations
- Donor heterogeneity: one donor may drive the apparent context interaction.
- Treatment/condition confounding: the intervention and macrophage context may not be orthogonal.
- Measurement/composition: targeted panels, pseudobulk summaries and duplicate gene labels can create apparent differences.
- Cell-state mislabeling: metadata labels must be reconciled with protocol before cell-specific claims.
- Selection: candidate genes selected from the same expression data are exploratory, not confirmatory.

## Data bindings
- E-MTAB-8316 counts: `[internal dataset path]`
- E-MTAB-8316 design: `[internal dataset path]`
- GSE95588 coculture counts: `[internal dataset path]`
- GSE95588 coculture design: `[internal dataset path]`

## Method comparison
- Baseline: donor-aware paired contrast within each macrophage context, with context fixed effect. This is transparent and directly interpretable.
- Learned/mechanistic alternative: donor-aware linear mixed model with donor random effects and context/intervention interaction. This can reveal donor stability and reduce false prioritization from a single donor. It is not a neural network; it is a mechanistically motivated mixed-effects model appropriate for the small, nested donor structure.
- Selection: the mixed model is preferred if donor heterogeneity is a real concern; otherwise the baseline is sufficient. A bounded diagnostic on the actual metadata will determine whether donor random effects are identifiable.

## Demonstration dispositions
- Delphi (natural history): not applicable to this molecular target-prioritization question; no disease-history trajectories or clinical event data are required.
- ALADYNOULLI (longitudinal latent structure): not applicable; the question is a context interaction in coculture expression, not a longitudinal patient trajectory.
- Oncoformer (multimodal EHR + imaging): not applicable; no imaging or longitudinal EHR data are available for this question.

## Unresolved and next steps
- Reconcile E-MTAB-8316 metadata with protocol to verify condition labels and donor structure.
- Resolve GSE95588 duplicate/date-like gene labels before naming targets.
- Run a bounded diagnostic on the actual metadata to determine whether donor random effects are identifiable.
