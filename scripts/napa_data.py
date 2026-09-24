# -*- coding: utf-8 -*-
CANDIDATES_URL = "https://www.napacounty.gov/DocumentCenter/View/46087/"

UNCONTESTED_FLAG = ('Uncontested - registrar marks this contest "On Ballot: No" (filed candidates do not '
                    'exceed available seats, so no election is held for this office)')

# (race, on_ballot(bool), [(name, occupation), ...])
RACES = [
    ("Napa County Board of Education Trustee Area 1", False, [("DON J HUFFMAN", "Incumbent")]),
    ("Napa County Board of Education Trustee Area 2", False, [("JANNA WALDINGER", "Incumbent")]),
    ("Napa County Board of Education Trustee Area 4", False, [("NADINE WADE", "Appointed Incumbent")]),
    ("Napa Valley College Trustee Area No. 2", True, [
        ("JEFF DODD", "Napa Valley College Trustee"),
        ("HERIVERTO RUIZ", "School Counselor"),
    ]),
    ("Napa Valley College Trustee Area No. 3", True, [
        ("EMILY PASTULA", "Teacher"),
        ("ELIZABETH L GOFF", "Retired Teacher"),
        ("KARINA SERVENTE", "Community Parent Liaison"),
    ]),
    ("Napa Valley College Trustee Area No. 4", True, [
        ("CINDY JOHNSON", "High School Counselor"),
        ('WILLIAM "KYLE" IVERSON', "Napa Valley College Trustee Dist. 4"),
    ]),
    ("Napa Valley College Trustee Area No. 5", False, [("LOTTE COSCA", "Appointed Incumbent")]),
    ("Napa Valley Unified School District Trustee Area No. 1", True, [
        ("ROBIN JANKIEWICZ", "Incumbent"),
        ("MATTHEW MCMANN", "Small Business Owner"),
    ]),
    ("Napa Valley Unified School District Trustee Area No. 3", False, [
        ("KATHERINE HYDE SHELTON", "Commercial Credit Lender"),
    ]),
    ("Napa Valley Unified School District Trustee Area No. 6", True, [
        ("ELBA GONZALEZ-MARES", "Executive Director"),
        ("TYRONE NAVARRO", "Retired Public Manager"),
    ]),
    ("Napa Valley Unified School District Trustee Area No. 7", True, [
        ("DAVID HILDEBRANDT", "Higher Education Professor"),
        ("JASON M. DOOLEY", "Attorney"),
        ("JOHN HOUSER", "Recreation Specialist"),
        ("GABRIEL CHAMPAGNE AFFONSO", "Community Volunteer"),
    ]),
    ("St Helena Unified School District Governing Board Member", False, [
        ("LAURA SYMON", "Incumbent"),
        ("SHAWN MOURA", "Incumbent"),
        ("JEANMARIE WOLF", "Incumbent"),
    ]),
    ("Calistoga Joint Unified School District Governing Board Member", True, [
        ("CECILIA RAMIREZ", "Hairdresser/Parent"),
        ("LAUREL RIOS", "Incumbent"),
        ("IRENE PENA", "School Psychologist"),
        ("REBECCA SAGER", "Teacher"),
    ]),
    ("Pope Valley Union School District Governing Board Member", False, [
        ("SHASTA TORREY", "Incumbent"),
        ("BRIAN VARNER", "Governing Board Member"),
    ]),
    ("City Council City of American Canyon", True, [
        ("JASON KISHINEFF", "Napa Valley College Board Trustee"),
        ("SINDY BIEDERMAN", "Napa County Office Of Education Board Trustee"),
        ("ROBERT COLE", "Non-Profit Organization President"),
        ("JIM GIRON", "Retired IT Executive"),
        ("DAVID ORO", "Business Owner/Councilmember"),
    ]),
    ("Mayor City of Calistoga", False, [("KEVIN EISENBERG", "Councilmember")]),
    ("City Council City of Calistoga", False, [
        ("LANA RICHARDSON", ""),
        ("SCOTT COOPER", ""),
    ]),
    ("City Council District 1 City of Napa", True, [("CHRISTOPHER DENATALE", "Appointed Incumbent")]),
    ("City Council District 3 City of Napa", True, [
        ("MARY LUROS", "Councilmember/Attorney/Mom"),
        ("JIM HINTON", "Caregiver"),
    ]),
    ("Mayor City of St Helena", True, [
        ("BONNIE SCHOCH", "Accountant"),
        ("PATRICK KENEALY", "Venture Capitalist"),
    ]),
    ("City Council City of St Helena", True, [
        ("KATE SPADAROTTO", "Appointed Incumbent"),
        ("JOSHUA PARKE", "Business Owner/Parent"),
        ("DANIEL HALE", "Designer"),
        ("JOHN PEDERSEN", "Father"),
        ("SCOTT DIAZ", "Appointed Incumbent"),
    ]),
    ("Mayor Town of Yountville", True, [
        ("MARJORIE MOHLER", "Mayor"),
        ("JOE TAGLIABOSCHI", "City Manager"),
    ]),
    ("Member of Town Council Town of Yountville", True, [
        ("ROBIN MCKEE", "Incumbent"),
        ("JESSI BUGDEN", ""),
        ("MATTHEW CHRZANOWSKI", "Winegrower"),
        ("HILLERY BOLT TRIPPE", "Retired Attorney"),
        ("JILL TURNER", "Businessperson"),
    ]),
    ("Circle Oaks Water District Board Member", False, [
        ("EVA VALENTI-BIRD", "Appointed Incumbent"),
        ("LISA M HACKETT", "Appointed Incumbent"),
    ]),
    ("Congress Valley Water District Board Member", False, [
        ("ERIK ERICKSON", "Retired Deputy Sheriff"),
        ("ADAM JOFFE", "Incumbent"),
        ("ROBERT EDWIN LEE", "Registered Nurse"),
    ]),
    ("Los Carneros Water District Board Member", False, [
        ("WILL DRAYTON", "Incumbent"),
        ("JIM LINCOLN", "Incumbent"),
    ]),
    ("Napa County Regional Park & Open Space Director, Ward 1", False, [
        ("BRAD WAGENKNECHT", "Parks Director Ward 1"),
    ]),
    ("Napa County Regional Park & Open Space Director, Ward 5", False, [
        ("BARRY CHRISTIAN", "Director Ward 5"),
    ]),
    ("Spanish Flat Water District Board Member", False, [
        ("CHERYL BEAN", "Incumbent"),
        ("JULIA ROBINSON", "Incumbent"),
        ("MEGAN JEPSEN", "Incumbent"),
    ]),
]

# (letter, jurisdiction, description, source_url, flag)
MEASURES = [
    ("B", "County of Napa",
     "AN INITIATIVE IMPOSING A ONE-HALF PERCENT (1/2%) SALES TAX FOR WILDFIRE PREPAREDNESS, WATERSHED PROTECTION, AND OPEN SPACE PRESERVATION\n\n"
     "SUMMARY: This initiative, entitled the “Napa County Wildfire Preparedness, Watershed Protection and Open Space Preservation Act of 2026” would add a new Chapter 3.38 to Title 3 of the Napa County Code.\n\n"
     "The Initiative, if enacted, would do all of the following:\n"
     "1) Impose a countywide retail transaction and use tax (“sales tax”) at the rate of one-half of one percent (1/2%), on the sale and use of tangible personal property within Napa County, including both the incorporated and unincorporated areas of the county. The sales tax would be imposed for eighteen (18) years, beginning on April 1, 2027 and expiring on March 31, 2045.\n"
     "2) Limit the use of, and require that sales tax proceeds be used for, the specific purposes identified in the Initiative’s Expenditure Plan, which includes wildfire preparedness, watershed protection, open space preservation, and administrative expenditures related to the planning and implementation of the Initiative. The Expenditure Plan outlines the specific program expenditure categories. The Expenditure Plan would be codified as Section 3.38.040 of the Napa County Code and would guide how the proceeds will be used.\n"
     "3) Require the County Auditor-Controller to establish a special fund for the deposit of sales tax proceeds and mandate allocation of 50% of sales tax proceeds to Napa County and 50% of the sales tax proceeds to the Napa County Regional Park and Open Space District (“Park District”).\n"
     "4) Require the County and the Park District to distribute the sales tax proceeds to grantees through a competitive grant process, as further described in the Initiative, to be used only for the purposes outlined in the Expenditure Plan. The County may award grants only to 501c3 nonprofit organizations, with exceptions as outlined in the Initiative. The Parks District may grant awards to 501c3 nonprofit corporations and public agencies as described in the Initiative.\n"
     "5) Establish an Oversight Committee tasked with reviewing the receipt and expenditure of sales tax proceeds, including an annual report of each grantee’s use of funds. The Committee will consist of nine Napa County resident members and 3 non-voting ex-officio members: County Auditor, Park District General Manager, and County Fire Administrator, or their respective designees.\n"
     "6) Increase the appropriations limit for the County by four years, to allow the use of all raised sales tax proceeds.",
     "https://www.napacounty.gov/2471/County-of-Napa---Measure-B ; https://www.napacounty.gov/DocumentCenter/View/40594/Measure-B---Ballot-Title-and-Summary---Napa-County-PDF",
     ""),
    ("P", "City of American Canyon", "",
     "https://www.napacounty.gov/2470/City-of-American-Canyon---Measure-P",
     'Could not retrieve ballot question text: Napa County’s page defers to the City of American Canyon’s own website ("americancanyon.gov/Work/Elections-Central") for Measure P details, and that site blocked every access attempt (Akamai "Access Denied", even via a real browser) - left blank rather than guess'),
    ("S", "City of St Helena",
     "St. Helena City Services Measure\n\nTo maintain/improve St. Helena’s long-term finances and maintain 911 fire/public safety response, St. Helena’s infrastructure including repairing roads/potholes/sidewalks; reducing local wildfire risk by managing brush/other fuels; maintain parks; supporting local businesses; for other general city services; shall the measure be adopted establishing a ½¢ locally controlled sales tax, generating approximately $2,000,000 annually until ended by voters, requiring independent audits, public spending disclosure, all funds benefiting St. Helena residents?",
     "https://www.napacounty.gov/2330/City-of-St-Helena---Measure-S ; https://www.cityofsthelena.gov/985/Measure-S---Ballot-Question",
     ""),
    ("Y", "Town of Yountville",
     "Proposed Ballot Measure – Increase in Appropriations (GANN) Limit\n\n"
     "“To fully utilize TOT and sales tax generated from visitors for public services, parks and recreation, police, and fire emergency programs, shall the appropriations limit set by Article 13B of the California Constitution be increased by $3,000,000 plus 1/4 of TOT revenues for the prior fiscal year, for each year for a four year period commencing FY 2027/2028? By approving this appropriation limit, no existing tax is increased, and no new taxes are created.”",
     "https://www.napacounty.gov/2472/Town-of-Yountville---Measure-Y ; https://www.townofyountville.com/DocumentCenter/View/4198",
     ""),
]
