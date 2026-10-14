> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UPA metabolic state: is the glycolytic/HIF-1a reprogramming signature already present in undifferentiated arthritis, or does it emerge only after established RA and treatment failure?

**Child of [prior hypothesis]** (D3-M3, E-MTAB-8322).
**Status: EXECUTED analysis. Managed compute [research job] (succeeded). Result: INCONCLUSIVE (bounded feasibility check, n=2 UPA).**

## Scientific opening

The parent candidate (candidate-75da3dd9, mu 34.38) established that treatment-resistant RA synovial macrophages carry a distinct glycolytic/HIF-1a metabolic program that is not simply a scaled version of the inflammatory state (OLS Resistant coefficient 0.79, p=0.033, after adjusting for inflammatory score; R²=0.82). That analysis used the full 5-condition gradient (HC, naive RA, UPA, remission, resistant RA) but the UPA group (n=2 after excluding SA149/SA149P) was underpowered and not the focus.

The unresolved question this candidate addresses: **WHEN does the metabolic reprogramming emerge?** Two materially different explanations:

- **Early-reprogramming hypothesis (H1):** The glycolytic/HIF-1a program is already present in UPA macrophages — the metabolic shift is an early, possibly initiating, feature of the disease trajectory. If true, the intervention window for metabolic reprogramming opens at the UPA stage, and early metabolic intervention could prevent progression to treatment resistance.
- **Late-reprogramming hypothesis (H2):** The metabolic program emerges only after established RA and treatment failure — it is a consequence of chronicity and/or treatment, not an early feature. If true, the intervention window is later and metabolic reprogramming is a marker of refractory disease.

These differ in a directly testable way: H1 predicts UPA metabolic score is elevated relative to HC and comparable to (or above) Resistant; H2 predicts UPA metabolic score is near HC and well below Resistant.

**Closest prior work actually inspected:** Fuentelsaz-Romero et al 2021 [K2] studied the UPA macrophage state directly and found the pro-inflammatory macrophage *polarization* (GM-CSF/activin A/TNFα/MMP12/CD209 by immunofluorescence) is already similar in UPA (UA>RA) and established RA — supporting an *early* inflammatory macrophage program. But that work examined inflammatory polarization markers, **not** the glycolytic/HIF-1a metabolic program, and did not include treatment-resistant RA. Luo et al 2026 [K1] establishes HIF-1α as a central RA node driving metabolic rewiring in synovial macrophages but does not compare across the UPA→RA→resistance trajectory. Batashkov et al 2026 [K3] frames the need for tissue-based metabolic/inflammatory endotypes to distinguish treatment response from resistance. **None of these tests whether the metabolic (as opposed to inflammatory) program is already present in UPA.** That is the gap this proposal fills.

## Hypothesis

H1 (early): the glycolytic/HIF-1a metabolic score in UPA macrophages is elevated relative to HC and is not lower than in Resistant RA, and the UPA metabolic residual (beyond inflammation) is positive.
H2 (late): the UPA metabolic score is near HC and well below Resistant, with a near-zero UPA residual.

## Data (verified bindings)

- **Counts**: `[internal dataset path]` (gzip TSV; 28 cols = 1 `feature` col + 27 samples; rows are Ensembl IDs; integer raw counts).
- **Design**: `.../prepared/E-MTAB-8322.design.json` (list of 27 sample dicts; fields `sample_id`, `donor_id`, `condition`, `donor_status`, `age`, `sex`).
- **Gene map**: `[internal dataset path]` (Ensembl→symbol, 33,694 rows; identical hash across all samples). All 29 gene-set symbols map to unique Ensembl IDs (verified).
- **Population**: 27 samples → **25 verified donors** after excluding SA149P and UPASA149 (both `donor_status=possible_related_or_repeated_donor_exclude_inference`). Conditions: HC (4), Naive RA (6), **UPA (2: SA154, UPASA153)**, Remission RA (7), Resistant RA (6).

## Gene sets (from parent candidate-75da3dd9)

- **Glycolytic (10)**: HK2, LDHA, PKM, PFKL, GPI, ENO1, PGK1, ALDOA, GAPDH, TPI1
- **HIF-1a targets (10)**: VEGFA, PDK1, ENO1, SLC2A1, NOS3, BNIP3, BNIP3L, PHGDH, ALAS2, CA9
- **Metabolic (19 unique)**: union of the two
- **Inflammatory (10)**: IL6, TNF, IL1B, CCL2, CXCL8, IL18, IL33, CXCL10, CCL3, CCL4

## Methods (executed)

1. Per-donor mean log2(count+1) of each gene set (identical to parent; per-donor scores exactly reproduce parent candidate-75da3dd9 support-2-per_donor_scores.json).
2. **Primary tests** — UPA vs each comparator, using **exact permutation** (enumerate all distinct labelings; two-sided p = (#perms with |diff| ≥ |obs| + 1)/(N+1)):
   - UPA vs Remission, UPA vs Resistant, UPA vs HC.
   - (N=10000 Monte Carlo was the planned fallback; exact enumeration was used because the labelings are few and exact — more conservative and fully reproducible, seed=42 for any MC.)
3. **Secondary (descriptive)** — UPA position on the 5-condition gradient.
4. **Residual analysis** — OLS metabolic_score ~ inflammatory_score (all 25 donors); condition-mean residuals.
5. **Per-gene descriptive** — UPA vs Remission / UPA vs Resistant direction for each of the 19 metabolic genes.

## Results (EXECUTED, [research job])

### Descriptive gradient (metabolic score mean)
| Condition | n | mean |
|-----------|---|------|
| HC | 4 | 7.113 |
| Naive | 6 | 8.742 |
| **UPA** | **2** | **8.677** |
| Remission | 7 | 7.884 |
| Resistant | 6 | 8.388 |

UPA (8.68) sits **between HC (7.11) and Naive (8.74)**, and is actually *slightly above* Resistant (8.39) — but n=2, so this is descriptive only. The two UPA donors are heterogeneous: SA154 met=9.28 (high), UPASA153 met=8.08 (intermediate).

### Primary permutation tests (exact)
| Contrast | observed diff (UPA−comp) | p (two-sided) | method |
|----------|--------------------------|---------------|--------|
| UPA vs Remission | +0.793 | **0.486** | exact (36 labelings) |
| UPA vs Resistant | +0.288 | **0.862** | exact (28 labelings) |
| UPA vs HC | +1.564 | **0.125** | exact (15 labelings) |

**No UPA contrast is significant.** UPA is directionally above HC (p=0.125, not significant) and above Remission (p=0.49), but not distinguishable from Resistant (p=0.86).

### Residual analysis (metabolic ~ inflammatory, all 25 donors)
- Slope = 0.735, R² = 0.760 (inflammatory score explains 76% of metabolic variance).
- Condition-mean residuals: HC −0.459, Naive +0.146, **UPA +0.213**, Remission −0.169, **Resistant +0.287**.
- UPA residual (+0.21) is positive (above HC and Remission) but **lower than Resistant (+0.29)**. UPA residual vs HC = +0.67; vs Remission = +0.38; vs Resistant = −0.07.

### Per-gene descriptive (19 metabolic genes)
- 17/19 genes: UPA > Remission (directional).
- 2/19 genes: UPA < Resistant (directional). No per-gene inference (n=2).

## Interpretation

**Result: INCONCLUSIVE.** The data cannot distinguish H1 (early) from H2 (late) metabolic reprogramming.

- **Directionally consistent with H1 (early):** UPA metabolic mean (8.68) is well above HC (7.11, diff +1.56) and above Remission (7.88); the UPA residual is positive (+0.21) and 17/19 metabolic genes are elevated in UPA vs Remission. This is the same qualitative pattern the parent found for resistant macrophages (positive residual beyond inflammation), and it is consistent with the closest prior work [K2] showing the pro-inflammatory macrophage program is already present in UPA.
- **Directionally consistent with H2 (late) / against a strong early claim:** UPA is *not* statistically different from Resistant (p=0.86) and its residual (+0.21) is below Resistant (+0.29). The UPA-vs-HC elevation is not significant (p=0.125). So we cannot claim the metabolic program is "already fully present" in UPA.
- **The decisive limitation is power, not direction.** With n=2, the exact UPA-vs-Remission permutation has only 36 labelings and can only reject if both UPA donors are the top-2 (or bottom-2) of the pooled 9; the smallest attainable two-sided p is ~1/37. The null result is therefore **uninformative about the true effect size** — it neither supports nor refutes early reprogramming.

**What this result would and would not establish:** It establishes that a 2-donor UPA group in E-MTAB-8322 yields a descriptive metabolic profile that is intermediate-to-high (between HC and Naive/Resistant) but statistically indistinguishable from established disease. It does **not** establish that the metabolic program is present in UPA (no significant UPA-vs-HC contrast) nor that it is absent (direction is positive). Resolving the early-vs-late question requires more UPA donors.

## Competing explanations

1. **Inflammatory confounding** — metabolic score is 76% explained by the inflammatory score; the UPA elevation may be a scaled version of its high inflammatory state. The residual analysis partially controls for this, but the 10-gene inflammatory score may not capture all pathways.
2. **Cell-type composition** — pseudobulk may reflect macrophage subpopulation shifts rather than within-cell reprogramming.
3. **Small-n / power** — n=2 UPA; the null is uninformative (see above).
4. **Cross-sectional design** — UPA is a snapshot; cannot establish the metabolic state as a precursor to resistance.
5. **UPA donor heterogeneity** — SA154 (high) vs UPASA153 (intermediate); the 2-donor mean is unstable.

## Falsification criteria (pre-specified)

- **Supportive (H1 early):** UPA-vs-HC p<0.05 AND UPA residual ≥ Resistant residual.
- **Adverse (H2 late):** UPA-vs-HC p>0.10 AND UPA residual ≤ 0.
- **Inconclusive:** UPA directionally between HC and Resistant but no contrast significant. **← OBSERVED RESULT.**

## What would change the next decision

- **If a larger UPA cohort (n≥8) shows UPA-vs-HC p<0.05 with a positive residual** → continue: the metabolic program is early; prioritize UPA-stage metabolic intervention and test the 19-gene set in single-cell (E-MTAB-8316) to confirm macrophage-intrinsic signal.
- **If a larger UPA cohort shows UPA near HC (p>0.10, residual ≤0)** → the metabolic program is late; refocus on resistant-RA-specific mechanisms (parent candidate) and drop the early-intervention framing.
- **If the larger UPA cohort is again indeterminate** → the question needs a different design (longitudinal UPA→RA biopsies, or a larger cross-sectional cohort with matched disease duration/activity).

## Clinical importance

Treatment-resistant RA affects ~30–40% of patients who fail first-line biologic DMARDs. If metabolic reprogramming is an *early* feature (present in UPA), early metabolic intervention could prevent treatment resistance; if *late*, the intervention window is later. This bounded feasibility check shows the question is answerable in principle with the available data (the UPA group yields a coherent, intermediate-to-high metabolic profile) but that n=2 is insufficient to decide it. The scientific value is in framing and bounding the early-vs-late question, not in the (necessarily inconclusive) statistical result.

## Key references

[K1] Luo TT, He LX, Yin Q, Wang ZF, Zuo J. "Hypoxia-Inducible Factors in Rheumatoid Arthritis: Central Pathogenic Roles and Therapeutic Opportunities." J Inflamm Res 19:600186 (2026). DOI: 10.2147/JIR.S600186. PMC13217440.
- **Claim supported:** HIF-1α accumulates in RA synovial macrophages and drives inflammatory + metabolic (glycolytic) reprogramming, correlating with disease activity.
- **Contribution:** This proposal tests *when* (UPA vs resistant) this program emerges, not just that it exists in RA.
- **Limitation:** Review; no UPA→RA→resistance comparison, no quantitative pseudobulk data.
- **Inspection:** abstract_only (full-text XML frozen, 205,661 bytes, SHA-256 abad758d...).

[K2] Fuentelsaz-Romero S, Cuervo AM, Estrada-Capetillo L, Celis R, Garcia-Campos R, Ramirez J, Sastre S, et al. "GM-CSF Expression and Macrophage Polarization in Joints of Undifferentiated Arthritis Patients Evolving to Rheumatoid Arthritis or Psoriatic Arthritis." Front Immunol 11:613975 (2021). DOI: 10.3389/fimmu.2020.613975.
- **Claim supported (closest prior work):** the pro-inflammatory macrophage polarization state is already similar in UPA (UA>RA) and established RA — an *early* inflammatory macrophage program.
- **Contribution:** This work examined inflammatory polarization (GM-CSF/activin A/TNFα/MMP12/CD209) by immunofluorescence; this proposal asks whether the *metabolic* (glycolytic/HIF-1a) program is likewise already present in UPA, and adds the treatment-resistant contrast.
- **Limitation:** Protein markers, not transcriptomic metabolic gene sets; small cohorts (UA>RA n=8, persistent UA n=16); no resistant RA.
- **Inspection:** abstract_only (full-text HTML frozen, 989,489 bytes, SHA-256 227cf2ab...).

[K3] Batashkov NA, Gerasimova EV, Gerasimova DA, et al. "Biomarkers of treatment response in rheumatoid arthritis: from conventional markers to tissue immunophenotype." Front Immunol 17:1880487 (2026). DOI: 10.3389/fimmu.2026.1880487.
- **Claim supported:** RA is biologically heterogeneous with variable therapeutic response; synovial pathotypes and macrophage subsets offer a mechanistically richer view of treatment response/resistance, supporting tissue-based endotyping.
- **Contribution:** This proposal operationalizes that framework by testing whether a specific metabolic endotype distinguishes resistant from early (UPA) disease.
- **Limitation:** Review; no quantitative metabolic gene expression across disease states, no UPA-vs-resistant contrast.
- **Inspection:** abstract_only (full-text XML frozen, 318,046 bytes, SHA-256 106d50af...).

## Method comparison

**Baseline (executed):** Per-donor gene-set mean log2(count+1) + exact permutation tests + OLS residual analysis. This is the standard, transparent approach for small-n multi-group transcriptomic comparisons and directly matches the parent's framework (ensuring comparability).

**Alternative considered:** Monte Carlo permutation (N=10000) as specified in the plan. Not used because exact enumeration is available (≤36 labelings) and is more conservative and fully reproducible; the MC path is retained in the script as a fallback for larger contrasts.

**Alternative considered:** Mixed-effects model with donor random effect. Not feasible — one sample per donor (no within-donor replication).

**Alternative considered:** Per-gene regression (metabolic gene ~ inflammatory gene + condition). Underpowered (n=25, 19 genes × 6 parameters); gene-set level is the appropriate power level (consistent with parent).

## Limitations

1. **n=2 UPA** — the central limitation; the null result is uninformative about effect size.
2. Cross-sectional; cannot establish longitudinal UPA→resistance transitions.
3. Pseudobulk; one sample per donor; no within-donor replication.
4. Age and disease duration not adjusted (age ranges 22–77; UPA donors 51 and 62).
5. Treatment history not in design metadata.
6. log2(count+1) normalization is simple; TPM/DESeq2 would remove library-size effects.
7. The 10-gene inflammatory score may not capture all inflammatory pathways.
