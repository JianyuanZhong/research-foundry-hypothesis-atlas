> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# UKB-23: Blood Cell Change Patterns and the CRC vs Hematologic Cancer Disease Fork

## Unresolved Question

When a patient's hemoglobin declines between two blood draws, the etiology is ambiguous: occult gastrointestinal bleeding (leading to iron-deficiency anemia with reactive thrombocytosis) versus early clonal hematopoietic disease (leading to multi-lineage cytopenias and dyserythropoiesis). These two etiologies lead to fundamentally different cancers—colorectal cancer (CRC) versus hematologic malignancy. **No prior study has tested whether the pattern of concurrent blood cell changes (platelet, WBC, RDW) during hemoglobin decline differentially predicts these two cancer types in a prospective cohort.** The unresolved question is: does the blood cell change "signature" during Hb decline carry etiology-specific information that can be used to fork the differential diagnosis?

## Hypothesis (Specific, Falsifiable)

In UK Biobank participants with repeat blood counts (v0 and v1) and no prior cancer:

**H1 (CRC fork):** Hb decline (ΔHb < −1.0 g/dL) accompanied by platelet elevation (ΔPlatelet > +20 ×10⁹/L) is associated with a higher hazard of subsequent CRC (ICD10 C18–C20) compared to Hb decline without platelet elevation, after adjustment for age, sex, CRP, and inter-measurement interval.

**H2 (Hematologic fork):** Hb decline accompanied by multi-lineage abnormality (ΔWBC > +2.0 ×10⁹/L OR ΔRDW > +3.0%) is associated with a higher hazard of subsequent hematologic malignancy (ICD10 C81–C95, D46–D48) compared to Hb decline without multi-lineage abnormality, after the same adjustment.

**Falsification:** If the ΔHb × ΔPlatelet interaction (for CRC) AND the ΔHb × (ΔWBC/ΔRDW) interaction (for hematologic malignancy) both have p > 0.10 in the adjusted Cox models, the disease-fork hypothesis is not supported by the data.

## Clinical Importance

1. **Diagnostic triage:** Anemia is one of the most common abnormal blood results in primary care. The current workup is generic (iron studies, B12/folate, renal function). If the *pattern* of concurrent blood cell changes can suggest the likely etiology (GI bleeding vs clonal disease), it could direct targeted investigations (colonoscopy vs hematology referral) and reduce time-to-diagnosis for both CRC and hematologic malignancy.

2. **CRC screening:** Iron-deficiency anemia with thrombocytosis is a recognized but under-appreciated red flag for CRC. Quantifying the hazard ratio in a large prospective cohort provides the evidence base for incorporating this pattern into screening algorithms.

3. **CHIP surveillance:** Clonal hematopoiesis of indeterminate potential (CHIP) is present in >10% of adults >70 and confers a 4–5× increased risk of hematologic malignancy [K2]. Most CHIP carriers are identified incidentally. If multi-lineage blood count changes during anemia can flag the highest-risk subgroup, it could focus limited sequencing resources.

4. **Avoiding misdiagnosis:** The same anemia phenotype can lead to incorrect workup. A patient with clonal disease who is sent for colonoscopy (or vice versa) delays correct diagnosis. The disease-fork framework directly addresses this.

## Evidence Base

### [K1] Eldesouki et al. 2026 — Prediagnostic laboratory abnormalities in CRC

Eldesouki MH, Salem AE, Hafez Y, et al. "Metabolic and Laboratory Biomarkers in Early-Onset Versus Late-Onset Colorectal Cancer: A Case–Control Study." *Cancers* 2026;18(13):2152. DOI: 10.3390/cancers18132152. PMC13359632.

**What this work establishes:** In a matched case-control study (TriNetX US Network, n=7,752 CRC cases + 30,770 controls), hematologic abnormalities were among the strongest prediagnostic features of CRC. Microcytosis (aOR 2.29), low ferritin (aOR 2.11), and elevated CRP (aOR 1.87) were the top independent features for early-onset CRC. Iron-deficiency anemia was more frequent in EOCRC than LOCRC. The authors explicitly note these are "hypothesis-generating prediagnostic associations, not as validated predictors or causal risk factors."

**What it does NOT establish:** (a) No prospective design—laboratory values were measured within 24 months before diagnosis, so reverse causation (cancer causing the lab abnormality) cannot be excluded. (b) No interaction testing between Hb change and platelet change. (c) No comparison with hematologic malignancy as a competing outcome. (d) US network only; generalizability to UK population unknown. (e) Single time-point labs, not change patterns.

**How our proposal extends it:** We use a prospective design (labs measured at v0 and v1, cancer diagnosed after v1), test the specific interaction between Hb decline and platelet elevation, and compare CRC against hematologic malignancy as a disease fork.

### [K2] Anastasiou et al. 2025 — CHIP and hematologic malignancy risk

Anastasiou IA, Kounatidis D, Vallianou NG, et al. "Clonal Hematopoiesis of Indeterminate Potential and Cardiometabolic Disease: Challenges, Controversies and Future Perspectives." *Int J Mol Sci* 2025;27(1):233. DOI: 10.3390/ijms27010233. PMC12785648.

**What this work establishes:** CHIP is detected in >20% of individuals over 80, most commonly through DNMT3A, TET2, ASXL1, and PPM1D mutations. "CHIP confers over a four-fold increased risk of hematologic malignancy." The review synthesizes epidemiological, mechanistic, and translational evidence. It notes that multi-omics approaches have identified epigenetic and proteomic signatures correlated with CHIP expansion, providing potential biomarkers for risk stratification.

**What it does NOT establish:** (a) This is a narrative review, not an original cohort study. (b) It does not test whether routine blood count changes (Hb, WBC, RDW, platelet) can serve as a proxy for CHIP status or predict hematologic malignancy risk in the absence of sequencing. (c) It does not compare hematologic malignancy risk against solid tumor risk in the same cohort. (d) The "four-fold" figure is from the original Jaiswal 2014 NEJM study, which we could not directly access.

**How our proposal extends it:** We test whether multi-lineage blood count changes (a readily available, inexpensive proxy for clonal disease) predict hematologic malignancy risk in a prospective cohort, without requiring sequencing. This is a bounded adaptation of the CHIP literature to a setting where only routine blood counts are available.

### [K3] Hoermann 2022 — CHIP and blood count abnormalities

Hoermann G. "Clinical Significance of Clonal Hematopoiesis of Indeterminate Potential in Hematology and Cardiovascular Disease." *Diagnostics* 2022;12(7):1613. DOI: 10.3390/diagnostics12071613. PMC9317488.

**What this work establishes:** "The hematological risk [of CHIP] increases with the co-occurrence of unexplained blood count abnormalities." This is the key bridge: it establishes that blood count abnormalities are not merely epiphenomena of CHIP but are part of the risk stratification for progression to hematologic neoplasm. The review covers clonal cytopenia of undetermined significance (CCUS) as a distinct entity where CHIP + cytopenia carries higher risk than CHIP alone.

**What it does NOT establish:** (a) It does not quantify the hazard ratio for specific blood count change patterns (e.g., ΔHb + ΔWBC) for subsequent hematologic malignancy. (b) It does not compare the predictive value of different blood count patterns for different cancer types. (c) It is a review, not an original study. (d) It does not address the CRC side of the disease fork.

**How our proposal extends it:** We quantify the specific hazard ratios for defined blood cell change patterns (Hb decline + multi-lineage abnormality) for hematologic malignancy, and critically, we test whether the same Hb decline pattern leads to different cancer types depending on the concurrent blood cell changes—the disease fork.

## Study Design

### Population
- **Source:** UK Biobank participants in `[UKB data file]` (502,371 participants)
- **Inclusion:**
  - Both Hb v0 (30020-0.0) and Hb v1 (30020-1.0) non-null → 18,380 participants
  - No cancer at v0: 40005-0.0 is null OR 40005-0.0 > 53-0.0 (cancer diagnosed after baseline AC visit)
  - Valid dates: 53-1.0 > 53-0.0 (v1 after v0)
- **Expected analytic cohort:** ~17,000–18,000 (after excluding prior cancer)

### Exposure (Blood Cell Change Patterns)
All changes computed as v1 − v0:
| Variable | Field v0 | Field v1 | Unit |
|----------|----------|----------|------|
| ΔHb | 30020-0.0 | 30020-1.0 | g/dL |
| ΔPlatelet | 30080-0.0 | 30080-1.0 | ×10⁹/L |
| ΔWBC | 30000-0.0 | 30000-1.0 | ×10⁹/L |
| ΔRDW | 30070-0.0 | 30070-1.0 | % |

**Defined patterns (pre-specified):**
- **Hb decline:** ΔHb < −1.0 g/dL
- **Thrombocytosis:** ΔPlatelet > +20 ×10⁹/L
- **Multi-lineage abnormality:** ΔWBC > +2.0 ×10⁹/L OR ΔRDW > +3.0%

**Exposure categories (4 groups):**
1. No Hb decline (ΔHb ≥ −1.0): reference
2. Hb decline + thrombocytosis (ΔHb < −1.0 AND ΔPlatelet > +20)
3. Hb decline + multi-lineage (ΔHb < −1.0 AND (ΔWBC > +2.0 OR ΔRDW > +3.0))
4. Hb decline + neither (ΔHb < −1.0, no thrombocytosis, no multi-lineage)

Note: Groups 2 and 3 can overlap (a participant can have both thrombocytosis and multi-lineage abnormality). In the primary analysis, we use the interaction model rather than mutually exclusive categories.

### Outcomes
- **Primary:** CRC (ICD10 C18, C19, C20 in field 40006-0.0) diagnosed after v1 date (40005-0.0 > 53-1.0)
- **Secondary:** Hematologic malignancy (ICD10 C81–C95, D46–D48 in field 40006-0.0) diagnosed after v1 date
- **Expected events:** ~275 CRC, ~223 hematologic (from feasibility check; will be reduced by the no-cancer-at-v0 filter)

### Follow-up
- Start: v1 AC date (53-1.0)
- End: cancer diagnosis date (40005-0.0) if cancer type matches, or data snapshot date (latest date in dataset) if no matching cancer
- Censoring: non-matching cancer diagnosis, loss to follow-up, data snapshot

### Covariates
| Covariate | Field | Type |
|-----------|-------|------|
| Age at v1 | 31-0.0 + (53-1.0 − 53-0.0) in years | Continuous |
| Sex | 34-0.0 (1=male, 2=female) | Binary |
| CRP at v0 | 30710-0.0 | Continuous (mg/L) |
| Time between v0 and v1 | (53-1.0 − 53-0.0) in years | Continuous |

### Analysis Plan

**Primary analysis (CRC):**
1. Univariate Cox PH: ΔHb (continuous, per 1 g/dL) → CRC
2. Adjusted Cox PH: ΔHb + ΔPlatelet + ΔHb×ΔPlatelet interaction, adjusted for age, sex, CRP, time interval
3. Key test: p-value for ΔHb×ΔPlatelet interaction
4. If interaction significant: stratified HRs for Hb decline ± thrombocytosis

**Secondary analysis (Hematologic malignancy):**
1. Univariate Cox PH: ΔHb (continuous) → hematologic malignancy
2. Adjusted Cox PH: ΔHb + ΔWBC + ΔRDW + ΔHb×ΔWBC + ΔHb×ΔRDW interactions, adjusted for age, sex, CRP, time interval
3. Key test: p-values for ΔHb×ΔWBC and ΔHb×ΔRDW interactions

**Sensitivity analyses:**
1. Exclude cancers diagnosed <1 year after v1 (address reverse causation / pre-existing occult cancer)
2. Restrict to Hb decline subgroup (ΔHb < −1.0) only
3. Continuous ΔHb and ΔPlatelet (not binary) with spline terms
4. Exclude participants with CRP > 10 mg/L at v0 (address inflammation-driven confounding)
5. Restrict to v0→v1 interval > 1 year (address measurement timing)

**Baseline comparison:**
- Univariate Cox with ΔHb alone (no interaction) as the baseline model
- The interaction model adds the ability to detect differential effects by concurrent blood cell changes
- What the interaction model reveals that the baseline loses: whether the Hb decline signal is *modified* by the concurrent platelet or WBC/RDW change, i.e., whether the same Hb drop means different things depending on the other blood cells

### Method Comparison: Cox PH (primary) vs Baseline Univariate

| Aspect | Baseline (univariate Cox) | Primary (adjusted Cox with interaction) |
|--------|--------------------------|----------------------------------------|
| Question | Does Hb decline predict cancer? | Does Hb decline predict *different* cancers depending on concurrent blood cell changes? |
| Covariates | None | Age, sex, CRP, time interval |
| Interaction | No | ΔHb×ΔPlatelet (CRC), ΔHb×ΔWBC/RDW (hematologic) |
| What it reveals | Overall Hb effect | Differential etiology-specific effects |
| Limitation | Cannot distinguish CRC from hematologic etiology | Requires sufficient events per interaction term |

The baseline univariate model is scientifically necessary as a reference: if ΔHb alone does not predict either cancer type, the interaction analysis is uninterpretable. If ΔHb predicts both equally, the interaction tests whether the *pattern* adds information.

## Data Bindings

### Source File
- **Path:** `[internal dataset path]`
- **Size:** 705 MB
- **Participants:** 502,371
- **Column type:** All STRING (parse to float for numeric, ISO date for dates)
- **Field naming convention:** `FIELDID-VISIT.0` (e.g., `30020-0.0`, `30020-1.0`)

### Required Fields and Non-Missing Counts
| Field | Description | Non-missing (v0) | Non-missing (v1) |
|-------|-------------|-------------------|-------------------|
| 30020-0.0 / 30020-1.0 | Hemoglobin (g/dL) | 478,046 | (subset of 18,380 repeat) |
| 30000-0.0 / 30000-1.0 | WBC (×10⁹/L) | 478,041 | (subset) |
| 30080-0.0 / 30080-1.0 | Platelet (×10⁹/L) | 478,043 | (subset) |
| 30070-0.0 / 30070-1.0 | RDW (%) | 478,044 | (subset) |
| 30710-0.0 | CRP (mg/L) | 468,446 | N/A (baseline only) |
| 40005-0.0 | Cancer diagnosis date (ISO) | — | — |
| 40006-0.0 | Cancer type ICD10 (string) | — | — |
| 53-0.0 | AC date v0 (ISO) | 502,371 | — |
| 53-1.0 | AC date v1 (ISO) | — | 20,343 |
| 34-0.0 | Sex (1=male, 2=female) | 502,368 | — |
| 31-0.0 | Age at AC (years) | 502,371 | — |

### Join Keys
- Single table; no joins required
- Participant ID is the row index (implicit)
- All fields are in the same row per participant

### Temporal Logic
- v0 date: 53-0.0 (all participants)
- v1 date: 53-1.0 (20,343 participants; 18,380 with both Hb v0 and v1)
- Cancer date: 40005-0.0
- Follow-up starts at 53-1.0
- Cancer must be after 53-1.0 for outcome; before 53-0.0 for exclusion

### ICD10 Code Mapping
- **CRC:** C18 (colon), C19 (junction), C20 (rectum)
- **Hematologic:** C81–C95 (lymphoid/myeloid neoplasms), D46–D48 (myeloproliferative/myelodysplastic)
- Field 40006-0.0 contains ICD10 codes as strings; may contain multiple codes (check for comma/semicolon separation)

## Falsification Criteria

The disease-fork hypothesis is **not supported** if:
1. **Primary falsification:** Both the ΔHb×ΔPlatelet interaction (CRC model) AND the ΔHb×(ΔWBC/ΔRDW) interaction (hematologic model) have p > 0.10 after adjustment.
2. **Directional falsification:** If the interaction is significant but in the *opposite* direction (e.g., Hb decline + thrombocytosis is associated with *lower* CRC risk, or Hb decline + multi-lineage is associated with *lower* hematologic risk), the specific etiological interpretation is falsified even if an interaction exists.
3. **Sensitivity falsification:** If the primary interaction disappears (p > 0.10) after excluding cancers diagnosed <1 year after v1, the finding is likely driven by reverse causation (pre-existing occult cancer causing both the blood changes and the diagnosis).

**Supportive result:** Interaction p < 0.05 in at least one of the two models, with the expected direction (Hb decline + thrombocytosis → higher CRC; Hb decline + multi-lineage → higher hematologic).

**Inconclusive result:** Interaction p between 0.05 and 0.10, or significant in only one model with the other non-significant. This would warrant a larger study or different exposure definition.

## Alternative Explanations and Sensitivity Analyses

| Alternative | Mechanism | How we address it |
|-------------|-----------|-------------------|
| Reverse causation (occult cancer → blood changes) | Pre-existing cancer causes both Hb drop and platelet/WBC changes before diagnosis | Exclude cancers <1 year after v1; check if interaction persists |
| Inflammation (CRP) driving both Hb drop and thrombocytosis | Systemic inflammation suppresses erythropoiesis and stimulates megakaryopoiesis | Adjust for CRP at v0; sensitivity excluding CRP > 10 |
| Iron deficiency from non-malignant causes | Menstruation, diet, malabsorption → Hb drop + reactive thrombocytosis | Cannot fully address (no iron studies in this subset); note as limitation |
| Measurement timing (v1 close to diagnosis) | Blood drawn during acute illness or pre-diagnostic phase | Adjust for v0→v1 interval; sensitivity restricting to interval > 1 year |
| Selection bias (who gets repeat bloods) | Participants with v1 may differ systematically | Describe v0→v1 interval distribution; note as limitation |
| Multiple testing | 4 exposure categories × 2 outcomes × multiple sensitivity analyses | Pre-specify primary analysis; use Bonferroni or FDR for secondary |

## Key References

### [K1] Eldesouki et al. 2026
- **Title:** Metabolic and Laboratory Biomarkers in Early-Onset Versus Late-Onset Colorectal Cancer: A Case–Control Study
- **Authors:** Eldesouki MH, Salem AE, Hafez Y, Ibrahim EEA, Youssef MY, Khan F, Alomari M, ElHananfi SE, Shaukat A
- **Year:** 2026
- **Journal:** Cancers (Basel), 18(13):2152
- **DOI:** 10.3390/cancers18132152
- **PMCID:** PMC13359632
- **Claim supported:** Hematologic abnormalities (microcytosis, low ferritin, elevated CRP) are among the strongest prediagnostic features of CRC, supporting the biological plausibility that anemia-related blood changes precede CRC diagnosis.
- **Contribution of this proposal:** Prospective design with change patterns (not single time-point), interaction testing, and disease-fork comparison with hematologic malignancy.
- **Limitation:** Case-control design cannot exclude reverse causation; no platelet interaction tested; US network only.
- **Inspection:** Full text (PMC13359632 XML, 141,626 bytes)

### [K2] Anastasiou et al. 2025
- **Title:** Clonal Hematopoiesis of Indeterminate Potential and Cardiometabolic Disease: Challenges, Controversies and Future Perspectives
- **Authors:** Anastasiou IA, Kounatidis D, Vallianou NG, Rebelos E, Karampela I, Dalamaga M
- **Year:** 2025
- **Journal:** Int J Mol Sci, 27(1):233
- **DOI:** 10.3390/ijms27010233
- **PMCID:** PMC12785648
- **Claim supported:** CHIP confers over a four-fold increased risk of hematologic malignancy; multi-omics signatures correlated with CHIP expansion may serve as risk stratification biomarkers.
- **Contribution of this proposal:** Tests whether routine blood count changes (a cheap, available proxy) can capture the hematologic malignancy risk signal, without requiring sequencing.
- **Limitation:** Narrative review, not original cohort; does not test blood count change patterns specifically; does not compare against solid tumor outcomes.
- **Inspection:** Full text (PMC12785648 XML, 394,395 bytes)

### [K3] Hoermann 2022
- **Title:** Clinical Significance of Clonal Hematopoiesis of Indeterminate Potential in Hematology and Cardiovascular Disease
- **Authors:** Hoermann G
- **Year:** 2022
- **Journal:** Diagnostics (Basel), 12(7):1613
- **DOI:** 10.3390/diagnostics12071613
- **PMCID:** PMC9317488
- **Claim supported:** The hematological risk of CHIP increases with the co-occurrence of unexplained blood count abnormalities, establishing that blood count changes are part of the risk stratification for hematologic malignancy progression.
- **Contribution of this proposal:** Quantifies specific hazard ratios for defined blood cell change patterns and tests the disease-fork hypothesis (same anemia, different etiology, different cancer).
- **Limitation:** Review, not original study; does not quantify hazard ratios for specific change patterns; does not address the CRC side.
- **Inspection:** Full text (PMC9317488 XML, 190,290 bytes)

## Limitations

1. **Single pair of repeat measurements:** We use v0 and v1 only. A true trajectory (multiple time points) would be more powerful but is not available in this subset.
2. **No iron studies:** We cannot directly confirm iron deficiency as the mechanism for Hb decline + thrombocytosis.
3. **No CHIP sequencing:** We use blood count changes as a proxy for clonal disease. True CHIP status would require NGS, which is not available for this subset.
4. **Cancer registry completeness:** UKB cancer ascertainment is through primary care records and cancer registry linkage. Some hematologic malignancies (especially early-stage) may be missed.
5. **Multiple ICD10 codes:** Field 40006-0.0 may contain multiple codes. We need to check for and handle multi-code entries.
6. **Selection bias:** Participants with v1 bloods may differ from those without. We describe but cannot fully address this.
7. **Generalizability:** UKB participants are healthier than the general population (healthy volunteer bias).

## Computational Requirements

- **Data loading:** 705 MB parquet → pandas DataFrame (~5–10 min on 4 CPUs)
- **Cohort construction:** Boolean filtering, date parsing (~1 min)
- **Cox PH models:** lifelines or statsmodels, ~17,000 participants, 275+223 events (~1–5 min per model)
- **Total compute:** < 30 min on 4 CPUs, 16 GB RAM
- **No GPU required**
