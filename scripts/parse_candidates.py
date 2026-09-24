import sys
from bs4 import BeautifulSoup

path = sys.argv[1]
with open(path, encoding='utf-8', errors='replace') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

# Each race block: <h2 class="candidate-list-table-header-div"> ... </h2> followed by a table
headers = soup.find_all('h2', class_='candidate-list-table-header-div')

results = []

for h in headers:
    span = h.find('span', class_='candidate-list-table-header')
    if not span:
        continue
    # race title text, strip trailing "On Ballot"/status span
    status_span = span.find('span')
    status_text = status_span.get_text(strip=True) if status_span else ''
    full_text = span.get_text(' ', strip=True)
    race_title = full_text
    if status_text:
        race_title = full_text.replace(status_text, '').strip(' -')

    # find the following table
    table = h.find_next('table', class_='candidate-list-table')
    rows = table.find_all('tr') if table else []
    candidates = []
    for tr in rows:
        tds = tr.find_all('td')
        if len(tds) < 5:
            continue
        cand_span = tds[0].find('span', class_='candidateName')
        cand_name = cand_span.get_text(strip=True) if cand_span else ''
        ballot_desig = tds[1].get_text(' ', strip=True)
        status = tds[3].get_text(strip=True)
        filing_agency = ''
        for div in tds[4].find_all('div'):
            heading = div.find('div', class_='candidate-detail-heading')
            data = div.find('div', class_='candidate-detail-data')
            if heading and data and 'Filing Agency' in heading.get_text():
                filing_agency = data.get_text(strip=True)
        if cand_name:
            candidates.append({
                'name': cand_name,
                'ballot_designation': ballot_desig,
                'status': status,
                'filing_agency': filing_agency,
            })

    results.append({
        'race_title': race_title,
        'status_text': status_text,
        'candidates': candidates,
    })

print(f"Total races found: {len(results)}")
print("---")
for r in results:
    agencies = set(c['filing_agency'] for c in r['candidates'])
    print(f"RACE: {r['race_title']!r} | status={r['status_text']} | agencies={agencies} | n_candidates={len(r['candidates'])}")
    for c in r['candidates']:
        print(f"    - {c['name']!r} | {c['ballot_designation']!r} | {c['status']} | {c['filing_agency']}")
