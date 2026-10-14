> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Corrected MerTK off-target control analysis on E-MTAB-8873 (D3-M2, ep13)

**Lineage:** targeted-repair child of `[prior hypothesis]` (ep12, executed MerTK
analysis, mu 25.0). Context-only board-top `candidate-75da3dd9` (D3-M3, unrelated branch) is NOT
a parent. Board revision 45.

## 1. Scientific question

Does the MerTK inhibitor (UNC106238) affect fibroblast-like synoviocytes (FLS) **directly**
(off-target), independent of macrophage contact?

The ep12 analysis (parent `candidate-dc57fbf5`) found that in FLS co-cultured with
MerTK/CD206**neg** macrophages, inhibitor pre-treatment produced a LARGER FLS transcriptomic
effect than in FLS co-cultured with MerTK/CD206**pos** macrophages, while Mpos vs
Mpos_Inhibitor was null (0 genes BH<0.05). Two competing explanations were left open:

- **(A) Off-target:** UNC106238 acts on FLS directly. Then FLS-only cultures with inhibitor
  should differ from FLS-only baseline, and part of the Mneg effect reflects this direct action.
- **(B) MerTK not the primary mediator:** the inhibitor has no direct FLS effect; the Mneg
  asymmetry is macrophage-conditioned or a single-sample artifact.

**The ep12 grouping error (now repaired):** ep12 declared "no true FLS-only + inhibitor control
exists". That is wrong. Verified from the design file, `R1_SA256A_FLS_Inhibitor` is an
FLS-ONLY culture with the MerTK inhibitor present, from the **same donor SA256A** as
`R1_SA256A_FLS_only` — exactly the paired off-target control. ep12 mislabeled it as
Mneg_Inhibitor.

## 2. Data (exact bindings)

- Counts: `[internal dataset path]`
  — 445 feature rows × 33 sample columns. Feature IDs preserved verbatim
  (`GENE|NM_xxxxx.x|Reference_end` / `...|PolyA_1`). 5 gene symbols (CD2, COL1A1, PGAM1,
  PRDM1, TNFAIP3) occur twice with distinct transcript IDs; **rows were NOT merged** —
  analysis unit is the 445 feature (440 unique symbols).
- Design: `[internal dataset path]`
  — 33 samples with `sample_id`, `donor_id`, `condition`, `treatment`.
- Transformation: `log2(counts + 1)` per feature (panel is a targeted, normalized-ish assay;
  no library-size normalization applied — see limitations).

**Corrected grouping (verified against design.json, written to `corrected_grouping.csv`):**

| Group | n | Samples |
|---|---|---|
| FLS_only | 5 | R1_SA256A_FLS_only, R2_SA257A_FLS_only, R2_SA258R_FLS_only, R5_SA263R_FLS_only, R5_SA266A_FLS_only |
| FLS_only_Inhibitor | 1 | R1_SA256A_FLS_Inhibitor (donor SA256A — paired with R1_SA256A_FLS_only) |
| Mpos | 8 | R1_SA256A_FLS_SA259A_Mpos, R1_SA256A_FLS_SA260R_Mpos, R2_SA257A_FLS_SA266A_Mpos, R2_SA257A_FLS_SA267R_Mpos, R2_SA258R_FLS_SA267R_Mpos, R5_SA263R_FLS_SA278R_Mpos, R5_SA266A_FLS_SA277A_Mpos, R5_SA266A_FLS_SA278R_Mpos |
| Mpos_Inhibitor | 4 | R1_SA256A_FLS_SA259A_Mpos_Inhibitor, R1_SA256A_FLS_SA260R_Mpos_Inhibitor, R2_SA257A_FLS_SA266A_Mpos_preInhibitor, R5_SA266A_FLS_SA277A_Mpos_preInhibitor |
| Mneg | 6 | R1_SA256A_FLS_SA259A_Mneg, R2_SA257A_FLS_SA266A_Mneg, R2_SA258R_FLS_SA266A_Mneg, R5_SA263R_FLS_SA277A_Mneg, R5_SA263R_FLS_SA278R_Mneg, R5_SA266A_FLS_SA277A_Mneg |
| Mneg_Inhibitor | 1 | R1_SA256A_FLS_SA259A_Mneg_Inhibitor |
| Mpos_LPS / Mneg_LPS / mixed | 1 / 4 / 3 | (not used in the four contrasts) |

## 3. Analyses EXECUTED (script `analysis_ep13.py`, log `ep13_run.log`)

Execution: scoped shell (timeout 120 s, elapsed ~14 s CPU, pandas/numpy/scipy/statsmodels).
`ehr_job_submit` was attempted first but rejected the `resources`/`inputs` argument shapes in
this adapter; the screening therefore ran in the scoped shell. **No managed compute job ID
exists; the screening_job_id in the experiment card records this honestly.**

### 3.1 PRIMARY — off-target test (FLS_only vs FLS_only_Inhibitor, donor SA256A)

`offtarget_paired_results.csv` (per feature: both sample values, log2FC, |FC|>=1 flag,
5-donor baseline SD).

- 84/445 features with |log2FC| >= 1; **but 146/445 features are zero in at least one of the
  two samples** (sparse targeted panel), and 146/445 have FC = 0. Mean FC = −0.069, median 0,
  150 up / 149 down — no directional bias.
- Wilcoxon signed-rank is not applicable (n=1 pair). Permutation background instead: 2000
  random assignments of the single "inhibitor" label among the 6 FLS-only-family samples,
  recomputing per-feature FC each time. **Empirical p = 1.0 for both max |FC| (obs 2.585) and
  mean |FC| (obs 0.404)** — the observed spread is not unusual relative to the
  within-donor-family label-shuffle null.
- Only **2.9%** of features exceed 2× their own across-5-donor baseline SD.
- **MERTK itself: log2FC = 0.0** (identical in both samples). AXL: +0.449.
- Donor-aware mixed-effects model (donor random effect, inhibitor fixed effect; 5 FLS_only +
  1 FLS_only_Inhibitor): 441/445 features converged (4 non-converged are zero-variance
  features); **0 features BH<0.05** (`offtarget_mixed_effects.csv`).

**Top |log2FC| features (descriptive, NOT significant):** S100A12 (−2.58), DUSP4 (−2.48),
CD79B (−2.32), LILRB4 (+2.32), IL2RB (−2.32), SELL (−2.17), CD8A (−2.00), FCN1 (−2.00),
KLRC3 (−2.00), CD52 (+2.00), CD8B (+2.00), IL23A (+1.81) — dominated by zero↔low-count
transitions in a sparse panel.

### 3.2 Corrected specificity interaction

`specificity_interaction.csv` (per feature: delta_Mpos_Inh, delta_Mneg_Inh, delta_FLSonly_Inh).

- r(delta_FLSonly, delta_Mneg) = **0.114** (p = 0.016, n = 445); r(delta_FLSonly, delta_Mpos)
  = **0.114** (p = 0.016). **Difference = 0.000; permutation p = 1.0.**
- Spearman: 0.067 (Mneg) vs 0.068 (Mpos). Partial r of delta_FLSonly ~ delta_Mneg controlling
  delta_Mpos = 0.062 (p = 0.19). Sign agreement among 299 nonzero delta_FLSonly features:
  150 with delta_Mneg vs 153 with delta_Mpos.
- The FLS-only delta does **not** preferentially explain the Mneg direction.
- Context: mean |delta_Mneg| = 0.889 vs mean |delta_Mpos| = 0.420 (the ep12 asymmetry is real
  in magnitude); top Mneg drivers (CCL4 −6.14, IL33 −4.90, CCL22 −4.58, EGR3 −4.30) have
  delta_FLSonly of 0.74, −1.58, 0.00, −1.54 — not a consistent signature.

### 3.3 Re-confirm Mpos vs Mpos_Inhibitor (ep12 null)

`mpos_vs_mpos_inhibitor_reconfirmed.csv`: Welch t per feature, 8 vs 4 samples.
**0 features BH<0.05 and 0 raw p<0.05** (top: IL12RB1 p = 0.052, log2FC +1.49). The ep12 null
is **re-confirmed** with the corrected grouping.

### 3.4 Baseline FLS_only vs Mpos (macrophage activation effect)

`baseline_fls_only_vs_mpos.csv`: **0 features BH<0.05**; top raw p = 0.0073 (CD163,
log2FC +2.94), then CD209 (+1.42, p = 0.012), TLR7 (+1.24, p = 0.017), RGS1 (+2.66, p = 0.018),
C1QB (+3.31, p = 0.025) — macrophage contact shifts FLS toward macrophage-associated markers
but below FDR at n = 5 vs 8.

## 4. Interpretation

**Off-target hypothesis (A): NOT supported (adverse result for A).** The decisive corrected
control — same-donor FLS-only with vs without inhibitor — shows no non-random transcriptomic
response: permutation p = 1.0, 2.9% above 2× baseline SD, 0 mixed-effects BH<0.05, MERTK
unchanged, no directional bias. The 84 |FC|>=1 features are consistent with sparse-panel
zero-count noise (explanation C), not a coherent direct drug effect.

**Consequence for the ep12 asymmetry:** the Mneg > Mpos inhibitor effect is **not explained by
direct FLS off-target action** (delta_FLSonly correlates identically with both). The remaining
live explanations are (B) MerTK not the primary mediator of the FLS response (the inhibitor
effect, where present, is macrophage-conditioned) or a **single-sample artifact** of the
n = 1 Mneg_Inhibitor sample (R1_SA256A_FLS_SA259A_Mneg_Inhibitor). These two are
**observationally indistinguishable with the current data**: one more Mneg_Inhibitor sample is
the minimal discriminating experiment.

**Supportive / adverse / inconclusive mapping for the off-target question:**
- *Supportive of (A) would have been:* non-random |FC| spread (perm p < 0.05), BH-significant
  mixed-effects genes, and delta_FLSonly → delta_Mneg correlation exceeding delta_Mpos.
- *Observed (adverse to A):* all three null (above).
- *Inconclusive:* power for moderate direct effects is unestablished (n = 1 pair); the Mneg
  asymmetry itself is neither confirmed nor refuted as biology.

**What this does NOT establish:** it does not prove UNC106238 is FLS-inert at all doses, does
not identify the mechanism of the Mneg asymmetry, and does not validate MerTK as (or against)
a therapeutic target in this system — those require the additional samples/assays below.

## 5. Key references (inspected this session; frozen full-text XML in source inventory)

- **[K1]** Wei W, Xu J. *Failed resolution as a mechanistic basis of difficult-to-treat
  rheumatoid arthritis: stromal–myeloid crosstalk in the synovium and emerging
  resolution-restoring therapies.* Front Immunol. 2026;17:1935792. doi:10.3389/fimmu.2026.1935792
  (PMC13591627; source_id 214f941d…). Abstract + Section 1 opening inspected. Bounds the
  question: which macrophage-to-stroma pathways sustain non-resolving synovitis; motivates
  testing individual mediator candidates in FLS co-culture. Does not test MerTK specifically.
- **[K2]** Mosallanejad K, Hubeau C, Schwartz Sterman A, Tan Y. *Macrophages and the Tissue
  Repair Circuit: Homeostasis, Autoimmune Diseases, and Resolution-Based Therapeutic
  Strategies.* Cells. 2026;15(15):1412. doi:10.3390/cells15151412 (PMC13464986; source_id
  62c98d9f…). Abstract + keyword group inspected. Supports MerTK as a resolution-relevant
  macrophage pathway candidate (MerTK is a named keyword); no primary inhibitor data.
- **[K3]** Li S, Li F, Xu M, Cheng N, Wan L, Zhang X. *m6A-associated GAS6 expression is
  associated with pathogenic activation of fibroblast-like synoviocytes in rheumatoid
  arthritis.* Sci Rep. 2026;16:26987. doi:10.1038/s41598-026-52639-9 (PMC13522453; source_id
  482f02fd…). Abstract inspected. Ligand-side (GAS6) + receptor (MERTK/AXL) evidence that the
  axis is engaged in pathogenic FLS activation via silencing — exactly the off-target
  possibility this analysis tests pharmacologically; found no direct FLS effect.

Bibliography and receipts: `key-references.json` + K1–K3 source snapshots in
`reference-bundle-95ae2bdc100012a7/` (attached via supporting_paths).

## 6. Limitations

1. **n = 1 off-target pair** (SA256A only) — permutation/background statistics bound the
   spread but cannot power detection of moderate effects; no paired Wilcoxon possible.
2. **n = 1 Mneg_Inhibitor sample** — the Mneg asymmetry is a single observation; artifact vs
   biology unresolved.
3. **Targeted 445-gene panel, sparse counts** — 146/445 features zero in one of the two
   off-target samples; |FC|>=1 is heavily inflated by zero↔low transitions.
4. No library-size normalization (log2(count+1) on panel values); no batch/cellularity
   covariates available in the design file.
5. Inhibitor exposure of FLS in the FLS_only_Inhibitor sample is inferred from sample naming
   (design `treatment: none`, `condition: not co-cultured`) — the protocol-level question of
   whether FLS themselves saw the drug is an expert adjudication item.
6. Mixed-effects model has 1 inhibitor sample total (all from donor SA256A): the "inhibitor"
   fixed effect is confounded with that donor's inhibitor response; convergence failures
   (4/445) are zero-variance features.

## 7. Next steps (falsification / confirmation)

- **Minimal discriminating test:** 2–3 additional same-donor FLS-only + inhibitor pairs.
  If the off-target null holds (perm p > 0.05, no BH hits), (A) is rejected with power and
  the Mneg asymmetry must be macrophage-conditioned or artifact.
- **Mneg replication:** 1–2 more Mneg_Inhibitor samples. If the Mneg effect replicates, (B)
  gains support (real Mneg-specific on-target phenomenon); if it disappears, single-sample
  artifact.
- **Dose/response in FLS-only:** UNC106238 dose series (or a second MerTK inhibitor) in
  FLS-only culture to test for any direct effect at higher exposure.
- **Full-counts analysis:** repeat on the full scRNA-seq count matrix (if available) so
  zero-count features do not dominate.

## 8. Deliverable files (this branch)

- `working-proposal.md` (this file)
- `experiment-card.json` (life-science-experiment-card-v1)
- `analysis_ep13.py`, `ep13_run.log`
- `corrected_grouping.csv`, `offtarget_paired_results.csv`, `offtarget_mixed_effects.csv`,
  `specificity_interaction.csv`, `mpos_vs_mpos_inhibitor_reconfirmed.csv`,
  `baseline_fls_only_vs_mpos.csv`, `feasibility-results.json`
- `checkpoint-note.md`
- Reference bundle: `reference-bundle-95ae2bdc100012a7/{K1.txt,K2.txt,K3.txt,key-references.json}`
