import json, re, time, subprocess

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/cc_election66.json') as f:
    data = json.load(f)

offices = data['offices']
local_cats = ['City', 'Schools', 'Special District']
local_offices = []
for cat in local_cats:
    for header, items in offices.get(cat, {}).items():
        for it in items:
            name = re.sub(r'<[^>]+>', '', it['name']).strip()
            if 'Superintendent of Public Instruction' in name:
                continue
            if it['hasCand']:
                local_offices.append({'id': it['id'], 'name': name, 'category': cat})

print(f"Total local offices: {len(local_offices)}")

BASE = "https://www.contracostavote.gov/ce/mobile/seam/resource/rest/election/getOfficeCandidates"
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'

results = []
for off in local_offices:
    url = f"{BASE}?eoid={off['id']}&lang=en-US"
    out = subprocess.run(['curl', '-s', '-A', UA, url], capture_output=True, text=True, check=True)
    j = json.loads(out.stdout)
    cands = [c['candidateDisplayName'].strip() for c in j.get('candidates', [])]
    results.append({
        'id': off['id'],
        'office_name': off['name'],
        'category': off['category'],
        'votefor': j.get('votefor'),
        'candidates': cands,
    })
    time.sleep(0.05)

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/cc_local_offices_candidates.json', 'w') as f:
    json.dump(results, f, indent=2)

total_cands = sum(len(r['candidates']) for r in results)
print(f"Total candidate rows: {total_cands}")
