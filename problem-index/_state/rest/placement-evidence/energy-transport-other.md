## renewable-power-producers
scores: E P M F R = 2 5 5 3 4
employers: Nira Energy (Forward Deployed Engineer, https://job-boards.greenhouse.io/niraenergy - board fetched today lists only CPTO and sales roles, FDE NOT open now; FDE role still on builtin.com/job/forward-deployed-engineer/7465958, stale); Pearl Street Technologies / Enverus (Full-Stack/Software Data Engineer, Interconnect + SUGAR, https://jobs.jobvite.com/enverus/job/oCzOAfwj - seen in search, open status not confirmed, some sibling postings marked closed); RatedPower (Software Data Engineer, https://jobs.elementalimpact.com/companies/ratedpower/jobs/68718574-software-data-engineer-2669 - not confirmed open)
pain: Interconnection queue still holds ~2,061 GW of generation/storage at end of 2025 and studies keep taking longer, so developers pay for queue analytics and study tooling (https://emp.lbl.gov/queued-2026-edition-characteristics)
mvp: Queue-position and withdrawal-risk scorer for a developer's candidate POIs using the LBNL Queued Up dataset plus ISO public queue files and EIA-860.
pitch: Founders/CEOs and VP Development of small-mid solar/storage developers; heads of interconnection at the startups above via ACP / SEIA / RE+ exhibitor and member lists, ISO stakeholder-meeting attendee lists, climate-tech job boards
note: Strongest pain/data pairing in the batch but the only FDE I found (Nira) is closed on its own board, so E capped at 2.

## electric-utilities
scores: E P M F R = 4 4 4 3 4
employers: Gridsight (Founding Forward Deployed Engineer, https://ats.rippling.com/gridsight/jobs/179f961a-7a10-4e62-bf84-a534eec28db4 - fetched, Apply button live; FDE); E Source (Forward Deployed AI/ML Engineer IV, https://www.builtinseattle.com/job/forward-deployed-ai-ml-engineer-iv/11195781 - seen in search results only; FDE); MLabs (Forward Deployed Software Engineer, Utilities, https://www.jointaro.com/jobs/mlabs/forward-deployed-software-engineer-utilities-7312ee1a - aggregator, not confirmed on company page; FDE); Nira Energy (careers page https://job-boards.greenhouse.io/niraenergy, only sales roles for utilities now, not counted)
pain: Utilities face load growth and must speed customer/large-load interconnection and use existing grid capacity, which is what Gridsight and E Source sell into (https://ats.rippling.com/gridsight/jobs/179f961a-7a10-4e62-bf84-a534eec28db4)
mvp: Large-load/hosting-capacity screening dashboard from utility hosting-capacity map downloads plus EIA-861 and EIA-860 data, or an LLM tariff/interconnection-doc Q&A on public PUC filings.
pitch: Pitch the vendors' founders/heads of engineering (Gridsight, E Source) and, for utility side, grid-planning or interconnection managers at co-ops/munis via EEI, APPA, NRECA member directories and DistribuTECH exhibitor list
note: E 4 relies on two aggregator-only roles; only Gridsight verified on ATS page. Utility buyers themselves are slow, so F scored on vendor founders.

## aircraft-mro-shops
scores: E P M F R = 3 5 3 4 4
employers: Zymbly (Forward Deployed Engineer, https://www.ycombinator.com/companies/zymbly/jobs/ueWPYCh-forward-deployed-engineer - page live with Apply button, SF/London; FDE); Soji AI (Forward Deployed Engineer (Aviation), https://join.com/companies/soji/16741622-forward-deployed-engineer-aviation - open, published 2026-03-21, Hamburg hybrid; FDE); Apt (Aviation Maintenance Software Engineer, https://www.tryapt.ai/careers/aviation-maintenance-software-engineer - page loaded but is a career-test page, role not confirmed)
pain: North America short ~17,000 aircraft mechanics, heavy checks take 45 days longer than pre-COVID, so shops pay to save technician hours on records and planning (https://www.bcg.com/publications/2026/older-aircraft-too-few-technicians-the-aerospace-fix)
mvp: Work-card and logbook-entry extraction/discrepancy checker using FAA Airworthiness Directives and FAA Service Difficulty Reports as reference data plus synthetic scanned work cards (real shop records are client data).
pitch: Directors of Maintenance / Quality Managers / owners of Part 145 repair stations via the FAA public repair station directory, MRO Americas and AEA exhibitor lists; Zymbly/Soji founders directly
note: Two verified FDE roles only, so E 3; incumbents (AMOS, Veryon, Rusada) had no roles found in search.

## ltl-carriers
scores: E P M F R = 2 4 3 3 3
employers: project44 (Software Engineer roles touching LTL visibility, https://job-boards.greenhouse.io/project44/jobs/7379339 - seen in search, open status not confirmed, Amsterdam/Bangalore); Pallet (Software Engineer, Agent Delivery, SF, https://job-boards.greenhouse.io/pallet/jobs/4978414007 - board fetched today lists it open, logistics-wide not LTL-specific)
pain: NMFTA Docket 2025-1 moved ~30% of LTL freight to density-based classing (effective 2025-07-19) with Docket 2026-1 following, driving reclass disputes and carrier dimensioning (https://www.cahoot.ai/nmfc-changes-ltl-freight/)
mvp: Freight-class and reclass-dispute estimator for a shipper/broker using the NMFC density bands from the NMFTA docket summaries and synthetic BOLs.
pitch: Pricing/revenue-quality managers at regional LTL carriers and 3PL/broker ops heads via TIA, Mid-America Trucking Show and Pricing/NMFTA conference exhibitor lists
note: Found no LTL-specific vendor with an open engineering role, so E 2.

## ocean-shipping-carriers
scores: E P M F R = 3 4 3 4 4
employers: Reform (Forward Deployed Engineer / Founding FDE, https://www.workatastartup.com/jobs/82937 - page loaded, open status not confirmed; FDE); Pallet (Software Engineer, Agent Delivery, https://job-boards.greenhouse.io/pallet/jobs/4978414007 - open on board today); Flexport (Forward Deployed Engineer, Supply Chain Solutions, https://jobera.com/job/flexport-forward-deployed-engineer-supply-chain-solutions-c5686bdf/ - aggregator, not confirmed); Zencargo (FDE, https://jobs.hvcapital.com/companies/zencargo/jobs/87710849-forward-deployed-engineer - fetched, CLOSED, not counted)
pain: Forwarders still do quoting, shipment creation and customs-clearance filing by inbox and spreadsheet, which YC-backed Reform and others are being funded to automate (https://ycombinator.com/companies/reform)
mvp: B/L and commercial-invoice extraction to a booking draft, using synthetic/sample bills of lading and ~public US import manifest data.
pitch: Founders and ops heads of small NVOCCs/forwarders via FMC licensed-OTI list, FIATA/regional forwarder association lists, YC directory for the startups
note: E 3 because only Pallet confirmed open and Reform unconfirmed; many FDE-heavy startups here but several postings closed.

## equipment-rental-companies
scores: E P M F R = 2 3 3 4 3
employers: Renterra (Senior Software Engineer, AI & Data, https://seedtable.com/jobs/19518 - aggregator, listed 2026-07-23; own careers page https://getrenterra.com/careers says team full, role not confirmed); EquipmentShare (software engineer roles, https://www.ycombinator.com/companies/equipmentshare/jobs/nRmVwyu-mid-level-software-engineer - old, likely stale)
pain: Rental operators pay for utilization, telematics and pricing software; Renterra raised a $9M Series A in Jan 2026 to build it (https://getrenterra.com/blog-posts/renterra-raises-9m-series-a-to-power-the-future-of-equipment-rental)
mvp: Fleet-utilization and rate-benchmark dashboard on synthetic telematics plus public auction/price listings (no good public rental telematics set).
pitch: Owner-operators and GMs of independent rental yards via ARA / The Rental Show exhibitor lists and state rental associations
note: No confirmed open engineering role, so E 2.

## heavy-civil-contractors
scores: E P M F R = 3 4 5 3 4
employers: Rudus (Forward Deployed Engineer, https://www.ycombinator.com/companies/rudus/jobs/62WqaHp-forward-deployed-engineer - fetched, active, SF/NYC; FDE, concrete takeoff not heavy civil); Trunk Tools (Forward Deployed Engineer / Forward Deployed Expert, https://wellfound.com/jobs/4762958-forward-deployed-engineer - aggregator, not confirmed; FDE); Edgevanta (heavy civil estimating AI, careers page not found, role not confirmed)
pain: Heavy civil estimating still runs on spreadsheets and experience, and estimators are asked to bid more with tighter margins (https://www.tcli.com/blog/ai-heavy-civil-estimating)
mvp: Bid-tab price-benchmarking and unit-price outlier checker from state DOT bid tabulations (e.g. TxDOT, Caltrans, WSDOT public tabs).
pitch: Chief estimators / owners of regional heavy civil firms and the founders at Edgevanta/Rudus via AGC and state heavy-highway association member lists, ConExpo exhibitor list
note: Strong data (public bid tabs) but only one verified open FDE role, and it is adjacent.

## highway-contractors
scores: E P M F R = 2 4 5 3 4
employers: B2W Software (estimating/DOT bidding vendor, no role seen, careers page not checked); TCLI (HeavyBid-adjacent vendor, no role seen); Rudus (FDE, https://www.ycombinator.com/companies/rudus/jobs/62WqaHp-forward-deployed-engineer - concrete, adjacent only)
pain: Contractors need DOT item databases and bid-tab analysis to price lettings faster (https://www.forconstructionpros.com/home/article/12265123/specialized-software-delivers-automation-advantages-for-dot-bidding)
mvp: Pre-letting competitor and unit-price analyzer from state DOT bid tabulations and published proposal item lists.
pitch: Estimating managers/presidents of paving and highway contractors via ARTBA, state road-builder association member lists and DOT prequalified-bidder lists
note: No highway-specific vendor with a confirmed open role found, so E 2; overlaps heavy-civil.

## franchisors
scores: E P M F R = 2 3 3 3 4
employers: Square (Staff Software Engineer, Franchise Suite, https://builtin.com/job/staff-software-engineer-franchise-suite/3946481 - seen in search, page returned 403, open status not confirmed); FranConnect (careers page, role not confirmed); Franchisely (careers page, role not confirmed)
pain: Franchisors must file annual FDDs in 13 registration states and any Item 19 earnings claim needs substantiation, mostly done by law firms by hand (https://www.franchiselawsolutions.com/learn/grow-your-franchise/fdd-registration-guide)
mvp: FDD Item 19/Item 20 extractor and cross-brand comparison using publicly filed FDDs from state portals (e.g. Wisconsin, Minnesota, California DFPI).
pitch: Franchise development directors / COOs of emerging brands via IFA exhibitor and speaker lists, state franchise registries, FranNet consultant network
note: No confirmed open engineering roles, so E 2.

## grantmaking-foundations
scores: E P M F R = 2 3 5 2 4
employers: Temelio (Founding Engineer, seen in an earlier search snippet at $120-180K, but follow-up found no open roles; https://www.trytemelio.com/about, not confirmed); Survival and Flourishing Corp (Full-Stack Software Engineer, grant evaluation, listed on https://www.lesswrong.com/posts/r5iMQwJu4nZpKejnn/job-openings-swe-pm-and-grants-coordinator-to-help-improve, not confirmed current); JustFund (no openings captured)
pain: Candid found billions in foundation grants missing from 990-PF/990 XML data, and Treasury lists expenditure responsibility among burden-reduction items (https://www.aspeninstitute.org/wp-content/uploads/2025/11/IRS-Comments-2025-Form-990-Series.pdf)
mvp: Grantee due-diligence and grant-landscape tool built on IRS 990-PF / 990 XML e-file data.
pitch: Program officers, grants managers and COOs at small-mid family foundations via Candid/Foundation Directory, Council on Foundations and regional grantmaker association member lists
note: E 2 and F 2 (foundation staff and boards are slow, small software budgets).

## colleges-and-universities
scores: E P M F R = 3 4 4 2 4
employers: Ellucian (Software Engineer II, https://www.edtech.com/jobs/software-engineer-ii-8086 - dated 2026-05; Software Engineer I entry-level, https://www.edtech.com/jobs/software-engineer-i-entry-level-puebla-mexico-57473 - dated 2026-10-14; aggregator, not on Ellucian ATS); CollegeVine (Forward Deployed Strategist / Engineer (AI), https://careers.silversmith.com/companies/collegevine/jobs/59743146-forward-deployed-strategist-engineer-ai - page shows Apply but "6+ months ago"; FDE); Memorang (Forward-Deployed Engineer, https://memorang.com/careers/forward-deployed-engineer - mostly corporate learning)
pain: Enrollment volatility is now "the new normal" and colleges are cutting budgets, so yield, retention and admin-cost tools get purchased (https://www.fortune.com/2026/06/20/college-enrollment-cliff-great-recession-university-budget-crisis/)
mvp: Student-retention/yield risk model on IPEDS and College Scorecard public data, plus a synthetic-record advising copilot.
pitch: Directors of enrollment management / institutional research / CIOs at small private colleges via EDUCAUSE, AACRAO exhibitor lists; vendor founders (CollegeVine) directly
note: F 2 because universities are committee/procurement driven; pitching an edtech vendor would be faster.

## appliance-repair-companies
scores: E P M F R = 1 3 3 5 3
employers: none found with an open engineering role; vendors seen: ApplianceOps (small product, https://www.producthunt.com/products/applianceops), ServiceBench (manufacturer-side warranty claims, https://app.dealroom.co/companies/servicebench), Fieldcode - no careers pages checked
pain: Shops juggle home-warranty split billing and claims by hand; the niche tool ApplianceOps exists mainly for this (https://www.producthunt.com/products/applianceops)
mvp: Warranty-claim packet generator (model/serial decode, parts lookup, claim form) on synthetic jobs and public manufacturer manuals.
pitch: Owner-operators of local repair shops and ServiceBench/home-warranty ops managers via Google Maps/Yelp business listings, regional appliance-service associations (~APSA)
note: Easiest buyer (owner-operators) but almost no software vendors hiring, so little employer path.

## mortgage-lenders
scores: E P M F R = 4 4 4 3 4
employers: Ocrolus (Mortgage Forward Deployed Engineer, Remote US, https://job-boards.greenhouse.io/ocrolusinc/jobs/5839067004 - board fetched today, listed; FDE); Valon (Forward Deployed Engineer, https://jobs.alleycorp.com/companies/valon-technologies/jobs/55569213-forward-deployed-engineer - aggregator, the greenhouse link returned 404, not confirmed; FDE); Addy AI (Forward Deployed AI Engineer, https://jobs.basisset.com/companies/addy-ai-2-0c788979-335e-4f72-93d3-fa13430491a4/jobs/78803553-forward-deployed-ai-engineer - posted 2026-05-14, not confirmed current; FDE); Saaf AI (Forward-Deployed AI Engineer, https://remotejobs.org/remote-jobs/forward-deployed-ai-engineer-saaf-finance - not confirmed; FDE)
pain: Inconsistent fee naming drives redisclosures; fee-related cures affect over 30% of mortgage loans, and CFPB opened an RFI on TRID in July 2026 (https://nationalmortgageprofessional.com/tag/trid-0)
mvp: Loan Estimate vs Closing Disclosure tolerance/fee-cure checker on synthetic disclosures with HMDA public LAR data for benchmarking.
pitch: COOs / heads of operations or compliance at independent mortgage banks and the founders/heads of FDE at the vendors above via MBA / state MBA exhibitor lists, NMLS Consumer Access, HousingWire Connect speakers
note: Best employer evidence in the batch (only Ocrolus verified on its ATS, rest aggregator); E 4 is borderline.

## title-and-settlement-offices
scores: E P M F R = 3 4 3 4 4
employers: Qualia (Senior Software Engineer I; Senior Software Engineer, Resware, https://www.qualia.com/careers - page fetched today, those roles listed; no Solutions Engineer roles); Propy (Applied AI Engineer, title/escrow AI, https://www.housingwire.com/articles/propy-leans-on-acquisitions-ai-to-modernize-title/ - article only, role not confirmed)
pain: Title/escrow offices are adopting AI closing agents (Propy Avery, HomeLight Eva) because closing coordination and wire handling are manual and high-stakes (https://news.inman.com/2026/06/04/homelight-eva-escrow/)
mvp: Title commitment / closing-package checker (exceptions, payoff, wire-instruction mismatch) on synthetic closing files plus county recorder public documents.
pitch: Owners of independent title agencies and escrow officers; Qualia/Propy product heads via ALTA member directory, state land title association lists, ALTA ONE exhibitor list
note: Real vendors hiring engineers (Qualia), but not FDE roles; needs synthetic data for real closing files.
