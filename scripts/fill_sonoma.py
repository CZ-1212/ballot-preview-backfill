# -*- coding: utf-8 -*-
import json, openpyxl

XLSX_PATH = "/Users/ciarazavala/Desktop/Ballot Preview Backfill/Measure_Candidate Backfill Info.xlsx"
CANDIDATES_SOURCE = "https://sonomacounty.gov/administrative-support-and-fiscal-services/registrar-of-voters/elections/november-3-2026-general-election-local-candidates-who-filed"
MEASURES_SOURCE = "https://sonomacounty.gov/administrative-support-and-fiscal-services/registrar-of-voters/elections/november-3-2026-general-election-props-and-measures-on-the-ballot"
COUNTY = "Sonoma County"

MEASURES = [
    ("Measure AB", "Sonoma County Junior College District",
     "Without increasing tax rates, to improve facilities to train students for careers in nursing/firefighting/first responders, building trades, agriculture, auto mechanics; attract/retain high quality faculty, prepare students for universities; repair leaky roofs; repair, construct, and acquire classrooms/sites/facilities/equipment, shall the Sonoma County Junior College District measure be adopted authorizing $830,000,000 in bonds at legal rates, levying $25 per $100,000 of assessed valuation ($55,300,000 annually), while bonds are outstanding, and with oversight/audits/local control?",
     "Cross-county jurisdiction (Sonoma, Marin, and Mendocino counties) - Sonoma County is the lead county for this measure; please verify"),
    ("Measure D", "Coast Life Support District",
     "Shall Measure D (the Coast Life Support District Emergency Medical Services Tax) be adopted? Allows Coast Life Support District to increase the current special parcel tax rate on real property to $101 per unit of benefit, for emergency medical services, including ambulance, life support and medical transport purposes and other necessary operating expenses, providing an estimated $1,972,934 annually, until the tax is amended or repealed; authorizes annual increases for inflation; and raises the District's appropriations limit to permit spending of the tax revenue.",
     "Cross-county jurisdiction (Mendocino and Sonoma counties) - Mendocino County is the lead county for this measure; please verify"),
    ("Measure E", "Waugh School District",
     "To improve the quality of education; replace heating, ventilation and air-conditioning systems; modernize outdated classrooms, restrooms and school facilities; and make health, safety and security improvements, shall Waugh School District's measure authorizing $16,000,000 in bonds, at legal interest rates, and levying approximately $30 per $100,000 of assessed valuation (raising $917,000 annually) while bonds are outstanding, be adopted, with a board appointed citizens' oversight committee and annual independent audits to assure proper expenditure of funds?",
     ""),
    ("Measure G", "West Sonoma County Union High School District",
     "To continue supporting academic excellence for West Sonoma County Union students without increasing current tax rates; protect music, art, dance, shop, culinary and other career technical programs; retain teachers and staff; and keep class sizes low, shall West Sonoma County Union High School District's measure be adopted, renewing its existing parcel tax for eight years at the same rate of $79 per parcel, raising approximately $1,950,000 annually with exemptions including seniors and all funds staying local?",
     ""),
    ("Measure H", "County of Sonoma",
     "Without raising taxes, to improve and protect Sonoma County's regional and neighborhood parks; safeguard water supplies, streams, rivers; reduce future wildfire risk; preserve fish and wildlife habitat; conserve natural areas for future generations; expand walking, hiking, and biking trails; shall Sonoma County continue a one-eighth-cent special transaction and use tax (sales tax) countywide until ended by voters, providing approximately $15.5 million annually, with community oversight, public disclosure, and annual audits?",
     ""),
    ("Measure I", "Town of Windsor",
     "To provide funding for the Town of Windsor to maintain essential local services, such as repairing potholes and maintaining streets; neighborhood police patrols / emergency response / traffic enforcement; preserving parks / community events; disaster preparedness and fire prevention — removing brush / flammable fuels, and for general government use; shall the measure establishing a 1% sales tax, providing approximately $5,700,000 annually until ended by voters, requiring independent audits, citizen oversight, and all funds remaining in Windsor under local control, be adopted?",
     ""),
    ("Measure J", "Windsor Unified School District",
     "Windsor Unified School District Classroom Repair/No Tax Increase Measure. To upgrade aging classrooms, labs, career training and school facilities for college/career readiness in math, science, technology, engineering, skilled trades; and fix deteriorating roofs, plumbing, HVAC, electrical, and safety systems, shall Windsor Unified School District's measure be adopted authorizing $96,000,000 in bonds at legal rates, without increasing projected tax rates, levying approximately $46 per $100,000 while bonds are outstanding ($6,000,000 annually), requiring independent oversight/audits and local control?",
     ""),
    ("Measure K", "City of Rohnert Park",
     "Rohnert Park Financial Viability, Community Health/Safety Measure. To maintain 911 response/fire protection/wildfire preparedness; protect local drinking water; keep parks clean/safe; prevent property crime/burglary/public safety officer reductions; repair streets/potholes; and other general city services; shall the measure, establishing a half-cent local sales tax, providing approximately $5,500,000 annually for locally controlled funding that cannot be taken by the state, until ended by voters, requiring audits/public spending disclosure, be adopted?",
     ""),
    ("Measure L", "City of Santa Rosa",
     "City of Santa Rosa Community Safety/Financial Stability Measure. Shall the measure maintaining Santa Rosa's quality of life, 911 emergency medical, police response to violent crimes; keeping all city fire stations open and public places safe/clean; fixing streets/repairing potholes; addressing homeless encampments; maintaining police, fire protection, other services, by reauthorizing the existing, voter approved sales tax at an updated 1¢ rate, providing approximately $46,000,000 annually until ended by voters; requiring audits, public disclosure, local control, be adopted?",
     ""),
    ("Measure M", "Harmony Union School District",
     "To maintain and enhance quality education programs by funding Harmony Union School District's Garden Enrichment Program at Harmony and Salmon Creek School, a comprehensive farm-to-table interactive education program, as well as student mental health and academic intervention services, shall Harmony Union School District's education parcel tax measure be adopted, at the rate of $75 per year (raising approximately $177,600 annually), for four years, with an exemption for those 65 years and older and all funds spent on local students?",
     ""),
    ("Measure N", "Schell-Vista Fire Protection District",
     "Shall the Schell Vista Fire Protection District adopt Ordinance No. 2026-01 retaining the District's increased limits on appropriations to assure continued fire, rescue and emergency medical services?",
     ""),
    ("Measure O", "Old Adobe Union School District",
     "To improve the quality of education; repair/replace leaky roofs; make health, safety and security improvements; replace outdated HVAC systems; make accessibility (ADA) improvements, modernize classrooms, restrooms and school facilities, including multi-purpose rooms; shall Old Adobe Union School District's measure be adopted authorizing $48,000,000 of bonds at legal rates, generating on average $2,800,000 annually while bonds are outstanding at approximate rates of $25 per $100,000 assessed value, with annual audits, oversight, no money for salaries, all money staying local?",
     ""),
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

races = json.load(open('/private/tmp/claude-501/-Users-ciarazavala-Desktop-Ballot-Preview-Backfill/28cd04c7-f986-44cf-90af-3f056f743036/scratchpad/sonoma_candidates_parsed.json'))

r = 2
while ws_c.cell(row=r, column=1).value:
    r += 1

cand_rows = 0
empty_races = 0
for race in races:
    name = race['race']
    seats = race['seats']
    cands = race['candidates']

    if not cands:
        ws_c.cell(row=r, column=1, value=COUNTY)
        ws_c.cell(row=r, column=2, value=name)
        ws_c.cell(row=r, column=3, value="")
        ws_c.cell(row=r, column=4, value="")
        ws_c.cell(row=r, column=5, value="")
        ws_c.cell(row=r, column=6, value=CANDIDATES_SOURCE)
        r += 1
        empty_races += 1
        continue

    uncontested = len(cands) <= seats
    flag = f"Uncontested - {len(cands)} candidate(s) for {seats} seat(s) per registrar" if uncontested else ""

    for c in cands:
        ws_c.cell(row=r, column=1, value=COUNTY)
        ws_c.cell(row=r, column=2, value=name)
        ws_c.cell(row=r, column=3, value=c['name'])
        ws_c.cell(row=r, column=4, value=c['occupation'])
        ws_c.cell(row=r, column=5, value=flag)
        ws_c.cell(row=r, column=6, value=CANDIDATES_SOURCE)
        r += 1
        cand_rows += 1

print(f"Wrote {cand_rows} candidate rows + {empty_races} empty-race rows across {len(races)} races")

wb.save(XLSX_PATH)
print("Saved.")
