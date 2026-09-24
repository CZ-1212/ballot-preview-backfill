# -*- coding: utf-8 -*-
import re, json

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/scc_full_text.txt') as f:
    raw_lines = f.read().split('\n')

SKIP_EXACT = {
    'Contest', 'Contests: 3120 to 6103 -', 'Final Qualified List of Local Eligible Candidates',
    'General Election - 11/3/2026', 'Qualified Candidates Only', 'All Qualified Dates',
    'Candidates flagged with Authority to Release',
}

lines = []
for l in raw_lines:
    s = l.strip()
    if s in SKIP_EXACT:
        continue
    if s.startswith('=== PAGE'):
        continue
    if s.startswith('CFMR009'):
        continue
    if s.startswith('Print Date and Time'):
        continue
    if re.match(r'^Page \d+ of \d+$', s):
        continue
    lines.append(s)

# find contest boundaries: race line, "On Ballot: X", digits, "Vote For: N"
contests = []
i = 0
n = len(lines)
while i < n - 3:
    if lines[i+1].startswith('On Ballot:') and re.match(r'^\d+$', lines[i+2]) and lines[i+3].startswith('Vote For:'):
        race = lines[i]
        onballot = lines[i+1].split(':',1)[1].strip()
        cid = lines[i+2]
        votefor = re.search(r'\d+', lines[i+3]).group()
        contests.append({'race': race, 'onballot': onballot, 'cid': cid, 'votefor': votefor, 'start': i+4})
        i += 4
    else:
        i += 1

# set end index for each contest = start index of next contest's race line (i.e next contest's 'start'-4), or end of lines
for idx, c in enumerate(contests):
    if idx + 1 < len(contests):
        c['end'] = contests[idx+1]['start'] - 4
    else:
        c['end'] = n

# parse candidates within each contest block
for c in contests:
    block = lines[c['start']:c['end']]
    candidates = []
    j = 0
    m = len(block)
    while j < m - 3:
        if block[j+1] == 'Qualified' and re.match(r'^\d+$', block[j+2]) and block[j+3] == 'Candidate Stmt Filed?':
            name = block[j]
            stmt = block[j+4] if j+4 < m else ''
            occ_idx = j + 5
            occupation = ''
            if occ_idx < m and not block[occ_idx].startswith('Res:'):
                occupation = block[occ_idx]
            if occupation in ('(No Ballot Designation)', 'No Ballot Designation'):
                occupation = ''
            candidates.append({'name': name, 'occupation': occupation})
            j += 5
        else:
            j += 1
    c['candidates'] = candidates

print(f"Total contests: {len(contests)}")
no_cand = [c for c in contests if not c['candidates']]
print(f"Contests with zero parsed candidates: {len(no_cand)}")
for c in no_cand[:10]:
    print(' ', c['race'], c['onballot'])

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/scc_parsed.json', 'w') as f:
    json.dump(contests, f, indent=2)
