# Niche Analysis — Aerospace Parts Suppliers

**Parent Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]

## Niche Selection

An aerospace parts supplier sells a part and the proof that it matches the drawing, under delivery pressure set by airframe and engine rate ramps it doesn't control. The eight niches below split the industry by what vendors and internal teams actually compete over: turning scarce castings and forgings into accepted engine parts, proving capacity for the next rate break, assembling first article packages, chasing outside special processors, bidding government spares, approving PMA replacements, quoting from drawings, and turning purchase-order flowdowns into checked requirements. Market sizes are estimates of software, services and the labour those tools would replace in each niche, not of the industry's ~$77.0B in receipts.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Engine Components & Rotating Parts | 🔵 High Market Share | ~$1.2B | Medium | VP Quality, plant GM |
| 2 | Aerostructures & Airframe Detail Parts | 🔵 High Market Share | ~$900M | Medium-low | VP Operations, programme manager |
| 3 | First Article Inspection & AS9102 Packages | 🟠 Low Digitized | ~$400M | Low | Quality manager |
| 4 | Outside Special Processing & Sub-Tier Expediting | 🟠 Low Digitized | ~$500M | Low | Production control manager |
| 5 | Small Shops Bidding Government Spare Parts | 🟣 Underserved Audience | ~$150M | Low-medium | Owner, contracts manager |
| 6 | PMA Parts Developers & Reverse-Engineering Teams | 🟣 Underserved Audience | ~$300M | Medium-low | VP Engineering, PMA programme manager |
| 7 | Drawing-to-Quote for Aerospace RFQs | ⚡ Highly Automatable | ~$700M | Medium | Estimating manager, owner |
| 8 | Customer Flowdown & Specification Revision Control | ⚡ Highly Automatable | ~$350M | Low | Quality or contracts manager |

## Why These Niches

Engine components take the largest share because 336412 holds ~57% of the two codes' receipts, and final inspection there decides how much scarce casting and forging capacity becomes saleable parts. Airframe structures are second because every rate break Boeing and Airbus attempt (the 737 moving from 42 to 47 a month in 2026 with more planned, per Boeing's 10-Q) lands on tier-2 and tier-3 suppliers first. The two low-digitized niches are the paper and phone at the centre of every shipment: first article packages assembled by hand and outside processors chased by phone. The two underserved audiences are the small AS9100 shop bidding DLA spares, which government-contracting software built for primes ignores, and the PMA engineering team, which design tools built for new parts don't serve. The two automatable niches are the most mechanical document work in the business: pricing an RFQ package from drawings, and reconciling every PO's clause list and spec revisions against the router before release.

## Niches

- [[niches/aerospace-parts-suppliers/engine-components-rotating-parts/profile|🔵 Engine Components & Rotating Parts]]
- [[niches/aerospace-parts-suppliers/aerostructures-detail-parts/profile|🔵 Aerostructures & Airframe Detail Parts]]
- [[niches/aerospace-parts-suppliers/first-article-inspection/profile|🟠 First Article Inspection & AS9102 Packages]]
  - [[niches/aerospace-parts-suppliers/drawing-ballooning-characteristics/profile|🎯 Drawing Ballooning & Characteristic Accountability]]
  - [[niches/aerospace-parts-suppliers/material-process-cert-verification/profile|🎯 Material & Special-Process Certification Verification]]
- [[niches/aerospace-parts-suppliers/outside-special-processing/profile|🟠 Outside Special Processing & Sub-Tier Expediting]]
- [[niches/aerospace-parts-suppliers/small-shops-government-spares/profile|🟣 Small Shops Bidding Government Spare Parts]]
- [[niches/aerospace-parts-suppliers/pma-parts-developers/profile|🟣 PMA Parts Developers & Reverse-Engineering Teams]]
- [[niches/aerospace-parts-suppliers/drawing-to-quote/profile|⚡ Drawing-to-Quote for Aerospace RFQs]]
- [[niches/aerospace-parts-suppliers/flowdown-spec-revision-control/profile|⚡ Customer Flowdown & Specification Revision Control]]

## Filter Notes

Seven of the eight level-1 niches are terminal. First Article Inspection is not. Writing its contested sentence produced two contests with different winners. On Form 3 the contest is reading every requirement off a drawing or model, notes included, and the winner is whoever has the highest characteristic recall on scanned legacy prints and model-based definitions. On Form 2 the contest is proving every material and special process with genuine, conforming certificates from approved processors, and the winner is whoever catches a bad or falsified cert earliest, the failure the 2024 falsified-titanium case exposed (search summary of AP and FAA statements). Inputs, vendors and failure modes differ, so it decomposes into Drawing Ballooning & Characteristic Accountability and Material & Special-Process Certification Verification. The parent keeps the package-assembly and delta-FAI work that spans both. The CMM-to-Form-3 transcription step is already held in [[niches/contract-manufacturing/aerospace-precision-machining/profile|Aerospace Precision Machining]] under contract manufacturing and is linked, not repeated.

Three terminal calls were close. **Small Shops Bidding Government Spare Parts** and **Drawing-to-Quote** both end in a quote, but the government contest is won on eligibility and award history (approved sources, technical data access, first article tests), while the commercial contest is won on estimation accuracy against job actuals. Different data, different clocks, different winners. **Outside Special Processing** and **Aerostructures & Airframe Detail Parts** both concern delivery, but one is a lot-level date prediction for work at processors the shop doesn't control and the other a capacity plan for a rate break the prime reviews. **Customer Flowdown & Specification Revision Control** overlaps the first-article parent's per-prime FAI rules; it is kept separate because its contest covers every PO clause and spec revision at release, not only the FAI.

Four candidates were considered and rejected. **ITAR and CMMC compliance for small suppliers** is real (Phase 2 of CMMC was suspended on 13 July 2026, while some primes still flow certification down), but it is already covered by [[niches/contract-manufacturing/veteran-owned-defense-contractors/profile|Veteran-Owned Defense Contractors]] and [[niches/electronics-contract-mfg/defense-itar-ems/profile|Defense & ITAR-Compliant EMS]], and its contest here would be generic GRC. **Counterfeit parts** were rejected as a separate niche because the DFARS 252.246-7007/7008 regime covers electronic parts only, held under electronics as the Pass 2 pocket [[niches/electronics-contract-mfg/counterfeit-component-intelligence/profile|🔍 Counterfeit Component Intelligence]]. The mechanical-parts version is certificate truth, which sits in the Form 2 sub-niche. **Castings and forgings process control** belongs to the queued investment-casting foundries and forging shops industries, and **aerospace fasteners** to the queued fastener manufacturers. **PMA installation and engine repair** belongs to [[industries/aircraft-mro-shops|Aircraft MRO Shops]], and prime integration to the queued aircraft manufacturers industry.

---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. Pass 1 searched across the operator layer, here suppliers from 20-person machine shops to Howmet's $4.3B engine-products segment, whose indirect staffs run quality and planning, not research. This pass sweeps seven positions in the value chain (aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry) looking for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Aerospace Fleet & Production Forecast Data | Data vendor | 20-100 | 43 | Below threshold |
| 10 | Aerospace Quality Standards & Supplier Registry | Association | 20-150 | 41 | ⚠️ Kill switch |
| 11 | Aerospace Supply Chain & M&A Advisory | Specialist advisory | 20-150 | 39 | ⚠️ Kill switch |
| 12 | PMA & DER Engineering Consultancies | Specialist advisory | 10-80 | 38 | ⚠️ Kill switch |
| 13 | Aerospace Component Rollups | Aggregator/rollup | 10-60 | 33 | Below threshold |
| 14 | Aviation Products Liability Underwriters | Payer & intermediary | 10-40 | 32 | Below threshold |
| 15 | Superalloy & Titanium Machining Applications Engineering | Supplier | 50-300 | 32 | Below threshold |
| 16 | DoD Spare-Parts Pricing Oversight | Regulatory | 10-30 per audit team | 29 | ⚠️ Kill switch |
| 17 | Prime & Engine-OEM Supplier Performance Analytics | Payer & intermediary | 20-200 | 29 | Below threshold |
| 18 | FAA Production Oversight & Suspected Unapproved Parts | Regulatory | <10 analysts | — | Fails gate |
| 19 | Supplier Quality Data Networks | Supplier | <10 | — | Fails gate |
| 20 | Aerospace Trade Association Research | Association | <10 | — | Fails gate |
| 21 | AS9100 Certification Bodies | Specialist advisory | production | — | Fails gate |

## Why These Pockets

Nothing qualifies, and the operators themselves fail the gate. A parts supplier's analysis serves its own shipments; its customers own the requirements, and its quality staff are production, however skilled. The organisations around it repeat the pattern seen in the earlier manufacturing sweeps. The closer an insight function sits to a supplier's actual parts, the more likely its data belongs to someone else (consultancies and DER firms under client NDAs, OASIS audit results submitted under scheme rules, government pricing teams under statutory confidentiality) or its output is sold as something other than insight (tools, premiums, certificates).

The strongest pocket is fleet and production forecast data at 43. Its forecast archive is the cleanest ungraded asset in the sweep: every production-rate forecast resolves against actual deliveries, and with Boeing planning 737 increases beyond 47 a month, an honestly graded record of past rate calls would be worth more than another forecast. It falls short on a self-set refresh clock, a buyer market of a handful of firms, a moat capped by public outcome records (OEM delivery reports and aircraft registries), and a labour mass that is mostly fleet-record production staff. The standards and registry pocket (41) carries a kill switch on its most interesting half: OASIS's Tier 2 audit results, the one record that could show which audit findings predict a supplier's later escapes, are scheme-submitted private data that suppliers release to customers only on request. Only the Tier 1 certificate listings are public, and they would not support a moat.

Several pockets that matter to this industry were already profiled elsewhere and are linked, not re-scored. Multi-tier supply mapping (Exiger, Interos, Resilinc, Everstream) is indexed as [[niches/contract-manufacturing/supply-chain-risk-intelligence/profile|🔍 Multi-Tier Supply Chain Risk Intelligence]] (54), and Exiger is hiring forward deployed engineers for defence supply chains now. The price-reporting-agency family is profiled as [[niches/metal-fabrication/metals-price-reporting-agencies/profile|🔍 Metals Price Reporting Agencies]] (51), but that profile covers steel, aluminium and scrap; titanium and nickel-alloy price assessments are not profiled anywhere in the vault. Nadcap, which lists 4,500+ accredited suppliers on PRI's own page, is scored twice with an ITAR kill switch, as [[niches/electronics-contract-mfg/nadcap-aerospace-quality-audits/profile|🔍 Aerospace & Defence Special Process Auditing]] and [[niches/testing-laboratories/aerospace-special-process-accreditation/profile|🔍 Aerospace Special-Process Accreditation]] (48). Should-cost modelling is [[niches/contract-manufacturing/should-cost-modeling-vendors/profile|🔍 Should-Cost Modelling Vendors]] (49), export classification [[niches/contract-manufacturing/export-control-classification/profile|🔍 Export Control Classification & Trade Compliance]] (48, kill switch) and materials data [[niches/contract-manufacturing/materials-property-databases/profile|🔍 Materials Property Databases]] (47). Government bid intelligence is [[niches/contract-research-labs/federal-opportunity-intelligence/profile|🔍 Federal R&D Opportunity Intelligence]] (46). Failure analysis and NDT are [[niches/metal-fabrication/materials-testing-failure-analysis/profile|🔍 Materials Testing & Failure Analysis]] (46, kill switch) and [[niches/metal-fabrication/nondestructive-testing-services/profile|🔍 Nondestructive Testing Services]] (48, kill switch), and second-party supplier audits are [[niches/contract-manufacturing/supplier-quality-audit-firms/profile|🔍 Supplier Quality Audit Firms]] (43, kill switch). The commercial opening in this industry is therefore Pass 1's: the paperwork vendors (SalesPatriot, First Resonance, Paperless Parts, Vendra) selling to suppliers, not a research engine selling to an insight team.

## Niches — Pass 2
- [[niches/aerospace-parts-suppliers/aerospace-fleet-production-forecasts/profile|🔍 Aerospace Fleet & Production Forecast Data]]
- [[niches/aerospace-parts-suppliers/aerospace-quality-standards-registry/profile|🔍 Aerospace Quality Standards & Supplier Registry]]
- [[niches/aerospace-parts-suppliers/aerospace-supply-chain-advisory/profile|🔍 Aerospace Supply Chain & M&A Advisory]]
- [[niches/aerospace-parts-suppliers/pma-der-engineering-consultancies/profile|🔍 PMA & DER Engineering Consultancies]]
- [[niches/aerospace-parts-suppliers/aerospace-component-rollups/profile|🔍 Aerospace Component Rollups]]
- [[niches/aerospace-parts-suppliers/aviation-products-liability-underwriters/profile|🔍 Aviation Products Liability Underwriters]]
- [[niches/aerospace-parts-suppliers/superalloy-machining-applications/profile|🔍 Superalloy & Titanium Machining Applications Engineering]]
- [[niches/aerospace-parts-suppliers/dod-spare-parts-pricing-oversight/profile|🔍 DoD Spare-Parts Pricing Oversight]]
- [[niches/aerospace-parts-suppliers/prime-supplier-performance-analytics/profile|🔍 Prime & Engine-OEM Supplier Performance Analytics]]
- [[niches/aerospace-parts-suppliers/faa-production-oversight/profile|🔍 FAA Production Oversight & Suspected Unapproved Parts]]
- [[niches/aerospace-parts-suppliers/supplier-quality-data-networks/profile|🔍 Supplier Quality Data Networks]]
- [[niches/aerospace-parts-suppliers/aerospace-association-research/profile|🔍 Aerospace Trade Association Research]]
- [[niches/aerospace-parts-suppliers/as9100-certification-bodies/profile|🔍 AS9100 Certification Bodies]]
