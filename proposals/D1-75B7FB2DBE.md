> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# B-beyond-P repeat-TACE execution repair

This targeted child preserves the frozen assay-specific experiment from `[prior hypothesis]`: adults with an independently selected first repeat-TACE event, complete assay-specific remote B / pre-repeat P / next observed same-assay Y values, and the fixed compact decision-time core. The exact five read-only HCC CSV sources, joins on (`patient master index`,`encounter number`), pathway/event ontology, 2018–2024 observation boundary, 14–180 day repeat-TACE gap, 15–90 day event window, B/P/Y clocks, and noncausal interpretation limits are unchanged.

## Mechanical repair

The inherited runner failed because `tace2_time` was not propagated into the event table although downstream encounter covariate reconstruction requires it. The repaired runner carries the field through the event merge. No population, temporal boundary, endpoint, estimand, or falsification criterion was changed. The runner also uses workspace-relative outputs and bounded controls (`N_BOOT`, `N_PART`, `N_PERM`) so a complete-source execution can finish under the resource limit.

## Computed execution

Managed job: `[research job]`, succeeded in 176.26 seconds using all rows of the five bound sources. Audit counts were encounters 105,044; diagnoses 1,810,646; procedures 338,040; medications 4,097,517; labs 28,159,928. Exact-assay lab rows were 476,846, with 476,820 valid uncensored numeric/time rows; seven duplicate groups and zero discordant groups were identified. Cohort counts were systemic 319 and comparator 1,491; selected repeat events were 159 and 526. Complete triplets were albumin 40 systemic / 118 comparator and total bilirubin 41 systemic / 119 comparator.

The bounded run used 5 fixed-pipeline bootstrap draws, 1 partition repetition, and 2 linkage permutations per assay; these are feasibility/indicative outputs, not substitutes for the frozen 2,000/20/500 requirements. Albumin primary held-out results: n=158, RMSE M0 3.2677 versus M1 3.1683, standardized delta-RMSE 0.02031. Total bilirubin: n=160, RMSE M0 9.8360 versus M1 9.8909, standardized delta-RMSE -0.00402. The bounded bootstrap intervals and permutation summaries are recorded in the JSON output, but are not interpreted as adequately powered inferential diagnostics.

Thus the run establishes computational feasibility and the exact reconstructed denominators. It does not establish clinical benefit, toxicity, hepatic failure, recovery, treatment effect, administration, adherence, mechanism, utility, or policy. Full mandated resampling, timing variants, influence/observation-selection gates, calibration diagnostics, and clinical adjudication remain unresolved.
