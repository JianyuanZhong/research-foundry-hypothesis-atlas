# Research hypothesis atlas

**Explore the aggregated hypothesis trees below.** Each node is a recorded hypothesis version or starting question; every line is a recorded parent link. These are AI-generated research proposals for expert review, not confirmed findings.

![All four aggregated hypothesis trees](figures/overview.svg)

**Snapshot:** 2026-10-05 01:02 China time. **2,582 nodes · 2,455 generated versions.**

| Domain | Nodes | Generated versions | Explore |
|---|---:|---:|---|
| Clinical & Population Health Research | 1,916 | 1,856 | [Proposals](domains/01-clinical-population.md) · [Full tree](figures/01-clinical-population.svg) |
| Therapeutic Target Prioritization | 47 | 45 | [Proposals](domains/02-therapeutic-targets.md) · [Full tree](figures/02-therapeutic-targets.svg) |
| Disease Mechanisms & Pathway Hypotheses | 37 | 34 | [Proposals](domains/03-disease-mechanisms.md) · [Full tree](figures/03-disease-mechanisms.svg) |
| Population Multi-omics & Disease Targets | 582 | 520 | [Proposals](domains/04-population-multiomics.md) · [Full tree](figures/04-population-multiomics.svg) |

## What is included

This refresh adds the Pure Qwen draft-first run, the completed Codex campaign, and 11 historical Sol runs across HCC, eICU, MIMIC-IV, and UK Biobank. Earlier atlas material is retained. The Codex campaign closed 80/80 episodes; Pure Qwen stopped at 58/60 and registered 114 drafts. Inclusion does not mean a proposal was selected, experimentally validated, or independently replicated. See [snapshot coverage](COVERAGE.md).

## Review a hypothesis

1. Choose a domain above and open its full tree or proposal catalog.
2. Follow a node ID to its complete scientific proposal.
3. Record feedback using the [review guide](REVIEW.md) and [review template](review-template.csv).

The overview includes every node and recorded edge. Large forests are dense at thumbnail scale: use the full SVG at native scale for node IDs, or search the domain catalog by ID or scientific term. IDs from the earlier edition remain stable.

## Reading the forests

Hollow nodes are imported starting questions; filled nodes are generated versions. Multiple parents indicate recorded recombination, so these forests are directed acyclic graphs rather than strict single-parent trees. Related questions are grouped by domain and dataset; no scientific relationship is inferred merely from similar titles. Shared seed records are deduplicated only when source identity and exact proposal text match; independently recorded generated versions remain separate. Node counts are not counts of unique discoveries.

UK Biobank hypotheses are grouped under Population Multi-omics & Disease Targets for continuity with the atlas taxonomy; many are clinical or epidemiological questions and do not use multi-omics. Dataset labels indicate study context, not replication.

## Public review edition

Proposal text is retained with internal paths, run references, source checksums, and incidental individual record references redacted. The public repository excludes source datasets, raw execution traces, private research packages, and credentials. Exact originals and source provenance are retained privately. The review catalogs do not display model scores or campaign labels next to hypotheses.

The [machine-readable graph](data/atlas.json) supports independent inspection. Rebuild all trees and catalogs with `python3 scripts/build_trees.py`; no model calls or private datasets are required.
