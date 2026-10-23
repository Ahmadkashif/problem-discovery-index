# Niche Analysis — Electric Distribution Utilities

**Parent Industry:** [[industries/electric-utilities|Electric Distribution Utilities]]

## Niche Selection

A distribution utility sells a regulated product at a price set in a rate case, and spends its effort on three things: connecting new load and generation to a grid sized for flat demand, keeping the lights on through storms and fire seasons, and getting customers billed and paid. Load growth from data centres and electrification, record rate requests and a decade of worse storms have put pressure on all three at once. The eight niches below split the industry by what vendors and internal teams actually compete over. Market sizes are estimates of software, services, consulting and staff spend within each niche, not of the ~$514B of retail electricity revenue (EIA, 2024) that flows through the utilities.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Interconnection & Large-Load Planning | 🔵 High Market Share | ~$2.5B | Medium | Director of Distribution Planning |
| 2 | Rate Cases & Revenue Requirement | 🔵 High Market Share | ~$1.5B | Medium | VP of Regulatory Affairs |
| 3 | Storm Restoration & Mutual Assistance | 🟠 Low Digitized | ~$1B | Low | Director of Emergency Preparedness |
| 4 | Vegetation Management & Wildfire Mitigation Programmes | 🟠 Low Digitized | ~$1.5B | Low | Director of Vegetation Management / Chief Wildfire Mitigation Officer |
| 5 | Small Cooperatives & Municipal Utilities | 🟣 Underserved Audience | ~$800M | Low | General Manager, often via G&T member services |
| 6 | Payment-Troubled Residential Customers | 🟣 Underserved Audience | ~$600M | Medium | Director of Credit & Collections |
| 7 | AMI Meter Data Operations | ⚡ Highly Automatable | ~$1.2B | High | Director of Meter Operations |
| 8 | New Service Connection Design & Estimating | ⚡ Highly Automatable | ~$900M | Medium | Manager of Distribution Design |

## Why These Niches

Interconnection and large-load planning takes the top market-share slot because it decides where most of the ~$208B 2025 investor-owned capital budget (EEI) goes, and it is where data-centre growth arrives first. Rate cases take the second because every other dollar in the industry is priced there, and requests hit a record in 2025. The two low-digitized niches are the ones still run on phone calls, paper and experience: crews requested by conference call before a storm, and trees judged by an inspector with a tablet code. The two underserved audiences are the ~2,900 small co-ops and munis (estimate) that vendors price out, and the households in arrears whom collections tools treat as debt rather than as people protected by state rules. The two automatable niches are the most mechanical, high-volume work in the utility: exceptions in interval meter data, and standard new-service designs that repeat hundreds of times a year.

## Niches

- [[niches/electric-utilities/interconnection-and-large-load-planning/profile|🔵 Interconnection & Large-Load Planning]]
  - [[niches/electric-utilities/der-interconnection-hosting-capacity/profile|🎯 DER Interconnection & Hosting Capacity]]
  - [[niches/electric-utilities/large-load-data-centre-interconnection/profile|🎯 Large-Load & Data Centre Interconnection]]
- [[niches/electric-utilities/rate-cases-revenue-requirement/profile|🔵 Rate Cases & Revenue Requirement]]
- [[niches/electric-utilities/storm-restoration-mutual-assistance/profile|🟠 Storm Restoration & Mutual Assistance]]
- [[niches/electric-utilities/vegetation-wildfire-mitigation-programs/profile|🟠 Vegetation Management & Wildfire Mitigation Programmes]]
- [[niches/electric-utilities/small-coops-and-munis/profile|🟣 Small Cooperatives & Municipal Utilities]]
- [[niches/electric-utilities/payment-troubled-customers/profile|🟣 Payment-Troubled Residential Customers]]
- [[niches/electric-utilities/ami-meter-data-operations/profile|⚡ AMI Meter Data Operations]]
- [[niches/electric-utilities/new-service-connection-design/profile|⚡ New Service Connection Design & Estimating]]

## Filter Notes

Seven of the eight level-1 niches are terminal. Interconnection & Large-Load Planning is not. Writing its contested sentence produced two contests with different winners. For distributed generation, storage and chargers, the contest is volume: clearing thousands of small applications against a hosting-capacity number that later reviews confirm, won by whoever automates screens inside the regulated interconnection process. For data centres and factories, the contest is a few enormous requests, many of them speculative: giving a megawatt figure, date and upgrade cost that hold until energisation, won by whoever best predicts which requests are real. Different volumes, buyers (interconnection managers versus system planners and economic-development executives) and data, so it decomposes into **DER Interconnection & Hosting Capacity** and **Large-Load & Data Centre Interconnection**. The bulk-system side of interconnection (grid-operator queues and generator studies) belongs to the queued Transmission & Grid Operators row and to [[niches/solar-installers/interconnection-grid-studies/profile|🔍 Interconnection & Grid Impact Studies]].

Two terminal calls were close. **Storm Restoration & Mutual Assistance** could split into pre-storm staging and post-storm cost recovery. It stays whole because one roster governs both: the crews requested, checked in and released are the same records that the prudence review and FEMA audits examine, so whoever owns staging owns the cost file. **Vegetation Management & Wildfire Mitigation Programmes** could split into reliability trimming (everywhere) and wildfire mitigation (the West). It stays whole because regulators in both cases now ask the same question, which is what each span of work prevented, and the winning evidence is the same span-level join of work to outcomes.

One niche was narrowed rather than decomposed. **Small Cooperatives & Municipal Utilities** first bundled planning, rate and grid analytics and named a sales channel (the G&T or statewide association) as its win condition. That is a route to market, not a contest. It now rests on one measurable outcome: overloads and capacity limits caught before they cause a failure or stall a connection. Rate studies for small utilities are left to the rate consultants logged under municipal services.

Four candidates were rejected. **Regulatory and compliance reporting** (EIA-861, FERC Form 1, NERC CIP evidence, state reliability reports) produced only a generic sentence, "produce filings faster", and its CIP half belongs to [[niches/cybersecurity-mssp/rural-cooperative-security/profile|🟣 Rural Cooperative & Utility Security]] and the transmission side. **Large commercial and industrial key accounts** overlaps the large-load sub-niche and the energy-advisory work in [[industries/energy-auditors|Energy Auditors]]. **DER management and virtual power plants** is a contest among aggregators and device vendors that sits closer to the queued Renewable Power Producers row than to the distribution utility's own work. **Retail choice and community choice aggregation** was set aside because the energy-only providers that win those customers are power marketers outside NAICS 221122's distribution work.

---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. Pass 1 swept across the utilities' own functions. This pass sweeps seven positions in the value chain: aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry. It looks for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`. Several pockets in this value chain were already profiled under neighbouring industries and are named in the prose below rather than profiled twice.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Load Forecasting & Resource Planning Consultancies | Specialist advisory | ~20-150 | 44 | Below threshold |
| 10 | Intervenor & Consumer-Advocate Expert Consultancies | Specialist advisory | ~15-80 | 43 | ⚠️ Kill switch |
| 11 | Utility Customer Satisfaction & Operational Benchmarking | Data vendor | ~10-30 | 41 | Below threshold |
| 12 | Utility Holding Company Regulatory & Rate Case Teams | Aggregator/rollup | ~30-150 | 40 | Below threshold |
| 13 | Wildfire Risk Modelling for Utility Mitigation Plans | Supplier | ~20-100 | 39 | ⚠️ Kill switch |
| 14 | Storm Outage Prediction Services | Supplier | ~10-40 | 39 | ⚠️ Kill switch |
| 15 | Rate Case Tracking & Regulatory Research Services | Data vendor | ~15-40 | 38 | Below threshold |
| 16 | Power & Utility Data Platforms | Data vendor | ~50-300 | 36 | Below threshold |
| 17 | Utility R&D Consortium | Association research arm | hundreds | 36 | ⚠️ Kill switch |
| 18 | G&T Cooperatives & Joint Action Agencies | Aggregator/rollup | ~10-60 | 36 | ⚠️ Kill switch |
| 19 | Utility Mutual Insurers & Wildfire Liability Underwriting | Payer & intermediary | ~20-80 | 34 | Below threshold |
| 20 | Distribution Planning & Hosting-Capacity Software Vendors | Supplier | ~10-60 | 33 | ⚠️ Kill switch |
| 21 | NERC Reliability Assessment & Compliance Monitoring | Regulatory | ~20-60 | 32 | ⚠️ Kill switch |
| 22 | Cooperative & Public Power Lenders | Payer & intermediary | ~20-60 | 32 | Below threshold |
| 23 | Federal Electricity Statistics | Regulatory | ~50-100 | 22 | Below threshold |
| 24 | Utility Trade Association Statistics | Association research arm | <10 | — | Fails gate |
| 25 | Transformer Brokers & Remanufacturers | Supplier | 2-15 | — | Fails gate |

## Why These Pockets

No pocket qualifies, and the central finding is that the utilities themselves are poor buyers under this rubric. They analyse their own grids, customers and costs, and invoice nothing. The nearest thing to a sold insight inside a utility is the holding company's rate case team (40): a real team on the hardest clock in the industry, whose output is a revenue claim before a regulator rather than a deliverable a client pays for. Much of the value chain around the utilities was already mapped under neighbouring industries. That includes [[niches/utility-contractors/utility-asset-rate-case-consulting/profile|🔍 Utility Asset Management & Rate Case Consulting]] (44, kill switch), [[niches/utility-contractors/utility-vegetation-management-analytics/profile|🔍 Utility Vegetation Management Analytics]] (46, kill switch), [[niches/utility-contractors/grid-reliability-outage-analytics/profile|🔍 Grid Reliability & Outage Analytics]] (46, kill switch) and [[niches/energy-auditors/utility-ami-analytics-vendors/profile|🔍 Utility Meter Data Analytics Vendors]] (46, kill switch). It also includes [[niches/solar-installers/interconnection-grid-studies/profile|🔍 Interconnection & Grid Impact Studies]] (44, kill switch), [[niches/solar-installers/state-utility-commissions/profile|🔍 State Utility Commissions & Interconnection Regulators]] (34), [[niches/energy-auditors/efficiency-potential-study-firms/profile|🔍 Energy Efficiency Potential Study Firms]] (47), [[niches/energy-auditors/utility-program-implementers/profile|🔍 Utility Efficiency Programme Implementers]] (48) and [[niches/municipal-services/utility-rate-consultants/profile|🔍 Municipal Utility Rate Consultants]] (40). Two indexed pockets touch this industry from outside: [[niches/energy-auditors/emv-evaluation-contractors/profile|🔍 Efficiency Programme Evaluation Contractors]] (51), whose evaluations decide the savings utilities may claim, and [[niches/municipal-services/municipal-credit-rating-analysis/profile|🔍 Municipal Credit Rating & Public Finance Analysis]] (56), which rates public power revenue bonds. Investor-owned utility debt is rated by the agencies logged as [[niches/financial-data-vendors/credit-rating-agency-analytics/profile|🔍 Credit Rating Agency Analytics]] (47, kill switch).

The new pockets split into two failure shapes. The supplier pockets are built on data the utility owns: utility-trained wildfire and storm outage models and planning software all train on or run against each client's asset, outage and network records, so nothing pools across clients and the kill switch is live. Their vendor-owned halves (fuel and fire-spread models, satellite layers, weather archives, public EAGLE-I outage data) are clean, but they score ~39–42 (estimate). The G&T cooperatives and the benchmarking consortia fail the same way, on data furnished by members. The clean data pockets, built on public dockets, federal filings and the firm's own surveys (rate case tracking, data platforms, the survey half of customer satisfaction studies), have their own data and their own invoice but sell into markets of a few firms on clocks they set themselves. Public utility data is unusually rich, from EIA-861 and EIA-860 through FERC Form 1 to the hosting-capacity maps DOE catalogues, and that keeps proprietary-data scores low across the board. It is also limited. EIA-861 and Form 1 are utility-level and EIA-860 covers generators of 1 MW and up. Feeder limits are public only where a utility publishes a hosting map (58 utilities and agencies in 26 states by May 2024, rarely refreshed), and no public source holds study outcomes. So an outsider's demo is hosting-map ingestion plus territory context, not a replica of the planner's read.

The strongest near-miss is load forecasting and resource planning consultancies (44). They have the shape every indexed qualifier shares: a forecast product with a later, unambiguous label, actual load published in FERC Form 714 and EIA-861, which the producer holds in its archive of vintages and never grades. Data-centre growth has made these forecasts the most contested numbers in resource-plan proceedings, so a graded track record would be a commercial asset. They fall short on team size, a consultancy market of perhaps 10–20 firms, and a clock that sits on the client's filing rather than on the forecast (Q4 4). The potential-study firms at 47 carry Q4 5 on the same kind of clock, which is logged as a likely defect. For the owner's placement aim the picture runs the other way. The operator layer that fails this rubric is where vendors are hiring now: Gridsight, E Source and Buzz Solutions all list forward deployed engineering roles on their own boards (source log, 2026-10-24).

## Niches — Pass 2
- [[niches/electric-utilities/load-forecasting-resource-planning-consultancies/profile|🔍 Load Forecasting & Resource Planning Consultancies]]
- [[niches/electric-utilities/intervenor-expert-consultancies/profile|🔍 Intervenor & Consumer-Advocate Expert Consultancies]]
- [[niches/electric-utilities/utility-customer-satisfaction-benchmarks/profile|🔍 Utility Customer Satisfaction & Operational Benchmarking]]
- [[niches/electric-utilities/holding-company-regulatory-teams/profile|🔍 Utility Holding Company Regulatory & Rate Case Teams]]
- [[niches/electric-utilities/wildfire-risk-modelling-vendors/profile|🔍 Wildfire Risk Modelling for Utility Mitigation Plans]]
- [[niches/electric-utilities/storm-outage-prediction-services/profile|🔍 Storm Outage Prediction Services]]
- [[niches/electric-utilities/rate-case-tracking-services/profile|🔍 Rate Case Tracking & Regulatory Research Services]]
- [[niches/electric-utilities/power-utility-data-platforms/profile|🔍 Power & Utility Data Platforms]]
- [[niches/electric-utilities/utility-rd-consortium/profile|🔍 Utility R&D Consortium]]
- [[niches/electric-utilities/gt-coops-joint-action-agencies/profile|🔍 G&T Cooperatives & Joint Action Agencies]]
- [[niches/electric-utilities/utility-mutual-insurers/profile|🔍 Utility Mutual Insurers & Wildfire Liability Underwriting]]
- [[niches/electric-utilities/hosting-capacity-planning-software/profile|🔍 Distribution Planning & Hosting-Capacity Software Vendors]]
- [[niches/electric-utilities/nerc-reliability-assessment-compliance/profile|🔍 NERC Reliability Assessment & Compliance Monitoring]]
- [[niches/electric-utilities/cooperative-utility-lenders/profile|🔍 Cooperative & Public Power Lenders]]
- [[niches/electric-utilities/federal-energy-statistics/profile|🔍 Federal Electricity Statistics]]
- [[niches/electric-utilities/utility-trade-association-statistics/profile|🔍 Utility Trade Association Statistics]]
- [[niches/electric-utilities/transformer-brokers-remanufacturers/profile|🔍 Transformer Brokers & Remanufacturers]]
