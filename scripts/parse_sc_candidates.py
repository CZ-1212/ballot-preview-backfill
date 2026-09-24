# -*- coding: utf-8 -*-
import re, json

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/sc_candidates_lines.txt') as f:
    raw = f.readlines()

# strip the "N " index prefix that our earlier dump added
lines = []
for l in raw:
    l = l.rstrip('\n')
    parts = l.split(' ', 1)
    lines.append(parts[1] if len(parts) > 1 else '')

# local section starts right after "Cities - refer to the city's website for more details"
start_idx = None
for i, l in enumerate(lines):
    if l.strip() == "Cities - refer to the city's website for more details":
        start_idx = i + 1
        break
end_idx = None
for i, l in enumerate(lines):
    if l.strip() == 'LOCATION':
        end_idx = i
        break

local_lines = [l.strip() for l in lines[start_idx:end_idx] if l.strip()]

SECTION_HEADERS = {'Boards of Education & Community Colleges', 'School Districts', 'Fire Districts', 'Water Districts'}
HEADER_COLS = {'Candidate Name', 'Party Preference', 'Ballot Designation', 'Mailing Address', 'Phone', 'Email', 'Website'}

PHONE_RE = re.compile(r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')
DOMAIN_RE = re.compile(r'^[A-Za-z0-9][A-Za-z0-9\-]*\.[A-Za-z]{2,4}$')
CA_ZIP_RE = re.compile(r'\bCA\.?\s+\d{5}\b')

def is_contact_line(line):
    if '@' in line:
        return True
    if PHONE_RE.match(line):
        return True
    if CA_ZIP_RE.search(line):
        return True
    if line.startswith('PO Box') or line.startswith('Box ') or line.startswith('Mailbox'):
        return True
    if re.match(r'^\d', line):  # street address starting with a number
        return True
    if DOMAIN_RE.match(line):
        return True
    return False

# split into race blocks: a race header is any line that is not a section header,
# not a column header, not "Incumbent: ...", and is followed eventually by "Candidate Name"
races = []
i = 0
n = len(local_lines)
current_section = None
while i < n:
    l = local_lines[i]
    if l in SECTION_HEADERS:
        current_section = l
        i += 1
        continue
    # race header: next non-incumbent lines lead to 'Candidate Name'
    race_name = l
    i += 1
    while i < n and local_lines[i].startswith('Incumbent:'):
        i += 1
    # expect column headers now
    if i < n and local_lines[i] == 'Candidate Name':
        while i < n and local_lines[i] in HEADER_COLS:
            i += 1
        # now parse candidates until next race header (i.e., until we hit a line that
        # doesn't look like a contact line AND isn't consumed as name/designation in pairs)
        block_start = i
        # find block end: scan forward for the next section header or next race pattern.
        # We detect race end by look-ahead: a race ends where the NEXT "Candidate Name" or
        # section header or end-of-data begins. Find next occurrence of 'Candidate Name' or section header.
        j = i
        while j < n and local_lines[j] != 'Candidate Name' and local_lines[j] not in SECTION_HEADERS:
            j += 1
        if j < n and local_lines[j] == 'Candidate Name':
            # walk back from j: the race header for the next block, and any Incumbent lines,
            # precede 'Candidate Name'. Walk back over Incumbent lines and the header line itself.
            k = j - 1
            while k > i and local_lines[k].startswith('Incumbent:'):
                k -= 1
            block_end = k  # k now points at the next race's name line (exclusive)
        else:
            block_end = j

        block = local_lines[block_start:block_end]
        candidates = []
        bi = 0
        bn = len(block)
        while bi < bn:
            name = block[bi]; bi += 1
            if bi >= bn:
                break
            designation = block[bi]; bi += 1
            candidates.append({'name': name, 'occupation': designation})
            while bi < bn and is_contact_line(block[bi]):
                bi += 1
        races.append({'section': current_section, 'race': race_name, 'candidates': candidates})
        i = block_end
    else:
        # not a real race header (shouldn't happen) - skip
        i += 1

for r in races:
    seats_m = re.search(r'-\s*(\d+)\s*Seats?', r['race'])
    r['seats'] = int(seats_m.group(1)) if seats_m else 1

print(f"Total races parsed: {len(races)}")
for r in races:
    print(f"- [{r['section']}] {r['race']} (seats={r['seats']}, candidates={len(r['candidates'])})")
    for c in r['candidates']:
        print(f"    {c['name']!r} | {c['occupation']!r}")

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/sc_candidates_parsed.json', 'w') as f:
    json.dump(races, f, indent=2)
