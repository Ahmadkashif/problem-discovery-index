# Niche Analysis — Public Adjusters

**Parent Industry:** [[industries/public-adjusters|Public Adjusters]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Residential Property Claims | 🔵 High Market Share | $2.5B | Medium | Solo/Small Firm PA |
| 2 | Commercial Property Claims | 🔵 High Market Share | $1.8B | Medium | Mid-Size PA Firm Owner |
| 3 | Catastrophe (CAT) Response | 🟠 Low Digitized | $1.2B | Low | CAT Team Manager |
| 4 | Contents & Inventory Claims | 🟠 Low Digitized | $600M | Low | PA / Contents Specialist |
| 5 | Non-English-Speaking Policyholders | 🟣 Underserved Audience | $400M | Low | Bilingual PA |
| 6 | Condo Association & HOA Claims | 🟣 Underserved Audience | $500M | Low-Medium | PA Specializing in Associations |
| 7 | Xactimate Estimate Automation | ⚡ Highly Automatable | $800M | Medium | PA Estimator / Firm Owner |
| 8 | Carrier Negotiation & Supplement Tracking | ⚡ Highly Automatable | $700M | Low-Medium | PA Negotiator / Office Manager |

## Why These Niches

Residential and commercial property claims represent the core revenue streams where public adjusters earn contingency fees (typically 10-15% of settlement). CAT response and contents claims are surprisingly low-digitized — adjusters deploy to disaster zones with paper forms and photo folders, and contents inventories are still built manually in spreadsheets. Non-English-speaking policyholders and condo associations are structurally underserved because most PAs market through English-language channels and focus on single-family properties. Xactimate estimating and carrier supplement negotiation are high-frequency, rule-intensive tasks consuming 40-60% of a PA's time that are ripe for automation.

## Niches
- [[niches/public-adjusters/residential-property/profile|🔵 Residential Property Claims]]
- [[niches/public-adjusters/commercial-property/profile|🔵 Commercial Property Claims]]
- [[niches/public-adjusters/cat-response/profile|🟠 Catastrophe (CAT) Response]]
- [[niches/public-adjusters/contents-inventory/profile|🟠 Contents & Inventory Claims]]
- [[niches/public-adjusters/non-english-policyholders/profile|🟣 Non-English-Speaking Policyholders]]
- [[niches/public-adjusters/condo-hoa-claims/profile|🟣 Condo Association & HOA Claims]]
- [[niches/public-adjusters/xactimate-automation/profile|⚡ Xactimate Estimate Automation]]
- [[niches/public-adjusters/supplement-tracking/profile|⚡ Carrier Negotiation & Supplement Tracking]]


---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. Pass 1 searched across the operator layer and found firms of 1-15 people; research functions do not exist at that altitude. This pass sweeps seven positions in the value chain — aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry — looking for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Property Repair Estimating Data | Data vendor | 400-1,500 | 58 | ↔ Cross-referenced |
| 10 | Catastrophe Modelling Firms | Data vendor | 500-2,000 | **56** | ✅ Indexed |
| 11 | Managed Repair Programme Administrators | Payer & intermediary | 200-1,500 | 53 | ↔ Cross-referenced |
| 12 | Forensic Engineering & Cause of Loss Investigation | Specialist advisory | 100-1,000 | 51 | ↔ Cross-referenced |
| 13 | Property Claims Data & Fraud Analytics | Data vendor | 300-1,500 | 47 | Below threshold |
| 14 | Weather Verification & Peril Event Data | Data vendor | 60-300 | 45 | Below threshold |
| 15 | Aerial Imagery & Property Measurement | Data vendor | 200-1,000 | 44 | Below threshold |
| 16 | Contents Inventory & Valuation Services | Supplier | 100-500 | 39 | Below threshold |
| 17 | Insurance Appraisal & Umpire Services | Specialist advisory | 20-100 | 38 | Below threshold |
| 18 | State Insurance Departments & Market Conduct | Regulatory | 100-600 | 36 | ⚠️ Kill switch |
| 19 | Claims Practice & Bad Faith Litigation Support | Specialist advisory | 20-100 | 35 | ⚠️ Kill switch |
| 20 | Public Adjusting Firm Rollups | Aggregator/rollup | 10-50 | 34 | Below threshold |
| 21 | Public Adjuster Association Research | Association research arm | 2-8 | — | ✗ Fails gate |

## Why These Pockets

A $2B industry sitting underneath one of the densest insight layers in this entire sweep. Four of the thirteen pockets score 51 or above, and three of those four are already indexed under other industries — property repair estimating data at 58 is the highest-scoring pocket in the whole index and is literally the software this industry negotiates inside, managed repair administrators at 53 are its direct commercial counterparty, and forensic engineering at 51 supplies the causation opinion both sides retain.

The new qualifier sits above all of them. Catastrophe modelling firms decide how much capital the property insurance system holds, what reinsurance costs, and what rate filings can assume. Pass 1 describes public adjusting as entirely catastrophe-driven — six to twelve months of overwhelming demand after a hurricane, then a year of drought — and this is the layer that priced that hurricane before it happened.

Its central defect is the most consequential unmeasured judgment found in this sweep. The models produce exceedance probability curves; events then occur and losses settle; and forecast performance is never assembled into a standing record across events, perils, regions and model versions. The stated reason is that catastrophe is too rare to validate — true for the tail, and it has been allowed to excuse validating nothing, including severe convective storm, which produces dozens of events a year, has become one of the largest sources of insured loss, and has among the least examined models. Meanwhile the most uncertain component in the chain, the vulnerability functions relating hazard intensity to damage, is calibrated on aggregate contributed claims while line-item settlement detail describing exactly what broke and what it cost sits in the estimating and managed repair layers directly beneath.

Two further gaps are as valuable. Exposure data — the address files the models consume — is universally poor, with missing construction types filled by regional defaults that are frequently the largest single source of uncertainty in a client's answer and are invisible in the output, cleaned by analysts for every client and every renewal. And model version changes move client losses by tens of per cent with consequences for reinsurance, capital and rate filings, explained by a change document rather than an attribution saying how much came from hazard, how much from vulnerability, and how much from a conservative demand surge assumption.

Below the qualifiers, the pattern of unexploited evidence continues. Aerial imagery firms hold before-and-after captures of the same roofs across storm events — direct evidence for the causation dispute the whole industry argues about — and sell geometry measurements. Insurance appraisal and umpire practices hold what may be the single most informative dataset in property claims, the positions both sides took and where an independent umpire landed between them, and are staffed in ones and twos. And the public adjusting firms themselves hold offer-to-settlement deltas against documented scope, which is exactly the tacit knowledge Pass 1 says determines claim value, with neither the scale nor the function to model it.

## Niches — Pass 2
- [[niches/public-adjusters/property-repair-estimating-crossref/profile|🔍 Property Repair Estimating Data]]
- [[niches/public-adjusters/catastrophe-modelling-firms/profile|🔍 Catastrophe Modelling Firms]]
- [[niches/public-adjusters/managed-repair-program-crossref/profile|🔍 Managed Repair Programme Administrators]]
- [[niches/public-adjusters/forensic-engineering-crossref/profile|🔍 Forensic Engineering & Cause of Loss Investigation]]
- [[niches/public-adjusters/claims-data-fraud-analytics/profile|🔍 Property Claims Data & Fraud Analytics]]
- [[niches/public-adjusters/weather-verification-data/profile|🔍 Weather Verification & Peril Event Data]]
- [[niches/public-adjusters/aerial-imagery-measurement/profile|🔍 Aerial Imagery & Property Measurement]]
- [[niches/public-adjusters/contents-inventory-valuation/profile|🔍 Contents Inventory & Valuation Services]]
- [[niches/public-adjusters/insurance-appraisal-umpire-services/profile|🔍 Insurance Appraisal & Umpire Services]]
- [[niches/public-adjusters/state-insurance-regulators/profile|🔍 State Insurance Departments & Market Conduct]]
- [[niches/public-adjusters/bad-faith-litigation-support/profile|🔍 Claims Practice & Bad Faith Litigation Support]]
- [[niches/public-adjusters/public-adjuster-firm-rollups/profile|🔍 Public Adjusting Firm Rollups]]
- [[niches/public-adjusters/public-adjuster-association-research/profile|🔍 Public Adjuster Association Research]]
