import re, json

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/sj_roster_fulltext.txt', encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f]

CONTEST_RE = re.compile(r'^(\d{3,5})\s+(.+?)\s+On Ballot:\s*(Yes|No)\s+Vote For:\s*(\d+)\s*$')
QUAL_RE = re.compile(r'^Qualified\s+(\d+)\s+(.+?)\s+Candidate Stmt Filed\?\s*(.*)$')
SKIP_PREFIXES = ('Res:', 'Alt:', 'Email:', 'Website:', 'CFMR', 'Print Date', 'Candidate List', 'November 3', 'Contests:', 'Qualified Candidates Only', 'All Qualified Dates', 'Contest')

races = []
cur = None
i = 0
n = len(lines)
while i < n:
    line = lines[i].strip()
    m = CONTEST_RE.match(line)
    if m:
        cid, rname, onballot, votefor = m.groups()
        cur = {'id': cid, 'race': rname, 'on_ballot': onballot == 'Yes', 'vote_for': votefor, 'candidates': []}
        races.append(cur)
        i += 1
        continue
    m2 = QUAL_RE.match(line)
    if m2 and cur is not None:
        num, name, stmt = m2.groups()
        # next non-skip line (if not starting with Res:) is occupation
        occ = ''
        j = i + 1
        if j < n:
            nxt = lines[j].strip()
            if not nxt.startswith(SKIP_PREFIXES) and not CONTEST_RE.match(nxt) and not QUAL_RE.match(nxt):
                occ = nxt
                j += 1
        cur['candidates'].append({'name': name.strip(), 'occupation': occ.strip()})
        i = j
        continue
    i += 1

print(f"Total contests parsed: {len(races)}")
json.dump(races, open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/sj_races_parsed.json', 'w'), indent=2)
for r in races:
    print(f"{r['id']} | {r['race']!r} | on_ballot={r['on_ballot']} | vote_for={r['vote_for']}")
    for c in r['candidates']:
        print(f"    - {c['name']!r} | {c['occupation']!r}")
