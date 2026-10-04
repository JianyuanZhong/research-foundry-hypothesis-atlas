"""Rebuild every public forest and catalog from data/atlas.json (standard library only)."""
from pathlib import Path
from collections import defaultdict,Counter
from html import escape
import json,math
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'data/atlas.json').read_text())
by={n['id']:n for n in data['nodes']}
BASE='https://github.com/JianyuanZhong/research-foundry-hypothesis-atlas/blob/main/'
COLORS={'HCC':'#e5ac76','MIMIC-IV':'#a2c7ed','eICU':'#b5d8a6','UK Biobank':'#c4b4ec','GEO / ArrayExpress':'#80cec4'}
depth={}
def level(i,active=()):
 if i in active:raise ValueError('Cycle in recorded lineage')
 if i not in depth:depth[i]=max((level(p,active+(i,))+1 for p in by[i]['parents']),default=0)
 return depth[i]
for i in by:level(i)

def layout(ns):
 layers=defaultdict(list)
 for n in ns:layers[depth[n['id']]].append(n['id'])
 order={}
 for d,ids in sorted(layers.items()):
  ids.sort(key=lambda i:(sum(order.get(p,0) for p in by[i]['parents'])/max(1,len(by[i]['parents'])),i))
  for j,i in enumerate(ids):order[i]=j/max(1,len(ids)-1)
 return {i:(d,j,len(ids)) for d,ids in layers.items() for j,i in enumerate(ids)}

def start(w,h,label):
 return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}"><rect width="100%" height="100%" fill="#111a21"/>']
def txt(out,x,y,s,size=14,color='#e5edf2',extra=''):
 out.append(f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial,sans-serif" font-size="{size}" {extra}>{escape(str(s))}</text>')
def graph(out,ns,box,detailed=False):
 x,y,w,h=box;pos=layout(ns);maxd=max((depth[n['id']] for n in ns),default=0)
 xy={i:(x+d*w/max(1,maxd),y+(j+.5)*h/count) for i,(d,j,count) in pos.items()}
 for n in ns:
  x2,y2=xy[n['id']]
  for p in n['parents']:
   if p not in xy:raise ValueError('Parent outside dataset forest')
   x1,y1=xy[p];middle=(x1+x2)/2
   out.append(f'<path d="M{x1:.2f},{y1:.2f} C{middle:.2f},{y1:.2f} {middle:.2f},{y2:.2f} {x2:.2f},{y2:.2f}" fill="none" stroke="#627787" stroke-opacity="{.65 if detailed else .30}" stroke-width="{1 if detailed else .55}"/>')
 for n in ns:
  xx,yy=xy[n['id']];color=COLORS[n['dataset']]
  out.append(f'<a href="{BASE+n["proposal"]}"><title>{escape(n["id"]+" · "+n["title"])}</title><circle cx="{xx:.2f}" cy="{yy:.2f}" r="{4 if detailed else 1.9}" fill="{color if not n["seed"] else "#111a21"}" stroke="{color}" stroke-width="1"/>')
  if detailed:txt(out,xx+8,yy+4,n['id'],10,color)
  out.append('</a>')
 return xy

def preview(out,domain,x,y,w,h):
 ns=[n for n in by.values() if n['domain']==domain['id']]
 out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#172630" stroke="#364a57"/>')
 names={'clinical_population':['Clinical & Population Health','HCC · MIMIC-IV · eICU'],'therapeutic_targets':['Therapeutic Target Prioritization','GEO / ArrayExpress'],'disease_mechanisms':['Disease Mechanisms & Pathways','GEO / ArrayExpress'],'population_multiomics':['Population Multi-omics & Targets','UK Biobank']}
 title,subtitle=names[domain['id']];txt(out,x+22,y+34,title,21);txt(out,x+22,y+59,f'{len(ns):,} nodes · {sum(not n["seed"] for n in ns):,} generated versions',14,'#bfd0db')
 groups=defaultdict(list)
 for n in ns:groups[n['dataset']].append(n)
 gh=(h-100)/len(groups)
 for j,(ds,group) in enumerate(sorted(groups.items())):
  yy=y+79+j*gh
  txt(out,x+22,yy+7,f'{ds} · {len(group):,}',12,COLORS[ds]);graph(out,group,(x+26,yy+20,w-57,gh-36))
 txt(out,x+22,y+h-12,'Recorded derivation →',10,'#91a7b5')

summary=[]
for d in data['domains']:
 ns=[n for n in by.values() if n['domain']==d['id']];slug=d['slug'];groups=defaultdict(list)
 for n in ns:groups[n['dataset']].append(n)
 # Detailed forest: IDs stay legible when opened at native scale.
 sizes={ds:max(200,max(Counter(depth[n['id']] for n in g).values())*27) for ds,g in groups.items()}
 width=max(1100,max(depth[n['id']] for n in ns)*170+260);height=sum(sizes.values())+100*len(groups)+110
 svg=start(width,height,d['name']+' — complete recorded forest')
 txt(svg,30,40,d['name'],27);txt(svg,30,68,f'{len(ns):,} nodes · {sum(len(n["parents"]) for n in ns):,} recorded parent links · download and open SVG for clickable IDs',15,'#aec1ce')
 offset=110
 for ds,group in sorted(groups.items()):
  txt(svg,30,offset,ds,21,COLORS[ds]);offset+=25
  graph(svg,group,(45,offset,max(170,max(depth[n['id']] for n in group)*170),sizes[ds]),True);offset+=sizes[ds]+75
 svg.append('</svg>');(ROOT/f'figures/{slug}.svg').write_text('\n'.join(svg)+'\n')
 sv=start(1160,820,d['name']);preview(sv,d,10,10,1140,800);sv.append('</svg>');(ROOT/f'figures/{slug}-preview.svg').write_text('\n'.join(sv)+'\n')
 lines=[f'# {d["name"]}','','[← All domains](../README.md) · [Expert review guide](../REVIEW.md)','',f'**{len(ns):,} nodes · {sum(not n["seed"] for n in ns):,} generated versions · {sum(len(n["parents"]) for n in ns):,} recorded parent links.**','',f'[![Aggregated hypothesis forest](../figures/{slug}-preview.svg)](../figures/{slug}.svg)','',f'[Open the complete tree with node IDs](../figures/{slug}.svg). Download and open the SVG at native scale for readable, clickable IDs. On GitHub, use the catalogs below to open proposals and search by ID or scientific term. Hollow nodes are starting questions; filled nodes are generated versions. Every recorded parent edge is retained, including multi-parent derivations. Separate roots are not artificially joined.','']
 for ds,group in sorted(groups.items()):
  lines += [f'## {ds}','',f'{len(group):,} nodes','']
  for n in sorted(group,key=lambda n:n['id']):
   parents=', '.join(f'[{p}](#{p.lower()})' for p in n['parents']) or '— (recorded root)'
   # Explicit stable anchors survive title edits and GitHub heading slug rules.
   lines += [f'<a id="{n["id"].lower()}"></a>',f'### {n["id"]} · {n["title"]}','','**Full scientific proposal:** [Read the public review copy](../'+n['proposal']+')','',f'**Derived from:** {parents}','','**Type:** '+('Starting question' if n['seed'] else 'Generated hypothesis version'),'']
 if d['id']=='clinical_population':
  # Keep each catalog comfortably below GitHub's large-Markdown display limits.
  header_end=next(i for i,line in enumerate(lines) if line.startswith('## '))
  index=lines[:header_end]+['## Dataset catalogs','']
  for ds,group in sorted(groups.items()):
   key={'HCC':'hcc','MIMIC-IV':'mimic','eICU':'eicu'}[ds]
   begin=lines.index('## '+ds)
   end=next((i for i in range(begin+1,len(lines)) if lines[i].startswith('## ')),len(lines))
   page=f'{slug}-{key}.md'
   page_lines=[f'# {ds} hypothesis catalog','','[← Clinical domain forest]('+slug+'.md)','','Search by node ID or scientific term. Parent IDs link within this catalog.','']+lines[begin:end]
   (ROOT/'domains'/page).write_text('\n'.join(page_lines).rstrip()+'\n')
   index += [f'- [{ds}: {len(group):,} hypotheses and starting questions]({page})','']
  lines=index
 (ROOT/f'domains/{slug}.md').write_text('\n'.join(lines)+'\n')
 summary.append((d,len(ns),sum(not n['seed'] for n in ns)))
svg=start(1240,1020,'Four aggregated domain hypothesis forests, all recorded nodes and parent links')
txt(svg,30,42,'Research hypothesis atlas',30);txt(svg,31,69,f'{len(by):,} nodes · {sum(not n["seed"] for n in by.values()):,} generated versions · {sum(len(n["parents"]) for n in by.values()):,} recorded parent links',17,'#bdd0db')
for i,d in enumerate(data['domains']):preview(svg,d,25+(i%2)*610,92+(i//2)*448,590,428)
txt(svg,30,1001,'All recorded lineages · hollow = starting question · filled = generated version · proposals require expert review',13,'#a9bdca');svg.append('</svg>')
(ROOT/'figures/overview.svg').write_text('\n'.join(svg)+'\n')
readme=['# Research hypothesis atlas','','**Explore the aggregated hypothesis trees below.** Each node is a recorded hypothesis version or starting question; every line is a recorded parent link. These are AI-generated research proposals for expert review, not confirmed findings.','','![All four aggregated hypothesis trees](figures/overview.svg)','',f'**Snapshot:** {data["frozen_at"][:16].replace("T"," ")} China time. **{len(by):,} nodes · {sum(not n["seed"] for n in by.values()):,} generated versions.**','','| Domain | Nodes | Generated versions | Explore |','|---|---:|---:|---|']
for d,n,g in summary:readme.append(f'| {d["name"]} | {n:,} | {g:,} | [Proposals](domains/{d["slug"]}.md) · [Full tree](figures/{d["slug"]}.svg) |')
readme += ['','## What is included','','This refresh adds the Pure Qwen draft-first run, the completed Codex campaign, and 11 historical Sol runs across HCC, eICU, MIMIC-IV, and UK Biobank. Earlier atlas material is retained. The Codex campaign closed 80/80 episodes; Pure Qwen stopped at 58/60 and registered 114 drafts. Inclusion does not mean a proposal was selected, experimentally validated, or independently replicated. See [snapshot coverage](COVERAGE.md).','','## Review a hypothesis','','1. Choose a domain above and open its full tree or proposal catalog.','2. Follow a node ID to its complete scientific proposal.','3. Record feedback using the [review guide](REVIEW.md) and [review template](review-template.csv).','','The overview includes every node and recorded edge. Large forests are dense at thumbnail scale: use the full SVG at native scale for node IDs, or search the domain catalog by ID or scientific term. IDs from the earlier edition remain stable.','','## Reading the forests','','Hollow nodes are imported starting questions; filled nodes are generated versions. Multiple parents indicate recorded recombination, so these forests are directed acyclic graphs rather than strict single-parent trees. Related questions are grouped by domain and dataset; no scientific relationship is inferred merely from similar titles. Shared seed records are deduplicated only when source identity and exact proposal text match; independently recorded generated versions remain separate. Node counts are not counts of unique discoveries.','','UK Biobank hypotheses are grouped under Population Multi-omics & Disease Targets for continuity with the atlas taxonomy; many are clinical or epidemiological questions and do not use multi-omics. Dataset labels indicate study context, not replication.','','## Public review edition','','Proposal text is retained with internal paths, run references, source checksums, and incidental individual record references redacted. The public repository excludes source datasets, raw execution traces, private research packages, and credentials. Exact originals and source provenance are retained privately. The review catalogs do not display model scores or campaign labels next to hypotheses.','','The [machine-readable graph](data/atlas.json) supports independent inspection. Rebuild all trees and catalogs with `python3 scripts/build_trees.py`; no model calls or private datasets are required.']
(ROOT/'README.md').write_text('\n'.join(readme)+'\n')
print('Built four complete forests, four previews, overview, domain catalogs and README.')
