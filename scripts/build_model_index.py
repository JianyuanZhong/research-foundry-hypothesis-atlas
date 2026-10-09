"""Build the unblinded model index from public attribution metadata; no model calls."""
import collections
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', ' ')


def build():
    atlas = json.loads((ROOT / 'data/atlas.json').read_text())
    attribution = json.loads((ROOT / 'data/model-attribution.json').read_text())
    nodes = {n['id']: n for n in atlas['nodes']}
    records = {r['id']: r for r in attribution['nodes']}
    campaigns = {c['id']: c for c in attribution['campaigns']}
    assert attribution['atlas_frozen_at'] == atlas['frozen_at']
    assert len(records) == len(attribution['nodes']) == len(nodes)
    assert records.keys() == nodes.keys()
    groups = collections.defaultdict(list)
    for node_id, record in records.items():
        node = nodes[node_id]
        if node['seed']:
            assert record['campaign_id'] is None
        else:
            assert record['campaign_id'] in campaigns
            groups[record['campaign_id']].append(node)

    (ROOT / 'models').mkdir(exist_ok=True)
    totals = collections.Counter()
    for cid, campaign in campaigns.items():
        subset = sorted(groups[cid], key=lambda n: n['id'])
        totals[campaign['model_version']] += len(subset)
        lines = [
            f'# {campaign["label"]}', '', '[← Model index](../MODEL_INDEX.md)', '',
            '**Unblinded attribution catalog.** Complete independent review before consulting this page.', '',
            f'**Model version:** {campaign["model_version"]}  ',
            f'**Recorded model ID:** `{campaign["model_id"]}`  ',
            f'**Harness version:** {campaign["harness_version"]}  ',
            f'**Generated hypothesis versions:** {len(subset):,}', '',
            '| Hypothesis ID | Dataset | Hypothesis | Attribution basis |',
            '|---|---|---|---|',
        ]
        for node in subset:
            lines.append(f'| [{node["id"]}](../{node["proposal"]}) | {cell(node["dataset"])} | '
                         f'{cell(node["title"])} | {records[node["id"]]["attribution_basis"]} |')
        (ROOT / f'models/{cid}.md').write_text('\n'.join(lines) + '\n')

    with (ROOT / 'data/model-index.csv').open('w', newline='') as output:
        fields = ['hypothesis_id', 'title', 'domain', 'dataset', 'type', 'model_version',
                  'model_id', 'campaign', 'harness_version', 'attribution_basis', 'proposal']
        writer = csv.DictWriter(output, fieldnames=fields)
        writer.writeheader()
        for node_id, node in sorted(nodes.items()):
            record = records[node_id]
            campaign = campaigns.get(record['campaign_id'], {})
            writer.writerow(dict(
                hypothesis_id=node_id, title=node['title'], domain=node['domain'],
                dataset=node['dataset'], type='starting question' if node['seed'] else 'generated version',
                model_version=campaign.get('model_version', 'Not attributed (imported starting question)'),
                model_id=campaign.get('model_id', ''), campaign=campaign.get('label', ''),
                harness_version=campaign.get('harness_version', ''),
                attribution_basis=record['attribution_basis'], proposal=node['proposal']))

    lines = [
        '# Hypothesis model index', '', '[← Atlas](README.md)', '',
        '**This index reveals model attribution.** For independent blinded assessment, '
        'finish reviewing the [anonymous copies](REVIEW.md) before opening the catalogs below.', '',
        f'Atlas snapshot: **{atlas["frozen_at"][:10]}**. '
        f'**{sum(totals.values()):,} generated hypothesis versions** are mapped to their producing model; '
        f'**{sum(n["seed"] for n in nodes.values()):,} imported starting questions** are not assigned a generator.', '',
        'Search a hypothesis ID or title in the [complete CSV index](data/model-index.csv), '
        'or choose a campaign below for clickable proposals. '
        'The [attribution JSON](data/model-attribution.json) joins to [atlas.json](data/atlas.json) by node ID.', '',
        '## Models', '', '| Model version | Generated versions |', '|---|---:|',
    ]
    for model, count in totals.items():
        lines.append(f'| {model} | {count:,} |')
    lines += ['', '## Campaign catalogs', '',
              '| Campaign / hypothesis links | Model version | Recorded model ID | Harness version | Generated versions |',
              '|---|---|---|---|---:|']
    for cid, campaign in campaigns.items():
        lines.append(f'| [{campaign["label"]}](models/{cid}.md) | {campaign["model_version"]} | '
                     f'`{campaign["model_id"]}` | {campaign["harness_version"]} | {len(groups[cid]):,} |')
    lines += [
        '', '## Attribution and version semantics', '',
        '- Attribution follows the frozen source-to-review mapping and exact original proposal hashes. '
        'Author-linked attempt configurations are used where available; other rows use the campaign configuration '
        'and launch records. The basis is explicit in every catalog and CSV row.',
        '- These are recorded model identifiers, not independently verified immutable provider weight revisions. '
        'The `pa/` prefix is retained in the model ID; totals group it with the corresponding version.',
        '- Discovery RSI is the in-house fine-tuned Qwen 3.8 27B model, served as '
        '`qwen38-27b-sft-256k`. An immutable checkpoint revision is not established by this index.',
        '- v0.3.0 through v0.7.0 identify harness releases, not different Sol model versions. '
        '“Not recorded” means no harness version is asserted here.',
        '- The September 23 Novita campaign is attributed to `pa/gpt-5.6-sol` from the '
        'author-linked generation attempts. Its later run configuration names Luna; that later value '
        'does not replace the model recorded for these 138 generated versions.',
        '- Attribution identifies the producer of each recorded version, not the origin of every idea '
        'in its ancestry. Imported starting questions, subsequent translation, review, and selection '
        'are not counted as newly generated hypotheses.',
        '', '## Rebuild', '',
        'Run `python3 scripts/build_model_index.py` after updating the public attribution metadata. '
        'It validates complete node coverage and rebuilds this page, campaign catalogs, and CSV without '
        'private data or model calls. Private source IDs, hashes, paths, and raw traces are excluded.',
    ]
    (ROOT / 'MODEL_INDEX.md').write_text('\n'.join(lines) + '\n')
    print(f'Built model index: {sum(totals.values()):,} generated versions, {len(campaigns)} campaigns.')


if __name__ == '__main__':
    build()
