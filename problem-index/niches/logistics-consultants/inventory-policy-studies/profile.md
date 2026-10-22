# Inventory Policy & Safety Stock Studies

**Parent Industry:** [[industries/logistics-consultants|Logistics Consultants]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to release working capital without a service-level miss the client's sales team will blame on the study, and whoever's policies hold their projected fill rate in the first two quarters after go-live takes the account.

## Profile
**Market Size:** ~$700M US consulting fees for inventory diagnostics, safety stock and replenishment policy studies (estimate)
**Share of Parent Industry:** ~2% of US logistics and process consulting fees (estimate)
**Digital Adoption:** Medium — the mathematics is standard and software exists; the inputs come from ERP extracts that were never designed for it
**Target Buyer:** CFO, VP Planning
**Automation Potential:** High for computation, medium for adoption

## What Makes This a Distinct Niche
An inventory study is bought by finance and lived with by planning and sales. The CFO wants a working-capital release figure; planners need a policy table — service targets, safety stock, reorder points and order quantities by SKU and location — they can load into the ERP; and sales will hold the study responsible for any stockout that follows. Studies are fixed-fee diagnostics of ~$60K–$250K (estimate), often six to ten weeks, and the computation itself is codified. What separates firms is whether the policy survives contact with real demand, which depends on handling censored demand, lead-time variability and intermittent sellers that the textbook formulas get wrong.

## Current Tools & Gaps
Inventory optimisation software (ToolsGroup, Slimstock, Netstock, Lokad, and the planning modules of Kinaxis, o9 and Blue Yonder) computes probabilistic and multi-echelon policies well, but is sold as continuous planning with integration projects. Consultants use Excel, Python and these tools under licence. Gaps: no back-test of the proposed policy against the client's actual last year before sign-off; stockout periods read as low demand; and lead-time variability reconstructed by hand. The data problem is set out in [[problems/logistics-consultants/low-impact-2|Inventory Policy Studies on Uncleaned Demand History]].

## Problems
- [[niches/logistics-consultants/inventory-policy-studies/build|🔨 Build: Policies Back-Tested Against Last Year Before Anyone Signs]]
- [[niches/logistics-consultants/inventory-policy-studies/buy|🛒 Buy: Inventory Optimisation Software in Study Mode]]
- [[niches/logistics-consultants/inventory-policy-studies/fix|🔧 Fix: Stockouts Recorded as Low Demand]]
