# Short-term placement filter

**Written:** 2026-10-23, at the owner's request. **Source:** `_state/rest/placement_filter.py` · full ranking of all 421 queued industries in `_state/rest/placement-filter.tsv` · web evidence with URLs in `_state/rest/placement-evidence/`.

The owner wants to move into a forward deployed, software or lead engineer role without the CV-and-job-board loop: build a small MVP for a live pain in an industry, then show it to a company that is hiring engineers or paying to make that pain go away. This filter picks the industries where that works fastest, so they get built first instead of waiting four weeks for the full 421-industry run.

## How it scores

Five factors, each 1–5:

| Factor | Question |
|---|---|
| **E** Employers | Do funded software or AI companies selling into this industry (or in-house tech teams) have open engineering or forward deployed roles now? |
| **P** Pain | Is there a paid-for problem that is still open: buyers already spend, a rule or deadline forces it, or a labour shortage drives it? |
| **M** MVP | Can one engineer build a convincing demo in about two weeks from public data, sample documents or synthetic data, without hardware, site access or client data? |
| **F** Fast yes | How fast can the person you'd pitch (a vendor's hiring manager or an owner-operator) hire or pay? Public procurement and hospital committees score 1–2. |
| **R** Reach | Can you find the decision-makers without LinkedIn: registries, association and exhibitor lists, startup directories? |

**Score = 3E + 2P + 2M + 2F + R** (max 50). **Gate:** E ≥ 3 and M ≥ 3. No employers means no placement, and no buildable demo means no proof.

All 421 were desk-scored first. The top 42 were then checked on the web on 2026-10-23: named vendors with open roles, one sourced pain, and a two-week MVP each. The web check was harsher than the desk scores: E fell by about one point on average, and 16 of the 42 failed the gate. Web-checked scores replace desk scores in the ranking.

## Ready now: already built and passing

These are already in the vault, so you can start an MVP today.

| Industry | Score (E P M F R) | Who's hiring, and the MVP |
|---|---|---|
| [[industries/legal-support-services\|Legal Support Services]] | **45** (5 4 5 4 4) | FDE roles: OpenAI legal, August, Norm AI; Everlaw, Phaselab; MVP: review demo on Enron/EDRM + CourtListener |
| [[industries/answering-services\|Telephone Answering Services]] | **43** (5 4 3 5 4) | FDE roles: Phonely, Acrely, Retell AI, PolyAI; Synthflow; MVP: voice receptionist on Twilio + LLM |
| [[industries/mortgage-lenders\|Mortgage Lenders]] | **38** (4 4 4 3 4) | Ocrolus mortgage FDE (confirmed); Valon, Addy AI, Saaf (FDE, aggregator); MVP: LE vs CD fee-cure checker |
| [[industries/health-insurance-carriers\|Health Insurance Carriers]] | **37** (4 5 4 2 3) | FDE roles: Cohere Health, CLERA, OpenAI, Hippocratic AI; FHIR prior-auth APIs due 2027-01-01 |
| [[industries/property-casualty-insurers\|Property & Casualty Insurers]] | **37** (3 4 4 4 4) | FDE roles: Strada, Outmarket, ReSource Pro (several dated or India-based); MVP: ACORD submission intake |
| [[industries/title-and-settlement-offices\|Title & Settlement Offices]] | **35** (3 4 3 4 4) | Qualia (engineering), Propy; MVP: closing-package checker on recorder documents |

Built but not web-checked, with high desk scores: [[industries/travel-agencies|Travel Agencies]], [[industries/biotech-research-firms|Biotech Research Firms]], [[industries/money-service-businesses|Money Service Businesses]], [[industries/executive-search-firms|Executive Search Firms]] and [[industries/community-banks|Community Banks]].

## Tonight's run: priority batches P1–P4

The night run on Sat 2026-10-24 (00:03–15:00 PKT, 3 agents) builds these before anything else, in this order. P1–P3 are the 20 web-checked industries that passed the gate. P4 adds the next eight by desk score, which have **not** been web-checked. Quota will probably run out somewhere in P3 or P4. Waste batch 9b and the normal sector order resume after P4.

### P1

| Industry | Score (E P M F R) | Evidence |
|---|---|---|
| Electrical Distributors | **43** (4 5 4 4 5) | FDE roles: Avent, Mercura, Comena (last two Munich); NAED AI business case; MVP: RFQ email to quote from catalog PDFs |
| Industrial Distributors | **42** (4 5 4 4 4) | FDE roles: Avent, Comena, Mercura; Hexa, Augment in the space; MVP: RFQ/PO email to ERP draft quote |
| General Hospitals | **41** (5 5 4 2 4) | FDE roles: OpenAI healthcare, Cair Health, Hippocratic AI, Opmed.ai, Smarter Technologies; pitch vendors, hospitals are slow |
| Skilled Nursing Facilities | **40** (4 4 5 3 4) | PointClickCare (AI engineer), Aline, SafelyYou; MVP: staffing-gap dashboard on CMS PBJ + Care Compare |
| Electric Distribution Utilities | **38** (4 4 4 3 4) | Gridsight (FDE, confirmed), E Source and MLabs (FDE, aggregator); MVP: hosting-capacity screen on EIA-860/861 |
| Physician Practices | **37** (4 4 3 4 3) | FDE roles: Commure/Athelas, Hippocratic AI, Opmed.ai; CMS-0057 prior-auth rules; MVP: prior-auth packet from Synthea + payer policy PDFs |
| Aerospace Parts Suppliers | **37** (3 4 4 4 4) | SalesPatriot (FDE, Lead FDE); MVP: auto-balloon drawing + AS9102 form |

### P2

| Industry | Score (E P M F R) | Evidence |
|---|---|---|
| Aircraft MRO & FBO Shops | **37** (3 5 3 4 4) | FDE roles: Zymbly, Soji AI; ~17,000 mechanic shortfall; MVP: work-card checker vs FAA ADs/SDRs |
| Building Material Dealers | **37** (3 4 4 4 4) | Avent (FDE), Mercura (FDE, Munich); MVP: priced lumber list from a public plan set |
| Heavy Civil Contractors | **37** (3 4 5 3 4) | Rudus (FDE), Trunk Tools (FDE, unconfirmed); MVP: unit-price outliers from state DOT bid tabs |
| Plumbing & HVAC Distributors | **37** (3 4 4 4 4) | Mercura, Avent, Comena (shared distributor vendors); Augment at Johnstone |
| Assisted Living Communities | **36** (4 3 3 4 4) | SafelyYou, Aline, Mon Ami, Sensorum, AxisCare; pain not sourced |
| Franchised Car Dealers | **35** (3 5 3 3 4) | BizzyCar (eng lead, full stack); Toma/Impel unconfirmed; 19M of 53M service calls missed in 2025 |
| Ocean Shipping Carriers | **35** (3 4 3 4 4) | Pallet confirmed, Reform FDE unconfirmed, Zencargo FDE closed; MVP: B/L to booking draft |

### P3

| Industry | Score (E P M F R) | Evidence |
|---|---|---|
| Diagnostic Imaging Centers | **34** (3 4 4 3 3) | HOPPR (FDE ML); heaviest prior-auth specialty; MVP: order vs ACR Appropriateness Criteria checker |
| Consumer Products Makers | **34** (3 5 3 3 3) | Confido (FDE + 3 engineering roles, NYC); deductions 3-7% of revenue (vendor figure) |
| Clinical Laboratories | **33** (3 4 3 3 4) | labs hire in-house (Quest, CareDx, Personalis); PAMA cuts resume 2027; MVP: underpayment finder on CMS lab fee schedule |
| Defense Systems Manufacturers | **33** (4 3 4 2 3) | FDE roles: Anduril, Vannevar Labs, SalesPatriot; clearance limits; CMMC L2 paused 2026-07 |
| Colleges & Universities | **33** (3 4 4 2 4) | Ellucian, CollegeVine (FDE, dated), Memorang; committee buyers |
| Pharmaceutical Manufacturers | **32** (3 4 4 2 3) | Seal (FDE, GxP, London); MVP: CAPA drafts from FDA warning letters; slow buyers |

### P4 (desk-ranked, not web-checked)

| Industry | Score (E P M F R) | Evidence |
|---|---|---|
| IDD Group Homes | **36** (3 4 4 4 3) | desk score only |
| IT Distributors & Value-Added Resellers | **36** (3 3 5 4 3) | desk score only |
| Land Developers | **36** (3 4 5 3 3) | desk score only |
| Optometry Practices | **36** (3 3 4 5 3) | desk score only |
| Powersports & Boat Dealers | **36** (3 3 4 5 3) | desk score only |
| Sportsbooks & Other Gambling Operators | **35** (4 3 4 3 3) | desk score only |
| Grocery Stores | **35** (4 4 3 3 3) | desk score only |
| Oil & Gas Producers | **35** (4 3 4 3 3) | desk score only |

## Checked and failed the gate

These have real pain, but no vendor had an open engineering role on its own page today (E ≤ 2), so they stay in their sector batches:

| Industry | Score (E P M F R) | Why it failed |
|---|---|---|
| Renewable Power Producers | **36** (2 5 5 3 4) | Nira FDE closed; Enverus/Pearl Street, RatedPower unconfirmed; MVP: queue risk on LBNL Queued Up + ISO queues |
| Highway & Bridge Contractors | **34** (2 4 5 3 4) | no highway-specific vendor role; same bid-tab MVP as heavy civil |
| Electronic Component Distributors | **33** (2 4 4 4 3) | Cassidy, Boardera exist, no open engineering role seen |
| Manufacturers' Representatives | **33** (2 3 3 5 5) | Parspec (sales roles only), Repfabric; owners fast and listed (MANA) |
| Medical Supply Distributors | **32** (2 4 3 4 4) | no DME vendor engineering role found; 2026 competitive bidding; owners reachable via VGM/AAHomecare |
| Metal Service Centers | **32** (2 4 3 4 4) | only Avent (generic); Uptool, Forgepoint unconfirmed |
| Residential Treatment Centers | **32** (2 4 3 4 4) | no engineering roles found; 42 CFR Part 2 enforceable 2026-02-16 |
| Tool, Die & Mold Shops | **32** (2 3 3 5 4) | Uptool, CloudNC, CADDi; no open role seen |
| Aircraft & Marine Parts Distributors | **31** (2 4 3 4 3) | ERP.Aero, ePlane AI exist, no role confirmed |
| Grantmaking Foundations | **30** (2 3 5 2 4) | no confirmed roles; IRS 990-PF XML data; slow buyers |
| Equipment Rental Companies | **29** (2 3 3 4 3) | Renterra, EquipmentShare, no confirmed role |
| LTL Carriers | **29** (2 4 3 3 3) | Pallet (agent delivery, logistics-wide), project44 unconfirmed; NMFC density reclass |
| Chemical Distributors | **28** (2 3 3 3 4) | no chemical-specific vendor role; incumbents ship AI order entry |
| Education Consulting & Testing Services | **28** (2 2 3 4 4) | no vendor engineering roles; small budgets |
| Franchisors | **28** (2 3 3 3 4) | no confirmed engineering roles; FDD Item 19 extractor from state portals |
| Appliance Repair Companies | **28** (1 3 3 5 3) | no vendors hiring |

Renewable power producers is the closest miss. It has the strongest pain and data of any industry checked: about 2,061 GW sits in interconnection queues, and LBNL's Queued Up dataset plus the ISO queue files are public. Its one FDE role (Nira Energy) had closed, so it fails the gate on E. Re-check it in a few weeks.

## Caveats

- Job postings change weekly. Re-open each link before you pitch. The URLs are in `_state/rest/placement-evidence/`.
- The three checkers weren't equally strict. The healthcare, insurance and legal group counted roles listed on company, ATS or VC job-board pages. The other two counted only roles they saw open on the page, so their E scores run a little low.
- The Mercura and Comena roles are in Munich. Avent is the US option among the distributor vendors.
- Defense roles (Anduril, Vannevar) often need US citizenship or a clearance.
- Rows marked desk in the TSV are judgement scores, not evidence.
- The 257 industries built before this plan (the original 118 plus Phase 4) are not scored here. The same script could score them.

## Priority order for the rest of the run (2026-10-27)

The owner restarted the run on 2026-10-27 with five industries a day (one agent, 00:00–12:00 PKT) and asked for the industries that matter most to the placement goal to go first, so the other ~290 can wait. `_state/rest/priority_order.py` put these 35 into daily batches Q1–Q7, right after waste batch 9b's three built industries. All of them are desk scores apart from the ones marked web, and desk E ran about a point high when the first 42 were checked. So each batch gets a web check (vendors with open engineering or FDE roles, own pages only) before its builders start, and any industry that fails moves behind Q7.

How they were picked: the filter score first; then a boost where an industry shares a vendor field that already proved out in P1–P4 (AI quoting for distributors, prior-auth and revenue-cycle vendors in healthcare, the dealer and auction stack in autos), so one demo can be shown to several vendors; then a cut for clearance or citizenship limits (owner works from Pakistan) and for buyers who move through public procurement.

| Day | Batch | Industries | Why this group |
|---|---|---|---|
| 1 | Q1 | Renewable Power Producers (36, web), Wholesale Auto Auctions (35), Community Health Centers (35), Parking Operators (35), Auto Parts Distributors (34) | Strongest pain and public data checked so far (interconnection queues), the auction and parts side of the built dealer stack, healthcare's FDE market with public HRSA UDS data, and parking's computer-vision vendors |
| 2 | Q2 | Sports Teams (35), Self-Storage Operators (35), Psychiatric Hospitals (34), Consumer Goods Wholesalers (34), Ambulance Services (34) | Public sports data for demos, storage revenue management, behavioural-health vendors, the distributor quoting field again, EMS billing |
| 3 | Q3 | Electronic Component Distributors (33, web), Air Cargo Carriers (34), Heavy Equipment Dealers (32), Plastic Molders (34), Specialty Hospitals (32) | BOM quoting, digital cargo booking, equipment pricing, job-shop quote automation |
| 4 | Q4 | Medical Supply Distributors (32, web), Residential Treatment Centers (32, web), Aircraft & Railcar Lessors (34), Biologics Manufacturers (33), LTL Carriers (29, web) | Web-checked near misses with real pain (2026 DME bidding, 42 CFR Part 2, NMFC reclass) plus lease-document and GxP work |
| 5 | Q5 | Metal Service Centers (32, web), PCB Fabricators (34), Manufacturers' Representatives (33, web), Aviation Parts Distributors (31, web), Fuel Distributors (32) | More of the distributor and job-shop fields; reps are fast, listed buyers (MANA); 8130-3 traceability paperwork |
| 6 | Q6 | Auto Salvage Yards (34), Thrift & Resale Stores (34), Transmission Operators (31), Nuclear Power Plants (34), Cosmetics Manufacturers (34) | Salvage auctions, resale pricing, transmission interconnection; nuclear sits late for citizenship limits |
| 7 | Q7 | Weight-Loss Centers (34), Dental Laboratories (34), Passenger Airlines (33), Charter Air Operators (34), Auto Glass Shops (34) | Reserves that move up when a Q1–Q6 pick fails its web check |

After Q7 the sector batches run in order of their mean placement score, highest first: wholesale, retail, education and specialty services lead, and the low-scoring plant, mill, mining and utility batches come last. Waste batch 9b closes with its three built industries; its three unbuilt ones moved to batch 9c in the tail.

**Owner rules added the same day.** No gambling and no alcohol: casinos, racetracks, racing stables (their purses come from wagering), beverage-alcohol distributors, liquor stores, bars and taverns, breweries, wineries and distilleries are skipped (status `blocked`, batch X), joining gambling-operators. Government goes last: the 16 public-administration industries plus courts, community colleges, transit agencies, airport and toll-road operators, and firms whose customer is an agency (highway contractors, school-bus contractors, youth group homes paid by state child-welfare agencies, avionics and defense electronics, shipyards, waste-to-energy plants) sit in batches G1–G4 after every other sector. That took beverage-alcohol distributors, courts and highway contractors out of Q5; three reserves moved up and Q7 took three new ones.

At five a day the Q batches take seven nights (2026-10-28 to 2026-11-03) and roughly 35–50% of a weekly quota per week. Re-decide after Q7 whether the tail is worth the quota.
