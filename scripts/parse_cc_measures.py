import re, json

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/cc_measures_fulltext.txt') as f:
    text = f.read()

# strip page footers "Page X of 3"
text = re.sub(r'Page \d+ of \d+', '', text)
# strip the doc header on page1
text = text.replace('Contra Costa County\nNovember 3, 2026 General Election\nLocal Ballot Measures – Updated 8/10/26\n', '')

# Split on measure letter blocks: a line that's just a letter/code (RTM, M, N, ... V) followed by "MEASURE"
pattern = re.compile(r'\n?([A-Z]{1,3})\nMEASURE\n(.*?)\n(Majority Overall Required to pass|Majority Required to pass|2/3 Required to pass|55% Required to pass)\n(.*?)(?=\n[A-Z]{1,3}\nMEASURE\n|\Z)', re.DOTALL)

CITY_NAMES = ['Clayton','Concord','Hercules','Richmond','San Pablo','Walnut Creek',
              'Antioch','Brentwood','El Cerrito','Martinez','Orinda','Pinole','Pittsburg','San Ramon']
TOWN_NAMES = ['Danville','Moraga']

def extract_jurisdiction(letter, caption):
    if letter == 'RTM':
        return None
    for c in CITY_NAMES:
        if caption.startswith(f'City of {c}'):
            return f'City of {c}'
    for t in TOWN_NAMES:
        if caption.startswith(f'Town of {t}'):
            return f'Town of {t}'
    # school districts / other: whole caption is the jurisdiction
    return caption.strip()

results = []
for m in pattern.finditer(text):
    letter, caption, threshold, desc = m.groups()
    caption = caption.strip()
    desc = desc.strip()
    jurisdiction = extract_jurisdiction(letter, caption)
    results.append({
        'letter': letter,
        'caption': caption,
        'threshold': threshold,
        'jurisdiction': jurisdiction,
        'description': desc,
    })

print(f"Parsed {len(results)} measures")
for r in results:
    print(f"Measure {r['letter']} | caption={r['caption']!r} | jurisdiction={r['jurisdiction']!r}")
    print('  desc:', r['description'][:100].replace(chr(10),' '), '...')

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/cc_measures_parsed.json', 'w') as f:
    json.dump(results, f, indent=2)
