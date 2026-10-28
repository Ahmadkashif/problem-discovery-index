# AI Parts-Identification & Fitment Vendors

**Parent Industry:** [[industries/auto-parts-distributors|Auto Parts Distributors & Stores]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Vendors whose product is a model that turns a repair job, a request or a photo into the exact purchasable part. Partly, headquartered in Austin with engineering in New Zealand, sells PartlyRepair to collision shops, workshops and parts suppliers on its Interpreter model, "trained on 1M+ car models and 1B+ parts," and claims 98.8% parts-list accuracy for estimators against 92.1% with existing tools (vendor figures). Catalog and e-catalog vendors are adding similar features. Customers pay by subscription or per job; parts suppliers use the output to win orders. The collision estimating databases of CCC, Mitchell and Audatex, indexed as [[niches/auto-body-shops/estimating-data-providers/profile|Collision Estimating Data Providers]] (56, pending Stage E), already identify and price parts inside each estimate; the difference is that Partly turns an estimate or job into purchasable part numbers across many suppliers' catalogs, and sells that resolution to the suppliers as well as to repairers.

## Insight Function
**Size:** ~15–50 ML, research and data engineers at the leading vendor (estimate; Partly's board lists an "AI Research & Software Engineering" department hiring in Austin, Christchurch and Auckland on 2026-10-28). Parts-data specialists who code records one at a time are production and are not counted
**Output:** Parts identification and parts lists inside repairers' and suppliers' workflows; model updates
**Proprietary data:** A parts graph built from licensed, non-exclusive vehicle-maker and supplier catalogs; corrections from customers' production jobs sit in a separate data regime and are not counted in Q3
**Clock:** Product release cycles; per-job and per-claim deadlines bind the customers' production work, not the vendor's analysis
**Buyer:** CEO or head of product at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 2 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 3 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **29/60** |

**Kill switches:** split by data regime. The **parts-graph half** (catalog content licensed to the vendor for its product) carries none: content licensed for republication is vendor product rights, as with [[niches/powersports-and-boat-dealers/parts-catalog-publishers/profile|Electronic Parts Catalog Publishers for Powersports & Marine]]. The **job-data half** (repairers' estimates, photos and corrections under service agreements whose terms were not read) would be live. Q3 is scored on the parts-graph half alone (3: large, but built from catalog licences any rival can also buy), and the verdict follows that half.
**Verdict:** Logged — below threshold (29; the job-data half alone would be a kill switch). Scored like [[niches/wholesale-auto-auctions/ai-vehicle-inspection-vendors/profile|AI Vehicle Inspection Vendors]] (32) under the batch Q1 ruling that a vendor with a real ML team is scored, not failed as product engineering: identification is sold as software, not invoiced as analysis, to a market of a few vendors. It sits three points lower because the inspection vendors' Q3 4 counts their labelled scan corpus (the half that carries their kill switch), while this pocket's Q3 counts only a graph built on licences rivals can buy. The general distributor order-intake vendors are a different field, profiled once as [[niches/industrial-distributors/rfq-and-order-intake-automation/profile|RFQ & Order Intake Automation]].
