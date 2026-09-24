# -*- coding: utf-8 -*-
import openpyxl

XLSX_PATH = "/Users/ciarazavala/Desktop/Ballot Preview Backfill/Measure_Candidate Backfill Info.xlsx"
MEASURES_PAGE = "https://smcacre.gov/elections/november-3-2026-statewide-general-election"

# letter -> (jurisdiction, description, source_pdf_url)
CONFIRMED = {
    "R": ("Burlingame School District",
          "To repair aging Burlingame schools and maintain academic excellence by fixing leaky roofs; removing dry rot, lead/asbestos; replacing aging plumbing/electrical systems; updating science, technology/engineering labs; and providing teachers with instructional tools to support student success, shall Burlingame Elementary School District's measure authorizing $100,000,000 in bonds at legal interest rates be adopted, at $16.00 per $100,000 of assessed value (approximately $6,567,830 annually) while bonds are outstanding, with oversight, audits, no funds for administrators, and local control?",
          "https://smcacre.gov/system/files/2026-07/52-ENG-M105-Contest%20Code-Reso-Burlingame%20ESD%20Bon_Redacted.pdf"),
    "Z": ("Cabrillo Unified School District",
          "With funds that cannot be taken by the State or Federal Government and spent elsewhere, shall Cabrillo Unified School District's measure to support local students by hiring and retaining highly qualified teachers and specialized educators; and expanding career training and college readiness programs, including agriculture, construction, and welding be adopted, replacing the current parcel tax at $239 per parcel for five years, (raising $2,600,000 annually) with senior exemptions, no administrator salaries or pensions, and public disclosure of spending?",
          "https://smcacre.gov/system/files/2026-07/52-ENG-M109-Contest%20Code-Reso-Cabrillo%20USD%20Parcel%20Tax.pdf"),
    "T": ("Pacifica School District",
          "To renew expiring local funding without increasing taxes, with local funding for elementary/middle schools the state cannot take away, to support strong math, science, history, reading/writing programs; attract/retain qualified teachers/counselors; maintain art/music/outdoor education programs, libraries and computer instruction, shall Pacifica School District's measure be adopted, levying $118 per parcel, raising $1,300,000 annually for 10 years, with senior exemptions, independent oversight and no money for administrator salaries?",
          "https://smcacre.gov/system/files/2026-06/52-ENG-M103-Contest%20Code-Reso-Pacifica%20SD%20Parcel%20Tax_Redacted.pdf"),
    "D": ("City of Burlingame",
          "To support city services such as: maintaining city streets/sidewalks and repairing potholes; maintaining parks and trees; enhancing emergency response, preparedness, and wildfire prevention; and for general government use; shall the City of Burlingame measure be adopted raising the transient occupancy (hotel) tax from 12% to 15%, paid only by hotel and lodging guests, until ended by voters, providing an estimated $5,700,000 annually, all funds locally controlled, with independent citizen oversight?",
          "https://smcacre.gov/system/files/2026-07/52-ENG-M107-Contest%20Code-Reso-Burlingame%20Occupancy%20Tax_Redacted_0.pdf"),
    "N": ("Town of Portola Valley",
          "Town of Portola Valley Autonomy Measure. Shall the measure maintaining Portola Valley’s independent status be adopted, providing: wildfire prevention/vegetation management; 911 emergency response/police patrols; local zoning/planning services; storm drain repair; and general government services; by adopting a charter for the Town of Portola Valley solely for, and establishing a real property transfer tax of $10 per $1,000, paid by buyers or sellers of property, until ended by voters, providing approximately $2,000,000 in locally controlled funding annually, with independent oversight?",
          "https://smcacre.gov/system/files/2026-07/52-ENG-M205-Contest%20Code-Reso-Portola%20Valley%20Transfer%20Tax_Redacted.pdf"),
    "F": ("City of San Mateo",
          "Shall the measure amending the City of San Mateo’s Charter to reflect the City’s current district-based election system, update the process for scheduling Council meetings and filling Council vacancies, update or remove obsolete provisions, and make other technical and conforming changes, be adopted?",
          "https://smcacre.gov/system/files/2026-07/52-ENG-M209-Contest%20Code-Reso-San%20Mateo%20Charter%20Amendment_Redacted.pdf"),
    "H": ("City of San Mateo",
          "To provide funding for San Mateo city services, such as keeping local streets, sidewalks, parks, infrastructure, and community facilities safe, clean, and well-maintained, fixing potholes, providing fire protection, paramedic, crime prevention, and 9-1-1 emergency response, and improvements to traffic safety/traffic management, shall the City of San Mateo’s ordinance establishing a one-quarter cent sales tax be adopted, providing 7 million dollars annually for general government use until ended by voters, with independent audits and all funds locally-controlled?",
          "https://smcacre.gov/system/files/2026-07/52-ENG-M301-Contest%20Code-Reso-San%20Mateo%20Transactions%20and%20Use%20Tax_Redacted.pdf"),
    "S": ("City of San Bruno",
          "Shall City of San Bruno Ordinance No. 1284, the 1977 zoning initiative that requires voter approval before the City Council can approve buildings exceeding specified height limits, residential density increases beyond 1974 zoning, multi-story parking structures, and certain roadway changes, be repealed given that State housing laws supersede local height limits and the ordinance interacts with current City economic development goals?",
          "https://smcacre.gov/system/files/2026-07/52-ENG-M303-Contest%20Code-Reso-San%20Bruno%20Hosuing%20Permit%20and%20Development_Redacted.pdf"),
    "DD": ("City of San Bruno",
           "Shall the City of San Bruno Safe and Sane Fireworks Ordinance be repealed to prohibit the sale, use, and discharge of safe and sane fireworks in the City of San Bruno?",
           "https://smcacre.gov/system/files/2026-07/52-ENG-M304-Contest%20Code-Reso-San%20Bruno%20Fireworks%20Ban_Redacted.pdf"),
    "EE": ("City of San Bruno",
           "San Bruno Essential Services Protection Measure. To protect essential services such as: fixing potholes/city streets; providing rapid response to 9-1-1 emergency calls; maintaining library programs for children, teens, adults/seniors; maintaining parks/open space; and general city services, shall the measure be adopted simplifying/modernizing San Bruno’s business license ordinance, making rates more equitable/equal, updating the tax rate schedule as described in the ordinance, until ended by voters, raising $4,000,000 annually, with annual independent audits?",
           "https://smcacre.gov/system/files/2026-08/52-ENG-M305-Contest%20Code-Reso-San%20Bruno%20Business%20License%20Tax_Redacted.pdf"),
    "W": ("San Mateo-Foster City School District",
          "To improve elementary and middle school classrooms for skilled trades, science, technology, engineering, and math; replace leaky roofs, old windows, fire alarms and emergency communications systems; provide affordable housing to attract/retain quality teachers/staff; acquire, construct, repair facilities, equipment, sites; shall San Mateo-Foster City School District’s measure be adopted, authorizing $498,000,000 in bonds at legal interest rates, levying $29 per $100,000 assessed value, averaging $35,000,000 annually while bonds are outstanding, with audits, independent oversight, and funds used locally?",
          "https://smcacre.gov/system/files/2026-08/52-ENG-M306-Contest%20Code-Reso-SMFCSD%20Bond_Redacted.pdf"),
    "V": ("San Mateo County Community College District",
          "Without increasing current tax rates and to protect affordable higher education at College of San Mateo, Cañada College, and Skyline College by repairing/constructing science, engineering, math, technology, skilled trades, and career-training classrooms that prepare students for in-demand careers; and repairing roofs, plumbing, electrical, shall San Mateo County Community College District’s measure authorizing $848,000,000 in bonds at legal rates be adopted, levying approximately $18 per $100,000 assessed value ($75,000,000 annually) while bonds are outstanding, with independent audits, oversight, and all money locally controlled?",
          "https://smcacre.gov/system/files/2026-08/52-ENG-M307-Contest%20Code-Reso-SMCCD%20Bond_Redacted.pdf"),
    "Y": ("City of Belmont",
          "City of Belmont Community Center Tax Measure. Shall the ordinance providing funding for and maintaining supervised children's play, youth, teen and adult programs, childcare, afterschool and senior programs in a disabled accessible, fire and earthquake resistant community center, usable as an emergency health and disaster relief facility, levying 33¢ per square foot of residential improvements and 54¢ per square foot of nonresidential improvements, providing $7,100,000 annually until ended by voters, with senior exemptions and independent audits, increasing the appropriation limit, be adopted?",
          "https://smcacre.gov/system/files/2026-08/52-ENG-M308-Contest%20Code-Reso-Belmont%20Special%20Tax_Redacted.pdf"),
    "I": ("City of Half Moon Bay",
          "Shall the Measure, amending the City of Half Moon Bay Local Coastal Land Use Plan, Title 17 (Subdivisions) and Title 18 (Zoning) of the Half Moon Bay Municipal Code, and other conforming edits so that the Measure D “Downtown Area” is redefined as the area designated as the “Town Center” (Figure 2-2) of the Local Coastal Land Use Plan, be adopted?",
          "https://smcacre.gov/system/files/2026-08/52-ENG-M309-Contest%20Code-Reso-Half%20Moon%20Bay%20Coastal%20Land_Redacted_0.pdf"),
    "Q": ("City of Half Moon Bay",
          "Shall Ordinance No. 2026-01, approving agreements with Mercy Housing California 110, L.P. (including a Ground Lease of Real Property for 99 years at a rate of $1/year, which is customary, and Affordable Housing and Property Disposition Agreement) providing for the development/operation of a Senior Affordable 40-Unit Residential Project for Agricultural Workers, which includes 2,653-square foot Community Space, at 535-555 Kelly Avenue in the City of Half Moon Bay, and authorizing other related actions, be adopted?",
          "https://smcacre.gov/system/files/2026-08/52-ENG-M401-Contest%20Code-Reso-Half%20Moon%20Bay%20Housing%20Initiative_Redacted.pdf"),
    "BB": ("City of Pacifica",
           "Pacifica City Services Measure. To protect Pacifica’s long-term financial stability; fund police, fire, 911 emergency response; prioritize paving streets in the worst conditions; keep parks, beaches and public spaces safe and maintained; and for general government use, shall the City of Pacifica’s measure establishing a 1% (1¢) transactions and use (sales) tax, generating approximately $5,000,000 annually until ended by voters, with public disclosure and local control of funds, and independent annual audits, be adopted?",
           "https://smcacre.gov/system/files/2026-08/52-ENG-M402-Contest%20Code-Reso-Pacifica%20Transactions%20and%20Use%20Tax_Redacted.pdf"),
}

wb = openpyxl.load_workbook(XLSX_PATH)
ws_m = wb['Measures']

updated = 0
for row in ws_m.iter_rows(min_row=2):
    county = row[0].value
    name = row[1].value
    if county != "San Mateo County" or not name:
        continue
    letter = name.replace("Measure ", "").strip()
    if letter in CONFIRMED:
        jurisdiction, desc, url = CONFIRMED[letter]
        row[2].value = jurisdiction
        row[3].value = desc
        row[4].value = ""
        row[5].value = url + " ; " + MEASURES_PAGE
        updated += 1

wb.save(XLSX_PATH)
print(f"Updated {updated} San Mateo measure rows with confirmed text")
