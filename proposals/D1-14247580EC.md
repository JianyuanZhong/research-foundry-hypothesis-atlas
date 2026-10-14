> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Discordant recovery after AKI: does creatinine recovery overstate renal recovery?

## Question

Among ICU patients with AKI, does creatinine-based recovery misclassify patients whose urine output remains abnormal, and does that discordant subgroup have worse subsequent renal escalation or mortality than concordant recovery or non-recovery?

## Evidence and design

MIMIC-IV v3.1 provides repeated creatinine, urine output, fluid balance, renal support, vasopressors, and mortality. The prior literature supports the concern that creatinine-based estimates can diverge from measured kidney function in critical illness [K1]. The experiment prespecifies AKI episode and index time, compares discordant, concordant, and non-recovered groups, and tests renal escalation, ICU death, and in-hospital death with severity-adjusted and negative-control analyses. Urine output is a direct but noisy renal output measure [K2]. Measured kidney function can diverge from creatinine-based estimates in critical illness [K3].

## Unresolved issues

The main unresolved issue is whether discordance is clinically consequential after accounting for illness severity, treatment intensity, and measurement practices, or whether it is explained by sampling and fluid-status artifacts.

## Key references

- [K1] Tang Y, Zhang S, Wang Q, Zhang Q, Ji L, Li R, Fang M. An interpretable machine learning model for early prediction of subsequent observed CRRT initiation in patients with sepsis-associated acute kidney injury. Clin Exp Med. 2026;26(1):345. doi:10.1007/s10238-026-02305-1.
- [K2] Miranda DW, Makarem A, Liquori C, et al. Rationale and design of a pilot randomized control trial of permissive hypotension after cardiac surgery: The PHACS trial. Am Heart J Plus. 2026;70:100852. doi:10.1016/j.ahjo.2026.100852.
- [K3] Shang N, Xu K, Stevens JS, Barasch J, Kiryluk K. Electronic Phenotype for Detection, Staging, and Subtyping of Acute Kidney Injury. Am J Kidney Dis. 2026;88(3):414-423.e1. doi:10.1053/j.ajkd.2026.04.010.

## Falsification

A severity-adjusted comparison showing no excess renal escalation or mortality in the discordant subgroup, or a discordance pattern fully explained by fluid status and sampling intensity, would falsify the claim of clinically consequential misclassification.

## Alternatives

The discordance may reflect sampling practices, fluid status, or measurement artifacts rather than true renal recovery discordance. A learned model that captures non-linear interactions between creatinine and urine output may outperform the simple discordance phenotype, providing a substantive alternative to the baseline comparison.
