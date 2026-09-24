# -*- coding: utf-8 -*-
CANDIDATES_URL = ("https://www.sf.gov/candidates-november-3-2026-general-election ; "
                   "https://api.sf.gov/documents/63094/November_2026_Local_Office_Names_and_Ballot_Designations.pdf")
MEASURES_URL = ("https://www.sf.gov/qualified-ballot-measures ; "
                 "https://api.sf.gov/documents/61682/Ballot_Questions_November_2026.pdf")

CITY = "City and County of San Francisco"

# (race, [(name, occupation), ...])
RACES = [
    ("Board of Supervisors, District 2", [
        ("Nicholas Berg", "Property Management Executive"),
        ("Guy McCoy", ""),
        ("Monthanus Ratanapakdee", "Community Advocate / Mother"),
        ("Stephen Sherrill", "Appointed Member, Board of Supervisors"),
    ]),
    ("Board of Supervisors, District 4", [
        ("Albert Chow", "Hardware Store Owner"),
        ("Jeremy Julian Greco", "Campus Coordinator / Monologist"),
        ("Alan Wong", "Appointed Member, Board of Supervisors"),
    ]),
    ("Board of Supervisors, District 6", [
        ("Alex Behrend", "Laborer / Community Organizer"),
        ("Matt Dorsey", "San Francisco Supervisor"),
    ]),
    ("Board of Supervisors, District 8", [
        ("Gary McCoy", "Healthcare Policy Advocate"),
        ("Michael T. Nguyen", "Attorney / Drag Producer"),
        ("Darshini Patel", "Community Advocate"),
        ('Emanuel "Manny" Yekutiel', "Small Business Owner"),
    ]),
    ("Board of Supervisors, District 10", [
        ('Pearci "PJ" Bastiany III', "MPA Graduate Student"),
        ("Dionjay (DJ) Brookter", "Community Organizer"),
        ("Deandra Bryant", "Housing Advocate"),
        ("Theo Ellington", "Public Policy Director"),
        ("J.R. Eppler", "Small Business Attorney"),
        ('Ellsworth "Ell" M. Jennison, Jr.', "Union Carpenter"),
        ("Mike Trouble Lin", "Small Business Consultant"),
        ("Jamo Muhammad", "Father"),
        ("Jessica Pessecow", "Nurse / Legal Representative"),
        ("Shawn M. Richard", ""),
    ]),
    ("Assessor-Recorder", [
        ("Joaquin Torres", "Incumbent"),
    ]),
    ("Public Defender", [
        ("Manohar Raju", "Public Defender"),
    ]),
    ("Board of Education", [
        ("Autumn Brown Garibay", "Public School Parent"),
        ("Virginia Cheung", "Nonprofit Executive / Mother"),
        ("Alida Fisher", "School Board Member"),
        ("Ryan Hazelton", "Children's Nonprofit Director"),
        ("Phil Kim", "School Board President"),
        ("Laurance Lee", "General Contractor"),
        ("Reina Tello", "Community Organizer / Parent"),
        ("Tim Tung", "Public Finance Analyst"),
    ]),
    ("Community College Board", [
        ("Elijah Ball", "College Campus Planner"),
        ("Rome Moses Jones", "Non-profit Executive"),
        ("Monroe Lace", "Public School Teacher"),
        ("Leah LaCroix", "Administrative Analyst"),
        ("Jeremy Lee", "Asset Manager"),
        ("Bunny McFadden", "Nonprofit Manager / Writer"),
        ("Erwin Tam", "Municipal Financial Advisor"),
        ("Lisa P Wynn II", "Health Equity Researcher"),
    ]),
    ("Community College Board Partial Term", [
        ("Ruth Ferguson", "Appointed Trustee, Community College"),
    ]),
    ("BART Board, District 8", [
        ("Sara Barz", "Transportation Planning Manager"),
    ]),
]

RTM_FLAG = ('Regional measure spanning 5 Bay Area counties (Alameda, Contra Costa, San Francisco, San Mateo, '
           'Santa Clara) - no single-jurisdiction name given by the registrar beyond the title')

# (letter, title, jurisdiction, description, flag)
MEASURES = [
    ("A", "Charter Changes Affecting Various City Departments and Commissions", CITY,
     "Shall the City amend the Charter to align it with how some City departments currently operate, change some processes, eliminate or reorganize certain commissions and advisory bodies, and require the Board of Supervisors to amend voter-approved laws to enact some of these changes?", ""),
    ("B", "Establishing a Municipal Finance Corporation and a Public Bank", CITY,
     "Shall the City amend the Charter to authorize the City to establish a municipal finance corporation and a public bank?", ""),
    ("C", "Contributions to the Housing Fund", CITY,
     "Shall the City amend the Charter to change how the City’s annual contributions to the Housing Trust Fund are set, increase funding and expand programs for affordable housing, and extend the Fund to 2058?", ""),
    ("D", "Changes to Ballot Measure Process", CITY,
     "Shall the City amend the Charter to increase the requirements for signature initiatives from 2% to 8% of registered voters in San Francisco (currently from about 10,600 to about 42,500 signatures), increase the requirements for calling special elections, allow signature initiatives to be withdrawn before an election, and remove the ability of a minority of Board of Supervisors members or the Mayor to place measures on the ballot?", ""),
    ("E", "City Administrator’s Authority and Changes to City Contracting", CITY,
     "Shall the City amend the Charter to give the City Administrator more authority by centralizing the City’s purchasing rules and processes, changing how the City approves purchasing rules, changing when contracts and leases require Board of Supervisors approval, and extending the City Administrator’s term?", ""),
    ("F", "Changes to Executive Branch Management", CITY,
     "Shall the City amend the Charter to expand the Mayor’s authority to transfer responsibilities between departments, hire deputy mayors, and hire some and fire most department heads; and to allow City officials to remove members of boards and commissions without cause?", ""),
    ("G", "Allowing Private Vehicles on the Great Highway in Sunset Dunes Park", CITY,
     "Shall the City close Sunset Dunes Park from Monday at 4:00 a.m. through Friday at 6:00 p.m., unless a holiday falls on a weekday, in order to reopen the roadway known as the Upper Great Highway to private vehicles during that time?", ""),
    ("H", "Parcel Tax to Fund Public Muni Operations", CITY,
     "Shall the City fund Muni service through a new annual parcel tax on real estate at rates ranging from $129 per parcel up to a maximum of $400,000 per parcel, depending on the type of property and its size and adjusted annually for inflation, for estimated revenue of $177 million a year for 15 years?", ""),
    ("I", "Changes to Real Property Transfer Tax", CITY,
     "Shall the City permanently dedicate half of the transfer tax revenues collected when certain real estate with a value or sales price of more than $10,000,000 changes hands, which will continue to be taxed at rates of 5.5% to 6%, to be spent only on affordable housing, including social housing developments and housing assistance, and exempt certain sales from the dedicated portion of the tax, for an estimated annual revenue decrease of approximately $1 million?", ""),
    ("J", "Removal of Foreclosure Exemption for Real Property Transfer Tax", CITY,
     "Shall the City permanently apply a transfer tax of between 0.5% and 6% of a property’s fair market value, on the transfer of properties such as commercial, industrial, and large residential properties, that are transferred to a lender because of foreclosure or to avoid foreclosure, for estimated annual revenue of $100 million to $150 million?", ""),
    ("RTM", "Regional Transit Measure", "",
     "To prevent major service cuts to BART and other transit, avoid increased traffic, and reduce pollution by: Preserving BART, Caltrain, VTA, SamTrans, AC Transit, Muni, other transit for everyone, including workers, students, seniors, persons with disabilities; Supporting transit safety, cleanliness, affordability, reliability; Repairing targeted roads/potholes; Requiring financial transparency, oversight, accountability; shall the measure enacting a 0.5% (Alameda, Contra Costa, San Mateo, Santa Clara counties), and 1% (San Francisco) sales tax for 14 years generating approximately $980,000,000 annually, be adopted?",
     RTM_FLAG),
]
