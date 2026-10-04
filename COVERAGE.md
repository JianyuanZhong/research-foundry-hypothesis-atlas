# Snapshot coverage

[← Trees and expert review](README.md)

The October 5, 2026 refresh contains **2,582 nodes: 2,455 generated versions and 127 starting questions**, with **2,932 recorded parent links**. The previous 403 nodes retain their public IDs and original scientific source text; public redactions may improve between editions.

## Additions since the previous edition

| Addition | Generated versions added | Notes |
|---|---:|---|
| Completed Codex campaign | 27 | Now 67 generated versions in total; 80/80 episodes closed. |
| Pure Qwen draft-first campaign | 114 | Stopped at 58/60 episodes; all registered drafts included, regardless of selection. |
| Historical Sol campaigns | 2,008 | Eleven runs covering HCC, eICU, MIMIC-IV, and UK Biobank. |
| Historical starting questions | — | 30 additional seed records; repeated imports of the same seed are deduplicated. |

This is an archive of recorded scientific proposals, not a collection restricted to successful or selected outputs. The Qwen selection replay does not add new hypotheses and is not counted as new research.

## Source inventory

The table identifies campaign families for coverage auditing. Individual proposal catalogs retain anonymous IDs and omit model scores.

| Campaign family | Generated versions retained | Closed episodes observed |
|---|---:|---:|
| Earlier Luna clinical / population campaign | 225 | 86 |
| Earlier four-domain Luna campaign | 41 | 28 |
| Completed four-domain Codex campaign | 67 | 80 |
| Pure Qwen draft-first campaign | 114 | 58 |
| Sol, September 9, Codex time-bounded run | 14 | 1 |
| Sol, September 9, Claude-hosted episode campaign and continuations | 667 | 356 |
| Sol, September 9, Codex-hosted episode campaign and continuations | 575 | 387 |
| Sol, September 9, restarted ablation | 10 | 4 |
| Sol, September 13, v0.3.0 | 60 | 40 |
| Sol, September 13, v0.3.1 | 56 | 39 |
| Sol, September 13, v0.3.2 proxy campaign | 41 | 35 |
| Sol, September 14, v0.4.0 | 200 | 200 |
| Sol, September 15, v0.5.0 | 243 | 200 |
| Sol, September 22, v0.7.0 | 4 | 5 |
| Sol, September 23, Novita campaign | 138 | 165 |

Counts use committed candidate records and non-null episode closure timestamps at collection. Historical runs may include continuations or have stopped early. Episode closure is not evidence of scientific success. Five seed-only Sol runs and one empty Sol run were inspected but add no generated material and are excluded from the forests.

## Counting and lineage

- A node is one recorded version or imported starting question, not necessarily a unique hypothesis or discovery.
- Shared seeds are collapsed only when domain, source candidate identity, and exact proposal text match. Previously published IDs are preserved, including earlier seed representations.
- Independently recorded generated versions remain distinct even when their text is similar or identical.
- All recorded parents must exist. No inferred links, artificial common ancestors, or model-score-based pruning are introduced.
- UK Biobank is grouped under Population Multi-omics & Disease Targets for continuity. This includes clinical and epidemiological work that does not itself use multi-omics.

The public graph contains only review IDs, domain and dataset labels, titles, seed flags, parent links, and paths to redacted proposals. Exact source exports, hashes, source-to-review mappings, and originals remain in the private archive. Source datasets and run databases were accessed read-only; this refresh launched no model rollouts, training, or new experiments.
