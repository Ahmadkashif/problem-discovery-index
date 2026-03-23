# LTL Consolidation Brokerages

**Parent Industry:** [[industries/freight-brokerage|Freight Brokerage]]
**Category:** High Market Share

## Profile
**Market Size:** $12-15B
**Share of Parent Industry:** ~17%
**Digital Adoption:** Medium — LTL brokers use carrier rate APIs (SMC3, Carrier Connect) but consolidation planning and multi-stop optimization remain largely manual
**Target Buyer:** LTL desk manager or operations director at brokerages with dedicated LTL divisions
**Automation Potential:** High — shipment consolidation, carrier rate comparison, and multi-stop routing are computationally intensive but well-defined problems

## What Makes This a Distinct Niche
LTL brokerage is fundamentally different from FTL: instead of one shipper filling one truck, LTL brokers coordinate partial shipments from multiple shippers into consolidated loads. The broker's value proposition is finding shipments that can share capacity on the same route, reducing per-shipment cost below what each shipper would pay individually. This requires consolidation planning — matching shipments by pickup region, delivery region, freight class, and timing — that FTL tools don't address. LTL also involves a distinct carrier ecosystem (ODFL, XPO, ABF Freight) with tariff-based pricing structures rather than spot rates, and accessorial charges (liftgate, inside delivery, limited access) that significantly affect the all-in cost.

## Current Tools & Gaps
SMC3 and Carrier Connect provide LTL carrier rate APIs. Banyan Technology provides multi-carrier LTL rate shopping. These handle rate comparison on individual shipments but don't optimize consolidation across the broker's daily shipment pool — identifying which shipments to combine, which carrier offers the best consolidated rate, and which pickup/delivery windows to coordinate.

## Problems
- [[niches/freight-brokerage/ltl-consolidation/build|🔨 Build: Multi-Shipment Consolidation Optimizer]]
- [[niches/freight-brokerage/ltl-consolidation/buy|🛒 Buy: LTL Accessorial Cost Predictor]]
- [[niches/freight-brokerage/ltl-consolidation/fix|🔧 Fix: Freight Class Misclassification Catch]]
