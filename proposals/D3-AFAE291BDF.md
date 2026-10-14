> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Directional macrophage-to-fibroblast communication in OA-like cocultures

Seed: D3-M2
Domain: Disease Mechanisms & Pathway Hypotheses
Status: hypothesis-stage proposal; no confirmatory analysis has been executed.

## Question and clinical importance

In osteoarthritis-like tissue, macrophages and fibroblast-like synoviocytes (FLS) can reinforce one another through paracrine signaling. The consequential unresolved question is whether a measured FLS response is better explained by directional macrophage-to-FLS communication or by an alternative, including endothelial-cell input, donor-specific baseline state, or simply changes in measured cell composition.

Resolving this matters because it changes the next mechanistic experiment and could inform whether anti-inflammatory strategies should target macrophage signaling, FLS intrinsic state, or tissue composition. It is not a treatment recommendation.

## Evidence opening

The seed points to paired coculture and inhibitor conditions in E-MTAB-8316 and E-MTAB-8873, plus GSE95588 coculture data. The available source catalog lists condition-specific RSEC matrices and design metadata, including macrophage-positive/negative and inhibitor conditions.

OA is a heterogeneous whole-joint disorder in which chronic low-grade inflammation is embedded within mechanical loading, metabolic dysfunction, synovitis, osteochondral remodeling, cellular senescence and pain sensitization rather than acting as a single-cytokine process [K1]. The NEBE framework organizes evidence around cellular nodes, communication edges, boundary conditions and emergent disease states [K1].

Post-GWAS interpretation of OA increasingly requires integration with single-cell biology because many risk loci likely act through sterile inflammatory remodeling, regulatory and inflammatory chondrocyte states, and tissue-stress biology rather than through large disease-stage expression shifts [K2].

PDGFRβ may influence stem cell behavior indirectly by modulating vascular stability, matrix remodeling, metabolic gradients, and biomechanical signaling [K3]. Receptor-specific functional evidence for PDGFRβ in limbal microenvironmental cells remains limited, and the limbal component is presented as a hypothesis-generating framework rather than as established evidence [K3].

## Hypothesis

In OA-like cocultures, a measured FLS response is better explained by directional macrophage-to-FLS communication than by endothelial-cell input, donor-specific baseline state, or changes in measured cell composition.

## Falsifiable test

If the inhibitor abolishes the FLS response, this supports directional macrophage-to-FLS communication. If the response persists despite inhibition, alternative explanations (endothelial input, donor baseline, composition changes) are more likely. If the response is absent in both conditions, the hypothesis is not supported.

## Data bindings

- E-MTAB-8316: [internal dataset path]; metadata [internal dataset path]
- E-MTAB-8873: [internal dataset path]; metadata [internal dataset path]
- GSE95588_coculture_htseq_counts: [internal dataset path]; metadata [internal dataset path]

## Method comparison

Baseline: donor-aware paired comparison of FLS expression in macrophage-positive vs. macrophage-negative conditions.
Alternative: inhibitor perturbation test to discriminate directional communication from alternative explanations.

## Key references

[K1] Zhang Z, Wei J, Du F, Geng S. The osteoarthritis inflammatory ecosystem: a node-edge-boundary-emergent framework toward precision stratification and therapeutic hypothesis generation. Front Med (Lausanne). 2026;13:1976217. doi:10.3389/fmed.2026.1976217.
[K2] Lu C, Wang L, Cao X, Zhao K, Yin N, Zhang D. Integrated post-GWAS, single-cell, and functional analyses prioritize TCTN2 at an osteoarthritis locus associated with innate immunity-related cartilage remodeling. Front Immunol. 2026;17:1883412. doi:10.3389/fimmu.2026.1883412.
[K3] Liao S, Li G. PDGFRβ in Stem Cell Microenvironments: Cross-Tissue Evidence and Hypotheses for the Limbal Stem Cell Niche. Stem Cells Int. 2026;2026:1536168. doi:10.1155/sci/1536168.

## Limitations

- Targeted assay; unmeasured genes are unavailable.
- Mixed/reused donors require appropriate modeling.
- No twelve-independent-donor claim.
- Metadata cell-type labels and experimental readout must be reconciled with protocol before cell-specific claims.
