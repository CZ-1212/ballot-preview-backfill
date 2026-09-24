import fitz, os

BASE = '/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_measure_pdfs/'
OUT = '/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/smc_page_images/'
os.makedirs(OUT, exist_ok=True)

# render ALL pages for the short docs (S, DD - 4 pages; Q - 6 pages)
jobs = [
    ('52-ENG-M303-Contest_Code-Reso-San_Bruno_Hosuing_Permit_and_Development_Redacted.pdf', None),
    ('52-ENG-M304-Contest_Code-Reso-San_Bruno_Fireworks_Ban_Redacted.pdf', None),
    ('52-ENG-M401-Contest_Code-Reso-Half_Moon_Bay_Housing_Initiative_Redacted.pdf', None),
]

for fname, pages in jobs:
    doc = fitz.open(BASE + fname)
    rng = range(len(doc)) if pages is None else pages
    for p in rng:
        page = doc[p]
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
        outname = OUT + fname.replace('.pdf','') + f'_p{p+1}.png'
        pix.save(outname)
        print(outname)
    doc.close()
