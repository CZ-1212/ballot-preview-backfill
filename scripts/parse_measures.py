import sys, json
from bs4 import BeautifulSoup

path = sys.argv[1]
with open(path, encoding='utf-8', errors='replace') as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')

groups = soup.find_all('div', class_='measureDescGroup')
results = []
for g in groups:
    h3 = g.find('h3', class_='measureDesc')
    p = g.find('p', class_='measureText')
    if not h3 or not p:
        continue
    title = h3.get_text(' ', strip=True)
    desc = p.get_text(' ', strip=True)
    parts = title.split(' - ', 2)
    if len(parts) >= 3:
        jurisdiction = parts[1].strip()
    else:
        jurisdiction = None
    results.append({'title': title, 'jurisdiction': jurisdiction, 'desc': desc})

print(json.dumps(results, indent=2))
