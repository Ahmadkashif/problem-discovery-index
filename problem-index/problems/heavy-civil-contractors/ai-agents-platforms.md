# AI Agents & Platform Opportunities — Heavy Civil Contractors

**Industry:** [[heavy-civil-contractors|Heavy Civil Contractors]]

---

## 1. Bid-Tab Unit-Price Checker
#ai-agent #bayesian-inference #linear-regression #hypothesis-testing #large-language-models #revenue-impact #quick-win

**Concept:** An agent that watches the lettings a contractor plans to bid. It pulls the past bid results of the Corps districts, port authorities, transit agencies and railroad owners it bids for, plus DOT tabulations filtered to marine, structures and rail items, maps each owner's item codes to a shared item taxonomy, and checks the estimator's draft bid schedule line by line against the market. It flags items priced outside the market's range for that quantity, region and date, items that look unbalanced, and items where the firm's own past bids sit consistently above the winners. After the letting it ingests the new tab, records who bid what, and updates each competitor's pattern. This is the owner's MVP: Corps dredging results plus one state DOT's structures, marine and rail items in, a ranked list of outlier items and a low-bid range out, demo-able in two weeks.
**Inputs:** Corps Navigation Data Center dredging bid abstracts and awards (bidder totals; line items where districts post full abstracts), SAM.gov awards, transit, port and railroad-owner bid results, DOT tabulations for non-highway items, published engineer's estimates, the contractor's draft bid schedule exported from HeavyBid, B2W or a spreadsheet.
**Outputs / Actions:** Outlier and unbalance flags per item with the comparable lettings shown; low-bid distribution; competitor watch list per letting; a post-letting debrief of where the firm lost and on which items.
**Why now:** Bid tabs are public but locked in PDFs and inconsistent item codes, and language models now parse and map them cheaply. The Corps' 125% award ceiling and the IIJA funding lapse on 1 October 2026 make each letting's price discipline matter more.
**Market:** Chief estimators at regional heavy civil, marine, dredging and rail contractors. DOT road-and-bridge unit-price intelligence belongs to the queued highway contractors build, which links here for non-highway owners. On the DOT side, Oman Systems' Bid Tabs Professional is the incumbent data product several DOTs use, and Edgevanta pitches a "Bid Tabs Agent" over 20+ states (both via search summary; no Edgevanta engineering role confirmed on 2026-10-24). This niche is mapped as [[niches/heavy-civil-contractors/public-bid-tab-unit-price-intelligence/profile|Public Bid Tab & Unit-Price Intelligence]].

---

## 2. Heavy Civil Estimating Copilot
#ai-agent #large-language-models #object-detection #cnns #gradient-boosting #tacit-knowledge-ml #workflow-orchestration

**Concept:** An agent that sits inside the estimating system during bid week. It reads the plans, specs and geotechnical report and drafts quantities for the items it can measure: concrete, sheet pile, stone, track, dredge prisms. It extracts the job conditions that move production rates, proposes a crew, spread and rate per item from the firm's own field actuals, and logs every override with a reason. It also reads addenda as they arrive and flags what changed in the bid schedule.
**Inputs:** Bid documents and addenda, geotechnical reports, the firm's estimate history and crew library, cost-code actuals from the field system, the bid-tab market prior from the checker above.
**Outputs / Actions:** Drafted quantities with source sheets; suggested rates with intervals and comparable jobs; an addendum change log; an override ledger that becomes the training set.
**Why now:** Vision-language models read civil drawings well enough to draft takeoffs, and the estimating systems (HCSS, Trimble's B2W, InEight) expose data to integrate with. Hiring checked on 2026-10-24: Rudus, a two-person YC company doing AI takeoff for structural and site concrete with exports to HeavyBid and B2W, had a Forward Deployed Engineer ($140K–$160K, on site with estimators), a Founding Engineer and a computer vision research scientist open. Trunk Tools, whose TrunkBid levels subcontractor bids, had a Forward Deployed Engineer, a Sr. II ML Engineer and integrations and platform engineers open on its own careers page, though its named customers are mostly large commercial GCs (search summary). HCSS had only DevOps and design-systems roles.
**Market:** Estimating departments at the ~734 firms with 20+ employees in the code (565 + 110 + 59 by size band, Census SUSB 2022) and at highway and utility contractors. The tacit core is the production-rate model in [[problems/heavy-civil-contractors/ml-opportunity|ML Opportunities]] entry 1.

---

## 3. Notice, Change and Delay Agent
#ai-agent #large-language-models #bert #graph-theory #compliance #workflow-orchestration

**Concept:** An agent that reads the field record every night (foremen's voice diaries, daily reports, RFIs, survey notes, owner correspondence). It detects events that start a contractual clock, tells the project manager which clause applies and when notice is due, drafts the notice, and drafts a time impact fragnet in the owner's required schedule format. It then tracks the owner's response and the cost records for the eventual change order.
**Inputs:** Contract and schedule spec, P6 schedules, daily reports and diaries, RFIs, correspondence, cost-code actuals, survey data.
**Outputs / Actions:** Notice deadlines and drafts; TIA fragnets; a change and claim register with evidence linked; a weekly entitlement summary.
**Why now:** Language models classify field text by event type and draft letters, and owners' specs (the Corps' 10-day justification rule, AACE 52R-06 TIAs) are explicit enough to encode. Trunk Tools sells TrunkChange into this workflow. Document Crunch, which reviews contract risk, listed no open roles on 2026-10-24.
**Market:** Project managers and schedulers at heavy civil and marine contractors. It reduces the work that ends up at [[niches/general-contractors/construction-claims-forensics/profile|Construction Claims & Schedule Forensics]], whose privilege-bound practices are not a buyer for it.

---

## 4. Fleet Utilisation and Equipment Cost-Rate Agent
#ai-agent #survival-analysis #k-means-clustering #optimization-fundamentals #data-integration #automation

**Concept:** An agent that pulls hours, fuel and location from every OEM's AEMP 2.0 feed and from aftermarket trackers. It infers work versus idle time, posts equipment hours to job cost codes so foremen stop typing them, forecasts when each machine will free up, and recommends moves, rentals and disposals. Each quarter it recomputes the internal ownership and operating rates the estimators charge per hour.
**Inputs:** OEM telematics feeds, trackers, job schedules, field equipment entries, rental invoices, maintenance and fuel records, the estimating system's equipment rate table.
**Outputs / Actions:** Equipment hours posted by cost code; idle alerts by job; a weekly redeployment and rental plan; updated hourly rates for estimating.
**Why now:** Mixed-fleet feeds have standardised enough to pull without new hardware, and equipment is the largest owned asset on a heavy civil balance sheet. Tenna, a construction equipment management platform, had an engineering manager, principal architect and principal data engineer open on 2026-10-24. Bedrock Robotics and Teleo, which automate the machines themselves, had autonomy, ML and fleet-platform software roles open; they are adjacent, not competitors for the fleet record.
**Market:** Equipment managers at mid-size and large heavy civil firms. The renter's side of the same data belongs to the queued equipment rental build, and lender-side equipment values are at [[niches/sales-finance-companies/equipment-valuation-guides/profile|Equipment Valuation & Residual Data Providers]].
