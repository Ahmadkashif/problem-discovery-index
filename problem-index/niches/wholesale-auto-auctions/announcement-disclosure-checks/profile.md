# Announcement & Disclosure Checks

**Parent Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to make each seller announcement and condition report complete enough that buyers cannot win an arbitration on it, and whoever has the fewest arbitrations granted on announceable items per thousand units sold takes the account.

## Profile
**Market Size:** ~$250M a year in consignment-desk staff time, condition-report QA, VIN decode and recall data feeds, and assurance products priced on disclosure risk (estimate)
**Share of Parent Industry:** ~3% of auction, service and floorplan revenue (estimate)
**Digital Adoption:** Medium — announcements and reports are entered digitally, but as free text and picklists that nothing checks against the guidelines
**Target Buyer:** VP of customer assurance or inspection at an auction; remarketing directors at commercial consignors who upload thousands of units
**Automation Potential:** High — decoding, recall lookup, category mapping and threshold rules are mechanical

## What Makes This a Distinct Niche
This is the pre-sale half of arbitration, and the 1 June 2026 guidelines made it mechanical and urgent at once. Generic "No Arb for [defect]" announcements are banned. A warning light announced without its cause no longer protects the seller. ADAS components are arbitrable. Cars at $50,000 and above face a 2% per-defect threshold. Each of those is a rule a machine can check against the announcement text, the condition report, the NHTSA vPIC decode and NHTSA recall campaigns before the car runs. The competitors are the auctions' own inspection and assurance teams and the assurance products that price what disclosure misses, ACV's Go Green and Cox's DealShield. Data feeds also compete: open-recall vendors ([[niches/franchised-car-dealers/recall-outreach-vendors/profile|Recall Outreach & Open-Recall Data Vendors]]) and VIN decode and configuration data ([[niches/franchised-car-dealers/incentive-data-services/profile|Automotive Incentive Data Services]]). Claim handling after the sale is [[niches/wholesale-auto-auctions/arbitration-post-sale-claims/profile|Arbitration & Post-Sale Claims]]. The pre-run arbitration-risk idea is already proposed at [[niches/auto-dealers-independent/auction-condition-report-ops/build|Arbitration Says Whether the Report Was True and Nobody Adds It Up]], under the auctions' condition-report pocket. That build scores inspectors against arbitration outcomes and targets re-inspection at risky cars: it is about the inspector's accuracy. This niche checks the seller's announcement wording, the price threshold, the VIN decode and recall campaigns against the 2026 rules at check-in: it is about the disclosure, not the inspection, and it runs on public data before any claim history exists.

## Current Tools & Gaps
Auction inspection apps with picklists, seller templates, the free NHTSA APIs, commercial recall and VIN feeds, and assurance products. ACV is hiring an Analytics Engineer III, Assurance to work on arbitration risk (2026-08-19). Gaps: no check of announcement wording against the 2026 rules; equipment never compared with the VIN decode; and recall campaigns not surfaced at check-in.

## Problems
- [[niches/wholesale-auto-auctions/announcement-disclosure-checks/build|🔨 Build: An Arbitration-Risk Checker on Every Condition Report]]
- [[niches/wholesale-auto-auctions/announcement-disclosure-checks/buy|🛒 Buy: Marketing Compliance Review Adapted to Seller Announcements]]
- [[niches/wholesale-auto-auctions/announcement-disclosure-checks/fix|🔧 Fix: The "No Arb for Oil Leaks" Template That Stopped Working on 1 June]]
