# Provisional HCC repair checkpoint

Proposed relationship: among adults with a recorded liver resection in the HCC snapshot, early postoperative laboratory trajectory will be associated with an operational day 0–30 deterioration proxy beyond baseline severity and operative context. This is not established.

Verified source bindings: procedures is HCC/data_手术_8024330590283626027.csv with 患者主索引, 就诊号, 手术, 开始时间, 结束时间, 手术来源; labs is HCC/data_检验_609065997844652188.csv with 患者主索引, 就诊号, 检验, 定性结果, 定量结果, 标本类型, 检验时间; encounters is HCC/data_基本信息_2500296761891079109.csv with 患者主索引, 就诊号, 年龄, 性别, 就诊时间, 入院时间, 出院时间, 就诊科室; diagnoses is HCC/data_诊断_7504718184492840569.csv with 患者主索引, 就诊号, 诊断名称, 诊断类型. Transfers is HCC/data_出入转_7369490831683459252.csv and is identifier-only (患者主索引, 就诊号), so it cannot define a timed endpoint. All joins use 患者主索引 + 就诊号 within HCC.

Observed source facts: procedures has 338,040 rows and a broad liver-resection label match of 60,389 rows, including 4,086 missing 开始时间; the exact label dictionary and deterministic index-event tie-break remain to be frozen. Labs has 28,159,928 rows, 1,809 assay labels, and missing 检验时间 for 1,732 rows. The schema has no unit column; therefore assay units and clinical thresholds are not assumed. A conservative operational endpoint can only use timed records available in the snapshot and must be frozen before fitting; no clinical adjudication is available.

Preserved experiment: compare a regularized baseline using preoperative covariates and first eligible postoperative values with a low-dimensional trajectory model using first/last/slope/availability summaries over postoperative days 0–7, evaluated on a later index-date holdout. The deliverable is held-out incremental association, calibration, uncertainty, and missingness diagnostics, not a causal or treatment claim.

Missing evidence: exact liver-resection label dictionary, assay/unit dictionary, valid endpoint rule, and exactly three inspected key-reference receipts/source snapshots. These are explicitly unresolved.
