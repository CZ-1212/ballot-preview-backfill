import re, json

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_roster_fulltext.txt', encoding='utf-8') as f:
    lines = [l.rstrip('\n') for l in f]

CONTEST_RE = re.compile(r'^(\d{3,5})\s+(.+?)\s+Vote for\s+(\d+)\s+On Ballot:\s*(Yes|No)\s*$')
QUAL_RE = re.compile(r'^Qualified:\s*(\d+)\s+(.+?)\s+Candidate Stmt Filed\?\s*(.*)$')
SKIP_PREFIXES = ('Res:', 'Mail:', 'Day:', 'Eve:', 'Email:', 'Website:', 'CFMR', 'Print Date',
                 'MARK CHURCH', 'CHIEF ELECTIONS', 'STATEWIDE', 'NOVEMBER', 'ROSTER',
                 'All Contests', 'Qualified Candidates Only', 'All Qualified Dates', 'Contest')

STATE_FEDERAL_EXACT = {
    'Governor', 'Lieutenant Governor', 'Secretary of State', 'Controller', 'Treasurer',
    'Attorney General', 'Insurance Commissioner', 'Member, State Board of Equalization, District 2',
    'U.S. Representative, District 15', 'U.S. Representative, District 16',
    'Member of the State Assembly, District 19', 'Member of the State Assembly, District 21',
    'Member of the State Assembly, District 23', 'Superintendent of Public Instruction',
}

races = []
cur = None
i = 0
n = len(lines)
while i < n:
    line = lines[i].strip()
    m = CONTEST_RE.match(line)
    if m:
        cid, rname, votefor, onballot = m.groups()
        cur = {'id': cid, 'race': rname, 'vote_for': votefor, 'on_ballot': onballot == 'Yes', 'candidates': []}
        races.append(cur)
        i += 1
        continue
    m2 = QUAL_RE.match(line)
    if m2 and cur is not None:
        num, name, stmt = m2.groups()
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

local_races = [r for r in races if r['race'] not in STATE_FEDERAL_EXACT]
print(f"Total races parsed: {len(races)}; local races: {len(local_races)}")
total_local_cands = sum(len(r['candidates']) for r in local_races)
print(f"Total local candidates: {total_local_cands}")

json.dump(local_races, open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_local_races.json', 'w'), indent=2)

for r in local_races:
    print(f"{r['id']} | {r['race']!r} | on_ballot={r['on_ballot']} | vote_for={r['vote_for']}")
    for c in r['candidates']:
        print(f"    - {c['name']!r} | {c['occupation']!r}")
