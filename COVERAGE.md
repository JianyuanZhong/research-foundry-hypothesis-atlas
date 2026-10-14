# Snapshot coverage

[← Trees and expert review](README.md)

**This page reveals aggregate campaign attribution.** Complete independent review from the [anonymous copies](REVIEW.md) before consulting the [model index](MODEL_INDEX.md).

The **2026-10-15 00:10 China time** refresh contains **4,649 nodes: 4,471 generated versions and 178 starting questions**, with **4,533 recorded parent links**. All previously published nodes retain their public IDs, proposal copies, and recorded lineage.

## Additions since October 5

This refresh adds **2,016 generated hypothesis versions** and no new starting questions. It includes original Qwen, additional tuned discoveryRSI campaigns, Claude, DeepSeek, and GLM, including the new mixed GLM/Luna campaign.

| Hypothesis writer | Generated versions in full atlas |
|---|---:|
| Qwen original | 628 |
| discoveryRSI (our model) | 1,176 |
| Claude | 23 |
| DeepSeek | 257 |
| GLM | 36 |
| GPT | 2,341 |

## Writer attribution

**Qwen original** includes original Qwen 3.5 4B and Qwen 3.8 27B checkpoints. **discoveryRSI (our model)** includes our tuned Qwen 3.5 4B SFT, Qwen 3.8 27B SFT, and Qwen 3.8 27B RAFT R2 checkpoints. Exact served model IDs and checkpoint variants are listed separately in the [model index](MODEL_INDEX.md) and CSV.

In mixed Qwen/Luna runs, attribution follows the model that wrote the hypothesis, using the author-linked attempt at candidate creation. Coordinators and reviewers are not assigned as hypothesis writers. A Qwen workflow setting does not change the label of a GLM-written hypothesis.

## Added source inventory

Counts describe the frozen records at collection. Closed episodes are observed closures, not successful experiments or a claim that a campaign has finished. Some October 14 campaigns may still be active.

| Campaign / retained hypothesis links | Writer | Newly added generated versions | Observed closed episodes |
|---|---|---:|---:|
| [Qwen original — balanced campaign](models/C16.md) | Qwen original | 95 | 120 |
| [discoveryRSI — balanced SFT campaign](models/C17.md) | discoveryRSI (our model) | 50 | 120 |
| [discoveryRSI — RAFT adapted campaign](models/C18.md) | discoveryRSI (our model) | 144 | 30 |
| [discoveryRSI — RAFT R2 campaign](models/C19.md) | discoveryRSI (our model) | 109 | 94 |
| [discoveryRSI — RAFT repaired campaign](models/C20.md) | discoveryRSI (our model) | 222 | 120 |
| [Qwen original — evidence iteration](models/C21.md) | Qwen original | 23 | 30 |
| [discoveryRSI — RAFT evidence iteration](models/C22.md) | discoveryRSI (our model) | 94 | 30 |
| [GLM — research contract campaign](models/C23.md) | GLM | 19 | 40 |
| [Claude — four-domain campaign](models/C24.md) | Claude | 33 | 21 |
| [Qwen original — initial 4B pilot](models/C25.md) | Qwen original | 1 | 1 |
| [Qwen original — mixed 4B campaign v8](models/C26.md) | Qwen original | 23 | 11 |
| [Qwen original — mixed 4B campaign v9](models/C27.md) | Qwen original | 176 | 40 |
| [Qwen original — 4B pilot v2](models/C28.md) | Qwen original | 15 | 25 |
| [Qwen original — 4B pilot v3](models/C29.md) | Qwen original | 39 | 36 |
| [Qwen original — 4B campaign v6](models/C30.md) | Qwen original | 42 | 40 |
| [Qwen original — 4B campaign v7](models/C31.md) | Qwen original | 153 | 40 |
| [Qwen original — mixed 27B campaign v9](models/C32.md) | Qwen original | 28 | 40 |
| [Qwen original — 27B campaign v7](models/C33.md) | Qwen original | 19 | 40 |
| [discoveryRSI — mixed 4B SFT campaign v9](models/C34.md) | discoveryRSI (our model) | 75 | 40 |
| [discoveryRSI — 4B SFT campaign v6](models/C35.md) | discoveryRSI (our model) | 11 | 40 |
| [discoveryRSI — 4B SFT campaign v7](models/C36.md) | discoveryRSI (our model) | 11 | 40 |
| [Qwen original — research contract replay](models/C37.md) | Qwen original | 14 | 30 |
| [discoveryRSI — RAFT research contract replay](models/C38.md) | discoveryRSI (our model) | 47 | 30 |
| [DeepSeek — four-domain campaign](models/C39.md) | DeepSeek | 257 | 281 |
| [discoveryRSI — fresh SFT campaign](models/C40.md) | discoveryRSI (our model) | 17 | 7 |
| [discoveryRSI — repaired fresh SFT campaign](models/C41.md) | discoveryRSI (our model) | 268 | 120 |
| [discoveryRSI — targeted SFT campaign](models/C42.md) | discoveryRSI (our model) | 3 | 13 |
| [discoveryRSI — fresh SFT continuation](models/C43.md) | discoveryRSI (our model) | 3 | 7 |
| [discoveryRSI — targeted SFT continuation](models/C44.md) | discoveryRSI (our model) | 8 | 15 |
| [GLM — mixed Luna research contract campaign](models/C45.md) | GLM | 17 | 64 |

The earlier 15 campaign catalogs remain included, covering GPT and the original 114-version tuned draft-first campaign. All campaigns are listed in the [complete model index](MODEL_INDEX.md). Empty and seed-only runs add no generated material. Evaluation copies, working files, unregistered drafts, selection replays, and reviewer outputs are not new scientific nodes.

## Counting and lineage

- A node is one registered hypothesis version or imported starting question, not necessarily a unique idea or discovery.
- All previously published IDs, review copies, dataset assignments, seed flags, and parent links are preserved.
- Shared seeds are collapsed only when domain, source candidate identity, and exact original proposal text match.
- 34 copied generated-record occurrences are reused when candidate identity, exact original proposal hash, episode, author, and creation timestamp all match. Independently recorded versions remain separate.
- All recorded parents must exist in the same domain and dataset. No inferred links, artificial common ancestors, or score-based pruning are introduced.
- UK Biobank remains under Population Multi-omics & Disease Targets for continuity, including clinical and epidemiological questions that do not use multi-omics.

## Public boundaries and languages

The public graph contains review IDs, domain and dataset labels, titles, seed flags, recorded parents, and paths to redacted proposals. Separate unblinded attribution metadata maps generated versions to their writer. Exact original source exports, hashes, and source-to-review mappings remain private. Source datasets, credentials, raw traces, and private execution packages are excluded.

Catalog titles are in English. Earlier English translations remain unchanged; 339 added copies retain Chinese source passages and carry explicit source-language notices. See [language and blinding notes](TRANSLATION.md). Source databases and datasets were accessed read-only. This update launches no new research rollouts, inference, training, or experiments.
