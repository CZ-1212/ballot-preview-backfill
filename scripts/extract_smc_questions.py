import re, glob, json, pdfplumber

QUOTE_CHARS = '"“”'

def normalize(t):
    t = re.sub(r'\s+', ' ', t)
    return t.strip()

def extract_questions(text):
    # Find quoted spans (curly or straight quotes) that end with a question mark
    text = text.replace('\n', ' ')
    results = []
    # pattern: opening quote, then content (non-greedy), then ? then closing quote
    pattern = re.compile(r'[“"]([^“”"]{60,2000}?\?)[”"]')
    for m in pattern.finditer(text):
        q = normalize(m.group(1))
        results.append(q)
    return results

files = sorted(glob.glob('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_measure_pdfs/*.pdf'))
out = {}
for f in files:
    with pdfplumber.open(f) as pdf:
        full_text = '\n'.join((p.extract_text() or '') for p in pdf.pages)
    qs = extract_questions(full_text)
    # dedup by first 50 chars
    seen = set()
    uniq = []
    for q in qs:
        key = q[:50]
        if key not in seen:
            seen.add(key)
            uniq.append(q)
    out[f.split('/')[-1]] = uniq

json.dump(out, open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_questions_raw.json', 'w'), indent=2)
for k, v in out.items():
    print('=====', k, '=====')
    for q in v:
        print(' -', q[:200])
    print()
