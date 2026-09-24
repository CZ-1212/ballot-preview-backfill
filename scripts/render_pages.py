import fitz, sys, os

BASE = '/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_measure_pdfs/'
OUT = '/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_page_images/'
os.makedirs(OUT, exist_ok=True)

jobs = [
    ('52-ENG-M101-Contest_Code-Reso-San_Carlos_SD_Parcel_Tax_Redacted.pdf', [4]),
    ('52-ENG-M106-Contest_Code-Reso-JUHSD_Parcel_Tax_Redacted.pdf', [4]),
    ('52-ENG-M207-Contest_-Code-Reso-EPA_Term_Limits_Redacted.pdf', [1]),
    ('52-ENG-M207-Contest_Code-Reso-City_of_East_Palo_Alto_Bond_Redacted.pdf', [1]),
    ('52-ENG-M104-Contest_Code-Reso-City_of_San_Carlos_Use_Tax_Redacted.pdf', [2]),
    ('52-ENG-M102-Contest_Code-Reso-Menlo_Park_Muni_Amendment_Redacted.pdf', [1]),
    ('52-ENG-M108-Contest_Code-Reso-RWC_Housing_Redacted.pdf', [1]),
    ('52-ENG-M302-Contest_Code-Reso-City_of_Brisbane_Business_License_Tax_Redacted_1.pdf', [1]),
    ('San_Mateo_County_Amendments.pdf', [2,3,4,5]),
]

for fname, pages in jobs:
    doc = fitz.open(BASE + fname)
    for p in pages:
        page = doc[p]
        pix = page.get_pixmap(matrix=fitz.Matrix(2.2, 2.2))
        outname = OUT + fname.replace('.pdf','') + f'_p{p+1}.png'
        pix.save(outname)
        print(outname)
    doc.close()
