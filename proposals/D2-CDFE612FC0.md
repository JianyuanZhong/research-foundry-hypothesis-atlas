> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Lead working proposal — Episode 29 (therapeutic_targets, domain 2)

Status: draft; branch = restart (context: mature E-MTAB-8873 MerTK/CD206pos→FLS in-vitro brake branch).
Owner: Lead. Delegated dossier: work/gen-state/.

## Unresolved question
In human RA synovium, does the MerTK/CD206pos "resolution" effector program identified by
Alivernini et al. correspond to a DISCRETE synovial-macrophage cell STATE, or is it merely the
low extreme of one continuous macrophage inflammatory-polarization axis? The mature island branch
tested a MerTK-brake → FLS-effector relation only in an in-vitro coculture (E-MTAB-8873) and in
macrophage pseudobulk disease groups (E-MTAB-8322) where composition vs state-resolution could not
be separated. The never-used per-donor 10x matrices of E-MTAB-8322 allow a cell-state-resolved test.

## Why it matters
If the resolution program is a discrete state, then "resolution macrophages" are a countable,
targetable cell population and their per-donor fraction is a candidate biomarker; if it is a
continuum, then state-fraction framing is a composition artifact and prioritization should shift
to the dominant inflammatory program. This changes which target/cell-population a follow-up
experiment or clinical stratification would pursue.

## Leading claim vs strongest rival
- H_state: resolution program is a discrete state (mixture of >=2 components on a pre-registered
  resolution–vs–inflammatory axis) that survives detection-rate/ambient adjustment and replicates
  across donors; its per-donor fraction differs by clinical context.
- R_continuum/composition: a single continuum; apparent "state" is the low tail of one axis and
  context differences in fraction reflect tissue-inflammation load / cell-yield composition.
- R_technical: cluster structure is driven by per-cell UMI/complexity, ambient macrophage RNA, or
  donor/batch, not a biological state.
Discriminating observation: covariate-adjusted 2-vs-1 component mixture on the resolution axis AND
cross-donor stability of the discrete component. If the 2-component model does not beat 1 component
after detection/ambient adjustment, or the discrete component does not replicate across donors,
H_state is falsified.

## Bound data (read-only; verified this episode; sha256 in work/lead/bindings.json)
- E-MTAB-8322.design.json — 27 macrophage records; fields sample_id, donor_id, donor_status,
  condition (HC / Naive / remission / resistant / Undifferentiated arthritis), age, sex, cells.
  sha256 4ef38a70...
- E-MTAB-8322.counts.tsv.gz (pseudobulk; join key sample_id) — secondary/context view.
  sha256 95bc3a96...
- Per-donor 10x triplets: [internal path]<SAMPLE>.{genes.tsv,barcodes.tsv,matrix.mtx}
  for the 27 samples (e.g., RemSA160 c5954507..., ResistantSA145 894d5050..., NaiveSA138
  822b25ae..., HC0547 2525bd90..., SA222 9386251b... genes.tsv 920b9e83...).
- Genes present: MERTK, MRC1, CD163, FOLR2, MARCO, LYVE1, CD68; effector MMP1/MMP3/MMP13/IL6/
  CXCL8/CCL2/TNF/IL1B; controls GAPDH/COL1A1. SELENOP absent.
- Relatedness caution: SA149/SA149P unresolved relatedness → excluded from independent-donor screens.

## Method comparison (baseline vs substantive alternative)
- Baseline: median-split / rank cells on a pre-registered resolution–vs–inflammatory score and test
  unimodality (dip-style tail check) with donor-clustered bootstrap — loses covariate structure.
- Alternative: per-cell QC- and ambient-adjusted mixture (1 vs >=2 components) on the same axis plus
  leave-one-donor-out cluster-identity stability — reveals whether discreteness is biological or an
  artifact of detection rate, and whether it is shared across donors. Justify selection by the result.

## Planned analysis / falsifiers (pre-registered; screening_status = planned)
Primary: per-donor fraction of the discrete resolution state under the adjusted 2-component fit.
F1 mixture: 2-component beats 1-component after adjusting for per-cell nUMI/nFeature and ambient
   macrophage-RNA fraction; F2 replication: discrete component recoverable in leave-one-donor-out
   across >=8 independent donors; F3 context: adjusted fraction ordered HC/remission vs naive/resistant
   with donor-level uncertainty (cross-sectional only — NOT a transition claim); F4 specificity:
   resolution-state signature must not be reproduced by a matched non-resolution macrophage control set.

## Outcomes
- Supportive: F1–F4 hold → discrete resolution state; prioritize state-fraction as a biomarker target.
- Adverse: 2-component fails after adjustment → continuum/tail explanation; deprioritize state framing.
- Inconclusive: structure sensitive to QC/donor subset or n too small → defer; needs deeper sequencing
  or external cohort. Cross-sectional groups cannot establish transitions; no clinical efficacy claim.

## Disposition of the three demonstrations
- cancer/ (supplement): not adopted — different disease/tissue; no binding here (scientific reason).
- bayesian/ (reporting summary): not adopted as a topic; its reporting discipline is noted.
- natural-history/ (41586_2025_9529): not adopted — non-synovial; no matching bound data.
Discovery here is data-bound to the RA synovium island, so these were dispositioned, not adapted.

## Open / unresolved
- Need K1–K3 inspected references (work/gen-state/key-references.json).
- Full single-cell execution is the FUTURE solver's deliverable; this proposal is discovery evidence.

## Inspected key works [K1] [K2] [K3]
[K1] Alivernini et al. 2020 Nat Med (doi:10.1038/s41591-020-0939-8): single-cell profiling of 32,000
synovial tissue macrophages resolves nine discrete phenotypic clusters whose frequencies differ by
clinical state (abstract inspected) - bounds the leading claim but does not itself test discretness of
the resolution axis after detection/ambient adjustment.
[K2] Zhang et al. 2023 Nature (doi:10.1038/s41586-023-06708-y): single-cell RA synovium atlas defining
inflammatory subtypes (title/author list + abstract opening inspected; partial capture) - the closest
independent atlas framework against which a synovial-macrophage resolution state must be placed.
[K3] Lin & Yu 2026 Adv Genet (doi:10.1002/ggn2.70045): cautions that equating computational clusters
with biological cell types is an inferential vulnerability and that strong mechanistic claims need
orthogonal validation (abstract inspected) - this bounds our claim: the discrete-state conclusion is
advanced ONLY if the adjusted 2-component mixture beats 1 and replicates across donor hold-outs.
