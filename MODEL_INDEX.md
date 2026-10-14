# Hypothesis model index

[← Atlas](README.md)

**This index reveals model attribution.** For independent blinded assessment, finish reviewing the [anonymous copies](REVIEW.md) before opening the catalogs below.

Atlas snapshot: **2026-10-14**. **4,444 generated hypothesis versions** are mapped to their producing model; **178 imported starting questions** are not assigned a generator.

Search a hypothesis ID or title in the [complete CSV index](data/model-index.csv), or choose a campaign below for clickable proposals. The [attribution JSON](data/model-attribution.json) joins to [atlas.json](data/atlas.json) by node ID.

**Mixed runs are labeled by the model that wrote the hypothesis.** Qwen-written outputs remain **Qwen original**; outputs from our tuned checkpoints are **discoveryRSI (our model)**, including when another model coordinates the run. Reviewers and coordinators are not assigned as hypothesis writers.

## Browse by hypothesis writer

| Hypothesis writer / all hypothesis links | Generated versions |
|---|---:|
| [Qwen original](models/qwen-original.md) | 628 |
| [discoveryRSI (our model)](models/discoveryrsi.md) | 1,176 |
| [Claude](models/claude.md) | 23 |
| [DeepSeek](models/deepseek.md) | 257 |
| [GLM](models/glm.md) | 19 |
| [GPT](models/gpt.md) | 2,341 |

## Model versions

| Model version | Generated versions |
|---|---:|
| gpt-5.6-luna | 266 |
| gpt-6-luna | 67 |
| discoveryRSI (Qwen 3.8 27B SFT) | 463 |
| gpt-5.6-sol | 2,008 |
| Qwen 3.8 27B (original) | 179 |
| discoveryRSI (Qwen 3.8 27B RAFT R2) | 616 |
| GLM 5.3 | 19 |
| Claude Opus 5 | 23 |
| Qwen 3.5 4B (original) | 449 |
| discoveryRSI (Qwen 3.5 4B SFT) | 97 |
| DeepSeek V4.1 Flash | 257 |

## Campaign catalogs

| Campaign / hypothesis links | Hypothesis writer | Model version | Recorded model ID | Harness version | Generated versions |
|---|---|---|---|---|---:|
| [Earlier Luna clinical / population campaign](models/C01.md) | GPT | gpt-5.6-luna | `pa/gpt-5.6-luna` | Not recorded | 225 |
| [Earlier four-domain Luna campaign](models/C02.md) | GPT | gpt-5.6-luna | `pa/gpt-5.6-luna` | Not recorded | 41 |
| [Completed four-domain Codex campaign](models/C03.md) | GPT | gpt-6-luna | `gpt-6-luna` | Not recorded | 67 |
| [discoveryRSI draft-first campaign](models/C04.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B SFT) | `qwen38-27b-sft-256k` | Not recorded | 114 |
| [Sol, September 9, Codex time-bounded run](models/C05.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | Not recorded | 14 |
| [Sol, September 9, Claude-hosted campaign and continuations](models/C06.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | Not recorded | 667 |
| [Sol, September 9, Codex-hosted campaign and continuations](models/C07.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | Not recorded | 575 |
| [Sol, September 9, restarted ablation](models/C08.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | Not recorded | 10 |
| [Sol, September 13, v0.3.0](models/C09.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | v0.3.0 | 60 |
| [Sol, September 13, v0.3.1](models/C10.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | v0.3.1 | 56 |
| [Sol, September 13, v0.3.2 proxy campaign](models/C11.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | v0.3.2 | 41 |
| [Sol, September 14, v0.4.0](models/C12.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | v0.4.0 | 200 |
| [Sol, September 15, v0.5.0](models/C13.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | v0.5.0 | 243 |
| [Sol, September 22, v0.7.0](models/C14.md) | GPT | gpt-5.6-sol | `gpt-5.6-sol` | v0.7.0 | 4 |
| [Sol, September 23, Novita campaign](models/C15.md) | GPT | gpt-5.6-sol | `pa/gpt-5.6-sol` | Not recorded | 138 |
| [Qwen original — balanced campaign](models/C16.md) | Qwen original | Qwen 3.8 27B (original) | `qwen38-27b` | Not recorded | 95 |
| [discoveryRSI — balanced SFT campaign](models/C17.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B SFT) | `qwen38-27b-sft-256k` | Not recorded | 50 |
| [discoveryRSI — RAFT adapted campaign](models/C18.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B RAFT R2) | `qwen38-27b-raft-r2-150` | Not recorded | 144 |
| [discoveryRSI — RAFT R2 campaign](models/C19.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B RAFT R2) | `qwen38-27b-raft-r2-150` | Not recorded | 109 |
| [discoveryRSI — RAFT repaired campaign](models/C20.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B RAFT R2) | `qwen38-27b-raft-r2-150` | Not recorded | 222 |
| [Qwen original — evidence iteration](models/C21.md) | Qwen original | Qwen 3.8 27B (original) | `qwen38-27b` | Not recorded | 23 |
| [discoveryRSI — RAFT evidence iteration](models/C22.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B RAFT R2) | `qwen38-27b-raft-r2-150` | Not recorded | 94 |
| [GLM — research contract campaign](models/C23.md) | GLM | GLM 5.3 | `glm-5.3` | Not recorded | 19 |
| [Claude — four-domain campaign](models/C24.md) | Claude | Claude Opus 5 | `claude-opus-5` | Not recorded | 23 |
| [Qwen original — initial 4B pilot](models/C25.md) | Qwen original | Qwen 3.5 4B (original) | `qwen-original` | Not recorded | 1 |
| [Qwen original — mixed 4B campaign v8](models/C26.md) | Qwen original | Qwen 3.5 4B (original) | `qwen-original` | Not recorded | 23 |
| [Qwen original — mixed 4B campaign v9](models/C27.md) | Qwen original | Qwen 3.5 4B (original) | `qwen-original` | Not recorded | 176 |
| [Qwen original — 4B pilot v2](models/C28.md) | Qwen original | Qwen 3.5 4B (original) | `qwen-original` | Not recorded | 15 |
| [Qwen original — 4B pilot v3](models/C29.md) | Qwen original | Qwen 3.5 4B (original) | `qwen-original` | Not recorded | 39 |
| [Qwen original — 4B campaign v6](models/C30.md) | Qwen original | Qwen 3.5 4B (original) | `qwen-original` | Not recorded | 42 |
| [Qwen original — 4B campaign v7](models/C31.md) | Qwen original | Qwen 3.5 4B (original) | `qwen-original` | Not recorded | 153 |
| [Qwen original — mixed 27B campaign v9](models/C32.md) | Qwen original | Qwen 3.8 27B (original) | `qwen38-27b` | Not recorded | 28 |
| [Qwen original — 27B campaign v7](models/C33.md) | Qwen original | Qwen 3.8 27B (original) | `qwen38-27b` | Not recorded | 19 |
| [discoveryRSI — mixed 4B SFT campaign v9](models/C34.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.5 4B SFT) | `qwen-sft-256k` | Not recorded | 75 |
| [discoveryRSI — 4B SFT campaign v6](models/C35.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.5 4B SFT) | `qwen-sft-256k` | Not recorded | 11 |
| [discoveryRSI — 4B SFT campaign v7](models/C36.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.5 4B SFT) | `qwen-sft-256k` | Not recorded | 11 |
| [Qwen original — research contract replay](models/C37.md) | Qwen original | Qwen 3.8 27B (original) | `qwen38-27b` | Not recorded | 14 |
| [discoveryRSI — RAFT research contract replay](models/C38.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B RAFT R2) | `qwen38-27b-raft-r2-150` | Not recorded | 47 |
| [DeepSeek — four-domain campaign](models/C39.md) | DeepSeek | DeepSeek V4.1 Flash | `deepseek-v4.1-flash` | Not recorded | 257 |
| [discoveryRSI — fresh SFT campaign](models/C40.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B SFT) | `qwen38-27b-sft-256k` | Not recorded | 17 |
| [discoveryRSI — repaired fresh SFT campaign](models/C41.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B SFT) | `qwen38-27b-sft-256k` | Not recorded | 268 |
| [discoveryRSI — targeted SFT campaign](models/C42.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B SFT) | `qwen38-27b-sft-256k` | Not recorded | 3 |
| [discoveryRSI — fresh SFT continuation](models/C43.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B SFT) | `qwen38-27b-sft-256k` | Not recorded | 3 |
| [discoveryRSI — targeted SFT continuation](models/C44.md) | discoveryRSI (our model) | discoveryRSI (Qwen 3.8 27B SFT) | `qwen38-27b-sft-256k` | Not recorded | 8 |

## Attribution and version semantics

- Attribution follows the frozen source-to-review mapping and exact original proposal hashes. Author-linked attempt configurations are used where available; other rows use the campaign configuration and launch records. The basis is explicit in every catalog and CSV row.
- These are recorded model identifiers, not independently verified immutable provider weight revisions. The `pa/` prefix is retained in the model ID; totals group it with the corresponding version.
- Qwen original includes the original Qwen 3.5 4B and Qwen 3.8 27B checkpoints. discoveryRSI (our model) includes our Qwen 3.5 4B SFT, Qwen 3.8 27B SFT, and Qwen 3.8 27B RAFT R2 checkpoints. The exact served ID and training variant remain visible in every campaign and CSV row. Immutable provider or checkpoint revisions are not independently established by this index.
- Mixed Qwen/Luna runs are assigned to Qwen original or discoveryRSI from the author-linked generation attempt at candidate creation, as requested. A Qwen workflow setting alone does not make GLM-generated proposals Qwen outputs.
- v0.3.0 through v0.7.0 identify harness releases, not different Sol model versions. “Not recorded” means no harness version is asserted here.
- The September 23 Novita campaign is attributed to `pa/gpt-5.6-sol` from the author-linked generation attempts. Its later run configuration names Luna; that later value does not replace the model recorded for these 138 generated versions.
- Attribution identifies the producer of each recorded version, not the origin of every idea in its ancestry. Imported starting questions, subsequent translation, review, and selection are not counted as newly generated hypotheses.

## Rebuild

Run `python3 scripts/build_model_index.py` after updating the public attribution metadata. It validates complete node coverage and rebuilds this page, campaign catalogs, and CSV without private data or model calls. Private source IDs, hashes, paths, and raw traces are excluded.
