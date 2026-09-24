# -*- coding: utf-8 -*-
import json, openpyxl

XLSX_PATH = "/Users/ciarazavala/Desktop/Ballot Preview Backfill/Measure_Candidate Backfill Info.xlsx"
CANDIDATES_SOURCE = "https://votescount.santacruzcountyca.gov/Home/Elections/November3,2026CaliforniaGeneralElection/ContactCandidates.aspx"
MEASURES_SOURCE = "https://votescount.santacruzcountyca.gov/Home/Elections/November3,2026CaliforniaGeneralElection/LocalMeasures.aspx"
COUNTY = "Santa Cruz County"

MEASURES = [
    ("Measure D", "County of Santa Cruz",
     "Measure A, passed in 1986, requires voters to approve land use changes for onshore facilities that support offshore oil and gas development. To protect our economy, environment, and quality of life, shall voters enact an ordinance to update Measure A to also require voter approval for land use changes related to deep-sea mining facilities and strengthen the law against legal challenges?",
     ""),
    ("Measure E", "County of Santa Cruz",
     "TEMPORARY EMERGENCY MEDICAL, HEALTHCARE, FOOD, HOUSING, AND ESSENTIAL SERVICES PROTECTION MEASURE. To keep local hospitals/emergency rooms open, protect ambulance response, sustain access to urgent healthcare, including reproductive and mental health care, support local food/housing assistance and other essential services, and partially restore critical lost federal funding, shall the County of Santa Cruz be authorized to collect a supplemental half-cent (0.5%) general sales tax for 5 years, providing $27,000,000 annually in locally controlled funds?",
     ""),
    ("Measure G", "City of Scotts Valley",
     "Shall the City of Scotts Valley adopt an ordinance amending Section 3.24.030 of the Municipal Code raising the transient occupancy tax rate from 11% to 13%?",
     ""),
    ("Measure N", "Los Gatos-Saratoga Union High School District",
     "To maintain quality academic facilities at Los Gatos High School and Saratoga High School by replacing leaky roofs and failing restrooms, plumbing, electrical, heating/cooling systems; improving school safety; updating, repairing and equipping schools including science, technology, engineering, arts, math, robotics, and career/college readiness classrooms/labs; shall Los Gatos­Saratoga Union High School District's measure be adopted, authorizing $321,000,000 in bonds at legal rates, levying approximately $30 per $100,000 assessed value ($23,000,000 annually) while bonds are outstanding, with oversight, annual audits, and local control?",
     "Cross-county jurisdiction (Santa Clara and Santa Cruz counties) - same measure as recorded under Santa Clara County; please verify"),
]

wb = openpyxl.load_workbook(XLSX_PATH)
ws_m = wb['Measures']
ws_c = wb['Candidates']

r = 2
while ws_m.cell(row=r, column=1).value:
    r += 1
for name, jurisdiction, desc, flag in MEASURES:
    ws_m.cell(row=r, column=1, value=COUNTY)
    ws_m.cell(row=r, column=2, value=name)
    ws_m.cell(row=r, column=3, value=jurisdiction)
    ws_m.cell(row=r, column=4, value=desc)
    ws_m.cell(row=r, column=5, value=flag)
    ws_m.cell(row=r, column=6, value=MEASURES_SOURCE)
    r += 1
print(f"Wrote {len(MEASURES)} measure rows")

# also retroactively flag Santa Clara's existing Measure N row as cross-county with Santa Cruz
sc_flag_updated = 0
for row in ws_m.iter_rows(min_row=2):
    if row[0].value == "Santa Clara County" and row[1].value == "Measure N":
        existing = row[4].value or ""
        note = "Cross-county jurisdiction (Santa Clara and Santa Cruz counties) - same measure as recorded under Santa Cruz County; please verify"
        row[4].value = (existing + " ; " + note).strip(" ;") if existing else note
        sc_flag_updated += 1
print(f"Retroactively flagged {sc_flag_updated} Santa Clara Measure N row(s) as cross-county")

races = json.load(open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/sc_candidates_parsed.json'))

r = 2
while ws_c.cell(row=r, column=1).value:
    r += 1

cand_rows = 0
for race in races:
    name_full = race['race']
    seats = race['seats']
    cands = race['candidates']
    uncontested = len(cands) <= seats
    flag = ""
    if uncontested:
        flag = f"Uncontested - {len(cands)} candidate(s) for {seats} seat(s) per registrar; on-ballot status not explicitly stated on this page, please verify"

    for cand in cands:
        ws_c.cell(row=r, column=1, value=COUNTY)
        ws_c.cell(row=r, column=2, value=name_full)
        ws_c.cell(row=r, column=3, value=cand['name'])
        ws_c.cell(row=r, column=4, value=cand['occupation'])
        ws_c.cell(row=r, column=5, value=flag)
        ws_c.cell(row=r, column=6, value=CANDIDATES_SOURCE)
        r += 1
        cand_rows += 1

print(f"Wrote {cand_rows} candidate rows across {len(races)} races")

wb.save(XLSX_PATH)
print("Saved.")
