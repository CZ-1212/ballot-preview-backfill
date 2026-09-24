import json
import openpyxl

XLSX_PATH = "/Users/ciarazavala/Desktop/Ballot Preview Backfill/Measure_Candidate Backfill Info.xlsx"
COUNTY = "Alameda County"
CANDIDATE_URL = 'https://alamedacountyca.gov/rov_app/candidatelist'

BASE_FLAG = "Uncontested - registrar shows this race as \"Not On Ballot\" (filed candidate(s) equal or exceed available seats, so no election is held; the candidate is seated/appointed without appearing on the ballot)"

CROSS_COUNTY = {
    "Byron - Bethany Irrigation District Directors": " ; Cross-county jurisdiction: filed with Contra Costa County per registrar's filing agency field - verify before publishing under \"Alameda County\"",
    "San Joaquin Delta Community College District Trustee, Area 4": " ; Cross-county jurisdiction: filed with San Joaquin County per registrar's filing agency field - verify before publishing under \"Alameda County\"",
}

data = json.load(open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/alameda_not_on_ballot.json'))

wb = openpyxl.load_workbook(XLSX_PATH)
ws_c = wb['Candidates']

c_row = 2
while ws_c.cell(row=c_row, column=1).value:
    c_row += 1

n = 0
for r in data:
    race = r['race_title']
    flag = BASE_FLAG + CROSS_COUNTY.get(race, "")
    if r['candidates']:
        for c in r['candidates']:
            occ = c['ballot_designation']
            row_flag = flag
            if c['status'] != 'Filing Completed':
                row_flag = flag + f" ; Candidate filing status: {c['status']}"
            ws_c.cell(row=c_row, column=1, value=COUNTY)
            ws_c.cell(row=c_row, column=2, value=race)
            ws_c.cell(row=c_row, column=3, value=c['name'])
            ws_c.cell(row=c_row, column=4, value=occ)
            ws_c.cell(row=c_row, column=5, value=row_flag)
            ws_c.cell(row=c_row, column=6, value=CANDIDATE_URL)
            c_row += 1
            n += 1
    else:
        ws_c.cell(row=c_row, column=1, value=COUNTY)
        ws_c.cell(row=c_row, column=2, value=race)
        ws_c.cell(row=c_row, column=3, value="")
        ws_c.cell(row=c_row, column=4, value="")
        ws_c.cell(row=c_row, column=5, value=flag)
        ws_c.cell(row=c_row, column=6, value=CANDIDATE_URL)
        c_row += 1
        n += 1

wb.save(XLSX_PATH)
print(f"Alameda uncontested rows appended: {n}")
