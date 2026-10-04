"""Validate lineage, review navigation, SVG coverage, and public export boundaries."""
from pathlib import Path
import collections,json,re,xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
d=json.loads((ROOT/'data/atlas.json').read_text());ns=d['nodes'];by={n['id']:n for n in ns}
assert len(by)==len(ns)
assert {p.stem for p in (ROOT/'proposals').glob('*.md')}==set(by)
seen=set();active=set()
def visit(i):
 if i in seen:return
 assert i not in active,('cycle',i)
 active.add(i)
 for p in by[i]['parents']:
  assert p in by and by[p]['domain']==by[i]['domain'] and by[p]['dataset']==by[i]['dataset'],(i,p)
  visit(p)
 active.remove(i);seen.add(i)
for i in by:visit(i)
all_catalogs='\n'.join(p.read_text() for p in (ROOT/'domains').glob('*.md'))
for n in ns:
 assert re.fullmatch('D[1-4]-[A-F0-9]{10}',n['id'])
 assert set(n)=={'id','domain','dataset','title','seed','parents','proposal'}
 assert f'### {n["id"]} · ' in all_catalogs
 assert f'<a id="{n["id"].lower()}"></a>' in all_catalogs
 assert (ROOT/n['proposal']).stat().st_size>0
for p in list((ROOT/'domains').glob('*.md'))+[ROOT/'README.md',ROOT/'COVERAGE.md',ROOT/'REVIEW.md',ROOT/'TRANSLATION.md']:
 s=p.read_text()
 for target in re.findall(r'\]\(([^)]+)\)',s):
  if target.startswith(('https:','http:')):continue
  path,_,anchor=target.partition('#');dest=(p.parent/path) if path else p
  assert dest.exists(),(p.name,target)
  if anchor:assert f'id="{anchor}"' in dest.read_text(),(p.name,target)
for dom in d['domains']:
 subset=[n for n in ns if n['domain']==dom['id']]
 for suffix in ['','-preview']:
  xml=ET.parse(ROOT/f'figures/{dom["slug"]}{suffix}.svg');elements=list(xml.getroot().iter())
  assert sum(e.tag.endswith('}circle') for e in elements)==len(subset)
  assert sum(e.tag.endswith('}path') for e in elements)==sum(len(n['parents']) for n in subset)
xml=ET.parse(ROOT/'figures/overview.svg');els=list(xml.getroot().iter());assert sum(e.tag.endswith('}circle') for e in els)==len(ns)
assert sum(e.tag.endswith('}path') for e in els)==sum(len(n['parents']) for n in ns)
patterns=[r'(?i)\b(?:patient|subject)\s+[0-9]{4,}\b',r'\bsk-[A-Za-z0-9_-]{16,}',r'-----BEGIN [A-Z ]*PRIVATE KEY-----',r'(?i)bearer\s+[a-z0-9._-]{20,}',r'(?i)(?:patientunitstayid|subject_id|hadm_id|patient_id)\s*[=:]\s*[\"\x27]?\d{4,}',r'(?i)(?:api[_ -]?key|auth[_ -]?token|password)\s*[=:]\s*[\"\x27][^\"\x27\n]{8,}',r'/(?:data_storage|Users)/',r'/?private/(?:data|runs|run|packages)/',r'\b(?:candidate|episode|job|attempt)-[a-f0-9]{12,}\b',r'\b[0-9a-f]{32,}\b']
compiled=[re.compile(p) for p in patterns]
for p in list((ROOT/'proposals').glob('*.md'))+[ROOT/'data/atlas.json']:
 s=p.read_text()
 for i,pattern in enumerate(compiled):assert not pattern.search(s),(p.name,'public policy check',i)
print(json.dumps({'nodes':len(ns),'generated':sum(not n['seed'] for n in ns),'edges':sum(len(n['parents']) for n in ns),'domains':dict(collections.Counter(n['domain'] for n in ns)),'lineage':'valid DAG','proposal_links':'complete','svg_coverage':'all nodes and edges','public_export_checks':'passed'},indent=2))

# Reviewer-facing surfaces must not carry explicit producer attribution.
producer=re.compile(r"(?i)\b(?:codex|qwen[\w.-]*|claude[\w.-]*|novita|openai|anthropic|deepseek[\w.-]*|polo|luna|discovery\s+rsi|gpt[- ]?(?:5|6)[\w.-]*)\b")
for p in list((ROOT/'proposals').glob('*.md'))+list((ROOT/'domains').glob('*.md'))+list((ROOT/'figures').glob('*.svg'))+[ROOT/'data/atlas.json',ROOT/'REVIEW.md',ROOT/'TRANSLATION.md']:
 s=p.read_text()
 assert not re.search('[\u3400-\u4dbf\u4e00-\u9fff]',s),(p.name,'untranslated Chinese')
 assert not producer.search(s),(p.name,'producer attribution')
 if p.parent.name=='proposals':
  assert s.startswith('> **Anonymous English review copy.**'),p.name
  assert not re.search(r'https://github\.com/[^\s)]+/blob/[0-9a-f]{7,40}/',s),(p.name,'individual provenance link')
  assert not re.search(r'^Date:\s*2026-',s,re.M),(p.name,'authoring date')
print('English-only review surfaces and explicit-attribution blinding: passed')
