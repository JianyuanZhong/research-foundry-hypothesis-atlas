# Structural missingness is mixed rather than a single absent-opportunity mechanism

## Question and substantive advance

The assessed parent `[prior hypothesis]` showed that the exact `carePlanGeneral` Ventilation labels were sparse, hospital-concentrated, and did not improve prediction of the inherited later structured respiratory-setting reduction. That result did not establish whether a zero label primarily meant that the generic care-plan interface was unavailable, that the Ventilation group was not used, or that a hospital used the group but selected other values.

This child tests the unresolved, falsifiable structural-missingness hypothesis: among independently eligible stays, hospital-level zeros for the exact or broader target are explained predominantly by no generic care-plan opportunity, no Ventilation-group opportunity, selective use of disjoint non-target Ventilation values, or a reproducible mixture of these states. The substantive advance is to replace an ambiguous label-zero interpretation with an outcome-blind, hospital-by-eligible-stay interface-footprint decomposition and sensitivity analysis. It does not infer bedside ventilation or the clinical meaning of any exported value.

The strongest evidence-supported claim remains limited to exported structured documentation: the exact and broader target values are sparse and concentrated, while the additional alternative `Ventilated -` values are rare. The experiment tests the documentation-opportunity explanation only. It does not test whether a value denotes invasive ventilation, daily evaluation, a spontaneous breathing trial, extubation readiness, extubation, quality, benefit, harm, or causality.

## Frozen population, timing, and source bindings

The inherited target-independent population, first qualifying stay selection, landmarks, airway definitions, and outcome boundaries are unchanged. The parent row artifact is `[internal dataset path]` ([source checksum]). It contains 22,421 inherited rows and 4,798 unique sid/landmark keys. No row sampling was used.

For each of `exact_unbounded`, `exact_airway_24h`, `exact_airway_12h`, and `exact_airway_6h`, the analysis used all inherited rows whose classification window was complete. The interface estimand retained a stay if at least one inherited landmark had a complete inclusive classification window `[L,L+360]`, and unioned all such landmarks within that stay. It did not access `robust_reduction`, complete outcome windows, or any outcome. The five landmarks were 1,440, 2,880, 4,320, 5,760, and 7,200 minutes.

The read-only eICU source was `carePlanGeneral`, ordinary gzip CSV `[internal dataset path]`, [source checksum]. Catalog table `datasets/eicu/table-33b82ae7a5609587.json` provides columns `cplgeneralid`, `patientunitstayid`, `activeupondischarge`, `cplitemoffset`, `cplgroup`, and `cplitemvalue`. The join key is `carePlanGeneral.patientunitstayid = inherited sid`; time is `cplitemoffset`, minutes from ICU admission; the classification window is `[L,L+360]` inclusive. There is no containing archive member. Hospital mapping for the source-wide descriptive check used `patient.csv.gz`, table `patient`, columns `patientunitstayid` and `hospitalid`, [source checksum].

## Interface footprint and negative controls

The executable scans all 3,115,018 rows before any outcome access. Normalization trims, collapses internal whitespace, and case-folds; missing values become `<na>`. The complete source-wide `cplgroup=Ventilation` vocabulary has exactly eight normalized values:

- `ventilated - with daily extubation evaluation` (51,862 rows)
- `ventilated - with no daily extubation trial` (14,907)
- `ventilated - rapid wean/extubation` (5,705)
- `ventilated - chronic dependency` (3,105)
- `spontaneous - adequate` (190,809)
- `spontaneous - tenuous` (32,587)
- `non-invasive ventilation` (26,836)
- `<na>` (7,581).

The exact target is the first two values. The broader target is every value with the literal normalized prefix `ventilated -`, adding only rapid-wean/extubation and chronic-dependency. The disjoint negative-control set is `<na>`, non-invasive ventilation, spontaneous-adequate, and spontaneous-tenuous; these are not treated as target synonyms. Generic opportunity is any care-plan row in the classification window, with Ventilation-group presence as the next layer. Hospital states are therefore: no generic row; generic row but no Ventilation row; Ventilation row but no broader target; and broader target present. Source-wide row presence is descriptive only and is not substituted for window opportunity.

For each definition, the primary unit is hospital by eligible stay. Footprints are binary stay indicators after unioning complete landmarks: generic care-plan presence, Ventilation-group presence, non-target Ventilation presence, exact target, broader target, alternative-broader target, spontaneous negative control, non-invasive negative control, and missing-valued Ventilation control. Common-support summaries require at least 20 eligible stays and five Ventilation-positive stays; the stricter local-selectivity subset requires at least five non-target-positive stays. Concentration is summarized by largest-hospital share and HHI. Hospital-specific broader-given-Ventilation proportions use Jeffreys 95% intervals. A 5,000-replicate outcome-blind bootstrap samples stays within each fixed hospital and definition, preserving all complete landmarks for sampled stays.

## Executed results

The scan found 131,623 rows belonging to inherited definition-repeated stays and 14,745 rows in inherited classification windows, with 9,286 inherited rows across the four definitions and 9,153 complete-window rows. Exact receipt reconstruction from raw care-plan rows matched every one of 9,153 complete-window inherited landmark rows (zero mismatches).

| airway definition | eligible stays | hospitals | generic stays | Ventilation-group stays | non-target stays | exact stays | broader stays | alternative-broader stays |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| unbounded | 1,993 | 76 | 828 | 294 | 204 | 97 | 99 | 3 |
| latest airway 24 h | 1,630 | 68 | 674 | 233 | 159 | 79 | 81 | 3 |
| latest airway 12 h | 1,113 | 43 | 483 | 160 | 99 | 62 | 64 | 2 |
| latest airway 6 h | 804 | 35 | 339 | 112 | 75 | 38 | 39 | 1 |

Hospital structural states, reported as hospitals and eligible stays, were:

| definition | no generic care-plan | generic but no Ventilation group | Ventilation group but no broader target | broader target present |
|---|---:|---:|---:|---:|
| unbounded | 15 / 27 | 15 / 75 | 28 / 456 | 18 / 1,435 |
| 24 h | 19 / 48 | 17 / 109 | 23 / 477 | 9 / 996 |
| 12 h | 15 / 35 | 7 / 31 | 14 / 362 | 7 / 685 |
| 6 h | 9 / 23 | 6 / 25 | 14 / 268 | 6 / 488 |

Among broader-zero hospitals, the fraction with no Ventilation-group footprint was 0.517 (unbounded), 0.610 (24 h), 0.611 (12 h), and 0.517 (6 h), below the prespecified 0.75 opportunity-dominance threshold. Selective local use was visible but not sufficiently reproducible for the prespecified gate: hospitals with at least 20 stays, at least five non-target-positive stays, and zero broader targets numbered 5, 4, 2, and 1 across the four definitions. The stricter rule required at least five unbounded and at least three in at least two bounded definitions, and therefore did not pass.

Footprints were concentrated differently. In the unbounded analysis, exact target stays had largest-hospital share 0.639 and HHI 0.422, whereas non-target Ventilation stays had share 0.221 and HHI 0.080. Broader target stays had share 0.646 and HHI 0.430. The corresponding exact/broader largest shares were 0.747/0.753 at 24 h, 0.774/0.781 at 12 h, and 0.658/0.667 at 6 h. Alternative-broader stays were only 3, 3, 2, and 1, all from one hospital. This supports both sparse target export and demonstrable local use of disjoint non-target values, but not a single universal mechanism.

The outcome-blind bootstrap medians (2.5th–97.5th percentiles) for broader-zero hospitals were 61 (59–65), 60 (59–62), 37 (36–39), and 30 (29–31). Selective-zero hospital medians were 5 (2–7), 4 (2–7), 2 (0–5), and 1 (0–3), showing attenuation with tighter airway bounds. Source-wide mapping found all eligible hospitals had at least one source care-plan, Ventilation, and broader row; thus source-wide availability does not establish availability in the frozen landmark windows. The source-wide check aggregates row totals, while hospital/stay interface states use window-restricted binary footprints.

## Falsification and interpretation

The prespecified gate was `inconclusive_mixed_opportunity_and_selectivity`: neither opportunity absence nor selective target omission dominated across the required sensitivity definitions. A supportive opportunity result would require at least 75% of broader-zero hospitals to lack Ventilation-group opportunity in unbounded and at least two bounded definitions. A supportive selective result would require the specified common-support selective-zero counts. Neither occurred. These criteria make the result falsifiable rather than allowing any zero pattern to be post hoc reclassified.

Supportive evidence for the mixed structural-missingness claim is that 28 unbounded hospitals (23, 14, and 14 under 24 h, 12 h, and 6 h) had Ventilation-group-positive eligible stays but no broader target, and disjoint spontaneous/non-invasive values were repeatedly observed. Adverse evidence against a simple no-opportunity explanation is the substantial fraction of broader-zero hospitals with a Ventilation footprint. Adverse evidence against a strong, general selective-vocabulary explanation is the sharp loss of selective support under tighter airway bounds and the failure of the prespecified cross-definition threshold. The result is inconclusive between several local workflow mechanisms, not evidence that any hospital provided or withheld clinical care.

The design cannot distinguish an unavailable local interface from a time-window mismatch, extraction rule, conflicting entries, or upstream mapping that collapses several concepts into the same exported value. It cannot adjudicate patient status, bedside actions, or clinical outcomes. Resolving those claims requires local interface/data-dictionary review, time-resolved device and airway records, SBT/extubation documentation, blinded clinical adjudication, or prospective multisite validation. Hospitals are the fixed observed set; bootstrap intervals do not transport to unseen hospitals.

## Reproducibility artifacts and verification boundary

Executable: `[internal dataset path]`, SHA-256 after removal of the invalid per-chunk unique-stay aggregation: `[source checksum]`.

Results: `[internal dataset path]` ([source checksum]). Compact output: `[internal dataset path]` ([source checksum]). Private stay cells: `[internal dataset path]`. Private hospital cells: `[internal dataset path]`.

An automatic verifier can check source hashes, complete source scan, normalization, vocabulary audit, frozen joins/windows, exact-receipt positive control, stay unioning, structural counts, concentration, fixed-hospital bootstrap, and prespecified gate logic. It cannot establish clinical semantics, workflow equivalence, care quality, benefit/harm, causality, or transportability.
