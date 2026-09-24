import re, json

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/cc_candidate_detail_fulltext.txt') as f:
    lines = [l.rstrip('\n') for l in f]

QUALDATE_RE = re.compile(r'^Qualified Date:')
CAND_PREFIX_RE = re.compile(r'^Candidate\(s\):\s*(.+)$')

occ_map = {}  # normalized name -> occupation (first occurrence kept)
n = len(lines)
for i, line in enumerate(lines):
    m = CAND_PREFIX_RE.match(line)
    if m:
        name = m.group(1).strip()
    elif line.strip() and line.strip() == line.strip().upper() and re.search(r'[A-Z]', line) and not line.strip().isdigit():
        # candidate a bare all-caps line; only treat as name if followed (within 2 lines) by Qualified Date
        name = line.strip()
    else:
        continue

    occupation = None
    if i + 1 < n and QUALDATE_RE.match(lines[i+1].strip()):
        occupation = ''
    elif i + 2 < n and QUALDATE_RE.match(lines[i+2].strip()):
        occupation = lines[i+1].strip()
    else:
        continue  # not a candidate-name line after all

    norm = re.sub(r'\s+', ' ', name).strip().upper()
    if norm not in occ_map:
        occ_map[norm] = occupation

print(f"Extracted {len(occ_map)} name->occupation entries")

with open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/cc_occ_map.json', 'w') as f:
    json.dump(occ_map, f, indent=2)

# quick sample
for k in list(occ_map.keys())[:15]:
    print(repr(k), '->', repr(occ_map[k]))
