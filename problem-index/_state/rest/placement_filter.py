"""Short-term placement filter: rank the 421 queued industries by how fast an engineer can get
placed (forward deployed, software or lead engineer) by building a small MVP for a live pain
and showing it to someone who is hiring or paying.

Usage (from the vault root): python3 _state/rest/placement_filter.py
Writes _state/rest/placement-filter.tsv (every row, ranked) and prints the shortlist.

Factors, each 1-5 (desk scores, 2026-10-23; the shortlist is then checked against the web and
corrected in EVIDENCE below):
  E  Employers   funded software or AI companies selling into the industry, or in-house tech
                 teams, hiring engineers or forward deployed engineers now
  P  Pain        a paid-for problem that is still open (buyers already spend, incumbents
                 haven't fixed it, or a rule or shortage makes it urgent)
  M  MVP         a solo engineer can build a convincing demo in about two weeks from public
                 data, sample documents or synthetic data (no hardware, plant access or
                 regulated client data)
  F  Fast yes    how quickly the person you pitch (vendor hiring manager or owner-operator)
                 can hire or pay; public procurement and hospital committees score 1-2
  R  Reach       decision-makers findable without LinkedIn: public registries, association
                 and exhibitor lists, startup directories, communities
Score = 3E + 2P + 2M + 2F + R (max 50). Gate: E >= 3 and M >= 3.
"""
import csv

S = """
architecture-firms 3 3 4 4 4
landscape-architecture-firms 2 2 3 4 3
interior-design-firms 3 3 4 5 4
graphic-design-studios 3 2 5 5 4
specialty-design-studios 2 2 3 4 3
drafting-services 3 3 4 4 3
testing-laboratories 3 4 3 3 3
geophysical-survey-firms 2 3 2 3 2
logistics-consultants 2 3 4 4 3
contract-research-labs 4 4 3 3 3
biotech-research-firms 5 4 4 3 4
public-relations-agencies 3 3 5 5 4
media-rep-firms 2 2 4 4 3
outdoor-advertising-companies 3 3 4 4 3
direct-mail-agencies 2 3 4 4 3
portrait-photography-studios 2 2 4 5 3
commercial-photographers 2 2 4 5 3
title-and-settlement-offices 4 4 5 4 4
notary-signing-services 3 3 4 5 4
legal-support-services 5 4 5 4 4
film-distributors 2 3 4 3 3
movie-theaters 2 2 3 3 3
postproduction-studios 3 3 4 4 3
music-publishers 3 4 4 4 3
recording-studios 2 2 4 5 3
directory-and-list-publishers 2 2 4 4 3
greeting-card-publishers 1 2 4 3 2
broadcast-stations 2 3 4 3 3
wired-broadband-providers 3 4 4 3 3
wireless-carriers 4 3 2 2 2
telecom-resellers 2 3 4 4 3
wireless-retail-agents 2 2 3 4 2
satellite-operators 4 3 3 3 3
libraries-and-archives 2 2 4 2 3
community-banks 4 4 4 3 4
credit-card-issuers 4 3 3 2 3
sales-finance-companies 3 3 4 3 3
mortgage-lenders 4 4 5 4 4
pawnshops 2 2 3 4 3
money-service-businesses 4 4 4 4 3
commodity-brokers 2 3 3 3 2
trust-companies 3 3 3 3 3
pension-funds 2 3 4 2 3
self-insured-benefit-pools 3 4 3 3 3
life-insurance-carriers 4 4 4 2 3
health-insurance-carriers 5 5 4 2 3
property-casualty-insurers 5 4 5 3 4
title-insurance-carriers 3 3 4 3 3
reinsurers 3 3 3 2 2
facilities-management-firms 3 3 3 3 3
executive-search-firms 3 3 5 5 4
professional-employer-organizations 3 3 4 3 3
document-preparation-services 2 2 5 5 3
answering-services 4 4 5 5 4
private-mail-centers 1 2 3 4 2
credit-bureaus 3 3 3 2 2
repossession-services 2 3 3 4 3
court-reporting-firms 3 4 4 4 3
travel-agencies 4 3 5 5 4
tour-operators 2 2 4 4 3
visitors-bureaus 1 2 4 2 3
ticketing-agencies 3 3 4 4 3
investigation-and-screening-firms 3 3 4 4 3
armored-car-services 1 2 2 3 2
security-alarm-integrators 3 3 3 4 3
locksmiths 1 2 3 5 3
contract-packagers 2 3 3 4 3
auctioneers 2 2 4 4 3
waste-haulers 3 3 3 3 3
hazardous-waste-firms 2 4 4 3 3
landfill-operators 2 3 2 2 2
waste-to-energy-plants 1 2 2 2 2
recycling-facilities 4 3 2 3 3
septic-service-companies 2 2 3 5 3
community-colleges 3 4 4 2 4
colleges-and-universities 4 4 4 2 4
it-training-bootcamps 2 2 5 4 3
flight-schools 2 3 3 4 3
fine-arts-schools 1 2 4 3 2
sports-instruction-schools 2 2 4 5 3
driving-schools 2 2 4 5 3
safety-training-providers 2 3 4 4 3
education-consulting-and-testing 4 3 5 4 4
physician-practices 5 5 5 4 4
optometry-practices 3 3 4 5 3
podiatry-practices 2 3 4 5 3
community-health-centers 3 4 4 3 4
dialysis-centers 3 4 3 2 2
clinical-laboratories 4 5 4 3 3
diagnostic-imaging-centers 5 4 4 3 3
ambulance-services 3 4 4 3 3
blood-and-organ-banks 2 3 3 2 2
health-screening-services 2 3 4 4 3
general-hospitals 5 5 3 3 3
psychiatric-hospitals 3 4 4 3 3
specialty-hospitals 3 4 3 3 3
skilled-nursing-facilities 4 5 5 3 4
assisted-living-communities 3 4 4 4 3
idd-group-homes 3 4 4 4 3
residential-treatment-centers 3 4 4 4 3
youth-group-homes 2 3 3 3 2
self-storage-operators 3 3 4 4 4
car-rental-companies 3 3 3 3 3
truck-and-trailer-lessors 3 3 3 3 3
rent-to-own-stores 2 2 3 3 2
formal-wear-rental-shops 1 2 3 4 2
recreational-rental-shops 2 2 4 5 3
equipment-rental-companies 4 4 4 3 4
aircraft-and-railcar-lessors 3 4 4 3 3
franchisors 3 3 5 4 4
performing-arts-companies 2 3 4 3 3
musical-groups 1 2 4 4 2
sports-teams 4 3 4 3 3
racetracks 2 2 3 3 2
racing-stables 1 2 3 4 2
event-venues 3 3 4 4 3
event-promoters 3 3 4 4 3
museums 2 2 4 2 3
zoos-and-botanical-gardens 1 2 3 2 2
theme-parks 3 3 3 2 2
family-entertainment-centers 2 2 4 5 3
casinos 4 3 3 2 3
gambling-operators 4 3 4 3 3
golf-clubs 2 2 4 4 3
ski-resorts 2 2 3 3 2
marinas 2 2 4 4 3
auto-glass-shops 3 3 4 4 3
quick-lube-shops 2 2 3 4 3
car-washes 3 3 3 4 3
electronics-repair-shops 2 2 4 5 3
industrial-repair-shops 2 3 3 4 3
appliance-repair-companies 3 3 4 5 3
upholstery-shops 1 2 3 5 2
shoe-repair-shops 1 1 3 5 2
nail-salons 2 2 4 5 3
weight-loss-centers 3 3 4 4 3
cemeteries-and-crematories 2 2 4 4 3
laundromats 2 2 3 5 3
drycleaners 2 2 3 5 3
commercial-laundries 2 2 3 3 2
photo-labs 1 1 3 4 2
parking-operators 4 3 4 3 3
bail-bond-agencies 2 2 4 5 3
grantmaking-foundations 3 3 5 4 4
advocacy-nonprofits 2 3 5 4 3
civic-and-fraternal-clubs 1 2 4 3 2
labor-unions 2 3 4 2 2
political-campaigns 2 3 5 4 4
bed-and-breakfasts 2 2 4 5 3
rv-parks-and-campgrounds 2 2 4 5 3
summer-camps 2 2 4 4 3
workforce-housing-operators 2 3 3 3 2
contract-food-service-operators 3 3 3 2 2
bars-and-taverns 2 2 3 5 3
wholesale-auto-auctions 4 3 4 3 3
auto-parts-distributors 3 4 4 3 3
auto-salvage-yards 3 3 4 4 3
home-furnishings-wholesalers 2 3 4 4 3
building-material-dealers 4 4 5 4 4
business-equipment-dealers 2 3 4 4 3
it-value-added-resellers 3 3 5 4 3
medical-supply-distributors 4 4 4 3 3
metal-service-centers 3 4 5 4 3
electrical-distributors 4 4 5 4 4
consumer-goods-wholesalers 3 3 4 4 3
electronic-component-distributors 4 4 5 4 3
hardware-wholesalers 2 3 4 4 3
plumbing-and-hvac-distributors 3 4 5 4 3
heavy-equipment-dealers 3 3 4 3 3
farm-equipment-dealers 2 3 3 3 3
industrial-distributors 4 4 5 4 4
aviation-parts-distributors 3 4 4 4 3
scrap-metal-recyclers 2 3 3 4 3
business-supplies-distributors 2 3 4 3 3
pharmaceutical-wholesalers 3 4 3 2 2
apparel-wholesalers 2 3 4 4 3
grain-elevators 2 3 3 3 2
livestock-auction-markets 2 2 3 4 2
chemical-distributors 3 4 5 3 3
fuel-distributors 3 3 4 3 3
beverage-alcohol-distributors 3 3 4 3 3
ag-input-retailers 3 3 4 3 3
floral-wholesalers 1 2 4 4 2
convenience-store-distributors 2 3 4 3 3
manufacturers-reps 3 3 5 5 3
franchised-car-dealers 5 4 5 4 4
powersports-and-boat-dealers 3 3 4 5 3
tire-dealers 2 3 4 4 3
hardware-stores 2 2 4 4 3
paint-stores 1 2 3 3 2
outdoor-power-equipment-dealers 2 2 4 4 3
garden-centers 2 2 4 4 3
grocery-stores 4 4 3 3 3
convenience-stores 3 3 3 3 3
vending-machine-operators 3 3 3 4 3
liquor-stores 2 2 4 4 3
furniture-stores 2 3 4 4 3
flooring-and-blinds-retailers 2 3 4 5 3
appliance-and-electronics-stores 2 2 3 3 2
general-merchandise-retailers 4 3 3 2 3
beauty-supply-stores 1 2 3 4 2
optical-retailers 3 3 4 4 3
supplement-stores 2 2 4 4 3
propane-and-heating-oil-dealers 3 3 4 4 3
jewelry-stores 2 2 4 5 3
sporting-goods-stores 2 2 3 3 2
hobby-and-craft-stores 1 2 3 3 2
musical-instrument-stores 1 2 4 4 2
bookstores 1 2 4 4 2
florists 2 2 4 5 3
thrift-and-resale-stores 3 3 4 4 3
pet-stores 2 2 4 4 3
art-galleries 2 2 4 4 3
manufactured-home-dealers 2 3 4 4 3
smoke-and-vape-shops 1 2 3 4 2
passenger-airlines 4 4 3 2 3
air-cargo-carriers 3 4 4 3 3
charter-air-operators 3 3 4 4 3
freight-railroads 3 3 3 1 2
rail-services-contractors 2 3 3 3 2
ocean-shipping-carriers 4 4 4 3 3
tug-and-barge-operators 2 3 3 3 2
cruise-lines 3 3 3 2 2
ferry-operators 1 2 3 2 2
boat-tour-operators 1 2 4 5 3
ltl-carriers 4 5 4 3 3
transit-agencies 4 3 5 1 3
school-bus-contractors 3 3 4 3 3
pipeline-operators 3 4 3 2 2
sightseeing-tour-companies 1 2 4 4 2
aerial-tour-operators 1 2 3 4 2
airport-operators 3 3 3 1 2
aircraft-mro-shops 4 5 4 3 3
port-terminal-operators 3 3 3 2 2
marine-pilotage-and-towing 1 2 3 2 2
toll-road-operators 2 2 3 1 2
crating-and-export-packers 2 3 4 4 3
land-developers 3 4 5 3 3
highway-contractors 3 4 5 3 3
heavy-civil-contractors 3 4 5 3 3
concrete-contractors 2 3 3 4 3
steel-erectors 2 3 3 4 2
framing-contractors 2 3 4 4 2
masonry-contractors 1 2 3 4 2
glazing-contractors 2 3 4 4 2
siding-contractors 2 2 4 5 3
elevator-contractors 2 3 3 3 2
drywall-and-insulation-contractors 3 3 4 4 2
flooring-contractors 2 3 4 4 2
tile-contractors 1 2 3 4 2
finish-carpentry-contractors 1 2 3 4 2
excavation-contractors 2 3 3 4 3
paving-contractors 2 3 4 4 3
hydroelectric-operators 2 3 3 2 2
thermal-power-plants 2 3 2 2 2
nuclear-power-plants 4 4 4 2 2
renewable-power-producers 4 5 5 3 3
transmission-operators 3 4 4 2 2
electric-utilities 4 5 4 2 3
gas-utilities 2 3 3 2 2
district-energy-operators 1 2 3 2 2
oil-and-gas-producers 4 3 4 3 3
coal-mines 1 2 2 2 2
metal-mines 3 3 3 2 2
gold-and-silver-mines 2 2 3 2 2
dimension-stone-quarries 1 2 2 3 2
aggregate-producers 2 3 3 3 2
industrial-mineral-mines 1 2 2 2 2
mining-contractors 2 3 3 3 2
fish-farms 2 3 2 3 2
shellfish-farms 1 2 2 3 2
beekeeping-operations 1 2 2 4 2
horse-breeding-farms 1 2 3 4 2
specialty-livestock-farms 1 2 3 4 2
timberland-managers 3 3 4 3 3
logging-companies 2 2 2 3 2
commercial-fishing-operations 1 2 2 3 2
hunting-outfitters 1 1 4 5 2
cotton-gins 1 2 2 3 2
custom-farming-contractors 2 2 3 4 2
produce-packing-houses 3 3 3 3 3
farm-labor-contractors 2 3 5 4 3
farm-management-firms 2 3 4 4 3
livestock-support-services 1 2 3 4 2
forestry-services 2 2 3 3 2
beverage-bottlers 2 3 3 3 2
breweries 2 2 4 5 3
wineries 2 2 4 4 3
distilleries 2 2 4 4 3
tobacco-manufacturers 1 2 2 2 1
textile-mills 1 2 2 2 2
nonwoven-fabric-mills 1 2 2 2 2
textile-dyers-and-finishers 1 2 2 3 2
carpet-mills 1 2 2 2 2
sewn-products-makers 2 2 3 4 2
apparel-manufacturers 3 3 4 3 3
tanneries 1 2 2 3 2
footwear-and-leather-goods-makers 2 2 3 3 2
sawmills 2 3 2 3 2
wood-treating-plants 1 2 2 3 2
engineered-wood-mills 1 2 2 2 2
millwork-manufacturers 2 3 4 4 2
pallet-manufacturers 1 2 3 4 2
factory-built-home-builders 2 3 3 3 2
pulp-and-paper-mills 2 3 2 2 2
paperboard-packaging-makers 2 3 4 3 2
paper-converters 2 2 3 3 2
petroleum-refineries 3 3 2 2 2
asphalt-plants 1 2 2 3 2
lubricant-blenders 2 2 3 3 2
petrochemical-plants 3 3 2 2 2
industrial-gas-producers 2 2 2 2 2
inorganic-chemical-plants 2 3 2 2 2
ethanol-plants 2 3 4 3 2
polymer-producers 2 3 2 2 2
fertilizer-plants 1 2 2 2 2
compost-producers 1 2 3 4 2
crop-protection-manufacturers 3 3 3 2 2
supplement-manufacturers 2 3 4 4 3
pharmaceutical-manufacturers 4 4 5 2 3
biologics-manufacturers 4 4 3 2 3
coatings-and-adhesives-makers 3 3 3 3 2
cleaning-chemical-makers 1 2 3 3 2
cosmetics-manufacturers 3 3 4 4 3
specialty-chemical-blenders 2 3 3 3 2
plastic-film-and-bag-makers 1 2 2 3 2
plastic-extruders 2 2 3 3 2
foam-product-makers 1 2 3 3 2
plastic-molders 3 3 4 4 3
tire-manufacturers 2 2 2 2 2
tire-retreaders 1 2 2 3 2
rubber-product-makers 2 2 3 3 2
ceramics-and-refractory-makers 1 2 2 3 2
glass-manufacturers 1 2 2 2 2
glass-fabricators 2 3 4 4 2
cement-and-lime-plants 2 3 2 2 2
ready-mix-concrete-producers 2 3 3 3 2
concrete-products-plants 2 2 3 3 2
building-products-plants 2 2 3 3 2
stone-countertop-fabricators 2 3 4 5 3
steel-mills 3 3 2 2 2
aluminum-extruders 2 3 3 3 2
nonferrous-metal-mills 2 2 2 2 2
sand-casting-foundries 2 3 3 3 2
investment-casting-foundries 2 3 3 3 2
die-casting-shops 2 3 3 3 2
forging-shops 2 3 3 3 2
metal-container-makers 1 2 2 2 2
tool-and-hardware-makers 2 2 3 3 2
fastener-manufacturers 2 3 4 3 2
valve-manufacturers 2 3 4 3 2
plumbing-products-makers 2 2 3 3 2
firearms-manufacturers 2 2 3 3 2
farm-equipment-manufacturers 3 3 3 2 2
heavy-machinery-manufacturers 3 3 3 2 2
oilfield-equipment-manufacturers 2 3 3 3 2
semiconductor-equipment-makers 4 3 2 2 2
industrial-machinery-builders 3 3 3 3 2
commercial-equipment-manufacturers 2 3 3 3 2
hvac-equipment-manufacturers 3 3 3 3 2
tool-die-and-mold-shops 3 4 4 4 3
machine-tool-builders 3 3 3 2 2
engine-and-turbine-makers 3 3 2 2 2
power-transmission-makers 2 2 3 3 2
pump-and-compressor-makers 2 2 3 3 2
material-handling-equipment-makers 4 3 2 3 3
fluid-power-manufacturers 2 2 3 3 2
computer-hardware-makers 3 2 2 2 2
communications-equipment-makers 3 2 2 2 2
audio-video-equipment-makers 2 2 3 3 2
pcb-fabricators 3 3 4 4 3
semiconductor-manufacturers 4 3 2 2 2
electronic-component-makers 2 3 3 3 2
avionics-and-defense-electronics-makers 4 3 3 2 2
process-instrument-makers 2 2 3 3 2
test-and-lab-instrument-makers 3 3 3 3 2
media-replication-plants 1 1 2 3 1
appliance-manufacturers 2 2 2 2 2
power-equipment-manufacturers 3 4 3 2 2
motor-and-control-makers 2 3 3 3 2
battery-manufacturers 4 3 2 2 2
wire-and-cable-manufacturers 2 3 3 3 2
electrical-products-manufacturers 2 3 3 3 2
vehicle-manufacturers 4 3 2 2 2
truck-body-and-trailer-builders 2 3 3 3 2
rv-manufacturers 2 3 3 3 2
auto-parts-suppliers 3 4 4 2 2
aircraft-manufacturers 4 3 2 2 2
aerospace-parts-suppliers 4 4 4 3 3
defense-systems-manufacturers 5 4 3 2 3
railcar-manufacturers 2 2 2 2 2
shipyards 3 4 3 2 2
boat-builders 2 2 3 3 2
powersports-vehicle-makers 2 2 3 2 2
cabinet-and-millwork-shops 2 3 4 5 3
furniture-manufacturers 2 2 3 3 2
contract-furniture-makers 2 3 4 3 2
dental-laboratories 3 4 3 4 3
jewelry-manufacturers 2 2 3 4 2
sporting-goods-manufacturers 2 2 3 3 2
toy-manufacturers 2 2 3 3 2
sign-shops 2 2 4 5 3
musical-instrument-makers 1 1 3 4 2
consumer-products-makers 4 4 5 4 3
legislative-bodies 2 2 4 1 3
tax-and-revenue-agencies 3 3 4 1 3
tribal-governments 2 3 3 2 2
courts 3 4 5 1 3
correctional-facilities 2 3 3 1 2
probation-and-parole-agencies 2 3 3 1 2
emergency-management-agencies 3 3 4 1 3
education-agencies 2 3 4 1 3
public-health-departments 2 3 4 1 3
benefits-administration-agencies 3 4 4 1 3
environmental-regulators 2 3 4 1 3
natural-resource-agencies 2 2 4 1 2
public-housing-authorities 2 3 4 2 3
economic-development-agencies 2 2 4 2 3
transportation-departments 3 3 4 1 3
utility-commissions 2 3 5 1 3
licensing-agencies 3 3 4 1 3
"""

# Web-checked corrections for the shortlist: slug -> (E, P, M, F, R, note). Filled after the
# evidence pass; a row here overrides the desk score above.
EVIDENCE = {
    # healthcare group (roles counted when listed on a company, ATS or VC job-board page)
    "physician-practices": (4, 4, 3, 4, 3, "FDE roles: Commure/Athelas, Hippocratic AI, Opmed.ai; CMS-0057 prior-auth rules; MVP: prior-auth packet from Synthea + payer policy PDFs"),
    "skilled-nursing-facilities": (4, 4, 5, 3, 4, "PointClickCare (AI engineer), Aline, SafelyYou; MVP: staffing-gap dashboard on CMS PBJ + Care Compare"),
    "diagnostic-imaging-centers": (3, 4, 4, 3, 3, "HOPPR (FDE ML); heaviest prior-auth specialty; MVP: order vs ACR Appropriateness Criteria checker"),
    "general-hospitals": (5, 5, 4, 2, 4, "FDE roles: OpenAI healthcare, Cair Health, Hippocratic AI, Opmed.ai, Smarter Technologies; pitch vendors, hospitals are slow"),
    "clinical-laboratories": (3, 4, 3, 3, 4, "labs hire in-house (Quest, CareDx, Personalis); PAMA cuts resume 2027; MVP: underpayment finder on CMS lab fee schedule"),
    "medical-supply-distributors": (2, 4, 3, 4, 4, "no DME vendor engineering role found; 2026 competitive bidding; owners reachable via VGM/AAHomecare"),
    "assisted-living-communities": (4, 3, 3, 4, 4, "SafelyYou, Aline, Mon Ami, Sensorum, AxisCare; pain not sourced"),
    "residential-treatment-centers": (2, 4, 3, 4, 4, "no engineering roles found; 42 CFR Part 2 enforceable 2026-02-16"),
    "pharmaceutical-manufacturers": (3, 4, 4, 2, 3, "Seal (FDE, GxP, London); MVP: CAPA drafts from FDA warning letters; slow buyers"),
    "education-consulting-and-testing": (2, 2, 3, 4, 4, "no vendor engineering roles; small budgets"),
    "health-insurance-carriers": (4, 5, 4, 2, 3, "FDE roles: Cohere Health, CLERA, OpenAI, Hippocratic AI; FHIR prior-auth APIs due 2027-01-01"),
    "property-casualty-insurers": (3, 4, 4, 4, 4, "FDE roles: Strada, Outmarket, ReSource Pro (several dated or India-based); MVP: ACORD submission intake"),
    "legal-support-services": (5, 4, 5, 4, 4, "FDE roles: OpenAI legal, August, Norm AI; Everlaw, Phaselab; MVP: review demo on Enron/EDRM + CourtListener"),
    "answering-services": (5, 4, 3, 5, 4, "FDE roles: Phonely, Acrely, Retell AI, PolyAI; Synthflow; MVP: voice receptionist on Twilio + LLM"),
    # distribution and manufacturing group (roles counted only when seen open on the page)
    "building-material-dealers": (3, 4, 4, 4, 4, "Avent (FDE), Mercura (FDE, Munich); MVP: priced lumber list from a public plan set"),
    "electrical-distributors": (4, 5, 4, 4, 5, "FDE roles: Avent, Mercura, Comena (last two Munich); NAED AI business case; MVP: RFQ email to quote from catalog PDFs"),
    "industrial-distributors": (4, 5, 4, 4, 4, "FDE roles: Avent, Comena, Mercura; Hexa, Augment in the space; MVP: RFQ/PO email to ERP draft quote"),
    "electronic-component-distributors": (2, 4, 4, 4, 3, "Cassidy, Boardera exist, no open engineering role seen"),
    "metal-service-centers": (2, 4, 3, 4, 4, "only Avent (generic); Uptool, Forgepoint unconfirmed"),
    "plumbing-and-hvac-distributors": (3, 4, 4, 4, 4, "Mercura, Avent, Comena (shared distributor vendors); Augment at Johnstone"),
    "manufacturers-reps": (2, 3, 3, 5, 5, "Parspec (sales roles only), Repfabric; owners fast and listed (MANA)"),
    "chemical-distributors": (2, 3, 3, 3, 4, "no chemical-specific vendor role; incumbents ship AI order entry"),
    "aviation-parts-distributors": (2, 4, 3, 4, 3, "ERP.Aero, ePlane AI exist, no role confirmed"),
    "consumer-products-makers": (3, 5, 3, 3, 3, "Confido (FDE + 3 engineering roles, NYC); deductions 3-7% of revenue (vendor figure)"),
    "tool-die-and-mold-shops": (2, 3, 3, 5, 4, "Uptool, CloudNC, CADDi; no open role seen"),
    "aerospace-parts-suppliers": (3, 4, 4, 4, 4, "SalesPatriot (FDE, Lead FDE); MVP: auto-balloon drawing + AS9102 form"),
    "defense-systems-manufacturers": (4, 3, 4, 2, 3, "FDE roles: Anduril, Vannevar Labs, SalesPatriot; clearance limits; CMMC L2 paused 2026-07"),
    "franchised-car-dealers": (3, 5, 3, 3, 4, "BizzyCar (eng lead, full stack); Toma/Impel unconfirmed; 19M of 53M service calls missed in 2025"),
    # energy, transport and other group (roles counted only when seen open on the page)
    "renewable-power-producers": (2, 5, 5, 3, 4, "Nira FDE closed; Enverus/Pearl Street, RatedPower unconfirmed; MVP: queue risk on LBNL Queued Up + ISO queues"),
    "electric-utilities": (4, 4, 4, 3, 4, "Gridsight (FDE, confirmed), E Source and MLabs (FDE, aggregator); MVP: hosting-capacity screen on EIA-860/861"),
    "aircraft-mro-shops": (3, 5, 3, 4, 4, "FDE roles: Zymbly, Soji AI; ~17,000 mechanic shortfall; MVP: work-card checker vs FAA ADs/SDRs"),
    "ltl-carriers": (2, 4, 3, 3, 3, "Pallet (agent delivery, logistics-wide), project44 unconfirmed; NMFC density reclass"),
    "ocean-shipping-carriers": (3, 4, 3, 4, 4, "Pallet confirmed, Reform FDE unconfirmed, Zencargo FDE closed; MVP: B/L to booking draft"),
    "equipment-rental-companies": (2, 3, 3, 4, 3, "Renterra, EquipmentShare, no confirmed role"),
    "heavy-civil-contractors": (3, 4, 5, 3, 4, "Rudus (FDE), Trunk Tools (FDE, unconfirmed); MVP: unit-price outliers from state DOT bid tabs"),
    "highway-contractors": (2, 4, 5, 3, 4, "no highway-specific vendor role; same bid-tab MVP as heavy civil"),
    "franchisors": (2, 3, 3, 3, 4, "no confirmed engineering roles; FDD Item 19 extractor from state portals"),
    "grantmaking-foundations": (2, 3, 5, 2, 4, "no confirmed roles; IRS 990-PF XML data; slow buyers"),
    "colleges-and-universities": (3, 4, 4, 2, 4, "Ellucian, CollegeVine (FDE, dated), Memorang; committee buyers"),
    "appliance-repair-companies": (1, 3, 3, 5, 3, "no vendors hiring"),
    "mortgage-lenders": (4, 4, 4, 3, 4, "Ocrolus mortgage FDE (confirmed); Valon, Addy AI, Saaf (FDE, aggregator); MVP: LE vs CD fee-cure checker"),
    "title-and-settlement-offices": (3, 4, 3, 4, 4, "Qualia (engineering), Propy; MVP: closing-package checker on recorder documents"),
}

desk = {}
for line in S.strip().splitlines():
    slug, *v = line.split()
    desk[slug] = list(map(int, v))

q = list(csv.DictReader(open("_state/rest/queue.tsv"), delimiter="\t"))
missing = {r["slug"] for r in q} - set(desk)
extra = set(desk) - {r["slug"] for r in q}
assert not missing and not extra, (sorted(missing), sorted(extra))

rows = []
for r in q:
    e, p, m, f, rr = (EVIDENCE[r["slug"]][:5] if r["slug"] in EVIDENCE else desk[r["slug"]])
    score = 3 * e + 2 * p + 2 * m + 2 * f + rr
    gate = e >= 3 and m >= 3
    rows.append({"slug": r["slug"], "name": r["name"], "category": r["category"], "status": r["status"],
                 "batch": r["batch"], "E": e, "P": p, "M": m, "F": f, "R": rr, "score": score,
                 "gate": "pass" if gate else "fail", "checked": "web" if r["slug"] in EVIDENCE else "desk",
                 "note": EVIDENCE.get(r["slug"], [""] * 6)[5]})
rows.sort(key=lambda x: (x["gate"] != "pass", -x["score"], -x["E"], x["slug"]))
for i, x in enumerate(rows, 1):
    x["rank"] = i
cols = ["rank", "slug", "name", "category", "status", "batch", "score", "E", "P", "M", "F", "R", "gate", "checked", "note"]
with open("_state/rest/placement-filter.tsv", "w", newline="") as fh:
    w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)
passing = [x for x in rows if x["gate"] == "pass"]
print(f"{len(rows)} industries, {len(passing)} pass the gate")
for x in passing[:60]:
    print(f"{x['rank']:>3} {x['score']:>2} {x['E']}{x['P']}{x['M']}{x['F']}{x['R']} {x['status'][:5]:<5} b{x['batch']:<3} {x['checked']} {x['slug']}")
