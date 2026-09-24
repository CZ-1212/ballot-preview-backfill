import json

data = json.load(open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/monterey_races.json'))

EXCLUDE_RACES = {"District 18", "District 19", "District 29", "District 30"}
STATEMENT_VALUES = {"Candidate Statement Filed (Scanned)", "No Candidate Statement Filed"}

local_on_ballot = []
for r in data:
    if r['race'] in EXCLUDE_RACES:
        continue
    if r['ballotStatus'] != 'On Ballot':
        continue
    candidates = []
    for c in r['candidates']:
        name = c[0]
        rest = [x for x in c[1:] if x not in STATEMENT_VALUES and not x.startswith('Party Preference')]
        occupation = rest[0] if rest else ''
        candidates.append((name, occupation))
    local_on_ballot.append({'race': r['race'], 'voteFor': r['voteFor'], 'candidates': candidates})

print(f"Total local on-ballot races: {len(local_on_ballot)}")
total_cands = sum(len(r['candidates']) for r in local_on_ballot)
print(f"Total candidate rows: {total_cands}")
print()
for r in local_on_ballot:
    print(f"RACE: {r['race']!r} ({r['voteFor']})")
    for n, o in r['candidates']:
        print(f"    - {n!r} | {o!r}")

json.dump(local_on_ballot, open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/monterey_local_onballot.json', 'w'), indent=2)
