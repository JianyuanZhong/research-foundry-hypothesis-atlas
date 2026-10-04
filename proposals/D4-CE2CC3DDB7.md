> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Audited frozen three-group CBC experiment: global non-rejection is supported; pairwise branch remains uncertified

## Purpose and lineage

This is an evidence-bounded successor of `[prior hypothesis]`, informed by the two published executed reports `[prior hypothesis]` and `[prior hypothesis]`. It does not change the frozen population, temporal boundaries, variables, six-dimensional estimand, nuisance models, primary global analysis, benchmark, sensitivities, falsifications, or claim limits after seeing the result. Its substantive advance is an independent reconciliation of the duplicate executed reports and a correction of what the artifacts can verify: the global result is supported, but the post-global pairwise labels are not.

The two executed children are not independent replications. They attach the identical execution program ([source checksum]), aggregate result ([source checksum]), audit program, and aggregate audit. Their numerical evidence must therefore be counted once. `[prior hypothesis]` provides the more complete narrative because it reports weak CRC nuisance calibration and benchmark sign discordance explicitly.

## Frozen scientific question and exact population

The tested hypothesis remains whether, among the exact 998 people selected because a first qualifying malignancy was recorded in inclusive `[E,H]`, adverse-oriented CBC trajectories have a nonzero adjusted six-dimensional residual moment across exhaustive first-diagnosis groups CRC, other GI, and non-GI. This is a selected-recorded-case association, not prospective cancer-risk estimation.

Retain without alteration:

- UK Biobank snapshot `[source checksum]`.
- Frozen private cohort [source checksum], with no sampling: 998 unique cases, 75 CRC, 69 other GI, and 854 non-GI.
- Assessment table `[internal dataset path]`, fields `53-0.0=B` and `53-1.0=L`.
- Biological-samples table `[internal dataset path]`, haemoglobin `30020`, MCV `30040`, primary platelet count `30080`, and exploratory RDW `30070`, instances 0 and 1.
- Population table `[internal dataset path]`, sex `31-0.0`, birth year `34-0.0`, birth month `52-0.0`.
- Health-outcomes table `[internal dataset path]`, recorded death `40000-0.0/1.0` and same-suffix cancer date/code pairs `40005-i.0`/`40006-i.0`, `i=0,...,21`.
- `E=L+366`, `H=L+1825`, inclusive `[E,H]`, completed age 40–75, and `365 <= L-B <= 2922`; day `E` is follow-up, not washout.
- Same-suffix date/code pairing; trim, uppercase and remove dots; `C00`–`C97` malignancy; no malignancy at or after recorded death; exact frozen-date and CRC reconciliation.
- First-date groups: CRC is any `C18`–`C20`; other GI is no CRC and any `C15`–`C17` or `C21`–`C26`; non-GI is no `C15`–`C26`.
- Annualization by `(instance1-instance0)/((L-B)/365.2425)` and orientation `S_Hb=-Hb slope`, `S_MCV=-MCV slope`, `S_PLT=+30080 slope`.
- Diagnosis lag `first_malignant_date-E`, with `lag_late=1` for 366–1459 days; it is post-landmark and cannot support prospective-risk claims.

## Frozen six-dimensional estimator and implementation audit

Let `G=(G_CRC,G_otherGI)`, non-GI reference; `C=(age at L, sex, repeat Hb, repeat MCV, repeat platelet, lag_late)`; and `S=(S_Hb,S_MCV,S_PLT)`. The frozen primary null remains

`E[(G-pi(C)) tensor (S-g(C))]=0`

in order CRC-Hb, CRC-MCV, CRC-PLT, otherGI-Hb, otherGI-MCV, otherGI-PLT.

The artifacts report the intended repeated cross-fitting implementation: 20 five-fold repetitions under seeds 20260909–20260928; joint outer stratification by group, lag and sex; all 100 test appearances retained; participant score contributions averaged over repetitions before one participant-level covariance; no treatment of 20 appearances as independent. Continuous comparators were standardized outer-training-only. Sex and lag remained on their defined scales. Five-fold inner tuning was training-only over `10^-4,...,10^4`, choosing the largest tied penalty. Inner folds were stratified by three-level group because the smallest outer-training group-by-lag-by-sex cell had only four people, making five-fold joint inner stratification impossible. This is a disclosed implementation limitation, not evidence of leakage.

Two binary ridge-logistic nuisances modeled CRC and other GI, and three ridge-linear nuisances modeled the trajectories. The logistic intercept and lag indicator were unpenalized. All 23,000 reported primary fits converged and all scores were finite. Held-out probability ranges were 0.0246–0.1162 for CRC and 0.0380–0.0933 for other GI. However, CRC nuisance performance was weak: the maximum penalty was selected in 88/100 CRC fits, cross-fitted log loss beat intercept-only in only 11/20 repetitions, and calibration slopes ranged from -1.486 to 0.614, including four negative slopes. Other-GI calibration was better but not perfect. These diagnostics do not invalidate the completed orthogonal score calculation, but they strengthen the requirement that non-rejection remain inconclusive.

## Verified primary result

The six estimates and robust SEs were:

- CRC-Hb -0.0002909713 (0.001583124)
- CRC-MCV -0.005606275 (0.005683865)
- CRC-PLT -0.027856870 (0.074301254)
- otherGI-Hb 0.0001557477 (0.001663687)
- otherGI-MCV 0.002452419 (0.005965456)
- otherGI-PLT -0.091487549 (0.096309513)

All max-statistic simultaneous 95% intervals cross zero. The reported global Wald statistic is 2.712829927. Independent aggregate calculation reproduces its chi-square reference p-value as 0.843929544623, and reproduces every simultaneous endpoint to within `1.12e-9`. The 20,000-draw participant-multiplier plus-one p-value is 0.8459577021, corresponding to 16,919 exceedances; its Monte Carlo uncertainty is immaterial to the gate decision. The multiplier 95th-percentile critical value is 12.55932. The covariance is positive definite with eigenvalues 0.002066–9.31844 and condition number 4509.68, below the frozen `10^10` threshold.

The global gate did not open. Therefore no component or pairwise contrast is scientifically interpreted.

## Pairwise contrast defect and bounded repair

The execution disclosed that its audit-only objects were the raw CRC score block for “CRC versus non-GI” and raw CRC-minus-otherGI score blocks for “CRC versus other-GI.” These labels are not mathematically justified by the frozen residual moments. For mutually exclusive groups, residualizing each binary indicator against `C` makes each raw score block a prevalence-weighted mixture of all three group-specific trajectory means. Even with no `C`, the raw CRC block changes when only the other-GI mean changes although the direct CRC-versus-non-GI mean difference is unchanged; similarly, CRC-minus-otherGI changes when only the non-GI mean changes although the direct CRC-versus-otherGI difference is unchanged. Thus neither raw object is generally proportional to its stated direct pairwise contrast.

This is a real design/compiler ambiguity in the supportive branch, not a reason for post-result redesign. Because the global gate was closed, it cannot change the observed decision. This successor therefore marks all reported local/FWER pairwise p-values as `AUDIT_ONLY_UNCERTIFIED_LABELS` and does not use them as evidence. It does not retrofit a new contrast definition after observing the result. Before any future supportive-path execution, the Lead must prespecify a mathematically identified pairwise estimand and its nuisance/score construction; that would be a new prospective design version, not a mechanical reinterpretation of this result.

An automatic verifier may check the six-dimensional global statistic, covariance, intervals, multiplier count and p-value, gate closure, and that no component/pairwise claim is made. It must fail any claim that the current raw contrast artifacts establish CRC-versus-other-GI or CRC-versus-non-GI differences.

## Benchmark, sensitivities, and negative controls

The ordinary unpenalized multinomial regression compared `C` with `C+S`. Its six-slope likelihood-ratio statistic was 2.1629155; all fits and 5,000 fitted-null parametric bootstrap samples converged; plus-one p=0.9052189562, corresponding to 4,526 exceedances. This is concordant with the primary analysis only at the global reject/non-reject decision level. It is not directional confirmation: five of six coefficient signs agree, while CRC-Hb differs.

Twenty joint three-slope permutation diagnostics within lag-by-sex strata reused group nuisances and retuned slope nuisances training-only, with 5,000 multipliers per seed. None had p<0.05; minimum p=0.05038992. That minimum corresponds to only 251 exceedances and has approximate Monte Carlo SE 0.00309, so “none below 0.05” should not be treated as a sharp calibration boundary. The defensible statement is that the 20 diagnostics showed no repeated extreme behavior. They do not establish finite-sample validity, exchangeability, or biological absence.

The exploratory two-dimensional RDW replacement was non-rejecting (Wald 0.85141, 20,000-draw multiplier p=0.65122) and cannot open or rescue the primary gate. Other GI remains a mechanistic comparator, not a negative control.

## Exact conclusion and falsification meaning

The strongest supported conclusion is:

`INCONCLUSIVE_WITHOUT_EVIDENCE_OF_GROUP_HETEROGENEITY; GLOBAL_GATE_CLOSED; PAIRWISE_BRANCH_UNCERTIFIED; NONREJECTION_IS_NOT_EQUIVALENCE`.

Supportive evidence was not observed. The global test did not reject, so no component or pairwise interpretation is permitted. The benchmark agreed only in global non-rejection. Adverse/equivalence evidence was not established because there is no clinically justified equivalence or incompatibility margin; simultaneous intervals are broad; CRC and other-GI groups are small; and CRC nuisance calibration is weak. The result does not show biological identity or absence of clinically important heterogeneity.

Had the global test rejected, the current artifacts still could not establish either named pairwise contrast because that branch was underdefined and then mislabeled in execution. Such a result would have been `INCONCLUSIVE_GLOBAL_HETEROGENEITY_WITH_UNCERTIFIED_PAIRWISE_LOCALIZATION` pending a prospectively specified pairwise experiment. This verifier branch is important even though the observed result did not trigger it.

Selection on future recorded malignancy can induce collider bias. The release-matched registry/prognosis gate remains `FAIL_UNCERTIFIED`. Available data do not certify registry completeness or provide pathology, stage, symptoms, FIT, endoscopy, treatment, routine-care CBC timing, harms, costs, or external validation. No equivalence, incidence, prospective-risk, causal, screening, sensitivity, specificity, PPV, lead-time, referral-utility, transportability, completeness, patient-benefit, mechanism, occult-bleeding, or inflammation claim is supported. Stronger biological or clinical conclusions require clinical coding/pathology/registry adjudication and a separate population-based study with people not selected on future malignancy and protocolized repeat CBCs.

## Independent aggregate support

A bounded managed audit read no source rows or participant data. It reconciled the identical child hashes, recomputed the chi-square reference and simultaneous intervals, reconstructed the plus-one exceedance counts and Monte Carlo precision, and supplied algebraic counterexamples to the pairwise labels. Artifact: `[internal dataset path]`, [source checksum]; managed job `[research job]`.
