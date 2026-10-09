# Hypothesis model index

[← Atlas](README.md)

**This index reveals model attribution.** For independent blinded assessment, finish reviewing the [anonymous copies](REVIEW.md) before opening the catalogs below.

Atlas snapshot: **2026-10-05**. **2,455 generated hypothesis versions** are mapped to their producing model; **127 imported starting questions** are not assigned a generator.

Search a hypothesis ID or title in the [complete CSV index](data/model-index.csv), or choose a campaign below for clickable proposals. The [attribution JSON](data/model-attribution.json) joins to [atlas.json](data/atlas.json) by node ID.

## Models

| Model version | Generated versions |
|---|---:|
| gpt-5.6-luna | 266 |
| gpt-6-luna | 67 |
| Discovery RSI (Qwen 3.8 27B SFT) | 114 |
| gpt-5.6-sol | 2,008 |

## Campaign catalogs

| Campaign / hypothesis links | Model version | Recorded model ID | Harness version | Generated versions |
|---|---|---|---|---:|
| [Earlier Luna clinical / population campaign](models/C01.md) | gpt-5.6-luna | `pa/gpt-5.6-luna` | Not recorded | 225 |
| [Earlier four-domain Luna campaign](models/C02.md) | gpt-5.6-luna | `pa/gpt-5.6-luna` | Not recorded | 41 |
| [Completed four-domain Codex campaign](models/C03.md) | gpt-6-luna | `gpt-6-luna` | Not recorded | 67 |
| [Discovery RSI draft-first campaign](models/C04.md) | Discovery RSI (Qwen 3.8 27B SFT) | `qwen38-27b-sft-256k` | Not recorded | 114 |
| [Sol, September 9, Codex time-bounded run](models/C05.md) | gpt-5.6-sol | `gpt-5.6-sol` | Not recorded | 14 |
| [Sol, September 9, Claude-hosted campaign and continuations](models/C06.md) | gpt-5.6-sol | `gpt-5.6-sol` | Not recorded | 667 |
| [Sol, September 9, Codex-hosted campaign and continuations](models/C07.md) | gpt-5.6-sol | `gpt-5.6-sol` | Not recorded | 575 |
| [Sol, September 9, restarted ablation](models/C08.md) | gpt-5.6-sol | `gpt-5.6-sol` | Not recorded | 10 |
| [Sol, September 13, v0.3.0](models/C09.md) | gpt-5.6-sol | `gpt-5.6-sol` | v0.3.0 | 60 |
| [Sol, September 13, v0.3.1](models/C10.md) | gpt-5.6-sol | `gpt-5.6-sol` | v0.3.1 | 56 |
| [Sol, September 13, v0.3.2 proxy campaign](models/C11.md) | gpt-5.6-sol | `gpt-5.6-sol` | v0.3.2 | 41 |
| [Sol, September 14, v0.4.0](models/C12.md) | gpt-5.6-sol | `gpt-5.6-sol` | v0.4.0 | 200 |
| [Sol, September 15, v0.5.0](models/C13.md) | gpt-5.6-sol | `gpt-5.6-sol` | v0.5.0 | 243 |
| [Sol, September 22, v0.7.0](models/C14.md) | gpt-5.6-sol | `gpt-5.6-sol` | v0.7.0 | 4 |
| [Sol, September 23, Novita campaign](models/C15.md) | gpt-5.6-sol | `pa/gpt-5.6-sol` | Not recorded | 138 |

## Attribution and version semantics

- Attribution follows the frozen source-to-review mapping and exact original proposal hashes. Author-linked attempt configurations are used where available; other rows use the campaign configuration and launch records. The basis is explicit in every catalog and CSV row.
- These are recorded model identifiers, not independently verified immutable provider weight revisions. The `pa/` prefix is retained in the model ID; totals group it with the corresponding version.
- Discovery RSI is the in-house fine-tuned Qwen 3.8 27B model, served as `qwen38-27b-sft-256k`. An immutable checkpoint revision is not established by this index.
- v0.3.0 through v0.7.0 identify harness releases, not different Sol model versions. “Not recorded” means no harness version is asserted here.
- The September 23 Novita campaign is attributed to `pa/gpt-5.6-sol` from the author-linked generation attempts. Its later run configuration names Luna; that later value does not replace the model recorded for these 138 generated versions.
- Attribution identifies the producer of each recorded version, not the origin of every idea in its ancestry. Imported starting questions, subsequent translation, review, and selection are not counted as newly generated hypotheses.

## Rebuild

Run `python3 scripts/build_model_index.py` after updating the public attribution metadata. It validates complete node coverage and rebuilds this page, campaign catalogs, and CSV without private data or model calls. Private source IDs, hashes, paths, and raw traces are excluded.
