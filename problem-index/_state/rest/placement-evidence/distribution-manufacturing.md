## building-material-dealers
scores: E P M F R = 3 4 4 4 4
employers: Avent (Founding Forward Deployed Engineer, Founding Engineer, https://www.ycombinator.com/companies/avent/jobs; FDE); Mercura (Forward Deployed Engineer, AI/LLM Engineer, https://www.ycombinator.com/companies/mercura/jobs; FDE; Munich); BuildVision AI / Paradigm Estimate / Beam AI (takeoff vendors seen in search, careers page not checked, role not confirmed)
pain: Takeoff and quoting from plan sets is manual estimator work and construction labour is short (ABC: ~349k workers needed in 2026) (https://distributionstrategy.com/2026/03/distributors-move-upstream-and-invest-heavily-to-rebuild-skilled-labor-pipeline/)
mvp: Read a public residential plan set PDF (county permit-portal sample plans) and output a priced lumber/sheet-goods list against a synthetic dealer price file.
pitch: Owner, GM, outside sales manager, estimating manager via NLBMDA / LBM Journal dealer lists and ProDealer/ LBM expo exhibitor lists
note: No lumber-specific vendor with a confirmed open engineering role; generic distributor-AI startups (Avent, Mercura) are the real employers.

## electrical-distributors
scores: E P M F R = 4 5 4 4 5
employers: Avent (Founding Forward Deployed Engineer, https://www.ycombinator.com/companies/avent/jobs; FDE); Mercura (Forward Deployed Engineer, Staff Engineer, https://www.ycombinator.com/companies/mercura/jobs; FDE; Munich); Comena (Forward Deployed Engineer, Fullstack Engineer, https://www.ycombinator.com/companies/comena/jobs; FDE; Munich); Distro (YC page shows no jobs; Wellfound listed a Tech Lead, not confirmed)
pain: Quote and order entry by hand, plus takeoffs from project documents; NAED itself publishes a business case for AI here (https://blog.naed.org/the-business-case-for-ai-in-electrical-distribution)
mvp: Build an RFQ email/PDF to line-item quote agent using manufacturer catalog/datasheet PDFs (public) and a synthetic price book and bid-list emails.
pitch: Owner/president, inside sales manager, VP operations via NAED member directory and NAED/ISA exhibitor lists (https://blog.naed.org/new-member-spotlight-distro shows how vendors get listed)
note: Two of the three vendors are Munich-based; US-only candidate gets Avent.

## industrial-distributors
scores: E P M F R = 4 5 4 4 4
employers: Avent (Founding Forward Deployed Engineer, https://www.ycombinator.com/companies/avent/jobs; FDE); Comena (Forward Deployed Engineer, https://www.ycombinator.com/companies/comena/jobs; FDE; Munich); Mercura (FDE, https://www.ycombinator.com/companies/mercura/jobs; FDE); Hexa (YC launch page seen, YC jobs page says no jobs: https://www.ycombinator.com/launches/Qfd-hexa-autonomous-operations-for-industrial-distributors)
pain: Inbound RFQ and PO email triage into the ERP is manual and slow (https://blog.naed.org/the-business-case-for-ai-in-electrical-distribution)
mvp: Open-source style RFQ-to-draft-quote agent over a public MRO catalog scrape (e.g. manufacturer catalogue PDFs) with synthetic customer emails.
pitch: President, VP sales, inside sales manager via IDN / NIAA / ISA / Industrial Supply Association member and show exhibitor lists
note: Most crowded niche (Avent, Comena, Mercura, Hexa, Augment), so competition for pilots is high but vendor demand for engineers is real.

## electronic-component-distributors
scores: E P M F R = 2 4 4 4 3
employers: Cassidy (email-to-quote for electronics RFQs, careers not checked, role not confirmed); Boardera (PCB quoting, careers not checked, role not confirmed); Rocket EMS (Quote/Cost Analyst only, ops role, https://job-boards.greenhouse.io/rocketems/jobs/4184893009)
pain: Hours spent turning RFQ emails and BOM attachments into quotes (https://www.cassidyai.com/solutions/ai-inside-sales-quote-agent)
mvp: BOM-to-quote tool using Octopart/DigiKey/Mouser public APIs and manufacturer datasheets with synthetic RFQ emails.
pitch: Owner, VP sales, quoting manager at independent brokers/franchised distributors via ECIA member list and ECSN/ERAI conference lists
note: Vendors exist but no open engineering role seen on a page today.

## metal-service-centers
scores: E P M F R = 2 4 3 4 4
employers: Nox Metals (service center itself, SDR owning inbound RFQs; not engineering, https://startup.jobs/sales-development-representative-sdr-nox-metals-8027208); Uptool (AI quoting for shops, careers not found, role not confirmed); Forgepoint (AI RFQ-to-quote, role not confirmed, https://sovereignmagazine.com/article/ai-quoting-software-forgepoint); Avent (generic, https://www.ycombinator.com/companies/avent/jobs; FDE)
pain: RFQs arrive by email and need cut-to-size price and lead time quickly; a public take-home even uses this exact task (https://kodiakllc.notion.site/Take-Home-Screen-ec3477d8d6ec49dbbf123ebf407b4d36)
mvp: RFQ email to structured quote for plate/bar using public mill spec sheets (ASTM/ASM grades) and synthetic price list and inventory.
pitch: GM, inside sales manager, owner via MSCI member directory and MSCI/FABTECH exhibitor lists
note: Only Avent has a confirmed role and it is not metals-specific.

## plumbing-and-hvac-distributors
scores: E P M F R = 3 4 4 4 4
employers: Mercura (FDE, AI/LLM Engineer, https://www.ycombinator.com/companies/mercura/jobs; FDE; Munich, targets HVAC/electrical/plumbing); Avent (https://www.ycombinator.com/companies/avent/jobs; FDE); Comena (https://www.ycombinator.com/companies/comena/jobs; FDE); Augment (Augie at Johnstone Supply; FDE posting seen is closed: https://careers.redpoint.com/companies/augment-2-1ddbf4c0-55ff-4e35-bef9-20d217893f99/jobs/60350414-forward-deployed-engineer); Rebar (HVAC estimating, $14M Series A, jobs not checked)
pain: Distributors automating sales order entry in Epicor Eclipse, takeoffs from mechanical drawings (https://www.phcppros.com/articles/23844-johnstone-supply-heartland-group-partners-with-augment-to-accelerate-quote-to-cash-with-ai)
mvp: Count equipment tags on public mechanical drawing sets and produce an equipment quote using manufacturer submittal PDFs and a synthetic price file.
pitch: Branch manager, owner, estimating manager via HARDI / PHCP Pros / NAW member and show lists
note: Employers are mostly the same generic vendors as the other distribution niches.

## manufacturers-reps
scores: E P M F R = 2 3 3 5 5
employers: Parspec (Ashby board https://jobs.ashbyhq.com/parspec showed Account Executive, Manufacturer & Rep Channel; engineering hub in Bangalore; no engineering role confirmed); Repfabric (CRM for reps, careers not checked); Avent (asks for IMR intros, https://www.ycombinator.com/companies/avent/jobs; FDE)
pain: Reps run quoting, RFQ close-out and commissions in spreadsheets; Parspec launched an AI sales-management platform for rep agencies in July 2026 (https://inside.lighting/press/26-q3/parspec-launches-sales-management-ai-native-platform-rfq-close-out-manufacturer-rep-agencies)
mvp: Commission statement reconciler that parses sample PDF commission reports against synthetic orders and rate tables.
pitch: Agency principal/owner via MANA and ERA/Lighting rep directories and Lightfair exhibitor lists
note: Tiny agency budgets (P3), but owners decide in days and are very listed.

## chemical-distributors
scores: E P M F R = 2 3 3 3 4
employers: Datacor (incumbent ERP with AI order entry, no role checked); Benchmark Gensuite (SDS AI extraction, role not confirmed); Avent (generic, https://www.ycombinator.com/companies/avent/jobs; FDE)
pain: Distributors must track DOT hazmat, EPA, OSHA paperwork and handle SDS; incumbents already ship AI order entry (https://www.airdev.co/erp/datacor)
mvp: SDS PDF extractor (GHS sections 1-16) over public manufacturer SDS PDFs, plus a hazmat shipping-doc checker.
pitch: Compliance manager, ops director, owner via NACD member directory and NACD/ChemExpo exhibitor lists
note: No chemical-specific vendor with an open engineering role found.

## aviation-parts-distributors
scores: E P M F R = 2 4 3 4 3
employers: ERP.Aero (iRFQ AI engine, careers not checked, role not confirmed); ePlane AI (email agent, Pentagon 2000 partner, role not confirmed, https://eplaneai.com/solutions/email); Ambry Hill VistaQuote (role not confirmed)
pain: Missing certs/trace documents sink quotes; buyers require unbroken traceability (https://erp.aero/articles/certification-trace-doc-readiness-at-quote-time)
mvp: Cert-packet checker that reads synthetic 8130-3/EASA Form 1 PDFs against FAA AC 00-56B requirements (https://www.faa.gov/documentLibrary/media/Advisory_Circular/AC_00-56B.pdf).
pitch: Sales/quality manager, owner via ASA member list and Aviation Week MRO / AIX exhibitor lists
note: Real tools exist, but no open engineering role confirmed on a page today.

## consumer-products-makers
scores: E P M F R = 3 5 3 3 3
employers: Confido (Forward Deployed Engineer, Staff Software Engineer, Senior Software Engineer, Applied AI/ML Engineer, https://www.ycombinator.com/companies/confido/jobs; FDE; NYC); Vividly, Revya AI, Glimpse, Adesso (deduction/TPM vendors, careers not checked, role not confirmed)
pain: Deductions run an estimated 3-7% of gross revenue and a meaningful share is invalid; figures are vendor-sourced (https://endlesscommerce.com/playbook/deduction-management-for-cpg-brands)
mvp: Deduction-to-invoice matcher over synthetic retailer remittance and deduction code files (Walmart/Kroger code lists public).
pitch: Finance/AR lead, head of sales ops at emerging brands via Expo West / Newtopia exhibitor lists and Product Hunt/ startup directories
note: Only one vendor confirmed, but with many open engineering roles.

## tool-die-and-mold-shops
scores: E P M F R = 2 3 3 5 4
employers: Uptool (careers not found, role not confirmed); ZW Z-FASTQ (role not confirmed); CADDi (role not confirmed); CloudNC (Quote Agent planned late 2026, careers not checked, https://www.robotics247.com/article/imts-2026-cloudnc-raises-20m-to-expand-ai-tools-for-precision-machining)
pain: Quoting a mold or die from CAD/drawings takes senior estimator hours (https://moldmakingtechnology.com/products/ai-powered-quoting-system-improves-moldmaking-estimation-process)
mvp: Feature extractor and cost estimator from public CAD (ABC/Fusion 360 Gallery datasets) with synthetic historic quotes.
pitch: Owner/estimator via AMBA and NTMA member directories and Amerimold / IMTS exhibitor lists
note: Owner-operators are fast, but no open engineering role seen.

## aerospace-parts-suppliers
scores: E P M F R = 3 4 4 4 4
employers: SalesPatriot (Forward Deployed Engineer, Lead FDE, Full Stack Engineer, https://www.ycombinator.com/companies/salespatriot/jobs; FDE); GroundControl (YC page shows only an Account Executive, no engineering role: https://www.ycombinator.com/companies/groundcontrol); Poka Labs (Full Stack/AI Engineer, listing on Vaia, not confirmed open)
pain: AS9102 first article inspection reports are manual; GroundControl reports ~1,000 reports a month on its platform (https://www.ycombinator.com/companies/groundcontrol)
mvp: Auto-balloon a drawing PDF and fill an AS9102 Form 1-3 from public sample drawings and the AS9102 form template.
pitch: Quality manager, VP ops, owner of small suppliers via AeroSpace Alliance / state aerospace association member lists and Farnborough/AeroDef exhibitor lists
note: Only one vendor with confirmed engineering roles.

## defense-systems-manufacturers
scores: E P M F R = 4 3 4 2 3
employers: Anduril (Forward Deployed Engineer, Air Defense, Costa Mesa, https://job-boards.greenhouse.io/andurilindustries/jobs/5057206007; FDE); Vannevar Labs (Forward Deployed Engineer - Oahu, TS/SCI, https://job-boards.greenhouse.io/vannevarlabs/jobs/5082044007; FDE); SalesPatriot (FDE, Lead FDE, https://www.ycombinator.com/companies/salespatriot/jobs; FDE); Sitrep (greenhouse board seen with 44 openings, no FDE role confirmed, https://job-boards.greenhouse.io/sitrepsllc/jobs/4093418009)
pain: CMMC third-party Level 2 was suspended July 2026 but NIST 800-171 and DFARS 7012 still apply to suppliers (https://www.clarkhill.com/news-events/news/dow-pauses-cmmc-phase-2-defense-contractors/)
mvp: SAM.gov/USAspending award-and-solicitation matching tool, or an SSP/POA&M generator from NIST 800-171 text.
pitch: Hiring managers and engineering leads (company is the target, not a buyer); contracting is slow for real sales via DSIAC / startup directories and event speaker lists
note: Great employer count, but clearance and on-site limits apply; pitching a buyer is slow (F2).

## franchised-car-dealers
scores: E P M F R = 3 5 3 3 4
employers: BizzyCar (Engineering Lead, Senior Full Stack Engineer, https://ats.rippling.com/bizzycar/jobs/e0b2c62c-33d1-4785-8b1b-0f59bc189bf7); Toma (Forward-Deployed Software Engineer on Work at a Startup was listed in search, page returned 404 and YC page shows no jobs, not confirmed); Impel (software engineer listed on Hirebase, page blocked, not confirmed); Dealer Copilot (Full-Stack Engineer, listing expires Aug 2026, not confirmed); Sandra AI (YC page: no jobs)
pain: About 19M of 53M inbound dealer service calls were missed opportunities in 2025 (https://carwars.com/main/resources/ai-service-playbook/)
mvp: Service-appointment voice/SMS agent demo on synthetic call transcripts and an open scheduling API mock.
pitch: Fixed ops director, service manager, dealer principal via NADA / state dealer association lists and NADA Show / Digital Dealer exhibitor lists
note: Many AI vendors but few engineering roles confirmed today.
