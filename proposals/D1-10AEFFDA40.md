> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Canonical namespaced repeat-TACE episode table and locked Delta-Brier contrasts

## Assigned repair and clinical question

This is a targeted child of `[prior hypothesis]`. It preserves that candidate's frozen repeat-TACE population, recorded-pathway ontology, exact five HCC source bindings, strict laboratory parser and duplicate rule, B/P/H clocks, independently selected repeat event, common same-encounter `[12h,36h]` post-event panel, two-stage observation and outcome estimands, fixed feature lists, folds, penalties, seeds, and interpretation branches.

The question remains whether two leakage-safe intermediate-to-current direction indicators add reproducible prediction of the fixed concordant albumin-down/total-bilirubin-up transition after matching current/remote state and measurement-process variables, and whether the same indicators predict whether the post-event panel is observed. The endpoint is a direction-only laboratory transition, not hepatic deterioration, toxicity, decompensation, complication, treatment response, or a clinically important change.

## Frozen data binding and reconstruction targets

The complete-source experiment is bound to HCC snapshot `[source checksum]` and these five ordinary read-only CSVs: encounters `[internal dataset path]` (`patient master index`,`encounter number`,`age`,`sex`,`encounter time`,`admission time`,`discharge time`,`encounter department`); diagnoses `[internal dataset path]` (`patient master index`,`encounter number`,`diagnosis name`,`diagnosis type`); procedures `[internal dataset path]` (`patient master index`,`encounter number`,`surgery`,`start time`,`end time`,`procedure source`); medications `[internal dataset path]` (`patient master index`,`encounter number`,`medication`,`start time`); and labs `[internal dataset path]` (`patient master index`,`encounter number`,`test`,`quantitative result`,`qualitative result`,`specimen type`,`test time`). Their catalog hashes are, respectively, `[source checksum]`, `[source checksum]`, `[source checksum]`, `[source checksum]`, and `[source checksum]`.

The frozen no-sampling reconstruction targets are 319 systemic-record and 1,491 comparator pathways; 159 and 526 independently selected repeat events; 28,159,928 laboratory rows; 476,846 exact target-assay rows; 476,820 valid uncensored numeric-time rows; seven duplicate timestamp groups and zero discordant groups; 55/187 both-B-and-P episodes; and 34/97 observed common post panels. The observation denominator is 242 and the outcome denominator is 131 (86 events, 45 non-events). Histories are assay-specific in the 242 denominator, with one process mismatch, and shared clocks agree in the 131 outcome episodes.

## Canonical table repair

Materialize the episode-level objects exactly once as `episode_repeat_tace_canonical_v1`, keyed by non-null unique `episode_id`, before either stage model. Namespaces are disjoint: `alb_`, `bili_`, `B_`, `P_`, `L_`, `BP_`, `HP_`, `obs_`, and `y_`; source-order tie-break fields are retained with explicit names. Required assertions are one row per episode, no duplicate patient key in the outcome table, no pandas merge suffixes, and many-to-one joins only. Stage functions consume this table and must not merge `primary_pre`, history summaries, or observation summaries onto it again. A failure is a computational failure, not permission to change the population or estimand.

The executable contract is `[internal dataset path]`; its schema/binding specification is `[internal dataset path]`. In this workspace the supplied aggregate result contains no row-level `canonical_episode_rows`, so the uniqueness guard correctly failed rather than fabricating row-level validation. This is the narrow implementation defect still requiring compiler execution against the parent executable/source-derived episode table.

## Locked analyses

For `Y`, fit the inherited nested fixed-L2 logistic models under the frozen arm-balanced SHA-256 five-fold partition: `M_obs` includes BP directions, arm, age, sex, TACE2-to-repeat days, older pre-event lead, and shared H_any/count/recency; `M_hist` adds only HP albumin-down and HP bilirubin-up. Standardize only continuous variables using each training fold's mean and population SD. The estimand is pooled paired out-of-fold `Delta_Brier = Brier(M_obs)-Brier(M_hist)`.

For observation, use the 242-episode outcome-blind denominator and assay-specific process variables in `G_process`; `G_value` adds only the two numeric-history directions. Use the locked arm/O-balanced folds and `Delta_O = Brier(G_process)-Brier(G_value)`. Do not use weighting to recover the 111 unobserved outcomes.

Retain the locked 1,000 full-refit stratified patient bootstrap, 500 history-linkage permutations, four additional partition salts, leave-one-out influence diagnostic, component analyses, and `(24h,48h]` timing diagnostic. Apply the ordered branch rules without post hoc redesign.

## Computed conclusions available from the parent execution

The inherited aggregate execution reports `M_obs` Brier 0.225157 and `M_hist` Brier 0.222049, hence `Delta_Brier=0.003108`, against null Brier 0.226224. The full-refit bootstrap used 1,000 estimable replicates and gave percentile 95% interval `[0.001174,0.005542]`, with fraction at or below zero 0.0. The 500-linkage permutation 95th percentile was 0.001118. All five partition estimates were positive (0.002701–0.003163); leave-one-out values ranged 0.002956–0.003260 with maximum shift 0.000152. The observation negative control gave `G_process` Brier 0.177293, `G_value` Brier 0.177410, `Delta_O=-0.000117`, below the 0.01 materiality margin and below its 500-permutation 95th percentile 0.000172. The secondary albumin contrast was 0.003429; bilirubin was not estimable under its frozen folds because held-out fold 3 lacked both classes. The 24–48-hour diagnostic retained 95.4% and yielded 0.002912.

These metrics support only the ordered precise-null branch for the design-sized +0.02 increment: a reproducible, sub-margin conditional predictive gain in the selected 131 observed-panel episodes. They do not support a clinical-benefit, deterioration, causal, treatment, monitoring-policy, missing-at-random, or transportability claim. The negative control does not prove absence of selection bias. The row-level canonical uniqueness assertion and source-to-table computation were not independently rerun in this workspace; therefore the child remains repairable rather than valid pending a clean compiler execution that produces the canonical table and verifies these aggregates against it.

## What changed and what remains uncertain

The substantive change is implementation-level but scientifically protective: one canonical namespaced table and hard key assertions prevent dataframe collisions from silently changing the locked estimand. No scientific population, endpoint, clock, source, model, or threshold changed. The remaining uncertainty is whether the inherited aggregate metrics can be reproduced from the five sources through this contract and whether the selected, direction-only laboratory endpoint has any clinical meaning. Additional units, assay harmonization, supportive-care data, verified treatment exposure, adjudicated outcomes, and external/prospective validation would be required for stronger claims.
