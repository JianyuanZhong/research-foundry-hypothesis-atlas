> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Discordant recovery after AKI: does creatinine recovery overstate renal recovery?

## Status
Working proposal for MIMIC-IV v3.1 (episode 11 repair). This is a scientific design, not a completed analysis. No patient-level results have been estimated yet.

## Clinical question
Among ICU patients with AKI, does apparent recovery defined by creatinine improvement identify patients whose urine output remains abnormal, and are those patients at higher risk of subsequent renal escalation, ICU death, or in-hospital death?

The clinically consequential unresolved claim is narrower than "creatinine is invalid." The claim is that a creatinine-based recovery definition can misclassify a subgroup whose urine output remains abnormal, and that this subgroup has worse subsequent outcomes than either patients with concordant recovery or patients who have not recovered.

## Why this matters
AKI recovery is often inferred from creatinine because it is repeatedly measured and familiar. However, creatinine generation and clearance can be affected by muscle mass, nutrition, fluid balance, and sampling practices. Urine output is a direct but noisy renal output measure. If creatinine recovery is discordant from urine output, the discordance may identify a clinically important subgroup that is missed by creatinine-based recovery criteria.

The prior literature supports the concern that creatinine-based estimates can diverge from measured kidney function in critical illness. [K1] Tang et al. developed an interpretable machine-learning model for observed CRRT initiation in sepsis-associated AKI using MIMIC-IV and eICU-CRD, retaining both serum creatinine and urine output as predictors, which supports the relevance of both measures in AKI prognosis. [K2] Jakobsen et al. systematically reviewed RIFLE criteria fulfillment in porcine sepsis models and found that measurement of GFR was associated with a higher likelihood of RIFLE fulfillment, highlighting the limitations of creatinine-based definitions. [K3] Tanasescu et al. reviewed renal biomarkers beyond creatinine and noted that conventional renal assessment based on serum creatinine, eGFR, and urine output often fails to detect early structural injury or pathway-specific cardiorenal risk, supporting the need for complementary measures.

## Unresolved question
The strongest claim the available evidence supports is that creatinine and urine output are both relevant to AKI prognosis, and that creatinine-based definitions have known limitations. The unresolved claim is whether discordance between creatinine recovery and urine output identifies a subgroup with worse subsequent outcomes after accounting for illness severity, treatment intensity, and measurement practices.

## Data and design
MIMIC-IV v3.1 provides repeated creatinine, urine output, fluid balance, renal support, vasopressors, and mortality. The experiment prespecifies AKI episode and index time, compares discordant, concordant, and non-recovered groups, and tests renal escalation, ICU death, and in-hospital death with severity-adjusted and negative-control analyses.

### Population
ICU patients with AKI defined by KDIGO criteria (creatinine and/or urine output). The index time is the first AKI episode meeting KDIGO criteria.

### Phenotype definitions
- Concordant recovery: creatinine improvement AND urine output normalization.
- Discordant recovery: creatinine improvement BUT urine output remains abnormal.
- Non-recovery: neither creatinine improvement nor urine output normalization.

### Outcomes
- Renal escalation (CRRT initiation or dialysis).
- ICU death.
- In-hospital death.

### Analysis
- Severity-adjusted logistic regression for each outcome.
- Negative-control analysis to assess measurement artifacts.
- Sensitivity analysis with alternative creatinine and urine output thresholds.

### Falsification criteria
- If discordant recovery is not associated with worse outcomes after severity adjustment, the hypothesis is not supported.
- If the association is explained by sampling frequency or fluid balance, the hypothesis is not supported.
- If the association is present only in a small subgroup with extreme values, the hypothesis is not robust.

## Baseline versus learned alternative
The baseline is a severity-adjusted logistic regression with creatinine and urine output as predictors. The learned alternative is a gradient-boosting model with the same predictors, which could reveal nonlinear interactions between creatinine and urine output that the baseline loses. The learned alternative is not required for the primary hypothesis test but could provide additional insight.

## Key references
[K1] Tang Y, Zhang S, Wang Q, Zhang Q, Ji L, Li R, Fang M. An interpretable machine learning model for early prediction of subsequent observed CRRT initiation in patients with sepsis-associated acute kidney injury. Clin Exp Med. 2026;26(1):345. doi:10.1007/s10238-026-02305-1.
[K2] Jakobsen K, Markussen VI, Backmann HJ, Reierth E, Kildal AB, Ytrebø LM. Does kidney function in experimental porcine sepsis fulfill the RIFLE criteria for acute kidney injury? A systematic review. Front Physiol. 2026;17:1810924. doi:10.3389/fphys.2026.1810924.
[K3] Tanasescu MD, Rosu AM, Minca A, Grigorie MM, Timofte D, Ionescu D. Beyond Creatinine: Novel Renal Biomarkers at the Interface of Kidney Injury and Cardiovascular Risk. Biomedicines. 2026;14(7):1525. doi:10.3390/biomedicines14071525.
