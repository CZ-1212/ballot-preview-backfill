import json, re

offices = json.load(open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/cc_local_offices_candidates.json'))
occ_map = json.load(open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/cc_occ_map.json'))

def norm(s):
    return re.sub(r'\s+', ' ', s).strip().upper()

# Manual fuzzy-match overrides: the live Candidates widget (JSON API, used for
# Candidate Name / authoritative spelling) and the Candidate Detail List PDF
# (used for occupation) spell these 6 names slightly differently. Verified by
# office + near-identical name that these are the same person in both sources.
NAME_OVERRIDES = {
    'MATTY MATTHEWS ALAPPAT': 'MATTY MATHEWS ALAPPAT',
    'MATTHEW "MATTY" AVERY': 'MATTHEW "MATT" AVERY',
    'ELIZABETH PABON-ALVARADO': 'ELIZABETH PABON ALVARADO',
    'STACY SCHWEPPE': 'STACEY SCHWEPPE',
    'SAMANTHA WATSON-ALAVARADO': 'SAMANTHA WATSON-ALVARADO',
    'STEVEN LICHLITER': 'STEVE LICHLITER',
}

unmatched = []
rows = []
for off in offices:
    for cand in off['candidates']:
        key = norm(cand)
        occ = occ_map.get(key)
        flag = ''
        if occ is None and key in NAME_OVERRIDES:
            occ = occ_map.get(NAME_OVERRIDES[key])
            flag = f'Name spelled differently across registrar sources: Candidates page has "{cand}"; Candidate Detail List PDF has "{NAME_OVERRIDES[key].title()}" - verify correct spelling'
        if occ is None:
            unmatched.append((off['office_name'], cand))
        rows.append({
            'office_name': off['office_name'],
            'category': off['category'],
            'candidate': cand,
            'occupation': occ if occ is not None else '',
            'matched': occ is not None,
            'flag': flag,
        })

print(f"Total rows: {len(rows)}; unmatched: {len(unmatched)}")
for u in unmatched:
    print(' UNMATCHED:', u)

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/cc_final_candidates.json', 'w') as f:
    json.dump(rows, f, indent=2)
