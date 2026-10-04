
# Episode 97 successor: decision-time content-identity frontier for findings-only HCC review allocation

## Clinical question and advance

The current HCC design asks whether a semantic report-based queue preserves a fixed-capacity retrospective documentary-M2 allocation advantage after all features attributable to the examination diagnosis/conclusion field are quarantined. A remaining clinically important ambiguity is that HCC stores an eventual examination payload but has no field showing whether that exact payload was final, released, retrievable, readable, or identical to the version present 24 hours before surgery. A model can pass a stored-content replay while depending on information unavailable at the decision point.

The decision question is narrow: among adults approaching a first eligible hepatobiliary resection, can a fixed number of preoperative review slots be allocated using routine CT/MRI report content so that more queued patients have an eventual source-defined documentary-M2 label, after restricting semantic features to findings-only text and stress-testing the minimum content-identical report coverage required for the margin to hold? This is a retrospective allocation experiment, not a treatment recommendation.

Strongest supported claim before execution: the HCC snapshot contains patient/encounter-linked procedures, examination acquisition starts, whole-accession report payloads with separate findings and diagnosis fields, and untimed same-encounter pathology narratives. A whole-source examination audit found 419,996 rows, 392,854 nonblank accession keys, 20,611 accessions with findings but no diagnosis, 39,462 with diagnosis but no findings, 332,653 with both, and 72 rows with blank accession keys. HCC has no report author/final/release/view/ingestion timestamp, report version identifier, raw images, pathology specimen/block/slide identifier or time, MDT roster, clinician action, treatment outcome, recurrence, or survival.

The unresolved claim is whether the documentary-M2 margin remains above the frozen threshold when (i) conclusion/mixed semantic features are masked, and (ii) the remaining findings-only stored content is restricted to a full-roster hypothetical mask satisfying a predeclared minimum fraction of content-identical report units, including singleton-stability stress. This can falsify a finite-corpus stored-content robustness claim. It cannot establish that any mask occurred clinically.

The advance is to separate eventual stored text, source-attributed findings-only text, and decision-time effective visibility/content identity. A supportive HCC result justifies a version-linked workflow audit or silent-mode study; it does not justify deployment. Missing lifecycle evidence produces an explicit inconclusive operational result, never an inferred “not visible” or “visible.”

## Hypothesis and estimands

Let G be the inherited frozen semantic score. Partition the locked 2019 feature manifest into PF (every source field exactly examinations.检查所见), PD (every source field exactly examinations.检查诊断), and PX (mixed, other, missing, or unresolved provenance). GF is a no-refit replay retaining PF and replacing PD/PX with the exact frozen unavailable block. GD retains only PD for diagnostic attribution; it cannot select a threshold or rescue GF.

For patient state z, pathology-reader book p, source/onset world omega, capacity ledger ell in {U,R,T}, and comparator C in {B,R,Gmask}, define the exact integer contrast:
D(F,C,ell,z) = 100 times [H(GF,ell,z) - H(C,ell,z)] / K.
H is the documentary-M2 count in a fixed top-K queue. All patient-slot, whole-accession, raw-component, and component-plus-text ledgers are evaluated.

For each eligible whole accession u=(患者主索引,就诊号,检查号), define a hypothetical bit ru. ru=1 means the stored report block is treated as available and content-identical to the version used by the frozen score; ru=0 masks all body-derived report features with the frozen unavailable block while retaining acquisition-only variables. This is a potential-data intervention, not observed availability. At fixed breakpoints c, require the full roster to have at least ceil(c times the number of clean eligible accessions) exposed units. After deleting patient j, restrict the same full-roster mask to survivors; never choose a new mask or reduced quota.

Primary hypothesis: there exists c* <= 0.80 for which GF passes every inherited gate and every coupled lower endpoint of D(F,C,ell,z) is strictly above 5 percentage points in both 2020 and untouched 2021 tests, under the same full-roster mask and anchored singleton deletion. The .80 value is fixed before outcomes and is a robustness benchmark, not an estimate of actual report-release probability.

Nested labels:
- stored-content supportive: GF and the exact anchored frontier pass;
- lifecycle/deployment supportive: prohibited from HCC-only computation; requires an external version-linked audit;
- adverse: valid computation fails a margin, comparator, randomization, deletion, patient-retention, content-identity, or anchored-frontier condition;
- inconclusive: any provenance, exact replay, outer-state, solve, or required external lifecycle prerequisite fails.

## Population and time

Use the first source-documented eligible hepatobiliary resection per patient: age at least 18; a prespecified dictionary independently reviewed by hepatobiliary surgeons; no earlier qualifying resection; and no recorded transplant, TACE/embolization, ablation, radiotherapy, targeted therapy, or immunotherapy in [t_op-365 days,t_op). Episode key is (患者主索引,就诊号); patient-wide medication/order searches retain encounter keys.

Use procedures.开始时间 for t_op only under the frozen source rule. A linked exact clock may be used only if clinically supported; date-like or midnight case-record values are represented as [date,date+24 hours), never as exact instants. Missing or competing clocks create coherent member/nonmember states, not favorable exclusion. Set t_dec=t_op-24 hours. An examination accession is eligible only when its 检查开始时间 interval is wholly within [t_op-90 days,t_dec). The primary cutoff is 24 hours; 12/48/72-hour onset worlds are descriptive sensitivities and cannot tune q*, K, c*, or the model.

Use patient-disjoint roles: 2015-2018 development; 2019 locks dictionary, preprocessing, feature/provenance manifest, models, reader books, ledgers, capacities, ties and seeds; 2020 threshold selection under the inherited protocol; 2021 untouched temporal confirmation; 2022 onward audit-only. GF and the frontier replay at inherited q* with no refitting, recalibration, feature reordering, or threshold change.

Retain K=floor(0.10 Nref), CU,CR,CT=floor(0.10 Wref^ell), nonvacuity checks, longest-prefix no-skip queues, fixed ties, no backfill, and no unused capacity. Retain complete coupled radiology/pathology books, two independent qualified readers plus adjudicator per modality, nine radiology-by-pathology pairs, unresolved labels, patient-disjoint deletion, and all three structural ledgers. Documentary-M2 is a frozen report/pathology text endpoint, not specimen-linked biological microvascular invasion.

## Exact source bindings

All sources are read-only ordinary CSVs; no archive member is used. Catalog:
 [internal dataset path]
with [source checksum].
HCC snapshot is [source checksum].

- encounters: [internal dataset path]; join (患者主索引,就诊号); 年龄,性别; 就诊时间,入院时间,出院时间.
- procedures: [internal dataset path]; same keys; 手术,手术来源; 开始时间,结束时间.
- examinations: [internal dataset path]; same keys plus 检查号 for whole-accession grain; 检查 modality; 检查所见 and 检查诊断 semantic fields; 开始时间 acquisition; 机器型号 audit. Preserve raw bytes, CSV ordinals, row multiplicity, payload digests and 检查号 bundles.
- pathology: [internal dataset path]; same keys; 病理,检查所见,检查诊断,机器型号 for documentary-M2 reader books only; no usable pathology time/specimen/accession.
- medications: [internal dataset path]; patient-wide 患者主索引 search, retaining 就诊号; 用药,药品类型,开始时间,结束时间 for prior-treatment exclusion only.
- orders: [internal dataset path](非药品)_2062526727266216118.csv; prior-treatment audit; 医嘱(非药品),医嘱状态,开立时间,开始时间,结束时间.
- diagnoses: [internal dataset path]; 诊断名称,诊断类型 for untimed corroboration/leakage audit only.
- clinical_documents: [internal dataset path]; narrative fields including 入院诊断__duplicate_2 for leakage audit only; no document time.
- labs: [internal dataset path]; 检验,定性结果,定量结果,标本类型,检验时间 for forbidden-predictor audit only; no separate unit column, so no cross-assay predictor.
- vitals: [internal dataset path]; only 患者主索引,就诊号; identifier-only.
- transfers: [internal dataset path]; only 患者主索引,就诊号; identifier-only.
- front_page: [internal dataset path]; 30-byte identifier-only file with 患者主索引,就诊号.

Same-encounter joins are exact on (患者主索引,就诊号). Examination grouping adds 检查号. Prior treatment is patient-wide before t_op. MIMIC, eICU, and UKB remain directly accessible read-only but are not pooled because there is no compatible HCC first-resection/eventual-Chinese-report/untimed-pathology-M2 frame or patient crosswalk.

## Computation and uncertainty

The compiler reads the inherited 2019 feature manifest, model, source audit, reader books, ledgers, threshold, tie key and hashes. Each feature must record model block/position/hash, exact table/field, accession and row ordinals, raw-byte digest, parser/tokenizer version and output digest, aggregation and missing block. PF is assigned only to features whose every contributing field is exactly examinations.检查所见. Mixed or absent provenance is masked. No clinical_documents, pathology, diagnoses, labs, identifiers, post-cutoff rows, reader labels or outcomes may enter the semantic predictor.

Compute inherited B,R,G,Gmask,GSA and then GF and diagnostic GD with byte-identical coefficients, feature order, scores, K, CU/CR/CT, ties, EMPTY positions, coupled states, 256 hash-random permutations and anchored deletions. For every year, source/onset world, reader/pathology book, ledger and c breakpoint, enumerate or certify exact extrema over full-roster masks. Require zero integer gap, residual <=1e-8, all tied maximizers, raw/quotient replay, and brute-force agreement on fixtures through 12 patients and real shards through 20. A sampled mask, timeout, favorable incumbent, state cap, missing witness or replay mismatch is inconclusive. Bootstrap is diagnostic only and cannot replace the exact finite-corpus estimand.

Required outputs:
- derived/findings_only_provenance_replay.parquet
- derived/full_roster_content_identity_masks.parquet
- derived/anchored_visibility_frontier.parquet
- derived/content_identity_audit.parquet
- derived/decision_time_lifecycle_certificate.json, which must be unavailable_in_hcc unless an external audit is supplied
- derived/result.json with one-hot outcome, c*, gates, witnesses and permitted conclusion.

## Falsification and limits

Use this precedence: computationally_inconclusive for any source/schema/hash/ordinal/byte/join/grain/provenance/model/replay/capacity/tie/exact-solve failure; feasibility_inconclusive for failed event, N/K/C, label-stable patient, book, nonvacuity or temporal-role requirement; decision_time_lifecycle_inconclusive whenever a claim would be about actual final/released/retrievable/readable content but the required external audit is absent; findings_only_adverse if GF fails inherited gates; stored_content_frontier_adverse if GF is valid but no c <= .80 gives all required lower endpoints above 5, with first failing world/year/comparator/ledger and patient/accession/feature witness; stored_content_frontier_supportive only when every computational gate passes in 2020 and 2021 and the exact anchored c* exists.

A supportive result means only that, in this frozen eventual-report corpus, a findings-only score retains a strict documentary-M2 capture margin under a stated hypothetical content-identity/release fraction and singleton-stable mask. It does not establish image-derived truth, semantic correctness, finalization, clinical availability, clinician reading, action, benefit, safety, fairness, transportability, treatment effect, recurrence, survival or cost. An adverse result falsifies this frozen robustness property, not report semantics generally. An inconclusive result identifies the missing evidence or computation.

An external version-linked audit must obtain report-version IDs, author/final/release/ingestion timestamps, service retrieval and clinician-view events, exact payload hashes, validated operation clocks, consecutive rosters and actual review capacity. Before deployment, a prospective silent-mode study must measure realized report availability, reviewer minutes, completion, clinician actions, subgroup performance, treatment decisions, harms, costs, recurrence, survival and patient benefit. Computation cannot establish resection dictionary correctness, reader qualification, Chinese semantic truth, pathology sampling adequacy, specimen-linked biological MVI, or treatment benefit.

The research-ambition README was inspected. The natural-history and Bayesian demonstrations were available locally and inspected in readable extracts; the Cell cancer main article and full STAR Methods remain unavailable and are not claimed as read. These references set a rigor standard only and do not determine the HCC topic.
