# Niche Analysis — Wireless Carriers

**Parent Industry:** [[industries/wireless-carriers|Wireless Carriers]]

## Niche Selection

A wireless carrier runs a radio network tuned by a few experienced engineers, extends it through a chain of tower owners, landlords and municipalities under FCC shot clocks, and earns its money by keeping postpaid lines from porting out. Three national carriers dominate after T-Mobile bought UScellular's wireless business in August 2025. Around them sit a few dozen regional and rural carriers and about 2,000 fixed wireless ISPs serving roughly 9 million homes. The eight niches below split the industry by what vendors and internal teams actually compete over. Market sizes are estimates of tooling, services, analytics and labour spend within each niche, not of carrier revenue.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Postpaid Phone Retention & Upgrade Lifecycle | 🔵 High Market Share | ~$15B | High | SVP Consumer Retention |
| 2 | RAN Capacity Planning & Spectrum Deployment | 🔵 High Market Share | ~$2B | High | VP RAN Engineering |
| 3 | Cell Site Field Operations & Fault Diagnosis | 🟠 Low Digitized | ~$6B | Low | VP Field Operations |
| 4 | Site Modifications, Leasing & Permitting | 🟠 Low Digitized | ~$3B | Low | VP Site Development & Real Estate |
| 5 | Rural & Regional Mobile Carriers | 🟣 Underserved Audience | ~$400M | Medium | Regional carrier CEO or CTO |
| 6 | Fixed Wireless ISPs (WISPs) | 🟣 Underserved Audience | ~$450M | Medium | WISP owner-operator |
| 7 | Number Porting, SIM Changes & Account Takeover Defence | ⚡ Highly Automatable | ~$800M | High | VP Fraud & Identity |
| 8 | NOC Alarm Correlation & Outage Reporting | ⚡ Highly Automatable | ~$2B | High | VP Network Operations |

## Why These Niches

Postpaid retention takes the largest share because retention credits and save desks are the biggest discretionary spend a carrier controls, with churn near 0.9% a month. Capacity planning is second: its own tooling budget is modest, but it steers most of the ~$30B a year carriers spend on their networks, and it now decides where fixed wireless can be sold. The two low-digitized niches are where paper and memory still run the work. Cell site field operations depend on technicians' private site knowledge, and site modifications run on PDFs, drawings and portal uploads between four parties. The two underserved audiences are operators that national-carrier tools ignore. Rural carriers defend roaming revenue with one or two engineers, and WISPs run real radio networks with a handful of staff. The two automatable niches are the most mechanical, high-volume decisions in the business: approving or stopping SIM and port requests, and turning alarm floods into incidents and FCC outage reports.

## Niches

- [[niches/wireless-carriers/postpaid-retention-lifecycle/profile|🔵 Postpaid Phone Retention & Upgrade Lifecycle]]
- [[niches/wireless-carriers/ran-capacity-planning/profile|🔵 RAN Capacity Planning & Spectrum Deployment]]
- [[niches/wireless-carriers/cell-site-field-operations/profile|🟠 Cell Site Field Operations & Fault Diagnosis]]
- [[niches/wireless-carriers/site-modification-permitting/profile|🟠 Site Modifications, Leasing & Permitting]]
- [[niches/wireless-carriers/rural-regional-carriers/profile|🟣 Rural & Regional Mobile Carriers]]
- [[niches/wireless-carriers/wisp-operators/profile|🟣 Fixed Wireless ISPs (WISPs)]]
  - [[niches/wireless-carriers/wisp-address-qualification/profile|🎯 WISP Address Qualification & Installs]]
  - [[niches/wireless-carriers/wisp-sector-qoe/profile|🎯 WISP Sector Congestion & Subscriber Experience]]
- [[niches/wireless-carriers/porting-sim-account-security/profile|⚡ Number Porting, SIM Changes & Account Takeover Defence]]
- [[niches/wireless-carriers/noc-alarm-outage-reporting/profile|⚡ NOC Alarm Correlation & Outage Reporting]]

## Filter Notes

Seven of the eight level-1 niches are terminal. Fixed Wireless ISPs is not. Writing its contested sentence produced two sentences with different winners. Before the sale, the contest is qualifying a specific roofline from a specific sector: line of sight, foliage and mounting height, labelled the same day by the install. After the sale, it is keeping evening-peak experience inside the plan on shared and often unlicensed spectrum: airtime, interference and backhaul, labelled every night by subscriber telemetry. The people (sales and installers against network engineers), the data (LiDAR and terrain against traffic and radio statistics) and the vendors (TowerCoverage and cnHeat against Preseem and radio controllers) all differ. So the niche decomposes into **WISP Address Qualification & Installs** and **WISP Sector Congestion & Subscriber Experience**.

Three terminal calls were close. **Postpaid retention** could be split into churn prevention and upgrade promotions, but upgrade offers are the main retention tool and are bought by the same team against the same port-out risk, so one contest governs. **Site modifications** could be split into lease work and permitting, but both are steps on one critical path to on-air, and programme managers win or lose on the whole chain. Rent negotiation under master lease agreements, a once-a-decade negotiation between a carrier and three tower companies, was excluded as a tooling contest. **Rural carriers** overlap with the coverage-filing problem in Pass 1, but they are kept as an audience because their contest is roaming revenue, which no national-carrier tool addresses.

Five candidates were considered and rejected. **Prepaid and thin-file device financing** has a real contest (approving device financing for customers without credit files without eating subscription fraud), but much of that work sits with authorised dealers and MVNO brands, analysed under [[industries/wireless-retail-agents|Wireless Retail Agents]] and [[industries/telecom-resellers|Telecom Resellers]]. **Enterprise and IoT accounts** produced only a generic sentence ("broadest coverage, lowest price"), and private 5G networks are a systems-integrator contest. **Public safety networks** were considered. FirstNet is one carrier's federal contract and the rivals' answer is a procurement contest, not a tooling contest. **Direct-to-cell satellite coverage** belongs to [[industries/satellite-operators|Satellite Operators]], where it is the niche [[niches/satellite-operators/direct-to-device-services/profile|🟣 Direct-to-Device: Users Beyond the Last Tower]]. **Spectrum auction bidding** is real and governed by FCC clocks, but it is episodic and done by outside advisers, so it is logged as a Pass 2 pocket. Tower construction and climbing crews belong to [[industries/utility-contractors|Utility Contractors]], and broadcast transmitter sites to [[niches/broadcast-stations/transmitter-and-rf-engineering/profile|🟠 Transmitter, Tower & RF Engineering]] under broadcast stations.

---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. Pass 1 searched across the operator layer: three national carriers whose large engineering and analytics teams serve their own networks and customers, a few dozen regional carriers and about 2,000 WISPs with a handful of staff each. This pass sweeps seven positions in the value chain (aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry), looking for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`. Pockets already profiled under other industries are named and linked below rather than profiled again.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Frequency Coordination & Interference Analysis Firms | Specialist advisory | ~20-60 at the leader | 44 | Below threshold |
| 10 | Mobile Operator Association Research | Association | ~50-100 | 43 | Below threshold |
| 11 | Telecom Strategy Research & Forecasting Houses | Data vendor | ~20-80 per firm | 42 | Below threshold |
| 12 | Device Protection & Trade-In Programme Administrators | Payer & intermediary | ~50-200 per firm | 42 | Below threshold |
| 13 | Spectrum Valuation & Auction Advisory | Specialist advisory | ~10-40 per practice | 42 | ⚠️ Kill switch |
| 14 | Spectrum Regulators' Auction & Licensing Analytics | Regulatory | ~100+ at the FCC | 33 | Below threshold |
| 15 | RAN Vendor Network Analytics & Managed Services | Supplier | hundreds per vendor | 31 | ⚠️ Kill switch |
| 16 | Carrier-Data Identity & SIM-Swap Signal Vendors | Payer & intermediary | ~20-80 per vendor | 29 | ⚠️ Kill switch |
| 17 | Tower Company Leasing & Site Analytics | Supplier | ~10-40 per company | 28 | Below threshold |
| 18 | CBRS Spectrum Access System Administrators | Regulatory | engineering only | — | Fails gate |
| 19 | Wireless Pricing & Channel Trackers | Data vendor | <10 | — | Fails gate |
| 20 | Tower Siting Environmental & RF Compliance Consultancies | Specialist advisory | production staff only | — | Fails gate |
| 21 | WISP Rollup Platforms | Aggregator/rollup | <10 | — | Fails gate |
| 22 | Wireless Carrier Trade Associations | Association | <10 | — | Fails gate |
| 23 | Spectrum Holding & Leasing Companies | Aggregator/rollup | <10 | — | Fails gate |

## Why These Pockets

No pocket qualifies, and the carriers themselves fail the gate. A national carrier employs hundreds of RF, capacity, churn and fraud analysts (estimate), but every one of them works on the carrier's own network and customers and invoices nothing. The tower companies (pocket 17) and spectrum holders (pocket 23) repeat the pattern on the supply side. The firms that do sell analysis around wireless split four ways. Two run on carrier data they can't reuse: the equipment vendors' managed services (pocket 15) and the carrier-data identity vendors (pocket 16), the second also an automated API product rather than analyst work. The device protection administrators (pocket 12) own their claims, repair and grading records and carry the risk themselves, the same shape as the F&I actuarial teams under independent auto dealers (46), but their analysis prices an insurance product rather than being sold, and there are two of them. Spectrum advisers (pocket 13) have the hardest clock in the sweep, the FCC's auction calendar, but work on client-owned bidding models under the anti-collusion rule. The rest are small research houses with their own calendars (pockets 10 and 11) or public bodies (pocket 14).

The strongest clean near-miss is frequency coordination (pocket 9, 44). It has the shape this sweep looks for: a repeatable, billed engineering analysis built on a decades-long database of coordinated paths, under a regulatory response window of 30 days. But the market is one leading firm and a few small ones, and much of the volume is compliance processing rather than analysis a client buys for its own sake. GSMA Intelligence (pocket 10, 43) is the cleanest research business, held back by self-set clocks and by being a single association unit.

Several insight businesses that matter to carriers are already profiled elsewhere and aren't profiled twice. Network benchmarking (Ookla's crowdsourced tests, RootMetrics drive tests and Opensignal) is [[niches/wired-broadband-providers/speed-test-data-vendors/profile|🔍 Network Performance & Speed-Test Data Vendors]] (43) under wired broadband providers; mobile benchmarking is the larger half of that business and would score the same here. J.D. Power's wireless network quality and purchase studies come from the same telecom practice as [[niches/wired-broadband-providers/isp-customer-experience-benchmarks/profile|🔍 ISP Customer Experience Benchmarks]] (41), and Kagan's wireless subscriber and spectrum data from the unit profiled as [[niches/wired-broadband-providers/subscriber-data-trackers/profile|🔍 Media & Communications Subscriber Data Trackers]] (40, with the operator-earnings clock scored 3). Call labelling by TNS, Hiya and First Orion, which the national carriers buy for their spam and scam warnings, is [[niches/telecom-resellers/robocall-analytics-engines/profile|🔍 Robocall Analytics & Call-Labelling Engines]] (40) under telecom resellers. Telecom equity analysts such as New Street Research and MoffettNathanson sit inside [[niches/sell-side-equity-research/independent-research-providers/profile|🔍 Independent Research Providers]] (48). Tower securitisations and device-payment ABS are rated by the teams in [[niches/financial-data-vendors/credit-rating-agency-analytics/profile|🔍 Credit Rating Agency Analytics]] (47, kill switch). Carrier merger reviews such as T-Mobile and UScellular go through [[niches/investment-banking-boutiques/antitrust-economic-consulting/profile|🔍 Antitrust Economic Consulting]] (46, kill switch). Investors that buy the ground rent under towers are [[niches/outdoor-advertising-companies/ground-lease-aggregators/profile|🔍 Billboard Ground Lease Aggregators & Lenders]] (30). Equipment market-share research (Dell'Oro and peers) belongs to the queued communications-equipment-makers industry.

For a research-insight engine, wireless is a market to sell around rather than into. For workflow and ML tools the opening is real and mostly in Pass 1: RF diagnosis, alarm triage, site-to-air paperwork, coverage filings and account takeover. Regional carriers and WISPs are the reachable buyers; national carriers are reached through their equipment vendors' platforms.

## Niches — Pass 2
- [[niches/wireless-carriers/frequency-coordination-firms/profile|🔍 Frequency Coordination & Interference Analysis Firms]]
- [[niches/wireless-carriers/mobile-operator-association-research/profile|🔍 Mobile Operator Association Research]]
- [[niches/wireless-carriers/telecom-research-houses/profile|🔍 Telecom Strategy Research & Forecasting Houses]]
- [[niches/wireless-carriers/device-protection-trade-in/profile|🔍 Device Protection & Trade-In Programme Administrators]]
- [[niches/wireless-carriers/spectrum-valuation-auction-advisory/profile|🔍 Spectrum Valuation & Auction Advisory]]
- [[niches/wireless-carriers/spectrum-regulator-analytics/profile|🔍 Spectrum Regulators' Auction & Licensing Analytics]]
- [[niches/wireless-carriers/ran-vendor-managed-services/profile|🔍 RAN Vendor Network Analytics & Managed Services]]
- [[niches/wireless-carriers/carrier-identity-signal-vendors/profile|🔍 Carrier-Data Identity & SIM-Swap Signal Vendors]]
- [[niches/wireless-carriers/tower-company-site-analytics/profile|🔍 Tower Company Leasing & Site Analytics]]
- [[niches/wireless-carriers/cbrs-sas-administrators/profile|🔍 CBRS Spectrum Access System Administrators]]
- [[niches/wireless-carriers/wireless-pricing-channel-trackers/profile|🔍 Wireless Pricing & Channel Trackers]]
- [[niches/wireless-carriers/tower-siting-compliance-consultancies/profile|🔍 Tower Siting Environmental & RF Compliance Consultancies]]
- [[niches/wireless-carriers/wisp-rollup-platforms/profile|🔍 WISP Rollup Platforms]]
- [[niches/wireless-carriers/carrier-trade-associations/profile|🔍 Wireless Carrier Trade Associations]]
- [[niches/wireless-carriers/spectrum-holding-companies/profile|🔍 Spectrum Holding & Leasing Companies]]
