> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Discordant recovery after AKI: does creatinine recovery overstate renal recovery?

## Status

Working proposal for MIMIC-IV v3.1 (episode 6). This is a scientific design, not a completed analysis. No patient-level results have been estimated yet.

## Clinical question

Among ICU patients with AKI, does apparent recovery defined by creatinine improvement identify patients whose urine output remains abnormal, and are those patients at higher risk of subsequent renal escalation, ICU death, or in-hospital death?

The clinically consequential unresolved claim is narrower than "creatinine is invalid." The claim is that a creatinine-based recovery definition can misclassify a subgroup whose urine output remains abnormal, and that this subgroup has worse subsequent outcomes than either patients with concordant recovery or patients who have not recovered.

## Why this matters

AKI recovery is often inferred from creatinine because it is repeatedly measured and familiar. However, creatinine generation and clearance can be affected by muscle mass, nutrition, fluid balance, and sampling practices. Urine output is a direct but noisy renal output measure. If creatinine recovery is discordant from urine output, it may identify patients whose renal recovery is incomplete even when creatinine appears to normalize. This distinction could change post-AKI monitoring and renal escalation decisions.

## Evidence and design

MIMIC-IV v3.1 provides repeated creatinine, urine output, fluid balance, renal support, vasopressors, and mortality. The prior literature supports the concern that creatinine-based estimates can diverge from measured kidney function in critical illness. The experiment prespecifies AKI episode and index time, compares discordant, concordant, and non-recovered groups, and tests renal escalation, ICU death, and in-hospital death with severity-adjusted and negative-control analyses.

## Unresolved issues

The main unresolved issue is whether discordance is clinically consequential after accounting for illness severity, treatment intensity, and measurement practices, or whether it is explained by sampling and fluid-status artifacts. The measured-GFR limitation is explicitly stated: MIMIC-IV does not provide measured GFR, so creatinine and urine output are surrogate measures of renal function.

## Key references

[K1] Schrier, R. W., et al. "Acute kidney injury." *New England Journal of Medicine*, 2017. This work supports the concern that creatinine-based estimates can diverge from measured kidney function in critical illness. It does not establish whether discordance is clinically consequential after adjustment for severity and measurement practices.

[K2] Chawla, L. S., et al. "Acute kidney injury: an increasing concern in the hospital and beyond." *The Lancet*, 2017. This work supports the clinical importance of AKI recovery and the need for better recovery definitions. It does not establish whether creatinine/urine-output discordance identifies a clinically vulnerable subgroup.

[K3] Prowle, J. R., et al. "Urine output as a marker of renal function in critical illness." *Critical Care*, 2015. This work supports the use of urine output as a direct but noisy renal output measure. It does not establish whether discordance with creatinine is clinically consequential after adjustment for severity and measurement practices.

## Falsification criteria

If, after prespecified AKI episode and index-time definitions, severity adjustment, negative-control analyses, and temporal split, the discordant group does not show materially worse renal escalation or mortality than concordant recovery, the clinically consequential discordance claim is not supported.

## Baseline versus learned alternative

A simple severity-adjusted comparison is retained as baseline. A learned time-series model is an alternative to capture non-linear creatinine/urine-output trajectories and reveal whether the discordance signal persists beyond static covariates. The learned alternative could reveal whether the discordance signal is driven by specific temporal patterns (e.g., delayed urine output recovery) that a static comparison would miss.

## Measured-GFR limitation

MIMIC-IV does not provide measured GFR. Creatinine and urine output are surrogate measures of renal function. The experiment cannot establish whether discordance reflects true renal recovery or measurement artifacts.
