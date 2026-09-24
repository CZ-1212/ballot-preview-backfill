import glob, json
import fitz

files = sorted(glob.glob('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_measure_pdfs/*.pdf'))
result = {}
for f in files:
    doc = fitz.open(f)
    pages_found = []
    for i in range(len(doc)):
        t = doc[i].get_text()
        tl = t.lower()
        if 'shall' in tl and '?' in t:
            pages_found.append(i)
    result[f.split('/')[-1]] = {'num_pages': len(doc), 'candidate_pages': pages_found}
    doc.close()

json.dump(result, open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_page_locations2.json', 'w'), indent=2)
for k, v in result.items():
    print(k, v)
