# Research hypothesis atlas

**Explore the aggregated hypothesis trees below.** For independent assessment, start with the [blinded review guide](REVIEW.md). Each node is a recorded hypothesis version or starting question; every line is a recorded parent link. These are AI-generated research proposals for expert review, not confirmed findings.

![All four aggregated hypothesis trees](figures/overview.svg)

**Snapshot:** 2026-10-15 00:10 China time. **4,649 nodes · 4,471 generated versions.**

| Domain | Nodes | Generated versions | Explore |
|---|---:|---:|---|
| Clinical & Population Health Research | 3,045 | 2,965 | [Proposals](domains/01-clinical-population.md) · [Full tree](figures/01-clinical-population.svg) |
| Therapeutic Target Prioritization | 262 | 258 | [Proposals](domains/02-therapeutic-targets.md) · [Full tree](figures/02-therapeutic-targets.svg) |
| Disease Mechanisms & Pathway Hypotheses | 334 | 328 | [Proposals](domains/03-disease-mechanisms.md) · [Full tree](figures/03-disease-mechanisms.svg) |
| Population Multi-omics & Disease Targets | 1,008 | 920 | [Proposals](domains/04-population-multiomics.md) · [Full tree](figures/04-population-multiomics.svg) |

## Browse by hypothesis writer

**[Complete model index](MODEL_INDEX.md)** · [Search every hypothesis in the CSV](data/model-index.csv). These indexes reveal attribution.

| Hypothesis writer / proposal catalog | Generated versions |
|---|---:|
| [Qwen original](models/qwen-original.md) | 628 |
| [discoveryRSI (our model)](models/discoveryrsi.md) | 1,176 |
| [Claude](models/claude.md) | 33 |
| [DeepSeek](models/deepseek.md) | 257 |
| [GLM](models/glm.md) | 36 |
| [GPT](models/gpt.md) | 2,341 |

**Qwen original** identifies hypotheses written by the original Qwen checkpoints. **discoveryRSI (our model)** identifies hypotheses written by our tuned checkpoints, including SFT and RAFT variants. Mixed runs use the hypothesis writer for the label; each campaign retains its exact recorded model ID in the [model index](MODEL_INDEX.md).

## What is included

The October 14 refresh adds original Qwen, additional discoveryRSI campaigns, Claude, DeepSeek, and GLM. All previously published hypotheses and IDs are retained. Counts include registered generated versions regardless of selection or outcome. Active campaigns contribute only their frozen records at collection. Inclusion does not mean a proposal was experimentally validated or independently replicated. See [snapshot coverage](COVERAGE.md).

## Review a hypothesis

1. Choose a domain above and open its full tree or proposal catalog.
2. Follow a node ID to its complete scientific proposal.
3. Record feedback using the [review guide](REVIEW.md) and [review template](review-template.csv).

The overview includes every node and recorded edge. Large forests are dense at thumbnail scale: use the full SVG at native scale for node IDs, or search the domain catalog by ID or scientific term. IDs from the earlier edition remain stable.

## Reading the forests

Hollow nodes are imported starting questions; filled nodes are generated versions. Multiple parents indicate recorded recombination, so these forests are directed acyclic graphs rather than strict single-parent trees. Related questions are grouped by domain and dataset; no scientific relationship is inferred merely from similar titles. Shared seed records are deduplicated only when source identity and exact proposal text match. Copied generated records are deduplicated only when candidate identity, exact original proposal hash, episode, author, and creation timestamp all match. Independently recorded generated versions remain separate. Node counts are not counts of unique discoveries.

UK Biobank hypotheses are grouped under Population Multi-omics & Disease Targets for continuity with the atlas taxonomy; many are clinical or epidemiological questions and do not use multi-omics. Dataset labels indicate study context, not replication.

## Public review edition

Proposal text is retained with internal paths, run references, source checksums, and incidental individual record references redacted. The public repository excludes source datasets, raw execution traces, private research packages, and credentials. Exact originals and source provenance are retained privately. Individual review copies and tree labels omit producer names, provider names, campaign identifiers, authoring dates, and individual provenance links. Model attribution is available separately in the [model index](MODEL_INDEX.md). Earlier English translations are preserved; newly added copies retain untranslated source passages where present and are labeled accordingly. Catalog titles are in English. See the [language and blinding notes](TRANSLATION.md).

The [machine-readable graph](data/atlas.json) supports independent inspection. Rebuild all trees and catalogs with `python3 scripts/build_trees.py`; no model calls or private datasets are required.
