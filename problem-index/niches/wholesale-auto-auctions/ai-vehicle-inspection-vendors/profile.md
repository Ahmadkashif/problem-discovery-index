# AI Vehicle Inspection Vendors

**Parent Industry:** [[industries/wholesale-auto-auctions|Wholesale Auto Auctions]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Companies selling drive-through scanners and phone-based AI inspection to auctions, dealers, rental companies and fleets. UVeye has systems at dealerships, fleet sites and auction lots, and launched a service-lane offering with Cox's vAuto in January 2026 (search summary). ProovStation, DeGould and Tchek are named from recall. Monk is now in-house at ACV, and so at Copart. They sell a damage and undercarriage scan per vehicle or a site subscription, and the hardware that captures it. The in-house version is visible in ACV's hiring: Machine Learning Engineers III and IV for damage-detection models on "hundreds of thousands of vehicle inspections annually" (Buffalo, virtual or Toronto, from 2026-07-02) and Monk engineers in Paris.

## Insight Function
**Size:** ~15–60 imaging scientists and ML engineers per larger vendor (estimate). Annotators and image reviewers are production and are not counted
**Output:** Automated damage, tyre and undercarriage reports; scanner hardware; model updates
**Proprietary data:** Labelled vehicle images, most of them captured on clients' vehicles at clients' sites under service agreements
**Clock:** Product release cycles and clients' sale days (client clocks); no third-party deadline
**Buyer:** Head of product / CTO at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 2 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 2 |
| **Weighted total** | | **32/60** |

**Kill switches:** live on the image corpus. The labelled scans that carry this pocket's Q3 score are taken on clients' vehicles for the client's use under service agreements whose terms were not seen, and under the batch ruling client data under service agreements carries the switch unless checked terms grant product rights. The hardware half (scanners sold as equipment) carries no switch and would sit below threshold at the same score.
**Verdict:** Logged — kill switch (32). The verdict follows the image half, because the ML teams and the data moat being scored are built on client scans. Scored to match [[niches/aircraft-mro-shops/borescope-ndt-inspection-ai-developers/profile|Borescope & NDT Inspection AI Developers]] (32, kill switch, labellers excluded) on the same reasoning: a real imaging and ML function sold through hardware and software rather than invoiced as analysis, to a market of a few vendors. The service-diagnosis version, where the report itself is what owners pay for, scores higher at [[niches/renewable-power-producers/wind-condition-monitoring-analytics/profile|Wind Turbine Condition Monitoring & SCADA Analytics Vendors]] (44, Q1 4 against 2). The auctions' own inspection workforce and its arbitration data are [[niches/auto-dealers-independent/auction-condition-report-ops/profile|Wholesale Auction Condition Report Operations]] (48; logged for Stage E: it counts 1,000–5,000 per-vehicle inspectors, who are production under this run's rulings, and takes Q4 4 on sale day, a client clock, so it would likely fail the gate).
