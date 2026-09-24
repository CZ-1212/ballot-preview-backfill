# -*- coding: utf-8 -*-
import re, json

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/sonoma_candidates_lines.txt') as f:
    lines = [l.rstrip('\n') for l in f.readlines()]

# content region
start = lines.index('School Offices', 100)
end = lines.index('▲ TOP ▲', 2000)  # last TOP marker before footer
content = lines[start:end]

ELECT_RE = re.compile(r'^\(Elect (\d+)\)$')
EMPTY_MARKERS = ('have filed and qualified for this office yet',)

SECTION_HEADERS = {
    'School Offices', 'County Boards of Education', 'Community College Governing Boards',
    'Unified School District Governing Boards', 'High School District Governing Boards',
    'Elementary School District Governing Boards', 'Municipal Offices',
    'Special District Offices', 'Community Services District Boards of Directors',
    'Fire Protection District Boards of Directors', 'Health Care District Boards of Directors',
    'Life Support District Boards of Directors', 'Recreation and Park District Boards of Directors',
    'Water District Boards of Directors',
}
CITY_HEADERS = {
    'City of Cloverdale', 'City of Cotati', 'City of Healdsburg', 'City of Petaluma',
    'City of Rohnert Park', 'City of Santa Rosa', 'City of Sebastopol', 'City of Sonoma',
    'Town of Windsor',
}
TOP_MARKER = '▲ TOP ▲'

races = []
i = 0
n = len(content)
current_section = None
while i < n:
    l = content[i]
    if l == TOP_MARKER:
        i += 1
        continue
    if l in SECTION_HEADERS:
        current_section = l
        i += 1
        continue
    if l in CITY_HEADERS:
        i += 1
        continue
    # check if this is a race header: next line matches (Elect N)
    if i + 1 < n and ELECT_RE.match(content[i+1]):
        race_name = l
        seats = int(ELECT_RE.match(content[i+1]).group(1))
        i += 2
        # skip notice lines (e.g. nomination deadline extended) until we hit
        # either 'Candidate Name' header or an empty-race disclaimer
        candidates = []
        is_empty = False
        while i < n:
            if 'Candidate Name' == content[i]:
                i += 1
                # skip fixed header lines
                for _ in range(4):
                    if i < n:
                        i += 1
                break
            elif any(m in content[i] for m in EMPTY_MARKERS):
                is_empty = True
                i += 1
                break
            elif ELECT_RE.match(content[i]) or content[i] in SECTION_HEADERS or content[i] in CITY_HEADERS or content[i] == TOP_MARKER:
                # malformed - bail without consuming
                break
            else:
                # a notice line (e.g. ***Nomination deadline extended...***)
                i += 1
        if not is_empty:
            # parse candidate groups of 5 until next race header pattern
            while i < n:
                # stop if next race header detected (current line + (Elect N) next)
                if i + 1 < n and ELECT_RE.match(content[i+1]):
                    break
                if content[i] in SECTION_HEADERS or content[i] in CITY_HEADERS or content[i] == TOP_MARKER:
                    break
                if i + 4 < n:
                    name = content[i]
                    designation = content[i+1]
                    date_q = content[i+2]
                    statement = content[i+3]
                    incumbent = content[i+4]
                    candidates.append({'name': name, 'occupation': designation,
                                        'statement': statement, 'incumbent': incumbent})
                    i += 5
                else:
                    i += 1
        races.append({'section': current_section, 'race': race_name, 'seats': seats, 'candidates': candidates})
    else:
        i += 1

print(f"Total races parsed: {len(races)}")
total_cand = sum(len(r['candidates']) for r in races)
empty = [r for r in races if not r['candidates']]
print(f"Total candidates: {total_cand}, empty races: {len(empty)}")
for r in races:
    print(f"- [{r['section']}] {r['race']} (seats={r['seats']}, cand={len(r['candidates'])})")
    for c in r['candidates']:
        print(f"    {c['name']!r} | {c['occupation']!r} | stmt={c['statement']} inc={c['incumbent']}")

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/sonoma_candidates_parsed.json', 'w') as f:
    json.dump(races, f, indent=2)
