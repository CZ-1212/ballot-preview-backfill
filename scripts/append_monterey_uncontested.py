import json
import openpyxl

XLSX_PATH = "/Users/ciarazavala/Desktop/Ballot Preview Backfill/Measure_Candidate Backfill Info.xlsx"
COUNTY = "Monterey County"
CANDIDATES_URL = "https://www.countyofmonterey.gov/government/departments-a-h/elections/elections/candidate-list"

EXCLUDE_RACES = {"District 18", "District 19", "District 29", "District 30"}
STATEMENT_VALUES = {"Candidate Statement Filed (Scanned)", "No Candidate Statement Filed"}

BASE_FLAG = 'Uncontested - registrar shows this race as "Appointed In-Lieu of Election" (filed candidates do not exceed available seats, so the candidate(s) are seated without appearing on the ballot)'

CROSS_COUNTY_KEYWORDS = {
    'FRESNO COUNTY BOARD OF EDUCATION': 'Fresno County',
    'WEST HILLS COMMUNITY COLLEGE DISTRICT': 'primarily Fresno/Kings County (West Hills College, Coalinga)',
    'COALINGA - HURON JOINT UNIFIED SCHOOL DISTRICT': 'Fresno County',
}

data = json.load(open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/monterey_races.json'))

appointed = []
for r in data:
    if r['race'] in EXCLUDE_RACES:
        continue
    if r['ballotStatus'] != 'Appointed In-Lieu of Election':
        continue
    candidates = []
    for c in r['candidates']:
        name = c[0]
        rest = [x for x in c[1:] if x not in STATEMENT_VALUES and not x.startswith('Party Preference')]
        occupation = rest[0] if rest else ''
        candidates.append((name, occupation))
    appointed.append({'race': r['race'], 'voteFor': r['voteFor'], 'candidates': candidates})

print(f"Total appointed-in-lieu local races: {len(appointed)}")
total_cands = sum(len(r['candidates']) for r in appointed)
print(f"Total candidate rows (incl. zero-candidate races): {total_cands}")

wb = openpyxl.load_workbook(XLSX_PATH)
ws_c = wb['Candidates']

c_row = 2
while ws_c.cell(row=c_row, column=1).value:
    c_row += 1

n = 0
for r in appointed:
    race = r['race']
    flag = BASE_FLAG
    for keyword, note in CROSS_COUNTY_KEYWORDS.items():
        if race.startswith(keyword):
            flag = flag + f' ; Cross-county jurisdiction: {note} - verify before publishing under "Monterey County"'
            break
    if r['candidates']:
        for name, occ in r['candidates']:
            ws_c.cell(row=c_row, column=1, value=COUNTY)
            ws_c.cell(row=c_row, column=2, value=race)
            ws_c.cell(row=c_row, column=3, value=name)
            ws_c.cell(row=c_row, column=4, value=occ)
            ws_c.cell(row=c_row, column=5, value=flag)
            ws_c.cell(row=c_row, column=6, value=CANDIDATES_URL)
            c_row += 1
            n += 1
    else:
        ws_c.cell(row=c_row, column=1, value=COUNTY)
        ws_c.cell(row=c_row, column=2, value=race)
        ws_c.cell(row=c_row, column=3, value="")
        ws_c.cell(row=c_row, column=4, value="")
        ws_c.cell(row=c_row, column=5, value=flag)
        ws_c.cell(row=c_row, column=6, value=CANDIDATES_URL)
        c_row += 1
        n += 1

wb.save(XLSX_PATH)
print(f"Monterey uncontested rows appended: {n}")
