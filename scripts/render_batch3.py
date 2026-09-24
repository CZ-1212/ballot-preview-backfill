import fitz, os

BASE = '/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_measure_pdfs/'
OUT = '/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_page_images/'
os.makedirs(OUT, exist_ok=True)

jobs = [
    ('52-ENG-M107-Contest_Code-Reso-Burlingame_Occupancy_Tax_Redacted_0.pdf', [1,2,3]),
    ('52-ENG-M209-Contest_Code-Reso-San_Mateo_Charter_Amendment_Redacted.pdf', [1,2,3]),
    ('52-ENG-M301-Contest_Code-Reso-San_Mateo_Transactions_and_Use_Tax_Redacted.pdf', [1,2,3]),
    ('52-ENG-M205-Contest_Code-Reso-Portola_Valley_Transfer_Tax_Redacted.pdf', [1,2,3]),
]

for fname, pages in jobs:
    doc = fitz.open(BASE + fname)
    for p in pages:
        page = doc[p]
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
        outname = OUT + fname.replace('.pdf','') + f'_p{p+1}.png'
        pix.save(outname)
        print(outname)
    doc.close()
