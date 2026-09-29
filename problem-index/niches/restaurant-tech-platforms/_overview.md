# Niche Analysis — Restaurant Tech Platforms

**Parent Industry:** [[industries/restaurant-tech-platforms|Restaurant Tech Platforms]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential, then held every candidate against the standing filter — terminal only when *"every serious competitor here is fighting to solve X, and whoever solves X best takes the account"* can be written without generality.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | Full-Service Restaurant POS & Operations | 🔵 High Market Share | $4.2B | High | Product leads at Toast-tier platforms; operators of full-service restaurants |
| 2 | Digital Ordering & Channel Middleware | 🔵 High Market Share | $1.8B | High | Product leads at Olo, Otter, Deliverect, Chowly and their competitors |
| 3 | Bar & Nightlife Operations | 🟠 Low Digitized | $700M | Low-Medium | Bar owners and beverage directors; product leads at beverage-focused vendors |
| 4 | Commissary & Ghost Kitchen Operations | 🟠 Low Digitized | $450M | Low | Operators of shared kitchen facilities and multi-brand virtual kitchens |
| 5 | Kitchen Staff & Back-of-House Tools | 🟣 Underserved Audience | $600M | Low | Kitchen managers and chefs; the actual users are line and prep cooks |
| 6 | Non-Commercial Foodservice | 🟣 Underserved Audience | $900M | Low-Medium | Foodservice directors at school districts, hospitals and senior living |
| 7 | Invoice-to-Recipe Costing | ⚡ Highly Automatable | $550M | Medium | Product leads at back-office vendors; every operator who has ever costed a plate |
| 8 | Labour Scheduling & Availability | ⚡ Highly Automatable | $800M | Medium | Product leads at scheduling vendors; restaurant managers as the real users |

## Why These Niches

The two large blocks are the two halves of a restaurant's technology stack that actually decide outcomes. The point of sale is where the demand history lives, and demand forecasting is the contested capability — the platform holds item-level transactions at minute resolution across hundreds of thousands of locations and returns a sales report, while the operator guesses at the two decisions that determine survival. That niche **failed the filter as one**: a single independent's forecasting problem is a thin-data problem solved by pooling, and a forty-unit chain's problem is making forty units' numbers mean the same thing, which is a different contest against different competitors. It is decomposed below.

Channel middleware is the other large block, and its contested capability is unusually concrete: keeping one menu correct across five channels that each model a modifier differently, measured in how many times a human has to rebuild it.

Bars and shared kitchens are the two underdigitised operating models, each for a specific reason — beverage inventory is measured in fractions of a bottle and shared kitchens have no unit of account for shared capacity. Kitchen staff and non-commercial foodservice are the two underserved buyers: the back of house is where most of the labour is and almost none of the software, and school, hospital and senior living foodservice operates under nutrition and reimbursement constraints that restaurant products do not model at all.

The automation niches are the industry's two most reliable time sinks: reconciling distributor invoice lines against recipe ingredients, and building a weekly schedule that survives contact with who can actually work.

## Niches
- [[niches/restaurant-tech-platforms/fsr-pos-operations/profile|🔵 Full-Service Restaurant POS & Operations]]
  - [[niches/restaurant-tech-platforms/independent-fsr-forecasting/profile|🎯 Independent Restaurant — Forecasting on a Thin History]]
  - [[niches/restaurant-tech-platforms/multi-unit-chain-operations/profile|🎯 Multi-Unit Chains — Making Units Comparable]]
- [[niches/restaurant-tech-platforms/digital-ordering-middleware/profile|🔵 Digital Ordering & Channel Middleware]]
- [[niches/restaurant-tech-platforms/bar-nightlife-operations/profile|🟠 Bar & Nightlife Operations]]
- [[niches/restaurant-tech-platforms/ghost-kitchen-commissary/profile|🟠 Commissary & Ghost Kitchen Operations]]
- [[niches/restaurant-tech-platforms/kitchen-staff-tools/profile|🟣 Kitchen Staff & Back-of-House Tools]]
- [[niches/restaurant-tech-platforms/non-commercial-foodservice/profile|🟣 Non-Commercial Foodservice]]
- [[niches/restaurant-tech-platforms/invoice-to-recipe-costing/profile|⚡ Invoice-to-Recipe Costing]]
- [[niches/restaurant-tech-platforms/labor-scheduling-availability/profile|⚡ Labour Scheduling & Availability]]

## Filter Notes

**Niche 1 failed the filter as stated and was decomposed.** "Full-service restaurant POS and operations" contains two businesses that buy from different vendors for different reasons. An independent operator has one location, two years of history, and a forecasting problem that cannot be solved from its own data — the contested capability is whether the vendor can borrow strength from a pooled corpus of comparable locations. A forty-unit operator has abundant data and a comparability problem — whether item, labour and waste numbers mean the same thing across units well enough to identify which unit is actually underperforming, which is an enforcement and standardisation contest fought by Crunchtime, Restaurant365 and Qu rather than by Toast. Both sub-niches are terminal.

**Niches 2–8 are terminal as stated.** Each names something a buyer can test: manual menu rebuilds per channel per period, variance between poured and sold beverage, cost allocation defensibility in a shared kitchen, whether a prep list reaches the line, whether a menu satisfies nutrition rules and a budget at once, invoice line match rate, and the share of a proposed schedule that survives the week without a phone call.
