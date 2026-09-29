# Niche Analysis — Credit Unions

**Parent Industry:** [[industries/credit-unions|Credit Unions]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Small Community CUs (<$500M Assets) | High Market Share | $800B assets | Low-Medium | CEO / VP of Lending |
| 2 | Auto Lending CUs | High Market Share | $500B+ outstanding | Medium | VP of Lending / Indirect Lending Manager |
| 3 | CDFI-Designated Credit Unions | Low Digitized | $30-50B assets | Low | CEO / Chief Lending Officer |
| 4 | Agricultural & Rural CUs | Low Digitized | $40-60B assets | Low | Branch manager / Ag lending specialist |
| 5 | Military & Federal Employee CUs | Underserved Audience | $200-300B assets | Medium-High | VP of Member Services / Digital Banking Manager |
| 6 | Underbanked Community CUs | Underserved Audience | $50-80B assets | Low | CEO / Community Development Officer |
| 7 | BSA/AML Compliance Operations | Highly Automatable | $2-3B (compliance cost) | Medium | BSA Officer / Compliance Manager |
| 8 | Member Onboarding & Cross-Sell Automation | Highly Automatable | $1-2B (embedded cost) | Low-Medium | VP of Marketing / Digital Banking Manager |

## Why These Niches

Credit unions fragment along asset size (small community CUs face fundamentally different technology and staffing constraints than large CUs), lending specialty (auto lending CUs have distinct workflow and risk management needs), community mission (CDFI and underbanked-serving CUs operate under additional regulatory frameworks and different economic models), member base (military/federal employee CUs serve a transient population with unique financial needs), and operational function (BSA/AML compliance and member onboarding are cross-cutting processes with the highest automation ROI). Excluded: large CUs over $5B in assets (effectively small banks with different tool sets), corporate credit unions (wholesale institutions serving other CUs), and CU service organizations/CUSOs (technology and service providers, not CUs themselves).

## Niches
- [[niches/credit-unions/small-community-cus/profile|🔵 Small Community CUs (<$500M Assets)]]
- [[niches/credit-unions/auto-lending-cus/profile|🔵 Auto Lending CUs]]
- [[niches/credit-unions/cdfi-credit-unions/profile|🟠 CDFI-Designated Credit Unions]]
- [[niches/credit-unions/agricultural-rural-cus/profile|🟠 Agricultural & Rural CUs]]
- [[niches/credit-unions/military-federal-cus/profile|🟣 Military & Federal Employee CUs]]
- [[niches/credit-unions/underbanked-community-cus/profile|🟣 Underbanked Community CUs]]
- [[niches/credit-unions/bsa-aml-compliance-ops/profile|⚡ BSA/AML Compliance Operations]]
- [[niches/credit-unions/member-onboarding-automation/profile|⚡ Member Onboarding & Cross-Sell Automation]]


---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. Pass 1 searched across the operator layer and found institutions from single-sponsor CUs to community charters; research functions of scale do not exist at that altitude. This pass sweeps seven positions in the value chain — aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry — looking for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`.

The credit scoring and identity resolution pockets that also serve this industry were logged under `collections-agencies` and are not duplicated here.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Deposit & Loan Pricing Benchmark Data | Data vendor | 100-500 | **54** | ✅ Indexed |
| 10 | Financial Crime Consortium Analytics | Supplier | 100-500 | **51** | ✅ Indexed |
| 11 | Credit Union Performance Analytics Providers | Data vendor | 30-120 | 49 | Below threshold |
| 12 | Asset-Liability & Interest Rate Risk Modelling Vendors | Data vendor | 30-150 | 48 | ⚠️ Kill switch |
| 13 | Model Validation Firms | Specialist advisory | 20-150 | 48 | ⚠️ Kill switch |
| 14 | Credit Union Merger & Valuation Advisory | Specialist advisory | 10-40 | 42 | Below threshold |
| 15 | Core Banking Platform Data Teams | Supplier | 100-600 | 41 | ⚠️ Kill switch |
| 16 | Member Marketing Analytics Vendors | Supplier | 20-100 | 41 | Below threshold |
| 17 | Corporate Credit Union Investment Research | Aggregator/rollup | 10-40 | 40 | Below threshold |
| 18 | CDFI Certification & Impact Reporting | Regulatory | 10-50 | 39 | Below threshold |
| 19 | Credit Union Research Institutes | Association research arm | 20-60 | 37 | Below threshold |
| 20 | Federal Credit Union Regulator Research | Regulatory | 30-120 | 36 | ⚠️ Kill switch |
| 21 | CUSO Lending Analytics | Aggregator/rollup | 3-12 | — | ✗ Fails gate |

## Why These Pockets

Both qualifiers exist because a credit union needs to know something about the world outside its own membership, and cannot see it alone.

Pricing benchmark providers hold contributed deposit and loan pricing and balance movement that no institution publishes and no regulator collects at that granularity, and the clock compresses violently whenever the policy rate moves. The unexploited asset is causal: institutions set rates using the vendor's elasticity models, balances then move, and both the decision and the outcome flow back through the same contribution stream — so the vendor holds everything needed to score its own predictions and does not. The second gap is the one this sweep keeps finding in benchmark businesses: a benchmark is a peer set plus a statistic, the peer set is the analytical act, and only the statistic is retained.

Financial crime consortium analytics is the more distinctive finding. Its entire premise is that pooling transaction data across hundreds of institutions reveals what no member can see — a mule network spread across twelve credit unions, elder fraud replicating across a region. Two gaps, both large. Investigators at member institutions dispose of millions of alerts a year, and each disposition is exactly the supervised label the detection models need, generated by trained people and left in institution-owned case systems — which is a substantial part of why false positive rates above ninety percent persist. And the typology knowledge that lets a senior investigator recognize a scheme from three details reaches the product only when someone happens to request a rule.

Eleven pockets logged without qualifying, and this industry shows the financial services pattern already established in collections: four carry supervisory kill switches. Risk modelling vendors and model validators both sell exactly the right written artefact against exam deadlines and sit inside model risk governance. Core banking platforms hold account and transaction data across thousands of institutions and tens of millions of members, contested in the contracts. The regulator holds the complete examination record and has no commercial buyer.

## Niches — Pass 2
- [[niches/credit-unions/deposit-loan-pricing-data/profile|🔍 Deposit & Loan Pricing Benchmark Data]]
- [[niches/credit-unions/financial-crime-consortium-analytics/profile|🔍 Financial Crime Consortium Analytics]]
- [[niches/credit-unions/cu-performance-benchmark-data/profile|🔍 Credit Union Performance Analytics Providers]]
- [[niches/credit-unions/alm-risk-modeling-vendors/profile|🔍 Asset-Liability & Interest Rate Risk Modelling Vendors]]
- [[niches/credit-unions/model-validation-firms/profile|🔍 Model Validation Firms]]
- [[niches/credit-unions/cu-merger-valuation-advisory/profile|🔍 Credit Union Merger & Valuation Advisory]]
- [[niches/credit-unions/core-banking-vendor-data/profile|🔍 Core Banking Platform Data Teams]]
- [[niches/credit-unions/cu-marketing-analytics-vendors/profile|🔍 Member Marketing Analytics Vendors]]
- [[niches/credit-unions/corporate-cu-investment-research/profile|🔍 Corporate Credit Union Investment Research]]
- [[niches/credit-unions/cdfi-impact-reporting/profile|🔍 CDFI Certification & Impact Reporting]]
- [[niches/credit-unions/cu-research-institutes/profile|🔍 Credit Union Research Institutes]]
- [[niches/credit-unions/ncua-economic-research/profile|🔍 Federal Credit Union Regulator Research]]
- [[niches/credit-unions/cuso-lending-analytics/profile|🔍 CUSO Lending Analytics]]
