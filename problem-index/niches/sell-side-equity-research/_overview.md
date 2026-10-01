# Niche Analysis — Sell-Side Equity Research

**Parent Industry:** [[industries/sell-side-equity-research|Sell-Side Equity Research]]

## Niche Selection

A sell-side research department is a forecasting institution that publishes every forecast it makes, timestamps it, and receives the answer four times a year in public filings — and almost never joins the two. Around that core sit a quarterly earnings cycle measured in minutes, a compliance review that every report must clear, a payment model split three ways between bundled, unbundled and partially rebundled regimes, a corporate access business run on spreadsheets, and thin small-cap teams carrying coverage the large brokers dropped after MiFID II. The eight niches below split the category by what competitors actually fight over.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Earnings Coverage | 🔵 High Market Share | ~$2.6B | Medium | Director of research; sector heads |
| 2 | Research Monetisation | 🔵 High Market Share | ~$2.0B | Low-Medium | Head of research sales; research COO |
| 3 | Research Compliance Review | 🟠 Low Digitized | ~$700M | Low | Head of research compliance |
| 4 | Corporate Access | 🟠 Low Digitized | ~$1.2B | Low | Head of corporate access |
| 5 | Small & Mid-Cap Coverage at Regional Brokers | 🟣 Underserved Audience | ~$900M | Low-Medium | Director of research, mid-tier and regional brokers |
| 6 | The Research Associate | 🟣 Underserved Audience | ~$600M | Medium | Director of research |
| 7 | Model Maintenance | ⚡ Highly Automatable | ~$800M | Medium | Director of research; research operations |
| 8 | Research Knowledge Reuse | ⚡ Highly Automatable | ~$700M | Medium | Director of research; research operations |

## Why These Niches

Earnings coverage takes the largest share because it is the most consumed product and the most time-critical, and because the contest is the read of the print rather than the note itself. Research monetisation is second because every research dollar passes through it and the payment regime is in flux on both sides of the Atlantic. The two low-digitized niches are where the work is still done by reading and by email: supervisory review of every report against Rule 2241 and Reg AC, and corporate access matched from memory. The two underserved audiences are the regional broker analyst covering twenty-five small caps alone and the associate doing the mechanical work of the department while supposed to be learning its judgment. The two automatable niches are the model fill — repetitive, deadline-bound and partly solved by extraction vendors — and the department's own archive of forecasts and views, which is its proprietary corpus and is used as a document store.

## Niches

- [[niches/sell-side-equity-research/earnings-coverage/profile|🔵 Earnings Coverage]]
- [[niches/sell-side-equity-research/research-monetisation/profile|🔵 Research Monetisation]]
  - [[niches/sell-side-equity-research/broker-vote-attribution/profile|🎯 Broker Vote Attribution]]
  - [[niches/sell-side-equity-research/research-subscription-pricing/profile|🎯 Research Subscription Pricing]]
- [[niches/sell-side-equity-research/research-compliance-review/profile|🟠 Research Compliance Review]]
- [[niches/sell-side-equity-research/corporate-access/profile|🟠 Corporate Access]]
- [[niches/sell-side-equity-research/small-mid-cap-coverage/profile|🟣 Small & Mid-Cap Coverage at Regional Brokers]]
- [[niches/sell-side-equity-research/the-research-associate/profile|🟣 The Research Associate]]
- [[niches/sell-side-equity-research/model-maintenance/profile|⚡ Model Maintenance]]
- [[niches/sell-side-equity-research/research-knowledge-reuse/profile|⚡ Research Knowledge Reuse]]

## Filter Notes

Seven of the eight level-1 niches are terminal. Research Monetisation is not: writing its contested sentence produces two sentences with different winners. Where research is still paid through execution commissions — most of the US — revenue is the broker vote, the voters are portfolio managers and analysts, and the contest is measuring which interactions earned the vote. Where it is unbundled — the EU since MiFID II, and the UK unless a firm uses the FCA's joint-payment route available since August 2024 — revenue is a priced subscription reviewed by a research budget committee, and the contest is packaging and pricing against measured consumption. Different client-side buyer, different data, different winners. It therefore decomposes into **Broker Vote Attribution** and **Research Subscription Pricing**.

Earnings Coverage and Model Maintenance were tested for overlap: the model fill is a mechanical, extraction-vendor contest won on speed and correctness, while earnings coverage is won on the read of the print, which is judgment. They are kept separate. The Research Associate and Model Maintenance share tasks but not buyer or contest — the associate niche is won on retention and development, not on fill speed.

Three candidates were considered and rejected as level-1 niches. **Credit research** inside broker-dealers is adjacent and in scope for the industry, but its contest — desk analysts supporting trading, under tighter information-barrier rules — splits across Earnings Coverage and Research Compliance Review rather than standing alone at this altitude; it is noted, not manufactured into a slot. **Independent research providers** sell the same product without a bank attached; they are a value-chain neighbour and are treated in Pass 2 below. **Research authoring and distribution platforms** are suppliers to the department, not a contest within it, and are also logged in Pass 2.

---

## Pass 2 — Insight-Layer Discovery

Second, orthogonal sweep. Pass 1 searched across the research department itself; this pass sweeps seven positions in the value chain — aggregator/rollup, payer & intermediary, data & benchmark vendors, association research arms, specialist advisory & valuation, regulatory bodies, and suppliers selling into the industry — looking for a dedicated insight function of 10+ people whose analytical output is the billable deliverable. Full method in `_direction.md`.

| # | Pocket | Position | Insight Function | Score | Verdict |
|---|---|---|---|---|---|
| 9 | Analyst Estimates & Consensus Data Providers | Data vendor | 300-1,500 | **52** | ✅ Indexed |
| 10 | Independent Research Providers | Specialist advisory | 20-300 per firm | 48 | Below threshold |
| 11 | Issuer-Sponsored Research Providers | Specialist advisory | 20-150 per firm | 47 | Below threshold |
| 12 | Fundamental Model Data Automation Vendors | Supplier | 100-600 | 47 | Below threshold |
| 13 | Company-Compiled Consensus & IR Analytics | Data vendor | 10-80 per firm | 45 | Below threshold |
| 14 | Analyst Rankings & Accuracy Scoring | Data vendor | 30-200 | 43 | Below threshold |
| 15 | Research Outsourcing & Knowledge Process Firms | Supplier | 1,000-6,000 | 36 | ⚠️ Kill switch |
| 16 | Research Authoring & Distribution Platforms | Supplier | 20-150 | 36 | ⚠️ Kill switch |
| 17 | Research Aggregation & Search Platforms | Aggregator | 100-1,000 | 32 | ⚠️ Kill switch |
| 18 | Outsourced Research Compliance & Supervisory Analyst Services | Specialist advisory | 10-60 per firm | 36 | ⚠️ Kill switch |
| 19 | Research Conflicts Regulators | Regulatory | 50-300 | 32 | ⚠️ Kill switch |
| 20 | Investment Profession Association Research | Association | 10-50 | 19 | Below threshold |
| 21 | Buy-Side Research Budget & Broker Review Desks | Payer & intermediary | 2-8 | — | Fails gate |
| 22 | Commission Sharing & Research Payment Account Administrators | Payer & intermediary | none | — | Fails gate |
| 23 | Broker-Dealer Consolidators — Research Integration | Aggregator/rollup | a few | — | Fails gate |

## Why These Pockets

One qualifier, and it sits exactly where the industry's central defect is most visible. Estimates and consensus providers hold the only complete, point-in-time, analyst-attributed record of what the sell side forecast and when, joined to what companies then reported — four decades of it at the longest-running provider. That is the sell side's tacit knowledge expressed as data: which analysts are right on which line items, who leads revisions after guidance and who follows, which management teams guide conservatively. Some of it is used — accuracy-weighted consensus exists at the EPS level — but the line-item, guidance-regime and lead-lag structure of the record is barely modelled, and the product most buyers see is still an average. The weak point is the buyer market: a handful of large vendors, so one reference does not unlock many more.

The near misses are instructive. Independent and issuer-sponsored research providers are the purest case of insight-as-invoice in the segment and score high on Q1 and Q2, but they work from public filings and their only proprietary corpus — their own forecast archive — is ungraded, which is the same defect the brokers have. Model data automation vendors are labour-linear and clock-bound but their corpus is reproducible from public documents. Rankings providers own the best record of what the buy side says it values but run on an annual clock.

The kill switches cluster where the data belongs to someone else: outsourcing firms working inside client models, authoring platforms and aggregators holding broker research under entitlement, compliance services handling unpublished research behind information barriers, and regulators behind government procurement. The payer side fails the gate outright — research budget desks at asset managers are a few people each, and commission administrators are an operations function.

## Niches — Pass 2
- [[niches/sell-side-equity-research/estimates-consensus-data/profile|🔍 Analyst Estimates & Consensus Data Providers]]
- [[niches/sell-side-equity-research/independent-research-providers/profile|🔍 Independent Research Providers]]
- [[niches/sell-side-equity-research/issuer-sponsored-research/profile|🔍 Issuer-Sponsored Research Providers]]
- [[niches/sell-side-equity-research/fundamental-model-data-automation/profile|🔍 Fundamental Model Data Automation Vendors]]
- [[niches/sell-side-equity-research/company-compiled-consensus/profile|🔍 Company-Compiled Consensus & IR Analytics]]
- [[niches/sell-side-equity-research/analyst-rankings-accuracy-scoring/profile|🔍 Analyst Rankings & Accuracy Scoring]]
- [[niches/sell-side-equity-research/research-outsourcing-kpo/profile|🔍 Research Outsourcing & Knowledge Process Firms]]
- [[niches/sell-side-equity-research/research-authoring-distribution-platforms/profile|🔍 Research Authoring & Distribution Platforms]]
- [[niches/sell-side-equity-research/research-aggregation-search-platforms/profile|🔍 Research Aggregation & Search Platforms]]
- [[niches/sell-side-equity-research/research-compliance-supervisory-services/profile|🔍 Outsourced Research Compliance & Supervisory Analyst Services]]
- [[niches/sell-side-equity-research/research-conflicts-regulators/profile|🔍 Research Conflicts Regulators]]
- [[niches/sell-side-equity-research/investment-profession-association-research/profile|🔍 Investment Profession Association Research]]
- [[niches/sell-side-equity-research/buy-side-research-budget-desks/profile|🔍 Buy-Side Research Budget & Broker Review Desks]]
- [[niches/sell-side-equity-research/commission-csa-rpa-administrators/profile|🔍 Commission Sharing & Research Payment Account Administrators]]
- [[niches/sell-side-equity-research/broker-consolidator-research-integration/profile|🔍 Broker-Dealer Consolidators — Research Integration]]
