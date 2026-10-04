> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Compiler-ready successor: bounded missing-Y stress test for the frozen HCC repeat-TACE P-beyond-B experiment

## Change and clinical question

This is a targeted child of `[prior hypothesis]`. It keeps the selected parent’s frozen repeat-TACE reconstruction, exact B/P/event/Y clocks, outcome-blind support funnel, non-overlapping annual forward blocks, nested ridge models, complete-triplet primary estimand, and executed denominator/observation findings. It does not add a treatment comparison, replace an outcome, pool assays, or infer a clinical endpoint that is absent from the snapshot.

The clinically important unresolved question is whether the apparent later-era prognostic contrast could be an artifact of which BP-eligible episodes received a post-event assay. This matters because the 2023 and 2024 BP-eligible episodes have severe Y loss (29/43 and 14/70 observed overall, respectively), and the 2024 systemic arm has only one observed complete outcome. A point estimate among observed complete triplets cannot answer whether the same contrast would hold over the outcome-blind eligible risk set.

The falsifiable question is: **within each fixed annual future block, can the direction of the M1-versus-M0 prediction contrast over all outcome-blind BP-eligible episodes be determined under an explicitly declared bounded completion of missing Y, using only pre-origin observed outcomes to define the bound?** This is partial identification of a predictive error contrast, not missing-at-random inference or recovery of clinical outcomes.

The supplied demonstrations motivate longitudinal, temporally separated prediction and explicit attention to missingness and selection, but do not supply HCC-specific assay validity or justify assumptions here. The natural-history article demonstrates that longitudinal health trajectories can support future prediction while emphasizing learned bias; the cancer supplement describes a missingness discriminator in a multimodal model but is supplementary material only and does not establish that missingness is ignorable. The Bayesian article describes explicit likelihood/selection adjustment in other cohorts with genetic data unavailable here. This experiment therefore uses transparent bounds rather than importing those assumptions.

## Claims, limits, and data requirement

The strongest available evidence is the parent’s executed audit: the reconstruction yielded 319 systemic and 1,491 comparator patients, 159 and 526 selected repeat events, 242 BP-eligible episodes per assay, and complete triplets of 40/118 for albumin and 41/119 for bilirubin; 2022 had 28/29 observed outcomes, while 2023 and 2024 had 29/43 and 14/70. These are data-quality and observation findings, not evidence of treatment benefit or clinical response.

The new test will determine whether a locked prognostic error contrast is sign-robust under a declared numerical support scenario. It cannot establish transport across eras, causal effects, safety, hepatic failure, response, survival, mortality, utility, actionability, or patient benefit. The absence of laboratory units and reference ranges means albumin and total bilirubin remain separate recorded numeric assays; abnormality and clinical comparability require adjudication and metadata not present here.

## Frozen source bindings and complete scan

Use HCC snapshot `[source checksum]`. All source files are read-only. The exact five required files and schema bindings are:

* Encounters table `encounters`, schema `[internal dataset path]`, source `[internal dataset path]`, [source checksum]. Read `patient master index`, `encounter number`, `age`, `sex`, `encounter time`, `admission time`, `discharge time`, `encounter department`.
* Diagnoses table `diagnoses`, schema `[internal dataset path]`, source `[internal dataset path]`, [source checksum]. Read `Patient Master Index`, `Visit Number`, `Diagnosis Name`, `Diagnosis Type`; require literal `Hepatocellular carcinoma`. Diagnosis timing is inherited only from its linked encounter.
* Procedures table `procedures`, schema `[internal dataset path]`, source `[internal dataset path]`, [source checksum]. Read `Patient Master Index`, `Encounter Number`, `Surgery`, `Start Time`, `End Time`, `Surgery Source`; case-insensitive `TACE` or literal `Chemoembolization`, valid `Start Time`.
* Medications table `medications`, schema `[internal dataset path]`, source `[internal dataset path]`, [source checksum]. Read `Patient Master Index`, `Visit Number`, `Medication`, `Start Time`, `End Time`, `Single Dose`, `Single Dose Unit`, `Frequency`, `Administration Route`, `Medication Type`; retain the inherited days 1–14 systemic-record ontology and placebo, prior-exposure, bevacizumab-only, and generic-procedure ambiguity exclusions. These are recorded orders, not verified administrations.
* Labs table `labs`, schema `[internal dataset path]`, source `[internal dataset path]`, [source checksum]. Read `Patient Master Index`, `Encounter Number`, `Test`, `Qualitative Result`, `Quantitative Result`, `Specimen Type`, `Test Time`; retain exact assays `Albumin` and `Total Bilirubin`, valid uncensored numeric `Quantitative Result`, and `Test Time`.

Join every child table to encounters on (`Patient Master Index`,`Encounter Number`), verify duplicate composite keys before joining, and prevent many-to-many multiplication. Sequence procedures by `Patient Master Index` only after same-patient same-calendar-day duplicate collapse. Scan every row in all five files; do not sample, project away required fields, or use clinical notes/free text. The other HCC files are not needed for this experiment. No source row, identifier, note, or raw lab value may appear in a published output.

## Frozen population, clocks, and primary analysis

Reconstruct the first adjacent TACE1/TACE2 pair separated by 14–180 days and the first strict repeat event 15–90 days after TACE2, exactly as in the parent. Retain the HCC diagnosis and inherited eligibility/exclusion rules. Preserve event-date origins `2021-01-01`, `2022-01-01`, `2023-01-01`, and `2024-01-01`; training events satisfy `event_date < origin`, and the disjoint future block is `[origin, origin + 365 days)`.

For each event and assay, use:

* `B`: latest valid uncensored assay on TACE2 calendar days −30 through −1;
* `P`: latest valid assay in the selected repeat encounter in `[event_time−72 hours,event_time)`;
* `Y`: valid assay in that encounter in `(event_time,event_time+72 hours]`, nearest +24 hours under the inherited deterministic tie rule.

Require `B_time < P_time < event_time < Y_time`, positive P lead, one patient-assay row, and no laboratory-informed event selection. Construct the `event -> B -> P -> BP_eligible` funnel before reading any Y. `Y` missingness never makes an episode ineligible and is never coded as a negative result.

Keep the exact locked models and preprocessing:

```
M0: Y ~ B + systemic-record indicator + age + sex indicators
       + TACE2-to-repeat days + P-lead hours
M1: M0 + P
```

Use only pre-origin complete triplets for training, training-only age median imputation plus age-missingness indicator, sex coding, variance filtering, centering/scaling, inner leave-one-patient-out alpha selection over `[0.01, 0.1, 1, 10, 100]`, and ridge fitting. The primary estimand remains assay-specific standardized held-out RMSE gain `(RMSE(M0)-RMSE(M1))/SD_test(Y)` on observed complete triplets, with the parent’s paired arm-stratified patient-frequency bootstrap conditional on fixed pre-origin fits. The missing-Y layer must not alter folds, fits, predictions, weights, eligibility, support gates, or that bootstrap.

Before Y is read, retain the parent’s support gates: at least 20 BP-eligible episodes overall and at least 10 in each descriptive arm in both train and test, plus the corresponding complete-triplet gate. Preserve calendar propensity/ESS, same-arm matching, observation fractions/Wilson intervals, observation model, SMD, drift, and influence diagnostics as contextual, non-causal diagnostics.

## New compiler-ready partial-identification layer

For each assay and origin, fit M0/M1 once on the frozen training complete triplets and generate fixed predictions for **every** future BP-eligible episode. Emit an internal row key only for computation; published results contain aggregates. Each row has arm, block, BP eligibility, Y-observed status, predictions, and Y only in memory/derived restricted output when observed.

### Bounds

Set `L = min(Y_train)` and `U = max(Y_train)` from the exact assay-specific valid numeric training outcomes, before accessing any future Y. If `L >= U`, or if any observed future Y is outside `[L,U]`, mark that assay/origin/block `bounded_support = unsupported`; do not widen the primary analysis or invent a finite bound. A secondary, clearly non-temporal descriptive diagnostic may use the full-source assay range, but it is never used in fitting, eligibility, transport interpretation, or the primary estimand.

Let `O` be observed-Y future BP-eligible rows and `M` missing-Y future BP-eligible rows, with `N=|O|+|M|`. For model `j`, `r_{ji}(y)=(y-p_{ji})^2`. Compute observed sums directly. For every missing row, compute

```
lo_ji = (clip(p_ji, L, U) - p_ji)^2
hi_ji = max((L-p_ji)^2, (U-p_ji)^2)
```

and `MSE_j^-=(sum_O r_ji(Y_i)+sum_M lo_ji)/N`, `MSE_j^+=(sum_O r_ji(Y_i)+sum_M hi_ji)/N`. These are sharp marginal intervals for each model’s missing-case squared-error sum.

The primary bounded contrast is defined with a sign convention stated in every output:

```
C = MSE_0 - MSE_1       (C > 0 favors incremental M1)
q_i(y) = (y-p_0i)^2 - (y-p_1i)^2
       = 2*y*(p_1i-p_0i) + p_0i^2 - p_1i^2
C^- = [sum_O q_i(Y_i) + sum_M min(q_i(L), q_i(U))]/N
C^+ = [sum_O q_i(Y_i) + sum_M max(q_i(L), q_i(U))]/N
```

Because `q_i` is affine in the unknown Y, `[C^-,C^+]` is the sharp interval for the all-BP-eligible MSE contrast, not a difference of independently optimized marginal intervals. Report it overall and by systemic/comparator arm, with exact N, observed N, missing N, and missing fraction. Also report the three deterministic scenario contrasts obtained by setting all missing Y to L, all to U, and each missing row to the endpoint that minimizes or maximizes `q_i` (least favorable to M1 and least favorable to M0, respectively). These are endpoint scenarios, not imputations or plausible clinical values.

Do not report a falsely “sharp” RMSE-difference interval by subtracting two marginal square-root intervals. If an RMSE-scale interval is requested, calculate it only by an explicitly verified global optimization of `sqrt(sum r_0/N)-sqrt(sum r_1/N)` over the missing-Y box; otherwise report the exact MSE contrast interval and the two marginal MSE intervals. The compiler’s required result is the exact MSE contrast, avoiding this common invalid operation.

### Tipping point

Use a pre-origin reference `mu_train = mean(Y_train)`, separately for each assay and origin. Define the locked one-parameter completion family for missing rows:

```
y_i(delta) = clip(mu_train + delta, L, U),  i in M
C(delta) = [sum_O q_i(Y_i) + sum_M q_i(y_i(delta))]/N
```

Find the smallest absolute `delta` for which `C(delta)=0`, if a root exists over `delta in [L-mu_train, U-mu_train]`. Compute this exactly by enumerating the two clipping breakpoints and solving the resulting affine pieces; verify the returned root by recomputing `C(delta)` and its residual. If there is no root, report `no_crossing_in_bounded_family` and whether C is positive or negative throughout that family. If the interval is unsupported, report tipping point unknown. This scalar family is a sensitivity coordinate, not a claim that missing outcomes share a common shift. A zero-containing sharp interval is called sign-unidentified regardless of the tipping-point value.

### Primary versus sensitivity outputs

For each block and arm, emit:

1. unchanged observed-complete-triplet primary standardized RMSE gain and parent bootstrap interval;
2. exact bounded `MSE_0`, `MSE_1`, and `C=MSE_0-MSE_1` intervals over all BP-eligible rows;
3. missing and observed counts/fractions, support status, and the endpoint scenario table;
4. the verified tipping-point status and residual;
5. observed-case-only contrast and annual-block results without pooling arms into a treatment or causal contrast.

The denominator for the bounded MSE contrast is N BP-eligible episodes, not the observed-Y subset. Never standardize this contrast by `SD_test(Y)` when Y is missing. An optional dimensionless display may divide by the fixed training SD, explicitly labeled secondary and not the parent estimand. All aggregate outputs include snapshot ID, source paths and hashes, parser/version identifiers, denominator assertions, and branch labels.

## Falsification and interpretation

* **Supportive bounded robustness:** reconstruction and clocks pass; outcome-blind and complete-triplet gates pass; the unchanged primary result meets the inherited prespecified criterion; and the sharp bounded C interval is strictly positive with no material arm-specific reversal. This supports only robustness of the short-horizon predictive association under the declared training-range scenario in that selected block.
* **Adverse:** the locked primary contrast is non-positive in a supported block, M1 repeatedly worsens, or a bounded endpoint completion reverses C in a supported block. This challenges incremental prediction or shows selection sensitivity; it does not imply treatment harm or that B is clinically sufficient.
* **Selection-sensitive:** the observed primary gain is favorable but the sharp C interval contains zero, an endpoint scenario reverses sign, or the tipping point is close to the reference range. Report no transport conclusion.
* **Inconclusive/unsupported:** any support gate fails, arm counts are below threshold, training range is degenerate, observed future Y falls outside the training range, test SD is unidentified, or numerical/accounting assertions fail. This is expected for much of 2023–2024 and especially the 2024 systemic arm.

A favorable result does not establish clinical assay validity, units, severity, response, toxicity, survival, mortality, treatment effect, utility, actionability, or benefit. A negative result does not prove no information in P; it may reflect sparse support, selection, or model misspecification. A null is not equivalence. Clinical adjudication and an independent later/external/prospective cohort with assay units, reference ranges, reliable outcome capture, treatment administration, disease burden, and mortality are required for stronger claims.

## Compiler and verifier contract

Compiler inputs are the five exact read-only CSVs and the frozen parent support artifact only as an audit reference; all event reconstruction and denominator assertions must still be recomputed from source. It must scan all rows, assert source hashes, reproduce 319/1,491 patients, 159/526 events, 242 BP-eligible episodes per assay, and 40/118 albumin and 41/119 bilirubin complete triplets before interpreting model output. Any mismatch stops interpretation.

The verifier must test composite-key uniqueness/many-to-one joins, literal procedure/diagnosis filters, duplicate-day collapse, exact clocks and strict inequalities, outcome-blind eligibility, training-only L/U and `mu_train`, affine endpoint optimization, clipping-piece tipping-point residual, row accounting, patient-level uniqueness, and unchanged primary complete-triplet fits/bootstrap. It must inject or inspect branches where observed-case gain is favorable but C contains zero, where later point estimates are favorable but support fails, where future Y exceeds `[L,U]`, and where C is robustly positive. It must reject conclusions that call endpoint scenarios imputations, treat arms causally, invoke MAR, or upgrade bounded robustness to multi-era transport or clinical truth. Computational checks cannot adjudicate units, clinical meaning, unrecorded care, or patient benefit.

## What changed and what remains uncertain

Compared with `[prior hypothesis]`, this successor makes the missing-Y layer mechanically executable without changing the frozen science. It fixes the key ambiguity in “RMSE-difference bounds” by requiring the sharp affine MSE-contrast interval and forbidding subtraction of unrelated marginal RMSE bounds. It defines a reproducible, pre-origin tipping family and an exact piecewise solution, makes unsupported-range behavior a hard branch, and turns all endpoint patterns, denominators, and residual checks into verifier obligations. The partial-identification results remain unexecuted until compilation; no robustness conclusion is claimed here.
