import sys, json, re
from bs4 import BeautifulSoup

path = '/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/candlist.html'
with open(path, encoding='utf-8', errors='replace') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')
headers = soup.find_all('h2', class_='candidate-list-table-header-div')

STATE_FEDERAL_EXACT = {
    'Governor', 'Lieutenant Governor', 'Secretary Of State', 'Controller',
    'Treasurer', 'Attorney General', 'Insurance Commissioner',
    'Member, State Board Of Equalization, 2nd District',
    "10th Congressional District", "12th Congressional District",
    "14th Congressional District", "17th Congressional District",
    "10th State Senate District",
    "14th Assembly District", "16th Assembly District", "18th Assembly District",
    "20th Assembly District", "24th Assembly District",
    "State Superintendent Of Public Instruction",
}

results = []
for h in headers:
    span = h.find('span', class_='candidate-list-table-header')
    if not span:
        continue
    status_span = span.find('span')
    status_text = status_span.get_text(strip=True) if status_span else ''
    full_text = span.get_text(' ', strip=True)
    race_title = full_text.replace(status_text, '').strip(' -').strip() if status_text else full_text.strip()

    table = h.find_next('table', class_='candidate-list-table')
    rows = table.find_all('tr') if table else []
    candidates = []
    for tr in rows:
        tds = tr.find_all('td')
        if len(tds) < 5:
            continue
        cand_span = tds[0].find('span', class_='candidateName')
        cand_name = cand_span.get_text(strip=True) if cand_span else ''
        cand_name = re.sub(r'\s+', ' ', cand_name).strip()
        ballot_desig = re.sub(r'\s+', ' ', tds[1].get_text(' ', strip=True)).strip()
        status = tds[3].get_text(strip=True)
        if cand_name:
            candidates.append({'name': cand_name, 'ballot_designation': ballot_desig, 'status': status})

    results.append({'race_title': race_title, 'status_text': status_text, 'candidates': candidates})

not_on_ballot_local = [r for r in results if r['status_text'] == 'Not On Ballot' and r['race_title'] not in STATE_FEDERAL_EXACT]

print(f"TOTAL not-on-ballot local races: {len(not_on_ballot_local)}")
for r in not_on_ballot_local:
    print(f"RACE: {r['race_title']!r} | n_cand={len(r['candidates'])}")
    for c in r['candidates']:
        print(f"    - {c['name']!r} | {c['ballot_designation']!r} | {c['status']}")

json.dump(not_on_ballot_local, open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/alameda_not_on_ballot.json', 'w'), indent=2)
