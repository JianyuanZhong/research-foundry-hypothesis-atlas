# Episode 27 targeted executable freeze: incremental grip value after UACR

## Controlling parent and exact repair

This is a targeted child of assessed-repairable `[prior hypothesis]`. The complete parent proposal is controlling. This child changes no hypothesis, population, eligibility or temporal boundary, variable, equation, development fit, score, coefficient, roster membership, assay capacity, endpoint, estimand, denominator, margin, bootstrap, multiplicity family, safeguard, supportive/adverse/inconclusive rule, parent non-rescue hierarchy, evidence claim, or interpretation limit.

The only repair is serialization of the all-O1_hold membership artifact. The parent attached values in column order `eid,G1_selected,AG1_selected,A1_selected` ([source checksum]) while its combined manifest authenticates order `eid,G1_selected,A1_selected,AG1_selected` ([source checksum]). The columns contain identical membership values; only order differs. Because exact byte identity is a declared gate, the parent is noncomputable despite valid science. This child attaches the manifest-consistent serialization and makes [source checksum] controlling. The old serialization must not be used. No roster is regenerated, reranked, refilled, or reweighted.

## Unchanged scientific question and clinical importance

The unresolved primary hypothesis remains:

> Among the exact O1_hold population of 2,334 participants, at the same fixed n1=466 cystatin-C capacity, frozen baseline-trained AG1—standard covariates, observed/fallback UACR, and grip—identifies materially more visit-1 equation-defined combined-eGFR<60 reclassifications H1 than separately fitted frozen baseline-trained A1 without grip, with adverse-bound yield difference at least +2 per 1,000, adverse-bound yield ratio at least 1.10, simultaneous lower limits beyond both margins, positive directional-swap yield, and directionally concordant D1 severe-discordance evidence.

The secondary, nonrescuing hypothesis remains whether AG1 also yields at least one additional fixed-list participant with observed visit-1 UACR <3.0 mg/mmol and a subsequent recorded inpatient N18 event before death within nine calendar years than A1. This can qualify grip's incremental relevance only after the biochemical child gate and every required parent gate support.

This is clinically important because grip is inexpensive and plausibly reflects a non-GFR determinant of creatinine, but a service that already has creatinine and UACR should not add grip to a constrained cystatin-allocation rule unless it changes who is selected and materially increases target yield. The experiment isolates that incremental decision without interpreting the grip coefficient causally.

## Supported evidence versus unresolved claim

The parent evidence record remains controlling. Chen et al. (Kidney Medicine 2024, DOI `10.1016/j.xkme.2024.100796`, PMCID `PMC10986041`) was inspected from frozen full-text XML source `[source checksum]`, retrieved-source [source checksum]. It supports internal predictability of creatinine-cystatin discordance, not this fixed-capacity grip increment. Lees et al. (JAMA Network Open 2022, DOI `10.1001/jamanetworkopen.2022.38300`, PMCID `PMC9597396`) was inspected from frozen full-text XML source `[source checksum]`, [source checksum]; it supports prognostic relevance of cystatin reclassification in low albuminuria, not AG1:A1 allocation. Current KDIGO 2024 evidence supports combined creatinine-cystatin estimation when creatinine may be inaccurate and decisions depend on GFR, but does not validate grip as a referral rule or these margins.

The strongest computational evidence already supported is outcome-blind feasibility: all 502,370 joined source rows were read; O=134,118, development O/L=80,516/80,470, O1=5,823, O1_hold=2,334 and n1=466 were reproduced; the separately fitted A model selected lambda `0.0031622776601683794`; A1 roster ascending/ranked LF hashes are `[source checksum]` and `[source checksum]`; and parent G1/AG1 rosters were reproduced exactly. AG1 and A1 overlap on 427 participants, leaving 39 per directional swap. No H1, D1, selected N18, death, or policy-yield result was opened. Therefore no evidence yet supports or refutes the hypothesis.

## Exact executable objects

The following attached objects are controlling:

- `analysis/episode27_frozen_model_and_roster_manifest.json`, [source checksum]: all G/A/AG transforms, CV losses, penalties, coefficients, counts, roster identities and artifact hashes.
- `analysis/episode27_A1_roster_ranked.csv`, [source checksum]: exact 466 A1 eids in rank order.
- `analysis/episode27_frozen_visit1_rosters.csv`, [source checksum]: all 2,334 canonical eids, ordered and named exactly `eid,G1_selected,A1_selected,AG1_selected`.
- `analysis/episode27_recompute_A1_roster.py`, [source checksum]: independent outcome-blind source recomputation.
- Parent complete Episodes 16/17/18/19, parent model/roster manifest, and parent G1/AG1 ranked rosters retain their published hashes and are attached again for self-containment.

Any discrepancy in file identity, column order, model constants, selected penalties, scores, rank order, membership, or hashes makes the child noncomputable/inconclusive. The compiler may not silently rename/reorder an unverified file, delete AG's grip coefficient to create A, refit, substitute, rerank, or refill.

## Unchanged population, temporal boundaries, outcomes, analysis and falsification

The complete parent proposal controls these design-defining elements. In concise form, O1_hold is the parent instance-1 eligible population with valid sex `31-0.0`, age `21003-1.0` 40–69, date `53-1.0`, positive BMI `21001-1.0`, positive maximum grip `46-1.0/47-1.0`, positive serum creatinine `30700-1.0`, 2021 race-free eGFRcr in [60,90), no position-paired inpatient N17/N18 on or before t1, and original development excluded by `h>=60`. A1 and AG1 were fit only on baseline development H labels and applied at visit 1 without refit. Missing outcomes never alter fixed membership or denominator 466.

H1 is parent equation-defined eGFRcr-cys1 <60 from `30700-1.0,30720-1.0`, age and sex. D1 is eGFRcys1/eGFRcr1 <=0.70. Use fixed-denominator per-1,000 AG1:A1 yields, sharp shared-person missing-label bounds, the exact 2,000 shared-multiplicity PCG64DXSM bootstrap, and the parent's max-t/fallback rules. Support, adverse and inconclusive labels remain exactly those in the parent candidate, including its H difference/ratio materiality boundaries, D conjunction, directional swaps, h-lock and sex-stability checks. Boundary crossing, sparse swaps, >1% missingness, zero variance, or noncomputability is inconclusive, not equivalence.

For the secondary endpoint, observed UACR1 comes only from `30500-1.0,30505-1.0,30510-1.0`; fallback never creates observed low UACR, `<6.7` maps to 3.35 mg/L, and exactly 3.0 is not low. Pair `41270-0.i` only with `41280-0.i`, i=0,...,258. N18 must occur in `(t1,t1+9 calendar years]` strictly before earliest `40000-0.0/40000-1.0` death; same-day death competes and N17 neither counts nor censors. Preserve all event gates and non-rescue rules.

## Exact source bindings and evidence limits

All sources are read-only ordinary CSVs, archive member null, one-to-one joined on canonical `eid`:

- `population`: `[internal dataset path]`, [source checksum]; schema `datasets/ukb/table-38565c9e35e7cb6c.json`, [source checksum]; key `eid`; `31-0.0,21022-0.0`.
- `assessment`: `[internal dataset path]`, [source checksum]; schema `datasets/ukb/table-901ef6c7ddce2d51.json`, [source checksum]; key `eid`; `53-0.0,53-1.0,21003-1.0,21001-0.0/1.0,46-0.0/1.0,47-0.0/1.0`.
- `biological_samples`: `[internal dataset path]`, [source checksum]; schema `datasets/ukb/table-c6b666d905f3b02f.json`, [source checksum]; key `eid`; `30500/30505/30510/30700/30720` at instances 0 and 1. `30515-1.0` is absent and must not be invented.
- `health_outcomes`: `[internal dataset path]`, [source checksum]; schema `datasets/ukb/table-3cfae45e0905b0e3.json`, [source checksum]; key `eid`; paired `41270/41280` positions 0...258 and deaths `40000-0.0/1.0`.

Snapshot is `[source checksum]`; catalog is `[internal dataset path]`, [source checksum]. All four schemas declare `temporal_columns=[]`; encoded dates require explicit parsing. HCC, MIMIC-IV including notes, and eICU remain accessible read-only but cannot link to UKB eid and are not used. No private row or note was sent to public search.

Automatic verification can establish source identities, exact computation, artifact equality, uncertainty, gates, and whether conclusions follow outputs. It cannot establish measured GFR, true/persistent CKD, sarcopenia or mechanism, specimen chronology, complete follow-up, causal actionability, safety, workflow value, cost, fairness, transportability, or patient benefit. Those require repeated timed biomarkers, measured GFR, outpatient/kidney-replacement and censoring data, actions/medications, chart/nephrologist adjudication, workflow/cost/harms/equity review, external validation, and a prospective implementation or randomized testing-strategy study. Verifier fixtures must reject correct arithmetic paired with any such unsupported conclusion and must accept appropriately bounded supportive, adverse, and inconclusive interpretations.
