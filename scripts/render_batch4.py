import fitz, os

BASE = '/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_measure_pdfs/'
OUT = '/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_page_images/'
os.makedirs(OUT, exist_ok=True)

jobs = [
    ('52-ENG-M105-Contest_Code-Reso-Burlingame_ESD_Bon_Redacted.pdf', [3,4,5]),
    ('52-ENG-M109-Contest_Code-Reso-Cabrillo_USD_Parcel_Tax.pdf', [3,4,5]),
    ('52-ENG-M103-Contest_Code-Reso-Pacifica_SD_Parcel_Tax_Redacted.pdf', [3,4,5]),
    ('52-ENG-M306-Contest_Code-Reso-SMFCSD_Bond_Redacted.pdf', [3,4,5]),
    ('52-ENG-M307-Contest_Code-Reso-SMCCD_Bond_Redacted.pdf', [3,4,5,6]),
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
