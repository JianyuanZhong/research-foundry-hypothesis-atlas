> **Anonymous English review copy.** Producer and execution provenance are withheld. Scientific methods and citations are retained.

# Provisional HCC repair checkpoint

Proposed relationship: among adults with a recorded liver resection in the HCC snapshot, early postoperative laboratory trajectory will be associated with an operational day 0–30 deterioration proxy beyond baseline severity and operative context. This is not established.

Verified source bindings: procedures is HCC/data_surgery_8024330590283626027.csv with patient master index, encounter number, surgery, start time, end time, surgery source; labs is HCC/data_labs_609065997844652188.csv with patient master index, encounter number, test, qualitative result, quantitative result, specimen type, test time; encounters is HCC/data_basic_information_2500296761891079109.csv with patient master index, encounter number, age, sex, encounter time, admission time, discharge time, encounter department; diagnoses is HCC/data_diagnosis_7504718184492840569.csv with patient master index, encounter number, diagnosis name, diagnosis type. Transfers is HCC/data_admission_discharge_transfer_7369490831683459252.csv and is identifier-only (patient master index, encounter number), so it cannot define a timed endpoint. All joins use patient master index + encounter number within HCC.

Observed source facts: procedures has 338,040 rows and a broad liver-resection label match of 60,389 rows, including 4,086 missing start times; the exact label dictionary and deterministic index-event tie-break remain to be frozen. Labs has 28,159,928 rows, 1,809 assay labels, and missing test times for 1,732 rows. The schema has no unit column; therefore assay units and clinical thresholds are not assumed. A conservative operational endpoint can only use timed records available in the snapshot and must be frozen before fitting; no clinical adjudication is available.

Preserved experiment: compare a regularized baseline using preoperative covariates and first eligible postoperative values with a low-dimensional trajectory model using first/last/slope/availability summaries over postoperative days 0–7, evaluated on a later index-date holdout. The deliverable is held-out incremental association, calibration, uncertainty, and missingness diagnostics, not a causal or treatment claim.

Missing evidence: exact liver-resection label dictionary, assay/unit dictionary, valid endpoint rule, and exactly three inspected key-reference receipts/source snapshots. These are explicitly unresolved.
